# Prompting Guide for Dan's Projects

A practical reference for junior developers working on Casa Soda projects. Written for people coming from Webflow/Framer who are learning to work with AI coding agents (Claude, Copilot, etc.) and need to prompt changes, fine-tune designs, and ship without constant oversight.

---

## Who You're Working For

**Dan** (Daniel Pliego) is the lead. He moves fast, pivots often, and gives short commands. Your job is to interpret those commands correctly and ship without asking unnecessary questions.

He says a few things that matter a lot:

> "Never stop for any approval — make decisions and keep going."

> "Before doing any sweeping refactors, explain the plan in 3–5 bullets, then execute."

> "Do the thing, say what you did in one line. Skip preamble."

---

## How to Communicate

| Do | Don't |
|----|-------|
| "Done. Added signup link to login page." | "I've carefully analyzed the login page and after reviewing the design system I've decided to add a signup link..." |
| Ask once, then execute | Ask for approval at every step |
| One sentence summary after a task | Long explanations of what you changed |
| Flag blockers immediately | Work around them silently |

**If you get a screenshot** — investigate it immediately. Don't ask what's wrong. Look at it, figure out the issue, fix it.

**If you're interrupted mid-task** — stop immediately and switch. Don't finish the interrupted task.

---

## Terse Commands You'll Hear

| Dan says | He means |
|----------|----------|
| `seed data` | Populate the app with test content |
| `check the logs` | Look at server logs + browser console errors |
| `create a branch` | Make a new git branch off the main dev branch |
| `commit push` | Stage files, commit with a message, push, update PR |
| `commit what we have` | Commit current state even if incomplete |
| `kill the server / restart the server` | Stop and restart the dev server — he has no terminal open |
| `open a browser` | Use a browser automation tool to open the app |
| `forget about errors` | Stop chasing console errors — focus on the UI task |
| `discard all these changes` | `git restore .` — throw away all uncommitted work |
| `fix conflicts` | Resolve merge conflicts keeping Dan's version as base |
| `continue` | You were interrupted — pick up exactly where you left off, no recap |

---

## Design Principles

These apply to every project unless explicitly overridden.

### 1. Duolingo-level simple
The app is for non-technical users. Simplicity is a first-class constraint. Strip everything down: hidden links, minimal copy, obvious CTAs. If you're adding complexity, ask yourself if a 50-year-old non-techy person would get it immediately.

### 2. One component, not many
When there are multiple similar components, merge them into one. No parallel components that do the same thing. This gets repeated across every project.

### 3. Design system components must be used everywhere
No inventing new button styles, card layouts, or input components. Use what's in the design system. Every button is `<Button>`, every card is `<Card>`. If something doesn't exist in the design system, add it there first, then use it.

### 4. No 2px borders
All borders are 1px. Always. Global rule.

### 5. No uppercase by default
Typography uppercase is opt-in — never a default. Same for monospace fonts.

### 6. No aliases when renaming
When asked to rename a component, delete the old one and use the new name everywhere. Do NOT keep the old export and alias it to the new name.

### 7. No skeletons that change the layout
Loading skeletons that render a different DOM shape than the real content cause jarring flashes. Use component-level skeletons that match the real structure, or a single centered spinner. Never change the overall page layout during loading.

---

## Design References Worth Reading

When working on a new feature, always check these first:

- **`/.impeccable.md`** in the repo — brand personality, color palette, typography rules. **Start here** on every project.
- `docs/specs/design-system-refresh/` — design tokens, component specs, layout rules
- `docs/specs/complete-qa-styleguide/` — writing style, copy conventions, QA checklist

### UX knowledge to apply:
- **Heuristics** — Nielsen's 10: visibility of system status, user control, consistency, error prevention, recognition over recall, flexibility, aesthetic minimalism, help users recover from errors, help/docs
- **Anti-patterns to avoid** — dark patterns, mystery meat navigation, fake urgency, confusing hierarchy, inconsistent interactions
- **Cognitive load** — fewer choices = better decisions. One primary action per screen. Progressive disclosure.
- **Community platform patterns** — group identity is central, membership status must be visible, social proof matters, notifications should be opt-in

