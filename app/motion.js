/* Ace motion: makes the portals feel alive without getting in the way.
   - each new screen eases in and its tiles and list rows arrive one after another
   - big numbers count up, progress bars and rings fill
   - tiles tilt toward the pointer (mouse and pen only) and every tap leaves a ripple
   - long pages reveal their lower sections as you scroll
   Everything is switched off when the device asks for reduced motion. Shared by the student app, Ace Campus and Ace Academy:
   AceMotion.view(root, key) is called after each render; it only animates when the screen (key) changes. */
(function () {
  'use strict';
  const RM = window.matchMedia ? matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };
  const FINE = window.matchMedia ? matchMedia('(hover: hover) and (pointer: fine)') : { matches: false };
  const CFG = {
    stagger: '.hm-main,.hq,.stats,.qa,.sg,.tg2,.tg,.lst,.au-subs,.au-tps,.tps,.st3,.acts,.sd,.grid,.cards,.goals,.paths,.pgrid,.tpls,.dash-r',
    tilt: '.stile,.tc,.au-sub,.sub,.card,.pcard,.au-cont,.cont',
    ripple: '.tc,.li,.stile,.au-sub,.au-tp,.au-cont,.nx,.play,.btn,.card,.pcard,.cont,.node,.tpa button,.sub',
    reveal: '.tpc,.au-mod,.box,.sd-mod>.box,.q,.lesson>h3,.lesson>.tip,.lesson>.chk'
  };
  let last = null, io = null, lastT = 0, mo = null, moRoot = null, pend = false;
  /* data that arrives just after a screen opens re-renders it outside the normal path: animate that fresh content too */
  function watch(root) {
    if (moRoot === root || !('MutationObserver' in window)) return; moRoot = root;
    mo = new MutationObserver(() => { if (pend || RM.matches || performance.now() - lastT > 2500) return; pend = true; requestAnimationFrame(() => { pend = false; const g = root.querySelector(CFG.stagger); if (g && !g.classList.contains('mx-st')) enter(root, true); }); });
    mo.observe(root, { childList: true });
  }

  function css() {
    if (document.getElementById('mx-css')) return;
    const st = document.createElement('style'); st.id = 'mx-css';
    st.textContent = `
.mx-in{animation:mxview .42s cubic-bezier(.22,1,.36,1) both}
.mx-st>*{animation:mxrise .55s cubic-bezier(.34,1.56,.64,1) both;animation-delay:calc(70ms + var(--mx,0) * 45ms)}
.mx-fill{animation:mxfill .9s cubic-bezier(.22,1,.36,1) both .15s}
.mx-ring{animation:mxring 1.1s cubic-bezier(.22,1,.36,1) both .2s}
.mx-rv{opacity:0;transform:translateY(18px);transition:opacity .5s ease,transform .6s cubic-bezier(.22,1,.36,1)}
.mx-rv.mx-seen{opacity:1;transform:none}
.mx-tl{transition:transform .25s cubic-bezier(.22,1,.36,1);will-change:transform}
.mx-tl.mx-tlon{transition:transform .08s linear}
mx-gl{display:block;position:absolute;inset:0;border-radius:inherit;pointer-events:none;background:radial-gradient(circle at var(--gx,50%) var(--gy,50%),rgba(255,255,255,.35),transparent 55%);opacity:0;transition:opacity .25s;mix-blend-mode:soft-light}
.mx-tlon>mx-gl{display:block;opacity:1}
mx-rp{display:block;position:absolute;inset:0;border-radius:inherit;overflow:hidden;pointer-events:none}
mx-rp i{position:absolute;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:var(--primary,var(--pri,currentColor));opacity:.16;transform:scale(0);animation:mxrip .6s ease-out forwards}
.mx-rel{position:relative}
@keyframes mxview{from{opacity:0;transform:translateY(14px)}}
@keyframes mxrise{from{opacity:0;transform:translateY(16px) scale(.97)}}
@keyframes mxfill{from{width:0}}
@keyframes mxring{from{stroke-dasharray:0 999}}
@keyframes mxrip{to{transform:scale(var(--rs,30));opacity:0}}
@media (prefers-reduced-motion:reduce){.mx-in,.mx-st>*,.mx-fill,.mx-ring{animation:none!important}.mx-rv{opacity:1!important;transform:none!important}}`;
    document.head.appendChild(st);
  }

  function countUp(el, to) {
    const t0 = performance.now(), ms = Math.min(1400, 500 + to * 4);
    (function f(t) { const k = Math.min(1, (t - t0) / ms), e = 1 - Math.pow(1 - k, 3); el.textContent = Math.round(to * e); if (k < 1 && el.isConnected) requestAnimationFrame(f); else el.textContent = to; })(t0);
  }

  function enter(root, again) {
    if (!root) return;
    if (!again) { root.classList.remove('mx-in'); void root.offsetWidth; root.classList.add('mx-in'); }
    root.querySelectorAll(CFG.stagger).forEach(g => {
      if (g.closest('.ls')) return;
      g.classList.remove('mx-st'); let i = 0;
      Array.from(g.children).forEach(ch => ch.style.setProperty('--mx', Math.min(i++, 14)));
      void g.offsetWidth; g.classList.add('mx-st');
    });
    root.querySelectorAll('.bar>i,.pb>i,.np>i,.bar2>i,.au-pb>i,.prog>i').forEach(b => { b.classList.remove('mx-fill'); void b.offsetWidth; b.classList.add('mx-fill'); });
    root.querySelectorAll('svg .fg,.ring circle:last-child').forEach(c => { c.classList.remove('mx-ring'); void c.getBoundingClientRect(); c.classList.add('mx-ring'); });
    root.querySelectorAll('b,strong,.num,h1,h2').forEach(el => {
      if (el.children.length || el.closest('.ls')) return; const tx = el.textContent.trim(); if (!/^\d{1,5}$/.test(tx)) return;
      const n = +tx; if (n < 2) return; const fs = parseFloat(getComputedStyle(el).fontSize) || 0; if (fs < 20) return; countUp(el, n);
    });
    reveal(root);
  }

  function reveal(root) {
    if (!('IntersectionObserver' in window)) return;
    if (!io) io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('mx-seen'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -6% 0px' });
    const h = innerHeight;
    root.querySelectorAll(CFG.reveal).forEach(el => {
      if (el.closest('.ls') || el.classList.contains('mx-rv')) return;
      const r = el.getBoundingClientRect(); if (r.top < h * 0.92) return;
      el.classList.add('mx-rv'); io.observe(el);
    });
  }

  /* pointer tilt with a soft highlight */
  let tl = null;
  function tiltMove(e) {
    if (RM.matches || !FINE.matches || e.pointerType === 'touch') return;
    const el = e.target.closest && e.target.closest(CFG.tilt); if (!el) { tiltOut(); return; } if (el !== tl) { tiltOut(); if (!el || el.closest('.ls') || el.disabled) return; tl = el; el.classList.add('mx-tl', 'mx-tlon'); if (getComputedStyle(el).position === 'static') el.classList.add('mx-rel'); if (!el.querySelector(':scope>mx-gl')) { const g = document.createElement('mx-gl'); g.setAttribute('aria-hidden', 'true'); el.appendChild(g); } }
    const r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height, m = Math.min(1, 220 / Math.max(r.width, 1));
    el.style.transform = `perspective(800px) rotateX(${((0.5 - y) * 7 * m).toFixed(2)}deg) rotateY(${((x - 0.5) * 9 * m).toFixed(2)}deg) translateY(-3px)`;
    el.style.setProperty('--gx', (x * 100).toFixed(1) + '%'); el.style.setProperty('--gy', (y * 100).toFixed(1) + '%');
  }
  function tiltOut() { if (!tl) return; tl.classList.remove('mx-tlon'); tl.style.transform = ''; tl = null; }

  /* tap ripple */
  function ripple(e) {
    if (RM.matches) return;
    const el = e.target.closest && e.target.closest(CFG.ripple); if (!el || el.disabled || el.closest('.ls')) return;
    if (getComputedStyle(el).position === 'static') el.classList.add('mx-rel');
    let w = el.querySelector(':scope>mx-rp'); if (!w) { w = document.createElement('mx-rp'); w.setAttribute('aria-hidden', 'true'); el.appendChild(w); }
    const r = el.getBoundingClientRect(), i = document.createElement('i');
    i.style.left = (e.clientX - r.left) + 'px'; i.style.top = (e.clientY - r.top) + 'px'; i.style.setProperty('--rs', Math.ceil(Math.hypot(r.width, r.height) / 6));
    w.appendChild(i); setTimeout(() => i.remove(), 650);
  }

  document.addEventListener('pointermove', tiltMove, { passive: true });
  document.addEventListener('pointerleave', tiltOut, true);
  document.addEventListener('pointerout', e => { if (tl && (!e.relatedTarget || !tl.contains(e.relatedTarget))) tiltOut(); }, { passive: true });
  document.addEventListener('pointerdown', ripple, { passive: true });
  css();

  window.AceMotion = {
    view(root, key) {
      if (!root) return; watch(root);
      if (RM.matches) { last = key; return; }
      if (key === last) { reveal(root); return; }
      last = key; lastT = performance.now(); enter(root);
    },
    enter, config: CFG
  };
})();
