/**
 * Builds Dictionary/C.md through Dictionary/Z.md from the Strudel source comments.
 * Descriptions and examples are copied from JSDoc. A and B are left as written.
 */
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, unlinkSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const awesome = join(here, '..');
const strudel = join(awesome, '../strudel');
const node = process.execPath;
const extractor = join(strudel, 'docs/learning/_extract-functions.mjs');
const indexPath = join(strudel, 'docs/learning/function-index.json');

execFileSync(node, [extractor], { cwd: strudel, stdio: 'inherit' });
const functions = JSON.parse(readFileSync(indexPath, 'utf8'));
unlinkSync(indexPath);

const byName = new Map(functions.map((fn) => [fn.name, fn]));
const catalog = readFileSync(join(awesome, 'function-dictionary.md'), 'utf8');

function lettersFrom(startLetter) {
  const start = catalog.indexOf(`### ${startLetter}\n`);
  const groups = new Map();
  let letter = null;
  for (const line of catalog.slice(start).split('\n')) {
    if (/^### [A-Z]$/.test(line)) {
      letter = line.slice(4);
      groups.set(letter, []);
    } else if (letter && line.startsWith('- `')) {
      groups.get(letter).push(line);
    }
  }
  return groups;
}

function paramName(param) {
  const match = param.match(/^\{[^}]*\}\s+([a-z][\w$]*)\b/);
  return match ? match[1] : '';
}

function hasBody(fn) {
  return Boolean(fn && ((fn.description && fn.description.trim()) || (fn.examples && fn.examples.length)));
}

function borrow(fn) {
  if (hasBody(fn) && fn.description && !fn.description.startsWith('Alias of ') && !(fn.summary || '').startsWith('Alias of ')) {
    return fn;
  }
  const targets = new Set(fn.aliases || []);
  const aliasSummary = (fn.summary || '').match(/^Alias of ([A-Za-z_][\w$]*)/);
  if (aliasSummary) targets.add(aliasSummary[1]);
  for (const other of byName.values()) {
    if ((other.aliases || []).includes(fn.name)) targets.add(other.name);
  }
  for (const target of targets) {
    const other = byName.get(target);
    if (other && other.description && !other.description.startsWith('Alias of ')) {
      return {
        ...fn,
        description: other.description,
        examples: fn.examples?.length ? fn.examples : other.examples,
        params: fn.params?.length ? fn.params : other.params,
        borrowed: other.name,
      };
    }
  }
  return fn;
}

const fileCache = new Map();
function readSource(rel) {
  if (!fileCache.has(rel)) fileCache.set(rel, readFileSync(join(strudel, rel), 'utf8'));
  return fileCache.get(rel);
}

function nearbyProse(fn) {
  const name = fn.name;
  for (const rel of fn.files || []) {
    let source;
    try {
      source = readSource(rel);
    } catch {
      continue;
    }
    const marks = [`'${name}'`, `"${name}"`];
    let at = -1;
    for (const mark of marks) {
      const found = source.indexOf(mark);
      if (found >= 0 && (at < 0 || found < at)) at = found;
    }
    if (at < 0) continue;
    const before = source.slice(Math.max(0, at - 2000), at);
    const blocks = [...before.matchAll(/\/\*\*?[\s\S]*?\*\//g)];
    if (!blocks.length) continue;
    const last = blocks[blocks.length - 1];
    const gap = before.slice(last.index + last[0].length);
    if (gap.trim().length > 40) continue;
    if (/Copyright \(C\)/.test(last[0])) continue;
    const named = last[0].match(/@name\s+(\S+)/);
    if (named && named[1] !== name) continue;
    const prose = last[0]
      .replace(/^\/\*+/, '')
      .replace(/\*+\/$/, '')
      .split('\n')
      .map((line) => line.replace(/^\s*\*\s?/, '').trimEnd())
      .join('\n')
      .replace(/@\w+[^\n]*/g, '')
      .trim();
    if (prose.length > 40) return prose;
  }
  return '';
}

function isMethod(fn) {
  if ((fn.kinds || []).some((kind) => kind === 'control' || kind === 'pattern-method' || kind === 'multi-control')) return true;
  const blob = (fn.examples || []).join('\n');
  if (new RegExp(`\\.${fn.name}\\s*\\(`).test(blob)) return true;
  for (const rel of fn.files || []) {
    let source = '';
    try {
      source = readSource(rel);
    } catch {
      continue;
    }
    if (source.includes(`_distortWithAlg('${fn.name}')`) || source.includes(`prototype.${fn.name}`)) return true;
  }
  return false;
}

function callLine(fn) {
  const names = [...new Set((fn.params || []).map(paramName).filter(Boolean))];
  const method = isMethod(fn);
  const takesArgs = names.length || (fn.examples || []).some((example) => new RegExp(`\\.?${fn.name}\\s*\\(\\s*[^)]`).test(example));
  let invoke;
  if (names.length) invoke = method ? `.${fn.name}(${names.join(', ')})` : `${fn.name}(${names.join(', ')})`;
  else if (takesArgs) invoke = method ? `.${fn.name}(…)` : `${fn.name}(…)`;
  else invoke = method ? `.${fn.name}()` : fn.name;
  const aliases = (fn.aliases || []).filter((alias) => alias !== fn.name && alias !== fn.borrowed);
  const aliasText = aliases.length ? ` Alias${aliases.length > 1 ? 'es' : ''}: ${aliases.map((alias) => `\`${alias}\``).join(', ')}.` : '';
  const borrowed = fn.borrowed ? ` Same as \`${fn.borrowed}\`.` : '';
  return `**Call:** \`${invoke}\`.${aliasText}${borrowed}`;
}

