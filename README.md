# Up2Front

Site de `up2front.com`, versionné et hébergé sur GitHub Pages. Le domaine et l'adresse `contact@up2front.com` restent gérés chez Infomaniak.

## Organisation

- `public/` contient les fichiers du site publiés.
- `public/index.html` contient la version française et détecte la langue du navigateur à la première visite.
- `public/en/index.html` contient la version anglaise complète.
- Le bouton **FR / EN** mémorise ensuite le choix du visiteur.
- `public/CNAME` relie le site au domaine `up2front.com`.
- `.github/workflows/deploy.yml` publie automatiquement `public/` après chaque modification de la branche `main`.
- Les deux formulaires transmettent directement les demandes à `contact@up2front.com` avec Web3Forms et précisent la langue utilisée, car GitHub Pages ne peut pas exécuter PHP.

## Activer GitHub Pages

1. Le dépôt doit être **Public** avec l'offre gratuite GitHub, ou privé avec une offre GitHub compatible.
2. Dans **Settings → Pages**, choisir **GitHub Actions** comme source.
3. Dans **Custom domain**, saisir `up2front.com` puis enregistrer.

## Relier le domaine Infomaniak

Dans la zone DNS de `up2front.com`, conserver tous les enregistrements email (`MX`, SPF, DKIM et DMARC) et modifier uniquement les enregistrements Web :

- quatre enregistrements `A` pour le domaine racine : `185.199.108.153`, `185.199.109.153`, `185.199.110.153` et `185.199.111.153` ;
- un `CNAME` pour `www` vers `mpdesignswiss-a11y.github.io`.

Après propagation du DNS, activer **Enforce HTTPS** dans **Settings → Pages**.

## Publication

Chaque envoi de code sur la branche `main` déclenche une publication. Son avancement est visible dans l'onglet **Actions** du dépôt.

## Référencement

Le site comprend des titres et descriptions propres à chaque langue, des adresses canoniques, les liens linguistiques `hreflang`, un plan de site XML, les consignes d'indexation, des données structurées et une image de partage pour les réseaux sociaux. Le plan de site à déclarer dans Google Search Console est `https://up2front.com/sitemap.xml`.

## Vérification

1. Ouvrir `https://up2front.com`.
2. Envoyer une demande avec le formulaire.
3. Vérifier l'affichage du message de réussite et la réception dans `contact@up2front.com`.
