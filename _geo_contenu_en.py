# -*- coding: utf-8 -*-
"""English versions of the core « Visibilité IA » pages (read by _geo_pages.py). Updated 27 October 2026.
Same rules as the French pages: sourced and dated figures, no guarantee, no invented reviews.
The Relevé itself is delivered in French: the English pages say so and offer e-mail contact instead."""

AR_EN = [("AI visibility", "en/ai-visibility/geneva-geo-agency.html")]

SRC = {
    "stgall": ("Schulte et al., University of St. Gallen, arXiv 2604.07585, April 2026 (instability of cited sources)", "https://arxiv.org/abs/2604.07585"),
    "kdd": ("Aggarwal et al., “GEO: Generative Engine Optimization”, KDD 2024", "https://arxiv.org/abs/2311.09735"),
    "comparis": ("Comparis / Innofact survey, March 2026 (n = 1,035), reported by swissinfo.ch on 1 April 2026", "https://www.swissinfo.ch/fre/trois-quarts-des-suisses-utilisent-des-outils-d%27ia-au-quotidien/91198092"),
    "aio_ch": ("blue News, “Google's Overview with AI now also available in Switzerland”, 26 March 2025", "https://www.bluewin.ch/en/news/googles-overview-with-ai-now-also-available-in-switzerland-li.2623883"),
    "aimode_ch": ("blue News, “AI mode in Google Search is coming to Switzerland and Europe”, 8 October 2025", "https://www.bluewin.ch/en/news/ai-mode-in-google-search-is-coming-to-switzerland-and-europe-2907273.html"),
    "ahrefs": ("Ahrefs, study of 75,000 brands, May 2025 (brand mentions and AI Overview visibility)", "https://ahrefs.com/blog/ai-overview-brand-correlation/"),
    "ma": ("Ma et al., arXiv 2509.14436, September 2025 (text clarity and citation probability)", "https://arxiv.org/abs/2509.14436"),
    "google_aif": ("Google Search Central, “AI features and your website”", "https://developers.google.com/search/docs/appearance/ai-features"),
    "etude": ("Up2Front, “Étude de visibilité IA — Architectes à Genève” (in French), 15 September 2026", "https://up2front.com/etudes/visibilite-ia-architectes-geneve.html"),
    "pac": ("Up2Front, “Pompes à chaleur à Genève : ce que répondent les IA” (in French), 27 October 2026", "https://up2front.com/etudes/pompes-a-chaleur-geneve-ia-octobre-2026.html"),
    "self": ("Up2Front, “Ce que les IA disent d'Up2Front” (in French), 27 October 2026", "https://up2front.com/visibilite-ia/ce-que-les-ia-disent-d-up2front.html"),
}


def src(*keys):
    return [SRC[k] for k in keys]


PAGES_EN = []

