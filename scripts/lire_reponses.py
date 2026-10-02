#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Robot « réponses » : lit la boîte contact@up2front.com (IMAP), regroupe les
messages reçus par bureau, et les pousse dans le Worker (page d'envoi en ligne)
pour qu'ils s'affichent en fil de discussion.

Tourne tout seul via GitHub Actions (voir .github/workflows/reponses.yml).
Ne casse rien : lecture seule de la boîte, les mails restent où ils sont.

Secrets / variables attendus (env) :
  IMAP_HOST      (déf. mail.infomaniak.com)
  IMAP_USER      (déf. contact@up2front.com)
  IMAP_PASS      *secret* — mot de passe de la boîte
  WORKER_URL     (déf. https://envoi-up2front.mpdesign-swiss.workers.dev)
  WORKER_USER    (déf. alex)
  WORKER_PASS    *secret* — mot de passe du Worker (ENVOI_PASSWORD)
  JOURS          (déf. 60) — on lit les messages reçus depuis N jours
"""
import os, ssl, json, base64, imaplib, email, urllib.request
from email.header import decode_header, make_header
from email.utils import parseaddr, parsedate_to_datetime
from datetime import datetime, timedelta, timezone

IMAP_HOST = os.environ.get("IMAP_HOST", "mail.infomaniak.com")
IMAP_USER = os.environ.get("IMAP_USER", "contact@up2front.com")
IMAP_PASS = os.environ.get("IMAP_PASS", "")
WORKER_URL = os.environ.get("WORKER_URL", "https://envoi-up2front.mpdesign-swiss.workers.dev").rstrip("/")
WORKER_USER = os.environ.get("WORKER_USER", "alex")
WORKER_PASS = os.environ.get("WORKER_PASS", "")
JOURS = int(os.environ.get("JOURS", "60"))

def _auth(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()

def bureaux_par_domaine():
    """Récupère la liste des bureaux du Worker → { domaine: slug }, { email: slug }."""
    req = urllib.request.Request(WORKER_URL + "/api/emails", method="GET")
    req.add_header("Authorization", _auth(WORKER_USER, WORKER_PASS))
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode())
    emails = data.get("emails", {})
    par_dom, par_mail = {}, {}
    for slug, d in emails.items():
        adr = (d.get("email") or "").lower().strip()
        if "@" in adr:
            par_mail[adr] = slug
            par_dom[adr.split("@", 1)[1]] = slug
    return par_dom, par_mail

def _decode(v):
    try: return str(make_header(decode_header(v or "")))
    except Exception: return v or ""

def _texte(msg):
    """Corps en texte simple, décodé, borné."""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition") or ""):
                try:
                    return part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", "replace")
                except Exception:
                    continue
        return ""
    try:
        return msg.get_payload(decode=True).decode(msg.get_content_charset() or "utf-8", "replace")
    except Exception:
        return msg.get_payload() or ""

def main():
    if not IMAP_PASS or not WORKER_PASS:
        raise SystemExit("IMAP_PASS et WORKER_PASS sont requis (secrets GitHub).")
    par_dom, par_mail = bureaux_par_domaine()

    M = imaplib.IMAP4_SSL(IMAP_HOST, ssl_context=ssl.create_default_context())
    M.login(IMAP_USER, IMAP_PASS)
    M.select("INBOX", readonly=True)
    depuis = (datetime.now(timezone.utc) - timedelta(days=JOURS)).strftime("%d-%b-%Y")
    typ, dat = M.search(None, f'(SINCE {depuis})')
    ids = dat[0].split() if dat and dat[0] else []

    fils = {}
    for i in ids:
        typ, d = M.fetch(i, "(RFC822)")
        if not d or not d[0]:
            continue
        msg = email.message_from_bytes(d[0][1])
        nom, adr = parseaddr(msg.get("From", ""))
        adr = (adr or "").lower().strip()
        if not adr or "@" not in adr:
            continue
        slug = par_mail.get(adr) or par_dom.get(adr.split("@", 1)[1])
        if not slug:
            continue  # pas un de nos bureaux
        try:
            dt = parsedate_to_datetime(msg.get("Date"))
            iso = dt.astimezone(timezone.utc).isoformat()
        except Exception:
            iso = ""
        fils.setdefault(slug, []).append({
            "de": _decode(nom) + (" <" + adr + ">" if nom else adr),
            "date": iso,
            "sujet": _decode(msg.get("Subject", "")),
            "texte": _texte(msg).strip()[:4000],
            "sens": "recu",
        })
    try: M.logout()
    except Exception: pass

    for slug in fils:
        fils[slug].sort(key=lambda m: m.get("date", ""))

    corps = json.dumps({"messages": fils}).encode()
    req = urllib.request.Request(WORKER_URL + "/api/messages", data=corps, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", _auth(WORKER_USER, WORKER_PASS))
    with urllib.request.urlopen(req, timeout=30) as r:
        rep = json.loads(r.read().decode())
    print("Réponses poussées :", rep)

if __name__ == "__main__":
    main()
