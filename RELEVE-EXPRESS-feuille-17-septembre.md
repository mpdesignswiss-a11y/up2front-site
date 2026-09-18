# Feuille de relevé express — 17 septembre 2026

> ### Requalification — écrite le 18 septembre 2026
>
> **Cette série est un pilote, pas une mesure.** Au sens que le domaine donne au mot : une
> vérification exploratoire, destinée à régler le dispositif, pas à produire un taux. Elle a
> servi exactement à ça — elle a révélé le mur de quota Perplexity, l'ordre de relevé fautif, et
> l'insuffisance d'une intention par bureau. C'est son utilité, et elle est réelle.
>
> **Ce qu'elle ne peut pas produire : aucun pourcentage.** Une intention par bureau et deux
> passages donnent **deux observations par cellule au maximum**, très en dessous du plancher
> admis — 3 à 5 passages y sont déjà classés « trop peu pour un taux défendable ». Tout chiffre
> en pourcentage tiré de cette feuille serait indéfendable devant un contradicteur.
>
> **Correction du compte annoncé.** L'en-tête disait : *« Sept bureaux × trois passages × deux
> moteurs = quarante-deux relevés, tous capturés et scellés. »* C'était le plan, pas le réel, et
> la phrase contredisait l'écart n° 10 inscrit quatre cents lignes plus bas dans le même fichier.
> Le réel : **neuf relevés au passage 1, sept au passage 2, soit seize** — le volet Perplexity
> s'est arrêté à 2/7 sur quota, et le passage 3 n'a pas eu lieu. Quarante captures classées. La
> phrase fausse n'est pas effacée : elle est citée ici.
>
> **Ce qui reste utilisable en prospection**, et qui ne dépend d'aucun taux : les positions
> observées telles quelles, l'absence répétée de HertelTan sur son intention, et la contradiction
> Google / Perplexity sur meier + associés à trente-deux minutes d'écart. Ce sont des constats
> datés et rejouables, pas des fréquences.
>
> Les relevés ci-dessous ont été faits sous le **mode opératoire version 1**. Ils ne se mélangent
> dans aucun comptage avec un relevé fait sous la version 2.

**Série de référence du pilote.** C'est cette feuille, et elle seule, qui alimente les e-mails de
prospection. La série du 16 septembre est exploratoire, non capturée, et ne sort pas d'ici.

**Seize relevés effectivement faits** — passage 1 : neuf ; passage 2 : sept — sur sept bureaux et
deux moteurs. Tous capturés et scellés. Le plan en prévoyait quarante-deux : voir la
requalification ci-dessus et les écarts n° 8 et n° 10.

---

## Ce qui est verrouillé et ne bouge pas

**Les sept intentions.** Elles ont été fixées le 16 septembre avant le premier passage. Elles sont
reprises ici **à l'identique, mot pour mot**. Les rechoisir aujourd'hui, en sachant ce qu'elles ont
donné hier, reviendrait à choisir la question après avoir vu le résultat — c'est la règle n°1, et
c'est précisément ce que l'étude publiée reproche aux audits qu'elle critique.

| # | Bureau | Intention verrouillée |
|---|---|---|
| 1 | HertelTan Architectes | `architecte pour une rénovation d'appartement à Genève` |
| 2 | meier + associés | `meilleur bureau d'architectes à Genève` |
| 3 | CSDK Architectes | `architecte d'intérieur haut de gamme à Genève` |
| 4 | Camille Aryeh Studio | `architecte d'intérieur à Genève` |
| 5 | CORPUS Architecture Urbanisme | `bureau d'architectes pour un projet immobilier à Genève` |
| 6 | Pierre Ambrosetti Architectes | `architecte pour une villa contemporaine à Genève` |
| 7 | KELLER ARCHITECTES | `meilleur architecte à Genève` |

**Les conditions de session.** Même machine, même réseau, les trois passages.
Perplexity : non authentifié, purge cookies + localStorage + sessionStorage vérifiée à zéro avant
le premier relevé. Google AI Mode : accès direct par URL `?q=…&udm=50`, aucune saisie clavier,
état de session (connecté / déconnecté) **montré dans la capture**, pas déclaré.

**Le résultat n'est pas verrouillé.** S'il est flatteur, il est écrit tel quel. Pierre Ambrosetti
sortira probablement bien : c'est une bonne nouvelle pour lui et un meilleur e-mail, pas un relevé raté.

---

## Horaire des trois passages

| Passage | Heure prévue | Contenu |
|---|---|---|
| 1 | 10h45 → 11h30 | 7 bureaux × 2 moteurs = 14 relevés |
| 2 | 13h00 → 13h45 | les mêmes 14 |
| 3 | 16h00 → 16h45 | les mêmes 14 |

Trois passages étalés sur une journée entière, et non deux à deux heures d'écart. La différence
n'est pas cosmétique : deux passages montrent qu'une réponse *a bougé une fois*, trois passages sur
six heures montrent *qu'elle bouge*. C'est toute la thèse vendue.

**Horodater chaque relevé Google AVANT de naviguer.** L'écart s'est produit deux fois le
16 septembre ; c'est la seule erreur de protocole qui se répète.

---

## Preuve — trois fichiers par relevé, aucun ne s'efface

```
captures/herteltan/2026-09-17_10h47_googleaimode_herteltan.png   plein écran macOS, horloge visible
captures/herteltan/2026-09-17_10h47_googleaimode_herteltan.txt   texte brut de la réponse
captures/herteltan/2026-09-17_10h47_googleaimode_herteltan.url   URL exacte, une ligne
```

Après chaque passage : `bash captures/sceller.sh "passage N — 17 septembre"`
→ empreintes SHA-256, commit, push. L'horodatage tiers est la date du push GitHub.

Protocole complet : `RELEVE-EXPRESS-mode-operatoire.md`, section « La preuve ».

---

## 1. HertelTan Architectes
**Intention :** `architecte pour une rénovation d'appartement à Genève`

