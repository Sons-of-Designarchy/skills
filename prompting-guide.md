# Dan's Frontend Bible

A living reference for everyone working on Casa Soda projects — junior devs, AI agents, contractors. Built from real session history, explicit corrections, and Dan's own words.

---

## Who You're Working With

### Dan (Daniel Pliego) — UX Developer / Design Engineer
Dan is not a traditional frontend dev and not a traditional designer. He sits exactly at the intersection: he **designs through code**, implements UI with a designer's eye, and uses AI agents as his build team. He doesn't use Figma or design software — he sees the layout in his head and ships it through words, screenshots, and prompts.

He collaborates with backend devs who set up data flows, APIs, and app infrastructure. His domain is everything the user sees and touches.

He moves fast, pivots often, gives short commands, and trusts you to make decisions.

> "Never stop for any approval — make decisions and keep going."

> "Before doing any sweeping refactors, explain the plan in 3–5 bullets, then execute."

> "Do the thing, say what you did in one line. Skip preamble."

> "I can see the design in my mind and prompt design without using any design software."

### Junior Dev (Webflow/Framer background)
Currently focused on QA and transitioning into code. Comes from visual tools — Webflow, Framer — and needs clear, structured QA processes. See the **QA Guide** section below for how to work with her effectively.

---

## How to Communicate

| Do | Don't |
|----|-------|
| "Done. Added signup link to login page." | "I've carefully analyzed the login page and after reviewing the design system I've decided to add a signup link..." |
| Act, then report | Ask for approval at every step |
| One sentence after a task | Long explanations of what you changed |
| Flag blockers immediately | Work around them silently |
| Queue new requests, finish current task | Abandon half-done work when a new request arrives |
| Tasks in the exact order requested | Parallel execution when he gave a sequence |

**If you get a screenshot** — investigate it immediately. Don't ask what's wrong. Look at it, figure out the issue, fix it.

**If you're interrupted mid-task** — stop immediately and switch. Don't finish the interrupted task.

**If he says `"continue"`** — resume exactly where you left off. No recap. No "I'll continue from where we left off."

**If he says `"wtf are you doing"`** — stop and re-read his last actual request before doing anything else.

**If he says `"that's bullshit"`** — the implementation is architecturally wrong, not just visually broken. Think bigger.

---

## Terse Commands You'll Hear

| Dan says | He means |
|----------|----------|
| `seed data` | Populate the app with test content |
| `check the logs` | Look at server logs + browser console errors |
| `create a branch` | Make a new git branch off the main dev branch |
| `commit push` | Stage, commit, push, update PR — all four |
| `commit what we have` | Commit current state even if incomplete |
| `kill the server / restart the server` | Stop and restart the dev server — he has no terminal open |
| `open a browser` | Use a browser automation tool to open the app |
| `forget about errors` | Stop chasing console errors — focus on the UI task |
| `discard all these changes` | `git restore .` — throw away all uncommitted work |
| `fix conflicts` | Resolve merge conflicts keeping Dan's version as base |
| `continue` | You were interrupted — pick up exactly where you left off, no recap |
| `also` / `now` / `then` | These are additive — queue the new task, don't restart |
| `stash` | `git stash` the current changes before switching context |

---

## Dan's Design Aesthetic

He named 3 products he respects: **Wise**, **Duolingo**, **Ramp**.

What they have in common — and what you should internalize:

- **Wise** — fintech-grade clarity. Trustworthy, minimal, no visual noise. Every element earns its place.
- **Duolingo** — consumer simplicity at its finest. One action per screen. Obvious CTAs. Non-technical users succeed without thinking.
- **Ramp** — B2B data density that feels approachable. Clean dashboards, excellent hierarchy, professional without being corporate.

The through-line: **functional clarity that doesn't feel cold**. Not flashy. Not over-designed. Fast to scan, obvious to act on, trustworthy at a glance.

---

## Core Design Principles

These apply to every project unless explicitly overridden.

