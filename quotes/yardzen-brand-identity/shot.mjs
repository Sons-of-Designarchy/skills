import { chromium } from "/Users/danielpliego/projects/yardzen/node_modules/.pnpm/playwright@1.55.1/node_modules/playwright/index.mjs";
const [file, out, ...idx] = process.argv.slice(2);
const b = await chromium.launch();
const pg = await b.newPage({ viewport: { width: 860, height: 1200 }, deviceScaleFactor: 1.4 });
await pg.goto(`file://${process.cwd()}/${file}`, { waitUntil: "networkidle" });
await pg.waitForTimeout(600);
const sheets = await pg.$$(".sheet");
for (const i of idx.map(Number)) {
  await sheets[i - 1].screenshot({ path: `/tmp/${out}-p${i}.png` });
}
await b.close();
console.log("ok");