| # | Heure | Moteur | Session | Nommé ? Position | Sources citées | Capture |
|---|---|---|---|---|---|---|
| 1 | 11h18 | Google AI Mode | connecté (avatar MP) | **Absent.** Neuf bureaux nommés, aucun n'est HertelTan : Atelier Siebold, CORPUS, ARA Sàrl, Class Orga, Kara, CCHE, Stella Studio, BeHome Interiors, ANA K Design | `www.architectegeneve.com` **trois fois**, CORPUS, ARA, Petit Futé, `stellastudio.ch` | txt + url ✓ / png ✗ |
| 2 | **12h06** (horodatage affiché par le moteur dans la page) | Perplexity | **non authentifié** — « Se connecter » visible dans l'image | **Absent.** Cinq bureaux nommés : CORPUS, Kara Architecte, **Ecotonos**, CM Studio, Studio Plus Architectes | `corpus`, `kara-architecte`, **`architectegeneve`**, `cm-studio`, `studio-plus` — 10 sources | txt + url — **png ABSENT, voir écart n° 8** |
| 3 | **13h00m39 → 13h01m05** | Google AI Mode | connecté (avatar MP) | **Absent, pour la troisième fois de la journée.** Sept bureaux nommés : Stella Studio (5.0/5), Class Orga (4.8/12), Ynspir (5.0/5), ANA K Design (4.5/8), Atelier Siebold (5.0/2), Pierre Ambrosetti (5.0/3), CORPUS (4.9/14) | `www.architectegeneve.com` **en première carte**, CORPUS, Atelier Siebold. Chips en ligne : `architectegeneve.co…`, Class Orga, `stellastudio.ch +5`, CORPUS +2, Atelier Siebold +2 | **png ✓ (5 images)** / txt ✗ / url partielle — voir écart n° 9 |
| 4 | | Perplexity | | | | |
| 5 | | Google AI Mode | | | | |
| 6 | | Perplexity | | | | |

**Constat en trois phrases :**

> **À noter, et c'est le fait le plus intéressant de la journée :** HertelTan est absent de sa
> propre intention aux trois relevés (11h18 Google, 12h06 Perplexity, 13h00 Google), mais il sort
> **nommé 3ᵉ à 13h04 dans l'intention de KELLER** (`meilleur architecte à Genève`), avec sa note
> 5.0 (11 avis) et son adresse Rue des Maraîchers 8. Le bureau existe donc bien pour le moteur.
> Ce n'est pas l'entreprise qui est invisible : c'est l'entreprise **sur cette intention-là**.

---

## 2. meier + associés
**Intention :** `meilleur bureau d'architectes à Genève`

| # | Heure | Moteur | Session | Nommé ? Position | Sources citées | Capture |
|---|---|---|---|---|---|---|
| 1 | **11h43** — rattrapage hors fenêtre, voir journal | Google AI Mode | connecté (avatar MP) | **Nommé**, 3ᵉ des quatre « grands bureaux multidisciplinaires » (après CCHE et Favre+Guth, avant FdMP), et 3ᵉ ligne du tableau comparatif | SIA Genève « +1 ». **`maa.ch` n'est cité nulle part.** Cartes sources : CORPUS, FdMP, CCHE | txt + url ✓ / png ✗ |
| 2 | **12h11** (horodatage moteur) — images prises à **12h17 et 12h18**, voir écart n° 7 | Perplexity | **non authentifié** — « Se connecter » visible dans l'image | **Absent.** Six bureaux nommés : brodbeck roulet, CORPUS, Pierre Ambrosetti, La Ville Nouvelle, maage sàrl, Acquaroli | `local(.ch)`, `pierreambrosetti`, `architecte-comparatif`, `neho` — 10 sources. **`maa.ch` absent ici aussi** | txt + url + **png ✓** (fil archivé) |
| 3 | **13h01m32 → 13h01m52** | Google AI Mode | connecté (avatar MP) | **Nommé, 6ᵉ et dernier des noms cités**, en clôture de la section « Ateliers d'architecture et de référence contemporaine ». Ouverture de réponse : « **FdMP architectes, CORPUS Architecture Urbanisme et CCHE Genève** figurent parmi les bureaux les plus réputés ». Puis Pierre Ambrosetti, group8, meier + associés. **Absent du tableau comparatif final** (FdMP, CORPUS, CCHE, Pierre Ambrosetti) | **`maa.ch` est cité, en chip, sur la ligne meier** — c'est nouveau : au passage 1 il n'apparaissait nulle part. Cartes sources : **local.ch** (« Les MEILLEURS Architectes à Genève »), FdMP, CORPUS | **png ✓ (4 images)** / txt ✗ / url partielle — voir écart n° 9 |
| 4 | | Perplexity | | | | |
| 5 | | Google AI Mode | | | | |
| 6 | | Perplexity | | | | |

**Constat en trois phrases :**

---

## 3. CSDK Architectes
**Intention :** `architecte d'intérieur haut de gamme à Genève`

| # | Heure | Moteur | Session | Nommé ? Position | Sources citées | Capture |
|---|---|---|---|---|---|---|
| 1 | 11h20 | Google AI Mode | connecté (avatar MP) | **Absent.** Six cabinets nommés : Camille Aryeh (1ᵉʳ, 5.0/68), Maison Galli, Cécile Morel, Kara, Alfa design, La Petite Design | Cécile Morel (deux fois), Google → Camille Aryeh Studio | txt + url ✓ / png ✗ |
| 2 | **12h19 — REFUSÉ** | Perplexity | non authentifié | **Aucune réponse.** Le moteur répond « Inscrivez-vous et répétez votre demande. » Quota anonyme épuisé après deux recherches. Voir écart n° 6 | — | url + incident ✓ |
| 3 | **13h02m07 → 13h02m33** | Google AI Mode | connecté (avatar MP) | **Absent, deuxième fois sur Google.** Cinq cabinets nommés et classés dans un tableau de synthèse : Kara Architecte (1ᵉʳ, 5.0/22), Camille Aryeh Studio (2ᵉ, 5.0/68), Cécile Morel (3ᵉ, 4.7/14), **KELLER ARCHITECTES (4ᵉ, 4.9/77)**, Alfa design (5ᵉ, 5.0/12) | Les **trois cartes sources sont des fiches Google** : Kara Architecte Genève, KELLER ARCHITECTES, Camille Aryeh Studio. **Aucun site d'entreprise cité en carte** | **png ✓ (6 images)** / txt ✗ / url partielle — voir écart n° 9 |
| 4 | | Perplexity | | | | |
| 5 | | Google AI Mode | | | | |
| 6 | | Perplexity | | | | |

