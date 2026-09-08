/* ============================================================
   UP2FRONT — comportements de page
   Tout est facultatif : sans GSAP, la page reste entièrement
   lisible et utilisable. Aucun contenu ne dépend du script.
   ============================================================ */
(function(){
"use strict";

var RM   = matchMedia('(prefers-reduced-motion: reduce)').matches;
var FINE = matchMedia('(hover:hover) and (pointer:fine)').matches;
var $  = function(s,c){ return (c||document).querySelector(s); };
var $$ = function(s,c){ return Array.prototype.slice.call((c||document).querySelectorAll(s)); };

/* ---------- Mémorisation de la langue choisie ---------- */
$$('[data-language]').forEach(function(link){
  link.addEventListener('click', function(){
    try { localStorage.setItem('up2front-language', link.dataset.language); } catch (e) {}
  });
});

/* ---------- Wordmarks : filet de sécurité, jamais d'agrandissement ---------- */
function fitText(el){
  if (!el || !el.parentElement) return;
  el.style.fontSize = '';
  var avail = el.parentElement.clientWidth;
  var w = el.getBoundingClientRect().width;
  if (!avail || !w || w <= avail) return;
  var cur = parseFloat(getComputedStyle(el).fontSize);
  el.style.fontSize = (cur * avail / w * 0.97).toFixed(2) + 'px';
}
function fitAll(){ [$('#heroMark'), $('#ftMark')].forEach(fitText); }

fitAll();
if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitAll);
addEventListener('load', fitAll);
var fitTimer;
addEventListener('resize', function(){ clearTimeout(fitTimer); fitTimer = setTimeout(fitAll, 120); });
addEventListener('orientationchange', function(){ setTimeout(fitAll, 220); });

/* ---------- Nav collante + tiroir : indépendants de GSAP ---------- */
addEventListener('scroll', function(){
  var n = $('#nav'); if (n) n.classList.toggle('stuck', scrollY > 24);
}, {passive:true});

/* ---------- Onglets des offres ---------- */
(function packs(){
  var tabs = $$('.pk-tab');
  if (!tabs.length) return;
  function show(i){
    tabs.forEach(function(t,k){
      t.classList.toggle('on', k === i);
      t.setAttribute('aria-selected', k === i);
    });
    $$('.pk-c[data-t]').forEach(function(c){
      c.classList.toggle('show', c.dataset.t === String(i));
    });
  }
  tabs.forEach(function(t,i){ t.addEventListener('click', function(){ show(i); }); });
  show(0);
})();

/* ---------- Repli complet si GSAP est absent ou bloqué ---------- */
if (!window.gsap || !window.ScrollTrigger){
  $$('.rv').forEach(function(e){ e.style.opacity = 1; e.style.transform = 'none'; });
  $$('.ac-a').forEach(function(e){ e.style.height = 'auto'; });
  $$('.ac-q').forEach(function(b){
    b.setAttribute('aria-expanded','true');
    b.addEventListener('click', function(){ b.closest('.ac').classList.toggle('on'); });
  });
  (function drawerPlain(){
    var b = $('#burger'), dr = $('#drawer');
    if (!b || !dr) return;
    var open = false;
    function toggle(state){
      open = state;
      b.classList.toggle('on', open);
      b.setAttribute('aria-expanded', open);
      document.body.classList.toggle('lock', open);
      dr.style.visibility = open ? 'visible' : 'hidden';
      dr.style.transform = open ? 'translateY(0)' : 'translateY(-100%)';
    }
    b.addEventListener('click', function(){ toggle(!open); });
    $$('#drawer a').forEach(function(a){ a.addEventListener('click', function(){ toggle(false); }); });
    addEventListener('keydown', function(e){ if (e.key === 'Escape' && open) toggle(false); });
  })();
  return;
}

gsap.registerPlugin(ScrollTrigger);

/* ---------- Tiroir animé ---------- */
(function drawer(){
  var b = $('#burger'), dr = $('#drawer');
  if (!b || !dr) return;
  var open = false;
  var tl = gsap.timeline({paused:true});
  tl.set(dr, {visibility:'visible'})
    .to(dr, {y:'0%', duration:.55, ease:'expo.inOut'})
    .from('.dr-links a, .dr-foot > *', {y:26, opacity:0, duration:.45, stagger:.05, ease:'power3.out'}, '-=.28');

  function toggle(state){
    open = state;
    b.classList.toggle('on', open);
    b.setAttribute('aria-expanded', open);
    document.body.classList.toggle('lock', open);
    open ? tl.play() : tl.reverse();
  }
  b.addEventListener('click', function(){ toggle(!open); });
  $$('#drawer a').forEach(function(a){ a.addEventListener('click', function(){ toggle(false); }); });
  addEventListener('keydown', function(e){ if (e.key === 'Escape' && open) toggle(false); });
})();

/* ---------- Entrée ---------- */
(function intro(){
  var mark = $('#heroMark');
  if (mark && !RM){
    mark.innerHTML = Array.from(mark.textContent.trim())
      .map(function(c){ return '<span class="fl">' + c + '</span>'; }).join('');
    fitText(mark);
    gsap.from($$('.fl', mark), {yPercent:108, opacity:0, duration:1, stagger:.045, ease:'expo.out'});
  }
  if (RM) gsap.set('.rv', {opacity:1, y:0});
  else gsap.to('#hero .rv', {opacity:1, y:0, duration:.8, stagger:.09, ease:'power3.out', delay:.4});
})();

/* ---------- Révélations ---------- */
$$('.rv').forEach(function(el){
  if (el.closest('#hero')) return;
  gsap.to(el, {opacity:1, y:0, duration:.8, ease:'power3.out',
    scrollTrigger:{trigger:el, start:'top 92%', once:true}});
});

/* ---------- Bandeau défilant ---------- */
(function strip(){
  var box = $('#strip');
  if (!box) return;
  var row = $('.strip-row', box);
  if (!row || RM) return;
  var need = Math.ceil(innerWidth / row.scrollWidth) + 1;
  for (var i=0; i<need; i++) box.appendChild(row.cloneNode(true));
  var rows = $$('.strip-row', box), w = row.scrollWidth;
  var x = 0, prev = scrollY, v = 0;
  (function raf(){
    requestAnimationFrame(raf);
    v = v + ((scrollY - prev) * .04 - v) * .1; prev = scrollY;
    x -= .45 + Math.abs(v);
    if (x <= -w) x += w;
    rows.forEach(function(r){ r.style.transform = 'translate3d(' + x + 'px,0,0)'; });
  })();
})();

/* ---------- FAQ ---------- */
$$('.ac').forEach(function(item){
  var q = $('.ac-q', item), a = $('.ac-a', item);
  q.setAttribute('aria-expanded','false');
  q.addEventListener('click', function(){
    var was = item.classList.contains('on');
    $$('.ac.on').forEach(function(o){
      o.classList.remove('on');
      $('.ac-q', o).setAttribute('aria-expanded','false');
      gsap.to($('.ac-a', o), {height:0, duration:.4, ease:'power3.inOut'});
    });
    if (!was){
      item.classList.add('on');
      q.setAttribute('aria-expanded','true');
      gsap.to(a, {height:'auto', duration:.45, ease:'power3.inOut',
        onComplete:function(){ ScrollTrigger.refresh(); }});
    }
  });
});

/* ---------- Ancres et barre de progression ---------- */
$$('a[href^="#"]').forEach(function(a){
  a.addEventListener('click', function(e){
    var id = a.getAttribute('href');
    if (id.length < 2) return;
    var t = $(id);
    if (!t) return;
    e.preventDefault();
    var go = function(){
      scrollTo({top: t.getBoundingClientRect().top + scrollY - 8,
                behavior: RM ? 'auto' : 'smooth'});
    };
    a.closest('#drawer') ? setTimeout(go, 400) : go();
  });
});

if ($('#prog'))
  gsap.to('#prog', {scaleX:1, ease:'none',
    scrollTrigger:{trigger:document.body, start:'top top', end:'bottom bottom', scrub:.3}});

/* ---------- Wordmark de pied ---------- */
(function ft(){
  var el = $('#ftMark');
  if (!el) return;
  el.innerHTML = Array.from(el.textContent.trim())
    .map(function(c){ return '<span class="fl">' + c + '</span>'; }).join('');
  var sp = $$('.fl', el);
  fitText(el);
  gsap.from(sp, {yPercent:105, opacity:0, duration:.85, ease:'expo.out', stagger:.04,
    scrollTrigger:{trigger:el, start:'top 96%', once:true}});
  if (!FINE || RM) return;
  el.addEventListener('mousemove', function(e){
    sp.forEach(function(l){
      var r = l.getBoundingClientRect();
      var k = Math.max(0, 1 - Math.abs(e.clientX - (r.left + r.width/2)) / 220);
      gsap.to(l, {y:-k*14, color: k>.5 ? '#FFC400' : 'rgba(251,251,250,.11)',
                  duration:.5, ease:'power3.out'});
    });
  });
  el.addEventListener('mouseleave', function(){
    gsap.to(sp, {y:0, color:'rgba(251,251,250,.11)', duration:.8, ease:'elastic.out(1,.5)'});
  });
})();

addEventListener('load', function(){ ScrollTrigger.refresh(); });
})();
