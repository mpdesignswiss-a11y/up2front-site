# -*- coding: utf-8 -*-
"""Pôle « Visibilité IA » d'up2front.com : pages de fond (méthode, questions, glossaire,
études, relevé public d'Up2Front, page agence).

Génère des pages HTML statiques dans public/ (GitHub Pages). Rien n'est mis en ligne :
la publication reste un geste de Max (commit + push).

    python3 _geo_pages.py          # écrit les pages
    python3 _geo_pages.py --liste  # affiche les adresses générées

Stratégie : knowledge/marketing/STRATEGIE-SEO-GEO-UP2FRONT.md (projet Up2Front AI visibility).
Chaque chiffre a sa source datée. Aucune garantie de position, aucun avis inventé.
"""
CUR = ' aria-current="page"'
import html, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(ICI, "public")
SITE = "https://up2front.com/"
ORG = SITE + "#organisation"
MAX = SITE + "#maxime-pilloud"
MAJ = "2026-10-27"
MAJ_TXT = "27 octobre 2026"

ORG_NODE = {
    "@type": ["Organization", "ProfessionalService"], "@id": ORG, "name": "Up2Front",
    "alternateName": "Up2Front Genève", "url": SITE, "email": "contact@up2front.com",
    "logo": SITE + "icone-512.png", "image": SITE + "og-image.png",
    "description": "Agence web genevoise : sites professionnels à forfait pour les PME suisses (dès CHF 290, livrés dès 2 jours) et mesure de la visibilité des entreprises dans les moteurs de réponse IA (Google AI Mode, ChatGPT, Gemini).",
    "foundingDate": "2026",
    "founder": {"@type": "Person", "@id": MAX, "name": "Maxime Pilloud", "jobTitle": "Fondateur"},
    "address": {"@type": "PostalAddress", "addressLocality": "Genève", "postalCode": "1205", "addressCountry": "CH"},
    "areaServed": {"@type": "Country", "name": "Suisse"},
    "knowsLanguage": ["fr", "en", "de", "it"],
    "knowsAbout": ["Création de sites web", "Visibilité dans les moteurs de réponse IA", "Generative Engine Optimization (GEO)", "Google AI Mode", "ChatGPT", "Référencement naturel (SEO)"],
    "currenciesAccepted": "CHF", "priceRange": "CHF 290 – CHF 690",
}

# ---------------------------------------------------------------- liens du pôle
POLE = [
    ("visibilite-ia.html", "Le Relevé offert", "Ce que trois IA répondent sur votre métier, daté à la minute."),
    ("visibilite-ia/methode.html", "La méthode", "Comment mesurer sa visibilité IA sans se tromper."),
    ("visibilite-ia/ce-que-les-ia-disent-d-up2front.html", "Notre propre score", "Ce que les IA disent d'Up2Front, chaque mois."),
    ("etudes/", "Les études", "Ce que les IA répondent, métier par métier."),
    ("visibilite-ia/agence-geo-geneve.html", "Agence GEO à Genève", "Ce que nous faisons, ce que nous ne promettons pas."),
    ("visibilite-ia/glossaire.html", "Glossaire GEO suisse", "Les mots du métier, avec le contexte suisse."),
]
QUESTIONS = [
    ("visibilite-ia/qu-est-ce-que-le-geo.html", "Qu'est-ce que le GEO ?"),
    ("visibilite-ia/geo-ou-seo.html", "GEO ou SEO : quelle différence ?"),
    ("visibilite-ia/prix-geo-suisse.html", "Combien coûte le GEO en Suisse ?"),
    ("visibilite-ia/pourquoi-chatgpt-ne-cite-pas-mon-entreprise.html", "Pourquoi ChatGPT ne cite pas mon entreprise ?"),
    ("visibilite-ia/google-ai-mode-suisse.html", "Google AI Mode en Suisse"),
]

