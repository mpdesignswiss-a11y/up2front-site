# -*- coding: utf-8 -*-
"""
Les neuf articles du blog, en français.

Le plan éditorial est celui d'Alex : ses neuf titres, dans son ordre, avec
ses neuf catégories. Ce que son dossier laissait « à rédiger » est écrit
ici.

Ligne éditoriale, la même que le reste du site : aucun chiffre inventé,
aucune statistique sans source, rien qui contredise les CGV publiées. Là
où un prix de marché est cité, il l'est en fourchette et daté, parce
qu'il bouge.

Angle SEO : chaque article vise une question que les PME romandes tapent
vraiment, répond dans les deux premiers paragraphes, puis développe. Le
titre H1 reprend la question, les H2 sont des sous-questions, et les
liens internes pointent vers les pages qui monétisent (tarifs, offres,
devis, brief).
"""

INDEX = {
    "sur_titre": "Le journal",
    "h1": ["Ce qu'on aurait aimé", "nous dire avant."],
    "lede": "Neuf articles courts, écrits pour les PME de Suisse romande. "
            "Des prix réels, des délais réels, et ce que nous ferions à "
            "votre place.",
    "sec_t": "Les articles.",
    "sec_c": "Classés du plus demandé au plus technique. Aucun n'a besoin "
             "des autres pour être lu.",
    "appel_h2": "Une question qui n'est pas traitée ici ?",
    "appel_p": "Écrivez-la, on répond le jour même du lundi au vendredi. "
               "Et si la réponse intéresse d'autres personnes, elle "
               "devient un article.",
}