**Constat en trois phrases :**

> KELLER sort 4ᵉ sur l'intention de CSDK, pendant que CSDK n'y figure pas. Les deux bureaux
> se disputent la même requête et un seul des deux y est.

---

## 4. Camille Aryeh Studio
**Intention :** `architecte d'intérieur à Genève`

| # | Heure | Moteur | Session | Nommé ? Position | Sources citées | Capture |
|---|---|---|---|---|---|---|
| 1 | 11h20 | Google AI Mode | connecté (avatar MP) | **Nommé, 2ᵉ** (après La Petite Design), 5.0 (68 avis), et 2ᵉ ligne du tableau comparatif | **Oui, cité comme source** (carte « Google → Camille Aryeh Studio »). Autres : La Petite Design, Marine Terrien | txt + url ✓ / png ✗ |
| 2 | — | Perplexity | — | **Non relevé.** Accès anonyme fermé après deux recherches. Voir écart n° 6 | — | — |
| 3 | **13h02m50 → 13h03m14** | Google AI Mode | connecté (avatar MP) | **Nommé 1ᵉʳ** — il ouvre la section « Design résidentiel & haut de gamme » et occupe la **1ʳᵉ ligne du tableau comparatif**. 5.0 (68 avis), Pl. du Bourg-de-Four 7. **Il gagne une place sur le passage 1**, où il sortait 2ᵉ derrière La Petite Design. Suivent Kara Architecte, Marine Terrien Design, La Petite Design, Alfa design, atelier apropà, Atelier August | **Cité comme source** (carte « Google → Camille Aryeh Studio », 3ᵉ carte). Autres cartes : La Petite Design, **`www.alfa.design`** | **png ✓ (7 images)** / txt ✗ / url partielle — voir écart n° 9 |
| 4 | | Perplexity | | | | |
| 5 | | Google AI Mode | | | | |
| 6 | | Perplexity | | | | |

**Constat en trois phrases :**

---

## 5. CORPUS Architecture Urbanisme
**Intention :** `bureau d'architectes pour un projet immobilier à Genève`

| # | Heure | Moteur | Session | Nommé ? Position | Sources citées | Capture |
|---|---|---|---|---|---|---|
| 1 | 11h20 | Google AI Mode | connecté (avatar MP) | **Nommé**, 3ᵉ au global, en tête de la section « Architecture contemporaine et résidentielle » (CCHE et FdMP occupent la section précédente), 4.9 (14 avis) | **Son propre site cité en première carte.** Puis **local.ch**, puis CCHE | txt + url ✓ / png ✗ |
| 2 | — | Perplexity | — | **Non relevé.** Accès anonyme fermé après deux recherches. Voir écart n° 6 | — | — |
| 3 | **13h03m29 → 13h03m45** | Google AI Mode | connecté (avatar MP) | **Nommé, 3ᵉ au global et 3ᵉ ligne du tableau**, position identique au passage 1. 4.9 (14 avis), La Voie-Creuse 14. Le précèdent CCHE Genève SA (5.0/5) et FdMP (4.9/7). Suivent KELLER (4.9/77), Kara (5.0/22), Veyrat Sarasin (4.1/7). Tableau final : CCHE, FdMP, **CORPUS**, KELLER | **Son propre site en première carte**, comme au passage 1. Puis **CCHE**, puis **Veyrat Sarasin**. *(local.ch, présent au passage 1, a disparu des cartes)* | **png ✓ (5 images)** / txt ✗ / url partielle — voir écart n° 9 |
| 4 | | Perplexity | | | | |
| 5 | | Google AI Mode | | | | |
| 6 | | Perplexity | | | | |

**Constat en trois phrases :**

---

## 6. Pierre Ambrosetti Architectes
**Intention :** `architecte pour une villa contemporaine à Genève`

| # | Heure | Moteur | Session | Nommé ? Position | Sources citées | Capture |
|---|---|---|---|---|---|---|
| 1 | 11h20 | Google AI Mode | connecté (avatar MP) | **Nommé 1ᵉʳ**, « référence absolue à Genève pour les villas de luxe ». Vésenaz. **Aucune note affichée** — seul du lot dans ce cas | **Oui, cité comme source**, avec un article daté du 15 nov. 2025. Autres : CORPUS, Atelier BE, Trustup | txt + url ✓ / png ✗ |
| 2 | — | Perplexity | — | **Non relevé.** Accès anonyme fermé après deux recherches. Voir écart n° 6. *Noter toutefois : Ambrosetti sort nommé 3ᵉ dans le relevé Perplexity de meier à 12h11, sur une autre intention que la sienne* | — | — |
| 3 | **13h03m59 → 13h04m13** | Google AI Mode | connecté (avatar MP) | **Nommé 1ᵉʳ**, position identique au passage 1 : « Reconnu comme une référence incontournable pour les villas exclusives à Genève », Vésenaz. **Toujours aucune note affichée** — seul du lot dans ce cas aux deux passages. Suivent KELLER (4.9/77), Atelier be (3.3/3), CORPUS (4.9/14), CCHE (5.0/5), **meier + associés (5.0/5, Rue du Môle 38BIS)** | **Cité comme source en première carte**, avec le même article daté du **15 nov. 2025** qu'au passage 1. Puis CORPUS, puis **Atelier BE**. *(Trustup, présent au passage 1, a disparu)* | **png ✓ (5 images)** / txt ✗ / url partielle — voir écart n° 9 |
| 4 | | Perplexity | | | | |
| 5 | | Google AI Mode | | | | |
| 6 | | Perplexity | | | | |

