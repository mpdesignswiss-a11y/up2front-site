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

**Test mené le 18 septembre 2026 entre 11h45 et 11h55, par Max. Six relevés complets sur huit
prévus.** Ce qui suit est écrit à partir des captures plein écran, pas de souvenirs.

### Conditions réelles

Les huit tentatives ont été faites **dans Google Chrome, en navigation privée, déconnecté des
deux moteurs**. La barre de menu et le libellé « Navigation privée (3) » sont dans chaque image.
Aucun écart de navigateur : j'avais écrit le contraire, à tort, et cette erreur est consignée
plus bas.

### Ce qu'on a observé

| Moteur | Passages tenus | Blocage | Cite ses sources |
|---|---|---|---|
| ChatGPT déconnecté | **4 sur 4** | aucun | oui — pastilles de domaine cliquables |
| Perplexity anonyme | **2 sur 4** | mur d'inscription au passage 3 | oui — 15 sources listées par réponse |

**ChatGPT a tenu les quatre passages d'affilée**, en dix minutes, sans mur de quota ni demande de
connexion. Chaque conversation porte une URL de la forme `chatgpt.com/uc/<identifiant>`, et les
quatre sont au registre. **Elles ne rouvrent pas** — voir plus bas, c'est une correction.

**Perplexity a bloqué au troisième passage**, à 11h55 : un mur d'inscription posé par-dessus une
réponse grisée, impossible à lire. Le passage 4 n'a pas été tenté — la série s'arrête là, comme
prévu. Le 17 septembre, le même mur était tombé au deuxième passage sur sept. Deux occurrences ne
font pas une loi, mais elles vont dans le même sens et suffisent à trancher un défaut de travail.

Une précision ajoutée en fin de journée, en rouvrant les URL : **la réponse du passage 3 existait
bel et bien sous le mur.** Perplexity l'avait produite — quatre bureaux, dix sources — et le mur
ne faisait que la masquer. Le résultat du test ne bouge pas d'un pouce : la question était de
savoir si un opérateur peut enchaîner quatre relevés, et la réponse reste non. Mais la formule
juste est **« réponse produite, illisible par l'opérateur »**, pas « pas de réponse », et le
registre a été corrigé dans ce sens. Ce texte n'ayant pas été vu au moment du test, il ne compte
dans aucun comptage.

**Les deux moteurs citent leurs sources avec des liens.** Le critère n° 2 ne les sépare donc pas.
C'est le mur de quota, et lui seul, qui départage.

### Ce qu'on en tire

**Le défaut de travail du mode opératoire v2 — ChatGPT déconnecté comme second moteur de
l'Express — est confirmé par la mesure.** Il l'était par hypothèse ; il ne l'est plus. La réserve
ouverte en fin de `RELEVE-EXPRESS-mode-operatoire.md` peut se fermer, et la ligne « Moteurs
interrogés » du niveau 2 tient telle quelle.

Portée de cette conclusion, et rien au-delà : elle vaut pour **une intention en français, marché
Genève, un après-midi, une machine, un réseau**. Elle dit qu'un opérateur peut enchaîner quatre
relevés ChatGPT déconnecté sans être arrêté. Elle ne dit pas que ça tiendra à quarante, ni
depuis une autre adresse, ni dans six mois. Le jour où un mur tombera sur ChatGPT aussi, il sera
écrit ici de la même façon.

### Une observation qui n'était pas demandée

**HertelTan Architectes n'apparaît dans aucun des six relevés complets**, sur leur propre
intention de cœur de métier. Les noms qui reviennent sont, chez ChatGPT, CM Studio, KELLER,
Marine Terrien, Cécile Morel, Alan Strappazzon, Kara, et chez Perplexity, Mahaut Design, Atelier
Nord, Kunz, maage, RK Interiors, mélimélo, Relief Intérieurs, Origami Rénovation.

Le pilote du 17 septembre donnait déjà 3 absences sur 3. On est à 9 sur 9. **Ce n'est toujours
pas un taux** — c'est une intention unique, deux journées, deux moteurs, et le jeu HertelTan
complet en compte quatre-vingts. Mais neuf observations concordantes sur l'intention centrale
d'un bureau, c'est la chose la plus solide qu'on ait à ce jour sur ce dossier, et ça mérite
d'être dit sans être gonflé.

### Une seconde observation non demandée, et celle-là compte

**Les quatre réponses ChatGPT s'ouvrent sur une carte, pas sur du texte.** Vérifié sur les
quatre, image par image : avant le moindre paragraphe, ChatGPT affiche un plan de Genève (rendu
Mapbox) avec des fiches d'établissements notées — CM STUDIO Architectes 5,0, ecotonos 4,5, Hilo
Architecture 5,0, Alan Strappazzon 4,5. Le texte et les liens viennent **après**, en dessous.

Si ça se confirme, ça déplace une partie du levier : pour une intention de service local, être
cité par ChatGPT ne passe pas seulement par un site web bien écrit, mais par une présence dans
la couche « établissements notés » qu'il affiche en premier. Ce n'est pas le même chantier, ni
la même promesse commerciale.

**Réserve, et elle est sérieuse.** Je ne sais pas ce qui alimente ces fiches ni d'où viennent
les notes. Elles ressemblent à des notes d'annuaire cartographique, mais **je ne l'ai pas
vérifié** et je ne l'écrirai pas comme un fait. Tant que la source n'est pas établie, cette
observation ne va dans aucun document client : elle reste une piste à instruire, sur quatre
relevés d'une seule intention.

