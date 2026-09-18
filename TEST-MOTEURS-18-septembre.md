# Test des moteurs — 18 septembre 2026

**Premier relevé fait sous le mode opératoire version 2.** Il sert deux choses à la fois, et c'est
assumé : il tranche le second moteur de l'Express, et il rode le registre avant les 80 relevés
HertelTan. Mieux vaut découvrir une colonne mal pensée sur huit lignes que sur quatre-vingts.

---

## La question à laquelle ce test répond

Le mode opératoire v2 retient **ChatGPT déconnecté en chat temporaire** comme second moteur de
l'Express. Ce choix est écrit noir sur blanc comme **un défaut de travail, pas un fait établi** :
personne ne l'a vérifié. Perplexity a été écarté pour une raison démontrée — le mur de quota
anonyme du 17 septembre, cinq relevés perdus sur sept. Mais « Perplexity échoue » ne prouve pas
« ChatGPT tient ».

Deux choses à observer, et rien d'autre :

1. **Lequel tient quatre relevés d'affilée** sans mur de quota, sans demande de connexion.
2. **Lequel cite réellement ses sources** — des liens cliquables, pas une réponse sans attache.
   Un moteur qui répond sans citer ne sert à rien pour notre métier : c'est la citation qui montre
   au bureau d'où vient la réponse, et donc où il manque.

Ce n'est **pas** un test de visibilité. Aucun taux n'en sort. Huit relevés sur une intention ne
disent rien de la position de qui que ce soit.

---

## Le dispositif

**L'intention**, identique aux huit relevés, mot pour mot :

```
architecte pour une rénovation d'appartement à Genève
```

C'est `HT-01`, celle du jeu HertelTan v2, elle-même reprise du pilote du 17 septembre. Choisie
pour ça : elle a déjà deux points de comparaison. Les réponses obtenues ici ne comptent dans
aucun taux, mais elles s'ajoutent au dossier comme observations datées.

**Huit relevés, dans cet ordre :** quatre ChatGPT d'affilée, puis quatre Perplexity d'affilée.
D'affilée, sans pause — c'est le mur de quota qu'on cherche à voir, et une pause le masquerait.

| Moteur | Conditions exigées |
|---|---|
| ChatGPT | déconnecté, **chat temporaire**, fenêtre privée neuve à chaque passage |
| Perplexity | déconnecté, fenêtre privée neuve à chaque passage, aucun historique |

Même machine, même réseau, les huit. Bannière cookies traitée **avant** de poser la question.

---

## Les six gestes, pour chacun des huit

1. Coller l'intention, mot pour mot.
2. Attendre la réponse **complète**.
3. Copier l'URL entière dans le registre.
4. Copier le texte intégral dans un `.txt` portant le nom de la capture.
5. **Capture plein écran macOS** — l'horloge de la barre de menu dans la même image.
6. Clore la ligne du registre.

Captures et textes dans `captures/_test-moteurs/`. Nommage :

```
2026-09-18_14h07_chatgpt_herteltan_HT-01_p01.png
2026-09-18_14h07_chatgpt_herteltan_HT-01_p01.txt
```

---

## Ce qui se passe si ça casse

**Si un moteur bloque au passage 2 ou 3 :** on ne recommence pas, on ne change pas de fenêtre pour
contourner. On écrit la ligne avec `reponse_complete = non` et la cause dans `ecart`, et la série
s'arrête là pour ce moteur. **Le blocage est le résultat**, pas un incident à effacer — c'est très
exactement ce que le 17 septembre a appris.

**Si les deux tiennent :** alors le critère devient la citation des sources, et il faudra le
trancher sur ce qu'on lit, pas sur ce qu'on préfère.

**Si aucun ne tient :** l'Express redevient un dispositif à un seul moteur, Google AI Mode, et la
page de vente doit cesser d'en annoncer deux.

---

## Le registre

Les huit lignes sont préremplies dans `REGISTRE-releves-TEST-MOTEURS.csv` : tout ce qui est connu
d'avance y est déjà écrit — étude, intention, moteur, passage, langue, marché, état du compte.
Restent à remplir les colonnes d'observation. Une fois le test clos, les huit lignes sont
recopiées dans `REGISTRE-releves.csv` et le fichier de test disparaît.

**Ce qui est prérempli est une intention, pas une observation.** Si les conditions réelles
diffèrent — un chat temporaire qui ne s'active pas, une bannière impossible à fermer — c'est la
ligne qu'on corrige, pas la réalité.

---

## Après

Le résultat s'écrit ici même, sous ce titre, le jour du test. Il modifie la ligne « Moteurs
interrogés » du niveau 2 dans le mode opératoire, et la réserve ouverte en fin de fichier se
ferme. Puis commit, puis push.
