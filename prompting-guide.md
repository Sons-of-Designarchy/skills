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

### Junior Dev / QA (Framer + Webflow background)
Comes from visual tools — Framer and Webflow. Currently focused on QA. Short-term goal: learn to use CLI tools and vibe code prototypes. Doesn't need to write production code — needs to be able to spin up prototypes, run dev servers, and validate designs without Figma. See the **QA Guide** and **Designer → CLI Guide** sections below.

### Designer (transitioning to prompting)
Pure designer background. The goal for the next few weeks is to prompt effectively — describing design intent in words that an AI agent can act on directly. Doesn't need to touch code. Needs to communicate design with enough precision that the agent can execute without back-and-forth. See the **Designer → CLI Guide** section below.

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
- **Don't say "it's ready" without QA at all viewports.** Before presenting any UI work as done, screenshot it at desktop (1280×800), tablet (768×1024), and mobile (390×844). Walk through the full flow at each size. Check focus states, borders, overflow, touch targets. Fix everything before showing Dan. He should review design, not bugs.
- **Don't use `focus:ring-*` on form inputs.** Fawnroad has a global `*:focus-visible` rule that adds a 2px gray outline. Use `outline-none focus-visible:outline-none ring-0 focus:ring-0 focus:border-black` to get a clean single-border focus state.

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

## Designer → CLI Guide

This section is for designers transitioning from Figma/Framer/Webflow into the terminal + AI-agent workflow. The goal isn't to become a developer. The goal is to **stop being blocked by not having a dev** — to spin up prototypes, validate ideas, and ship design decisions independently.

---

### The Mental Shift

In Figma/Framer: you drag, click, and see results instantly.
In this workflow: you describe, and the agent builds. The tool is language, not a mouse.

The quality of what you get back = the quality of how you describe it.

This is not harder than design — it's just different. Your design vocabulary is your superpower here. You already know what things are called, what good looks like, and what's wrong. That's 80% of the skill.

---

### Track 1 — CLI + Vibe Coding (Junior Dev / QA)

**Goal:** Run dev servers, make small code changes with AI help, build throwaway prototypes to validate ideas before they go into production.

#### Terminal Basics (the only 10 commands you need)

```bash
# Navigate
ls                    # list files in current folder
cd folder-name        # go into a folder
cd ..                 # go up one level
pwd                   # show where you are right now

# Dev servers
npm run dev           # start the dev server (Fawnroad)
yarn start            # start the dev server (Finsera)
ctrl+C                # stop whatever is running

# Git basics
git status            # what changed?
git pull              # get latest from team

# When something breaks
rm -rf node_modules && npm install   # nuclear reset for dependencies
```

**Rule:** You don't need to understand everything. You need to recognize patterns. When you see an error in red, copy it and paste it to Claude. It knows what to do.

#### Vibe Coding Workflow

This is the loop for prototyping:

1. **Open Claude Code** in the project folder
2. **Load the skill:** `/soda-front`
3. **Describe what you want** — use the prompt structure below
4. **Watch it build** — don't interrupt unless it's clearly going wrong
5. **Open the browser** — check `localhost:3000` (or whatever port)
6. **Screenshot what's wrong** — paste into Claude, say "fix this"
7. **Repeat until it looks right**

You don't commit or push. Dan or another dev takes it from there.

#### How to Describe What You Want

```
"I want [WHAT] on [WHERE].
It should look like [REFERENCE or DESCRIPTION].
Use [COMPONENT or STYLE] if it exists.
Don't touch [WHAT TO LEAVE ALONE]."
```

**Examples:**

> "I want a card component on the home feed that shows a user avatar, their name, and a short bio. It should look like a Twitter/X profile card — minimal, no borders, just subtle shadow. Use the existing Card component. Don't touch the layout around it."

> "The spacing between the header and the first card feels too big. Reduce it by about half. Only change that gap, nothing else."