ARTICLES = [
 {
  "slug": "prix-site-web-suisse.html",
  "cat": "Tarifs",
  "titre": "Combien coûte vraiment un site web en Suisse en 2026 ?",
  "h1": ["Combien coûte vraiment", "un site web en Suisse ?"],
  "desc": "Les quatre fourchettes du marché suisse, ce qui fait monter la "
          "facture, et les frais annuels que personne ne chiffre au départ.",
  "dek": "Réponse courte : entre CHF 300 et CHF 30 000. L'écart n'est pas "
         "une question de qualité, c'est une question de ce qu'on achète. "
         "Voici comment lire un devis.",
  "lecture": "7 min",
  "corps": """
<p>Personne ne répond jamais à cette question, et c'est agaçant. Alors
commençons par le chiffre&nbsp;: en Suisse, en 2026, un site web
professionnel pour une PME se paie entre <strong>CHF 300 et CHF
30&nbsp;000</strong>. Cet écart de un à cent n'est pas un écart de
qualité. C'est un écart de périmètre — et surtout d'heures humaines
facturées.</p>

<p>Le reste de cet article sert à savoir dans quelle fourchette vous vous
situez, et à ne pas payer une fourchette pour obtenir le contenu de la
précédente.</p>

<h2>Les quatre fourchettes du marché suisse</h2>

<p><strong>De CHF 0 à 500 — vous faites vous-même.</strong> Un
constructeur en ligne, un modèle du catalogue, vos textes, vos photos.
Le coût réel n'est pas l'abonnement, c'est votre week-end. Comptez de
vingt à quarante heures pour un résultat honnête, davantage si vous
découvrez l'outil. Viable si votre site n'est qu'une carte de visite.</p>

<p><strong>De CHF 300 à 1 500 — le forfait.</strong> Un professionnel
travaille sur une structure qu'il a déjà éprouvée, vous remplissez un
brief, il livre en quelques jours. C'est là que nous nous situons, avec
des forfaits fermes à <a href="../offres/pro-landing-page.html">CHF
290</a>, <a href="../offres/ultimate-website.html">CHF 490</a> et
<a href="../offres/advanced-website.html">CHF 690</a>. Le prix tient
parce que le périmètre est fixé d'avance, pas parce que le travail est
bâclé.</p>

<p><strong>De CHF 3 000 à 12 000 — le sur-mesure d'indépendant ou de
petit studio.</strong> On repart d'une page blanche&nbsp;: ateliers,
arborescence, maquettes, allers-retours, intégration. Deux à huit
semaines. C'est le bon budget dès que votre site doit faire quelque chose
de particulier — un configurateur, une réservation, un catalogue qui
bouge.</p>

<p><strong>De CHF 15 000 à 30 000 et au-delà — l'agence.</strong>
Stratégie, direction artistique, rédaction, développement, suivi,
et plusieurs personnes autour de la table. Justifié quand le site est
un canal de vente principal et qu'un point de conversion gagné vaut
plusieurs dizaines de milliers de francs par an.</p>

<h2>Ce qui fait vraiment monter la facture</h2>

<p>Ce n'est presque jamais le design. Ce sont, dans l'ordre&nbsp;:</p>

<ul>
  <li><strong>Les allers-retours non bornés.</strong> Un projet sans
  périmètre écrit dérive, et la dérive se facture à l'heure. C'est le
  premier poste caché de tous les devis.</li>
  <li><strong>Le contenu.</strong> Si l'agence doit écrire vos textes,
  interviewer vos équipes et faire venir un photographe, vous financez
  trois métiers, pas un.</li>
  <li><strong>Les fonctionnalités.</strong> Paiement en ligne, espace
  client, réservation, synchronisation avec votre logiciel de gestion&nbsp;:
  chacune est un petit projet.</li>
  <li><strong>Le multilingue.</strong> Chaque langue ajoute de la
  traduction, de la relecture et une maintenance qui se démultiplie.</li>
  <li><strong>Le CMS.</strong> Rendre un site modifiable par vous double
  souvent le temps d'intégration. Utile si vous publiez chaque semaine,
  inutile si vous changez un numéro de téléphone une fois par an.</li>
</ul>

<h2>Les frais annuels que personne ne chiffre</h2>

<p>Le devis de création est la moitié de l'histoire. Ce qui revient
chaque année, en Suisse, aux prix courants de 2026&nbsp;:</p>

<ul>
  <li><strong>Nom de domaine en <code>.ch</code></strong> — une dizaine
  de francs par an. Un <code>.com</code>, une quinzaine.</li>
  <li><strong>Hébergement</strong> — de CHF 0 pour un site statique sur
  une plateforme comme Netlify ou Cloudflare Pages, à CHF 200–400 par an
  pour un hébergeur suisse mutualisé, davantage pour un serveur dédié.</li>
  <li><strong>Adresses e-mail professionnelles</strong> — de CHF 60 à 150
  par an et par boîte selon le fournisseur. C'est souvent la surprise.</li>
  <li><strong>Certificat HTTPS</strong> — gratuit aujourd'hui
  (Let's Encrypt), et automatique chez la plupart des hébergeurs. Si on
  vous le facture, demandez pourquoi.</li>
  <li><strong>Maintenance</strong> — de CHF 0 pour un site statique à
  CHF 600–1 800 par an pour un WordPress qu'il faut mettre à jour, et
  qu'il faut bien mettre à jour&nbsp;: c'est la première cause de piratage
  de sites de PME.</li>
</ul>

<p>Autrement dit&nbsp;: un site à CHF 2 000 qui coûte CHF 1 200 par an
en entretien est plus cher, sur cinq ans, qu'un site à CHF 5 000 qui ne
coûte que son domaine.</p>

<h2>Ce qu'un forfait ferme change</h2>

<p>Un prix ferme déplace le risque. Si le projet prend plus de temps que
prévu, c'est le problème du prestataire, pas le vôtre. En échange, le
périmètre est écrit avant de commencer&nbsp;: nombre de pages, nombre de
langues, ce qui est compris, ce qui fait l'objet d'un devis séparé.</p>

<p>C'est ce cadre qui nous permet d'annoncer une <a
href="../index.html#tarifs">grille publique</a> et une livraison
<strong>dès deux jours ouvrés</strong> à partir du brief complet, avec
<strong>trente jours de révisions illimitées</strong> et un
<strong>remboursement intégral</strong> si le résultat ne vous convient
pas. Les <a href="../legal/conditions.html">conditions générales</a> le
disent noir sur blanc, ce qui est le seul endroit où une promesse
commerciale vaut quelque chose.</p>

<h2>Combien faut-il prévoir, concrètement</h2>

<ul>
  <li><strong>Artisan ou indépendant, une page qui présente et fait
  appeler</strong> — CHF 300 à 800 de création, moins de CHF 50 par an.</li>
  <li><strong>PME de services, quatre à six pages, une langue</strong> —
  CHF 500 à 2 500 de création.</li>
  <li><strong>PME romande qui doit exister en français et en
  allemand</strong> — CHF 700 à 4 000, la traduction pesant plus que le
  design.</li>
  <li><strong>Commerce avec vente en ligne</strong> — CHF 3 000 à 15 000,
  et un vrai budget de temps pour le catalogue.</li>
</ul>

<p>Si vous hésitez entre deux fourchettes, la question utile n'est pas
«&nbsp;quel budget ai-je&nbsp;?&nbsp;» mais «&nbsp;combien vaut un client
pour moi&nbsp;?&nbsp;». Un cabinet dont un client vaut CHF 3 000 rentabilise
un site à CHF 5 000 avec deux clients. Un commerce dont le panier moyen
est de CHF 40 doit raisonner autrement.</p>

<h2>Trois questions qu'on nous pose</h2>

<h3>Un site à CHF 290, c'est possible ou c'est un appât ?</h3>
<p>C'est possible à trois conditions&nbsp;: une page et non huit, une
structure déjà éprouvée plutôt qu'une page blanche, et un brief que vous
remplissez vous-même. Retirez une de ces trois conditions et le prix
double. Notre <a href="../offres/pro-landing-page.html">Landing Pro</a>
dit exactement ce qu'elle contient et ce qu'elle ne contient pas.</p>

<h3>Pourquoi deux devis pour le même site varient du simple au triple ?</h3>
<p>Parce qu'ils ne décrivent pas le même travail. Comparez le nombre de
pages, le nombre de cycles de correction inclus, qui écrit les textes,
qui fournit les photos, et ce qui se passe si vous changez d'avis. Neuf
fois sur dix, l'écart est là et non dans le talent.</p>

<h3>Faut-il payer un abonnement mensuel ?</h3>
<p>Uniquement si vous recevez quelque chose chaque mois — des
modifications, une surveillance, un rapport. Un abonnement qui ne
finance que l'hébergement d'un site statique se remplace par une
dizaine de francs de domaine par an.</p>
""",
  "faq": [
    ("Combien coûte un site web pour une PME en Suisse ?",
     "Entre CHF 300 et CHF 30 000 selon le périmètre. Un forfait pour un "
     "site vitrine de une à sept pages se situe entre CHF 300 et CHF 1 500 ; "
     "un projet sur mesure avec fonctionnalités démarre autour de CHF 3 000."),
    ("Quels sont les frais annuels d'un site web ?",
     "Le nom de domaine (environ CHF 10 par an en .ch), l'hébergement (de "
     "gratuit pour un site statique à CHF 400 par an), les adresses e-mail "
     "professionnelles (CHF 60 à 150 par boîte et par an) et la maintenance "
     "si le site tourne sur un CMS."),
    ("Un forfait ferme est-il moins cher qu'un devis à l'heure ?",
     "Pas systématiquement, mais il est prévisible : le périmètre est écrit "
     "avant de commencer et un dépassement de temps est à la charge du "
     "prestataire."),
  ],
 },

 {
  "slug": "landing-page-ou-site-complet.html",
  "cat": "Décider",
  "titre": "Landing page ou site complet : comment choisir",
  "h1": ["Landing page ou site complet.", "Comment choisir."],
  "desc": "La question n'est pas le nombre de pages, c'est le nombre de "
          "décisions que votre visiteur doit prendre. Un test en trois "
          "questions.",
  "dek": "Une page unique n'est pas une version au rabais d'un site. "
         "C'est un outil différent, qui gagne dans certains cas et perd "
         "dans d'autres.",
  "lecture": "5 min",
  "corps": """
<p>On nous demande presque toujours «&nbsp;combien de pages me
faut-il&nbsp;?&nbsp;». C'est la mauvaise question&nbsp;: elle porte sur la
quantité alors que le problème est un problème de parcours. La bonne
question est <strong>combien de décisions différentes votre visiteur
doit-il prendre</strong> avant de vous contacter.</p>

<p>Une décision, une page. Plusieurs décisions, plusieurs pages.</p>

<h2>Quand une seule page suffit</h2>

<p>Une page unique fonctionne quand tous vos visiteurs veulent la même
chose, et qu'il n'y a qu'un seul geste au bout&nbsp;: appeler, réserver,
demander un devis.</p>

<ul>
  <li>Un artisan qui veut être appelé pour des chantiers.</li>
  <li>Un restaurant&nbsp;: la carte, les horaires, l'adresse, la réservation.</li>
  <li>Un cabinet ou un thérapeute avec une seule prestation principale.</li>
  <li>Une offre unique lancée pour une campagne, avec un formulaire au bout.</li>
</ul>

<p>Son avantage n'est pas le prix, c'est l'absence de choix. Sur une page
bien construite, le visiteur descend et arrive au formulaire. Sur un site
de huit pages, il erre dans le menu et sort. C'est aussi pour cela qu'une
page unique se met en ligne <a href="../index.html#process">en deux jours
ouvrés</a>&nbsp;: il y a moins à décider, donc moins à arbitrer.</p>

<h2>Quand il en faut plusieurs</h2>

<p>Plusieurs pages deviennent nécessaires dès qu'une de ces trois choses
est vraie.</p>

<p><strong>Vous avez plusieurs prestations qui ne parlent pas aux mêmes
personnes.</strong> Un fiduciaire qui fait de la comptabilité, de la
fiscalité et de la paie a trois publics. Une seule page les mélange et
n'en convainc aucun. Trois pages, chacune avec son vocabulaire, sont
aussi trois portes d'entrée pour Google&nbsp;: c'est la raison la plus
rentable d'ajouter des pages.</p>

<p><strong>Vous devez être trouvé sur des recherches différentes.</strong>
Google classe des pages, pas des sites. «&nbsp;Ferblantier Lausanne&nbsp;»
et «&nbsp;réparation de toiture Lausanne&nbsp;» méritent deux pages, sinon
vous vous positionnez à moitié sur les deux.</p>

<p><strong>La confiance demande de la place.</strong> Plus le panier est
élevé, plus le visiteur veut des références, des avis, une page
«&nbsp;à propos&nbsp;», parfois des conditions. Un achat à CHF 15 000 ne se
décide pas sur une page qui défile.</p>

<h2>Le test des trois questions</h2>

<ol>
  <li><strong>Combien de prestations différentes voulez-vous vendre&nbsp;?</strong>
  Une&nbsp;: une page. Deux à cinq&nbsp;: une page par prestation.</li>
  <li><strong>Combien de recherches Google différentes voulez-vous
  gagner&nbsp;?</strong> Comptez une page par recherche importante.</li>
  <li><strong>Votre visiteur a-t-il besoin de vérifier quelque chose avant
  de vous écrire&nbsp;?</strong> Si oui, prévoyez la page qui le lui
  permet — références, avis, équipe.</li>
</ol>

<p>Additionnez. Une page si le total est de un, cinq pages si le total
tourne autour de quatre ou cinq, sept si vous avez un vrai catalogue de
prestations. C'est exactement la logique de nos trois paliers&nbsp;:
<a href="../offres/pro-landing-page.html">Landing Pro</a> pour une page,
<a href="../offres/ultimate-website.html">Site Complet</a> jusqu'à cinq,
<a href="../offres/advanced-website.html">Site Étendu</a> jusqu'à sept et
en trois langues.</p>

<h2>L'erreur la plus fréquente</h2>

<p>Commander huit pages et n'en remplir que trois. Un site à moitié vide
inspire moins confiance qu'une page dense et finie, et il coûte plus
cher à produire comme à maintenir. Si vous n'avez pas le contenu
aujourd'hui, prenez moins de pages aujourd'hui.</p>

<p>L'erreur symétrique existe aussi&nbsp;: entasser cinq prestations sur
une page unique parce qu'elle coûtait moins cher. Le visiteur ne lit pas
la sixième section, et Google ne sait pas sur quoi vous positionner.</p>

<h2>Et si je me trompe ?</h2>

<p>Ce n'est pas grave, à deux conditions. La première&nbsp;: que le site
soit construit pour qu'on puisse lui ajouter une page sans le refaire.
La seconde&nbsp;: que <a href="../legal/conditions.html">votre nom de
domaine soit à votre nom</a> — c'est lui qui porte votre référencement,
pas le site.</p>

<p>Dans les faits, la plupart de nos clients commencent par une page,
regardent d'où viennent leurs appels pendant trois mois, puis ajoutent
les deux ou trois pages que les appels ont désignées. C'est moins
élégant qu'un plan parfait, et bien plus efficace.</p>

<p>Si vous hésitez encore, <a href="../devis.html">écrivez-nous les trois
réponses du test</a>&nbsp;: on vous dit lequel des trois paliers vous
convient, y compris quand la réponse est le moins cher.</p>
""",
  "faq": [
    ("Une landing page suffit-elle pour être visible sur Google ?",
     "Oui pour une recherche principale, non pour plusieurs. Google classe "
     "des pages : une page unique se positionne bien sur un sujet, mais ne "
     "peut pas couvrir « métier + ville » et trois prestations distinctes."),
    ("Peut-on ajouter des pages plus tard ?",
     "Oui, si le site a été construit pour cela. C'est le parcours le plus "
     "fréquent : commencer par une page, observer d'où viennent les appels "
     "pendant trois mois, puis ajouter les pages utiles."),
  ],
 },

 {
  "slug": "fiche-google-business.html",
  "cat": "Visibilité",
  "titre": "Fiche Google Business : le réglage que la plupart des PME ratent",
  "h1": ["Fiche Google Business&nbsp;:", "le réglage que tout le monde rate."],
  "desc": "La catégorie principale décide de la moitié de votre visibilité "
          "locale. Et presque personne ne la choisit correctement.",
  "dek": "Pour une PME locale, la fiche Google pèse souvent plus lourd que "
         "le site lui-même. Un seul champ y décide de l'essentiel.",
  "lecture": "6 min",
  "corps": """
<p>Si vous servez des clients dans un rayon de trente kilomètres, votre
fiche Google Business vous apporte probablement plus d'appels que votre
site. C'est elle qui s'affiche dans le bloc de carte, en haut, avant les
résultats classiques — et c'est gratuit.</p>

<p>Il y a un champ dans cette fiche qui pèse plus que tous les autres, et
que la majorité des PME romandes remplit de travers&nbsp;: la
<strong>catégorie principale</strong>.</p>

<h2>Le réglage raté</h2>

<p>Google vous demande une catégorie principale et autorise des
catégories secondaires. Presque tout le monde choisit la catégorie
principale de la façon la plus naturelle — celle qui décrit le métier
au sens large — et c'est exactement l'erreur.</p>

<p>La catégorie principale est ce qui détermine <em>pour quelles
recherches</em> Google envisage de vous afficher. Les secondaires n'ont
qu'un poids marginal. Donc&nbsp;:</p>

<ul>
  <li>Si vous êtes menuisier mais que 80&nbsp;% de votre chiffre vient des
  cuisines sur mesure, la catégorie principale doit être celle des
  cuisines, pas «&nbsp;Menuisier&nbsp;».</li>
  <li>Si vous êtes physiothérapeute spécialisé en sport, la catégorie
  sport passe en principale.</li>
  <li>Si vous êtes fiduciaire mais vendez surtout de la déclaration
  d'impôts aux particuliers, choisissez la catégorie fiscale.</li>
</ul>

<p>La bonne méthode est mécanique&nbsp;: tapez dans Google la recherche
que vous voulez gagner, regardez les trois fiches qui sortent dans le
bloc de carte, ouvrez-les, lisez leur catégorie principale. Prenez la
même. Vous n'avez pas à devinez ce que Google associe à quoi&nbsp;: il
vous le montre.</p>

<h2>Les champs qui bougent réellement le classement</h2>

<p>Le classement local repose sur trois piliers — la pertinence, la
distance et la notoriété. Vous n'agissez pas sur la distance. Restent
les champs suivants, par ordre d'effet observé&nbsp;:</p>

<ol>
  <li><strong>La catégorie principale</strong>, on vient de le voir.</li>
  <li><strong>Le nom exact de l'établissement.</strong> Mettez le nom
  réel, tel qu'il figure sur votre vitrine et vos factures. Y ajouter des
  mots-clés («&nbsp;Dupont Plomberie Genève Dépannage 24h&nbsp;») est
  contraire aux règles de Google et expose à une suspension.</li>
  <li><strong>Les prestations.</strong> Champ sous-exploité&nbsp;: on peut
  y lister ses prestations une par une, avec une description. Chaque
  entrée est un mot-clé de plus, légitime celle-là.</li>
  <li><strong>La zone desservie.</strong> Si vous vous déplacez, déclarez
  les communes. Si vous recevez, donnez une adresse et n'en déclarez pas.</li>
  <li><strong>Les horaires, y compris les jours fériés.</strong> Google
  affiche «&nbsp;horaires peut-être différents&nbsp;» quand ils ne sont pas
  confirmés, et ce doute coûte des appels.</li>
  <li><strong>Le lien du site.</strong> Pointez-le vers la page qui parle
  de la prestation concernée, pas systématiquement vers l'accueil.</li>
</ol>

<h2>Les photos : la règle des trois</h2>

<p>Les fiches qui convertissent ont au minimum&nbsp;: l'extérieur avec
l'enseigne visible (le client doit reconnaître l'endroit en arrivant),
l'intérieur, et le travail fini. Ajoutez-en quelques-unes par mois plutôt
que trente d'un coup&nbsp;: une fiche vivante est mieux traitée qu'une
fiche figée.</p>

<p>Évitez les images de banque d'images. Elles se repèrent, et elles
enlèvent précisément ce que la fiche est censée apporter&nbsp;: la preuve
que vous existez vraiment à cet endroit.</p>

<h2>Les avis, sans les mendier</h2>

<p>Le nombre d'avis et leur régularité comptent davantage que la note
moyenne. Une fiche à 4,6 avec un avis par mois passe devant une fiche à
5,0 figée depuis deux ans.</p>

<p>Ce qui marche, dans l'ordre&nbsp;: demander au bon moment (juste après
la fin du travail, jamais par une relance groupée), donner le lien court
de demande d'avis que Google génère dans votre tableau de bord, et
<strong>répondre à tous les avis</strong>, y compris les mauvais, en deux
lignes et sans se justifier. Les réponses sont lues par les prospects
bien plus que par les auteurs.</p>

<p>Ce qui ne marche pas&nbsp;: acheter des avis (détecté, et sanctionné
par la suppression de la fiche), en demander en échange d'une remise
(interdit), ou installer une tablette au comptoir qui collecte dix avis
depuis la même adresse IP.</p>

<h2>Ce qui fait chuter une fiche</h2>

<ul>
  <li>Une adresse ou un numéro différent de celui du site. Faites en sorte
  que nom, adresse et téléphone soient rigoureusement identiques
  partout&nbsp;: fiche, site, annuaires, réseaux.</li>
  <li>Des mots-clés entassés dans le nom de l'établissement.</li>
  <li>Une adresse de domicile déclarée comme boutique alors que vous ne
  recevez personne.</li>
  <li>Deux fiches pour le même établissement — cela arrive après un
  changement de raison sociale, et coupe votre notoriété en deux.</li>
  <li>Le silence. Une fiche qu'on ne touche jamais perd du terrain sur
  une fiche entretenue.</li>
</ul>

<h2>Et le site, alors ?</h2>

<p>La fiche apporte l'appel&nbsp;; le site fait la vente. Les prospects
qui hésitent ouvrent votre site depuis la fiche&nbsp;: s'il n'existe pas,
ou s'il date, vous perdez une partie de ce que la fiche vous a amené.
Les deux travaillent ensemble, et le plus rentable est de faire
correspondre la prestation vedette de la fiche avec une page dédiée du
site.</p>

<p>C'est ce que couvre <a href="../index.html#methode">La Méthode Client
Local</a>, le guide que nous remettons avec le
<a href="../offres/ultimate-website.html">Site Complet</a>&nbsp;: la fiche
Google, les recherches «&nbsp;métier + ville&nbsp;», et la manière de se
faire citer par ChatGPT quand quelqu'un cherche votre métier près de chez
lui.</p>
""",
  "faq": [
    ("Quelle catégorie principale choisir sur Google Business ?",
     "Celle de votre prestation la plus rentable, pas celle de votre métier "
     "au sens large. Méthode : tapez la recherche que vous voulez gagner, "
     "ouvrez les fiches qui sortent dans le bloc de carte et reprenez leur "
     "catégorie principale."),
    ("Peut-on ajouter des mots-clés au nom de son établissement ?",
     "Non. Les règles de Google exigent le nom réel de l'établissement ; "
     "ajouter des mots-clés expose à la suspension de la fiche."),
    ("La note moyenne compte-t-elle plus que le nombre d'avis ?",
     "Non. La régularité des avis et les réponses apportées pèsent "
     "davantage qu'une note parfaite obtenue il y a deux ans."),
  ],
 },

 {
  "slug": "que-mettre-sur-sa-page-d-accueil.html",
  "cat": "Rédaction",
  "titre": "Ce qu'il faut écrire sur sa page d'accueil",
  "h1": ["Ce qu'il faut écrire", "sur sa page d'accueil."],
  "desc": "Cinq secondes pour répondre à trois questions. Le plan d'une "
          "page d'accueil qui fait décrocher le téléphone, section par "
          "section.",
  "dek": "Votre visiteur accorde à votre page d'accueil le temps d'un feu "
         "rouge. Voici l'ordre dans lequel il veut ses réponses.",
  "lecture": "6 min",
  "corps": """
<p>Un visiteur qui arrive sur votre page d'accueil se pose trois
questions, dans cet ordre&nbsp;: <strong>où suis-je, est-ce pour moi,
et qu'est-ce que je fais maintenant&nbsp;?</strong> Il vous accorde
quelques secondes pour les trois. Tout ce qui ne sert pas ces réponses
peut descendre ou disparaître.</p>

<p>Voici ce que nous écrivons, dans l'ordre où nous l'écrivons.</p>

<h2>1. La phrase du haut</h2>

<p>Elle dit ce que vous faites, pour qui, et où. Rien d'autre. Elle ne
doit pas être belle, elle doit être exacte.</p>

<ul>
  <li>✗ «&nbsp;L'excellence au service de vos projets&nbsp;»</li>
  <li>✓ «&nbsp;Électricien à Nyon, dépannage le jour même&nbsp;»</li>
  <li>✗ «&nbsp;Réinventons ensemble votre communication&nbsp;»</li>
  <li>✓ «&nbsp;Logos et identités visuelles pour les PME romandes, en
  deux semaines&nbsp;»</li>
</ul>

<p>Test simple&nbsp;: montrez la phrase à quelqu'un qui ne connaît pas
votre métier. S'il ne peut pas répéter ce que vous vendez, elle est à
réécrire. Et si votre métier est local, mettez la ville dedans&nbsp;: ce
n'est pas du référencement, c'est de la politesse envers le visiteur.</p>

<h2>2. Le bouton, tout de suite</h2>

<p>Le premier appel à l'action se place dans le premier écran, à côté de
la phrase du haut. Certains visiteurs sont déjà décidés&nbsp;: ne les
faites pas défiler.</p>

<p>Un libellé qui dit ce qui va se passer convertit mieux qu'un libellé
vague. «&nbsp;Demander un devis&nbsp;» plutôt que «&nbsp;En savoir
plus&nbsp;». «&nbsp;Réserver une table&nbsp;» plutôt que
«&nbsp;Contact&nbsp;». Et un seul bouton principal&nbsp;: deux boutons de
même poids, c'est une décision de plus à prendre.</p>

<h2>3. Les trois raisons de rester</h2>

<p>Juste sous le premier écran, trois arguments courts. Pas dix. Ils
répondent à «&nbsp;est-ce pour moi&nbsp;?&nbsp;» et doivent être
<strong>vérifiables</strong>&nbsp;: un délai, un prix, une zone, une
garantie, un chiffre que vous pouvez prouver.</p>

<p>«&nbsp;Qualité, sérieux, réactivité&nbsp;» ne dit rien parce que
personne n'écrirait le contraire. «&nbsp;Devis sous 24 heures, prix ferme,
intervention dans le canton de Vaud&nbsp;» dit quelque chose.</p>

<h2>4. La preuve</h2>

<p>C'est la section la plus négligée et la plus rentable. Dans l'ordre de
puissance&nbsp;: des photos de votre travail réel, des avis nominatifs,
des logos de clients, des chiffres.</p>

<p>Une règle que nous appliquons à nous-mêmes&nbsp;: <strong>si vous ne
l'avez pas, ne l'inventez pas</strong>. Un faux avis se repère, et le jour
où il se repère il emporte tout le reste avec lui. Quand vous démarrez et
que vous n'avez encore rien à montrer, dites-le et remplacez la preuve par
la transparence&nbsp;: vos prix, votre méthode, vos conditions. Ça marche
mieux qu'on ne le croit.</p>

<h2>5. Les objections, avant qu'elles ne bloquent</h2>

<p>Votre visiteur a deux ou trois raisons de ne pas vous écrire.
«&nbsp;C'est sûrement trop cher.&nbsp;» «&nbsp;Ça va prendre des
mois.&nbsp;» «&nbsp;Je vais me retrouver coincé.&nbsp;» Traitez-les
explicitement, sur la page&nbsp;: un prix ou une fourchette, un délai,
ce qui se passe si ça ne va pas.</p>

<p>C'est contre-intuitif d'écrire un prix quand on croit que le prix fait
fuir. Dans les faits, l'absence de prix fait fuir davantage&nbsp;: elle
laisse le visiteur imaginer le pire et partir chez celui qui l'affiche.
C'est pour cette raison que <a href="../index.html#tarifs">nos trois
tarifs sont publics</a>.</p>

<h2>6. Le rappel de l'action</h2>

<p>Répétez l'appel à l'action en bas, et donnez-en deux formes&nbsp;: un
formulaire pour ceux qui écrivent, un numéro ou un WhatsApp pour ceux qui
préfèrent parler. Ajoutez ce que vous faites de la demande&nbsp;: «&nbsp;on
répond le jour même, du lundi au vendredi&nbsp;». Le visiteur veut savoir
dans quoi il s'engage.</p>

<h2>Ce qu'il faut enlever</h2>

<ul>
  <li><strong>Le mot «&nbsp;Bienvenue&nbsp;».</strong> Il occupe la ligne
  la plus lue de la page pour ne rien dire.</li>
  <li><strong>L'histoire de l'entreprise, en haut.</strong> Elle
  intéresse, mais après. Sa place est une page «&nbsp;à propos&nbsp;».</li>
  <li><strong>Le carrousel qui défile tout seul.</strong> Personne ne voit
  la troisième image, et il ralentit la page.</li>
  <li><strong>Les images de banque d'images.</strong> Une photo de votre
  atelier prise au téléphone vaut mieux qu'un décor de bureau américain.</li>
  <li><strong>Les longs paragraphes.</strong> Deux ou trois phrases,
  jamais plus, et des sous-titres qui se lisent seuls.</li>
</ul>

<h2>Le test final</h2>

<p>Faites lire votre page d'accueil sur un téléphone à une personne
extérieure, chronomètre en main, pendant cinq secondes. Puis demandez-lui
ce que vous vendez, à qui, et ce qu'elle ferait pour vous contacter. Si
les trois réponses sortent, la page est bonne. Sinon, ce n'est pas le
design qu'il faut changer, c'est l'ordre des sections.</p>

<p>Nous posons ces questions dans notre <a href="../brief.html">brief de
départ</a>&nbsp;: c'est la partie qui prend le plus de temps aux clients,
et celle qui fait toute la différence sur le résultat.</p>
""",
  "faq": [
    ("Faut-il afficher ses prix sur son site ?",
     "Dans la grande majorité des cas, oui — au moins une fourchette. "
     "L'absence de prix fait partir le visiteur vers un concurrent qui "
     "l'affiche, et fait perdre du temps en demandes hors budget."),
    ("Quelle est la première chose à écrire sur une page d'accueil ?",
     "Une phrase qui dit ce que vous faites, pour qui et où. Si une "
     "personne extérieure à votre métier ne peut pas la répéter, elle est "
     "à réécrire."),
  ],
 },

 {
  "slug": "wix-squarespace-ou-sur-mesure.html",
  "cat": "Comparer",
  "titre": "Wix, Squarespace ou sur mesure : le comparatif honnête",
  "h1": ["Wix, Squarespace", "ou sur mesure&nbsp;?"],
  "desc": "Ce que chaque solution fait très bien, là où chacune coince, et "
          "le coût réel sur trois ans pour une PME suisse.",
  "dek": "Nous sommes juges et parties : nous vendons du sur-mesure. "
         "Raison de plus pour dire précisément dans quels cas les "
         "constructeurs en ligne sont le bon choix.",
  "lecture": "7 min",
  "corps": """
<p>Autant le dire d'entrée&nbsp;: nous vendons des sites faits à la main.
Un comparatif écrit par nous n'est donc pas neutre. Nous allons quand
même essayer d'être exacts, parce qu'il y a de vrais cas où un
constructeur en ligne est la meilleure décision, et que vous perdriez
votre argent chez nous.</p>

<h2>Ce que Wix fait très bien</h2>

<ul>
  <li><strong>Démarrer aujourd'hui sans personne.</strong> Vous pouvez
  avoir un site en ligne dans l'après-midi, seul, sans compétence.</li>
  <li><strong>Tout au même endroit.</strong> Domaine, hébergement,
  certificat, formulaires, boutique, réservation, newsletter&nbsp;: une
  seule facture, un seul mot de passe.</li>
  <li><strong>Modifier soi-même, vraiment.</strong> L'éditeur est très
  permissif&nbsp;: on déplace un élément où l'on veut.</li>
  <li><strong>Les fonctions de métier.</strong> Prise de rendez-vous,
  planning de cours, réservation&nbsp;: disponibles en quelques clics,
  alors que les redévelopper coûterait des milliers de francs.</li>
</ul>

<h2>Ce que Squarespace fait très bien</h2>

<ul>
  <li><strong>Le résultat visuel par défaut.</strong> Les gabarits sont
  plus soignés et plus difficiles à casser. Pour un photographe, un
  architecte, un restaurant, le rendu est bon sans direction
  artistique.</li>
  <li><strong>La cohérence.</strong> Le système de styles global évite
  le site qui part dans douze directions au bout de six mois.</li>
  <li><strong>La vente de petits catalogues.</strong> Une vingtaine de
  produits ou quelques prestations&nbsp;: c'est propre et suffisant.</li>
</ul>

<h2>Là où les deux coincent</h2>

<p><strong>La vitesse.</strong> Ces plateformes chargent beaucoup de code
pour rester modifiables dans le navigateur. Sur un téléphone en 4G, cela
se voit. La vitesse est un critère de classement Google, et surtout un
critère d'abandon&nbsp;: le visiteur ferme avant d'avoir vu votre
offre.</p>

<p><strong>La sortie.</strong> C'est le point le plus sérieux et le moins
discuté. Vous ne pouvez pas emporter votre site&nbsp;: on récupère
généralement ses textes, ses images et son nom de domaine, mais pas la
mise en page. Changer de plateforme, c'est refaire. L'abonnement n'est
donc pas seulement un loyer, c'est un coût de sortie qui grandit avec le
temps.</p>

<p><strong>Le référencement fin.</strong> L'essentiel est accessible
(titres, descriptions, adresses de pages). Ce qui l'est moins&nbsp;: le
contrôle précis du balisage, des données structurées avancées, de la
gestion du multilingue. Pour un site local, ça passe. Pour une stratégie
de contenu ambitieuse, ça freine.</p>

<p><strong>Le multilingue.</strong> Possible, mais c'est souvent la partie
la plus pénible — et en Suisse romande, c'est rarement optionnel.</p>

<p><strong>Le prix qui monte.</strong> Le tarif d'appel ne comprend
presque jamais ce qu'il vous faut. Les fonctions utiles (boutique,
réservation, suppression de la publicité, adresses e-mail) sont sur des
paliers supérieurs, et les paliers augmentent avec les années.</p>

<h2>Ce que le sur-mesure fait très bien</h2>

<ul>
  <li><strong>La vitesse.</strong> Un site statique bien construit se
  charge quasi instantanément et n'a besoin d'aucun entretien
  technique.</li>
  <li><strong>Vous appartenir.</strong> Les fichiers sont à vous, chez
  l'hébergeur que vous voulez, et transférables ailleurs.</li>
  <li><strong>Dire exactement ce que vous voulez dire.</strong> Aucun
  gabarit à contourner.</li>
  <li><strong>Le coût de fonctionnement.</strong> Souvent le prix du
  domaine, et rien d'autre.</li>
</ul>

<p>Et ses limites, qui sont réelles&nbsp;: vous dépendez de quelqu'un pour
les modifications lourdes, il faut un brief au départ, et les
fonctionnalités de métier (réservation, agenda, boutique) sont un budget
séparé au lieu d'être incluses.</p>

<h2>Le coût réel sur trois ans</h2>

<p>À titre d'ordre de grandeur, pour une PME romande, aux prix constatés
en 2026 — les tarifs des plateformes évoluent, vérifiez-les&nbsp;:</p>

<ul>
  <li><strong>Constructeur en ligne, formule qui convient à une
  entreprise</strong> — autour de CHF 20 à 35 par mois, soit
  <strong>CHF 720 à 1 260 sur trois ans</strong>, plus votre temps de
  fabrication, plus les paliers si vous ajoutez la boutique ou les
  e-mails.</li>
  <li><strong>Forfait fait à la main</strong> — CHF 290 à 690 une fois,
  plus une dizaine de francs de domaine par an, soit
  <strong>CHF 320 à 720 sur trois ans</strong>.</li>
  <li><strong>Sur-mesure d'agence</strong> — CHF 5 000 et plus, justifié
  quand le site est un canal de vente principal.</li>
</ul>

<p>Sur trois ans, l'écart entre un abonnement et un forfait est donc
faible&nbsp;; sur six ans, il s'inverse nettement. Ce qui départage
n'est pas le prix&nbsp;: c'est la propriété et la vitesse.</p>

<h2>Comment choisir, en trois cas</h2>

<p><strong>Prenez un constructeur en ligne</strong> si vous avez besoin
d'une réservation ou d'un agenda tout de suite, si vous prévoyez de
modifier votre site chaque semaine vous-même, ou si vous testez une
activité dont vous ne savez pas encore si elle tiendra.</p>

<p><strong>Prenez un forfait fait à la main</strong> si votre site doit
surtout convaincre et faire décrocher un téléphone, si vous ne voulez pas
d'abonnement, ou si votre visibilité locale compte plus que la liberté de
tout déplacer.</p>

<p><strong>Prenez une agence</strong> si votre site est le canal de vente
principal et qu'un point de conversion gagné se chiffre en dizaines de
milliers de francs.</p>

<h2>Une chose à faire dans tous les cas</h2>

<p>Achetez votre nom de domaine à votre nom, sur un compte qui vous
appartient, quelle que soit la solution retenue. C'est le seul élément
irremplaçable&nbsp;: un site se refait, une adresse qui a dix ans
d'historique, non. Si votre domaine est aujourd'hui au nom d'un
prestataire, <a href="recuperer-son-nom-de-domaine.html">voici comment le
récupérer</a>.</p>

<p>Et si vous voulez savoir dans quel cas vous tombez, <a
href="../devis.html">décrivez-nous votre situation en trois
lignes</a>&nbsp;: on vous le dit, y compris quand la réponse est
«&nbsp;prenez un abonnement, ça vous suffira&nbsp;».</p>
""",
  "faq": [
    ("Peut-on récupérer son site en quittant Wix ou Squarespace ?",
     "On récupère ses textes, ses images et son nom de domaine, mais pas la "
     "mise en page : changer de plateforme implique de refaire le site."),
    ("Un site sur mesure est-il plus rapide qu'un site Wix ?",
     "En général oui : un site statique fait à la main charge beaucoup moins "
     "de code, parce qu'il n'a pas à rester modifiable dans un éditeur en "
     "ligne."),
    ("Quelle solution coûte le moins cher sur trois ans ?",
     "Un forfait unique avec un simple nom de domaine à entretenir reste "
     "généralement sous le total d'un abonnement mensuel sur trois ans, et "
     "l'écart se creuse ensuite."),
  ],
 },

 {
  "slug": "sept-sections-landing-page.html",
  "cat": "Conversion",
  "titre": "Les 7 sections d'une landing page qui convertit",
  "h1": ["Les sept sections", "d'une page qui convertit."],
  "desc": "L'ordre qui fonctionne, section par section, avec ce qu'il faut "
          "écrire dans chacune et l'erreur à ne pas y commettre.",
  "dek": "Une page qui convertit n'est pas une page qui persuade. C'est "
         "une page qui répond aux objections dans l'ordre où elles "
         "arrivent.",
  "lecture": "6 min",
  "corps": """
<p>Une page unique dont le seul but est de faire accomplir un geste —
appeler, réserver, remplir un formulaire — suit presque toujours le même
plan. Non par paresse, mais parce que les objections d'un visiteur
arrivent dans un ordre assez stable.</p>

<p>Voici les sept sections, l'objection que chacune traite, et l'erreur
que nous voyons le plus souvent.</p>

<h2>1. L'accroche</h2>

<p><em>Objection traitée&nbsp;: «&nbsp;est-ce que je suis au bon
endroit&nbsp;?&nbsp;»</em></p>

<p>Ce que vous faites, pour qui, où, et un bouton. Une phrase, un
sous-titre d'une ligne, un appel à l'action. C'est tout ce qui devrait
tenir dans le premier écran d'un téléphone.</p>

<p><strong>L'erreur&nbsp;:</strong> une phrase d'ambiance
(«&nbsp;Donnons vie à vos idées&nbsp;») qui oblige le visiteur à défiler
pour comprendre votre métier. Il ne défile pas&nbsp;: il repart.</p>

<h2>2. Les trois points d'appui</h2>

<p><em>Objection traitée&nbsp;: «&nbsp;pourquoi vous&nbsp;?&nbsp;»</em></p>

<p>Trois arguments vérifiables, courts, alignés. Un délai, un prix, une
zone, une garantie. Trois, parce que deux paraît maigre et cinq ne se
lit plus.</p>

<p><strong>L'erreur&nbsp;:</strong> des qualités que personne ne
revendiquerait à l'envers. «&nbsp;Sérieux, qualité, écoute&nbsp;» n'est
pas un argument, c'est un minimum.</p>

<h2>3. La preuve</h2>

<p><em>Objection traitée&nbsp;: «&nbsp;est-ce que ça marche
vraiment&nbsp;?&nbsp;»</em></p>

<p>Photos de travaux réels, avis signés, logos, chiffres. Placez-la tôt —
juste après les points d'appui — parce que c'est elle qui autorise le
visiteur à lire la suite.</p>

<p><strong>L'erreur&nbsp;:</strong> inventer. Un avis fabriqué se repère
à son vocabulaire, et il détruit la crédibilité de toute la page. Si vous
démarrez, remplacez la preuve par de la transparence&nbsp;: méthode,
prix, conditions. Nous faisons exactement cela sur ce site&nbsp;: nos
<a href="../temoignages.html">avis</a> sont ceux que nous avons, et pas
un de plus.</p>

<h2>4. Le comment</h2>

<p><em>Objection traitée&nbsp;: «&nbsp;dans quoi je m'engage&nbsp;?&nbsp;»</em></p>

<p>Trois ou quatre étapes numérotées&nbsp;: ce que vous faites, ce que le
client fait, combien de temps ça prend. Cette section rassure énormément
pour un coût de rédaction quasi nul, et c'est la plus souvent oubliée.</p>

<p><strong>L'erreur&nbsp;:</strong> décrire votre processus interne. Le
visiteur veut savoir ce qui va lui arriver à lui, pas comment vous
organisez vos dossiers.</p>

<h2>5. Le prix</h2>

<p><em>Objection traitée&nbsp;: «&nbsp;est-ce dans mon
budget&nbsp;?&nbsp;»</em></p>

<p>Un prix, une fourchette, ou à tout le moins un point de repère
(«&nbsp;à partir de&nbsp;», «&nbsp;la plupart de nos chantiers sont
entre X et Y&nbsp;»). Dites aussi ce qui est compris et ce qui ne l'est
pas.</p>

<p><strong>L'erreur&nbsp;:</strong> «&nbsp;devis sur demande&nbsp;». Le
visiteur ne demande pas&nbsp;: il suppose que c'est cher et il va voir
ailleurs. Et vous recevez des demandes hors budget qui vous coûtent du
temps. Nos <a href="../index.html#tarifs">trois tarifs</a> sont publics
pour cette seule raison.</p>

<h2>6. Les objections restantes</h2>

<p><em>Objection traitée&nbsp;: «&nbsp;oui mais si…&nbsp;»</em></p>

<p>Une petite FAQ de quatre à six questions, qui reprend ce qu'on vous
demande vraiment au téléphone. Écrivez les vraies questions, y compris
gênantes&nbsp;: «&nbsp;et si je ne suis pas satisfait&nbsp;?&nbsp;»,
«&nbsp;qui est propriétaire du site&nbsp;?&nbsp;», «&nbsp;que se passe-t-il
si vous disparaissez&nbsp;?&nbsp;».</p>

<p><strong>L'erreur&nbsp;:</strong> une FAQ de complaisance qui pose des
questions dont la réponse vous arrange. Elle ne traite aucun frein et
occupe de la place.</p>

<h2>7. La dernière action</h2>

<p><em>Objection traitée&nbsp;: «&nbsp;qu'est-ce que je fais
maintenant&nbsp;?&nbsp;»</em></p>

<p>Le même appel à l'action qu'en haut, avec deux canaux&nbsp;: un
formulaire court et un moyen de parler à quelqu'un. Précisez le délai de
réponse. Et gardez le formulaire court&nbsp;: chaque champ supplémentaire
fait perdre des envois. Nom, moyen de contact, deux lignes de message
suffisent presque toujours.</p>

<p><strong>L'erreur&nbsp;:</strong> un formulaire de douze champs qui
demande le chiffre d'affaires et le nombre d'employés avant même le
premier échange.</p>

<h2>Ce qui compte plus que l'ordre</h2>

<ul>
  <li><strong>La vitesse.</strong> Une page lente perd des visiteurs avant
  la section&nbsp;2. C'est la première chose à corriger, avant toute
  réécriture.</li>
  <li><strong>Le téléphone d'abord.</strong> La majorité de vos visiteurs
  sont sur mobile. Concevez pour l'écran de téléphone, vérifiez ensuite
  sur ordinateur.</li>
  <li><strong>Un seul geste.</strong> Une page qui propose d'appeler,
  d'écrire, de s'abonner, de télécharger et de suivre sur Instagram ne
  fait rien accomplir du tout.</li>
</ul>

<p>C'est ce plan que nous appliquons sur la
<a href="../offres/pro-landing-page.html">Landing Pro</a>&nbsp;: cinq
sections au minimum, sept quand le contenu le justifie, et jamais deux
boutons principaux qui se disputent la même page.</p>
""",
  "faq": [
    ("Combien de sections faut-il sur une landing page ?",
     "Cinq au minimum, sept quand le contenu le justifie. Ce qui compte est "
     "que chaque section traite une objection réelle, dans l'ordre où elle "
     "se présente."),
    ("Combien de champs mettre dans le formulaire ?",
     "Le moins possible : un nom, un moyen de contact et deux lignes de "
     "message suffisent presque toujours. Chaque champ supplémentaire fait "
     "perdre des envois."),
  ],
 },

 {
  "slug": "photos-professionnelles-site-web.html",
  "cat": "Photographie",
  "titre": "Photos : quand une séance pro change vraiment quelque chose",
  "h1": ["Photos&nbsp;: quand une séance", "change vraiment quelque chose."],
  "desc": "Les trois cas où une séance photo est rentable, les trois où "
          "elle ne l'est pas, et le brief à donner au photographe.",
  "dek": "Une séance coûte entre CHF 400 et CHF 1 500 en Suisse. Parfois "
         "c'est le meilleur franc dépensé du projet, parfois c'est un "
         "franc perdu.",
  "lecture": "5 min",
  "corps": """
<p>La photo est le poste où l'on hésite le plus, parce qu'il est visible
et qu'il n'est pas indispensable. Une séance professionnelle se négocie,
en Suisse, entre CHF 400 pour une demi-journée avec un jeune photographe
et CHF 1 500 pour une journée complète avec retouches. Voici comment
savoir si c'est votre cas.</p>

<h2>Ce que la photo change réellement</h2>

<p>Elle ne rend pas votre offre meilleure. Elle fait deux choses&nbsp;:
elle <strong>prouve que vous existez</strong>, et elle
<strong>montre le niveau de finition</strong> de votre travail. C'est tout
— et selon les métiers, c'est énorme ou négligeable.</p>

<h2>Les trois cas où une séance est rentable</h2>

<p><strong>1. Votre travail se voit.</strong> Coiffure, cuisine,
menuiserie, aménagement, carrosserie, esthétique, paysagisme, fleurs.
La photo <em>est</em> l'argument de vente. Ici, de mauvaises photos
coûtent plus cher que pas de photos, et une séance est le premier
investissement à faire, avant même le site.</p>

<p><strong>2. On achète une personne.</strong> Thérapeute, avocat,
coach, courtier, notaire, médecin. Un portrait correct — regard caméra,
lumière douce, fond neutre — augmente franchement le taux de prise de
contact. Pas besoin d'une journée&nbsp;: une heure suffit, et c'est le
meilleur rapport qualité-prix de toute la liste.</p>

<p><strong>3. Votre lieu est un argument.</strong> Restaurant, hôtel,
salon, cabinet, boutique. Le client veut voir où il met les pieds. Ici
la séance doit se faire à l'heure où le lieu est le plus beau, ce qui
suppose de bloquer un créneau.</p>

<h2>Les trois cas où ce n'est pas la priorité</h2>

<p><strong>1. Votre travail est invisible.</strong> Informatique,
comptabilité, conseil, assurance, traduction. Photographier des gens qui
sourient devant un ordinateur n'ajoute rien. Mettez l'argent dans le
texte, dans les références clients et dans la fiche Google.</p>

<p><strong>2. Vous vendez un produit que le fabricant a déjà
photographié.</strong> Utilisez ses visuels&nbsp;: ils sont souvent
meilleurs et fournis, vérifiez simplement que vous avez le droit de les
employer.</p>

<p><strong>3. Vous ne savez pas encore ce que vous vendez.</strong> Si
votre offre va bouger dans six mois, les photos aussi. Commencez au
téléphone&nbsp;: vous ferez la séance quand l'offre sera stable.</p>

<h2>Ce qu'un téléphone fait très bien</h2>

<p>Un téléphone récent, à la bonne heure, donne de très bons résultats.
Trois règles suffisent&nbsp;:</p>

<ul>
  <li><strong>La lumière du jour, jamais le flash.</strong> Placez le
  sujet face à une fenêtre, pas dos à elle. Dehors, évitez le plein
  soleil de midi&nbsp;: la fin de journée est plus flatteuse.</li>
  <li><strong>Nettoyez le cadre.</strong> Le câble qui traîne, le carton,
  la poubelle. Nettoyer le fond fait plus pour une photo que n'importe
  quel filtre.</li>
  <li><strong>Cadrez large et horizontal.</strong> On recadre toujours en
  moins, jamais en plus. Une photo verticale ne rentre pas dans une
  bannière de site.</li>
</ul>

<p>Gardez les fichiers d'origine&nbsp;: une capture d'écran d'une photo,
ou une image qui a fait trois fois le tour de WhatsApp, arrive
irrécupérable.</p>

<h2>Le brief à donner au photographe</h2>

<p>La différence entre une séance utile et une séance jolie tient à ce
qu'on demande avant. Six lignes suffisent&nbsp;:</p>

<ol>
  <li>À quoi les images vont servir — site, fiche Google, réseaux — et
  dans quels formats.</li>
  <li>Trois images obligatoires (par exemple&nbsp;: la façade avec
  l'enseigne lisible, l'équipe, un travail terminé).</li>
  <li>Une <strong>image très large et horizontale</strong> pour le haut
  de la page d'accueil, avec de l'espace vide sur un côté&nbsp;: c'est là
  que le texte se posera.</li>
  <li>Le style&nbsp;: deux ou trois exemples de sites que vous aimez,
  cela vaut mieux qu'une page d'adjectifs.</li>
  <li>Les droits&nbsp;: usage web illimité dans le temps, et écrit.</li>
  <li>La livraison&nbsp;: fichiers d'origine en pleine résolution, plus
  une version allégée pour le web.</li>
</ol>

<p>Ce dernier point compte&nbsp;: des images de 8 Mo livrées telles quelles
sur un site le rendent lent, et un site lent perd des visiteurs. Nous
redimensionnons et compressons systématiquement ce que nos clients nous
envoient, mais autant partir des bons fichiers.</p>

<h2>Combien y consacrer</h2>

<ul>
  <li><strong>Portrait seul</strong> — CHF 150 à 400 pour une heure. À
  faire dès que votre visage est votre offre.</li>
  <li><strong>Demi-journée sur place</strong> — CHF 400 à 800. Suffit
  pour un commerce, un salon, un cabinet.</li>
  <li><strong>Journée complète</strong> — CHF 900 à 1 500. Justifiée quand
  il faut couvrir plusieurs prestations ou plusieurs lieux.</li>
</ul>

<p>Un repère utile&nbsp;: si votre site coûte CHF 500 et vos photos
CHF 1 200, ce n'est pas absurde — dans les métiers visuels, la photo
travaille plus que la mise en page. L'inverse l'est parfois davantage.</p>

<p>Si votre identité visuelle est à reprendre en même temps (logo,
couleurs, déclinaisons), c'est le bon moment&nbsp;: c'est l'objet du
<a href="../upsell-branding.html">Pack Branding</a>, et cela évite de
photographier une enseigne que vous allez changer trois mois plus tard.</p>
""",
  "faq": [
    ("Une séance photo professionnelle est-elle indispensable ?",
     "Non. Elle est déterminante dans les métiers où le travail se voit "
     "(coiffure, cuisine, aménagement) et dans ceux où l'on achète une "
     "personne. Elle est secondaire pour les services immatériels."),
    ("Combien coûte une séance photo en Suisse ?",
     "De CHF 150 à 400 pour un portrait d'une heure, CHF 400 à 800 pour une "
     "demi-journée sur place, CHF 900 à 1 500 pour une journée complète "
     "avec retouches."),
  ],
 },

 {
  "slug": "premier-client-via-son-site.html",
  "cat": "Attentes",
  "titre": "Combien de temps avant le premier client via son site ?",
  "h1": ["Combien de temps avant", "le premier client&nbsp;?"],
  "desc": "Ce qui se passe semaine après semaine après une mise en ligne, "
          "les trois sources de trafic et leur vitesse respective.",
  "dek": "Un site n'est pas un interrupteur. Selon la source de trafic "
         "que vous activez, le premier client arrive en trois jours ou "
         "en cinq mois.",
  "lecture": "6 min",
  "corps": """
<p>C'est la question qu'on nous pose juste après le prix, et la réponse
honnête est&nbsp;: cela ne dépend presque pas du site. Cela dépend de la
manière dont les gens y arrivent. Il y a trois routes, et elles n'ont
pas du tout la même vitesse.</p>

<h2>Les trois sources, et leur délai</h2>

<p><strong>Le trafic que vous amenez vous-même — immédiat.</strong> Vous
mettez l'adresse dans votre signature d'e-mail, sur vos devis, sur votre
véhicule, dans votre bio Instagram, et vous l'envoyez à vos contacts.
Premier effet en quelques jours. C'est la source la plus sous-estimée et
la seule qui soit gratuite et instantanée.</p>

<p><strong>La publicité — quelques jours.</strong> Google Ads, Meta, et
désormais les annonces dans les assistants de type ChatGPT. Vous payez,
vous avez des visiteurs demain. C'est la seule façon d'avoir du volume
tout de suite, et cela s'arrête le jour où vous arrêtez de payer.</p>

<p><strong>Le référencement naturel — deux à six mois.</strong> Google
doit découvrir vos pages, les évaluer, puis vous faire remonter. Pour une
recherche locale peu concurrentielle («&nbsp;serrurier Morges&nbsp;»),
comptez six à dix semaines. Pour une recherche disputée, six mois et
plus. Aucun prestataire sérieux ne vous promettra mieux.</p>

<h2>Ce qui se passe, semaine par semaine</h2>

<p><strong>Semaines 1 et 2.</strong> Le site est en ligne. Vos visiteurs
sont ceux que vous amenez&nbsp;: proches, clients existants, contacts.
Les premières demandes viennent souvent de clients que vous aviez déjà —
ils découvrent une prestation qu'ils ignoraient. C'est un vrai gain, et
personne ne le compte.</p>

<p><strong>Semaines 3 à 6.</strong> Google a indexé les pages. Vous
commencez à apparaître sur votre propre nom, puis sur des recherches très
précises. Le volume est faible mais la qualité est haute&nbsp;: quelqu'un
qui tape «&nbsp;réparation volet roulant Chêne-Bougeries&nbsp;» vous
appelle presque toujours.</p>

<p><strong>Mois 2 et 3.</strong> Si votre fiche Google Business est bien
réglée, elle devient votre première source d'appels, devant le site.
Les deux travaillent ensemble&nbsp;: la fiche amène, le site convainc.
C'est le moment où l'on voit si les pages disent les bonnes choses.</p>

<p><strong>Mois 4 à 6.</strong> Le référencement des pages de prestations
se met en place. Si vous avez publié un peu de contenu et récolté quelques
avis, la courbe se redresse nettement. C'est aussi le moment où l'on sait
quelles pages ajouter&nbsp;: les demandes vous l'ont dit.</p>

<h2>Ce qui accélère vraiment</h2>

<ul>
  <li><strong>Une fiche Google Business complète.</strong> Effet en
  quelques jours et gratuit. C'est le levier n°1 pour une PME locale —
  <a href="fiche-google-business.html">le réglage à ne pas rater</a>.</li>
  <li><strong>Mettre l'adresse partout.</strong> Signature, devis,
  factures, véhicule, vitrine, réseaux. Cela ne coûte rien et double
  souvent le trafic du premier mois.</li>
  <li><strong>Une page par prestation.</strong> Cinq pages précises se
  positionnent bien mieux qu'une page qui parle de tout.</li>
  <li><strong>Les avis, régulièrement.</strong> Un par mois vaut mieux que
  dix d'un coup.</li>
  <li><strong>Un petit budget publicitaire au démarrage.</strong> CHF 200
  à 500 sur trois semaines suffisent pour savoir si votre page convertit,
  ce qui est une information qu'on n'obtient pas autrement.</li>
</ul>

<h2>Ce qui ralentit</h2>

<ul>
  <li><strong>Un site lent.</strong> Les visiteurs partent avant de lire
  l'offre&nbsp;; le référencement en souffre aussi.</li>
  <li><strong>Pas de prix, pas de zone, pas de délai.</strong> Le
  visiteur ne demande pas, il suppose, et il part.</li>
  <li><strong>Attendre d'avoir tout.</strong> Un site en ligne qui se
  complète bat un site parfait dans six mois.</li>
  <li><strong>Changer de nom de domaine.</strong> Vous repartez de zéro.
  Choisissez-le une fois et gardez-le.</li>
</ul>

<h2>Ce qu'il faut mesurer</h2>

<p>Trois chiffres, une fois par mois, dix minutes&nbsp;:</p>

<ol>
  <li><strong>Combien de visiteurs</strong>, et d'où ils viennent
  (recherche, réseaux, direct).</li>
  <li><strong>Combien de demandes</strong> — formulaires, appels,
  WhatsApp.</li>
  <li><strong>Combien de clients</strong> issus de ces demandes.</li>
</ol>

<p>Le rapport entre le premier et le deuxième chiffre juge votre page.
Le rapport entre le deuxième et le troisième juge votre offre et votre
manière de répondre. Deux problèmes différents&nbsp;: ne corrigez pas le
site quand c'est le devis qui pose problème.</p>

<h2>Un repère honnête</h2>

<p>Pour une PME locale romande avec une fiche Google correctement réglée,
un site clair et de l'adresse mise partout&nbsp;: <strong>les premières
demandes arrivent en général dans les deux à quatre semaines</strong>,
et le site devient une source régulière autour du troisième au sixième
mois. Sans fiche Google, sans avis et sans adresse diffusée, ce peut être
beaucoup plus long — et ce n'est alors pas un problème de site.</p>

<p>Si vous voulez le plan des trente premiers jours après la mise en
ligne, il fait partie de <a href="../index.html#methode">La Méthode Client
Local</a> que nous remettons avec le
<a href="../offres/ultimate-website.html">Site Complet</a>.</p>
""",
  "faq": [
    ("Combien de temps pour être visible sur Google après une mise en ligne ?",
     "Quelques jours pour être indexé, six à dix semaines pour se "
     "positionner sur une recherche locale peu concurrentielle, six mois et "
     "plus sur une recherche disputée."),
    ("Quand arrive la première demande via un site ?",
     "En général dans les deux à quatre semaines pour une PME locale qui "
     "diffuse son adresse et dispose d'une fiche Google Business correctement "
     "réglée."),
  ],
 },

 {
  "slug": "recuperer-son-nom-de-domaine.html",
  "cat": "Pratique",
  "titre": "Récupérer son nom de domaine en cinq étapes",
  "h1": ["Récupérer son nom", "de domaine en cinq étapes."],
  "desc": "Votre domaine est au nom de votre ancien prestataire ? Voici la "
          "procédure exacte, et ce qu'il faut faire s'il ne répond plus.",
  "dek": "Le nom de domaine est le seul élément de votre présence en ligne "
         "qui ne se refait pas. S'il n'est pas à votre nom, c'est la "
         "première chose à corriger.",
  "lecture": "6 min",
  "corps": """
<p>Un site se reconstruit. Un nom de domaine qui a huit ans d'historique,
des liens entrants et vos adresses e-mail, non. C'est pour cette raison
que nous achetons toujours le domaine au nom du client et que nos
<a href="../legal/conditions.html">conditions générales</a> prévoient son
transfert sur simple demande et sans frais.</p>

<p>Tous les prestataires ne fonctionnent pas ainsi. Si le vôtre détient
votre domaine, voici la marche à suivre.</p>

<h2>Étape 1 — Savoir où il est et à qui il est</h2>

<p>Deux choses à distinguer&nbsp;: le <strong>titulaire</strong> (le
propriétaire légal) et le <strong>registrar</strong> (l'entreprise chez
qui le domaine est enregistré).</p>

<p>Pour un <code>.ch</code>, l'annuaire public du registre suisse
(<em>whois</em> de SWITCH, via nic.ch) vous donne le registrar. Pour un
<code>.com</code>, la recherche whois de l'ICANN. Les coordonnées du
titulaire sont souvent masquées pour des raisons de protection des
données, mais le registrar, lui, est toujours visible — et c'est ce dont
vous avez besoin.</p>

<p>Notez aussi la <strong>date d'expiration</strong>. Si elle est dans
moins de quinze jours, traitez le dossier en urgence&nbsp;: un domaine
expiré peut être racheté par n'importe qui.</p>

<h2>Étape 2 — Demander le transfert, par écrit</h2>

<p>Écrivez au prestataire un message court, factuel, en demandant
explicitement ces trois éléments&nbsp;:</p>

<ul>
  <li>le <strong>code d'autorisation de transfert</strong> (appelé code
  auth, code EPP ou <em>authcode</em>)&nbsp;;</li>
  <li>le <strong>déverrouillage</strong> du domaine (le <em>transfer
  lock</em>)&nbsp;;</li>
  <li>le passage du titulaire à votre nom, si le domaine n'est pas déjà
  à votre nom.</li>
</ul>

<p>Fixez une échéance raisonnable — dix jours ouvrables — et gardez une
trace écrite. Dans la grande majorité des cas, cela suffit&nbsp;: la
plupart des prestataires n'ont aucune envie de garder en otage le domaine
d'un client qui part.</p>

<h2>Étape 3 — Ouvrir un compte chez un registrar, à votre nom</h2>

<p>Créez le compte avec <strong>votre</strong> adresse e-mail et
<strong>votre</strong> carte — c'est ce compte qui fera de vous le
propriétaire pour les dix prochaines années. N'utilisez pas une adresse
qui dépend du domaine que vous transférez&nbsp;: si le transfert tourne
mal, vous perdez l'accès à votre boîte en même temps que le domaine.</p>

<p>Pour un <code>.ch</code>, un registrar suisse simplifie la facturation
et le support en français. Le tarif courant tourne autour d'une dizaine
de francs par an&nbsp;; la différence de prix entre registrars est
négligeable, la qualité du support ne l'est pas.</p>

<h2>Étape 4 — Lancer le transfert</h2>

<p>Depuis le nouveau registrar&nbsp;: «&nbsp;transférer un domaine&nbsp;»,
puis le nom et le code d'autorisation. Le registre envoie une demande de
confirmation à l'adresse du titulaire. Confirmez.</p>

<p>Comptez de un à sept jours selon l'extension. Pendant ce temps,
<strong>votre site et vos e-mails continuent de fonctionner</strong>&nbsp;:
un transfert de registrar ne change pas les DNS. C'est une inquiétude
fréquente et injustifiée.</p>

<p>Deux détails qui coincent&nbsp;: un domaine enregistré ou transféré il
y a moins de soixante jours ne peut pas être transféré à nouveau (règle de
l'ICANN), et un domaine resté verrouillé fera échouer la demande sans
explication claire.</p>

<h2>Étape 5 — Vérifier les DNS, et surtout les e-mails</h2>

<p>Une fois le transfert terminé, ouvrez la zone DNS chez le nouveau
registrar et comparez-la à l'ancienne, ligne par ligne. La plupart des
registrars reprennent les enregistrements automatiquement, mais pas
tous.</p>

<p>Regardez en particulier&nbsp;:</p>

<ul>
  <li>les enregistrements <strong>A</strong> et <strong>CNAME</strong>,
  qui font pointer le site&nbsp;;</li>
  <li>les enregistrements <strong>MX</strong>, qui font arriver vos
  e-mails — c'est <em>là</em> que se produisent les accidents&nbsp;;</li>
  <li>les enregistrements <strong>TXT</strong> de type SPF, DKIM et
  DMARC, sans lesquels vos e-mails partent en indésirable.</li>
</ul>

<p>Faites la vérification un jour de semaine, le matin, et envoyez-vous un
e-mail de test depuis une adresse extérieure dans l'heure qui suit.</p>

<h2>Si le prestataire ne répond pas</h2>

<ol>
  <li><strong>Relancez par écrit</strong>, en recommandé s'il le faut, en
  citant votre contrat et en fixant un délai.</li>
  <li><strong>Écrivez directement au registrar</strong> avec vos preuves
  de propriété&nbsp;: factures de renouvellement, extrait du registre du
  commerce, marque déposée. Les registrars ont une procédure pour les
  litiges de titularité.</li>
  <li><strong>Pour un <code>.ch</code></strong>, le registre suisse dispose
  d'une procédure de règlement des différends&nbsp;; pour les extensions
  génériques, c'est la procédure UDRP de l'OMPI. Elles sont conçues pour
  les cas de mauvaise foi et ont un coût.</li>
  <li><strong>En dernier recours</strong>, achetez une variante
  (<code>.ch</code> au lieu de <code>.com</code>, ou un nom légèrement
  différent) et redirigez. Vous perdez de l'historique, mais vous
  reprenez le contrôle — et c'est souvent moins coûteux qu'une procédure
  de six mois.</li>
</ol>

<h2>Pour que cela n'arrive plus</h2>

<ul>
  <li>Le domaine est enregistré <strong>à votre nom</strong>, sur un compte
  dont <strong>vous</strong> avez les identifiants.</li>
  <li>L'adresse e-mail du compte ne dépend pas du domaine lui-même.</li>
  <li>Le renouvellement automatique est activé, sur une carte valide.</li>
  <li>Le verrou de transfert est activé en temps normal&nbsp;: c'est ce qui
  empêche un détournement.</li>
  <li>Vos identifiants sont notés ailleurs que dans la tête d'une seule
  personne.</li>
</ul>

<p>Nous appliquons cela par défaut&nbsp;: le domaine est acheté à votre
nom, il reste votre propriété en tout temps, et il vous est transféré
sur demande sans frais, y compris si vous partez ailleurs. C'est écrit
dans nos conditions, ce qui est le seul endroit où cela compte. Si vous
avez un domaine à récupérer avant de refaire votre site,
<a href="../devis.html">dites-le nous</a>&nbsp;: c'est une opération que
nous faisons régulièrement.</p>
""",
  "faq": [
    ("Perd-on son site et ses e-mails pendant un transfert de domaine ?",
     "Non. Un transfert de registrar ne modifie pas les DNS : le site et les "
     "e-mails continuent de fonctionner. Les coupures viennent d'une zone "
     "DNS mal recopiée après le transfert, en particulier des "
     "enregistrements MX."),
    ("Que faire si l'ancien prestataire refuse de rendre le domaine ?",
     "Relancer par écrit avec un délai, puis saisir le registrar avec des "
     "preuves de propriété. Il existe une procédure de règlement des "
     "différends pour les .ch et la procédure UDRP de l'OMPI pour les "
     "extensions génériques."),
    ("Combien coûte un nom de domaine .ch par an ?",
     "Une dizaine de francs par an chez la plupart des registrars. L'écart "
     "de prix entre prestataires est négligeable."),
  ],
 },
]