# =====================================================================================
PAGES_EN.append(dict(
    path="en/ai-visibility/geneva-geo-agency.html", court="GEO agency in Geneva",
    title="GEO agency in Geneva — measured AI visibility, no promises | Up2Front",
    titre="GEO agency in Geneva: what Up2Front does, and what it never promises",
    desc="Up2Front, a web agency in Geneva, measures and improves how SMEs appear in Google AI Mode, ChatGPT and Gemini. Every answer kept word for word and timed to the minute. No ranking guaranteed.",
    eyebrow="GEO agency · Geneva and French-speaking Switzerland",
    h1="GEO agency in Geneva: <em>measure first</em>, never promise",
    chapo="GEO means getting a business understood and cited by AI answer engines. About twenty agencies offer it in French-speaking Switzerland. Here is what Up2Front does, how we work, and what we refuse to sell.",
    reponse="<strong>Up2Front</strong> is a Geneva web agency founded by Maxime Pilloud. It measures what <strong>Google AI Mode, ChatGPT and Gemini</strong> answer when a client looks for your trade in your town, then fixes what stops you from being cited. Every answer is kept <strong>word for word</strong>, timed <strong>to the minute</strong>, on a page in your name. No agency can guarantee a place in an AI answer, and neither can we.",
    corps='''    <h2>What we do</h2>
    <ol>
      <li><strong>The measurement.</strong> We ask three engines the question one of your clients would ask (“who is the best [your trade] in [your town]?”), twice, a few hours apart. You get every answer word for word, the time to the minute, and the sources the engines cited. Our standard Relevé is free and delivered in French; for an English-language measurement, write to us.</li>
      <li><strong>The work (quoted, only if you ask).</strong> We fix what blocks you: pages engines cannot read, an unclear identity, absence from the directories and sources AI engines actually use.</li>
      <li><strong>A new measurement after 90 days.</strong> Same question, same engines, so you can see what moved and what did not.</li>
    </ol>

    <h2>What we never promise</h2>
    <ul>
      <li><strong>No guaranteed position.</strong> AI answers change from one day to the next: about 65% of cited sources change from one day to the next, according to the University of St. Gallen (April 2026).</li>
      <li><strong>No invented reviews, no fake articles.</strong> Engines cross-check, and what is false ends up showing.</li>
      <li><strong>No useless work.</strong> If your clients mostly come through an insurer, a property manager or a colleague, AI matters little to you. We will say so and sell you nothing.</li>
    </ul>

    <h2>We measure ourselves, in public</h2>
    <p>On 27 October 2026 we asked the three engines four client questions about our own trade. <strong>Up2Front was named in none of the 12 answers.</strong> We publish that score and its progress every month (<a href="{R}visibilite-ia/ce-que-les-ia-disent-d-up2front.html" hreflang="fr">in French</a>). Selling measurement without showing your own would not be serious.</p>

    <h2>Our published studies</h2>
    <ul>
      <li><a href="{R}etudes/pompes-a-chaleur-geneve-ia-octobre-2026.html" hreflang="fr">Heat pumps in Geneva</a> (in French): 180 AI answers. The most cited source is the State of Geneva's heat pump page, not any installer's website.</li>
      <li><a href="{R}etudes/visibilite-ia-architectes-geneve.html" hreflang="fr">Architects in Geneva</a> (in French): Google AI Mode answered the same question three different ways within one hour.</li>
    </ul>

    <h2>Five questions to ask any GEO agency</h2>
    <ol>
      <li>How many times do you ask each question? One answer proves nothing.</li>
      <li>Will you show me the engines' full answers, or only a score?</li>
      <li>Which engines do you measure, and on what exact date?</li>
      <li>Which sources do the engines cite instead of my website?</li>
      <li>What happens if nothing moves after 90 days?</li>
    </ol>''',
    faq=[
        ("Does Up2Front work in English?", "Yes. Our standard Relevé is delivered in French, but we can measure English-language questions on request: write to contact@up2front.com."),
        ("Can Up2Front guarantee a place in ChatGPT?", "No. AI answers change from day to day and no agency can guarantee a citation. Up2Front measures, fixes what blocks you, then measures again after 90 days."),
        ("Which engines does Up2Front measure?", "Google AI Mode, ChatGPT and Gemini, twice per question, with every answer timed to the minute."),
    ],
    sources_extra=src("stgall", "self", "pac", "etude"),
))

