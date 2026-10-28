# -*- coding: utf-8 -*-
"""Contenu du pôle « Visibilité IA » (lu par _geo_pages.py). Mis à jour le 27 octobre 2026.
Règles : chiffres sourcés et datés, aucune garantie, aucun avis inventé, jamais de prix de chantier."""

AR_Q = [("Questions", "visibilite-ia/methode.html")]

PAGES = []

# =====================================================================================
PAGES.append(dict(
    path="visibilite-ia/agence-geo-geneve.html", court="Agence GEO à Genève",
    title="Agence GEO à Genève — visibilité IA mesurée, sans promesse | Up2Front",
    titre="Agence GEO à Genève : ce que fait Up2Front, et ce qu'elle ne promet pas",
    desc="Up2Front, agence web à Genève, mesure et améliore la visibilité des PME dans Google AI Mode, ChatGPT et Gemini. Relevé offert, réponses datées à la minute, aucune position garantie.",
    eyebrow="Agence GEO · Genève et Suisse romande",
    h1="Agence GEO à Genève : <em>la mesure d'abord</em>, la promesse jamais",
    chapo="Le GEO consiste à faire comprendre et citer une entreprise par les moteurs de réponse IA. Une vingtaine d'agences le proposent en Suisse romande. Voici ce que fait Up2Front, comment on travaille et ce qu'on refuse de vendre.",
    reponse="<strong>Up2Front</strong> est une agence web genevoise fondée par Maxime Pilloud. Elle mesure ce que <strong>Google AI Mode, ChatGPT et Gemini</strong> répondent quand un client cherche votre métier, puis corrige ce qui vous empêche d'être cité. Le premier pas est <strong>le Relevé, offert</strong> : vos réponses mot pour mot, datées à la minute, sur une page à votre nom. Aucune agence ne peut garantir une place dans une réponse IA, et nous non plus.",
    corps='''    <h2>Ce que nous faisons</h2>
    <ol>
      <li><strong>Le Relevé (offert).</strong> Nous posons la question qu'un de vos clients poserait (« quel est le meilleur [votre métier] à [votre ville] ? ») à trois moteurs, deux fois, à quelques heures d'écart. Vous recevez sous 2 jours ouvrés une page à votre nom avec chaque réponse <strong>mot pour mot</strong>, l'heure à la minute et les sources que les moteurs ont citées.</li>
      <li><strong>Le chantier (sur devis, seulement si vous le demandez).</strong> Nous corrigeons ce qui bloque : pages que les moteurs ne savent pas lire, identité floue, absence dans les annuaires et les sources que les IA consultent vraiment.</li>
      <li><strong>La nouvelle mesure à 90 jours.</strong> Nous refaisons le même relevé, avec la même question, pour que vous voyiez ce qui a bougé ou non.</li>
    </ol>

    <h2>Ce que nous ne promettons pas</h2>
    <ul>
      <li><strong>Aucune position garantie.</strong> Les réponses des IA changent d'un jour à l'autre : environ 65 % des sources citées changent d'une journée à la suivante, selon l'Université de Saint-Gall (avril 2026). Quiconque garantit « la première place dans ChatGPT » vend autre chose que la réalité.</li>
      <li><strong>Aucun avis inventé, aucun faux article.</strong> Ce qui est faux finit par se voir, et les moteurs le recoupent.</li>
      <li><strong>Pas de chantier inutile.</strong> Si vos clients vous arrivent surtout par une assurance, une régie ou un confrère, l'IA pèse peu dans votre activité. Nous vous le dirons, et nous ne vous vendrons rien.</li>
    </ul>

    <h2>Nous nous mesurons nous-mêmes, en public</h2>
    <p>Le 27 octobre 2026, nous avons posé quatre questions de clients aux trois moteurs. <strong>Up2Front n'a été nommé dans aucune des 12 réponses.</strong> Nous publions ce score et sa progression chaque mois, avec les réponses complètes : <a href="{R}visibilite-ia/ce-que-les-ia-disent-d-up2front.html">ce que les IA disent d'Up2Front</a>. Vendre la mesure sans montrer la sienne ne serait pas sérieux.</p>

    <h2>Cinq questions à poser à n'importe quelle agence GEO</h2>
    <ol>
      <li>Combien de fois posez-vous chaque question ? Une seule réponse ne prouve rien, puisque la même question donne des classements différents dans la même heure (<a href="{R}etudes/visibilite-ia-architectes-geneve.html">notre étude sur les architectes genevois</a>).</li>
      <li>Me montrez-vous les réponses complètes des moteurs, ou seulement un score ?</li>
      <li>Quels moteurs mesurez-vous, et à quelle date exacte ?</li>
      <li>Quelles sources les moteurs citent-ils à la place de mon site ?</li>
      <li>Que se passe-t-il si rien ne bouge après 90 jours ?</li>
    </ol>

    <h2>Où nous travaillons</h2>
    <p>À Genève et dans toute la Suisse romande, en français. Up2Front crée aussi des <a href="{R}index.html">sites web professionnels à forfait</a>, dès CHF 290.</p>''',
    faq=[
        ("Combien coûte le Relevé d'Up2Front ?", "Le Relevé est offert. Il montre ce que Google AI Mode, ChatGPT et Gemini répondent sur votre métier, deux fois à quelques heures d'écart, sur une page à votre nom, sous 2 jours ouvrés."),
        ("Up2Front garantit-elle d'apparaître dans ChatGPT ?", "Non. Les réponses des moteurs IA varient d'un jour à l'autre et aucune agence ne peut garantir une citation. Up2Front mesure, corrige ce qui bloque, puis refait la mesure à 90 jours."),
        ("Quels moteurs Up2Front mesure-t-elle ?", "Google AI Mode, ChatGPT et Gemini, avec deux passages par question. Les relevés sont datés à la minute."),
        ("Où se trouve Up2Front ?", "À Genève. Up2Front travaille pour les PME de toute la Suisse romande."),
    ],
    sources=["stgall", "etude", "self"],
))

