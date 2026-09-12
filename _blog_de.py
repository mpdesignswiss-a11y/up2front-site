# -*- coding: utf-8 -*-
"""
Die neun Blogartikel, auf Deutsch (Schweizer Hochdeutsch).

Übersetzung von `_blog_fr.py`, Struktur identisch: gleiche Variablen,
gleiche Schlüssel, gleiche Reihenfolge der neun Artikel. Die `slug` und
alle internen Links bleiben unverändert — die URL sind in allen vier
Sprachen dieselben.

Schreibweise: kein Eszett, immer «ss». Sie-Form. Die drei Angebotsnamen
(Landing Pro, Site Complet, Site Étendu) sind Markennamen und bleiben
unübersetzt.

Redaktionslinie wie im Rest der Website: keine erfundenen Zahlen, keine
Statistik ohne Quelle, nichts, was den veröffentlichten AGB widerspricht.
Marktpreise werden als Spanne und mit Datum genannt, weil sie sich
bewegen.
"""

INDEX = {
    "sur_titre": "Das Journal",
    "h1": ["Was uns vorher", "niemand gesagt hat."],
    "lede": "Neun kurze Artikel, geschrieben für Schweizer KMU. Echte "
            "Preise, echte Fristen, und was wir an Ihrer Stelle tun "
            "würden.",
    "sec_t": "Die Artikel.",
    "sec_c": "Sortiert vom meistgefragten zum technischsten. Keiner "
             "braucht die anderen, um gelesen zu werden.",
    "appel_h2": "Eine Frage, die hier nicht behandelt wird?",
    "appel_p": "Schreiben Sie sie uns, wir antworten am selben Tag, von "
               "Montag bis Freitag. Und wenn die Antwort andere "
               "interessiert, wird ein Artikel daraus.",
}

