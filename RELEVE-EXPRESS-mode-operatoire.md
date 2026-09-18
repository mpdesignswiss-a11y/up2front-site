# Mode opératoire — version 2

**Écrit le 18 septembre 2026. Remplace la version 1 à compter de cette date.**

La version 1 n'est pas supprimée : elle reste dans l'historique git, consultable, y compris les
deux lignes qui ont causé une panne. On ne réécrit pas le passé, on date les corrections.

> **Le nom du fichier ne change pas** (`RELEVE-EXPRESS-mode-operatoire.md`) alors que sa portée
> s'élargit aux trois niveaux. C'est délibéré : renommer casserait le fil de l'historique git, et
> ce fil est une partie de la preuve.

**Rien de ce qui suit ne s'applique rétroactivement.** Les relevés du 16 et du 17 septembre ont été
faits sous la version 1. Ils restent tels quels, avec leurs dix écarts déclarés. Un relevé fait
sous v1 et un relevé fait sous v2 ne se mélangent jamais dans un même comptage.

---

## Ce que la version 2 change, et pourquoi

Quatre corrections. Chacune a une cause datée, pas une préférence.

**1. La ligne Perplexity est retirée.** La version 1 imposait : *« Perplexity : fenêtre de
navigation privée, non authentifié, aucun historique. »* C'est la cause directe du blocage du
17 septembre — quota anonyme atteint, **cinq relevés sur sept perdus**, passage clos à 2/7. La
consigne était juste sur le principe (pas d'historique) et fausse en pratique (le moteur refuse
de servir). Voir « Conditions de session » plus bas.

**2. Le nombre de passages n'est plus fixé à quatre.** La version 1 annonçait *« Quatre passages :
Perplexity ×2, Google AI Mode ×2 »* alors que le dispositif réellement lancé le 17 en prévoyait
trois. Cette contradiction a survécu à deux relectures. Le nombre de passages dépend désormais du
niveau, et il est écrit une seule fois par niveau.

**3. Une intention par bureau, c'est trop peu pour un taux.** Le pilote a produit **2 observations
par cellule au maximum**. La table de référence du domaine classe 3 à 5 passages comme
« vérification exploratoire, trop peu pour un taux de visibilité défendable » ; 10 passages
donnent un pilote directionnel ; 20 à 30 un suivi de routine. Nous étions sous le plancher
exploratoire. Le produit payant passe à **8 intentions × 10 passages**.

**4. L'ordre du relevé est imposé.** L'écart n° 9 du 17 septembre : la capture a été prise avant
la copie de l'URL et du texte, et l'URL s'est retrouvée tronquée. Un ordre explicite est écrit
plus bas et ne se négocie pas.

---

## Les trois niveaux

| | **Étude** | **Express** | **Relevé 690** |
|---|---|---|---|
| Statut | pilote | aperçu | mesure |
| Intentions | 1, commune aux 7 bureaux | 1, la leur | 8 sur mesure |
| Moteurs interrogés | Google AI Mode + Perplexity | Google AI Mode + ChatGPT | Google AI Mode, ChatGPT, Perplexity |
| Taux calculé sur | aucun taux | aucun taux | Google AI Mode seul |
| Passages par intention | 2 | 2 | 10 |
| Fenêtres | 1 jour | 1 jour | 2 jours distincts, 5 + 5 |
| Total relevés | 14 | 4 | 80 |

Le mot **audit** est réservé au niveau 3. L'Express est un aperçu. Appeler audit une chose à
quatre relevés dévalue celle à quatre-vingts.

La ligne « Moteurs interrogés » de l'Express est vérifiée depuis le 18 septembre : ChatGPT
déconnecté encaisse quatre passages d'affilée. Au niveau 3, Perplexity reste dans la liste comme
**illustration ponctuelle, jamais comptée** — anonyme il bloque au troisième passage, authentifié
il répond à notre historique et non à celui d'un client genevois. Aucun taux ne sortira jamais
de lui.