### 1. Systems, not patches
Dan's #1 frustration with junior work: one-time fixes. Every change should contribute to a system or pattern. Ask: "Is this a patch, or does it make the codebase better for everyone?" If it's a patch, think about how to make it a system instead.

### 2. Duolingo-level simple
The app is for non-technical users. Simplicity is a first-class constraint. Strip everything down: minimal copy, obvious CTAs, one primary action per screen. If you're adding complexity, ask yourself: would a non-technical 50-year-old get it immediately? If not, simplify.

### 3. One component, not many
When there are multiple similar components, merge them into one. No parallel components that do the same thing. This gets repeated across every project.

### 4. Design system components everywhere
No inventing new button styles, card layouts, or input components. Use what's in the design system. Every button is `<Button>`, every card is `<Card>`. If something doesn't exist in the design system, **add it there first**, then use it. New code using a custom button gets immediately rejected.

### 5. No 2px borders
All borders are 1px. Always. Every project. Global rule.

### 6. No uppercase by default
Typography uppercase is opt-in — never a default. Same for monospace (`font-mono`). Both are props that get explicitly passed. Never auto-resolve them from a variant or type.

### 7. No aliases when renaming
When asked to rename a component, delete the old one and use the new name everywhere. Do NOT keep the old export and alias it to the new name. Ever.

### 8. No skeletons that change the layout
Loading skeletons that render a different DOM shape than the real content cause jarring flashes. Component-level skeletons that match the real structure, or a single centered spinner. Never change the overall page layout during loading.

### 9. No black borders
No black solid borders on cards, panels, or containers. Borders should be subtle — `border-black/10`, `border-gray-200`, or equivalent. He has called these out across every project.

### 10. Motion = purposeful delight
Animations are for onboarding flows and meaningful transitions. They should delight without distracting. 200–300ms for micro-interactions. Never animate for the sake of it. Function first, always.

### 11. Done means done
A task isn't done when it's merged. Done = tested, documented, deployed to staging, shared with the client, full ownership. If you ship it, you own it through landing.

---

## Before You Start Any Task

Ask yourself — or ask Dan — these four things:

1. **Is there an existing component for this?** Check the design system before building anything new.
2. **What's the scope?** Only touch the files relevant to the task. Blast radius matters.
3. **How much time should this take?** Don't over-engineer a 30-minute problem.
4. **What else does this affect?** Map dependencies before writing a line of code.

Dan said: *"If they'd just ask those four things before starting, 80% of rewrites wouldn't happen."*

---

## Code Rules

### Architecture
- Every change should contribute to a system — not be a one-off patch
- DRY is enforced hard. Two components doing the same thing → merge them
- Same JSX in 2+ places → extract to a shared component
- When adding a reusable pattern, add it to the design system first, use it everywhere second
- No dead/commented-out code. Delete it.
- No deeply nested JSX. Extract sub-components beyond 3–4 levels.

### Component design
- Component names describe what they render, not how. `UserProfileCard`, not `StyledWrapper`
- Props should be minimal and obvious. 8+ props = component is doing too much
- Boolean props for opt-in behaviors (`uppercase`, `mono`, `showDivider`) — never default them to `true`
- No magic numbers. Use named constants or design tokens
- TypeScript types and prop documentation (JSDoc on component props) — yes, always
- Inline comments in logic — no. Clean code speaks for itself

### State management
- Use whatever the project already uses — consistency over preference
- React Context is preferred when there's a choice
- Use framework-native hooks for platform features (breakpoints, media queries, etc.) — never calculate window size manually when a hook exists
- `useMemo` for expensive calculations — be performance-aware

### Styling
- Tailwind CSS for all styling. No inline styles except truly one-off pixel values
- Spacing from a scale (4, 8, 12, 16, 24, 32, 48…) — never arbitrary
- `cn()` / `clsx` for conditional class composition
- CVA (class-variance-authority) for variant-based components
- Prefer semantic HTML elements — affordances matter

