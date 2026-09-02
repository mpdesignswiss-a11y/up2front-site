/* ============================================================
   UP2FRONT — couche de mouvement
   Ajoutée le 2 septembre 2026, en complément de app.js.

   app.js porte le fonctionnement du site (Stripe, filtres,
   récapitulatif de commande). Ce fichier-ci ne porte que le
   rendu : il n'ajoute aucun texte, ne déplace aucun élément,
   ne modifie aucun contenu.

   Principe de sûreté : c'est ce script qui pose les classes
   d'animation. Sans lui — JavaScript coupé, erreur, robot
   d'indexation — aucune classe n'est posée, donc rien n'est
   masqué et la page reste entièrement lisible.
   ============================================================ */
(function () {
  'use strict';

  var doux = window.matchMedia &&
             window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --------------------------------------------------------
     1. En-tête : état « collé » dès qu'on quitte le haut
     -------------------------------------------------------- */
  var entete = document.querySelector('header.nav');
  if (entete) {
    var majEntete = function () {
      entete.classList.toggle('stuck', window.scrollY > 12);
    };
    majEntete();
    window.addEventListener('scroll', majEntete, { passive: true });
  }

  if (doux) return;   // au-delà, tout est décoratif

  /* --------------------------------------------------------
     2. Entrée en vue
     --------------------------------------------------------
     On marque les éléments porteurs de sens visuel, puis on les
     révèle une seule fois, quand ils arrivent dans le champ.
     Les enfants d'une même grille sont décalés les uns après les
     autres — c'est ce léger retard qui donne l'impression que la
     page se construit plutôt qu'elle n'apparaît.
  -------------------------------------------------------- */
  if (!('IntersectionObserver' in window)) return;

  var seuls = [
    '.sec > .wrap > h2', '.sec-head', '.lede', '.label',
    '.big-rev', '.vs', '.custom-cta', '.cta-arrow', '.quote',
    '.ebook', '.faq-wrap', '.trust', '.hero-strip', '.stat',
    '.pay-row', '.auth-row', '.notice', '.checkout > *'
  ];
  var groupes = [
    '.plans', '.grid', '.team-row', '.steps', '.flist',
    '.wall', '.pills', '.tabs', '.filters'
  ];

  var observateur = new IntersectionObserver(function (entrees) {
    entrees.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('is-in');
      observateur.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  var suivre = function (el, retard) {
    if (!el || el.classList.contains('rv') || el.classList.contains('rv-l')) return;
    el.classList.add(retard ? 'rv-l' : 'rv');
    if (retard) el.style.transitionDelay = retard + 'ms';
    observateur.observe(el);
  };

  seuls.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) { suivre(el, 0); });
  });

  groupes.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (conteneur) {
      var enfants = Array.prototype.slice.call(conteneur.children);
      // Au-delà d'une douzaine, le décalage devient une attente :
      // on plafonne le retard cumulé.
      enfants.forEach(function (enfant, i) {
        suivre(enfant, Math.min(i, 8) * 70);
      });
    });
  });

  /* Le titre du hero ne passe pas par l'observateur : il est déjà
     visible au chargement. Il monte une fois, tout de suite. */
  var h1 = document.querySelector('.hero h1');
  if (h1) {
    h1.classList.add('rv');
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { h1.classList.add('is-in'); });
    });
  }
  ['.hero .eyebrow', '.hero .lede', '.hero-kicker', '.hero-cta'].forEach(function (sel, i) {
    var el = document.querySelector(sel);
    if (!el) return;
    el.classList.add('rv');
    el.style.transitionDelay = (110 + i * 90) + 'ms';
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { el.classList.add('is-in'); });
    });
  });

  /* --------------------------------------------------------
     3. Boutons magnétiques
     --------------------------------------------------------
     Le bouton se décale de quelques pixels vers le curseur qui
     l'approche. Très peu — six pixels au maximum. Assez pour que
     la main sente que la cible vient à elle.
  -------------------------------------------------------- */
  if (window.matchMedia && window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.btn-lg, .rnd').forEach(function (b) {
      b.addEventListener('mousemove', function (e) {
        var r = b.getBoundingClientRect();
        var x = (e.clientX - r.left - r.width / 2) / r.width;
        var y = (e.clientY - r.top - r.height / 2) / r.height;
        b.style.transform = 'translate(' + (x * 12).toFixed(2) + 'px,' +
                                           (y * 8).toFixed(2) + 'px)';
      });
      b.addEventListener('mouseleave', function () { b.style.transform = ''; });
    });
  }

  /* --------------------------------------------------------
     4. Compteurs
     --------------------------------------------------------
     Les nombres des blocs .stat comptent depuis zéro à leur
     arrivée. Le texte d'origine est relu tel quel puis remis à
     l'identique en fin d'animation : ni le format ni l'unité ne
     sont réécrits.
  -------------------------------------------------------- */
  document.querySelectorAll('.stat b').forEach(function (b) {
    var final = b.textContent;
    var m = final.match(/^(\D*)([\d'’ ]+)(.*)$/);
    if (!m) return;
    var cible = parseInt(m[2].replace(/[^\d]/g, ''), 10);
    if (!cible || cible > 1000000) return;

    var o = new IntersectionObserver(function (ent) {
      if (!ent[0].isIntersecting) return;
      o.disconnect();
      var t0 = performance.now(), duree = 1100;
      (function pas(t) {
        var p = Math.min(1, (t - t0) / duree);
        var e = 1 - Math.pow(1 - p, 3);
        if (p < 1) {
          b.textContent = m[1] + Math.round(cible * e) + m[3];
          requestAnimationFrame(pas);
        } else {
          b.textContent = final;      // on rend le texte d'origine
        }
      })(performance.now());
    }, { threshold: 0.6 });
    o.observe(b);
  });

  /* --------------------------------------------------------
     5. Parallaxe des maquettes
     --------------------------------------------------------
     Les aperçus de site dérivent un peu plus lentement que la
     page. Amplitude volontairement faible : au-delà, l'effet se
     voit, et un effet qui se voit fatigue.
  -------------------------------------------------------- */
  var flottants = Array.prototype.slice.call(
    document.querySelectorAll('.pack-cell .mock, .g3 > .mock, .g2 > .mock')
  );
  if (flottants.length) {
    var enCours = false;
    var placer = function () {
      var h = window.innerHeight;
      flottants.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > h + 200) return;
        var d = (r.top + r.height / 2 - h / 2) / h;   // -1 … 1
        el.style.setProperty('--par', (d * -14).toFixed(2) + 'px');
        el.style.translate = '0 var(--par)';
      });
      enCours = false;
    };
    window.addEventListener('scroll', function () {
      if (enCours) return;
      enCours = true;
      requestAnimationFrame(placer);
    }, { passive: true });
    placer();
  }
})();
