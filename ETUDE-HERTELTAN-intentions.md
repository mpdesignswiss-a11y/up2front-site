# Étude approfondie — HertelTan Architectes EPF SIA

## Jeu d'intentions, version 2 — verrouillé le 18 septembre 2026

> **Ce fichier est verrouillé.** Les intentions comptées sont fixées **avant** toute mesure. Elles
> ne seront ni ajoutées, ni retirées, ni reformulées une fois les premiers relevés lancés — quel
> que soit le résultat, flatteur ou non. Toute modification ultérieure ouvre une version datée,
> avec la raison écrite, et les versions ne se mélangent pas dans les comptages. C'est la seule
> façon d'empêcher la question qu'un architecte posera tôt ou tard : « vous n'auriez pas choisi vos
> questions après avoir vu les réponses ? »

> ### Version 2 — huit intentions comptées au lieu de dix-huit
>
> **Écrite le 18 septembre 2026, avant le premier relevé.** La version 1 de ce fichier, écrite le
> matin même et poussée sur GitHub dans le commit `a39fd62`, verrouillait dix-huit intentions.
> Elle n'est pas supprimée : elle reste dans l'historique git, horodatée chez un tiers, et
> vérifiable. Le changement est donc contrôlable par quiconque.
>
> **Raison.** Le mode opératoire version 2 fixe le produit vendu à **huit intentions × dix
> passages**. Une étude de cas à dix-huit intentions démontrerait quelque chose qui n'est pas en
> vente ; le bureau qui achèterait ensuite le Relevé 690 recevrait un dossier deux fois plus
> mince que celui qui l'a convaincu. La vitrine doit être le produit, pas une version augmentée
> du produit.
>
> **Ce qui autorise le changement.** Aucune mesure n'a commencé. La règle de verrouillage interdit
> de changer les intentions *après avoir vu les réponses* ; elle n'interdit pas de réduire le jeu
> avant le premier relevé, à condition que ce soit écrit, daté, et motivé par autre chose qu'un
> résultat. Ici le motif est l'alignement sur le produit, et il est vérifiable : la sélection suit
> les critères écrits plus bas, pas des observations.

---

## Pourquoi ce bureau

Sur les sept bureaux du pilote du 17 septembre, six occupent des positions solides — Pierre
Ambrosetti 1ᵉʳ, KELLER 1ᵉʳ, Camille Aryeh 1ᵉʳ puis 2ᵉ, CORPUS 3ᵉ deux fois. On ne construit pas
une étude de diagnostic sur des bureaux qui vont bien.

HertelTan est le seul cas où le pilote a produit un fait qui mérite d'être creusé, et il est plus
précis qu'un simple « vous êtes invisible » :

- **Absent trois fois sur trois** de sa propre intention (`architecte pour une rénovation
  d'appartement à Genève`), aux trois relevés du 17 septembre.
- **Mais nommé 3ᵉ** à 13h04 sur `meilleur architecte à Genève`, avec sa note (5.0/11) et son
  adresse (Rue des Maraîchers 8), et décrit par une source citée (Neho) comme l'un des bureaux
  genevois les plus en vue.

Le moteur connaît donc l'entreprise. Il ne la sort pas quand on cherche son métier. **C'est un
diagnostic vérifiable, pas une affirmation** — et c'est exactement ce qu'une étude à 200
observations peut établir ou démentir, là où trois relevés ne le peuvent pas.

---

## D'où viennent les intentions

Elles ne sortent pas de mon imagination ni d'un outil de mots-clés. **Chacune est adossée à une
page publique de leur propre site** (`herteltan.ch`, plan de site consulté le 18 septembre 2026).
Le bureau a six pages « expertise » et trois articles de fond : ce sont les prestations qu'il
déclare vendre. Une intention qui ne correspond à aucune de ces pages serait un procès d'intention.

Les six pages expertise : `logements`, `commerces-et-bureaux`, `conception-interieur`,
`conception-interieur-restaurant`, `renovation-energetique`, `expertise-immobiliere`.
Les trois articles : *Trouver un architecte anglophone à Genève*, *Prestations ordinaires d'un
bureau d'architecte en Suisse*, *Architecte suisse — portrait d'une profession clé*.

**Règle de formulation :** l'intention est écrite comme un client la taperait, pas comme un
architecte la rédigerait. Aucune ne contient le nom « HertelTan » — une intention de marque
mesurerait la notoriété, pas la visibilité commerciale.

---

## Le jeu compté — huit intentions

Ce sont les seules qui entrent dans le taux. Dix passages chacune, réparties 5 + 5 sur deux jours
distincts, Google AI Mode seul : **80 relevés comptés**.

