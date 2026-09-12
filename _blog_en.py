# -*- coding: utf-8 -*-
"""
The nine blog articles, in English.

The editorial plan is Alex's: his nine titles, in his order, with his nine
categories. What his folder left "to be written" is written here.

Editorial line, the same as the rest of the site: no invented figures, no
statistics without a source, nothing that contradicts the published terms
and conditions. Where a market price is quoted, it is quoted as a range
and dated, because it moves.

SEO angle: each article targets a question Swiss SMEs actually type,
answers it in the first two paragraphs, then develops. The H1 picks up the
question, the H2s are sub-questions, and the internal links point to the
pages that monetise (pricing, packages, quote, brief).
"""

INDEX = {
    "sur_titre": "The journal",
    "h1": ["What we wish someone", "had told us sooner."],
    "lede": "Nine short articles, written for Swiss SMEs. Real prices, real "
            "lead times, and what we would do in your place.",
    "sec_t": "The articles.",
    "sec_c": "Ordered from the most asked to the most technical. None of "
             "them needs the others to be worth reading.",
    "appel_h2": "A question that isn't covered here?",
    "appel_p": "Write it to us, we answer the same day, Monday to Friday. "
               "And if the answer is useful to other people, it becomes an "
               "article.",
}

ARTICLES = [
 {
  "slug": "prix-site-web-suisse.html",
  "cat": "Pricing",
  "titre": "What does a website really cost in Switzerland in 2026?",
  "h1": ["How much does a website", "really cost in Switzerland?"],
  "desc": "The four brackets on the Swiss market, what really pushes the "
          "bill up, and the annual costs nobody puts a figure on at the start.",
  "dek": "Short answer: between CHF 300 and CHF 30,000. The gap is not a "
         "question of quality, it is a question of what you are buying. "
         "Here is how to read a quote.",
  "lecture": "7 min",
  "corps": """
<p>Nobody ever answers this question, and it is irritating. So let us
start with the figure: in Switzerland, in 2026, a professional website for
a small business costs between <strong>CHF 300 and CHF 30,000</strong>.
That hundredfold gap is not a gap in quality. It is a gap in scope — and
above all in billed human hours.</p>

<p>The rest of this article is about working out which bracket you are in,
and about not paying for one bracket to get the contents of the one
below.</p>

<h2>The four brackets on the Swiss market</h2>

<p><strong>CHF 0 to 500 — you do it yourself.</strong> An online builder,
a template from the catalogue, your copy, your photos. The real cost is
not the subscription, it is your weekend. Count twenty to forty hours for
a decent result, more if you are learning the tool as you go. Viable if
your site is only a business card.</p>

<p><strong>CHF 300 to 1,500 — the fixed package.</strong> A professional
works from a structure they have already proven, you fill in a brief, they
deliver within a few days. This is where we sit, with firm packages at
<a href="../offres/pro-landing-page.html">CHF 290</a>,
<a href="../offres/ultimate-website.html">CHF 490</a> and
<a href="../offres/advanced-website.html">CHF 690</a>. The price holds
because the scope is fixed in advance, not because the work is rushed.</p>

<p><strong>CHF 3,000 to 12,000 — bespoke work from a freelancer or a small
studio.</strong> You start from a blank page: workshops, site structure,
mock-ups, rounds of feedback, build. Two to eight weeks. This is the right
budget as soon as your site has to do something particular — a
configurator, a booking system, a catalogue that changes.</p>

<p><strong>CHF 15,000 to 30,000 and beyond — the agency.</strong>
Strategy, art direction, copywriting, development, follow-up, and several
people around the table. Justified when the site is a main sales channel
and one point of conversion gained is worth tens of thousands of francs a
year.</p>

<h2>What really pushes the bill up</h2>

<p>It is almost never the design. It is, in order:</p>

<ul>
  <li><strong>Unbounded rounds of feedback.</strong> A project with no
  written scope drifts, and drift is billed by the hour. It is the first
  hidden line item in every quote.</li>
  <li><strong>The content.</strong> If the agency has to write your copy,
  interview your teams and bring in a photographer, you are funding three
  trades, not one.</li>
  <li><strong>The features.</strong> Online payment, client area, booking,
  syncing with your management software:
  each one is a small project.</li>
  <li><strong>Multiple languages.</strong> Every language adds
  translation, proofreading and maintenance that multiplies.</li>
  <li><strong>The CMS.</strong> Making a site editable by you often
  doubles the build time. Useful if you publish every week, pointless if
  you change a phone number once a year.</li>
</ul>

<h2>The annual costs nobody puts a figure on</h2>

<p>The build quote is half the story. Here is what comes back every year,
in Switzerland, at 2026 market rates:</p>

<ul>
  <li><strong>A <code>.ch</code> domain name</strong> — about ten
  francs a year. A <code>.com</code>, about fifteen.</li>
  <li><strong>Hosting</strong> — from CHF 0 for a static site on a
  platform such as Netlify or Cloudflare Pages, to CHF 200–400 a year
  for shared Swiss hosting, more for a dedicated server.</li>
  <li><strong>Professional email addresses</strong> — CHF 60 to 150
  a year per mailbox depending on the provider. This is often the
  surprise.</li>
  <li><strong>HTTPS certificate</strong> — free today
  (Let's Encrypt), and automatic with most hosts. If you are being
  billed for one, ask why.</li>
  <li><strong>Maintenance</strong> — from CHF 0 for a static site to
  CHF 600–1,800 a year for a WordPress that has to be updated, and
  really does have to be updated: it is the leading cause of small
  business sites being hacked.</li>
</ul>

<p>Put another way: a CHF 2,000 site that costs CHF 1,200 a year to
maintain is more expensive, over five years, than a CHF 5,000 site that
costs nothing but its domain.</p>

<h2>What a firm package changes</h2>

<p>A firm price moves the risk. If the project takes longer than expected,
that is the supplier's problem, not yours. In exchange, the scope is
written down before anything starts: number of pages, number of
languages, what is included, what is the subject of a separate quote.</p>

<p>It is that framework that lets us publish a <a
href="../index.html#tarifs">public price list</a> and deliver
<strong>from two working days</strong> once the brief is complete, with
<strong>thirty days of unlimited revisions</strong> and a
<strong>full refund</strong> if the result does not suit you. Our <a
href="../legal/conditions.html">terms and conditions</a> say so in black
and white, which is the only place where a commercial promise is worth
anything.</p>

<h2>What to budget, in practice</h2>

<ul>
  <li><strong>A tradesperson or freelancer, one page that presents the
  work and gets the phone ringing</strong> — CHF 300 to 800 to build,
  under CHF 50 a year.</li>
  <li><strong>A service business, four to six pages, one language</strong> —
  CHF 500 to 2,500 to build.</li>
  <li><strong>A Swiss business that has to exist in French and in
  German</strong> — CHF 700 to 4,000, with translation weighing more than
  design.</li>
  <li><strong>A shop selling online</strong> — CHF 3,000 to 15,000,
  and a real time budget for the catalogue.</li>
</ul>

<p>If you are hesitating between two brackets, the useful question is not
“what budget do I have?” but “what is one client worth to me?”. A practice
where one client is worth CHF 3,000 pays for a CHF 5,000 site with two
clients. A shop whose average basket is CHF 40 has to reason
differently.</p>

<h2>Three questions we get asked</h2>

<h3>Is a CHF 290 site possible, or is it bait?</h3>
<p>It is possible on three conditions: one page and not eight, a
structure already proven rather than a blank page, and a brief you fill in
yourself. Remove one of those three conditions and the price doubles. Our
<a href="../offres/pro-landing-page.html">Landing Pro</a> says exactly
what it contains and what it does not.</p>

<h3>Why do two quotes for the same site vary threefold?</h3>
<p>Because they do not describe the same work. Compare the number of
pages, the number of correction rounds included, who writes the copy, who
supplies the photos, and what happens if you change your mind. Nine times
out of ten the gap is there, and not in the talent.</p>

<h3>Should you pay a monthly subscription?</h3>
<p>Only if you receive something every month — changes, monitoring, a
report. A subscription that only funds the hosting of a static site can
be replaced by ten francs of domain name a year.</p>
""",
  "faq": [
    ("How much does a website cost for a small business in Switzerland?",
     "Between CHF 300 and CHF 30,000 depending on scope. A package for a "
     "one- to seven-page brochure site sits between CHF 300 and CHF 1,500; "
     "a bespoke project with features starts around CHF 3,000."),
    ("What are the annual costs of a website?",
     "The domain name (around CHF 10 a year for a .ch), hosting (from free "
     "for a static site to CHF 400 a year), professional email addresses "
     "(CHF 60 to 150 per mailbox per year) and maintenance if the site runs "
     "on a CMS."),
    ("Is a firm package cheaper than an hourly quote?",
     "Not systematically, but it is predictable: the scope is written down "
     "before the work starts and any time overrun is the supplier's "
     "problem."),
  ],
 },

 {
  "slug": "landing-page-ou-site-complet.html",
  "cat": "Deciding",
  "titre": "Landing page or full website: how to choose",
  "h1": ["Landing page or full website.", "How to choose."],
  "desc": "The question is not the number of pages, it is the number of "
          "decisions your visitor has to make. A test in three questions.",
  "dek": "A single page is not a cut-price version of a website. It is a "
         "different tool, which wins in some cases and loses in others.",
  "lecture": "5 min",
  "corps": """
<p>We are almost always asked “how many pages do I need?”. It is the wrong
question: it is about quantity when the problem is a problem of journey.
The right question is <strong>how many different decisions does your
visitor have to make</strong> before contacting you.</p>

<p>One decision, one page. Several decisions, several pages.</p>

<h2>When a single page is enough</h2>

<p>A single page works when all your visitors want the same thing, and
there is only one action at the end: to call, to book, to ask for a
quote.</p>

<ul>
  <li>A tradesperson who wants to be called about jobs.</li>
  <li>A restaurant: the menu, the opening hours, the address, the booking.</li>
  <li>A practice or a therapist with a single main service.</li>
  <li>A single offer launched for a campaign, with a form at the end.</li>
</ul>

<p>Its advantage is not the price, it is the absence of choice. On a
well-built page, the visitor scrolls down and arrives at the form. On an
eight-page site, they wander around the menu and leave. It is also why a
single page goes live <a href="../index.html#process">in two working
days</a>: there is less to decide, so less to arbitrate.</p>

<h2>When you need several</h2>

<p>Several pages become necessary as soon as one of these three things is
true.</p>

<p><strong>You have several services that do not speak to the same
people.</strong> An accountancy firm doing bookkeeping, tax and payroll
has three audiences. A single page mixes them together and convinces none
of them. Three pages, each with its own vocabulary, are also three front
doors for Google: it is the most profitable reason to add pages.</p>

<p><strong>You need to be found on different searches.</strong>
Google ranks pages, not sites. “Roofer Lausanne” and “roof repair
Lausanne” deserve two pages, otherwise you rank halfway on both.</p>

<p><strong>Trust takes room.</strong> The higher the basket, the more the
visitor wants references, reviews, an “about” page, sometimes terms. A
CHF 15,000 purchase is not decided on a page that scrolls.</p>

<h2>The three-question test</h2>

<ol>
  <li><strong>How many different services do you want to sell?</strong>
  One: one page. Two to five: one page per service.</li>
  <li><strong>How many different Google searches do you want to
  win?</strong> Count one page per important search.</li>
  <li><strong>Does your visitor need to check something before writing to
  you?</strong> If so, plan the page that lets them do it — references,
  reviews, team.</li>
</ol>

<p>Add it up. One page if the total is one, five pages if the total is
around four or five, seven if you have a real catalogue of services. That
is exactly the logic of our three tiers:
<a href="../offres/pro-landing-page.html">Landing Pro</a> for one page,
<a href="../offres/ultimate-website.html">Site Complet</a> up to five,
<a href="../offres/advanced-website.html">Site Étendu</a> up to seven and
in three languages.</p>

<h2>The most frequent mistake</h2>

<p>Ordering eight pages and filling only three. A half-empty site inspires
less confidence than one dense, finished page, and it costs more to
produce and to maintain. If you do not have the content today, take fewer
pages today.</p>

<p>The opposite mistake exists too: piling five services onto a single
page because it cost less. The visitor does not read the sixth section,
and Google does not know what to rank you on.</p>

<h2>And if I get it wrong?</h2>

<p>It does not matter, on two conditions. The first: that the site is
built so that a page can be added without rebuilding it. The second: that
<a href="../legal/conditions.html">your domain name is in your name</a> —
it is the domain that carries your search ranking, not the site.</p>

<p>In practice, most of our clients start with one page, watch where their
calls come from for three months, then add the two or three pages the
calls have pointed out. It is less elegant than a perfect plan, and far
more effective.</p>

<p>If you are still hesitating, <a href="../devis.html">write us the three
answers to the test</a>: we will tell you which of the three tiers suits
you, including when the answer is the cheapest one.</p>
""",
  "faq": [
    ("Is a landing page enough to be visible on Google?",
     "Yes for one main search, no for several. Google ranks pages: a single "
     "page ranks well on one subject, but cannot cover “trade + town” and "
     "three distinct services."),
    ("Can pages be added later?",
     "Yes, if the site was built for it. It is the most common path: start "
     "with one page, watch where the calls come from for three months, then "
     "add the pages that are useful."),
  ],
 },

 {
  "slug": "fiche-google-business.html",
  "cat": "Visibility",
  "titre": "Google Business Profile: the setting most small businesses get wrong",
  "h1": ["Google Business Profile:", "the setting everyone gets wrong."],
  "desc": "The primary category decides half of your local visibility. And "
          "almost nobody chooses it correctly.",
  "dek": "For a local business, the Google profile often weighs more than "
         "the site itself. A single field decides most of it.",
  "lecture": "6 min",
  "corps": """
<p>If you serve clients within a thirty-kilometre radius, your Google
Business Profile probably brings you more calls than your site. It is what
appears in the map block, at the top, before the classic results — and it
is free.</p>

<p>There is one field in that profile that weighs more than all the
others, and that most Swiss SMEs fill in the wrong way: the
<strong>primary category</strong>.</p>

<h2>The setting that gets missed</h2>

<p>Google asks you for a primary category and allows secondary
categories. Almost everyone picks the primary category the most natural
way — the one that describes the trade in the broad sense — and that is
exactly the mistake.</p>

<p>The primary category is what determines <em>which searches</em> Google
will consider showing you on. The secondary ones carry only marginal
weight. So:</p>

<ul>
  <li>If you are a joiner but 80% of your turnover comes from bespoke
  kitchens, the primary category has to be the kitchen one, not
  “Joiner”.</li>
  <li>If you are a physiotherapist specialising in sport, the sport
  category becomes the primary one.</li>
  <li>If you are an accountant but mostly sell tax returns to private
  individuals, choose the tax category.</li>
</ul>

<p>The right method is mechanical: type into Google the search you want to
win, look at the three profiles that come out in the map block, open them,
read their primary category. Take the same one. You do not have to guess
what Google associates with what: it shows you.</p>

<h2>The fields that actually move the ranking</h2>

<p>Local ranking rests on three pillars — relevance, distance and
prominence. You cannot act on distance. That leaves the following fields,
in order of observed effect:</p>

<ol>
  <li><strong>The primary category</strong>, as we have just seen.</li>
  <li><strong>The exact business name.</strong> Use the real name, as it
  appears on your shopfront and on your invoices. Adding keywords to it
  (“Dupont Plumbing Geneva 24h Callout”) is against Google's rules and
  exposes you to suspension.</li>
  <li><strong>The services.</strong> An underused field: you can list your
  services one by one, each with a description. Every entry is one more
  keyword, and a legitimate one.</li>
  <li><strong>The service area.</strong> If you travel to clients, declare
  the municipalities. If you receive them, give an address and declare
  none.</li>
  <li><strong>The opening hours, including public holidays.</strong>
  Google shows “hours might differ” when they are not confirmed, and that
  doubt costs calls.</li>
  <li><strong>The website link.</strong> Point it at the page that talks
  about the service concerned, not systematically at the home page.</li>
</ol>

<h2>Photos: the rule of three</h2>

<p>Profiles that convert have, at a minimum: the exterior with the sign
visible (the client has to recognise the place on arrival), the interior,
and the finished work. Add a few every month rather than thirty at once:
a living profile is treated better than a frozen one.</p>

<p>Avoid stock images. They are spotted, and they remove precisely what
the profile is meant to provide: proof that you really exist in that
place.</p>

<h2>Reviews, without begging for them</h2>

<p>The number of reviews and their regularity count for more than the
average score. A profile at 4.6 with one review a month gets ahead of a
profile at 5.0 that has been frozen for two years.</p>

<p>What works, in order: asking at the right moment (just after the work
is finished, never through a bulk reminder), giving the short review link
that Google generates in your dashboard, and <strong>replying to every
review</strong>, including the bad ones, in two lines and without
justifying yourself. The replies are read by prospects far more than by
their authors.</p>

<p>What does not work: buying reviews (detected, and punished by removal
of the profile), asking for them in exchange for a discount (prohibited),
or putting a tablet on the counter that collects ten reviews from the same
IP address.</p>

<h2>What makes a profile fall</h2>

<ul>
  <li>An address or a phone number different from the one on the site.
  Make sure name, address and telephone are rigorously identical
  everywhere: profile, site, directories, social networks.</li>
  <li>Keywords stuffed into the business name.</li>
  <li>A home address declared as a shop when you receive nobody.</li>
  <li>Two profiles for the same business — it happens after a change of
  company name, and it cuts your prominence in half.</li>
  <li>Silence. A profile nobody ever touches loses ground to a profile
  that is maintained.</li>
</ul>

<h2>So what about the site?</h2>

<p>The profile brings the call; the site makes the sale. Prospects who
hesitate open your site from the profile: if it does not exist, or if it
is dated, you lose part of what the profile brought you. The two work
together, and the most profitable move is to match the profile's flagship
service with a dedicated page on the site.</p>

<p>That is what <a href="../index.html#methode">The Local Client
Method</a> covers, the guide we hand over with the
<a href="../offres/ultimate-website.html">Site Complet</a>: the Google
profile, “trade + town” searches, and how to get cited by ChatGPT when
someone is looking for your trade near where they live.</p>
""",
  "faq": [
    ("Which primary category should you choose on Google Business Profile?",
     "The one for your most profitable service, not the one for your trade "
     "in the broad sense. Method: type the search you want to win, open the "
     "profiles that come out in the map block and take their primary "
     "category."),
    ("Can you add keywords to your business name?",
     "No. Google's rules require the real business name; adding keywords "
     "exposes the profile to suspension."),
    ("Does the average score count more than the number of reviews?",
     "No. The regularity of reviews and the replies given weigh more than a "
     "perfect score obtained two years ago."),
  ],
 },

 {
  "slug": "que-mettre-sur-sa-page-d-accueil.html",
  "cat": "Copywriting",
  "titre": "What to write on your home page",
  "h1": ["What to write", "on your home page."],
  "desc": "Five seconds to answer three questions. The plan of a home page "
          "that gets the phone ringing, section by section.",
  "dek": "Your visitor gives your home page about as long as a red light. "
         "Here is the order in which they want their answers.",
  "lecture": "6 min",
  "corps": """
<p>A visitor arriving on your home page asks three questions, in this
order: <strong>where am I, is this for me, and what do I do now?</strong>
They give you a few seconds for all three. Anything that does not serve
those answers can move down or disappear.</p>

<p>Here is what we write, in the order we write it.</p>

<h2>1. The top line</h2>

<p>It says what you do, for whom, and where. Nothing else. It does not
have to be beautiful, it has to be accurate.</p>

<ul>
  <li>✗ “Excellence at the service of your projects”</li>
  <li>✓ “Electrician in Nyon, same-day callouts”</li>
  <li>✗ “Let's reinvent your communication together”</li>
  <li>✓ “Logos and visual identities for Swiss SMEs, in two weeks”</li>
</ul>

<p>Simple test: show the sentence to someone who does not know your trade.
If they cannot repeat what you sell, it needs rewriting. And if your trade
is local, put the town in it: that is not search optimisation, it is
courtesy towards the visitor.</p>

<h2>2. The button, straight away</h2>

<p>The first call to action goes in the first screen, next to the top
line. Some visitors have already made up their mind: do not make them
scroll.</p>

<p>A label that says what is going to happen converts better than a vague
one. “Request a quote” rather than “Find out more”. “Book a table” rather
than “Contact”. And one main button only: two buttons of equal weight is
one more decision to make.</p>

<h2>3. The three reasons to stay</h2>

<p>Just below the first screen, three short arguments. Not ten. They
answer “is this for me?” and they have to be
<strong>verifiable</strong>: a lead time, a price, an area, a guarantee, a
figure you can prove.</p>

<p>“Quality, professionalism, responsiveness” says nothing because nobody
would write the opposite. “Quote within 24 hours, firm price, callouts in
the canton of Vaud” says something.</p>

<h2>4. The proof</h2>

<p>This is the most neglected and the most profitable section. In order of
power: photos of your real work, named reviews, client logos, figures.</p>

<p>A rule we apply to ourselves: <strong>if you do not have it, do not
invent it</strong>. A fake review gets spotted, and the day it is spotted
it takes everything else with it. When you are starting out and have
nothing to show yet, say so and replace the proof with transparency: your
prices, your method, your terms. It works better than people think.</p>

<h2>5. The objections, before they block</h2>

<p>Your visitor has two or three reasons not to write to you. “It is
probably too expensive.” “This is going to take months.” “I will end up
locked in.” Deal with them explicitly, on the page: a price or a range, a
lead time, what happens if things go wrong.</p>

<p>It feels counter-intuitive to write a price when you believe the price
scares people off. In practice, the absence of a price scares them off
more: it leaves the visitor imagining the worst and going to whoever does
display one. That is why <a href="../index.html#tarifs">our three prices
are public</a>.</p>

<h2>6. The reminder of the action</h2>

<p>Repeat the call to action at the bottom, and give it in two forms: a
form for those who write, a number or a WhatsApp for those who prefer to
talk. Add what you do with the request: “we answer the same day, Monday to
Friday”. The visitor wants to know what they are getting into.</p>

<h2>What to take out</h2>

<ul>
  <li><strong>The word “Welcome”.</strong> It occupies the most-read line
  on the page to say nothing.</li>
  <li><strong>The company history, at the top.</strong> It is of interest,
  but later. Its place is an “about” page.</li>
  <li><strong>The carousel that scrolls by itself.</strong> Nobody sees
  the third image, and it slows the page down.</li>
  <li><strong>Stock images.</strong> A photo of your workshop taken on a
  phone is worth more than an American office set.</li>
  <li><strong>Long paragraphs.</strong> Two or three sentences, never
  more, and subheadings that read on their own.</li>
</ul>

<h2>The final test</h2>

<p>Have someone from outside read your home page on a phone, stopwatch in
hand, for five seconds. Then ask them what you sell, to whom, and what
they would do to contact you. If the three answers come out, the page is
good. If not, it is not the design that needs changing, it is the order of
the sections.</p>

<p>We ask these questions in our <a href="../brief.html">starting
brief</a>: it is the part that takes clients the longest, and the one that
makes all the difference to the result.</p>
""",
  "faq": [
    ("Should you display your prices on your site?",
     "In the vast majority of cases, yes — at least a range. The absence of "
     "a price sends the visitor to a competitor who displays one, and wastes "
     "time on enquiries that are outside the budget."),
    ("What is the first thing to write on a home page?",
     "A sentence that says what you do, for whom and where. If someone from "
     "outside your trade cannot repeat it, it needs rewriting."),
  ],
 },

 {
  "slug": "wix-squarespace-ou-sur-mesure.html",
  "cat": "Comparing",
  "titre": "Wix, Squarespace or bespoke: the honest comparison",
  "h1": ["Wix, Squarespace", "or bespoke?"],
  "desc": "What each solution does very well, where each one struggles, and "
          "the real cost over three years for a Swiss SME.",
  "dek": "We are judge and party: we sell bespoke work. All the more reason "
         "to say precisely in which cases online builders are the right "
         "choice.",
  "lecture": "7 min",
  "corps": """
<p>Let us say it straight away: we sell hand-built sites. A comparison
written by us is therefore not neutral. We are still going to try to be
accurate, because there are genuine cases where an online builder is the
better decision, and where you would be wasting your money with us.</p>

<h2>What Wix does very well</h2>

<ul>
  <li><strong>Starting today, without anyone.</strong> You can have a site
  online this afternoon, on your own, with no skills.</li>
  <li><strong>Everything in one place.</strong> Domain, hosting,
  certificate, forms, shop, booking, newsletter: one invoice, one
  password.</li>
  <li><strong>Editing it yourself, genuinely.</strong> The editor is very
  permissive: you move an element wherever you want.</li>
  <li><strong>Trade features.</strong> Appointment booking, class
  timetables, reservations: available in a few clicks, whereas rebuilding
  them would cost thousands of francs.</li>
</ul>

<h2>What Squarespace does very well</h2>

<ul>
  <li><strong>The visual result by default.</strong> The templates are
  more polished and harder to break. For a photographer, an architect, a
  restaurant, the result is good with no art direction.</li>
  <li><strong>Consistency.</strong> The global style system avoids the
  site that goes off in twelve directions after six months.</li>
  <li><strong>Selling small catalogues.</strong> Twenty or so products or
  a handful of services: it is clean and sufficient.</li>
</ul>

<h2>Where both struggle</h2>

<p><strong>Speed.</strong> These platforms load a lot of code in order to
stay editable in the browser. On a phone on 4G, it shows. Speed is a
Google ranking criterion, and above all a criterion for abandonment: the
visitor closes the page before having seen your offer.</p>

<p><strong>Leaving.</strong> This is the most serious point and the least
discussed. You cannot take your site with you: you generally recover your
copy, your images and your domain name, but not the layout. Changing
platform means rebuilding. The subscription is therefore not only a rent,
it is an exit cost that grows with time.</p>

<p><strong>Fine-grained search optimisation.</strong> The essentials are
accessible (titles, descriptions, page addresses). What is less so:
precise control of the markup, advanced structured data, handling
multiple languages. For a local site it will do. For an ambitious content
strategy it holds you back.</p>

<p><strong>Multiple languages.</strong> Possible, but often the most
painful part — and in Switzerland it is rarely optional.</p>

<p><strong>The price that climbs.</strong> The entry rate almost never
includes what you need. The useful features (shop, booking, removing the
advertising, email addresses) are on higher tiers, and the tiers go up
over the years.</p>

<h2>What bespoke does very well</h2>

<ul>
  <li><strong>Speed.</strong> A well-built static site loads almost
  instantly and needs no technical upkeep.</li>
  <li><strong>Belonging to you.</strong> The files are yours, with
  whichever host you want, and transferable elsewhere.</li>
  <li><strong>Saying exactly what you want to say.</strong> No template to
  work around.</li>
  <li><strong>The running cost.</strong> Often the price of the domain,
  and nothing else.</li>
</ul>

<p>And its limits, which are real: you depend on someone for heavy
changes, you need a brief at the start, and trade features (booking,
calendars, shop) are a separate budget instead of being included.</p>

<h2>The real cost over three years</h2>

<p>As an order of magnitude, for a Swiss SME, at the prices observed in
2026 — platform rates change, check them:</p>

<ul>
  <li><strong>Online builder, on a plan that suits a
  business</strong> — around CHF 20 to 35 a month, that is
  <strong>CHF 720 to 1,260 over three years</strong>, plus your build
  time, plus the higher tiers if you add the shop or the email
  addresses.</li>
  <li><strong>Hand-built package</strong> — CHF 290 to 690 once,
  plus around ten francs of domain a year, that is
  <strong>CHF 320 to 720 over three years</strong>.</li>
  <li><strong>Bespoke agency work</strong> — CHF 5,000 and up, justified
  when the site is a main sales channel.</li>
</ul>

<p>Over three years, the gap between a subscription and a package is
therefore small; over six years, it reverses clearly. What settles it is
not the price: it is ownership and speed.</p>

<h2>How to choose, in three cases</h2>

<p><strong>Take an online builder</strong> if you need booking or a
calendar right now, if you plan to change your site every week yourself,
or if you are testing an activity you do not yet know will last.</p>

<p><strong>Take a hand-built package</strong> if your site mainly has to
convince and get the phone ringing, if you do not want a subscription, or
if your local visibility matters more than the freedom to move everything
around.</p>

<p><strong>Take an agency</strong> if your site is the main sales channel
and one point of conversion gained runs into tens of thousands of
francs.</p>

<h2>One thing to do in every case</h2>

<p>Buy your domain name in your own name, on an account that belongs to
you, whatever solution you go for. It is the only irreplaceable element: a
site can be rebuilt, an address with ten years of history cannot. If your
domain is currently in a supplier's name, <a
href="recuperer-son-nom-de-domaine.html">here is how to get it
back</a>.</p>

<p>And if you want to know which case you fall into, <a
href="../devis.html">describe your situation in three lines</a>: we will
tell you, including when the answer is “take a subscription, that will be
enough for you”.</p>
""",
  "faq": [
    ("Can you take your site with you when leaving Wix or Squarespace?",
     "You recover your copy, your images and your domain name, but not the "
     "layout: changing platform means rebuilding the site."),
    ("Is a bespoke site faster than a Wix site?",
     "Generally yes: a hand-built static site loads far less code, because "
     "it does not have to stay editable in an online editor."),
    ("Which solution costs the least over three years?",
     "A one-off package with nothing but a domain name to maintain generally "
     "stays below the total of a monthly subscription over three years, and "
     "the gap widens after that."),
  ],
 },

 {
  "slug": "sept-sections-landing-page.html",
  "cat": "Conversion",
  "titre": "The 7 sections of a landing page that converts",
  "h1": ["The seven sections", "of a page that converts."],
  "desc": "The order that works, section by section, with what to write in "
          "each one and the mistake not to make in it.",
  "dek": "A page that converts is not a page that persuades. It is a page "
         "that answers objections in the order in which they arrive.",
  "lecture": "6 min",
  "corps": """
<p>A single page whose only purpose is to get one action done — a call, a
booking, a completed form — almost always follows the same plan. Not out
of laziness, but because a visitor's objections arrive in a fairly stable
order.</p>

<p>Here are the seven sections, the objection each one handles, and the
mistake we see most often.</p>

<h2>1. The hook</h2>

<p><em>Objection handled: “am I in the right place?”</em></p>

<p>What you do, for whom, where, and a button. One sentence, a one-line
subheading, a call to action. That is all that should fit in the first
screen of a phone.</p>

<p><strong>The mistake:</strong> a mood sentence (“Let's bring your ideas
to life”) that forces the visitor to scroll to understand your trade. They
do not scroll: they leave.</p>

<h2>2. The three supporting points</h2>

<p><em>Objection handled: “why you?”</em></p>

<p>Three verifiable arguments, short, aligned. A lead time, a price, an
area, a guarantee. Three, because two looks thin and five no longer gets
read.</p>

<p><strong>The mistake:</strong> qualities nobody would claim the opposite
of. “Professionalism, quality, attentiveness” is not an argument, it is a
minimum.</p>

<h2>3. The proof</h2>

<p><em>Objection handled: “does this actually work?”</em></p>

<p>Photos of real work, signed reviews, logos, figures. Place it early —
just after the supporting points — because it is what allows the visitor
to read the rest.</p>

<p><strong>The mistake:</strong> inventing. A fabricated review is spotted
by its vocabulary, and it destroys the credibility of the whole page. If
you are starting out, replace proof with transparency: method, prices,
terms. We do exactly that on this site: our
<a href="../temoignages.html">reviews</a> are the ones we have, and not
one more.</p>

<h2>4. The how</h2>

<p><em>Objection handled: “what am I committing to?”</em></p>

<p>Three or four numbered steps: what you do, what the client does, how
long it takes. This section is enormously reassuring for an almost zero
writing cost, and it is the one most often forgotten.</p>

<p><strong>The mistake:</strong> describing your internal process. The
visitor wants to know what is going to happen to them, not how you
organise your files.</p>

<h2>5. The price</h2>

<p><em>Objection handled: “is this within my budget?”</em></p>

<p>A price, a range, or at the very least a reference point (“from”, “most
of our jobs are between X and Y”). Also say what is included and what is
not.</p>

<p><strong>The mistake:</strong> “quote on request”. The visitor does not
request: they assume it is expensive and go elsewhere. And you receive
enquiries outside the budget that cost you time. Our
<a href="../index.html#tarifs">three prices</a> are public for that reason
alone.</p>

<h2>6. The remaining objections</h2>

<p><em>Objection handled: “yes, but what if…”</em></p>

<p>A small FAQ of four to six questions, taking up what you actually get
asked on the phone. Write the real questions, including the awkward ones:
“what if I am not satisfied?”, “who owns the site?”, “what happens if you
disappear?”.</p>

<p><strong>The mistake:</strong> a self-serving FAQ that asks questions
whose answers suit you. It handles no obstacle and takes up space.</p>

<h2>7. The final action</h2>

<p><em>Objection handled: “what do I do now?”</em></p>

<p>The same call to action as at the top, with two channels: a short form
and a way to speak to someone. State the response time. And keep the form
short: every extra field loses submissions. A name, a means of contact and
two lines of message are almost always enough.</p>

<p><strong>The mistake:</strong> a twelve-field form asking for turnover
and headcount before the first exchange has even happened.</p>

<h2>What matters more than the order</h2>

<ul>
  <li><strong>Speed.</strong> A slow page loses visitors before section 2.
  It is the first thing to fix, before any rewriting.</li>
  <li><strong>Phone first.</strong> Most of your visitors are on mobile.
  Design for the phone screen, then check on a computer.</li>
  <li><strong>One single action.</strong> A page offering to call, to
  write, to subscribe, to download and to follow on Instagram gets nothing
  done at all.</li>
</ul>

<p>That is the plan we apply on the
<a href="../offres/pro-landing-page.html">Landing Pro</a>: five sections
at a minimum, seven when the content justifies it, and never two main
buttons competing for the same page.</p>
""",
  "faq": [
    ("How many sections should a landing page have?",
     "Five at a minimum, seven when the content justifies it. What matters "
     "is that each section handles a real objection, in the order in which "
     "it comes up."),
    ("How many fields should the form have?",
     "As few as possible: a name, a means of contact and two lines of "
     "message are almost always enough. Every extra field loses "
     "submissions."),
  ],
 },

 {
  "slug": "photos-professionnelles-site-web.html",
  "cat": "Photography",
  "titre": "Photos: when a professional shoot really changes something",
  "h1": ["Photos: when a shoot", "really changes something."],
  "desc": "The three cases where a photo shoot pays for itself, the three "
          "where it does not, and the brief to give the photographer.",
  "dek": "A shoot costs between CHF 400 and CHF 1,500 in Switzerland. "
         "Sometimes it is the best franc spent on the project, sometimes it "
         "is a franc lost.",
  "lecture": "5 min",
  "corps": """
<p>Photography is the line item people hesitate over most, because it is
visible and it is not indispensable. A professional shoot is negotiated,
in Switzerland, between CHF 400 for a half-day with a young photographer
and CHF 1,500 for a full day with retouching. Here is how to know whether
it is your case.</p>

<h2>What photography actually changes</h2>

<p>It does not make your offer better. It does two things: it
<strong>proves that you exist</strong>, and it <strong>shows the level of
finish</strong> of your work. That is all — and depending on the trade,
that is either enormous or negligible.</p>

<h2>The three cases where a shoot pays for itself</h2>

<p><strong>1. Your work is visible.</strong> Hairdressing, cooking,
joinery, interiors, bodywork, beauty, landscaping, flowers. The photo
<em>is</em> the sales argument. Here, bad photos cost more than no photos,
and a shoot is the first investment to make, before the site itself.</p>

<p><strong>2. People are buying a person.</strong> Therapist, lawyer,
coach, broker, notary, doctor. A decent portrait — looking at the camera,
soft light, neutral background — clearly increases the rate at which
people get in touch. No need for a full day: an hour is enough, and it is
the best value for money on the whole list.</p>

<p><strong>3. Your premises are an argument.</strong> Restaurant, hotel,
salon, practice, shop. The client wants to see where they are setting
foot. Here the shoot has to happen at the time of day when the place looks
best, which means blocking out a slot.</p>

<h2>The three cases where it is not the priority</h2>

<p><strong>1. Your work is invisible.</strong> IT, accountancy,
consulting, insurance, translation. Photographing people smiling in front
of a computer adds nothing. Put the money into the copy, into client
references and into the Google profile.</p>

<p><strong>2. You sell a product the manufacturer has already
photographed.</strong> Use their images: they are often better and
supplied free, just check that you have the right to use them.</p>

<p><strong>3. You do not yet know what you are selling.</strong> If your
offer is going to move in six months, the photos will too. Start with a
phone: you will do the shoot when the offer is stable.</p>

<h2>What a phone does very well</h2>

<p>A recent phone, at the right time of day, gives very good results.
Three rules are enough:</p>

<ul>
  <li><strong>Daylight, never the flash.</strong> Put the subject facing a
  window, not with their back to it. Outdoors, avoid the full midday sun:
  the end of the day is more flattering.</li>
  <li><strong>Clean up the frame.</strong> The trailing cable, the
  cardboard box, the bin. Cleaning the background does more for a photo
  than any filter.</li>
  <li><strong>Frame wide and horizontal.</strong> You can always crop in,
  never out. A vertical photo does not fit in a site banner.</li>
</ul>

<p>Keep the original files: a screenshot of a photo, or an image that has
been round WhatsApp three times, arrives beyond saving.</p>

<h2>The brief to give the photographer</h2>

<p>The difference between a useful shoot and a pretty one comes down to
what is asked for beforehand. Six lines are enough:</p>

<ol>
  <li>What the images are for — site, Google profile, social networks —
  and in which formats.</li>
  <li>Three compulsory images (for example: the frontage with the sign
  legible, the team, a finished job).</li>
  <li>One <strong>very wide, horizontal image</strong> for the top of the
  home page, with empty space on one side: that is where the text will
  sit.</li>
  <li>The style: two or three examples of sites you like, which is worth
  more than a page of adjectives.</li>
  <li>The rights: unlimited web use over time, and in writing.</li>
  <li>The delivery: original files at full resolution, plus a lightened
  version for the web.</li>
</ol>

<p>That last point matters: 8 MB images delivered as they are onto a site
make it slow, and a slow site loses visitors. We systematically resize and
compress what our clients send us, but it is better to start from the
right files.</p>

<h2>How much to spend on it</h2>

<ul>
  <li><strong>Portrait only</strong> — CHF 150 to 400 for an hour. Worth
  doing as soon as your face is your offer.</li>
  <li><strong>Half a day on site</strong> — CHF 400 to 800. Enough for a
  shop, a salon, a practice.</li>
  <li><strong>Full day</strong> — CHF 900 to 1,500. Justified when several
  services or several locations have to be covered.</li>
</ul>

<p>A useful benchmark: if your site costs CHF 500 and your photos
CHF 1,200, that is not absurd — in visual trades, the photography works
harder than the layout. The reverse is sometimes more so.</p>

<p>If your visual identity is being redone at the same time (logo,
colours, variants), this is the right moment: that is what the
<a href="../upsell-branding.html">Branding pack</a> is for, and it avoids
photographing a sign you are going to change three months later.</p>
""",
  "faq": [
    ("Is a professional photo shoot indispensable?",
     "No. It is decisive in trades where the work is visible (hairdressing, "
     "cooking, interiors) and in those where people are buying a person. It "
     "is secondary for intangible services."),
    ("How much does a photo shoot cost in Switzerland?",
     "From CHF 150 to 400 for a one-hour portrait, CHF 400 to 800 for a "
     "half-day on site, CHF 900 to 1,500 for a full day with retouching."),
  ],
 },

 {
  "slug": "premier-client-via-son-site.html",
  "cat": "Expectations",
  "titre": "How long before the first client through your site?",
  "h1": ["How long before", "the first client?"],
  "desc": "What happens week after week once a site goes live, the three "
          "sources of traffic and how fast each of them is.",
  "dek": "A site is not a switch. Depending on the source of traffic you "
         "turn on, the first client arrives in three days or in five "
         "months.",
  "lecture": "6 min",
  "corps": """
<p>This is the question we get asked right after the price, and the honest
answer is: it barely depends on the site. It depends on how people get to
it. There are three routes, and they do not move at anything like the same
speed.</p>

<h2>The three sources, and their timescale</h2>

<p><strong>The traffic you bring yourself — immediate.</strong> You put
the address in your email signature, on your quotes, on your van, in your
Instagram bio, and you send it to your contacts. First effect within a few
days. It is the most underestimated source and the only one that is both
free and instant.</p>

<p><strong>Advertising — a few days.</strong> Google Ads, Meta, and now
ads inside assistants such as ChatGPT. You pay, you have visitors
tomorrow. It is the only way to get volume straight away, and it stops the
day you stop paying.</p>

<p><strong>Organic search — two to six months.</strong> Google has to
discover your pages, assess them, then bring you up. For an
uncompetitive local search (“locksmith Morges”), count six to ten weeks.
For a contested search, six months and more. No serious supplier will
promise you better.</p>

<h2>What happens, week by week</h2>

<p><strong>Weeks 1 and 2.</strong> The site is live. Your visitors are the
ones you bring: friends and family, existing clients, contacts. The first
enquiries often come from clients you already had — they discover a
service they did not know about. That is a real gain, and nobody counts
it.</p>

<p><strong>Weeks 3 to 6.</strong> Google has indexed the pages. You start
appearing on your own name, then on very precise searches. The volume is
low but the quality is high: someone typing “roller shutter repair
Chêne-Bougeries” almost always calls you.</p>

<p><strong>Months 2 and 3.</strong> If your Google Business Profile is
properly set up, it becomes your first source of calls, ahead of the site.
The two work together: the profile brings them in, the site convinces
them. This is the moment when you see whether the pages say the right
things.</p>

<p><strong>Months 4 to 6.</strong> The search ranking of the service pages
settles in. If you have published a little content and collected a few
reviews, the curve straightens noticeably. It is also the moment when you
know which pages to add: the enquiries have told you.</p>

<h2>What really speeds things up</h2>

<ul>
  <li><strong>A complete Google Business Profile.</strong> Effect within a
  few days, and free. It is lever number one for a local business —
  <a href="fiche-google-business.html">the setting not to get wrong</a>.</li>
  <li><strong>Putting the address everywhere.</strong> Signature, quotes,
  invoices, van, shopfront, social networks. It costs nothing and often
  doubles first-month traffic.</li>
  <li><strong>One page per service.</strong> Five precise pages rank far
  better than one page that talks about everything.</li>
  <li><strong>Reviews, regularly.</strong> One a month is worth more than
  ten at once.</li>
  <li><strong>A small advertising budget at the start.</strong> CHF 200
  to 500 over three weeks is enough to find out whether your page
  converts, which is information you cannot get any other way.</li>
</ul>

<h2>What slows things down</h2>

<ul>
  <li><strong>A slow site.</strong> Visitors leave before reading the
  offer; the search ranking suffers too.</li>
  <li><strong>No price, no area, no lead time.</strong> The visitor does
  not ask, they assume, and they leave.</li>
  <li><strong>Waiting until you have everything.</strong> A site that is
  live and gets completed beats a perfect site in six months.</li>
  <li><strong>Changing domain name.</strong> You start again from zero.
  Choose it once and keep it.</li>
</ul>

<h2>What to measure</h2>

<p>Three figures, once a month, ten minutes:</p>

<ol>
  <li><strong>How many visitors</strong>, and where they come from
  (search, social, direct).</li>
  <li><strong>How many enquiries</strong> — forms, calls,
  WhatsApp.</li>
  <li><strong>How many clients</strong> out of those enquiries.</li>
</ol>

<p>The ratio between the first and the second figure judges your page. The
ratio between the second and the third judges your offer and the way you
answer. Two different problems: do not fix the site when it is the quote
that is the problem.</p>

<h2>An honest benchmark</h2>

<p>For a local Swiss SME with a properly set up Google profile, a clear
site and the address put everywhere: <strong>the first enquiries generally
arrive within two to four weeks</strong>, and the site becomes a regular
source somewhere between the third and the sixth month. With no Google
profile, no reviews and no address circulating, it can take a great deal
longer — and that is not a site problem.</p>

<p>If you want the plan for the first thirty days after going live, it is
part of <a href="../index.html#methode">The Local Client Method</a> that
we hand over with the
<a href="../offres/ultimate-website.html">Site Complet</a>.</p>
""",
  "faq": [
    ("How long does it take to be visible on Google after going live?",
     "A few days to be indexed, six to ten weeks to rank on an "
     "uncompetitive local search, six months and more on a contested "
     "search."),
    ("When does the first enquiry through a site arrive?",
     "Generally within two to four weeks for a local business that "
     "circulates its address and has a properly set up Google Business "
     "Profile."),
  ],
 },

 {
  "slug": "recuperer-son-nom-de-domaine.html",
  "cat": "Practical",
  "titre": "Getting your domain name back in five steps",
  "h1": ["Getting your domain", "name back in five steps."],
  "desc": "Your domain is in your former supplier's name? Here is the exact "
          "procedure, and what to do if they no longer reply.",
  "dek": "The domain name is the one part of your online presence that "
         "cannot be rebuilt. If it is not in your name, it is the first "
         "thing to fix.",
  "lecture": "6 min",
  "corps": """
<p>A site can be rebuilt. A domain name with eight years of history,
inbound links and your email addresses cannot. That is why we always buy
the domain in the client's name and why our
<a href="../legal/conditions.html">terms and conditions</a> provide for it
to be transferred on request and free of charge.</p>

<p>Not every supplier works this way. If yours holds your domain, here is
the procedure.</p>

<h2>Step 1 — Find out where it is and whose it is</h2>

<p>Two things to distinguish: the <strong>registrant</strong> (the legal
owner) and the <strong>registrar</strong> (the company the domain is
registered with).</p>

<p>For a <code>.ch</code>, the public directory of the Swiss registry
(SWITCH's <em>whois</em>, via nic.ch) gives you the registrar. For a
<code>.com</code>, ICANN's whois search. The registrant's details are
often hidden for data protection reasons, but the registrar is always
visible — and that is what you need.</p>

<p>Note the <strong>expiry date</strong> as well. If it is less than
fifteen days away, treat the matter as urgent: an expired domain can be
bought by anyone.</p>

<h2>Step 2 — Ask for the transfer, in writing</h2>

<p>Write the supplier a short, factual message, explicitly asking for
these three things:</p>

<ul>
  <li>the <strong>transfer authorisation code</strong> (called the auth
  code, EPP code or <em>authcode</em>);</li>
  <li>the <strong>unlocking</strong> of the domain (the <em>transfer
  lock</em>);</li>
  <li>the change of registrant to your name, if the domain is not already
  in your name.</li>
</ul>

<p>Set a reasonable deadline — ten working days — and keep a written
record. In the vast majority of cases that is enough: most suppliers have
no wish to hold hostage the domain of a client who is leaving.</p>

<h2>Step 3 — Open an account with a registrar, in your name</h2>

<p>Create the account with <strong>your</strong> email address and
<strong>your</strong> card — that account is what will make you the owner
for the next ten years. Do not use an address that depends on the domain
you are transferring: if the transfer goes wrong, you lose access to your
mailbox at the same time as the domain.</p>

<p>For a <code>.ch</code>, a Swiss registrar makes billing and support
simpler. The going rate is around ten francs a year; the price difference
between registrars is negligible, the quality of the support is not.</p>

<h2>Step 4 — Start the transfer</h2>

<p>From the new registrar: “transfer a domain”, then the name and the
authorisation code. The registry sends a confirmation request to the
registrant's address. Confirm it.</p>

<p>Count one to seven days depending on the extension. During that time,
<strong>your site and your emails carry on working</strong>: a registrar
transfer does not change the DNS. This is a frequent and unfounded
worry.</p>

<p>Two details that cause trouble: a domain registered or transferred less
than sixty days ago cannot be transferred again (an ICANN rule), and a
domain left locked will make the request fail without any clear
explanation.</p>

<h2>Step 5 — Check the DNS, and above all the email</h2>

<p>Once the transfer is complete, open the DNS zone at the new registrar
and compare it with the old one, line by line. Most registrars copy the
records across automatically, but not all.</p>

<p>Look in particular at:</p>

<ul>
  <li>the <strong>A</strong> and <strong>CNAME</strong> records, which
  point the site;</li>
  <li>the <strong>MX</strong> records, which bring in your email — this is
  <em>where</em> the accidents happen;</li>
  <li>the <strong>TXT</strong> records of the SPF, DKIM and DMARC type,
  without which your emails end up in the junk folder.</li>
</ul>

<p>Do the check on a weekday, in the morning, and send yourself a test
email from an outside address within the hour.</p>

<h2>If the supplier does not reply</h2>

<ol>
  <li><strong>Follow up in writing</strong>, by registered post if need
  be, citing your contract and setting a deadline.</li>
  <li><strong>Write to the registrar directly</strong> with your proof of
  ownership: renewal invoices, commercial register extract, registered
  trade mark. Registrars have a procedure for ownership disputes.</li>
  <li><strong>For a <code>.ch</code></strong>, the Swiss registry has a
  dispute resolution procedure; for generic extensions, it is WIPO's UDRP
  procedure. They are designed for cases of bad faith and they have a
  cost.</li>
  <li><strong>As a last resort</strong>, buy a variant
  (<code>.ch</code> instead of <code>.com</code>, or a slightly different
  name) and redirect. You lose history, but you take back control — and it
  is often less costly than a six-month procedure.</li>
</ol>

<h2>So that it does not happen again</h2>

<ul>
  <li>The domain is registered <strong>in your name</strong>, on an
  account <strong>you</strong> hold the credentials for.</li>
  <li>The account's email address does not depend on the domain itself.</li>
  <li>Automatic renewal is switched on, against a valid card.</li>
  <li>The transfer lock is switched on in normal times: that is what
  prevents a hijacking.</li>
  <li>Your credentials are written down somewhere other than in one
  person's head.</li>
</ul>

<p>We apply this by default: the domain is bought in your name, it remains
your property at all times, and it is transferred to you on request free
of charge, including if you go elsewhere. It is written in our terms,
which is the only place where it counts. If you have a domain to recover
before rebuilding your site, <a href="../devis.html">tell us</a>: it is an
operation we carry out regularly.</p>
""",
  "faq": [
    ("Do you lose your site and your email during a domain transfer?",
     "No. A registrar transfer does not change the DNS: the site and the "
     "email carry on working. Outages come from a DNS zone badly copied "
     "after the transfer, in particular the MX records."),
    ("What can you do if the former supplier refuses to hand the domain back?",
     "Follow up in writing with a deadline, then take it to the registrar "
     "with proof of ownership. There is a dispute resolution procedure for "
     ".ch domains and WIPO's UDRP procedure for generic extensions."),
    ("How much does a .ch domain name cost per year?",
     "Around ten francs a year with most registrars. The price gap between "
     "suppliers is negligible."),
  ],
 },
]


