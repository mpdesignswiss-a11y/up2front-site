/* ============================================================
   UP2FRONT — moteur de la couche d'effet
   Posé le 2 septembre 2026, en complément de motion.js.

   app.js    : le fonctionnement (Stripe, filtres, récapitulatif)
   motion.js : les entrées en vue, les compteurs, la parallaxe
   wow.js    : ce fichier — le rideau, le curseur, le découpage
               des titres, la lumière sous la souris.

   Deux règles tenues d'un bout à l'autre :

   1. Aucun mot n'est ajouté, retiré ni déplacé. Le découpage des
      titres emballe les mots existants, espaces compris ; le
      texte lu par un lecteur d'écran ou un robot d'indexation
      est mot pour mot celui d'Alex.

   2. Tout ce qui est décoratif est posé d'ici. JavaScript coupé,
      erreur, indexation : aucune classe n'existe, aucune règle de
      wow.css ne s'applique, la page reste celle de style.css.
   ============================================================ */
(function () {
  'use strict';

  var racine = document.documentElement;
  var doux = window.matchMedia &&
             window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fin = window.matchMedia &&
            window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* Petite aide : borne une valeur. */
  function borne(v, min, max) { return v < min ? min : (v > max ? max : v); }

  /* ==========================================================
     1. Rideau
     ==========================================================
     Il n'existe que si l'animation est acceptée. Il est retiré
     du flux par un compte à rebours de sécurité : si un
     évènement se perd, la page se découvre quand même.
  ========================================================== */
  var rideau = null;

  function poserRideau() {
    rideau = document.createElement('div');
    rideau.className = 'curtain';
    rideau.setAttribute('aria-hidden', 'true');
    for (var i = 0; i < 5; i++) rideau.appendChild(document.createElement('i'));
    rideau.appendChild(document.createElement('b'));
    document.body.appendChild(rideau);

    var lever = function () { rideau.classList.add('up'); };
    // Deux images d'attente : le temps que les polices arrivent.
    requestAnimationFrame(function () { requestAnimationFrame(lever); });
    setTimeout(lever, 900);              // filet de sécurité
    setTimeout(function () {
      if (rideau && rideau.parentNode) rideau.style.display = 'none';
    }, 2600);
  }

  function baisserRideau(vers) {
    if (!rideau) { window.location.href = vers; return; }
    rideau.style.display = '';
    rideau.classList.remove('up');
    rideau.classList.add('down');
    setTimeout(function () { window.location.href = vers; }, 620);
  }

  /* Un lien mène-t-il à une autre page de ce site ? */
  function lienInterne(a, ev) {
    if (ev.defaultPrevented || ev.button !== 0) return false;
    if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return false;
    if (a.target && a.target !== '_self') return false;
    if (a.hasAttribute('download')) return false;
    var href = a.getAttribute('href') || '';
    if (!href || href.charAt(0) === '#') return false;
    if (/^(mailto:|tel:|javascript:|https?:\/\/(?!localhost))/i.test(href)) {
      // Un lien absolu ne passe que s'il reste sur le même hôte.
      if (a.hostname && a.hostname !== window.location.hostname) return false;
    }
    if (a.hostname && a.hostname !== window.location.hostname) return false;
    // Même page, ancre différente : le navigateur s'en charge.
    if (a.pathname === window.location.pathname && a.hash) return false;
    return true;
  }

  if (!doux) {
    poserRideau();

    document.addEventListener('click', function (ev) {
      var a = ev.target.closest ? ev.target.closest('a[href]') : null;
      if (!a || !lienInterne(a, ev)) return;
      ev.preventDefault();
      baisserRideau(a.href);
    });

    // Retour arrière depuis le cache du navigateur : on relève.
    window.addEventListener('pageshow', function (e) {
      if (!e.persisted || !rideau) return;
      rideau.style.display = '';
      rideau.classList.remove('down');
      requestAnimationFrame(function () { rideau.classList.add('up'); });
      setTimeout(function () { rideau.style.display = 'none'; }, 1600);
    });
  }

  /* ==========================================================
     2. Curseur
     ==========================================================
     Le point ne traîne pas : il colle au pixel, sinon viser
     devient pénible. Seul l'anneau retarde, et c'est lui qui
     donne la sensation de matière.
  ========================================================== */
  if (fin && !doux) {
    racine.classList.add('cur');

    var point = document.createElement('div'); point.className = 'cur-dot';
    var anneau = document.createElement('div'); anneau.className = 'cur-ring';
    point.setAttribute('aria-hidden', 'true');
    anneau.setAttribute('aria-hidden', 'true');
    document.body.appendChild(point);
    document.body.appendChild(anneau);

    var sx = window.innerWidth / 2, sy = window.innerHeight / 2;
    var ax = sx, ay = sy;

    window.addEventListener('mousemove', function (e) {
      sx = e.clientX; sy = e.clientY;
      point.style.transform = 'translate(' + sx + 'px,' + sy + 'px)';
    }, { passive: true });

    (function suivre() {
      ax += (sx - ax) * 0.16;
      ay += (sy - ay) * 0.16;
      anneau.style.transform = 'translate(' + ax + 'px,' + ay + 'px)';
      requestAnimationFrame(suivre);
    })();

    var cibles = 'a,button,summary,input,select,textarea,label,' +
                 '[role="button"],.card,.plan,.tile,.mock,.member,.rnd';
    document.addEventListener('mouseover', function (e) {
      if (e.target.closest && e.target.closest(cibles)) racine.classList.add('cur-on');
    });
    document.addEventListener('mouseout', function (e) {
      if (e.target.closest && e.target.closest(cibles)) racine.classList.remove('cur-on');
    });
    document.addEventListener('mousedown', function () { racine.classList.add('cur-press'); });
    document.addEventListener('mouseup', function () { racine.classList.remove('cur-press'); });
    document.addEventListener('mouseleave', function () { racine.classList.add('cur-out'); });
    document.addEventListener('mouseenter', function () { racine.classList.remove('cur-out'); });
  }

  /* ==========================================================
     3. Fil de lecture
  ========================================================== */
  if (!doux) {
    var fil = document.createElement('div');
    fil.className = 'prog';
    fil.setAttribute('aria-hidden', 'true');
    document.body.appendChild(fil);

    var majFil = function () {
      var course = document.body.scrollHeight - window.innerHeight;
      var p = course > 0 ? window.scrollY / course : 0;
      fil.style.transform = 'scaleX(' + borne(p, 0, 1).toFixed(4) + ')';
    };
    majFil();
    window.addEventListener('scroll', majFil, { passive: true });
    window.addEventListener('resize', majFil);
  }

  /* ==========================================================
     4. Découpage des titres
     ==========================================================
     On parcourt les enfants du titre. Un nœud de texte est
     découpé sur les espaces, en conservant les espaces tels
     quels ; un élément (un <u> souligné, un <b>) est repris
     entier dans une seule fenêtre, sans être ouvert — ce qui
     préserve le trait qui se dessine sous les mots soulignés.

     Résultat : element.textContent après découpage est
     rigoureusement identique à celui d'avant.
  ========================================================== */
  function decouper(titre) {
    if (titre.dataset.decoupe) return;

    var frag = document.createDocumentFragment();
    var noeuds = Array.prototype.slice.call(titre.childNodes);
    var rang = 0;

    var fenetre = function (contenu) {
      var w = document.createElement('span');
      w.className = 'w';
      var i = document.createElement('i');
      i.style.transitionDelay = Math.min(rang, 14) * 48 + 'ms';
      rang++;
      i.appendChild(contenu);
      w.appendChild(i);
      return w;
    };

    noeuds.forEach(function (n) {
      if (n.nodeType === 3) {                       // texte
        var morceaux = n.nodeValue.split(/(\s+)/);
        morceaux.forEach(function (m) {
          if (m === '') return;
          if (/^\s+$/.test(m)) {                    // l'espace reste un espace
            frag.appendChild(document.createTextNode(m));
          } else {
            frag.appendChild(fenetre(document.createTextNode(m)));
          }
        });
      } else if (n.nodeType === 1) {                // élément
        if (n.tagName === 'BR') { frag.appendChild(n.cloneNode(true)); return; }
        frag.appendChild(fenetre(n.cloneNode(true)));
      }
    });

    while (titre.firstChild) titre.removeChild(titre.firstChild);
    titre.appendChild(frag);
    titre.classList.add('split');
    titre.dataset.decoupe = '1';
  }

  if (!doux) {
    var titres = Array.prototype.slice.call(document.querySelectorAll('h1, h2'));
    titres.forEach(decouper);

    if ('IntersectionObserver' in window) {
      var oeil = new IntersectionObserver(function (entrees) {
        entrees.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-in');
          oeil.unobserve(e.target);
        });
      }, { rootMargin: '0px 0px -6% 0px', threshold: 0.15 });
      titres.forEach(function (t) { oeil.observe(t); });
    } else {
      titres.forEach(function (t) { t.classList.add('is-in'); });
    }
  }

  /* ==========================================================
     5. Maquettes : ouverture par volet
     ==========================================================
     On ne touche pas aux maquettes que motion.js fait déjà
     dériver en parallaxe : deux transformations sur le même
     élément se disputeraient.
  ========================================================== */
  if (!doux && 'IntersectionObserver' in window) {
    var volets = Array.prototype.slice.call(document.querySelectorAll('.tile .thumb, .face'));
    if (volets.length) {
      var oeilVolet = new IntersectionObserver(function (entrees) {
        entrees.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-in');
          oeilVolet.unobserve(e.target);
        });
      }, { rootMargin: '0px 0px -5% 0px', threshold: 0.2 });
      volets.forEach(function (v) {
        v.classList.add('rv-clip');
        oeilVolet.observe(v);
      });
    }
  }

  /* ==========================================================
     6. Lumière et inclinaison sous le curseur
     ==========================================================
     Trois degrés au maximum. Au-delà, la carte devient un jouet
     et le texte se met à onduler à la lecture.
  ========================================================== */
  if (fin && !doux) {
    var aCaler = document.querySelectorAll(
      '.card, .plan, .tile, .mock, .panel, .member, .btn, .rnd'
    );
    aCaler.forEach(function (el) {
      el.classList.add('tilt');
      // Les boutons sont déjà aimantés par motion.js : on ne leur
      // ajoute que la lumière, sinon deux transformations se
      // disputeraient le même élément.
      var incline = !el.classList.contains('btn') && !el.classList.contains('rnd');

      var lueur = document.createElement('i');
      lueur.className = 'glow';
      lueur.setAttribute('aria-hidden', 'true');
      el.appendChild(lueur);

      el.addEventListener('mousemove', function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width;
        var y = (e.clientY - r.top) / r.height;
        el.style.setProperty('--mx', (x * 100).toFixed(1) + '%');
        el.style.setProperty('--my', (y * 100).toFixed(1) + '%');
        if (incline) {
          el.style.transform =
            'perspective(1000px) rotateX(' + ((0.5 - y) * 5).toFixed(2) + 'deg)' +
            ' rotateY(' + ((x - 0.5) * 5).toFixed(2) + 'deg)' +
            ' translateY(-6px)';
        }
      });
      el.addEventListener('mouseenter', function () { el.classList.add('hot'); });
      el.addEventListener('mouseleave', function () {
        el.classList.remove('hot');
        if (incline) el.style.transform = '';
      });
    });
  }

  /* ==========================================================
     7. Élan du défilement
     ==========================================================
     La vitesse est publiée en --vel, normalisée puis amortie.
     Sans amortissement, l'inclinaison se fige quand on arrête
     de scroller, ce qui se voit tout de suite.
  ========================================================== */
  if (!doux) {
    racine.classList.add('velo');
    var dernier = window.scrollY, vitesse = 0, tourne = false;

    var amortir = function () {
      vitesse *= 0.88;
      if (Math.abs(vitesse) < 0.002) { vitesse = 0; tourne = false; }
      racine.style.setProperty('--vel', vitesse.toFixed(4));
      racine.style.setProperty('--vel-abs', Math.abs(vitesse).toFixed(4));
      if (tourne) requestAnimationFrame(amortir);
    };

    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      vitesse = borne((y - dernier) / 55, -1, 1);
      dernier = y;
      if (!tourne) { tourne = true; requestAnimationFrame(amortir); }
    }, { passive: true });
  }

  /* ==========================================================
     8. Les liens de navigation roulent
     ==========================================================
     Le mot est repris à l'identique en contenu généré : rien
     n'entre dans le document, donc rien ne change pour un
     lecteur d'écran, qui continue d'entendre le mot une fois.

     La fenêtre qui coupe est un <span> intérieur, pas le lien :
     le lien a un rembourrage vertical, et une coupe posée sur
     lui laisserait le mot remonté visible dans ce rembourrage.
  ========================================================== */
  if (fin && !doux) {
    document.querySelectorAll('.nav-links a').forEach(function (a) {
      if (a.children.length) return;              // déjà structuré, on laisse
      var mot = a.textContent;
      var fenetre = document.createElement('span');
      fenetre.className = 'roll-m';
      fenetre.setAttribute('data-roll', mot);
      var s = document.createElement('span');
      s.textContent = mot;
      fenetre.appendChild(s);
      while (a.firstChild) a.removeChild(a.firstChild);
      a.appendChild(fenetre);
      a.classList.add('roll');
    });
  }

  /* ==========================================================
     9. Le remplissage à la lecture
     ==========================================================
     Les mots d'une grande phrase s'allument un à un à mesure
     qu'on la traverse. C'est la signature du modèle : le seul
     effet du site qui suit la lecture au lieu de se déclencher
     une fois à l'entrée en vue.

     Découpage identique à celui des titres : on emballe les
     mots existants, les espaces restent des nœuds de texte.
     textContent est rigoureusement le même après coup — c'est
     ce que vérifie la comparaison mot à mot des 45 pages.

     Sûreté : la classe .fill n'est posée qu'ici. Sans elle,
     aucune règle de couleur ne s'applique et la phrase garde
     sa couleur de style.css.
  ========================================================== */
  function remplir(bloc) {
    if (bloc.dataset.rempli) return null;
    var mots = [];
    var frag = document.createDocumentFragment();
    var noeuds = Array.prototype.slice.call(bloc.childNodes);

    var emballer = function (contenu) {
      var s = document.createElement('span');
      s.className = 'fw';
      s.appendChild(contenu);
      mots.push(s);
      return s;
    };

    noeuds.forEach(function (n) {
      if (n.nodeType === 3) {
        n.nodeValue.split(/(\s+)/).forEach(function (m) {
          if (m === '') return;
          if (/^\s+$/.test(m)) frag.appendChild(document.createTextNode(m));
          else frag.appendChild(emballer(document.createTextNode(m)));
        });
      } else if (n.nodeType === 1) {
        if (n.tagName === 'BR') { frag.appendChild(n.cloneNode(true)); return; }
        frag.appendChild(emballer(n.cloneNode(true)));   // préserve <u>, <b>, <a>
      }
    });

    if (!mots.length) return null;
    while (bloc.firstChild) bloc.removeChild(bloc.firstChild);
    bloc.appendChild(frag);
    bloc.classList.add('fill');
    bloc.dataset.rempli = '1';
    return { bloc: bloc, mots: mots, pose: -1 };
  }

  if (!doux) {
    var aRemplir = [];

    /* Les grandes citations, toujours. */
    document.querySelectorAll('.quote, .quote-2').forEach(function (q) {
      var r = remplir(q);
      if (r) aRemplir.push(r);
    });

    /* Et les chapeaux longs des sections, mais pas ceux du hero :
       au-dessus de la ligne de flottaison, la phrase serait déjà
       traversée avant qu'on ait commencé à lire. */
    document.querySelectorAll('.sec .lede').forEach(function (l) {
      if (l.closest('.hero')) return;
      if ((l.textContent || '').length < 110) return;
      var r = remplir(l);
      if (r) aRemplir.push(r);
    });

    if (aRemplir.length) {
      var relire = function () {
        var h = window.innerHeight;
        aRemplir.forEach(function (e) {
          var r = e.bloc.getBoundingClientRect();
          if (r.bottom < -200 || r.top > h + 200) return;
          /* La phrase se remplit entre 78 % et 34 % de la hauteur
             de fenêtre : elle finit donc un peu avant d'arriver
             au milieu de l'écran, là où on la lit vraiment. */
          var p = (h * 0.78 - r.top) / Math.max(r.height + h * 0.44, 1);
          var n = Math.round(borne(p, 0, 1) * e.mots.length);
          if (n === e.pose) return;
          for (var i = 0; i < e.mots.length; i++) {
            e.mots[i].classList.toggle('on', i < n);
          }
          e.pose = n;
        });
      };
      var attend = false;
      window.addEventListener('scroll', function () {
        if (attend) return;
        attend = true;
        requestAnimationFrame(function () { attend = false; relire(); });
      }, { passive: true });
      window.addEventListener('resize', relire, { passive: true });
      relire();
    }
  }

  /* ==========================================================
     10. Éclats du hero
     ==========================================================
     Quatre croix citron qui scintillent très lentement au fond.
     Purement décoratives : hors flux, aria-hidden, et elles
     n'existent pas du tout si l'on a demandé moins d'animation.
  ========================================================== */
  if (!doux) {
    var hero = document.querySelector('.hero');
    if (hero) {
      for (var k = 0; k < 4; k++) {
        var e = document.createElement('i');
        e.className = 'spark';
        e.setAttribute('aria-hidden', 'true');
        hero.appendChild(e);
      }
    }
  }
})();

