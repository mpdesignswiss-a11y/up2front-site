#!/bin/bash
# Range les captures d'écran du Bureau dans captures/<bureau>/
# avec le nom normalisé du protocole. Double-cliquer pour lancer.
#
# Hypothèse : tu as capturé les 7 bureaux DANS L'ORDRE de la feuille,
# une image par bureau (ou plusieurs si tu as scrollé — voir plus bas).
# L'heure vient de la date de création du fichier, pas d'une horloge
# que quelqu'un aurait pu régler.

cd "$(dirname "$0")/.." || exit 1
RACINE="$(pwd)"
BUREAU="$HOME/Desktop"

ORDRE=(herteltan meier csdk camille-aryeh corpus ambrosetti keller)
LIBELLE=("HertelTan" "meier + associés" "CSDK" "Camille Aryeh" "CORPUS" "Pierre Ambrosetti" "KELLER")

echo ""
echo "=============================================="
echo "  RANGEMENT DES CAPTURES — relevé express"
echo "=============================================="
echo ""

printf "Moteur ? (1 = Google AI Mode, 2 = Perplexity) : "
read -r M
case "$M" in
  1) MOTEUR="googleaimode" ;;
  2) MOTEUR="perplexity" ;;
  *) echo "Réponse non comprise. Rien n'a été touché."; read -r _; exit 1 ;;
esac

printf "Combien d'images à ranger ? (7 si un bureau = une image) : "
read -r N
if ! [[ "$N" =~ ^[0-9]+$ ]] || [ "$N" -lt 1 ]; then
  echo "Nombre non compris. Rien n'a été touché."; read -r _; exit 1
fi

# Les N PNG les plus récents du Bureau, du plus ancien au plus récent.
FICHIERS=()
while IFS= read -r f; do FICHIERS+=("$f"); done < <(
  ls -t "$BUREAU"/*.png 2>/dev/null | head -n "$N" | tail -r
)

if [ "${#FICHIERS[@]}" -lt "$N" ]; then
  echo ""
  echo "Trouvé seulement ${#FICHIERS[@]} image(s) PNG sur le Bureau. Rien n'a été touché."
  read -r _; exit 1
fi

echo ""
echo "Voici ce qui va être fait — RIEN n'est déplacé avant ta confirmation :"
echo ""

CIBLES=()
for i in "${!FICHIERS[@]}"; do
  f="${FICHIERS[$i]}"
  if [ "$N" -eq 7 ]; then
    slug="${ORDRE[$i]}"; lib="${LIBELLE[$i]}"
  else
    slug="_a-trier"; lib="à trier à la main"
  fi
  H=$(stat -f '%SB' -t '%Y-%m-%d_%Hh%M' "$f")
  nom="${H}_${MOTEUR}_${slug}.png"
  # suffixe si le nom existe déjà (deuxième capture du même relevé)
  n=2; base="${H}_${MOTEUR}_${slug}"
  while [ -e "$RACINE/captures/$slug/$nom" ]; do
    nom="${base}_suite${n}.png"; n=$((n+1))
  done
  CIBLES+=("$slug/$nom")
  printf "  %-45s  ->  captures/%s/%s   [%s]\n" "$(basename "$f")" "$slug" "$nom" "$lib"
done

echo ""
printf "On range ? (o / n) : "
read -r OK
[ "$OK" = "o" ] || { echo "Annulé. Rien n'a été touché."; read -r _; exit 0; }

for i in "${!FICHIERS[@]}"; do
  cible="$RACINE/captures/${CIBLES[$i]}"
  mkdir -p "$(dirname "$cible")"
  mv "${FICHIERS[$i]}" "$cible" && echo "  rangé : captures/${CIBLES[$i]}"
done

echo ""
echo "Terminé. Les images sont dans captures/."
echo "Prochaine étape : bash captures/sceller.sh \"passage N — 17 septembre\""
echo ""
printf "Appuie sur Entrée pour fermer."
read -r _