# ---------------------------------------------------------------------------
# Libellés d'interface (tout ce qui n'est pas du corps d'article)
# ---------------------------------------------------------------------------

UI = {
    "accueil": "Accueil",
    "fil_blog": "Blog",
    "blog_titre": "Blog : sites web et visibilité pour les PME suisses | Up2Front",
    "blog_desc": "Neuf articles pour les PME de Suisse romande : prix réels, "
                 "délais réels, et ce que nous ferions à votre place.",
    "date_texte": "12 septembre 2026",
    "meta": "Publié le {date} · lecture {lecture}",
    "retour": "Tous les articles",
    "voir_tarifs": "Voir les tarifs",
    "demander_devis": "Demander un devis",
    "lire": "Lire l'article",
    "faq_t": "Questions fréquentes.",
    "faq_c": "Les questions qu'on nous pose sur ce sujet, avec la réponse "
             "courte.",
    "suite_t": "À lire ensuite.",
    "suite_c": "Deux autres articles du journal, sur des sujets voisins.",
    "art_appel_h2": "Un avis sur votre cas précis ?",
    "art_appel_p": "Décrivez votre activité en trois lignes. Nous répondons "
                   "le jour même, du lundi au vendredi, et nous disons aussi "
                   "quand un site n'est pas votre priorité.",
    "art_appel_b1": "Demander un devis",
    "art_appel_b2": "Voir les tarifs",
    "ecrire": "Écrire à contact@up2front.com",
}