---

## Les règles communes aux trois niveaux

**L'intention est fixée avant le premier passage et ne bouge plus.** Aller à la pêche jusqu'à
trouver la question où le bureau est absent, c'est fabriquer un problème. Si ça se sait une fois,
tout le positionnement tombe. Toute modification ouvre une version datée du jeu d'intentions, avec
la raison écrite, et les deux versions ne se mélangent pas dans les comptages.

**Session fraîche à chaque passage.** Pas seulement au début de la série : à **chaque** passage.
Une fenêtre privée rouverte, pas une fenêtre privée réutilisée.

**L'état du compte est noté à chaque ligne**, et montré dans l'image plutôt que déclaré :
l'avatar en haut à droite chez Google, la mention « Connectez-vous… » chez Perplexity.

**L'ordre du relevé est celui écrit plus bas.** Six gestes, toujours les mêmes.

**Si le résultat est flatteur, on le dit.** Un bureau premier aux dix passages, ça arrive. Le
message ne devient pas faux, il change d'angle. C'est un meilleur message, pas un moins bon.

**Aucune extrapolation.** Quatre relevés ne disent pas une position. Quatre-vingts non plus : ils
disent un taux, avec un intervalle, sur un moteur, sur deux jours.

**Le journal intégral est publié, y compris ce qui dessert la vente.** Le vrai soupçon n'est pas
« il a truqué l'image », c'est « il a fait vingt relevés et n'a montré que celui qui l'arrange ».
La seule défense qui tienne est le journal complet.

---

## Conditions de session, par moteur

**Google AI Mode.** Fenêtre de navigation privée, **déconnecté**, une fenêtre neuve par passage.
La bannière cookies se traite **avant** de poser la question — une bannière non traitée produit
une réponse tronquée, et la réponse tronquée n'est pas la même donnée. L'état déconnecté doit
être visible dans la capture.

**ChatGPT.** Déconnecté, en **chat temporaire**. Session propre, aucun historique, aucune mémoire.
C'est cette propreté qui le fait préférer à un Perplexity authentifié.

**Perplexity.** **Ne pas l'utiliser en anonyme pour une série.** Le quota tombe après quelques
questions et la série meurt en cours de route — c'est ce qui s'est produit le 17 septembre. Deux
usages restent permis : un relevé isolé, ou une illustration ponctuelle au niveau 3, jamais
comptée. Un compte authentifié règle le quota mais personnalise les réponses selon l'historique :
on mesurerait alors ce que Perplexity répond **à nous**, pas à un client genevois. Disqualifiant
pour une mesure, acceptable pour une illustration déclarée comme telle.

**Même machine, même réseau, pour toute une série.** Sinon la comparaison ne veut rien dire.

**Réserve levée le 18 septembre 2026.** Le choix de ChatGPT comme second moteur de l'Express
était un défaut de travail ; il est désormais mesuré. Huit tentatives prévues sur la même
intention, en navigation privée Chrome, déconnecté des deux côtés : **ChatGPT a tenu ses quatre
passages d'affilée sans mur** et produit une URL de conversation stable à chaque fois ;
**Perplexity anonyme a été bloqué par un mur d'inscription au troisième passage**, après deux
réponses complètes. Les deux citent leurs sources avec des liens — le critère de citation ne les
sépare pas, c'est le quota qui tranche. Détail, captures et écarts déclarés dans
`TEST-MOTEURS-18-septembre.md`.

Portée : une intention, en français, marché Genève, une machine, un réseau, un après-midi. Cela
établit qu'un opérateur peut enchaîner quatre relevés ChatGPT déconnecté sans être arrêté. Cela
n'établit pas que ça tiendra à quarante ni dans six mois. Le jour où un mur tombe sur ChatGPT
aussi, il s'écrit ici.

---

## L'ordre du relevé — six gestes, jamais dans un autre ordre

