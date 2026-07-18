#!/usr/bin/env python3
"""Early Bloomers LLC — static site generator.

Edit the CONSTANTS below, run `python3 build.py`, and every page updates.
Nothing here is required to host the site; GitHub Pages ignores this file.
"""

import pathlib

OUT = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- constants
SLOGAN = "Growing little minds one step at a time."
OWNER = "Michelle Lopez"
OWNER_TITLE = "Owner and Early Interventionist"
PHONE_DISPLAY = "704-676-2661"
PHONE_HREF = "+17046762661"
FAX_DISPLAY = "864-751-4352"
EMAIL = "EarlyBloomersllc@gmail.com"
HOURS = "Monday&ndash;Friday, 8:00&nbsp;AM&ndash;5:00&nbsp;PM"
COUNTIES = "Greenville, Spartanburg, and Pickens counties, South Carolina"
COUNTIES_SHORT = "Greenville, Spartanburg &amp; Pickens"
AGES = "birth to five"
BUILDER = "WB3 Ventures LLC"
SITE = "https://early-bloomers.com"

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("milestones.html", "Milestones"),
    ("resources.html", "Resources"),
    ("about.html", "About"),
]

SM = '<span class="stepmark" aria-hidden="true"><i></i><i></i><i></i></span>'

STAIR = ('<svg class="stair{mod}" viewBox="0 0 1200 38" preserveAspectRatio="none" '
         'aria-hidden="true" focusable="false">'
         '<path fill="currentColor" d="M0 38h150V28h150v-7h150v-6h150v-6H900V4h150V0h150v38z"/></svg>')

STAR = ('<svg width="18" height="18" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" '
        'focusable="false"><path d="M10 1l2.6 5.3 5.9.8-4.3 4.1 1 5.8L10 14.3 4.8 17l1-5.8L1.5 7.1l5.9-.8L10 1z"/></svg>')


def shell(page, title, desc, body, og_image="Images/Image1.jpg"):
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
<meta name="author" content="Early Bloomers LLC">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Early Bloomers LLC">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:url" content="{SITE}/{page}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{SITE}/{page}">
<link rel="icon" href="Images/EBLogo1.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,600&family=Karla:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<a class="skip" href="#main">Skip to content</a>

<header class="hdr" id="hdr">
  <div class="hdr__in">
    <a class="brand" href="index.html">
      <img class="brand__logo" src="Images/EBLogo1.png" width="104" height="104"
           alt="Early Bloomers LLC logo: a periwinkle flower with green leaves inside a gold arch">
      <span>
        <span class="brand__name">Early Bloomers</span>
        <span class="brand__tag">{SLOGAN}</span>
      </span>
    </a>

    <button class="burger" id="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
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
        <p>Early intervention and developmental services for children {AGES}, delivered in the places your family already lives. Serving {COUNTIES_SHORT} counties.</p>
      </div>
      <div>
        <h2>Explore</h2>
        <ul>
          <li><a href="services.html">Services</a></li>
          <li><a href="milestones.html">Milestones</a></li>
          <li><a href="resources.html">Resources</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html">Refer a child</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="tel:{PHONE_HREF}">{PHONE_DISPLAY}</a></li>
          <li>Fax: {FAX_DISPLAY}</li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{HOURS}</li>
          <li><a href="https://www.scdhhs.gov/resources/programs-and-initiatives/babynet" target="_blank" rel="noopener">BabyNet (SCDHHS)</a></li>
        </ul>
      </div>
    </div>

    <div class="ftr__base">
      <span>&copy; <span id="yr">2026</span> Early Bloomers LLC. All rights reserved.</span>
      <span>Site built by {BUILDER}</span>
    </div>
    <p class="ftr__legal">The information on this site is educational and is not medical advice, a developmental screening, or a diagnosis. Developmental milestones referenced here are adapted from the Centers for Disease Control and Prevention&rsquo;s &ldquo;Learn the Signs. Act Early.&rdquo; program and are not developmental guidelines or standards. If you have concerns about your child&rsquo;s development, talk with your child&rsquo;s doctor and ask about developmental screening.</p>
  </div>
</footer>