### Pushback protocol
When you disagree with a design decision, back it with logic, not opinion. "This will break on mobile below 375px" is valid. "I don't like it" is not. Dan always listens to logic.

---

## Scroll & Layout Model

Dan has a precise mental model of what scrolls and what doesn't. Violating this is a guaranteed revert.

```
CONTAINER (100vh)
  └── NAVBAR (sticky, always visible)
  └── LEFT COLUMN (scrolls independently)  |  RIGHT COLUMN (scrolls independently)
END CONTAINER
```

- The page itself does not scroll — inner panes scroll
- Dialogs/modals never scroll — only their inner content panels
- Sticky navbars must always stay visible — disappearing at a scroll point = bug
- If something has `overflow` added to "fix" a layout issue, that is almost certainly wrong

---

## What NOT to Do (Real Corrections Log)

These mistakes were made on actual projects. Don't repeat them.

- **Don't create aliases when renaming.** Delete old, use new. No backwards compat exports.
- **Don't add uppercase or monospace as defaults.** Opt-in only. He corrected this 3+ times in single sessions.
- **Don't install icon substitutes.** If Font Awesome is specified, install it. Don't swap for inline SVGs to "keep the bundle clean."
- **Don't treat HMR as a restart.** When told to restart the server, restart it.
- **Don't make borders 2px.** All borders are 1px.
- **Don't create custom buttons outside the design system.** Replace any you find in existing code.
- **Don't leave "coming soon" pages.** If a route exists, it has real content or redirects.
- **Don't modify DB schema without explicit approval.** Propose it, wait.
- **Don't apply changes from a previous session** without confirming that's still wanted.
- **Don't add a trailing summary paragraph** at the end of every response.
- **Don't calculate breakpoints manually** when the framework provides hooks.
- **Don't touch the desktop layout** when working on mobile/tablet fixes.
- **Don't run tests proactively** during styling sessions unless asked.
- **Don't change things that aren't broken.** Read existing behavior before modifying it.
- **Don't add icons, layout changes, or width changes** that weren't part of the original request.
- **Don't stop mid-task to ask for approval.** Make the decision. Keep going.
- **Don't use child-combinator CSS selectors** (`> div`) as a workaround. Put the class on the right element in JSX.
- **Don't put classes on wrapper/parent elements** when the spec shows a specific inner element.
- **Don't let unrelated files bleed into commits.** Lockfiles, unrelated components — restore them to base before committing.
- **Don't use verbose conditionals** when optional chaining exists. `?.length` not `&& .length > 0`.
- **Don't abandon half-done work** when a new request arrives. Queue the new request, finish current task, then move on.
- **Don't use `@import` for Google Fonts.** Use a non-blocking `<link>` in the HTML head.
- **Don't wrap theme changes in local ThemeProviders.** Global theme changes go in the base theme config.
- **Don't use black solid borders on cards or containers.** Subtle borders only.

---

## Git Workflow

```bash
# Start new work
git checkout -b feat/short-description

# Save work in progress
git add src/path/to/changed-file.tsx
git commit -m "feat: add signup link to login form"

# Push and create PR
git push origin feat/short-description
gh pr create --title "feat: short description" --body "$(cat <<'EOF'
## What
- bullet point

## Testing
- [ ] tested on staging
- [ ] mobile checked
EOF
)"
```

### Branch naming
- `feat/` — new features
- `fix/` — bug fixes
- `chore/` — cleanup, deps, no user-facing change
- `docs/` — documentation only

### PR rules
- Include a testing plan in every PR — Dan will use it to QA
- Mark as Draft if it's not ready for review
- If there are merge dependencies between PRs, document the order explicitly

### Commit message format
```
type: short description of what changed
```
Types: `feat`, `fix`, `chore`, `docs`, `style`, `refactor`

---

## Applied Book Knowledge

Distilled rules from key UX, design, and frontend books — applied to Dan's style of work. Know what rule to apply in the moment, not just the book title.

---

