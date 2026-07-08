---
name: screens
description: Screenshot any app at desktop + mobile viewports into ~/Desktop/screens/<app>/ and open the folders. The canonical Screenshot QA pattern — use when asked to screenshot an app, QA a UI change visually, or capture routes for review. Args: <app> [routes...] (e.g. "/screens build-marketplace / /packages").
---

# /screens — Screenshot QA, The One Pattern

Screenshot an app at fixed viewports, one PNG per route, into `~/Desktop/screens/<app>/desktop/` and `.../mobile/`, then open both folders. No custom drivers, no manual resizing, no improvised sizes. Everyone — devs, QA, AI agents — uses this exact pattern.

## Arguments

`/screens <app> [routes...]` — app name (folder under `~/Desktop/screens/`) and space-separated routes. Defaults to `/` if no routes given. No app given? Infer it from the project you're working in (see port table).

## Step 1 — Ensure the dev server is running

Check the port first; only start the server if it isn't already up. **Never `sleep 5` — poll the port.**

```bash
curl -sf http://localhost:PORT >/dev/null || {
  # from the app's directory, use the project's dev command (background)
  npm run dev &          # or: npx nx serve build-marketplace, yarn start, etc.
  echo $! > /tmp/dev.pid
  timeout 90 bash -c 'until curl -sf http://localhost:PORT >/dev/null; do sleep 1; done'
}
```

| Project / app | Port | Dev command (from) |
|---|---|---|
| Yardzen `build-marketplace` | 4200 | `npx nx serve build-marketplace` (monorepo root) |
| Yardzen `back-office` | 4210 | `npx nx serve back-office` (monorepo root, Node 24) |
| Yardzen design-sandbox apps | 5173 | `npm run dev` (from the app folder) |
| Finsera dashboard | 3000 | `yarn start` |
| Finsera thematic-baskets | 3002 | `yarn start` |
| Fawnroad | 8888 | `npm run dev:start` (from `apps/web`) |

If you started the server, stop it afterwards with `kill $(cat /tmp/dev.pid)`. If it was already running, leave it alone.

## Step 2 — Run the screenshot script

Run from a directory whose `node_modules` has `playwright` (Yardzen: `apps/design-sandbox/new-yardzen` has it; Fawnroad: `apps/web`). If `require("playwright")` fails, `npm i -D playwright` once in that app — Chromium is already cached at `~/Library/Caches/ms-playwright` (first time ever: `npx playwright install chromium`).

```bash
APP=build-marketplace BASE=http://localhost:4200 ROUTES="/ /packages" node - <<'EOF'
const { chromium } = require("playwright");
const { mkdirSync } = require("fs");
const { homedir } = require("os");

const app = process.env.APP, base = process.env.BASE;
const routes = (process.env.ROUTES || "/").trim().split(/\s+/);
const VIEWPORTS = {
  desktop: { width: 1280, height: 800 },
  mobile:  { width: 390,  height: 844 },
};
if (process.env.TABLET) VIEWPORTS.tablet = { width: 768, height: 1024 };

(async () => {
  const browser = await chromium.launch();
  for (const [name, viewport] of Object.entries(VIEWPORTS)) {
    const dir = `${homedir()}/Desktop/screens/${app}/${name}`;
    mkdirSync(dir, { recursive: true });
    const page = await browser.newPage({ viewport });
    for (const route of routes) {
      await page.goto(base + route, { waitUntil: "load" });
      await page.waitForTimeout(Number(process.env.SETTLE_MS) || 1500); // let fonts/data settle
      const slug = route === "/" ? "home" : route.replace(/^\//, "").replace(/\//g, "-");
      await page.screenshot({ path: `${dir}/${slug}.png`, fullPage: true });
      console.log(`${name}/${slug}.png`);
    }
    await page.close();
  }
  await browser.close();
})();
EOF
```

- `APP` — folder name under `~/Desktop/screens/`
- `BASE` — dev server URL
- `ROUTES` — space-separated routes; defaults to `/`
- `TABLET=1` — adds 768×1024 tablet shots (only when asked)
- `SETTLE_MS=4000` — longer wait for slow routes (Vite/Next compile on demand; first paint can take 10s+). If a route renders blank, bump this or use `page.waitForSelector()` on a real element.
- Page needs auth or a click first? Add the `fill`/`click` lines before the screenshot — don't switch tools.

## Step 3 — Open the folders and verify (macOS)

```bash
open ~/Desktop/screens/$APP/desktop ~/Desktop/screens/$APP/mobile
```

## Rules

- Viewports are fixed: desktop **1280×800**, mobile **390×844**, tablet **768×1024** — same numbers as the Visual QA Checklist. Don't improvise sizes.
- **Look at every screenshot before sharing.** A blank frame means the page didn't load — that's a failure to fix, not a deliverable.
- Multiple apps in one request → run the script once per app with its own `APP`/`BASE`. Separate folders per app, always.
- When the screenshots are the deliverable, send them to the user.
