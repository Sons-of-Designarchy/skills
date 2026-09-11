#!/usr/bin/env python3
"""
Builds the three Yardzen Brand Book proposal variants from one content source.

  python3 build.py          -> index.html (A), b-showcase.html, c-business-case.html

House rules: all black, zero grey copy, DM Sans only, 1px rules, A4 sheets.
Export:  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
           --headless=new --disable-gpu --no-pdf-header-footer \
           --print-to-pdf=NAME.pdf "file://$PWD/NAME.html"
"""

CSS = open("_css.html").read()

def doc(title, pages):
    head = CSS.replace("{{TITLE}}", title)
    return head + "\n<body>\n\n" + "".join(pages) + "</body>\n</html>\n"

def sheet(inner, n=None, doc_label="Yardzen · Brand Book 2026"):
    p = f'\n  <div class="pnum">{n}</div>' if n else ""
    return (f'<div class="sheet">\n  <div class="head">\n    <div class="wm">Casa Soda</div>\n'
            f'    <div class="doc">{doc_label}</div>\n  </div>\n  <div class="line thick"></div>\n'
            f'{inner}{p}\n</div>\n\n')

# ══════════════════════════════════════════════════════════════════
# SHARED BLOCKS
# ══════════════════════════════════════════════════════════════════

COVER = '''<div class="sheet">
  <div class="head">
    <div class="wm">Casa Soda</div>
    <div class="doc">Proposal · 11 Sep 2026</div>
  </div>
  <div class="line thick"></div>
  <div class="title">
    <div class="eyebrow">Yardzen · Visual Identity System</div>
    <h1>Brand<br>Book<br>2026</h1>
  </div>
  <div class="line"></div>
  <p class="cover-lead">{{LEAD}}</p>
  <div class="line"></div>
  <div class="info">
    <div class="cell"><div class="k">Prepared for</div><div class="v">Brian Radics · Yardzen</div></div>
    <div class="cell"><div class="k">Prepared by</div><div class="v">Daniel Pliego · Casa Soda</div></div>
  </div>
  <div class="line"></div>
  <div class="info">
    <div class="cell"><div class="k">Engagement</div><div class="v">Three phases · Sep to Dec 2026</div></div>
    <div class="cell"><div class="k">Investment</div><div class="v">$24,000 USD</div></div>
  </div>
  <div class="line thick"></div>
  <div class="foot">
    <div class="sal">Casa Soda</div>
    <div class="contact"><span>Mexico City</span><span>hola@casasoda.com</span><span>+52 55 1026 5196</span></div>
  </div>
</div>

'''

PROBLEM = sheet('''  <div class="sec">Why now</div>
  <h2 class="big">The brand isn't held to the standard the work is.</h2>
  <p>Your brief says it plainly:</p>
  <div class="quote">"Erosion of the brand equity due to a lack of adherence to standards: inconsistent font usage, varying tones of voice, lack of brand breakthrough, and brand visuals that lack the quality standards expected."</div>
  <p>Yardzen delivers world-class landscape design every week. The brand around it doesn't present at that level, and you have already connected that gap to revenue: <b>more brand quality means more leads and more design purchases.</b></p>
  <div class="line"></div>
  <h3>Nobody is ignoring the brand. There's nothing to follow.</h3>
  <p>Every marketing request today is answered from scratch. Someone picks a typeface, chooses a crop, guesses a colour. Some of it lands on brand. Some of it doesn't. All of it costs a designer.</p>
  <p class="big"><b>The standards slip because doing it right is slower than doing it wrong.</b></p>
  <p>That's a system problem, not a discipline problem, and it doesn't improve on its own.</p>''')

TODAY_AFTER = '''  <div class="sec">What changes</div>
  <h2 class="big">From every request<br>starting at zero</h2>
  <table>
    <tr><th>Today</th><th class="brand" style="text-align:left">After</th></tr>
    <tr><td>Every request starts from zero</td><td style="text-align:left"><b>The right answer is the fastest one</b></td></tr>
    <tr><td>Marketing needs a designer to stay on brand</td><td style="text-align:left"><b>Marketing fills a template and stays on brand</b></td></tr>
    <tr><td>A new partner or segment is a new design project</td><td style="text-align:left"><b>A new partner is a rule already written down</b></td></tr>
    <tr><td>"Is this on brand?" is a matter of opinion</td><td style="text-align:left"><b>It's a matter of checking</b></td></tr>
    <tr><td>Quality depends on who picked up the ticket</td><td style="text-align:left"><b>Quality is the floor, not the ceiling</b></td></tr>
  </table>'''