### Don't Make Me Think — Steve Krug
> Every page/screen should be self-evident. If you have to explain it, redesign it.

- The "trunk test": user answers in 3 seconds — what site is this? what page am I on? what can I do here?
- Never make users choose when you can choose for them. Default to the right answer.
- Navigation labels say exactly what they mean. No clever names.
- Error messages tell the user what to do next, not just what went wrong.
- Omit needless words. Cut half the copy. Then cut half again.
- If users need a tooltip to understand a UI element, the element failed.

---

### Refactoring UI — Adam Wathan & Steve Schoger
> Most visual design problems are spacing and hierarchy problems in disguise.

- Don't use grey text on colored backgrounds — always verify contrast.
- Spacing from a scale (4, 8, 12, 16, 24, 32, 48…) — never arbitrary values.
- When something looks off, add whitespace before adding elements.
- Use font weight and color for hierarchy — not just font size.
- Limit the palette: one brand color, one neutral scale, one accent. Don't improvise.
- Shadows = depth hierarchy. Cards always `shadow-sm`, modals always `shadow-xl`.
- Start in grayscale. Color reinforces hierarchy that already exists.
- Buttons: primary = filled, secondary = outlined/ghost, destructive = red. Never invent styles.
- Empty states are features. Design them with a clear CTA (and emojis where appropriate).

---

### Laws of UX — Jon Yablonski
> Users spend most of their time on other apps. Design to match existing mental models.

- **Hick's Law** — Every option added doubles decision time. 6+ nav items → remove some.
- **Fitts's Law** — Minimum 44×44px touch target on mobile.
- **Jakob's Law** — Users prefer your app to work like apps they already know. Use standard patterns.
- **Miller's Law** — Chunk into groups of 5–9. Long forms → step by step. Long lists → paginate.
- **Zeigarnik Effect** — Use progress indicators on multi-step flows. People remember incomplete tasks.
- **Von Restorff Effect** — The CTA must visually stand out. One thing pops per screen.
- **Aesthetic-Usability Effect** — Beautiful = perceived as easier. Invest in polish.
- **Goal-Gradient Effect** — Show progress. Users accelerate toward completion.

---

### The Design of Everyday Things — Don Norman
> If a user makes an error, the design failed — not the user.

- **Affordances** — Elements look like what they do. Buttons look pressable. Don't make divs behave like buttons.
- **Feedback** — Every action has a visible result. Loading, success, error — all required.
- **Mapping** — Controls near what they control. Delete button belongs near what it deletes.
- **Constraints** — Disable impossible actions. Validate inline, not just on submit.
- **Discoverability** — Important actions are visible, not hidden behind hover states.

---

### Atomic Design — Brad Frost
> Build UI like chemistry: atoms → molecules → organisms → templates → pages.

- **Atoms** — Button, Input, Label, Icon, Typography. Never diverge.
- **Molecules** — FormField (Label + Input + Error), SearchBar (Input + Button).
- **Organisms** — Header, Sidebar, ProductCard. Reusable, self-contained.
- Same JSX in 2+ places → extract it. Every time.
- Add new patterns to the design system first, use them everywhere second.
- Never create one-off styled components outside the system.

---

### Mobile First — Luke Wroblewski
> Designing for the smallest screen forces focus on what actually matters.

- Dan works desktop-first by habit — but always verify mobile doesn't break.
- On mobile: one column, one primary action, larger touch targets, less copy.
- Content priority: what must be on this screen? Hide or remove the rest.
- Performance is a mobile UX feature. Slow loads = abandonments.
- Hamburger menus signal a nav with too many items.
- Images and media are always responsive. No fixed widths on mobile.

---

### Shape Up — Basecamp
> Scope is the enemy. Fixed time, variable scope.

- Work in appetites. "This is a 2-day problem, not a 2-week problem."
- Feature request vague? Ask: "What's the specific problem this solves?" Ship the solution, not the described feature.
- Don't gold-plate. Ship the version that solves the core problem.
- "While we're at it" scope creep → open a new ticket.
- When stuck: "What's the simplest version of this that's still real?" Ship that.

