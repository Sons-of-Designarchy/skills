import html,os
SUF=" Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice."
BASE="https://themes.finsera.com/videos?source=reddit_explore&utm_source=reddit&utm_medium=paid_social&utm_campaign=tb_nov26_signups&utm_content="
C=[
("product_v1","Product","Clean product view of the themes list. No returns, scores or charts (the planned 'Product' ad).","Browse 90+ investing themes, not just tickers. See what each theme covers, compare them, and build your own."+SUF,"All four communities (control vs the live 'Themes' ad)"),
("explainer_ai_v1","Theme explainer","What is inside the AI theme, by segment. Educational, no tickers.","What's actually inside an “AI stocks” theme? Chips, cloud, data, software and robotics, grouped in one place so you can research each part."+SUF,"r/stocks, r/StockMarket (tech-leaning); later r/artificial"),
("question_v1","Question hook (native)","Plain text-forward, reads like a post, not a banner.","How do you research a theme like AI or cybersecurity? Most people start with a single ticker. We start with the theme, then go company by company."+SUF,"r/investing, r/stocks (discussion-heavy)"),
("compare_v1","Compare themes","Three theme cards side by side with what each covers.","AI, robotics or cybersecurity? Compare themes side by side and see what each one covers."+SUF,"r/investing, r/ETFs (people who already compare funds)"),
("build_v1","Build your own theme","Custom-basket builder, placeholder company names.","Can't find your theme? Build your own. Name it, add companies, and track it in one place."+SUF,"r/ETFs, r/ValueInvesting, r/dividends (DIY researchers)"),
("statement_v1","Statement","Navy brand card, one line. Different visual weight in the feed.","Start with a theme, not a ticker. Research AI, robotics, cybersecurity and 90+ more ideas."+SUF,"All communities (broad awareness test)"),
]
for c in C: assert len(c[3])<=300,(c[0],len(c[3]))
S=[
("1. Creative bake-off","Traffic (same as today)",
 "Same 4 communities (r/investing, r/stocks, r/StockMarket, r/ETFs), US only. One ad group, 4 ads: live 'Themes' (explore_v1), product_v1, question_v1, explainer_ai_v1.",
 "$20/day, even rotation. Pause nothing for the first 3 days.",
 "Day 3: each ad has 150+ impressions per dollar-day... simply: each ad has at least $4 spend and 1,000 impressions; compare CTR and CPC. Day 14: best ad has lowest cost per click and at least 1 SignUp per ~$30-40 of spend (verify with real CPC).",
 "Kill any ad with CTR under half of the best ad after $5 spend. Kill all but the top 2 at day 7."),
("2. Theme-matched communities","Traffic",
 "Ad group A (AI/tech): r/artificial, r/ArtificialInteligence, r/NVDA_Stock. Ad group B (research-minded): r/ValueInvesting, r/dividends, r/SecurityAnalysis. Creatives: explainer_ai_v1 + statement_v1 on A; compare_v1 + question_v1 on B. Keep current 4 communities paused or at $0 for this test.",
 "$12/day group A, $8/day group B.",
 "Day 3: CTR and CPC in each group at or better than the current campaign's day-1 numbers. Day 14: signups per $ beats the control (strategy 1 winner). Judge by signup_source, set a new source for each group (reddit_ai, reddit_research).",
 "Kill a community group if CPC is 2x control by day 7. Skip r/wallstreetbets (meme/YOLO audience, brand risk), r/Bogleheads (index-only, hostile to stock themes), r/financialindependence and r/personalfinance (strict anti-promotion culture). Check each community's rules and ad sensitivity in Reddit's targeting preview, I could not verify them."),
("3. Optimize for SignUp","Conversions (SignUp pixel event)",
 "Only after Dan's test signup shows SignUp in Events Manager. Targeting: the 4 current communities plus interest targeting (Investing, Personal Finance, Technology) and keywords such as 'AI stocks', 'thematic investing', 'ETF', 'cybersecurity stocks'. Ads: top 2 from strategy 1.",
 "$20/day, one ad group. Conversions needs volume (Reddit learns best with about 50 events a week), so run it as a 7-day trial, not a full swap.",
 "Day 3: delivery is steady and at least 1 SignUp is recorded (learning phase, do not edit). Day 14: cost per SignUp is at or below the Traffic campaign's cost per SignUp.",
 "Kill if under 3 SignUps after $100 spend by day 7, then go back to Traffic. Also kill if signups arrive but never complete onboarding (low quality)."),
]
S[0]=(S[0][0],S[0][1],S[0][2],S[0][3],"Day 3: each ad has at least $4 spend and 1,000 impressions; compare CTR and CPC. Day 14: the best ad has the lowest cost per click and a signup rate you can live with (check against real CPC, not an assumed one).",S[0][5])
e=html.escape
# README
r="# Finsera Themes: Reddit ads, round 2\n\nCompliance in every creative: no returns, no performance numbers, no charts. Each headline keeps the free plan / price line and the not-a-broker disclaimer. PNGs: `<name>_1200x628.png` and `<name>_1080x1080.png`. Source HTML in `src/` (`node src/gen.js && node src/render.js` rebuilds them).\n\nURL pattern: `"+BASE+"<utm_content>`\n\n## Creatives\n\n| Creative | Image | utm_content | CTA | Best for |\n|---|---|---|---|---|\n"
for k,n,d,h,g in C: r+=f"| {n} | `{k}_*.png` | `{k}` | Sign Up | {g} |\n"
r+="\n### Headlines (all under 300 characters)\n\n"
for k,n,d,h,g in C: r+=f"**{n}** ({len(h)} chars)\n> {h}\n\n"
r+="## Alternate strategies\n\n"
for t,o,tg,b,s,k in S: r+=f"### {t}\n- **Objective:** {o}\n- **Targeting:** {tg}\n- **Budget:** {b}\n- **Success:** {s}\n- **Kill:** {k}\n\n"
r+="Note: all CPC/CTR thresholds are relative to your own day-1 data, because we have no baseline yet. Each new ad group needs its own `source` value in the URL.\n"
open('README.md','w').write(r)
# Artifact
cards=""
for k,n,d,h,g in C:
    cards+=f'''<article class="cr"><h3>{e(n)}</h3><p class="d">{e(d)}</p>
<div class="imgs"><figure><img src="img/{k}_1200x628.png" alt="{e(n)} 1200x628"><figcaption>1200×628</figcaption></figure><figure class="sqf"><img src="img/{k}_1080x1080.png" alt="{e(n)} 1080x1080"><figcaption>1080×1080</figcaption></figure></div>
<dl><dt>Headline ({len(h)}/300)</dt><dd>{e(h)}</dd><dt>CTA</dt><dd>Sign Up</dd><dt>utm_content</dt><dd><code>{k}</code></dd><dt>Ad group</dt><dd>{e(g)}</dd></dl></article>'''
strat=""
for t,o,tg,b,s,k in S:
    strat+=f'<article class="st"><h3>{e(t)}</h3><dl><dt>Objective</dt><dd>{e(o)}</dd><dt>Targeting</dt><dd>{e(tg)}</dd><dt>Budget</dt><dd>{e(b)}</dd><dt>Success</dt><dd>{e(s)}</dd><dt>Kill</dt><dd>{e(k)}</dd></dl></article>'