/* ============================================================
   11.  AMPLEUR — rail des étapes, trait des blocs de nuit,
        parallaxe d'image dans les tuiles.
   ------------------------------------------------------------
   Tout passe par des classes et des variables CSS posées ici :
   aucune balise n'est ajoutée, aucun texte n'est touché.
============================================================ */
(function () {
  'use strict';
  var doux = window.matchMedia &&
             window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* -- Le rail qui se remplit le long des étapes ------------- */
  var rails = Array.prototype.slice.call(document.querySelectorAll('.steps'));
  if (rails.length && !doux) {
    var enCours = false;
    var majRail = function () {
      enCours = false;
      var h = window.innerHeight;
      for (var i = 0; i < rails.length; i++) {
        var r = rails[i].getBoundingClientRect();
        /* 0 quand le bloc arrive au tiers bas, 1 quand il sort par le haut */
        var p = (h * 0.62 - r.top) / (r.height || 1);
        p = p < 0 ? 0 : (p > 1 ? 1 : p);
        rails[i].style.setProperty('--rail', p.toFixed(3));
      }
    };
    var planifier = function () {
      if (enCours) return;
      enCours = true;
      requestAnimationFrame(majRail);
    };
    window.addEventListener('scroll', planifier, { passive: true });
    window.addEventListener('resize', planifier);
    majRail();
  }

  /* -- Le trait de lumière au haut des blocs de nuit ---------- */
  var nuits = document.querySelectorAll('.sec-dark');
  if (nuits.length && 'IntersectionObserver' in window) {
    var oeilNuit = new IntersectionObserver(function (ent) {
      ent.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('lit');
          oeilNuit.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -12% 0px' });
    Array.prototype.forEach.call(nuits, function (n) { oeilNuit.observe(n); });
  }

  /* -- Rattrapage : tout bloc oublie par motion.js entre lui aussi -- */
  if (!doux && 'IntersectionObserver' in window) {
    var oeilBloc = new IntersectionObserver(function (ent) {
      ent.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          oeilBloc.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll('.tile, .mock, .card, .rev, .plan, .panel, .face-card')
      .forEach(function (el) {
        if (el.classList.contains('rv') || el.classList.contains('rv-l')) return;
        if (el.closest('.tile') && el.closest('.tile') !== el) return;  /* la tuile porte deja l entree */
        var freres = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) : 0;
        el.classList.add('rv');
        el.style.transitionDelay = (Math.min(freres, 8) * 70) + 'ms';
        oeilBloc.observe(el);
      });
  }

  /* -- L'image de la tuile suit la souris, de quelques pixels -- */
  if (!doux && window.matchMedia('(pointer:fine)').matches) {
    document.querySelectorAll('.tile').forEach(function (t) {
      var img = t.querySelector('.mock-h');
      if (!img) return;
      t.addEventListener('mousemove', function (e) {
        var r = t.getBoundingClientRect();
        var x = ((e.clientX - r.left) / r.width - 0.5) * 14;
        var y = ((e.clientY - r.top) / r.height - 0.5) * 10;
        img.style.backgroundPosition = 'calc(50% + ' + x.toFixed(1) + 'px) calc(50% + ' + y.toFixed(1) + 'px)';
      });
      t.addEventListener('mouseleave', function () {
        img.style.backgroundPosition = '';
      });
    });
  }
})();
