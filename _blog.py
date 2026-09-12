#!/usr/bin/env python3
"""
Générateur du blog et de la page parrainage.

Le contenu vit dans _blog_<lg>.py (données pures). Ce script ne fait que
l'habillage : il reprend l'ossature exacte d'une page intérieure déjà en
ligne (carrieres.html de la langue concernée), en garde l'en-tête, le
pied, le widget WhatsApp et les scripts tels quels, et ne réécrit que ce
qui est propre à la page — titre, description, canonique, hreflang,
sélecteur de langue, fil d'Ariane, données structurées, contenu.

Les liens de l'ossature sont recalculés par rapport au dossier de
destination : un article vit dans blog/, donc un cran plus bas que la
page source.

Usage :  python3 _blog.py            (toutes les langues disponibles)
         python3 _blog.py fr en      (seulement celles-là)
"""

import importlib
import json
import os
import re
import sys

SITE = "https://up2front.com/"
RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

# code de langue -> dossier dans public/
LANGUES = [("fr", ""), ("en", "en"), ("de", "de"), ("it", "it")]
DOSSIER = dict(LANGUES)


# ---------------------------------------------------------------------------
# Outils
# ---------------------------------------------------------------------------

def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read()


def ecrire(chemin, contenu):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)


def url(lg, rel):
    """URL absolue d'une page, rel étant relatif à la racine de la langue."""
    d = DOSSIER[lg]
    return SITE + (d + "/" if d else "") + rel


def chemin_fichier(lg, rel):
    d = DOSSIER[lg]
    return os.path.join(RACINE, d, rel) if d else os.path.join(RACINE, rel)


def vers(depuis_rel, lg, cible_rel):
    """Lien relatif de la page depuis_rel vers cible_rel, même langue."""
    a = os.path.dirname(chemin_fichier(lg, depuis_rel))
    b = chemin_fichier(lg, cible_rel)
    return os.path.relpath(b, a)


def vers_autre(depuis_rel, lg, autre_lg, cible_rel):
    a = os.path.dirname(chemin_fichier(lg, depuis_rel))
    b = chemin_fichier(autre_lg, cible_rel)
    return os.path.relpath(b, a)


def prefixe_racine(lg, rel):
    """Chemin relatif de la page vers la racine de public/ (avec / final)."""
    a = os.path.dirname(chemin_fichier(lg, rel))
    p = os.path.relpath(RACINE, a)
    return "" if p == "." else p + "/"


EXTERNE = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//|#|/)", re.I)


def recaler_liens(html, dossier_source, dossier_cible):
    """Recalcule les href/src relatifs d'un bloc d'ossature."""
    if os.path.normpath(dossier_source) == os.path.normpath(dossier_cible):
        return html

    def remplacer(m):
        attr, val = m.group(1), m.group(2)
        if EXTERNE.match(val):
            return m.group(0)
        chemin, sep, ancre = val.partition("#")
        if not chemin:
            return m.group(0)
        cible = os.path.normpath(os.path.join(dossier_source, chemin))
        neuf = os.path.relpath(cible, dossier_cible)
        return '%s="%s"' % (attr, neuf + sep + ancre)

    return re.sub(r'\b(href|src)="([^"]*)"', remplacer, html)


def ld(objet):
    return ('<script type="application/ld+json">\n'
            + json.dumps(objet, ensure_ascii=False, indent=1)
            + "\n</script>")


# ---------------------------------------------------------------------------
# Ossature reprise de carrieres.html
# ---------------------------------------------------------------------------

