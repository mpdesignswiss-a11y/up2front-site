#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bascule unique : préparer public/ à recevoir le nouveau site (site-v3) à la racine
sans casser ce qui est déjà en ligne et indexé.

Ce script ne se lance qu'UNE fois. Il fait trois choses :

  1. Déplace les anciens assets (assets/u2f.css, assets/u2f.js) dans
     assets/heritage/ et réécrit les références des pages qui les utilisent
     — sinon le CSS de v3, qui porte le même nom, casserait le site anglais
     et les anciennes pages légales.

  2. Remplace les anciennes URL légales françaises par des pages de
     redirection vers leurs équivalents v3, pour que les liens déjà donnés
     aux clients (et l'URL des CGV dans Stripe) continuent de fonctionner.

  3. Réécrit robots.txt et sitemap.xml sur le nouveau jeu d'URL.

Ce qui n'est jamais touché : CNAME, le site anglais /en/, fonts/.
"""

import pathlib, re, sys, datetime

RACINE = pathlib.Path(__file__).resolve().parent
PUBLIC = RACINE / "public"

# --------------------------------------------------------------------------
# 1. anciens assets → assets/heritage/
# --------------------------------------------------------------------------

# pages construites par l'ancien générateur, qui doivent continuer à pointer
# vers l'ancien CSS
PAGES_HERITAGE = [
    "en/index.html",
    "en/terms/index.html",
    "en/legal-notice/index.html",
    "en/privacy/index.html",
]

def deplacer_assets():
    src = PUBLIC / "assets"
    dst = src / "heritage"
    dst.mkdir(parents=True, exist_ok=True)
    deplaces = []
    for nom in ("u2f.css", "u2f.js"):
        origine = src / nom
        if origine.exists() and not (dst / nom).exists():
            (dst / nom).write_bytes(origine.read_bytes())
            deplaces.append(nom)
    if not deplaces:
        print("   assets déjà déplacés — rien à faire.")
        return

    for rel in PAGES_HERITAGE:
        p = PUBLIC / rel
        if not p.exists():
            print("   ATTENTION : %s introuvable" % rel)
            continue
        t = p.read_text(encoding="utf-8")
        avant = t
        t = t.replace("assets/u2f.css", "assets/heritage/u2f.css")
        t = t.replace("assets/u2f.js", "assets/heritage/u2f.js")
        if t != avant:
            p.write_text(t, encoding="utf-8")
    print("   %s déplacés dans assets/heritage/, %d pages réécrites."
          % (" et ".join(deplaces), len(PAGES_HERITAGE)))


# --------------------------------------------------------------------------
# 2. redirections des anciennes URL
# --------------------------------------------------------------------------

# chemin ancien -> (cible, titre, faut-il reporter ?session_id=… )
#
# /merci/ était la page « Paiement confirmé » : c'est là que Stripe renvoie le
# client après paiement, avec ?session_id=… dans l'URL. La redirection doit
# donc reporter la chaîne de requête, sinon l'identifiant de session est perdu.
REDIRECTIONS = {
    "cgv/index.html":               ("/legal/conditions.html",
                                     "Conditions générales de vente", False),
    "mentions-legales/index.html":  ("/legal/mentions-legales.html",
                                     "Mentions légales", False),
    "confidentialite/index.html":   ("/legal/confidentialite.html",
                                     "Politique de confidentialité", False),
    "merci/index.html":             ("/commande-confirmee.html",
                                     "Paiement confirmé", True),
}

GABARIT = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titre} — Up2Front</title>
<link rel="canonical" href="https://up2front.com{cible}">
<meta http-equiv="refresh" content="0; url=https://up2front.com{cible}">
<meta name="robots" content="noindex,follow">
<style>
  html{{color-scheme:dark}}
  body{{margin:0;min-height:100vh;display:flex;align-items:center;
       justify-content:center;background:#0b0b0d;color:#f4f4f5;
       font:16px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif;
       text-align:center;padding:2rem}}
  a{{color:#f4f4f5}}
</style>
<script>location.replace("{cible}"{suffixe});</script>
</head>
<body>
<p>Cette page a déménagé.<br>
<a href="{cible}">{titre} — continuer</a></p>
</body>
</html>
"""

def poser_redirections():
    for rel, (cible, titre, garder_query) in REDIRECTIONS.items():
        p = PUBLIC / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        suffixe = " + location.search" if garder_query else ""
        p.write_text(GABARIT.format(cible=cible, titre=titre, suffixe=suffixe),
                     encoding="utf-8")
        print("   %-32s → %s%s" % ("/" + rel.replace("index.html", ""), cible,
                                   "  (+ ?session_id)" if garder_query else ""))


# --------------------------------------------------------------------------
# 3. robots.txt et sitemap.xml
# --------------------------------------------------------------------------

ROBOTS = """User-agent: *
Allow: /
Disallow: /nouveau/

Sitemap: https://up2front.com/sitemap.xml
"""

# pages v3 à référencer, plus les deux pages anglaises conservées
URLS = [
    ("/",                                          "1.0"),
    ("/realisations.html",                         "0.9"),
    ("/temoignages.html",                          "0.7"),
    ("/devis.html",                                "0.9"),
    ("/offres/pro-landing-page.html",              "0.9"),
    ("/offres/advanced-website.html",              "0.9"),
    ("/offres/ultimate-website.html",              "0.9"),
    ("/etudes-de-cas/projet-01.html",              "0.6"),
    ("/etudes-de-cas/projet-02.html",              "0.6"),
    ("/etudes-de-cas/projet-03.html",              "0.6"),
    ("/etudes-de-cas/projet-04.html",              "0.6"),
    ("/etudes-de-cas/projet-05.html",              "0.6"),
    ("/etudes-de-cas/projet-06.html",              "0.6"),
    ("/legal/conditions.html",                     "0.4"),
    ("/legal/mentions-legales.html",               "0.4"),
    ("/legal/confidentialite.html",                "0.4"),
    ("/legal/remboursement.html",                  "0.4"),
    ("/legal/affiliation.html",                    "0.4"),
    ("/en/",                                       "0.5"),
    ("/en/terms/",                                 "0.3"),
    ("/en/legal-notice/",                          "0.3"),
    ("/en/privacy/",                               "0.3"),
]

def ecrire_robots_sitemap():
    (PUBLIC / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    jour = datetime.date.today().isoformat()
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, prio in URLS:
        lignes += ["  <url>",
                   "    <loc>https://up2front.com%s</loc>" % url,
                   "    <lastmod>%s</lastmod>" % jour,
                   "    <priority>%s</priority>" % prio,
                   "  </url>"]
    lignes.append("</urlset>")
    (PUBLIC / "sitemap.xml").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("   robots.txt et sitemap.xml réécrits (%d URL)." % len(URLS))


# --------------------------------------------------------------------------

def main():
    if not PUBLIC.is_dir():
        sys.exit("public/ introuvable — lancez ce script depuis le dépôt du site.")
    print("1. anciens assets")
    deplacer_assets()
    print("2. redirections")
    poser_redirections()
    print("3. référencement")
    ecrire_robots_sitemap()
    print("\nTerminé.")


if __name__ == "__main__":
    main()