# =====================================================================================
PAGES.append(dict(
    path="visibilite-ia/ce-que-les-ia-disent-d-up2front.html", court="Ce que les IA disent d'Up2Front",
    title="Ce que les IA disent d'Up2Front — notre relevé public, chaque mois | Up2Front",
    titre="Ce que les IA disent d'Up2Front : notre propre relevé, publié chaque mois",
    desc="Chaque mois, Up2Front publie ce que Google AI Mode, ChatGPT et Gemini répondent sur son propre métier. Octobre 2026 : nommé dans 0 réponse sur 12.",
    type="Report",
    eyebrow="Relevé public · octobre 2026",
    h1="Ce que les IA disent d'Up2Front : <em>0 sur 12</em> en octobre",
    chapo="Nous vendons la mesure de la visibilité IA. Il serait malhonnête de ne pas publier la nôtre. Chaque mois, nous posons les mêmes questions aux mêmes moteurs et nous publions les résultats, même quand ils ne nous flattent pas.",
    reponse="Le <strong>27 octobre 2026</strong>, nous avons posé quatre questions de clients à <strong>Google AI Mode, ChatGPT et Gemini</strong>. Up2Front n'est nommé dans <strong>aucune des 12 réponses</strong>. Les moteurs citent à sa place plus de vingt agences romandes et quatre outils de mesure suisses. Ce relevé ne compte encore qu'un passage sur deux : à lui seul, il ne prouve rien, et le second passage le complétera.",
    corps='''    <h2>Le relevé du 27 octobre 2026</h2>
    <p>Premier passage, entre 20h06 et 20h11 (UTC). Session neuve, sans compte ni historique, marché suisse, en français.</p>
    <div class="tab"><table>
      <thead><tr><th>Question posée</th><th>Google AI Mode</th><th>ChatGPT</th><th>Gemini</th><th>Cités à notre place (extraits)</th></tr></thead>
      <tbody>
        <tr><td>« Quelle agence peut rendre mon entreprise visible dans ChatGPT et les réponses IA à Genève ? »</td><td class="zero">non cité</td><td class="zero">non cité</td><td class="zero">non cité</td><td>Soleil Digital, DEEPSEO, MW Agency, FirstPoint, EWM, agence-geo.ch, Wild, Eminence, Procab</td></tr>
        <tr><td>« Qui propose du référencement IA (GEO) pour les PME en Suisse romande ? »</td><td class="zero">non cité</td><td class="zero">non cité</td><td class="zero">non cité</td><td>Soleil Digital, FirstPoint, Link IA, FlashDesign, Léman Studio, HumAIn, Suisseo, Emblematik</td></tr>
        <tr><td>« Comment savoir si mon entreprise est recommandée par ChatGPT ou Google en Suisse ? »</td><td class="zero">non cité</td><td class="zero">non cité</td><td class="zero">non cité</td><td>CheckAI.ch, anewera.ch, Bombelli Analytics, FirstPoint, Soleil Digital</td></tr>
        <tr><td>« agence pour créer un site internet à Genève »</td><td class="zero">non cité</td><td class="zero">non cité</td><td class="zero">non cité</td><td>Wecode, Helveit, Igeneve, Simply Design, Procab Studio, Swiss Tomato, miind</td></tr>
      </tbody>
    </table></div>
    <p class="note">Les noms ci-dessus sont ceux que les moteurs ont eux-mêmes publiés dans leurs réponses. Leur présence ne vaut ni recommandation ni jugement de notre part.</p>

    <h2>Ce que ces réponses nous apprennent</h2>
    <ul>
      <li><strong>Les moteurs citent les pages « agence GEO à [ville] »</strong> des agences elles-mêmes. Nous n'en avions pas : <a href="{R}visibilite-ia/agence-geo-geneve.html">c'est corrigé</a>.</li>
      <li><strong>Google cite des articles de tiers</strong> (presse économique romande, blogs spécialisés). Être mentionné ailleurs pèse plus que parler de soi.</li>
      <li><strong>ChatGPT reprend les faits chiffrés</strong> : les prix publiés par les agences et le nombre d'avis Google.</li>
      <li><strong>Notre nom prêtait à confusion</strong> pour une machine : « Up2Front » ressemble à « Up Front ». Notre site décrit désormais clairement qui nous sommes et ce que nous faisons.</li>
    </ul>

    <h2>Ce que nous avons changé ce mois-ci</h2>
    <ul>
      <li>Une fiche d'identité unique et lisible par les machines sur toutes les pages du site.</li>
      <li>Un pôle de pages qui répondent aux questions qu'on se pose avant de choisir : <a href="{R}visibilite-ia/methode.html">la méthode</a>, <a href="{R}visibilite-ia/prix-geo-suisse.html">les prix du marché</a>, <a href="{R}visibilite-ia/glossaire.html">le glossaire</a>.</li>
      <li>Une page qui regroupe <a href="{R}etudes/">nos études</a>.</li>
    </ul>

    <h2>Le protocole, pour que chacun puisse le refaire</h2>
    <p>Les mêmes questions chaque mois, aux mêmes trois moteurs, deux passages à quelques heures d'écart, en session neuve. Nous notons si Up2Front est nommé, si up2front.com est cité comme source, et qui est cité à notre place. Le détail est sur la page <a href="{R}visibilite-ia/methode.html">méthode</a>.</p>
    <p><strong>Prochain relevé : mardi 3 novembre 2026.</strong></p>''',
    sans_appel=False,
    sources=["stgall"],
    sources_extra=[("Relevé Up2Front du 27 octobre 2026, réponses complètes archivées (disponibles sur demande à contact@up2front.com)", "https://up2front.com/visibilite-ia/ce-que-les-ia-disent-d-up2front.html")],
))

# =====================================================================================
PAGES.append(dict(
    path="visibilite-ia/methode.html", court="La méthode",
    title="Comment mesurer sa visibilité dans ChatGPT et Google AI Mode — la méthode | Up2Front",
    titre="Comment mesurer sa visibilité dans les réponses des IA : la méthode Up2Front",
    desc="La méthode pour savoir si ChatGPT, Google AI Mode et Gemini recommandent votre entreprise : la bonne question, la session neuve, deux passages, l'heure à la minute. Reproductible et gratuite.",
    eyebrow="Méthode · reproductible",
    h1="Comment savoir si <em>les IA recommandent</em> votre entreprise",
    chapo="Taper le nom de son entreprise dans ChatGPT ne mesure rien : l'IA confirme ce qu'on lui suggère. Voici la méthode que nous appliquons à chaque relevé. Vous pouvez la suivre seul, gratuitement.",
    reponse="Posez <strong>la question qu'un client poserait</strong>, sans jamais citer votre nom, dans une <strong>session neuve</strong>, à <strong>plusieurs moteurs</strong> (Google AI Mode, ChatGPT, Gemini). Recommencez <strong>quelques heures plus tard</strong>, notez l'heure à la minute et gardez chaque réponse <strong>mot pour mot</strong>. Une seule réponse ne prouve rien : la même question donne des classements différents dans la même heure.",
    corps='''    <h2>Les sept règles d'un relevé fiable</h2>
    <ol>
      <li><strong>Une question de client, pas de nom.</strong> « Quel est le meilleur chauffagiste à Carouge pour une pompe à chaleur ? », jamais « Que penses-tu de Chauffage Dupont ? ».</li>
      <li><strong>Une session neuve.</strong> Navigation privée, sans compte connecté ni historique : sinon le moteur répond à partir de ce qu'il sait déjà de vous.</li>
      <li><strong>Plusieurs moteurs.</strong> Google AI Mode, ChatGPT et Gemini ne lisent pas les mêmes sources. Être cité par l'un ne dit rien des autres.</li>
      <li><strong>Au moins deux passages, espacés de quelques heures.</strong> Selon l'Université de Saint-Gall (avril 2026), environ 65 % des sources citées changent d'un jour à l'autre, même pour une question identique.</li>
      <li><strong>L'heure à la minute.</strong> Une réponse sans date n'est pas une mesure.</li>
      <li><strong>La réponse complète, mot pour mot.</strong> Pas un résumé : la phrase exacte où vous êtes cité, ou pas.</li>
      <li><strong>Trois choses à noter.</strong> Êtes-vous nommé ? Votre site est-il cité comme source ? Qui est nommé à votre place ?</li>
    </ol>

    <h2>La preuve que deux passages sont indispensables</h2>
    <p>Le 15 septembre 2026, nous avons posé la même question sur les architectes genevois à Google AI Mode à plusieurs reprises en une heure. <strong>Google a répondu trois fois, et jamais la même chose.</strong> Détails, heures et captures dans <a href="{R}etudes/visibilite-ia-architectes-geneve.html">l'étude publiée</a>.</p>

    <h2>Les limites, écrites noir sur blanc</h2>
    <ul>
      <li>Deux passages donnent une tendance, pas une fréquence statistique. Les chercheurs de Saint-Gall recommandent plusieurs passages par jour sur plusieurs semaines pour une mesure scientifique.</li>
      <li>Les moteurs changent de modèle sans prévenir. Une mesure vaut pour sa date.</li>
      <li>Un relevé dit <strong>ce que l'IA répond</strong>. Il ne dit pas combien de clients posent la question.</li>
    </ul>

    <h2>Le faire soi-même ou le confier</h2>
    <p>Tout ce qui précède se fait gratuitement, avec un peu de discipline. Si vous préférez ne pas y passer une soirée, <a href="{R}visibilite-ia.html">le Relevé Up2Front</a> applique exactement ce protocole et vous rend une page à votre nom. Nous appliquons la même méthode <a href="{R}visibilite-ia/ce-que-les-ia-disent-d-up2front.html">à nous-mêmes, chaque mois</a>.</p>''',
    faq=[
        ("Peut-on mesurer soi-même sa visibilité dans ChatGPT ?", "Oui. Posez la question qu'un client poserait, sans citer votre nom, en session neuve, à plusieurs moteurs, deux fois à quelques heures d'écart, et gardez chaque réponse mot pour mot avec l'heure."),
        ("Pourquoi une seule réponse ne suffit-elle pas ?", "Parce que les réponses changent : environ 65 % des sources citées changent d'un jour à l'autre selon l'Université de Saint-Gall (2026), et Google AI Mode a donné trois classements différents en une heure dans l'étude Up2Front du 15 septembre 2026."),
        ("Faut-il tester avec le nom de son entreprise ?", "Non. Avec votre nom, l'IA confirme ce qu'on lui suggère. Il faut poser la question d'un client qui ne vous connaît pas encore."),
    ],
    sources=["stgall", "etude"],
))