1. Coller l'intention, mot pour mot, telle qu'elle est écrite dans le jeu verrouillé.
2. Attendre que la réponse soit **complète** — pas de capture en cours de génération.
3. **Copier l'URL entière** dans le registre. Entière : sur Google AI Mode elle contient la
   question en clair (`?q=…&udm=50`), c'est elle qu'on donne au prospect pour qu'il rejoue.
4. **Copier le texte intégral** de la réponse dans un `.txt` portant le nom de la capture.
5. **Capture plein écran macOS** — pas capture de navigateur : l'horloge de la barre de menu doit
   se trouver dans la même image que la réponse.
6. Écrire la ligne du registre et la clore.

Les gestes 3 et 4 **avant** le geste 5. C'est l'écart n° 9, et il ne se reproduit pas.

**Sur ChatGPT déconnecté, le geste 4 n'a aucun rattrapage.** Vérifié le 18 septembre au soir :
l'URL `chatgpt.com/uc/…` qu'on copie au geste 3 **ne rouvre pas la conversation** — elle renvoie
sur une page d'accueil vide. Le texte n'est donc récupérable qu'à l'écran, pendant le passage. Si
la fenêtre se ferme avant le `.txt`, la réponse est perdue et la capture devient le seul état qui
en reste. Perplexity et Google AI Mode rouvrent, eux : là, le geste 4 se rattrape. Sur ChatGPT,
non — et c'est le moteur où il faut donc être le plus discipliné.

Nommage des captures :

```
2026-09-22_09h14_googleaimode_herteltan_HT-01_p03.png
```

soit : date, heure, moteur, bureau, identifiant d'intention, numéro de passage. Un dossier par
bureau. Ces fichiers ne s'effacent pas.

---

## Le registre de collecte

Créé le 18 septembre 2026, vide : `REGISTRE-releves.csv`. **Une ligne par relevé.** Pas une ligne
par intention, pas une ligne par journée : par relevé. Un passage qui n'a pas eu lieu s'écrit
quand même, avec sa cause en colonne `ecart` — c'est ainsi que le 17 septembre aurait dû se tenir.

Les colonnes, et ce qu'elles servent à défendre :

| Colonne | Nom de référence | Ce qu'elle sert à défendre |
|---|---|---|
| `etude_id` | `study_id` | Deux études ne se mélangent jamais dans un comptage. |
| `bureau` | — | Le sujet mesuré. |
| `intention_id` / `intention_version` | `prompt_id` / `prompt_version` | Une intention reformulée devient une **autre** intention : nouvelle version, comptage séparé. |
| `intention_texte` | `prompt_text` | Le texte exact, mot pour mot. Un prospect doit pouvoir le recoller. |
| `passage_id` | `run_id` | Le numéro de passage, 1 à 10. |
| `fenetre` | — | `J1` ou `J2`. C'est elle qui permet de publier le taux par journée **à côté** du taux groupé. |
| `horodatage_local` / `horodatage_utc` | `timestamp_utc` | L'heure locale est celle de la capture ; l'UTC est celle qui se compare. |
| `moteur` / `modele` / `mode` | `platform` / `model` / `mode` | `google` / `aimode` n'est pas `google` / `web`. Deux modes, deux populations. |
| `marche` / `langue` | `market` / `language` | `CH-GE` / `fr`. Un relevé en anglais ne compte pas avec un relevé en français. |
| `etat_du_compte` | `account_state` | `deconnecte`, `temporaire`, `connecte`. La colonne qui a tué la série Perplexity. |
| `session_neuve` | `fresh_session` | `oui` / `non`. À chaque passage, pas seulement au début de la série. |
| `banniere_traitee` | — | Une bannière non traitée produit une réponse tronquée. Ce n'est pas la même donnée. |
| `reponse_complete` | — | `oui` / `non`. Une génération interrompue ne compte pas. |
| `fichier_reponse` | `response_text` | **Écart assumé** — voir ci-dessous. |
| `bureau_mentionne` / `bureau_recommande` | `brand_mentioned` / `brand_recommended` | Être nommé et être recommandé sont deux choses. Le taux vendu porte sur la mention. |
| `rang_mention` | — | Rang dans la réponse, ou vide. Jamais agrégé sans le dire. |
| `citations_brutes` / `citations_normalisees` | `citation_urls_raw` / `citation_urls_normalized` | Brut = ce que l'écran affiche. Normalisé = domaine racine. On compte sur le normalisé, on prouve sur le brut. |
| `domaine_cible_cite` | `target_domain_cited` | Le site du bureau, cité ou non. C'est le chiffre qui fait mal, donc c'est celui qui vend. |
| `capture` | `capture_reference` | Le nom de fichier exact. Une ligne sans capture n'est pas un relevé. |
| `observateur` | — | Qui a tenu la main. |
| `ecart` | — | Vide si rien. Rempli, toujours, si quelque chose. |