PHASES_TABLE = '''  <table>
    <tr><th>Phase</th><th style="text-align:left">What it answers</th><th>Lands</th></tr>
    <tr><td><b>1 · Foundations</b></td><td style="text-align:left"><b>The brand.</b> What Yardzen looks like, printed</td><td><b>Sep 29</b></td></tr>
    <tr><td><b>2 · Copy</b></td><td style="text-align:left"><b>The rules.</b> How anyone else uses it</td><td>End of Nov</td></tr>
    <tr><td><b>3 · Adaptations</b></td><td style="text-align:left"><b>The templates.</b> It applied to real surfaces</td><td>December</td></tr>
  </table>'''

SEP29 = sheet('''  <div class="sec">Phase 1 · Foundations</div>
  <h2 class="big">September 29:<br>the brand,<br>printed.</h2>
  <p class="big">We don't present a logo on a white page.</p>
  <p>The first deliverable is <b>a 15-slide brand guide, designed in the new identity and printed</b>. It's the guide and the proof at the same time: the identity doing its actual job, in your hands, not an artifact in isolation.</p>
  <div class="line"></div>
  <div class="numrow"><div class="n">01</div><div class="t"><b>Mission</b>Who Yardzen is for and what it's for.</div></div>
  <div class="numrow"><div class="n">02</div><div class="t"><b>Manifesto</b>What Yardzen believes, said in Yardzen's voice.</div></div>
  <div class="numrow"><div class="n">03</div><div class="t"><b>How we speak</b>Tone of voice, designed from Yardzen's own source material.</div></div>
  <div class="numrow"><div class="n">04</div><div class="t"><b>How we look</b>The identity: marks, colour, type, elements, art direction.</div></div>
  <div class="numrow"><div class="n">05</div><div class="t"><b>How it looks for partners</b>How the brand holds up when somebody else is holding it.</div></div>
  <div class="line"></div>
  <p class="tnote">Minimum text per slide, by design. A guide nobody reads is a guide nobody follows. It gets presented September 29, then resolved and specified through October.</p>
  <div class="line"></div>
  <p class="big"><b>This shows you the brand. It doesn't yet tell a stranger how to use it.</b></p>
  <p>That's the difference between Phase 1 and Phase 2, and it's worth being exact about. September hands you the identity, made real. November hands your teams, your contractors and your partners the rules that let them apply it without a designer in the room. They're two different documents doing two different jobs.</p>''')

DELIVERABLES_1 = sheet('''  <div class="sec">Deliverables · Phase 1</div>
  <h2 class="big">Foundations</h2>
  <p class="tnote" style="padding-bottom:10px">Everything named here's included in the $24,000. Anything not named here's a change order.</p>
  <table class="deliv">
    <tr><th style="text-align:left">Item</th><th style="text-align:left">Exactly what</th><th>Count</th></tr>
    <tr><td><b>Brand guide</b></td><td style="text-align:left">Designed and printed, in the new identity</td><td><b>15 slides</b></td></tr>
    <tr><td><b>Moodboards</b></td><td style="text-align:left">Style direction and territories, with the argument for each</td><td>3 routes</td></tr>
    <tr><td><b>Logo architecture</b></td><td style="text-align:left">The full system of marks and how they relate</td><td>1 system</td></tr>
    <tr><td><b>Symbol</b></td><td style="text-align:left">YZ explored in multiple directions, plus the current Y-in-circle evaluated standalone and beside the wordmark</td><td>1 chosen</td></tr>
    <tr><td><b>Lockups</b></td><td style="text-align:left">Primary, secondary, vertical · safe areas · minimum sizes · placement · dos and don'ts</td><td>3 lockups</td></tr>
    <tr><td><b>Colour system</b></td><td style="text-align:left">HEX, RGB, CMYK and Pantone values · usage ratios · the rule for deriving new accents</td><td>1 palette</td></tr>
    <tr><td><b>Typography</b></td><td style="text-align:left">Arsenal, Geist and one further open-licence face · type scale · lockups · casing rules</td><td>3 faces</td></tr>
    <tr><td><b>Graphic elements</b></td><td style="text-align:left">The proprietary devices that make a layout recognisably Yardzen at a glance</td><td>1 set</td></tr>
    <tr><td><b>Iconography</b></td><td style="text-align:left">Style definition plus a core set</td><td>1 set</td></tr>
    <tr><td><b>Art direction</b></td><td style="text-align:left">How the parts compose into a consistent world</td><td>1 system</td></tr>
    <tr><td><b>Compositional system</b></td><td style="text-align:left">The grid, headline zones, CTA placement, contextual type usage</td><td>1 system</td></tr>
  </table>
  <p class="tnote"><b>The compositional system is the one to watch.</b> It's what makes the identity a system rather than a style sheet, and it's the reason marketing can eventually self-serve.</p>''')

