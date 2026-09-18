#!/bin/bash
# Range les captures du test des moteurs (18 septembre) dans
# captures/_test-moteurs/ avec le nom normalisé du protocole.
# Double-cliquer pour lancer.
#
# Version 2. La version 1 prenait « les N images les plus récentes du Bureau »,
# en supposant qu'aucune autre capture n'avait été prise pendant ou après le
# relevé. Cette hypothèse était fausse : des captures de travail (fenêtre
# Finder, Terminal) se sont glissées parmi les relevés. Le script ne devine
# plus. Il montre TOUT ce qu'il y a sur le Bureau, avec l'heure de création de
# chaque fichier, et demande d'écarter ce qui n'est pas un relevé.
#
# L'heure vient de la date de création du fichier, jamais d'une horloge qu'on
# aurait pu régler.

cd "$(dirname "$0")" || exit 1
CIBLE="$(pwd)/_test-moteurs"
BUREAU="$HOME/Desktop"
ETUDE="herteltan_HT-01"

echo ""
echo "======================================================"
echo "  RANGEMENT — test des moteurs, 18 septembre"
echo "======================================================"

# ---------------------------------------------------------------
# 1. Le catalogue : tous les PNG du Bureau, du plus ancien au plus récent.
# ---------------------------------------------------------------
TOUS=()
while IFS= read -r f; do TOUS+=("$f"); done < <(
  ls -t "$BUREAU"/*.png 2>/dev/null | tail -r
)

if [ "${#TOUS[@]}" -eq 0 ]; then
  echo ""; echo "Aucun PNG sur le Bureau. Rien à ranger."; read -r _; exit 1
fi

echo ""
echo "Les images du Bureau, de la plus ANCIENNE à la plus RÉCENTE."
echo "L'heure est celle de création du fichier."
echo ""
for i in "${!TOUS[@]}"; do
  n=$((i+1))
  h=$(stat -f '%SB' -t '%d/%m %Hh%M:%S' "${TOUS[$i]}")
  printf "  %3d.  %s   %s\n" "$n" "$h" "$(basename "${TOUS[$i]}")"
done

# ---------------------------------------------------------------
# 2. Écarter ce qui n'est pas un relevé.
# ---------------------------------------------------------------
echo ""
echo "Quels numéros NE SONT PAS des relevés ? (captures de travail, autres)"
echo "Séparés par des espaces. Laisser vide si tout est un relevé."
echo ""
printf "À écarter : "
read -r ECARTES

declare -a GARDE
for i in "${!TOUS[@]}"; do
  n=$((i+1)); jeter=0
  for e in $ECARTES; do [ "$e" = "$n" ] && jeter=1; done
  [ "$jeter" -eq 0 ] && GARDE+=("${TOUS[$i]}")
done

echo ""
echo "Il reste ${#GARDE[@]} image(s) de relevé :"
for f in "${GARDE[@]}"; do
  h=$(stat -f '%SB' -t '%Hh%M:%S' "$f")
  printf "     %s   %s\n" "$h" "$(basename "$f")"
done

if [ "${#GARDE[@]}" -eq 0 ]; then
  echo ""; echo "Plus rien à ranger. Rien n'a été touché."; read -r _; exit 1
fi

# ---------------------------------------------------------------
# 3. Combien d'images par relevé.
# ---------------------------------------------------------------
echo ""
echo "Maintenant, comment ces ${#GARDE[@]} images se répartissent en relevés."
echo "Un nombre par relevé, dans l'ordre, séparés par des espaces."
echo "Exemple : 2 1 1 1  =  quatre relevés, deux images au premier."
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

if [ "$N" -ne "${#GARDE[@]}" ]; then
  echo ""
  echo "Le compte ne tombe pas juste : tu déclares $N image(s) réparties en"
  echo "relevés, mais il en reste ${#GARDE[@]} après écartement."
  echo "Rien n'a été touché. Relance et reprends le compte."
  read -r _; exit 1
fi

FICHIERS=("${GARDE[@]}")

# ---------------------------------------------------------------
# 4. L'aperçu. Rien ne bouge avant « o ».
# ---------------------------------------------------------------
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
