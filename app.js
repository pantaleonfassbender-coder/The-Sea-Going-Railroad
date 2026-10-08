/* The Sea-Going Railroad — a documentary apparatus. Vanilla JS, hash routes. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };
const SIDES = { company: "The company and its engineers", labour: "The workers", weather: "Storms and warnings", state: "Courts and government", keys: "Key West and the Keys" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });
const NUM = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight"];

async function boot() {
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  const pl = plateOf("vaughan1908");
  const planned = D.mods.planned || [];
  view.innerHTML = `
  <div class="hero">
    <div>
      <span class="tag">1904–1938 · Henry Flagler · the Florida East Coast Railway · the Keys</span>
      <h1>Who carried the risk?</h1>
      <p class="lede">Between 1905 and 1912 the Florida East Coast Railway carried its line 128 miles from the mainland across the Florida Keys to Key West, over seventeen miles of bridges and concrete arches built in open water. Men recruited by the thousand in New York, Spaniards, and Black workers from Florida and the Bahamas lived on quarterboats and in camps on the keys. Hurricanes struck the work in 1906, 1909 and 1910. The line never paid its way; on 2 September 1935 a hurricane destroyed forty miles of it, and with it the camps of hundreds of war veterans on relief work.</p>
      <p class="readable">This apparatus follows the railroad through the documents that record it: the engineering press, the reports of the Weather Bureau, the inquiries into the recruiting of labour, the hearings of 1936 and the decisions of the Interstate Commerce Commission. Every text is public domain and carried in whole passages, each linked to its printing.</p>
      <p class="quote">"The quarter boats of the East Coast Extension were carried out to sea and many lives, probably more than 100, were lost."
      <br><span class="fine">Monthly Weather Review, October 1906, report from Key West</span></p>
    </div>
    <figure><img src="assets/plates/${pl.id}.jpg" alt="${esc(pl.titel)}">
      <figcaption>${esc(pl.caption)} <a href="#/plates">All plates →</a></figcaption></figure>
  </div>

  ${D.mods.shipped.length ? `<h2>What the apparatus carries</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
  ${planned.length ? `<h2>Planned modules</h2><div class="grid g2">${planned.map(plannedCard).join("")}</div>` : ""}

  <h2>The questions it asks</h2>
  <div class="grid g2">
    <div class="panel"><h3>How many died?</h3>
      <p>For the storm of October 1906 a single article of the Monthly Weather Review gives three figures: more than a hundred, about 135, and 124. For 2 September 1935 the Red Cross counted 409 dead and missing; the Florida relief administration recovered 485 bodies, 257 of them veterans. The apparatus sets the figures side by side instead of choosing one.</p></div>
    <div class="panel"><h3>Who came to work, and on what terms?</h3>
      <p>Labour agents in New York were paid by the head; the fare south was deducted from the first month's wages, and a quarter of the men recruited never reached the keys. In 1908 agents and engineers of the line were tried for peonage in New York and acquitted. The company blamed the stories on deserters sent to the chain gang as vagrants.</p></div>
    <div class="panel"><h3>Arches or fill?</h3>
      <p>Where the line crossed open water it was carried on concrete arches and steel spans; elsewhere on embankments of fill. After the storms of 1909 and 1910 the company added miles of arches. In 1935 the fill and the track were swept away; the bridges stood, and from 1938 the Overseas Highway ran on their piers.</p></div>
    <div class="panel"><h3>Who paid for the end?</h3>
      <p>From 1930 to 1935 the extension lost between $220,000 and $376,000 a year, and from 1931 the railway was in receivership. In 1936 the Interstate Commerce Commission allowed it to abandon the line; the State bought the right of way and the bridges for $640,000 out of a federal loan.</p></div>
    <div class="panel"><h3>"An act of God"?</h3>
      <p>The report to the President of 8 September 1935 found that no one was to blame for the deaths of the veterans in the camps on the keys. The hearings of 1936 asked about the warnings, the rescue train that left Miami at twenty-five past four in the afternoon, and who had decided that the men should stay. The companion game takes its title from that report.</p></div>
    <div class="panel"><h3>Can it be played?</h3>
      <p>The companion game <a href="https://an-act-of-god.netlify.app/" target="_blank" rel="noopener"><em>An Act of God</em></a> (prototype 0): as the line's engineers, season by season from 1905 to 1912, you decide how it is built, how the men are recruited, where they live and what you do when the Weather Bureau warns; 1935 shows what your choices left standing. Every card links back to its passage here.</p></div>
  </div>`;
}
function plannedCard(m) {
  return `<div class="card planned"><div>${side(m.side)} <span class="fine">in preparation</span></div><h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  const total = D.mods.shipped.length + (D.mods.planned || []).length;
  view.innerHTML = `
    <span class="tag">Texts</span><h1>The corpus</h1>
    <p class="lede">${(D.mods.planned || []).length ? (D.mods.shipped.length ? `Stage 1 of the collection is in progress: ${NUM[D.mods.shipped.length]} of ${NUM[total]} modules are carried, the others are planned.` : `Stage 1 of the collection has begun: ${NUM[total]} modules are planned, none is carried yet.`) : `Stage 1 of the collection is complete: all ${NUM[total]} modules are carried.`} What is not carried, and why, is listed below.</p>
    ${D.mods.shipped.length ? `<h2>Carried</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>Planned</h2><div class="grid g2">${D.mods.planned.map(plannedCard).join("")}</div>` : ""}
    <h2 id="missing">Not carried</h2><div class="grid g2">${(D.mods.missing || []).map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">not carried</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Loading…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← All texts</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · cited as ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">Source and editorial note</span>
      <p><b>Source.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Cite as ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg">${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(u.titel)}</h4>` : ""}<div class="text">${esc(u.en)}</div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">Compare</span><h1>One event, several records</h1>
      <p class="lede">${esc(CMP.lede)}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(p.titel)}</h3><p class="fine">${esc(p.frage)}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">← All comparisons</a></p><p class="fine">Loading…</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(sec.titel)}</b><br><span class="fine">${esc(t.titel)}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(u.titel)}` : ""}${u.pg ? `<br>${esc(u.pg)}` : ""}</div>
        <div class="text">${esc(u.en)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">← All comparisons</a></p>
    <span class="tag">Compare</span><h1>${esc(pair.titel)}</h1>
    <p class="lede">${esc(pair.frage)}</p>
    <div class="panel readable"><p>${esc(pair.note)}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Timeline</span><h1>1904–1938</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}
        ${s.src ? `<p class="fine">Source: ${esc(s.src)}</p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Plates</span><h1>Arches, trains, and a weather map</h1>
    <p class="lede">Photographs taken while the line was built and opened, illustrations from the engineering and reference books of the time, and the Weather Bureau's charts of 1935. No photograph of the dead of 1906 or 1935 is shown here.</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Sources, method, limits</span><h1>How this apparatus is made</h1>
    <div class="readable">
    <p><b>Public domain only.</b> Every text is carried from a printing that is out of copyright in the United States: the engineering press and company publications before 1931, and the work of the federal government at any date (the Monthly Weather Review, the reports of the Immigration Commission, the hearings of Congress, the decisions of the Interstate Commerce Commission, the publications of the National Park Service). Later accounts in copyright, among them Ernest Hemingway's article of 1935 on the veterans and the modern histories of the railroad, are named but not quoted.</p>
    <p><b>Read against the page.</b> Every passage is checked against the page image or the text layer of a scan, and its page is given. Where the scan could not be reached, the passage is not carried.</p>
    <p><b>Figures as given.</b> The sources disagree about how many men worked on the line, what it cost and how many died. The apparatus gives each figure with its source and does not average or choose.</p>
    <p><b>Voices and distances.</b> Most of what survives was written by the company, its engineers and the engineering press, which wrote for engineers and investors; the workers speak only through investigators, prosecutors and newspapers. Each module says whose voice it carries.</p>
    <p><b>The dead.</b> Photographs of the dead of 1935 survive in federal files and are in the public domain. The apparatus does not show them.</p>
    </div>
    <h2>Sources carried</h2>
    ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>` : `<p class="readable">No module is carried yet. The sources of the planned modules are listed in the repository's source survey; each module will name its printings here.</p>`}
    <h2>Plates</h2><p class="fine readable">${esc(D.plates.credit)}</p>`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Could not load the apparatus: ${esc(e.message)}</p>`; });