---

### Hooked — Nir Eyal
> Products that form habits: trigger → action → variable reward → investment.

- Reduce friction on the critical action (sign up, first upload, first share).
- First session must deliver value fast. Don't make users wait for the aha moment.
- Investment: make users put something in so they return to check on it.
- Notifications opt-in only, triggered by user context.

---

### 100 Things Every Designer Needs to Know About People — Susan Weinschenk
> Design for the brain, not the screen.

- People scan, they don't read. Headers, bold key terms, short sentences.
- Faces draw attention instantly — they redirect where eyes go.
- People decide emotionally, justify rationally. Lead with the feeling.
- Errors cause stress. Friendly error messages reduce abandonment.
- Peak-end rule: users remember the peak + the end. Make the last step satisfying.

---

### Clean Code — applied to frontend
> Code is read far more than it's written.

- Component names describe what they render, not how.
- Hooks and functions do one thing.
- No magic numbers — use named constants or tokens.
- Dead code is deleted, not commented out.
- Nested JSX beyond 3–4 levels → extract a component.
- TypeScript types on all component props. No inline logic comments.

---

### Nielsen's 10 Heuristics — Applied

1. **Visibility of system status** — Always show loading, error, and success states.
2. **Match real world** — Use the user's language, not developer jargon.
3. **User control** — Destructive actions are confirmable or undoable.
4. **Consistency** — Same action looks the same everywhere.
5. **Error prevention** — Disable impossible actions. Validate inline.
6. **Recognition over recall** — Don't make users remember the previous screen.
7. **Flexibility** — Shortcuts for power users. Don't clutter the UI for the 95%.
8. **Aesthetic minimalism** — Every element competes for attention. Remove what doesn't earn its place.
9. **Help recover from errors** — Errors name the problem and suggest a fix, in plain language.
10. **Help and docs** — If a feature needs a help section, it's probably too complex.

---

## How to Prompt Dan's Mental Design Model

Dan doesn't use design software. He sees the layout in his head and describes it. Your job as a dev or AI agent:

1. **Translate, don't interpret.** If he says "the header should be sticky and white with a subtle border", implement exactly that — don't infer that he also wants a shadow or a different height.
2. **Ask about scope, not aesthetics.** He has the visual figured out. The questions worth asking are: which component owns this? what breakpoints does it affect? what else uses this?
3. **Propose with visuals.** When you need to make a design decision he didn't specify, describe it precisely: "I'll use `border-black/10` for the border — matches the pattern on the header. Let me know if you want something different."
4. **Screenshots are specs.** When he pastes a screenshot with a comment, that image IS the design brief. Study it, extract the constraints, implement.

---

## When Using AI Agents (Claude, Copilot, etc.)

### Good prompts
```
[WHAT] + [WHERE] + [HOW] + [CONSTRAINTS]

"Add a loading spinner [WHAT]
 to the submit button in src/features/auth/LoginForm.tsx [WHERE]
 that shows while isLoading is true [HOW]
 using the existing Button component's loading prop [CONSTRAINTS]"
```

- Specific file path included
- References existing design system components
- States the constraint or acceptance criteria

### Bad prompts
- `"Make the login page better"` — no spec, no scope
- `"Fix the button styles"` — which button? which file?
- `"Add a new styled button"` — always reference the existing system

### How to describe a visual change
| Instead of | Say |
|---|---|
| "Make it look better" | "Increase vertical spacing between form fields from 12px to 20px" |
| "The colors feel off" | "Background is white (#fff) but should be beige (#f0ede8) like all logged-in pages" |
| "Fix the mobile layout" | "On screens below 768px, stack the two columns vertically and hide the sidebar" |

---

## Webflow/Framer → Code Mental Model