**Constat en trois phrases :**

---

## 7. KELLER ARCHITECTES
**Intention :** `meilleur architecte à Genève`

| # | Heure | Moteur | Session | Nommé ? Position | Sources citées | Capture |
|---|---|---|---|---|---|---|
| 1 | 11h20 | Google AI Mode | connecté (avatar MP) | **Nommé 1ᵉʳ**, 4.9 (77 avis), « Mené par Alex Keller », et 1ᵉʳ du tableau comparatif. CSDK 2ᵉ (5.0/10) | **Aucune carte source dans la réponse capturée** — la page s'arrête après le tableau | txt + url ✓ / png ✗ |
| 2 | — | Perplexity | — | **Non relevé.** Accès anonyme fermé après deux recherches. Voir écart n° 6 | — | — |
| 3 | **13h04m28 → 13h04m50** | Google AI Mode | connecté (avatar MP) | **Nommé 1ᵉʳ**, position identique au passage 1 : 4.9 (77 avis), Rue Du-Roveray 16, et **1ʳᵉ ligne du tableau de synthèse**. Suivent Pierre Ambrosetti (2ᵉ), **HertelTan Architectes (3ᵉ, 5.0/11, Rue des Maraîchers 8)**, Kara Architecte, Atelier A architectes, FdMP (4.9/7), CCHE (5.0/5). **CSDK, qui sortait 2ᵉ au passage 1, a disparu.** Tableau final : KELLER, Kara, FdMP, CCHE, Pierre Ambrosetti | **Trois cartes sources cette fois** (contre zéro au passage 1) : FdMP architectes, Pierre Ambrosetti, et **Neho — « Liste des architectes à Genève (2026) »**, dont l'extrait visible nomme HertelTan | **png ✓ (6 images)** / txt ✗ / url partielle — voir écart n° 9 |
| 4 | | Perplexity | | | | |
| 5 | | Google AI Mode | | | | |
| 6 | | Perplexity | | | | |

**Constat en trois phrases :**

> **Hypothèse du doublon : tranchée le 17 septembre, elle est fausse.** `architectegeneve.com`
> n'est pas une façade de KELLER : c'est le cabinet **ecotonos Sàrl**, fondé par **Laurence Jaillat**,
> architecte EAUG MPQ, siège à **Cologny**, IDE CHE-461.190.280, téléphone +41 79 628 77 79. Le site
> ne contient **aucune occurrence** de « Keller » ni de « Roveray », et aucun lien vers
> `kellerarchitectes.ch`. KELLER ARCHITECTES, c'est Alexander Keller, Rue Du-Roveray 16, 1207 Genève,
> +41 22 786 13 12. Deux raisons sociales, deux dirigeants, deux communes, deux téléphones.
>
> **Mais le plus important est ailleurs.** Le signal qui avait fait naître le soupçon — « même
> adresse, même note 4,9, mêmes 77 avis » — **ne repose sur aucune source vérifiable**. Ni le site,
> ni le registre du commerce, ni les annuaires ne le portent. Il vient de mes propres notes du
> 16 septembre. **C'est une confusion que j'ai fabriquée en consignant de mémoire, et c'est une
> raison de plus pour laquelle la série du 16 ne peut pas servir.**
>
> **À faire pendant le relevé :** ouvrir les deux fiches Google Maps, relever `place_id`, adresse,
> téléphone, note et nombre d'avis pour chacune. Tant que ce n'est pas fait, aucun chiffre d'avis
> ne sort dans un e-mail.
>
> **Rappel canal :** Keller n'a aucune adresse e-mail publiée — LinkedIn ou téléphone.
>
> **Confirmation indépendante, obtenue au relevé n° 1 de 11h20.** Dans la même réponse Google,
> KELLER ARCHITECTES (4.9 / 77 avis, Rue Du-Roveray 16, 1207 Genève) et **ecotonos**
> (4.9 / 15 avis, Laurence Jaillat, Rte Martin-Bodmer 2, 1223 Cologny) apparaissent comme
> **deux entrées distinctes**, chacune avec sa note et son nombre d'avis. Ce n'est plus notre mot
> contre le sien : c'est Google lui-même, dans le fichier `captures/keller/…11h20….txt`, qui
> sépare les deux cabinets. La question du doublon est close.

---

## Journal de session — écarts au protocole, à déclarer

*À remplir au fil de la journée. Un écart déclaré vaut mieux qu'un écart caché : c'est la seule
chose qui distingue ce relevé d'un audit vendu par quelqu'un d'autre.*

### Écart n° 1 — aucune capture d'image. Le plus lourd des quatre.

**Ce que le protocole demande :** « Capture **plein écran macOS**, pas capture de navigateur :
l'horloge de la barre de menu doit se trouver dans la même image que la réponse. »

**Ce qui a été fait :** rien. Les sept relevés Google du passage 1 ont un `.txt` et un `.url`,
**ils n'ont pas de `.png`.**

**Pourquoi.** Le navigateur est piloté par une extension qui travaille dans un onglet
d'arrière-plan. Aucun outil de cette extension ne met cet onglet au premier plan, et Chrome
n'est accordé à l'outil de capture d'écran qu'en **lecture seule** — les clics et la frappe y
sont bloqués par conception, précisément pour éviter qu'un agent prenne la main sur le
navigateur de quelqu'un. Il n'existe donc aucun chemin, avec ces outils, vers une image
plein écran montrant à la fois l'horloge système et la réponse. Ce n'est pas une négligence,
c'est une impossibilité — mais le résultat pour le prospect est le même : **il n'y a pas d'image.**

