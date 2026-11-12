#!/usr/bin/env node
// Genera quotes/<slug>/entregables/timeline.html desde quotes/<slug>/project.json.
// La fuente de verdad son las fases en ClickUp; project.json es la exportación que hace el skill.
// Uso: node portal/build-timeline.mjs <slug> [--today YYYY-MM-DD]
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "..");
const slug = process.argv[2];
if (!slug) { console.error("Uso: node portal/build-timeline.mjs <slug> [--today YYYY-MM-DD]"); process.exit(1); }
const todayArg = process.argv.indexOf("--today") > -1 ? process.argv[process.argv.indexOf("--today") + 1] : null;

const p = JSON.parse(fs.readFileSync(path.join(root, "quotes", slug, "project.json"), "utf8"));
const tpl = fs.readFileSync(path.join(here, "timeline.template.html"), "utf8");

// ---- fechas en días hábiles. Índice 1 = lunes de la semana de arranque.
const MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];
const DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
const d = (s) => new Date(s + "T12:00:00");
const fmt = (dt) => `${dt.getDate()} ${MESES[dt.getMonth()]}`;
const monday = (dt) => { const m = new Date(dt); m.setDate(m.getDate() - ((m.getDay() + 6) % 7)); return m; };
const start = monday(d(p.start));
const launch = d(p.launch);
const idx = (dt) => { // día hábil 1..N; fines de semana caen al viernes anterior
  let n = 0; const cur = new Date(start);
  while (cur < dt) { cur.setDate(cur.getDate() + 1); if (cur.getDay() !== 0 && cur.getDay() !== 6) n++; }
  if (dt.getDay() === 0 || dt.getDay() === 6) return n;
  return n + 1;
};
const NDAYS = idx(launch);
const NWEEKS = Math.ceil(NDAYS / 5);
const WEEKS = Array.from({ length: NWEEKS }, (_, i) => { const w = new Date(start); w.setDate(w.getDate() + i * 7); return fmt(w); });
const todayDate = todayArg ? d(todayArg) : new Date();
const TODAY = Math.min(Math.max(idx(todayDate), 1), NDAYS);

// ---- filas: fases (barras) + lanzamiento + revisión semanal
const rowsByLabel = new Map();
const rows = [];
const addRow = (label, sub) => { if (!rowsByLabel.has(label)) { const r = { label, sub, bars: [], ms: [] }; rowsByLabel.set(label, r); rows.push(r); } return rowsByLabel.get(label); };
if (p.weeklyReview) {
  const r = addRow(p.weeklyReview.label, p.weeklyReview.sub);
  for (let w = 0; w < NWEEKS; w++) { const day = w * 5 + p.weeklyReview.weekday; if (day <= NDAYS) r.ms.push({ day, text: "Revisión", dot: true }); }
}
for (const ph of p.phases) {
  const r = addRow(ph.label, ph.sub);
  r.bars.push({ from: idx(d(ph.start)), to: idx(d(ph.end)), who: ph.who, text: ph.label });
}
addRow("Lanzamiento", `${p.softLaunch ? "Soft " + fmt(d(p.softLaunch)) + " · " : ""}Final ${fmt(launch)}`);
for (const m of p.milestones) {
  const r = rowsByLabel.get(m.row) || rowsByLabel.get("Lanzamiento");
  r.ms.push({ day: idx(d(m.date)), text: m.big ? fmt(d(m.date)) : m.what, big: !!m.big });
}

const DATA = `  const WEEKS = ${JSON.stringify(WEEKS)};\n  const TODAY = ${TODAY}; // ${fmt(todayDate)}\n  const ROWS = ${JSON.stringify(rows, null, 2).replace(/\n/g, "\n  ")};`;
const KEYS = p.milestones.map(m => {
  const when = m.big ? `<mark>${fmt(d(m.date))}</mark>` : fmt(d(m.date));
  return `      <div class="key${m.big ? " launch-key" : ""}"><div class="when">${when}</div><div class="what">${m.what}</div><div class="who">${m.who}</div></div>`;
}).join("\n");
const LAUNCH = `${DIAS[launch.getDay()][0].toUpperCase()}${DIAS[launch.getDay()].slice(1)} ${fmt(launch)}`;

let out = tpl
  .replaceAll("{{CLIENT}}", p.client)
  .replaceAll("{{CLIENT_LONG}}", p.clientLong || p.client)
  .replaceAll("{{PROJECT}}", p.project)
  .replaceAll("{{NDAYS}}", String(NDAYS))
  .replaceAll("{{LAUNCH}}", LAUNCH)
  .replace("{{KEYS}}", KEYS)
  .replace("{{DATA}}", DATA);
// el grid del template está en 40 columnas; se ajusta al número real de días
out = out.replace(/repeat\(40,/g, `repeat(${NDAYS},`).replace(/grid-column:\s*2\s*\/\s*42/g, `grid-column:2 / ${NDAYS + 2}`);

const outPath = path.join(root, "quotes", slug, "entregables", "timeline.html");
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, out);
console.log(`ok ${path.relative(root, outPath)} · ${NDAYS} días hábiles · ${NWEEKS} semanas · hoy = día ${TODAY} (${fmt(todayDate)}) · lanzamiento ${LAUNCH}`);