page=f'''<title>Finsera Reddit Ads</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Caslon+Text:wght@400;700&display=swap">
<style>
/* Review sheet: one column of creatives, then strategies. Navy/blue from the Finsera theme. */
:root{{--bg:#F5F7FB;--card:#fff;--fg:#202541;--mut:#5B6479;--line:#E1E6EF;--acc:#305A9C;--accl:#E9EFF8;--serif:'Libre Caslon Text',Georgia,serif;--sans:Inter,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#12152A;--card:#1B203A;--fg:#EDF0F8;--mut:#A3ACC4;--line:#2D3454;--acc:#8FB1E6;--accl:#242C4D;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#12152A;--card:#1B203A;--fg:#EDF0F8;--mut:#A3ACC4;--line:#2D3454;--acc:#8FB1E6;--accl:#242C4D;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:15px;line-height:1.5;padding-block:32px 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1000px;margin:0 auto;display:flex;flex-direction:column;gap:32px}}
h1,h2{{font-family:var(--serif);font-weight:700;text-wrap:balance;line-height:1.15}}h1{{font-size:30px}}h2{{font-size:24px;margin-top:16px}}h3{{font-size:17px;font-weight:600}}
.lead{{color:var(--mut);max-width:65ch}}
.cr,.st{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:14px;min-width:0}}
.d{{color:var(--mut)}}
.imgs{{display:grid;grid-template-columns:1.9fr 1fr;gap:12px;align-items:start}}
figure{{margin:0;min-width:0}}img{{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:8px}}
figcaption{{font-size:12px;color:var(--mut);margin-top:4px}}
dl{{display:grid;grid-template-columns:110px 1fr;gap:8px 14px;margin:0}}dt{{color:var(--mut);font-size:13px}}dd{{margin:0;min-width:0;overflow-wrap:anywhere}}
code{{background:var(--accl);color:var(--acc);padding:1px 6px;border-radius:5px;font-size:13px}}
.url{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:13px;overflow-wrap:anywhere;color:var(--mut)}}
@media(max-width:560px){{.imgs{{grid-template-columns:1fr}}dl{{grid-template-columns:1fr;gap:2px}}dt{{margin-top:8px}}}}
</style>
<main>
<header><h1>Reddit ads, round 2</h1><p class="lead">Six image ads (1200×628 and 1080×1080) and three strategies to test. No returns or performance numbers anywhere. PNGs are in ~/Desktop/finsera-reddit-ads/.</p></header>
<div class="url">URL for every ad: {e(BASE)}<b>&lt;utm_content&gt;</b></div>
<h2>Creatives</h2>{cards}
<h2>Strategies to test</h2>{strat}
<p class="d">Thresholds are relative to your own day-1 data; we have no baseline yet. Check each community's rules in Reddit's targeting preview before adding it.</p>
</main>'''
open('src/review.html','w').write(page)
