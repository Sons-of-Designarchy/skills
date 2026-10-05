# Handoff: Yardzen PM work (2026-10-05)

PM work moves to the other laptop (no dev servers there). PR / code work stays on the main laptop.
Read `soda-yardzen.md` (section "Work Tracking (Jira boards)") first, then this file.

## How Dan wants it done
- Short answers, action first. No em dashes anywhere (chat, docs, tickets).
- Process docs use roles, never names: Yardzen stakeholder, Soda PM, Soda designer, Soda front-end.
- **Dan edits the ClickUp docs himself.** Before changing a page: read it first, then use `append`. Only use `replace` right after a fresh read, changing just the part asked for.
- Contentful / component tickets get the ClickUp tag `pair with dan`.
- No ticket numbers in code. Jira numbers go in branch, PR title, commits.

## Key places (ClickUp, workspace 90131023048)
| What | ID / link |
|---|---|
| Process doc "Yardzen QA - PM & tasks process" | doc `2ky3mh68-18953`, page `2ky3mh68-19213` |
| Monthly log "Soda x Yardzen: completed work by month" | doc `2ky3mh68-18973`, page October 2026 `2ky3mh68-19233` (empty template) |
| Ticket review for Alicia | doc `2ky3mh68-18893` (pages "Review with Alicia", "Code backlog", "Regionalization") |
| PR Guide | doc `2ky3mh68-18853` |
| Lists | YZ-Product & Marketing `901317911700`, EPICS `901326742650`, MINUTES `901326954036` |
| Folders | Yardzen `901311488510`, Documentación (Docs-2026) `901318687610` |
| Client Drive | https://drive.google.com/drive/folders/1J523tu38ZqfXU4Gzd7WmIMnrKFGg9xl6 |
| Branding epic | task `17tn048ue1t` (4 branding tasks linked, assigned to Valeria) |
| Prep meeting Alicia Mon Oct 5 | task `17tn048ue4g` (MINUTES) |

ClickUp statuses (YZ-Product & Marketing): minutes, backlog, on hold, block, shaping, next up, on going, internal review, in client review, listo para entregar, eng review / handoff, done this quarter (done), ready (closed).

## The process (agreed)
- Jira = what Yardzen sees. YZ Engineering (EN-) if it ends in a PR, YZ Design if it ends in Figma / asset / copy / decision, both linked if design becomes code.
- ClickUp = Soda's internal copy of every Jira ticket (one Jira ticket can be 5 or 6 ClickUp tasks). Internal review happens only in ClickUp.
- Jira moves only when the ClickUp task reaches **in client review**.
- Claude creates the Jira ticket first, then the linked ClickUp copy. PM reviews and assigns.
- Every task that reaches done gets a row in the monthly log.

## Open work (pick up here)
1. **Atlassian access.** Works on the main laptop (cloudId `08e7e050-5173-446b-b5cc-7dc663c43d03`, site yardzen.atlassian.net, project EN = YZ Engineering). Each laptop authenticates its own: `/mcp` → atlassian. EN-6265 has a comment with the "Toll on Trellis" scope (2026-10-05).
2. **Migration from the Slack table.** Dan pastes the Slack table. Build a draft list (board, existing EN- or new, ClickUp copy yes/no, status). Dan reviews. Only then create tickets and links.
3. **Make "done" automatic (Dan doesn't want manual).** Proposal, not built yet:
   - New list `COMPLETED` in the Yardzen folder.
   - ClickUp automation (set in the UI, the API can't create automations): when status changes to `done this quarter` → move task to `COMPLETED`.
   - In `COMPLETED`, a view filtered "Date closed is this month", grouped by month. Embed that view in the monthly log page, so the log fills itself.
   - Clean up now: move the current done tasks out of YZ-Product & Marketing into `COMPLETED`.
   - Confirm with Dan before moving tasks.
4. **City landings** (shaping): pilot task `17tn048ue4j`, local team mockup `17tn048ue4d`, 5 missing landings `17tn048ue4c`, regionalization `17tn048ue4e`. Contentful drafts need manual mode (auto mode blocks Contentful writes). Copy owner to confirm with Alicia.
5. **Affirm show/hide ticket**: Jira text given to Dan, waiting for the EN- number.

## Jira numbers already assigned
EN-6381 My Account button (PR #6509) · EN-6382 reviews badges (PR #6510) · EN-6383 design profile quiz (PR #6342) · EN-6384 reviews automatic vs hand-picked (+ per-review source logo, Google / Houzz) · EN-6265 Toll layout (branch pushed, no PR yet, QA in progress on the main laptop).

## Onboarding on Trellis (code plan, agreed 2026-10-05)
Goal: consistency. Toll onboarding built from Trellis so the layout lives in one place.
- **PR 1 "Toll on Trellis"** (branch EN-6265, being built on the main laptop): BottomActionsBar floating (StepFooter deleted), uploader `size="sm"`, MediaPreview (extracted from uploader + error state, fixes "NoSuchBucket"), SiteInfo (from unused property-confirm-modal), vertical LabeledStepper (StepSidebar deleted), HelpCard on ContentCard (BannerCard deleted, one support contact), AppShell (renamed AdminPageLayout) + SectionShell (OnboardingFlowShell deleted). Standard onboarding unchanged.
- **PR 2 "One onboarding header"** (after PR 1 merges): OnboardingNavbar with slots (logo, center, right), project data in the navbar for both flows; delete CoBrandedHeader and ProjectCard. Touches the standard onboarding in prod: QA both flows at 3 sizes.
- Needs Jira tickets for both (EN-6265 may cover PR 1).