# =====================================================================================
PAGES.append(dict(
    path="visibilite-ia/qu-est-ce-que-le-geo.html", court="Qu'est-ce que le GEO ?", ariane=AR_Q,
    title="Qu'est-ce que le GEO (Generative Engine Optimization) ? Définition simple | Up2Front",
    titre="Qu'est-ce que le GEO (Generative Engine Optimization) ?",
    desc="Le GEO, c'est l'ensemble des actions qui aident une entreprise à être comprise et citée par les moteurs de réponse IA : Google AI Mode, ChatGPT, Gemini. Définition, exemples suisses, ce qui marche et ce qui est surévalué.",
    eyebrow="Question fréquente · définition",
    h1="Qu'est-ce que <em>le GEO</em> ?",
    chapo="GEO veut dire Generative Engine Optimization : l'optimisation pour les moteurs génératifs. Le terme vient d'un article de recherche publié en 2023 par des chercheurs de Princeton et présenté à la conférence KDD en 2024.",
    reponse="Le <strong>GEO</strong> regroupe tout ce qui aide une entreprise à être <strong>comprise et citée</strong> par les moteurs qui répondent à la place d'une liste de liens : <strong>Google AI Mode et les aperçus IA de Google, ChatGPT, Gemini, Perplexity, Claude</strong>. Là où le SEO vise une place dans une liste, le GEO vise une mention dans la réponse elle-même.",
    corps='''    <h2>Pourquoi le sujet compte en Suisse</h2>
    <p>En mars 2026, <strong>76 % des Suisses</strong> utilisaient des outils d'IA au quotidien, et <strong>81,6 % en Suisse romande</strong>. <strong>41,6 %</strong> s'en servaient pour remplacer un moteur de recherche classique (sondage Comparis / Innofact, 1 035 personnes). Google affiche des aperçus IA en Suisse depuis le 26 mars 2025, dans les quatre langues, et son mode IA depuis octobre 2025.</p>

    <h2>Ce qui fait vraiment citer une entreprise</h2>
    <ul>
      <li><strong>Être mentionné ailleurs que chez soi.</strong> Sur 75 000 marques, les mentions sur d'autres sites pèsent environ trois fois plus que les liens (Ahrefs, mai 2025).</li>
      <li><strong>Des pages claires qui répondent tout de suite.</strong> Un texte simple et prévisible augmente la probabilité d'être cité de 47 % à 56 % (Ma et al., 2025). Citer des sources et des chiffres l'augmente aussi (Aggarwal et al., KDD 2024).</li>
      <li><strong>Laisser entrer les robots des moteurs</strong> (OAI-SearchBot pour ChatGPT, Googlebot pour Google, etc.). Un site qui les bloque ne peut pas être cité.</li>
      <li><strong>Être présent dans les sources locales</strong> que les moteurs consultent : annuaires suisses (local.ch, search.ch), registres de profession, presse régionale.</li>
    </ul>

    <h2>Ce qui est surévalué</h2>
    <ul>
      <li><strong>Le fichier llms.txt</strong> : aucun effet démontré à ce jour, selon Google lui-même.</li>
      <li><strong>Les données structurées comme « levier magique »</strong> : utiles pour que les machines comprennent qui vous êtes, mais Google précise qu'aucun balisage spécial n'est nécessaire pour ses fonctions IA.</li>
      <li><strong>Les promesses de « première place dans ChatGPT »</strong> : impossibles, puisque les réponses changent d'un jour à l'autre.</li>
    </ul>

    <h2>Les autres noms du GEO</h2>
    <p>On parle aussi de <strong>référencement IA</strong>, d'<strong>AEO</strong> (Answer Engine Optimization), de <strong>LLMO</strong> ou de <strong>visibilité IA</strong>. Ces mots désignent la même chose. Voir le <a href="{R}visibilite-ia/glossaire.html">glossaire GEO suisse</a>.</p>''',
    faq=[
        ("Que veut dire GEO ?", "Generative Engine Optimization : l'optimisation pour les moteurs génératifs. C'est l'ensemble des actions qui aident une entreprise à être comprise et citée par Google AI Mode, ChatGPT, Gemini, Perplexity ou Claude."),
        ("Le GEO remplace-t-il le SEO ?", "Non. Le GEO s'appuie sur les mêmes fondations (un site lisible, une bonne réputation), mais il vise une mention dans la réponse de l'IA plutôt qu'une place dans une liste de liens."),
        ("Le GEO est-il utile pour une PME suisse ?", "Oui si ses clients cherchent un prestataire en ligne : en mars 2026, 41,6 % des Suisses utilisaient l'IA pour remplacer un moteur de recherche classique (Comparis / Innofact)."),
    ],
    sources=["kdd", "comparis", "aio_ch", "aimode_ch", "ahrefs", "ma", "google_aif"],
))

# =====================================================================================
PAGES.append(dict(
    path="visibilite-ia/geo-ou-seo.html", court="GEO ou SEO ?", ariane=AR_Q,
    title="GEO ou SEO : quelle différence pour une PME suisse ? | Up2Front",
    titre="GEO ou SEO : quelle différence pour une PME suisse ?",
    desc="Le SEO vise une place dans la liste de Google, le GEO une mention dans la réponse de l'IA. Ce qui est commun, ce qui change, et par quoi commencer quand on est une PME en Suisse romande.",
    eyebrow="Question fréquente · comparaison",
    h1="GEO ou SEO : <em>quelle différence</em> ?",
    chapo="Les deux partagent les mêmes fondations. Mais être bien placé dans Google ne garantit plus d'être cité par l'IA, et l'inverse est vrai aussi.",
    reponse="Le <strong>SEO</strong> travaille votre <strong>place dans une liste de liens</strong>. Le <strong>GEO</strong> travaille votre <strong>présence dans la réponse</strong> que l'IA écrit à la place de cette liste. Les fondations sont communes (un site lisible, une réputation solide), mais une étude de 2025 montre que <strong>53 % des sites cités par les aperçus IA de Google ne sont pas dans les dix premiers résultats</strong>.",
    corps='''    <h2>Ce qui change</h2>
    <div class="tab"><table>
      <thead><tr><th></th><th>SEO</th><th>GEO</th></tr></thead>
      <tbody>
        <tr><td><strong>Objectif</strong></td><td>Une place dans la liste de résultats</td><td>Une mention dans la réponse écrite par l'IA</td></tr>
        <tr><td><strong>Ce que voit le client</strong></td><td>Dix liens, il choisit et clique</td><td>Une réponse avec trois à huit noms, souvent sans clic</td></tr>
        <tr><td><strong>Ce qui pèse le plus</strong></td><td>Pertinence de la page, liens, technique</td><td>Mentions sur d'autres sites, clarté, sources fiables</td></tr>
        <tr><td><strong>Stabilité</strong></td><td>Classement assez stable d'un jour à l'autre</td><td>Réponses qui changent d'un jour à l'autre (environ 65 % des sources)</td></tr>
        <tr><td><strong>Mesure</strong></td><td>Search Console : positions, clics</td><td>Relevés répétés + rapport IA de la Search Console (affichages)</td></tr>
      </tbody>
    </table></div>

    <h2>Ce qui reste commun</h2>
    <ul>
      <li>Un site rapide, lisible sans JavaScript, avec une page par prestation.</li>
      <li>Une identité claire : même nom, même adresse, mêmes informations partout.</li>
      <li>Une réputation construite hors de votre site : annuaires, presse, avis de vrais clients.</li>
    </ul>
    <p>Google le dit lui-même : ses fonctions IA reposent sur son index habituel, et aucune exigence technique supplémentaire n'est nécessaire.</p>

    <h2>Par quoi commencer</h2>
    <p>Par une mesure. Avant d'investir dans l'un ou l'autre, regardez ce que les IA répondent aujourd'hui quand un client cherche votre métier : la <a href="{R}visibilite-ia/methode.html">méthode</a> est gratuite, et <a href="{R}visibilite-ia.html">le Relevé</a> est offert.</p>''',
    faq=[
        ("Peut-on être bien placé dans Google mais absent de ChatGPT ?", "Oui. Une étude de 2025 (Bochum / MPI-SWS) montre que 53 % des sites cités par les aperçus IA de Google ne figurent pas dans les dix premiers résultats classiques, et ChatGPT utilise son propre robot d'indexation."),
        ("Faut-il abandonner le SEO pour le GEO ?", "Non. Les fondations sont communes et Google construit ses réponses IA à partir de son index habituel. Le GEO ajoute un travail sur les mentions externes et la clarté des pages."),
    ],
    sources=["bochum", "stgall", "google_aif", "gsc_ia"],
))