ARTICLES = [
 {
  "slug": "prix-site-web-suisse.html",
  "cat": "Preise",
  "titre": "Was kostet eine Website in der Schweiz 2026 wirklich?",
  "h1": ["Was kostet eine Website", "in der Schweiz wirklich?"],
  "desc": "Die vier Preisspannen des Schweizer Markts, was die Rechnung "
          "treibt, und die jährlichen Kosten, die am Anfang niemand "
          "beziffert.",
  "dek": "Kurze Antwort: zwischen CHF&nbsp;300 und CHF&nbsp;30&nbsp;000. Der "
         "Unterschied ist keine Frage der Qualität, sondern dessen, was man "
         "kauft. So liest man eine Offerte.",
  "lecture": "7 Min.",
  "corps": """
<p>Niemand beantwortet diese Frage je, und das ist ärgerlich. Also
beginnen wir mit der Zahl: In der Schweiz kostet eine professionelle
Website für ein KMU im Jahr 2026 zwischen <strong>CHF&nbsp;300 und
CHF&nbsp;30&nbsp;000</strong>. Dieser Faktor hundert ist kein
Qualitätsunterschied. Es ist ein Unterschied im Umfang — und vor allem
in den verrechneten Arbeitsstunden.</p>

<p>Der Rest dieses Artikels dient dazu, herauszufinden, in welche Spanne
Sie gehören, und nicht den Preis einer Spanne für den Inhalt der
vorherigen zu bezahlen.</p>

<h2>Die vier Spannen des Schweizer Markts</h2>

<p><strong>Von CHF&nbsp;0 bis 500 — Sie machen es selbst.</strong> Ein
Baukasten, eine Vorlage aus dem Katalog, Ihre Texte, Ihre Fotos. Die
tatsächlichen Kosten sind nicht das Abo, sondern Ihr Wochenende. Rechnen
Sie mit zwanzig bis vierzig Stunden für ein anständiges Ergebnis, mehr,
wenn Sie das Werkzeug erst kennenlernen. Tragbar, wenn Ihre Website nur
eine Visitenkarte ist.</p>

<p><strong>Von CHF&nbsp;300 bis 1 500 — das Pauschalangebot.</strong> Eine
Fachperson arbeitet auf einer bereits erprobten Struktur, Sie füllen ein
Briefing aus, sie liefert in wenigen Tagen. Hier sind wir angesiedelt, mit
Festpreisen von <a href="../offres/pro-landing-page.html">CHF
290</a>, <a href="../offres/ultimate-website.html">CHF 490</a> und
<a href="../offres/advanced-website.html">CHF 690</a>. Der Preis hält,
weil der Umfang im Voraus festgelegt ist, nicht weil die Arbeit
geschludert wäre.</p>

<p><strong>Von CHF&nbsp;3 000 bis 12 000 — massgeschneidert von
Selbstständigen oder kleinen Studios.</strong> Man startet auf einem
weissen Blatt: Workshops, Seitenstruktur, Entwürfe, Korrekturrunden,
Umsetzung. Zwei bis acht Wochen. Das ist das richtige Budget, sobald Ihre
Website etwas Besonderes können muss — einen Konfigurator, eine
Reservation, einen Katalog, der sich bewegt.</p>

<p><strong>Von CHF&nbsp;15 000 bis 30 000 und darüber — die
Agentur.</strong> Strategie, Art Direction, Redaktion, Entwicklung,
Betreuung, und mehrere Personen am Tisch. Gerechtfertigt, wenn die
Website ein Hauptverkaufskanal ist und ein gewonnener Prozentpunkt bei der
Konversion mehrere Zehntausend Franken pro Jahr wert ist.</p>

<h2>Was die Rechnung wirklich treibt</h2>

<p>Fast nie das Design. Es sind, der Reihe nach:</p>

<ul>
  <li><strong>Unbegrenzte Korrekturrunden.</strong> Ein Projekt ohne
  schriftlichen Umfang driftet ab, und die Abweichung wird nach Stunden
  verrechnet. Das ist der erste versteckte Posten jeder Offerte.</li>
  <li><strong>Der Inhalt.</strong> Wenn die Agentur Ihre Texte schreiben,
  Ihre Teams interviewen und eine Fotografin aufbieten muss, finanzieren
  Sie drei Berufe, nicht einen.</li>
  <li><strong>Die Funktionen.</strong> Onlinezahlung, Kundenbereich,
  Reservation, Abgleich mit Ihrer Verwaltungssoftware: jede davon ist ein
  kleines Projekt.</li>
  <li><strong>Die Mehrsprachigkeit.</strong> Jede Sprache bringt
  Übersetzung, Korrektorat und einen Unterhalt, der sich
  vervielfacht.</li>
  <li><strong>Das CMS.</strong> Eine Website für Sie selbst bearbeitbar zu
  machen, verdoppelt oft die Umsetzungszeit. Nützlich, wenn Sie jede Woche
  publizieren, nutzlos, wenn Sie einmal im Jahr eine Telefonnummer
  ändern.</li>
</ul>

<h2>Die jährlichen Kosten, die niemand beziffert</h2>

<p>Die Offerte für die Erstellung ist die halbe Geschichte. Was in der
Schweiz jedes Jahr wiederkehrt, zu den gängigen Preisen von 2026:</p>

<ul>
  <li><strong>Domainname auf <code>.ch</code></strong> — rund zehn Franken
  pro Jahr. Ein <code>.com</code> etwa fünfzehn.</li>
  <li><strong>Hosting</strong> — von CHF&nbsp;0 für eine statische Website
  auf einer Plattform wie Netlify oder Cloudflare Pages bis CHF&nbsp;200–400
  pro Jahr bei einem Schweizer Shared Hosting, mehr für einen eigenen
  Server.</li>
  <li><strong>Geschäftliche E-Mail-Adressen</strong> — von CHF&nbsp;60 bis
  150 pro Jahr und Postfach, je nach Anbieter. Das ist oft die
  Überraschung.</li>
  <li><strong>HTTPS-Zertifikat</strong> — heute gratis (Let's Encrypt) und
  bei den meisten Hostern automatisch. Wenn es Ihnen verrechnet wird,
  fragen Sie nach dem Grund.</li>
  <li><strong>Unterhalt</strong> — von CHF&nbsp;0 für eine statische
  Website bis CHF&nbsp;600–1 800 pro Jahr für ein WordPress, das aktualisiert
  werden muss, und das auch wirklich aktualisiert werden muss: Das ist die
  häufigste Ursache für gehackte KMU-Websites.</li>
</ul>

<p>Anders gesagt: Eine Website für CHF&nbsp;2 000, die CHF&nbsp;1 200 Unterhalt
pro Jahr kostet, ist auf fünf Jahre teurer als eine Website für
CHF&nbsp;5 000, die nur ihre Domain kostet.</p>

<h2>Was ein Festpreis ändert</h2>

<p>Ein Festpreis verschiebt das Risiko. Dauert das Projekt länger als
vorgesehen, ist das das Problem des Anbieters, nicht Ihres. Im Gegenzug
wird der Umfang vor dem Start schriftlich festgehalten: Anzahl Seiten,
Anzahl Sprachen, was enthalten ist und was Gegenstand einer separaten
Offerte wird.</p>

<p>Dieser Rahmen erlaubt uns eine <a
href="../index.html#tarifs">öffentliche Preisliste</a> und eine Lieferung
<strong>ab zwei Werktagen</strong> ab vollständigem Briefing, mit
<strong>dreissig Tagen unbegrenzten Korrekturen</strong> und
<strong>voller Rückerstattung</strong>, wenn Ihnen das Ergebnis nicht
zusagt. Unsere <a href="../legal/conditions.html">Allgemeinen
Geschäftsbedingungen</a> sagen es schwarz auf weiss, und das ist der
einzige Ort, an dem ein Verkaufsversprechen etwas wert ist.</p>

<h2>Womit man konkret rechnen muss</h2>

<ul>
  <li><strong>Handwerk oder selbstständig, eine Seite, die vorstellt und
  Anrufe bringt</strong> — CHF&nbsp;300 bis 800 Erstellung, weniger als
  CHF&nbsp;50 pro Jahr.</li>
  <li><strong>Dienstleistungs-KMU, vier bis sechs Seiten, eine
  Sprache</strong> — CHF&nbsp;500 bis 2 500 Erstellung.</li>
  <li><strong>KMU, das auf Deutsch und Französisch bestehen
  muss</strong> — CHF&nbsp;700 bis 4 000, wobei die Übersetzung mehr wiegt
  als das Design.</li>
  <li><strong>Handel mit Onlineverkauf</strong> — CHF&nbsp;3 000 bis 15 000,
  plus ein echtes Zeitbudget für den Katalog.</li>
</ul>

<p>Wenn Sie zwischen zwei Spannen schwanken, ist die nützliche Frage nicht
«welches Budget habe ich?», sondern «was ist mir ein Kunde wert?». Eine
Praxis, bei der ein Kunde CHF&nbsp;3 000 wert ist, amortisiert eine Website
für CHF&nbsp;5 000 mit zwei Kunden. Ein Geschäft mit einem
durchschnittlichen Warenkorb von CHF&nbsp;40 muss anders rechnen.</p>

<h2>Drei Fragen, die uns gestellt werden</h2>

<h3>Ist eine Website für CHF 290 möglich oder ein Lockvogel?</h3>
<p>Möglich unter drei Bedingungen: eine Seite und nicht acht, eine bereits
erprobte Struktur statt eines weissen Blatts, und ein Briefing, das Sie
selbst ausfüllen. Nehmen Sie eine dieser drei Bedingungen weg, und der
Preis verdoppelt sich. Unsere <a href="../offres/pro-landing-page.html">Landing Pro</a>
sagt genau, was sie enthält und was nicht.</p>

<h3>Warum unterscheiden sich zwei Offerten für dieselbe Website um das Dreifache?</h3>
<p>Weil sie nicht dieselbe Arbeit beschreiben. Vergleichen Sie die Anzahl
Seiten, die Anzahl enthaltener Korrekturrunden, wer die Texte schreibt,
wer die Fotos liefert, und was passiert, wenn Sie es sich anders
überlegen. In neun von zehn Fällen liegt der Unterschied dort und nicht
beim Talent.</p>

<h3>Muss man ein monatliches Abo bezahlen?</h3>
<p>Nur wenn Sie jeden Monat etwas dafür erhalten — Änderungen, eine
Überwachung, einen Bericht. Ein Abo, das nur das Hosting einer statischen
Website finanziert, lässt sich durch rund zehn Franken Domaingebühr pro
Jahr ersetzen.</p>
""",
  "faq": [
    ("Was kostet eine Website für ein KMU in der Schweiz?",
     "Zwischen CHF 300 und CHF 30 000, je nach Umfang. Ein Pauschalangebot "
     "für eine Firmenwebsite mit einer bis sieben Seiten liegt zwischen "
     "CHF 300 und CHF 1 500; ein massgeschneidertes Projekt mit Funktionen "
     "beginnt bei rund CHF 3 000."),
    ("Welche jährlichen Kosten hat eine Website?",
     "Der Domainname (rund CHF 10 pro Jahr bei .ch), das Hosting (von gratis "
     "für eine statische Website bis CHF 400 pro Jahr), die geschäftlichen "
     "E-Mail-Adressen (CHF 60 bis 150 pro Postfach und Jahr) und der "
     "Unterhalt, wenn die Website auf einem CMS läuft."),
    ("Ist ein Festpreis günstiger als eine Offerte nach Stundenaufwand?",
     "Nicht zwingend, aber er ist planbar: Der Umfang wird vor dem Start "
     "schriftlich festgehalten, und ein Mehraufwand geht zulasten des "
     "Anbieters."),
  ],
 },
 {
  "slug": "landing-page-ou-site-complet.html",
  "cat": "Entscheiden",
  "titre": "Landing Page oder mehrseitige Website: wie man wählt",
  "h1": ["Landing Page oder", "mehrseitige Website?"],
  "desc": "Die Frage ist nicht die Anzahl Seiten, sondern die Anzahl "
          "Entscheidungen, die Ihre Besucher treffen müssen. Ein Test mit "
          "drei Fragen.",
  "dek": "Eine einzelne Seite ist keine Sparversion einer Website. Sie ist "
         "ein anderes Werkzeug, das in gewissen Fällen gewinnt und in "
         "anderen verliert.",
  "lecture": "5 Min.",
  "corps": """
<p>Man fragt uns fast immer «wie viele Seiten brauche ich?». Das ist die
falsche Frage: Sie zielt auf die Menge, obwohl das Problem eines der
Nutzerführung ist. Die richtige Frage lautet: <strong>wie viele
verschiedene Entscheidungen müssen Ihre Besucher treffen</strong>, bevor
sie Sie kontaktieren.</p>

<p>Eine Entscheidung, eine Seite. Mehrere Entscheidungen, mehrere
Seiten.</p>

<h2>Wann eine einzige Seite genügt</h2>

<p>Eine einzelne Seite funktioniert, wenn alle Ihre Besucher dasselbe
wollen und es am Ende nur eine Handlung gibt: anrufen, reservieren, eine
Offerte anfordern.</p>

<ul>
  <li>Ein Handwerksbetrieb, der für Aufträge angerufen werden will.</li>
  <li>Ein Restaurant: die Karte, die Öffnungszeiten, die Adresse, die Reservation.</li>
  <li>Eine Praxis oder eine Therapeutin mit einer einzigen Hauptleistung.</li>
  <li>Ein einzelnes Angebot für eine Kampagne, mit einem Formular am Ende.</li>
</ul>

<p>Ihr Vorteil ist nicht der Preis, sondern die Abwesenheit von Auswahl.
Auf einer gut gebauten Seite scrollt der Besucher hinunter und landet beim
Formular. Auf einer Website mit acht Seiten irrt er durchs Menü und geht.
Auch deshalb geht eine einzelne Seite <a
href="../index.html#process">in zwei Werktagen</a> online: Es gibt weniger
zu entscheiden, also weniger abzuwägen.</p>

<h2>Wann es mehrere braucht</h2>

<p>Mehrere Seiten werden nötig, sobald eines dieser drei Dinge zutrifft.</p>

<p><strong>Sie haben mehrere Leistungen, die nicht dieselben Menschen
ansprechen.</strong> Ein Treuhandbüro mit Buchhaltung, Steuern und
Lohnwesen hat drei Zielgruppen. Eine einzige Seite vermischt sie und
überzeugt keine davon. Drei Seiten, jede mit ihrem Vokabular, sind
zugleich drei Eingangstüren für Google: der rentabelste Grund, Seiten
hinzuzufügen.</p>

<p><strong>Sie müssen bei verschiedenen Suchanfragen gefunden
werden.</strong> Google bewertet Seiten, nicht Websites. «Spengler
Lausanne» und «Dachreparatur Lausanne» verdienen zwei Seiten, sonst
positionieren Sie sich bei beiden nur halb.</p>

<p><strong>Vertrauen braucht Platz.</strong> Je höher der Betrag, desto
mehr will der Besucher Referenzen, Bewertungen, eine Seite «über uns»,
manchmal Bedingungen. Ein Kauf für CHF&nbsp;15 000 wird nicht auf einer
Seite entschieden, die man durchscrollt.</p>

<h2>Der Test mit den drei Fragen</h2>

<ol>
  <li><strong>Wie viele verschiedene Leistungen wollen Sie verkaufen?</strong>
  Eine: eine Seite. Zwei bis fünf: eine Seite pro Leistung.</li>
  <li><strong>Wie viele verschiedene Google-Suchanfragen wollen Sie
  gewinnen?</strong> Rechnen Sie mit einer Seite pro wichtiger Suche.</li>
  <li><strong>Muss Ihr Besucher etwas überprüfen, bevor er Ihnen
  schreibt?</strong> Wenn ja, sehen Sie die Seite vor, die ihm das
  erlaubt — Referenzen, Bewertungen, Team.</li>
</ol>

<p>Zählen Sie zusammen. Eine Seite, wenn das Total eins ist, fünf Seiten,
wenn es bei vier oder fünf liegt, sieben, wenn Sie einen echten
Leistungskatalog haben. Genau das ist die Logik unserer drei Stufen:
<a href="../offres/pro-landing-page.html">Landing Pro</a> für eine Seite,
<a href="../offres/ultimate-website.html">Site Complet</a> bis fünf,
<a href="../offres/advanced-website.html">Site Étendu</a> bis sieben und in
drei Sprachen.</p>

<h2>Der häufigste Fehler</h2>

<p>Acht Seiten bestellen und nur drei füllen. Eine halbleere Website weckt
weniger Vertrauen als eine dichte, fertige Seite, und sie kostet mehr in
der Produktion wie im Unterhalt. Wenn Sie den Inhalt heute nicht haben,
nehmen Sie heute weniger Seiten.</p>

<p>Den umgekehrten Fehler gibt es auch: fünf Leistungen auf eine einzige
Seite stapeln, weil sie weniger kostete. Der Besucher liest den sechsten
Abschnitt nicht, und Google weiss nicht, wofür es Sie einordnen soll.</p>

<h2>Und wenn ich mich irre?</h2>

<p>Das ist nicht schlimm, unter zwei Bedingungen. Erstens: dass die
Website so gebaut ist, dass man ihr eine Seite hinzufügen kann, ohne sie
neu zu machen. Zweitens: dass <a href="../legal/conditions.html">Ihr
Domainname auf Ihren Namen lautet</a> — er trägt Ihre Auffindbarkeit, nicht
die Website.</p>

<p>In der Praxis beginnen die meisten unserer Kunden mit einer Seite,
schauen drei Monate lang, woher ihre Anrufe kommen, und fügen dann die
zwei oder drei Seiten hinzu, die die Anrufe benannt haben. Das ist weniger
elegant als ein perfekter Plan, und deutlich wirksamer.</p>

<p>Wenn Sie noch zögern, <a href="../devis.html">schreiben Sie uns die drei
Antworten des Tests</a>: Wir sagen Ihnen, welche der drei Stufen zu Ihnen
passt, auch dann, wenn die Antwort die günstigste ist.</p>
""",
  "faq": [
    ("Genügt eine Landing Page, um auf Google sichtbar zu sein?",
     "Ja für eine Hauptsuchanfrage, nein für mehrere. Google bewertet "
     "Seiten: Eine einzelne Seite positioniert sich gut zu einem Thema, kann "
     "aber nicht «Branche + Ort» und drei verschiedene Leistungen "
     "abdecken."),
    ("Kann man später Seiten hinzufügen?",
     "Ja, wenn die Website dafür gebaut wurde. Das ist der häufigste Weg: "
     "mit einer Seite beginnen, drei Monate lang beobachten, woher die "
     "Anrufe kommen, und dann die nützlichen Seiten ergänzen."),
  ],
 },

 {
  "slug": "fiche-google-business.html",
  "cat": "Sichtbarkeit",
  "titre": "Google-Business-Profil: die Einstellung, die fast alle KMU verpassen",
  "h1": ["Google-Business-Profil:", "die verpasste Einstellung."],
  "desc": "Die Hauptkategorie entscheidet über die Hälfte Ihrer lokalen "
          "Sichtbarkeit. Und fast niemand wählt sie richtig.",
  "dek": "Für ein lokales KMU wiegt das Google-Profil oft schwerer als die "
         "Website selbst. Ein einziges Feld entscheidet dort über das "
         "Wesentliche.",
  "lecture": "6 Min.",
  "corps": """
<p>Wenn Sie Kunden im Umkreis von dreissig Kilometern bedienen, bringt
Ihnen Ihr Google-Business-Profil vermutlich mehr Anrufe als Ihre Website.
Es erscheint im Kartenblock, zuoberst, vor den klassischen Resultaten —
und es ist gratis.</p>

<p>In diesem Profil gibt es ein Feld, das schwerer wiegt als alle anderen
und das die Mehrheit der Schweizer KMU falsch ausfüllt: die
<strong>Hauptkategorie</strong>.</p>

<h2>Die verpasste Einstellung</h2>

<p>Google verlangt eine Hauptkategorie und erlaubt Nebenkategorien. Fast
alle wählen die Hauptkategorie auf die naheliegendste Art — jene, die den
Beruf im weiten Sinn beschreibt — und genau das ist der Fehler.</p>

<p>Die Hauptkategorie bestimmt, <em>für welche Suchanfragen</em> Google Sie
überhaupt in Betracht zieht. Die Nebenkategorien haben nur marginales
Gewicht. Also:</p>

<ul>
  <li>Wenn Sie Schreiner sind, aber 80&nbsp;% Ihres Umsatzes aus
  massgefertigten Küchen kommt, muss die Hauptkategorie jene der Küchen
  sein, nicht «Schreiner».</li>
  <li>Wenn Sie Physiotherapeut mit Spezialisierung auf Sport sind, kommt
  die Sportkategorie an die erste Stelle.</li>
  <li>Wenn Sie Treuhänder sind, aber vor allem Steuererklärungen für
  Privatpersonen verkaufen, wählen Sie die Steuerkategorie.</li>
</ul>

<p>Die richtige Methode ist mechanisch: Tippen Sie bei Google die Suche
ein, die Sie gewinnen wollen, schauen Sie die drei Profile an, die im
Kartenblock erscheinen, öffnen Sie sie, lesen Sie deren Hauptkategorie.
Nehmen Sie dieselbe. Sie müssen nicht raten, was Google womit verbindet:
Es zeigt es Ihnen.</p>

<h2>Die Felder, die das Ranking wirklich bewegen</h2>

<p>Das lokale Ranking beruht auf drei Säulen — Relevanz, Distanz und
Bekanntheit. Auf die Distanz haben Sie keinen Einfluss. Bleiben die
folgenden Felder, nach beobachteter Wirkung geordnet:</p>

<ol>
  <li><strong>Die Hauptkategorie</strong>, wie eben gesehen.</li>
  <li><strong>Der genaue Name des Betriebs.</strong> Tragen Sie den
  echten Namen ein, so wie er an Ihrem Schaufenster und auf Ihren
  Rechnungen steht. Stichwörter hinzuzufügen («Dupont Sanitär Genf
  24h-Notdienst») verstösst gegen die Regeln von Google und riskiert eine
  Sperrung.</li>
  <li><strong>Die Leistungen.</strong> Ein unterschätztes Feld: Man kann
  seine Leistungen einzeln auflisten, mit Beschreibung. Jeder Eintrag ist
  ein weiteres Stichwort, dieses hier legitim.</li>
  <li><strong>Das Einzugsgebiet.</strong> Wenn Sie hinfahren, deklarieren
  Sie die Gemeinden. Wenn Sie Kundschaft empfangen, geben Sie eine
  Adresse an und deklarieren Sie kein Gebiet.</li>
  <li><strong>Die Öffnungszeiten, inklusive Feiertage.</strong> Google
  zeigt «Öffnungszeiten können abweichen», wenn sie nicht bestätigt sind,
  und dieser Zweifel kostet Anrufe.</li>
  <li><strong>Der Link zur Website.</strong> Richten Sie ihn auf die Seite,
  die von der betreffenden Leistung handelt, nicht automatisch auf die
  Startseite.</li>
</ol>

<h2>Die Fotos: die Dreierregel</h2>

<p>Profile, die konvertieren, haben mindestens: das Äussere mit sichtbarer
Beschriftung (die Kundschaft muss den Ort beim Ankommen erkennen), das
Innere, und die fertige Arbeit. Fügen Sie jeden Monat ein paar hinzu statt
dreissig auf einmal: Ein lebendiges Profil wird besser behandelt als ein
eingefrorenes.</p>

<p>Vermeiden Sie Stockfotos. Man erkennt sie, und sie nehmen genau das
weg, was das Profil bringen soll: den Beweis, dass es Sie an diesem Ort
wirklich gibt.</p>

<h2>Bewertungen, ohne zu betteln</h2>

<p>Die Anzahl der Bewertungen und ihre Regelmässigkeit zählen mehr als die
Durchschnittsnote. Ein Profil mit 4,6 und einer Bewertung pro Monat zieht
an einem Profil mit 5,0 vorbei, das seit zwei Jahren stillsteht.</p>

<p>Was funktioniert, der Reihe nach: im richtigen Moment fragen (direkt
nach Abschluss der Arbeit, nie über eine Sammelmail), den kurzen
Bewertungslink weitergeben, den Google in Ihrem Dashboard erzeugt, und
<strong>auf alle Bewertungen antworten</strong>, auch auf die schlechten,
in zwei Zeilen und ohne sich zu rechtfertigen. Die Antworten werden von
Interessenten weit mehr gelesen als von den Verfassern.</p>

<p>Was nicht funktioniert: Bewertungen kaufen (wird erkannt und mit der
Löschung des Profils geahndet), sie gegen einen Rabatt verlangen
(verboten), oder ein Tablet auf den Tresen stellen, das zehn Bewertungen
von derselben IP-Adresse sammelt.</p>

<h2>Was ein Profil abstürzen lässt</h2>

<ul>
  <li>Eine Adresse oder Nummer, die von jener der Website abweicht. Sorgen
  Sie dafür, dass Name, Adresse und Telefon überall exakt gleich sind:
  Profil, Website, Verzeichnisse, soziale Netzwerke.</li>
  <li>Stichwörter, die in den Betriebsnamen gestopft werden.</li>
  <li>Eine Wohnadresse, die als Ladenlokal deklariert wird, obwohl Sie
  niemanden empfangen.</li>
  <li>Zwei Profile für denselben Betrieb — das kommt nach einer Änderung
  der Firmenbezeichnung vor und halbiert Ihre Bekanntheit.</li>
  <li>Schweigen. Ein Profil, das man nie anfasst, verliert gegen ein
  gepflegtes Profil an Boden.</li>
</ul>

<h2>Und was ist mit der Website?</h2>

<p>Das Profil bringt den Anruf; die Website macht den Verkauf.
Interessenten, die zögern, öffnen Ihre Website aus dem Profil heraus:
Wenn es sie nicht gibt oder sie veraltet ist, verlieren Sie einen Teil
dessen, was das Profil Ihnen gebracht hat. Beide arbeiten zusammen, und am
rentabelsten ist es, die Hauptleistung des Profils mit einer eigenen Seite
der Website in Übereinstimmung zu bringen.</p>

<p>Genau das behandelt <a href="../index.html#methode">Die Methode Lokale
Kundschaft</a>, der Leitfaden, den wir zum
<a href="../offres/ultimate-website.html">Site Complet</a> abgeben: das
Google-Profil, die Suchanfragen «Branche + Ort», und wie man von ChatGPT
zitiert wird, wenn jemand in der Nähe nach Ihrer Branche sucht.</p>
""",
  "faq": [
    ("Welche Hauptkategorie soll man im Google-Business-Profil wählen?",
     "Jene Ihrer rentabelsten Leistung, nicht jene Ihres Berufs im weiten "
     "Sinn. Methode: Tippen Sie die Suche ein, die Sie gewinnen wollen, "
     "öffnen Sie die Profile im Kartenblock und übernehmen Sie deren "
     "Hauptkategorie."),
    ("Darf man dem Betriebsnamen Stichwörter hinzufügen?",
     "Nein. Die Regeln von Google verlangen den echten Namen des Betriebs; "
     "Stichwörter hinzuzufügen riskiert die Sperrung des Profils."),
    ("Zählt die Durchschnittsnote mehr als die Anzahl Bewertungen?",
     "Nein. Die Regelmässigkeit der Bewertungen und die gegebenen Antworten "
     "wiegen schwerer als eine perfekte Note von vor zwei Jahren."),
  ],
 },
 {
  "slug": "que-mettre-sur-sa-page-d-accueil.html",
  "cat": "Redaktion",
  "titre": "Was auf die Startseite gehört",
  "h1": ["Was Sie auf Ihre", "Startseite schreiben."],
  "desc": "Fünf Sekunden, um drei Fragen zu beantworten. Der Aufbau einer "
          "Startseite, die das Telefon klingeln lässt, Abschnitt für "
          "Abschnitt.",
  "dek": "Ihre Besucher geben Ihrer Startseite die Zeit einer Rotphase. "
         "Hier ist die Reihenfolge, in der sie ihre Antworten wollen.",
  "lecture": "6 Min.",
  "corps": """
<p>Wer auf Ihrer Startseite landet, stellt sich drei Fragen, in dieser
Reihenfolge: <strong>wo bin ich, ist das für mich, und was mache ich
jetzt?</strong> Für alle drei gibt er Ihnen ein paar Sekunden. Alles, was
diesen Antworten nicht dient, kann nach unten oder weg.</p>

<p>Hier ist, was wir schreiben, in der Reihenfolge, in der wir es
schreiben.</p>

<h2>1. Der Satz zuoberst</h2>

<p>Er sagt, was Sie tun, für wen, und wo. Nichts anderes. Er muss nicht
schön sein, er muss stimmen.</p>

<ul>
  <li>✗ «Exzellenz im Dienst Ihrer Projekte»</li>
  <li>✓ «Elektriker in Nyon, Notdienst am selben Tag»</li>
  <li>✗ «Denken wir Ihre Kommunikation gemeinsam neu»</li>
  <li>✓ «Logos und visuelle Identitäten für Schweizer KMU, in zwei
  Wochen»</li>
</ul>

<p>Einfacher Test: Zeigen Sie den Satz jemandem, der Ihren Beruf nicht
kennt. Kann er nicht wiederholen, was Sie verkaufen, muss er neu
geschrieben werden. Und wenn Ihr Beruf lokal ist, schreiben Sie den Ort
hinein: Das ist keine Suchmaschinenoptimierung, das ist Höflichkeit
gegenüber dem Besucher.</p>

<h2>2. Der Button, sofort</h2>

<p>Die erste Handlungsaufforderung gehört in den ersten Bildschirm, neben
den Satz zuoberst. Manche Besucher sind bereits entschieden: Lassen Sie
sie nicht scrollen.</p>

<p>Eine Beschriftung, die sagt, was passieren wird, konvertiert besser als
eine vage. «Offerte anfordern» statt «Mehr erfahren». «Tisch reservieren»
statt «Kontakt». Und nur ein Hauptbutton: Zwei Buttons mit gleichem
Gewicht sind eine Entscheidung mehr.</p>

<h2>3. Die drei Gründe zu bleiben</h2>

<p>Direkt unter dem ersten Bildschirm drei kurze Argumente. Nicht zehn.
Sie beantworten «ist das für mich?» und müssen
<strong>überprüfbar</strong> sein: eine Frist, ein Preis, ein Gebiet, eine
Garantie, eine Zahl, die Sie belegen können.</p>

<p>«Qualität, Seriosität, Reaktionsschnelligkeit» sagt nichts, weil
niemand das Gegenteil schreiben würde. «Offerte innert 24 Stunden,
Festpreis, Einsatz im Kanton Waadt» sagt etwas.</p>

<h2>4. Der Beweis</h2>

<p>Das ist der am meisten vernachlässigte und der rentabelste Abschnitt.
Nach Wirkung geordnet: Fotos Ihrer echten Arbeit, namentliche
Bewertungen, Kundenlogos, Zahlen.</p>

<p>Eine Regel, die wir auf uns selbst anwenden: <strong>wenn Sie es nicht
haben, erfinden Sie es nicht</strong>. Eine gefälschte Bewertung fällt
auf, und an dem Tag, an dem sie auffällt, reisst sie alles andere mit.
Wenn Sie starten und noch nichts zu zeigen haben, sagen Sie es und
ersetzen Sie den Beweis durch Transparenz: Ihre Preise, Ihre Methode, Ihre
Bedingungen. Das wirkt besser, als man denkt.</p>

<h2>5. Die Einwände, bevor sie blockieren</h2>

<p>Ihr Besucher hat zwei oder drei Gründe, Ihnen nicht zu schreiben. «Das
ist sicher zu teuer.» «Das dauert Monate.» «Ich sitze dann fest.»
Behandeln Sie sie ausdrücklich, auf der Seite: einen Preis oder eine
Spanne, eine Frist, und was passiert, wenn es nicht passt.</p>

<p>Es ist widersinnig, einen Preis zu schreiben, wenn man glaubt, der
Preis vertreibe die Leute. In der Praxis vertreibt das Fehlen eines
Preises mehr: Es lässt den Besucher das Schlimmste vermuten und zu dem
gehen, der ihn anzeigt. Deshalb sind <a href="../index.html#tarifs">unsere
drei Preise öffentlich</a>.</p>

<h2>6. Die Erinnerung an die Handlung</h2>

<p>Wiederholen Sie die Handlungsaufforderung unten, und bieten Sie zwei
Formen an: ein Formular für jene, die schreiben, eine Nummer oder ein
WhatsApp für jene, die lieber sprechen. Ergänzen Sie, was Sie mit der
Anfrage tun: «wir antworten am selben Tag, von Montag bis Freitag». Der
Besucher will wissen, worauf er sich einlässt.</p>

<h2>Was weg muss</h2>

<ul>
  <li><strong>Das Wort «Willkommen».</strong> Es belegt die meistgelesene
  Zeile der Seite, um nichts zu sagen.</li>
  <li><strong>Die Firmengeschichte, zuoberst.</strong> Sie interessiert,
  aber später. Ihr Platz ist eine Seite «über uns».</li>
  <li><strong>Das Karussell, das von allein weiterläuft.</strong> Niemand
  sieht das dritte Bild, und es bremst die Seite.</li>
  <li><strong>Stockfotos.</strong> Ein mit dem Handy aufgenommenes Foto
  Ihrer Werkstatt ist mehr wert als eine amerikanische Bürokulisse.</li>
  <li><strong>Lange Absätze.</strong> Zwei oder drei Sätze, nie mehr, und
  Zwischentitel, die sich allein lesen lassen.</li>
</ul>

<h2>Der letzte Test</h2>

<p>Lassen Sie Ihre Startseite von einer aussenstehenden Person fünf
Sekunden lang auf einem Handy lesen, mit der Uhr in der Hand. Fragen Sie
danach, was Sie verkaufen, an wen, und was sie tun würde, um Sie zu
kontaktieren. Kommen alle drei Antworten, ist die Seite gut. Sonst ist
nicht das Design zu ändern, sondern die Reihenfolge der Abschnitte.</p>

<p>Diese Fragen stellen wir in unserem <a href="../brief.html">Briefing zu
Beginn</a>: Es ist der Teil, der die Kundschaft am meisten Zeit kostet, und
jener, der den ganzen Unterschied im Ergebnis ausmacht.</p>
""",
  "faq": [
    ("Soll man seine Preise auf der Website anzeigen?",
     "In der grossen Mehrheit der Fälle ja — zumindest eine Spanne. Das "
     "Fehlen eines Preises schickt den Besucher zu einer Konkurrenz, die ihn "
     "anzeigt, und kostet Zeit durch Anfragen ausserhalb des Budgets."),
    ("Was gehört als Erstes auf eine Startseite?",
     "Ein Satz, der sagt, was Sie tun, für wen und wo. Wenn eine Person "
     "ausserhalb Ihrer Branche ihn nicht wiederholen kann, muss er neu "
     "geschrieben werden."),
  ],
 },

 {
  "slug": "wix-squarespace-ou-sur-mesure.html",
  "cat": "Vergleich",
  "titre": "Wix, Squarespace oder massgeschneidert: der ehrliche Vergleich",
  "h1": ["Wix, Squarespace", "oder massgeschneidert?"],
  "desc": "Was jede Lösung sehr gut kann, wo jede hakt, und die realen "
          "Kosten über drei Jahre für ein Schweizer KMU.",
  "dek": "Wir sind Partei: Wir verkaufen Massarbeit. Umso mehr Grund, genau "
         "zu sagen, in welchen Fällen Baukästen die richtige Wahl sind.",
  "lecture": "7 Min.",
  "corps": """
<p>Sagen wir es gleich: Wir verkaufen von Hand gebaute Websites. Ein
Vergleich aus unserer Feder ist also nicht neutral. Wir versuchen trotzdem,
korrekt zu sein, denn es gibt echte Fälle, in denen ein Baukasten die
bessere Entscheidung ist und Sie Ihr Geld bei uns verlieren würden.</p>

<h2>Was Wix sehr gut kann</h2>

<ul>
  <li><strong>Heute starten, ohne jemanden.</strong> Sie können am
  Nachmittag eine Website online haben, allein, ohne Vorkenntnisse.</li>
  <li><strong>Alles am selben Ort.</strong> Domain, Hosting, Zertifikat,
  Formulare, Shop, Reservation, Newsletter: eine Rechnung, ein
  Passwort.</li>
  <li><strong>Selber ändern, wirklich.</strong> Der Editor ist sehr
  grosszügig: Man verschiebt ein Element, wohin man will.</li>
  <li><strong>Die Branchenfunktionen.</strong> Terminbuchung, Kursplan,
  Reservation: in wenigen Klicks verfügbar, während sie neu zu entwickeln
  Tausende von Franken kosten würde.</li>
</ul>

<h2>Was Squarespace sehr gut kann</h2>

<ul>
  <li><strong>Das visuelle Standardergebnis.</strong> Die Vorlagen sind
  sorgfältiger und schwerer kaputtzumachen. Für eine Fotografin, einen
  Architekten, ein Restaurant ist das Ergebnis auch ohne Art Direction
  gut.</li>
  <li><strong>Die Konsistenz.</strong> Das globale Stilsystem verhindert
  die Website, die nach sechs Monaten in zwölf Richtungen läuft.</li>
  <li><strong>Der Verkauf kleiner Kataloge.</strong> Etwa zwanzig Produkte
  oder ein paar Leistungen: sauber und ausreichend.</li>
</ul>

<h2>Wo beide haken</h2>

<p><strong>Die Geschwindigkeit.</strong> Diese Plattformen laden viel
Code, um im Browser bearbeitbar zu bleiben. Auf einem Handy im 4G-Netz
sieht man das. Geschwindigkeit ist ein Rankingkriterium bei Google und vor
allem ein Abbruchkriterium: Der Besucher schliesst, bevor er Ihr Angebot
gesehen hat.</p>

<p><strong>Der Ausstieg.</strong> Das ist der ernsteste und am wenigsten
diskutierte Punkt. Sie können Ihre Website nicht mitnehmen: Man bekommt in
der Regel seine Texte, seine Bilder und seinen Domainnamen zurück, aber
nicht das Layout. Die Plattform wechseln heisst neu machen. Das Abo ist
also nicht nur eine Miete, es ist ein Ausstiegspreis, der mit der Zeit
wächst.</p>

<p><strong>Die feine Suchmaschinenoptimierung.</strong> Das Wesentliche
ist zugänglich (Titel, Beschreibungen, Seitenadressen). Weniger zugänglich
ist: die genaue Kontrolle über das Markup, über fortgeschrittene
strukturierte Daten, über die Verwaltung der Mehrsprachigkeit. Für eine
lokale Website geht das. Für eine ambitionierte Inhaltsstrategie
bremst es.</p>

<p><strong>Die Mehrsprachigkeit.</strong> Möglich, aber oft der
mühsamste Teil — und in der Schweiz ist sie selten optional.</p>

<p><strong>Der Preis, der steigt.</strong> Der Einstiegstarif enthält fast
nie das, was Sie brauchen. Die nützlichen Funktionen (Shop, Reservation,
Entfernen der Werbung, E-Mail-Adressen) liegen auf höheren Stufen, und die
Stufen werden mit den Jahren teurer.</p>

<h2>Was Massarbeit sehr gut kann</h2>

<ul>
  <li><strong>Die Geschwindigkeit.</strong> Eine gut gebaute statische
  Website lädt praktisch sofort und braucht keinerlei technischen
  Unterhalt.</li>
  <li><strong>Ihnen gehören.</strong> Die Dateien sind Ihre, bei dem
  Hoster, den Sie wollen, und anderswohin übertragbar.</li>
  <li><strong>Genau sagen, was Sie sagen wollen.</strong> Keine Vorlage,
  die zu umgehen wäre.</li>
  <li><strong>Die Betriebskosten.</strong> Oft der Preis der Domain, und
  sonst nichts.</li>
</ul>

<p>Und ihre Grenzen, die real sind: Sie sind für grössere Änderungen von
jemandem abhängig, es braucht am Anfang ein Briefing, und die
Branchenfunktionen (Reservation, Kalender, Shop) sind ein separates Budget
statt inbegriffen.</p>

<h2>Die realen Kosten über drei Jahre</h2>

<p>Als Grössenordnung für ein Schweizer KMU, zu den 2026 beobachteten
Preisen — die Tarife der Plattformen ändern sich, prüfen Sie sie:</p>

<ul>
  <li><strong>Baukasten, Abo, das für ein Unternehmen passt</strong> — rund
  CHF&nbsp;20 bis 35 pro Monat, also <strong>CHF&nbsp;720 bis 1 260 über drei
  Jahre</strong>, plus Ihre Herstellungszeit, plus die höheren Stufen, wenn
  Sie Shop oder E-Mails dazunehmen.</li>
  <li><strong>Von Hand gebautes Pauschalangebot</strong> — CHF&nbsp;290 bis
  690 einmalig, plus rund zehn Franken Domain pro Jahr, also
  <strong>CHF&nbsp;320 bis 720 über drei Jahre</strong>.</li>
  <li><strong>Massarbeit einer Agentur</strong> — CHF&nbsp;5 000 und mehr,
  gerechtfertigt, wenn die Website ein Hauptverkaufskanal ist.</li>
</ul>

<p>Über drei Jahre ist der Unterschied zwischen Abo und Pauschale also
gering; über sechs Jahre kehrt er sich deutlich um. Was den Ausschlag
gibt, ist nicht der Preis: Es sind Eigentum und Geschwindigkeit.</p>

<h2>Wie man wählt, in drei Fällen</h2>

<p><strong>Nehmen Sie einen Baukasten</strong>, wenn Sie sofort eine
Reservation oder einen Kalender brauchen, wenn Sie Ihre Website jede Woche
selbst ändern wollen, oder wenn Sie eine Tätigkeit testen, von der Sie
noch nicht wissen, ob sie hält.</p>

<p><strong>Nehmen Sie ein von Hand gebautes Pauschalangebot</strong>, wenn
Ihre Website vor allem überzeugen und das Telefon klingeln lassen soll,
wenn Sie kein Abo wollen, oder wenn Ihre lokale Sichtbarkeit mehr zählt
als die Freiheit, alles zu verschieben.</p>

<p><strong>Nehmen Sie eine Agentur</strong>, wenn Ihre Website der
Hauptverkaufskanal ist und ein gewonnener Prozentpunkt bei der Konversion
Zehntausende von Franken ausmacht.</p>

<h2>Eines sollten Sie in jedem Fall tun</h2>

<p>Kaufen Sie Ihren Domainnamen auf Ihren Namen, auf einem Konto, das
Ihnen gehört, unabhängig von der gewählten Lösung. Das ist das einzige
unersetzliche Element: Eine Website macht man neu, eine Adresse mit zehn
Jahren Geschichte nicht. Wenn Ihre Domain heute auf einen Anbieter lautet,
<a href="recuperer-son-nom-de-domaine.html">hier steht, wie Sie sie
zurückholen</a>.</p>

<p>Und wenn Sie wissen wollen, welcher Fall auf Sie zutrifft, <a
href="../devis.html">beschreiben Sie uns Ihre Situation in drei
Zeilen</a>: Wir sagen es Ihnen, auch dann, wenn die Antwort «nehmen Sie ein
Abo, das genügt Ihnen» lautet.</p>
""",
  "faq": [
    ("Kann man seine Website mitnehmen, wenn man Wix oder Squarespace verlässt?",
     "Man bekommt seine Texte, seine Bilder und seinen Domainnamen zurück, "
     "aber nicht das Layout: Ein Plattformwechsel bedeutet, die Website neu "
     "zu bauen."),
    ("Ist eine massgeschneiderte Website schneller als eine Wix-Website?",
     "In der Regel ja: Eine von Hand gebaute statische Website lädt viel "
     "weniger Code, weil sie nicht in einem Onlineeditor bearbeitbar bleiben "
     "muss."),
    ("Welche Lösung kostet über drei Jahre am wenigsten?",
     "Ein einmaliges Pauschalangebot mit einer einfachen Domain im Unterhalt "
     "bleibt über drei Jahre in der Regel unter dem Total eines "
     "Monatsabos, und der Abstand wächst danach weiter."),
  ],
 },
 {
  "slug": "sept-sections-landing-page.html",
  "cat": "Konversion",
  "titre": "Die 7 Abschnitte einer Landing Page, die konvertiert",
  "h1": ["Die sieben Abschnitte", "einer Seite, die konvertiert."],
  "desc": "Die Reihenfolge, die funktioniert, Abschnitt für Abschnitt, mit "
          "dem, was in jeden gehört, und dem Fehler, den man dort nicht "
          "machen darf.",
  "dek": "Eine Seite, die konvertiert, ist keine Seite, die überredet. Es "
         "ist eine Seite, die die Einwände in der Reihenfolge beantwortet, "
         "in der sie auftreten.",
  "lecture": "6 Min.",
  "corps": """
<p>Eine einzelne Seite, deren einziges Ziel eine Handlung ist — anrufen,
reservieren, ein Formular ausfüllen — folgt fast immer demselben Aufbau.
Nicht aus Faulheit, sondern weil die Einwände eines Besuchers in einer
recht stabilen Reihenfolge kommen.</p>

<p>Hier sind die sieben Abschnitte, der Einwand, den jeder behandelt, und
der Fehler, den wir am häufigsten sehen.</p>

<h2>1. Der Aufhänger</h2>

<p><em>Behandelter Einwand: «bin ich am richtigen Ort?»</em></p>

<p>Was Sie tun, für wen, wo, und ein Button. Ein Satz, ein einzeiliger
Untertitel, eine Handlungsaufforderung. Das ist alles, was in den ersten
Bildschirm eines Handys gehört.</p>

<p><strong>Der Fehler:</strong> ein Stimmungssatz («Bringen wir Ihre Ideen
zum Leben»), der den Besucher zum Scrollen zwingt, um Ihren Beruf zu
verstehen. Er scrollt nicht: Er geht.</p>

<h2>2. Die drei Stützpunkte</h2>

<p><em>Behandelter Einwand: «warum Sie?»</em></p>

<p>Drei überprüfbare, kurze, ausgerichtete Argumente. Eine Frist, ein
Preis, ein Gebiet, eine Garantie. Drei, weil zwei mager wirkt und fünf
nicht mehr gelesen wird.</p>

<p><strong>Der Fehler:</strong> Eigenschaften, die niemand umgekehrt für
sich beanspruchen würde. «Seriös, hochwertig, zuhörend» ist kein Argument,
das ist ein Minimum.</p>

<h2>3. Der Beweis</h2>

<p><em>Behandelter Einwand: «funktioniert das wirklich?»</em></p>

<p>Fotos echter Arbeiten, unterzeichnete Bewertungen, Logos, Zahlen.
Platzieren Sie ihn früh — direkt nach den Stützpunkten — denn er ist es,
der dem Besucher erlaubt, weiterzulesen.</p>

<p><strong>Der Fehler:</strong> erfinden. Eine fabrizierte Bewertung fällt
an ihrem Vokabular auf, und sie zerstört die Glaubwürdigkeit der ganzen
Seite. Wenn Sie starten, ersetzen Sie den Beweis durch Transparenz:
Methode, Preise, Bedingungen. Genau das machen wir auf dieser Website:
Unsere <a href="../temoignages.html">Kundenstimmen</a> sind jene, die wir
haben, und keine einzige mehr.</p>

<h2>4. Das Wie</h2>

<p><em>Behandelter Einwand: «worauf lasse ich mich ein?»</em></p>

<p>Drei oder vier numerierte Schritte: was Sie tun, was die Kundschaft
tut, wie lange es dauert. Dieser Abschnitt beruhigt enorm bei praktisch
null Schreibaufwand, und er wird am häufigsten vergessen.</p>

<p><strong>Der Fehler:</strong> Ihren internen Ablauf beschreiben. Der
Besucher will wissen, was ihm passieren wird, nicht wie Sie Ihre Dossiers
organisieren.</p>

<h2>5. Der Preis</h2>

<p><em>Behandelter Einwand: «liegt das in meinem Budget?»</em></p>

<p>Ein Preis, eine Spanne, oder zumindest ein Anhaltspunkt («ab», «die
meisten unserer Aufträge liegen zwischen X und Y»). Sagen Sie auch, was
inbegriffen ist und was nicht.</p>

<p><strong>Der Fehler:</strong> «Offerte auf Anfrage». Der Besucher fragt
nicht: Er nimmt an, dass es teuer ist, und schaut anderswo. Und Sie
erhalten Anfragen ausserhalb des Budgets, die Sie Zeit kosten. Unsere
<a href="../index.html#tarifs">drei Preise</a> sind allein aus diesem Grund
öffentlich.</p>

<h2>6. Die verbleibenden Einwände</h2>

<p><em>Behandelter Einwand: «ja, aber wenn…»</em></p>

<p>Eine kleine FAQ mit vier bis sechs Fragen, die aufgreift, was man Sie
am Telefon wirklich fragt. Schreiben Sie die echten Fragen, auch die
unangenehmen: «und wenn ich nicht zufrieden bin?», «wem gehört die
Website?», «was passiert, wenn Sie verschwinden?».</p>

<p><strong>Der Fehler:</strong> eine Gefälligkeits-FAQ, die Fragen stellt,
deren Antwort Ihnen passt. Sie behandelt keine Hemmschwelle und belegt
Platz.</p>

<h2>7. Die letzte Handlung</h2>

<p><em>Behandelter Einwand: «was mache ich jetzt?»</em></p>

<p>Dieselbe Handlungsaufforderung wie oben, mit zwei Kanälen: ein kurzes
Formular und eine Möglichkeit, mit jemandem zu sprechen. Nennen Sie die
Antwortfrist. Und halten Sie das Formular kurz: Jedes zusätzliche Feld
kostet Einsendungen. Name, Kontaktmöglichkeit, zwei Zeilen Nachricht
genügen fast immer.</p>

<p><strong>Der Fehler:</strong> ein Formular mit zwölf Feldern, das nach
Umsatz und Mitarbeiterzahl fragt, noch vor dem ersten Austausch.</p>

<h2>Was mehr zählt als die Reihenfolge</h2>

<ul>
  <li><strong>Die Geschwindigkeit.</strong> Eine langsame Seite verliert
  Besucher noch vor Abschnitt 2. Das ist das Erste, was zu korrigieren
  ist, vor jedem Umschreiben.</li>
  <li><strong>Das Handy zuerst.</strong> Die Mehrheit Ihrer Besucher ist
  mobil unterwegs. Entwerfen Sie für den Handybildschirm und prüfen Sie
  danach am Computer.</li>
  <li><strong>Eine einzige Handlung.</strong> Eine Seite, die anrufen,
  schreiben, abonnieren, herunterladen und auf Instagram folgen anbietet,
  bringt gar nichts zustande.</li>
</ul>

<p>Diesen Aufbau wenden wir auf der
<a href="../offres/pro-landing-page.html">Landing Pro</a> an: mindestens
fünf Abschnitte, sieben wenn der Inhalt es rechtfertigt, und nie zwei
Hauptbuttons, die sich um dieselbe Seite streiten.</p>
""",
  "faq": [
    ("Wie viele Abschnitte braucht eine Landing Page?",
     "Fünf mindestens, sieben wenn der Inhalt es rechtfertigt. Entscheidend "
     "ist, dass jeder Abschnitt einen echten Einwand behandelt, in der "
     "Reihenfolge, in der er auftritt."),
    ("Wie viele Felder soll das Formular haben?",
     "So wenige wie möglich: ein Name, eine Kontaktmöglichkeit und zwei "
     "Zeilen Nachricht genügen fast immer. Jedes zusätzliche Feld kostet "
     "Einsendungen."),
  ],
 },

 {
  "slug": "photos-professionnelles-site-web.html",
  "cat": "Fotografie",
  "titre": "Fotos: wann ein professionelles Shooting wirklich etwas ändert",
  "h1": ["Fotos: wann ein Shooting", "wirklich etwas ändert."],
  "desc": "Die drei Fälle, in denen ein Fotoshooting rentabel ist, die drei, "
          "in denen es das nicht ist, und das Briefing für die Fotografin.",
  "dek": "Ein Shooting kostet in der Schweiz zwischen CHF&nbsp;400 und "
         "CHF&nbsp;1 500. Manchmal ist es der bestangelegte Franken des "
         "Projekts, manchmal ein verlorener.",
  "lecture": "5 Min.",
  "corps": """
<p>Die Fotografie ist der Posten, bei dem man am meisten zögert, weil er
sichtbar und nicht unverzichtbar ist. Ein professionelles Shooting
verhandelt man in der Schweiz zwischen CHF&nbsp;400 für einen halben Tag mit
einem jungen Fotografen und CHF&nbsp;1 500 für einen ganzen Tag mit
Retusche. So finden Sie heraus, ob das Ihr Fall ist.</p>

<h2>Was die Fotografie wirklich ändert</h2>

<p>Sie macht Ihr Angebot nicht besser. Sie tut zwei Dinge: Sie
<strong>beweist, dass es Sie gibt</strong>, und sie <strong>zeigt den
Verarbeitungsgrad</strong> Ihrer Arbeit. Das ist alles — und je nach
Branche ist das enorm oder unerheblich.</p>

<h2>Die drei Fälle, in denen ein Shooting rentabel ist</h2>

<p><strong>1. Ihre Arbeit ist sichtbar.</strong> Coiffure, Küche,
Schreinerei, Innenausbau, Karosserie, Kosmetik, Gartenbau, Blumen. Das
Foto <em>ist</em> das Verkaufsargument. Hier kosten schlechte Fotos mehr
als keine Fotos, und ein Shooting ist die erste Investition, noch vor der
Website.</p>

<p><strong>2. Man kauft eine Person.</strong> Therapeutin, Anwalt, Coach,
Makler, Notar, Ärztin. Ein anständiges Porträt — Blick in die Kamera,
weiches Licht, neutraler Hintergrund — erhöht die Kontaktrate deutlich. Es
braucht keinen ganzen Tag: Eine Stunde genügt, und es ist das beste
Preis-Leistungs-Verhältnis der ganzen Liste.</p>

<p><strong>3. Ihr Ort ist ein Argument.</strong> Restaurant, Hotel,
Salon, Praxis, Laden. Die Kundschaft will sehen, wohin sie geht. Hier muss
das Shooting zu jener Stunde stattfinden, in der der Ort am schönsten ist,
was ein reserviertes Zeitfenster voraussetzt.</p>

<h2>Die drei Fälle, in denen es nicht Priorität hat</h2>

<p><strong>1. Ihre Arbeit ist unsichtbar.</strong> Informatik,
Buchhaltung, Beratung, Versicherung, Übersetzung. Menschen zu
fotografieren, die vor einem Computer lächeln, bringt nichts. Stecken Sie
das Geld in den Text, in Kundenreferenzen und in das
Google-Business-Profil.</p>

<p><strong>2. Sie verkaufen ein Produkt, das der Hersteller schon
fotografiert hat.</strong> Verwenden Sie seine Bilder: Sie sind oft besser
und werden mitgeliefert, prüfen Sie nur, ob Sie sie verwenden dürfen.</p>

<p><strong>3. Sie wissen noch nicht, was Sie verkaufen.</strong> Wenn sich
Ihr Angebot in sechs Monaten bewegt, bewegen sich die Fotos auch. Fangen
Sie mit dem Handy an: Das Shooting machen Sie, wenn das Angebot stabil
ist.</p>

<h2>Was ein Handy sehr gut kann</h2>

<p>Ein neueres Handy liefert zur richtigen Stunde sehr gute Ergebnisse.
Drei Regeln genügen:</p>

<ul>
  <li><strong>Tageslicht, nie den Blitz.</strong> Stellen Sie das Motiv
  zum Fenster hin, nicht mit dem Rücken dazu. Draussen vermeiden Sie die
  Mittagssonne: Der späte Nachmittag ist vorteilhafter.</li>
  <li><strong>Räumen Sie den Bildrand auf.</strong> Das herumliegende
  Kabel, der Karton, der Abfalleimer. Den Hintergrund aufzuräumen bringt
  einem Foto mehr als jeder Filter.</li>
  <li><strong>Fotografieren Sie weit und horizontal.</strong> Man schneidet
  immer weg, nie hinzu. Ein vertikales Foto passt nicht in ein
  Website-Banner.</li>
</ul>

<p>Behalten Sie die Originaldateien: Ein Screenshot eines Fotos oder ein
Bild, das dreimal durch WhatsApp gelaufen ist, kommt unbrauchbar an.</p>

<h2>Das Briefing für die Fotografin</h2>

<p>Der Unterschied zwischen einem nützlichen und einem bloss schönen
Shooting liegt darin, was vorher verlangt wird. Sechs Zeilen genügen:</p>

<ol>
  <li>Wofür die Bilder dienen — Website, Google-Profil, soziale Netzwerke —
  und in welchen Formaten.</li>
  <li>Drei Pflichtbilder (zum Beispiel: die Fassade mit lesbarer
  Beschriftung, das Team, eine fertige Arbeit).</li>
  <li>Ein <strong>sehr breites, horizontales Bild</strong> für den oberen
  Teil der Startseite, mit leerer Fläche auf einer Seite: Dort wird der
  Text liegen.</li>
  <li>Der Stil: zwei oder drei Beispiele von Websites, die Sie mögen, das
  ist mehr wert als eine Seite Adjektive.</li>
  <li>Die Rechte: zeitlich unbegrenzte Webnutzung, und schriftlich.</li>
  <li>Die Lieferung: Originaldateien in voller Auflösung, plus eine
  leichtere Version fürs Web.</li>
</ol>

<p>Dieser letzte Punkt zählt: Bilder mit 8 MB, die unverändert auf eine
Website kommen, machen sie langsam, und eine langsame Website verliert
Besucher. Wir skalieren und komprimieren grundsätzlich alles, was unsere
Kundschaft uns schickt, aber es ist besser, von guten Dateien
auszugehen.</p>

<h2>Wie viel dafür einsetzen</h2>

<ul>
  <li><strong>Porträt allein</strong> — CHF&nbsp;150 bis 400 für eine
  Stunde. Zu machen, sobald Ihr Gesicht Ihr Angebot ist.</li>
  <li><strong>Halber Tag vor Ort</strong> — CHF&nbsp;400 bis 800. Genügt für
  ein Geschäft, einen Salon, eine Praxis.</li>
  <li><strong>Ganzer Tag</strong> — CHF&nbsp;900 bis 1 500. Gerechtfertigt,
  wenn mehrere Leistungen oder mehrere Orte abzudecken sind.</li>
</ul>

<p>Ein nützlicher Anhaltspunkt: Wenn Ihre Website CHF&nbsp;500 kostet und
Ihre Fotos CHF&nbsp;1 200, ist das nicht absurd — in visuellen Berufen
arbeitet das Foto mehr als das Layout. Das Umgekehrte ist es manchmal
eher.</p>

<p>Wenn Ihre visuelle Identität gleichzeitig zu überarbeiten ist (Logo,
Farben, Ableitungen), ist jetzt der richtige Moment: Das ist Gegenstand
des <a href="../upsell-branding.html">Branding-Pakets</a>, und es
verhindert, eine Beschriftung zu fotografieren, die Sie drei Monate später
ändern.</p>
""",
  "faq": [
    ("Ist ein professionelles Fotoshooting unverzichtbar?",
     "Nein. Es ist entscheidend in Berufen, in denen die Arbeit sichtbar ist "
     "(Coiffure, Küche, Innenausbau), und in jenen, in denen man eine Person "
     "kauft. Für immaterielle Dienstleistungen ist es zweitrangig."),
    ("Was kostet ein Fotoshooting in der Schweiz?",
     "Von CHF 150 bis 400 für ein Porträt von einer Stunde, CHF 400 bis 800 "
     "für einen halben Tag vor Ort, CHF 900 bis 1 500 für einen ganzen Tag "
     "mit Retusche."),
  ],
 },
 {
  "slug": "premier-client-via-son-site.html",
  "cat": "Erwartungen",
  "titre": "Wie lange dauert es bis zum ersten Kunden über die Website?",
  "h1": ["Wie lange bis zum", "ersten Kunden?"],
  "desc": "Was Woche für Woche nach einem Onlinegang passiert, die drei "
          "Trafficquellen und ihr jeweiliges Tempo.",
  "dek": "Eine Website ist kein Lichtschalter. Je nach Trafficquelle, die "
         "Sie aktivieren, kommt der erste Kunde in drei Tagen oder in fünf "
         "Monaten.",
  "lecture": "6 Min.",
  "corps": """
<p>Das ist die Frage, die uns direkt nach dem Preis gestellt wird, und die
ehrliche Antwort lautet: Es hängt fast nicht von der Website ab. Es hängt
davon ab, wie die Leute dort ankommen. Es gibt drei Wege, und sie haben
ganz unterschiedliches Tempo.</p>

<h2>Die drei Quellen und ihre Frist</h2>

<p><strong>Der Traffic, den Sie selbst bringen — sofort.</strong> Sie
setzen die Adresse in Ihre E-Mail-Signatur, auf Ihre Offerten, auf Ihr
Fahrzeug, in Ihre Instagram-Bio, und Sie schicken sie Ihren Kontakten.
Erste Wirkung in wenigen Tagen. Das ist die am meisten unterschätzte
Quelle und die einzige, die gratis und sofort wirkt.</p>

<p><strong>Die Werbung — einige Tage.</strong> Google Ads, Meta, und
inzwischen Anzeigen in Assistenten wie ChatGPT. Sie zahlen, Sie haben
morgen Besucher. Das ist die einzige Art, sofort Volumen zu haben, und es
hört an dem Tag auf, an dem Sie aufhören zu zahlen.</p>

<p><strong>Die natürliche Auffindbarkeit — zwei bis sechs
Monate.</strong> Google muss Ihre Seiten entdecken, bewerten und dann
nach oben nehmen. Für eine lokale Suche mit wenig Konkurrenz («Schlosser
Morges») rechnen Sie mit sechs bis zehn Wochen. Für eine umkämpfte Suche
sechs Monate und mehr. Kein seriöser Anbieter verspricht Ihnen mehr.</p>

<h2>Was Woche für Woche passiert</h2>

<p><strong>Wochen 1 und 2.</strong> Die Website ist online. Ihre Besucher
sind jene, die Sie bringen: Nahestehende, bestehende Kundschaft, Kontakte.
Die ersten Anfragen kommen oft von Kunden, die Sie schon hatten — sie
entdecken eine Leistung, von der sie nichts wussten. Das ist ein echter
Gewinn, und niemand zählt ihn.</p>

<p><strong>Wochen 3 bis 6.</strong> Google hat die Seiten indexiert. Sie
erscheinen zuerst auf Ihren eigenen Namen, dann bei sehr präzisen Suchen.
Das Volumen ist klein, aber die Qualität ist hoch: Wer «Rollladenreparatur
Chêne-Bougeries» eintippt, ruft Sie fast immer an.</p>

<p><strong>Monate 2 und 3.</strong> Wenn Ihr Google-Business-Profil gut
eingestellt ist, wird es Ihre erste Anrufquelle, noch vor der Website.
Beide arbeiten zusammen: Das Profil bringt, die Website überzeugt. Das ist
der Moment, in dem sich zeigt, ob die Seiten die richtigen Dinge
sagen.</p>

<p><strong>Monate 4 bis 6.</strong> Die Auffindbarkeit der
Leistungsseiten setzt ein. Wenn Sie ein wenig Inhalt publiziert und ein
paar Bewertungen gesammelt haben, richtet sich die Kurve deutlich auf. Das
ist auch der Moment, in dem man weiss, welche Seiten hinzuzufügen sind:
Die Anfragen haben es Ihnen gesagt.</p>

<h2>Was wirklich beschleunigt</h2>

<ul>
  <li><strong>Ein vollständiges Google-Business-Profil.</strong> Wirkung in
  wenigen Tagen und gratis. Das ist der Hebel Nr. 1 für ein lokales KMU —
  <a href="fiche-google-business.html">die Einstellung, die Sie nicht
  verpassen dürfen</a>.</li>
  <li><strong>Die Adresse überall hinschreiben.</strong> Signatur,
  Offerten, Rechnungen, Fahrzeug, Schaufenster, soziale Netzwerke. Das
  kostet nichts und verdoppelt oft den Traffic des ersten Monats.</li>
  <li><strong>Eine Seite pro Leistung.</strong> Fünf präzise Seiten
  positionieren sich viel besser als eine Seite, die von allem
  spricht.</li>
  <li><strong>Bewertungen, regelmässig.</strong> Eine pro Monat ist mehr
  wert als zehn auf einmal.</li>
  <li><strong>Ein kleines Werbebudget zum Start.</strong> CHF&nbsp;200 bis
  500 über drei Wochen genügen, um zu wissen, ob Ihre Seite konvertiert —
  eine Information, die man anders nicht erhält.</li>
</ul>

<h2>Was bremst</h2>

<ul>
  <li><strong>Eine langsame Website.</strong> Die Besucher gehen, bevor
  sie das Angebot lesen; die Auffindbarkeit leidet ebenfalls.</li>
  <li><strong>Kein Preis, kein Gebiet, keine Frist.</strong> Der Besucher
  fragt nicht, er nimmt an, und er geht.</li>
  <li><strong>Warten, bis man alles hat.</strong> Eine Website, die online
  ist und sich ergänzt, schlägt eine perfekte Website in sechs
  Monaten.</li>
  <li><strong>Den Domainnamen wechseln.</strong> Sie beginnen bei null.
  Wählen Sie ihn einmal und behalten Sie ihn.</li>
</ul>

<h2>Was zu messen ist</h2>

<p>Drei Zahlen, einmal im Monat, zehn Minuten:</p>

<ol>
  <li><strong>Wie viele Besucher</strong>, und woher sie kommen (Suche,
  soziale Netzwerke, direkt).</li>
  <li><strong>Wie viele Anfragen</strong> — Formulare, Anrufe,
  WhatsApp.</li>
  <li><strong>Wie viele Kunden</strong> aus diesen Anfragen.</li>
</ol>

<p>Das Verhältnis zwischen der ersten und der zweiten Zahl beurteilt Ihre
Seite. Das Verhältnis zwischen der zweiten und der dritten beurteilt Ihr
Angebot und Ihre Art zu antworten. Zwei verschiedene Probleme: Korrigieren
Sie nicht die Website, wenn die Offerte das Problem ist.</p>

<h2>Ein ehrlicher Anhaltspunkt</h2>

<p>Für ein lokales Schweizer KMU mit einem korrekt eingestellten
Google-Profil, einer klaren Website und der überall verbreiteten Adresse:
<strong>die ersten Anfragen kommen in der Regel innerhalb von zwei bis
vier Wochen</strong>, und die Website wird zwischen dem dritten und
sechsten Monat zu einer regelmässigen Quelle. Ohne Google-Profil, ohne
Bewertungen und ohne verbreitete Adresse kann es viel länger dauern — und
dann ist es kein Problem der Website.</p>

<p>Wenn Sie den Plan für die ersten dreissig Tage nach dem Onlinegang
wollen, er ist Teil von <a href="../index.html#methode">Die Methode Lokale
Kundschaft</a>, die wir zum
<a href="../offres/ultimate-website.html">Site Complet</a> abgeben.</p>
""",
  "faq": [
    ("Wie lange dauert es nach einem Onlinegang, bis man auf Google sichtbar ist?",
     "Einige Tage, um indexiert zu werden, sechs bis zehn Wochen, um sich "
     "bei einer lokalen Suche mit wenig Konkurrenz zu positionieren, sechs "
     "Monate und mehr bei einer umkämpften Suche."),
    ("Wann kommt die erste Anfrage über eine Website?",
     "In der Regel innerhalb von zwei bis vier Wochen für ein lokales KMU, "
     "das seine Adresse verbreitet und über ein korrekt eingestelltes "
     "Google-Business-Profil verfügt."),
  ],
 },

 {
  "slug": "recuperer-son-nom-de-domaine.html",
  "cat": "Praxis",
  "titre": "Den eigenen Domainnamen in fünf Schritten zurückholen",
  "h1": ["Den Domainnamen", "zurückholen: fünf Schritte."],
  "desc": "Ihre Domain lautet auf Ihren früheren Anbieter? Hier ist das "
          "genaue Vorgehen, und was zu tun ist, wenn er nicht mehr "
          "antwortet.",
  "dek": "Der Domainname ist das einzige Element Ihrer Onlinepräsenz, das "
         "man nicht neu machen kann. Lautet er nicht auf Ihren Namen, ist "
         "das das Erste, was zu korrigieren ist.",
  "lecture": "6 Min.",
  "corps": """
<p>Eine Website baut man neu. Einen Domainnamen mit acht Jahren
Geschichte, eingehenden Links und Ihren E-Mail-Adressen nicht. Deshalb
kaufen wir die Domain immer auf den Namen der Kundschaft, und deshalb sehen
unsere <a href="../legal/conditions.html">Allgemeinen
Geschäftsbedingungen</a> ihre Übertragung auf einfache Anfrage und
kostenlos vor.</p>

<p>Nicht alle Anbieter handeln so. Wenn Ihrer Ihre Domain hält, hier das
Vorgehen.</p>

<h2>Schritt 1 — Herausfinden, wo sie liegt und wem sie gehört</h2>

<p>Zwei Dinge sind zu unterscheiden: der <strong>Inhaber</strong> (der
rechtliche Eigentümer) und der <strong>Registrar</strong> (das
Unternehmen, bei dem die Domain registriert ist).</p>

<p>Für eine <code>.ch</code> gibt Ihnen das öffentliche Verzeichnis der
Schweizer Registerstelle (<em>whois</em> von SWITCH, über nic.ch) den
Registrar. Für eine <code>.com</code> die Whois-Suche der ICANN. Die
Kontaktdaten des Inhabers sind aus Datenschutzgründen oft verborgen, der
Registrar dagegen ist immer sichtbar — und den brauchen Sie.</p>

<p>Notieren Sie auch das <strong>Ablaufdatum</strong>. Liegt es weniger
als fünfzehn Tage in der Zukunft, behandeln Sie das Dossier dringend: Eine
abgelaufene Domain kann von jedem gekauft werden.</p>

<h2>Schritt 2 — Die Übertragung schriftlich verlangen</h2>

<p>Schreiben Sie dem Anbieter eine kurze, sachliche Nachricht und
verlangen Sie ausdrücklich diese drei Dinge:</p>

<ul>
  <li>den <strong>Autorisierungscode für die Übertragung</strong> (Auth
  Code, EPP-Code oder <em>Authcode</em>);</li>
  <li>die <strong>Entsperrung</strong> der Domain (den <em>Transfer
  Lock</em>);</li>
  <li>die Umschreibung des Inhabers auf Ihren Namen, falls die Domain
  nicht schon auf Ihren Namen lautet.</li>
</ul>

<p>Setzen Sie eine angemessene Frist — zehn Arbeitstage — und behalten Sie
einen schriftlichen Nachweis. In der grossen Mehrheit der Fälle genügt
das: Die meisten Anbieter haben keine Lust, die Domain einer Kundschaft
als Pfand zu behalten, die geht.</p>

<h2>Schritt 3 — Ein Konto bei einem Registrar eröffnen, auf Ihren Namen</h2>

<p>Erstellen Sie das Konto mit <strong>Ihrer</strong> E-Mail-Adresse und
<strong>Ihrer</strong> Karte — dieses Konto macht Sie für die nächsten zehn
Jahre zur Eigentümerin. Verwenden Sie keine Adresse, die von der Domain
abhängt, die Sie übertragen: Läuft die Übertragung schief, verlieren Sie
den Zugang zu Ihrem Postfach zugleich mit der Domain.</p>

<p>Für eine <code>.ch</code> vereinfacht ein Schweizer Registrar die
Rechnungsstellung und den Support in der Landessprache. Der gängige Tarif
liegt bei rund zehn Franken pro Jahr; der Preisunterschied zwischen
Registraren ist unerheblich, die Qualität des Supports nicht.</p>

<h2>Schritt 4 — Die Übertragung starten</h2>

<p>Beim neuen Registrar: «Domain übertragen», dann den Namen und den
Autorisierungscode. Die Registerstelle schickt eine
Bestätigungsanfrage an die Adresse des Inhabers. Bestätigen Sie.</p>

<p>Rechnen Sie mit einem bis sieben Tagen, je nach Endung. Währenddessen
<strong>funktionieren Ihre Website und Ihre E-Mails weiter</strong>: Eine
Registrarübertragung ändert das DNS nicht. Das ist eine häufige und
unbegründete Sorge.</p>

<p>Zwei Details, die hängen bleiben: Eine Domain, die vor weniger als
sechzig Tagen registriert oder übertragen wurde, kann nicht erneut
übertragen werden (Regel der ICANN), und eine gesperrt gebliebene Domain
lässt die Anfrage ohne klare Erklärung scheitern.</p>

<h2>Schritt 5 — Das DNS prüfen, und vor allem die E-Mails</h2>

<p>Sobald die Übertragung abgeschlossen ist, öffnen Sie die DNS-Zone beim
neuen Registrar und vergleichen Sie sie Zeile für Zeile mit der alten. Die
meisten Registrare übernehmen die Einträge automatisch, aber nicht
alle.</p>

<p>Achten Sie besonders auf:</p>

<ul>
  <li>die Einträge <strong>A</strong> und <strong>CNAME</strong>, die auf
  die Website zeigen;</li>
  <li>die <strong>MX</strong>-Einträge, über die Ihre E-Mails ankommen —
  <em>dort</em> passieren die Unfälle;</li>
  <li>die <strong>TXT</strong>-Einträge vom Typ SPF, DKIM und DMARC, ohne
  die Ihre E-Mails im Spam landen.</li>
</ul>

<p>Machen Sie die Prüfung an einem Wochentag, am Morgen, und schicken Sie
sich innerhalb der folgenden Stunde von einer externen Adresse eine
Test-E-Mail.</p>

<h2>Wenn der Anbieter nicht antwortet</h2>

<ol>
  <li><strong>Mahnen Sie schriftlich</strong>, wenn nötig eingeschrieben,
  unter Verweis auf Ihren Vertrag und mit einer Frist.</li>
  <li><strong>Schreiben Sie direkt dem Registrar</strong> mit Ihren
  Eigentumsnachweisen: Erneuerungsrechnungen,
  Handelsregisterauszug, eingetragene Marke. Registrare haben ein
  Verfahren für Streitigkeiten über die Inhaberschaft.</li>
  <li><strong>Für eine <code>.ch</code></strong> verfügt die Schweizer
  Registerstelle über ein Streitbeilegungsverfahren; für die generischen
  Endungen ist es das UDRP-Verfahren der WIPO. Sie sind für Fälle von
  Bösgläubigkeit gedacht und kosten etwas.</li>
  <li><strong>Als letztes Mittel</strong> kaufen Sie eine Variante
  (<code>.ch</code> statt <code>.com</code>, oder einen leicht anderen
  Namen) und leiten um. Sie verlieren Geschichte, aber Sie gewinnen die
  Kontrolle zurück — und das ist oft günstiger als ein Verfahren über
  sechs Monate.</li>
</ol>

<h2>Damit das nicht mehr vorkommt</h2>

<ul>
  <li>Die Domain ist <strong>auf Ihren Namen</strong> registriert, auf
  einem Konto, dessen Zugangsdaten <strong>Sie</strong> haben.</li>
  <li>Die E-Mail-Adresse des Kontos hängt nicht von der Domain selbst
  ab.</li>
  <li>Die automatische Erneuerung ist aktiv, auf einer gültigen Karte.</li>
  <li>Der Transfer Lock ist im Normalfall aktiv: Er verhindert eine
  Entwendung.</li>
  <li>Ihre Zugangsdaten sind anderswo notiert als im Kopf einer einzigen
  Person.</li>
</ul>

<p>Wir handhaben das standardmässig so: Die Domain wird auf Ihren Namen
gekauft, sie bleibt jederzeit Ihr Eigentum, und sie wird Ihnen auf Anfrage
kostenlos übertragen, auch wenn Sie anderswohin gehen. Das steht in
unseren Bedingungen, und das ist der einzige Ort, an dem es zählt. Wenn
Sie eine Domain zurückholen müssen, bevor Sie Ihre Website neu machen,
<a href="../devis.html">sagen Sie es uns</a>: Das ist eine Aufgabe, die
wir regelmässig erledigen.</p>
""",
  "faq": [
    ("Verliert man Website und E-Mails während einer Domainübertragung?",
     "Nein. Eine Registrarübertragung ändert das DNS nicht: Website und "
     "E-Mails funktionieren weiter. Ausfälle kommen von einer nach der "
     "Übertragung falsch kopierten DNS-Zone, insbesondere von den "
     "MX-Einträgen."),
    ("Was tun, wenn der frühere Anbieter die Domain nicht herausgibt?",
     "Schriftlich mahnen mit einer Frist, dann den Registrar mit "
     "Eigentumsnachweisen einschalten. Für .ch gibt es ein "
     "Streitbeilegungsverfahren, für die generischen Endungen das "
     "UDRP-Verfahren der WIPO."),
    ("Was kostet ein .ch-Domainname pro Jahr?",
     "Rund zehn Franken pro Jahr bei den meisten Registraren. Der "
     "Preisunterschied zwischen Anbietern ist unerheblich."),
  ],
 },
]