**Écart assumé sur `response_text`.** La colonne annoncée contenait le texte intégral de la
réponse. Le registre porte à la place `fichier_reponse`, qui pointe vers un `.txt` posé à côté de
la capture et portant le même nom. Cause : le registre se remplit à la main, et une réponse de
deux mille signes dans une cellule rend la feuille illisible. Le texte reste conservé **mot pour
mot** ; il change seulement de fichier. Rien ne se perd, mais l'écart est écrit.

---

## Niveau 3 — le Relevé 690, protocole complet

**Les intentions.** Huit, formulées comme un client les taperait, **chacune adossée à une page
publique du site du bureau**. Une intention qui ne correspond à aucune de leurs pages est un
procès d'intention. Aucune ne contient le nom du bureau : une intention de marque mesure la
notoriété, pas la visibilité commerciale. Le jeu est verrouillé avant le premier passage et daté.
Modèle de référence : `ETUDE-HERTELTAN-intentions.md`.

**Le moteur compté.** Google AI Mode, seul. Un pourcentage qui mélange Google et Perplexity ne
veut rien dire : ce sont deux populations différentes. ChatGPT et Perplexity sont interrogés une
fois chacun, cités dans le dossier comme illustration, et **n'entrent dans aucun comptage**.

**Les passages.** Dix par intention, répartis **5 + 5 sur deux jours distincts**. Pas dix d'affilée :
un taux mesuré sur une seule journée ne distingue pas l'instabilité du moteur d'un accident de
journée. Total : **80 relevés comptés**.

**Le comptage.** Trois règles.

*On rapporte des comptes, pas des verdicts.* « 3 mentions sur 10 passages » se vérifie ; « vous
êtes absent » est une conclusion que les données ne portent pas.

*On rapporte un intervalle de Wilson, jamais un intervalle de Wald.* Sur de petits effectifs et
des taux proches de 0 ou de 1, Wald produit des bornes absurdes. Deux repères à connaître par
cœur, parce qu'ils désamorcent les deux malentendus les plus fréquents :

| Observé | Taux | Intervalle de Wilson à 95 % |
|---|---|---|
| 3 mentions sur 10 | 30 % | **10,8 % – 60,3 %** |
| 0 mention sur 10 | 0 % | **0 % – 27,8 %** |

La seconde ligne est la plus importante : **zéro sur dix ne veut pas dire zéro.** Ça veut dire
« au plus 28 %, et probablement bien moins ». Un dossier qui écrit « 0 % » sans son intervalle
affirme plus que ce qu'il a mesuré.

*On rapporte le taux par jour à côté du taux global.* Un taux global de 50 % peut recouvrir
0 % un jour et 100 % l'autre. Les deux sont dans le dossier. Et parce que les dix passages d'une
même intention ne sont pas indépendants entre eux, le taux global sur les 80 relevés est donné
avec sa réserve écrite : traiter chaque passage comme indépendant sous-estime l'incertitude.

**Le délai annoncé au client.** Cinq jours ouvrés — imposé par les deux fenêtres, pas par la
charge de travail.

