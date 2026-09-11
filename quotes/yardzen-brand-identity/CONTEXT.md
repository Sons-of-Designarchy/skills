# Yardzen Brand Book 2026 — working context

Session of 10–11 Sep 2026. Read this first before touching the proposal.

## Where it stands

Deal shape is **settled**. The proposal document is **not** — Dan's verdict on the current draft: *"the formating is stupid, i dont get the project, at all."* It reads like a contract instead of a pitch, and the timeline is built around calendar months when Dan had already agreed **phases** with Brian.

## Source material

- Brian's brief — `~/Downloads/Yardzen - Brand Design Brief.docx` (Sep 2 2026)
- Brian's quality reference — `~/Downloads/tg-brand-book-master-v1.3.pdf` (Topgolf Brand Book, 104pp)
- Google Doc (ELI5 version, live) — https://docs.google.com/document/d/1rjV3oCsWQqsSL0OweeAgvOOn7Vb90oBhNj3S92BDXYI/edit

## Two facts that set the negotiating position

1. **"Budget: TBC based on the aligned upon scope of work and timing."** No client anchor — Casa Soda sets the number.
2. **"We want to move fast. Let's map out the project phasing together."** Phasing is invited.

Brian's own situation section is the narrative spine — brand equity erosion, inconsistent fonts, varying tone, visuals below standard, and an explicit belief that better brand design means *"more client leads, more design purchases."*

## The money table (settled — do not re-open)

| Line | August | September | Oct–Dec *(each)* | Q1 |
|---|---|---|---|---|
| Product | $9k | $9k | $9k | $9k |
| Code Design System | $3k | $3k | $1k | $1k |
| Marketing asks | $1k | — | $1k | $1k |
| **Brand** | — | **$3k** | **$7k** | **$4k** |
| | | *logo directions* | *build the book* | *adoption + expansion* |
| **Yardzen pays** | **$13k** | **$15k** | **$18k** | **$15k** |

- **Brand Book project = $24,000 USD.** September $3k + $7k each in Oct/Nov/Dec. The only number quoted.
- Q1 is direction, not commitment. **No Q1 total, no Q2 column** — sums there imply commitments nobody is making.
- Product holds at $9k in every period. It never drops.
- Code Design System and Marketing asks reduce to $1k during the build rather than vanishing — they don't actually stop, and pretending they do means doing that work inside the brand budget for free.
- How the table was reached: $13k today is really ~$9k product + $3k code design system + $1k ad-hoc marketing. The DS and marketing money is already brand work with no brand behind it, so it redirects into the build. Incremental ask is therefore small, not $24k of new spend.

## Scope decisions (settled)

- **No custom typefaces.** Arsenal + Geist + one more open-licence face picked in September. $0 licensing. Arsenal is already Yardzen's display face, Geist already runs in product — the book disciplines what exists.
- **Master brand + sub-brand derivation rule + co-branding rules.** Brian's Objective 1 asks for a system flexing across *Clients, Contractors, Partners* — segments, not sub-brands. YardAI / Pros / Build Studio appear nowhere in his brief. The book ships the **rule**; resolved sub-brands are Q1.
- **A compositional system that organises the identity** — Yardzen's equivalent of Topgolf's "Dynamic Grid". This is the answer to distinctiveness and to marketing self-serve.
- **Applications: one representative template per named surface, 8 total.** Brian names surfaces but not depth; Topgolf's reference has ~24 spec'd artifacts across 8 formats. Must be stated explicitly or he'll assume Topgolf.
- **2 revision rounds per stage.** Extras: $2,500/template, $1,500/round.
- **Team line:** "A dedicated brand designer joins the team for this engagement." Present tense, no date, no conditional — Dan is still hiring.
- **Out-of-category references:** Brian left `Fill in . . .` blank. Leave it — that's Brand Foundation, Yardzen's half.

## Two protective terms Dan added

- **Weekly branding review, separate from the product meeting.** Brand decisions need brand deciders in the room, and a review sharing product's agenda gets postponed into a missed deadline.
- **If product scope expands during Oct–Dec, it carries to Q1.** Stops brand work being quietly eaten by product creep.

## RACI (from Brian's brief)

Responsible: Casa Soda · Accountable: **Brian Radics** · Consulted: **Allison, Alicia, Adam** · Informed: **Alison**, Marketing team.
Note: Allison and Alison are two different people.