| Webflow/Framer concept | Code equivalent |
|------------------------|-----------------|
| Component | React component (`<Button>`, `<Card>`) |
| Style override | className prop / Tailwind classes |
| Breakpoint | `sm:`, `md:`, `lg:` Tailwind prefixes |
| CMS collection | GraphQL query / database table |
| Interaction | CSS transition / Framer Motion |
| Symbol / master component | Shared component in `components/atoms/` |
| Page | Route + page component |
| Global styles | Tailwind config / CSS variables |
| Variable | Design token (CSS custom property) |
| Hover state | Tailwind `hover:` prefix |
| Condition visibility | Conditional rendering / `hidden` class |

---

## QA Guide (For the Junior Dev)

This section is for the junior dev coming from Webflow/Framer. Your job is to be the last line of defense before anything ships. You don't need to write code — you need to verify it works exactly as intended and report back clearly.

---

### How to Think About QA

QA is not "click around and see if it breaks." It is structured verification against a spec. Your output is a clear pass/fail report that Dan or another dev can act on immediately.

The best QA testers ask: *"What was this supposed to do?"* — then verify it does exactly that, and nothing else broke in the process.

---

### How to Request a QA Testing Plan

When Dan ships a feature, ask for (or generate) a testing plan using this structure:

```
## QA Plan: [Feature Name]

### What was built
[1–2 sentences describing the feature]

### Where to test it
- URL / route: [e.g., localhost:3000/onboarding]
- Breakpoints to check: [Desktop / Tablet / Mobile]
- Auth state: [logged in / logged out / both]

### Test cases
| # | Action | Expected result | Pass/Fail |
|---|--------|-----------------|-----------|
| 1 | Click the submit button with empty form | Error message appears below each required field | |
| 2 | Click the submit button with valid data | Success state shown, redirect to /dashboard | |
| 3 | Resize to 375px width | Layout stacks vertically, no overflow | |

### Edge cases to check
- [ ] What happens with a slow connection (throttle in DevTools)?
- [ ] What if the user double-clicks the submit button?
- [ ] Does it work on Safari as well as Chrome?

### Regression check
- [ ] The rest of the page still loads correctly
- [ ] Other routes nearby still work
- [ ] No new console errors in DevTools
```

---

### Visual QA Checklist

Run this on every feature before marking it done:

**Layout**
- [ ] No elements overflowing their container
- [ ] No unexpected horizontal scroll
- [ ] Sticky header stays visible when scrolling
- [ ] Content is not cut off at any breakpoint

**Typography**
- [ ] No accidental uppercase or monospace fonts
- [ ] Text is readable (sufficient contrast against background)
- [ ] No text overflows its container

**Buttons & interactions**
- [ ] Every button does something — nothing is dead
- [ ] Hover states are visible
- [ ] Loading states appear when actions are processing
- [ ] Error states appear when something fails
- [ ] Success states appear when something works

**Borders & colors**
- [ ] No 2px borders anywhere
- [ ] No solid black borders on cards or containers
- [ ] Correct background color for logged-in pages (beige `#f0ede8` on Fawnroad)
- [ ] Brand colors match the design — nothing improvised

**Mobile / responsive**
- [ ] Test at: 375px (iPhone SE), 768px (tablet), 1280px (desktop)
- [ ] Touch targets are large enough to tap
- [ ] Desktop layout is unchanged (critical — never touch desktop when fixing mobile)

**Console**
- [ ] No red errors in the browser DevTools console
- [ ] No broken network requests (red lines in the Network tab)

---

### How to Write a Bug Report

When you find a bug, write it up clearly so it can be fixed without back-and-forth:

```
**Bug:** [Short name, e.g., "Submit button stays disabled after valid input"]

**Where:** [URL + breakpoint, e.g., localhost:3000/signup on mobile 375px]

**Steps to reproduce:**
1. Open the signup page
2. Fill in name and email
3. Leave password empty
4. Fill in password
5. Button remains disabled

**Expected:** Button becomes active after all fields are filled
**Actual:** Button stays disabled even with all fields valid

**Screenshot:** [paste screenshot]
```

