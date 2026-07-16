#!/usr/bin/env python3
"""Assembles the Early Bloomers static site from a shared shell.
Run:  python3 build.py    (outputs .html files next to styles.css)"""

import pathlib

OUT = pathlib.Path(__file__).parent

SLOGAN = "Growing little minds one step at a time."
PHONE_DISPLAY = "704-676-2661"
PHONE_HREF = "+17046762661"
FAX_DISPLAY = "864-751-4352"
EMAIL = "earlybloomersllc@gmail.com"

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("milestones.html", "Milestones"),
    ("resources.html", "Resources"),
    ("about.html", "About"),
]

STEPMARK = '<span class="stepmark" aria-hidden="true"><i></i><i></i><i></i></span>'

STAIR = '''<svg class="stair {mod}" viewBox="0 0 1200 34" preserveAspectRatio="none" aria-hidden="true">
  <path fill="currentColor" d="M0 34h150V25h150v-6h150v-5h150v-5h150V4h150V0h300v34z"/>
</svg>'''


def shell(page, title, desc, body, extra_head=""):
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ""
        links += f'      <a href="{href}"{cur}>{label}</a>\n'
    cta_cur = ' aria-current="page"' if page == "contact.html" else ""

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="Images/Image1.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="Images/EBLogo1.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Karla:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
{extra_head}</head>
<body>

<a class="skip" href="#main">Skip to content</a>

<header class="hdr" id="hdr">
  <div class="hdr__in">
    <a class="brand" href="index.html">
      <img class="brand__logo" src="Images/EBLogo1.png" alt="Early Bloomers logo: a periwinkle flower with green leaves">
      <span>
        <span class="brand__name">Early Bloomers</span>
        <span class="brand__tag">{SLOGAN}</span>
      </span>
    </a>

    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>

    <nav class="nav" id="nav" aria-label="Main">
{links}      <a class="nav__cta" href="contact.html"{cta_cur}>Refer a child</a>
    </nav>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="ftr">
  <div class="wrap">
    <div class="ftr__grid">
      <div class="ftr__brand">
        <b>Early Bloomers LLC</b>
        <p class="ftr__slogan">{SLOGAN}</p>
        <p>Early intervention for infants and toddlers, delivered in the places your family already lives — in partnership with you, not around you.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="services.html">Services</a></li>
          <li><a href="milestones.html">Milestones</a></li>
          <li><a href="resources.html">Resources</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html">Refer a child</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_HREF}">{PHONE_DISPLAY}</a></li>
          <li>Fax: {FAX_DISPLAY}</li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="https://www.scdhhs.gov/resources/programs-and-initiatives/babynet" target="_blank" rel="noopener">BabyNet (SCDHHS)</a></li>
        </ul>
      </div>
    </div>
    <div class="ftr__base">
      <span>&copy; <span id="yr">2026</span> Early Bloomers LLC. All rights reserved.</span>
      <span>Information on this site is educational and is not medical advice.</span>
    </div>
  </div>
</footer>