> "Add an empty state to this page. Use an emoji, a short title, and a button that says 'Get started'. Make it feel alive, not corporate."

#### What NOT to Ask the Agent to Do (as a prototype)

- Don't ask it to connect real data — use hardcoded dummy content for prototypes
- Don't ask it to add auth — skip it, just show the logged-in state
- Don't ask it to "make it production ready" — prototype first, polish later
- Don't ask it to change multiple screens at once — one component at a time

---

### Track 2 — Design Prompting (Designer)

**Goal:** Describe design decisions with enough precision that an AI agent (or a developer) can execute without asking follow-up questions.

The shift from Figma to prompting is this: instead of showing pixels, you describe intent.

#### The Precision Test

Before sending a prompt, ask yourself: if 3 different people read this, would they all build the same thing?

If no → add more specifics.

#### Prompt Formula

```
[COMPONENT or SCREEN] should [DO WHAT / LOOK LIKE WHAT].
[SPECIFIC visual detail: color, spacing, size, alignment].
[What it should feel like — emotional/brand tone].
[What to avoid].
[Reference — a product, a pattern, a screenshot].
```

**Weak prompt:**
> "The button should look better."

**Strong prompt:**
> "The primary CTA button should feel more confident. Increase the padding so it's wider — more Wise-style, less Bootstrap. Keep the existing color. The text should be slightly larger, not uppercase. It should feel like it deserves to be clicked."

**Weak prompt:**
> "The empty state looks sad."

**Strong prompt:**
> "The empty state needs to feel alive. Add a large emoji (pick something relevant to groups, like 👥 or ✨). Title in bold, one line max, friendly tone. A short subtitle — one sentence, lowercase, muted color. A primary CTA button below. The whole thing should feel like Duolingo — encouraging, not apologetic."

#### The 5 Things Designers Know That Make Prompts Better

1. **Name the component** — "the card", "the nav", "the input field" not "that thing"
2. **Name the state** — "on hover", "when loading", "when empty", "on mobile"
3. **Reference something real** — "like Wise", "like the card on the home page", "like the existing Button component"
4. **Specify what to leave alone** — "don't change the desktop layout, only mobile"
5. **Describe the feeling, not just the pixels** — "feels corporate → make it warmer" is a valid design note

#### Common Design Decisions → How to Prompt Them

| You notice | You say |
|---|---|
| Too much whitespace | "Reduce the vertical gap between X and Y by about half" |
| Color feels off | "The background should match the beige (#f0ede8) used on all other logged-in pages" |
| Text hierarchy broken | "The title should be bigger/bolder than the subtitle. Make the hierarchy more obvious" |
| Component looks inconsistent | "This button doesn't match the style of the other buttons on this page — align it" |
| Mobile layout broken | "On screens below 768px, stack these two columns vertically instead of side by side" |
| Animation feels wrong | "Remove the animation — it's distracting. Just show the content immediately" |
| Border looks too heavy | "Change the border to 1px, subtle — like `border-black/10`, not a solid black line" |

#### First Week Goals (Designer)

1. Load `/soda-front` in a Claude Code session and read through it
2. Pick one existing screen across any project and write a prompt to improve one thing
3. Share the prompt in the team channel — Dan gives feedback
4. Repeat until prompts get executed without clarifying questions

---

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

**Stack:** Turborepo (Yarn classic), React 19, TypeScript 5, MUI 7, Vite 7, Vitest, Redux + redux-thunk, amCharts 5, MUI X Data Grid Premium, lodash-es, PostHog, Sentry

**Monorepo layout:**
```
apps/
  finsera/            # Main dashboard SPA (Vite, client-only) — localhost:3000
  thematic-baskets/   # Public SSR app (React Router v7, SSR) — localhost:3002
  portfolios/         # localhost:3001
  design-system/      # Component QA gallery — localhost:3003
packages/
  finsera-core/       # @local/finsera-core — shared components, theme, API, types
```

