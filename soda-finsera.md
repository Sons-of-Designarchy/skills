# Finsera — Project Guide

Part of the Casa Soda skill set. Load alongside `/soda-front` for full context on Dan's workflow, design principles, and communication style.

> Missing `/soda-front`? Run `bash ~/projects/soda/skills/setup.sh` to install/update all Casa Soda skills.

---

## Stack

Turborepo (Yarn classic), React 19, TypeScript 5, MUI 7, Vite 7, Vitest, Redux + redux-thunk, amCharts 5, MUI X Data Grid Premium, lodash-es, PostHog, Sentry

**MUI is the foundation.** No Tailwind, no shadcn. The theme is the design system — nail `base-config-theme.ts` and everything downstream snaps into place.

---

## Monorepo Layout

```
apps/
  finsera/            # Main dashboard SPA (Vite, client-only) — localhost:3000
  thematic-baskets/   # Public SSR app (React Router v7, SSR) — localhost:3002
  portfolios/         # localhost:3001
  design-system/      # Component QA gallery — localhost:3003
packages/
  finsera-core/       # @local/finsera-core — shared components, theme, API, types
```

---

## Dev Workflow

```bash
# Node version — Finsera pins 20.19.x (NOT the Soda-wide Node 24 default)
nvm use 20.19.6

# Run all apps
yarn start

# Run just one app (e.g. design-system)
cd apps/design-system && vite   # script name is "start", not "dev"

# If it fails
yarn   # reinstall

# Nuclear clean
rm -rf .turbo apps/finsera/.turbo/ apps/portfolios/.turbo/ packages/finsera-core/.turbo/ packages/thematic-baskets/.turbo/
rm -rf node_modules apps/finsera/node_modules/ apps/portfolios/node_modules/ packages/finsera-core/node_modules/ packages/thematic-baskets/node_modules/
yarn

# Lint, type check, test
yarn lint
yarn tsc
yarn test:no-watch
yarn format
```

> ⛔ **DO NOT run `yarn tsc` / `yarn lint` / `eslint` / `prettier` after every edit or every turn — it is SUPER SLOW and Dan hates it.** Make the edits and keep moving. Dan runs the checks himself at the end, only when the work is ready to be merged. Run a final check only if HE explicitly asks. Same for commits: **never `git commit` / `git merge` / `git push` until Dan explicitly tells you — always.**

---

## Git Workflow

- Base branch: `master`
- Always `git pull` before starting new work
- Branch names come from Shortcut — use the "copy branch" setting
- Use Finsera Chrome browser profile when working in Shortcut
- Commit format: `sc-XXXXX short description` — no `feat:`/`fix:` prefixes, no Claude trailers
- **Every commit must start with the ticket ID** — GitLab enforces the pattern `^(sc[\s-]|Sc[\s-]|SC[\s-])?([0-9]{4,}|Merge).+$` on squash commits. A commit message like "Add enterprise plan" will fail the pipeline. Always prefix: `sc-83133 add enterprise plan for the website`.
- When a branch has multiple commits, squash them into one before merging: `git reset --soft master && git commit -m "sc-XXXXX description"` then force-push.

**GitLab MR workflow** — no `glab` CLI. Push branch, use the MR URL printed in push output:
```
remote: To create a merge request for feat/xxx, visit:
remote:   https://gitlab.com/finsera/web-ui/-/merge_requests/new?...
```

---

## Environments

| Name | URL |
|---|---|
| localhost | `localhost:3002/` (thematic-baskets) |
| development | `https://themes.finseradev.net/` |
| staging | `https://themes.finserastg.net/` |
| production | `https://themes.finsera.com/` |

**Tools:** Shortcut (tasks), GitLab (code hosting), Pitch (presentations), PostHog (analytics)

**Meetings:** Monday 12pm — testing meeting + new feature demo

---

## Shared Package — `@local/finsera-core`

```ts
import { ui, uitheme, hooks, helpers, enums, types, coreData } from '@local/finsera-core';
import { FinseraCoreProvider } from '@local/finsera-core';
```

