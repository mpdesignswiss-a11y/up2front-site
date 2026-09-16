#!/bin/bash
# Double-cliquer ce fichier depuis le Finder. Rien à taper.
#
# Ouvre le site en local, sur votre machine uniquement, à l'adresse
# http://localhost:8787 — rien n'est publié, rien ne sort de l'ordinateur.
# Sert à relire et à corriger les pages avant la vraie mise en ligne.
#
# Pour arrêter : fermer cette fenêtre, ou Ctrl+C.

cd "$(dirname "$0")" || exit 1

bleu()  { printf "\033[1;34m%s\033[0m\n" "$1"; }
vert()  { printf "\033[1;32m%s\033[0m\n" "$1"; }
jaune() { printf "\033[1;33m%s\033[0m\n" "$1"; }
rouge() { printf "\033[1;31m%s\033[0m\n" "$1"; }
gris()  { printf "\033[0;90m%s\033[0m\n" "$1"; }

PORT=8787

echo
bleu "Up2Front — aperçu local"
gris "Dossier : $(pwd)/public"
echo

if [ ! -d public ]; then
  rouge "Le dossier public/ est introuvable."
  gris "  Ce fichier doit rester à la racine de up2front-site."
  echo
  read -r -p "Appuyez sur Entrée pour fermer cette fenêtre."
  exit 1
fi

# --- Le port est-il déjà pris ? ---------------------------------------------

if lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  jaune "Un aperçu tourne déjà sur le port $PORT."
  gris "  On réutilise celui-là plutôt que d'en lancer un deuxième."
  DEJA=1
else
  DEJA=0
fi

# --- Démarrage --------------------------------------------------------------

if [ "$DEJA" -eq 0 ]; then
  cd public || exit 1
  python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 &
  SERVEUR=$!
  cd .. || exit 1
  sleep 1

  if ! kill -0 "$SERVEUR" 2>/dev/null; then
    rouge "Le serveur local n'a pas démarré."
    gris "  Vérifiez que python3 est installé : tapez « python3 --version »."
    echo
    read -r -p "Appuyez sur Entrée pour fermer cette fenêtre."
    exit 1
  fi

  # Arrêter proprement le serveur quand la fenêtre se ferme
  trap 'kill "$SERVEUR" 2>/dev/null; echo; gris "Aperçu arrêté."; exit 0' INT TERM HUP EXIT
fi

vert "L'aperçu tourne."
echo
gris "  Accueil          http://localhost:$PORT/"
gris "  Visibilité IA    http://localhost:$PORT/visibilite-ia.html"
gris "  L'étude          http://localhost:$PORT/etudes/visibilite-ia-architectes-geneve.html"
echo
jaune "Visible uniquement depuis cet ordinateur. Rien n'est publié."
echo

open "http://localhost:$PORT/visibilite-ia.html"

gris "Laissez cette fenêtre ouverte tant que vous travaillez sur le site."
gris "Pour arrêter : fermez la fenêtre, ou Ctrl+C."
echo

if [ "$DEJA" -eq 0 ]; then
  wait "$SERVEUR"
else
  read -r -p "Appuyez sur Entrée pour fermer cette fenêtre."
fi