DELIVERABLES_2 = sheet('''  <div class="sec">Deliverables · Phase 2</div>
  <h2 class="big">Copy</h2>
  <p class="big">What are the rules, in writing.</p>
  <p>A system nobody can read is a system nobody can follow. This phase is the written document, made so it can be handed to someone and used without a briefing.</p>
  <p><b>Half of it already exists.</b> Your Tone and Voice Guide is done, and it's good: brand voice against human voice, split again by whether someone has paid. It's specific in the way this whole book needs to be. That guide doesn't get rewritten. It gets a face, and the visual rules get written to sit beside it at the same standard.</p>
  <table class="deliv">
    <tr><th style="text-align:left">Item</th><th style="text-align:left">Exactly what</th><th>Count</th></tr>
    <tr><td><b>Visual principles</b></td><td style="text-align:left">Photography · AI-generated artwork · the role of humanity · video · angles and cropping</td><td>5 sections</td></tr>
    <tr><td><b>Dos and don'ts</b></td><td style="text-align:left">Written for a contractor, a partner, or a marketing hire in their first week</td><td>Per section</td></tr>
    <tr><td><b>Sub-brand rule</b></td><td style="text-align:left">How a future sub-brand takes its colour and lockup from the master brand, without a new design project each time</td><td>1 rule</td></tr>
    <tr><td><b>Co-branding rules</b></td><td style="text-align:left">How Yardzen sits beside a partner's mark, so partner work stops being negotiated case by case</td><td>1 rule</td></tr>
  </table>
  <div class="line"></div>
  <p><b>The book ships the rule, not the sub-brands.</b> Resolving named sub-brands into finished identities is separate work, and it's the natural first job of Q1. The rule has to exist before anything can be derived from it.</p>''')

DELIVERABLES_3 = sheet('''  <div class="sec">Deliverables · Phase 3</div>
  <h2 class="big">Adaptations</h2>
  <p class="big">What does it look like applied.</p>
  <p>One complete, editable, specified template for each named surface. <b>Eight in total.</b></p>
  <table class="deliv">
    <tr><th style="text-align:left">Surface</th><th style="text-align:left">Surface</th></tr>
    <tr><td>Website</td><td style="text-align:left">Mailers</td></tr>
    <tr><td>Advertising</td><td style="text-align:left">Partner decks</td></tr>
    <tr><td>Social media</td><td style="text-align:left">Signage</td></tr>
    <tr><td>Paid digital media</td><td style="text-align:left">Apparel and swag</td></tr>
  </table>
  <p class="tnote"><b>What "one template per surface" means.</b> Each is a complete, specified, editable design: the pattern every future piece on that surface is built from. It isn't every size, format or variant a surface will eventually need. Additional templates are $2,500 each and are natural Q1 work.</p>
  <div class="line"></div>
  <h3>Then the handoff</h3>
  <table class="deliv">
    <tr><td><b>Brand Guidelines</b></td><td style="text-align:left">The complete document, compiled</td><td>PDF</td></tr>
    <tr><td><b>Source files</b></td><td style="text-align:left">Editable, organised, yours</td><td>Figma</td></tr>
    <tr><td><b>Asset packs</b></td><td style="text-align:left">Logo and elements exported in the formats each surface needs</td><td>SVG · PNG · EPS</td></tr>
  </table>''')