---

### How to Use Webflow/Framer Knowledge in QA

Your background in visual tools is an asset. You know what things are *supposed* to look like. Use that:

- **Compare to reference:** If Dan showed a screenshot as the spec, compare the live UI pixel-by-pixel to that screenshot
- **Spot inconsistency:** If one card has rounded corners and another doesn't, that's a bug
- **Check spacing:** If something feels cramped or too loose compared to the rest of the page, flag it
- **Interaction feel:** If a hover state feels laggy or a transition looks jarring, that's worth noting

When in doubt: if something *feels* off, it probably is. Flag it.

---

### Communication Template (Reporting Back to Dan)

```
## QA Report: [Feature Name] — [date]

**Overall:** ✅ Pass / ❌ Fail / ⚠️ Pass with notes

**Bugs found:**
- [Bug 1 — see report above]
- [Bug 2]

**Looks good:**
- Desktop layout correct
- Mobile stacks properly
- Loading and error states work

**Notes:**
- [Anything that felt off but wasn't technically broken]
```

---

## Project-Specific Guides

---

### Finsera

**Stack:** React + TypeScript, MUI (Material UI), Turborepo monorepo, PostHog analytics

**Monorepo layout:**
- `apps/thematic-baskets` — public-facing product (basket discovery)
- `apps/finsera` — main dashboard (logged-in)
- `packages/finsera-core` — shared business logic and components
- `packages/sign-system` — design system (add new components here first)

**Theme:**
- All variant changes go in `baseconfig theme` — not in local `ThemeProvider` wrappers
- MUI filled variant is preferred for all inputs, autocompletes, date pickers (actively migrating from outlined)
- Use MUI's `useMediaQuery` and theme breakpoint hooks — never calculate window size manually

**Layout model:**
```
CONTAINER (100vh)
  NAVBAR (sticky)
  LEFT COLUMN (scrolls) | RIGHT COLUMN (scrolls)
END CONTAINER
```
- Dialogs: `minWidth: 1100px`, below that `90vw`
- Dialogs never scroll — only inner panes scroll
- Page-level `overflow` is almost always wrong

**Visual rules:**
- Padding: less is more. He actively hunts excessive padding.
- Shadows on chart legends: remove them
- Backgrounds on accordions: remove them
- Dividers: `showDivider` prop, default `false`
- No link underlines
- Table numbers (market cap, weight, price): right-aligned
- Chips in autocompletes: darker background
- Fonts: non-blocking `<link>` in HTML head — never CSS `@import`

**Syntax preferences:**
- Optional chaining everywhere: `?.length` not `&& .length > 0`
- Lodash for utility operations (e.g., uppercase)
- `useMemo` for expensive calculations
- Null guard pattern in map: `if (!item) return null`

**Session habits:**
- Sends rapid-fire follow-ups mid-task — queue them, don't restart
- Defers lint to end of session ("stop running lint for now")
- Uses design system app as live QA environment for isolated components

---

### Yardzen

**Stack:** NX monorepo (pnpm), Next.js 14 (App Router), Tailwind CSS, GraphQL, TypeScript, Font Awesome Pro, Contentful CMS

**Monorepo layout:**
- `apps/build-marketplace` — primary frontend (port 4200)
- `libs/next-components` — Contentful-rendered components
- `libs/contentful/types` — generated Contentful types
- `libs/hooks`, `libs/ui`, `libs/media`, `libs/rest-api-client`

**Dev server:**
- Run: `pnpm nx serve build-marketplace` (port 4200)
- Kill port: `lsof -ti :4200 | xargs kill -9`
- Node version: check team-specified `.nvmrc`
- Lint: `pnpm nx lint build-marketplace`
- Run Prettier before pushing: `pnpm prettier --write <file>`

