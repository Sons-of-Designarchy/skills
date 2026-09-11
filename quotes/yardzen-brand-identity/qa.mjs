import { chromium } from "/Users/danielpliego/projects/yardzen/node_modules/.pnpm/playwright@1.55.1/node_modules/playwright/index.mjs";
const files = process.argv.slice(2);
const b = await chromium.launch();
for (const f of files) {
  const pg = await b.newPage({ viewport: { width: 1000, height: 1400 } });
  await pg.goto(`file://${process.cwd()}/${f}`, { waitUntil: "networkidle" });
  await pg.waitForTimeout(500);
  const r = await pg.evaluate(() => {
    const A4 = 297 * 96 / 25.4; // px at 96dpi
    return [...document.querySelectorAll(".sheet")].map((s, i) => {
      const h = s.getBoundingClientRect().height;
      const grey = [...s.querySelectorAll("*")].filter(e => {
        const c = getComputedStyle(e).color;
        const m = c.match(/\d+/g);
        return m && m[0] > 40 && m[0] < 210 && m[0] === m[1] && m[1] === m[2];
      }).length;
      return { p: i + 1, h: Math.round(h), over: h > A4 + 2, grey };
    });
  });
  const bad = r.filter(x => x.over);
  const grey = r.filter(x => x.grey);
  console.log(`\n${f}  ${r.length} pages`);
  console.log(`  overflow: ${bad.length ? bad.map(x => `p${x.p} ${x.h}px`).join(", ") : "none ✓"}`);
  console.log(`  grey copy: ${grey.length ? grey.map(x => `p${x.p}(${x.grey})`).join(", ") : "none ✓"}`);
  await pg.close();
}
await b.close();