OBJECTIVES = sheet('''  <div class="sec">Your brief, answered</div>
  <h2 class="big">Five objectives,<br>five answers</h2>
  <p>You set these. Here's what in this proposal answers each one.</p>
  <div class="numrow"><div class="n">01</div><div class="t"><b>Consistency at scale</b>A flexible system that adapts across Clients, Contractors and Partners without fragmenting. Answered by the compositional system and the co-branding rules.</div></div>
  <div class="numrow"><div class="n">02</div><div class="t"><b>Distinctiveness</b>Proprietary, recognisable assets. Answered by the graphic elements and the symbol, not by a logo on a page.</div></div>
  <div class="numrow"><div class="n">03</div><div class="t"><b>Elevated perception</b>A premium, design-led identity that makes the promise of a premium landscape credible before anyone reads a word. Answered by the art direction and the visual principles.</div></div>
  <div class="numrow"><div class="n">04</div><div class="t"><b>Instill intent</b>An art direction that associates Yardzen with aspiration, outdoor living and transformation. Answered by the photography and imagery principles.</div></div>
  <div class="numrow"><div class="n">05</div><div class="t"><b>Lifestyle brand community</b>A mark with enough character that people will wear it and identify with it. Answered by the symbol, designed to work on a hat as well as a header.</div></div>
  <div class="line"></div>
  <p class="tnote"><b>On depth.</b> Your quality reference is the Topgolf book, which specifies roughly 24 artifacts across 8 formats. This engagement delivers <b>one complete template for each of 8 surfaces</b>, plus the system and rules to produce the rest. Additional templates are $2,500 each.</p>''')

MONEY = sheet('''  <div class="sec">Investment</div>
  <h2 class="big">$24,000 USD<br>Fixed scope.</h2>
  <p class="big"><b>Most of it isn't new spend.</b></p>
  <p>Yardzen already funds design system and marketing work every month. That work is brand work with no brand behind it. During the build, it points at the book instead.</p>
  <table>
    <tr><th>Line</th><th>August</th><th>September</th><th>Oct–Dec <i>each</i></th><th>Q1</th></tr>
    <tr><td>Product</td><td>$9k</td><td>$9k</td><td>$9k</td><td>$9k</td></tr>
    <tr><td>Code Design System</td><td>$3k</td><td>$3k</td><td>$1k</td><td>$1k</td></tr>
    <tr><td>Marketing asks</td><td>$1k</td><td>—</td><td>$1k</td><td>$1k</td></tr>
    <tr><td class="brand">Brand</td><td class="brand">—</td><td class="brand">$3k</td><td class="brand">$7k</td><td class="brand">$4k</td></tr>
    <tr class="total"><td>Yardzen pays</td><td>$13k</td><td>$15k</td><td>$18k</td><td>$15k</td></tr>
  </table>
  <p class="tnote"><b>The incremental ask is the difference between those bottom numbers, not $24,000 of new spend.</b> Q1 is shown as direction, not commitment. It gets scoped once the book exists.</p>
  <div class="line"></div>
  <h3>Product doesn't pay for this</h3>
  <p><b>Product holds at $9k in every period.</b> It never drops to fund the brand work. A dedicated brand designer joins the team for this engagement and Said leads brand execution. Casa Soda is adding capacity, not moving your product hours onto a brand book.</p>''')

FITS = sheet('''  <div class="sec">How it fits</div>
  <h2 class="big">Two decisions that save money</h2>
  <h3>We deliberately don't repaint the product yet</h3>
  <p>An unreleased brand should not be applied to live product UI.</p>
  <p>Through the build we align the <b>structure</b> of the design tokens to the incoming brand and flag conflicts. We don't restyle the product against a system still under review, because applying it early means doing it twice.</p>
  <p>That adoption is what Q1 is for. It lands in the product once it's approved, not while it's being decided.</p>
  <div class="line"></div>
  <h3>No custom typefaces</h3>
  <p>Arsenal is already your display face. Geist already runs in the product. The book disciplines what exists rather than replacing it, and one further open-licence face gets selected in September.</p>
  <p class="big"><b>$0 in licensing.</b></p>''')

