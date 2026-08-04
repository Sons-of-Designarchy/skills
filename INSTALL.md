# How to Set Up Claude Code with the Casa Soda Skills

This guide gets your machine set up so Claude Code automatically loads Dan's working preferences, design rules, and project-specific guides in every session.

---

## What You're Installing

The Casa Soda skill set:

| Skill | What it is |
|---|---|
| `/soda-front` | **Dan's Frontend Bible** — how Dan works, communication, universal design & code rules. Load in every session. |
| `/soda-finsera` | Finsera project guide — stack, theme system, workflows |
| `/soda-yardzen` | Yardzen project guide — monorepo, Contentful, sandbox deploys |
| `/soda-fawnroad` | Fawnroad project guide — stack, design system, flows |
| `/soda-help` | Quick reference — ports, commands, troubleshooting |
| `/screens` | Screenshot QA at fixed viewports |
| `/soda-quote` | Client quotes and pricing |

Once installed, you run `/soda-front` at the start of any Claude Code session (plus the skill for the project you're in) and Claude instantly has full context.

---

## Step 1 — Install Claude Code

If you don't have it yet:

```bash
npm install -g @anthropic/claude-code
```

Then authenticate:

```bash
claude
```

Follow the prompts to log in with your Anthropic account.

---

## Step 2 — Clone the repo and run setup

```bash
git clone https://github.com/Sons-of-Designarchy/skills.git ~/projects/soda/skills
bash ~/projects/soda/skills/setup.sh
```

`setup.sh` does everything:
- Symlinks all the skills into `~/.claude/skills` and `~/.claude/commands` (so a `git pull` always gives you the latest)
- Installs **nvm** if you don't have it
- Installs the Node versions our projects use (`24.0.0` default, `20.19.6` for Finsera)

It's idempotent — safe to re-run any time. Already had the old single-file setup? Running it migrates you automatically.

---

## Step 3 — Verify it works

Open a new Claude Code session in any project:

```bash
claude
```

Then type:

```
/soda-front
```

You should see Dan's Frontend Bible load. Then try `/soda-help`. If both load, you're done.

---

## Keeping It Up to Date

```bash
cd ~/projects/soda/skills && git pull && bash setup.sh
```

Usually `git pull` alone is enough (the symlinks always point to the latest files) — run `setup.sh` again when new skills are added.

---

## How to Use It

At the start of any work session with Claude Code:

1. Load `/soda-front`
2. Load the project skill for the repo you're in: `/soda-finsera`, `/soda-yardzen`, or `/soda-fawnroad`

Claude now knows:
- Dan's design rules and preferences
- The project-specific tech stack and conventions
- What not to do (the corrections log)
- How to request QA plans (for the junior dev)

You don't need to re-explain context. Just give commands. Need a quick reference? `/soda-help`.

---

## For the Junior Dev — QA Quick Start

Once you have the skills installed, load `/soda-front` and go to the **QA Guide** section. That section has:

- A template for requesting a QA testing plan from Dan or another dev
- A visual QA checklist to run before anything ships
- How to write a clear bug report
- A template for reporting results back to Dan

When Dan says a feature is ready for QA, ask him to share the staging URL and run the checklist. Report back using the template.

---

## Questions?

Run `/soda-help`. Then ask Dan.
