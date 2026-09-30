# Tierra de Monte — Project Guide

Part of the Casa Soda skill set. Load alongside `/soda-front` for Dan's workflow, design principles, and communication style.

Shopify theme for Tierra de Monte (store `tierra-de-monte.myshopify.com`, Dawn 15.4 base, heavily customised). Two people work on it:

- **Karla** builds pages and sections by prompting Claude Code, and tests the site. Speed over polish.
- **Dan** does the design layer at the end: cleans, merges duplicates, moves everything onto the tokens, and is the only one who publishes.

This file is how the two hand work back and forth without overwriting each other or breaking the live site.

---

## The one thing to never forget

**`main` IS the live site.** The repo (`Sons-of-Designarchy/tierra-de-monte`) is connected to the store through Shopify's GitHub integration. It syncs both ways:

- Anything merged or pushed to `main` goes live within a minute.
- Anything edited in the Shopify admin (theme editor text, images, section order) is committed back to `main` by `shopify[bot]` as "Update from Shopify for theme tierra-de-monte/main".

**Claude never commits, merges or pushes to `main`. Not with "push", not with "sin miedo", not ever.** "Push" always means the current working branch. Only Dan moves work to `main`, himself.

---

## Setup (once per machine)

```bash
git clone git@github.com:Sons-of-Designarchy/tierra-de-monte.git ~/projects/tierra-de-monte
cd ~/projects/tierra-de-monte
git checkout refactor/foundations
shopify version          # Shopify CLI 3.x — install with: brew install shopify-cli
```

Local preview (the first time it asks you to log in to Shopify in the browser; your account needs staff or collaborator access to the store):

```bash
shopify theme dev --store tierra-de-monte.myshopify.com
```

It serves the theme at `http://127.0.0.1:9292` with hot reload, using real store data. It never touches the published theme.

---

## The working loop

There is one shared working branch: **`refactor/foundations`**. Karla builds and tests on it; Dan reviews the result and publishes.

```
 Karla builds + tests  ──►  Dan reviews + cleans  ──►  Dan publishes (main)
 (refactor/foundations)     (same branch)               (only Dan, only when approved)
```

### Karla — every session

```bash
cd ~/projects/tierra-de-monte
git checkout refactor/foundations
git pull                                   # always first: Dan may have pushed a clean pass
shopify theme dev --store tierra-de-monte.myshopify.com
```

Build by prompting. Commit often, push to the branch:

```bash
git add <the files you changed>
git commit -m "aliados: hero slider + comparison table"
git push                                   # goes to refactor/foundations, never main
```

Then add a line to `HANDOFF.md` and tell Dan. Done means: it works in the preview on desktop and mobile. It does not need to be clean — that's Dan's pass.

### Dan — the clean layer

```bash
git checkout refactor/foundations && git pull
git fetch origin && git merge origin/main   # pick up any admin edits first
```

Run the clean-pass checklist below, commit on the branch, push.

### Content-only edits

Changing text, images, or section order in the Shopify theme editor on the live theme lands on `main` by itself. Dan merges `origin/main` into the branch during his pass so nothing is lost.

### Publishing (Dan only)

⚠️ On 2026-09-29 the branch was merged to `main` by mistake (`29cce5a`) and reverted (`93c53d4`). Because of that revert, a plain merge will NOT bring the changes back. The first real publish must be:

```bash
git checkout main && git pull
git revert 93c53d4                          # revert the revert
git merge --no-ff refactor/foundations
git push origin main                        # ← goes live
```

---

## Trying a redesign without touching the real page

Make a copy of the page template with a suffix and open it with `?view=`:

- `templates/page.aliados.json` → the real Aliados page, `/pages/aliados`
- `templates/page.aliados-propuesta.json` → a proposal, `/pages/aliados?view=aliados-propuesta`

Any template whose suffix contains `aliados` gets the Aliados header, footer, favicon and colour scheme. Compare both in the preview; when the proposal wins, copy its sections into the real template.

---

## Rules for prompting (Karla, paste these into your requests)

These keep the clean layer short. Every rule here exists because breaking it cost hours to undo.

1. **Use what exists first.** Before asking for a new section, check the component list below. Need a variation? Add a setting or a style option to the existing section. Never duplicate a section file or a layout.
2. **Tokens only.** Colours, radii, spacing, shadows and reading-text sizes come from `assets/tdm-foundations.css` (`--tdm-*`) or from the section's colour scheme (`rgb(var(--color-foreground))`). No hex codes in CSS. Missing a colour? Ask Dan for a token or a scheme.
3. **CSS goes in an asset file.** New section → `sections/<name>.liquid` + `assets/section-tdm-<name>.css`, loaded with `{{ 'section-tdm-<name>.css' | asset_url | stylesheet_tag }}`. No `<style>` blocks in the section except the padding snippet.
4. **Settings become custom properties.** Editor values go on the root element as `style="--thing: {{ section.settings.thing }}px;"`, CSS reads `var(--thing)`. Nothing else goes in `style=""`.
5. **No `!important`.** If Dawn wins, make the selector more specific with the section's root class.
6. **Shared pieces, not copies:** mono type = `tdm-mono` class (+ `tdm-upper` for uppercase); padding = `section-padding` snippet; eyebrow = `tdm-section-eyebrow` snippet; jump link = `tdm-anchor` snippet; photo behind a section = `tdm-section-background` snippet.
7. **JavaScript goes in an asset** as a custom element in `assets/tdm-<name>.js`, guarded with `customElements.get`, with cleanup in `disconnectedCallback`.
8. **Photos over flat colour.** White page, colour and photography layered on top. Prefer photo cards and photo backgrounds to plain green boxes.
9. **1px borders, no uppercase by default, fonts in rem not px, mobile first (390px).**
10. **Never touch `main`, never copy `layout/theme.liquid`.**