- `ui.*` — all shared UI components (Button, Card, FinDataGrid, LineChart, PieChart, AssetSelector, etc.)
- `uitheme.blue` / `uitheme.green` — MUI theme objects
- `mui.core.*`, `mui.icons.*`, `mui.lab.*` — all MUI re-exports

**Never import from `@mui/material` directly.** Always go through `mui.core.*`.

---

## Theme

- Theme files: `packages/finsera-core/src/theme/`
- All MUI overrides → `base-config-theme.ts` — **never** in local `ThemeProvider` wrappers
- MUI spacing base: `4px` (so `theme.spacing(2) = 8px`)
- Custom breakpoints: `xs:0, sm:600, md:900, lg:1300, xl:1536`
- Design tokens in `layout-size.ts`: `FONT_SIZE`, `INPUT_SIZE`, `APP_BAR_HEIGHT (50px)`, `LEFT_DRAWER_WIDTH (270px)`, `SECTION_BG`, `Z_INDEX`
- Fonts: Libre Caslon Condensed (serif heading) + Inter (body), loaded via `fonts.css`
- MUI filled variant is preferred for all inputs, autocompletes, date pickers
- Use `uitheme.blue` by default, `uitheme.green` for production mode
- Custom button variant: `'light'`

---

## Import Pattern

```ts
// Everything comes from the _core barrel — never direct imports
import { mui, React, ts, ui, api } from '_core';
// baseUrl is "src" so all imports are from src/
import Layout from 'views/layout';
```

---

## Data Fetching — REST Only (no GraphQL)

```ts
// SCRUD factory generates get/search/create/update/delete per resource
const basket = await api.baskets.get(id);
await api.baskets.update(id, data);
// thematic-baskets uses adminApi/usersApi for server-side loaders
const data = await adminApi(request.headers).baskets.search({ query: [...] });
```

---

## Auth

- `finsera` app: cookie `fauth`, session fetched on mount via `api.auth.getSession()`
- `thematic-baskets`: cookie `fauth` read in root middleware, role-based access via `checkAccessByRole()`
- Role hierarchy: `ANONYMOUS → FREE → PREMIUM → ADMIN`

**thematic-baskets role hierarchy:**
- `ANONYMOUS → FREE → TIER1 (Pro) → TIER2 (Max) → ADMIN`
- **FREE** — limited access, 10 baskets, basic overview. No login required to browse.
- **TIER1 / Pro** — full basket library, compare baskets & ETFs, holdings/performance views, watchlists. Currently free for a limited time.
- **TIER2 / Max** — custom baskets, guided support, advanced workflows. Coming soon.
- **ADMIN** — full access.
- Welcome modal variant (`free` vs `tier1`) driven by `user.thematic_baskets_metadata`.
- "Public Beta" was the old name for TIER1/Pro — it is now called **Pro** everywhere.

---

## Routing

- `finsera`: React Router v7 as library in Vite SPA — `logged-in-router.tsx` + `logged-out-router.tsx`, all lazy-loaded
- `thematic-baskets`: React Router v7 SSR — config-based route table in `app/routes.ts`

---

## Layout Model

```
CONTAINER (100vh)
  NAVBAR (sticky, always visible — APP_BAR_HEIGHT: 50px)
  LEFT COLUMN (scrolls) | RIGHT COLUMN (scrolls)
END CONTAINER
```

- Dialogs: `minWidth: 1100px`, below that `90vw`
- Dialogs never scroll — only inner panes scroll
- Page-level `overflow` is almost always wrong

---

## Key Files to Read First

1. `packages/finsera-core/src/index.ts` — everything exported from the shared library
2. `packages/finsera-core/src/theme/base-config-theme.ts` — all MUI overrides
3. `packages/finsera-core/src/theme/layout-size.ts` — all design tokens
4. `apps/finsera/src/_core/index.ts` — the import barrel
5. `apps/finsera/src/in-app.tsx` — auth boot, session fetch, router switching
6. `apps/thematic-baskets/app/routes.ts` — complete SSR route table
7. `apps/thematic-baskets/app/_helpers/server/with-access-control.ts` — role-based auth guard

