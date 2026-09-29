# Tierra de Monte — Project Guide

Part of the Casa Soda skill set. Load alongside `/soda-front` for Dan's workflow, design principles, and communication style.

Shopify theme for tierradmonte (Dawn 15.4 base, heavily customised). Two people work on it:

- **Karla** builds pages and sections by prompting Claude Code. Speed over polish.
- **Dan** does the design layer at the end: cleans, merges duplicates, moves everything onto the tokens.

This file is how the two hand work back and forth without overwriting each other or breaking the live site.

---

## The one thing to never forget

**`main` IS the live site.** The repo (`Sons-of-Designarchy/tierra-de-monte`) is connected to the store through Shopify's GitHub integration. It syncs both ways:

- Anything merged or pushed to `main` goes live within a minute.
- Anything edited in the Shopify admin (theme editor text, images, section order) is committed back to `main` by `shopify[bot]` as "Update from Shopify for theme tierra-de-monte/main".

So: never commit straight to `main`, and always pull before starting, because the admin may have changed templates since your last session.

---

## Setup (once per machine)

```bash
git clone git@github.com:Sons-of-Designarchy/tierra-de-monte.git ~/projects/tierra-de-monte
cd ~/projects/tierra-de-monte
shopify version          # Shopify CLI 3.x — install with: brew install shopify-cli
```

Local preview (opens a browser login the first time):

```bash
shopify theme dev --store <store>.myshopify.com
```

It serves the theme at `http://127.0.0.1:9292` with hot reload, using real store data. It never touches the published theme.

---

## The hand-off loop

```
 Karla builds  ──►  Dan cleans  ──►  preview + approve  ──►  live  ──►  Karla continues
 (karla/<thing>)    (same branch)    (unpublished theme)     (main)     (new branch from main)
```

### 1. Karla — start a piece of work

```bash
cd ~/projects/tierra-de-monte
git checkout main && git pull
git checkout -b karla/<short-name>        # e.g. karla/aliados-page
```

Build by prompting. Preview with `shopify theme dev`. Commit often:

```bash
git add <the files you changed>
git commit -m "aliados: hero slider + comparison table"
git push -u origin karla/<short-name>
```

Then add a line to `HANDOFF.md` (repo root) and tell Dan the branch name. Done means: it works in the preview on desktop and mobile. It does not need to be clean — that's the next step.

### 2. Dan — the clean layer

```bash
git fetch origin
git checkout karla/<short-name>
git merge origin/main                      # pick up any admin edits first
```

Then run the clean pass (checklist below), commit on the same branch, push.

### 3. Preview and approve

Push the branch as an unpublished theme so anyone can open it in a browser:

```bash
shopify theme push --unpublished --theme "preview-<short-name>"
```

Share the preview link. Nothing is live yet.

### 4. Go live

Only when Dan approves:

```bash
git checkout main && git pull
git merge --no-ff karla/<short-name>
git push origin main                        # ← this is the moment it goes live
```

### 5. Karla continues

```bash
git checkout main && git pull
git checkout -b karla/<next-thing>
```

Never keep building on a branch that has already been merged. Start fresh from `main`, so you get Dan's cleaned version.

### Content-only edits

Changing text, images, or section order in the Shopify theme editor is fine at any time. It lands on `main` by itself. That's why step 1 always starts with `git pull`.

---

## Rules for prompting (Karla, paste these into your requests)

These keep the clean layer short. Every rule here exists because breaking it cost hours to undo.

1. **Tokens only.** Colours, radii, spacing, and shadows come from `assets/tdm-foundations.css` (`--tdm-*`) or from the section's colour scheme (`rgb(var(--color-foreground))`, `rgb(var(--color-background))`). No hex codes in CSS. If a colour is missing, ask Dan to add a token.
2. **No new forks.** Need a variation of an existing section? Add a setting or a layout option to it. Never duplicate a section file (`multicolumn-sept2026` is exactly what not to do).
3. **CSS goes in an asset file.** New section → `sections/<name>.liquid` + `assets/section-tdm-<name>.css`, loaded with `{{ 'section-tdm-<name>.css' | asset_url | stylesheet_tag }}`. No `<style>` blocks in the section except the padding snippet.
4. **Settings become custom properties.** Values from the theme editor go on the root element as `style="--thing: {{ section.settings.thing }}px;"` and the CSS reads `var(--thing)`. Nothing else goes in `style=""`.
5. **No `!important`.** If Dawn wins, make the selector more specific with the section's root class.
6. **Mono type = one class.** Add `tdm-mono` to the element (and `tdm-upper` if it should be uppercase). Never write `font-family: "IBM Plex Mono"` or another `@font-face`.
7. **Padding = the snippet.** `{% render 'section-padding', id: section.id, top: section.settings.padding_top, bottom: section.settings.padding_bottom %}` and put `section-{{ section.id }}-padding` on the element.
8. **JavaScript goes in an asset.** Interactive sections use a custom element in `assets/tdm-<name>.js`, not an inline `<script>`.
9. **Don't copy layouts.** A page that needs a different header/footer does not get a copy of `layout/theme.liquid`. Ask Dan.
10. **1px borders, no uppercase by default, fonts in rem not px.**

Short version to paste at the end of any prompt:

> Follow the Tierra de Monte rules in /soda-tdm: tokens from tdm-foundations.css, no hex, no !important, no inline style except custom properties, CSS in assets/section-tdm-*.css, tdm-mono for mono, section-padding snippet, no duplicated sections or layouts.

---

## Dan's clean-pass checklist

Run on every hand-off branch, after merging `origin/main`:

- [ ] New sections that fork an existing one → fold into the original as a setting/layout option, migrate the template JSON, delete the fork.
- [ ] Inline `<style>` → `assets/section-tdm-*.css`, root class instead of `#shopify-section-{{ section.id }}`.
- [ ] Hex / rgba → tokens or scheme colours. Missing token → add to `tdm-foundations.css`.
- [ ] `!important` → removed (or kept with a comment naming the Dawn selector it beats).
- [ ] Inline `<script>` → custom element in `assets/`.
- [ ] Mono / padding / eyebrow → shared classes and snippet.
- [ ] Template JSON still references only section types that exist.
- [ ] `shopify theme check` — no new offenses in touched files.
- [ ] `/screens` at 1280 / 768 / 390 on every page the branch touches.

---

## Map

| Thing | Where |
|---|---|
| Tokens + shared utilities | `assets/tdm-foundations.css` (loaded in `layout/theme.liquid`) |
| Mono font tokens | `layout/theme.liquid` (`--font-mono-*`, single IBM Plex Mono `@font-face`) |
| Section padding | `snippets/section-padding.liquid` |
| Feature (stats / cards / rows) | `sections/tdm-feature.liquid` + `assets/section-tdm-feature.css` |
| Team grid | `blocks/team-grid.liquid` + `blocks/team-member.liquid` + `assets/block-tdm-team.css` |
| Footer overrides | `assets/section-tdm-footer.css` |
| Product extras (buttons, benefits, ingredients) | `snippets/product-extras.liquid` |
| Hand-off log | `HANDOFF.md` |

Colour schemes live in the theme editor (Theme settings → Colors) and in `config/settings_data.json`. Sections pick one with a `color_scheme` setting.

---

## HANDOFF.md format

One line per hand-off, newest on top:

```
2026-09-29 · karla → dan · karla/aliados-page · Aliados page: hero slider, comparison table, slide gallery. Mobile hero looks off.
2026-09-30 · dan → karla · karla/aliados-page · Cleaned + live. Multicolumn Sept 2026 folded into Feature (layout: "gallery").
```
