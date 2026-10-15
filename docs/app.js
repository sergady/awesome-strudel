const data = window.DICTIONARY;
const byName = new Map(data.names.map((item) => [item.name, item]));
const main = document.querySelector("#main");
const countEl = document.querySelector("#count");
const input = document.querySelector("#q");
const lettersEl = document.querySelector("#letters");

let shown = { view: "", letter: "", needle: "" };

const escapeHtml = (text) =>
  text.replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));

const targetOf = (item) => item.aliasOf || item.name;

const hashFor = (name) => {
  const item = byName.get(name);
  const target = item ? targetOf(item) : name;
  const owner = byName.get(target) || item;
  return `#${owner.letter}/${encodeURIComponent(target)}`;
};

const parseHash = () => {
  const raw = decodeURIComponent(location.hash.replace(/^#/, ""));
  if (raw === "all") return { view: "all", letter: "", name: "" };
  if (raw === "home" || raw.startsWith("home/")) return { view: "home", letter: "", name: raw.slice(5) };
  if (!raw) return { view: "home", letter: "", name: "" };
  const slash = raw.indexOf("/");
  if (slash === -1 && data.letters.includes(raw)) return { view: "letter", letter: raw, name: "" };
  if (slash > 0) {
    const letter = raw.slice(0, slash);
    const name = raw.slice(slash + 1);
    if (data.letters.includes(letter)) return { view: "letter", letter, name };
  }
  const item = byName.get(raw);
  if (!item) return { view: "home", letter: "", name: "" };
  const target = targetOf(item);
  return { view: "letter", letter: byName.get(target).letter, name: target };
};

const renderNav = (route) => {
  const current = route.letter;
  const links = [
    `<li><a href="#"${route.view === "home" ? ' aria-current="page"' : ""}>Home</a></li>`,
    `<li><a href="#all"${route.view === "all" ? ' aria-current="page"' : ""}>All</a></li>`,
  ];
  for (const letter of data.letters) {
    const currentAttr = letter === current ? ' aria-current="page"' : "";
    links.push(`<li><a href="#${letter}"${currentAttr}>${letter}</a></li>`);
  }
  lettersEl.innerHTML = links.join("");
};

const renderHome = () => {
  document.title = "Strudel function dictionary";
  main.innerHTML = `<section class="intro"><p>This is unofficial documentation for the Strudel project. Visit the <a href="https://strudel.cc/">official Strudel website</a> for the project and its documentation.</p><p><a href="#all">Browse all functions →</a></p></section><article class="entry introduction">${data.basicHtml}</article>`;
  countEl.textContent = "";
};

const renderAll = (needle) => {
  document.title = "Strudel function dictionary";
  input.placeholder = "Filter functions";
  const sections = [];
  let total = 0;
  for (const letter of data.letters) {
    const items = data.names.filter((item) => item.letter === letter && (!needle || `${item.name} ${item.aliasOf || ""}`.toLowerCase().includes(needle)));
    if (!items.length) continue;
    total += items.length;
    const rows = items
      .map((item) => {
        const alias = item.aliasOf ? ` <span class="alias">alias of ${escapeHtml(item.aliasOf)}</span>` : "";
        return `<li><a href="${hashFor(item.name)}"><code>${escapeHtml(item.name)}</code></a>${alias}</li>`;
      })
      .join("");
    sections.push(
      `<section class="group"><h2><a href="#${letter}">${letter}</a></h2><ul class="names">${rows}</ul></section>`,
    );
  }
  main.innerHTML = sections.join("") || `<p id="empty">No functions match.</p>`;
  countEl.textContent = total === 1 ? "1 function" : `${total} functions`;
};

const renderLetter = (letter, name, needle, scroll) => {
  document.title = `${letter} — Strudel functions`;
  input.placeholder = `Filter ${letter}`;
  const entries = data.entries[letter].filter((entry) => !needle || entry.name.toLowerCase().includes(needle));
  if (!entries.length) {
    main.innerHTML = `<p id="empty">No functions match.</p>`;
  } else {
    const jumps = entries
      .map((entry) => `<li><a href="#${letter}/${encodeURIComponent(entry.name)}"><code>${escapeHtml(entry.name)}</code></a></li>`)
      .join("");
    const articles = entries
      .map(
        (entry) =>
          `<article class="entry" id="${escapeHtml(entry.name)}"><h2><a href="#${letter}/${encodeURIComponent(entry.name)}">${escapeHtml(entry.name)}</a></h2>${entry.html}</article>`,
      )
      .join("");
    main.innerHTML = `<ul class="jumps">${jumps}</ul>${articles}`;
  }
  countEl.textContent = entries.length === 1 ? "1 function" : `${entries.length} functions`;
  if (scroll && name) document.getElementById(name)?.scrollIntoView();
};

const render = (scroll) => {
  const route = parseHash();
  const needle = input.value.trim().toLowerCase();
  renderNav(route);
  document.querySelector(".tools").hidden = route.view === "home";
  const sameView = shown.view === route.view && shown.letter === route.letter && shown.needle === needle;
  shown = { view: route.view, letter: route.letter, needle };
  if (sameView) {
    if (scroll && route.name) document.getElementById(route.name)?.scrollIntoView();
    return;
  }
  if (route.view === "home") {
    renderHome();
    if (scroll && route.name) document.getElementById(route.name)?.scrollIntoView();
  } else if (route.view === "all") renderAll(needle);
  else renderLetter(route.letter, route.name, needle, scroll);
};

input.addEventListener("input", () => render(false));
window.addEventListener("hashchange", () => {
  const route = parseHash();
  if (route.view !== shown.view || route.letter !== shown.letter) input.value = "";
  render(true);
});
render(true);