class Ossature:
    def __init__(self, lg):
        self.lg = lg
        src = chemin_fichier(lg, "carrieres.html")
        self.dossier_source = os.path.dirname(src)
        s = lire(src)

        self.html_lang = re.search(r'<html lang="([^"]+)"', s).group(1)
        self.og_locale = re.search(r'og:locale" content="([^"]+)"', s).group(1)

        m = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*'
                      r'</script>\s*</head>', s, re.S)
        self.graph = m.group(1)

        d = s.index("<body>")
        f = s.index('<main id="contenu">') + len('<main id="contenu">')
        self.haut = s[d:f]
        self.bas = s[s.index("</main>"):]

        # le sélecteur de langue est reconstruit page par page
        self.haut = re.sub(r'<div class="lg" data-langues>.*?</div>',
                           "@@LANGUES@@", self.haut, count=1, flags=re.S)
        assert "@@LANGUES@@" in self.haut, "sélecteur de langue introuvable"

    def selecteur(self, rel):
        libelle = {"fr": "FR", "en": "EN", "de": "DE", "it": "IT"}
        hl = {"fr": "fr-CH", "en": "en", "de": "de-CH", "it": "it-CH"}
        bouts = []
        for code, _ in LANGUES:
            if code == self.lg:
                bouts.append('<span class="lg-a" aria-current="true">%s</span>'
                             % libelle[code])
            else:
                bouts.append('<a class="o" href="%s" hreflang="%s" lang="%s">'
                             '%s</a>' % (vers_autre(rel, self.lg, code, rel),
                                         hl[code], hl[code], libelle[code]))
        return '<div class="lg" data-langues>' + "".join(bouts) + "</div>"

    def enveloppe(self, rel, titre, desc, ld_sup, corps, og="website"):
        cible = os.path.dirname(chemin_fichier(self.lg, rel))
        pfx = prefixe_racine(self.lg, rel)
        can = url(self.lg, rel)

        alt = "\n".join(
            '<link rel="alternate" hreflang="%s" href="%s">' % (h, url(c, rel))
            for c, h in (("fr", "fr-CH"), ("en", "en"),
                         ("de", "de-CH"), ("it", "it-CH")))

        # le sélecteur est déjà calculé depuis le dossier de destination :
        # il est posé après le recalage, sinon il serait décalé deux fois.
        haut = recaler_liens(self.haut, self.dossier_source, cible)
        haut = haut.replace("@@LANGUES@@", self.selecteur(rel))
        bas = recaler_liens(self.bas, self.dossier_source, cible)

        tete = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{can}">
{alt}
<link rel="alternate" hreflang="x-default" href="{xdef}">

<meta property="og:type" content="{og}">
<meta property="og:site_name" content="Up2Front">
<meta property="og:locale" content="{locale}">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{can}">
<meta property="og:image" content="https://up2front.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#000000">
<link rel="icon" href="{pfx}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{pfx}favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="{pfx}apple-touch-icon.png">
<link rel="manifest" href="{pfx}site.webmanifest">
<link rel="preload" href="{pfx}assets/polices/mona-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pfx}assets/polices/polices.css">
<link rel="stylesheet" href="{pfx}assets/u2f.css">
<link rel="stylesheet" href="{pfx}assets/u2f-pages.css">
<script type="application/ld+json">
{graph}
</script>
{ld_sup}</head>
""".format(lang=self.html_lang, titre=titre, desc=desc, can=can, alt=alt, og=og,
           xdef=url("fr", rel), locale=self.og_locale, pfx=pfx,
           graph=self.graph,
           ld_sup=(ld_sup + "\n") if ld_sup else "")

        return tete + haut + "\n" + corps + "\n" + bas


# ---------------------------------------------------------------------------
# Morceaux de page
# ---------------------------------------------------------------------------

def fil(rel, lg, elements):
    """elements : liste de (nom, cible_rel or None)."""
    bouts = []
    items = []
    for i, (nom, cible) in enumerate(elements, 1):
        if cible is not None:
            bouts.append('<a href="%s">%s</a>' % (vers(rel, lg, cible), nom))
            items.append({"@type": "ListItem", "position": i, "name": nom,
                          "item": url(lg, cible).replace("index.html", "")})
        else:
            bouts.append("<span>%s</span>" % nom)
            it = {"@type": "ListItem", "position": i, "name": nom}
            if i == len(elements):
                it["item"] = url(lg, rel)
            items.append(it)
    sep = '<span class="sep" aria-hidden="true">›</span>'
    nav = ('<nav class="fil wrap" aria-label="Fil d\'Ariane">\n  '
           + sep.join(bouts) + "\n</nav>\n")
    return nav + ld({"@context": "https://schema.org",
                     "@type": "BreadcrumbList",
                     "itemListElement": items})


def hero(sur_titre, lignes_h1, lede, boutons):
    lignes = "\n".join('    <span class="ln"><i>%s</i></span>' % l
                       for l in lignes_h1)
    cta = "".join('<a class="btn %s" href="%s">%s</a>' % (c, h, t)
                  for c, h, t in boutons)
    return """<section class="hero hero-page wrap">
  <p class="sur-titre rv">{sur}</p>
  <h1>
{lignes}
  </h1>
  <div class="hgrid">
    <div><p class="lede rv">{lede}</p></div>
    <div><div class="cta rv">{cta}</div></div>
  </div>
</section>""".format(sur=sur_titre, lignes=lignes, lede=lede, cta=cta)


def appel(h2, p, boutons):
    cta = "".join('<a class="btn %s" href="%s">%s</a>' % (c, h, t)
                  for c, h, t in boutons)
    return """<section class="appel wrap">
  <h2>{h2}</h2>
  <p>{p}</p>
  <div class="cta rv">{cta}</div>
