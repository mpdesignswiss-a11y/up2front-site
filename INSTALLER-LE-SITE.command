#!/bin/bash
# Double-cliquer ce fichier depuis le Finder. Rien à taper.
# Installe les dépendances du nouveau site Astro (dossier site/), vérifie qu'il
# se construit, puis le lance sur http://localhost:4321
#
# Ce script ne touche jamais à public/, qui reste ce qui est publié en ligne
# sur up2front.com tant que la bascule n'a pas été faite.

cd "$(dirname "$0")" || exit 1

bleu()  { printf "\033[1;34m%s\033[0m\n" "$1"; }
vert()  { printf "\033[1;32m%s\033[0m\n" "$1"; }
jaune() { printf "\033[1;33m%s\033[0m\n" "$1"; }
rouge() { printf "\033[1;31m%s\033[0m\n" "$1"; }
gris()  { printf "\033[0;90m%s\033[0m\n" "$1"; }

echo
bleu "Up2Front — nouveau site (Astro)"
gris "Dossier : $(pwd)/site"
echo

if [ ! -d site ]; then
  rouge "Le dossier site/ est introuvable."
  gris "  Ce fichier doit rester à la racine du dépôt up2front-site."
  echo; read -r -p "Entrée pour fermer."; exit 1
fi

# --- 1. Node ---------------------------------------------------------------
# Un script lancé au double-clic ne charge pas le profil du shell : Node peut
# être installé sans être visible. On va le chercher là où il se trouve.
if ! command -v node >/dev/null 2>&1; then
  gris "Node introuvable dans le PATH — recherche dans les emplacements habituels…"

  for d in /opt/homebrew/bin /usr/local/bin /opt/local/bin "$HOME/.local/bin"; do
    [ -x "$d/node" ] && export PATH="$d:$PATH" && break
  done

  # nvm
  if ! command -v node >/dev/null 2>&1; then
    export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
    if [ -s "$NVM_DIR/nvm.sh" ]; then
      # shellcheck disable=SC1091
      . "$NVM_DIR/nvm.sh" >/dev/null 2>&1
      nvm use --lts >/dev/null 2>&1 || nvm use default >/dev/null 2>&1
    fi
  fi

  # fnm / volta / asdf
  if ! command -v node >/dev/null 2>&1; then
    for d in "$HOME/.volta/bin" "$HOME/.asdf/shims" "$HOME/Library/Application Support/fnm/aliases/default/bin"; do
      [ -x "$d/node" ] && export PATH="$d:$PATH" && break
    done
  fi

  # dernier recours : la version la plus récente sous ~/.nvm
  if ! command -v node >/dev/null 2>&1; then
    CAND=$(ls -d "$HOME"/.nvm/versions/node/*/bin 2>/dev/null | sort -V | tail -1)
    [ -n "$CAND" ] && [ -x "$CAND/node" ] && export PATH="$CAND:$PATH"
  fi

  if command -v node >/dev/null 2>&1; then
    vert "Node trouvé : $(command -v node)"
  fi
fi

if ! command -v node >/dev/null 2>&1; then
  rouge "Node.js n'est pas installé sur cette machine."
  echo
  echo "  Va sur  https://nodejs.org  et prends le gros bouton de gauche (LTS)."
  echo "  Ouvre le fichier .pkg téléchargé, suis l'installateur, laisse tout par défaut."
  echo "  Il te demandera ton mot de passe Mac : c'est normal."
  echo "  Puis reviens ici et double-clique à nouveau sur ce fichier."
  echo
  read -r -p "Entrée pour fermer."; exit 1
fi

VERSION=$(node -v | sed 's/v//' | cut -d. -f1)
if [ "$VERSION" -lt 18 ]; then
  rouge "Node $(node -v) est trop ancien — il faut la version 18 ou plus."
  echo "  Installe la LTS sur https://nodejs.org puis relance ce fichier."
  echo; read -r -p "Entrée pour fermer."; exit 1
fi
vert "Node $(node -v) — bon"

cd site || exit 1

# --- 2. Résidu d'un ancien montage -----------------------------------------
# Une session précédente avait posé un lien symbolique node_modules pointant
# vers un chemin qui n'existe pas sur ce Mac. S'il traîne encore, npm échoue.
if [ -L node_modules ]; then
  jaune "Lien node_modules hérité détecté — suppression."
  rm -f node_modules
fi

# --- 3. Polices ------------------------------------------------------------
MANQUE=0
[ -f public/fonts/display.woff2 ] || MANQUE=1
[ -f public/fonts/texte.woff2 ]   || MANQUE=1
if [ "$MANQUE" -eq 1 ]; then
  jaune "Les polices ne sont pas encore posées."
  gris "  Le site s'affichera dans la police système : rendu dégradé, mais rien ne casse."
  gris "  Les deux blocs @font-face de src/theme/tokens.css sont commentés exprès,"
  gris "  pour ne pas demander au navigateur des fichiers absents."
  gris "  Pour corriger : déposer display.woff2 et texte.woff2 dans site/public/fonts/"
  gris "  (fichiers gratuits sur https://www.fontshare.com), puis décommenter."
else
  vert "Polices présentes"
fi
echo

# --- 4. Installation -------------------------------------------------------
bleu "Installation des dépendances — deux à trois minutes la première fois…"
INSTALL_OK=0
if [ -f package-lock.json ]; then
  # npm ci installe exactement les versions inscrites au verrou, ni plus ni moins.
  if npm ci --no-audit --no-fund; then
    INSTALL_OK=1
  else
    jaune "npm ci a échoué — le verrou est peut-être décalé. Reprise avec npm install."
    npm install --no-audit --no-fund && INSTALL_OK=1
  fi
else
  npm install --no-audit --no-fund && INSTALL_OK=1
fi

if [ "$INSTALL_OK" -ne 1 ]; then
  echo
  rouge "L'installation a échoué."
  gris "  Copie les lignes rouges ci-dessus et envoie-les à Claude."
  echo; read -r -p "Entrée pour fermer."; exit 1
fi
vert "Dépendances installées"
echo

# --- 5. Construction de vérification ---------------------------------------
bleu "Vérification : construction du site…"
if ! npm run build; then
  echo
  rouge "Le site ne se construit pas."
  gris "  Copie les lignes rouges ci-dessus et envoie-les à Claude."
  echo; read -r -p "Entrée pour fermer."; exit 1
fi
echo
vert "Le site se construit sans erreur."
gris "  Résultat dans site/dist/ — pas encore publié."
gris "  up2front.com continue de servir public/ jusqu'à la bascule."
echo

# --- 6. Serveur de développement -------------------------------------------
bleu "Lancement du site sur http://localhost:4321"
gris "  Le navigateur va s'ouvrir tout seul."
gris "  Pour arrêter : Ctrl + C dans cette fenêtre."
echo
( sleep 4; open "http://localhost:4321" ) &
npm run dev

echo
read -r -p "Entrée pour fermer."