# =====================================================================================
PAGES_EN.append(dict(
    path="en/ai-visibility/how-to-measure-ai-visibility.html", court="The method", ariane=AR_EN,
    title="How to measure your visibility in ChatGPT and Google AI Mode — the method | Up2Front",
    titre="How to measure your visibility in AI answers: the Up2Front method",
    desc="How to find out whether ChatGPT, Google AI Mode and Gemini recommend your business: the right question, a fresh session, two runs, the time to the minute. Free and repeatable.",
    eyebrow="Method · repeatable",
    h1="How to know whether <em>AI engines recommend</em> your business",
    chapo="Typing your company name into ChatGPT measures nothing: the AI confirms what you suggest. Here is the method we apply to every measurement. You can follow it yourself, for free.",
    reponse="Ask <strong>the question a client would ask</strong>, without ever naming yourself, in a <strong>fresh session</strong>, to <strong>several engines</strong> (Google AI Mode, ChatGPT, Gemini). Do it again <strong>a few hours later</strong>, note the time to the minute and keep every answer <strong>word for word</strong>. One answer proves nothing: the same question gives different rankings within the same hour.",
    corps='''    <h2>Seven rules for a reliable measurement</h2>
    <ol>
      <li><strong>A client's question, not your name.</strong> “Who is the best heat pump installer in Carouge?”, never “What do you think of Dupont Heating?”.</li>
      <li><strong>A fresh session.</strong> Private browsing, no signed-in account, no history: otherwise the engine answers from what it already knows about you.</li>
      <li><strong>Several engines.</strong> Google AI Mode, ChatGPT and Gemini do not read the same sources. Being cited by one says nothing about the others.</li>
      <li><strong>At least two runs, a few hours apart.</strong> According to the University of St. Gallen (April 2026), about 65% of cited sources change from one day to the next, even for an identical question.</li>
      <li><strong>The time to the minute.</strong> An undated answer is not a measurement.</li>
      <li><strong>The full answer, word for word.</strong> Not a summary: the exact sentence where you are cited, or not.</li>
      <li><strong>Three things to note.</strong> Are you named? Is your website cited as a source? Who is named instead of you?</li>
    </ol>

    <h2>Proof that two runs are essential</h2>
    <p>In our <a href="{R}etudes/pompes-a-chaleur-geneve-ia-octobre-2026.html" hreflang="fr">heat pump study</a> (27 October 2026), for <strong>16 of 90</strong> installer-and-engine pairs, the same engine named the installer in one run and left it out in the other, a few hours apart. In our architects study (15 September 2026), Google AI Mode answered the same question <strong>three different ways within one hour</strong>.</p>

    <h2>Limits, in black and white</h2>
    <ul>
      <li>Two runs show a trend, not a statistical frequency. The St. Gallen researchers recommend several runs a day over several weeks for a scientific measurement.</li>
      <li>Engines change models without notice. A measurement is valid for its date.</li>
      <li>A measurement says <strong>what the AI answers</strong>. It does not say how many clients ask the question.</li>
    </ul>''',
    faq=[
        ("Can I measure my own visibility in ChatGPT?", "Yes. Ask the question a client would ask, without naming your business, in a fresh session, to several engines, twice a few hours apart, and keep every answer word for word with its time."),
        ("Why is one answer not enough?", "Because answers change: about 65% of cited sources change from one day to the next according to the University of St. Gallen (2026), and in Up2Front's heat pump study one installer in five appeared in one run and not in the other."),
        ("Should I test with my company name?", "No. With your name, the AI confirms what you suggest. Ask the question of a client who does not know you yet."),
    ],
    sources_extra=src("stgall", "pac", "etude"),
))

