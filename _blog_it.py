# -*- coding: utf-8 -*-
"""
I nove articoli del blog, in italiano.

Il piano editoriale è quello di Alex: i suoi nove titoli, nel suo ordine,
con le sue nove categorie. Ciò che il suo dossier lasciava «da scrivere» è
scritto qui.

Linea editoriale, la stessa del resto del sito: nessuna cifra inventata,
nessuna statistica senza fonte, niente che contraddica le condizioni
generali pubblicate. Dove è citato un prezzo di mercato, lo è per fasce e
con una data, perché si muove.

Angolo SEO: ogni articolo punta a una domanda che le PMI svizzere digitano
davvero, risponde nei primi due paragrafi, poi sviluppa. Il titolo H1
riprende la domanda, gli H2 sono sotto-domande, e i link interni puntano
alle pagine che monetizzano (prezzi, offerte, preventivo, briefing).
"""

INDEX = {
    "sur_titre": "Il giornale",
    "h1": ["Quello che avremmo", "voluto sapere prima."],
    "lede": "Nove articoli brevi, scritti per le PMI svizzere. Prezzi "
            "reali, tempi reali, e quello che faremmo al Suo posto.",
    "sec_t": "Gli articoli.",
    "sec_c": "Ordinati dal più richiesto al più tecnico. Nessuno ha "
             "bisogno degli altri per essere letto.",
    "appel_h2": "Una domanda che non è trattata qui?",
    "appel_p": "Ce la scriva, rispondiamo in giornata dal lunedì al "
               "venerdì. E se la risposta interessa anche ad altri, "
               "diventa un articolo.",
}

