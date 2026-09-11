# Yardzen — Project Guide

Part of the Casa Soda skill set. Load alongside `/soda-front` for Dan's workflow, design principles, and communication style.

---

## Stack

NX monorepo (pnpm), Next.js 15 (App Router), TypeScript strict, Tailwind CSS, GraphQL (Apollo codegen), Prisma + PostgreSQL, Contentful CMS, NextAuth v4 + custom V2 JWT auth, Split.io feature flags

---

## Design Values — Dan's Brand Doc (living draft)

> There is currently no dedicated brand/design lead at Yardzen — Dan owns brand judgment. This section is his working read of the brand, distilled from what's actually shipped (tokens, type, photography rules, partner lineup). Treat it as the source of truth for design decisions until it graduates into a standalone brand doc. If a decision isn't covered here, Dan decides — then it gets added here.

### 1. Real yards, real work
Trust is the product. Yardzen sells a transformation people can't preview, so every image must be a real Yardzen project — never Unsplash, never stock, never AI-generated filler. If we don't have the photo, we change the layout, not the honesty. (This is why the `@yz-ds` asset rule exists — it's a brand value enforced in code.)

### 2. Nature does the color
The palette stays quiet so the landscapes carry the color. Deep green `action-main` (#1B6245) for action, warm near-black `typo-primary` (#323232) for text, warm off-white `texture-primary` (#F6F5F4) for surfaces. The UI is the frame, the yard is the painting. Never introduce a loud accent that competes with plant/photo imagery.

### 3. Editorial warmth, utilitarian clarity
The type system is the brand's voice: **Arsenal** (serif display) gives the garden-magazine, considered-design feel; **Roboto** (app) / **Geist** (sandbox body) do the work. Serif for aspiration, sans for action. Never swap the roles — a serif button or a sans hero headline both read as off-brand.

### 4. Premium taste, approachable delivery
The partner lineup (Serena & Lily, McGee & Co., Belgard…) signals design-world credibility. The product should feel like working with a design studio, not using a SaaS tool — but a homeowner who's never hired a designer must never feel out of their depth. Aspirational imagery, plain-spoken copy, obvious next steps.

### 5. Calm layouts, portfolio whitespace
Photography-first composition: generous whitespace, few competing elements, hierarchy through scale and weight rather than boxes and borders. Follows the global Soda rules (1px subtle borders, no visual noise) but leans warmer and more editorial than fintech-clean.

### 6. One system, no forks
Brand consistency is credibility. Everything comes from the design system (Trellis / `@yardzen/ui` in-app, `@yz-ds` in sandboxes). A one-off style is a brand leak — when the system has a gap, file the ticket and surface it, don't invent around it.

### 7. The feeling to protect
If a screen could belong to a generic home-services marketplace, it's wrong. The target feeling: *"these people have taste, and they'll handle it."* Confident, warm, grounded in real outdoor living — never corporate, never salesy, never sterile.

---

## Dev Setup

```bash
cd yardzen-app        # or wherever the monorepo is cloned
nvm use 24.0.0
git checkout dev && git pull    # base branch is dev (not main/master)
```

**Node version:** Next.js requires Node `^18.18.0` or `>=20` — `nvm use 24` before running dev servers.

## Dev Commands (run from monorepo root)

```bash
# Run only build-marketplace (most common)
npx nx run-many --target=serve --projects=build-marketplace

# Run with API backend too (required for: design profile quiz, any Prisma DB features)
npx nx run-many --target=serve --projects=api,build-marketplace

# If the API build fails with Prisma errors after a branch switch/pull
# (TS2339 "Property X does not exist on type 'PrismaService'", missing
# @prisma/client enums) — the client/DB are stale vs the schema. Fix:
pnpm run prisma -- migrate dev

# Run API alone (only when you need backend data — not the default)
nx serve dev

# Run single app directly
nx serve build-marketplace                    # port 4200

nx build build-marketplace                    # production build
nx lint build-marketplace                     # lint
nx test build-marketplace                     # tests
nx run build-marketplace:graphql-codegen      # regenerate GQL types

# Always run before pushing:
pnpm run lint
```

**NX project graph errors — common fix:**
- `Failed to process project graph` → run `nx reset` first
- If it persists with `--verbose`, look for: duplicate project names, missing packages, or ESM/CJS conflicts in `next.config.js` files
- Known issue: `apps/design-sandbox/trellis-v2` must have a unique `name` in `package.json` — not `"trellis"` (conflicts with `apps/trellis`)
- "Failed to process project graph" or "crypto is not defined" → you're on Node 18. `nvm use 24` and retry.

---

## Git & PR Workflow

- Base branch: **`dev`** (not `main` — that's a different branch, exists but is not ours)
- Always pull from `dev` before starting
- Open Jira ticket first, create branch from the ticket (use Jira's "create branch" option)
- Commit format: `git ci -m "message-branch"`
- Run `pnpm run lint` before every push
- PR must include: title matching ticket name, bullet-point description of changes, before/after screenshots, local URL + which component to test
- Add Natalie and the other dev as reviewers on every PR
- Add screenshot with link to Dan's playground in the GitHub PR conversation
- Use the Yardzen Chrome browser profile for Claude and GitLab access — always run Claude from the batman account via this profile

**PR hygiene — clean branches:**
- Each PR should contain **only the commits for that ticket** — no inherited commits from previous branches
- If a branch has extra commits (from branching off a non-dev branch), create a clean branch:
  ```bash
  git checkout dev
  git checkout -b my-clean-branch
  git cherry-pick <commit-sha>
  git push origin my-clean-branch
  ```
- Then close the dirty PR and open a new one from the clean branch
- Dan reviews PRs visually on GitHub — dirty commit history is always flagged

**Git merge conflicts:**
- When merging and you want to keep the incoming branch version: `git checkout --theirs <file>`
- When you want your version: `git checkout --ours <file>`
- When in doubt about which side is "theirs" vs "ours", ask Dan

**CI:**
- Formatting errors are the most common real cause of CI failures — run Prettier first
- Re-run failed jobs via GitHub Actions UI before diagnosing code issues

---

## Contentful Access

- Email: `daniel.pliego@yardzen.com`
- Password: (see 1Password)

## Yard Capture (mobile app) Setup

```bash
cd yardzen-app/mobile-apps/yardzen-capture
./start.sh            # loads QR code for the mobile app
```

---

## Route Groups in `app/`

| Group | Paths | Purpose |
|---|---|---|
| `(default)` | `/login`, `/profile`, `/gallery`, `/build-studio`, `/payments/[invoiceId]` | Authenticated user flows |
| `(marketing)` | `/home`, `/packages`, `/[...slug]` | Public marketing, Contentful-driven |
| `(minimal)` | `/checkout`, `/checkout/extras` | Stripped shell, no main nav |
| `(quiz)` | `/design-consultation/[survey_id]/[[...slug]]` | Multi-step design quiz |

## Key Files to Read First

1. `middleware.ts` — auth gating, `PUBLIC_PATHS`, anonymous ID creation
2. `app/(default)/layout.tsx` + `ClientsideLayout.tsx` — full provider stack (Apollo, GTM, Split, Datadog)
3. `app/(default)/ServerContext.ts` — `getUserIdFromServerContext()` — canonical user getter in server components
4. `providers/V2Auth/serverSideV2Auth.ts` — dual-token (V1 Firebase / V2 JWT) auth chain
5. `app/(marketing)/packages/ContentfulPage.tsx` — Contentful section router (`isTypeXxx` chain)
6. `libs/contentful/utils/getEntry.ts` — caching, overrides, preview logic
7. `app/(default)/prisma.ts` — Prisma singleton
8. `codegen.ts` + `gql/apollo.ts` — generated GQL types imported everywhere

## Shared Libs (most-used)

| Alias | Role |
|---|---|
| `@contentful/types` | Generated TypeScript skeletons for every Contentful type |
| `@contentful/utils` | `getPage()`, `getPackageDetail()`, `getBanner()` with ISR cache tagging |
| `@yardzen/components/*` | Granular component subpath exports |
| `@yardzen/ui/components/*` | Base design system (Page, Footer, Spinner, Link, etc.) |
| `@yardzen/next-api-util` | `fetchYzGqlApi()` — server-side typed GQL fetcher |
| `@yardzen/next-client-util` | `GQLClient()`, GTM events, analytics helpers |
| `@yardzen/splitio` | Feature flags — `SplitTreatmentName` enum, server/client wrappers |
| `@yardzen/auth` | `validateV2Token()`, `validateLegacyToken()`, `exchangeV1ForV2Token()` |
| `@yardzen/ui` | Trellis itself (`libs/ui`) — the shipped design system, 160 components |
| `@yz-ds` | `libs/ui-v2` — the waiting room, 198 components not yet in Trellis. Sandbox-only alias, set per app in `vite.config.ts` |

## Trellis Catalog & Shipping

The catalog at **https://yz-trellis-v2.vercel.app** (`apps/design-sandbox/trellis-v2`, port 3001) is the one true list of what exists. It reads a generated manifest, so it cannot drift from the code.

**The two row files.** Every component file needs a row, or the build fails:

| File | Holds | Row shape |
|---|---|---|
| `libs/ui/catalog/taxonomy.ts` | Trellis (`libs/ui`) — what shipped | `file`, `type`, `id`, `name` |
| `libs/ui-v2/catalog/purgatory.ts` | ui-v2 (`@yz-ds`) — what is waiting to graduate | + `graduation`, `target?`, `concern?` |

`graduation` is `add` (net-new, straight promotion), `merge` (a Trellis twin exists — needs a merge + impact audit) or `archive` (stays on purpose). `concern` is the expensive half of duplicate detection: two rows with the same concern are two implementations of one idea, which no name-keyed inventory can see.

**Regenerate after any component change:**

```bash
node libs/ui/catalog/build.mjs --with-purgatory          # writes components.json + duplicates.md
node libs/ui/catalog/build.mjs --with-purgatory --strict # same, but exits 1 on any gate failure
```

Gates that fail the build: a component file with no taxonomy row, a row naming a file that no longer exists, a duplicate anchor id, and a Storybook title that disagrees with the taxonomy. The manifest is deterministic — no timestamps — so re-running produces no diff and a real change is legible in review.

**Filing a new row:** put it in its existing `// ── <type> — N` block and bump the count in that header. Never append to the end of the file. **New types need Dan's approval** — the type vocabulary is shared between both files, so a new one has to be added in both.

**Shipping — one command, never `vercel deploy` by hand:**

```bash
cd apps/design-sandbox/trellis-v2
npm run check    # regenerate → typecheck → build → route-check, no deploy
npm run ship     # the same, then deploy, re-alias and verify the alias serves this build
```

`ship.mjs` route-checks 15 routes at 1440px and 390px against the *built* bundle (blank renders, page errors, horizontal overflow, tap targets under 24px), then re-points `yz-trellis-v2.vercel.app` — `vercel deploy --prod` only moves the project's generated domain, which is how the site once sat six days behind the branch while every deploy reported success.

**Routes:** `/intro` (front door), `/all` (full catalog), `/f/:family`, `/t/:type`, `/foundations`, `/spacing`, `/icons`, `/practice` (the laws, with `#rules`), `/shipping`, `/dev-tools`.

The do/don't rules live once, as data, in `src/content/rules.ts` — a rule earns its place by having cost us something. Pull one by id rather than restating it.

## Auth

- Two systems coexist: V1 (Firebase JWT) and V2 (custom JWT, preferred)
- Server components: use `getUserIdFromServerContext()` or `getAuthedUserInfo()`
- If V2 token missing, auto-generated from V1 — no redirect
- Add new public routes to `PUBLIC_PATHS` in `middleware.ts`

## GraphQL

- Run codegen after any schema change: `nx run build-marketplace:graphql-codegen`
- Queries in co-located `queries.ts` files using `gql` tag
- Server-side: `fetchYzGqlApi<QueryType, VariablesType>({ query, variables })`
- Client-side: standard Apollo hooks from `gql/apollo.ts`
- Never write raw fetch calls — always use typed helpers

## Contentful Integration

- Types in `libs/contentful/types/` — always use generated types
- Fields accessed as `entry.fields.fieldName` — guard with `?.` (can be `undefined`)
- `customStyles` prop = scoped `<style>` tag in component root — intentional architecture, not a hack
- `internalYardzenId` field → prefix with `hero-` → CSS class for per-instance scoping
- Class goes on the **correct inner element**, never a generic outer wrapper
- Section routing: `isTypeXxx(section) && <Component />` chain — no switch/case

**Contentful components — key files:**

| Component | Path | Notes |
|---|---|---|
| `Heading` | `libs/next-components/src/contentful/Heading.tsx` | Used for consult call module, section headings. Has `full-width` and `medium-width` variants via CVA. |
| `HeadingBanner` | `libs/next-components/src/contentful/HeadingBanner.tsx` | Like Heading but with rich text + background color |
| `BeforeAndAfterSection` | `libs/next-components/src/contentful/BeforeAndAfterSection.tsx` | Renders tabbed before/after gallery |
| `GridItemCollection` | `libs/next-components/src/contentful/GridItemCollection.tsx` | Grid of cards — many variants: `large-top-image`, `small-top-image`, `medium-top-image`, `headshot`, `small/medium-left-side-image` |
| `MultiModuleContainer` | `libs/next-components/src/contentful/MultiModuleContainer.tsx` | Side-by-side module layout. Uses `Heading` via `headingClassName` prop overrides — watch for hardcoded `pt-*` classes here |
| `CalendlyEmbed` | `libs/next-components/src/contentful/CalendlyEmbed.tsx` | Calendly iframe embed — this IS the "consult call" Contentful module |

**GridItemCollection — important behavior:**
- `numberOfMobileColumns` and `numberOfDesktopColumns` come from Contentful CMS fields
- Grid uses `grid-cols-${mobileColumnsResolved} sm:grid-cols-2 md:grid-cols-${desktopColumnsResolved}` — `sm:grid-cols-2` only applies to `large-top-image`, `small-top-image`, `medium-top-image` variants
- Logo cards (cards with `backgroundColor !== "none"`) get fixed `h-[108px]` image container + `object-contain` — full-width image cards don't
- `headshot`, `small-left-side-image`, `medium-left-side-image` variants are unaffected by the tablet grid fix

## Styling

- Tailwind extends `libs/ui/src/tailwind.config.js`
- Fonts: `Arsenal` (serif) and `Roboto` via `next/font/google`
- Custom tokens: `action-main` (#1B6245), `typo-primary` (#323232), `texture-primary` (#F6F5F4)
- Run Prettier before pushing — formatting failures are the most common CI break

**Color roles and schemes (`libs/ui/src/tokens/`).** Four files stack in this order, emitted by `tailwind.config.js`: legacy primitives (`tokens.js` → `--yz-brand-*`, `--yz-c-*`), the v2 seedground set (`tokens-v2.js` → `--yz-color-*` role vocabulary: surface / text / action / border), the default scheme, then one `[data-scheme="…"]` block per curated scheme (`green-accent`, `dark-green`, `toll-brothers`, `dark`).

- **One axis.** A scheme that happens to be dark is just a scheme — there is no separate light/dark theme axis. To combine looks, add a named scheme; finite curated names protect brand and contrast, and it is exactly what a Contentful editor picks from one dropdown.
- Colour comes from a token: `bg-[var(--yz-color-action)]`, never `bg-[#626e58]`. Same pixels today; the difference is what happens when the brand green moves.
- Overrides belong inside a scheme, never at bare `:root` — an app-level `:root` override outranks every scheme, so the canvas stays put while text flips. That is what washes headings out in dark mode.
- Borders are always 1px. Radii and spacing come off the scale (`var(--yz-radius-lg)`) — an unscaled `7px` is a value nobody chose on purpose.

**Typography — every visible text node, no exceptions.** In any sandbox app on `@yz-ds`, use `<Typography>`. No raw `<h1>`–`<h6>`, `<p>` or `<span>` with inline font styles.

- Font → `font="display"` (Arsenal) or `font="body"` (Geist). Never `fontFamily` in a `style` prop.
- Size → `variant` preset or `size`. Only use `fontSize` in `style` for clamp/fluid values with no preset.
- Colour → `color` prop only (`"primary"`, `"secondary"`, `"muted"`, `"inherit"`). **Never a hex, rgba or CSS var on a Typography element.** No `const C = "..."` colour constants, ever.
- Links with hover colour changes: set `color` on the `<Link>`, `color="inherit"` on the `<Typography>` inside.
- Weight → `weight` prop. Never `fontWeight` in a `style` prop.

```tsx
// ❌ raw element with inline styles
<h2 style={{ fontFamily: "var(--yz-font-display)", fontSize: 40, color: "#212121" }}>
// ❌ colour constant anywhere in the file
const C = "#212121";
// ✅ correct
<Typography font="display" weight="normal" as="h2" style={{ fontSize: "clamp(40px, 5vw, 64px)", lineHeight: 1.08 }}>
<Typography color="secondary" variant="body-sm">
// ✅ correct hover pattern
<Link style={{ color: "var(--yz-color-text-secondary)" }} onMouseEnter={...}>
  <Typography color="inherit" variant="body-sm">link text</Typography>
</Link>
```

## Conventions

- No `@/` alias — use relative paths within the app; monorepo libs via `@yardzen/<lib>`
- Server components: async functions, no directive. Client components: `"use client"` as first line.
- Pattern: server component fetches → passes serializable props to client leaf
- Co-located: `queries.ts` (GQL), `actions.ts` (server actions), `classes.ts` (Tailwind strings)

**Self-verify with a headless browser before saying it's done.** Dan reviews visual work live himself and does not want screenshots handed to him — that is about not slowing *him* down, not permission to skip verifying your own. Every time you touch CSS, layout or interaction in a sandbox app, measure the real thing:

```js
const { chromium } = require("/Users/casasoda/projects/yardzen/yardzen/node_modules/.pnpm/playwright@1.55.1/node_modules/playwright");
// pin the version actually installed — check node_modules/.pnpm/ if this path 404s
```

If the browser binary is not cached (`browserType.launch: Executable doesn't exist`), download it once — this only writes to `~/Library/Caches/ms-playwright`, never the repo:

```bash
PLAYWRIGHT_BROWSERS_PATH="$HOME/Library/Caches/ms-playwright" \
  node node_modules/.pnpm/playwright@1.55.1/node_modules/playwright/cli.js install chromium
```

Use it to measure real `getBoundingClientRect()` and computed styles rather than eyeballing a fix from the diff, to drive an app's own dev-panel stage jumps instead of clicking through a whole funnel, and to simulate flows end to end — pin-drops, form fills, even camera recorders via `chromium.launch({ args: ["--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"] })`. Also the fastest way to tell a blank page from a slow one: a crashed component blanks the whole route while the dev server still reports success.

Bugs a code read alone missed:
- A pill/badge shape that only reads correctly for short text — a full sentence in `rounded-full` clips against the container edge. Fine for a 2–3 word value, broken for a clause; check the rendered width.
- A native `<img>` is draggable by default, so a click-drag near an annotation pin kicks off the browser's own image-drag and its edge-auto-scroll. Looks like a scroll bug, isn't one — `draggable={false}` on the image.

## Scope Discipline

- Only touch files relevant to the task
- Lockfiles, unrelated components, go files must NOT appear in a feature branch commit

## Icons

- Font Awesome Pro — don't swap it, don't add icon changes without explicit confirmation
- Custom SVG icons live in `libs/ui/src/icons/src/`
- To update an icon: replace the SVG file with the same filename — no code changes needed
- Quiz start icon: `libs/ui/src/icons/src/quiz-start.svg`

## Local Dev with DB (design profile quiz requires this)

- Docker must be running before starting the API
- TablePlus is used to inspect the local DB
- Run API in a **separate terminal tab** from build-marketplace:
  - Tab 1: `npx nx serve api` (port 3000)
  - Tab 2: `npx nx serve build-marketplace` (port 4200)
- DB connection: `postgresql://yardzen:yardzen@localhost:5432/yardzen`
- If Postgres container not running: `docker-compose -f apps/api/docker-compose.test.yml up -d`

---

## Design Sandbox Deployments

Design sandbox apps live in `apps/design-sandbox/` inside the NX monorepo. They are standalone Vite SPAs — each has its own `package.json`, `vite.config.ts`, and `vercel.json`.

**Why they must build locally:** every app imports from `libs/ui-v2/` via the `@yz-ds` alias in `vite.config.ts`. That path resolves to `../../../libs/ui-v2/src` — outside the app subdirectory — so Vercel's remote build fails with "Can't resolve libs/ui-v2/...". The fix: always build locally first, then push the `build/` output to Vercel.

### Deploy workflow — same for every app

```bash
cd apps/design-sandbox/<app-name>
npm run build           # resolves libs/ui-v2 correctly from the monorepo
vercel --yes --prod     # uploads build/ and serves it — done in ~15 seconds
```

That's it. No environment variables, no secrets, no special flags.

### All deployed apps

Audited 2026-09-04. Ports come from each app's `vite.config.ts`; project names from its `.vercel/project.json`.

| App | Vercel project | Live URL | Port |
|---|---|---|---|
| `trellis-v2` | `trellis-v2` | https://yz-trellis-v2.vercel.app | 3001 |
| `unified-funnel` | `unified-funnel` | https://unified-funnel.vercel.app | 4202 |
| `client-account` | `design-delivery` | https://design-delivery.vercel.app | 4211 |
| `lowes-yardai` | `lowes-yardai` | https://lowes-yardai.vercel.app | 4214 |
| `yardzen-for-pros-july` | `yardzen-for-pros-july` | https://yardzen-for-pros-july.vercel.app | 4212 |
| `toll-brothers-onboarding` | `yz-toll-brothers` | https://yz-toll-brothers.vercel.app | 4213 |
| `shop-full` | `shop-full` | https://shop-full-sigma.vercel.app | 3001 |
| `pros-landing` | `yz-for-pros-landing` | https://yz-for-pros-landing.vercel.app | 3002 |
| `new-yardzen` | `new-yardzen` | https://new-yardzen.vercel.app | 3000 |
| `yardzen-for-pros-pilot` | not linked | — | 4213 |
| `back-office` (Next) | `yz-back-office` | https://yz-back-office.vercel.app | 4210 |
| `pro-portal` (Next) | `pro-portal` | https://pro-portal-chi.vercel.app | 4212 |

Not deployable as they stand: `color-schemes` and `toll-brothers-landing` (no `package.json`), `archive/shop-mvp`.

**Ports collide** — `trellis-v2`/`shop-full` on 3001, `toll-brothers-onboarding`/`yardzen-for-pros-pilot` on 4213, `yardzen-for-pros-july`/`pro-portal` on 4212. Only one of each pair runs at a time; `lsof -ti :<port> | xargs kill -9`.

**`client-account` was `design-delivery`** — renamed in `c1609d9d9`, but the Vercel project and its URL still say design-delivery. An untracked `apps/design-sandbox/design-delivery/` (367MB of `build/` and `node_modules/`) is left behind from before the rename; it is not the app.

**`trellis-v2` never deploys with a bare `vercel --yes --prod`** — use `npm run ship`. See the Trellis Catalog & Shipping section: the deploy is gated on the manifest, a typecheck, a build and 30 route checks, and the canonical alias has to be re-pointed afterwards.

All projects are under the `danielpliego-4456s-projects` Vercel scope.

### First-time setup on a new machine

```bash
npm install -g vercel
vercel login            # authenticate — use your Yardzen or personal account
                        # Dan will add you to the danielpliego-4456s-projects scope
```

Then deploy any app:
```bash
cd apps/design-sandbox/<app-name>
npm run build
vercel --yes --prod     # first run: Vercel prompts to link to the existing project
                        # pick "link to existing project" and enter the project name from the table above
```

After the first link, subsequent deploys just need `npm run build && vercel --yes --prod`.

### Adding a new design sandbox app to Vercel

1. Copy `vercel.json` from `lean-onboarding-v2` — use `buildCommand: ""`, `installCommand: ""`, `outputDirectory: "build"` to prevent remote builds
2. Build locally: `npm run build`
3. Deploy: `vercel --yes --prod` (Vercel auto-detects Vite, creates a new project)
4. Optionally set a vanity alias: `vercel alias set <generated>.vercel.app <alias>.vercel.app`
5. Add the project to the table above

---

### The two Next.js sandboxes — back-office and pro-portal

Not Vite SPAs. Both are **Next.js App Router** apps wired into Nx (they mirror eden's structure) and both use **`@yardzen/ui` (Trellis)**, never `@yz-ds`. The point is that a page built here can be copy-pasted into eden with zero rewrite — same framework, same imports, same conventions. Run them with Nx, not npm:

```bash
nvm use 24
npx nx serve back-office      # http://localhost:4210 → redirects to /wireframe/
npx nx serve pro-portal       # http://localhost:4212
```

**back-office** (`apps/design-sandbox/back-office`, live at https://yz-back-office.vercel.app) is the wireframe for the new **Yardzen Design Studio** — the back-office tool that replaces Liisa for designers. Everything lives under `app/wireframe/` (`_components/`, `_data/`, `project/`). Wireframe mode: mock data only, no backend, no auth, fast iteration. `CONTEXT.md` in that folder is its source of truth — read it end to end before touching the app.

**Trellis discipline — the whole point of these two.** Import from `@yardzen/ui/components/<name>`, the exact path eden uses. When you hit a gap — a missing variant, a missing token, an inline hex — file it against `libs/ui` rather than working around it. These apps exist to surface those gaps. Reusable layouts are first-class: if you build the same shell twice, extract it.

**Deploying a Next.js sandbox** is a static export, because Nx generates a bloated `package.json` and a lockfile referencing private Yardzen FontAwesome packages, so Vercel's `pnpm install` always fails. Static export skips install entirely:

```bash
nvm use 24
npx nx build back-office --configuration=production
cd dist/apps/design-sandbox/back-office
mv dist/.next/* . && rm -rf dist
vercel --yes --prod --scope danielpliego-4456s-projects
```

`vercel.json` in that dist folder: `{"buildCommand": "", "installCommand": "", "outputDirectory": ".", "framework": null, "cleanUrls": true, "trailingSlash": true}`.

What makes it work in `next.config.js`: `output: "export"` (required — produces static HTML), `distDir: "dist/.next"`, `trailingSlash: true`, `images: { unoptimized: true }`.

**`redirect()` from `next/navigation` throws at build time under static export.** Redirect on the client instead:

```tsx
"use client";
useEffect(() => { router.replace("/wireframe/"); }, [router]);
return null;
```

## Shared Image Assets (`libs/ui-v2`)

Real Yardzen project photos live in `libs/ui-v2/src/assets/` and are exported from `@yz-ds`. Any design sandbox app that needs project imagery imports from there — never Unsplash, never hardcoded URLs, never local copies.

**Rule:** No Unsplash URLs anywhere in design sandbox apps. No hardcoded image URLs. Images come from `@yz-ds`.

### Brand/partner logos — ALWAYS the CDN, NEVER a local file

Partner brand logos (Belgard, Serena & Lily, McGee & Co., Volt, Lowe's, …) live on the Yardzen prod CDN and are resolved through **one helper** in `libs/ui-v2/src/brand-logos.ts`, exported from `@yz-ds`:

```ts
import { brandLogoUrl, brandLogoUrlByName } from "@yz-ds";

brandLogoUrl("mcgee-and-co");        // → https://prod-cdn-images.yardzen.com/brand-logos/brand-mcgee-and-co.png
brandLogoUrlByName("Serena & Lily"); // → same, resolved by display name (or null if no CDN asset)
```

**Hard rules:**
- **Never** import or hardcode a logo from any `logo-brands/` folder. The folder under `libs/ui-v2/src/assets/logo-brands/` is a local *working copy* for reference/re-upload only — apps must not read it, and apps must not keep their own copy (`public/assets/logo-brands/`, `src/lib/ui-v2/logo-brands/`, etc. are banned).
- **Never** write a raw `https://prod-cdn-images.yardzen.com/...` string in an app. Go through `brandLogoUrl()` so the CDN host lives in exactly one place.
- Keys are URL-safe kebab (`mcgee-and-co`, `serena-and-lily`, `catalyst-fence`). CDN files are `brand-<key>.png`.
- Exceptions that stay bundled: **CB2** is an SVG (`logoCB2` from `@yz-ds`), and a few Figma-only marks (Ledge Lounger, Toja Grid, Sherwin-Williams) have no CDN asset yet.
- To add a logo: upload `brand-<key>.png` to the CDN, drop the same file in `libs/ui-v2/src/assets/logo-brands/` for reference, and add `<key>` to `BRAND_LOGO_KEYS` (+ a display alias in `BRAND_NAME_TO_KEY` if consumers key by name).

### Current asset catalog

| Export name | File | What it is |
|---|---|---|
| `imgCallahanHero` | `looks/callahan-florida/hero-look-callahan-florida.jpg` | Callahan Florida hero |
| `imgCallahan01–06` | `looks/callahan-florida/look-callahan-florida-0N.jpg` | Callahan gallery shots |
| `imgNapaHero` | `looks/napa/hero-look-napa.jpg` | Napa look hero |
| `imgNapa01–06` | `looks/napa/look-napa-0N.jpg` | Napa gallery shots |

### Import pattern (any sandbox app)

```ts
import {
  imgCallahanHero,
  imgCallahan01,
  imgNapaHero,
  imgNapa03,
} from "@yz-ds";

// Use directly as src:
<img src={imgCallahanHero} alt="..." />
```

### Adding new shared images

1. Copy the image file(s) into the appropriate folder under `libs/ui-v2/src/assets/`
   - Project/look photos → `assets/looks/<look-name>/`
   - Everything else → create a logical subfolder (e.g. `assets/misc/`)
2. Add named exports to `libs/ui-v2/src/assets/index.ts`
3. Use in any sandbox app via `import { imgName } from "@yz-ds"`

**What goes in ui-v2 assets vs stays in the app:**
- ✅ ui-v2: real Yardzen project photos used across multiple apps (looks, before/afters, hero shots)
- ❌ stays in app: shop-specific category heroes, product images, collection covers — anything that only makes sense in one app
