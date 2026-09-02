#!/bin/bash
# Double-cliquer ce fichier depuis le Finder. Rien à taper.
# Envoie sur GitHub tout ce qui a été préparé dans public/ et déclenche la
# mise en ligne de up2front.com. Le déploiement lui-même prend une à deux
# minutes après l'envoi ; ce script vous dit où le suivre.
#
# Ce script n'écrit rien : il ne fait qu'envoyer des commits déjà faits.

cd "$(dirname "$0")" || exit 1

bleu()  { printf "\033[1;34m%s\033[0m\n" "$1"; }
vert()  { printf "\033[1;32m%s\033[0m\n" "$1"; }
jaune() { printf "\033[1;33m%s\033[0m\n" "$1"; }
rouge() { printf "\033[1;31m%s\033[0m\n" "$1"; }
gris()  { printf "\033[0;90m%s\033[0m\n" "$1"; }

fin() { echo; read -r -p "Appuyez sur Entrée pour fermer cette fenêtre."; exit "$1"; }

echo
bleu "Up2Front — mise en ligne"
gris "Dossier : $(pwd)"
echo

if [ ! -d .git ]; then
  rouge "Ce dossier n'est pas le dépôt du site."
  gris "  Ce fichier doit rester à la racine de up2front-site."
  fin 1
fi

# --- 1. Y a-t-il quelque chose à envoyer ? ----------------------------------
git fetch origin main --quiet 2>/dev/null

en_avance=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "?")
non_commite=$(git status --porcelain public public-v2 2>/dev/null | wc -l | tr -d ' ')

if [ "$non_commite" != "0" ]; then
  jaune "Attention : des modifications dans public/ ne sont pas enregistrées."
  gris "  Elles ne partiront pas. Fichiers concernés :"
  git status --short public public-v2 | sed 's/^/    /'
  echo
fi

if [ "$en_avance" = "0" ]; then
  vert "Il n'y a rien de nouveau à envoyer — le site en ligne est déjà à jour."
  fin 0
fi

gris "$en_avance nouveau(x) commit(s) à envoyer :"
git log --oneline origin/main..HEAD | sed 's/^/    /'
echo

# --- 2. Envoi ---------------------------------------------------------------
bleu "Envoi vers GitHub…"
if ! git push origin main; then
  echo
  rouge "L'envoi a échoué."
  gris "  Le plus souvent, c'est la clé SSH qui n'est pas chargée."
  gris "  Essayez dans le Terminal :  ssh -T git@github.com"
  fin 1
fi

echo
vert "Envoyé. GitHub publie le site dans la minute qui vient."
echo
gris "Suivre la publication :"
gris "  https://github.com/mpdesignswiss-a11y/up2front-site/actions"
echo
gris "Vérifier une fois publié :"
gris "  https://up2front.com/"
gris "  https://up2front.com/cgv/"
gris "  https://up2front.com/mentions-legales/"
gris "  https://up2front.com/confidentialite/"
gris "  https://up2front.com/en/terms/"
gris "  https://up2front.com/en/legal-notice/"
gris "  https://up2front.com/en/privacy/"

fin 0
