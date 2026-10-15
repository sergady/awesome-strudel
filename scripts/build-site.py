#!/usr/bin/env python3
"""Build docs/dictionary.js for the single-page dictionary site."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INDEX = ROOT / "function-dictionary.md"
LETTERS = ROOT / "Dictionary"

INLINE = re.compile(r"`([^`]+)`|\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)\s]+)\)")


def escape(text):
    return html.escape(text, quote=True)


def rewrite_href(href):
    basic = re.match(r"^basic-functions-dictionary\.md(#.*)?$", href)
    if basic:
        anchor = basic.group(1) or ""
        return "https://github.com/sergady/awesome-strudel/blob/main/basic-functions-dictionary.md" + anchor
    return href


def inline(text):
    out = []
    pos = 0
    for match in INLINE.finditer(text):
        out.append(escape(text[pos : match.start()]))
        if match.group(1) is not None:
            out.append(f"<code>{escape(match.group(1))}</code>")
        elif match.group(2) is not None:
            out.append(f"<strong>{escape(match.group(2))}</strong>")
        else:
            href = rewrite_href(match.group(4))
            out.append(f'<a href="{escape(href)}">{escape(match.group(3))}</a>')
        pos = match.end()
    out.append(escape(text[pos:]))
    return "".join(out)


def render_md(text):
    lines = text.strip().splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```") or line.startswith("~~~"):
            fence = line[:3]
            buf = []
            i += 1
            while i < len(lines) and not lines[i].startswith(fence):
                buf.append(lines[i])
                i += 1
            i += 1
            blocks.append(f"<pre><code>{escape(chr(10).join(buf))}</code></pre>")
            continue
        if not line.strip():
            i += 1
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("```") and not lines[i].startswith("~~~"):
            para.append(lines[i])
            i += 1
        if all(item.lstrip().startswith("- ") for item in para):
            items = "".join(f"<li>{inline(item.lstrip()[2:])}</li>" for item in para)
            blocks.append(f"<ul>{items}</ul>")
        else:
            blocks.append("<p>" + inline(" ".join(para)) + "</p>")
    return "\n".join(blocks)


def parse_index():
    text = INDEX.read_text()
    body = text.split("## Index", 1)[1]
    groups = []
    current = None
    for line in body.splitlines():
        if re.fullmatch(r"### [A-Z]", line):
            current = {"letter": line[-1], "items": []}
            groups.append(current)
        elif current and line.startswith("- `"):
            match = re.match(r"- `([^`]+)`(?: — alias of `([^`]+)`)?", line)
            current["items"].append({"name": match.group(1), "alias_of": match.group(2)})
    return groups


def parse_entries(letter):
    text = (LETTERS / f"{letter}.md").read_text()
    _, _, rest = text.partition("\n## Entries\n")
    rest = rest.strip()
    if rest.startswith("### "):
        rest = rest[4:]
    chunks = re.split(r"\n### ", rest)
    entries = []
    for chunk in chunks:
        if not chunk.strip():
            continue
        name, _, body = chunk.partition("\n")
        entries.append({"name": name.strip(), "html": render_md(body)})
    return entries


def main():
    groups = parse_index()
    payload = {"letters": [], "names": [], "entries": {}}
    for group in groups:
        letter = group["letter"]
        payload["letters"].append(letter)
        for item in group["items"]:
            payload["names"].append({"name": item["name"], "letter": letter, "aliasOf": item["alias_of"]})
        entries = parse_entries(letter)
        payload["entries"][letter] = entries
        print(f"{letter} {len(entries)} entries")
    text = "window.DICTIONARY = " + json.dumps(payload, ensure_ascii=True, separators=(",", ":")) + ";\n"
    (DOCS / "dictionary.js").write_text(text)
    (DOCS / ".nojekyll").write_text("")
    for path in DOCS.glob("*.html"):
        if path.name != "index.html":
            path.unlink()
    search = DOCS / "search.js"
    if search.exists():
        search.unlink()
    print(f"names {len(payload['names'])} bytes {len(text)}")


if __name__ == "__main__":
    main()