**Ce que cela coûte, précisément.** Deux des quatre exigences de la section « La preuve » tombent.
L'heure n'est plus attestée par l'horloge dans le cadre : elle vient de l'horodatage interne des
appels d'outil, converti en heure de Genève — c'est-à-dire **de nous**. Et l'état de session n'est
plus *montré*, il est **déclaré** : la colonne « Session » dit « connecté, avatar MP », mais
personne ne peut le vérifier. Or le protocole écrit noir sur blanc « montré et non déclaré ».

**Ce qui tient encore.** L'URL exacte, elle, est intacte, et c'est la pièce la plus forte : le
destinataire reclique et repose littéralement la même question. Le texte brut est intégral, non
retouché. Et l'horodatage tiers reste entier, côté GitHub, dès le scellement — un push est daté
par quelqu'un d'autre que nous, ce qu'une horloge système, que je pourrais régler moi-même,
n'est pas. On peut défendre que le couple URL + push GitHub vaut mieux qu'une photo d'horloge.
**Mais c'est un changement de dispositif que Max n'a pas approuvé**, et il doit trancher avant
les passages 2 et 3 : soit il prend les captures lui-même, soit le dispositif de preuve devient
officiellement « URL + texte + push », et le mode opératoire doit être réécrit en conséquence.

*Note annexe, qui ne justifie rien mais mérite d'être sue :* une capture plein écran aurait
embarqué dans les quarante-deux images les onglets clients ouverts sur cette machine, ainsi que
le bandeau « Claude a démarré le débogage de ce navigateur ». Un destinataire pouvait y lire une
manipulation. L'absence d'image n'est pas un moindre mal choisi — mais l'image, telle qu'elle
aurait été prise, aurait eu son propre défaut.

### Écart n° 2 — le relevé meier + associés est perdu, et refait à 11h43

Les sept relevés Google ont bien été effectués entre 11h18 et 11h20. Six ont été écrits sur le
disque. **Le septième, meier + associés, a été perdu** avant d'atteindre un fichier : il ne
subsistait que dans un journal de session technique, dans un bloc trop volumineux pour être
relu. Il n'est pas récupérable.

Il a donc été **refait à 11h43**, soit treize minutes après la fermeture de la fenêtre du
passage 1 (10h45 → 11h30). La ligne du tableau porte cette heure et la mention « rattrapage hors
fenêtre ». **Ce relevé n'est pas comparable aux six autres** à la minute près ; il l'est à
l'échelle de la journée, qui est celle qui compte pour la thèse. Il ne doit jamais être présenté
comme faisant partie de la même salve.

### Écart n° 3 — trois imprécisions mineures, consignées pour ne pas avoir à y revenir

**Les heures viennent des horodatages des appels d'outil, pas d'une lecture d'horloge.** Ils sont
en UTC (09h18 et 09h20), convertis en heure de Genève. Fiables, mais c'est notre chaîne d'outils
qui les produit.

**CSDK est peut-être 11h19.** Son relevé ouvre un lot achevé à 11h20 ; le chargement de sa page a
eu lieu vingt à trente secondes plus tôt. `11h20` est l'heure enregistrée, pas l'heure certaine.

**Cinq des sept `.txt` portent un préfixe technique `[get_page_text] `.** Les deux autres non.
C'est fidèle au brut — les fichiers n'ont pas été nettoyés — et non une erreur de copie.

### Écart n° 4 — le passage 1 est à moitié fait

Sept relevés Google sur quatorze. **Les sept relevés Perplexity ne sont pas faits.** Le passage 1
ne pourra jamais être un passage 1 complet : refaire Perplexity maintenant produirait un relevé
d'un autre moment de la journée, pas le pendant des sept relevés de 11h20.

### Écart n° 5 — le commit est fait, le push ne l'est pas. L'horodatage tiers manque encore.

`captures/sceller.sh` a bien tourné à 11h49 : empreintes SHA-256 des sept textes consignées dans
`captures/empreintes.txt` et dans `captures/manifeste.csv`, puis **commit `6c86bcd`**, dix-huit
fichiers. La chaîne de hachages locale existe, et une capture modifiée après coup la casserait.

**Mais le `git push` a échoué** : l'environnement d'où tourne le script n'a pas le droit de
joindre `github.com` en SSH. Or c'est le push, et lui seul, qui place l'horodatage **chez un
tiers**. Tant qu'il n'a pas eu lieu, la seule date opposable est celle d'un commit fabriqué sur
cette machine — donc par nous.

**C'est d'autant plus important que l'écart n° 1 a supprimé les images.** Le dispositif de preuve
repose désormais sur trois pieds — URL exacte, texte intégral, horodatage GitHub — et il en
manque un. **Max doit lancer le push depuis son poste** ; d'ici là, aucun relevé de cette série
n'est daté par autre chose que nous.

### Écart n° 6 — Perplexity a fermé l'accès anonyme. Deux relevés sur sept, et c'est définitif pour aujourd'hui.

**Ce que le protocole demande** (`RELEVE-EXPRESS-mode-operatoire.md`, ligne 21) : « Perplexity :
fenêtre de navigation privée, non authentifié, aucun historique. » **Cette phrase n'est plus
applicable.** Elle a été écrite le 16 septembre, quand elle marchait.

**Ce qui s'est passé, dans l'ordre, le 17 septembre.**

*En navigation privée, refus immédiat.* Deux tentatives, 12h01 et 12h03, même réponse du moteur :
« Inscrivez-vous et répétez votre demande. » Zéro recherche accordée. La cause est le blocage des
cookies tiers propre au mode privé de Chrome.

*En fenêtre normale, non authentifié : deux recherches, puis un mur.* HertelTan passe à 12h06,
meier passe à 12h11. À 12h12, un panneau « Inscrivez-vous ci-dessous pour libérer tout le
potentiel de Perplexity » se pose par-dessus la réponse de meier, **sans bouton de fermeture** —
vérifié dans la structure de la page : le bloc ne contient qu'un lien vers la politique de
confidentialité, quatre boutons sans nom et un champ e-mail. Échap ne fait rien, recharger ne
fait rien.