<script src="main.js"></script>
</body>
</html>
'''


def phero(eyebrow, h1, lede):
    return f'''<section class="phero">
  <div class="wrap">
    <p class="eyebrow">{STEPMARK}{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>
{STAIR.format(mod="")}'''


# ============================================================ HOME
home = f'''<section class="hero wrap">
  <div class="hero__grid">
    <div>
      <p class="eyebrow">{STEPMARK}Birth to three &middot; [Your counties], SC</p>
      <h1>If you're wondering whether to <em>wait and see</em> &mdash; don't.</h1>
      <p class="lede">
        Trusting your gut about your child's development isn't overreacting. It's the most
        useful thing a parent can do. Early Bloomers is an early intervention provider working
        with families across [your counties] &mdash; coaching, assessing, and connecting you to
        what your child needs. Growing little minds one step at a time.
      </p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="contact.html">Refer a child</a>
        <a class="btn btn--ghost" href="milestones.html">See milestones by age</a>
      </div>
      <p class="hero__note">Anyone can make a referral &mdash; a parent, doctor, caregiver, teacher, or friend. You don't need a diagnosis to start.</p>
    </div>

    <div class="hero__art">
      <img src="Images/Image1.jpg" alt="An early interventionist sitting on the floor playing with a toddler during a home visit" fetchpriority="high">
      <div class="hero__badge">
        <b>No cost</b>
        <span>Children who meet BabyNet eligibility are served regardless of family income.</span>
      </div>
    </div>
  </div>
</section>

<section class="band band--white">
  <div class="wrap">
    <div class="tiles rv">
      <div class="tile">
        <h3>You know your child best</h3>
        <p>You don't need a diagnosis, a referral, or certainty to reach out. A hunch is reason enough to ask the question.</p>
      </div>
      <div class="tile">
        <h3>The brain is never faster</h3>
        <p>More than a million neural connections form every second in the first three years. Support lands harder now than it ever will again.</p>
      </div>
      <div class="tile">
        <h3>Learning happens in the ordinary</h3>
        <p>Meals, baths, car rides, play. We coach you through the routines you already have, rather than adding new ones.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{STEPMARK}What we do</p>
      <h2>Three ways we walk alongside your family</h2>
      <p class="lede">Every plan starts with your priorities. Nothing here is off the shelf.</p>
    </div>

    <div class="cards rv">
      <article class="card">
        <img src="Images/Image2.avif" alt="An early interventionist and toddler engaged in play-based learning on the floor">
        <div class="card__body">
          <h3>Early Intervention Sessions</h3>
          <p>Regular one-hour visits with you and your child, using play-based strategies built around their interests.</p>
          <ul>
            <li>Weekly or bi-weekly, in your home</li>
            <li>Play-based, research-backed strategies</li>
            <li>Coaching so you can carry it into the week</li>
            <li>Your time to ask anything</li>
          </ul>
        </div>
      </article>

      <article class="card">
        <img src="Images/Image3.png" alt="A child stacking wooden blocks while an interventionist observes and records progress">
        <div class="card__body">
          <h3>Developmental Assessments</h3>
          <p>A look at the whole child every six months, so everyone can see progress and make better decisions together.</p>
          <ul>
            <li>Six areas of development</li>
            <li>Every six months</li>
            <li>Plain-language results</li>
            <li>Your input carries weight</li>
          </ul>
        </div>
      </article>

      <article class="card">
        <img src="Images/Image4.jpg" alt="A caregiver and infant during a home visit while an interventionist takes notes">
        <div class="card__body">
          <h3>Service Coordination</h3>
          <p>One person who keeps the whole picture straight, links you to outside resources, and makes referrals.</p>
          <ul>
            <li>Referrals for speech, OT, and PT</li>
            <li>Navigating BabyNet and OIDD</li>
            <li>Community resource linking</li>
            <li>Transition planning at age three</li>
          </ul>
        </div>
      </article>
    </div>

    <p style="margin-top:2rem"><a class="btn btn--ghost" href="services.html">See how each one works &rarr;</a></p>
  </div>
</section>

<section class="band band--leaf">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{STEPMARK}How it works</p>
      <h2>One step at a time, from first call to first visit</h2>
      <p class="lede">Nobody expects you to know the system. That's our job &mdash; here's the shape of it.</p>
    </div>

    <div class="steps-h rv">
      <div class="steps-h__item">
        <h3>Reach out</h3>
        <p>Call, email, or send the form. Tell us what you're noticing, even if it's vague.</p>
      </div>
      <div class="steps-h__item">
        <h3>Referral &amp; evaluation</h3>
        <p>A referral goes to BabyNet and your child is evaluated at no cost to you.</p>
      </div>
      <div class="steps-h__item">
        <h3>Build the plan</h3>
        <p>If eligible, we set goals together around your family's real routines.</p>
      </div>
      <div class="steps-h__item">
        <h3>Start walking</h3>
        <p>Regular sessions begin, and we adjust as your child grows.</p>
      </div>
    </div>

    <p style="margin-top:2.4rem"><a class="btn btn--primary" href="contact.html">Take the first step</a></p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="callout rv center" style="max-width:820px">
      <p class="eyebrow" style="justify-content:center">{STEPMARK}Not sure yet?</p>
      <h2>Wondering is a good enough reason to call.</h2>
      <p class="lede center">Most families who reach out aren't certain anything's wrong. That's normal. A conversation costs nothing, and often ends with us saying your child looks right on track.</p>
      <a class="btn btn--primary" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>'''

# ============================================================ SERVICES
services = phero(
    "Services",
    "Support built around one child &mdash; yours",
    "Early Bloomers provides early intervention for infants and toddlers: regular play-based "
    "sessions, developmental assessments, and the service coordination that keeps everything "
    "connected. Here's what each one actually looks like."
) + f'''
<section class="band">
  <div class="wrap">
    <div class="cards rv">
      <article class="card">
        <img src="Images/Image2.avif" alt="An early interventionist and toddler engaged in play-based learning on the floor">
        <div class="card__body">
          <h3>Early Intervention Sessions</h3>
          <p>A weekly or bi-weekly one-hour session with you and your child. Your Early Interventionist uses play-based strategies to help your child learn and grow &mdash; and it's your time to ask questions and learn how best to help.</p>
          <ul>
            <li>Built around your child's interests</li>
            <li>In your home, daycare, or community</li>
            <li>Research-based strategies</li>
            <li>Caregiver coaching, every session</li>
          </ul>
        </div>
      </article>

      <article class="card">
        <img src="Images/Image3.png" alt="A child stacking wooden blocks while an interventionist observes and records progress">
        <div class="card__body">
          <h3>Developmental Assessments</h3>
          <p>Every six months, we assess how your child has progressed across six areas of development, so we get a look at the whole child rather than one slice of them.</p>
          <ul>
            <li>Six developmental domains</li>
            <li>Progress you can actually see</li>
            <li>Everyone's input gathered</li>
            <li>Explained in plain language</li>
          </ul>
        </div>
      </article>

      <article class="card">
        <img src="Images/Image4.jpg" alt="A caregiver and infant during a home visit while an interventionist takes notes">
        <div class="card__body">
          <h3>Service Coordination</h3>
          <p>Your Early Interventionist links you to outside resources and makes referrals for other services &mdash; so you're not the one holding the whole system together.</p>
          <ul>
            <li>Referrals for speech, physical, and occupational therapy</li>
            <li>Assistive technology exploration</li>
            <li>Community resources and supports</li>
            <li>Transition planning as your child turns three</li>
          </ul>
        </div>
      </article>
    </div>

    <div class="ms__disc rv" style="max-width:none;margin-top:2.4rem">
      <p><strong>About therapy services.</strong> Early Bloomers provides early intervention and
      service coordination. We don't deliver speech, physical, or occupational therapy ourselves &mdash;
      we connect your family to qualified providers who do, and we stay involved to make sure the
      pieces work together. If your child needs one of those therapies, we'll say so and help you get there.</p>
    </div>
  </div>
</section>

<section class="band band--leaf">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{STEPMARK}The path</p>
      <h2>Every step, in order</h2>
      <p class="lede">This is the whole journey from the first phone call through your child's third birthday. Most families move through the early steps in [X] weeks.</p>
    </div>

    <div class="steps rv">
      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>You reach out</h3>
          <p>Call, email, or send the contact form. Tell us what you're noticing &mdash; "he's almost two and not really talking yet" is plenty to start with. Anyone can make a referral: a parent, doctor, caregiver, teacher, or friend.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>Referral to BabyNet</h3>
          <p>BabyNet is South Carolina's early intervention system for children under three with developmental delays, or conditions associated with them. A referral can go through us, or you can call the Central Referral Team directly at 1-866-512-8881.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>Evaluation and eligibility</h3>
          <p>Your child is evaluated at no cost to determine whether they're eligible. Children who meet the criteria are served regardless of family income.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>We build the plan together</h3>
          <p>You share your priorities, concerns, and hopes. We set goals that fit your family's values and your child's strengths &mdash; not a generic checklist.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>Sessions begin</h3>
          <p>Regular visits start, in the places your child already spends their days. You're a huge part of the team &mdash; most of what works happens in the hours we're not there.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>We check the map every six months</h3>
          <p>An assessment across six developmental areas shows what's moved. Goals get adjusted. Nothing runs on autopilot.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>Transition at three</h3>
          <p>BabyNet ends at age three. We help you plan what comes next well before you get there, whether that's continued services through OIDD, your school district, or nothing at all because your child is thriving.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="callout rv center" style="max-width:820px">
      <h2>Ready to take the first step?</h2>
      <p class="lede center">It starts with a conversation. No referral needed to talk to us.</p>
      <a class="btn btn--primary" href="contact.html">Refer a child</a>
    </div>
  </div>
</section>'''

# ============================================================ MILESTONES
BANDS = [
    ("2\u20136 months", "The social baby", "Looking, smiling, and starting to answer back.", [
        "Smiles on their own to get your attention",
        "Makes sounds back when you talk to them",
        "Holds head steady without support when held",
        "Brings hands to mouth",
        "Pushes up on elbows during tummy time",
        "Looks at you, moves, or makes sounds to keep your notice",
    ]),
    ("9\u201312 months", "Names and games", "Responding to you, and getting hands into everything.", [
        "Looks when you call their name",
        "Plays games with you, like peek-a-boo",
        "Sits without support",
        "Picks up small things between thumb and finger",
        "Waves bye-bye",
        'Calls a parent "mama" or "dada"',
    ]),
    ("15\u201318 months", "First words, first steps", "Pointing at the world and naming a bit of it.", [
        "Takes a few steps on their own",
        "Uses several single words",
        "Points to show you something interesting",
        "Copies you doing chores, like sweeping",
        "Drinks from a cup without a lid, with some spilling",
        "Moves away from you but checks back to be sure you're near",
    ]),
    ("2 years", "Words snap together", "Two words at a time, and noticing other people.", [
        'Says at least two words together, like "more milk"',
        "Points to things in a book when you ask",
        "Notices when others are hurt or upset",
        "Kicks a ball",
        "Runs",
        "Eats with a spoon",
    ]),
    ("2\u00bd\u20133 years", "Conversations", "Being understood, and playing with other children.", [
        "Talks with you in at least two back-and-forth exchanges",
        "Says about three words together in a sentence",
        "Most people can understand what they say",
        "Plays alongside, and sometimes with, other children",
        "Puts on some clothes by themselves",
        "Draws a circle when you show them how",
    ]),
]

tabs_html = ""
panels_html = ""
for i, (label, title, sub, items) in enumerate(BANDS, 1):
    sel = "true" if i == 1 else "false"
    tabindex = "" if i == 1 else ' tabindex="-1"'
    hidden = "" if i == 1 else " hidden"
    tabs_html += (f'        <button class="ms__tab" role="tab" id="t-{i}" aria-controls="p-{i}" '
                  f'aria-selected="{sel}"{tabindex}>{label}</button>\n')
    lis = "\n".join(f'          <li><span class="ms__dot"></span>{x}</li>' for x in items)
    panels_html += f'''      <div class="ms__panel" role="tabpanel" id="p-{i}" aria-labelledby="t-{i}" tabindex="0"{hidden}>
        <h3>{title}</h3>
        <p class="ms__age">{label} &mdash; {sub}</p>
        <ul class="ms__list">
{lis}
        </ul>
        <div class="ms__foot">
          <a href="https://www.cdc.gov/act-early/milestones/index.html" target="_blank" rel="noopener">Full CDC checklist for this age &rarr;</a>
        </div>
      </div>
'''

milestones = phero(
    "Milestones by age",
    "Every child climbs at their own pace",
    "These are examples of things most children &mdash; about 75% or more &mdash; can do by each age. "
    "They're conversation starters, not a test. If something here gives you pause, that's worth a "
    "conversation, not a wait."
) + f'''
<section class="band">
  <div class="wrap">
    <div class="ms rv">
      <div class="ms__tabs" role="tablist" aria-label="Milestones by age">
{tabs_html}      </div>
{panels_html}    </div>

    <div class="ms__disc rv">
      <p><strong>Please read this part.</strong> These milestones are adapted from the CDC's
      <a href="https://www.cdc.gov/act-early/index.html" target="_blank" rel="noopener">Learn the Signs. Act Early.</a>
      program. They are not developmental guidelines or standards, and this page is
      <strong>not a screening or diagnostic tool</strong>. It cannot tell you whether your child has a delay.</p>
      <p>Children develop at different rates, and a missed milestone on its own doesn't mean something
      is wrong. What it means is: bring it up. Talk to your child's doctor and ask about developmental
      screening. The American Academy of Pediatrics recommends screening at 9, 18, and 30 months, and
      for autism at 18 and 24 months &mdash; or any time you or a provider has a concern.</p>
      <p>If your child has lost a skill they used to have, don't wait on that one. Call your doctor.</p>
    </div>
  </div>
</section>

<section class="band band--leaf">
  <div class="wrap">
    <div class="callout rv center" style="max-width:820px">
      <p class="eyebrow" style="justify-content:center">{STEPMARK}Something give you pause?</p>
      <h2>Then it's worth a conversation.</h2>
      <p class="lede center">A referral costs nothing and commits you to nothing. We'd rather tell you your child is on track than have you spend six months wondering.</p>
      <a class="btn btn--primary" href="contact.html">Refer a child</a>
    </div>
  </div>
</section>'''

# ============================================================ RESOURCES
resources = phero(
    "Resources",
    "The map, and who else is on it",
    "Early intervention in South Carolina runs through a few different doors. Here are the ones "
    "worth knowing about &mdash; including the ones that have nothing to do with us."
) + f'''
<section class="band">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{STEPMARK}Start here</p>
      <h2>South Carolina programs</h2>
    </div>

    <div class="res rv">
      <div class="res__item">
        <div>
          <h3>BabyNet</h3>
          <p>South Carolina's interagency early intervention system for infants and toddlers under three with developmental delays, or conditions associated with delays. Funded through IDEA and administered by SCDHHS. Anyone can make a referral, and services are provided at no cost to families.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.scdhhs.gov/resources/programs-and-initiatives/babynet" target="_blank" rel="noopener">Visit &rarr;</a>
      </div>

      <div class="res__item">
        <div>
          <h3>BabyNet Central Referral Team</h3>
          <p>Call 1-866-512-8881 to refer a child from birth to three, or complete the online referral form. You do not need a doctor's referral, and you don't need to go through us to do it.</p>
        </div>
        <a class="btn btn--ghost" href="tel:+18665128881">1-866-512-8881</a>
      </div>

      <div class="res__item">
        <div>
          <h3>BHDD-OIDD (formerly DDSN)</h3>
          <p>For children who are over three, or transitioning out of BabyNet. Eligibility line: 1-800-289-7012.</p>
        </div>
        <a class="btn btn--ghost" href="https://ddsn.sc.gov/babynet" target="_blank" rel="noopener">Visit &rarr;</a>
      </div>

      <div class="res__item">
        <div>
          <h3>BabyNet Central Directory</h3>
          <p>An online directory of services for children birth to three with developmental delays or disabilities, managed by Family Connection of South Carolina.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.scdhhs.gov/resources/programs-and-initiatives/babynet/families/babynet-central-directory" target="_blank" rel="noopener">Visit &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="band band--white">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{STEPMARK}For families</p>
      <h2>Understanding development</h2>
    </div>

    <div class="res rv">
      <div class="res__item">
        <div>
          <h3>CDC &mdash; Learn the Signs. Act Early.</h3>
          <p>Free milestone checklists for every age from two months to five years, in a dozen languages. The source our milestones page draws from.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.cdc.gov/act-early/index.html" target="_blank" rel="noopener">Visit &rarr;</a>
      </div>

      <div class="res__item">
        <div>
          <h3>CDC Milestone Tracker app</h3>
          <p>Interactive, illustrated checklists on your phone, with photos and video of what each milestone looks like. Free for iOS and Android.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.cdc.gov/act-early/milestones/index.html" target="_blank" rel="noopener">Visit &rarr;</a>
      </div>

      <div class="res__item">
        <div>
          <h3>Milestones in Action</h3>
          <p>A photo and video library showing what each milestone actually looks like &mdash; useful when a checklist item is hard to picture.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.cdc.gov/act-early/milestones-in-action/index.html" target="_blank" rel="noopener">Visit &rarr;</a>
      </div>
    </div>

    <div class="ms__disc rv" style="margin-top:2rem">
      <p><strong>A note on the obvious.</strong> Several links here go to programs you can use without
      ever contacting us. That's on purpose. If BabyNet is the right door for your family and we're not,
      we'd rather you walk through it than wait. Call the Central Referral Team at 1-866-512-8881.</p>
    </div>
  </div>
</section>'''

# ============================================================ ABOUT
about = phero(
    "About",
    "Family partnership isn't a tagline here",
    "Early Bloomers exists because the first three years only happen once, and no family should "
    "have to navigate them alone or guess at the system."
) + f'''
<section class="band">
  <div class="wrap">
    <div class="split rv">
      <img src="Images/Image4.jpg" alt="[Replace: a photo of your lead Early Interventionist working with a child]">
      <div>
        <p class="eyebrow">{STEPMARK}Our story</p>
        <h2>Why we started</h2>
        <p>[Replace this with your real story &mdash; who founded Early Bloomers, why, and what
        families can expect from you. Two or three short paragraphs. This is the section parents
        read most carefully, because they're deciding whether to trust you with their child.]</p>
        <p>[Specifics beat adjectives. Where you trained, how many years in early intervention,
        what you believe about how children learn, and what changed in you the day you decided to
        do this. "Passionate about children" is what every site says. What's the thing only you
        can say?]</p>
        <ul class="creds">
          <li>
            <svg width="17" height="17" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="M10 1l2.6 5.3 5.9.8-4.3 4.1 1 5.8L10 14.3 4.8 17l1-5.8L1.5 7.1l5.9-.8L10 1z"/></svg>
            <span>[BabyNet participating provider &mdash; confirm and state it plainly]</span>
          </li>
          <li>
            <svg width="17" height="17" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="M10 1l2.6 5.3 5.9.8-4.3 4.1 1 5.8L10 14.3 4.8 17l1-5.8L1.5 7.1l5.9-.8L10 1z"/></svg>
            <span>[Degrees and field &mdash; e.g. B.A. Psychology, Anderson University]</span>
          </li>
          <li>
            <svg width="17" height="17" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="M10 1l2.6 5.3 5.9.8-4.3 4.1 1 5.8L10 14.3 4.8 17l1-5.8L1.5 7.1l5.9-.8L10 1z"/></svg>
            <span>[Years of experience in early intervention]</span>
          </li>
          <li>
            <svg width="17" height="17" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="M10 1l2.6 5.3 5.9.8-4.3 4.1 1 5.8L10 14.3 4.8 17l1-5.8L1.5 7.1l5.9-.8L10 1z"/></svg>
            <span>[Counties served]</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="band band--leaf">
  <div class="wrap">
    <div class="shead rv center">
      <p class="eyebrow">{STEPMARK}What we believe</p>
      <h2>Four things we hold to</h2>
    </div>
    <div class="tiles rv">
      <div class="tile">
        <h3>You lead</h3>
        <p>Families take the lead role in helping their child. We bring strategies and information; you bring the expertise on your own child. That order matters.</p>
      </div>
      <div class="tile">
        <h3>Ordinary moments do the work</h3>
        <p>Infants and toddlers learn best with familiar people in familiar places. An hour a week matters because of what it changes in the other hundred and sixty-seven.</p>
      </div>
      <div class="tile">
        <h3>Plain language, always</h3>
        <p>If we explain something and you leave more confused than you arrived, we did it wrong. Ask us to say it again, differently. We won't mind.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="shead rv center">
      <p class="eyebrow">{STEPMARK}Questions</p>
      <h2>The things families ask first</h2>
    </div>

    <div class="faq rv">
      <details open>
        <summary>What ages do you work with?</summary>
        <div class="faq__a"><p>[Replace &mdash; e.g. birth to three through BabyNet, and up to age six through OIDD. Confirm your own range.]</p></div>
      </details>
      <details>
        <summary>Do I need a referral from my pediatrician?</summary>
        <div class="faq__a"><p>No. Anyone can make a referral &mdash; a parent, doctor, caregiver, teacher, or friend. You can contact us directly, or call the BabyNet Central Referral Team at 1-866-512-8881 yourself.</p></div>
      </details>
      <details>
        <summary>What does it cost?</summary>
        <div class="faq__a"><p>Children who meet BabyNet eligibility criteria are served regardless of family income, and BabyNet services are provided at no cost to families. [Confirm this reflects your situation, and add anything specific about services outside BabyNet.]</p></div>
      </details>
      <details>
        <summary>Where do sessions happen?</summary>
        <div class="faq__a"><p>[Replace &mdash; home, daycare, community? What's your travel radius, and which counties?]</p></div>
      </details>
      <details>
        <summary>Do you provide speech, occupational, or physical therapy?</summary>
        <div class="faq__a"><p>Not directly. We provide early intervention and service coordination, and we link families to qualified providers for speech, physical, and occupational therapy, and assistive technology. We stay involved so the pieces work together.</p></div>
      </details>
      <details>
        <summary>What happens when my child turns three?</summary>
        <div class="faq__a"><p>BabyNet eligibility ends at three. Some children continue with services through BHDD-OIDD up to age six; others transition to their school district; others don't need anything further. We start planning that step well before the birthday. [Confirm and add your specifics.]</p></div>
      </details>
      <details>
        <summary>What if I'm not sure anything's actually wrong?</summary>
        <div class="faq__a"><p>That's the most common reason families call, and it's a good reason. An evaluation costs nothing and often ends with confirmation that your child is right on track. Knowing beats wondering, and if support would help, starting sooner makes it work better.</p></div>
      </details>
    </div>
  </div>
</section>'''

# ============================================================ CONTACT
contact = phero(
    "Refer a child",
    "Let's start with a conversation",
    "Tell us what you're noticing and we'll tell you honestly whether we think we can help &mdash; "
    "and if we're not the right fit, we'll point you to who is."
) + f'''
<section class="band">
  <div class="wrap">
    <div class="contact rv">
      <form class="form" action="https://formspree.io/f/REPLACE_WITH_YOUR_FORM_ID" method="POST">
        <div class="field">
          <label for="name">Your name</label>
          <input id="name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="rel">You are the child's&hellip;</label>
          <select id="rel" name="relationship">
            <option value="">Select one</option>
            <option>Parent or guardian</option>
            <option>Doctor or health provider</option>
            <option>Caregiver or teacher</option>
            <option>Friend or family member</option>
            <option>Other</option>
          </select>
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input id="email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="phone">Phone</label>
          <input id="phone" name="phone" type="tel" autocomplete="tel">
        </div>
        <div class="field">
          <label for="age">The child's age</label>
          <select id="age" name="child_age">
            <option value="">Select an age</option>
            <option>Under 6 months</option>
            <option>6&ndash;12 months</option>
            <option>12&ndash;18 months</option>
            <option>18&ndash;24 months</option>
            <option>2&ndash;3 years</option>
            <option>Over 3 years</option>
          </select>
        </div>
        <div class="field">
          <label for="county">County</label>
          <input id="county" name="county" type="text" placeholder="e.g. Greenville">
        </div>
        <div class="field">
          <label for="msg">What are you noticing?</label>
          <textarea id="msg" name="message" placeholder="It's okay to be vague. &quot;He's almost two and not really talking yet&quot; is plenty to start with." required></textarea>
        </div>
        <button class="btn btn--primary" type="submit">Send message</button>
        <p class="form__note">Please don't include sensitive medical details in this form &mdash; we'll cover those securely once we're in touch.</p>
      </form>

      <div>
        <div class="cinfo">
          <h3>Other ways to reach us</h3>
          <dl>
            <dt>Phone</dt>
            <dd><a href="tel:{PHONE_HREF}">{PHONE_DISPLAY}</a></dd>

            <dt>Fax</dt>
            <dd>{FAX_DISPLAY}</dd>

            <dt>Email</dt>
            <dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>

            <dt>Service area</dt>
            <dd>[Your counties, SC]</dd>

            <dt>Hours</dt>
            <dd>[e.g. Monday&ndash;Friday, 8am&ndash;5pm]</dd>
          </dl>
        </div>

        <div class="ms__disc" style="margin-top:20px">
          <p><strong>You can also skip us entirely.</strong> To refer a child from birth to three
          directly to South Carolina's early intervention system, call the BabyNet Central Referral
          Team at <a href="tel:+18665128881">1-866-512-8881</a>. Anyone can make that referral, and
          it costs nothing. If we're not the right provider for your family, that number still is.</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

PAGES = [
    ("index.html", "Early Bloomers &mdash; Early Intervention for Infants &amp; Toddlers",
     "Early Bloomers provides early intervention, developmental assessments, and service coordination for infants and toddlers in South Carolina. Growing little minds one step at a time.", home),
    ("services.html", "Services &mdash; Early Bloomers",
     "Early intervention sessions, developmental assessments every six months, and service coordination that links your family to speech, OT, and PT.", services),
    ("milestones.html", "Milestones by Age &mdash; Early Bloomers",
     "Developmental milestones by age, adapted from the CDC's Learn the Signs. Act Early. program. A conversation starter, not a screening tool.", milestones),
    ("resources.html", "Resources &mdash; Early Bloomers",
     "BabyNet, BHDD-OIDD, CDC milestone checklists, and the other doors into early intervention in South Carolina.", resources),
    ("about.html", "About &mdash; Early Bloomers",
     "Who we are, what we believe about early intervention, and the questions families ask first.", about),
    ("contact.html", "Refer a Child &mdash; Early Bloomers",
     f"Contact Early Bloomers at {PHONE_DISPLAY} or {EMAIL}. Anyone can refer a child &mdash; parent, doctor, caregiver, teacher, or friend.", contact),
]

for name, title, desc, body in PAGES:
    (OUT / name).write_text(shell(name, title, desc, body), encoding="utf-8")
    print("wrote", name)
