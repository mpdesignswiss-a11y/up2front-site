<?php
/* ============================================================
   Up2Front — traitement du formulaire de contact
   Envoi SMTP authentifié via Infomaniak (mail.infomaniak.com).

   Infomaniak désactive la fonction PHP mail() par défaut et
   déconseille son usage : les messages partent « non authentifiés »,
   sont soumis à des limites et finissent souvent en indésirables.
   On passe donc par PHPMailer en SMTP, comme leur doc le recommande.

   Le secret SMTP est chargé depuis contact-config.php. Ce fichier
   existe uniquement sur Infomaniak et n'est jamais versionné.
   ============================================================ */

declare(strict_types=1);

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception as MailException;

// L'adresse d'authentification et l'expéditeur doivent être identiques.
const SMTP_USER = 'contact@up2front.com';
const DESTINATAIRE = 'contact@up2front.com';

const NOM_SITE  = 'Up2Front';
const SMTP_HOST = 'mail.infomaniak.com';
const SMTP_PORT = 465;   // 465 = SSL/TLS. Si bloqué, mettre 587 (STARTTLS).

/* ============================================================
   À partir d'ici, rien à modifier
   ============================================================ */

ini_set('display_errors', '0');
date_default_timezone_set('Europe/Zurich');

$estFetch = ($_SERVER['HTTP_X_REQUESTED_WITH'] ?? '') === 'fetch';

function repondre(int $code, array $data): void {
    global $estFetch;
    http_response_code($code);
    if ($estFetch) {
        header('Content-Type: application/json; charset=utf-8');
        header('X-Content-Type-Options: nosniff');
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
    } else {
        // Repli sans JavaScript : retour sur la page
        header('Location: index.html?envoi=' . (($data['ok'] ?? false) ? 'ok' : 'erreur') . '#start');
    }
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    repondre(405, ['ok' => false, 'error' => 'Méthode non autorisée']);
}

define('UP2FRONT_INTERNAL', true);
$configPath = __DIR__ . '/contact-config.php';
if (!is_file($configPath)) {
    error_log('Up2Front : fichier contact-config.php introuvable');
    repondre(500, ['ok' => false, 'error' => 'Configuration incomplète']);
}
$config = require $configPath;
$smtpPass = is_array($config) ? (string)($config['smtp_password'] ?? '') : '';
if ($smtpPass === '' || $smtpPass === 'REMPLACEZ_PAR_LE_MOT_DE_PASSE') {
    error_log('Up2Front : mot de passe SMTP non configuré');
    repondre(500, ['ok' => false, 'error' => 'Configuration incomplète']);
}

/* --- Anti-robots : champ piège + soumission instantanée --- */
if (trim((string)($_POST['site'] ?? '')) !== '') {
    repondre(200, ['ok' => true]);
}
$ts = (int)($_POST['ts'] ?? 0);
if ($ts > 0 && (time() - $ts) < 3) {
    repondre(200, ['ok' => true]);
}

/* --- Nettoyage --- */
function champ(string $cle, int $max = 200): string {
    $v = trim((string)($_POST[$cle] ?? ''));
    $v = str_replace(["\r", "\n", "\0"], ' ', $v);   // anti-injection d'en-têtes
    return mb_substr($v, 0, $max);
}
function bloc(string $cle, int $max = 4000): string {
    return mb_substr(str_replace("\0", '', trim((string)($_POST[$cle] ?? ''))), 0, $max);
}

$nom        = champ('nom', 120);
$entreprise = champ('entreprise', 140);
$email      = champ('email', 180);
$whatsapp   = champ('whatsapp', 40);
$metier     = champ('metier', 80);
$contenus   = champ('contenus', 80);
$devis      = champ('devis', 240);
$message    = bloc('message');

/* --- Validation : nom et email seulement --- */
$erreurs = [];
if (mb_strlen($nom) < 2)                        { $erreurs[] = 'nom'; }
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { $erreurs[] = 'email'; }
if ($erreurs) {
    repondre(422, ['ok' => false, 'champs' => $erreurs]);
}

/* --- Contenu --- */
$sujet = 'Demande site — ' . ($entreprise !== '' ? $entreprise : $nom);

$champs = [
    'Nom'           => $nom,
    'Commerce'      => $entreprise ?: '—',
    'Email'         => $email,
    'WhatsApp'      => $whatsapp ?: '—',
    'Métier'        => $metier ?: '—',
    'Contenus'      => $contenus ?: '—',
    'Devis composé' => $devis ?: '—',
];

$texte = "Nouvelle demande depuis le site\n" . str_repeat('-', 46) . "\n";
foreach ($champs as $k => $v) {
    $texte .= str_pad($k, 15) . ': ' . $v . "\n";
}
$texte .= "\nMessage :\n" . ($message !== '' ? $message : '—') . "\n\n"
        . str_repeat('-', 46) . "\nReçu le " . date('d.m.Y à H:i') . "\n";

$html = '<h2 style="font:600 18px system-ui">Nouvelle demande depuis le site</h2>'
      . '<table style="font:14px system-ui;border-collapse:collapse">';
foreach ($champs as $k => $v) {
    $html .= '<tr><td style="padding:6px 16px 6px 0;color:#666">'
           . htmlspecialchars($k, ENT_QUOTES, 'UTF-8')
           . '</td><td style="padding:6px 0"><strong>'
           . htmlspecialchars($v, ENT_QUOTES, 'UTF-8') . '</strong></td></tr>';
}
$html .= '</table><p style="font:14px system-ui;white-space:pre-wrap;margin-top:18px">'
       . htmlspecialchars($message !== '' ? $message : '—', ENT_QUOTES, 'UTF-8') . '</p>';

/* --- Envoi --- */
$src = __DIR__ . '/PHPMailer/src/';
if (!is_file($src . 'PHPMailer.php')) {
    error_log('Up2Front : PHPMailer introuvable dans ' . $src);
    repondre(500, ['ok' => false, 'error' => 'Configuration incomplète']);
}
require $src . 'Exception.php';
require $src . 'PHPMailer.php';
require $src . 'SMTP.php';

$mail = new PHPMailer(true);
try {
    $mail->isSMTP();
    $mail->Host       = SMTP_HOST;
    $mail->SMTPAuth   = true;
    $mail->Username   = SMTP_USER;
    $mail->Password   = $smtpPass;
    $mail->SMTPSecure = (SMTP_PORT === 587)
        ? PHPMailer::ENCRYPTION_STARTTLS
        : PHPMailer::ENCRYPTION_SMTPS;
    $mail->Port    = SMTP_PORT;
    $mail->CharSet = 'UTF-8';

    // L'expéditeur DOIT être l'adresse authentifiée.
    // L'adresse du visiteur part en Reply-To, jamais en expéditeur.
    $mail->setFrom(SMTP_USER, NOM_SITE);
    $mail->addAddress(DESTINATAIRE);
    $mail->addReplyTo($email, $nom);

    $mail->isHTML(true);
    $mail->Subject = $sujet;
    $mail->Body    = $html;
    $mail->AltBody = $texte;

    $mail->send();
    repondre(200, ['ok' => true]);

} catch (MailException $e) {
    error_log('Up2Front — échec SMTP : ' . $mail->ErrorInfo);
    repondre(500, ['ok' => false, 'error' => "L'envoi a échoué"]);
}