function fence(example) {
  const text = example.replace(/\s+$/, '');
  const mark = text.includes('```') ? '~~~' : '```';
  return `${mark}js\n${text}\n${mark}`;
}

function entry(name) {
  const raw = byName.get(name);
  if (!raw) {
    return `### ${name}\n\n**Call:** \`${name}\`.\n\nNo description or example in this checkout.\n`;
  }
  const fn = borrow(raw);
  if (!fn.description) {
    const prose = nearbyProse(fn);
    if (prose) fn.description = prose;
  }
  const lines = [`### ${name}`, '', callLine(fn), ''];
  if (fn.description) lines.push(fn.description.trim(), '');
  else lines.push('No description or example in this checkout.', '');
  for (const example of fn.examples || []) {
    lines.push(fence(example), '');
  }
  const source = (fn.files && fn.files[0]) || '';
  if (source) lines.push(`Source: \`${source}\`.`, '');
  return lines.join('\n');
}

const stats = { entries: 0, described: 0, examples: 0, empty: 0, borrowed: 0 };
const linkLines = ['- [A](Dictionary/A.md)', '- [B](Dictionary/B.md)'];

for (const [letter, lines] of lettersFrom('C')) {
  const primaries = lines
    .filter((line) => !line.includes('alias of'))
    .map((line) => line.match(/`([^`]+)`/)[1]);
  const body = [`### ${letter}`, '', ...lines, '', '## Entries', ''];
  for (const name of primaries) {
    const raw = byName.get(name);
    const fn = raw ? borrow(raw) : null;
    if (fn && !fn.description) {
      const prose = nearbyProse(fn);
      if (prose) fn.description = prose;
    }
    stats.entries += 1;
    if (fn?.borrowed) stats.borrowed += 1;
    if (fn?.description) stats.described += 1;
    else stats.empty += 1;
    if (fn?.examples?.length) stats.examples += 1;
    body.push(entry(name).trimEnd(), '');
  }
  writeFileSync(join(awesome, 'Dictionary', `${letter}.md`), body.join('\n').trimEnd() + '\n');
  linkLines.push(`- [${letter}](Dictionary/${letter}.md)`);
  console.log(`${letter} ${primaries.length}`);
}

const progress = `**Progress:** letter files are complete through **Z**. [A](Dictionary/A.md) and [B](Dictionary/B.md) are hand-written listening notes. C–Z copy the description and example from the source when the code has them.

${linkLines.join('\n')}`;

const updated = catalog.replace(
  /\*\*Progress:\*\*[\s\S]*?\n\n## Index/,
  `${progress}\n\n## Index`,
);
writeFileSync(join(awesome, 'function-dictionary.md'), updated);
console.log(stats);