OWNERSHIP = sheet('''  <div class="sec">Ownership</div>
  <h2 class="big">Two halves,<br>two owners</h2>
  <table>
    <tr><th>Yardzen owns · Brand Foundation</th><th style="text-align:left">Casa Soda owns · Visual Identity</th></tr>
    <tr><td>Vision and mission</td><td style="text-align:left">Core visual identity</td></tr>
    <tr><td>Target audience</td><td style="text-align:left">Visual principles</td></tr>
    <tr><td>Positioning and comms platform</td><td style="text-align:left">Applications</td></tr>
    <tr><td>Tone of voice</td><td style="text-align:left">Guidance and governance</td></tr>
    <tr><td>Out-of-category references</td><td style="text-align:left">Compiling the book</td></tr>
  </table>
  <p class="tnote"><b>Brand Foundation is needed by end of September.</b> The Sep 29 guide designs Yardzen's own words, so mission, manifesto and voice have to exist as source material for it to set them. If Foundation is late, Phase 1 compresses.</p>
  <div class="line"></div>
  <h3>One approver</h3>
  <div class="kv"><div class="kk">Responsible</div><div class="vv">Casa Soda</div></div>
  <div class="kv"><div class="kk">Accountable</div><div class="vv"><b>Brian Radics</b></div></div>
  <div class="kv"><div class="kk">Consulted</div><div class="vv">Allison, Alicia, Adam</div></div>
  <div class="kv"><div class="kk">Informed</div><div class="vv">Alison, Marketing</div></div>
  <p class="tnote" style="padding-top:12px"><b>A visual identity reviewed by committee converges on the least objectionable option</b>, which is the opposite of the distinctiveness the brief asks for. Consultation at every stage. The decision sits in one place.</p>''')

WORKING = sheet('''  <div class="sec">Working together</div>
  <h2 class="big">How we work</h2>
  <div class="numrow"><div class="n">01</div><div class="t"><b>A weekly brand review, separate from the product meeting.</b>Brand decisions need brand deciders in the room, and a review sharing product's agenda is a review that gets postponed. On a fixed schedule that turns into a missed date.</div></div>
  <div class="numrow"><div class="n">02</div><div class="t"><b>If product scope grows during the build, it carries to Q1.</b>It doesn't get absorbed alongside a fixed-date deliverable.</div></div>
  <div class="numrow"><div class="n">03</div><div class="t"><b>Two revision rounds per phase.</b>A round is one consolidated set of feedback from the approver, not opinions arriving separately.</div></div>
  <div class="line"></div>
  <div class="sec">Terms</div>
  <div class="kv"><div class="kk">Fee</div><div class="vv"><b>$24,000 USD</b>, fixed scope</div></div>
  <div class="kv"><div class="kk">Schedule</div><div class="vv">$3k September · $7k Oct, Nov, Dec</div></div>
  <div class="kv"><div class="kk">Billing</div><div class="vv">50% at start of month, 50% on approval</div></div>
  <div class="kv"><div class="kk">Revisions</div><div class="vv">2 rounds per phase · additional $1,500</div></div>
  <div class="kv"><div class="kk">Extra templates</div><div class="vv">$2,500 each</div></div>
  <div class="kv"><div class="kk">Intellectual property</div><div class="vv">Transfers to Yardzen on final payment</div></div>
  <div class="kv"><div class="kk">Product retainer</div><div class="vv">Separate line, unaffected</div></div>
  <div class="kv"><div class="kk">If either side stops</div><div class="vv">30 days' notice · completed phases settled, nothing further owed</div></div>
  <p class="tnote" style="padding-top:12px"><b>What we need from you:</b> Brand Foundation by end of September · one approver · consolidated feedback within five working days · access to the photography library · attendance at the weekly review.</p>''')

def CLOSE(final_line):
    return f'''<div class="sheet">
  <div class="head">
    <div class="wm">Casa Soda</div>
    <div class="doc">Yardzen · Brand Book 2026</div>
  </div>
  <div class="line thick"></div>
  <div class="sec">After the book</div>
  <h2 class="big">A brand book that's delivered and not adopted has changed nothing.</h2>
  <p>Q1 is where it stops being a document.</p>
  <div class="numrow"><div class="n">Adoption</div><div class="t">The identity implemented in the product. Tokens updated from structure to values, components restyled, the code design system brought onto the approved brand. This is the work deliberately held back during the build.</div></div>
  <div class="numrow"><div class="n">Expansion</div><div class="t">Sub-brands derived through the rule the book establishes. More templates for the surfaces marketing uses most.</div></div>
  <div class="line"></div>
  <div class="info">
    <div class="cell"><div class="k">Brand Book 2026</div><div class="v">$24,000 USD</div></div>
    <div class="cell"><div class="k">First presentation</div><div class="v">September 29, 2026</div></div>
  </div>
  <div class="line"></div>
  {final_line}
  <div class="line"></div>
  <div class="sec">What happens next</div>
  <div class="kv"><div class="kk">You</div><div class="vv">Approve the scope, or tell me what to change</div></div>
  <div class="kv"><div class="kk">Casa Soda</div><div class="vv">Territories and moodboards start the same week</div></div>
  <div class="kv"><div class="kk">Yardzen</div><div class="vv">Brand Foundation to us by <b>September 30</b></div></div>
  <div class="kv"><div class="kk">Together</div><div class="vv">First presentation <b>September 29</b></div></div>
  <div class="foot">
    <div class="line thick" style="margin-bottom:18px"></div>
    <div class="sal">Thank you</div>
    <div class="name">Daniel Pliego <span>Casa Soda</span></div>
    <div class="contact"><span>Mexico City</span><span>+52 55 1026 5196</span><span>hola@casasoda.com</span></div>
    <div class="visit">See our work at <a href="https://casasoda.com">casasoda.com</a></div>
  </div>
</div>

'''