# ---------------------------------------------------------------------------
# Interface labels (everything that is not article body copy)
# ---------------------------------------------------------------------------

UI = {
    "accueil": "Home",
    "fil_blog": "Blog",
    "blog_titre": "Blog: websites and visibility for Swiss SMEs | Up2Front",
    "blog_desc": "Nine articles for Swiss SMEs: real prices, real lead "
                 "times, and what we would do in your place.",
    "date_texte": "12 September 2026",
    "meta": "Published on {date} · {lecture} read",
    "retour": "All articles",
    "voir_tarifs": "See pricing",
    "demander_devis": "Request a quote",
    "lire": "Read the article",
    "faq_t": "Frequently asked questions.",
    "faq_c": "The questions we get asked on this subject, with the short "
             "answer.",
    "suite_t": "Read next.",
    "suite_c": "Two more articles from the journal, on neighbouring subjects.",
    "art_appel_h2": "A view on your own case?",
    "art_appel_p": "Describe your business in three lines. We answer the "
                   "same day, Monday to Friday, and we also say when a "
                   "website is not your priority.",
    "art_appel_b1": "Request a quote",
    "art_appel_b2": "See pricing",
    "ecrire": "Write to contact@up2front.com",
}


# ---------------------------------------------------------------------------
# Referral page — announced, not open
# ---------------------------------------------------------------------------