ARTICLES = [
 {
  "slug": "prix-site-web-suisse.html",
  "cat": "Prezzi",
  "titre": "Quanto costa davvero un sito web in Svizzera nel 2026?",
  "h1": ["Quanto costa davvero", "un sito web in Svizzera?"],
  "desc": "Le quattro fasce del mercato svizzero, ciò che fa salire il "
          "conto, e le spese annuali che nessuno calcola all'inizio.",
  "dek": "Risposta breve: tra CHF 300 e CHF 30 000. Lo scarto non è una "
         "questione di qualità, è una questione di ciò che si compra. "
         "Ecco come leggere un preventivo.",
  "lecture": "7 min",
  "corps": """
<p>Nessuno risponde mai a questa domanda, ed è irritante. Cominciamo
quindi dalla cifra: in Svizzera, nel 2026, un sito web professionale per
una PMI si paga tra <strong>CHF 300 e CHF 30&nbsp;000</strong>. Questo
scarto da uno a cento non è uno scarto di qualità. È uno scarto di
perimetro — e soprattutto di ore umane fatturate.</p>

<p>Il resto di questo articolo serve a sapere in quale fascia si colloca,
e a non pagare una fascia per ottenere il contenuto di quella
precedente.</p>

<h2>Le quattro fasce del mercato svizzero</h2>

<p><strong>Da CHF 0 a 500 — fa da sé.</strong> Un costruttore online, un
modello del catalogo, i Suoi testi, le Sue foto. Il costo reale non è
l'abbonamento, è il Suo fine settimana. Conti da venti a quaranta ore per
un risultato onesto, di più se deve ancora scoprire lo strumento.
Sostenibile se il Suo sito è soltanto un biglietto da visita.</p>

<p><strong>Da CHF 300 a 1 500 — il pacchetto a prezzo fisso.</strong> Un
professionista lavora su una struttura che ha già collaudato, Lei compila
un briefing, lui consegna in qualche giorno. È qui che ci collochiamo, con
pacchetti a prezzo fisso a <a href="../offres/pro-landing-page.html">CHF
290</a>, <a href="../offres/ultimate-website.html">CHF 490</a> e
<a href="../offres/advanced-website.html">CHF 690</a>. Il prezzo tiene
perché il perimetro è fissato in anticipo, non perché il lavoro sia
raffazzonato.</p>

<p><strong>Da CHF 3 000 a 12 000 — il su misura di un indipendente o di
un piccolo studio.</strong> Si riparte da una pagina bianca: incontri di
lavoro, struttura del sito, bozze, scambi, integrazione. Da due a otto
settimane. È il budget giusto non appena il Suo sito deve fare qualcosa di
particolare — un configuratore, una prenotazione, un catalogo che
cambia.</p>

<p><strong>Da CHF 15 000 a 30 000 e oltre — l'agenzia.</strong>
Strategia, direzione artistica, redazione, sviluppo, monitoraggio, e più
persone attorno al tavolo. Giustificato quando il sito è un canale di
vendita principale e un punto di conversione guadagnato vale diverse
decine di migliaia di franchi all'anno.</p>

<h2>Ciò che fa salire davvero il conto</h2>

<p>Non è quasi mai il design. Sono, nell'ordine:</p>

<ul>
  <li><strong>Gli scambi senza limiti.</strong> Un progetto senza
  perimetro scritto va alla deriva, e la deriva si fattura a ore. È la
  prima voce nascosta di tutti i preventivi.</li>
  <li><strong>I contenuti.</strong> Se l'agenzia deve scrivere i Suoi
  testi, intervistare i Suoi collaboratori e far venire un fotografo, Lei
  finanzia tre mestieri, non uno.</li>
  <li><strong>Le funzionalità.</strong> Pagamento online, area clienti,
  prenotazione, sincronizzazione con il Suo gestionale: ognuna è un
  piccolo progetto.</li>
  <li><strong>Il multilingue.</strong> Ogni lingua aggiunge traduzione,
  rilettura e una manutenzione che si moltiplica.</li>
  <li><strong>Il CMS.</strong> Rendere un sito modificabile da Lei
  raddoppia spesso il tempo di integrazione. Utile se pubblica ogni
  settimana, inutile se cambia un numero di telefono una volta
  all'anno.</li>
</ul>

<h2>Le spese annuali che nessuno calcola</h2>

<p>Il preventivo di creazione è metà della storia. Ciò che torna ogni
anno, in Svizzera, ai prezzi correnti del 2026:</p>

<ul>
  <li><strong>Nome a dominio in <code>.ch</code></strong> — una decina di
  franchi all'anno. Un <code>.com</code>, una quindicina.</li>
  <li><strong>Hosting</strong> — da CHF 0 per un sito statico su una
  piattaforma come Netlify o Cloudflare Pages, a CHF 200–400 all'anno per
  un hosting condiviso svizzero, di più per un server dedicato.</li>
  <li><strong>Indirizzi e-mail professionali</strong> — da CHF 60 a 150
  all'anno per casella, secondo il fornitore. È spesso la sorpresa.</li>
  <li><strong>Certificato HTTPS</strong> — oggi gratuito
  (Let's Encrypt), e automatico presso la maggior parte degli hoster. Se
  glielo fatturano, chieda perché.</li>
  <li><strong>Manutenzione</strong> — da CHF 0 per un sito statico a
  CHF 600–1 800 all'anno per un WordPress che va aggiornato, e che
  aggiornare bisogna: è la prima causa di violazione dei siti delle
  PMI.</li>
</ul>

<p>In altre parole: un sito da CHF 2 000 che costa CHF 1 200 all'anno di
manutenzione è più caro, su cinque anni, di un sito da CHF 5 000 che costa
solo il suo dominio.</p>

<h2>Che cosa cambia un prezzo fisso</h2>

<p>Un prezzo fisso sposta il rischio. Se il progetto richiede più tempo
del previsto, è un problema del fornitore, non Suo. In cambio, il
perimetro è scritto prima di cominciare: numero di pagine, numero di
lingue, ciò che è compreso, ciò che è oggetto di un preventivo
separato.</p>

<p>È questo quadro che ci permette di annunciare un <a
href="../index.html#tarifs">listino pubblico</a> e una consegna
<strong>da due giorni lavorativi</strong> a partire dal briefing completo,
con <strong>trenta giorni di revisioni illimitate</strong> e un
<strong>rimborso integrale</strong> se il risultato non Le va bene. Le
<a href="../legal/conditions.html">condizioni generali</a> lo dicono nero
su bianco, che è l'unico posto in cui una promessa commerciale vale
qualcosa.</p>

<h2>Quanto prevedere, concretamente</h2>

<ul>
  <li><strong>Artigiano o indipendente, una pagina che presenta e fa
  telefonare</strong> — CHF 300 a 800 di creazione, meno di CHF 50
  all'anno.</li>
  <li><strong>PMI di servizi, da quattro a sei pagine, una lingua</strong>
  — CHF 500 a 2 500 di creazione.</li>
  <li><strong>PMI svizzera che deve esistere in italiano e in
  tedesco</strong> — CHF 700 a 4 000, con la traduzione che pesa più del
  design.</li>
  <li><strong>Negozio con vendita online</strong> — CHF 3 000 a 15 000, e
  un vero budget di tempo per il catalogo.</li>
</ul>

<p>Se esita tra due fasce, la domanda utile non è «quale budget ho?» ma
«quanto vale un cliente per me?». Uno studio per cui un cliente vale
CHF 3 000 ripaga un sito da CHF 5 000 con due clienti. Un negozio il cui
scontrino medio è di CHF 40 deve ragionare diversamente.</p>

<h2>Tre domande che ci vengono poste</h2>

<h3>Un sito a CHF 290 è possibile o è un'esca?</h3>
<p>È possibile a tre condizioni: una pagina e non otto, una struttura già
collaudata invece di una pagina bianca, e un briefing che compila Lei
stesso. Tolga una di queste tre condizioni e il prezzo raddoppia. La
nostra <a href="../offres/pro-landing-page.html">Landing Pro</a> dice
esattamente che cosa contiene e che cosa non contiene.</p>

<h3>Perché due preventivi per lo stesso sito variano dal semplice al triplo?</h3>
<p>Perché non descrivono lo stesso lavoro. Confronti il numero di pagine,
il numero di cicli di correzione inclusi, chi scrive i testi, chi
fornisce le foto, e che cosa succede se cambia idea. Nove volte su dieci
la differenza è lì, e non nel talento.</p>

<h3>Bisogna pagare un abbonamento mensile?</h3>
<p>Soltanto se riceve qualcosa ogni mese — modifiche, una sorveglianza,
un rapporto. Un abbonamento che finanzia solo l'hosting di un sito
statico si sostituisce con una decina di franchi di dominio
all'anno.</p>
""",
  "faq": [
    ("Quanto costa un sito web per una PMI in Svizzera?",
     "Tra CHF 300 e CHF 30 000 secondo il perimetro. Un pacchetto per un "
     "sito vetrina da una a sette pagine si colloca tra CHF 300 e CHF 1 500; "
     "un progetto su misura con funzionalità parte attorno a CHF 3 000."),
    ("Quali sono le spese annuali di un sito web?",
     "Il nome a dominio (circa CHF 10 all'anno per un .ch), l'hosting (da "
     "gratuito per un sito statico a CHF 400 all'anno), gli indirizzi e-mail "
     "professionali (CHF 60 a 150 per casella e per anno) e la manutenzione "
     "se il sito gira su un CMS."),
    ("Un prezzo fisso costa meno di un preventivo a ore?",
     "Non sistematicamente, ma è prevedibile: il perimetro è scritto prima "
     "di cominciare e uno sforamento di tempo è a carico del fornitore."),
  ],
 },

 {
  "slug": "landing-page-ou-site-complet.html",
  "cat": "Decidere",
  "titre": "Landing page o sito completo: come scegliere",
  "h1": ["Landing page o sito completo.", "Come scegliere."],
  "desc": "La domanda non è il numero di pagine, è il numero di decisioni "
          "che il Suo visitatore deve prendere. Un test in tre domande.",
  "dek": "Una pagina unica non è una versione ridotta di un sito. È uno "
         "strumento diverso, che vince in certi casi e perde in altri.",
  "lecture": "5 min",
  "corps": """
<p>Ci viene chiesto quasi sempre «quante pagine mi servono?». È la domanda
sbagliata: riguarda la quantità mentre il problema è un problema di
percorso. La domanda giusta è <strong>quante decisioni diverse deve
prendere il Suo visitatore</strong> prima di contattarLa.</p>

<p>Una decisione, una pagina. Più decisioni, più pagine.</p>

<h2>Quando basta una sola pagina</h2>

<p>Una pagina unica funziona quando tutti i Suoi visitatori vogliono la
stessa cosa, e alla fine c'è un solo gesto: telefonare, prenotare,
chiedere un preventivo.</p>

<ul>
  <li>Un artigiano che vuole essere chiamato per dei cantieri.</li>
  <li>Un ristorante: il menu, gli orari, l'indirizzo, la prenotazione.</li>
  <li>Uno studio o un terapista con una sola prestazione principale.</li>
  <li>Un'offerta unica lanciata per una campagna, con un modulo alla fine.</li>
</ul>

<p>Il suo vantaggio non è il prezzo, è l'assenza di scelta. Su una pagina
ben costruita, il visitatore scende e arriva al modulo. Su un sito di
otto pagine, si perde nel menu ed esce. È anche per questo che una pagina
unica si pubblica <a href="../index.html#process">in due giorni
lavorativi</a>: c'è meno da decidere, quindi meno da arbitrare.</p>

<h2>Quando ne servono diverse</h2>

<p>Più pagine diventano necessarie non appena una di queste tre cose è
vera.</p>

<p><strong>Ha più prestazioni che non parlano alle stesse
persone.</strong> Un fiduciario che fa contabilità, fiscalità e salari ha
tre pubblici. Una pagina sola li mescola e non ne convince nessuno. Tre
pagine, ciascuna con il suo vocabolario, sono anche tre porte d'ingresso
per Google: è la ragione più redditizia per aggiungere pagine.</p>

<p><strong>Deve essere trovato su ricerche diverse.</strong>
Google classifica pagine, non siti. «Lattoniere Lugano» e «riparazione
tetti Lugano» meritano due pagine, altrimenti si posiziona a metà su
entrambe.</p>

<p><strong>La fiducia richiede spazio.</strong> Più l'importo è alto, più
il visitatore vuole referenze, recensioni, una pagina «chi siamo», a volte
delle condizioni. Un acquisto da CHF 15 000 non si decide su una pagina
che scorre.</p>

<h2>Il test delle tre domande</h2>

<ol>
  <li><strong>Quante prestazioni diverse vuole vendere?</strong>
  Una: una pagina. Da due a cinque: una pagina per prestazione.</li>
  <li><strong>Quante ricerche Google diverse vuole vincere?</strong>
  Conti una pagina per ogni ricerca importante.</li>
  <li><strong>Il Suo visitatore ha bisogno di verificare qualcosa prima di
  scriverLe?</strong> Se sì, preveda la pagina che glielo permette —
  referenze, recensioni, team.</li>
</ol>

<p>Sommi. Una pagina se il totale è uno, cinque pagine se il totale si
aggira attorno a quattro o cinque, sette se ha un vero catalogo di
prestazioni. È esattamente la logica dei nostri tre livelli:
<a href="../offres/pro-landing-page.html">Landing Pro</a> per una pagina,
<a href="../offres/ultimate-website.html">Site Complet</a> fino a cinque,
<a href="../offres/advanced-website.html">Site Étendu</a> fino a sette e
in tre lingue.</p>

<h2>L'errore più frequente</h2>

<p>Ordinare otto pagine e riempirne soltanto tre. Un sito mezzo vuoto
ispira meno fiducia di una pagina densa e finita, e costa di più da
produrre come da mantenere. Se oggi non ha i contenuti, oggi prenda meno
pagine.</p>

<p>Esiste anche l'errore simmetrico: ammassare cinque prestazioni su una
pagina unica perché costava meno. Il visitatore non legge la sesta
sezione, e Google non sa su che cosa posizionarLa.</p>

<h2>E se mi sbaglio?</h2>

<p>Non è grave, a due condizioni. La prima: che il sito sia costruito in
modo da potergli aggiungere una pagina senza rifarlo. La seconda: che
<a href="../legal/conditions.html">il Suo nome a dominio sia intestato a
Lei</a> — è lui che porta il Suo posizionamento, non il sito.</p>

<p>Nei fatti, la maggior parte dei nostri clienti comincia con una pagina,
guarda per tre mesi da dove arrivano le chiamate, poi aggiunge le due o
tre pagine che le chiamate hanno indicato. È meno elegante di un piano
perfetto, ed è molto più efficace.</p>

<p>Se esita ancora, <a href="../devis.html">ci scriva le tre risposte del
test</a>: Le diciamo quale dei tre livelli fa al caso Suo, anche quando la
risposta è il meno caro.</p>
""",
  "faq": [
    ("Una landing page basta per essere visibili su Google?",
     "Sì per una ricerca principale, no per diverse. Google classifica "
     "pagine: una pagina unica si posiziona bene su un tema, ma non può "
     "coprire « mestiere + città » e tre prestazioni distinte."),
    ("Si possono aggiungere pagine più tardi?",
     "Sì, se il sito è stato costruito per questo. È il percorso più "
     "frequente: cominciare con una pagina, osservare per tre mesi da dove "
     "arrivano le chiamate, poi aggiungere le pagine utili."),
  ],
 },

 {
  "slug": "fiche-google-business.html",
  "cat": "Visibilità",
  "titre": "Scheda Google Business: l'impostazione che quasi tutte le PMI sbagliano",
  "h1": ["Scheda Google Business:", "l'impostazione che tutti sbagliano."],
  "desc": "La categoria principale decide metà della Sua visibilità locale. "
          "E quasi nessuno la sceglie correttamente.",
  "dek": "Per una PMI locale, la scheda Google pesa spesso più del sito "
         "stesso. Un solo campo vi decide l'essenziale.",
  "lecture": "6 min",
  "corps": """
<p>Se serve clienti in un raggio di trenta chilometri, la Sua scheda
Google Business Le porta probabilmente più chiamate del Suo sito. È lei
che appare nel blocco della mappa, in alto, prima dei risultati classici —
ed è gratuita.</p>

<p>C'è un campo in questa scheda che pesa più di tutti gli altri, e che la
maggior parte delle PMI svizzere compila di traverso: la
<strong>categoria principale</strong>.</p>

<h2>L'impostazione sbagliata</h2>

<p>Google Le chiede una categoria principale e autorizza categorie
secondarie. Quasi tutti scelgono la categoria principale nel modo più
naturale — quella che descrive il mestiere in senso ampio — ed è
esattamente l'errore.</p>

<p>La categoria principale è ciò che determina <em>per quali ricerche</em>
Google prende in considerazione di mostrarLa. Le secondarie hanno solo un
peso marginale. Quindi:</p>

<ul>
  <li>Se è falegname ma l'80% del Suo fatturato viene dalle cucine su
  misura, la categoria principale deve essere quella delle cucine, non
  «Falegname».</li>
  <li>Se è fisioterapista specializzato nello sport, la categoria sport
  passa in principale.</li>
  <li>Se è fiduciario ma vende soprattutto dichiarazioni d'imposta ai
  privati, scelga la categoria fiscale.</li>
</ul>

<p>Il metodo giusto è meccanico: digiti su Google la ricerca che vuole
vincere, guardi le tre schede che escono nel blocco della mappa, le apra,
legga la loro categoria principale. Prenda la stessa. Non deve indovinare
che cosa Google associa a che cosa: glielo mostra.</p>

<h2>I campi che spostano davvero la classifica</h2>

<p>La classifica locale poggia su tre pilastri — la pertinenza, la
distanza e la notorietà. Sulla distanza non può agire. Restano i campi
seguenti, in ordine di effetto osservato:</p>

<ol>
  <li><strong>La categoria principale</strong>, l'abbiamo appena visto.</li>
  <li><strong>Il nome esatto dell'attività.</strong> Metta il nome reale,
  quello che figura sulla Sua vetrina e sulle Sue fatture. Aggiungervi
  parole chiave («Dupont Idraulica Lugano Pronto Intervento 24h») è
  contrario alle regole di Google ed espone a una sospensione.</li>
  <li><strong>Le prestazioni.</strong> Campo poco sfruttato: vi si possono
  elencare le proprie prestazioni una per una, con una descrizione. Ogni
  voce è una parola chiave in più, e questa è legittima.</li>
  <li><strong>La zona servita.</strong> Se si sposta, dichiari i comuni.
  Se riceve, dia un indirizzo e non ne dichiari.</li>
  <li><strong>Gli orari, compresi i giorni festivi.</strong> Google mostra
  «orari forse diversi» quando non sono confermati, e questo dubbio costa
  chiamate.</li>
  <li><strong>Il link del sito.</strong> Lo punti verso la pagina che
  parla della prestazione in questione, non sistematicamente verso la
  home.</li>
</ol>

<h2>Le foto: la regola del tre</h2>

<p>Le schede che convertono hanno come minimo: l'esterno con l'insegna
visibile (il cliente deve riconoscere il posto arrivando), l'interno, e il
lavoro finito. Ne aggiunga qualcuna al mese invece di trenta in una volta:
una scheda viva è trattata meglio di una scheda ferma.</p>

<p>Eviti le immagini di archivio. Si riconoscono, e tolgono precisamente
ciò che la scheda dovrebbe portare: la prova che esiste davvero in quel
posto.</p>

<h2>Le recensioni, senza elemosinarle</h2>

<p>Il numero di recensioni e la loro regolarità contano più della media
dei voti. Una scheda a 4,6 con una recensione al mese passa davanti a una
scheda a 5,0 ferma da due anni.</p>

<p>Ciò che funziona, nell'ordine: chiedere al momento giusto (subito dopo
la fine del lavoro, mai con un sollecito collettivo), dare il link breve
di richiesta di recensione che Google genera nel Suo pannello, e
<strong>rispondere a tutte le recensioni</strong>, comprese quelle
negative, in due righe e senza giustificarsi. Le risposte sono lette dai
potenziali clienti molto più che dagli autori.</p>

<p>Ciò che non funziona: comprare recensioni (viene rilevato, e sanzionato
con la rimozione della scheda), chiederne in cambio di uno sconto
(vietato), o installare un tablet al banco che raccoglie dieci recensioni
dallo stesso indirizzo IP.</p>

<h2>Ciò che fa crollare una scheda</h2>

<ul>
  <li>Un indirizzo o un numero diverso da quello del sito. Faccia in modo
  che nome, indirizzo e telefono siano rigorosamente identici ovunque:
  scheda, sito, elenchi, social.</li>
  <li>Parole chiave ammassate nel nome dell'attività.</li>
  <li>Un indirizzo di domicilio dichiarato come negozio mentre non riceve
  nessuno.</li>
  <li>Due schede per la stessa attività — succede dopo un cambio di
  ragione sociale, e taglia in due la Sua notorietà.</li>
  <li>Il silenzio. Una scheda che non si tocca mai perde terreno su una
  scheda curata.</li>
</ul>

<h2>E il sito, allora?</h2>

<p>La scheda porta la chiamata; il sito fa la vendita. I potenziali
clienti che esitano aprono il Suo sito dalla scheda: se non esiste, o se è
datato, perde una parte di ciò che la scheda Le ha portato. I due
lavorano insieme, e la cosa più redditizia è far corrispondere la
prestazione di punta della scheda con una pagina dedicata del sito.</p>

<p>È ciò che copre <a href="../index.html#methode">Il Metodo Cliente
Locale</a>, la guida che consegniamo con il
<a href="../offres/ultimate-website.html">Site Complet</a>: la scheda
Google, le ricerche «mestiere + città», e il modo di farsi citare da
ChatGPT quando qualcuno cerca il Suo mestiere vicino a casa.</p>
""",
  "faq": [
    ("Quale categoria principale scegliere su Google Business?",
     "Quella della Sua prestazione più redditizia, non quella del Suo "
     "mestiere in senso ampio. Metodo: digiti la ricerca che vuole vincere, "
     "apra le schede che escono nel blocco della mappa e riprenda la loro "
     "categoria principale."),
    ("Si possono aggiungere parole chiave al nome della propria attività?",
     "No. Le regole di Google impongono il nome reale dell'attività; "
     "aggiungere parole chiave espone alla sospensione della scheda."),
    ("La media dei voti conta più del numero di recensioni?",
     "No. La regolarità delle recensioni e le risposte date pesano più di "
     "un voto perfetto ottenuto due anni fa."),
  ],
 },

 {
  "slug": "que-mettre-sur-sa-page-d-accueil.html",
  "cat": "Redazione",
  "titre": "Che cosa scrivere sulla propria home page",
  "h1": ["Che cosa scrivere", "sulla propria home page."],
  "desc": "Cinque secondi per rispondere a tre domande. Il piano di una "
          "home page che fa squillare il telefono, sezione per sezione.",
  "dek": "Il Suo visitatore concede alla Sua home page il tempo di un "
         "semaforo rosso. Ecco l'ordine in cui vuole le risposte.",
  "lecture": "6 min",
  "corps": """
<p>Un visitatore che arriva sulla Sua home page si pone tre domande, in
quest'ordine: <strong>dove sono, è una cosa per me, e adesso che cosa
faccio?</strong> Le concede qualche secondo per tutte e tre. Tutto ciò
che non serve a queste risposte può scendere o sparire.</p>

<p>Ecco che cosa scriviamo, nell'ordine in cui lo scriviamo.</p>

<h2>1. La frase in alto</h2>

<p>Dice che cosa fa, per chi, e dove. Nient'altro. Non deve essere bella,
deve essere esatta.</p>

<ul>
  <li>✗ «L'eccellenza al servizio dei vostri progetti»</li>
  <li>✓ «Elettricista a Lugano, pronto intervento in giornata»</li>
  <li>✗ «Reinventiamo insieme la vostra comunicazione»</li>
  <li>✓ «Loghi e identità visive per le PMI svizzere, in due
  settimane»</li>
</ul>

<p>Test semplice: mostri la frase a qualcuno che non conosce il Suo
mestiere. Se non riesce a ripetere che cosa vende, va riscritta. E se il
Suo mestiere è locale, ci metta dentro la città: non è posizionamento, è
cortesia verso il visitatore.</p>

<h2>2. Il pulsante, subito</h2>

<p>Il primo invito all'azione si mette nella prima schermata, accanto alla
frase in alto. Certi visitatori hanno già deciso: non li faccia
scorrere.</p>

<p>Un'etichetta che dice che cosa succederà converte meglio di
un'etichetta vaga. «Chiedere un preventivo» invece di «Saperne di più».
«Prenotare un tavolo» invece di «Contatti». E un solo pulsante
principale: due pulsanti dello stesso peso sono una decisione in più da
prendere.</p>

<h2>3. Le tre ragioni per restare</h2>

<p>Appena sotto la prima schermata, tre argomenti brevi. Non dieci.
Rispondono a «è una cosa per me?» e devono essere
<strong>verificabili</strong>: un tempo, un prezzo, una zona, una
garanzia, una cifra che può dimostrare.</p>

<p>«Qualità, serietà, reattività» non dice nulla perché nessuno
scriverebbe il contrario. «Preventivo entro 24 ore, prezzo fisso,
interventi in Ticino» dice qualcosa.</p>

<h2>4. La prova</h2>

<p>È la sezione più trascurata e la più redditizia. In ordine di forza:
foto del Suo lavoro reale, recensioni con nome e cognome, loghi di
clienti, cifre.</p>

<p>Una regola che applichiamo a noi stessi: <strong>se non ce l'ha, non
se la inventi</strong>. Una recensione falsa si riconosce, e il giorno in
cui si riconosce si porta via tutto il resto. Quando inizia e non ha
ancora niente da mostrare, lo dica e sostituisca la prova con la
trasparenza: i Suoi prezzi, il Suo metodo, le Sue condizioni. Funziona
meglio di quanto si creda.</p>

<h2>5. Le obiezioni, prima che blocchino</h2>

<p>Il Suo visitatore ha due o tre ragioni per non scriverLe. «Sarà
sicuramente troppo caro.» «Ci vorranno mesi.» «Mi ritroverò
bloccato.» Le tratti esplicitamente, sulla pagina: un prezzo o una
fascia, un tempo, che cosa succede se le cose non vanno.</p>

<p>È controintuitivo scrivere un prezzo quando si crede che il prezzo
faccia scappare. Nei fatti, l'assenza di prezzo fa scappare di più: lascia
il visitatore immaginare il peggio e andarsene da chi lo espone. È per
questo che <a href="../index.html#tarifs">i nostri tre prezzi sono
pubblici</a>.</p>

<h2>6. Il richiamo all'azione</h2>

<p>Ripeta l'invito all'azione in basso, e ne dia due forme: un modulo per
chi scrive, un numero o un WhatsApp per chi preferisce parlare. Aggiunga
che cosa fa della richiesta: «rispondiamo in giornata, dal lunedì al
venerdì». Il visitatore vuole sapere in che cosa si impegna.</p>

<h2>Che cosa togliere</h2>

<ul>
  <li><strong>La parola «Benvenuti».</strong> Occupa la riga più letta
  della pagina per non dire nulla.</li>
  <li><strong>La storia dell'azienda, in alto.</strong> Interessa, ma
  dopo. Il suo posto è una pagina «chi siamo».</li>
  <li><strong>Il carosello che scorre da solo.</strong> Nessuno vede la
  terza immagine, e rallenta la pagina.</li>
  <li><strong>Le immagini di archivio.</strong> Una foto del Suo
  laboratorio fatta col telefono vale più di un ufficio americano da
  catalogo.</li>
  <li><strong>I paragrafi lunghi.</strong> Due o tre frasi, mai di più, e
  sottotitoli che si leggono da soli.</li>
</ul>

<h2>Il test finale</h2>

<p>Faccia leggere la Sua home page su un telefono a una persona esterna,
cronometro alla mano, per cinque secondi. Poi le chieda che cosa vende, a
chi, e che cosa farebbe per contattarLa. Se escono tutte e tre le
risposte, la pagina è buona. Altrimenti non è il design da cambiare, è
l'ordine delle sezioni.</p>

<p>Poniamo queste domande nel nostro <a href="../brief.html">briefing
iniziale</a>: è la parte che prende più tempo ai clienti, e quella che fa
tutta la differenza sul risultato.</p>
""",
  "faq": [
    ("Bisogna mostrare i propri prezzi sul sito?",
     "Nella grande maggioranza dei casi sì — almeno una fascia. L'assenza "
     "di prezzo fa andare il visitatore verso un concorrente che lo mostra, "
     "e fa perdere tempo con richieste fuori budget."),
    ("Qual è la prima cosa da scrivere su una home page?",
     "Una frase che dice che cosa fa, per chi e dove. Se una persona "
     "estranea al Suo mestiere non riesce a ripeterla, va riscritta."),
  ],
 },

 {
  "slug": "wix-squarespace-ou-sur-mesure.html",
  "cat": "Confronto",
  "titre": "Wix, Squarespace o su misura: il confronto onesto",
  "h1": ["Wix, Squarespace", "o su misura?"],
  "desc": "Ciò che ogni soluzione fa molto bene, dove ciascuna si inceppa, "
          "e il costo reale su tre anni per una PMI svizzera.",
  "dek": "Siamo giudici e parte in causa: vendiamo su misura. Ragione in "
         "più per dire con precisione in quali casi i costruttori online "
         "sono la scelta giusta.",
  "lecture": "7 min",
  "corps": """
<p>Tanto vale dirlo subito: vendiamo siti fatti a mano. Un confronto
scritto da noi non è quindi neutro. Proveremo comunque a essere esatti,
perché ci sono casi veri in cui un costruttore online è la decisione
migliore, e in cui da noi perderebbe i Suoi soldi.</p>

<h2>Ciò che Wix fa molto bene</h2>

<ul>
  <li><strong>Cominciare oggi senza nessuno.</strong> Può avere un sito
  online nel pomeriggio, da solo, senza competenze.</li>
  <li><strong>Tutto nello stesso posto.</strong> Dominio, hosting,
  certificato, moduli, negozio, prenotazione, newsletter: una sola
  fattura, una sola password.</li>
  <li><strong>Modificare da sé, davvero.</strong> L'editor è molto
  permissivo: si sposta un elemento dove si vuole.</li>
  <li><strong>Le funzioni di mestiere.</strong> Presa di appuntamenti,
  calendario dei corsi, prenotazione: disponibili in pochi clic, mentre
  risvilupparle costerebbe migliaia di franchi.</li>
</ul>

<h2>Ciò che Squarespace fa molto bene</h2>

<ul>
  <li><strong>Il risultato visivo di default.</strong> I modelli sono più
  curati e più difficili da rovinare. Per un fotografo, un architetto, un
  ristorante, la resa è buona senza direzione artistica.</li>
  <li><strong>La coerenza.</strong> Il sistema di stili globale evita il
  sito che parte in dodici direzioni dopo sei mesi.</li>
  <li><strong>La vendita di piccoli cataloghi.</strong> Una ventina di
  prodotti o qualche prestazione: è pulito e sufficiente.</li>
</ul>

<h2>Dove entrambi si inceppano</h2>

<p><strong>La velocità.</strong> Queste piattaforme caricano molto codice
per restare modificabili nel browser. Su un telefono in 4G si vede. La
velocità è un criterio di classificazione per Google, e soprattutto un
criterio di abbandono: il visitatore chiude prima di aver visto la Sua
offerta.</p>

<p><strong>L'uscita.</strong> È il punto più serio e il meno discusso. Non
può portarsi via il Suo sito: in genere si recuperano i testi, le immagini
e il nome a dominio, ma non l'impaginazione. Cambiare piattaforma
significa rifare. L'abbonamento non è quindi soltanto un affitto, è un
costo di uscita che cresce con il tempo.</p>

<p><strong>Il posizionamento fine.</strong> L'essenziale è accessibile
(titoli, descrizioni, indirizzi delle pagine). Ciò che lo è meno: il
controllo preciso del codice, dei dati strutturati avanzati, della
gestione del multilingue. Per un sito locale va bene. Per una strategia di
contenuti ambiziosa, frena.</p>

<p><strong>Il multilingue.</strong> Possibile, ma è spesso la parte più
faticosa — e in Svizzera è raramente facoltativo.</p>

<p><strong>Il prezzo che sale.</strong> La tariffa d'ingresso non
comprende quasi mai ciò che Le serve. Le funzioni utili (negozio,
prenotazione, rimozione della pubblicità, indirizzi e-mail) sono su
livelli superiori, e i livelli aumentano con gli anni.</p>

<h2>Ciò che il su misura fa molto bene</h2>

<ul>
  <li><strong>La velocità.</strong> Un sito statico ben costruito si carica
  quasi istantaneamente e non ha bisogno di alcuna manutenzione
  tecnica.</li>
  <li><strong>AppartenerLe.</strong> I file sono Suoi, presso l'hoster che
  vuole, e trasferibili altrove.</li>
  <li><strong>Dire esattamente ciò che vuole dire.</strong> Nessun modello
  da aggirare.</li>
  <li><strong>Il costo di funzionamento.</strong> Spesso il prezzo del
  dominio, e nient'altro.</li>
</ul>

<p>E i suoi limiti, che sono reali: dipende da qualcuno per le modifiche
pesanti, serve un briefing all'inizio, e le funzionalità di mestiere
(prenotazione, agenda, negozio) sono un budget separato invece di essere
incluse.</p>

<h2>Il costo reale su tre anni</h2>

<p>Come ordine di grandezza, per una PMI svizzera, ai prezzi rilevati nel
2026 — le tariffe delle piattaforme evolvono, le verifichi:</p>

<ul>
  <li><strong>Costruttore online, formula adatta a un'azienda</strong> —
  attorno a CHF 20 a 35 al mese, ossia <strong>CHF 720 a 1 260 su tre
  anni</strong>, più il Suo tempo di realizzazione, più i livelli
  superiori se aggiunge il negozio o le e-mail.</li>
  <li><strong>Pacchetto fatto a mano</strong> — CHF 290 a 690 una volta,
  più una decina di franchi di dominio all'anno, ossia <strong>CHF 320 a
  720 su tre anni</strong>.</li>
  <li><strong>Su misura d'agenzia</strong> — CHF 5 000 e più, giustificato
  quando il sito è un canale di vendita principale.</li>
</ul>

<p>Su tre anni la differenza tra un abbonamento e un pacchetto è quindi
piccola; su sei anni si rovescia nettamente. Ciò che decide non è il
prezzo: è la proprietà e la velocità.</p>

<h2>Come scegliere, in tre casi</h2>

<p><strong>Prenda un costruttore online</strong> se ha bisogno subito di
una prenotazione o di un'agenda, se prevede di modificare il Suo sito ogni
settimana da solo, o se sta testando un'attività di cui non sa ancora se
reggerà.</p>

<p><strong>Prenda un pacchetto fatto a mano</strong> se il Suo sito deve
soprattutto convincere e far squillare il telefono, se non vuole
abbonamenti, o se la Sua visibilità locale conta più della libertà di
spostare tutto.</p>

<p><strong>Prenda un'agenzia</strong> se il Suo sito è il canale di
vendita principale e un punto di conversione guadagnato si conta in
decine di migliaia di franchi.</p>

<h2>Una cosa da fare in ogni caso</h2>

<p>Compri il Suo nome a dominio a Suo nome, su un account che Le
appartiene, qualunque sia la soluzione scelta. È l'unico elemento
insostituibile: un sito si rifà, un indirizzo che ha dieci anni di storia
no. Se oggi il Suo dominio è intestato a un fornitore,
<a href="recuperer-son-nom-de-domaine.html">ecco come recuperarlo</a>.</p>

<p>E se vuole sapere in quale caso ricade, <a
href="../devis.html">ci descriva la Sua situazione in tre righe</a>: glielo
diciamo, anche quando la risposta è «prenda un abbonamento, Le
basterà».</p>
""",
  "faq": [
    ("Si può recuperare il proprio sito lasciando Wix o Squarespace?",
     "Si recuperano i testi, le immagini e il nome a dominio, ma non "
     "l'impaginazione: cambiare piattaforma implica rifare il sito."),
    ("Un sito su misura è più rapido di un sito Wix?",
     "In genere sì: un sito statico fatto a mano carica molto meno codice, "
     "perché non deve restare modificabile in un editor online."),
    ("Quale soluzione costa meno su tre anni?",
     "Un pacchetto unico con un semplice nome a dominio da mantenere resta "
     "generalmente sotto il totale di un abbonamento mensile su tre anni, e "
     "la differenza si allarga in seguito."),
  ],
 },

 {
  "slug": "sept-sections-landing-page.html",
  "cat": "Conversione",
  "titre": "Le 7 sezioni di una landing page che converte",
  "h1": ["Le sette sezioni", "di una pagina che converte."],
  "desc": "L'ordine che funziona, sezione per sezione, con ciò che va "
          "scritto in ognuna e l'errore da non commettervi.",
  "dek": "Una pagina che converte non è una pagina che persuade. È una "
         "pagina che risponde alle obiezioni nell'ordine in cui arrivano.",
  "lecture": "6 min",
  "corps": """
<p>Una pagina unica il cui solo scopo è far compiere un gesto —
telefonare, prenotare, compilare un modulo — segue quasi sempre lo stesso
piano. Non per pigrizia, ma perché le obiezioni di un visitatore arrivano
in un ordine abbastanza stabile.</p>

<p>Ecco le sette sezioni, l'obiezione che ciascuna tratta, e l'errore che
vediamo più spesso.</p>

<h2>1. L'apertura</h2>

<p><em>Obiezione trattata: «sono nel posto giusto?»</em></p>

<p>Che cosa fa, per chi, dove, e un pulsante. Una frase, un sottotitolo di
una riga, un invito all'azione. È tutto ciò che dovrebbe stare nella prima
schermata di un telefono.</p>

<p><strong>L'errore:</strong> una frase d'atmosfera («Diamo vita alle
vostre idee») che obbliga il visitatore a scorrere per capire il Suo
mestiere. Lui non scorre: se ne va.</p>

<h2>2. I tre punti d'appoggio</h2>

<p><em>Obiezione trattata: «perché voi?»</em></p>

<p>Tre argomenti verificabili, brevi, allineati. Un tempo, un prezzo, una
zona, una garanzia. Tre, perché due sembra poco e cinque non si legge
più.</p>

<p><strong>L'errore:</strong> qualità che nessuno rivendicherebbe al
contrario. «Serietà, qualità, ascolto» non è un argomento, è un
minimo.</p>

<h2>3. La prova</h2>

<p><em>Obiezione trattata: «funziona davvero?»</em></p>

<p>Foto di lavori reali, recensioni firmate, loghi, cifre. La metta
presto — subito dopo i punti d'appoggio — perché è lei che autorizza il
visitatore a leggere il seguito.</p>

<p><strong>L'errore:</strong> inventare. Una recensione fabbricata si
riconosce dal vocabolario, e distrugge la credibilità di tutta la pagina.
Se sta iniziando, sostituisca la prova con la trasparenza: metodo, prezzi,
condizioni. Facciamo esattamente questo su questo sito: le nostre
<a href="../temoignages.html">recensioni</a> sono quelle che abbiamo, e non
una di più.</p>

<h2>4. Il come</h2>

<p><em>Obiezione trattata: «in che cosa mi impegno?»</em></p>

<p>Tre o quattro tappe numerate: che cosa fa Lei, che cosa fa il cliente,
quanto tempo ci vuole. Questa sezione rassicura enormemente per un costo
di redazione quasi nullo, ed è quella più spesso dimenticata.</p>

<p><strong>L'errore:</strong> descrivere il proprio processo interno. Il
visitatore vuole sapere che cosa succederà a lui, non come Lei organizza
le Sue pratiche.</p>

<h2>5. Il prezzo</h2>

<p><em>Obiezione trattata: «rientra nel mio budget?»</em></p>

<p>Un prezzo, una fascia, o quantomeno un punto di riferimento («a partire
da», «la maggior parte dei nostri cantieri è tra X e Y»). Dica anche che
cosa è compreso e che cosa non lo è.</p>

<p><strong>L'errore:</strong> «preventivo su richiesta». Il visitatore non
chiede: suppone che sia caro e va a vedere altrove. E Lei riceve richieste
fuori budget che Le costano tempo. I nostri
<a href="../index.html#tarifs">tre prezzi</a> sono pubblici per questa
sola ragione.</p>

<h2>6. Le obiezioni rimaste</h2>

<p><em>Obiezione trattata: «sì, ma se…»</em></p>

<p>Una piccola FAQ di quattro a sei domande, che riprende ciò che Le
viene chiesto davvero al telefono. Scriva le vere domande, comprese quelle
scomode: «e se non sono soddisfatto?», «di chi è la proprietà del
sito?», «che cosa succede se sparite?».</p>

<p><strong>L'errore:</strong> una FAQ di comodo che pone domande la cui
risposta Le fa comodo. Non tratta nessun freno e occupa spazio.</p>

<h2>7. L'ultima azione</h2>

<p><em>Obiezione trattata: «adesso che cosa faccio?»</em></p>

<p>Lo stesso invito all'azione che in alto, con due canali: un modulo
breve e un modo per parlare con qualcuno. Precisi il tempo di risposta. E
tenga il modulo breve: ogni campo in più fa perdere invii. Nome, recapito,
due righe di messaggio bastano quasi sempre.</p>

<p><strong>L'errore:</strong> un modulo di dodici campi che chiede il
fatturato e il numero di dipendenti ancora prima del primo scambio.</p>

<h2>Ciò che conta più dell'ordine</h2>

<ul>
  <li><strong>La velocità.</strong> Una pagina lenta perde visitatori prima
  della sezione 2. È la prima cosa da correggere, prima di qualsiasi
  riscrittura.</li>
  <li><strong>Il telefono prima di tutto.</strong> La maggior parte dei
  Suoi visitatori è su mobile. Progetti per lo schermo del telefono,
  verifichi poi sul computer.</li>
  <li><strong>Un solo gesto.</strong> Una pagina che propone di
  telefonare, scrivere, iscriversi, scaricare e seguire su Instagram non
  fa compiere proprio nulla.</li>
</ul>

<p>È questo il piano che applichiamo sulla
<a href="../offres/pro-landing-page.html">Landing Pro</a>: cinque sezioni
come minimo, sette quando il contenuto lo giustifica, e mai due pulsanti
principali che si contendono la stessa pagina.</p>
""",
  "faq": [
    ("Quante sezioni servono su una landing page?",
     "Cinque come minimo, sette quando il contenuto lo giustifica. Ciò che "
     "conta è che ogni sezione tratti un'obiezione reale, nell'ordine in cui "
     "si presenta."),
    ("Quanti campi mettere nel modulo?",
     "Il meno possibile: un nome, un recapito e due righe di messaggio "
     "bastano quasi sempre. Ogni campo in più fa perdere invii."),
  ],
 },

 {
  "slug": "photos-professionnelles-site-web.html",
  "cat": "Fotografia",
  "titre": "Foto: quando un servizio professionale cambia davvero qualcosa",
  "h1": ["Foto: quando un servizio", "cambia davvero qualcosa."],
  "desc": "I tre casi in cui un servizio fotografico è redditizio, i tre in "
          "cui non lo è, e il briefing da dare al fotografo.",
  "dek": "Un servizio costa tra CHF 400 e CHF 1 500 in Svizzera. A volte è "
         "il miglior franco speso del progetto, a volte è un franco "
         "perso.",
  "lecture": "5 min",
  "corps": """
<p>La foto è la voce su cui si esita di più, perché è visibile e non è
indispensabile. Un servizio professionale si negozia, in Svizzera, tra
CHF 400 per una mezza giornata con un giovane fotografo e CHF 1 500 per
una giornata intera con ritocchi. Ecco come sapere se è il Suo caso.</p>

<h2>Che cosa cambia davvero la foto</h2>

<p>Non rende migliore la Sua offerta. Fa due cose: <strong>prova che
esiste</strong>, e <strong>mostra il livello di finitura</strong> del Suo
lavoro. È tutto — e a seconda dei mestieri è enorme o trascurabile.</p>

<h2>I tre casi in cui un servizio è redditizio</h2>

<p><strong>1. Il Suo lavoro si vede.</strong> Parrucchieri, cucina,
falegnameria, arredamento, carrozzeria, estetica, giardinaggio, fiori. La
foto <em>è</em> l'argomento di vendita. Qui delle brutte foto costano più
di nessuna foto, e un servizio è il primo investimento da fare, ancora
prima del sito.</p>

<p><strong>2. Si compra una persona.</strong> Terapista, avvocato, coach,
broker, notaio, medico. Un ritratto corretto — sguardo in camera, luce
morbida, sfondo neutro — aumenta nettamente il tasso di presa di contatto.
Non serve una giornata: un'ora basta, ed è il miglior rapporto
qualità-prezzo di tutto l'elenco.</p>

<p><strong>3. Il Suo locale è un argomento.</strong> Ristorante, albergo,
salone, studio, negozio. Il cliente vuole vedere dove mette piede. Qui il
servizio va fatto nell'ora in cui il locale è più bello, il che presuppone
di bloccare una fascia oraria.</p>

<h2>I tre casi in cui non è la priorità</h2>

<p><strong>1. Il Suo lavoro è invisibile.</strong> Informatica,
contabilità, consulenza, assicurazioni, traduzione. Fotografare persone
che sorridono davanti a un computer non aggiunge nulla. Metta i soldi nel
testo, nelle referenze dei clienti e nella scheda Google.</p>

<p><strong>2. Vende un prodotto che il fabbricante ha già
fotografato.</strong> Usi le sue immagini: sono spesso migliori e già
fornite, verifichi semplicemente di avere il diritto di usarle.</p>

<p><strong>3. Non sa ancora che cosa vende.</strong> Se la Sua offerta
cambierà tra sei mesi, cambieranno anche le foto. Cominci col telefono:
farà il servizio quando l'offerta sarà stabile.</p>

<h2>Che cosa fa molto bene un telefono</h2>

<p>Un telefono recente, all'ora giusta, dà ottimi risultati. Bastano tre
regole:</p>

<ul>
  <li><strong>La luce del giorno, mai il flash.</strong> Metta il soggetto
  di fronte a una finestra, non di spalle. All'aperto eviti il pieno sole
  di mezzogiorno: la fine della giornata è più generosa.</li>
  <li><strong>Pulisca l'inquadratura.</strong> Il cavo che penzola, il
  cartone, il bidone. Pulire lo sfondo fa più per una foto di qualsiasi
  filtro.</li>
  <li><strong>Inquadri largo e orizzontale.</strong> Si ritaglia sempre in
  meno, mai in più. Una foto verticale non entra in una fascia d'apertura
  di un sito.</li>
</ul>

<p>Conservi i file originali: uno screenshot di una foto, o un'immagine
che ha fatto tre volte il giro di WhatsApp, arriva irrecuperabile.</p>

<h2>Il briefing da dare al fotografo</h2>

<p>La differenza tra un servizio utile e un servizio carino sta in ciò che
si chiede prima. Bastano sei righe:</p>

<ol>
  <li>A che cosa serviranno le immagini — sito, scheda Google, social — e
  in quali formati.</li>
  <li>Tre immagini obbligatorie (per esempio: la facciata con l'insegna
  leggibile, il team, un lavoro terminato).</li>
  <li>Un'<strong>immagine molto larga e orizzontale</strong> per la parte
  alta della home page, con dello spazio vuoto su un lato: è lì che si
  poserà il testo.</li>
  <li>Lo stile: due o tre esempi di siti che Le piacciono valgono più di
  una pagina di aggettivi.</li>
  <li>I diritti: uso web illimitato nel tempo, e per iscritto.</li>
  <li>La consegna: file originali a piena risoluzione, più una versione
  alleggerita per il web.</li>
</ol>

<p>Quest'ultimo punto conta: immagini da 8 MB consegnate così come sono su
un sito lo rendono lento, e un sito lento perde visitatori.
Ridimensioniamo e comprimiamo sistematicamente ciò che i nostri clienti ci
inviano, ma tanto vale partire dai file giusti.</p>

<h2>Quanto dedicarvi</h2>

<ul>
  <li><strong>Ritratto da solo</strong> — CHF 150 a 400 per un'ora. Da
  fare non appena il Suo volto è la Sua offerta.</li>
  <li><strong>Mezza giornata sul posto</strong> — CHF 400 a 800. Basta per
  un negozio, un salone, uno studio.</li>
  <li><strong>Giornata intera</strong> — CHF 900 a 1 500. Giustificata
  quando bisogna coprire più prestazioni o più luoghi.</li>
</ul>

<p>Un riferimento utile: se il Suo sito costa CHF 500 e le Sue foto
CHF 1 200, non è assurdo — nei mestieri visivi la foto lavora più
dell'impaginazione. Il contrario a volte lo è di più.</p>

<p>Se anche la Sua identità visiva è da rivedere allo stesso tempo (logo,
colori, declinazioni), è il momento giusto: è l'oggetto del
<a href="../upsell-branding.html">Pacchetto Branding</a>, ed evita di
fotografare un'insegna che cambierà tre mesi dopo.</p>
""",
  "faq": [
    ("Un servizio fotografico professionale è indispensabile?",
     "No. È determinante nei mestieri in cui il lavoro si vede "
     "(parrucchieri, cucina, arredamento) e in quelli in cui si compra una "
     "persona. È secondario per i servizi immateriali."),
    ("Quanto costa un servizio fotografico in Svizzera?",
     "Da CHF 150 a 400 per un ritratto di un'ora, CHF 400 a 800 per una "
     "mezza giornata sul posto, CHF 900 a 1 500 per una giornata intera con "
     "ritocchi."),
  ],
 },

 {
  "slug": "premier-client-via-son-site.html",
  "cat": "Attese",
  "titre": "Quanto tempo prima del primo cliente tramite il sito?",
  "h1": ["Quanto tempo prima", "del primo cliente?"],
  "desc": "Che cosa succede settimana dopo settimana dopo una pubblicazione, "
          "le tre fonti di traffico e la loro rispettiva velocità.",
  "dek": "Un sito non è un interruttore. Secondo la fonte di traffico che "
         "attiva, il primo cliente arriva in tre giorni o in cinque mesi.",
  "lecture": "6 min",
  "corps": """
<p>È la domanda che ci viene posta subito dopo il prezzo, e la risposta
onesta è: non dipende quasi dal sito. Dipende dal modo in cui le persone
ci arrivano. Ci sono tre strade, e non hanno affatto la stessa
velocità.</p>

<h2>Le tre fonti, e i loro tempi</h2>

<p><strong>Il traffico che porta Lei stesso — immediato.</strong> Mette
l'indirizzo nella firma delle e-mail, sui preventivi, sul veicolo, nella
bio Instagram, e lo manda ai Suoi contatti. Primo effetto in qualche
giorno. È la fonte più sottovalutata e l'unica che sia gratuita e
istantanea.</p>

<p><strong>La pubblicità — qualche giorno.</strong> Google Ads, Meta, e
ormai gli annunci negli assistenti tipo ChatGPT. Paga, e ha visitatori
domani. È l'unico modo per avere volume subito, e si ferma il giorno in
cui smette di pagare.</p>

<p><strong>Il posizionamento naturale — da due a sei mesi.</strong> Google
deve scoprire le Sue pagine, valutarle, poi farLa salire. Per una ricerca
locale poco concorrenziale («fabbro Lugano»), conti da sei a dieci
settimane. Per una ricerca contesa, sei mesi e più. Nessun fornitore serio
Le prometterà di meglio.</p>

<h2>Che cosa succede, settimana per settimana</h2>

<p><strong>Settimane 1 e 2.</strong> Il sito è online. I Suoi visitatori
sono quelli che porta Lei: conoscenti, clienti esistenti, contatti. Le
prime richieste vengono spesso da clienti che aveva già — scoprono una
prestazione che ignoravano. È un guadagno vero, e nessuno lo conta.</p>

<p><strong>Settimane da 3 a 6.</strong> Google ha indicizzato le pagine.
Comincia ad apparire sul Suo stesso nome, poi su ricerche molto precise.
Il volume è basso ma la qualità è alta: chi digita «riparazione tapparelle
Massagno» La chiama quasi sempre.</p>

<p><strong>Mesi 2 e 3.</strong> Se la Sua scheda Google Business è ben
impostata, diventa la Sua prima fonte di chiamate, davanti al sito. I due
lavorano insieme: la scheda porta, il sito convince. È il momento in cui
si vede se le pagine dicono le cose giuste.</p>

<p><strong>Mesi da 4 a 6.</strong> Il posizionamento delle pagine di
prestazione si mette in moto. Se ha pubblicato un po' di contenuti e
raccolto qualche recensione, la curva si raddrizza nettamente. È anche il
momento in cui si sa quali pagine aggiungere: glielo hanno detto le
richieste.</p>

<h2>Che cosa accelera davvero</h2>

<ul>
  <li><strong>Una scheda Google Business completa.</strong> Effetto in
  qualche giorno e gratuito. È la leva n°1 per una PMI locale —
  <a href="fiche-google-business.html">l'impostazione da non
  sbagliare</a>.</li>
  <li><strong>Mettere l'indirizzo ovunque.</strong> Firma, preventivi,
  fatture, veicolo, vetrina, social. Non costa nulla e spesso raddoppia il
  traffico del primo mese.</li>
  <li><strong>Una pagina per prestazione.</strong> Cinque pagine precise si
  posizionano molto meglio di una pagina che parla di tutto.</li>
  <li><strong>Le recensioni, con regolarità.</strong> Una al mese vale più
  di dieci in una volta.</li>
  <li><strong>Un piccolo budget pubblicitario all'avvio.</strong> CHF 200 a
  500 su tre settimane bastano per sapere se la Sua pagina converte, che è
  un'informazione che non si ottiene altrimenti.</li>
</ul>

<h2>Che cosa rallenta</h2>

<ul>
  <li><strong>Un sito lento.</strong> I visitatori se ne vanno prima di
  leggere l'offerta; ne soffre anche il posizionamento.</li>
  <li><strong>Niente prezzi, niente zona, niente tempi.</strong> Il
  visitatore non chiede, suppone, e se ne va.</li>
  <li><strong>Aspettare di avere tutto.</strong> Un sito online che si
  completa batte un sito perfetto tra sei mesi.</li>
  <li><strong>Cambiare nome a dominio.</strong> Riparte da zero. Lo scelga
  una volta e lo tenga.</li>
</ul>

<h2>Che cosa misurare</h2>

<p>Tre cifre, una volta al mese, dieci minuti:</p>

<ol>
  <li><strong>Quanti visitatori</strong>, e da dove vengono (ricerca,
  social, diretto).</li>
  <li><strong>Quante richieste</strong> — moduli, chiamate, WhatsApp.</li>
  <li><strong>Quanti clienti</strong> nati da queste richieste.</li>
</ol>

<p>Il rapporto tra la prima e la seconda cifra giudica la Sua pagina. Il
rapporto tra la seconda e la terza giudica la Sua offerta e il Suo modo di
rispondere. Due problemi diversi: non corregga il sito quando è il
preventivo a fare problema.</p>

<h2>Un riferimento onesto</h2>

<p>Per una PMI locale svizzera con una scheda Google impostata
correttamente, un sito chiaro e l'indirizzo messo ovunque: <strong>le prime
richieste arrivano in genere entro due o quattro settimane</strong>, e il
sito diventa una fonte regolare attorno al terzo o sesto mese. Senza
scheda Google, senza recensioni e senza indirizzo diffuso, può volerci
molto di più — e allora non è un problema di sito.</p>

<p>Se vuole il piano dei primi trenta giorni dopo la pubblicazione, fa
parte de <a href="../index.html#methode">Il Metodo Cliente Locale</a> che
consegniamo con il
<a href="../offres/ultimate-website.html">Site Complet</a>.</p>
""",
  "faq": [
    ("Quanto tempo per essere visibili su Google dopo una pubblicazione?",
     "Qualche giorno per essere indicizzati, da sei a dieci settimane per "
     "posizionarsi su una ricerca locale poco concorrenziale, sei mesi e più "
     "su una ricerca contesa."),
    ("Quando arriva la prima richiesta tramite un sito?",
     "In genere entro due o quattro settimane per una PMI locale che diffonde "
     "il proprio indirizzo e dispone di una scheda Google Business impostata "
     "correttamente."),
  ],
 },

 {
  "slug": "recuperer-son-nom-de-domaine.html",
  "cat": "Pratica",
  "titre": "Recuperare il proprio nome a dominio in cinque tappe",
  "h1": ["Recuperare il nome", "a dominio in cinque tappe."],
  "desc": "Il Suo dominio è intestato al Suo vecchio fornitore? Ecco la "
          "procedura esatta, e che cosa fare se non risponde più.",
  "dek": "Il nome a dominio è l'unico elemento della Sua presenza online "
         "che non si rifà. Se non è a Suo nome, è la prima cosa da "
         "correggere.",
  "lecture": "6 min",
  "corps": """
<p>Un sito si ricostruisce. Un nome a dominio che ha otto anni di storia,
link in entrata e i Suoi indirizzi e-mail, no. È per questo che compriamo
sempre il dominio a nome del cliente e che le nostre
<a href="../legal/conditions.html">condizioni generali</a> prevedono il suo
trasferimento su semplice richiesta e senza spese.</p>

<p>Non tutti i fornitori funzionano così. Se il Suo detiene il Suo
dominio, ecco come procedere.</p>

<h2>Tappa 1 — Sapere dov'è e di chi è</h2>

<p>Due cose da distinguere: il <strong>titolare</strong> (il proprietario
legale) e il <strong>registrar</strong> (l'azienda presso cui il dominio è
registrato).</p>

<p>Per un <code>.ch</code>, l'elenco pubblico del registro svizzero
(<em>whois</em> di SWITCH, via nic.ch) Le dà il registrar. Per un
<code>.com</code>, la ricerca whois dell'ICANN. I recapiti del titolare
sono spesso nascosti per ragioni di protezione dei dati, ma il registrar è
sempre visibile — ed è ciò di cui ha bisogno.</p>

<p>Annoti anche la <strong>data di scadenza</strong>. Se è tra meno di
quindici giorni, tratti la pratica con urgenza: un dominio scaduto può
essere ricomprato da chiunque.</p>

<h2>Tappa 2 — Chiedere il trasferimento, per iscritto</h2>

<p>Scriva al fornitore un messaggio breve, fattuale, chiedendo
esplicitamente questi tre elementi:</p>

<ul>
  <li>il <strong>codice di autorizzazione al trasferimento</strong>
  (chiamato codice auth, codice EPP o <em>authcode</em>);</li>
  <li>lo <strong>sblocco</strong> del dominio (il <em>transfer
  lock</em>);</li>
  <li>il passaggio del titolare a Suo nome, se il dominio non è già a Suo
  nome.</li>
</ul>

<p>Fissi una scadenza ragionevole — dieci giorni lavorativi — e conservi
una traccia scritta. Nella grande maggioranza dei casi basta: la maggior
parte dei fornitori non ha alcuna voglia di tenere in ostaggio il dominio
di un cliente che se ne va.</p>

<h2>Tappa 3 — Aprire un conto presso un registrar, a Suo nome</h2>

<p>Crei il conto con il <strong>Suo</strong> indirizzo e-mail e la
<strong>Sua</strong> carta — è questo conto che farà di Lei il proprietario
per i prossimi dieci anni. Non usi un indirizzo che dipende dal dominio
che sta trasferendo: se il trasferimento va male, perde l'accesso alla Sua
casella insieme al dominio.</p>

<p>Per un <code>.ch</code>, un registrar svizzero semplifica la
fatturazione e l'assistenza in italiano. La tariffa corrente si aggira
attorno a una decina di franchi all'anno; la differenza di prezzo tra
registrar è trascurabile, la qualità dell'assistenza no.</p>

<h2>Tappa 4 — Avviare il trasferimento</h2>

<p>Dal nuovo registrar: «trasferire un dominio», poi il nome e il codice
di autorizzazione. Il registro invia una richiesta di conferma
all'indirizzo del titolare. Confermi.</p>

<p>Conti da uno a sette giorni secondo l'estensione. Nel frattempo,
<strong>il Suo sito e le Sue e-mail continuano a funzionare</strong>: un
trasferimento di registrar non cambia i DNS. È una preoccupazione
frequente e ingiustificata.</p>

<p>Due dettagli che si inceppano: un dominio registrato o trasferito da
meno di sessanta giorni non può essere trasferito di nuovo (regola
dell'ICANN), e un dominio rimasto bloccato farà fallire la richiesta senza
una spiegazione chiara.</p>

<h2>Tappa 5 — Verificare i DNS, e soprattutto le e-mail</h2>

<p>Una volta terminato il trasferimento, apra la zona DNS presso il nuovo
registrar e la confronti con la vecchia, riga per riga. La maggior parte
dei registrar riprende i record automaticamente, ma non tutti.</p>

<p>Guardi in particolare:</p>

<ul>
  <li>i record <strong>A</strong> e <strong>CNAME</strong>, che fanno
  puntare il sito;</li>
  <li>i record <strong>MX</strong>, che fanno arrivare le Sue e-mail — è
  <em>lì</em> che si producono gli incidenti;</li>
  <li>i record <strong>TXT</strong> di tipo SPF, DKIM e DMARC, senza i
  quali le Sue e-mail finiscono nella posta indesiderata.</li>
</ul>

<p>Faccia la verifica in un giorno feriale, al mattino, e si mandi
un'e-mail di prova da un indirizzo esterno entro l'ora successiva.</p>

<h2>Se il fornitore non risponde</h2>

<ol>
  <li><strong>Solleciti per iscritto</strong>, con raccomandata se serve,
  citando il Suo contratto e fissando un termine.</li>
  <li><strong>Scriva direttamente al registrar</strong> con le Sue prove di
  proprietà: fatture di rinnovo, estratto del registro di commercio,
  marchio depositato. I registrar hanno una procedura per le controversie
  sulla titolarità.</li>
  <li><strong>Per un <code>.ch</code></strong>, il registro svizzero
  dispone di una procedura di risoluzione delle controversie; per le
  estensioni generiche è la procedura UDRP dell'OMPI. Sono pensate per i
  casi di malafede e hanno un costo.</li>
  <li><strong>Come ultima risorsa</strong>, compri una variante
  (<code>.ch</code> al posto di <code>.com</code>, o un nome leggermente
  diverso) e reindirizzi. Perde storico, ma riprende il controllo — ed è
  spesso meno costoso di una procedura di sei mesi.</li>
</ol>

<h2>Perché non succeda più</h2>

<ul>
  <li>Il dominio è registrato <strong>a Suo nome</strong>, su un conto di
  cui <strong>Lei</strong> ha le credenziali.</li>
  <li>L'indirizzo e-mail del conto non dipende dal dominio stesso.</li>
  <li>Il rinnovo automatico è attivo, su una carta valida.</li>
  <li>Il blocco di trasferimento è attivo in tempi normali: è ciò che
  impedisce una sottrazione.</li>
  <li>Le Sue credenziali sono annotate altrove che nella testa di una sola
  persona.</li>
</ul>

<p>Noi applichiamo questo per impostazione predefinita: il dominio è
comprato a Suo nome, resta di Sua proprietà in ogni momento, e Le viene
trasferito su richiesta senza spese, anche se se ne va altrove. È scritto
nelle nostre condizioni, che è l'unico posto in cui questo conta. Se ha un
dominio da recuperare prima di rifare il Suo sito,
<a href="../devis.html">ce lo dica</a>: è un'operazione che facciamo
regolarmente.</p>
""",
  "faq": [
    ("Si perdono il sito e le e-mail durante un trasferimento di dominio?",
     "No. Un trasferimento di registrar non modifica i DNS: il sito e le "
     "e-mail continuano a funzionare. Le interruzioni vengono da una zona DNS "
     "ricopiata male dopo il trasferimento, in particolare dai record MX."),
    ("Che cosa fare se il vecchio fornitore rifiuta di restituire il dominio?",
     "Sollecitare per iscritto con un termine, poi rivolgersi al registrar con "
     "prove di proprietà. Esiste una procedura di risoluzione delle "
     "controversie per i .ch e la procedura UDRP dell'OMPI per le estensioni "
     "generiche."),
    ("Quanto costa un nome a dominio .ch all'anno?",
     "Una decina di franchi all'anno presso la maggior parte dei registrar. "
     "La differenza di prezzo tra fornitori è trascurabile."),
  ],
 },
]


