# Otterly.AI — premier retour sur HertelTan, 18 septembre 2026

Compte ouvert le 18 septembre en début d'après-midi, essai gratuit. Rapport généré à 14h28,
export des quinze questions à 14h29. Les deux pièces sont au dépôt, sans retouche, sous
`captures/_otterly/`, avec leurs empreintes sha256 et un `_PROVENANCE.txt` qui dit ce qu'elles
valent.

Marque suivie : **`herteltan.ch`**.

> **Réserve levée le 18 septembre.** Nos notes avaient d'abord écrit `hertelan.ch`, par erreur de
> saisie ; le PDF d'Otterly écrit `herteltan.ch` en en-tête de neuf de ses onze pages. Max a
> ouvert https://herteltan.ch et confirmé cette forme. C'est elle qui fait foi partout.

**Toute phrase de ce fichier doit pouvoir être recalculée depuis le CSV.** En cas de divergence
entre le CSV et le PDF, c'est le CSV qui fait foi — il est vérifiable ligne à ligne, le PDF non.

---

## Ce que cette mesure n'est pas

Ce ne sont pas nos relevés. Nous n'avons pas vu les réponses des moteurs, pas capturé d'écran,
pas horodaté de passage. Nous avons commandé quinze questions à un outil tiers et lu ce qu'il a
renvoyé. **C'est une source, pas une observation de terrain, et les deux ne se mélangent jamais
dans un même comptage.**

Trois limites de portée, à dire avant tout chiffre :

La portée est **le pays**, `ch`. Pas le canton de Genève. Otterly ne descend pas sous le pays, et
nos relevés manuels, eux, sont `CH-GE`. Un chiffre Otterly et un chiffre du registre ne
s'additionnent pas et ne se comparent pas directement.

La fenêtre affichée est « Last 14 days », mais le compte a été créé le jour même : **le graphe ne
porte qu'un seul point.** Il n'y a pas de tendance. Il y a une photographie, prise une fois.

Les moteurs sont agrégés sous « All Engines », sans détail par moteur dans l'export. On ne peut
donc pas savoir lequel nomme et lequel ignore.

---

## Les deux séries, et pourquoi elles ne s'additionnent pas

Otterly refuse de valider un suivi en dessous de quinze questions — bouton « Next » inactif à
huit, vérifié à 14h22. Les huit intentions verrouillées le matin sont donc accompagnées de sept
questions écrites sur place pour débloquer le formulaire (série OT-01 à OT-07, détaillée dans
`ETUDE-HERTELTAN-intentions.md`).

Les huit sortent des pages d'expertise du bureau. Les sept sortent d'une contrainte logicielle.
**Un taux se donne sur les huit, ou sur les sept, jamais sur quinze.**

| | mentions | questions touchées | domaine cité |
|---|---|---|---|
| **Série HT** (huit intentions verrouillées) | 2 | 2 / 8 | 2 |
| **Série OT** (sept questions de remplissage) | 5 | 4 / 7 | 3 |
| Total export | 7 | 6 / 15 | 5 |

Le détail, question par question :

