/* =====================================================================
   Up2Front — comportements des pages intérieures
   Volontairement indépendant de GSAP : si un CDN tombe, le menu, les
   options de commande et le total continuent de fonctionner.
   ===================================================================== */
(function(){
"use strict";

var q  = function(s,r){ return (r||document).querySelector(s); };
var qq = function(s,r){ return Array.prototype.slice.call((r||document).querySelectorAll(s)); };

/* ---------------------------------------------------------------------
   1 · Menu mobile
   --------------------------------------------------------------------- */
var burger = q('.burger');
var menu   = q('.menu-mobile');
if(burger && menu){
  burger.addEventListener('click', function(){
    var ouvert = burger.getAttribute('aria-expanded') === 'true';
    burger.setAttribute('aria-expanded', String(!ouvert));
    burger.setAttribute('aria-label', ouvert ? 'Ouvrir le menu' : 'Fermer le menu');
    menu.hidden = ouvert;
    document.documentElement.style.overflow = ouvert ? '' : 'hidden';
  });
  qq('a', menu).forEach(function(a){
    a.addEventListener('click', function(){
      burger.setAttribute('aria-expanded','false');
      menu.hidden = true;
      document.documentElement.style.overflow = '';
    });
  });
  /* un passage au grand écran ne doit pas laisser le menu ouvert */
  window.matchMedia('(min-width:901px)').addEventListener('change', function(e){
    if(e.matches){
      burger.setAttribute('aria-expanded','false');
      menu.hidden = true;
      document.documentElement.style.overflow = '';
    }
  });
}

/* ---------------------------------------------------------------------
   2 · Tunnel de commande — total vivant
   Chaque option porte data-prix ; le total et le libellé du bouton se
   recalculent à chaque changement. Le montant réellement débité reste
   celui de Stripe : les options sont transmises en paramètres.
   --------------------------------------------------------------------- */
var form = q('[data-commande]');
if(form){
  var base    = parseFloat(form.getAttribute('data-base')) || 0;
  var devise  = form.getAttribute('data-devise') || 'CHF';
  var sortie  = q('[data-total]', form);
  var libelle = q('[data-total-bouton]', form);
  var lignes  = q('[data-lignes-options]', form);
  var options = qq('input[data-prix]', form);

  var fmt = function(n){
    return devise + ' ' + n.toLocaleString('fr-CH', {minimumFractionDigits:0});
  };

  var recalculer = function(){
    var total = base;
    var html  = '';
    options.forEach(function(o){
      if(o.checked){
        var p = parseFloat(o.getAttribute('data-prix')) || 0;
        total += p;
        html += '<div class="ligne"><span>' + o.getAttribute('data-nom') +
                '</span><span>+ ' + p + '.—</span></div>';
      }
    });
    if(lignes) lignes.innerHTML = html;
    if(sortie)  sortie.textContent  = fmt(total);
    if(libelle) libelle.textContent = fmt(total);
    form.setAttribute('data-total-courant', String(total));
  };

  options.forEach(function(o){ o.addEventListener('change', recalculer); });
  recalculer();

  /* les coordonnées : mémorisées d'une page à l'autre, et l'adresse e-mail
     part sur Stripe pour que la commande retombe sur la bonne personne. */
  var champs = qq('[data-coord]', form);
  var memoire = function(){
    try{
      champs.forEach(function(c){
        var v = sessionStorage.getItem('u2f-' + c.name);
        if(v && !c.value) c.value = v;
      });
    }catch(e){}
  };
  memoire();
  champs.forEach(function(c){
    c.addEventListener('input', function(){
      try{ sessionStorage.setItem('u2f-' + c.name, c.value); }catch(e){}
    });
  });

  var courriel = function(){
    var c = champs.filter(function(x){ return x.name === 'email'; })[0];
    return c ? c.value.trim() : '';
  };
  var valide = function(v){ return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v); };

  /* départ vers Stripe : on emporte les options choisies, pour que la
     commande arrivée dans Notion soit complète même si le montant Stripe
     ne couvre que le forfait de base. */
  var bouton = q('[data-payer]', form);
  var erreur = q('[data-erreur]', form);
  if(bouton){
    bouton.addEventListener('click', function(e){
      e.preventDefault();
      var url = form.getAttribute('data-stripe');
      if(!url) return;

      var mail = courriel();
      if(!valide(mail)){
        if(erreur){
          erreur.textContent = 'Indiquez une adresse e-mail valide : c’est là que le brief et le site vous seront envoyés.';
          erreur.hidden = false;
        }
        var champMail = champs.filter(function(x){ return x.name === 'email'; })[0];
        if(champMail) champMail.focus();
        return;
      }
      if(erreur) erreur.hidden = true;

      /* on emporte les clés courtes (« langue », « logo ») et non les
         libellés : les accents survivent mal dans une référence Stripe, et
         Make attend une valeur stable. */
      var choisies = options.filter(function(o){ return o.checked; })
                            .map(function(o){ return o.getAttribute('data-cle') ||
                                                     o.getAttribute('data-nom'); });
      var sep = url.indexOf('?') < 0 ? '?' : '&';
      var ref = form.getAttribute('data-offre') +
                (choisies.length ? '|' + choisies.join('|') : '');
      window.location.href = url + sep +
        'client_reference_id=' + encodeURIComponent(ref.replace(/[^A-Za-z0-9|_-]/g,'-')) +
        '&prefilled_email=' + encodeURIComponent(mail);
    });
  }
}

/* ---------------------------------------------------------------------
   3 · Code promotionnel — un champ qui ne ment pas
   Aucun code n'est validé côté navigateur : la remise se fait sur Stripe.
   --------------------------------------------------------------------- */
var promo = q('[data-promo]');
if(promo){
  var champPromo = q('input', promo);
  var motPromo   = q('[data-promo-message]', promo);
  var btnPromo   = q('button', promo);
  if(btnPromo){
    btnPromo.addEventListener('click', function(e){
      e.preventDefault();
      if(!motPromo) return;
      motPromo.textContent = (champPromo && champPromo.value.trim())
        ? 'Code noté. Il sera appliqué sur la page de paiement.'
        : 'Saisissez un code avant de valider.';
    });
  }
}

/* ---------------------------------------------------------------------
   4 · Sites en ligne — la vignette est le site, pas une capture
   Le site est chargé dans un cadre de 1440 px puis réduit par homothétie
   (--k).

   Le chargement a d'abord attendu le survol, pour épargner la page : trois
   sites complets qui s'ajoutent au nôtre, cela se sent. Mais un visiteur qui
   ne survole pas ne voyait qu'un dessin d'attente à l'endroit exact où le
   travail doit se prouver. C'est cher payé pour quelques dixièmes de seconde.
   On charge donc à l'approche de l'écran — et un seul site à la fois, le
   suivant partant quand le précédent a fini (ou au bout d'une seconde et
   demie, si le réseau traîne). Le survol reste un déclencheur : celui qui va
   droit sur la carte n'attend pas son tour. Une fois chargé, le cadre reste :
   on ne paie qu'une fois.
   --------------------------------------------------------------------- */
var cadres = qq('[data-cadre]');
if(cadres.length){
  var LARGEUR_REF = 1440;

  /* Un seul site vivant à la fois — sur téléphone comme sur ordinateur.
     Une vignette, c'est un navigateur complet de 1440 px de large qui charge
     un vrai site, avec ses images, ses polices et son propre moteur
     d'animation. Trois de ces cadres tenaient sur un ordinateur de bureau,
     et sur un iPhone ils s'ajoutaient aux 1,5 Go que Safari accorde à un
     onglet : le système tuait l'onglet — « Un problème récurrent est
     survenu », puis rechargement complet.
     Ils ne tiennent pas mieux que ça sur un portable ordinaire : la page
     saccade, le défilement colle, et c'est ce qu'on nous a signalé. La règle
     du téléphone devient donc la règle partout : celui qui est à l'écran
     charge, ceux qui s'en éloignent sont déchargés et rendent leur mémoire.
     La hauteur chargée retombe à un écran pour les mêmes raisons : 2,6
     écrans de haut, c'est 2,6 fois le travail de rendu pour un effet de
     survol. Cet effet revient dès qu'une capture remplace le site vivant —
     faire défiler une image ne coûte rien. */
  var PETIT = window.matchMedia('(max-width:900px)').matches;

  var ajuster = function(cadre){
    var k = cadre.clientWidth / LARGEUR_REF;
    if(!k) return;
    cadre.style.setProperty('--k', k);
    var img = q('img.cap', cadre);
    var f = img ? null : q('iframe', cadre);
    if(!img && !f) return;

    /* Le cas de la capture. « --defile » est la course exacte, en pixels du
       cadre : ce que l'image dépasse en hauteur, plafonné à ce que data-haut
       autorise. On la calcule ici parce que le CSS ne connaît ni la hauteur
       du cadre ni celle de l'image. Tant que l'image n'est pas décodée,
       naturalHeight vaut 0 et la course reste nulle — le rendez-vous est
       repris au « load » de l'image, plus bas. */
    var haut = parseFloat(cadre.getAttribute('data-haut')) || 1;
    if(img){
      var course = (img.naturalHeight || 0) * k - cadre.clientHeight;
      var plafond = PETIT ? 0 : cadre.clientHeight * (haut - 1);
      cadre.style.setProperty('--defile',
        '-' + Math.max(0, Math.round(Math.min(course, plafond))) + 'px');
      return;
    }

    /* Le cas du site vivant : une hauteur d'écran, pas davantage, et donc
       pas de course de survol. C'est le prix à payer pour que la page reste
       fluide tant qu'on n'a pas de captures. */
    f.style.height = (cadre.clientHeight / k) + 'px';
    cadre.style.setProperty('--defile', '0px');
  };

  cadres.forEach(ajuster);
  /* Une capture arrive après coup : sa hauteur naturelle n'est connue qu'une
     fois décodée. On rejoue le calcul à ce moment-là. */
  cadres.forEach(function(cadre){
    var img = q('img.cap', cadre);
    if(img && !img.complete){
      img.addEventListener('load', function(){ ajuster(cadre); }, { once:true });
    }
  });

  if(window.ResizeObserver){
    var ro = new ResizeObserver(function(entrees){
      entrees.forEach(function(e){ ajuster(e.target); });
    });
    cadres.forEach(function(c){ ro.observe(c); });
  }else{
    window.addEventListener('resize', function(){ cadres.forEach(ajuster); });
  }

  /* Le chargement. Quatre stratégies se sont succédé ici, et il faut dire
     pourquoi on en est à la quatrième.

     1. À l'approche de l'écran, les trois d'un coup : la page piquait du nez au
        moment où la galerie arrivait.
     2. Au survol seulement : celui qui ne survolait pas ne voyait rien, à
        l'endroit précis où le travail doit se prouver.
     3. À l'approche, un site à la fois, en file : mieux, mais la vignette
        restait un rectangle teinté le temps que le tour vienne — et sur trois
        sites qui chargent des photos, ce temps se comptait en secondes.
     4. Les trois ensemble dès que NOTRE page avait fini de charger la sienne.
        La vignette était belle et la page ramait : trois navigateurs complets
        qui s'animent en même temps, cela se voit au défilement.

     Aujourd'hui : un seul cadre vivant, celui qui est à l'écran, sur tous les
     formats. La bonne réponse n'est pas là de toute façon — elle est dans une
     capture d'écran, qui pèse cent fois moins et montre la même chose. Le
     champ « capture » de donnees.py attend le fichier ; tant qu'il est vide,
     ce qui suit tient la maison debout. */
  var charger = function(cadre){
    var f = q('iframe', cadre);
    if(!f || f.src) return;               /* déjà parti : rien à faire */
    f.addEventListener('load', function(){ cadre.classList.add('est-prete'); },
                       { once:true });
    /* Filet. Si « load » ne vient jamais — une police, une photo qui traîne —
       on montre quand même au bout de cinq secondes ce qui est arrivé : mieux
       vaut le site à demi peint que le voile de couleur. Le minuteur est
       gardé : un cadre déchargé entre-temps ne doit pas se voir déclaré prêt
       par le minuteur de son chargement précédent, ce qui montrerait le blanc
       d'une page vide. */
    if(cadre.__filet) clearTimeout(cadre.__filet);
    cadre.__filet = setTimeout(function(){
      cadre.classList.add('est-prete');
    }, 5000);
    f.src = f.getAttribute('data-src');
  };

  /* Décharger, c'est retirer le « src » : le cadre redevient une page vide et
     le navigateur rend la mémoire du site, de ses images et de ses scripts.
     On enlève aussi « est-prete » pour que le fond teinté reprenne sa place,
     sinon on verrait le blanc de la page vide au travers. */
  var decharger = function(cadre){
    var f = q('iframe', cadre);
    if(!f || !f.src) return;
    if(cadre.__filet){ clearTimeout(cadre.__filet); cadre.__filet = null; }
    cadre.classList.remove('est-prete');
    f.removeAttribute('src');
  };

  /* Les cadres qui portent une capture n'ont pas d'iframe : ils sont déjà
     servis, et rien ne doit se charger pour eux. On ne fait la file d'attente
     qu'avec ceux qui restent. */
  cadres = cadres.filter(function(c){ return !q('img.cap', c); });

  if(cadres.length && PETIT && window.IntersectionObserver){
    /* Téléphone. Un seul cadre vivant, jamais deux : le cadre le plus proche
       du centre de l'écran gagne, les autres rendent leur mémoire. On ne se
       contente pas de « entre dans l'écran / sort de l'écran » : au milieu
       d'un défilement, deux cadres peuvent être visibles ensemble, et c'est
       précisément ce qu'on veut éviter. */
    var vus = [];
    var arbitrer = function(){
      var milieu = window.innerHeight / 2, meilleur = null, ecart = Infinity;
      vus.forEach(function(c){
        var r = c.getBoundingClientRect();
        var d = Math.abs((r.top + r.bottom) / 2 - milieu);
        if(d < ecart){ ecart = d; meilleur = c; }
      });
      cadres.forEach(function(c){
        if(c === meilleur) charger(c); else decharger(c);
      });
    };
    var io = new IntersectionObserver(function(entrees){
      entrees.forEach(function(e){
        var i = vus.indexOf(e.target);
        if(e.isIntersecting){ if(i < 0) vus.push(e.target); }
        else if(i >= 0){ vus.splice(i, 1); }
      });
      arbitrer();
    }, { rootMargin: '10% 0px' });
    cadres.forEach(function(c){ io.observe(c); });
  }else if(cadres.length && window.IntersectionObserver){
    /* Ordinateur. La mémoire n'est pas le problème ici — le nôtre est que
       trois navigateurs complets démarraient à la même seconde, chacun avec
       ses photos, ses polices et son moteur d'animation. C'est ce chevauchement
       qui faisait saccader la page, pas le nombre de cadres une fois posés.
       On charge donc en file : un site part, le suivant attend qu'il ait fini
       — ou une seconde et demie, si le réseau traîne. Rien ne se décharge : le
       visiteur qui remonte retrouve la galerie telle qu'il l'a laissée.
       Et rien ne part avant que la galerie approche de l'écran : une visite
       qui s'arrête au premier écran ne paie aucun de ces trois chargements. */
    var file = cadres.slice(), enCours = false;
    var suivant = function(){
      if(enCours) return;
      var cadre = file.shift();
      if(!cadre) return;
      var f = q('iframe', cadre);
      if(!f || f.src){ suivant(); return; }
      enCours = true;
      var passer = function(){
        if(!enCours) return;
        enCours = false;
        clearTimeout(minuteur);
        suivant();
      };
      var minuteur = setTimeout(passer, 1500);
      f.addEventListener('load', passer, { once:true });
      charger(cadre);
    };
    /* Doubler la file : le cadre survolé passe devant. Celui qui va droit sur
       une carte n'a pas à attendre le tour des deux autres. */
    var devant = function(cadre){
      var i = file.indexOf(cadre);
      if(i > 0){ file.splice(i, 1); file.unshift(cadre); }
      suivant();
    };
    var io = new IntersectionObserver(function(entrees){
      var vu = false;
      entrees.forEach(function(e){ if(e.isIntersecting) vu = true; });
      if(vu) suivant();
    }, { rootMargin: '25% 0px' });
    cadres.forEach(function(cadre){
      io.observe(cadre);
      var zone = cadre.closest ? (cadre.closest('.cas') || cadre.closest('.site') || cadre)
                               : cadre;
      var lancer = function(){ devant(cadre); };
      ['pointerenter','focusin'].forEach(function(evt){
        zone.addEventListener(evt, lancer, { once:true, passive:true });
      });
    });
  }else{
    /* Sans IntersectionObserver — de très vieux navigateurs — on ne sait pas
       dire lequel est à l'écran. On s'en tient alors au survol : rien ne part
       tout seul, donc rien ne peut faire trois chargements d'un coup. La
       vignette reste un voile teinté pour qui ne survole pas, ce qui est le
       moindre mal face à une page qui saccade. */
    cadres.forEach(function(cadre){
      var zone = cadre.closest ? (cadre.closest('.cas') || cadre.closest('.site') || cadre)
                               : cadre;
      var lancer = function(){ charger(cadre); };
      ['pointerenter','focusin','touchstart'].forEach(function(evt){
        zone.addEventListener(evt, lancer, { once:true, passive:true });
      });
    });
  }
}

/* ---------------------------------------------------------------------
   5 · Aperçu plein écran — voir le site sans quitter le nôtre
   --------------------------------------------------------------------- */
var apercu = q('#apercu');
if(apercu){
  var vue      = q('[data-vue]', apercu);
  var nomEl    = q('[data-nom]', apercu);
  /* L'en-tête portait aussi l'hôte du site — « smash-house-984.netlify.app ».
     Il a été retiré du gabarit : le nom de l'hébergeur n'apprend rien au
     visiteur et faisait passer un site fini pour un essai gratuit. L'adresse
     réelle reste dans « Ouvrir dans un onglet ↗ », à un clic. */
  var lienEl   = q('[data-lien]', apercu);
  var boutLarg = qq('[data-larg]', apercu);
  var appelant = null;   /* le bouton qui a ouvert : on lui rend le focus */

  var largeur = function(mode){
    apercu.classList.toggle('est-mobile', mode === 'mobile');
    boutLarg.forEach(function(b){
      b.setAttribute('aria-pressed',
        String(b.getAttribute('data-larg') === mode));
    });
  };

  var ouvrir = function(url, nom, source){
    appelant = source || null;
    if(nomEl)  nomEl.textContent  = nom  || '';
    if(lienEl) lienEl.href = url;
    if(vue){
      vue.setAttribute('title', 'Aperçu du site ' + (nom || ''));
      vue.src = url;
    }
    largeur('bureau');
    apercu.hidden = false;
    document.documentElement.style.overflow = 'hidden';
    if(window.u2fLenis) window.u2fLenis.stop();
    requestAnimationFrame(function(){ apercu.classList.add('est-ouvert'); });
    var x = q('.apercu-x', apercu);
    if(x) x.focus();
  };

  var fermer = function(){
    apercu.classList.remove('est-ouvert');
    document.documentElement.style.overflow = '';
    if(window.u2fLenis) window.u2fLenis.start();
    window.setTimeout(function(){
      apercu.hidden = true;
      if(vue) vue.removeAttribute('src');   /* on coupe scripts et sons */
    }, 320);
    if(appelant && appelant.focus) appelant.focus();
    appelant = null;
  };

  qq('[data-apercu]').forEach(function(b){
    b.addEventListener('click', function(){
      ouvrir(b.getAttribute('data-apercu'),
             b.getAttribute('data-nom'), b);
    });
  });

  qq('[data-fermer]', apercu).forEach(function(b){
    b.addEventListener('click', fermer);
  });

  boutLarg.forEach(function(b){
    b.addEventListener('click', function(){ largeur(b.getAttribute('data-larg')); });
  });

  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && !apercu.hidden) fermer();
  });
}

/* ---------------------------------------------------------------------
   6 · Année du pied de page, si un jour elle est marquée
   --------------------------------------------------------------------- */
qq('[data-annee]').forEach(function(el){
  el.textContent = String(new Date().getFullYear());
});

})();