# ---------------------------------------------------------------------------
# Page parrainage — annoncée, pas ouverte
# ---------------------------------------------------------------------------

PARRAINAGE = {
    "titre": "Parrainage | Up2Front",
    "desc": "Notre programme de parrainage n'est pas encore ouvert. Voici ce "
            "qui est en préparation, et comment être prévenu le jour où il "
            "démarre.",
    "fil": "Parrainage",
    "sur_titre": "Bientôt disponible",
    "h1": ["Le parrainage arrive.", "Il n'est pas encore ouvert."],
    "lede": "Nous préparons un programme de parrainage pour ceux qui nous "
            "recommandent déjà. Tant qu'il n'est pas en place, nous "
            "n'affichons aucun montant et ne demandons aucune coordonnée "
            "bancaire.",
    "b1": "Être prévenu du lancement",
    "b2": "Lire les conditions actuelles",
    "prose": """
<p class="maj">État au 12 septembre 2026 — programme en préparation</p>

<p><strong>Il n'y a aujourd'hui aucun programme de parrainage ouvert chez
Up2Front.</strong> Aucune commission n'est promise, aucune inscription
n'est ouverte, et aucun versement ne peut être réclamé sur la base d'une
recommandation. Cette page existe pour annoncer ce que nous préparons,
pas pour faire signer quoi que ce soit.</p>

<p>Nous aurions pu publier un barème dès maintenant&nbsp;: c'est une
ligne de texte à écrire. Mais un parrainage tenable demande un dispositif
derrière — savoir qui a recommandé qui, vérifier qu'une commande a
réellement été payée, verser une somme à une personne qui n'est pas
cliente, et traiter ce versement correctement sur le plan comptable et
fiscal. C'est ce dispositif que nous mettons en place avant d'ouvrir.</p>

<h2>Ce qui sera annoncé le jour du lancement</h2>

<ul>
  <li>Qui peut participer, et à quelles conditions.</li>
  <li>Ce qui déclenche exactement une contrepartie, et à quel moment.</li>
  <li>Le montant, ou le pourcentage, écrit noir sur blanc.</li>
  <li>Le délai de versement et le moyen utilisé.</li>
  <li>Les cas où rien n'est dû — annulation, remboursement, commande
  passée par vous-même.</li>
</ul>

<p>Tant que ces cinq points ne sont pas écrits, il n'y a pas de programme.
Nos <a href="legal/affiliation.html">conditions de parrainage et
d'affiliation</a> le disent dans les mêmes termes, et elles font foi.</p>

<h2>Si vous nous recommandez d'ici là</h2>

<p>Cela arrive, et c'est ce qui fait vivre une jeune entreprise. Si
quelqu'un commande grâce à vous, écrivez-nous à
<a href="mailto:contact@up2front.com">contact@up2front.com</a>&nbsp;: nous
en discuterons de gré à gré, au cas par cas. Ce sera un accord ponctuel,
pas l'application d'un programme — et nous le dirons comme tel.</p>

<h2>Être prévenu</h2>

<p>Un message à <a href="mailto:contact@up2front.com?subject=Parrainage%20—%20me%20pr%C3%A9venir%20du%20lancement">contact@up2front.com</a>
avec la mention «&nbsp;parrainage&nbsp;» suffit. Nous n'avons pas besoin
de vos coordonnées bancaires pour vous inscrire à une liste d'attente, et
nous ne vous les demanderons jamais avant qu'une somme soit réellement
due.</p>
""",
    "etapes_t": "Ce que nous mettons en place.",
    "etapes_c": "Trois chantiers, dans cet ordre. Le programme ouvrira quand "
                "les trois seront terminés.",
    "etapes": [
        ("Chantier 1", "Le suivi des recommandations",
         "Un lien de parrainage nominatif, rattaché à une commande payée. "
         "Sans ce suivi, impossible de savoir qui a droit à quoi."),
        ("Chantier 2", "Le cadre écrit",
         "Des conditions de parrainage complètes, intégrées aux CGV, qui "
         "disent aussi dans quels cas rien n'est dû."),
        ("Chantier 3", "Le versement",
         "Le traitement comptable et fiscal d'une contrepartie versée à une "
         "personne qui n'est pas cliente. C'est le point le plus long."),
    ],
    "appel_h2": "En attendant, la façon la plus simple de nous aider",
    "appel_p": "Parlez de nous à quelqu'un qui en a besoin, et dites-le nous. "
               "Nous répondons le jour même, du lundi au vendredi.",
    "appel_b1": "Écrire à contact@up2front.com",
    "appel_b2": "Voir les tarifs",
}
