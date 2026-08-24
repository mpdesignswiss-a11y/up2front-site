# Up2Front

Site de `up2front.com`, versionné et hébergé sur GitHub Pages. Le domaine et l'adresse `contact@up2front.com` restent gérés chez Infomaniak.

## Organisation

- `public/` contient les fichiers du site publiés.
- `public/CNAME` relie le site au domaine `up2front.com`.
- `.github/workflows/deploy.yml` publie automatiquement `public/` après chaque modification de la branche `main`.
- Le formulaire prépare un email adressé à `contact@up2front.com`, car GitHub Pages ne peut pas exécuter PHP.

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

## Vérification

1. Ouvrir `https://up2front.com`.
2. Remplir le formulaire et vérifier que la messagerie s'ouvre avec un email prérempli pour `contact@up2front.com`.
3. Envoyer l'email et vérifier sa réception.