# ══════════════════════════════════════════════════════════════════
# VARIANT A — THE SYSTEM.  Leads with why the standards slip.
# ══════════════════════════════════════════════════════════════════
A = [
  COVER.replace("{{LEAD}}", "A visual identity for Yardzen, designed, written down, and applied, so every team can use it without asking anyone's permission."),
  PROBLEM,
  OBJECTIVES,
  sheet(TODAY_AFTER + '''
  <div class="line"></div>
  <h3>What we're actually building</h3>
  <p>Not a logo. Not a PDF that gets saved and never opened.</p>
  <p class="big"><b>A system that makes the on-brand version the easy version</b>, so the people asking for work stop needing us in the room to get it right.</p>'''),
  sheet('''  <div class="sec">The work</div>
  <h2 class="big">Three phases</h2>
  <p>We run this in phases rather than calendar months. Each is approved before the next begins.</p>
''' + PHASES_TABLE + '''
  <div class="line"></div>
  <h3>The brand. The rules. The templates.</h3>
  <p><b>Foundations</b> settles what Yardzen looks like, and proves it by printing the brand guide in the new identity itself.</p>
  <p><b>Copy</b> turns that into rules somebody who wasn't in the room can follow.</p>
  <p><b>Adaptations</b> shows it working on the eight surfaces marketing actually uses, then hands everything over.</p>
  <p class="tnote"><b>Why the last two are not one phase.</b> September shows you the brand. It doesn't yet tell a stranger how to apply it, and it doesn't yet exist on a single real surface. Those are separate jobs and they're where the work actually is.</p>'''),
  SEP29, DELIVERABLES_1, DELIVERABLES_2, DELIVERABLES_3,
  MONEY, FITS, OWNERSHIP, WORKING,
  CLOSE('''<p>The brief asks for a distinctive, design-led brand worthy of the landscape work behind it. That ambition is reachable, because the raw material already exists in the projects Yardzen delivers every week.</p>
  <p class="big"><b>What's missing is the system that presents them to one standard.</b></p>'''),
]

# ══════════════════════════════════════════════════════════════════
# VARIANT B — THE SHOWCASE.  Leads with Sep 29. Shortest.
# ══════════════════════════════════════════════════════════════════
B = [
  COVER.replace("{{LEAD}}", "On September 29 you're holding the Yardzen brand guide, printed in the new identity. Everything after that's making it usable by everyone else."),
  SEP29,
  sheet('''  <div class="sec">Why this first</div>
  <h2 class="big">Judge it doing its job, not on a white page.</h2>
  <p>A logo presented in isolation tells you almost nothing about whether the brand works. A printed guide, set in the new type, on the new colour, laying out Yardzen's own mission and manifesto, tells you everything.</p>
  <p class="big"><b>It's the fastest way to find what doesn't work, while it's still cheap to change.</b></p>
  <div class="line"></div>
''' + TODAY_AFTER),
  sheet('''  <div class="sec">The work</div>
  <h2 class="big">Then two more phases</h2>
''' + PHASES_TABLE + '''
  <div class="line"></div>
  <p><b>Copy</b> turns the identity into rules somebody who wasn't in the room can follow: visual principles, dos and don'ts, and the rules for sub-brands and partners.</p>
  <p><b>Adaptations</b> builds one complete template for each of the eight surfaces marketing actually uses, then hands over the compiled guidelines, the source files and the asset packs.</p>
  <div class="line"></div>
  <h3>Nobody is ignoring the brand. There's nothing to follow.</h3>
  <p>Every marketing request today is answered from scratch, which is why the standards slip. <b>Doing it right is currently slower than doing it wrong.</b> That's a system problem, and it doesn't improve on its own.</p>'''),
  OBJECTIVES,
  DELIVERABLES_1, DELIVERABLES_2, DELIVERABLES_3,
  MONEY, OWNERSHIP, WORKING,
  CLOSE('''<p class="big"><b>The raw material already exists in the projects Yardzen delivers every week. What's missing is the system that presents them to one standard.</b></p>'''),
]