# =====================================================================================
PAGES.append(dict(
    path="visibilite-ia/prix-geo-suisse.html", court="Prix du GEO en Suisse", ariane=AR_Q,
    title="Combien coûte le GEO en Suisse ? Les prix publiés en 2026 | Up2Front",
    titre="Combien coûte le GEO en Suisse ? Les prix publiés, sources à l'appui",
    desc="Prix du GEO et de la visibilité IA en Suisse en 2026 : outils de suivi dès CHF 24 par mois, audits de CHF 390 à CHF 4 000, accompagnements de CHF 550 à plus de CHF 1 200 par mois. Prix publics, datés, avec leurs sources.",
    eyebrow="Question fréquente · prix",
    h1="Combien coûte <em>le GEO</em> en Suisse ?",
    chapo="Les prix varient de zéro à plusieurs milliers de francs selon ce qu'on achète : un outil automatique, un audit ou un accompagnement. Voici les prix que les prestataires suisses publient eux-mêmes, avec la date à laquelle nous les avons lus.",
    reponse="En Suisse, en octobre 2026, un <strong>outil de suivi automatique</strong> coûte de <strong>CHF 0 à CHF 165 par mois</strong>, un <strong>audit</strong> de <strong>CHF 390 à CHF 4 000</strong>, et un <strong>accompagnement mensuel</strong> de <strong>CHF 550 à plus de CHF 1 200 par mois</strong>. Beaucoup d'agences ne publient aucun prix. Aucun prix sérieux n'inclut une garantie de citation.",
    corps='''    <h2>Les prix publiés par les prestataires</h2>
    <div class="tab"><table>
      <thead><tr><th>Prestataire</th><th>Ce qui est vendu</th><th>Prix publié</th><th>Lu le</th></tr></thead>
      <tbody>
        <tr><td>CheckAI.ch</td><td>Outil : test gratuit (6 questions, ChatGPT et AI Mode) ; relevé ponctuel ; suivi hebdomadaire ; suivi quotidien</td><td class="num">0 · CHF 8 · CHF 24/mois · CHF 165/mois</td><td class="num">27.10.2026</td></tr>
        <tr><td>visiblement.ch</td><td>Audit en 48 h (ChatGPT, Perplexity, Google) ; suivi inclus dans un forfait de maintenance</td><td class="num">CHF 390 · CHF 199/mois</td><td class="num">03.10.2026</td></tr>
        <tr><td>FirstPoint (Lausanne)</td><td>Suivi de 30 à 50 questions ; + contenu ; + publication</td><td class="num">dès CHF 550 · 1 250 · 1 750/mois</td><td class="num">27.10.2026</td></tr>
        <tr><td>Soleil Digital (Genève)</td><td>Audit « light » ; audit complet ; suivi continu</td><td class="num">CHF 1 200 · 2 900 à 4 000 · 1 200/mois (HT)</td><td class="num">03.10.2026</td></tr>
        <tr><td>DEEPSEO (Carouge)</td><td>Accompagnement SEO et GEO ; audit gratuit en 48 h</td><td class="num">dès CHF 1 200/mois</td><td class="num">27.10.2026</td></tr>
        <tr><td>Up2Front (Genève)</td><td>Le Relevé : 3 moteurs, 2 passages, réponses mot pour mot sur une page à votre nom ; chantier sur devis</td><td class="num">Relevé offert</td><td class="num">27.10.2026</td></tr>
      </tbody>
    </table></div>
    <p class="note">Prix lus sur les pages publiques des prestataires, hors TVA quand c'est indiqué. Ils peuvent avoir changé depuis : vérifiez auprès de chacun. Cette liste n'est ni un classement ni une recommandation.</p>

    <h2>Ce que le prix doit vous acheter</h2>
    <ul>
      <li><strong>Plusieurs passages par question</strong>, à des heures différentes. Une seule réponse ne prouve rien.</li>
      <li><strong>Les réponses complètes</strong>, pas seulement un score.</li>
      <li><strong>Des dates</strong> : une mesure sans date n'est pas une mesure.</li>
      <li><strong>Une nouvelle mesure</strong> après le travail, avec les mêmes questions.</li>
    </ul>

    <h2>Ce qui ne devrait rien coûter</h2>
    <p>Vérifier que votre site laisse entrer les robots des moteurs, ouvrir une fiche Google Business, être inscrit sur local.ch et search.ch, poser vous-même les bonnes questions aux IA : tout cela est gratuit. La <a href="{R}visibilite-ia/methode.html">méthode</a> est expliquée pas à pas.</p>''',
    faq=[
        ("Combien coûte un audit de visibilité IA en Suisse ?", "En octobre 2026, les audits publiés vont de CHF 390 (visiblement.ch) à CHF 2 900 à 4 000 (audit complet de Soleil Digital). Plusieurs acteurs proposent un premier test gratuit, et le Relevé d'Up2Front est offert."),
        ("Combien coûte un suivi mensuel de la visibilité IA ?", "De CHF 24 par mois pour un outil automatique hebdomadaire (CheckAI.ch) à CHF 1 200 par mois et plus pour un suivi par une agence (Soleil Digital, DEEPSEO), selon les prix publiés en octobre 2026."),
        ("Un prestataire peut-il garantir une place dans ChatGPT ?", "Non. Les réponses des moteurs IA changent d'un jour à l'autre ; une garantie de citation n'est pas sérieuse."),
    ],
    sources=[],
    sources_extra=[
        ("CheckAI.ch, page tarifs, lue le 27.10.2026", "https://checkai.ch/en/?cur=chf"),
        ("visiblement.ch, offre audit et suivi, lue le 03.10.2026", "https://visiblement.ch/"),
        ("FirstPoint, « Agence GEO en Suisse romande », lue le 27.10.2026", "https://www.firstpoint.ch/marketing-digital/agence-geo-optimisation-ia"),
        ("Soleil Digital, « Audit ChatGPT », lue le 03.10.2026", "https://www.soleil-digital.ch/audit-chatgpt/"),
        ("DEEPSEO, « Référencement IA », lue le 27.10.2026", "https://deepseo.ch/services/referencement-ia/"),
    ],
))