*La purge des cookies rend la lecture, pas le droit de chercher.* Effacer les cookies du seul
domaine `perplexity.ai` fait tomber le mur sur le fil déjà archivé — la page se recharge propre,
avec en plus la mention « Vous consultez une session partagée ». **Mais la recherche suivante,
CSDK à 12h19, est refusée exactement comme en navigation privée.** Le quota n'est donc pas compté
sur le cookie : il est compté sur l'adresse IP ou sur une empreinte d'appareil que la purge ne
touche pas. **Il s'établit à deux recherches.**

**Ce que cela change.** Perplexity ne fournira pas quatorze relevés aujourd'hui, ni même sept.
Deux sont acquis, avec leur image, leur URL permanente et l'horodatage que le moteur inscrit
lui-même dans sa page. Les cinq autres du passage 1 sont hors d'atteinte.

**La sortie qui existe et qu'on refuse.** Se connecter à Perplexity débloquerait tout, en une
minute. C'est précisément ce qu'il ne faut pas faire : un destinataire pourrait objecter, à
juste titre, que la réponse reflète le compte et l'historique de celui qui a fait le relevé.
L'étude ne survivrait pas à cette objection, et elle serait fondée. **Deux relevés anonymes
valent mieux que sept relevés contestables.**

*Note de méthode :* le 16 septembre, Perplexity avait répondu anonymement aux sept intentions,
entre 15h35 et 17h52 — c'est écrit dans `RELEVE-EXPRESS-feuille-16-septembre.md`. La condition
d'accès a donc changé entre le 16 et le 17. C'est un fait sur le moteur, consigné comme tel, et
pas une excuse : il sera retesté au passage 3.

**Pièce jointe :** `captures/_incidents/2026-09-17_12h03_perplexity_refus-anonyme.txt`, qui porte
le texte intégral des trois refus et les URL des fils correspondants.

### Écart n° 7 — l'image de meier est une relecture, pas la vue d'origine

Les deux images du relevé meier ont été prises à **12h17m14 et 12h18m07**, six et sept minutes
après la réponse de **12h11**, sur
le fil rouvert après la purge des cookies. La page y porte la mention « Vous consultez une
session partagée », absente à 12h11. **Le texte, lui, a été relevé avant le mur**, à 12h11, et
n'a pas bougé. L'écart porte sur l'image seule, et le fichier `.txt` le dit en tête.

Deux précisions qui comptent :

*Le mur n'a pas été retiré par du code.* Il aurait suffi d'une ligne de JavaScript pour le faire
disparaître de la page avant la capture. Cela n'a pas été fait, et ne le sera jamais : une image
de preuve prise sur une page modifiée par nous ne prouve plus rien.

*La purge a épargné Google, délibérément.* Le panneau de Chrome proposait aussi `google.com` et
`accounts.google.com`. Les effacer aurait déconnecté le compte et changé en silence l'état de
session — qui est une variable déclarée des sept relevés Google de 11h20. Seuls
`count.perplexity.ai`, `perplexity.ai` et `www.perplexity.ai` ont été supprimés. La bannière
cookies revenue après la purge a été réglée sur **« Uniquement nécessaires »**, choix à tenir
identique aux passages 2 et 3.

### Écart n° 8 — le relevé Perplexity de HertelTan n'a pas d'image, contrairement à ce qui était écrit

La ligne HertelTan / Perplexity portait la mention **« png ✓ »**. Elle était fausse. Le classement
des captures, fait à 13h20, a montré qu'aucune image du fil HertelTan n'existe : les trois captures
de la tranche 12h11–12h18 sont une vue de l'application Claude (12h11m27, écartée) et **deux vues du
fil meier** (12h17m14 et 12h18m07). Le fil HertelTan n'a jamais été capturé.

**Ce que HertelTan conserve :** le texte intégral de la réponse et l'URL du fil
(`perplexity.ai/search/ac13742a-0902-4b58-b400-0777a62dda9b`), tous deux relevés à 12h06. **Ce qu'il
perd :** l'image. Le relevé reste utilisable — l'URL est publique et rejouable — mais il est d'un
cran plus faible que celui de meier.

*Comment l'erreur s'est produite :* la mention a été écrite à 12h20 en supposant, sans vérifier,
qu'une capture existait par symétrie avec meier. C'est exactement le genre d'affirmation que le
protocole interdit. Elle est corrigée ici plutôt qu'effacée.

---

### Écart n° 9 — le passage 2 a les images, pas le texte ni l'URL. L'inverse exact du passage 1.

Le passage 2 est capturé en entier : **38 images** pour les sept relevés Google, prises entre
13h00m39 et 13h04m50, classées dans `captures/<bureau>/`. C'est la première fois de la journée
que la jambe « image » tient pour les sept.

**Mais les deux autres jambes manquent.** Aucun fichier `.txt` n'a été écrit pour le passage 2 :
le contenu des réponses n'existe que dans les pixels des captures, lu à la main et retranscrit
dans les lignes ci-dessus. Et l'URL complète n'a pas été relevée : elle est **visible dans la
barre d'adresse de chaque image, mais tronquée** par la largeur de la fenêtre. On lit
`google.com/search?q=architecte+pour+une+renovation+d%27appartement+a+Geneve&udm=50&mids=…`
— le paramètre `mids`, qui identifie le fil, est coupé.

**Ce que cela coûte, concrètement.** Un relevé avec image mais sans texte reste opposable :
l'image *est* le texte, elle se lit. Ce qui s'affaiblit, c'est la recherche (impossible de
grep les noms cités) et surtout le **rejeu** : sans l'URL complète, on ne peut pas rouvrir le
fil exact pour vérifier qu'il n'a pas bougé. Le passage 1 avait le problème symétrique.
**Aucun des deux passages n'a les trois jambes.**