# ══════════════════════════════════════════════════════════════════
# VARIANT C — THE BUSINESS CASE.  Leads with the money shape.
# ══════════════════════════════════════════════════════════════════
C = [
  COVER.replace("{{LEAD}}", "A complete visual identity for Yardzen. Most of it's funded by redirecting spend that already goes out every month."),
  sheet('''  <div class="sec">The ask</div>
  <h2 class="big">$24,000, and most of it isn't new spend.</h2>
  <p>Yardzen already pays for a code design system and ad-hoc marketing work every month. <b>That's brand work with no brand behind it.</b> During the build it points at the book instead.</p>
  <table>
    <tr><th>Line</th><th>August</th><th>September</th><th>Oct–Dec <i>each</i></th><th>Q1</th></tr>
    <tr><td>Product</td><td>$9k</td><td>$9k</td><td>$9k</td><td>$9k</td></tr>
    <tr><td>Code Design System</td><td>$3k</td><td>$3k</td><td>$1k</td><td>$1k</td></tr>
    <tr><td>Marketing asks</td><td>$1k</td><td>—</td><td>$1k</td><td>$1k</td></tr>
    <tr><td class="brand">Brand</td><td class="brand">—</td><td class="brand">$3k</td><td class="brand">$7k</td><td class="brand">$4k</td></tr>
    <tr class="total"><td>Yardzen pays</td><td>$13k</td><td>$15k</td><td>$18k</td><td>$15k</td></tr>
  </table>
  <p class="tnote"><b>The incremental ask is the difference between those bottom numbers.</b> Peak is $18k a month for three months, against $13k today. Q1 is direction, not commitment.</p>
  <div class="line"></div>
  <h3>Product doesn't pay for this</h3>
  <p><b>Product holds at $9k in every period.</b> A dedicated brand designer joins for this engagement and Said leads brand execution. Casa Soda is adding capacity, not moving your product hours onto a brand book.</p>'''),
  PROBLEM,
  OBJECTIVES,
  sheet(TODAY_AFTER + '''
  <div class="line"></div>
  <h3>Where the return is</h3>
  <p>You have already made the revenue argument yourself: <b>better brand design means more client leads and more design purchases.</b></p>
  <p>The operating saving is separate and more immediate. Every marketing request currently consumes design time because there's no template to reach for. The eight application templates in Phase 3 are the permanent answer to work that's re-invented every time it's asked for.</p>'''),
  sheet('''  <div class="sec">The work</div>
  <h2 class="big">Three phases</h2>
  <p>Phases rather than calendar months, each approved before the next begins.</p>
''' + PHASES_TABLE + '''
  <div class="line"></div>
  <h3>You see it working on September 29</h3>
  <p>The first deliverable is <b>a 15-slide brand guide, designed in the new identity and printed</b>. Not a logo on a white page. The identity doing its job, in your hands, three weeks from signature.</p>'''),
  SEP29, DELIVERABLES_1, DELIVERABLES_2, DELIVERABLES_3,
  FITS, OWNERSHIP, WORKING,
  CLOSE('''<p>The brief asks for a distinctive, design-led brand worthy of the landscape work behind it. That ambition is reachable, because the raw material already exists in the projects Yardzen delivers every week.</p>
  <p class="big"><b>What's missing is the system that presents them to one standard.</b></p>'''),
]

def number(pages):
    out = [pages[0]]
    for i, p in enumerate(pages[1:], start=1):
        out.append(p.replace("</div>\n\n", f'  <div class="pnum">{i:02d}</div>\n</div>\n\n', 1)
                   if False else p)
    return pages

for name, pages, title in [
    ("index.html", A, "Casa Soda — Yardzen Brand Book 2026"),
    ("b-showcase.html", B, "Casa Soda — Yardzen Brand Book 2026 (B)"),
    ("c-business-case.html", C, "Casa Soda — Yardzen Brand Book 2026 (C)"),
]:
    open(name, "w").write(doc(title, pages))
    print(f"{name}: {len(pages)} pages")
