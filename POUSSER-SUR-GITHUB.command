#!/bin/bash
# Envoie les commits locaux sur GitHub.
# C'est le push, et lui seul, qui place l'horodatage chez un tiers.
# Double-cliquer pour lancer.

cd "$(dirname "$0")" || exit 1

echo ""
echo "=============================================="
echo "  PUSH GITHUB — horodatage tiers des relevés"
echo "=============================================="
echo ""
echo "Dépôt : $(git remote get-url origin 2>/dev/null)"
echo "Branche : $(git branch --show-current 2>/dev/null)"
echo ""
echo "Commits qui vont partir :"
git log --oneline origin/main..HEAD 2>/dev/null || git log --oneline -5
echo ""

printf "On envoie ? (o / n) : "
read -r OK
[ "$OK" = "o" ] || { echo "Annulé."; printf "Entrée pour fermer."; read -r _; exit 0; }

echo ""
git push origin main
CODE=$?

echo ""
if [ $CODE -eq 0 ]; then
  echo "✅ Envoyé. L'horodatage GitHub existe désormais."
  echo "   Vérifiable ici : https://github.com/mpdesignswiss-a11y/up2front-site/commits/main"
else
  echo "❌ Échec (code $CODE)."
  echo "   Si le message parle de 'Permission denied (publickey)', la clé SSH"
  echo "   de cette machine n'est pas reconnue par GitHub — dis-le moi."
fi
echo ""
printf "Appuie sur Entrée pour fermer."
read -r _
