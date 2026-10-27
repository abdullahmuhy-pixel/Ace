/* Ace UI runtime: device layouts, Ace the pencil, sound effects, read-aloud, confetti and lesson motion.
   The app rebuilds #v on every click, so motion is driven by state changes noticed after each render
   (a new question key plays the entrance; a change to "ok"/"no" plays the feedback), never by the rebuild itself. */
(function () {
  'use strict';
  const H = document.documentElement, $ = s => document.querySelector(s), $$ = s => Array.from(document.querySelectorAll(s));
  const RM = matchMedia('(prefers-reduced-motion: reduce)');
  const pref = () => { try { return P; } catch (e) { return window.P || {}; } };
  if (pref() && typeof pref() === 'object' && pref() === (function () { try { return P; } catch (e) { return null; } })()) { if (P.snd == null) P.snd = true; if (P.voice == null) P.voice = false; if (P.vc == null) P.vc = 'melodic'; }

  /* ---------- device ---------- */
  function device() {
    const w = innerWidth, coarse = matchMedia('(pointer: coarse)').matches;
    if (w < 700) return 'mobile';
    if (w < 1100 || (coarse && w < 1280)) return 'tablet';
    return 'desktop';
  }
  function setDevice() { const d = device(); if (H.dataset.device !== d) H.dataset.device = d; }
  setDevice(); addEventListener('resize', setDevice); addEventListener('orientationchange', setDevice);

  /* ---------- Ace the pencil ---------- */
  const SVG = `<svg viewBox="0 0 100 140" aria-hidden="true"><g class="a-all" stroke="#17123A" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<path class="a-arm-l" d="M27 70 L13 84" fill="none"/><circle class="a-arm-l" cx="12" cy="85" r="3.5" fill="#FFC72C"/>
<path class="a-arm-r" d="M73 70 L87 84" fill="none"/><circle class="a-arm-r" cx="88" cy="85" r="3.5" fill="#FFC72C"/>
<rect x="29" y="7" width="42" height="19" rx="9" fill="#FF8FB1"/>
<rect x="27" y="24" width="46" height="13" rx="2" fill="#CBD0EC"/><path d="M27 30.5h46" fill="none" stroke-width="2"/>
<path d="M27 37h46v61H27z" fill="#FFC72C"/><path d="M27 37h11v61H27z" fill="#F2AE12" stroke="none"/><path d="M62 37h11v61H62z" fill="#FFDB6E" stroke="none"/><path d="M27 37h46v61H27z" fill="none"/>
<path d="M27 98h46L50 133z" fill="#F7D9AE"/><path d="M42.6 121.6h14.8L50 133z" fill="#3B3358"/>
<g class="a-eyes"><ellipse cx="41" cy="60" rx="6" ry="7" fill="#fff"/><ellipse cx="59" cy="60" rx="6" ry="7" fill="#fff"/>
<g class="a-pupils" stroke="none" fill="#17123A"><circle cx="42" cy="61" r="3.3"/><circle cx="60" cy="61" r="3.3"/><circle cx="43.2" cy="59.6" r="1.1" fill="#fff"/><circle cx="61.2" cy="59.6" r="1.1" fill="#fff"/></g></g>
<g stroke="none" fill="#FF8FB1" opacity=".75"><ellipse cx="34" cy="73" rx="4" ry="2.6"/><ellipse cx="66" cy="73" rx="4" ry="2.6"/></g>
<path class="mo m-smile" d="M43 73 Q50 80 57 73" fill="none"/>
<path class="mo m-open" d="M42.5 71.5 Q50 86 57.5 71.5 Z" fill="#17123A"/>
<path class="mo m-oops" d="M44 77 Q50 71.5 56 77" fill="none"/>
<path class="mo m-think" d="M45 76 L56 73.5" fill="none"/>
<path class="brow" d="M35 50 L45 48.5 M55 48.5 L65 50" fill="none" stroke-width="2.5"/>
<g class="a-spark" fill="#FFC72C" stroke-width="2"><path d="M12 22l3 7 7 3-7 3-3 7-3-7-7-3 7-3z"/><path d="M86 12l2.4 5.6 5.6 2.4-5.6 2.4L86 28l-2.4-5.6L78 20l5.6-2.4z"/></g>
<path class="a-drop" d="M80 40 Q84 47 80 50 Q76 47 80 40z" fill="#8FD3FF" stroke-width="2"/>
</g></svg>`;
  function fillAce(root) { (root || document).querySelectorAll('.ace').forEach(e => { if (!e.firstChild) e.innerHTML = SVG; }); }

  /* ---------- sound (synthesised, no files) ---------- */
  let AC = null;
  function ctx() { if (!AC) { try { AC = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { AC = null; } } if (AC && AC.state === 'suspended') AC.resume(); return AC; }
  function tone(f, t0, d, o) {
    const a = ctx(); if (!a) return; o = o || {};
    const os = a.createOscillator(), g = a.createGain(), st = a.currentTime + t0;
    os.type = o.type || 'sine'; os.frequency.setValueAtTime(f, st); if (o.to) os.frequency.exponentialRampToValueAtTime(o.to, st + d);
    g.gain.setValueAtTime(0.0001, st); g.gain.exponentialRampToValueAtTime(o.v || 0.12, st + 0.012); g.gain.exponentialRampToValueAtTime(0.0001, st + d);
    let n = os; if (o.lp) { const f2 = a.createBiquadFilter(); f2.type = 'lowpass'; f2.frequency.value = o.lp; os.connect(f2); n = f2; }
    n.connect(g); g.connect(a.destination); os.start(st); os.stop(st + d + 0.05);
  }
  const FX = {
    on: () => pref().snd !== false,
    tap() { if (FX.on()) tone(540, 0, 0.05, { v: 0.035, type: 'triangle' }); },
    pick() { if (FX.on()) tone(620, 0, 0.09, { v: 0.07, type: 'triangle', to: 880 }); },
    ok() { if (!FX.on()) return; [784, 988, 1319].forEach((f, i) => { tone(f, i * 0.075, 0.32, { v: 0.11 }); tone(f * 2, i * 0.075, 0.18, { v: 0.025, type: 'triangle' }); }); },
    no() { if (FX.on()) { tone(220, 0, 0.22, { v: 0.12, type: 'sawtooth', to: 130, lp: 700 }); tone(165, 0.09, 0.26, { v: 0.08, type: 'square', to: 110, lp: 500 }); } },
    done() { if (!FX.on()) return; [523, 659, 784, 1047, 1319].forEach((f, i) => tone(f, i * 0.09, 0.42, { v: 0.1 })); [1568, 2093].forEach((f, i) => tone(f, 0.5 + i * 0.06, 0.5, { v: 0.03, type: 'triangle' })); },
    combo(n) { if (FX.on()) tone(880 + Math.min(n, 8) * 70, 0.32, 0.16, { v: 0.05, type: 'triangle' }); }
  };

  /* ---------- read aloud ---------- */
  const SY = window.speechSynthesis;
  function say(text, onend) {
    if (!SY || !text) { if (onend) onend(); return; } SY.cancel();
    const AT = window.AceTeacher; if (AT) AT.pause();
    const lang = H.lang || 'en', u = new SpeechSynthesisUtterance(AT ? AT.spoken(text, lang) : String(text).replace(/\s+/g, ' ').trim());
    let pick = AT && AT.voiceFor(lang, H.dataset.country);
    if (!pick) { const vs = SY.getVoices().filter(v => v.lang && v.lang.toLowerCase().startsWith(lang.slice(0, 2))); pick = vs.find(v => /natural|neural|google|samantha|daniel|serena/i.test(v.name)) || vs[0]; }
    if (pick) u.voice = pick;
    u.lang = pick ? pick.lang : lang; const deep = pref().vc === 'deep'; u.pitch = deep ? 0.8 : 1.05; u.rate = (deep ? 0.95 : 1) * (AT ? AT.rate() : 1);
    if (onend) { let fired = false; const f = () => { if (!fired) { fired = true; onend(); } }; u.onend = f; u.onerror = f; }
    SY.speak(u);
  }
  function mainText() { const m = $('.ls .ls-main'); return m ? m.innerText.replace(/\s+/g, ' ').trim() : ''; }
  function qSpeech() {
    const q = $('.ls .qtext'); if (!q || !$('.ls .ops')) return mainText();
    const ops = $$('.ls .op').map((o, i) => 'ABCD'[i] + '. ' + o.textContent.replace(/^[A-D]/, '').replace(/[1-4]$/, '').trim());
    return q.textContent + '. ' + ops.join('. ');
  }
  function fbSpeech() { const f = $('.ls .fb'); return f ? $$('.ls .fb h3, .ls .fb p').map(e => e.textContent).join('. ') : ''; }
  /* Auto-play: narrate the step, then move on by itself, like a video. Muted: wait for a reading-time estimate instead. */
  let AUTO = null, AUTOK = null;
  function stopAuto() { if (AUTO) clearTimeout(AUTO); AUTO = null; AUTOK = null; }
  function runAuto(key) {
    stopAuto(); AUTOK = key; const txt = mainText(), go = () => { if (AUTOK !== key) return; const ls = $('.ls'); if (!ls || ls.dataset.key !== key || ls.dataset.auto !== '1') return; const n = $('.ls-foot .nx'); if (n && !n.disabled) n.click(); };
    const words = txt.split(' ').length, est = Math.max(3200, words * 330);
    if (pref().snd !== false && SY) { const t0 = Date.now(); AUTO = setTimeout(() => say(txt, () => { if (AUTOK === key) AUTO = setTimeout(go, Math.max(900, est - (Date.now() - t0))); }), 700); }
    else AUTO = setTimeout(go, est + 700);
  }

  /* ---------- confetti ---------- */
  function confetti(n, x, y, spread) {
    if (RM.matches) return; let c = $('#fxc');
    if (!c) { c = document.createElement('canvas'); c.id = 'fxc'; document.body.appendChild(c); }
    const d = devicePixelRatio || 1, W = c.width = innerWidth * d, Hh = c.height = innerHeight * d, g = c.getContext('2d');
    const col = ['#3D35F5', '#FFC72C', '#12B886', '#FF5A5F', '#FF8FB1', '#8FD3FF'];
    const ox = (x == null ? innerWidth / 2 : x) * d, oy = (y == null ? innerHeight * 0.35 : y) * d, sp = spread || 1;
    const P = Array.from({ length: n }, () => ({ x: ox, y: oy, vx: (Math.random() - 0.5) * 22 * d * sp, vy: (-Math.random() * 16 - 6) * d * sp, r: (Math.random() * 6 + 4) * d, a: Math.random() * 6, va: (Math.random() - 0.5) * 0.4, c: col[Math.floor(Math.random() * col.length)], s: Math.random() < 0.3 }));
    const t0 = performance.now();
    (function f(t) {
      const k = (t - t0) / 1000; g.clearRect(0, 0, W, Hh);
      P.forEach(p => { p.vy += 0.55 * d; p.vx *= 0.985; p.x += p.vx; p.y += p.vy; p.a += p.va; g.save(); g.translate(p.x, p.y); g.rotate(p.a); g.globalAlpha = Math.max(0, 1 - k / 1.9); g.fillStyle = p.c;
        if (p.s) { g.beginPath(); g.arc(0, 0, p.r * 0.55, 0, 7); g.fill(); } else g.fillRect(-p.r / 2, -p.r / 4, p.r, p.r / 2); g.restore(); });
      if (k < 1.9) requestAnimationFrame(f); else g.clearRect(0, 0, W, Hh);
    })(t0);
  }

  /* ---------- motion helpers ---------- */
  function splitWords(el) {
    if (!el || el.dataset.split) return 0; el.dataset.split = 1; let n = 0;
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), L = []; while (w.nextNode()) L.push(w.currentNode);
    L.forEach(t => { const parts = t.nodeValue.split(/(\s+)/), f = document.createDocumentFragment();
      parts.forEach(p => { if (!p) return; if (/^\s+$/.test(p)) { f.appendChild(document.createTextNode(p)); return; } const s = document.createElement('span'); s.className = 'w'; s.style.setProperty('--d', Math.min(n++, 40)); s.textContent = p; f.appendChild(s); });
      t.parentNode.replaceChild(f, t); });
    return n;
  }
  function splitSentences(root) {
    (root ? root.querySelectorAll('.fb p') : []).forEach((p, pi) => {
      if (p.dataset.split || p.children.length) return; p.dataset.split = 1;
      const ss = p.textContent.match(/[^.!?]+[.!?]*\s*/g) || [p.textContent]; p.textContent = '';
      ss.forEach((s, i) => { const e = document.createElement('span'); e.className = 's'; e.style.setProperty('--d', i + pi); e.textContent = s; p.appendChild(e); });
    });
  }
  function countUp(el, to, ms) { if (!el) return; if (RM.matches) { el.textContent = to; return; } const t0 = performance.now(); (function f(t) { const k = Math.min(1, (t - t0) / ms), e = 1 - Math.pow(1 - k, 3); el.textContent = Math.round(to * e); if (k < 1) requestAnimationFrame(f); })(t0); }

  /* ---------- after every render ---------- */
  const LAST = { k: null, st: null, r: null };
  function after() {
    fillAce();
    const ls = $('.ls');
    H.toggleAttribute('data-lesson', !!ls);
    if (ls) {
      const k = ls.dataset.key, st = ls.dataset.st || '';
      if (k !== LAST.k) {
        ls.classList.add('in');
        ls.querySelectorAll('.stg').forEach(g => Array.from(g.children).forEach((e, i) => e.style.setProperty('--i', Math.min(i, 12)))); const n = splitWords(ls.querySelector('.qtext')); ls.style.setProperty('--wd', Math.min(n, 24));
        if (window.AceTeacher) AceTeacher.pause(); if (SY) SY.cancel(); stopAuto();
        if (ls.dataset.auto === '1') runAuto(k); else if (pref().voice) setTimeout(() => say(qSpeech()), 250);
        const cb = ls.querySelector('.combo'); if (cb && +cb.dataset.n > 1) cb.classList.add('hot');
      } else if (st !== LAST.st && (st === 'ok' || st === 'no')) {
        ls.classList.add('fx-' + st); splitSentences(ls);
        const o = ls.querySelector('.op.' + st) || ls.querySelector('.op.ok');
        if (st === 'ok') { FX.ok(); const cb = ls.querySelector('.combo'); if (cb) { cb.classList.add('hot'); FX.combo(+cb.dataset.n || 0); }
          if (o) { const r = o.getBoundingClientRect(); confetti(46, r.left + r.width / 2, r.top + r.height / 2, 0.55); } }
        else { FX.no(); try { navigator.vibrate && navigator.vibrate([30, 40, 30]); } catch (e) {} }
        if (pref().voice) setTimeout(() => say(fbSpeech()), 380);
      }
      else if (ls.dataset.auto === '1' && AUTOK !== k) runAuto(k);
      else if (ls.dataset.auto !== '1' && AUTOK) { stopAuto(); if (SY) SY.cancel(); }
      LAST.k = k; LAST.st = st;
    } else { LAST.k = null; LAST.st = null; if (AUTOK) { stopAuto(); if (SY) SY.cancel(); } }
    const r = $('.res');
    if (r && r.dataset.key !== LAST.r) {
      r.classList.add('in'); FX.done(); const p = +r.dataset.p || 0;
      if (p >= 70) setTimeout(() => confetti(160), 350);
      countUp(r.querySelector('.sring b span'), p, 1100);
    }
    LAST.r = r ? r.dataset.key : null;
    try { if (window.AceMotion && !ls) { const v = document.getElementById('v'); AceMotion.view(v, [S.tab, S.sub, S.aus, S.qb && S.qb.s, S.qb && !!S.qb.items, S.fl && S.fl.subj, S.fc && S.fc.topic].join('|')); } } catch (e) { }
    const sp = $('[data-u="snd"]'); if (sp) { sp.setAttribute('aria-pressed', String(pref().snd !== false)); sp.textContent = pref().snd !== false ? '🔊' : '🔈'; }
  }

  /* ---------- hook render ---------- */
  if (typeof window.render === 'function') {
    const base = window.render;
    window.render = function () { const out = base.apply(this, arguments); try { after(); } catch (e) { console.warn('[ace-ui]', e); } return out; };
  }

  /* ---------- desktop sidebar extras ---------- */
  function sidebar() {
    const nav = $('nav'); if (!nav || nav.querySelector('.nv-brand')) return;
    const es = (H.lang || 'en').startsWith('es');
    const b = document.createElement('div'); b.className = 'nv-brand'; b.innerHTML = '<span class="ace" data-mood="idle"></span><span>Ace <b>' + (window.ACE_MODE === 'campus' ? 'Campus' : 'Education') + '</b></span>';
    const f = document.createElement('div'); f.className = 'nv-foot';
    f.innerHTML = TX('<b>Keyboard shortcuts</b>In a lesson: <kbd>1</kbd>–<kbd>4</kbd> choose, <kbd>Enter</kbd> check, <kbd>R</kbd> read aloud, <kbd>M</kbd> mute.','<b>Atajos de teclado</b>En una lección: <kbd>1</kbd>–<kbd>4</kbd> elegir, <kbd>Enter</kbd> comprobar, <kbd>R</kbd> leer en voz alta, <kbd>M</kbd> sonido.');
    nav.insertBefore(b, nav.firstChild); nav.appendChild(f); fillAce(b);
  }

  /* ---------- input ---------- */
  document.addEventListener('click', e => {
    const u = e.target.closest('[data-u]');
    if (u) {
      const k = u.dataset.u;
      if (k === 'say') { if (SY && SY.speaking) SY.cancel(); else say($('.ls .fb') ? fbSpeech() : qSpeech()); }
      else if (k === 'snd') { const p = pref(); p.snd = p.snd === false; try { svP(); } catch (x) {} after(); if (p.snd) FX.pick(); }
      return;
    }
    const b = e.target.closest('button,a,[role=button]'); if (!b) return;
    const a = b.dataset.a;
    if (a === 'qchk' || a === 'dchk' || a === 'dans') return;
    if (a === 'qpk' || a === 'dpick' || (a === 'qa' && b.classList.contains('op'))) FX.pick(); else FX.tap();
  }, true);

  document.addEventListener('keydown', e => {
    const ls = $('.ls'); if (!ls || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.target.closest('input,textarea,select,[contenteditable]') || $('.scrim')) return;
    const k = e.key.toLowerCase(), ops = $$('.ls .ops .op');
    const ix = '1234'.indexOf(k) >= 0 ? '1234'.indexOf(k) : 'abcd'.indexOf(k);
    if (ix >= 0 && ops[ix] && !ops[ix].disabled) { e.preventDefault(); ops[ix].click(); return; }
    if (k === 'enter') { const n = $('.ls-foot .nx'); if (n && !n.disabled) { e.preventDefault(); n.click(); } return; }
    if (k === 'r') { e.preventDefault(); $('[data-u="say"]') && $('[data-u="say"]').click(); return; }
    if (k === 'm') { e.preventDefault(); $('[data-u="snd"]') && $('[data-u="snd"]').click(); return; }
    if (k === 'escape') { const x = $('.ls-x'); if (x) x.click(); }
  });

  window.AceUI = { say, FX, confetti, after, device, svg: () => SVG };
  /* views that load data re-render without going through render(): keep Ace drawn */
  try { new MutationObserver(() => fillAce()).observe(document.getElementById('v'), { childList: true, subtree: true }); } catch (e) { }
  sidebar(); after();
})();