# =====================================================================================
PAGES_EN.append(dict(
    path="en/ai-visibility/what-is-geo.html", court="What is GEO?", ariane=AR_EN,
    title="What is GEO (Generative Engine Optimization)? A plain definition | Up2Front",
    titre="What is GEO (Generative Engine Optimization)?",
    desc="GEO is everything that helps a business be understood and cited by AI answer engines: Google AI Mode, ChatGPT, Gemini. Definition, Swiss figures, what works and what is overrated.",
    eyebrow="FAQ · definition",
    h1="What is <em>GEO</em>?",
    chapo="GEO stands for Generative Engine Optimization. The term comes from a research paper published in 2023 by Princeton researchers and presented at the KDD conference in 2024.",
    reponse="<strong>GEO</strong> covers everything that helps a business be <strong>understood and cited</strong> by engines that answer instead of listing links: <strong>Google AI Mode and Google's AI Overviews, ChatGPT, Gemini, Perplexity, Claude</strong>. Where SEO aims for a place in a list, GEO aims for a mention in the answer itself.",
    corps='''    <h2>Why it matters in Switzerland</h2>
    <p>In March 2026, <strong>76% of Swiss residents</strong> used AI tools daily, and <strong>81.6% in French-speaking Switzerland</strong>. <strong>41.6%</strong> used them instead of a classic search engine (Comparis / Innofact survey, 1,035 people). Google has shown AI Overviews in Switzerland since 26 March 2025, in all four national languages, and its AI Mode since October 2025.</p>

    <h2>What actually gets a business cited</h2>
    <ul>
      <li><strong>Being mentioned elsewhere.</strong> Across 75,000 brands, mentions on other websites weigh about three times more than links (Ahrefs, May 2025).</li>
      <li><strong>Clear pages that answer straight away.</strong> Simple, predictable text raises the probability of being cited by 47% to 56% (Ma et al., 2025). Citing sources and figures helps too (Aggarwal et al., KDD 2024).</li>
      <li><strong>Letting the engines' crawlers in</strong> (OAI-SearchBot for ChatGPT, Googlebot for Google). A site that blocks them cannot be cited.</li>
      <li><strong>Being present in the local sources engines read.</strong> In our Geneva heat pump study, the State of Geneva's website, local.ch and search.ch were cited more often than installers' own websites.</li>
    </ul>

    <h2>What is overrated</h2>
    <ul>
      <li><strong>The llms.txt file</strong>: no demonstrated effect so far, according to Google itself.</li>
      <li><strong>Structured data as a magic lever</strong>: useful for machines to understand who you are, but Google states that no special markup is needed for its AI features.</li>
      <li><strong>Promises of “first place in ChatGPT”</strong>: impossible, since answers change from day to day.</li>
    </ul>

    <h2>Other names for GEO</h2>
    <p>You will also see <strong>AEO</strong> (Answer Engine Optimization), <strong>LLMO</strong>, <strong>AI SEO</strong> or <strong>AI visibility</strong>. They all mean the same thing.</p>''',
    faq=[
        ("What does GEO stand for?", "Generative Engine Optimization: everything that helps a business be understood and cited by Google AI Mode, ChatGPT, Gemini, Perplexity or Claude."),
        ("Does GEO replace SEO?", "No. GEO builds on the same foundations (a readable website, a good reputation), but it aims for a mention in the AI's answer rather than a place in a list of links."),
        ("Is GEO useful for a Swiss SME?", "Yes if its clients look for providers online: in March 2026, 41.6% of Swiss residents used AI instead of a classic search engine (Comparis / Innofact)."),
    ],
    sources_extra=src("kdd", "comparis", "aio_ch", "aimode_ch", "ahrefs", "ma", "google_aif", "pac"),
))

