# Fawnroad — Project Guide

Part of the Casa Soda skill set. Load alongside `/soda-front` for Dan's workflow, design principles, and communication style.

> **First time here?** Read `docs/ux-testing-bible.md` first — it has every user flow mapped out by persona with step-by-step test plans. Best way to understand what the app does.

---

## Stack

React 19, TypeScript 5.9, Vite 7, Wouter 3.7 (routing), Apollo Client 3.12, Hono 4.11 (server), GraphQL 16, Drizzle ORM 0.45, AWS Aurora Data API, Tailwind CSS 4.1, CVA 0.7, Biome 2.3 (lint+format), Vitest 3.2, Playwright 1.50

**Node requirement:** >= 24.12.0, npm >= 11.6.0

---

## Dev Server — port 8888

```bash
cd apps/web
npm run dev              # foreground
npm run dev:start        # background daemon
npm run dev:status       # check if running + URL
npm run dev:stop         # stop
npm run dev:logs         # tail logs

# With public tunnel (Stripe webhooks, OAuth testing only)
TUNNEL=1 npm run dev:start
```

## First-Time Setup

```bash
npm run setup:dev        # from repo root or apps/web
# After first login, grant yourself super admin:
node .opencode/skills/local-db/scripts/set-super-admin.mjs you@example.com
```

## All Commands (from `apps/web/`)

```bash
npm run lint             # Biome format + check (writes)
npm run lint:tsc         # TypeScript check
npm run format           # Biome format only
npm run graphql:codegen  # Regenerate types after schema change
npm run db:generate      # Generate migration from schema changes
npm run db:migrate       # Apply migrations
npm run test:backend     # Backend/resolver tests
npm run test:frontend    # Component tests
npm run test:watch       # Watch mode
```

---

## Project Structure (`apps/web/src/`)

```
app/                    # App wiring (providers, router, layouts)
features/               # Domain modules — self-contained, never import each other
  auth/                 # Magic link flow
  home/                 # Home feed (/h)
  messaging/            # Direct messages
  profile/              # User profiles (/p/*)
  supporter/            # Supporter dashboard
  admin/group/          # Group admin
  admin/platform/       # Platform admin (/a/*)
shared/
  ui/                   # Design system (barrel-exported from shared/ui/index.ts)
  hooks/                # useAuth, useRouting, etc.
  lib/routes.ts         # ALL route helpers as typed factory functions
db/schema/              # Drizzle schema (modular by domain)
graphql/
  schema.graphql        # Single source of truth (~109 types)
  resolvers/            # Function-based resolvers by domain
  generated/            # Auto-generated — never edit manually
server/app/             # Hono server (index.tsx, services/)
```

**Import aliases:**
```ts
@/*         → ./src/*
@app/*      → ./src/app/*
@features/* → ./src/features/*
@shared/*   → ./src/shared/*
```

---

## Design System — always import from barrel

```ts
import { Button, Card, Typography, Input, Badge, EmptyState } from '@/shared/ui';
// NEVER: import { Button } from '@/shared/ui/Button/Button'
```

**Full component list:** Alert, Badge, Button (polymorphic, variants: primary/secondary/danger/ghost), Card/CardHeader/CardContent/CardFooter/CardTitle/CardDescription/CardAction (variants: default/outlined/shadowed), Checkbox, ColorPicker, ConfirmDialog, DataTable, Drawer, Dropdown, EmptyState, ErrorBoundary, FawnroadEditor, Footer/Header, GroupAvatar/UserAvatar, Input/Select/Textarea, LoadingBar/LoadingSpinner, MediaRenderer/MediaUpload, MemberAccessGate, Modal, PageLoader, Popover, Skeleton (PageSkeleton/SkeletonCard/SkeletonLine/SkeletonTable/SkeletonAvatar/SkeletonButton), StatCard, Tabs, Typography

**Typography component:**
- Variants: `display1`, `display2`, `h1`–`h6`, `body1`, `body2`, `caption`, `legend`
- Colors: `primary`, `secondary`, `muted`, `inherit`
- Font family: `sans` | `mono` — always explicit, **never auto-resolved from variant**
- `uppercase` — boolean prop, **never a default**
- Always include a space before `className=` — `variant='h1' className=` not `variant='h1'className=`

