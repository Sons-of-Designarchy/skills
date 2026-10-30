# Handoff: Finsera growth / marketing taskforce (2026-10-30)

Continue on the other laptop. Read `soda-finsera.md` first (Git Workflow, Thematic Baskets sections), then this file.
Everything is committed and pushed. Nothing merged except the videos page.

## How Dan wants it done
- Short answers. Split commit / push / MR into separate commands so permission prompts stay readable.
- Never commit or push to `master` / `main`. Dan merges.
- Laurent owns marketing copy. Technical MRs (SEO, plumbing) must not rewrite on-page copy. Copy proposals go in the MR description, not the diff.
- Funnel decision: homepage → "Create an account" → product. No plan step at signup, plans come later.
- Platform direction: "more open". Anonymous visitors see theme pages; the real gate is server side (no weights, top 5 holdings only).
- No code comments. MUI fontWeight 500, never 600. Never touch desktop styles.
- Commit trailer required by Dan's Claude setup: `Claude-Session: https://claude.ai/code/session_014YbzZQi8MZzgbBoXbxdwNV`. MR descriptions end with that URL.
- **Every draft MR gets a Shortcut story in the epic "Marketing taskforce"** (epic 85210, workspace `finsera-1`): https://app.shortcut.com/finsera-1/epic/85210. Backfill of the 9 MRs below is still pending (Chrome extension was attached to a profile not logged into Shortcut).

## Repos and remotes
| Repo | Local path (main laptop) | Remote |
|---|---|---|
| web-ui | `~/projects/finsera/web-ui` | push to `finseradev` (gitlab.finseradev.net/finsera/web-ui). `origin` (gitlab.com) is dead. |
| finsera-website (Astro, new marketing site) | `~/projects/finsera/finsera-website` | `origin` = gitlab.finseradev.net/finsera/finsera-website. Deploy: `vercel --prod --yes --scope finsera1` (project `finsera-website`). |

glab needs the host: `GITLAB_HOST=gitlab.finseradev.net glab mr list --repo gitlab.finseradev.net/finsera/web-ui`.

## Open MRs (all draft except the two plumbing ones)
web-ui, target `master`, base https://gitlab.finseradev.net/finsera/web-ui/-/merge_requests/
| MR | Branch | What |
|---|---|---|
| !6411 | `danielpliego2282/seo-audit` | SEO plumbing: canonical, og:url/og:image, Organization + SoftwareApplication JSON-LD (real Sanity pricing), robots disallows, 404 status. Marcel's SEO/GEO audit appended with a coverage table. Ready for review. |
| !6412 | `danielpliego2282/simplify-signup` | One-step register, no plan selection, `returnTo` cookie through check-email → set-password → auto-login, "Create an account" CTAs. e2e Scenarios RG-002/RG-003 updated, test sync pending (`e2e-plan` skill). |
| !6413 | `danielpliego2282/public-theme-pages` | Public SSR `/themes/:slug` pages, anonymous curated `/basket/:id/:slug` 301s there, `allHoldings` now `free`, `latest_weights` stripped for anonymous, sitemap emits `/themes/<slug>`, `/emerging` removed. 9 unit tests. |
| !6414 | `danielpliego2282/about-founders` | About page founders + credibility line + Organization/Person JSON-LD. New Sanity `aboutPage.founders` / `credibility` fields, Dan fills them in Sanity. |
| !6415 | `danielpliego2282/shareable-watchlists` | Share buttons (copy link, LinkedIn, X) on curated themes + `theme_shared` PostHog event. Shared watchlists blocked on fin-gen (see below). |
| !6416 | `danielpliego2282/etf-comparison-pages` | Public `/etf/:ticker` pages from a hand-written ticker → theme config (`app/_core/config/etf-pages.ts`), FAQPage + BreadcrumbList JSON-LD. Validate the 8 tickers against real related-ETF output before launch. |

finsera-website, target `main`, base https://gitlab.finseradev.net/finsera/finsera-website/-/merge_requests/
| MR | Branch | What |
|---|---|---|
| !3 | `danielpliego2282/seo-audit` | Canonical, og:url, default og image, `jsonLd` prop on `Layout.astro`, Organization + SoftwareApplication on the home. "Monitore" → "Monitor". |
| !4 | `danielpliego2282/thematic-cta-create-account` | "Visit Website" → "Create an account" linking to `themes.finsera.com/register?source=finsera_com`. |
| !5 | `danielpliego2282/about-founders` | Founders section, credibility line, JSON-LD. |

Scratch: `scratch/integration` on `finseradev` = seo-audit + public-theme-pages + simplify-signup merged (conflicts only in the import blocks of `routes/login.tsx` and `routes/register.tsx`). tsc + 243 tests pass. Not an MR.

Shipped: finsera.com `/videos` with 3 Vimeo demos, merged and deployed.

## Set up on the new laptop
```bash
cd ~/projects/finsera/web-ui && git fetch finseradev
for b in seo-audit simplify-signup public-theme-pages about-founders shareable-watchlists etf-comparison-pages; do
  git worktree add ../web-ui-$b danielpliego2282/$b
done
cd ../web-ui-seo-audit && yarn install --frozen-lockfile && sh serverless/create-config-local.sh
yarn workspace thematic-baskets start --port 3002
```
`create-config-local.sh` writes stub `packages/finsera-core/*.local.js`. Copy the real ones from the main checkout by hand if you want the API locally (Claude is blocked from copying secrets). Without them SSR pages 404 locally.

## Merge order and follow-ups
1. !6411 then !6413 then !6412 (the scratch branch proves they merge cleanly). Then !6414, !6416, !6415.
2. After the first merge unify `app/_helpers/seo.ts`, `seo-meta.ts`, `seo-about.ts`, `seo-etf.ts` into one helper.
3. Sync e2e tests for RG-002/RG-003 with the `e2e-plan` skill (the e2e MCP timed out on the main laptop).
4. Small items from Marcel's audit, not done: one H1 per page on the home (`views/home/hero-section.tsx` and `features-section.tsx` both use h1), FAQPage JSON-LD on `/why-thematic-baskets`, footer address mismatch (app says Suite 1200 in `_components/footer.tsx`, www says Suite 120 in `Footer.astro` and `contact.astro`; ask Dan which is right).
5. Decisions for Laurent / Dan: one product name ("Thematic Explorer" vs "Thematic Baskets"), blog host, GEO hub pages, measurement.

## Dan must fix outside code
Sanity: home hero "Built or analyze" typo, Enterprise plan "For individual use", tier1 title "Basic" → "Premium", fill `aboutPage.founders` and `credibility`. Admin: Autonomous Defense theme tagged Climate.

## Blocked on fin-gen
Shared / public watchlists: workspace reads are limited to the creator or `context='production'` (`src/web_api/resources/access/publish_by_context.py`). Proposal in !6415: allow reads where `workspace_metadata.is_public`, or add a `share_token` column + public endpoint.

## Deferred ideas (researched, not built)
Hero prompt → `/explore/[slug]` (curated-theme match, no LLM, in-memory rate limit), dynamic OG images (satori on ECS, risky), embed widget `/embed/theme/[id]`, company pages `/company/[ticker]`, weekly rankings, self-serve referral links.

Source doc: "Finsera Growth — Project Brief" (Claude Doc TeBxUrGGZvcsA4dQLxb88o). Marcel's SEO/GEO audit is quoted in full in !6411.