Short version to paste at the end of any prompt:

> Follow the Tierra de Monte rules in /soda-tdm: reuse existing sections and snippets first, tokens from tdm-foundations.css, no hex, no !important, no inline style except custom properties, CSS in assets/section-tdm-*.css, JS as a guarded custom element in assets, no duplicated sections or layouts, never commit to main.

---

## Components you can use

| Section (editor name) | File | What it's for |
|---|---|---|
| Feature | `sections/tdm-feature.liquid` | Lead copy + stats / icon cards / clickable rows (layout picker) |
| Tarjetas | `sections/tdm-card-grid.liquid` | Card grid. `card_media_style`: icon (default), photo_top, photo_bg; `photo_ratio`; per-card `photo` |
| Impacto | `sections/tdm-impact.liquid` | High-impact band: photo background, 2–4 big stats or a diagram, CTA |
| Detail spotlight | `sections/tdm-detail-spotlight.liquid` | Product/detail gallery with spotlight |
| Scroll steps | `sections/tdm-scroll-steps.liquid` | Numbered process that pins while scrolling |
| Hero slider | `sections/hero-slider.liquid` | Multi-slide hero with overlay and two CTAs |
| Hero overlay card | `sections/hero-overlay-card.liquid` | Single photo hero with a floating card |
| Slide gallery | `sections/slide-gallery.liquid` | Intro + Dawn slideshow |
| Tabla comparativa | `sections/comparison-table.liquid` | Plan/level comparison table |
| Ticker | `sections/ticker.liquid` | Infinite text marquee |
| Logo bar, Reviews, Grid gallery, Tabbed collections, Blog nav, Rich text + logo | `sections/…` | As named |
| Team grid | `blocks/team-grid.liquid` + `blocks/team-member.liquid` | Team members as blocks |

Photo background (`bg_image`, `bg_image_mobile`, `bg_overlay`, `bg_position`) is available on: Feature, Tarjetas, Impacto, Rich text, Tabla comparativa, Collapsible content. With a photo, pick a dark scheme so text is white.

| Snippet | Use |
|---|---|
| `section-padding` | Section top/bottom padding (75% on mobile) |
| `tdm-section-eyebrow` | Small label + rule above a section |
| `tdm-anchor` | Jump target: set "ID de ancla", link to `/pages/…#id` |
| `tdm-section-background` | Photo + scrim behind a section (see its comment for the settings to copy) |
| `product-extras` | Product page: safety/datasheet buttons, benefits, ingredients |

### Colour schemes

- **Blanco** (`scheme-tdm-blanco`) — white, dark-green text. The base for Aliados.
- **Crema** (`scheme-tdm-crema`) — warm off-white, for rhythm between white sections.
- Mint `#B2D286` and dark green `#003118` schemes — accents, used on purpose, not as the page base.

Aliados page-wide settings: Theme settings → **Aliados (landing)** (base scheme, favicon, full-opacity reading text).

---

## Dan's clean-pass checklist

Run on every hand-off, after merging `origin/main` into the branch:

- [ ] New sections that fork an existing one → fold into the original as a setting/style option, migrate the template JSON, delete the fork.
- [ ] Inline `<style>` → `assets/section-tdm-*.css`, root class instead of `#shopify-section-{{ section.id }}`.
- [ ] Hex / rgba → tokens or scheme colours. Missing token → add to `tdm-foundations.css`.
- [ ] `!important` → removed (or kept with a comment naming the Dawn selector it beats).
- [ ] Inline `<script>` → custom element in `assets/`.
- [ ] Hardcoded ids/files in `layout/theme.liquid` → theme settings.
- [ ] Mono / padding / eyebrow / anchor / background → shared classes and snippets.
- [ ] Template JSON still references only section types that exist.
- [ ] `shopify theme check` — no new offenses in touched files.
- [ ] `/screens` at 1280 / 768 / 390 on every page the branch touches.

---

## Map

| Thing | Where |
|---|---|
| Tokens + shared utilities | `assets/tdm-foundations.css` (loaded in `layout/theme.liquid`) |
| Mono font tokens | `layout/theme.liquid` (`--font-mono-*`, single IBM Plex Mono `@font-face`) |
| Aliados header/footer switch | `layout/theme.liquid` (`is_aliados`, suffix contains `aliados`) |
| Footer overrides | `assets/section-tdm-footer.css` |
| Hand-off log | `HANDOFF.md` (repo root) |

---

## HANDOFF.md format

One line per hand-off, newest on top:

```
2026-09-29 · karla → dan · refactor/foundations · Aliados: spotlight + scroll steps. Mobile hero looks off.
2026-09-30 · dan → karla · refactor/foundations · Clean pass + photo proposal (?view=aliados-propuesta). Pull.
```
