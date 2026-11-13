# Finsera growth: handoff 2026-11-13

Continues `finsera-growth-2026-11-06.md` (read it too). Dan replies in Spanish, wants it SHORT, is tired: give one next action, not lists. Load `/soda-front`, `/soda-finsera` and the new `/soda-conversions` (funnel, what to measure, testing rules).

## Goal
2 Reddit ads running, each with its own landing:
1. **Normal** → `/videos` (live in production). Ad "Themes" is live but the campaign showed **Processing** after Laurent's card (normal; ad review up to ~24h). Check Ads tab statuses and Billing if still stuck.
2. **Compare** → Finsera vs Schwab landing (MR below).

## MR !6469 (draft) — Finsera vs Schwab landing
https://gitlab.finseradev.net/finsera/web-ui/-/merge_requests/6469 · branch `sc-85373/danielpliego2282/compare-schwab` · one commit `4badadbf3`. Built from Dan's WIP branch `danielpliego2282/compare-pages` (untouched).
- `/compare/thematic-explorer-vs-schwab-investing-themes`. Only Schwab is `approved` in bundled content (`apps/cms/projects/thematic-explorer/comparison-defaults.ts`); other five pages stay drafts (404 in prod).
- Hero now goes straight to the compare (Framer `framer-vs-webflow` pattern): title "Thematic Explorer vs Schwab Investing Themes", subtitle, CTA "Create a free account" + "See the comparison" (anchor), then the table "Side by side". Product screenshot removed (it showed returns).
- Signup CTAs carry `?source=` (default `reddit_vs_schwab`).
- **Shell Sign up buttons** (top bar, mobile menu, sidebar, desktop actions) now keep the page's `?source=` via `_helpers/signup-source.ts` (`getRegisterHref`) + `_hooks/use-register-href.ts`. Fixes the known leak on `/videos` too.
- **Cookie banner** compact on phones (`packages/finsera-ui/src/_components/cookie-consent`).
- Checks: eslint, tsc, comparisons + demo tests pass. Dan hasn't QA'd the new hero yet.
- Dan runs the pipeline and merges; then cherry-pick to the current staging/release branch (last one used: `rc329`).

## Open before launching ad 2
- **Ad creative `vs_schwab_v1`** (copied to `handoffs/finsera-reddit-ads/` in this repo, HTML sources in `src/`, re-render with `node src/gen.js && node src/render.js`) says "Look before you buy a theme." → no longer matches the hero. Redo it with the "vs" title (message match). Review page: https://claude.ai/artifact/Mm2GKqkMaw2HPhGkzqySXC (6 other creatives too; Dan/Laurent pick).
- Schwab facts ("$250 minimum", "40+ themes, up to 25 stocks", "$0 to access", "adjust holdings") come from a Dec 2023 press release: confirm still true.
- Disclaimer: page says "Research only"; the exact "Research tool, not a broker. Not investment advice." isn't on it. Ask Dan.
- "We earn nothing when you invest": confirm with Laurent.
- Sanity: if a Schwab `comparisonPage` doc was ever seeded as draft, it overrides the bundled one → 404 in prod. Approve or delete it in Studio.
- Ad URL: `https://themes.finsera.com/compare/thematic-explorer-vs-schwab-investing-themes?source=reddit_vs_schwab&utm_source=reddit&utm_medium=paid_social&utm_campaign=tb_nov26_signups&utm_content=vs_schwab_v1`

## Still pending from before
- Dan: test signup end to end in incognito from the ad URL (admin shows `signup_source`, Reddit Events Manager shows SignUp).
- `/videos` still has returns in `preview-poster.jpg` / `dashboard-mockup-flat.png` and "thematic investing" copy.
- Signal header fix !6456 (separate Pipeline / Portfolio Pipeline, full dates) merged state unknown; already cherry-picked and pushed to `rc329` (`4d3d782c3`).

## Gotchas
- Master now needs Node 22+ (`nvm use 24.0.0`); `/soda-finsera` still says 20.19 — update it.
- Don't launch agents to build something before checking remote branches: Dan already had compare pages on the other laptop.
- No screenshots unless Dan asks.