**Ce qu'on ne promet pas.** Aucun résultat. Tant que la remesure HertelTan à 90 jours n'est pas
faite, nous savons **ce que le moteur cite**, nous ne savons pas que corriger les annuaires change
ce que le moteur répond. Vendre la causalité avant de l'avoir mesurée, c'est exactement ce que
notre propre protocole interdit.

---

## Niveau 2 — l'Express, protocole complet

Vingt minutes par bureau. Il ne se vend pas et ne se livre pas : il sert à écrire les trois
phrases du deuxième paragraphe du message d'approche.

Une intention, la leur, tirée de leur site. Deux moteurs : Google AI Mode et ChatGPT déconnecté.
Deux passages par moteur, **au moins trente minutes d'intervalle** entre le premier et le second
d'un même moteur — c'est l'intervalle qui fait apparaître la contradiction, et la contradiction
est tout l'intérêt de l'Express. Quatre passages enchaînés en cinq minutes ne montrent rien.

En pratique : enchaîner les sept bureaux en premier passage, puis les sept en second. L'intervalle
vient tout seul.

**Aucun taux, jamais.** Le constat fait trois phrases : ce qui a été observé, à quelle heure, sur
quel moteur, et ce qui a changé entre deux passages. Rien d'autre.

Ce que l'Express montre est une contradiction, pas un chiffre. Le 17 septembre en fournit le
modèle : à 11h43 Google nommait meier + associés sur `architecte pour une rénovation d'appartement
à Genève` ; trente-deux minutes plus tard, Perplexity ne le nommait pas sur la même intention.
Deux moteurs, aucun taux, un fait solide.

---

## Niveau 1 — l'Étude, close

La série des 16 et 17 septembre est un **pilote** au sens du domaine : une passe exploratoire dont
le travail est de révéler la variabilité, les contraintes et les défauts de méthode — pas de
produire un taux. Elle a rempli ce rôle et elle est close.

Ce qu'elle a révélé : l'instabilité de meier + associés entre deux moteurs à trente-deux minutes
d'écart ; le mur de quota de Perplexity en anonyme ; le défaut d'ordre de capture ; et le fait que
les sources citées par Google pour ces intentions sont `local.ch`, `Neho`, `architecte-comparatif.ch`,
`Petit Futé` et `architectegeneve.com` — presque jamais les sites des bureaux eux-mêmes.

Elle ne produit aucun taux et n'en produira pas. Ses dix écarts sont déclarés dans
`RELEVE-EXPRESS-feuille-17-septembre.md` et y restent.

**Sa version publique doit être anonymisée** — « un bureau d'architecture genevois de onze avis » —
tant que les bureaux n'ont pas donné d'accord écrit, et tant que les réserves LCD ne sont pas
levées par un avocat. Ces réserves ne sont pas levées par le volume de preuve.

> **Correction du 18 septembre.** Ce paragraphe disait « art. 3 al. 1 let. o, publicité
> comparative et dénigrement ». **C'est faux, et c'est une erreur de Claude.** Vérifié auprès de
> l'OFCOM : la let. o vise le pollupostage, c'est-à-dire l'envoi **en masse** de publicité par
> voie de télécommunication sans consentement préalable (opt-in, en vigueur depuis le
> 1ᵉʳ avril 2007). Elle ne parle ni de comparaison ni de dénigrement.
> Les deux réserves sont distinctes et se traitent séparément :
> — **let. o : la méthode d'envoi.** Elle concerne le démarchage par e-mail, pas le contenu.
> — **let. a (dénigrement) et let. e (comparaison inexacte ou fallacieuse) : le contenu.**
> C'est là que se joue le fait de nommer, comparer ou classer des bureaux tiers.
> Aucun des deux points n'est tranché. Ni Claude ni Max ne sont juristes ; ce qui précède
> situe les articles, il ne dit pas ce qui est permis.

---

## Le scellement

Après chaque passage, dans l'ordre :