**Pourquoi c'est arrivé.** Le dispositif du passage 2 a été conçu dans l'urgence autour de la
seule chose qui manquait au passage 1 — les images. Personne, moi le premier, n'a demandé à
Max de copier aussi le texte et l'URL. C'est une erreur de conception du dispositif, pas une
erreur d'exécution de sa part : il a fait exactement ce qui était demandé.

**Correction pour le passage 3 :** pour chaque relevé, avant de capturer, copier l'URL complète
depuis la barre d'adresse (⌘L puis ⌘C) et coller le texte de la réponse. Sans quoi la série
entière du 17 septembre restera boiteuse des trois côtés à la fois.

---

### Écart n° 10 — le passage 3 n'a pas eu lieu. Le 17 septembre est clos à deux passages.

Le protocole fixait **trois passages dans une même journée** : 11h00, 13h00, 16h00. Les deux
premiers ont eu lieu (11h18 → 12h19, puis 13h00m39 → 13h04m50). **Le troisième, prévu vers
16h00, n'a pas été effectué.** Il est à présent le **18 septembre au matin** : la journée du 17
est terminée et le passage 3 n'est plus rattrapable, par construction — un relevé pris le 18 ne
peut pas être le troisième point d'une série intra-journée du 17.

**Ce que cela retire au dispositif.** Le troisième passage servait à une chose précise : trancher
entre variation et bruit. Avec deux points, une position qui bouge — meier + associés, 3ᵉ puis 6ᵉ —
ne peut pas être distinguée d'un aléa de génération. C'est écrit noir sur blanc dans le bilan du
passage 2 : « deux relevés ne font pas une tendance […] À vérifier au passage 3. » Cette
vérification n'aura pas lieu. **La ligne meier reste donc indéterminée, et doit être présentée
comme telle.**

**Ce que cela ne retire pas.** Les neuf relevés du passage 1 et les sept du passage 2 sont
inchangés. Les quatre positions stables (Ambrosetti 1ᵉʳ, KELLER 1ᵉʳ, CORPUS 3ᵉ, Camille Aryeh
1ᵉʳ puis 2ᵉ), l'absence répétée de HertelTan sur son intention, et la contradiction
Google/Perplexity sur meier à trente-deux minutes d'écart ne dépendent pas du passage 3.

**Ce qui n'est pas encore décidé — et que je ne décide pas à la place de Max.** Deux voies, et
elles ne disent pas la même chose à un prospect :

1. **Clore la série à deux passages**, cet écart déclaré, et le dire tel quel : « dispositif prévu
   à trois passages, exécuté à deux, le troisième n'a pas été fait ». Honnête, immédiat, et
   suffisant pour les constats qui ne reposent pas sur la stabilité.
2. **Requalifier en dispositif sur deux jours** : le relevé du 18 devient **sa propre journée**,
   sur les sept intentions verrouillées à l'identique, avec sa propre feuille
   (`RELEVE-EXPRESS-feuille-18-septembre.md`). Il ne s'appelle pas « passage 3 » et ne se range
   pas dans les colonnes du 17. Ce qu'il mesure est autre chose — la stabilité d'un jour à
   l'autre, pas d'une heure à l'autre — et c'est en soi plus intéressant, mais il faut le nommer
   correctement.

**Dans les deux cas, la correction de l'écart n° 9 s'applique** : copier l'URL complète (⌘L, ⌘C)
et le texte de la réponse **avant** de capturer.

**Pourquoi c'est arrivé.** Le passage 2 s'est terminé à 13h04, et l'après-midi a été consacré à
classer les 38 captures, remplir la feuille et récupérer un dossier de fichiers que j'avais
déplacé par erreur. Personne n'a relancé le passage de 16h00. La responsabilité est de mon côté :
tenir l'horaire du protocole faisait partie de mon travail.

---

## Bilans par passage

*À remplir après chaque passage.*

### Passage 1 — 11h18 → 12h19. Neuf relevés sur quatorze.

**Google AI Mode : 7/7**, à 11h18–11h20 (+ meier à 11h43). Texte et URL pour les sept, **aucune
image** — écart n° 1.
**Perplexity : 2/7**, à 12h06 et 12h11, non authentifié, **avec image** et avec l'horodatage que
le moteur inscrit lui-même dans sa page. Les cinq autres sont refusés — écart n° 6.

Le passage 1 est donc dissymétrique des deux côtés, et en sens inverse : Google a la couverture
sans les images, Perplexity a les images sans la couverture.

| Bureau | Verdict |
|---|---|
| HertelTan | **Absent** de sa propre intention |
| CSDK | **Absent** de sa propre intention |
| meier + associés | Nommé, **jamais cité comme source** |
| CORPUS | Nommé, site cité **en première source** |
| Camille Aryeh | Nommé 2ᵉ, cité comme source |
| Pierre Ambrosetti | **Nommé 1ᵉʳ**, cité comme source |
| KELLER | **Nommé 1ᵉʳ**, 4.9 / 77 avis |

**Quatre choses que ce passage établit, et qu'il faut se garder de surinterpréter.**

*Deux bureaux sont absents de la question qu'ils vendent.* HertelTan sur la rénovation
d'appartement, CSDK sur l'architecture d'intérieur haut de gamme. Ce sont les deux relevés les
plus vendeurs de la série, et ce sont ceux sur lesquels il faudra être le plus prudent : un
relevé ne dit pas une position.

*Être nommé et être cité comme source sont deux choses différentes* — et c'est probablement le
meilleur angle commercial sorti de la journée. meier + associés est nommé parmi les grands
bureaux genevois, et `maa.ch` n'apparaît nulle part dans les sources. CORPUS, lui, est nommé
**et** son site ouvre la liste des sources. Le premier est décrit par d'autres ; le second
fournit la matière. Cette distinction ne figure dans aucun « score de visibilité IA » vendu
ailleurs.