| ID | Intention exacte | Strate | Page du site qui la justifie |
|----|------------------|--------|------------------------------|
| HT-01 | `architecte pour une rénovation d'appartement à Genève` | Logement | `/expertise/logements/` — **reprise du pilote du 17 septembre, mot pour mot**, pour garder un point de comparaison |
| HT-02 | `qui contacter pour transformer un appartement à Genève` | Logement | `/expertise/logements/` |
| HT-03 | `architecte pour rénover une villa à Genève` | Logement | `/expertise/logements/` |
| HT-06 | `architecte rénovation énergétique Genève` | Énergie | `/expertise/renovation-energetique/` |
| HT-09 | `architecte pour aménager des bureaux à Genève` | Tertiaire | `/expertise/commerces-et-bureaux/` |
| HT-12 | `architecte d'intérieur à Genève pour un appartement haut de gamme` | Intérieur | `/expertise/conception-interieur/` |
| HT-14 | `expertise immobilière avant achat à Genève` | Expertise | `/expertise/expertise-immobiliere/` |
| HT-18 | `combien coûte un architecte à Genève pour une rénovation` | Profil | `/prestations-ordinaires-dun-bureau-darchitecte-en-suisse/` |

**Les identifiants ne sont pas renumérotés.** HT-04, HT-05, HT-07 et les autres n'existent pas
dans le jeu compté, et leur absence est visible d'un coup d'œil. Renuméroter de 1 à 8 effacerait
la trace de la réduction.

**Répartition : 3 logement, et une par autre strate.** Les six strates du site sont toutes
représentées — aucune prestation déclarée n'est laissée de côté. Le logement en porte trois parce
que c'est le cœur déclaré du bureau et parce que c'est là que le pilote a trouvé l'absence. Cette
pondération est décidée **maintenant**, avant de mesurer, et sera rappelée dans le rapport.

**Les critères de sélection, écrits avant le premier relevé :** une intention par page expertise ;
HT-01 conservée parce qu'elle seule se compare au pilote ; la strate logement renforcée ; à
l'intérieur d'une strate, l'intention la plus proche de la façon dont un client formule sa
demande. Aucun critère ne fait référence à un résultat observé, pour la bonne raison qu'aucun
résultat n'existe.

### Les dix intentions écartées du comptage

HT-04, HT-05, HT-07, HT-08, HT-10, HT-11, HT-13, HT-15, HT-16, HT-17. Elles restent écrites dans
l'historique git (commit `a39fd62`) et forment une **réserve** : si le bureau achète un suivi,
elles sont la seconde vague, déjà adossée à leurs pages, déjà datée d'avant toute mesure.

Une l'est pour une raison de méthode et pas d'arbitrage : **HT-16 `English speaking architect in
Geneva` est en anglais.** Le registre sépare les relevés par langue, et un relevé anglais ne se
compte pas avec un relevé français — ce serait mélanger deux populations, la faute même que nous
reprochons aux audits qui additionnent Google et Perplexity. Elle méritera sa propre série, avec
son propre taux.

---

## Ce qui est volontairement exclu

- **Les intentions de marque** (`HertelTan`, `HertelTan Architectes`) : elles mesurent si le moteur
  sait répondre quand on connaît déjà le nom. Ce n'est pas le sujet.
- **Les intentions hors canton** (Lausanne, Vaud, Suisse romande) : le bureau est inscrit à Genève
  et Vaud, mais le pilote et la liste de prospection sont genevois. Mélanger les marchés sans
  stratifier fausserait les comptages.
- **`meilleur architecte à Genève`** : c'est l'intention sur laquelle HertelTan **sort** 3ᵉ. Elle
  est trop générique pour un client réel, et l'inclure gonflerait artificiellement le taux de
  mention. Elle sera citée dans le rapport comme **contre-preuve** — la démonstration que le moteur
  connaît le bureau — mais **elle ne compte pas dans le taux**.

Ce dernier point est important et doit rester écrit : nous excluons du comptage la seule intention
qui arrange le diagnostic. C'est l'inverse d'un tri favorable.

---

## La série OT — sept questions ajoutées le 18 septembre à 14h22, et pourquoi

Le compte Otterly.AI a été ouvert le 18 septembre en début d'après-midi. **L'outil refuse de
valider un suivi en dessous de quinze questions** : le bouton « Next » reste inactif à huit,
vérifié à 14h22. Il fallait donc sept questions de plus, ou renoncer à l'outil.

Sept ont été écrites sur place, en quelques minutes. Elles portent les identifiants **OT-01 à
OT-07** — « OT » pour Otterly, l'outil qui les a imposées — et elles ne sont pas de même nature
que les huit. Les huit sortent des pages d'expertise du bureau et sont verrouillées le 18 septembre
au matin, avant la moindre mesure. Les sept sortent d'une contrainte logicielle, l'après-midi du
même jour, mais **avant qu'Otterly n'ait rien mesuré** — c'est la seule chose qui les sauve.

