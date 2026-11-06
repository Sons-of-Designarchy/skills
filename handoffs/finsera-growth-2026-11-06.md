# Finsera growth: handoff 2026-11-06

Continues `finsera-growth-2026-10-30.md`. Dan replies in Spanish and wants it SHORT. One goal right now: **1 Reddit ad running**. Everything else waits.

## Rules learned this week
- Main checkout `~/projects/fin/finsera` stays on master. MR work and QA happen in `~/projects/fin/finsera-worktree`. `git worktree add` is blocked by a hook.
- Run MR tasks in background agents so Dan doesn't wait (one at a time; they share the worktree folder).
- MR descriptions: short Why / What / Tested. No Claude mention, no session links.
- Dan runs pipelines and merges. Never trigger CI.
- finsera-website: no MRs. Commit to `main`, push, then `npx vercel --prod` (team `finsera1`) after Dan's OK.
- Releases go out from branch `r327`: after a merge to master, cherry-pick onto r327. r327 has the OLD package layout (`_core` barrel, `@local/finsera-core`, no `finsera-ui` package, no `_helpers/seo-meta`), so picks need import fixes. Then Dan deploys.
- Node 24 (`nvm use -s 24`). Local maintenance bypass: cookie `_internal` from `packages/finsera-core/server-config.local.js` (never print it).
- Don't overcomplicate. Dan got frustrated when the privacy work ballooned.

## The Reddit ad (campaign "TB Nov26 Signups - Explore")
- Standard campaign, Traffic objective, Lowest cost, auto-targeting OFF, US only.
- Communities: r/investing, r/stocks, r/StockMarket, r/ETFs. Feed. Comments off, Redditor Highlights off.
- Budget $20/day, Nov 9–23, spend cap $280 (Laurent had said $10; Dan chose $20).
- Ad "Themes": image ad, headline (no body field in this format):
  `Researching AI, robotics or cybersecurity stocks? Start with a theme. Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice.`
- Image `finsera-reddit-explore-v2.png` (4 theme cards, no returns), thumbnail `finsera-reddit-thumbnail.png`. Both made on the old laptop in the session scratchpad; Dan already uploaded them to Reddit.
- CTA Sign Up. URL: `https://themes.finsera.com/videos?source=reddit_explore&utm_source=reddit&utm_medium=paid_social&utm_campaign=tb_nov26_signups&utm_content=explore_v1`
- A second ad "Product" (real product screenshot, A/B on image) was planned; its image isn't made yet. The product table shows returns, so it needs a view without percentages. Dan was told to delete it for today.
- **Status:** published, but Inactive: **no credit card**. Laurent (California) adds the card, sets the $280 cap and republishes. Laurent says Reddit compliance is already done.

## Live in production
- themes.finsera.com (r327 at `666590f1b`): GTM + cookie banner, PostHog only after Accept, Terms + Privacy pages and links, /videos landing (research copy, cost + risk block, `?source=` passed to signup buttons, demo button secondary). Verified after deploy.
- GTM `GTM-NXN44DFJ` v6: Reddit pixel `a2_jxfarl2gxs48` tags PageVisit, Lead (Demo Scheduled Page, kept on purpose) and SignUp (Custom Event `sign_up`), all require ad_storage + ad_user_data. Verified: Reddit doesn't fire before choice or after Reject; fires on next page load after Accept.
- finsera.com (`bb1d321`): RB2B removed, PostHog only after Accept, Privacy Policy page + footer link, Terms section 11 (duplicate + law-firm stamps) removed.

## Next steps, in order
1. **Dan: test signup** in incognito from the ad URL above → Accept all → Get started → email signup (not Google) → "Check your email". Then check admin shows `signup_source = reddit_explore` and Reddit Events Manager shows SignUp. Unverified risk: `completeOnboarding` may overwrite `thematic_baskets_metadata` and lose the source.
2. Laurent: card + cap + republish; create `privacy@finsera.com`.
3. When approved: click test, check spend and signups day 1, re-forecast from real CPC on day 3. Decide on day 14.

## Open, after the ad
- /videos still shows returns in two images (`/demo-assets/preview-poster.jpg`, `dashboard-mockup-flat.png`) and says "Thematic investing…", "Ready to try thematic investing?", "our investment options track real growth". Video not reviewed.
- Privacy follow-ups (California review by an agent, not a lawyer): GPC handling, "Your Privacy Choices" footer link to reopen the banner, email in `/register/check-email?email=` URL leaks to GA, signup notice at collection, banner text should mention advertising and link Privacy, policy wording (session recordings, SnapTrade portfolio data if on themes, sale/share with Reddit, retention by criteria, rights + privacy@ email). Policy says "clear the cookie" to change choice, which doesn't work on finsera.com (localStorage).
- Lint: `apps/thematic-baskets/app/views/demo/use-youtube-player.ts` line 35 has 2 unused-arg errors (pre-existing).
- Signups via Google and the top-bar "Sign up" don't carry `source`.
- About page (!6414, sc-85235): 2 commits only on the OLD laptop, unpushed (branch `danielpliego2282/about-founders` in finsera-worktree: merge of master + cut "Who we serve"/"Principles" + new copy). Push from the old laptop or redo.
- ETF pages (!6416, sc-85237) draft, waiting Dan's QA. Blog scoping and Reddit masterclass reports lived in the old session scratchpad.
- Shortcut API token still 401.

## Shortcut stories this week (epic 85210 Marketing taskforce)
sc-85234 signup (merged), sc-85301 GTM/consent/PostHog, sc-85302 demo-scheduled, sc-85237 ETF pages, sc-85235 About, sc-85372 Terms+Privacy on themes, sc-85373 Reddit landing /videos.
