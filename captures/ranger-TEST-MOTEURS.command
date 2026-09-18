#!/bin/bash
# Range les captures du test des moteurs (18 septembre) dans
# captures/_test-moteurs/ avec le nom normalisé du protocole.
# Double-cliquer pour lancer. À faire UNE FOIS, à la fin des huit relevés.
#
# Hypothèse : les captures ont été prises DANS L'ORDRE du protocole —
# les ChatGPT d'abord, puis les Perplexity — sans rien capturer d'autre
# entre-temps. L'heure vient de la date de création du fichier, pas
# d'une horloge qu'on aurait pu régler.
#
# Un relevé peut porter plusieurs images (réponse longue, scroll).
# Le script demande combien d'images par relevé ; il ne devine pas.

cd "$(dirname "$0")" || exit 1
CIBLE="$(pwd)/_test-moteurs"
BUREAU="$HOME/Desktop"
ETUDE="herteltan_HT-01"

echo ""
echo "======================================================"
echo "  RANGEMENT — test des moteurs, 18 septembre"
echo "======================================================"
echo ""
echo "Combien d'images par relevé, séparées par des espaces."
echo "Exemple : 2 2 1 1  =  quatre relevés, deux images aux deux premiers."
echo "Laisser vide si le moteur n'a produit aucun relevé."
echo ""

printf "ChatGPT    : "
read -r LIGNE_CG
printf "Perplexity : "
read -r LIGNE_PX

MOTEURS=()
PASSAGES=()
COMPTES=()

lire_serie () {
  local moteur="$1" ligne="$2" p=1
  for n in $ligne; do
    if ! [[ "$n" =~ ^[0-9]+$ ]] || [ "$n" -lt 1 ]; then
      echo ""; echo "« $n » n'est pas un nombre d'images valable. Rien n'a été touché."
      read -r _; exit 1
    fi
    MOTEURS+=("$moteur"); PASSAGES+=("$p"); COMPTES+=("$n")
    p=$((p+1))
  done
}

lire_serie chatgpt    "$LIGNE_CG"
lire_serie perplexity "$LIGNE_PX"

if [ "${#COMPTES[@]}" -eq 0 ]; then
  echo ""; echo "Aucun relevé déclaré. Rien n'a été touché."; read -r _; exit 1
fi

N=0
for c in "${COMPTES[@]}"; do N=$((N+c)); done

# Les N PNG les plus récents du Bureau, du plus ancien au plus récent.
FICHIERS=()
while IFS= read -r f; do FICHIERS+=("$f"); done < <(
  ls -t "$BUREAU"/*.png 2>/dev/null | head -n "$N" | tail -r
)

if [ "${#FICHIERS[@]}" -lt "$N" ]; then
  echo ""
  echo "Il faut $N image(s) ; le Bureau n'en contient que ${#FICHIERS[@]}."
  echo "Rien n'a été touché."
  read -r _; exit 1
fi

echo ""
echo "Voici ce qui va être fait — RIEN n'est déplacé avant ta confirmation :"
echo ""

CIBLES=()
TXT_ATTENDUS=()
k=0
for i in "${!COMPTES[@]}"; do
  moteur="${MOTEURS[$i]}"
  p=$(printf '%02d' "${PASSAGES[$i]}")
  n="${COMPTES[$i]}"
  # L'heure du relevé = celle de sa PREMIÈRE image.
  H=$(stat -f '%SB' -t '%Y-%m-%d_%Hh%M' "${FICHIERS[$k]}")
  base="${H}_${moteur}_${ETUDE}_p${p}"
  TXT_ATTENDUS+=("${base}.txt")
  for j in $(seq 1 "$n"); do
    if [ "$n" -eq 1 ]; then
      nom="${base}.png"
    else
      # a, b, c, ...
      suf=$(printf "\\$(printf '%03o' $((96+j)))")
      nom="${base}_${suf}.png"
    fi
    CIBLES+=("$nom")
    printf "  %-38s  ->  %s\n" "$(basename "${FICHIERS[$k]}")" "$nom"
    k=$((k+1))
  done
done

echo ""
echo "Destination : captures/_test-moteurs/"
echo ""
printf "On range ? (o / n) : "
read -r OK
[ "$OK" = "o" ] || { echo "Annulé. Rien n'a été touché."; read -r _; exit 0; }

mkdir -p "$CIBLE"
for i in "${!FICHIERS[@]}"; do
  dest="$CIBLE/${CIBLES[$i]}"
  if [ -e "$dest" ]; then
    echo "  REFUSÉ : ${CIBLES[$i]} existe déjà. Fichier laissé sur le Bureau."
    continue
  fi
  mv "${FICHIERS[$i]}" "$dest" && echo "  rangé : ${CIBLES[$i]}"
done

# Les .txt déjà nommés selon le protocole suivent leurs images.
for t in "$BUREAU"/*"${ETUDE}"*.txt; do
  [ -e "$t" ] || continue
  mv "$t" "$CIBLE/" && echo "  rangé : $(basename "$t")"
done

echo ""
echo "Les textes attendus à côté des captures :"
for t in "${TXT_ATTENDUS[@]}"; do echo "  $t"; done
echo ""
echo "Ceux qui manquent sont à créer à la main, avec le texte intégral"
echo "de la réponse — mot pour mot, sans résumé."
echo ""
printf "Appuie sur Entrée pour fermer."
read -r _