# ---------------------------------------------------------------------------
# Bezeichnungen der Oberfläche (alles, was nicht Artikeltext ist)
# ---------------------------------------------------------------------------

UI = {
    "accueil": "Startseite",
    "fil_blog": "Blog",
    "blog_titre": "Blog: Websites und Sichtbarkeit für Schweizer KMU | Up2Front",
    "blog_desc": "Neun Artikel für Schweizer KMU: echte Preise, echte "
                 "Fristen, und was wir an Ihrer Stelle tun würden.",
    "date_texte": "12. September 2026",
    "meta": "Veröffentlicht am {date} · Lesezeit {lecture}",
    "retour": "Alle Artikel",
    "voir_tarifs": "Preise ansehen",
    "demander_devis": "Offerte anfordern",
    "lire": "Artikel lesen",
    "faq_t": "Häufige Fragen.",
    "faq_c": "Die Fragen, die uns zu diesem Thema gestellt werden, mit der "
             "kurzen Antwort.",
    "suite_t": "Als Nächstes lesen.",
    "suite_c": "Zwei weitere Artikel aus dem Journal, zu verwandten Themen.",
    "art_appel_h2": "Eine Einschätzung zu Ihrem Fall?",
    "art_appel_p": "Beschreiben Sie Ihre Tätigkeit in drei Zeilen. Wir "
                   "antworten am selben Tag, von Montag bis Freitag, und wir "
                   "sagen auch, wann eine Website nicht Ihre Priorität ist.",
    "art_appel_b1": "Offerte anfordern",
    "art_appel_b2": "Preise ansehen",
    "ecrire": "An contact@up2front.com schreiben",
}