**Dev workflow:**
```bash
# Setup
nvm use 20.19.3
yarn start            # runs all apps in parallel via Turborepo

# If it fails:
yarn                  # reinstall all packages

# Clean install (nuclear):
rm -rf .turbo apps/finsera/.turbo/ apps/portfolios/.turbo/ packages/finsera-core/.turbo/ packages/thematic-baskets/.turbo/
rm -rf node_modules apps/finsera/node_modules/ apps/portfolios/node_modules/ packages/finsera-core/node_modules/ packages/thematic-baskets/node_modules/
yarn

# Lint, type check, test
yarn lint
yarn tsc
yarn test:no-watch    # CI single-run
yarn format           # prettier --write
```

**Git workflow:**
- Base branch: `master`
- Always `git pull` before starting new work
- Branch names come from Shortcut — use the "copy branch" setting in Shortcut
- Use Finsera Chrome browser profile when working in Shortcut

**Environments:**
| Name | URL |
|---|---|
| localhost | `localhost:3002/` (thematic-baskets) |
| development | `https://themes.finseradev.net/` |
| staging | `https://themes.finserastg.net/` |
| production | `https://themes.finsera.com/` |

**Tools used:** Shortcut (tasks), GitLab (code hosting), Pitch (presentations), RB2B (tracking), PostHog (analytics)

**Meetings:**
- Monday 12pm — testing meeting + new feature demo

**Shared package — `@local/finsera-core`:**
```ts
import { ui, uitheme, hooks, helpers, enums, types, coreData } from '@local/finsera-core';
import { FinseraCoreProvider } from '@local/finsera-core';
```
- `ui.*` — all shared UI components (Button, Card, FinDataGrid, LineChart, PieChart, AssetSelector, etc.)
- `uitheme.blue` / `uitheme.green` — MUI theme objects
- `mui.core.*`, `mui.icons.*`, `mui.lab.*` — all MUI re-exports (never import from `@mui/material` directly)

**Theme:**
- Theme files: `packages/finsera-core/src/theme/`
- All MUI overrides → `base-config-theme.ts` — never in local `ThemeProvider` wrappers
- MUI spacing base: `4px` (so `theme.spacing(2) = 8px`)
- Custom breakpoints: `xs:0, sm:600, md:900, lg:1300, xl:1536`
- Design tokens in `layout-size.ts`: `FONT_SIZE`, `INPUT_SIZE`, `APP_BAR_HEIGHT (50px)`, `LEFT_DRAWER_WIDTH (270px)`, `SECTION_BG`, `Z_INDEX`
- Fonts: Libre Caslon Condensed (serif heading) + Inter (body), loaded via `fonts.css`
- MUI filled variant is preferred for all inputs, autocompletes, date pickers (migrating from outlined)
- Use `uitheme.blue` by default, `uitheme.green` for production mode
- Custom button variant added: `'light'`

**Import pattern in apps:**
```ts
// Everything comes from the _core barrel — never direct imports
import { mui, React, ts, ui, api } from '_core';
// baseUrl is "src" so all imports are from src/
import Layout from 'views/layout';
```

**Data fetching — REST only (no GraphQL):**
```ts
// SCRUD factory generates get/search/create/update/delete per resource
const basket = await api.baskets.get(id);
await api.baskets.update(id, data);
// thematic-baskets uses adminApi/usersApi for server-side loaders
const data = await adminApi(request.headers).baskets.search({ query: [...] });
```

**Auth:**
- `finsera` app: cookie `fauth`, session fetched on mount via `api.auth.getSession()`
- `thematic-baskets`: cookie `fauth` read in root middleware, role-based access via `checkAccessByRole()`
- Role hierarchy: `ANONYMOUS → FREE → PREMIUM → ADMIN`

**Routing:**
- `finsera`: React Router v7 as library in Vite SPA — `logged-in-router.tsx` + `logged-out-router.tsx`, all lazy-loaded
- `thematic-baskets`: React Router v7 SSR — config-based route table in `app/routes.ts`