# ---------------------------------------------------------------- versions anglaises
EN_POLE = [
    ("en/ai-visibility/geneva-geo-agency.html", "GEO agency in Geneva", "What we do, and what we never promise."),
    ("en/ai-visibility/how-to-measure-ai-visibility.html", "The method", "How to check whether AI engines recommend you."),
    ("en/ai-visibility/what-is-geo.html", "What is GEO?", "A plain definition, with Swiss figures."),
    ("en/ai-visibility/geo-pricing-switzerland.html", "GEO pricing in Switzerland", "Published prices, dated and sourced."),
]
# correspondances FR <-> EN (hreflang)
ALT = {
    "visibilite-ia/agence-geo-geneve.html": "en/ai-visibility/geneva-geo-agency.html",
    "visibilite-ia/methode.html": "en/ai-visibility/how-to-measure-ai-visibility.html",
    "visibilite-ia/qu-est-ce-que-le-geo.html": "en/ai-visibility/what-is-geo.html",
    "visibilite-ia/prix-geo-suisse.html": "en/ai-visibility/geo-pricing-switzerland.html",
}
ALT.update({v: k for k, v in list(ALT.items())})

# ---------------------------------------------------------------- sources communes
S = {
    "comparis": ("Comparis / Innofact, sondage de mars 2026 (n = 1 035), rapporté par swissinfo.ch le 1er avril 2026", "https://www.swissinfo.ch/fre/trois-quarts-des-suisses-utilisent-des-outils-d%27ia-au-quotidien/91198092"),
    "aio_ch": ("blue News, « Google's Overview with AI now also available in Switzerland », 26 mars 2025", "https://www.bluewin.ch/en/news/googles-overview-with-ai-now-also-available-in-switzerland-li.2623883"),
    "aimode_ch": ("blue News, « AI mode in Google Search is coming to Switzerland and Europe », 8 octobre 2025", "https://www.bluewin.ch/en/news/ai-mode-in-google-search-is-coming-to-switzerland-and-europe-2907273.html"),
    "gsc_ia": ("Google Search Central Blog, « Introducing Search Generative AI performance reports in Search Console », 3 juin 2026", "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"),
    "stgall": ("Schulte et al., Université de Saint-Gall, arXiv 2604.07585, avril 2026 (instabilité des sources citées)", "https://arxiv.org/abs/2604.07585"),
    "kdd": ("Aggarwal et al., « GEO: Generative Engine Optimization », KDD 2024", "https://arxiv.org/abs/2311.09735"),
    "ma": ("Ma et al., arXiv 2509.14436, septembre 2025 (clarté du texte et probabilité de citation)", "https://arxiv.org/abs/2509.14436"),
    "ahrefs": ("Ahrefs, étude sur 75 000 marques, mai 2025 (mentions de marque et visibilité dans les AI Overviews)", "https://ahrefs.com/blog/ai-overview-brand-correlation/"),
    "bochum": ("Kirsten et al., Bochum / MPI-SWS, arXiv 2510.11560, octobre 2025", "https://arxiv.org/abs/2510.11560"),
    "google_aif": ("Google Search Central, « AI features and your website »", "https://developers.google.com/search/docs/appearance/ai-features"),
    "oai": ("OpenAI, « Overview of OpenAI crawlers » (OAI-SearchBot)", "https://platform.openai.com/docs/bots"),
    "brave": ("TechCrunch, « Anthropic appears to be using Brave to power web searches for its Claude chatbot », 21 mars 2025", "https://techcrunch.com/2025/03/21/anthropic-appears-to-be-using-brave-to-power-web-searches-for-its-claude-chatbot/"),
    "etude": ("Up2Front, « Étude de visibilité IA — Architectes à Genève », relevés du 15 septembre 2026", SITE + "etudes/visibilite-ia-architectes-geneve.html"),
    "self": ("Up2Front, « Ce que les IA disent d'Up2Front », relevé du 27 octobre 2026", SITE + "visibilite-ia/ce-que-les-ia-disent-d-up2front.html"),
}



def espaces_fines(doc):
    """Typo française : espace insécable avant : ? ! ; hors <script> (un deux-points ne doit pas commencer une ligne)."""
    import re
    morceaux = re.split(r"(<script[\s\S]*?</script>|<[^>]+>)", doc)
    for i in range(0, len(morceaux), 2):
        morceaux[i] = re.sub(r" ([:?!;])", "\u00a0\\1", morceaux[i])
    return "".join(morceaux)

