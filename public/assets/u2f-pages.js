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
   (--k). On ne le charge qu'à l'approche de l'écran, pour ne pas payer
   trois sites au chargement de la page.
   --------------------------------------------------------------------- */
var cadres = qq('[data-cadre]');
if(cadres.length){
  var LARGEUR_REF = 1440;

  var ajuster = function(cadre){
    var k = cadre.clientWidth / LARGEUR_REF;
    if(!k) return;
    cadre.style.setProperty('--k', k);
    var f = q('iframe', cadre);
    if(f) f.style.height = (cadre.clientHeight / k) + 'px';
  };

  var charger = function(cadre){
    var f = q('iframe', cadre);
    if(!f || f.src) return;
    f.addEventListener('load', function(){ cadre.classList.add('est-prete'); });
    f.src = f.getAttribute('data-src');
  };

  cadres.forEach(ajuster);

  if(window.ResizeObserver){
    var ro = new ResizeObserver(function(entrees){
      entrees.forEach(function(e){ ajuster(e.target); });
    });
    cadres.forEach(function(c){ ro.observe(c); });
  }else{
    window.addEventListener('resize', function(){ cadres.forEach(ajuster); });
  }

  if(window.IntersectionObserver){
    var io = new IntersectionObserver(function(entrees, obs){
      entrees.forEach(function(e){
        if(!e.isIntersecting) return;
        charger(e.target);
        obs.unobserve(e.target);
      });
    }, { rootMargin: '400px' });
    cadres.forEach(function(c){ io.observe(c); });
  }else{
    cadres.forEach(charger);
  }
}

/* ---------------------------------------------------------------------
   5 · Aperçu plein écran — voir le site sans quitter le nôtre
   --------------------------------------------------------------------- */
var apercu = q('#apercu');
if(apercu){
  var vue      = q('[data-vue]', apercu);
  var nomEl    = q('[data-nom]', apercu);
  var hoteEl   = q('[data-hote]', apercu);
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

  var ouvrir = function(url, nom, hote, source){
    appelant = source || null;
    if(nomEl)  nomEl.textContent  = nom  || '';
    if(hoteEl) hoteEl.textContent = hote || '';
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
             b.getAttribute('data-nom'),
             b.getAttribute('data-hote'), b);
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
