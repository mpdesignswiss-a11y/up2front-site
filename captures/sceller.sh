#!/bin/bash
# Scelle le passage : recalcule les empreintes, complète le manifeste, commit et pousse.
# Usage : bash captures/sceller.sh "passage 3 — 17 septembre"
set -e
cd "$(dirname "$0")/.."
echo "— empreintes —"
find captures -type f \( -name '*.png' -o -name '*.txt' \) | sort | while read -r f; do
  printf '%s  %s\n' "$( (command -v shasum >/dev/null && shasum -a 256 "$f" || sha256sum "$f") | cut -d' ' -f1)" "$f"
done | tee captures/empreintes.txt
echo
echo "— scellement git —"
git add captures/
git commit -m "Relevés : ${1:-passage} — captures et empreintes"
git push
echo "Scellé. Horodatage tiers = date du push GitHub."
