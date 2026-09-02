#!/bin/bash
# Double-cliquer ce fichier depuis le Finder. Rien à taper.
#
# Ce script recopie le nouveau design depuis le dossier de travail
# (Bureau/Up2Front/fichier-alex-branche) vers le dossier publié
# (public/nouveau), enregistre le changement, et l'envoie en ligne.
#
# Résultat : https://up2front.com/nouveau/ est à jour en une ou deux minutes.
# Le site principal, https://up2front.com/, n'est jamais touché.

cd "$(dirname "$0")" || exit 1

SOURCE="$HOME/Desktop/Up2Front/fichier-alex-branche"
CIBLE="public/nouveau"

bleu()  { printf "\033[1;34m%s\033[0m\n" "$1"; }
vert()  { printf "\033[1;32m%s\033[0m\n" "$1"; }
jaune() { printf "\033[1;33m%s\033[0m\n" "$1"; }
rouge() { printf "\033[1;31m%s\033[0m\n" "$1"; }
gris()  { printf "\033[0;90m%s\033[0m\n" "$1"; }

fin() { echo; read -r -p "Appuyez sur Entrée pour fermer cette fenêtre."; exit "$1"; }

echo
bleu "Up2Front — mise à jour du nouveau design"
gris "Source : $SOURCE"
gris "Cible  : $(pwd)/$CIBLE"
echo

if [ ! -d .git ]; then
  rouge "Ce dossier n'est pas le dépôt du site."
  gris "  Ce fichier doit rester à la racine de up2front-site."
  fin 1
fi

if [ ! -d "$SOURCE" ]; then
  rouge "Le dossier de travail est introuvable."
  gris "  Attendu ici : $SOURCE"
  fin 1
fi

# --- 1. Recopie -------------------------------------------------------------
bleu "Recopie des fichiers…"
rm -rf "$CIBLE"
mkdir -p "$CIBLE"
rsync -a --exclude '*.alex-original' --exclude '.DS_Store' "$SOURCE"/ "$CIBLE"/

pages=$(find "$CIBLE" -name '*.html' | wc -l | tr -d ' ')
gris "  $pages pages recopiées."

# --- 2. Cette copie ne doit pas concurrencer le vrai site dans Google --------
python3 - "$CIBLE" <<'PY'
import pathlib, sys
cible = pathlib.Path(sys.argv[1])
balise = '<meta name="robots" content="noindex,nofollow">'
ancre  = '<meta name="viewport" content="width=device-width,initial-scale=1">'
n = 0
for p in sorted(cible.rglob('*.html')):
    t = p.read_text(encoding='utf-8')
    if 'name="robots"' in t:
        continue
    if ancre in t:
        p.write_text(t.replace(ancre, ancre + '\n' + balise, 1), encoding='utf-8')
        n += 1
print(f"  {n} pages passées en noindex (aperçu non référencé).")
PY

# --- 3. Rien n'a changé ? On s'arrête là ------------------------------------
if [ -z "$(git status --porcelain "$CIBLE")" ]; then
  vert "Aucun changement depuis la dernière publication — tout est déjà en ligne."
  fin 0
fi

echo
gris "Fichiers modifiés :"
git status --short "$CIBLE" | head -12 | sed 's/^/    /'
total=$(git status --porcelain "$CIBLE" | wc -l | tr -d ' ')
[ "$total" -gt 12 ] && gris "    … et $((total - 12)) autres."
echo

# --- 4. Enregistrement ------------------------------------------------------
bleu "Enregistrement…"
git add -A "$CIBLE"
git commit -q -m "Nouveau design : mise à jour de l'aperçu /nouveau/ ($(date '+%d.%m.%Y %H:%M'))"
vert "  Enregistré."

# --- 5. Envoi ---------------------------------------------------------------
echo
bleu "Envoi vers GitHub…"
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
gris "Suivre la publication :"
gris "  https://github.com/mpdesignswiss-a11y/up2front-site/actions"
echo
gris "Vérifier une fois publié :"
gris "  https://up2front.com/nouveau/"
gris "  https://up2front.com/nouveau/realisations.html"
gris "  https://up2front.com/nouveau/offres/pro-landing-page-checkout.html"
echo
gris "Le site principal n'a pas bougé :"
gris "  https://up2front.com/"

fin 0