| Code | Question | Mentions | Rang | Domaine cité | Citations |
|---|---|---|---|---|---|
| HT-01 | architecte pour une rénovation d'appartement à Genève | 1 | 4 | 0 | 26 |
| HT-02 | qui contacter pour transformer un appartement à Genève | 0 | — | 0 | 18 |
| HT-03 | architecte pour rénover une villa à Genève | 0 | — | 0 | 33 |
| HT-06 | architecte rénovation énergétique Genève | 1 | 2 | 2 | 45 |
| HT-09 | architecte pour aménager des bureaux à Genève | 0 | — | 0 | 25 |
| HT-12 | architecte d'intérieur à Genève pour un appartement haut de gamme | 0 | — | 0 | 20 |
| HT-14 | expertise immobilière avant achat à Genève | 0 | — | 0 | 25 |
| HT-18 | combien coûte un architecte à Genève pour une rénovation | 0 | — | 0 | 26 |
| OT-01 | architecte pour aménager un restaurant à Genève | 1 | 1 | 1 | 18 |
| OT-02 | architecte pour l'aménagement d'un commerce à Genève | 1 | 3 | 1 | 24 |
| OT-03 | meilleur architecte à Genève *(intention exclue — voir l'étude)* | 1 | 1 | 0 | 34 |
| OT-04 | architecte d'intérieur à Genève | 0 | — | 0 | 10 |
| OT-05 | bureau d'architectes à Genève pour un immeuble de logements | 2 | 1 | 1 | 24 |
| OT-06 | architecte pour rénover une cuisine et une salle de bain à Genève | 0 | — | 0 | 22 |
| OT-07 | cabinet d'architecture à Genève pour un projet de rénovation | 0 | — | 0 | 18 |

**Total citations, toutes questions confondues : 368.**

### Ce que ce tableau dit, et qui n'est pas confortable

Le bureau se montre mieux sur les questions écrites pour remplir un formulaire que sur celles
tirées de ses propres pages d'expertise : **cinq mentions sur quatre questions de remplissage,
deux mentions sur deux questions verrouillées.** Formulé autrement : HertelTan apparaît sur des
formulations génériques — un immeuble de logements, un restaurant, un commerce — et disparaît sur
six de ses huit spécialités déclarées.

La seule exception est `architecte rénovation énergétique Genève`, la seule question de la série
verrouillée où le domaine du bureau est effectivement cité, deux fois. C'est aussi la question la
plus disputée du lot : 45 citations, le maximum des quinze. Et c'est la seule ligne de l'export
où la colonne `Brand Sentiment` porte une valeur positive, +50 — attention, cela ne veut pas dire
que c'est le seul sentiment positif du rapport : le PDF en attribue à neuf marques, dont +25 à
HertelTan globalement et +100 à Marine Terrien. Les deux pièces mesurent le sentiment à deux
échelles différentes, par question et par marque.

Six des huit intentions verrouillées ne rapportent rien du tout : transformation d'appartement,
villa, bureaux, intérieur haut de gamme, expertise immobilière, question de prix.

---

## Nommé n'est pas cité

Otterly distingue deux colonnes que tout le monde confond, et la confusion est commode :

**« Your brand mentioned »** — le nom du bureau apparaît dans la réponse. Sept fois sur l'export.

**« Your domain cited »** — le site du bureau figure parmi les sources auxquelles le moteur
renvoie. **Cinq fois, sur 368 citations.**

La seconde colonne est la seule qui mesure ce que l'offre vend. Être nommé dans un paragraphe
sans que le site soit la source, c'est être cité de mémoire par le moteur ; le clic, lui, part
ailleurs. Aucun chiffre montré à un prospect ne doit reposer sur « mentioned » seul.

---

## Deux questions que personne n'occupe

Deux des quinze questions produisent des citations en quantité et **ne nomment aucune marque du
panel, pas une seule** :

`combien coûte un architecte à Genève pour une rénovation` — 26 citations, zéro marque nommée.

`expertise immobilière avant achat à Genève` — 25 citations, zéro marque nommée.

Sur ces deux intentions, le moteur répond en citant des sources qui ne sont les pages d'aucun
bureau d'architectes du panel. C'est le constat le plus exploitable du rapport, et il ne se voit
qu'en lisant les zéros. Il ne se transforme pas en promesse : il dit qu'une place est vide, pas
qu'elle est prenable, encore moins par nous.

---

## Part de voix, recalculée

Sur le panel suivi, les 60 mentions de l'export se répartissent ainsi :

| Marque | Mentions | Part |
|---|---|---|
| Kara Architecte | 17 | 28.3 % |
| Ecotonos | 9 | 15.0 % |
| Marine Terrien | 7 | 11.7 % |
| **HertelTan** | **7** | **11.7 %** |
| CM Studio | 6 | 10.0 % |
| Alan Strappazzon | 4 | 6.7 % |
| Cécile Morel | 4 | 6.7 % |
| KELLER Architectes | 3 | 5.0 % |
| Mahaut Design | 1 | 1.7 % |
| RK Interiors | 1 | 1.7 % |
| maage | 1 | 1.7 % |

Ce classement ne vaut que pour ce panel de marques, choisi par nous, sur ces quinze questions,
choisies par nous, un jour donné. Changer le panel change le classement. Ce n'est pas un
classement du marché genevois.

---

## Trois pièges dans les chiffres d'Otterly

**« Average brand position : 1.27 » ne veut pas dire « classé 1,27 ».** C'est la position moyenne
*à l'intérieur des réponses où la marque est nommée* — quand on le nomme, on le nomme tôt. Sur
l'ensemble du panel, Otterly range le bureau **3ᵉ sur 10** et le classe en **« Niche »**
(couverture 14 %, « likelihood to buy » 87 %). Un prospect à qui l'on montre 1,27 sans cette
phrase est trompé. C'est le chiffre le plus flatteur du rapport et le plus facile à mal lire.

**Deux rangs coexistent, et ce fichier les porte tous les deux.** Otterly classe HertelTan 3ᵉ ;
notre part de voix recalculée ci-dessus le place 4ᵉ, à égalité de mentions avec Marine Terrien
(7 chacun). L'écart vient de l'ordre d'affichage d'Otterly, qui départage deux ex æquo sans dire
comment. **Aucun des deux rangs n'est employé seul dans un écrit externe** : sept mentions
ex æquo, voilà le fait ; le rang est une mise en forme.

**« Brand coverage » désigne deux quantités différentes selon l'écran.** Dans le tableau de
classement, c'est 14 % pour HertelTan — le recalcul retrouve exactement un dénominateur de 51
(17 → 33 %, 9 → 18 %, 3 → 5,9 %, 1 → 2 %), et **nous ne savons pas ce que vaut ce 51** ; ce n'est
ni le nombre de questions, ni le total des mentions. Dans l'export par question, le même mot ne
prend que les valeurs 0, 25 et 50 % — ce qui *ressemble* à une fraction de moteurs sur quatre,
mais **Otterly ne le documente nulle part et nous ne le déduisons pas**. Même mot, deux
quantités, aucune des deux définie.

**La part de voix d'Otterly ignore une marque.** L'outil annonce 12 % pour HertelTan : c'est
7 sur 59, le total des dix marques classées. Notre recalcul donne 11,7 %, soit 7 sur 60, parce
que nous comptons aussi RK Interiors — présent dans l'index de visibilité mais absent du top 10
des mentions. L'écart est minuscule ; il est signalé parce que les deux bases circulent.

**« Intent volume : 1 - Very low » sur 13 des 15 questions.** Personne ne mesure sérieusement le
volume des questions posées à un moteur de réponse — ni Otterly, ni nous, ni quiconque
aujourd'hui. Ce chiffre ne fonde ni la lecture pessimiste (« ces questions n'intéressent
personne ») ni l'optimiste (« l'outil sous-estime »). Nous le signalons avant qu'un prospect ne
le trouve, et nous n'en tirons rien.

