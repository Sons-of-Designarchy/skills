# Finsera Themes: Reddit ads, round 2

Compliance in every creative: no returns, no performance numbers, no charts. Each headline keeps the free plan / price line and the not-a-broker disclaimer. PNGs: `<name>_1200x628.png` and `<name>_1080x1080.png`. Source HTML in `src/` (`node src/gen.js && node src/render.js` rebuilds them).

URL pattern: `https://themes.finsera.com/videos?source=reddit_explore&utm_source=reddit&utm_medium=paid_social&utm_campaign=tb_nov26_signups&utm_content=<utm_content>`

## Creatives

| Creative | Image | utm_content | CTA | Best for |
|---|---|---|---|---|
| Product | `product_v1_*.png` | `product_v1` | Sign Up | All four communities (control vs the live 'Themes' ad) |
| Theme explainer | `explainer_ai_v1_*.png` | `explainer_ai_v1` | Sign Up | r/stocks, r/StockMarket (tech-leaning); later r/artificial |
| Question hook (native) | `question_v1_*.png` | `question_v1` | Sign Up | r/investing, r/stocks (discussion-heavy) |
| Compare themes | `compare_v1_*.png` | `compare_v1` | Sign Up | r/investing, r/ETFs (people who already compare funds) |
| Build your own theme | `build_v1_*.png` | `build_v1` | Sign Up | r/ETFs, r/ValueInvesting, r/dividends (DIY researchers) |
| Statement | `statement_v1_*.png` | `statement_v1` | Sign Up | All communities (broad awareness test) |
| Finsera vs Schwab | `vs_schwab_v1_*.png` | `vs_schwab_v1` | Sign Up | Second ad; lands on the Schwab comparison page (own URL below) |

Schwab ad URL (lands on the comparison page, not /videos): `https://themes.finsera.com/compare/thematic-explorer-vs-schwab-investing-themes?source=reddit_vs_schwab&utm_source=reddit&utm_medium=paid_social&utm_campaign=tb_nov26_signups&utm_content=vs_schwab_v1`

### Headlines (all under 300 characters)

**Product** (207 chars)
> Browse 90+ investing themes, not just tickers. See what each theme covers, compare them, and build your own. Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice.

**Theme explainer** (238 chars)
> What's actually inside an “AI stocks” theme? Chips, cloud, data, software and robotics, grouped in one place so you can research each part. Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice.

**Question hook (native)** (245 chars)
> How do you research a theme like AI or cybersecurity? Most people start with a single ticker. We start with the theme, then go company by company. Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice.

**Compare themes** (187 chars)
> AI, robotics or cybersecurity? Compare themes side by side and see what each one covers. Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice.

**Build your own theme** (188 chars)
> Can't find your theme? Build your own. Name it, add companies, and track it in one place. Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice.

**Finsera vs Schwab** (240 chars)
> Schwab Investing Themes lets you buy a theme. Finsera lets you study one first. Type an idea, see the companies, compare it with the S&P 500. Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice.

**Statement** (189 chars)
> Start with a theme, not a ticker. Research AI, robotics, cybersecurity and 90+ more ideas. Free plan available, paid plans from $96/year. Research tool, not a broker. Not investment advice.

## Alternate strategies

### 1. Creative bake-off
- **Objective:** Traffic (same as today)
- **Targeting:** Same 4 communities (r/investing, r/stocks, r/StockMarket, r/ETFs), US only. One ad group, 4 ads: live 'Themes' (explore_v1), product_v1, question_v1, explainer_ai_v1.
- **Budget:** $20/day, even rotation. Pause nothing for the first 3 days.
- **Success:** Day 3: each ad has at least $4 spend and 1,000 impressions; compare CTR and CPC. Day 14: the best ad has the lowest cost per click and a signup rate you can live with (check against real CPC, not an assumed one).
- **Kill:** Kill any ad with CTR under half of the best ad after $5 spend. Kill all but the top 2 at day 7.

### 2. Theme-matched communities
- **Objective:** Traffic
- **Targeting:** Ad group A (AI/tech): r/artificial, r/ArtificialInteligence, r/NVDA_Stock. Ad group B (research-minded): r/ValueInvesting, r/dividends, r/SecurityAnalysis. Creatives: explainer_ai_v1 + statement_v1 on A; compare_v1 + question_v1 on B. Keep current 4 communities paused or at $0 for this test.
- **Budget:** $12/day group A, $8/day group B.
- **Success:** Day 3: CTR and CPC in each group at or better than the current campaign's day-1 numbers. Day 14: signups per $ beats the control (strategy 1 winner). Judge by signup_source, set a new source for each group (reddit_ai, reddit_research).
- **Kill:** Kill a community group if CPC is 2x control by day 7. Skip r/wallstreetbets (meme/YOLO audience, brand risk), r/Bogleheads (index-only, hostile to stock themes), r/financialindependence and r/personalfinance (strict anti-promotion culture). Check each community's rules and ad sensitivity in Reddit's targeting preview, I could not verify them.

### 3. Optimize for SignUp
- **Objective:** Conversions (SignUp pixel event)
- **Targeting:** Only after Dan's test signup shows SignUp in Events Manager. Targeting: the 4 current communities plus interest targeting (Investing, Personal Finance, Technology) and keywords such as 'AI stocks', 'thematic investing', 'ETF', 'cybersecurity stocks'. Ads: top 2 from strategy 1.
- **Budget:** $20/day, one ad group. Conversions needs volume (Reddit learns best with about 50 events a week), so run it as a 7-day trial, not a full swap.
- **Success:** Day 3: delivery is steady and at least 1 SignUp is recorded (learning phase, do not edit). Day 14: cost per SignUp is at or below the Traffic campaign's cost per SignUp.
- **Kill:** Kill if under 3 SignUps after $100 spend by day 7, then go back to Traffic. Also kill if signups arrive but never complete onboarding (low quality).

Note: all CPC/CTR thresholds are relative to your own day-1 data, because we have no baseline yet. Each new ad group needs its own `source` value in the URL.
