---
name: screens
description: Screenshot any app at desktop + mobile viewports into ~/Desktop/screens/<app>/ and open the folders. The canonical Screenshot QA pattern — use when asked to screenshot an app, QA a UI change visually, or capture routes for review. Args: <app> [routes...] (e.g. "/screens build-marketplace / /packages").
---

# /screens — Screenshot QA, The One Pattern

Screenshot an app at fixed viewports, one PNG per route, into `~/Desktop/screens/<app>/desktop/` and `.../mobile/`, then open both folders. No custom drivers, no manual resizing, no improvised sizes. Everyone — devs, QA, AI agents — uses this exact pattern.

## Arguments

`/screens <app> [targets...]` — app name (folder under `~/Desktop/screens/`) plus what to shoot. Defaults to `/` if no targets given. No app given? Infer it from the project you're working in (see port table).

Each target is one of:
- **A route** — starts with `/` (e.g. `/packages`). Shot directly with the script below.
- **A flow or screen name** — plain words (e.g. `budget`, `upload flow`, `checkout empty state`). The state lives behind client-side navigation, so you must drive the browser to it — see "Targeting a specific flow or screen".

Only shoot what was asked. `budget` means the budget step — not the whole funnel.

## Targeting a specific flow or screen

For SPA prototypes (funnels, quizzes, steppers) the interesting states are not routes. To capture one:

1. **Look for a deep link first.** Read the app source for query-param or hash support (`useSearchParams`, `?stage=`, `?step=`, dev-only stage jumpers). If one exists, it's just a route — use the normal script (`ROUTES="/?stage=budget"`).
2. **Otherwise, script the walk.** Copy the script inline and add the interaction steps before the screenshot — `page.click`, `page.fill`, `page.getByRole(...)` — reading the app's components to find real button labels and selectors. Never guess selectors; read the source.
3. **Name shots by state, not route:** slug = the flow/step name (`budget.png`, `upload-flow-2-of-3.png`). One PNG per requested state, both viewports, same output folders.
4. A multi-step flow request ("the upload flow") = one shot per meaningful step of that flow, in order — not one shot of the last screen.
5. Re-run the walk fresh for each viewport (state doesn't carry across pages).

## Step 1 — Ensure the dev server is running

**ALWAYS check for an already-running server before starting one — never spawn a duplicate.**

1. **Find the app's real port** — read its `vite.config.ts` / `package.json` / `project.json` for a configured port. The table below is a starting point, not truth (e.g. `new-yardzen-july` is configured for 4202, not the Vite default).
2. **Check for a listener**: `curl -sf http://localhost:PORT >/dev/null` (and `lsof -i :PORT -sTCP:LISTEN` to see what owns it). If the app is already being served — use it and leave it alone.
3. Only if nothing is running, start it and **poll the port — never `sleep 5`**. Watch the startup log: if the port was busy and the server picked another one (Vite does this), use the port from the log — but first check the busy port isn't already the same app.

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
