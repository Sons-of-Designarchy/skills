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

## Conventions

- No `@/` alias — use relative paths within the app; monorepo libs via `@yardzen/<lib>`
- Server components: async functions, no directive. Client components: `"use client"` as first line.
- Pattern: server component fetches → passes serializable props to client leaf
- Co-located: `queries.ts` (GQL), `actions.ts` (server actions), `classes.ts` (Tailwind strings)

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

## Typography for ALL text — no exceptions (yardzen-shop)

Every visible text node in `apps/design-sandbox/yardzen-shop` must use `<Typography>` from `@yz-ds`. No raw `<h1>`–`<h6>`, `<p>`, or `<span>` with inline font styles.

**Rules:**
- Font → `font="display"` (Arsenal) or `font="body"` (Geist). Never `fontFamily` in a `style` prop on Typography.
- Size → `variant` preset or `size` prop. Only use `fontSize` in `style` for clamp/fluid values with no preset equivalent.
- Color → `color` prop only (`"primary"`, `"secondary"`, `"muted"`, `"inherit"`, etc.). **Never a hardcoded hex, rgba, or CSS var on a Typography element.** No `const C = "..."` color constants — ever.
- For links with hover color changes: set `color` on the `<Link>` element, use `color="inherit"` on the `<Typography>` inside.
- Weight → `weight` prop. Never `fontWeight` in a `style` prop on Typography.

**Violations that get immediately rejected:**
```tsx
// ❌ raw element with inline styles
<h2 style={{ fontFamily: "var(--yz-font-display)", fontSize: 40, color: "#212121" }}>

// ❌ color constant anywhere in the file
const C = "#212121";

// ❌ fontFamily or color on a Typography style prop
<Typography style={{ fontFamily: "var(--yz-font-display)", color: "#212121" }}>

// ✅ correct
<Typography font="display" weight="normal" as="h2" style={{ fontSize: "clamp(40px, 5vw, 64px)", lineHeight: 1.08 }}>
<Typography color="secondary" variant="body-sm">
// ✅ correct hover pattern
<Link style={{ color: "var(--yz-color-text-secondary)" }} onMouseEnter={...}>
  <Typography color="inherit" variant="body-sm">link text</Typography>
</Link>
```

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

| App | Vercel project name | Primary URL | Local path |
|-----|---------------------|-------------|------------|
| lean-onboarding-v2 | `lean-onboarding-v2` | https://lean-onboarding-v2.vercel.app | `apps/design-sandbox/lean-onboarding-v2/` |
| yardzen-shop | `yardzen-shop` | https://yardzen-shop.vercel.app | `apps/design-sandbox/yardzen-shop/` |
| pros-landing | `yz-for-pros-landing` | https://yz-for-pros-landing.vercel.app | `apps/design-sandbox/pros-landing/` |
| toll-brothers-onboarding | `yz-toll-brothers` | https://yz-toll-brothers.vercel.app | `apps/design-sandbox/toll-brothers-onboarding/` |
| trend-report | `yz-trend-report-26` | https://yz-trend-report-26.vercel.app | `apps/design-sandbox/trend-report/` |
| trellis-v2 | (not yet linked) | — | `apps/design-sandbox/trellis-v2/` |

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

## Back Office (Next.js sandbox)

The back-office prototype is different from the other design sandbox apps: it's a **Next.js App Router** app inside the NX monorepo (mirrors eden's structure), uses **`@yardzen/ui` (Trellis from `libs/ui`)** for components, and is the proving ground for both Trellis components AND reusable page layouts (workstation shell, sidebar, role tabs, dashboards).

**Why it's not a Vite SPA like the others:** the goal is that pages built here can be copy-pasted directly back into eden with zero rewrite. Same framework, same imports, same conventions.

**Live:** https://yz-back-office.vercel.app
**Local path:** `apps/design-sandbox/back-office/`
**Dev port:** `4210`

### Run locally

```bash
nvm use 24
npx nx serve back-office
# → http://localhost:4210 (redirects to /back-office/design-studio)
```

If port 4210 is in use: `lsof -ti :4210 | xargs kill -9`.