---

## Visual Rules

- Padding: less is more — actively hunts excessive padding
- Shadows on chart legends: remove
- Backgrounds on accordions: remove
- Dividers: `showDivider` prop, default `false`
- No link underlines
- Table numbers (market cap, weight, price): right-aligned
- Chips in autocompletes: darker background
- Fonts loaded via `<link>` in HTML head — never CSS `@import`
- **Icon containers:** Use `<mui.core.IconButton disabled>` instead of a plain `<Box>` when displaying a non-interactive icon with a background. This gives consistent sizing, border-radius, and hover/focus states for free. Override `&.Mui-disabled` to preserve the background color.
- **Buttons:** Never apply custom `sx` styles (fontSize, fontWeight, padding, borderRadius) to buttons. Use `ui.Button` with standard `variant` and `size` props. The theme handles everything.

## MUI Gotchas (real corrections — don't repeat)

- **Never use custom hex colors or rgba values in MUI sx props.** Always use theme colors (`color="warning"`, `bgcolor: 'primary.main'`, etc.). Only use custom values when Dan explicitly asks for them.
- **Don't use `pt` on `mui.core.DialogContent`.** MUI's internal styles override it silently. Use `mt` on the first child inside DialogContent instead (e.g. wrap first element in `<Box mt={3}>`).
- **Don't use ButtonBase for custom-shaped clickable cards.** ButtonBase inherits theme `borderRadius` and overrides any explicit value, causing pills/ovals. Use a plain `Box` with `onClick`, `role="button"`, and `tabIndex={0}` instead.

---

## Syntax Preferences

- Optional chaining everywhere: `?.length` not `&& .length > 0`
- Lodash (`lodash-es`) for utility operations
- `useMemo` for expensive calculations
- MUI breakpoint hooks — never calculate window size manually
- Null guard in map: `if (!item) return null`

---

## Design System App (localhost:3003)

The `apps/design-system` app is the component QA gallery. Script is `start`, not `dev`.

**Current initiative:** consolidating all local finsera components into `finsera-core`. An audit page lives at the top of the design system gallery showing:
- All components in `apps/finsera/src/_components/` that aren't from core
- Status: `candidate-for-core` or `app-specific`
- Cross-app duplicates flagged (currently: `merged-asset`, `section-title`)

**Process:**
1. Use the audit page to pick a component group
2. Create a branch
3. Move candidates into `finsera-core`
4. Delete local copies, update imports in finsera
5. Verify thematic-baskets and portfolios aren't affected

---

## Thematic Baskets — App Architecture

**Routes & views:**
- `/dashboard` → `views/dashboard/index.tsx` → `ChartsSection` → `EmergingBaskets`
- `/basket/:id/:slug` → `views/basket/index.tsx` → `BasketDetail`
- `/watchlist/:id` → watchlist view with sidebar
- `/custom-themes` — TIER1+ only

**Key contexts:**
- `BasketsContext` (`_contexts/baskets-context.tsx`) — all basket data, polling, CRUD callbacks
  - `allBaskets`, `baskets` (non-ETF), `userBaskets`, `labels`, `isLoading`
  - `startPolling()` / `stopPolling()` — called in dashboard/basket route effects
- `UserContext` — current user, `thematic_baskets_role`, `thematic_baskets_metadata`

**ExtendedBasket type** (`_core/typescript-definitions/app.ts`):
```ts
type ExtendedBasket = ReducedBasket
  & { jobStatus: JobStatus }
  & { returns: { [key in PORTFOLIOS_HISTORY_ENUM]: number } }
  & { exposures: { theme_momentum, theme_volume, theme_sentiment, theme_hedge_fund, theme_overall } }
  & { is_etf?, is_user_basket? }
```