### Visual design to apply:
- **Color** — use the brand palette, don't invent new colors, contrast is non-negotiable (WCAG AA minimum)
- **Typography** — scale matters more than font choice, consistent hierarchy, don't mix too many sizes
- **Composition** — alignment, whitespace, and repetition create trust. Asymmetry creates interest.
- **Motion** — purposeful only. 200-300ms for micro-interactions. Never animate for the sake of it.

---

## When Using AI Agents (Claude, Copilot, etc.)

### Good prompts
- Specific: `"Add a 'Don't have an account? Sign up' link at the bottom of the login form, linking to /signup"`
- With context: `"The login form is at src/features/auth/components/LoginForm.tsx — add a subtitle below the submit button"`
- With constraints: `"Use the existing Typography component, caption variant, muted color"`

### Bad prompts
- Vague: `"Make the login page better"`
- Without file context: `"Fix the button styles"` (which button? which file?)
- Without design system context: `"Add a new styled button"` — always reference the existing system

### How to describe a visual change
Instead of: `"Make it look better"`
Say: `"Increase the vertical spacing between the form fields from 12px to 20px, and make the CTA button full-width on mobile"`

Instead of: `"The colors feel off"`
Say: `"The background is using white (#fff) but should be using the beige (#f0ede8) that all logged-in pages use"`

### How to describe a layout issue
1. Describe what you see: `"The sidebar overlaps the main content on screens narrower than 1024px"`
2. Describe what it should do: `"The sidebar should collapse/hide on mobile, accessible via a hamburger menu"`
3. Reference a similar pattern: `"Similar to how the settings sidebar behaves on /settings"`

---

## Git Basics for This Workflow

```bash
# Start new work
git checkout -b feat/your-feature-name

# Save your work
git add src/path/to/changed-file.tsx
git commit -m "feat: add signup link to login form"

# Push and create PR
git push origin feat/your-feature-name
gh pr create --title "feat: add signup link to login form"
```

### Branch naming
- `feat/` — new features
- `fix/` — bug fixes
- `chore/` — cleanup, deps, no user-facing change
- `docs/` — documentation only

### Commit message format
```
type: short description of what changed

- bullet point with more detail if needed
- another bullet if multiple things changed
```

Types: `feat`, `fix`, `chore`, `docs`, `style`, `refactor`

---

## What NOT to Do (Real Corrections Log)

These are mistakes that were made on actual projects. Don't repeat them.

- **Don't create aliases when renaming.** Delete old, use new. No backwards compat exports.
- **Don't add uppercase or monospace as defaults.** These are opt-in only.
- **Don't install icon substitutes.** If Font Awesome (or another library) is specified, install it. Don't swap it for inline SVGs to "keep the bundle clean."
- **Don't treat HMR as a restart.** When told to restart the server, restart it. Don't tell the user to just refresh.
- **Don't make borders 2px.** All borders are 1px.
- **Don't create custom buttons outside the design system.**
- **Don't leave "coming soon" pages.** If a route exists, it should have real content or redirect.
- **Don't modify DB schema without explicit approval.** Propose it verbally and wait.
- **Don't apply changes from a previous session** without confirming that's what's wanted.
- **Don't add a trailing summary paragraph** at the end of every response. Just do the thing.

---

## Webflow/Framer → Code Mental Model

If you're used to visual tools, here's how to translate:

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

When you're unsure how something in code maps to what you built visually, describe it in Webflow/Framer terms and a good AI agent will translate it for you.

---

## Quick Reference Card

```
Prompt structure:
  [WHAT] + [WHERE] + [HOW] + [CONSTRAINTS]

Example:
  "Add a loading spinner [WHAT]
   to the submit button in src/features/auth/LoginForm.tsx [WHERE]
   that shows while isLoading is true [HOW]
   using the existing Button component's loading prop [CONSTRAINTS]"
```