---

## Qui fournit les sources : des annuaires, pas des bureaux

Otterly classe les domaines cités par « domain coverage ». **Ce ne sont pas des parts des 368
citations** : les quinze valeurs listées totalisent 158 %. Ce que mesure exactement ce
pourcentage n'est pas documenté, et nous ne le déduisons pas. Il n'est utilisé ici que pour son
ordre.

| Domaine | Couverture | Ce que c'est |
|---|---|---|
| local.ch | 17 % | annuaire |
| kara-architecte.ch | 17 % | bureau d'architectes |
| corpus.ch | 15 % | annuaire / plateforme |
| architectegeneve.com | 13 % | plateforme d'apport d'affaires |
| hilo-architectes.ch | 12 % | bureau, non identifié au dossier |
| kellerarchitectes.com | 12 % | bureau |
| pierreambrosetti.ch | 12 % | non identifié au dossier |
| … | | |
| **herteltan.ch** | **7 %** | **14ᵉ des quinze domaines listés, ex æquo à 7 % avec `architectes.ch`, `ranq.ch` et `csdk.ch`** |

Et dans le classement des URL les plus citées — les dix premières — **`herteltan.ch` ne figure
pas.** Les deux premières places vont à `corpus.ch/fr` (9 citations) et à une page de rénovation
de `cm-studio.ch` (6). Une page, pas un site : la granularité de la réponse, c'est l'URL.

