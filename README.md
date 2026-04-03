# Casa Soda — Skills & Guides

This repo contains the team's shared knowledge base for working with AI agents (Claude Code) across all projects.

---

## What's in here

| File | What it is |
|---|---|
| `prompting-guide.md` | The main guide — read this first |
| `INSTALL.md` | How to install everything on your computer |

---

## Install in 4 commands

Open your terminal and paste this:

```bash
git clone https://github.com/Sons-of-Designarchy/skills.git ~/projects/soda/skills
mkdir -p ~/.claude/skills ~/.claude/commands
ln -s ~/projects/soda/skills/prompting-guide.md ~/.claude/skills/soda-front.md
ln -s ~/projects/soda/skills/prompting-guide.md ~/.claude/commands/soda-front.md
```

Done. Now open Claude Code in any project and type `/soda-front`.

---

## How to update

When the guide gets updated, pull the latest:

```bash
cd ~/projects/soda/skills && git pull
```

No reinstall needed — the link always points to the newest version.

---

## Terminal survival guide

You don't need to know much. Here are the commands you'll actually use:

### Moving around

```bash
ls                    # what's in this folder?
cd folder-name        # go into a folder
cd ..                 # go back one level
pwd                   # where am I right now?
```

### Running projects

```bash
# Fawnroad
cd apps/web
npm run dev           # start the app (localhost:8888)

# Finsera
nvm use 20.19.3
yarn start            # start all apps

# Yardzen
nvm use 24.0.0
npx nx run-many --target=serve --projects=build-marketplace
```

### Stopping things

```bash
ctrl + C              # stop whatever is running in the terminal
```

### When things break

```bash
# "it won't start"
# Just copy the red error text → paste into Claude → it'll fix it

# "nothing works at all" (Finsera nuclear reset)
rm -rf node_modules && yarn

# "port already in use"
lsof -ti :3000 | xargs kill -9   # replace 3000 with the port number
```

### Git basics

```bash
git status            # what files changed?
git pull              # get the latest from the team
git checkout -b my-branch-name   # start working on a new thing
```

---

## How to use Claude Code

### Starting a session

1. Open your terminal
2. Go to the project folder (`cd path/to/project`)
3. Type `claude` and hit enter
4. When it loads, type `/soda-front` — this loads all the rules and context

### Giving instructions

Keep it simple and specific:

```
"Add a loading spinner to the submit button.
 It should show while the form is submitting.
 Use the existing Button component."
```

If something looks wrong, take a screenshot and paste it in:

```
"[paste screenshot] — the spacing here is too big, reduce it"
```

### When Claude does something wrong

Just say what's wrong:

```
"no, revert that — I didn't want the button to be full width"
"undo the last change and try again"
"stop — read my last message again"
```

### When you're done for the day

Don't push anything unless you've been told to. Just tell Dan what's ready.

---

## Prompting cheatsheet

**Too vague — won't work well:**
> "Make it look better"

**Specific — works great:**
> "The gap between the title and the first card is too large. Reduce it by half. Don't change anything else."

**Formula:**
```
[WHAT] + [WHERE] + [WHAT IT SHOULD DO/LOOK LIKE] + [WHAT TO LEAVE ALONE]
```

---

## If you're stuck

1. Copy the error → paste it to Claude
2. Take a screenshot → paste it to Claude with a description
3. If Claude keeps getting it wrong → type "stop" and describe the problem differently
4. Still stuck → ask Dan

---

## Keep this updated

If Dan tells you something that isn't in this guide, let him know — he'll add it so the whole team benefits.