**Component patterns:**
- CVA for all variant-based components
- Polymorphic `as` prop on Button and Typography
- `import { clsx as cn } from 'clsx'` for class merging
- `export function ComponentName` — named exports, no arrow functions at module level
- `interface XxxProps` for prop types — never `type`
- `import type` for all type-only imports

### New Design System Components (April 2026)

Added to `shared/ui/` for the quiz-style application flow. Use them in any multi-step form or onboarding:

| Component | Path | What it does |
|-----------|------|-------------|
| `SelectionCard` | `shared/ui/SelectionCard/` | Clickable card with icon + title + description. Selected state has yellow tint + ring. CVA-based. Use for single-select card grids (org type, tier picker, etc.) |
| `ChipSelector` | `shared/ui/ChipSelector/` | Pill/tag grid for single or multi-select. Use for category pickers, tag selectors. |
| `InfoBox` | `shared/ui/InfoBox/` | Gray rounded box for helper text, requirements lists, disclaimers. |
| `QuizLayout` | `shared/ui/QuizLayout/` | Two-column layout: white left panel (sticky headline + step counter) + gray right panel (form content). Bottom nav bar with back arrow, progress bar, continue button. Supports overlay prop for modals. GoFundMe-inspired. |

All exported from `shared/ui/index.ts`.

---

## Routing (Wouter)

- All routes defined as factory functions in `shared/lib/routes.ts` — always use these, never hardcode strings
- Route guards: `NeedsAuth` (redirects to `/o/login`), `NeedsAdmin`, `NotInProduction`
- All major route groups are `React.lazy()` loaded

**Route segments:**

| Segment | What | Auth |
|---|---|---|
| `/h` | Home feed | NeedsAuth |
| `/o/*` | Auth (login, verify, logout) | Public |
| `/p/*` | Supporter/personal | NeedsAuth |
| `/a/*` | Platform admin | NeedsAdmin |
| `/d/*` | Dev tools / component viewer | Non-prod only |
| `/u/:username` | User profile | Public |
| `/:groupSlug/*` | Group pages (catch-all, must be last) | Mixed |

---

## GraphQL — exclusive data layer (no REST for mutations)

```ts
import { useQuery, useMutation } from '@apollo/client';
// Queries in feature api/ files or graphql/documents/
// Run codegen after any schema change: npm run graphql:codegen
```
- `@auth` directive — requires authenticated user
- `@requiresRole(role: ADMIN)` — role-based access
- Resolver pattern: `const { user, helpers } = getContext(_ctx)` — always destructure first

## Database

- Drizzle ORM, AWS Aurora Data API — ALL environments (no local Postgres)
- Primary keys: nanoid strings — not auto-increment integers
- Types: `InferSelectModel<typeof table>` / `InferInsertModel<typeof table>`
- DB is read-only by default — state changes via browser UI or GraphQL mutations, never direct SQL
- Migrations: `npm run db:generate` then `npm run db:migrate` — never write migration SQL manually

## Auth — magic link only

1. `/o/login` → `requestMagicLink` mutation
2. User clicks link → `/o/verify?email=...&code=...` → `verifyMagicLink`
3. Session cookie set, redirect to original path
- In dev: login form shows "Continue as [random user]" button that auto-navigates the magic link
- Auth state in `FawnroadContext` — access via `useAuth()` hook

### Login for testing

```bash
# Get a magic link code in dev
curl -s -X POST http://localhost:8888/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation { requestMagicLink(input: { email: \"hola@casasoda.com\", path: \"/h\" }) { magicCode } }"}'

# Then navigate to:
# http://localhost:8888/oauth/verify?email=hola@casasoda.com&code=<CODE>&path=/h
```

### Super admin

```bash
# Grant via Aurora Data API (env vars from apps/web/.env.default)
# 1. Get user ID
aws rds-data execute-statement --resource-arn "$RESOURCE_ARN" --secret-arn "$SECRET_ARN" --database "$DB_NAME" --sql "SELECT id FROM users WHERE email = 'hola@casasoda.com'" --region us-east-1

# 2. Insert role
aws rds-data execute-statement --resource-arn "$RESOURCE_ARN" --secret-arn "$SECRET_ARN" --database "$DB_NAME" --region us-east-1 --sql "INSERT INTO user_roles (id, \"userId\", role, \"createdAt\", \"updatedAt\") VALUES ('$(openssl rand -hex 11)', '<USER_ID>', 'SUPER_ADMIN', NOW(), NOW()) ON CONFLICT DO NOTHING"
```

