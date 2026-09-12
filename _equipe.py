#!/usr/bin/env python3
"""
Pose la section « L'équipe » sur la page d'accueil des quatre langues.

Insertion juste avant le commentaire de la FAQ. Le script est idempotent :
si la section est déjà là, il ne fait rien.

Les classes .team / .mbr existent déjà dans assets/u2f.css (grille de trois,
deux colonnes en tablette, une en mobile) : rien à ajouter au style.

« Fondateur » ne vaut que pour Maxime Pilloud : Up2Front est une entreprise
individuelle, elle n'a qu'un titulaire. Alexandre Tranchant est associé, les
cinq autres sont indépendants — le sous-titre le dit, pour que la page
d'accueil ne contredise pas les mentions légales.
"""

import os
import re

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

CHAPEAU = {
    "fr": ("L'équipe", "Qui travaille sur votre site.",
           "Un fondateur, un associé et des indépendants qui collaborent "
           "régulièrement avec nous. Vous savez à qui vous écrivez, et qui "
           "fait quoi."),
    "en": ("The team", "Who works on your website.",
           "A founder, a partner and independent collaborators who work with "
           "us regularly. You know who you are writing to, and who does what."),
    "de": ("Das Team", "Wer an Ihrer Website arbeitet.",
           "Ein Gründer, ein Partner und Selbstständige, die regelmässig mit "
           "uns arbeiten. Sie wissen, wem Sie schreiben und wer was macht."),
    "it": ("Il team", "Chi lavora al vostro sito.",
           "Un fondatore, un socio e collaboratori indipendenti che lavorano "
           "regolarmente con noi. Sapete a chi scrivete e chi fa che cosa."),
}

# Une personne = une entrée. Le rôle et la ligne de description sont portés
# par la personne elle-même, langue par langue : plus de deux listes à tenir
# alignées quand l'équipe s'agrandit.
GENS = [
    {
        "nom": "Maxime Pilloud", "ini": "MP",
        "fr": ("Fondateur", "Design et développement des sites."),
        "en": ("Founder", "Design and development of the websites."),
        "de": ("Gründer", "Design und Entwicklung der Websites."),
        "it": ("Fondatore", "Design e sviluppo dei siti."),
    },
    {
        "nom": "Alex Tranchant", "ini": "AT",
        "fr": ("Associé", "Développement commercial et marketing."),
        "en": ("Partner", "Client acquisition and marketing."),
        "de": ("Partner", "Kundengewinnung und Marketing."),
        "it": ("Socio", "Sviluppo commerciale e marketing."),
    },
    {
        "nom": "Nina Levaux", "ini": "NL",
        "fr": ("UI/UX Design", "Maquettes et expérience utilisateur."),
        "en": ("UI/UX Design", "Mock-ups and user experience."),
        "de": ("UI/UX-Design", "Entwürfe und Nutzererfahrung."),
        "it": ("UI/UX Design", "Mockup ed esperienza utente."),
    },
    {
        "nom": "Nicolas Herni", "ini": "NH",
        "fr": ("Développeur", "Intégration, performance, mise en ligne."),
        "en": ("Developer", "Build, performance, going live."),
        "de": ("Entwickler", "Umsetzung, Performance, Livegang."),
        "it": ("Sviluppatore", "Integrazione, prestazioni, messa online."),
    },
    {
        "nom": "Gaetan Curtis", "ini": "GC",
        "fr": ("Business Developer", "Votre premier interlocuteur en Suisse romande."),
        "en": ("Business Developer", "Your first point of contact in French-speaking Switzerland."),
        "de": ("Business Developer", "Ihre erste Ansprechperson in der Westschweiz."),
        "it": ("Business Developer", "Il vostro primo interlocutore nella Svizzera romanda."),
    },
    {
        "nom": "Loic Nuvel", "ini": "LN",
        "fr": ("Marketing digital", "Visibilité, référencement, campagnes."),
        "en": ("Digital marketing", "Visibility, search ranking, campaigns."),
        "de": ("Digitales Marketing", "Sichtbarkeit, Suchmaschinen, Kampagnen."),
        "it": ("Marketing digitale", "Visibilità, posizionamento, campagne."),
    },
    {
        "nom": "Alex Buler", "ini": "AB",
        "fr": ("Customer Success", "Le suivi après la mise en ligne et les révisions."),
        "en": ("Customer Success", "Follow-up after launch and revisions."),
        "de": ("Customer Success", "Betreuung nach dem Livegang und Korrekturen."),
        "it": ("Customer Success", "Il seguito dopo la messa online e le revisioni."),
    },
]

CARTE = """    <div class="mbr rv">
      <div class="av"><svg viewBox="0 0 56 56" aria-hidden="true"><text x="28" y="35"
        text-anchor="middle" font-size="20" font-weight="600" fill="#0b0b0b">%s</text></svg></div>
      <b>%s</b>
      <em>%s</em>
      <span>%s</span>
    </div>
"""


def section(lg):
    lbl, h2, sub = CHAPEAU[lg]
    cartes = "".join(
        CARTE % (g["ini"], g[lg][0], g["nom"], g[lg][1]) for g in GENS)
    return (
        '<!-- ============ ÉQUIPE ============ -->\n'
        '<section class="sec wrap" id="equipe">\n'
        '  <p class="lbl rv">%s</p>\n'
        '  <h2 class="h2 rv" data-eclats>%s</h2>\n'
        '  <p class="sub rv">%s</p>\n\n'
        '  <div class="team">\n%s  </div>\n'
        '</section>\n\n' % (lbl, h2, sub, cartes))


BLOC = re.compile(
    r'(?:<!-- =+ ÉQUIPE =+ -->\n)?'
    r'<section class="sec wrap" id="equipe">.*?</section>\n\n?', re.S)


def traiter(chemin, lg):
    """Pose la section, ou remplace celle qui est déjà là."""
    s = open(chemin, encoding="utf-8").read()
    avant = s

    if 'id="equipe"' in s:
        s = BLOC.sub(section(lg), s, count=1)
    else:
        m = re.search(
            r'\n(?:<!-- =+ FAQ[^\n]*-->\n)?<section class="sec wrap" id="faq">', s)
        assert m, "ancre FAQ introuvable dans " + chemin
        s = s[:m.start() + 1] + section(lg) + s[m.start() + 1:]

    if s == avant:
        return False
    open(chemin, "w", encoding="utf-8").write(s)
    return True


if __name__ == "__main__":
    cibles = [("fr", "index.html"), ("en", "en/index.html"),
              ("de", "de/index.html"), ("it", "it/index.html")]
    for lg, rel in cibles:
        chemin = os.path.join(RACINE, rel)
        print("%-16s %s" % (rel, "posée" if traiter(chemin, lg) else "déjà là"))