<script src="main.js"></script>
</body>
</html>
'''


def phero(eyebrow, h1, lede, stair=False):
    tail = STAIR.format(mod="") if stair else ""
    return f'''<section class="phero">
  <div class="wrap">
    <p class="eyebrow">{SM}{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>
{tail}'''


def slogan_band():
    return f'''<section class="slogan-band" aria-label="Our slogan">
  <div class="wrap">
    <span class="stepmark" aria-hidden="true"><i></i><i></i><i></i></span>
    <p>{SLOGAN}</p>
  </div>
</section>'''


# ================================================================= HOME
home = f'''<section class="hero wrap">
  <div class="hero__grid">
    <div>
      <p class="eyebrow">{SM}Birth to five &middot; {COUNTIES_SHORT}, SC</p>
      <h1>If you're wondering whether to <em>wait and see</em> &mdash; don't.</h1>
      <p class="hero__slogan">{SLOGAN}</p>
      <p class="lede">
        Trusting your gut about your child's development isn't overreacting. It's the most useful
        thing a parent can do. Early Bloomers is an early intervention practice serving families
        across {COUNTIES_SHORT} counties, one step at a time.
      </p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="contact.html">Refer a child</a>
        <a class="btn btn--ghost" href="milestones.html">See milestones by age</a>
      </div>
      <p class="hero__note">Anyone can make a referral: a parent, doctor, caregiver, teacher, or friend. You don't need a diagnosis to start.</p>
    </div>

    <div class="hero__art">
      <img src="Images/Image1.jpg" width="800" height="680" fetchpriority="high"
           alt="A toddler sitting on a rug, focused on pushing a wooden toy train along a track">
      <div class="hero__badge">
        <b>No cost</b>
        <span>Children who meet BabyNet eligibility are served regardless of family income.</span>
      </div>
    </div>
  </div>
</section>

<section class="band band--white" aria-labelledby="why-h">
  <div class="wrap">
    <h2 class="visually-hidden" id="why-h">Why families reach out</h2>
    <div class="tiles rv">
      <div class="tile">
        <h3>You know your child best</h3>
        <p>You don't need a diagnosis, a referral, or certainty to reach out. A hunch is reason enough to ask the question.</p>
      </div>
      <div class="tile">
        <h3>The brain is never faster</h3>
        <p>More than a million neural connections form every second in the first years of life. Support lands harder now than it ever will again.</p>
      </div>
      <div class="tile">
        <h3>Learning happens in the ordinary</h3>
        <p>Meals, baths, car rides, play. We work inside the routines you already have rather than adding new ones to your week.</p>
      </div>
    </div>
  </div>
</section>

{slogan_band()}

<section class="band">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{SM}What we do</p>
      <h2>Three ways we walk alongside your family</h2>
      <p class="lede">Every plan starts with your priorities and your child's strengths. Nothing here is off the shelf.</p>
    </div>

    <div class="cards rv">
      <article class="card">
        <img src="Images/Image2.avif" width="600" height="450"
             alt="An adult and a young child sitting together at a table during a play-based learning activity">
        <div class="card__body">
          <h3>Early Intervention Sessions</h3>
          <p>Regular one-hour visits with you and your child, using play-based strategies built around what already holds their attention.</p>
          <ul>
            <li>In your home, daycare, or community</li>
            <li>Research-based strategies</li>
            <li>Coaching so you can carry it into the week</li>
            <li>Your time to ask anything</li>
          </ul>
        </div>
      </article>

      <article class="card">
        <img src="Images/Image3.png" width="600" height="450"
             alt="A young child stacking colourful wooden blocks on a table">
        <div class="card__body">
          <h3>Developmental Assessments</h3>
          <p>A look at the whole child across six areas of development, so everyone can see what's moved and decide what comes next together.</p>
          <ul>
            <li>Six developmental areas</li>
            <li>Progress you can actually see</li>
            <li>Your input carries weight</li>
            <li>Explained in plain language</li>
          </ul>
        </div>
      </article>

      <article class="card">
        <img src="Images/Image4.jpg" width="600" height="450"
             alt="Three young children playing together with toys on the floor">
        <div class="card__body">
          <h3>Service Coordination</h3>
          <p>One person who keeps the whole picture straight, links you to outside resources, and makes referrals so you're not holding the system together alone.</p>
          <ul>
            <li>Referrals for speech, OT, PT, and ABA</li>
            <li>Navigating BabyNet and BHDD-OIDD</li>
            <li>Community resource linking</li>
            <li>Transition planning as your child grows</li>
          </ul>
        </div>
      </article>
    </div>

    <p style="margin-top:2.4rem"><a class="btn btn--ghost" href="services.html">See how each one works</a></p>
  </div>
</section>

<section class="band band--leaf">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{SM}How it works</p>
      <h2>Four steps to get started</h2>
      <p class="lede">Nobody expects you to know the system. That part is our job.</p>
    </div>

    <div class="steps-h rv">
      <div class="steps-h__item">
        <h3>Reach out</h3>
        <p>Call, email, or send the form. Tell us what you're noticing, even if it's vague.</p>
      </div>
      <div class="steps-h__item">
        <h3>Referral &amp; evaluation</h3>
        <p>A referral goes to BabyNet, and your child is evaluated at no cost to you.</p>
      </div>
      <div class="steps-h__item">
        <h3>Build the plan</h3>
        <p>If eligible, we set goals together around your family's real routines.</p>
      </div>
      <div class="steps-h__item">
        <h3>Start walking</h3>
        <p>Regular sessions begin, and we adjust the plan as your child grows.</p>
      </div>
    </div>

    <p style="margin-top:2.8rem"><a class="btn btn--primary" href="contact.html">Take the first step</a></p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <figure class="quote rv" style="max-width:900px;margin-inline:auto">
      <blockquote>
        &ldquo;I believe parents are the most important people in a child's development. My goal is to
        partner with families by providing practical strategies that fit naturally into their daily
        routines, celebrating every milestone along the way.&rdquo;
      </blockquote>
      <figcaption>{OWNER}, {OWNER_TITLE}</figcaption>
    </figure>
  </div>
</section>

<section class="band band--white">
  <div class="wrap">
    <div class="callout rv center" style="max-width:860px">
      <p class="eyebrow" style="justify-content:center">{SM}Not sure yet?</p>
      <h2>Wondering is a good enough reason to call.</h2>
      <p class="lede center">Most families who reach out aren't certain anything's wrong. That's normal. A conversation costs nothing, and often ends with us saying your child looks right on track.</p>
      <a class="btn btn--primary" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>'''

# ================================================================= SERVICES
services = phero(
    "Services",
    "Support built around one child &mdash; yours",
    f"Early Bloomers provides early intervention and developmental services for children {AGES}: "
    "regular play-based sessions, developmental assessments, and the service coordination that "
    "keeps everything connected. Here is what each one actually looks like."
) + f'''
<section class="band" aria-labelledby="svc-h">
  <div class="wrap">
    <h2 class="visually-hidden" id="svc-h">What we provide</h2>
    <div class="cards rv">
      <article class="card">
        <img src="Images/Image2.avif" width="600" height="450"
             alt="An adult and a young child sitting together at a table during a play-based learning activity">
        <div class="card__body">
          <h3>Early Intervention Sessions</h3>
          <p>A one-hour session with you and your child, using play-based strategies to help your child learn and grow. It's also your time to ask questions and learn how best to help.</p>
          <ul>
            <li>Built around your child's own interests</li>
            <li>In your home, daycare, or the community</li>
            <li>Research-based strategies</li>
            <li>Caregiver coaching in every session</li>
          </ul>
        </div>
      </article>

      <article class="card">
        <img src="Images/Image3.png" width="600" height="450"
             alt="A young child stacking colourful wooden blocks on a table">
        <div class="card__body">
          <h3>Developmental Assessments</h3>
          <p>An assessment across six areas of development, so we see the whole child rather than one slice of them, and so progress is visible to everyone.</p>
          <ul>
            <li>Six developmental areas</li>
            <li>Gathers everyone's input, including yours</li>
            <li>Guides what we work on next</li>
            <li>Explained in plain language</li>
          </ul>
        </div>
      </article>

      <article class="card">
        <img src="Images/Image4.jpg" width="600" height="450"
             alt="Three young children playing together with toys on the floor">
        <div class="card__body">
          <h3>Service Coordination</h3>
          <p>Linking your family to outside resources and making referrals for other services, so the pieces work together instead of landing on you to assemble.</p>
          <ul>
            <li>Referrals for speech and language therapy</li>
            <li>Referrals for occupational and physical therapy</li>
            <li>Referrals for ABA and other specialized services</li>
            <li>Navigating BabyNet, BHDD-OIDD, and transitions</li>
          </ul>
        </div>
      </article>
    </div>

    <div class="ms__disc rv" style="margin-top:2.6rem">
      <p><strong>About therapy services.</strong> Early Bloomers provides early intervention and
      developmental services directly, and coordinates care. Speech therapy, occupational therapy,
      physical therapy, ABA, and other specialized services are referred to appropriate providers
      when your child needs them. If one of those is the right next step, we will say so and help
      you get there.</p>
    </div>
  </div>
</section>

<section class="band band--leaf">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{SM}The path</p>
      <h2>Every step, in order</h2>
      <p class="lede">This is the whole walk, from the first phone call through your child's transition out of services.</p>
    </div>

    <div class="steps rv">
      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>You reach out</h3>
          <p>Call, email, or send the contact form. Tell us what you're noticing. &ldquo;He's almost two and not really talking yet&rdquo; is plenty to start with. Anyone can make a referral: a parent, doctor, caregiver, teacher, or friend.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>Referral to BabyNet</h3>
          <p>BabyNet is South Carolina's early intervention system for children under three with developmental delays, or with conditions associated with delays. A referral can go through us, or you can call the Central Referral Team yourself at 1-866-512-8881.</p>
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
          <p>You share your priorities, concerns, and hopes for your child. We set individualized goals that fit your family's values and build on your child's strengths, rather than working from a generic checklist.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>Sessions begin</h3>
          <p>Regular visits start in the places your child already spends their days. You are a huge part of the team. Most of what works happens in the hours we are not there.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>We check the map as we go</h3>
          <p>Assessment across six developmental areas shows what has moved. Goals get adjusted. Nothing runs on autopilot, and nothing continues just because it's on a plan somewhere.</p>
        </div>
      </div>

      <div class="steps__item">
        <div class="steps__num"></div>
        <div class="steps__body">
          <h3>Transition</h3>
          <p>BabyNet eligibility ends at age three. Some children continue through BHDD-OIDD, some move on to their school district, and some don't need anything further. We plan that step well before you get to it.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{slogan_band()}

<section class="band">
  <div class="wrap">
    <div class="callout rv center" style="max-width:860px">
      <h2>Ready to take the first step?</h2>
      <p class="lede center">It starts with a conversation. You don't need a referral to talk to us.</p>
      <a class="btn btn--primary" href="contact.html">Refer a child</a>
    </div>
  </div>
</section>'''

# ================================================================= MILESTONES
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
        "Calls a parent &ldquo;mama&rdquo; or &ldquo;dada&rdquo;",
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
        "Says at least two words together, like &ldquo;more milk&rdquo;",
        "Points to things in a book when you ask",
        "Notices when others are hurt or upset",
        "Kicks a ball",
        "Runs",
        "Eats with a spoon",
    ]),
    ("3 years", "Conversations", "Being understood, and joining other children.", [
        "Talks with you in at least two back-and-forth exchanges",
        "Asks who, what, where, or why questions",
        "Says their first name when asked",
        "Talks well enough for others to understand most of the time",
        "Notices other children and joins them to play",
        "Draws a circle when you show them how",
    ]),
    ("4 years", "Stories and pretending", "Imagination, longer sentences, and helping.", [
        "Pretends to be something else during play",
        "Says sentences with four or more words",
        "Talks about at least one thing that happened during their day",
        "Names a few colours of things",
        "Draws a person with three or more body parts",
        "Comforts others who are hurt or sad",
    ]),
    ("5 years", "Ready for what's next", "Rules, rhymes, counting, and keeping a conversation going.", [
        "Follows rules or takes turns when playing games with other children",
        "Tells a story they heard or made up with at least two events",
        "Keeps a conversation going with more than three back-and-forth exchanges",
        "Counts to 10",
        "Writes some letters in their name",
        "Hops on one foot",
    ]),
]

tabs_html = ""
panels_html = ""
for i, (label, title, sub, items) in enumerate(BANDS, 1):
    sel = "true" if i == 1 else "false"
    tabindex = "" if i == 1 else ' tabindex="-1"'
    hidden = "" if i == 1 else " hidden"
    tabs_html += (f'        <button class="ms__tab" type="button" role="tab" id="t-{i}" '
                  f'aria-controls="p-{i}" aria-selected="{sel}"{tabindex}>{label}</button>\n')
    lis = "\n".join(f'          <li><span class="ms__dot" aria-hidden="true"></span>{x}</li>' for x in items)
    panels_html += f'''      <div class="ms__panel" role="tabpanel" id="p-{i}" aria-labelledby="t-{i}"{hidden}>
        <h3>{title}</h3>
        <p class="ms__age">{label} &mdash; {sub}</p>
        <ul class="ms__list">
{lis}
        </ul>
        <div class="ms__foot">
          <a href="https://www.cdc.gov/act-early/milestones/index.html" target="_blank" rel="noopener">See the CDC&rsquo;s full milestone checklists<span class="visually-hidden"> (opens in a new tab)</span></a>
        </div>
      </div>
'''

milestones = phero(
    "Milestones by age",
    "Every child climbs at their own pace",
    "These are examples of things most children, about 75% or more, can do by each age. They are "
    "conversation starters, not a test. If something here gives you pause, that's worth a "
    "conversation, not a wait."
) + f'''
<section class="band" aria-labelledby="ms-h">
  <div class="wrap">
    <h2 class="visually-hidden" id="ms-h">Milestones by age band</h2>
    <div class="ms rv">
      <div class="ms__tabs" role="tablist" aria-label="Milestones by age">
{tabs_html}      </div>
{panels_html}    </div>

    <div class="ms__disc rv">
      <p><strong>Please read this part.</strong> These milestones are adapted from the CDC's
      <a href="https://www.cdc.gov/act-early/index.html" target="_blank" rel="noopener">Learn the Signs. Act Early.<span class="visually-hidden"> (opens in a new tab)</span></a>
      program. They are not developmental guidelines or standards, and this page is
      <strong>not a screening or diagnostic tool</strong>. It cannot tell you whether your child has a delay.</p>
      <p>Children develop at different rates, and a missed milestone on its own doesn't mean something
      is wrong. What it means is: bring it up. Talk to your child's doctor and ask about developmental
      screening. The American Academy of Pediatrics recommends screening at 9, 18, and 30 months, and
      for autism at 18 and 24 months, or any time you or a provider has a concern.</p>
      <p>If your child has lost a skill they used to have, don't wait on that one. Call your doctor.</p>
    </div>
  </div>
</section>

{slogan_band()}

<section class="band">
  <div class="wrap">
    <div class="callout rv center" style="max-width:860px">
      <p class="eyebrow" style="justify-content:center">{SM}Something give you pause?</p>
      <h2>Then it's worth a conversation.</h2>
      <p class="lede center">A referral costs nothing and commits you to nothing. We would rather tell you your child is on track than have you spend six months wondering.</p>
      <a class="btn btn--primary" href="contact.html">Refer a child</a>
    </div>
  </div>
</section>'''

# ================================================================= RESOURCES
resources = phero(
    "Resources",
    "The map, and who else is on it",
    "Early intervention in South Carolina runs through a few different doors. Here are the ones "
    "worth knowing about, including the ones that have nothing to do with us."
) + f'''
<section class="band">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{SM}Start here</p>
      <h2>South Carolina programs</h2>
    </div>

    <div class="res rv">
      <div class="res__item">
        <div>
          <h3>BabyNet</h3>
          <p>South Carolina's interagency early intervention system for infants and toddlers under three with developmental delays, or conditions associated with delays. Funded through IDEA and administered by SCDHHS. Anyone can make a referral, and services are provided at no cost to families.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.scdhhs.gov/resources/programs-and-initiatives/babynet" target="_blank" rel="noopener">Visit<span class="visually-hidden"> BabyNet (opens in a new tab)</span></a>
      </div>

      <div class="res__item">
        <div>
          <h3>BabyNet Central Referral Team</h3>
          <p>Call to refer a child from birth to three, or complete the online referral form. You do not need a doctor's referral, and you do not need to go through us to do it.</p>
        </div>
        <a class="btn btn--ghost" href="tel:+18665128881">1-866-512-8881</a>
      </div>

      <div class="res__item">
        <div>
          <h3>BHDD-OIDD (formerly DDSN)</h3>
          <p>For children over three, or transitioning out of BabyNet. Early intervention services continue through OIDD up to age six. Eligibility line: 1-800-289-7012.</p>
        </div>
        <a class="btn btn--ghost" href="https://ddsn.sc.gov/babynet" target="_blank" rel="noopener">Visit<span class="visually-hidden"> BHDD-OIDD (opens in a new tab)</span></a>
      </div>

      <div class="res__item">
        <div>
          <h3>BabyNet Central Directory</h3>
          <p>An online directory of services for children birth to three with developmental delays or disabilities, managed by Family Connection of South Carolina.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.scdhhs.gov/resources/programs-and-initiatives/babynet/families/babynet-central-directory" target="_blank" rel="noopener">Visit<span class="visually-hidden"> the Central Directory (opens in a new tab)</span></a>
      </div>
    </div>
  </div>
</section>

<section class="band band--white">
  <div class="wrap">
    <div class="shead rv">
      <p class="eyebrow">{SM}For families</p>
      <h2>Understanding development</h2>
    </div>

    <div class="res rv">
      <div class="res__item">
        <div>
          <h3>CDC &mdash; Learn the Signs. Act Early.</h3>
          <p>Free milestone checklists for every age from two months to five years, in a dozen languages. This is the source our milestones page draws from.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.cdc.gov/act-early/index.html" target="_blank" rel="noopener">Visit<span class="visually-hidden"> Learn the Signs. Act Early. (opens in a new tab)</span></a>
      </div>

      <div class="res__item">
        <div>
          <h3>CDC Milestone Tracker app</h3>
          <p>Interactive, illustrated checklists on your phone, with reminders and tips. Free for iOS and Android.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.cdc.gov/act-early/milestones/index.html" target="_blank" rel="noopener">Visit<span class="visually-hidden"> the Milestone Tracker app page (opens in a new tab)</span></a>
      </div>

      <div class="res__item">
        <div>
          <h3>Milestones in Action</h3>
          <p>A photo and video library showing what each milestone actually looks like, which helps when a checklist item is hard to picture.</p>
        </div>
        <a class="btn btn--ghost" href="https://www.cdc.gov/act-early/milestones-in-action/index.html" target="_blank" rel="noopener">Visit<span class="visually-hidden"> Milestones in Action (opens in a new tab)</span></a>
      </div>
    </div>

    <div class="ms__disc rv" style="margin-top:2.2rem">
      <p><strong>A note on the obvious.</strong> Several links here go to programs you can use without
      ever contacting us. That is on purpose. If BabyNet is the right door for your family and we are
      not, we would rather you walk through it than wait. The Central Referral Team is at
      <a href="tel:+18665128881">1-866-512-8881</a>.</p>
    </div>
  </div>
</section>'''

# ================================================================= ABOUT
about = phero(
    "About",
    f"Hi, I'm {OWNER}",
    "Early Bloomers was born from a leap of faith and a deep passion for serving children and "
    f"families. Here's how it started, and why I'm honored to walk alongside yours."
) + f'''
<section class="band">
  <div class="wrap">
    <div class="split rv">
      <figure class="portrait">
        <img src="Images/MichelleWakefieldLopez.jpg"
             alt="{OWNER}, {OWNER_TITLE} at Early Bloomers, pictured with her husband"
             loading="lazy">
        <figcaption>{OWNER}, {OWNER_TITLE}</figcaption>
      </figure>

      <div>
        <p class="eyebrow">{SM}In my own words</p>
        <h2>A leap of faith</h2>
        <div class="story">
          <p>
            My name is {OWNER}, and I am the owner of Early Bloomers Early Intervention.
            Early Bloomers was born from a leap of faith and a deep passion for serving children
            and families. After nearly a decade as an Early Interventionist, I felt God calling me
            to step out of the familiar and build something of my own: an organization rooted in
            compassion, excellence, and the belief that every child deserves the opportunity to
            thrive.
          </p>
        </div>
      </div>
    </div>

    <div class="story story--full rv">
      <p>
        The journey wasn't without uncertainty. Starting a business came with countless unknowns,
        but God faithfully opened doors every step of the way. During the development of Early
        Bloomers, Bloom &amp; Blossom graciously welcomed me, providing support, encouragement, and
        the opportunity to continue serving families while laying the foundation for my own company.
        Their kindness became an important stepping stone in turning this dream into reality.
      </p>
      <p>
        Soon after taking that leap, my husband and I received another incredible blessing: we found
        out we were expecting our miracle baby after several years of infertility. It was a season
        filled with both new beginnings and constant reminders of God's faithfulness. As Early
        Bloomers continued to grow, so did my appreciation for His perfect timing.
      </p>
      <p>
        Today, Early Bloomers Early Intervention exists to partner with families, celebrate every
        milestone, and empower children to reach their fullest potential. I am honored to walk
        alongside families during some of the most important years of their children's lives, and I
        look forward to growing little minds one step at a time.
      </p>
    </div>

    <figure class="quote rv" style="max-width:900px;margin-inline:auto">
      <blockquote>
        &ldquo;More than just a business, it is the fulfillment of a calling and a testament to what
        God can do when we choose faith over fear.&rdquo;
      </blockquote>
      <figcaption>{OWNER}, {OWNER_TITLE}</figcaption>
    </figure>

    <ul class="creds creds--wide rv">
      <li>{STAR}<span>BabyNet Early Intervention Provider</span></li>
      <li>{STAR}<span>South Carolina BHDD-OIDD Provider</span></li>
      <li>{STAR}<span>Bachelor of Arts in Elementary Education, Bob Jones University, 2011</span></li>
      <li>{STAR}<span>In early intervention since 2015, with over eleven years of experience</span></li>
      <li>{STAR}<span>Serving {COUNTIES}</span></li>
    </ul>
  </div>
</section>

{slogan_band()}

<section class="band band--white">
  <div class="wrap">
    <div class="shead rv center">
      <p class="eyebrow">{SM}What I believe</p>
      <h2>Three things I hold to</h2>
    </div>
    <div class="tiles rv">
      <div class="tile">
        <h3>You lead</h3>
        <p>Parents are the most important people in a child's development. I bring strategies and information. You bring the expertise on your own child. That order matters.</p>
      </div>
      <div class="tile">
        <h3>Ordinary moments do the work</h3>
        <p>Strategies should fit naturally into the routines you already have. An hour a week matters because of what it changes in the other hundred and sixty-seven.</p>
      </div>
      <div class="tile">
        <h3>Every step gets celebrated</h3>
        <p>Progress in early intervention is rarely a leap. It's a step, then another. Each one is worth stopping to notice, and I will notice them with you.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="shead rv center">
      <p class="eyebrow">{SM}Questions</p>
      <h2>The things families ask first</h2>
    </div>

    <div class="faq rv">
      <details open>
        <summary>What ages do you work with?</summary>
        <div class="faq__a"><p>Birth to five years old. Children under three are typically served through BabyNet, and children over three through BHDD-OIDD.</p></div>
      </details>
      <details>
        <summary>Do I need a referral from my pediatrician?</summary>
        <div class="faq__a"><p>No. Anyone can make a referral: a parent, doctor, caregiver, teacher, or friend. You can contact me directly, or call the BabyNet Central Referral Team yourself at 1-866-512-8881.</p></div>
      </details>
      <details>
        <summary>What does it cost?</summary>
        <div class="faq__a"><p>Children who meet BabyNet eligibility criteria are served regardless of family income, and BabyNet services are provided at no cost to families.</p></div>
      </details>
      <details>
        <summary>Where do sessions happen?</summary>
        <div class="faq__a"><p>In your home, at your child's daycare, or in community settings. Whichever fits your family's routine best.</p></div>
      </details>
      <details>
        <summary>Which counties do you serve?</summary>
        <div class="faq__a"><p>{COUNTIES}. Three counties, because I drive to you, and I would rather cover a smaller area well than a wider one thinly.</p></div>
      </details>
      <details>
        <summary>Do you provide speech, occupational, or physical therapy?</summary>
        <div class="faq__a"><p>Not directly. I provide early intervention and developmental services and coordinate care. Speech therapy, occupational therapy, physical therapy, ABA, and other specialized services are referred to appropriate providers when your child needs them.</p></div>
      </details>
      <details>
        <summary>What are your hours?</summary>
        <div class="faq__a"><p>{HOURS}.</p></div>
      </details>
      <details>
        <summary>What if I'm not sure anything's actually wrong?</summary>
        <div class="faq__a"><p>That is the most common reason families call, and it's a good reason. An evaluation costs nothing and often ends with confirmation that your child is right on track. Knowing beats wondering, and if support would help, starting sooner makes it work better.</p></div>
      </details>
    </div>
  </div>
</section>'''

# ================================================================= CONTACT
contact = phero(
    "Refer a child",
    "Let's start with a conversation",
    "Tell me what you're noticing and I'll tell you honestly whether I think I can help. If I'm "
    "not the right fit, I'll point you to who is."
) + f'''
<section class="band" aria-labelledby="contact-h">
  <div class="wrap">
    <h2 class="visually-hidden" id="contact-h">Contact form and details</h2>
    <div class="contact rv">
      <form class="form" id="contact-form" data-to="{EMAIL}"
            action="https://formsubmit.co/{EMAIL}" method="POST">

        <!-- FormSubmit configuration -->
        <input type="hidden" name="_subject" value="New referral from the Early Bloomers website">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" class="visually-hidden" tabindex="-1" autocomplete="off" aria-hidden="true">

        <p class="form__req">Fields marked <span class="req">*</span> are required.</p>

        <fieldset>
          <legend>About you</legend>

          <div class="field">
            <label for="name">Your name <span class="req" aria-hidden="true">*</span></label>
            <input id="name" name="name" type="text" autocomplete="name" required aria-required="true">
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
            <label for="email">Email <span class="req" aria-hidden="true">*</span></label>
            <input id="email" name="email" type="email" autocomplete="email" required aria-required="true">
          </div>

          <div class="field">
            <label for="phone">Phone</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel">
          </div>
        </fieldset>

        <fieldset>
          <legend>About the child</legend>

          <div class="field">
            <label for="age">Age</label>
            <select id="age" name="child_age">
              <option value="">Select an age</option>
              <option>Under 6 months</option>
              <option>6&ndash;12 months</option>
              <option>12&ndash;18 months</option>
              <option>18&ndash;24 months</option>
              <option>2&ndash;3 years</option>
              <option>3&ndash;5 years</option>
              <option>Over 5 years</option>
            </select>
          </div>

          <div class="field">
            <label for="county">County</label>
            <select id="county" name="county">
              <option value="">Select a county</option>
              <option>Greenville</option>
              <option>Spartanburg</option>
              <option>Pickens</option>
              <option>Somewhere else</option>
            </select>
          </div>

          <div class="field">
            <label for="msg">What are you noticing? <span class="req" aria-hidden="true">*</span></label>
            <textarea id="msg" name="message" required aria-required="true" aria-describedby="msg-hint"></textarea>
            <p class="hint" id="msg-hint">It's okay to be vague. &ldquo;He's almost two and not really talking yet&rdquo; is plenty to start with.</p>
          </div>
        </fieldset>

        <p class="form__status" id="form-status" role="status" aria-live="polite"></p>

        <div>
          <button class="btn btn--primary" type="submit" id="form-submit">Send message</button>
        </div>

        <p class="form__note">
          <strong>What happens to what you send.</strong> This form is delivered to
          {EMAIL} and is used only to respond to you. It is not sold, shared, or added
          to any mailing list. Please don't include sensitive medical details here, since email
          isn't a secure channel. We'll cover those by phone once we're in touch.
        </p>
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

            <dt>Hours</dt>
            <dd>{HOURS}</dd>

            <dt>Service area</dt>
            <dd>{COUNTIES}</dd>
          </dl>
        </div>

        <div class="ms__disc" style="margin-top:22px">
          <p><strong>You can also skip us entirely.</strong> To refer a child from birth to three
          directly to South Carolina's early intervention system, call the BabyNet Central Referral
          Team at <a href="tel:+18665128881">1-866-512-8881</a>. Anyone can make that referral and
          it costs nothing. If we are not the right provider for your family, that number still is.</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

# ================================================================= WRITE
PAGES = [
    ("index.html",
     "Early Bloomers LLC &mdash; Early Intervention in Greenville, Spartanburg &amp; Pickens, SC",
     f"Early Bloomers LLC provides early intervention, developmental assessments, and service coordination for children birth to five across Greenville, Spartanburg, and Pickens counties, SC. {SLOGAN}",
     home),
    ("services.html", "Services &mdash; Early Bloomers LLC",
     "Early intervention sessions, developmental assessments across six areas, and service coordination linking your family to speech, OT, PT, and ABA.",
     services),
    ("milestones.html", "Milestones by Age &mdash; Early Bloomers LLC",
     "Developmental milestones from birth to five, adapted from the CDC's Learn the Signs. Act Early. program. A conversation starter, not a screening tool.",
     milestones),
    ("resources.html", "Resources &mdash; Early Bloomers LLC",
     "BabyNet, BHDD-OIDD, CDC milestone checklists, and the other doors into early intervention in South Carolina.",
     resources),
    ("about.html", f"About {OWNER} &mdash; Early Bloomers LLC",
     f"{OWNER}, {OWNER_TITLE}. BabyNet and BHDD-OIDD provider serving Greenville, Spartanburg, and Pickens counties since 2015.",
     about),
    ("contact.html", "Refer a Child &mdash; Early Bloomers LLC",
     f"Contact Early Bloomers LLC at {PHONE_DISPLAY} or {EMAIL}. Anyone can refer a child: parent, doctor, caregiver, teacher, or friend.",
     contact),
]

OG = {"about.html": "Images/MichelleWakefieldLopez.jpg"}

for name, title, desc, body in PAGES:
    (OUT / name).write_text(
        shell(name, title, desc, body, OG.get(name, "Images/Image1.jpg")),
        encoding="utf-8")
    print("wrote", name)