1. SHA-256 de chaque capture et de chaque texte, consignés dans `captures/manifeste.csv` — une
   ligne par relevé : date, heure locale, moteur, bureau, identifiant et texte exact de
   l'intention, URL, état de session, empreinte de l'image, empreinte du texte.
2. `git add captures/ && git commit && git push`.

Les commits git forment une chaîne de hachages : une capture modifiée après coup casse la chaîne,
et cela se vérifie en une commande. Le push place en outre l'horodatage **chez un tiers**, côté
GitHub. Dix secondes par passage, gratuit, et très au-dessus de ce que fournit la concurrence.

**Le push n'est pas optionnel.** Sans lui, l'horodatage reste sur la machine de celui qui affirme,
et la troisième jambe de la preuve manque.

---

## L'asymétrie qui joue pour nous

Ce qui est vendu n'est pas « votre position est X », c'est « votre position est instable ». Donc
un prospect qui rejoue la question et trouve autre chose que la capture **confirme la thèse au lieu
de la démonter**. Le seul scénario destructeur serait qu'il rejoue et retrouve, invariablement, un
résultat flatteur qu'on aurait prétendu absent — c'est-à-dire le scénario où l'on a triché. Tant
qu'on ne triche pas, la preuve se défend seule.

Il n'existe pas de dispositif fiable à 100 %, et prétendre le contraire serait exactement ce que
nous reprochons aux vendeurs de « score IA ». Ce protocole ne vise pas la certitude : il vise à
rendre chaque affirmation vérifiable par le destinataire lui-même, sans avoir à nous croire.

Le vrai 100 %, quand il est demandé : le rejeu devant témoin. « Prenons dix minutes en visio, je
partage mon écran, on repose la question ensemble, en direct. » Un problème de preuve vient de se
transformer en rendez-vous. Le constat d'huissier existe et n'a aucun sens ici : plusieurs
centaines de francs par constat, sur une vente à 690.

---

## Les captures ne partent pas en pièce jointe

Un premier e-mail à un inconnu avec quatre images attachées, c'est la combinaison la plus sûre
pour finir en indésirables, et le destinataire qui ne vous connaît pas n'ouvrira pas les fichiers
de toute façon.

Le constat va donc **en texte** dans le corps du message, avec les heures. Les captures sont
mentionnées et proposées : « je vous les envoie si vous les voulez. » Deux avantages — la
délivrabilité, et le fait que demander les captures est une réponse à coût nul, beaucoup plus
facile à obtenir qu'un « oui je veux acheter ». Une demande de captures est un prospect en
conversation.

---

## Ce qui reste ouvert au 18 septembre 2026

- ~~Le registre de collecte n'existe pas encore.~~ **Fait le 18 septembre :** `REGISTRE-releves.csv`,
  vide, avec un écart déclaré sur `response_text`. Le test des moteurs, qui servait aussi à roder
  le registre, a fait apparaître une colonne manquante : l'URL de la réponse n'avait nulle part
  où aller. **Ajoutée le 18 septembre** sous le nom `url_reponse`, après `fichier_reponse` —
  vingt-neuf colonnes. C'est exactement ce qu'on cherchait à découvrir sur huit lignes plutôt que
  sur quatre-vingts.
- ~~Le test ChatGPT / Perplexity n'est pas fait.~~ **Fait le 18 septembre.** ChatGPT déconnecté
  tient quatre passages, Perplexity anonyme bloque au troisième. Le second moteur de l'Express
  n'est plus un défaut de travail : voir `TEST-MOTEURS-18-septembre.md`.
- **Otterly n'est pas ouvert.** Tant qu'il ne l'est pas, les 80 relevés du niveau 3 coûtent environ
  sept heures à la main au lieu d'une. Ce qui s'automatise est le comptage ; la capture horodatée
  reste manuelle, parce que c'est elle le produit.
- **La réserve LCD** conditionne la version publique de l'étude comme le message d'approche.
- **La causalité n'est pas établie.** Elle le sera, ou non, par la remesure HertelTan à 90 jours.
