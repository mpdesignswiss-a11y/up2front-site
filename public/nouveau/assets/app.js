/* Up2Front — interactions */
(function () {
  /* code promo : copie au clic */
  document.querySelectorAll('[data-copy]').forEach(function (el) {
    el.addEventListener('click', function () {
      navigator.clipboard && navigator.clipboard.writeText(el.dataset.copy);
      var t = el.textContent; el.textContent = 'Copié ✓';
      setTimeout(function () { el.textContent = t; }, 1600);
    });
  });

  /* filtres portfolio */
  var fbtns = document.querySelectorAll('.filters button');
  fbtns.forEach(function (b) {
    b.addEventListener('click', function () {
      fbtns.forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      var f = b.dataset.filter;
      document.querySelectorAll('[data-cat]').forEach(function (t) {
        t.style.display = (f === 'all' || t.dataset.cat === f) ? '' : 'none';
      });
    });
  });

  /* compte à rebours (offres uniques) */
  document.querySelectorAll('[data-countdown]').forEach(function (c) {
    var end = Date.now() + parseInt(c.dataset.countdown, 10) * 1000;
    var out = c.querySelectorAll('b');
    (function tick() {
      var s = Math.max(0, Math.floor((end - Date.now()) / 1000));
      var v = [Math.floor(s / 86400), Math.floor(s / 3600) % 24, Math.floor(s / 60) % 60, s % 60];
      out.forEach(function (o, i) { o.textContent = String(v[i]).padStart(2, '0'); });
      if (s > 0) setTimeout(tick, 1000);
    })();
  });

  /* choix du moyen de paiement */
  document.querySelectorAll('.pay .opt').forEach(function (o) {
    o.addEventListener('click', function () {
      o.parentNode.querySelectorAll('.opt').forEach(function (x) { x.classList.remove('on'); });
      o.classList.add('on');
      var r = o.querySelector('input'); if (r) r.checked = true;
    });
  });

  /* récapitulatif de commande : options additionnelles */
  var sum = document.querySelector('[data-base]');
  if (sum) {
    var base = parseInt(sum.dataset.base, 10);
    var lines = document.getElementById('sum-lines');
    var totals = document.querySelectorAll('[data-total]');
    function refresh() {
      var extra = 0, html = '';
      document.querySelectorAll('.bump input[type=checkbox]').forEach(function (cb) {
        cb.closest('.bump').classList.toggle('on', cb.checked);
        if (cb.checked) {
          extra += parseInt(cb.dataset.price, 10);
          html += '<div class="sum-row"><span>' + cb.dataset.name + '</span><span>CHF ' +
                  cb.dataset.price + '.00</span></div>';
        }
      });
      if (lines) lines.innerHTML = html;
      totals.forEach(function (t) { t.textContent = 'CHF ' + (base + extra); });
    }
    document.querySelectorAll('.bump input[type=checkbox]').forEach(function (cb) {
      cb.addEventListener('change', refresh);
    });
    refresh();
  }

  /* formulaires branchés sur un lien de paiement Stripe */
  document.querySelectorAll('form[data-stripe]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var u = f.dataset.stripe;
      if (!u) return;
      var q = [];
      var mail = f.querySelector('input[type=email]');
      if (mail && mail.value) q.push('prefilled_email=' + encodeURIComponent(mail.value));
      location.href = u + (q.length ? (u.indexOf('?') < 0 ? '?' : '&') + q.join('&') : '');
    });
  });

  /* formulaires de démonstration */
  document.querySelectorAll('form[data-demo]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var n = f.dataset.demo;
      if (n) location.href = n;
    });
  });
})();

/* ---- places restantes : varie automatiquement dans la semaine (1 à 4) ---- */
(function () {
  var el = document.querySelectorAll('[data-spots]');
  if (!el.length) return;
  // lundi 4 → vendredi 1, week-end intermédiaire : toujours entre 1 et 4
  var parSemaine = [3, 4, 4, 3, 2, 1, 2];       // dim, lun, mar, mer, jeu, ven, sam
  var d = new Date();
  var n = parSemaine[d.getDay()];
  // légère variation selon la semaine de l'année, sans jamais sortir de 1–4
  var sem = Math.floor((d - new Date(d.getFullYear(), 0, 1)) / 604800000);
  if (sem % 3 === 0 && n > 1) n -= 1;
  el.forEach(function (e) { e.textContent = n; });
})();

/* ---- minuteur « votre place est réservée » ---- */
document.querySelectorAll('[data-hold]').forEach(function (h) {
  var s = parseInt(h.dataset.hold, 10);
  (function tick() {
    var m = Math.floor(s / 60), sec = s % 60;
    h.textContent = m + ':' + String(sec).padStart(2, '0');
    if (s-- > 0) setTimeout(tick, 1000);
  })();
});

/* ---- flèches des carrousels ---- */
document.querySelectorAll('[data-scroll]').forEach(function (b) {
  b.addEventListener('click', function () {
    var box = document.getElementById('cas-scroll');
    if (box) box.scrollBy({ left: parseInt(b.dataset.scroll, 10) * 440, behavior: 'smooth' });
  });
});
