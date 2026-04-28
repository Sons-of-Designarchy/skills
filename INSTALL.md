# How to Set Up Claude Code with Dan's Frontend Bible

This guide gets your machine set up so Claude Code automatically loads Dan's working preferences, design rules, and project-specific guides in every session.

---

## What You're Installing

**Dan's Frontend Bible** (`soda-front`) is a skill file that loads into Claude Code and tells it:
- How Dan works, how to communicate with him, and what his commands mean
- Universal design and code rules across all projects
- Project-specific rules for Finsera, Yardzen, and Fawnroad
- A QA guide for the junior dev

Once installed, you run `/soda-front` at the start of any Claude Code session and it instantly has full context.

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

## Step 2 — Clone the skills repo

```bash
git clone https://github.com/Sons-of-Designarchy/skills.git ~/projects/soda/skills
```

---

## Step 3 — Create the Claude config directories

```bash
mkdir -p ~/.claude/skills
mkdir -p ~/.claude/commands
```

---

## Step 4 — Symlink the skill file

This links the file from the repo into Claude's config so you always have the latest version when you `git pull`.

```bash
ln -s ~/projects/soda/skills/prompting-guide.md ~/.claude/skills/soda-front.md
ln -s ~/projects/soda/skills/prompting-guide.md ~/.claude/commands/soda-front.md
ln -s ~/projects/soda/skills/soda-quote.md ~/.claude/skills/soda-quote.md
ln -s ~/projects/soda/skills/soda-quote.md ~/.claude/commands/soda-quote.md
```

---

## Step 5 — Verify it works

Open a new Claude Code session in any project:

```bash
claude
```

Then type:

```
/soda-front
```

You should see Dan's Frontend Bible load. If it loads, you're done.

---

## Keeping It Up to Date

The skill lives in the repo, so updating is just a pull:

```bash
cd ~/projects/soda/skills && git pull
```

No need to re-symlink — the symlink always points to the latest file.

---

## How to Use It

At the start of any work session with Claude Code, load the skill:

```
/soda-front
```

Claude now knows:
- Dan's design rules and preferences
- The project-specific tech stack and conventions
- What not to do (the corrections log)
- How to request QA plans (for the junior dev)

You don't need to re-explain context. Just give commands.

---

## For the Junior Dev — QA Quick Start

Once you have the skill installed, load it and go to the **QA Guide** section. That section has:

- A template for requesting a QA testing plan from Dan or another dev
- A visual QA checklist to run before anything ships
- How to write a clear bug report
- A template for reporting results back to Dan

When Dan says a feature is ready for QA, ask him to share the staging URL and run the checklist. Report back using the template.

---

## Questions?

Ask Dan.