# ---------------------------------------------------------------------------
# Seite Empfehlungsprogramm — angekündigt, nicht offen
# ---------------------------------------------------------------------------

PARRAINAGE = {
    "titre": "Empfehlungsprogramm | Up2Front",
    "desc": "Unser Empfehlungsprogramm ist noch nicht offen. Hier steht, was "
            "in Vorbereitung ist, und wie Sie benachrichtigt werden, wenn es "
            "startet.",
    "fil": "Empfehlungen",
    "sur_titre": "Bald verfügbar",
    "h1": ["Das Empfehlungsprogramm kommt.", "Offen ist es noch nicht."],
    "lede": "Wir bereiten ein Empfehlungsprogramm für jene vor, die uns "
            "schon heute weiterempfehlen. Solange es nicht steht, zeigen wir "
            "keinen Betrag an und verlangen keine Bankverbindung.",
    "b1": "Über den Start informiert werden",
    "b2": "Aktuelle Bedingungen lesen",
    "prose": """
<p class="maj">Stand 12. September 2026 — Programm in Vorbereitung</p>

<p><strong>Bei Up2Front ist heute kein Empfehlungsprogramm offen.</strong>
Es wird keine Provision versprochen, es ist keine Anmeldung offen, und
aufgrund einer Empfehlung kann keine Zahlung gefordert werden. Diese Seite
existiert, um anzukündigen, was wir vorbereiten, nicht um irgendetwas
unterschreiben zu lassen.</p>

<p>Wir hätten schon jetzt eine Provisionstabelle veröffentlichen können:
Das ist eine Zeile Text. Aber ein tragfähiges Empfehlungsprogramm
verlangt einen Apparat dahinter — nachverfolgen, wer wen empfohlen hat,
prüfen, dass eine Bestellung tatsächlich bezahlt wurde, einen Betrag an
eine Person auszahlen, die nicht Kunde ist, und diese Auszahlung
buchhalterisch und steuerlich korrekt behandeln. Diesen Apparat richten
wir ein, bevor wir öffnen.</p>

<h2>Was am Tag des Starts angekündigt wird</h2>

<ul>
  <li>Wer teilnehmen kann, und unter welchen Bedingungen.</li>
  <li>Was genau eine Gegenleistung auslöst, und zu welchem Zeitpunkt.</li>
  <li>Der Betrag oder der Prozentsatz, schwarz auf weiss.</li>
  <li>Die Zahlungsfrist und das verwendete Mittel.</li>
  <li>Die Fälle, in denen nichts geschuldet ist — Storno, Rückerstattung,
  Bestellung durch Sie selbst.</li>
</ul>

<p>Solange diese fünf Punkte nicht geschrieben sind, gibt es kein
Programm. Unsere <a href="legal/affiliation.html">Bedingungen für
Empfehlungen und Partnerschaften</a> sagen es mit denselben Worten, und
sie sind massgebend.</p>

<h2>Wenn Sie uns bis dahin weiterempfehlen</h2>

<p>Das kommt vor, und davon lebt ein junges Unternehmen. Wenn jemand dank
Ihnen bestellt, schreiben Sie uns an
<a href="mailto:contact@up2front.com">contact@up2front.com</a>: Wir
besprechen das einvernehmlich, von Fall zu Fall. Es wird eine einmalige
Vereinbarung sein, nicht die Anwendung eines Programms — und wir werden es
auch so nennen.</p>

<h2>Benachrichtigt werden</h2>

<p>Eine Nachricht an <a href="mailto:contact@up2front.com?subject=Parrainage%20—%20me%20pr%C3%A9venir%20du%20lancement">contact@up2front.com</a>
mit dem Vermerk «Empfehlung» genügt. Wir brauchen Ihre Bankverbindung
nicht, um Sie auf eine Warteliste zu setzen, und wir werden sie nie
verlangen, bevor ein Betrag tatsächlich geschuldet ist.</p>
""",
    "etapes_t": "Was wir einrichten.",
    "etapes_c": "Drei Baustellen, in dieser Reihenfolge. Das Programm "
                "öffnet, wenn alle drei fertig sind.",
    "etapes": [
        ("Baustelle 1", "Die Nachverfolgung der Empfehlungen",
         "Ein persönlicher Empfehlungslink, verknüpft mit einer bezahlten "
         "Bestellung. Ohne diese Nachverfolgung lässt sich nicht sagen, wer "
         "worauf Anspruch hat."),
        ("Baustelle 2", "Der schriftliche Rahmen",
         "Vollständige Empfehlungsbedingungen, in die AGB integriert, die "
         "auch sagen, in welchen Fällen nichts geschuldet ist."),
        ("Baustelle 3", "Die Auszahlung",
         "Die buchhalterische und steuerliche Behandlung einer "
         "Gegenleistung an eine Person, die nicht Kunde ist. Das ist der "
         "längste Punkt."),
    ],
    "appel_h2": "Bis dahin die einfachste Art, uns zu helfen",
    "appel_p": "Sprechen Sie mit jemandem über uns, der es braucht, und "
               "sagen Sie es uns. Wir antworten am selben Tag, von Montag "
               "bis Freitag.",
    "appel_b1": "An contact@up2front.com schreiben",
    "appel_b2": "Preise ansehen",
}