# =====================================================================================
PAGES.append(dict(
    path="visibilite-ia/pourquoi-chatgpt-ne-cite-pas-mon-entreprise.html", court="Pourquoi ChatGPT ne me cite pas", ariane=AR_Q,
    title="Pourquoi ChatGPT ne cite pas mon entreprise ? Les 6 causes | Up2Front",
    titre="Pourquoi ChatGPT ne cite pas mon entreprise ?",
    desc="Les six causes les plus fréquentes pour lesquelles ChatGPT, Google AI Mode ou Gemini ne nomment pas une PME suisse, et comment vérifier chacune gratuitement.",
    eyebrow="Question fréquente · diagnostic",
    h1="Pourquoi ChatGPT <em>ne cite pas</em> mon entreprise ?",
    chapo="Dans la plupart des cas, ce n'est ni un oubli ni une injustice. L'IA ne cite que ce qu'elle trouve, comprend et voit confirmé ailleurs. Six causes reviennent presque toujours.",
    reponse="ChatGPT ne cite pas une entreprise quand il <strong>ne peut pas lire son site</strong>, quand il <strong>ne comprend pas ce qu'elle fait ni où</strong>, quand <strong>personne d'autre ne parle d'elle</strong>, ou quand des concurrents ont des pages plus claires sur la question posée. La réponse change aussi d'un jour à l'autre : il faut <strong>vérifier plusieurs fois</strong> avant de conclure.",
    corps='''    <h2>Les six causes, et comment vérifier</h2>
    <h3>1. Votre site bloque les robots des IA</h3>
    <p>ChatGPT indexe le web avec son propre robot, <strong>OAI-SearchBot</strong>. S'il est bloqué dans votre fichier robots.txt ou par votre hébergeur, votre site ne peut pas être cité. <strong>Vérifier :</strong> ouvrez <em>votresite.ch/robots.txt</em> et cherchez « Disallow » sous OAI-SearchBot, GPTBot ou « * ».</p>
    <h3>2. Votre site ne dit pas clairement quoi et où</h3>
    <p>« Solutions sur mesure pour vos projets » ne dit rien à une machine. « Chauffagiste à Carouge, pompes à chaleur » dit tout. Le métier et la ville doivent figurer dans le titre et la première phrase de chaque page.</p>
    <h3>3. Votre contenu n'est visible qu'avec JavaScript</h3>
    <p>Certains sites n'affichent leur texte qu'après exécution de scripts. Plusieurs robots d'IA ne les exécutent pas et voient une page vide.</p>
    <h3>4. Personne d'autre ne parle de vous</h3>
    <p>C'est la cause la plus fréquente. Les mentions sur d'autres sites pèsent environ trois fois plus que les liens (Ahrefs, 75 000 marques, 2025). Annuaires suisses, registre de votre profession, presse locale, associations : l'IA recoupe.</p>
    <h3>5. Vos concurrents répondent mieux à la question</h3>
    <p>Quand quelqu'un demande « quelle agence GEO à Genève ? », les moteurs citent les pages intitulées « Agence GEO à Genève ». C'est ce que nous avons observé le 27 octobre 2026 dans <a href="{R}visibilite-ia/ce-que-les-ia-disent-d-up2front.html">notre propre relevé</a>.</p>
    <h3>6. Vous avez testé une seule fois</h3>
    <p>La même question donne des réponses différentes d'une heure à l'autre. Avant de conclure, suivez <a href="{R}visibilite-ia/methode.html">la méthode</a> : session neuve, plusieurs moteurs, deux passages.</p>

    <h2>Et si vos clients ne passent pas par l'IA ?</h2>
    <p>Si vos clients vous arrivent surtout par une assurance, une régie ou un confrère, être absent de ChatGPT a peu d'effet sur votre activité. Le bon réflexe est de mesurer avant d'investir.</p>''',
    faq=[
        ("ChatGPT utilise-t-il Google pour trouver les entreprises ?", "Non. ChatGPT indexe le web avec son propre robot, OAI-SearchBot. Il faut que votre site lui soit ouvert dans le fichier robots.txt."),
        ("Combien de temps faut-il pour apparaître dans ChatGPT ?", "Personne ne peut le promettre : les réponses changent d'un jour à l'autre. On mesure, on corrige, puis on refait la même mesure quelques semaines plus tard."),
    ],
    sources=["oai", "ahrefs", "self"],
))

# =====================================================================================
PAGES.append(dict(
    path="visibilite-ia/google-ai-mode-suisse.html", court="Google AI Mode en Suisse", ariane=AR_Q,
    title="Google AI Mode en Suisse : ce qui change pour une PME | Up2Front",
    titre="Google AI Mode en Suisse : ce qui change pour une PME",
    desc="Depuis mars 2025, Google affiche des aperçus IA en Suisse, et depuis octobre 2025 un mode IA complet. Ce que cela change pour la visibilité d'une PME romande, et comment le mesurer.",
    eyebrow="Question fréquente · Google",
    h1="Google AI Mode <em>en Suisse</em>",
    chapo="Google ne se contente plus d'une liste de liens. Pour beaucoup de questions, il écrit d'abord une réponse, et c'est cette réponse que le client lit en premier.",
    reponse="Google affiche des <strong>aperçus IA</strong> (AI Overviews) en Suisse depuis le <strong>26 mars 2025</strong>, en allemand, français, italien et anglais. Le <strong>mode IA</strong> (AI Mode), un onglet de conversation complet, est activé en Suisse depuis <strong>octobre 2025</strong>. Les deux s'appuient sur l'index Google habituel, et aucun balisage spécial n'est nécessaire pour y figurer.",
    corps='''    <h2>Aperçus IA et mode IA : deux choses différentes</h2>
    <ul>
      <li><strong>Les aperçus IA</strong> apparaissent au-dessus des résultats habituels, pour certaines recherches. Ils résument et citent quelques sources.</li>
      <li><strong>Le mode IA</strong> est un onglet séparé où l'on converse avec Google. Il cite davantage de sources et peut afficher une carte avec des établissements.</li>
    </ul>

    <h2>Ce que ça change pour une PME</h2>
    <p>Quand un client demande « quel est le meilleur chauffagiste à Carouge ? », Google AI Mode répond par une sélection de trois à huit noms. Être dans cette sélection, ou pas, se joue avant le moindre clic. Dans notre <a href="{R}etudes/visibilite-ia-architectes-geneve.html">étude sur les architectes genevois</a>, Google a donné trois classements différents à la même question en une heure.</p>

    <h2>Comment le mesurer</h2>
    <ul>
      <li><strong>La Search Console</strong> (gratuite) propose depuis juin 2026 des rapports sur les affichages de votre site dans les aperçus IA et le mode IA. Le déploiement est progressif ; ces rapports comptent les affichages, pas les clics.</li>
      <li><strong>Un relevé</strong> : poser la question d'un client en session neuve, deux fois à quelques heures d'écart. Voir <a href="{R}visibilite-ia/methode.html">la méthode</a>.</li>
    </ul>

    <h2>Ce qui aide à y figurer</h2>
    <ul>
      <li>Être indexé par Google et éligible à un extrait : c'est la seule condition que Google pose.</li>
      <li>Des pages qui répondent directement à la question, avec le métier et la ville.</li>
      <li>Une fiche Google Business complète et des avis de vrais clients, pour les recherches locales.</li>
      <li>Être cité par d'autres sites que Google juge fiables.</li>
    </ul>
    <p class="note">Bloquer « Google-Extended » dans robots.txt ne retire pas un site des aperçus IA : ce réglage concerne l'entraînement des modèles Gemini, pas la recherche.</p>''',
    faq=[
        ("Depuis quand Google AI Mode est-il disponible en Suisse ?", "Google a activé AI Mode en Suisse en octobre 2025. Les aperçus IA (AI Overviews) sont affichés en Suisse depuis le 26 mars 2025, dans les quatre langues."),
        ("Faut-il un balisage spécial pour apparaître dans Google AI Mode ?", "Non. Google indique qu'aucune exigence supplémentaire n'est nécessaire : la page doit être indexée et éligible à un extrait dans la recherche classique."),
        ("Comment savoir si mon site apparaît dans les aperçus IA de Google ?", "La Search Console propose depuis juin 2026 un rapport des affichages dans les fonctions IA, en déploiement progressif. Un relevé manuel répété complète cette mesure."),
    ],
    sources=["aio_ch", "aimode_ch", "google_aif", "gsc_ia", "etude"],
))

