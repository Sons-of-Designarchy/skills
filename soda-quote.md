# Soda Quote

## On load

Always show the tutorial below first, every single time the skill loads. Then say: "Ready to quote. Paste the transcript (or describe the project) and I'll take it from there."

---

## Tutorial — How we quote at Soda (ELI5)

**Soda. Quoting a project. Today is [current date].**

Quoting at Soda has three moves: understand the project → pick a plan (or build a custom one) → send the number with confidence.

---

### 1. What are we selling?

We sell three things:

| Type | What it is |
|------|------------|
| **Branding** | Logo, identity system, brand guidelines, visual language |
| **Website** | Design + dev of a marketing or product site |
| **Package** | Branding + Website together (better value for client, better project for us) |

If a client asks for something outside these three, it's a **custom scope** — price it line by line.

---

### 2. The plans

We have fixed plans for websites. They anchor the conversation so we're not inventing prices from scratch every time.

| Plan | Who it's for | Starting price |
|------|-------------|----------------|
| **WEBSITE SUPPORT** | Existing site, maintenance or small changes | [ADD PRICE] |
| **EARLY** | Small businesses, first website, simple scope | [ADD PRICE] |
| **MID** | Growing companies, some complexity, clear brand | [ADD PRICE] |
| **SENIOR** | Established brand, complex site, multiple sections | [ADD PRICE] |
| **PRO / ANCHOR** | Enterprise, long-term, highest complexity | [ADD PRICE] |

AI does a lot of the heavy lifting now — that's priced in. We're not charging 2019 rates.

**Addons** are line items on top of any plan:
- [ADD YOUR ADDON LIST — e.g. copywriting, SEO setup, extra pages, animations, etc.]

**Custom quote:** If none of the plans fit, build from scratch using the Excel calculator. List deliverables → estimate hours → multiply by rate → add buffer.

---

### 3. What you need to know before quoting

Before assigning a plan, you need to know:

1. **Project type** — branding, website, or both?
2. **Scope clarity** — do they know what they want, or is it vague?
3. **Number of pages / sections** — for websites
4. **Existing brand?** — do they have one or does it need to be created?
5. **Timeline** — when do they need it? Rush = premium
6. **Who decides?** — are we talking to the decision maker?
7. **Budget signal** — have they mentioned a number? Don't assume.
8. **Tech requirements** — CMS? E-commerce? Custom integrations?

The Figma quiz covers these in the discovery call. Use those answers to lock the plan.

---

### 4. How to use this skill

1. Paste a transcript (audio transcription, WhatsApp, email, notes — anything)
2. I extract all the info I can and create the ClickUp task in **Soda Ventas → Nuevos Leads**
3. I tell you exactly what's missing and ask the right follow-up questions
4. I suggest the best plan match — or flag it as custom with reasoning
5. You answer the questions → I update the task and lock the quote

That's it. Let's go.

---

## Workflow

### Step 1 — Extract from transcript

From any input, extract:
- **Client / company name** → task name
- **Contact person name** → Contact field
- **Email** → Email field
- **Website** → Website field
- **Project type** → branding / website / package / custom
- **Scope description** → what they want, in plain language
- **Timeline** → any deadline or urgency signals
- **Budget signal** → any numbers they mentioned
- **Decision maker?** → yes/no/unclear
- **Tech requirements** → CMS, e-commerce, integrations, etc.
- **Existing brand?** → yes/no/partial

### Step 2 — Create ClickUp task

Create a task in list **Nuevos Leads** (`901324607712`) with:
- Name: client/company name
- Description: structured brief with all extracted info + open questions section
- Custom fields to fill from what you know:
  - `Contact` → contact person name
  - `Email` → email address
  - `Website` → website URL
  - `Notes` → scope summary in 2-3 sentences
  - `Next Step` → "Answer open questions → assign plan"
  - `Plan` → best match from dropdown, or leave blank if custom
  - `Opportunity` → estimated price if plan is assigned

### Step 3 — Flag gaps and ask questions

After creating the task, output a numbered list of specific questions — only what's actually missing. Do not ask about things already in the transcript.

Use this question bank (add the Figma quiz questions here):
- What type of project is this? (if unclear)
- How many pages / sections does the site need?
- Do they have an existing brand identity?
- What's the deadline?
- Is this person the decision maker, or is there someone else?
- Do they have a budget in mind?
- Does the site need a CMS (e.g. Webflow, WordPress)?
- Any e-commerce or custom integrations?
- Are there reference sites they like?
- [ADD FIGMA QUIZ QUESTIONS HERE]

### Step 4 — Suggest a plan

Based on what you know, pick the best plan and explain your reasoning in one sentence. If it's clearly custom, say so and list the line items to build from.

Format:
> **Suggested plan: MID** — Three-section marketing site, existing brand, no CMS complexity, 6-week timeline.
> **Estimated: $[X]** + [addon if any]

or:

> **Custom scope** — Client needs e-commerce + brand creation + 8+ pages. Build from Excel: [list deliverables].

---

## ClickUp field IDs (Nuevos Leads)

| Field | ID |
|-------|----|
| Contact | `1bb97627-7548-4b53-bacc-dbd8035a5ffd` |
| Email | `6c859e6b-2081-4f19-bc0c-3a78795c01b5` |
| Website | `7ee49725-c6ce-4034-96cc-d15f2588176c` |
| Notes | `27eb50da-c850-4a4f-aeba-9d7b6be3a608` |
| Next Step | `61474f35-7134-4bc0-8a46-abb42ff88051` |
| Plan | `3ec2ecdb-5b38-4b7c-99ec-7092c74f008d` |
| Opportunity | `7b53feb4-bc1b-4e73-817a-7c6f17cc3656` |
| Country | `8cf087c6-10ae-4bf0-b97b-8f73832f913f` |
| Next action date | `e35c6261-883f-4539-9a1d-3b2ec36fcaf0` |

**Plan dropdown IDs:**
| Plan name | Option ID |
|-----------|-----------|
| WEBSITE SUPPORT | `a92378c2-24bc-4b80-a472-f80309d8c202` |
| EARLY | `3410cf24-3323-443b-a4be-92b4349c94ce` |
| MID | `e54662c4-f4b4-40ad-8953-615ef17dbe88` |
| SENIOR | `5995772b-56f4-410b-bb46-a6f29fb77d58` |
| PRO / ANCHOR | `fb2978a2-ee2e-4e6d-8a72-b17af71dd325` |

---

## What to fill in next

Before this skill is complete, add:
1. **Plan prices** — replace `[ADD PRICE]` in the tutorial table
2. **Addon list** — replace `[ADD YOUR ADDON LIST]` with real line items
3. **Figma quiz questions** — paste them into the question bank in Step 3
