(function(){
"use strict";

var q  = function(s,r){ return (r||document).querySelector(s); };
var qq = function(s,r){ return Array.prototype.slice.call((r||document).querySelectorAll(s)); };

/* =====================================================================
   0 · SECOURS — si un CDN ne répond pas, la page reste entièrement lisible
   ===================================================================== */
function toutMontrer(){
  qq('.rv').forEach(function(el){ el.style.opacity = 1; el.style.transform = 'none'; });
  qq('h1 .ln i').forEach(function(el){ el.style.transform = 'none'; });
  qq('.fan i').forEach(function(el){ el.style.opacity = 1; });
  var e = q('.enleve'); if(e) e.style.setProperty('--trait','1');
  qq('.accroche h2').forEach(function(el){ el.style.color = 'var(--blanc)'; });
}
if(!window.gsap || !window.ScrollTrigger){ toutMontrer(); return; }

gsap.registerPlugin(ScrollTrigger);
if(window.SplitText)           gsap.registerPlugin(SplitText);
if(window.ScrambleTextPlugin)  gsap.registerPlugin(ScrambleTextPlugin);
if(window.CustomEase){
  gsap.registerPlugin(CustomEase);
  CustomEase.create('oryzen',     '0.16,1,0.3,1');
  CustomEase.create('oryzenDoux', '0.33,1,0.68,1');
}
var E  = window.CustomEase ? 'oryzen'     : 'power3.out';
var ED = window.CustomEase ? 'oryzenDoux' : 'power2.out';

var reduit = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var fin    = window.matchMedia('(hover:hover) and (pointer:fine)').matches;

/* =====================================================================
   1 · MODE SOBRE — état final posé d'un coup, aucune animation
   ===================================================================== */
if(reduit){ toutMontrer(); return; }

/* =====================================================================
   2 · LENIS — défilement lissé branché sur l'horloge de GSAP.
   Ce pont est la pièce maîtresse : sans lui, Lenis et ScrollTrigger
   lisent deux positions de défilement différentes et tout déraille.
   ===================================================================== */
var lenis = null;
if(window.Lenis){
  lenis = new Lenis({
    duration: 1.15,
    easing: function(t){ return Math.min(1, 1.001 - Math.pow(2, -10*t)); },
    smoothWheel: true,
    touchMultiplier: 1.6
  });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add(function(t){ lenis.raf(t * 1000); });
  gsap.ticker.lagSmoothing(0);
  /* exposé pour u2f-pages.js : une modale doit pouvoir suspendre le
     défilement lissé, sinon la page continue de glisser derrière. */
  window.u2fLenis = lenis;
}

qq('a[href^="#"]').forEach(function(a){
  a.addEventListener('click', function(e){
    var c = q(a.getAttribute('href'));
    if(!c) return;
    e.preventDefault();
    if(lenis) lenis.scrollTo(c, {offset:-90, duration:1.4});
    else c.scrollIntoView({behavior:'smooth'});
  });
});

/* =====================================================================
   3 · POSITIONS DE DÉPART
   ===================================================================== */
gsap.set(['.lede','.prix','.cta','.faces'], {y:30});
/* le CSS masque déjà les lignes du titre ; on le retraduit en unités GSAP,
   sinon GSAP lit translateY(112%) comme un y en pixels et la ligne
   retombe décalée à la fin du tween. */
gsap.set('h1 .ln i', {y:0, yPercent:112});
gsap.set('.badges', {opacity:1});
gsap.set('.logos .rv, .accroche .rv, .tarifs .rv', {y:60});

/* =====================================================================
   4 · INTRO — le titre monte ligne par ligne, le reste suit en cascade
   ===================================================================== */
var intro = gsap.timeline({ delay:.12, defaults:{ ease:E } });

intro
  .from('.tick',    {opacity:0, y:-18, duration:.85})
  .to('h1 .ln i',   {yPercent:0, duration:1.15, stagger:.09}, '-=.5')
  .to('.lede',      {opacity:1, y:0, duration:1}, '-=.72')
  .to('.prix',      {opacity:1, y:0, duration:.9}, '-=.85')
  .to('.cta',       {opacity:1, y:0, duration:.9}, '-=.75')
  .from('.btn',     {y:26, opacity:0, duration:.8, stagger:.09, clearProps:'transform'}, '-=.8')
  .to('.faces',     {opacity:1, y:0, duration:.6}, '-=.7')
  .from('.face',    {scale:0, duration:.55, stagger:.04, ease:'back.out(2)',
                     clearProps:'transform'}, '-=.5');

/* --- brouillage du prix, une fois le bloc visible --- */
var prix = q('[data-scramble]');
if(prix && window.ScrambleTextPlugin){
  intro.to(prix, {
    duration: 1.5,
    scrambleText: { text: prix.textContent, chars:'upperCase', speed:.55, revealDelay:.35 }
  }, '-=1.7');
}

/* =====================================================================
   5 · CARTES — apparition puis flottement perpétuel
        (relevé au mot près sur la timeline GSAP du template)
   ===================================================================== */
var fan = q('.fan');
if(fan){
  var cartes = qq('.fan i');

  ScrollTrigger.create({
    trigger: fan, start:'top 92%', once:true,
    onEnter: function(){
      /* 1 · entrée : from opacity 0 / y 30, 0.5s, stagger 0.05, power2.out */
      gsap.fromTo(cartes, {opacity:0, y:30}, {
        opacity:1, y:0, duration:.5, ease:'power2.out',
        stagger:{each:.05},
        onComplete: function(){
          /* 2 · flottement : from y 15, 0.6s, yoyo infini, stagger 0.2 sine.in */
          gsap.from(cartes, {
            y:15, duration:.6, repeat:-1, yoyo:true, ease:'none',
            stagger:{each:.2, from:'start', grid:'auto', axis:'x', ease:'sine.in'}
          });
        }
      });
    }
  });
}

/* =====================================================================
   6 · ACCROCHE — les mots s'allument au fil du défilement
   ===================================================================== */
var h2 = q('[data-mots]');
if(h2 && window.SplitText){
  var cut  = new SplitText(h2, {type:'words', wordsClass:'mot'});
  var mots = cut.words;
  qq('[data-em]', h2).forEach(function(n){
    mots.forEach(function(w){ if(n.contains(w)) w.dataset.em = '1'; });
  });

  gsap.to(mots, {
    color: function(i, t){ return t.dataset.em ? 'var(--vert)' : 'var(--blanc)'; },
    duration: .5, stagger: .12, ease:'none',
    scrollTrigger: { trigger:h2, start:'top 84%', end:'bottom 60%', scrub:.55 }
  });
}else if(h2){
  h2.style.color = 'var(--blanc)';
}

/* --- « On a tout enlevé. » et son trait vert --- */
var enl = q('.enleve');
if(enl){
  gsap.from(enl, {
    y:44, opacity:0, duration:1, ease:E,
    scrollTrigger:{ trigger:enl, start:'top 90%', once:true }
  });
  gsap.fromTo(enl, {'--trait':0}, {
    '--trait':1, duration:1.1, ease:E, delay:.25,
    scrollTrigger:{ trigger:enl, start:'top 88%', once:true }
  });
}

/* =====================================================================
   7 · BANDEAUX — vitesse et sens pilotés par le défilement (signature Oryzen)
   ===================================================================== */
/* La boucle elle-même est en CSS (@keyframes u2f-defile, u2f.css) : elle
   tourne donc sans JavaScript, sur toutes les pages, même si un CDN tombe.
   Ce qui reste ici, c'est la seule chose que le CSS ne sait pas faire :
   accélérer la bande quand on défile vite, et la ramener à son allure de
   croisière quand on s'arrête. On agit sur playbackRate de l'animation CSS.
   Le sens ne s'inverse jamais : on repart toujours vers +1, sinon un seul
   défilement vers le haut laissait la bande à l'envers pour de bon. */
function bandeau(sel){
  var ul = q(sel);
  if(!ul || !ul.getAnimations) return;
  var repos;
  ScrollTrigger.create({
    onUpdate: function(self){
      var v = self.getVelocity();
      if(!v) return;
      var anims = ul.getAnimations();
      if(!anims.length) return;
      var a = anims[0];
      a.playbackRate = gsap.utils.clamp(1, 6, 1 + Math.abs(v)/420);
      clearTimeout(repos);
      repos = setTimeout(function(){
        var b = ul.getAnimations()[0];
        if(b) b.playbackRate = 1;
      }, 380);
    }
  });
}
bandeau('.tick ul');
bandeau('.marq ul');

/* =====================================================================
   8 · RÉVÉLATIONS PAR LOTS
   ===================================================================== */
function lot(sel, opts){
  opts = opts || {};
  /* on résout le sélecteur une seule fois, puis on marque ce qui est pris en
     charge : le filet de la fin de fichier saura ce qui reste. On passe
     ensuite les éléments — et non le sélecteur — à ScrollTrigger, sinon un
     sélecteur du genre « :not([data-lot]) » ne trouverait plus rien. */
  var elements = (typeof sel === 'string') ? qq(sel) : sel;
  if(!elements.length) return;
  elements.forEach(function(el){ el.setAttribute('data-lot',''); });
  ScrollTrigger.batch(elements, {
    start: 'top 88%', once: true,
    onEnter: function(cibles){
      gsap.to(cibles, {
        opacity:1, y:0, duration: opts.duree || 1,
        stagger: opts.stagger || .08, ease:E,
        onComplete: function(){ gsap.set(cibles, {clearProps:'transform'}); }
      });
    }
  });
}
lot('.logos .rv');
lot('.accroche .top .rv');
lot('.arg');
lot('.thead .rv');
lot('.plan', {duree:1.15, stagger:.11});

/* --- bandeaux de confiance : chaque case se déroule en largeur, au scrub
       (mécanique « statistic-card » du template : width 0 → 100 %) --- */
qq('.badges>div').forEach(function(c, i){
  gsap.fromTo(c,
    {opacity:1, y:0, clipPath:'inset(0 100% 0 0)'},
    {clipPath:'inset(0 0% 0 0)', ease:'none',
     scrollTrigger:{ trigger:c, start:'top 100%', end:'top 55%', scrub:.8 }});
});

qq('.plan').forEach(function(p){
  gsap.from(qq('.feat li', p), {
    opacity:0, y:14, duration:.5, stagger:.026, ease:ED,
    scrollTrigger:{ trigger:p, start:'top 70%', once:true }
  });
});

/* =====================================================================
   8 bis · LES QUATRE MÉCANIQUES DE DÉFILEMENT DU TEMPLATE
           (relevées une à une sur sa timeline GSAP)
   ===================================================================== */

/* --- a · titre en éclats : chaque mot naît d'un point, dans le désordre
       (from opacity 0 / scale 0, stagger .03 « random », scrub .8) --- */
qq('[data-eclats]').forEach(function(ecl){
  if(!window.SplitText) return;
  var dec = new SplitText(ecl, {type:'words', wordsClass:'eclat'});
  gsap.from(dec.words, {
    opacity:0, scale:0, duration:.08, ease:'none',
    stagger:{each:.03, from:'random'},
    scrollTrigger:{ trigger:ecl, start:'top bottom', end:'top 45%', scrub:.8 }
  });
});

/* --- b · paragraphe ligne à ligne : chacune glisse depuis la gauche
       (from opacity .5 / x -50, stagger .1, scrub .8, top 65 %) --- */
qq('[data-lignes]').forEach(function(lig){
  if(!window.SplitText) return;
  var dl = new SplitText(lig, {type:'lines', linesClass:'ligne'});
  gsap.from(dl.lines, {
    opacity:.5, x:-50, duration:.5, ease:ED,
    stagger:{each:.1},
    scrollTrigger:{ trigger:lig, start:'top 78%', end:'bottom 55%', scrub:.8 }
  });
});

/* --- b bis · même recette, mais sur les éléments d'une liste plutôt que
       sur des lignes découpées : SplitText type:'lines' remonterait ses
       .ligne au rang d'enfants directs du <ul> et détruirait les <li>. --- */
qq('[data-items]').forEach(function(lst){
  gsap.from(qq('li', lst), {
    opacity:.5, x:-50, duration:.5, ease:ED,
    stagger:{each:.1},
    scrollTrigger:{ trigger:lst, start:'top 78%', end:'bottom 55%', scrub:.8 }
  });
});

/* --- c · cartes de prix : dérive différenciée, la carte centrale remonte
       pendant que les deux autres descendent (parallaxe du template) --- */
var derive = [7, -8, 7];
qq('.plan').forEach(function(p, i){
  gsap.to(p, {
    yPercent: derive[i] || 0, ease:'none',
    scrollTrigger:{ trigger:'.tarifs .grid', start:'top bottom', end:'bottom top', scrub:.8 }
  });
});

/* --- d · le bandeau de logos se décale aussi au défilement, par-dessus
       sa boucle : deux vitesses superposées, comme sur le template --- */
var mu = q('.marq ul');
if(mu){
  gsap.fromTo(mu, {x:150}, {
    x:-150, ease:'none',
    scrollTrigger:{ trigger:'.marq', start:'top bottom', end:'bottom top', scrub:.8 }
  });
}

/* --- e · le compteur monte jusqu'au chiffre, puis rend le texte exact --- */
var cpt = q('[data-compte]');
if(cpt){
  var final = cpt.textContent;                    // « 1 500 », espace comprise
  var sep   = final.replace(/[0-9]/g, '').charAt(0) || '';
  var cible = parseFloat(cpt.dataset.compte);
  var obj   = {v:0};
  gsap.to(obj, {
    v: cible, duration: 2, ease:'power1.out', snap:{v:1},
    scrollTrigger:{ trigger:cpt, start:'top 85%', once:true },
    onUpdate: function(){
      var n = Math.round(obj.v).toString();
      cpt.textContent = sep ? n.replace(/\B(?=(\d{3})+(?!\d))/g, sep) : n;
    },
    onComplete: function(){ cpt.textContent = final; }
  });
}

/* =====================================================================
   8 ter · LE RESTE DU VOCABULAIRE DU TEMPLATE
           (redressement, croissance, contre-bandeau, dérive multiple)
   ===================================================================== */

/* --- f · les cartes de prix se redressent : couchées vers l'arrière au bas
       de l'écran, elles se remettent d'aplomb en montant. C'est la
       mécanique « project-rest-parent » du template : rotationX → 0deg,
       charnière au pied de la carte, au scrub. Le signe compte : l'angle
       est positif, le haut de la carte part vers le fond. Négatif, il
       viendrait vers l'œil et la projection déborderait de l'écran. --- */
qq('.plan').forEach(function(p){
  gsap.fromTo(p,
    {rotationX:34, transformOrigin:'50% 100%'},
    {rotationX:0, ease:'none',
     scrollTrigger:{ trigger:p, start:'top bottom', end:'top 58%', scrub:.8 }});
});

/* --- g · le pavé hachuré grandit en entrant, du huitième à sa pleine
       largeur (mécanique « project-inner-parent » : width/height → 100 %,
       de clamp(top 85 %) à clamp(bottom 90 %)) --- */
var hach = q('.stripe');
if(hach){
  gsap.fromTo(hach,
    {width:'22%', height:'34px'},
    {width:'100%', height:'96px', ease:'none',
     scrollTrigger:{ trigger:hach, start:'top 88%', end:'bottom 62%', scrub:.8 }});
}

/* --- h · les deux bandeaux tirent en sens contraire pendant le défilement,
       comme les deux rangées du template (x 0 % d'un côté, −50 % de
       l'autre). Le ruban du héros part vers la droite, celui des logos
       vers la gauche. --- */
var tu = q('.tick ul');
if(tu){
  gsap.fromTo(tu, {x:-120}, {
    x:120, ease:'none',
    scrollTrigger:{ trigger:'.hero', start:'top top', end:'bottom top', scrub:.8 }
  });
}

/* --- i · dérive différenciée dans la grille d'arguments : la grille elle-même
       ne bouge pas (ses filets d'un pixel doivent rester joints), mais le
       texte de chaque case suit sa propre vitesse — les uns montent, les
       autres descendent. C'est la parallaxe multi-cible du template
       (y 80 / 90 / 120 / −100 / −80, durées 0,4 à 0,9). --- */
var vites = [14, -11, 18, -15, -12, 17, -9, 13];
qq('.arg p').forEach(function(t, i){
  gsap.fromTo(t,
    {y: -vites[i % vites.length]},
    {y:  vites[i % vites.length], ease:'none',
     scrollTrigger:{ trigger:'.args', start:'top bottom', end:'bottom top', scrub:.8 }});
});

/* =====================================================================
   8 quater · LES SECTIONS REPRISES DU FICHIER D'ALEX
              (mêmes mécaniques que ci-dessus, rien de nouveau : on rejoue
              le vocabulaire relevé sur le template)
   ===================================================================== */

/* --- révélations par lots, section par section --- */
lot('#transformation .h2, #transformation .sub, #transformation .cta-l');
lot('#transformation .col', {duree:1.1, stagger:.12});
lot('.puce', {duree:.7, stagger:.045});
lot('#inclus .h2, #inclus .sub');
lot('.incl > .rv', {duree:.85, stagger:.05});
lot('#realisations .h2, #realisations .sub, #realisations .cta-l');
lot('.filtres .rv', {duree:.7, stagger:.05});
lot('#realisations .cas', {duree:1, stagger:.08});
lot('#process .rv');
lot('#bilan .h2');
lot('.bal > .rv', {duree:1.05, stagger:.12});
lot('.franc');
lot('#garantie .rv', {duree:1.05, stagger:.1});
lot('#avis .rv');
lot('#equipe .h2, #equipe .sub');
lot('.mbr', {duree:.95, stagger:.06});
/* Les sections « cas » et « methode » ont été retirées de l'accueil : la
   première faisait doublon avec la galerie #realisations, la seconde offrait un
   guide qui n'existe pas. Leurs lignes d'animation partent avec elles. */
lot('#faq .rv');

/* --- j · le tri par thème.

   Les cinq pastilles étaient jusqu'ici des <b> décoratifs : rien ne les
   écoutait, et cliquer dessus ne faisait rien. Ce sont maintenant de vrais
   boutons, et chaque carte porte le thème auquel elle appartient. Le tri se
   fait donc en comparant deux attributs, sans liste tenue à part qui
   pourrait se désynchroniser des cartes.

   Trois précautions. On masque avec l'attribut « hidden » plutôt qu'avec un
   style, pour que la carte sorte aussi de l'arbre d'accessibilité — un lien
   invisible mais encore tabulable est un piège au clavier. On rejoue une
   courte apparition sur les cartes qui reviennent, sinon le changement est
   brutal. Et on prévient ScrollTrigger que les hauteurs ont bougé, faute de
   quoi les révélations du bas de page se déclenchent au mauvais endroit. --- */
(function(){
  var barre = q('.filtres'), grille = q('.cases');
  if(!barre || !grille) return;

  var boutons = qq('button', barre), cartes = qq('.cas', grille);
  var vide = q('.cases-vide');

  /* Une carte porte une ou plusieurs clés, séparées par une barre verticale :
     « Commerce|En ligne ». Le séparateur n'est ni l'espace ni la virgule parce
     que les familles en contiennent déjà (« Santé & bien-être »). C'est ce qui
     permet au filtre « En ligne » de traverser les familles au lieu d'en être
     une de plus. */
  function trier(theme){
    var visibles = 0;
    cartes.forEach(function(c){
      var cles = (c.dataset.famille || '').split('|');
      var garde = (theme === '*' || cles.indexOf(theme) !== -1);
      if(garde){
        var etait = c.hidden;
        c.hidden = false;
        visibles++;
        if(etait) gsap.fromTo(c, {opacity:0, y:14},
                              {opacity:1, y:0, duration:.42, ease:E});
      }else{
        c.hidden = true;
      }
    });
    boutons.forEach(function(b){
      b.setAttribute('aria-pressed', String(b.dataset.filtre === theme));
    });
    if(vide) vide.hidden = visibles > 0;
    ScrollTrigger.refresh();
  }

  boutons.forEach(function(b){
    b.addEventListener('click', function(){ trier(b.dataset.filtre); });
  });
})();

/* --- k · le bandeau des moyens de paiement et le mot géant du pied de page
       reprennent la boucle pilotée par la vitesse de défilement --- */
bandeau('.moyens ul');
bandeau('.fmarq ul');

/* --- l · et, comme sur le template, ce mot géant tire en sens contraire
       de sa propre boucle --- */
var fm = q('.fmarq ul');
if(fm){
  gsap.fromTo(fm, {x:-160}, {
    x:160, ease:'none',
    scrollTrigger:{ trigger:'footer', start:'top bottom', end:'bottom bottom', scrub:.8 }
  });
}

/* --- m · le trait de la couverture se déploie de gauche à droite
       (même croissance en largeur que le pavé hachuré) --- */
var bar = q('.couv .bar');
if(bar){
  gsap.fromTo(bar, {scaleX:0}, {
    scaleX:1, ease:'none',
    scrollTrigger:{ trigger:'.couv', start:'top 82%', end:'bottom 72%', scrub:.8 }
  });
}

/* --- n · les trois avis dérivent à des vitesses différentes : c'est la
       parallaxe des témoignages du template (y 80 / 90 / 120 px, ease none,
       scrub .8, de top bottom à bottom top) --- */
var davis = [30, -24, 38];
qq('.avis-c').forEach(function(c, i){
  gsap.fromTo(c,
    {y: -davis[i % davis.length]},
    {y:  davis[i % davis.length], ease:'none',
     scrollTrigger:{ trigger:'.avis-g', start:'top bottom', end:'bottom top', scrub:.8 }});
});

/* --- o · les lignes de la comparaison et du bilan glissent une à une --- */
qq('#transformation .col, .bal > div').forEach(function(b){
  gsap.from(qq('li', b), {
    opacity:0, x:-24, duration:.55, stagger:.058, ease:ED,
    scrollTrigger:{ trigger:b, start:'top 80%', once:true }
  });
});

/* --- p · la FAQ : à l'ouverture, la réponse se déroule en hauteur plutôt
       que d'apparaître d'un bloc --- */
qq('.qa').forEach(function(d){
  var rep = q('.rep', d), som = q('summary', d);
  if(!rep || !som) return;
  som.addEventListener('click', function(e){
    e.preventDefault();
    if(d.open){
      gsap.to(rep, {height:0, opacity:0, duration:.34, ease:ED, onComplete:function(){
        d.open = false; gsap.set(rep, {height:'auto', opacity:1});
      }});
    }else{
      d.open = true;
      gsap.from(rep, {height:0, opacity:0, duration:.42, ease:E,
        onComplete:function(){ ScrollTrigger.refresh(); }});
    }
  });
});

/* =====================================================================
   9 · SURVOLS, AIMANTATION, CURSEUR — transform appartient à GSAP
   ===================================================================== */
if(fin){
  qq('.plan').forEach(function(p){
    var h = p.classList.contains('best') ? -11 : -7;
    p.addEventListener('mouseenter', function(){ gsap.to(p, {y:h, duration:.5, ease:E}); });
    p.addEventListener('mouseleave', function(){ gsap.to(p, {y:0, duration:.5, ease:E}); });
  });

  var faces = q('.faces');
  if(faces){
    faces.addEventListener('mouseenter', function(){
      gsap.to('.face', {y:-5, duration:.4, stagger:.02, ease:E});
    });
    faces.addEventListener('mouseleave', function(){
      gsap.to('.face', {y:0, duration:.4, stagger:.02, ease:E});
    });
  }

  qq('.btn, .go').forEach(function(b){
    var force = b.classList.contains('go') ? .2 : .32;
    b.addEventListener('mousemove', function(e){
      var r = b.getBoundingClientRect();
      gsap.to(b, {
        x:(e.clientX - r.left - r.width/2)  * force,
        y:(e.clientY - r.top  - r.height/2) * force,
        duration:.4, ease:'power3.out'
      });
    });
    b.addEventListener('mouseleave', function(){
      gsap.to(b, {x:0, y:0, duration:.75, ease:'elastic.out(1,.45)'});
    });
  });

  var pt = document.createElement('div'); pt.className = 'pointeur';
  var an = document.createElement('div'); an.className = 'anneau';
  document.body.appendChild(pt); document.body.appendChild(an);

  var xP = gsap.quickTo(pt, 'x', {duration:.13, ease:'power3'});
  var yP = gsap.quickTo(pt, 'y', {duration:.13, ease:'power3'});
  var xA = gsap.quickTo(an, 'x', {duration:.5,  ease:'power3'});
  var yA = gsap.quickTo(an, 'y', {duration:.5,  ease:'power3'});
  var vu = false;

  window.addEventListener('mousemove', function(e){
    xP(e.clientX - 7);  yP(e.clientY - 7);
    xA(e.clientX - 21); yA(e.clientY - 21);
    if(!vu){ vu = true; gsap.to([pt, an], {opacity:1, duration:.3}); }
  }, {passive:true});

  document.addEventListener('mouseleave', function(){
    vu = false; gsap.to([pt, an], {opacity:0, duration:.3});
  });

  /* ces cartes portent déjà une dérive en y pilotée par le défilement :
     le survol joue donc sur l'échelle, composante distincte pour GSAP,
     pour ne pas écraser la parallaxe. */
  qq('.cas, .avis-c').forEach(function(c){
    c.addEventListener('mouseenter', function(){ gsap.to(c, {scale:1.018, duration:.45, ease:E}); });
    c.addEventListener('mouseleave', function(){ gsap.to(c, {scale:1,     duration:.45, ease:E}); });
  });
  qq('.mbr').forEach(function(c){
    c.addEventListener('mouseenter', function(){ gsap.to(c, {y:-8, duration:.45, ease:E}); });
    c.addEventListener('mouseleave', function(){ gsap.to(c, {y:0,  duration:.45, ease:E}); });
  });

  qq('a, .plan, .arg, .badges>div, .marq li, .face, .puce, .cas, .mbr, ' +
     '.qa summary, .fgrid li, .moyens li, .filtres button').forEach(function(el){
    el.addEventListener('mouseenter', function(){
      gsap.to(an, {scale:1.9, borderColor:'rgba(210,255,197,.9)', duration:.35, ease:E});
      gsap.to(pt, {scale:.4, duration:.35, ease:E});
    });
    el.addEventListener('mouseleave', function(){
      gsap.to(an, {scale:1, borderColor:'rgba(210,255,197,.55)', duration:.35, ease:E});
      gsap.to(pt, {scale:1, duration:.35, ease:E});
    });
  });
}

/* =====================================================================
   9bis · FILET DE RÉVÉLATION
   Les lots ci-dessus sont nommés section par section : ils décrivent
   l'accueil. Les pages intérieures portent les mêmes classes .rv sans
   appartenir à aucun de ces lots — sans ce filet, elles resteraient à
   opacity 0. Une seule règle, donc, pour tout le reste du site.
   ===================================================================== */
/* l'intro s'occupe déjà de ces quatre-là, sur toutes les pages */
qq('.lede, .cta, .prix, .faces').forEach(function(el){ el.setAttribute('data-lot',''); });
var restants = qq('.rv:not([data-lot])');
if(restants.length){
  gsap.set(restants, {y:26});
  lot(restants, {duree:.9, stagger:.07});
}

/* =====================================================================
   10 · RECALCUL une fois les polices variables chargées
   ===================================================================== */
if(document.fonts && document.fonts.ready){
  document.fonts.ready.then(function(){ ScrollTrigger.refresh(); });
}
window.addEventListener('load', function(){ ScrollTrigger.refresh(); });

})();