# =====================================================================================
TERMES = [
    ("GEO (Generative Engine Optimization)", "L'ensemble des actions qui aident une entreprise à être comprise et citée par les moteurs de réponse IA.", "Le terme se répand en Suisse romande depuis 2025 ; on dit aussi « référencement IA »."),
    ("Moteur de réponse", "Un service qui répond par un texte rédigé plutôt que par une liste de liens : Google AI Mode, ChatGPT, Gemini, Perplexity, Claude, Copilot.", "En mars 2026, 41,6 % des Suisses utilisaient l'IA pour remplacer un moteur de recherche classique (Comparis / Innofact)."),
    ("Aperçus IA (AI Overviews)", "Le résumé rédigé par Google au-dessus des résultats habituels, pour certaines recherches.", "Affichés en Suisse depuis le 26 mars 2025, en allemand, français, italien et anglais."),
    ("Mode IA (AI Mode)", "L'onglet de conversation de Google, qui répond longuement et cite plusieurs sources.", "Activé en Suisse en octobre 2025."),
    ("Citation", "Le fait qu'un moteur de réponse nomme une entreprise ou affiche un lien vers son site comme source.", "Nous distinguons « être nommé » et « être cité comme source » : ce n'est pas la même chose."),
    ("Passage", "Une interrogation d'un moteur, à une heure donnée. Un relevé sérieux en compte au moins deux par question.", "Dans l'étude Up2Front du 15 septembre 2026, Google AI Mode a donné trois classements différents en une heure."),
    ("Session neuve", "Une interrogation sans compte connecté ni historique, pour que le moteur ne réponde pas à partir de ce qu'il sait déjà de vous.", ""),
    ("Relevé", "La trace datée de ce qu'un moteur a répondu, mot pour mot, à une question donnée.", "Le Relevé d'Up2Front porte sur trois moteurs et deux passages."),
    ("Entité", "La façon dont une machine identifie une entreprise : un nom, une activité, un lieu, des liens vers ses autres profils. Une entité floue est mal citée.", ""),
    ("Données structurées (schema.org)", "Un code invisible qui décrit une page aux machines : qui l'a écrite, de quelle entreprise il s'agit, où elle se trouve.", "Utile pour l'identité ; Google précise qu'aucun balisage spécial n'est nécessaire pour ses fonctions IA."),
    ("robots.txt", "Le fichier qui dit aux robots quelles pages ils peuvent lire. Un site qui bloque les robots des IA ne peut pas être cité.", ""),
    ("OAI-SearchBot", "Le robot avec lequel ChatGPT indexe le web pour ses réponses. À distinguer de GPTBot, qui sert à l'entraînement.", ""),
    ("Mention de marque", "Le fait que votre nom apparaisse sur un autre site, avec ou sans lien. C'est le signal qui pèse le plus pour être cité.", "Annuaires suisses, registres de profession, presse régionale."),
    ("llms.txt", "Un fichier proposé pour guider les IA dans un site. Aucun effet démontré à ce jour, selon Google.", ""),
    ("Annuaires suisses", "local.ch, search.ch et les registres de profession : des sources que les moteurs consultent pour vérifier qu'une entreprise existe.", "Sur search.ch, un astérisque signale qu'une entreprise ne souhaite pas recevoir de publicité."),
    ("Rapport IA de la Search Console", "Le rapport gratuit de Google qui compte les affichages d'un site dans les aperçus IA et le mode IA.", "Annoncé le 3 juin 2026, déployé progressivement, déjà visible chez des utilisateurs suisses."),
]
PAGES.append(dict(
    path="visibilite-ia/glossaire.html", court="Glossaire GEO", type="DefinedTermSet", termes=TERMES,
    title="Glossaire GEO : les mots de la visibilité IA, avec le contexte suisse | Up2Front",
    titre="Glossaire GEO suisse",
    desc="Seize termes de la visibilité IA et du GEO expliqués simplement, avec pour chacun le contexte suisse : dates de lancement, annuaires .ch, chiffres locaux.",
    eyebrow="Glossaire · 16 termes",
    h1="Glossaire <em>GEO</em>, version suisse",
    chapo="Les mots de la visibilité dans les moteurs de réponse IA, expliqués en une ou deux phrases. Pour chacun, ce qui est propre à la Suisse.",
    reponse="",
    corps='    <dl class="gl">\n' + "\n".join(
        f'      <div id="t{i}"><dt>{t}</dt><dd>{d}' + (f'<span class="ch">{c}</span>' if c else "") + "</dd></div>"
        for i, (t, d, c) in enumerate(TERMES, 1)) + "\n    </dl>",
    sources=["comparis", "aio_ch", "aimode_ch", "gsc_ia", "google_aif", "oai", "etude"],
))

# =====================================================================================
PAGES.append(dict(
    path="etudes/index.html", court="Études", type="CollectionPage", maj="2026-10-28",
    title="Études de visibilité IA en Suisse romande | Up2Front",
    titre="Études de visibilité IA en Suisse romande",
    desc="Ce que Google AI Mode, ChatGPT et Gemini répondent vraiment, métier par métier, en Suisse romande. Relevés datés à la minute, méthode publiée, limites écrites.",
    eyebrow="Études · Suisse romande",
    h1="Ce que les IA répondent, <em>métier par métier</em>",
    chapo="Chaque étude pose aux moteurs de réponse les questions que posent de vrais clients, note l'heure à la minute et publie les réponses. La méthode est publique et les limites sont écrites noir sur blanc.",
    reponse="",
    corps='''    <h2>Publiées</h2>
    <div class="pole">
      <a href="{R}etudes/visibilite-ia-architectes-geneve.html"><b>Architectes à Genève</b><span>15 septembre 2026 · 4 moteurs · Google a répondu trois fois, et jamais la même chose.</span></a>
      <a href="{R}etudes/pompes-a-chaleur-geneve-ia-octobre-2026.html"><b>Pompes à chaleur à Genève</b><span>27 octobre 2026 · 3 moteurs · 180 réponses : la première source est ge.ch, pas un installateur.</span></a>
      <a href="{R}etudes/informatique-pme-geneve-ia-octobre-2026.html"><b>Informatique et cybersécurité pour PME à Genève</b><span>27 et 28 octobre 2026 · 3 moteurs · 96 réponses : 14 prestataires sur 16 jamais nommés.</span></a>
      <a href="{R}visibilite-ia/ce-que-les-ia-disent-d-up2front.html"><b>Up2Front, mesuré par Up2Front</b><span>Chaque mois · 3 moteurs · octobre 2026 : 0 réponse sur 12.</span></a>
    </div>

    <h2>En préparation</h2>
    <p>Installateurs solaires en Suisse romande, fiduciaires, piscinistes et menuisiers. Les chiffres publiés seront agrégés ; seules les entreprises bien citées par les moteurs seront nommées.</p>

    <h2>Comment nous travaillons</h2>
    <p>Une question de client, en session neuve, à plusieurs moteurs, avec au moins deux passages espacés. Chaque réponse est conservée mot pour mot. Voir <a href="{R}visibilite-ia/methode.html">la méthode</a>.</p>''',
    sources=["stgall"],
    ariane=[],
))

