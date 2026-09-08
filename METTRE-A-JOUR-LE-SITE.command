#!/bin/bash
# Double-cliquer ce fichier depuis le Finder. Rien à taper.
#
# Reconstruit le site depuis Bureau/Up2Front/site-v3, le recopie à la racine
# publiée (public/), enregistre le changement et l'envoie en ligne.
#
# Ce qui n'est jamais écrasé : CNAME (le domaine), le site anglais /en/,
# les polices, et les redirections des anciennes URL légales.

cd "$(dirname "$0")" || exit 1

SOURCE="$HOME/Desktop/Up2Front/site-v3"

bleu()  { printf "\033[1;34m%s\033[0m\n" "$1"; }
vert()  { printf "\033[1;32m%s\033[0m\n" "$1"; }
rouge() { printf "\033[1;31m%s\033[0m\n" "$1"; }
gris()  { printf "\033[0;90m%s\033[0m\n" "$1"; }

fin() { echo; read -r -p "Appuyez sur Entrée pour fermer cette fenêtre."; exit "$1"; }

echo
bleu "Up2Front — mise à jour du site"
gris "Source : $SOURCE"
echo

[ -d .git ]      || { rouge "Ce dossier n'est pas le dépôt du site."; fin 1; }
[ -d "$SOURCE" ] || { rouge "Dossier de travail introuvable : $SOURCE"; fin 1; }

# --- 1. Reconstruction -----------------------------------------------------
bleu "Reconstruction des pages…"
if ! ( cd "$SOURCE" && python3 _construire/construire.py ); then
  rouge "La construction a échoué. Rien n'a été publié."
  fin 1
fi

# --- 2. Recopie ------------------------------------------------------------
echo
bleu "Recopie vers public/…"
rsync -a \
  --exclude '_construire' \
  --exclude '__pycache__' \
  --exclude '.DS_Store' \
  --exclude 'assets/_corps-accueil.html' \
  "$SOURCE"/ public/

pages=$(find public -name '*.html' -not -path 'public/nouveau/*' | wc -l | tr -d ' ')
gris "  $pages pages en place."

# --- 3. Rien changé ? ------------------------------------------------------
if [ -z "$(git status --porcelain public)" ]; then
  vert "Aucun changement — le site en ligne est déjà à jour."
  fin 0
fi

echo
gris "Fichiers modifiés :"
git status --short public | head -12 | sed 's/^/    /'
total=$(git status --porcelain public | wc -l | tr -d ' ')
[ "$total" -gt 12 ] && gris "    … et $((total - 12)) autres."

# --- 4. Enregistrement et envoi --------------------------------------------
echo
bleu "Enregistrement et envoi…"
git add -A public
git commit -q -m "Site : mise à jour ($(date '+%d.%m.%Y %H:%M'))"

if ! git push origin main; then
  echo
  rouge "L'envoi a échoué."
  gris "  Le plus souvent, c'est la clé SSH qui n'est pas chargée."
  gris "  Essayez dans le Terminal :  ssh -T git@github.com"
  gris "  Le travail est enregistré : relancez ce fichier une fois réglé."
  fin 1
fi

echo
vert "Envoyé. GitHub republie dans la minute qui vient."
echo
gris "Suivre :   https://github.com/mpdesignswiss-a11y/up2front-site/actions"
gris "Vérifier : https://up2front.com/"
gris "           https://up2front.com/realisations.html"
gris "           https://up2front.com/cgv/   (redirige vers les nouvelles CGV)"

fin 0