# =====================================================================================
PAGES_EN.append(dict(
    path="en/ai-visibility/geo-pricing-switzerland.html", court="GEO pricing in Switzerland", ariane=AR_EN,
    title="How much does GEO cost in Switzerland? Published prices, 2026 | Up2Front",
    titre="How much does GEO cost in Switzerland? Published prices, with sources",
    desc="GEO and AI visibility prices in Switzerland in 2026: tracking tools from CHF 24 a month, audits from CHF 390 to CHF 4,000, monthly support from CHF 550 to over CHF 1,200. Public prices, dated and sourced.",
    eyebrow="FAQ · pricing",
    h1="How much does <em>GEO</em> cost in Switzerland?",
    chapo="Prices range from zero to several thousand francs depending on what you buy: an automated tool, an audit or ongoing support. Here are the prices Swiss providers publish themselves, with the date we read them.",
    reponse="In Switzerland, in October 2026, an <strong>automated tracking tool</strong> costs <strong>CHF 0 to CHF 165 a month</strong>, an <strong>audit</strong> <strong>CHF 390 to CHF 4,000</strong>, and <strong>monthly support</strong> <strong>CHF 550 to over CHF 1,200 a month</strong>. Many agencies publish no price at all. No serious price includes a guaranteed citation.",
    corps='''    <h2>Prices published by providers</h2>
    <div class="tab"><table>
      <thead><tr><th>Provider</th><th>What is sold</th><th>Published price</th><th>Read on</th></tr></thead>
      <tbody>
        <tr><td>CheckAI.ch</td><td>Tool: free test (6 questions, ChatGPT and AI Mode); one-off report; weekly tracking; daily tracking</td><td class="num">0 · CHF 8 · CHF 24/month · CHF 165/month</td><td class="num">27.10.2026</td></tr>
        <tr><td>visiblement.ch</td><td>48-hour audit (ChatGPT, Perplexity, Google); tracking included in a maintenance plan</td><td class="num">CHF 390 · CHF 199/month</td><td class="num">03.10.2026</td></tr>
        <tr><td>FirstPoint (Lausanne)</td><td>Tracking of 30 to 50 questions; + content; + publishing</td><td class="num">from CHF 550 · 1,250 · 1,750/month</td><td class="num">27.10.2026</td></tr>
        <tr><td>Soleil Digital (Geneva)</td><td>Light audit; full audit; ongoing tracking</td><td class="num">CHF 1,200 · 2,900 to 4,000 · 1,200/month (excl. VAT)</td><td class="num">03.10.2026</td></tr>
        <tr><td>DEEPSEO (Carouge)</td><td>SEO and GEO support; free 48-hour audit</td><td class="num">from CHF 1,200/month</td><td class="num">27.10.2026</td></tr>
        <tr><td>Up2Front (Geneva)</td><td>The Relevé: 3 engines, 2 runs, answers word for word on a page in your name (in French); work quoted separately</td><td class="num">Relevé free</td><td class="num">27.10.2026</td></tr>
      </tbody>
    </table></div>
    <p class="note">Prices read on providers' public pages, excluding VAT where stated. They may have changed since: check with each provider. This list is neither a ranking nor a recommendation.</p>

    <h2>What the price should buy you</h2>
    <ul>
      <li><strong>Several runs per question</strong>, at different times. One answer proves nothing.</li>
      <li><strong>The full answers</strong>, not just a score.</li>
      <li><strong>Dates</strong>: an undated measurement is not a measurement.</li>
      <li><strong>A new measurement</strong> after the work, with the same questions.</li>
    </ul>

    <h2>What should cost nothing</h2>
    <p>Checking that your site lets the engines' crawlers in, opening a Google Business Profile, listing your business on local.ch and search.ch, asking the AI engines the right questions yourself: all free. The <a href="{R}en/ai-visibility/how-to-measure-ai-visibility.html">method</a> is explained step by step.</p>''',
    faq=[
        ("How much does an AI visibility audit cost in Switzerland?", "In October 2026, published audits range from CHF 390 (visiblement.ch) to CHF 2,900–4,000 (Soleil Digital's full audit). Several providers offer a free first test, and Up2Front's Relevé is free."),
        ("How much does monthly AI visibility tracking cost?", "From CHF 24 a month for a weekly automated tool (CheckAI.ch) to CHF 1,200 a month and more for agency tracking (Soleil Digital, DEEPSEO), according to prices published in October 2026."),
        ("Can a provider guarantee a place in ChatGPT?", "No. AI answers change from day to day; a guaranteed citation is not a serious promise."),
    ],
    sources_extra=[
        ("CheckAI.ch, pricing page, read 27.10.2026", "https://checkai.ch/en/?cur=chf"),
        ("visiblement.ch, audit and tracking offer, read 03.10.2026", "https://visiblement.ch/"),
        ("FirstPoint, “Agence GEO en Suisse romande”, read 27.10.2026", "https://www.firstpoint.ch/marketing-digital/agence-geo-optimisation-ia"),
        ("Soleil Digital, “Audit ChatGPT”, read 03.10.2026", "https://www.soleil-digital.ch/audit-chatgpt/"),
        ("DEEPSEO, “Référencement IA”, read 27.10.2026", "https://deepseo.ch/services/referencement-ia/"),
    ],
))