def e(t):
    return html.escape(t, quote=True)


def rel(depth, href):
    if href.startswith("http") or href.startswith("mailto:") or href.startswith("#"):
        return href
    return ("../" * depth) + href


def nav(depth, actif):
    if actif.startswith("en/"):
        a = "\n".join(f'      <a href="{rel(depth, h)}"{CUR if h == actif else ""}>{e(t)}</a>' for h, t, _ in EN_POLE)
        fr = ALT.get(actif, "visibilite-ia.html")
        return f'''<nav class="nav">
  <div class="in wrap">
    <a class="mark" href="{rel(depth, "en/index.html")}"><b>Up2<i>Front</i></b><span>AI visibility</span></a>
    <div class="links">
{a}
      <a href="{rel(depth, fr)}" hreflang="fr" lang="fr">Français</a>
    </div>
    <a class="btn" href="mailto:contact@up2front.com">contact@up2front.com</a>
  </div>
</nav>'''
    liens = [("visibilite-ia/methode.html", "La méthode"), ("etudes/", "Les études"),
             ("visibilite-ia/ce-que-les-ia-disent-d-up2front.html", "Notre score"),
             ("visibilite-ia/glossaire.html", "Glossaire"), ("verificateur.html", "Le vérificateur")]
    a = "\n".join(
        f'      <a href="{rel(depth, h)}"{CUR if h == actif else ""}>{e(t)}</a>' for h, t in liens)
    return f'''<nav class="nav">
  <div class="in wrap">
    <a class="mark" href="{rel(depth, "index.html")}"><b>Up2<i>Front</i></b><span>Visibilité IA</span></a>
    <div class="links">
{a}
    </div>
    <a class="btn" href="{rel(depth, "visibilite-ia.html#commander")}">Mon Relevé — offert</a>
  </div>
</nav>'''


def footer(depth, en=False):
    if en:
        q = "\n".join(f'          <li><a href="{rel(depth, h)}">{e(t)}</a></li>' for h, t, _ in EN_POLE)
        return f'''<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <a class="mark" href="{rel(depth, "en/index.html")}"><b>Up2<i>Front</i></b><span>AI visibility</span></a>
        <p>Web agency in Geneva: fixed-price websites and measurement of visibility in AI answer engines, for Swiss SMEs.</p>
      </div>
      <div class="fcol">
        <h4>AI visibility</h4>
        <ul>
{q}
        </ul>
      </div>
      <div class="fcol">
        <h4>Up2Front</h4>
        <ul>
          <li><a href="{rel(depth, "en/index.html")}">Websites from CHF&nbsp;290</a></li>
          <li><a href="{rel(depth, "visibilite-ia.html")}" hreflang="fr" lang="fr">Le Relevé (en français)</a></li>
          <li>contact@up2front.com</li>
        </ul>
      </div>
    </div>
    <div class="fbas">
      <span>© Up2Front 2026</span>
      <span>Maxime Pilloud, sole proprietorship · Geneva, Switzerland</span>
    </div>
  </div>
</footer>'''
    q = "\n".join(f'          <li><a href="{rel(depth, h)}">{e(t)}</a></li>' for h, t in QUESTIONS)
    return f'''<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <a class="mark" href="{rel(depth, "index.html")}"><b>Up2<i>Front</i></b><span>Visibilité IA</span></a>
        <p>Agence web à Genève : sites professionnels à forfait et mesure de la visibilité dans les moteurs de réponse IA, pour les PME suisses.</p>
      </div>
      <div class="fcol">
        <h4>Questions fréquentes</h4>
        <ul>
{q}
        </ul>
      </div>
      <div class="fcol">
        <h4>Up2Front</h4>
        <ul>
          <li><a href="{rel(depth, "visibilite-ia.html")}">Le Relevé offert</a></li>
          <li><a href="{rel(depth, "visibilite-ia/agence-geo-geneve.html")}">Agence GEO à Genève</a></li>
          <li><a href="{rel(depth, "index.html")}">Sites web dès CHF&nbsp;290</a></li>
          <li><a href="{rel(depth, "legal/confidentialite.html")}">Confidentialité</a></li>
          <li>contact@up2front.com</li>
        </ul>
      </div>
    </div>
    <div class="fbas">
      <span>© Up2Front 2026</span>
      <span>Maxime Pilloud, entreprise individuelle · Genève, Suisse</span>
    </div>
  </div>
</footer>'''