PARRAINAGE = {
    "titre": "Referrals | Up2Front",
    "desc": "Our referral programme is not open yet. Here is what is being "
            "prepared, and how to be told on the day it starts.",
    "fil": "Referrals",
    "sur_titre": "Coming soon",
    "h1": ["The referral scheme is coming.", "It is not open yet."],
    "lede": "We are preparing a referral programme for the people who "
            "already recommend us. Until it is in place, we display no "
            "amount and ask for no bank details.",
    "b1": "Be told when it launches",
    "b2": "Read the current terms",
    "prose": """
<p class="maj">Status on 12 September 2026 — programme in preparation</p>

<p><strong>There is no referral programme open at Up2Front today.</strong>
No commission is promised, no sign-up is open, and no payment can be
claimed on the basis of a recommendation. This page exists to announce
what we are preparing, not to get anything signed.</p>

<p>We could have published a rate card right now: it is one line of text
to write. But a referral scheme that holds up needs machinery behind it —
knowing who recommended whom, checking that an order was actually paid
for, paying a sum to someone who is not a client, and handling that
payment correctly for accounting and tax purposes. It is that machinery we
are putting in place before opening.</p>

<h2>What will be announced on launch day</h2>

<ul>
  <li>Who can take part, and on what conditions.</li>
  <li>What exactly triggers a reward, and at what point.</li>
  <li>The amount, or the percentage, in black and white.</li>
  <li>The payment deadline and the method used.</li>
  <li>The cases where nothing is due — cancellation, refund, an order
  placed by yourself.</li>
</ul>

<p>As long as those five points are not written down, there is no
programme. Our <a href="legal/affiliation.html">referral and affiliate
terms</a> say so in the same words, and they are what counts.</p>

<h2>If you recommend us before then</h2>

<p>It happens, and it is what keeps a young business alive. If someone
orders because of you, write to us at
<a href="mailto:contact@up2front.com">contact@up2front.com</a>: we will
discuss it directly, case by case. It will be a one-off arrangement, not
the application of a programme — and we will say so as such.</p>

<h2>Being told</h2>

<p>A message to <a href="mailto:contact@up2front.com?subject=Referral%20%E2%80%94%20notify%20me%20at%20launch">contact@up2front.com</a>
with the word “referral” is enough. We do not need your bank details to
put you on a waiting list, and we will never ask for them before a sum is
actually due.</p>
""",
    "etapes_t": "What we are putting in place.",
    "etapes_c": "Three pieces of work, in this order. The programme will "
                "open when all three are finished.",
    "etapes": [
        ("Workstream 1", "Tracking recommendations",
         "A named referral link, tied to a paid order. Without that "
         "tracking, there is no way of knowing who is entitled to what."),
        ("Workstream 2", "The written framework",
         "Full referral terms, built into the terms and conditions, which "
         "also say in which cases nothing is due."),
        ("Workstream 3", "The payment",
         "The accounting and tax treatment of a reward paid to someone who "
         "is not a client. This is the longest part."),
    ],
    "appel_h2": "In the meantime, the simplest way to help us",
    "appel_p": "Tell someone who needs it about us, and let us know. We "
               "answer the same day, Monday to Friday.",
    "appel_b1": "Write to contact@up2front.com",
    "appel_b2": "See pricing",
}