# =====================================================================================
PAGES.append(dict(
    path="etudes/pompes-a-chaleur-geneve-ia-octobre-2026.html", court="Pompes à chaleur à Genève",
    ariane=[("Études", "etudes/")], type="Report", publie="2026-10-27",
    title="Pompes à chaleur à Genève : ce que répondent les IA — étude, octobre 2026 | Up2Front",
    titre="Pompes à chaleur à Genève : ce que Google AI Mode, ChatGPT et Gemini répondent (octobre 2026)",
    desc="180 réponses IA analysées le 27 octobre 2026 : quand un Genevois cherche un installateur de pompe à chaleur, les moteurs nomment 163 entreprises différentes, citent d'abord ge.ch et changent d'avis en quelques heures.",
    eyebrow="Étude · chauffage et pompes à chaleur · Genève",
    h1="Pompes à chaleur à Genève : <em>ce que répondent les IA</em>",
    chapo="Nous avons posé 30 questions de propriétaires genevois à trois moteurs de réponse, deux fois dans la même journée. Voici ce qu'ils répondent, quelles sources ils lisent et à quel point leurs réponses tiennent.",
    reponse="Le <strong>27 octobre 2026</strong>, 30 questions sur l'installation d'une pompe à chaleur à Genève ont produit <strong>180 réponses</strong> de Google AI Mode, ChatGPT et Gemini. Les moteurs y nomment <strong>163 entreprises différentes</strong>, environ <strong>4 par réponse</strong>. La source la plus citée n'est le site d'aucune entreprise : c'est <strong>la page de l'État de Genève sur les pompes à chaleur</strong>. Et pour <strong>près d'une entreprise sur cinq</strong>, le même moteur l'a citée le matin et oubliée l'après-midi, ou l'inverse.",
    corps='''    <h2>Le protocole</h2>
    <ul>
      <li><strong>30 questions</strong> formulées comme un propriétaire les poserait (« chauffagiste pour installer une pompe à chaleur dans une maison à Genève », « installateur de pompe à chaleur pour chauffer une piscine à Genève »…), chacune pensée pour le créneau d'un installateur genevois réel.</li>
      <li><strong>3 moteurs</strong> : Google AI Mode, ChatGPT et Gemini (version Flash-Lite, interrogée par programme).</li>
      <li><strong>2 passages</strong> le même jour, entre 14h15 et 19h40 heure de Genève, en session neuve, sans historique.</li>
      <li>Chaque réponse est <strong>conservée mot pour mot</strong>, avec l'heure à la minute, puis relue par une personne avant analyse.</li>
    </ul>

    <h2>Ce que nous avons trouvé</h2>
    <h3>1. L'IA ne cite pas « le » meilleur installateur : elle en cite beaucoup</h3>
    <p>Sur 180 réponses, <strong>163 entreprises différentes</strong> sont nommées. Une réponse en nomme environ quatre. ChatGPT est le plus généreux (4,5 noms en moyenne), Gemini le plus avare (2,8).</p>

    <h3>2. Plus d'un tiers des installateurs étudiés n'apparaît jamais</h3>
    <p>Sur les 30 installateurs genevois dont nous avions reformulé la question type, <strong>11 n'ont été nommés dans aucune des six réponses</strong> les concernant. Les écarts entre moteurs sont nets :</p>
    <div class="tab"><table>
      <thead><tr><th>Moteur</th><th>Réponses où l'installateur visé est nommé</th><th>Réponses qui citent au moins une source</th></tr></thead>
      <tbody>
        <tr><td>ChatGPT</td><td class="num">24 sur 60 (40 %)</td><td class="num">60 sur 60</td></tr>
        <tr><td>Google AI Mode</td><td class="num">15 sur 60 (25 %)</td><td class="num">40 sur 60</td></tr>
        <tr><td>Gemini</td><td class="num">7 sur 60 (12 %)</td><td class="num">50 sur 60</td></tr>
      </tbody>
    </table></div>
    <p class="note">Être visible dans ChatGPT ne dit rien de Gemini : il faut mesurer chaque moteur séparément.</p>

    <h3>3. La première source n'est pas un site d'entreprise</h3>
    <p>Les moteurs construisent leur réponse à partir de pages publiques genevoises avant les sites des installateurs :</p>
    <div class="tab"><table>
      <thead><tr><th>Source citée</th><th>Réponses (sur 180)</th></tr></thead>
      <tbody>
        <tr><td>ge.ch, pages de l'État de Genève (surtout « Installer ou remplacer un chauffage : pompe à chaleur » et les subventions énergie)</td><td class="num">66 (37 %)</td></tr>
        <tr><td>local.ch, annuaire</td><td class="num">32 (18 %)</td></tr>
        <tr><td>sig-ge.ch, Services industriels de Genève (pages pompes à chaleur pour villas)</td><td class="num">27 (15 %)</td></tr>
        <tr><td>search.ch, annuaire</td><td class="num">13 (7 %)</td></tr>
        <tr><td>Le site de l'installateur visé par la question</td><td class="num">30 (17 %)</td></tr>
      </tbody>
    </table></div>
    <p>Pour un installateur, cela veut dire deux choses : une fiche complète et exacte dans les annuaires que les moteurs lisent compte autant que son propre site, et son site doit répondre aux questions que les pages officielles soulèvent (subventions, autorisations, délais).</p>

    <h3>4. La même question ne donne pas la même réponse quelques heures plus tard</h3>
    <p>Pour chaque installateur et chaque moteur, nous avons comparé les deux passages. Dans <strong>16 cas sur 90 (18 %)</strong>, l'installateur était nommé à un passage et absent à l'autre. Une capture d'écran unique ne prouve donc ni une présence, ni une absence.</p>

    <h2>Ce qu'un installateur peut faire, sans payer personne</h2>
    <ol>
      <li>Poser lui-même la question de ses clients aux trois moteurs, deux fois, en suivant <a href="{R}visibilite-ia/methode.html">notre méthode</a>.</li>
      <li>Vérifier et compléter sa fiche sur local.ch et search.ch : nom exact, adresse, téléphone, prestations « pompe à chaleur ».</li>
      <li>Écrire sur son site une page claire par prestation (pompe à chaleur pour villa, pour piscine, remplacement d'une chaudière), avec la commune desservie et les démarches genevoises.</li>
      <li>Remesurer dans trois mois, avec les mêmes questions.</li>
    </ol>

    <h2>Limites</h2>
    <p>Un seul jour de mesure, un seul canton, des questions en français. Gemini a été interrogé dans sa version Flash-Lite, plus économe que celle de l'application grand public. Les 30 questions visaient chacune le créneau d'un installateur précis : ce n'est pas un classement du marché genevois. <strong>Nous ne publions aucun nom d'entreprise avec un score</strong> : chaque installateur concerné peut demander son propre relevé, offert, avec les réponses complètes.</p>''',
    faq=[
        ("Quelles sources les IA utilisent-elles pour recommander un installateur de pompe à chaleur à Genève ?", "Dans 180 réponses relevées le 27 octobre 2026, la source la plus citée est la page de l'État de Genève sur les pompes à chaleur (ge.ch, 37 % des réponses), devant l'annuaire local.ch (18 %), les pages des SIG (15 %) et search.ch (7 %). Le site de l'installateur visé n'était cité que dans 17 % des réponses."),
        ("ChatGPT, Gemini et Google AI Mode donnent-ils les mêmes installateurs ?", "Non. L'installateur visé par la question était nommé dans 40 % des réponses de ChatGPT, 25 % de celles de Google AI Mode et 12 % de celles de Gemini."),
        ("Les réponses des IA sont-elles stables ?", "Pas tout à fait. En reposant la même question au même moteur quelques heures plus tard, un installateur sur cinq environ apparaissait à un passage et disparaissait à l'autre."),
    ],
    sources=["stgall"],
    sources_extra=[("Relevé Up2Front du 27 octobre 2026 (Google AI Mode, ChatGPT, Gemini), 180 réponses archivées mot pour mot", "https://up2front.com/etudes/pompes-a-chaleur-geneve-ia-octobre-2026.html"),
                   ("République et canton de Genève, « Installer ou remplacer un chauffage : pompe à chaleur »", "https://www.ge.ch/installer-remplacer-chauffage/pompe-chaleur")],
))