def sources_html(cles, extra=(), en=False):
    items = [S[k] for k in cles] + list(extra)
    if not items:
        return ""
    li = "\n".join(f'      <li><a href="{e(u)}">{e(t)}</a></li>' for t, u in items)
    return f'''  <section class="sources" aria-labelledby="src">
    <h2 id="src">Sources</h2>
    <ol>
{li}
    </ol>
  </section>'''


def pole_html(depth, sauf):
    en = sauf.startswith("en/")
    cartes = "\n".join(
        f'      <a href="{rel(depth, h)}"><b>{e(t)}</b><span>{e(d)}</span></a>' for h, t, d in (EN_POLE if en else POLE) if h != sauf)
    return f'''  <section class="texte" aria-labelledby="pole">
    <h2 id="pole">{"Read next" if en else "Pour aller plus loin"}</h2>
    <div class="pole">
{cartes}
    </div>
  </section>'''


APPEL = '''  <aside class="appel">
    <h2>Savoir ce que les IA répondent sur votre métier</h2>
    <p>Le Relevé est offert : la question qu'un client poserait, trois moteurs (Google AI Mode, ChatGPT, Gemini), deux passages à quelques heures d'écart, chaque réponse datée à la minute, sur une page à votre nom. Sous 2 jours ouvrés.</p>
    <div class="cta"><a class="btn" href="{relevé}">Demander mon Relevé</a><a class="btn btn-o" href="{verif}">Tester en 1 minute</a></div>
  </aside>'''

APPEL_EN = '''  <aside class="appel">
    <h2>Find out what AI engines say about your business</h2>
    <p>We ask Google AI Mode, ChatGPT and Gemini the question your clients would ask, twice, a few hours apart, and keep every answer word for word with its time to the minute. Our standard Relevé is delivered in French; for an English-language measurement, write to us.</p>
    <div class="cta"><a class="btn" href="mailto:contact@up2front.com">contact@up2front.com</a><a class="btn btn-o" href="{relevé}" hreflang="fr">Le Relevé (français)</a></div>
  </aside>'''