## Phases — RESOLVED 11 Sep, except Copy

Settled with Dan and against the FigJam board
(https://www.figma.com/file/oJ7qzUikg6yB6zFnr5zYhm, whiteboard):

1. **Phase 1 — Foundations · "the brand"** (presented **Sep 29**)
   Not logo directions. A **15-slide brand guide, designed in the new identity and
   printed**: Mission · Manifesto · How we speak · How we look · How it looks for
   agencies/partners. Minimum text per slide, per the board. Plus the full identity
   underneath it: moodboards, logo architecture, symbol (YZ directions + the
   current Y-in-circle evaluated), lockups, colour, type, graphic elements,
   iconography, art direction, compositional system. Resolved and specified
   through October.
2. **Phase 2 — Copy · "the rules"** — ⚠ STILL OPEN. Dan: *"its another doc i can
   share."* Current content is the best available reading: visual principles
   (photography, AI artwork, humanity, video, cropping), dos and don'ts,
   sub-brand derivation rule, co-branding rules. **Replace once the doc lands.**
3. **Phase 3 — Adaptations · "the templates"** — the 8 templates, then the compiled
   guidelines, source files and asset packs. Product adoption stays in Q1.

**The distinction that makes the money make sense:** September shows you the brand.
It does not yet tell a stranger how to use it, and it does not yet exist on a single
real surface. Without saying that outright, Phase 1 and Phase 2 read as the same
deliverable sold twice, which was the biggest hole the review found.

Money maps as: Foundations $3k Sep + $7k Oct · Copy $7k Nov · Adaptations $7k Dec.

## Board signal worth keeping

Direction stickies from the FigJam, in Dan's words: *color por tipo de plan, sobre
todo en premium* · *people living alive high design and tech* · *YZ as lens* ·
*phones in backyards* · *colorful backgrounds: paintings, photos, grass, nature,
garden elements zoomed in, materiales de jardin de Oldcastle* · *aspirational in a
modern way* · *get Allison tone and voice*. Reference studio: Mouthwash (Seed, Casa).

## Proposed document shape (not yet approved)

Dan wants the case made *before* the number:

1. **Why you need this** — the selling, with the cost of inaction. Longest section.
2. **The three phases** — Foundations → Copy → Adaptations, what lands when
3. **What you get** — full book contents (legally required per Dan)
4. **What it costs** — money mapped onto phases, not months
5. **How we work** — weekly brand review, single approver, Q1 carry rule
6. **Terms** — short

Format still undecided: deck-style HTML→PDF, restructured Google Doc, or both.

## Files here

Three variants, all built from one source. `python3 build.py` regenerates all of
them; edit `build.py`, never the HTML.

- **`build.py`** — the single content source. Shared blocks at the top, then the
  three variants as page lists.
- **`_css.html`** — shared head + house styles.
- **`index.html` → A · The System.** 14pp. Leads with why the standards slip:
  *doing it right is slower than doing it wrong.* Best for Brian as an operator.
- **`b-showcase.html` → B · The Showcase.** 12pp, shortest. Leads with Sep 29 and
  the printed guide. Best for momentum, and built to be presented rather than read.
- **`c-business-case.html` → C · The Business Case.** 14pp. Leads with the money
  shape: most of the $24k is redirected spend, not new spend. Best if the number
  has to survive somebody above Brian.
- `REVIEW.md` — the five review passes and what each one changed.
- `qa.mjs` — page-overflow and grey-copy check. `node qa.mjs *.html`.
- `shot.mjs` — screenshot single pages. `node shot.mjs index.html A 1 5 6`.
- `proposal.md`, `proposal-v2.md` — superseded drafts, kept for the wording.
- `icon-black.png` — Casa Soda mark.

## Two things to fix elsewhere

1. **`soda-quote.md`'s branding anchors are stale.** They top out at $5,500 for a
   full brand system. This engagement is $24,000. The next brand lead gets
   mispriced badly unless that table is redone.
2. **The playbook says Soda sends proposals as live URLs**, not PDFs. This folder
   is A4/PDF because that is what the engagement started as. Worth deciding which
   one Yardzen gets.

## House rules that apply

All black, zero grey copy. DM Sans only. Cut text ~50%. No dev jargon. Screenshot-QA before showing Dan. Drive API mangles HTML tables — headings and paragraphs only in Google Docs, and it cannot edit a doc body after creation, only the title.