</section>""".format(h2=h2, p=p, cta=cta)


def carte_article(href, eti, titre, desc, lire_txt):
    return ('<a class="carte rv" href="%s"><div class="eti">%s</div>'
            '<h3>%s</h3><p>%s</p><span class="fleche">%s →</span></a>'
            % (href, eti, titre, desc, lire_txt))


def bloc_faq(titre, chapo, paires):
    qa = "\n".join(
        '    <details class="qa"><summary>%s</summary>'
        '<div class="rep"><p>%s</p></div></details>' % (q, r)
        for q, r in paires)
    return """<section class="sec wrap">
  <h2 class="sec-t">{t}</h2>
  <p class="sec-c">{c}</p>
  <div class="faq">
{qa}
  </div>
</section>""".format(t=titre, c=chapo, qa=qa)


# ---------------------------------------------------------------------------
# Les pages
# ---------------------------------------------------------------------------

def page_index(oss, D):
    lg, rel = oss.lg, "blog.html"
    I, U = D.INDEX, D.UI

    cartes = "\n    ".join(
        carte_article(vers(rel, lg, "blog/" + a["slug"]),
                      "%s · %s" % (a["cat"], a["lecture"]),
                      a["titre"], a["desc"], U["lire"])
        for a in D.ARTICLES)

    corps = "\n".join([
        fil(rel, lg, [(U["accueil"], "index.html"), (U["fil_blog"], None)]),
        hero(I["sur_titre"], I["h1"], I["lede"],
             [("btn-p", vers(rel, lg, "index.html") + "#tarifs",
               U["voir_tarifs"]),
              ("btn-s", vers(rel, lg, "devis.html"), U["demander_devis"])]),
        """<section class="sec wrap">
  <h2 class="sec-t">{t}</h2>
  <p class="sec-c">{c}</p>
  <div class="grille g-2">
    {cartes}
  </div>
</section>""".format(t=I["sec_t"], c=I["sec_c"], cartes=cartes),
        appel(I["appel_h2"], I["appel_p"],
              [("btn-p", "mailto:contact@up2front.com", U["ecrire"]),
               ("btn-s", vers(rel, lg, "index.html") + "#faq",
                U["faq_t"].rstrip("."))]),
    ])

    ld_sup = ld({
        "@context": "https://schema.org",
        "@type": "Blog",
        "@id": url(lg, rel) + "#blog",
        "url": url(lg, rel),
        "name": I["sur_titre"] + " — Up2Front",
        "description": U["blog_desc"],
        "inLanguage": oss.html_lang,
        "publisher": {"@id": "https://up2front.com/#organisation"},
        "blogPost": [
            {"@type": "BlogPosting",
             "headline": a["titre"],
             "url": url(lg, "blog/" + a["slug"]),
             "datePublished": D.UI["date_iso"],
             "author": {"@type": "Person", "name": "Maxime Pilloud"}}
            for a in D.ARTICLES],
    })
    return oss.enveloppe(rel, U["blog_titre"], U["blog_desc"], ld_sup, corps)


def page_article(oss, D, i):
    lg = oss.lg
    a = D.ARTICLES[i]
    U = D.UI
    rel = "blog/" + a["slug"]

    suivants = [D.ARTICLES[(i + 1) % len(D.ARTICLES)],
                D.ARTICLES[(i + 2) % len(D.ARTICLES)]]
    cartes = "\n    ".join(
        carte_article(s["slug"], "%s · %s" % (s["cat"], s["lecture"]),
                      s["titre"], s["desc"], U["lire"]) for s in suivants)

    meta = U["meta"].format(date=U["date_texte"], lecture=a["lecture"])

    corps = "\n".join([
        fil(rel, lg, [(U["accueil"], "index.html"),
                      (U["fil_blog"], "blog.html"), (a["cat"], None)]),
        hero(a["cat"], a["h1"], a["dek"],
             [("btn-p", vers(rel, lg, "index.html") + "#tarifs",
               U["voir_tarifs"]),
              ("btn-s", vers(rel, lg, "blog.html"), U["retour"])]),
        '<section class="wrap"><div class="prose">\n<p class="maj">%s</p>\n%s'
        '</div></section>' % (meta, a["corps"]),
        bloc_faq(U["faq_t"], U["faq_c"], a["faq"]),
        """<section class="sec wrap">
  <h2 class="sec-t">{t}</h2>
  <p class="sec-c">{c}</p>
  <div class="grille g-2">
    {cartes}
  </div>
