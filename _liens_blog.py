#!/usr/bin/env python3
"""
Câble le blog et la page parrainage dans la navigation de tout le site.

Deux points d'insertion, sur les 4 langues :
  · pied de page, colonne « Explorer » — après l'entrée FAQ ;
  · menu mobile — après l'entrée FAQ.

Le chemin relatif est déduit du lien FAQ déjà présent dans le fichier, ce
qui évite de recalculer une profondeur : un lien qui marche déjà donne le
préfixe correct. Le script est idempotent.
"""

import os
import re

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

LIBELLES = {
    "fr": ("Blog", "Parrainage"),
    "en": ("Blog", "Referrals"),
    "de": ("Blog", "Empfehlungsprogramm"),
    "it": ("Blog", "Segnalazioni"),
}


def langue(chemin):
    rel = os.path.relpath(chemin, RACINE).split(os.sep)
    return rel[0] if rel[0] in ("en", "de", "it") else "fr"


FAQ_LI = re.compile(
    r'(<li><a class="o" href="([^"]*)index\.html#faq">[^<]*</a></li>)')
FAQ_MM = re.compile(r'(<a href="([^"]*)index\.html#faq">[^<]*</a>)')


def traiter(chemin):
    s = open(chemin, encoding="utf-8").read()
    lg = langue(chemin)
    blog, parr = LIBELLES[lg]
    avant = s

    if ">%s</a></li>" % blog not in s:
        def pied(m):
            pfx = m.group(2)
            return (m.group(1)
                    + '\n        <li><a class="o" href="%sblog.html">%s</a></li>'
                      % (pfx, blog)
                    + '\n        <li><a class="o" href="%sparrainage.html">%s'
                      '</a></li>' % (pfx, parr))
        s = FAQ_LI.sub(pied, s, count=1)

    if '"menu-mobile"' in s:
        deb = s.index('class="menu-mobile"')
        fin = s.index("</div>", deb)
        bloc = s[deb:fin]
        if ">%s</a>" % blog not in bloc:
            def mob(m):
                return (m.group(1) + '\n    <a href="%sblog.html">%s</a>'
                        % (m.group(2), blog))
            s = s[:deb] + FAQ_MM.sub(mob, bloc, count=1) + s[fin:]

    if s != avant:
        open(chemin, "w", encoding="utf-8").write(s)
        return True
    return False


if __name__ == "__main__":
    n = t = 0
    for d, _, fs in os.walk(RACINE):
        for f in sorted(fs):
            if f.endswith(".html"):
                t += 1
                if traiter(os.path.join(d, f)):
                    n += 1
    print("%d fichiers modifiés sur %d" % (n, t))