### App structure

```
apps/design-sandbox/back-office/
├── app/
│   ├── layout.tsx             # root layout (fonts, no auth)
│   ├── ClientsideLayout.tsx   # YzThemeProvider + ToastProvider only
│   ├── global.css
│   ├── page.tsx               # → redirects to /back-office/design-studio
│   └── back-office/
│       ├── layout.tsx         # top bar + IconRail + RoleTabs + Sidebar
│       ├── page.tsx           # → redirects to design-studio dashboard
│       ├── _components/       # Chip, ScoreBar, KanbanBoard, DropZone,
│       │                      # RoleTabs, BackOfficeSidebar, IconRail,
│       │                      # Dashboard (shared dashboard layout)
│       ├── design-studio/     # dashboard + 5 leaf pages
│       ├── design-ops/        # dashboard + 5 leaf pages
│       ├── build-studio/      # dashboard + 4 leaf pages
│       └── build-ops/         # dashboard + 5 leaf pages
```

### Trellis discipline (the whole point of this app)

- **Always import from `@yardzen/ui`** (Trellis / `libs/ui`) — never `@yz-ds` / `libs/ui-v2` here.
- Same import path eden uses: `import { Button } from "@yardzen/ui/components/button"` etc.
- When you hit a Trellis gap (missing variant, missing token, inline hex like `#6E56CF`) — file a ticket against `libs/ui` rather than work around it. This app exists to surface those gaps.
- **Reusable layouts are first-class.** The `Dashboard` component in `_components/Dashboard.tsx` is the prototype for what eventually becomes a Trellis layout primitive. Same for `IconRail`, `RoleTabs`, `BackOfficeSidebar`. If you find yourself building the same shell twice, extract it.

### Deploy workflow

The back-office is a Next.js app, so deploys work differently from the Vite sandbox apps. We deploy a **static export** because all pages are SSG.

```bash
# 1. Build (Nx will produce dist/apps/design-sandbox/back-office/dist/.next/ as static HTML)
nvm use 24
npx nx build back-office --configuration=production

# 2. From the dist output, flatten and deploy
cd dist/apps/design-sandbox/back-office
mv dist/.next/* . && rm -rf dist
# Write vercel.json (see below) then:
vercel --yes --prod --scope danielpliego-4456s-projects
```

`vercel.json` in the dist folder:
```json
{
  "buildCommand": "",
  "installCommand": "",
  "outputDirectory": ".",
  "framework": null,
  "cleanUrls": true,
  "trailingSlash": true
}
```

Why this dance: Nx generates a bloated `package.json` (every monorepo dep) and a `pnpm-lock.yaml` that references private Yardzen FontAwesome packages — Vercel's `pnpm install` always fails on those. Static export bypasses install entirely.

### `next.config.js` settings that make this work

```js
const nextConfig = {
  nx: { svgr: false },
  distDir: "dist/.next",
  output: "export",        // required — produces static HTML
  trailingSlash: true,     // matches Vercel routing
  images: { unoptimized: true },  // required for static export
};
```

### Important: `redirect()` is NOT allowed in static export

Server-side `redirect()` from `next/navigation` throws at build time. Use client-side redirects instead:

```tsx
"use client";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function BackOfficePage() {
  const router = useRouter();
  useEffect(() => {
    router.replace("/back-office/design-studio/");
  }, [router]);
  return null;
}
```

### Routes

| Route | What |
|---|---|
| `/back-office/design-studio` | Designer dashboard |
| `/back-office/design-ops` | Delivery cockpit (Trello replacement) |
| `/back-office/build-studio` | Homeowner Rep workstation |
| `/back-office/build-ops` | Build operations cockpit |
| `/back-office/<workstation>/<page>` | Leaf pages (co-design, pipeline, etc.) |

### Source of truth

The back-office prototype follows the **New Back Office System Requirements** spec by Alicia Kim (June 15, 2026). 4 workstations, one project record, AI/manual mode toggle per deliverable, tier-based default mode set at assignment, CRH pull-through end-to-end. When in doubt about behavior, the spec wins.

---

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