| Code | Formulation | Pourquoi elle existe |
|---|---|---|
| OT-01 | `architecte pour aménager un restaurant à Genève` | Couvre `/expertise/conception-interieur-restaurant/`, sans intention dans les huit |
| OT-02 | `architecte pour l'aménagement d'un commerce à Genève` | Couvre le volet « commerces » de `/expertise/commerces-et-bureaux/` |
| OT-03 | `meilleur architecte à Genève` | **Voir ci-dessous — c'est une faute** |
| OT-04 | `architecte d'intérieur à Genève` | Variante courte de HT-12, sans le qualificatif de standing |
| OT-05 | `bureau d'architectes à Genève pour un immeuble de logements` | Échelle immeuble, absente des huit qui sont toutes à l'échelle du logement |
| OT-06 | `architecte pour rénover une cuisine et une salle de bain à Genève` | Formulation par pièce, la plus proche du langage d'un particulier |
| OT-07 | `cabinet d'architecture à Genève pour un projet de rénovation` | Variante générique, témoin |

**La règle, et elle n'a pas d'exception : les deux séries ne s'additionnent jamais dans un chiffre
montré à un prospect.** Un taux Otterly se donne sur les huit, ou sur les sept, jamais sur quinze.
Le rapport du 18 septembre le montre : HertelTan récolte 2 mentions sur les huit intentions
verrouillées et 5 sur les sept de remplissage. Additionner donnerait « 7 mentions sur 15
questions », un chiffre flatteur et faux, construit majoritairement sur des questions écrites pour
débloquer un bouton.

### OT-03 est une faute, et elle est de Claude

`meilleur architecte à Genève` **figure dans la liste des exclusions ci-dessus**, décidée le matin
même, pour un motif explicite : « l'inclure gonflerait artificiellement le taux de mention ». Cette
exclusion est le passage dont l'étude dit qu'il est « l'inverse d'un tri favorable ».

Elle a été réintroduite l'après-midi pour combler un formulaire, sans que personne ne rouvre le
fichier. Et elle a rapporté une mention, rang 1 — exactement l'effet que l'exclusion visait à
prévenir.

Elle reste dans le suivi Otterly, parce que la retirer casserait la série avant qu'elle n'ait
commencé et parce que voir bouger cette question-là dans la durée a son intérêt. Mais **elle ne
compte dans aucun taux**, ni avec les huit, ni avec les sept. Son statut est inchangé depuis le
matin : contre-preuve, jamais numérateur.

La leçon, pour la suite : une décision de méthode écrite dans un fichier ne protège de rien si
personne ne rouvre le fichier au moment de décider.

---

## Avant de publier quoi que ce soit

Cette étude est construite sur une entreprise réelle, nommée, qui n'a rien demandé. Deux
conséquences, à traiter avant tout envoi ou toute publication :

1. **Le rapport nominatif est destiné à HertelTan, pas au public.** Il leur est adressé
   directement. Une version publique devra être **anonymisée** (« un bureau d'architecture
   genevois de onze avis »), sauf accord écrit de leur part.
2. **Les réserves LCD restent ouvertes**, et elles sont deux, pas une. **Let. o** vise le
   pollupostage — l'envoi *en masse* de publicité par voie de télécommunication sans
   consentement préalable ; c'est une réserve sur la **méthode d'envoi**. **Let. a**
   (dénigrement) et **let. e** (comparaison inexacte ou fallacieuse) visent le **contenu** :
   nommer, comparer ou classer des bureaux tiers. Ce fichier a longtemps attribué à la let. o
   « publicité comparative et dénigrement » — c'était faux, corrigé le 18 septembre après
   vérification auprès de l'OFCOM.
   Elle n'est pas levée par le volume de preuve. Elle demande un avis d'avocat, et cet avis
   conditionne la version publique comme l'e-mail d'approche.

---

## Ce qui vient ensuite, dans l'ordre

1. ~~Mode opératoire version 2 écrit et commité.~~ **Fait le 18 septembre**, commit `e8fd149`.
2. ~~Registre de collecte créé, vide, avec ses colonnes.~~ **Fait le 18 septembre**, commit `a47d229`.
3. ~~Jeu d'intentions aligné sur le produit.~~ **Fait le 18 septembre** : huit intentions comptées.
4. Test ChatGPT / Perplexity, vingt minutes, sous version 2 avec registre — il tranche le second
   moteur de l'Express, pas celui du Relevé 690.
5. ~~Les huit intentions chargées dans l'outil de suivi.~~ **Fait le 18 septembre à 14h28** :
   compte Otterly.AI ouvert, quinze questions chargées — les huit verrouillées plus les sept de
   remplissage de la série OT. Portée pays = Suisse, pas canton de Genève : **l'outil ne remplace
   pas les 80 relevés à la main, il mesure autre chose, à une autre échelle.** Les deux comptages
   restent séparés. Premier retour consigné dans `OTTERLY-18-septembre.md`.
6. Première fenêtre : 5 passages par intention, session fraîche à chaque fois, Google AI Mode seul.
7. Deuxième fenêtre, un autre jour, 5 passages, même protocole.
8. Comptages, taux par journée **à côté** du taux groupé, intervalles de Wilson, rapport.
9. Remesure à 90 jours. C'est elle, et elle seule, qui dira si corriger change ce que le moteur
   répond. Rien n'est promis avant.

Les points 1 à 3 sont scellés. Le premier relevé peut commencer.
