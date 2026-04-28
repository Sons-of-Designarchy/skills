# Soda Ops Skill
**Trigger:** `/soda-ops` or when user says "transcribe the meeting", "format the meeting notes", "create meeting doc", or pastes raw meeting notes / audio transcript after a design sync.

---

## What This Skill Does

Dan leads a weekly Yardzen design sync. After the meeting he's tired — he pastes raw notes or an audio transcript and wants a clean doc + ClickUp tasks created automatically, with zero friction and no questions.

Steps:
1. Parse the raw input (audio transcript, messy notes, or both)
2. Format into the standard one-pager doc (see template + length rules below)
3. Save to `/Users/danpliego/Desktop/design-sync-YYYY-MM-DD.md`
4. Check ClickUp MINUTES list for an existing task for this date — if one exists, add subtasks under it; if not, create the task first then add subtasks
5. Confirm in one line

---

## Rules

- **Never ask clarifying questions.** Make your best inference and go.
- **One-pager only.** The doc must be readable at a glance — like the April 21 entry (see reference below). No wall of text. No deep nested sections. Bullet points, not paragraphs.
- If a section has nothing to say, omit it entirely.
- Keep all names as-is: Dan/Casa, Alicia, Allison, Jenn/Jennifer, Karla, Said, Federico/Fede, Kendra.
- Dates: `YYYY-MM-DD` in filename, readable format in doc header.
- Action items: plain bullets with owner in parens — no tables.

---

## Format & Length

**Target: fits on one printed page. No headers with `---` dividers. No sub-sections. Short bullets only.**

```
Yardzen design sync — meeting notes [Month DD, YYYY]
Attendees: [list]

[Topic]
- [bullet]
- [bullet]

[Topic 2]
- [bullet]

Status:
[Project] — [status]
[Project] — [status]

Waiting on:
- @[Person] — [what we need from them]
- @[Person] — [blocker or dependency]

Action items ([main owner]):
- [task]
- [task]
```

Rules:
- Max ~40 lines total
- No deep nesting, no tables, no headers with dividers
- "Waiting on" section is mandatory — call out every blocker by person
- Action items: only list what isn't already covered in "Waiting on"
- Cut anything that can be inferred or isn't actionable

---

## ClickUp API

**Token:** `pk_132248519_HWWFGVYPD0RBFJ55VLZMFOURJSZGNA0A`
**Workspace:** `90131023048` (Casa Soda)
**MINUTES list ID:** `901326954036`
**Statuses:** `shaping`, `internal review`, `sent to client`, `close`

**Flow:**
1. Check for existing task: `GET /api/v2/list/901326954036/task`
2. If task exists for this date → use its ID as parent for subtasks
3. If not → `POST /api/v2/list/901326954036/task` with name `DD MONTH YY` (e.g. `28 ABRIL 26`) and description = the formatted notes
4. Create subtasks: `POST /api/v2/list/901326954036/task` with `"parent": "<task_id>"` — one subtask per action item, status `shaping`

**Base URL:** `https://api.clickup.com/api/v2`
**Header:** `Authorization: pk_132248519_HWWFGVYPD0RBFJ55VLZMFOURJSZGNA0A`

---

## Recurring Context

**Regular attendees:** Alicia (PM/lead), Allison (design/brand), Jenn/Jennifer (assets/partnerships), Dan/Casa (UX dev, frontend lead), Karla (design/assets), Said (design components), Federico/Fede (eng), Kendra (growth/copy).

**Naming:** Casa = Dan, Fede = Federico, Yard AI = AI-powered design product, CRH = contractor referral hub, DPQ = design profile quiz.

**Recurring topics:** DPQ / onboarding flow, shop (components + assets), Yardzen for Pros, blog/CRH/website status, Yard AI routing, design system migration, partner data feeds (Outer, Cowboys, Scheller, CB2, Serena & Lily).

---

## Output

- Write file to `/Users/danpliego/Desktop/design-sync-YYYY-MM-DD.md`
- Create/update ClickUp task + subtasks
- Reply: `Done — design-sync-YYYY-MM-DD.md saved + N subtasks added to ClickUp`
- Nothing else.