# ---------------------------------------------------------------------------
# Etichette d'interfaccia (tutto ciò che non è corpo d'articolo)
# ---------------------------------------------------------------------------

UI = {
    "accueil": "Home",
    "fil_blog": "Blog",
    "blog_titre": "Blog: siti web e visibilità per le PMI svizzere | Up2Front",
    "blog_desc": "Nove articoli per le PMI svizzere: prezzi reali, tempi "
                 "reali, e quello che faremmo al Suo posto.",
    "date_texte": "12 settembre 2026",
    "meta": "Pubblicato il {date} · lettura {lecture}",
    "retour": "Tutti gli articoli",
    "voir_tarifs": "Vedi i prezzi",
    "demander_devis": "Richiedi un preventivo",
    "lire": "Leggi l'articolo",
    "faq_t": "Domande frequenti.",
    "faq_c": "Le domande che ci vengono poste su questo tema, con la "
             "risposta breve.",
    "suite_t": "Da leggere dopo.",
    "suite_c": "Altri due articoli del giornale, su temi vicini.",
    "art_appel_h2": "Un parere sul Suo caso preciso?",
    "art_appel_p": "Descriva la Sua attività in tre righe. Rispondiamo in "
                   "giornata, dal lunedì al venerdì, e diciamo anche quando "
                   "un sito non è la Sua priorità.",
    "art_appel_b1": "Richiedi un preventivo",
    "art_appel_b2": "Vedi i prezzi",
    "ecrire": "Scrivere a contact@up2front.com",
}