### Écarts et corrections déclarés

**Un écart de protocole.** Le quatrième relevé ChatGPT (11h50) n'est pas un échange à un seul
tour : le moteur a d'abord demandé de quelle ville il s'agissait, et Max a répondu « Genève ».
La réponse mesurée est donc arrivée au second tour. Elle est conservée et comptée comme passage
tenu — la question portait sur le mur de quota, qui n'est pas tombé — mais elle n'est **pas**
comparable mot pour mot aux trois autres, et c'est écrit dans la colonne `ecart` de sa ligne.

**Deux erreurs de ma part, dans ce fil, avant l'ouverture des captures.** J'ai affirmé que
ChatGPT déconnecté ne produisait aucune URL à copier, et que la colonne `citations_brutes`
resterait donc vide : c'est faux, les quatre conversations ont chacune leur URL. Et j'ai écrit
que le test avait été fait pour partie dans Safari, pour partie dans Chrome, et je l'avais
consigné comme écart : c'est faux aussi, Max avait raison, tout est dans Chrome. Les deux
affirmations venaient de moi, pas d'une observation. Elles sont retirées et consignées plutôt
qu'effacées.

**Une troisième correction, le soir même, et elle porte sur la précédente.** J'avais écrit plus
haut que les quatre URL ChatGPT étaient « consultables et donc vérifiables après coup ». Je l'ai
écrit sans avoir essayé. J'ai essayé : **les quatre adresses `chatgpt.com/uc/…` ne rouvrent
rien** — elles renvoient sur une page d'accueil vide, déconnectée. Ce qui est vrai, c'est que
ChatGPT déconnecté *attribue* une URL à la conversation ; ce qui est faux, c'est qu'on puisse y
revenir. Les trois URL Perplexity, elles, rouvrent normalement, en session partagée.

Conséquence concrète, et elle compte pour la suite : **pour ChatGPT, la capture plein écran est
le seul état de la réponse.** Il n'y a pas de filet. Si une capture manque ou coupe, le contenu
est perdu, sans recours. Pour les quatre-vingts relevés HertelTan, cela veut dire que le geste
n° 4 — copier le texte intégral dans un `.txt` — doit être fait **pendant** le relevé sur
ChatGPT, pas après, et que le geste n° 5 doit couvrir la réponse entière.

**Une réserve honnête sur les conditions.** Le lanceur ouvrait ChatGPT avec le paramètre de chat
temporaire, mais **les captures ne permettent pas de confirmer que ce mode était bien actif** —
la mention n'y est pas lisible. Ce qui est établi par l'image, c'est l'état déconnecté et la
fenêtre privée. La colonne `mode` du registre porte donc cette nuance.

### Ce que le rodage du registre a appris

Le test devait aussi servir à trouver une colonne mal pensée avant les quatre-vingts relevés
HertelTan. Il en a trouvé une, par manque : **le geste n° 3 demande de copier l'URL de la
réponse, et aucune colonne ne l'accueillait.** `citations_brutes` sert aux sources citées, pas à
l'adresse de la conversation. La colonne **`url_reponse`** a donc été ajoutée juste après
`fichier_reponse`, dans le registre de test comme dans `REGISTRE-releves.csv`, qui passe de
vingt-huit à vingt-neuf colonnes. Les huit URL y sont.

### Reste à faire

~~Ranger les captures.~~ **Fait le 18 septembre à 12h15 :** vingt images dans
`captures/_test-moteurs/`, nommées par `ranger-TEST-MOTEURS.command`. Une seule divergence entre
le registre et les fichiers, et le registre a cédé : le mur Perplexity a été capturé à 11h55:55
mais le fichier a été écrit à 11h56:01, donc la capture porte `11h56` tandis que l'horodatage du
relevé reste 11:55. Six secondes, écrites plutôt que gommées.

~~Les `.txt` de texte intégral.~~ **Faits pour Perplexity le 18 septembre au soir, impossibles
pour ChatGPT.** Les trois réponses Perplexity ont été récupérées mot pour mot depuis leurs URL et
écrites en `.txt` à côté de leurs captures, chacune avec un en-tête de provenance qui dit ce
qu'elle est : un texte **rouvert après coup, depuis un autre contexte de navigateur**, et non une
transcription faite à l'écran au moment du relevé. En cas de divergence, la capture fait foi.
Les colonnes `citations_brutes` des trois lignes portent maintenant les domaines réellement cités
dans le corps de la réponse, à la place de « non relevées une à une ».

Pour les quatre relevés ChatGPT, il n'y a pas de `.txt` et il n'y en aura pas : les URL ne
rouvrent pas. La colonne `fichier_reponse` de ces quatre lignes a été vidée plutôt que de
pointer un fichier inexistant, et la raison est écrite dans leur colonne `ecart`. Les listes de
bureaux ChatGPT consignées en `ecart` restent donc **ma lecture des images** : assez pour
trancher quel moteur tient, pas assez pour compter. Si on veut un jour compter sur ChatGPT, il
faudra refaire des relevés avec le texte copié pendant le passage.

Puis recopier les huit lignes dans `REGISTRE-releves.csv` et supprimer le fichier de registre de
test.
