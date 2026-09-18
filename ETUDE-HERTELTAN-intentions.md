# Étude approfondie — HertelTan Architectes EPF SIA

## Jeu d'intentions, version 1 — verrouillé le 18 septembre 2026

> **Ce fichier est verrouillé.** Les dix-huit intentions ci-dessous sont fixées **avant** toute
> mesure. Elles ne seront ni ajoutées, ni retirées, ni reformulées une fois les premiers relevés
> lancés — quel que soit le résultat, flatteur ou non. Toute modification ultérieure ouvre une
> **version 2** datée, avec la raison écrite, et les deux versions ne se mélangent pas dans les
> comptages. C'est la seule façon d'empêcher la question qu'un architecte posera tôt ou tard :
> « vous n'auriez pas choisi vos questions après avoir vu les réponses ? »

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

## D'où viennent les dix-huit intentions

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

## Le jeu verrouillé

| ID | Intention exacte | Strate | Page du site qui la justifie |
|----|------------------|--------|------------------------------|
| HT-01 | `architecte pour une rénovation d'appartement à Genève` | Logement | `/expertise/logements/` — **reprise du pilote du 17 septembre, mot pour mot**, pour garder un point de comparaison |
| HT-02 | `qui contacter pour transformer un appartement à Genève` | Logement | `/expertise/logements/` |
| HT-03 | `architecte pour rénover une villa à Genève` | Logement | `/expertise/logements/` |
| HT-04 | `bureau d'architecture pour la rénovation d'un immeuble à Genève` | Logement | `/expertise/logements/` |
| HT-05 | `architecte pour une surélévation à Genève` | Logement | `/expertise/logements/` |
| HT-06 | `architecte rénovation énergétique Genève` | Énergie | `/expertise/renovation-energetique/` |
| HT-07 | `comment rénover et isoler un immeuble ancien à Genève` | Énergie | `/expertise/renovation-energetique/` |
| HT-08 | `qui peut m'accompagner pour une rénovation énergétique subventionnée à Genève` | Énergie | `/expertise/renovation-energetique/` |
| HT-09 | `architecte pour aménager des bureaux à Genève` | Tertiaire | `/expertise/commerces-et-bureaux/` |
| HT-10 | `architecte pour aménager une boutique à Genève` | Tertiaire | `/expertise/commerces-et-bureaux/` |
| HT-11 | `architecte pour l'agencement d'un restaurant à Genève` | Tertiaire | `/expertise/conception-interieur-restaurant/` |
| HT-12 | `architecte d'intérieur à Genève pour un appartement haut de gamme` | Intérieur | `/expertise/conception-interieur/` |
| HT-13 | `qui conçoit une cuisine sur mesure à Genève` | Intérieur | `/expertise/conception-interieur/` |
| HT-14 | `expertise immobilière avant achat à Genève` | Expertise | `/expertise/expertise-immobiliere/` |
| HT-15 | `faire évaluer l'état d'un bien avant de l'acheter à Genève` | Expertise | `/expertise/expertise-immobiliere/` |
| HT-16 | `English speaking architect in Geneva` | Profil | `/trouver-un-architecte-anglophone-a-geneve/` — **article écrit exprès pour cette intention** |
| HT-17 | `architecte SIA à Genève pour un projet privé` | Profil | `/equipe/` — architectes inscrits GE et VD, membres SIA |
| HT-18 | `combien coûte un architecte à Genève pour une rénovation` | Profil | `/prestations-ordinaires-dun-bureau-darchitecte-en-suisse/` |

**Répartition :** 5 logement, 3 énergie, 3 tertiaire, 2 intérieur, 2 expertise, 3 profil.
La strate « logement » est la plus fournie parce que c'est le cœur déclaré du bureau et parce que
c'est là que le pilote a trouvé l'absence. Cette pondération est décidée **maintenant**, avant de
mesurer, et sera rappelée dans le rapport.

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

1. Mode opératoire version 2 écrit et commité — **avant** le premier relevé.
2. Registre de collecte créé, vide, avec ses colonnes.
3. Les 18 intentions chargées dans l'outil de suivi.
4. Premier passage : 10 relevés par intention, session fraîche à chaque fois, Google AI Mode seul.
5. Deuxième fenêtre de collecte, un autre jour, même protocole.
6. Comptages, intervalles de Wilson, rapport.

Rien de tout cela ne commence tant que les points 1 et 2 ne sont pas écrits et scellés.