# ---------------------------------------------------------------------------
# Pagina segnalazione — annunciata, non aperta
# ---------------------------------------------------------------------------

PARRAINAGE = {
    "titre": "Segnalazione | Up2Front",
    "desc": "Il nostro programma di segnalazione non è ancora aperto. Ecco "
            "che cosa stiamo preparando, e come essere avvisato il giorno in "
            "cui parte.",
    "fil": "Segnalazione",
    "sur_titre": "Presto disponibile",
    "h1": ["La segnalazione arriva.", "Non è ancora aperta."],
    "lede": "Stiamo preparando un programma di segnalazione per chi ci "
            "raccomanda già. Finché non è in piedi, non esponiamo alcun "
            "importo e non chiediamo alcuna coordinata bancaria.",
    "b1": "Essere avvisato del lancio",
    "b2": "Leggere le condizioni attuali",
    "prose": """
<p class="maj">Situazione al 12 settembre 2026 — programma in preparazione</p>

<p><strong>Oggi non c'è alcun programma di segnalazione aperto presso
Up2Front.</strong> Nessuna commissione è promessa, nessuna iscrizione è
aperta, e nessun versamento può essere richiesto sulla base di una
raccomandazione. Questa pagina esiste per annunciare ciò che stiamo
preparando, non per far firmare alcunché.</p>

<p>Avremmo potuto pubblicare una tabella fin da ora: è una riga di testo da
scrivere. Ma una segnalazione sostenibile richiede un dispositivo dietro —
sapere chi ha raccomandato chi, verificare che un ordine sia stato
realmente pagato, versare una somma a una persona che non è cliente, e
trattare correttamente questo versamento sul piano contabile e fiscale. È
questo dispositivo che stiamo mettendo in piedi prima di aprire.</p>

<h2>Ciò che sarà annunciato il giorno del lancio</h2>

<ul>
  <li>Chi può partecipare, e a quali condizioni.</li>
  <li>Che cosa fa scattare esattamente un compenso, e in quale momento.</li>
  <li>L'importo, o la percentuale, scritto nero su bianco.</li>
  <li>Il termine di versamento e il mezzo utilizzato.</li>
  <li>I casi in cui non è dovuto nulla — annullamento, rimborso, ordine
  effettuato da Lei stesso.</li>
</ul>

<p>Finché questi cinque punti non sono scritti, non c'è programma. Le
nostre <a href="legal/affiliation.html">condizioni di segnalazione e di
affiliazione</a> lo dicono negli stessi termini, e fanno fede.</p>

<h2>Se ci raccomanda da qui ad allora</h2>

<p>Succede, ed è ciò che fa vivere una giovane impresa. Se qualcuno ordina
grazie a Lei, ci scriva a
<a href="mailto:contact@up2front.com">contact@up2front.com</a>: ne
discuteremo di comune accordo, caso per caso. Sarà un accordo puntuale,
non l'applicazione di un programma — e lo diremo come tale.</p>

<h2>Essere avvisato</h2>

<p>Basta un messaggio a <a href="mailto:contact@up2front.com?subject=Segnalazione%20—%20avvisarmi%20del%20lancio">contact@up2front.com</a>
con la dicitura «segnalazione». Non abbiamo bisogno delle Sue coordinate
bancarie per iscriverLa a una lista d'attesa, e non gliele chiederemo mai
prima che una somma sia realmente dovuta.</p>
""",
    "etapes_t": "Ciò che stiamo mettendo in piedi.",
    "etapes_c": "Tre cantieri, in quest'ordine. Il programma aprirà quando "
                "tutti e tre saranno terminati.",
    "etapes": [
        ("Cantiere 1", "Il tracciamento delle raccomandazioni",
         "Un link di segnalazione nominativo, collegato a un ordine pagato. "
         "Senza questo tracciamento, impossibile sapere chi ha diritto a "
         "che cosa."),
        ("Cantiere 2", "Il quadro scritto",
         "Condizioni di segnalazione complete, integrate nelle condizioni "
         "generali, che dicono anche in quali casi non è dovuto nulla."),
        ("Cantiere 3", "Il versamento",
         "Il trattamento contabile e fiscale di un compenso versato a una "
         "persona che non è cliente. È il punto più lungo."),
    ],
    "appel_h2": "Nel frattempo, il modo più semplice di aiutarci",
    "appel_p": "Parli di noi a qualcuno che ne ha bisogno, e ce lo dica. "
               "Rispondiamo in giornata, dal lunedì al venerdì.",
    "appel_b1": "Scrivere a contact@up2front.com",
    "appel_b2": "Vedi i prezzi",
}