**En tête, à égalité, un annuaire et un bureau** — `local.ch` et `kara-architecte.ch`, 17 %
chacun. Viennent ensuite `corpus.ch` (15 %) et `architectegeneve.com` (13 %). Autrement dit, trois
des quatre premières sources ne sont pas des bureaux d'architectes mais des annuaires et des
plateformes d'apport d'affaires, qui se placent entre le moteur et le bureau. Voilà la forme
réelle du problème, et elle ne se lit ni dans le nombre de mentions ni dans la position moyenne.

### Le « Brand 74 % » du camembert ne veut rien dire

L'outil répartit les 368 citations en catégories et annonce **« Brand 74 % »**. Pris au mot, cela
signifierait que 74 % des sources citées sont le site de HertelTan. Or `herteltan.ch` est cité
**5 fois sur 368, soit 1,4 %**.

L'explication est dans le tableau : Otterly étiquette « Brand » des domaines qui n'ont rien à
voir avec la marque suivie — `local.ch`, `corpus.ch`, `hilo-architectes.ch`,
`kellerarchitectes.com`, `ranq.ch`, `csdk.ch` — et étiquette « Competitor » `kara-architecte.ch`,
`cm-studio.ch`, `cecilemorel.ch`. La catégorie est incohérente, et l'incohérence penche du côté
flatteur.

**Ce chiffre est inutilisable et ne sera cité nulle part.** Il est consigné ici pour une seule
raison : c'est exactement le genre de nombre qu'un vendeur de GEO met en première page d'un
rapport client.

---

## Le tableau de bord et l'export se recoupent — et ma première lecture était fausse

Vérification faite en extrayant le texte du PDF et en le confrontant au recalcul du CSV :

| | Export CSV | Rapport PDF |
|---|---|---|
| Mentions HertelTan | 7 | 7 |
| Citations totales | 368 | 368 |
| Kara Architecte | 17 | 17 |
| Ecotonos | 9 | 9 |
| Marine Terrien | 7 | 7 |
| CM Studio | 6 | 6 |
| Alan Strappazzon | 4 | 4 |
| Cécile Morel | 4 | 4 |
| KELLER Architectes | 3 | 3 |
| Mahaut Design, maage | 1 | 1 |
| RK Interiors | 1 | *absent du tableau* |

**Les deux pièces se recoupent sur tous les décomptes vérifiables.** Une seule marque manque au
tableau du PDF : RK Interiors, 1 mention au CSV, écartée parce que le classement s'arrête aux dix
premières. Ce n'est pas un écart de mesure, c'est une troncature — c'est elle qui explique les
deux bases de part de voix, 59 chez Otterly et 60 chez nous.

J'ai d'abord écrit l'inverse. J'ai consigné, dans `_PROVENANCE.txt` et ici, un tableau d'écarts
— 7 contre 5 mentions, 368 contre 333 citations — annoncé comme « vérifié par recalcul ».
**Il ne l'était pas.** Ces chiffres venaient d'une lecture à l'écran du tableau de bord en direct
à 14h26 ; le PDF, lui, n'avait pas été ouvert. Une fois son texte extrait, aucun écart ne
subsiste.

On ne saura pas si le tableau de bord en direct différait réellement du PDF généré deux minutes
plus tard, ou si ma lecture d'écran était simplement fausse. **La seconde hypothèse est la plus
probable, et c'est celle qu'on retient faute de pièce** : le tableau de bord en direct n'est
archivé nulle part, il n'est pas revérifiable, il ne peut donc rien prouver — ni dans un sens ni
dans l'autre.

Deux autres chiffres issus de cette même lecture d'écran étaient faux au même titre : la position
moyenne annoncée à 1,33 — le PDF dit **1,27** — et un « 5 mentions sur 51 », dont seul le
dénominateur tient : le numérateur est 7, pas 5.

**La règle qui en sort : aucun chiffre lu à l'écran n'entre dans un écrit sans être retrouvé dans
une pièce archivée.** C'est la troisième fois en une journée qu'une lecture d'écran me fait
écrire un faux — après l'erreur sur le verrou des quinze questions, puis celle sur HT-01
ci-dessous. Le point commun des trois est identique : j'ai regardé au lieu de recalculer.

---

## Ma correction : HT-01 contredit le relevé du matin