**Returns keys** — always use `ts.enums.PORTFOLIOS_HISTORY_ENUM.*`:
- `ONE_DAY` (LD), `ONE_MONTH` (LM), `YTD`, `THREE` (L3Y), `FULL`

**Exposure keys** (from `EXPOSURE_RANK_METRICS` in `_core/shared-variables.ts`):
- `theme_momentum`, `theme_volume`, `theme_sentiment`, `theme_hedge_fund`, `theme_overall`

**Enums access pattern:**
```ts
import { ts } from '_core';
basket.returns[ts.enums.PORTFOLIOS_HISTORY_ENUM.YTD]
```

**Component locations:**
- `_components/basket/basket-detail.tsx` — full basket detail (tabs: overview, compare, related_etfs)
- `_components/basket/basket-nav-footer.tsx` — guided next/back footer
- `_components/chart-sections/emerging-baskets/index.tsx` — dashboard table + filters
- `_components/insight-banner/index.tsx` — "what's happening now" banner
- `_components/welcome/index.tsx` — onboarding modal (3-step guided flow)
- `_components/basket-image.tsx` — basket icon/image renderer
- `_helpers/basket.ts` — `generateBasketUrl`, `generateBasketSlug`, `getBasketSegments`, `extendBasketMetadata`

**ClickUp EPICS:** `Clientes CS 2026 → Finsera / Fawnroad / Novena → EPICS` (list id: `901326864344`)

**Product context (April 2026):** Active initiative is "Guided Discovery & Insight Activation" — turning the app from a data tool into a guided experience for decision-makers. All work is frontend-first from BasketsContext data (no new API calls without approval).

---

## PostHog Analytics

PostHog is installed and initialized in `app/root.tsx`. The init is gated by `import.meta.env.MODE`:
- Currently `=== 'development'` (for dev demo) — **swap to `=== 'production'` before prod launch**
- Key: `phc_4KjaZlE7ca3KY2QfjMk9KzLUO8EwxzSDDKsdBwBcsAt`, host: `https://us.i.posthog.com`
- If PostHog is not initialized (wrong env), all `.capture()` calls silently no-op — safe.

`posthog` is exported from `@local/finsera-core` → re-exported from `_core` barrel. Always import from `_core`:
```ts
import { posthog } from '_core';
```

**Hotjar has been removed.** Do not re-add it.

**Identity** — called in `views/dashboard/index.tsx` on user load:
```ts
posthog.identify(String(user.id), { email: user.email });
```

**Events currently tracked:**

| Event | File |
|---|---|
| `page_viewed` | root.tsx |
| `auth_completed` + identify | views/dashboard/index.tsx |
| `basket_viewed` | views/basket/index.tsx |
| `basket_tab_clicked` | _components/basket/basket-detail.tsx |
| `add_to_watchlist_clicked` | _components/basket/basket-detail.tsx + views/watchlist/add-to-watchlist.tsx |
| `watchlist_created` | views/watchlist/add-to-watchlist.tsx + views/watchlist/watchlist-form.tsx |
| `upgrade_prompt_shown` | _components/call-to-action-chart.tsx |
| `upgrade_prompt_clicked` | _components/call-to-action-chart.tsx |
| `register_step_viewed` | views/authentication/register/index.tsx |
| `pricing_viewed` | views/pricing/index.tsx |
| `upgrade_clicked` | views/pricing/price-boxes.tsx |
| `period_selector_clicked` | _components/period-selector.tsx |

**GTM docs** live in `apps/thematic-baskets/GTM/`:
- `tracking.md` — full event plan (Priority 1/2/3)
- `plan-6-weeks.md` — 6-week shape-up sprint plan
- `market-research.md` — competitive landscape, ICPs, pricing benchmarks
- `research.md` — full basket catalog with performance data
- `wiki.md` — technical + product wiki for team/future hires

**GTM state (May 2026):** 0 users, access-key gated, 6-week sprint starting May 2026. North star: weekly active users who viewed 3+ baskets. PostHog deployed to dev for demo, migrate to prod after sprint week 1.