# =====================================================================================
PAGES.append(dict(
    path="etudes/informatique-pme-geneve-ia-octobre-2026.html", court="Informatique pour PME à Genève",
    ariane=[("Études", "etudes/")], type="Report", publie="2026-10-28", maj="2026-10-28",
    title="Informatique et cybersécurité pour PME à Genève : ce que répondent les IA — étude, octobre 2026 | Up2Front",
    titre="Informatique et cybersécurité pour PME à Genève : ce que Google AI Mode, ChatGPT et Gemini répondent (octobre 2026)",
    desc="96 réponses IA analysées les 27 et 28 octobre 2026 : quand une PME genevoise cherche un informaticien ou un spécialiste en cybersécurité, les moteurs nomment 163 entreprises, mais 14 des 16 prestataires étudiés n'apparaissent jamais.",
    eyebrow="Étude · informatique et cybersécurité · Genève",
    h1="Informatique pour PME à Genève : <em>ce que répondent les IA</em>",
    chapo="Nous avons posé 16 questions de dirigeants de PME genevoises à trois moteurs de réponse, une fois le soir et une fois le lendemain matin. Voici qui ils nomment, quelles sources ils lisent et à quel point leurs réponses tiennent.",
    reponse="Les <strong>27 et 28 octobre 2026</strong>, 16 questions sur l'informatique et la cybersécurité d'une PME à Genève ont produit <strong>96 réponses</strong> de Google AI Mode, ChatGPT et Gemini. Les moteurs y nomment <strong>163 entreprises différentes</strong>, environ <strong>4,5 par réponse</strong>. Mais <strong>14 des 16 prestataires genevois étudiés n'ont été nommés dans aucune réponse</strong>. Contrairement au chauffage, les moteurs lisent ici surtout <strong>les sites des prestataires eux-mêmes</strong>, très peu les annuaires. Et leurs réponses sont stables : un seul cas sur vingt-quatre a changé d'un passage à l'autre.",
    corps='''    <h2>Le protocole</h2>
    <ul>
      <li><strong>16 questions</strong> formulées comme un dirigeant de PME les poserait (« informaticien pour une petite entreprise à Genève », « entreprise pour faire un test d'intrusion dans une PME à Genève », « prestataire informatique pour une régie immobilière à Genève »…), chacune pensée pour le créneau d'un prestataire genevois réel.</li>
      <li><strong>3 moteurs</strong> : Google AI Mode, ChatGPT et Gemini (version Flash-Lite, interrogée par programme).</li>
      <li><strong>2 passages</strong> : le 27 octobre entre 20h05 et 20h20, puis le 28 octobre entre 6h17 et 6h28, heure de Genève, en session neuve, sans historique.</li>
      <li>Chaque réponse est <strong>conservée mot pour mot</strong>, avec l'heure à la minute, puis relue par une personne avant analyse.</li>
    </ul>

    <h2>Ce que nous avons trouvé</h2>
    <h3>1. Beaucoup de noms, mais une poignée revient sans cesse</h3>
    <p>Sur 96 réponses, <strong>163 entreprises différentes</strong> sont nommées, environ 4,5 par réponse. Google AI Mode est le plus généreux (5,2 noms en moyenne), Gemini le plus avare (3,8). Pourtant la moitié de ces entreprises (82) n'apparaît qu'une seule fois, alors que le prestataire le plus cité revient dans <strong>28 réponses sur 96</strong>. Quelques acteurs captent l'essentiel des recommandations.</p>

    <h3>2. 14 prestataires étudiés sur 16 n'apparaissent jamais</h3>
    <p>Pour chacun des 16 prestataires genevois dont nous avions reformulé la question type, nous avons regardé s'il était nommé dans les six réponses le concernant :</p>
    <div class="tab"><table>
      <thead><tr><th>Moteur</th><th>Réponses où le prestataire visé est nommé</th><th>Réponses qui citent au moins une source</th></tr></thead>
      <tbody>
        <tr><td>ChatGPT</td><td class="num">3 sur 32 (9 %)</td><td class="num">32 sur 32</td></tr>
        <tr><td>Google AI Mode</td><td class="num">2 sur 32 (6 %)</td><td class="num">27 sur 32</td></tr>
        <tr><td>Gemini</td><td class="num">1 sur 32 (3 %)</td><td class="num">18 sur 32</td></tr>
      </tbody>
    </table></div>
    <p class="note">Gemini n'a nommé aucune entreprise dans 5 réponses sur 32 : il a refusé de recommander ou s'en est tenu à des conseils généraux.</p>

    <h3>3. Les moteurs lisent les sites des prestataires, pas les annuaires</h3>
    <p>Dans le chauffage, la première source était la page de l'État de Genève. Ici, c'est l'inverse : la grande majorité des 182 sites cités sont ceux de prestataires informatiques. L'annuaire local.ch ou search.ch n'apparaît que dans <strong>8 réponses sur 96</strong>, et une page officielle (ge.ch, admin.ch, centre national pour la cybersécurité) dans <strong>4</strong>. Le site du prestataire visé par la question n'était cité que dans <strong>6 réponses</strong>.</p>
    <p>Pour un prestataire informatique, cela veut dire que son propre site fait presque tout le travail : une page claire par service (infogérance, test d'intrusion, sauvegarde, formation au phishing), avec la clientèle visée (PME, études d'avocats, régies, pharmacies) et la ville, pèse plus qu'une fiche d'annuaire.</p>

    <h3>4. Des réponses stables d'un jour à l'autre</h3>
    <p>Pour chaque prestataire et chaque moteur, nous avons comparé les deux passages, espacés d'environ dix heures. Dans <strong>2 cas sur 48 (4 %)</strong> seulement, le prestataire était nommé à un passage et absent à l'autre, contre près d'un cas sur cinq dans notre étude sur les pompes à chaleur. Dans ce métier, une absence mesurée deux fois a donc de bonnes chances d'être durable.</p>

    <h2>Ce qu'un prestataire peut faire, sans payer personne</h2>
    <ol>
      <li>Poser lui-même la question de ses clients aux trois moteurs, deux fois, en suivant <a href="{R}visibilite-ia/methode.html">notre méthode</a>.</li>
      <li>Écrire une page par service et par type de client, avec Genève et les communes desservies, plutôt qu'une seule page « services ».</li>
      <li>Rendre visibles ses preuves : certifications, labels, secteurs servis, nom des responsables.</li>
      <li>Remesurer dans trois mois, avec les mêmes questions.</li>
    </ol>

    <h2>Limites</h2>
    <p>Deux passages sur deux jours, un seul canton, des questions en français. Gemini a été interrogé dans sa version Flash-Lite, plus économe que celle de l'application grand public. Les 16 questions visaient chacune le créneau d'un prestataire précis : ce n'est pas un classement du marché genevois. <strong>Nous ne publions aucun nom d'entreprise avec un score</strong> : chaque prestataire concerné peut demander son propre relevé, offert, avec les réponses complètes.</p>''',
    faq=[
        ("Quels prestataires informatiques les IA recommandent-elles aux PME de Genève ?", "Dans 96 réponses relevées les 27 et 28 octobre 2026, Google AI Mode, ChatGPT et Gemini nomment 163 entreprises différentes, environ 4,5 par réponse. Quelques acteurs reviennent très souvent, et 14 des 16 prestataires genevois étudiés n'ont été nommés dans aucune réponse."),
        ("Quelles sources les IA lisent-elles pour recommander un informaticien à Genève ?", "Surtout les sites des prestataires eux-mêmes. Les annuaires local.ch et search.ch n'apparaissent que dans 8 réponses sur 96, et les pages officielles dans 4."),
        ("Les réponses des IA sont-elles stables dans l'informatique ?", "Oui, davantage que dans le chauffage : entre deux passages espacés d'environ dix heures, seuls 2 cas sur 48 ont changé (4 %), contre près d'un sur cinq pour les pompes à chaleur."),
    ],
    sources=["stgall"],
    sources_extra=[("Relevé Up2Front des 27 et 28 octobre 2026 (Google AI Mode, ChatGPT, Gemini), 96 réponses archivées mot pour mot", "https://up2front.com/etudes/informatique-pme-geneve-ia-octobre-2026.html")],
))

# versions anglaises
from _geo_contenu_en import PAGES_EN  # noqa: E402
PAGES += PAGES_EN