Le 18 septembre au matin, le relevé manuel sur `architecte pour une rénovation d'appartement à
Genève` donnait HertelTan **absent sur 9 passages sur 9**. L'après-midi, Otterly donne la même
question avec **1 mention, rang 4**.

J'ai d'abord annoncé le contraire — j'ai écrit qu'Otterly « confirmait le relevé manuel », après
avoir lu une liste tronquée à l'écran au lieu du CSV. C'était faux, et sur la question la plus
importante des huit. Le CSV, lui, est sans ambiguïté.

**Les deux méthodes ne convergent pas sur la question cœur : elles se contredisent.** Et la
contradiction est cohérente avec ce qui a été observé le 16 septembre — *« le mode de réponse
varie dans le temps, sur la même question, au même compte, en deux heures »*. Ici s'ajoutent une
autre échelle géographique (pays contre canton), un autre agrégat de moteurs et un autre
opérateur. Quatre raisons de diverger, aucune manière de savoir laquelle joue.

La conséquence pratique est nette : **aucun chiffre d'absence ne sera présenté à un prospect
comme un fait stable.** Ce qui est stable, à ce stade, c'est la variabilité elle-même.

---

## L'instabilité d'Otterly est elle-même un fait mesuré

À 13h54 puis à 14h16, sur la même marque, le même compte et sans qu'aucun paramètre ait été
touché, l'outil a proposé **deux listes de concurrents matériellement différentes** : quatre noms
sur neuf ont survécu, et un domaine s'est corrigé tout seul de `.com` en `.ch`. Vingt-deux
minutes d'écart.

Cette instabilité n'est pas un défaut à cacher dans un argumentaire — c'est le phénomène même que
l'offre prétend traiter, observé sur l'outil de mesure au lieu du moteur mesuré.

Rappel de fond : les concurrents suggérés par Otterly sont des **pairs de positionnement**,
dérivés de ce qu'un site dit de lui-même. Notre registre, lui, construit des **pairs de
citation** : qui occupe effectivement la réponse sur une intention d'achat. Les deux listes n'ont
aucune raison de coïncider, et elles ne coïncident pas.

---

## Ce qui est décidé, et ce qui ne l'est pas

**Décidé.** Les quinze questions restent en place, intouchées. La série a besoin d'une semaine
pour produire un second point ; sans second point il n'y a pas de tendance, et sans tendance
l'outil ne sert à rien d'autre qu'à cette photographie.

**Décidé.** Les relevés manuels `CH-GE` continuent en parallèle, sans fusion. Otterly ne les
remplace pas : il ne descend pas sous le pays.

**Pas décidé.** Rien de ce fichier ne part vers HertelTan. Deux réserves LCD distinctes restent
ouvertes : la **let. o** sur la méthode (pollupostage, envoi en masse sans consentement) et les
**let. a / let. e** sur le contenu (dénigrement, comparaison inexacte ou fallacieuse). La
première conditionne l'e-mail d'approche, la seconde la version publique. Elles se lèvent
séparément, par un avocat.

**Reporté.** Six domaines à fort poids dans les sources citées ne sont identifiés par personne au
dossier : `hilo-architectes.ch` (12 %), `pierreambrosetti.ch` (12 %), `classorga.ch` (8 %),
`nessell.ch` (8 %), `csdk.ch` (7 %), `ranq.ch` (7 %). C'est une piste de prospection, pas une
conclusion, et elle attend.

**À vérifier avant tout usage.** `kara-architecte.ch` apparaît deux fois dans le classement des
URL les plus citées, en `http://` et en `https://`, 5 citations chacune. Si l'outil compte deux
fois le même site, son total de 17 mentions est à revoir — et c'est le premier du classement.
Non tranché, donc non utilisé.

---

## Pièces

`captures/_otterly/2026-09-18_14h28_otterly_herteltan_rapport-de-marque.pdf`
sha256 `3b457699daa6da8ca7423f72e6c7a809f14ddf4fe0682ab2bc7d610cfcd592f6`

`captures/_otterly/2026-09-18_14h29_otterly_herteltan_export-15-prompts.csv`
sha256 `27c8f3bdd0b6320fc350ea1be0e56e663b97f798190ce77a049375a747ca6f30`

`captures/_otterly/_PROVENANCE.txt` — ce que ces pièces valent, et ce qu'elles ne valent pas.