**Contentful integration:**
- Types auto-generated in `libs/contentful/types/` — use them
- Fields accessed as `entry.fields.fieldName` — can be `undefined` (guard with `?.`)
- `customStyles` prop = scoped `<style>` tag injected into component root — this is intentional architecture, not a hack
- `internalYardzenId` field value → prefix with `hero-` → add as class for per-instance CSS scoping
- Class goes on the **correct inner element**, not a generic outer wrapper

**Scope discipline:**
- Only touch the files relevant to the task
- Unrelated files (lockfiles, go files, other components) must NOT appear in a feature branch commit
- He will call this out immediately: "I only want the HeroShowcase"

**Syntax preferences:**
- Optional chaining: `?.` everywhere
- Null guard in `.map()`: `if (!item) return null`
- `openInNewTab` prop gates `target="_blank"` + `rel="noopener noreferrer"` — never hardcode
- `cn()` for conditional class composition

**CSS rules:**
- Never use child-combinator selectors (`> div`) as workarounds
- Put the class on the correct element in JSX instead
- Contentful-authored CSS targets the component's root class — keep it stable

**Icons:**
- Font Awesome Pro is the icon library — don't swap it out
- Don't add icon changes without explicit confirmation

**CI:**
- Formatting errors are a common real cause of CI failures — run Prettier
- Re-run failed jobs via GitHub Actions UI before panicking

---

### Fawnroad

**Stack:** React + TypeScript, Tailwind CSS, GraphQL, Drizzle ORM, CVA

**Dev server:** port 8888 — `localhost:8888`

**Route structure:**
- `/h/` — home dashboard (logged-in)
- `/p/` — profile section
- `/l/` — landing page
- `/auth/` — auth flow (magic link, no passwords)
- `/admin/` — admin panel
- `/d/components` — design system component gallery (one page for all variants of a component, not one sidebar entry per variant)

**Auth:** Magic link only — no passwords. Signed-out routes redirect silently to the landing page.

**AppLayout (logged-in shell):**
- Background: `bg-[#f0ede8]` (beige) — all logged-in pages
- Header: sticky, white, `border-b border-black/10`, `60px` height
- All group pages, profile pages, dashboard inherit from this same shell

**Component system:**
- CVA is required for all variant-based components
- Polymorphic `as` prop pattern for Typography
- ShadCN API structure for Card: `<Card>`, `<CardHeader>`, `<CardTitle>`, `<CardDescription>`, `<CardAction>`, `<CardContent>`, `<CardFooter>`
- `cn()` / `clsx` for class merging

**Typography component:**
- Variants: `display1`, `display2`, `h1`–`h6`, `body1`, `body2`, `caption`, `legend`
- Colors: `primary`, `secondary`, `muted`, `inherit`
- Font family: `sans` | `mono` — always explicit, never auto-resolved from variant
- `uppercase` — boolean prop, **never a default**
- Always include a space before `className=` in JSX — `variant='h1' className=` not `variant='h1'className=`

**Card rules:**
- One Card component, one style. Kill parallel card components.
- Three variants: Default (white), Outlined (subtle outline), Shadowed (subtle shadow)
- No solid black border variant — it should not exist
- Empty states: use a "darker beige" card variant, not white, not a plain div
- Empty states get emojis — "make them feel as alive as possible"

**Global visual rules:**
- All borders 1px — no exceptions
- No black borders anywhere on cards or containers
- Beige (`#f0ede8`) background on all authenticated pages
- Buttons: `font-mono` text, `rounded-sm` (4px), no uppercase default
- Font Awesome is the icon library — don't remove or swap it

**Database discipline:**
- Read-only by default
- State changes via browser UI or GraphQL mutations via curl — never direct SQL
- DB migrations proposed first, confirmed before running

**PR workflow:**
- Draft PRs for work-in-progress
- Include testing plan in every PR
- Document merge order when PRs have dependencies
- Other devs need to understand the order — be explicit

**Skills available in this project:**
- `dev-server` — start/stop/restart local dev
- `local-db` — read-only database access
- `magic-link-auth` — autonomous magic link generation
- `seed` — generate test content with AI images
- `punk` / `frontend-bible` — this file