</section>""".format(t=U["suite_t"], c=U["suite_c"], cartes=cartes),
        appel(U["art_appel_h2"], U["art_appel_p"],
              [("btn-p", vers(rel, lg, "devis.html"), U["art_appel_b1"]),
               ("btn-s", vers(rel, lg, "index.html") + "#tarifs",
                U["art_appel_b2"])]),
    ])

    article_ld = ld({
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "@id": url(lg, rel) + "#article",
        "headline": a["titre"],
        "description": a["desc"],
        "url": url(lg, rel),
        "inLanguage": oss.html_lang,
        "datePublished": U["date_iso"],
        "dateModified": U["date_iso"],
        "articleSection": a["cat"],
        "image": "https://up2front.com/og-image.png",
        "author": {"@type": "Person", "name": "Maxime Pilloud",
                   "url": "https://up2front.com/"},
        "publisher": {"@id": "https://up2front.com/#organisation"},
        "isPartOf": {"@id": url(lg, "blog.html") + "#blog"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url(lg, rel)},
    })
    faq_ld = ld({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": r}}
            for q, r in a["faq"]],
    })
    titre = a["titre"] + " | Up2Front"
    return oss.enveloppe(rel, titre, a["desc"],
                         article_ld + "\n" + faq_ld, corps, og="article")


def page_parrainage(oss, D):
    lg, rel = oss.lg, "parrainage.html"
    P, U = D.PARRAINAGE, D.UI

    etapes = "\n  ".join(
        '<div class="rv">\n    <div class="n">%s</div>\n    <h3>%s</h3>\n'
        '    <p>%s</p>\n  </div>' % e for e in P["etapes"])

    corps = "\n".join([
        fil(rel, lg, [(U["accueil"], "index.html"), (P["fil"], None)]),
        hero(P["sur_titre"], P["h1"], P["lede"],
             [("btn-p", "mailto:contact@up2front.com"
               "?subject=Parrainage", P["b1"]),
              ("btn-s", vers(rel, lg, "legal/affiliation.html"), P["b2"])]),
        '<section class="wrap"><div class="prose">%s</div></section>'
        % P["prose"],
        """<section class="sec wrap">
  <h2 class="sec-t">{t}</h2>
  <p class="sec-c">{c}</p>
  <div class="suite suite-3">
  {etapes}
  </div>
</section>""".format(t=P["etapes_t"], c=P["etapes_c"], etapes=etapes),
        appel(P["appel_h2"], P["appel_p"],
              [("btn-p", "mailto:contact@up2front.com", P["appel_b1"]),
               ("btn-s", vers(rel, lg, "index.html") + "#tarifs",
                P["appel_b2"])]),
    ])
    return oss.enveloppe(rel, P["titre"], P["desc"], "", corps)


# ---------------------------------------------------------------------------

FINE = [(" ?", " ?"), (" !", " !"), (" ;", " ;"),
        (" :", " :"), (" »", " »"), ("« ", "« ")]


def franciser(x):
    """Espace insécable avant la ponctuation double (règle française).

    Un caractère U+00A0 plutôt qu'une entité : le même texte sert au HTML
    et au JSON-LD, où « &nbsp; » s'afficherait tel quel.
    """
    if isinstance(x, str):
        for a, b in FINE:
            x = x.replace(a, b)
        return x
    if isinstance(x, list):
        return [franciser(v) for v in x]
    if isinstance(x, tuple):
        return tuple(franciser(v) for v in x)
    if isinstance(x, dict):
        return {k: franciser(v) for k, v in x.items()}
    return x


def construire(lg):
    D = importlib.import_module("_blog_" + lg)
    D.UI.setdefault("date_iso", "2026-09-12")
    if lg == "fr":
        D.INDEX = franciser(D.INDEX)
        D.UI = franciser(D.UI)
        D.PARRAINAGE = franciser(D.PARRAINAGE)
        D.ARTICLES = [franciser(a) for a in D.ARTICLES]
    oss = Ossature(lg)
    faits = []

    for rel, html in [("blog.html", page_index(oss, D)),
                      ("parrainage.html", page_parrainage(oss, D))] + \
                     [("blog/" + a["slug"], page_article(oss, D, i))
                      for i, a in enumerate(D.ARTICLES)]:
        ecrire(chemin_fichier(lg, rel), html)
        faits.append(os.path.relpath(chemin_fichier(lg, rel), RACINE))
    return faits


if __name__ == "__main__":
    demandees = sys.argv[1:] or [c for c, _ in LANGUES]
    for code in demandees:
        try:
            importlib.import_module("_blog_" + code)
        except ImportError:
            print("· %s : pas de contenu (_blog_%s.py absent)" % (code, code))
            continue
        f = construire(code)
        print("· %s : %d pages" % (code, len(f)))
        for x in f:
            print("    ", x)
