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

## Avant de publier quoi que ce soit

Cette étude est construite sur une entreprise réelle, nommée, qui n'a rien demandé. Deux
conséquences, à traiter avant tout envoi ou toute publication :

1. **Le rapport nominatif est destiné à HertelTan, pas au public.** Il leur est adressé
   directement. Une version publique devra être **anonymisée** (« un bureau d'architecture
   genevois de onze avis »), sauf accord écrit de leur part.
2. **La réserve LCD reste ouverte** (art. 3 al. 1 let. o, publicité comparative et dénigrement).
   Elle n'est pas levée par le volume de preuve. Elle demande un avis d'avocat, et cet avis
   conditionne la version publique comme l'e-mail d'approche.

---

## Ce qui vient ensuite, dans l'ordre

1. ~~Mode opératoire version 2 écrit et commité.~~ **Fait le 18 septembre**, commit `e8fd149`.
2. ~~Registre de collecte créé, vide, avec ses colonnes.~~ **Fait le 18 septembre**, commit `a47d229`.
3. ~~Jeu d'intentions aligné sur le produit.~~ **Fait le 18 septembre** : huit intentions comptées.
4. Test ChatGPT / Perplexity, vingt minutes, sous version 2 avec registre — il tranche le second
   moteur de l'Express, pas celui du Relevé 690.
5. Les huit intentions chargées dans l'outil de suivi. Le compte Otterly n'est pas ouvert ; tant
   qu'il ne l'est pas, les 80 relevés se font à la main.
6. Première fenêtre : 5 passages par intention, session fraîche à chaque fois, Google AI Mode seul.
7. Deuxième fenêtre, un autre jour, 5 passages, même protocole.
8. Comptages, taux par journée **à côté** du taux groupé, intervalles de Wilson, rapport.
9. Remesure à 90 jours. C'est elle, et elle seule, qui dira si corriger change ce que le moteur
   répond. Rien n'est promis avant.

Les points 1 à 3 sont scellés. Le premier relevé peut commencer.