def page(p):
    path = p["path"]
    en = path.startswith("en/")
    depth = path.count("/")
    url = SITE + (path[:-len("index.html")] if path.endswith("index.html") else path)
    ariane = ([("Up2Front", "en/index.html")] if en else [("Up2Front", "index.html"), ("Visibilité IA", "visibilite-ia.html")]) + p.get("ariane", [])
    ar_html = " › ".join(f'<a href="{rel(depth, h)}">{e(t)}</a>' for t, h in ariane) + f' › <span>{e(p["court"])}</span>'
    bc = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, "item": SITE + h} for i, (t, h) in enumerate(ariane)]}
    bc["itemListElement"].append({"@type": "ListItem", "position": len(ariane) + 1, "name": p["court"], "item": url})
    main = {"@type": p.get("type", "Article"), "@id": url + "#page", "headline": p["titre"], "name": p["titre"],
            "description": p["desc"], "url": url, "inLanguage": "en" if en else "fr-CH", "datePublished": p.get("publie", MAJ),
            "dateModified": p.get("maj", MAJ), "author": {"@type": "Person", "@id": MAX, "name": "Maxime Pilloud"},
            "publisher": {"@id": ORG}, "mainEntityOfPage": url}
    if p.get("type") == "DefinedTermSet":
        main = {"@type": "DefinedTermSet", "@id": url + "#glossaire", "name": p["titre"], "description": p["desc"],
                "url": url, "inLanguage": "fr-CH", "publisher": {"@id": ORG},
                "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d, "inDefinedTermSet": url + "#glossaire"}
                                   for t, d, _ in p["termes"]]}
    if p.get("type") == "CollectionPage":
        main = {"@type": "CollectionPage", "@id": url + "#page", "name": p["titre"], "description": p["desc"], "url": url,
                "inLanguage": "fr-CH", "publisher": {"@id": ORG}, "dateModified": MAJ}
    graph = [main, bc, ORG_NODE]
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    for x in p.get("graph_extra", []):
        graph.append(x)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    faq_html = ""
    if p.get("faq"):
        faq_html = '  <section class="texte" aria-labelledby="faq">\n    <h2 id="faq">' + ("Frequently asked questions" if en else "Questions fréquentes") + '</h2>\n' + "\n".join(
            f"    <h3>{e(q)}</h3>\n    <p>{e(a)}</p>" for q, a in p["faq"]) + "\n  </section>"
    reponse = ""
    if p.get("reponse"):
        reponse = f'''  <div class="reponse" role="note">
    <div class="k">{"In short" if en else "En bref"}</div>
    <p>{p["reponse"]}</p>
  </div>'''
    appel = "" if p.get("sans_appel") else (APPEL_EN if en else APPEL).replace("{relevé}", rel(depth, "visibilite-ia.html#commander")).replace("{verif}", rel(depth, "verificateur.html"))
    body = p["corps"].replace("{R}", "../" * depth)
    og_slug = path.replace("/index.html", "").replace(".html", "").replace("/", "-")
    alternates = ""
    if path in ALT:
        fr_p, en_p = (ALT[path], path) if en else (path, ALT[path])
        alternates = (f'\n<link rel="alternate" hreflang="fr" href="{SITE + fr_p}">'
                      f'\n<link rel="alternate" hreflang="en" href="{SITE + en_p}">'
                      f'\n<link rel="alternate" hreflang="x-default" href="{SITE + fr_p}">')
    maj = p.get("maj", MAJ)
    mois = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    maj_txt = f"{int(maj[8:])} {mois[int(maj[5:7])-1]} {maj[:4]}"
    date_html = (f'<span>By <b>Maxime Pilloud</b>, Up2Front</span><span>Updated <b><time datetime="{MAJ}">27 October 2026</time></b></span>' if en
                 else f'<span>Par <b>Maxime Pilloud</b>, Up2Front</span><span>Mis à jour le <b><time datetime="{maj}">{maj_txt}</time></b></span>')
    return f'''<!DOCTYPE html>
<html lang="{"en" if en else "fr-CH"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["desc"])}">
<link rel="canonical" href="{url}">{alternates}
<meta property="og:type" content="article">
<meta property="og:site_name" content="Up2Front">
<meta property="og:locale" content="{"en_GB" if en else "fr_CH"}">
<meta property="og:title" content="{e(p["title"])}">
<meta property="og:description" content="{e(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/og/{og_slug}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="article:modified_time" content="{p.get('maj', MAJ)}">
<link rel="icon" href="{rel(depth, "favicon.svg")}" type="image/svg+xml">
<link rel="icon" href="{rel(depth, "favicon-32x32.png")}" sizes="32x32">
<link rel="apple-touch-icon" href="{rel(depth, "apple-touch-icon.png")}">
<link rel="stylesheet" href="{rel(depth, "assets/polices/polices.css")}">
<link rel="stylesheet" href="{rel(depth, "assets/geo.css")}">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#contenu">{"Skip to content" if en else "Aller au contenu"}</a>
{nav(depth, path)}
<main id="contenu" class="wrap">
 <div class="col">
  <p class="ariane">{ar_html}</p>
  <header class="tete">
    <span class="eyebrow">{e(p["eyebrow"])}</span>
    <h1>{p["h1"]}</h1>
    <p class="chapo">{p["chapo"]}</p>
    <p class="date">{date_html}</p>
  </header>
{reponse}
  <div class="texte">
{body}
  </div>
{faq_html}
{appel}
{pole_html(depth, path)}
{sources_html(p.get("sources", []), p.get("sources_extra", []))}
 </div>
</main>
{footer(depth, en)}
</body>
</html>
'''


from _geo_contenu import PAGES  # noqa: E402  (le contenu vit à part, plus lisible)

if __name__ == "__main__":
    for p in PAGES:
        out = os.path.join(PUBLIC, p["path"])
        if "--liste" in sys.argv:
            print(SITE + p["path"]); continue
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(page(p) if p["path"].startswith("en/") else espaces_fines(page(p)))
        print("écrit", p["path"])