**Layout model:**
```
CONTAINER (100vh)
  NAVBAR (sticky, always visible — APP_BAR_HEIGHT: 50px)
  LEFT COLUMN (scrolls) | RIGHT COLUMN (scrolls)
END CONTAINER
```
- Dialogs: `minWidth: 1100px`, below that `90vw`
- Dialogs never scroll — only inner panes scroll
- Page-level `overflow` is almost always wrong

**Key files to read first:**
1. `packages/finsera-core/src/index.ts` — everything exported from the shared library
2. `packages/finsera-core/src/theme/base-config-theme.ts` — all MUI overrides
3. `packages/finsera-core/src/theme/layout-size.ts` — all design tokens
4. `apps/finsera/src/_core/index.ts` — the import barrel
5. `apps/finsera/src/in-app.tsx` — auth boot, session fetch, router switching
6. `apps/thematic-baskets/app/routes.ts` — complete SSR route table
7. `apps/thematic-baskets/app/_helpers/server/with-access-control.ts` — role-based auth guard

**Visual rules:**
- Padding: less is more — he actively hunts excessive padding
- Shadows on chart legends: remove
- Backgrounds on accordions: remove
- Dividers: `showDivider` prop, default `false`
- No link underlines
- Table numbers (market cap, weight, price): right-aligned
- Chips in autocompletes: darker background
- Fonts loaded via `<link>` in HTML head — never CSS `@import`

**Syntax preferences:**
- Optional chaining everywhere: `?.length` not `&& .length > 0`
- Lodash (`lodash-es`) for utility operations
- `useMemo` for expensive calculations
- MUI breakpoint hooks — never calculate window size manually
- Null guard in map: `if (!item) return null`

---

### Yardzen

**Stack:** NX monorepo (pnpm), Next.js 15 (App Router), TypeScript strict, Tailwind CSS, GraphQL (Apollo codegen), Prisma + PostgreSQL, Contentful CMS, NextAuth v4 + custom V2 JWT auth, Split.io feature flags

**Dev setup:**
```bash
cd yardzen-app        # or wherever the monorepo is cloned
nvm use 24.0.0
git checkout dev && git pull    # base branch is dev (not main/master)
```

**Dev commands** (run from monorepo root):
```bash
# Run only build-marketplace (most common)
npx nx run-many --target=serve --projects=build-marketplace

# Run with API backend too
npx nx run-many --target=serve --projects=api,build-marketplace

# Run single app directly
nx serve build-marketplace                    # port 4200

nx build build-marketplace                    # production build
nx lint build-marketplace                     # lint
nx test build-marketplace                     # tests
nx run build-marketplace:graphql-codegen      # regenerate GQL types

# Always run before pushing:
pnpm run lint
```

