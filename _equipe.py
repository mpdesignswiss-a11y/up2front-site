#!/usr/bin/env python3
"""
Pose la section « L'équipe » sur la page d'accueil des quatre langues.

Insertion juste avant le commentaire de la FAQ. Le script est idempotent :
si la section est déjà là, il ne fait rien.

Les classes .team / .mbr existent déjà dans assets/u2f.css (grille de trois,
deux colonnes en tablette, une en mobile) : rien à ajouter au style.
"""

import os
import re

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

# prénom, nom, initiales — l'ordre vaut pour les quatre langues
GENS = [
    ("Maxime Pilloud",  "MP"),
    ("Gaetan Curtis",   "GC"),
    ("Loic Nuvel",      "LN"),
    ("Alex Buler",      "AB"),
    ("Nicolas Herni",   "NH"),
]

TEXTES = {
    "fr": {
        "lbl": "L'équipe",
        "h2": "Qui travaille sur votre site.",
        "sub": "Vous savez à qui vous écrivez, et qui fait quoi.",
        "roles": [
            ("Fondateur", "Design et développement des sites."),
            ("Business Developer", "Votre premier interlocuteur en Suisse romande."),
            ("Marketing digital", "Visibilité, référencement, campagnes."),
            ("Customer Success", "Le suivi après la mise en ligne et les révisions."),
            ("Développeur", "Intégration, performance, mise en ligne."),
        ],
    },
    "en": {
        "lbl": "The team",
        "h2": "Who works on your website.",
        "sub": "You know who you are writing to, and who does what.",
        "roles": [
            ("Founder", "Design and development of the websites."),
            ("Business Developer", "Your first point of contact in French-speaking Switzerland."),
            ("Digital marketing", "Visibility, search ranking, campaigns."),
            ("Customer Success", "Follow-up after launch and revisions."),
            ("Developer", "Build, performance, going live."),
        ],
    },
    "de": {
        "lbl": "Das Team",
        "h2": "Wer an Ihrer Website arbeitet.",
        "sub": "Sie wissen, wem Sie schreiben und wer was macht.",
        "roles": [
            ("Gründer", "Design und Entwicklung der Websites."),
            ("Business Developer", "Ihre erste Ansprechperson in der Westschweiz."),
            ("Digitales Marketing", "Sichtbarkeit, Suchmaschinen, Kampagnen."),
            ("Customer Success", "Betreuung nach dem Livegang und Korrekturen."),
            ("Entwickler", "Umsetzung, Performance, Livegang."),
        ],
    },
    "it": {
        "lbl": "Il team",
        "h2": "Chi lavora al vostro sito.",
        "sub": "Sapete a chi scrivete e chi fa che cosa.",
        "roles": [
            ("Fondatore", "Design e sviluppo dei siti."),
            ("Business Developer", "Il vostro primo interlocutore nella Svizzera romanda."),
            ("Marketing digitale", "Visibilità, posizionamento, campagne."),
            ("Customer Success", "Il seguito dopo la messa online e le revisioni."),
            ("Sviluppatore", "Integrazione, prestazioni, messa online."),
        ],
    },
}

CARTE = """    <div class="mbr rv">
      <div class="av"><svg viewBox="0 0 56 56" aria-hidden="true"><text x="28" y="35"
        text-anchor="middle" font-size="20" font-weight="600" fill="#0b0b0b">%s</text></svg></div>
      <b>%s</b>
      <em>%s</em>
      <span>%s</span>
    </div>
"""


def section(lg):
    t = TEXTES[lg]
    cartes = "".join(
        CARTE % (ini, role, nom, desc)
        for (nom, ini), (role, desc) in zip(GENS, t["roles"]))
    return (
        '<!-- ============ ÉQUIPE ============ -->\n'
        '<section class="sec wrap" id="equipe">\n'
        '  <p class="lbl rv">%s</p>\n'
        '  <h2 class="h2 rv" data-eclats>%s</h2>\n'
        '  <p class="sub rv">%s</p>\n\n'
        '  <div class="team">\n%s  </div>\n'
        '</section>\n\n' % (t["lbl"], t["h2"], t["sub"], cartes))


def traiter(chemin, lg):
    s = open(chemin, encoding="utf-8").read()
    if 'id="equipe"' in s:
        return False
    m = re.search(r'\n(<!-- =+ FAQ[^\n]*-->\n)?<section class="sec wrap" id="faq">',
                  s)
    assert m, "ancre FAQ introuvable dans " + chemin
    debut = m.start() + 1
    s = s[:debut] + section(lg) + s[debut:]
    open(chemin, "w", encoding="utf-8").write(s)
    return True


if __name__ == "__main__":
    cibles = [("fr", "index.html"), ("en", "en/index.html"),
              ("de", "de/index.html"), ("it", "it/index.html")]
    for lg, rel in cibles:
        chemin = os.path.join(RACINE, rel)
        print("%-16s %s" % (rel, "posée" if traiter(chemin, lg) else "déjà là"))
