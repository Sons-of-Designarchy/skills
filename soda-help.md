# Casa Soda — Help & Quick Reference

The cheat sheet for anyone on the team. If someone loads this skill, answer their question using the info below — short and direct, no lectures.

---

## The Skill Set

| Skill | Load when |
|---|---|
| `/soda-front` | **Always — every session.** Dan's rules, communication style, design principles. |
| `/soda-finsera` | Working on Finsera (dashboard, thematic-baskets, portfolios, design-system) |
| `/soda-yardzen` | Working on Yardzen (build-marketplace, design sandbox, back-office) |
| `/soda-fawnroad` | Working on Fawnroad (apps/web) |
| `/screens` | Screenshot QA — capture any app at desktop + mobile viewports |
| `/soda-quote` | Client quotes and pricing |
| `/soda-help` | This card |

Rule of thumb: `/soda-front` + the skill for the repo you're in.

---

## Dev Servers — ports & commands

| Project / app | Node | Command | URL |
|---|---|---|---|
| Finsera (all apps) | `nvm use 20.19.6` | `yarn start` (repo root) | localhost:3000 (dashboard), 3001 (portfolios), 3002 (thematic-baskets), 3003 (design-system) |
| Yardzen build-marketplace | `nvm use 24.0.0` | `npx nx serve build-marketplace` (monorepo root) | localhost:4200 |
| Yardzen design-sandbox apps | `nvm use 24.0.0` | `npm run dev` (from the app folder) | localhost:5173 |
| Yardzen back-office | `nvm use 24.0.0` | `npx nx serve back-office` | localhost:4210 |
| Fawnroad | `nvm use 24.0.0` | `npm run dev:start` (from `apps/web`) | localhost:8888 |

**Node versions:** Soda default is `24.0.0`. Finsera is the exception: `20.19.6`.

---

## Troubleshooting One-Liners

```bash
# "Cannot find native binding" / Tailwind CSS won't compile
nvm use 24.0.0 && rm -rf node_modules package-lock.json .next && npm install

# Finsera nuclear reset
rm -rf .turbo apps/*/.turbo packages/*/.turbo node_modules apps/*/node_modules packages/*/node_modules && yarn

# Yardzen "Failed to process project graph" / "crypto is not defined"
nvm use 24 && nx reset

# Port already in use (replace 3000 with your port)
lsof -ti :3000 | xargs kill -9

# Fawnroad dev server status / logs
cd apps/web && npm run dev:status && npm run dev:logs
```

When you see an error in red you don't understand: copy it, paste it into Claude. That's the workflow.

---

## Update Your Setup

```bash
cd ~/projects/soda/skills && git pull && bash setup.sh
```

`setup.sh` is idempotent — it refreshes all skill symlinks and Node versions. Run it whenever something seems out of date.

First time on a new machine:

```bash
git clone https://github.com/Sons-of-Designarchy/skills.git ~/projects/soda/skills
bash ~/projects/soda/skills/setup.sh
```

---

## Golden Rules (the ones people forget)

- Load `/soda-front` at the start of every session
- Don't commit or push unless Dan told you to
- 1px borders, no black borders, no uppercase by default
- Use the design system — never invent buttons or cards
- Screenshot QA at 1280×800 / 768×1024 / 390×844 before saying "it's ready"
- Stuck → copy the error to Claude → still stuck → ask Dan