**Git & PR workflow:**
- Base branch: **`dev`** (not `main` — that's a different branch)
- Always pull from `dev` before starting
- Open Jira ticket first, create branch from the ticket
- Run `pnpm run lint` before every push
- PR must include: title matching ticket name, bullet-point description of changes, before/after screenshots, local URL + which component to test
- Use the Yardzen Chrome browser profile for Claude and GitLab access

**Yard Capture (mobile app) setup:**
```bash
cd yardzen/mobile-apps/yardzen-capture
./start.sh            # loads QR code for the mobile app
```

**Route groups in `app/`:**
| Group | Paths | Purpose |
|---|---|---|
| `(default)` | `/login`, `/profile`, `/gallery`, `/build-studio`, `/payments/[invoiceId]` | Authenticated user flows |
| `(marketing)` | `/home`, `/packages`, `/[...slug]` | Public marketing, Contentful-driven |
| `(minimal)` | `/checkout`, `/checkout/extras` | Stripped shell, no main nav |
| `(quiz)` | `/design-consultation/[survey_id]/[[...slug]]` | Multi-step design quiz |

**Key files to read first:**
1. `middleware.ts` — auth gating, `PUBLIC_PATHS`, anonymous ID creation
2. `app/(default)/layout.tsx` + `ClientsideLayout.tsx` — full provider stack (Apollo, GTM, Split, Datadog)
3. `app/(default)/ServerContext.ts` — `getUserIdFromServerContext()` — canonical user getter in server components
4. `providers/V2Auth/serverSideV2Auth.ts` — dual-token (V1 Firebase / V2 JWT) auth chain
5. `app/(marketing)/packages/ContentfulPage.tsx` — Contentful section router (`isTypeXxx` chain)
6. `libs/contentful/utils/getEntry.ts` — caching, overrides, preview logic
7. `app/(default)/prisma.ts` — Prisma singleton
8. `codegen.ts` + `gql/apollo.ts` — generated GQL types imported everywhere

**Shared libs (most-used):**
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

**Auth:**
- Two systems coexist: V1 (Firebase JWT) and V2 (custom JWT, preferred)
- Server components: use `getUserIdFromServerContext()` or `getAuthedUserInfo()`
- If V2 token missing, auto-generated from V1 — no redirect
- Add new public routes to `PUBLIC_PATHS` in `middleware.ts`

**GraphQL:**
- Run codegen after any schema change: `nx run build-marketplace:graphql-codegen`
- Queries in co-located `queries.ts` files using `gql` tag
- Server-side: `fetchYzGqlApi<QueryType, VariablesType>({ query, variables })`
- Client-side: standard Apollo hooks from `gql/apollo.ts`
- Never write raw fetch calls — always use typed helpers

**Contentful integration:**
- Types in `libs/contentful/types/` — always use generated types
- Fields accessed as `entry.fields.fieldName` — guard with `?.` (can be `undefined`)
- `customStyles` prop = scoped `<style>` tag in component root — intentional architecture, not a hack
- `internalYardzenId` field → prefix with `hero-` → CSS class for per-instance scoping
- Class goes on the **correct inner element**, never a generic outer wrapper
- Section routing: `isTypeXxx(section) && <Component />` chain — no switch/case

**Styling:**
- Tailwind extends `libs/ui/src/tailwind.config.js`
- Fonts: `Arsenal` (serif) and `Roboto` via `next/font/google`
- Custom tokens: `action-main` (#1B6245), `typo-primary` (#323232), `texture-primary` (#F6F5F4)
- Run Prettier before pushing — formatting failures are the most common CI break

**Conventions:**
- No `@/` alias — use relative paths within the app; monorepo libs via `@yardzen/<lib>`
- Server components: async functions, no directive. Client components: `"use client"` as first line.
- Pattern: server component fetches → passes serializable props to client leaf
- Co-located: `queries.ts` (GQL), `actions.ts` (server actions), `classes.ts` (Tailwind strings)

**Scope discipline:**
- Only touch files relevant to the task
- Lockfiles, unrelated components, go files must NOT appear in a feature branch commit

**Icons:**
- Font Awesome Pro — don't swap it, don't add icon changes without explicit confirmation

**CI:**
- Formatting errors are the most common real cause of CI failures — run Prettier first
- Re-run failed jobs via GitHub Actions UI before diagnosing code issues

---

### Fawnroad

> **First time here?** Read `docs/ux-testing-bible.md` first — it has every user flow mapped out by persona with step-by-step test plans. Best way to understand what the app does.

**Stack:** React 19, TypeScript 5.9, Vite 7, Wouter 3.7 (routing), Apollo Client 3.12, Hono 4.11 (server), GraphQL 16, Drizzle ORM 0.45, AWS Aurora Data API, Tailwind CSS 4.1, CVA 0.7, Biome 2.3 (lint+format), Vitest 3.2, Playwright 1.50

**Node requirement:** >= 24.12.0, npm >= 11.6.0

**Dev server — port 8888:**
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

**First-time setup:**
```bash
npm run setup:dev        # from repo root or apps/web
# After first login, grant yourself super admin:
node .opencode/skills/local-db/scripts/set-super-admin.mjs you@example.com
```

**All commands from `apps/web/`:**
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

**Project structure (`apps/web/src/`):**
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

**Design system — always import from barrel:**
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

**Routing (Wouter):**
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

**GraphQL — exclusive data layer (no REST for mutations):**
```ts
import { useQuery, useMutation } from '@apollo/client';
// Queries in feature api/ files or graphql/documents/
// Run codegen after any schema change: npm run graphql:codegen
```
- `@auth` directive — requires authenticated user
- `@requiresRole(role: ADMIN)` — role-based access
- Resolver pattern: `const { user, helpers } = getContext(_ctx)` — always destructure first

**Database:**
- Drizzle ORM, AWS Aurora Data API — ALL environments (no local Postgres)
- Primary keys: nanoid strings — not auto-increment integers
- Types: `InferSelectModel<typeof table>` / `InferInsertModel<typeof table>`
- DB is read-only by default — state changes via browser UI or GraphQL mutations, never direct SQL
- Migrations: `npm run db:generate` then `npm run db:migrate` — never write migration SQL manually

**Auth — magic link only:**
1. `/o/login` → `requestMagicLink` mutation
2. User clicks link → `/o/verify?email=...&code=...` → `verifyMagicLink`
3. Session cookie set, redirect to original path
- In dev: login form shows "Continue as [random user]" button that auto-navigates the magic link
- Auth state in `FawnroadContext` — access via `useAuth()` hook

**Styling:**
- Tailwind CSS 4 — semantic classes only, never raw hex colors or Tailwind gray utilities
- Primary display font: `font-mono` (Geist Mono) — for headings, buttons, badges
- Design tokens (CSS custom properties): `--color-surface`, `--color-text-primary`, `--color-border`, `--color-accent` (#f4ea60 yellow), `--color-accent-cta` (#c1d8ec blue)
- Brand palette: yellow `#f4ea60`, blue `#c1d8ec`, lime `#c0dc6a`, orange `#e66e34`
- Body: white (`bg-white`), black text — no dark mode

**Card rules:**
- Three variants: default (white), outlined, shadowed — no solid black border variant
- Empty states: use `EmptyState` component with emoji icon, title, description, optional CTA action
- Empty states get emojis — "make them feel as alive as possible"

**Global visual rules:**
- All borders 1px — no exceptions
- No black solid borders on cards or containers (`border-border` or `border-border-secondary` only)
- 1px borders: `border border-border` or `border-border-secondary`

**PR workflow:**
- Draft PRs for work-in-progress
- Include testing plan in every PR
- Document merge order when PRs have dependencies

**Skills in `.opencode/skills/` (also at `.claude/skills/`):**
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

**Key files to read first:**
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

**New to the project?** Start by reading `docs/ux-testing-bible.md` — it maps every user journey (10 flows across 6 personas) with exact routes and expected behavior. It's the fastest way to understand what the app does and how to test it.

**Target audiences** (full list in `docs/ux-testing-bible.md`):
- Groups that outgrew Facebook (neighborhood clubs, parent co-ops, Buy Nothing groups)
- Groups that collect money but hate their tools (tenant associations, youth sports, community gardens, maker spaces)
- Activist / advocacy orgs (mutual aid, tenant unions, immigrant defense, environmental justice, harm reduction)
- Faith & cultural (small congregations, cultural preservation, diaspora orgs)
- Creative & professional (journalism collectives, zine distros, DIY music venues, freelancer co-ops)
- Solo operators (tutors, personal trainers, community educators, doulas)

---

### Fawnroad — Active Work Context (April 2026)

#### UX Testing Bible
`docs/ux-testing-bible.md` — the team-wide source of truth for all user flows. 6 personas (P1–P6), 10 end-to-end flows with step-by-step test tables. Any team member can follow a flow to test the app. Update this file when flows change.

#### User Story Specs
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

#### New Design System Components (April 2026)
These were added to `shared/ui/` for the quiz-style application flow. Use them in any multi-step form or onboarding:

| Component | Path | What it does |
|-----------|------|-------------|
| `SelectionCard` | `shared/ui/SelectionCard/` | Clickable card with icon + title + description. Selected state has yellow tint + ring. CVA-based. Use for single-select card grids (org type, tier picker, etc.) |
| `ChipSelector` | `shared/ui/ChipSelector/` | Pill/tag grid for single or multi-select. Use for category pickers, tag selectors. |
| `InfoBox` | `shared/ui/InfoBox/` | Gray rounded box for helper text, requirements lists, disclaimers. |
| `QuizLayout` | `shared/ui/QuizLayout/` | Two-column layout: white left panel (sticky headline + step counter) + gray right panel (form content). Bottom nav bar with back arrow, progress bar, continue button. Supports overlay prop for modals. GoFundMe-inspired. |

All exported from `shared/ui/index.ts`.

#### Application Flow Refactor (In Progress — branch `danpliego/apply-quiz-stepper`)
The group application form (`/j/form`) is being rebuilt from a single giant form into a Duolingo/GoFundMe-style quiz stepper:

- **Route:** `/j/form` — no longer requires auth (removed `NeedsAuth` wrapper)
- **Layout:** `QuizLayout` — two-column, left sticky headline, right form content
- **Steps:** 7 steps (name → description → org type → nonprofit details [conditional] → website → fiscal sponsorship → review + terms)
- **Auth:** happens at the END via inline modal overlay — not a redirect. User fills everything first, then signs in/up to submit.
- **Backend:** unchanged — same `submitMembershipGroupApplication` GraphQL mutation, same fields
- **File:** `src/features/public/routes/ApplyFormRoute.tsx`

#### How to Work on User Flows
Dan's process for tackling flows:
1. Pick a flow from the UX Testing Bible
2. Dan provides an audio transcript scoping the work
3. Create a branch: `danpliego/<flow-slug>`
4. Read the relevant spec(s) in `docs/specs/`
5. Build frontend only — no backend/schema changes without Dan's approval
6. Use existing design system components (`Button`, `Card`, `Typography`, `SelectionCard`, `QuizLayout`, etc.)
7. Screenshot each state with Playwright, upload to files.fwnrd.net
8. One flow at a time, finish completely before starting the next

#### Branch Naming for Flows
- `danpliego/apply-quiz-stepper` — Flow 1 (organizer application)
- Pattern: `danpliego/<flow-name>`

#### Login for Testing
```bash
# Get a magic link code in dev
curl -s -X POST http://localhost:8888/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation { requestMagicLink(input: { email: \"hola@casasoda.com\", path: \"/h\" }) { magicCode } }"}'

# Then navigate to:
# http://localhost:8888/oauth/verify?email=hola@casasoda.com&code=<CODE>&path=/h
```

#### Super Admin
```bash
# Grant via Aurora Data API (env vars from apps/web/.env.default)
# 1. Get user ID
aws rds-data execute-statement --resource-arn "$RESOURCE_ARN" --secret-arn "$SECRET_ARN" --database "$DB_NAME" --sql "SELECT id FROM users WHERE email = 'hola@casasoda.com'" --region us-east-1

# 2. Insert role
aws rds-data execute-statement --resource-arn "$RESOURCE_ARN" --secret-arn "$SECRET_ARN" --database "$DB_NAME" --region us-east-1 --sql "INSERT INTO user_roles (id, \"userId\", role, \"createdAt\", \"updatedAt\") VALUES ('$(openssl rand -hex 11)', '<USER_ID>', 'SUPER_ADMIN', NOW(), NOW()) ON CONFLICT DO NOTHING"
```
