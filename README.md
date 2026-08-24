# Up2Front

Site commercial de `up2front.com`, versionné sur GitHub et déployé automatiquement sur l'hébergement Web Infomaniak.

## Organisation

- `public/` contient uniquement les fichiers mis en ligne.
- `.github/workflows/deploy.yml` déploie `public/` après chaque modification de la branche `main`.
- `public/contact-config.php` contient le secret SMTP uniquement sur Infomaniak. Il est ignoré par Git et préservé lors des déploiements.

## Préparer Infomaniak

1. Ajouter `up2front.com` comme site vierge sur l'hébergement Web.
2. Créer l'adresse `contact@up2front.com` et définir son mot de passe.
3. Dans **FTP / SSH**, créer un compte **FTP uniquement**, limité au dossier du site `up2front.com`.
4. Noter le serveur FTP, l'utilisateur et le mot de passe de ce compte.
5. Dans le Web FTP, créer `contact-config.php` à la racine du site avec ce contenu :

```php
<?php

defined('UP2FRONT_INTERNAL') || exit;

return [
    'smtp_password' => 'MOT_DE_PASSE_DE_CONTACT_UP2FRONT_COM',
];
```

Le mot de passe SMTP ne doit jamais être ajouté au dépôt GitHub.

## Configurer GitHub

Dans **Settings → Secrets and variables → Actions**, créer ces trois secrets :

- `INFOMANIAK_FTP_HOST` : serveur du type `xxxx.ftp.infomaniak.com`
- `INFOMANIAK_FTP_USER` : utilisateur FTP limité au site
- `INFOMANIAK_FTP_PASSWORD` : mot de passe de cet utilisateur FTP

Le premier envoi sur la branche `main` déclenche automatiquement la mise en ligne. Les exécutions sont visibles dans l'onglet **Actions** du dépôt.

## Vérification

1. Ouvrir `https://up2front.com`.
2. Envoyer une demande avec le formulaire.
3. Vérifier la réception dans `contact@up2front.com` et répondre au visiteur avec l'adresse placée en `Reply-To`.