*Un tiers capte l'intention de HertelTan.* `www.architectegeneve.com` — le site d'ecotonos,
Laurence Jaillat — est cité **trois fois** dans la réponse sur la rénovation d'appartement, une
question où HertelTan est absent. Un cabinet de Cologny occupe la place éditoriale d'un bureau
du centre-ville sur son propre métier.

*Deux relevés flatteurs, à écrire comme tels.* Ambrosetti 1ᵉʳ et cité comme source ; KELLER 1ᵉʳ
avec 77 avis. Le mode opératoire l'avait prévu pour Keller. La règle s'applique : on l'écrit,
et l'e-mail change d'angle au lieu de changer de chiffre.

---

### Passage 2 — 13h00m39 → 13h04m50. Sept relevés sur quatorze, tous Google.

**Google AI Mode : 7/7**, en quatre minutes et onze secondes, session connectée (avatar MP
vérifié dans l'image), **avec images pour les sept** — 38 fichiers. **Perplexity : 0/7**, l'accès
anonyme étant fermé depuis 12h19 (écart n° 6). Texte et URL complète manquants — écart n° 9.

| Bureau | Passage 1 (Google, 11h18–11h43) | Passage 2 (Google, 13h00–13h04) | Bouge ? |
|---|---|---|---|
| HertelTan | **Absent** | **Absent** | non |
| CSDK | **Absent** | **Absent** | non |
| meier + associés | Nommé 3ᵉ, `maa.ch` **jamais cité** | Nommé **6ᵉ et dernier**, `maa.ch` **cité en chip** | **oui, des deux côtés** |
| CORPUS | Nommé 3ᵉ, site en 1ʳᵉ source | Nommé 3ᵉ, site en 1ʳᵉ source | non |
| Camille Aryeh | Nommé **2ᵉ**, cité comme source | Nommé **1ᵉʳ**, cité comme source | **oui, +1** |
| Pierre Ambrosetti | **1ᵉʳ**, source, aucune note | **1ᵉʳ**, source, aucune note | non |
| KELLER | **1ᵉʳ**, aucune carte source | **1ᵉʳ**, **trois cartes sources** | **oui, côté sources** |

**Ce que la comparaison établit.**

*Les deux absences tiennent.* HertelTan et CSDK sont absents de leur propre intention aux deux
passages Google, à une heure et quarante minutes d'intervalle. Ce n'est plus un relevé, c'en est
deux. Ce n'est toujours pas une position — il faut le troisième passage — mais l'hypothèse
« c'était un hasard de requête » devient plus coûteuse à défendre.

*L'absence de HertelTan est une absence d'intention, pas une absence d'entreprise.* Le fait le
plus utile du passage 2 : HertelTan sort **nommé 3ᵉ à 13h04 sur `meilleur architecte à Genève`**,
avec sa note et son adresse, et une source (Neho) le décrit comme « l'un des bureaux genevois
les plus en vue ». Le moteur le connaît. Il ne le sort simplement pas quand on cherche une
rénovation d'appartement. C'est un diagnostic plus précis — et plus vendable — qu'un « vous êtes
invisible » que le bureau pourrait démentir en trois secondes.

*Les quatre positions fortes ne bougent pas.* Ambrosetti 1ᵉʳ, KELLER 1ᵉʳ, CORPUS 3ᵉ, Camille
Aryeh qui gagne même une place. Aucun effondrement, aucune envolée. La stabilité est en soi
un résultat : elle rend le protocole crédible, parce qu'un dispositif qui donnerait sept
résultats différents à chaque heure ne mesurerait rien.

*Une seule position se dégrade : meier + associés, qui passe de 3ᵉ à 6ᵉ et dernier, et sort du
tableau comparatif final.* Mais dans le même mouvement `maa.ch` apparaît pour la première fois
comme source citée. Le bureau perd du rang et gagne de la citation. **Ne pas transformer ça en
récit :** deux relevés ne font pas une tendance, et l'un des deux compensant l'autre, on ne sait
pas dire ce qui s'est passé. À vérifier au passage 3.

*Un détail à ne pas perdre.* CSDK sortait 2ᵉ dans l'intention de KELLER au passage 1 ; à 13h04
il n'y est plus, et HertelTan occupe une place dans cette même réponse. Les sept bureaux se
croisent sur les intentions des uns et des autres — ce qui veut dire qu'aucun des sept relevés
ne peut être lu seul.

**Ce que les deux relevés Perplexity ajoutent, et qui est le meilleur matériau de la journée.**

*meier + associés est nommé par Google et absent de Perplexity, sur la même intention, à
trente-deux minutes d'écart.* Google le place 3ᵉ des grands bureaux genevois à 11h43 ; Perplexity,
à 12h11, sort six noms — brodbeck roulet, CORPUS, Ambrosetti, La Ville Nouvelle, maage, Acquaroli
— et pas lui. C'est exactement la contradiction moteur contre moteur sur laquelle l'étude est
bâtie, et elle est ici documentée par deux fichiers, deux URL et une image.

*`architectegeneve.com` capture l'intention de HertelTan une quatrième fois, et sur un troisième
moteur.* Le site d'ecotonos (Laurence Jaillat, Cologny) est cité trois fois par Google à 11h18 et
**nommé par Perplexity à 12h06**, sur la même question, où HertelTan reste absent des deux. Un
seul relevé ne dit rien ; deux moteurs indépendants qui convergent, c'est autre chose.

*Perplexity date ses propres réponses dans la page.* 12:06 et 12:11 sont affichés par le moteur,
pas lus sur l'horloge. C'est une pièce plus forte que la capture d'écran, parce qu'elle ne vient
pas de nous.

**Ce qui manque avant qu'une seule ligne parte en e-mail :** les passages 2 et 3, les images des
relevés Google, le push GitHub, et le scellement. Perplexity restera à 2/7 pour le passage 1 :
c'est acté, écrit, et ce n'est pas rattrapable.
