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
   4 · Année du pied de page, si un jour elle est marquée
   --------------------------------------------------------------------- */
qq('[data-annee]').forEach(function(el){
  el.textContent = String(new Date().getFullYear());
});

})();