---

## Styling

- Tailwind CSS 4 — semantic classes only, never raw hex colors or Tailwind gray utilities
- Primary display font: `font-mono` (Geist Mono) — for headings, buttons, badges
- Design tokens (CSS custom properties): `--color-surface`, `--color-text-primary`, `--color-border`, `--color-accent` (#f4ea60 yellow), `--color-accent-cta` (#c1d8ec blue)
- Brand palette: yellow `#f4ea60`, blue `#c1d8ec`, lime `#c0dc6a`, orange `#e66e34`
- Body: white (`bg-white`), black text — no dark mode

### The `fr-*` class system — mandatory

Fawnroad has global CSS classes in `styles.css` prefixed `fr-`. Use them instead of repeating Tailwind chains. Key classes: `fr-label` (bold uppercase mono black), `fr-input` (clean border + focus), `fr-input-error`, `fr-body`, `fr-body-muted`, `fr-headline`, `fr-error`, `fr-info`, `fr-step-counter`, `fr-review-label`, `fr-review-value`, `fr-btn`, `fr-btn-primary`, `fr-btn-secondary`. **Never write a raw Tailwind chain when an `fr-*` class exists for it.**

### Fawnroad-specific visual rules

- **Never use gray/muted labels.** Labels, field names, and table headers must be bold uppercase mono black (`font-semibold uppercase font-mono text-black`). No gray-ish faded labels — ever.
- **Never hardcode color hex values.** Always use the Fawnroad brand palette from CSS vars (`--fawnroad-yellow`, `--fawnroad-blue`, `--fawnroad-lime`, `--fawnroad-purple`, `--fawnroad-orange`, `--fawnroad-green`, `--fawnroad-red`, `--fawnroad-brown`). When you need a tint/pastel version, derive it from the brand color. In JS/TSX components, reference the constants — never invent new colors.
- **Don't use `focus:ring-*` on form inputs.** Fawnroad has a global `*:focus-visible` rule that adds a 2px gray outline. Use `outline-none focus-visible:outline-none ring-0 focus:ring-0 focus:border-black` to get a clean single-border focus state.

### Card rules

- Three variants: default (white), outlined, shadowed — no solid black border variant
- Empty states: use `EmptyState` component with emoji icon, title, description, optional CTA action
- Empty states get emojis — "make them feel as alive as possible"

### Global visual rules

- All borders 1px — no exceptions
- No black solid borders on cards or containers (`border-border` or `border-border-secondary` only)
- 1px borders: `border border-border` or `border-border-secondary`

---

## Test Mode Lifecycle

When creating a feature branch, enable test mode (`localStorage.setItem('fawnroad-test-mode', 'true')`) so forms prefill with edge-case data for fast QA. Before creating a PR, disable it (`localStorage.setItem('fawnroad-test-mode', 'false')`) and ensure the default is opt-in only. Test mode code stays in the build (dev-only via `import.meta.env.DEV`) but must never auto-enable in production or by default.

---

## PR Workflow

- Draft PRs for work-in-progress
- Include testing plan in every PR
- Document merge order when PRs have dependencies

---

## Repo Skills (`.opencode/skills/`, also at `.claude/skills/`)

- `frontend-conventions` — full architecture guide, component patterns, import rules
- `graphql-policy` — GraphQL-only mutation policy
- `dev-server` — start/stop/restart commands
- `local-db` — read-only DB access
- `magic-link-auth` — local and staging auth flows
- `seed` — generate test groups/tiers/posts/polls
- `git-conventions` — branch naming, commit format
- `targeted-testing` — TDD process, test naming
- `deploy` — deployment pipeline (develop → staging, v* tags → production)
- `onboard` — first-time setup and health check

## Key Files to Read First

1. `shared/lib/routes.ts` — every route as typed factory functions
2. `app/router/routes.tsx` — full Wouter route tree with guards
3. `graphql/schema.graphql` — entire GraphQL contract
4. `styles.css` — design tokens, CSS variables
5. `shared/ui/index.ts` — full design system component catalog
6. `shared/ui/Button/Button.tsx` — canonical CVA + polymorphic pattern
7. `app/providers/FawnroadContext.tsx` — global auth/SSR state
8. `db/schema.ts` — all DB table re-exports
9. `.opencode/skills/frontend-conventions/skill.md` — most comprehensive coding guide
10. `.opencode/skills/graphql-policy/skill.md` — data fetching rules
11. `docs/ux-testing-bible.md` — all user flows by persona, step-by-step test plans

## Target Audiences (full list in `docs/ux-testing-bible.md`)

- Groups that outgrew Facebook (neighborhood clubs, parent co-ops, Buy Nothing groups)
- Groups that collect money but hate their tools (tenant associations, youth sports, community gardens, maker spaces)
- Activist / advocacy orgs (mutual aid, tenant unions, immigrant defense, environmental justice, harm reduction)
- Faith & cultural (small congregations, cultural preservation, diaspora orgs)
- Creative & professional (journalism collectives, zine distros, DIY music venues, freelancer co-ops)
- Solo operators (tutors, personal trainers, community educators, doulas)

---

## Active Work Context (April 2026)

### UX Testing Bible

`docs/ux-testing-bible.md` — the team-wide source of truth for all user flows. 6 personas (P1–P6), 10 end-to-end flows with step-by-step test tables. Any team member can follow a flow to test the app. Update this file when flows change.

### User Story Specs

Jorge wrote 18 product specs in `docs/specs/*/user-stories.md`. They are organized by feature, not by user flow. The 15 key product areas:

| # | Story | Spec folder |
|---|-------|-------------|
| 1 | Group Public Page | `group-public-page` |
| 2 | Group Navigation & Redesign | `group-redesign` |
| 3 | Group Posts & Broadcasts | `group-posts`, `group-broadcasts`, `broadcast-image-upload` |
| 4 | Group Events & Ticketing | `group-events` |
| 5 | Group Polls | `group-polls` |
| 6 | Group File Manager | `group-file-manager` |
| 7 | Group Email & Mailing Lists | `group-email-archive` |
| 8 | Messaging (DMs) | `messaging-system` |
| 9 | Notifications & Digests | `notifications` |
| 10 | Tiers & Checkout | `tier-system-rework`, `admin-tier` |
| 11 | User Profile & Avatar | `user-avatar`, `sc-1273-profile-settings` |
| 12 | Admin Dashboard & Platform Admin | (permissions in `permissions-matrix.md`) |
| 13 | Billing & Payments | `sc-1291-billing-advance` |
| 14 | App Polish & Beta-Ready | `beta-test-ready` |
| 15 | UX Audit & Production Readiness | `ux-audit`, `production-readiness` |

### Application Flow Refactor (In Progress — branch `danpliego/apply-quiz-stepper`)

The group application form (`/j/form`) is being rebuilt from a single giant form into a Duolingo/GoFundMe-style quiz stepper:

- **Route:** `/j/form` — no longer requires auth (removed `NeedsAuth` wrapper)
- **Layout:** `QuizLayout` — two-column, left sticky headline, right form content
- **Steps:** 7 steps (name → description → org type → nonprofit details [conditional] → website → fiscal sponsorship → review + terms)
- **Auth:** happens at the END via inline modal overlay — not a redirect. User fills everything first, then signs in/up to submit.
- **Backend:** unchanged — same `submitMembershipGroupApplication` GraphQL mutation, same fields
- **File:** `src/features/public/routes/ApplyFormRoute.tsx`

### How to Work on User Flows

Dan's process for tackling flows:
1. Pick a flow from the UX Testing Bible
2. Dan provides an audio transcript scoping the work
3. Create a branch: `danpliego/<flow-slug>`
4. Read the relevant spec(s) in `docs/specs/`
5. Build frontend only — no backend/schema changes without Dan's approval
6. Use existing design system components (`Button`, `Card`, `Typography`, `SelectionCard`, `QuizLayout`, etc.)
7. Screenshot each state with Playwright, upload to files.fwnrd.net
8. One flow at a time, finish completely before starting the next

### Branch Naming for Flows

- `danpliego/apply-quiz-stepper` — Flow 1 (organizer application)
- Pattern: `danpliego/<flow-name>`
