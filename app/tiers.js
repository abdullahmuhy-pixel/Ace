/* Ace free and paid tiers, on the app side. The server is the authority for AI limits (public.consume_ai_kind);
   this module only shows them, gates the parts that run in the browser (mock exams and the mock breakdown),
   and opens the upgrade sheet. Loaded after the main app script.
   Free: 5 Ace messages a day, 1 photo question a day, 1 essay or answer marking a week, 2 study packs a week,
   the first mock exam in each subject. Plan, trial or school licence: up to 60 messages a day, unlimited mocks
   and the topic-by-topic mock breakdown. */
(function () {
  'use strict';
  const L = (en, es) => TX(en, es), F = (en, es, v) => TXF(en, es, v);
  // monthly price per country, from tools/plan_prices.py (public.plans is the real price list)
  const MONTH = {"GB":["GBP",499],"IE":["EUR",499],"MT":["EUR",499],"ES":["EUR",499],"FR":["EUR",499],"CA":["CAD",799],"ZA":["ZAR",5900],"BW":["BWP",4000],"NG":["NGN",150000],"GH":["GHS",2000],"KE":["KES",20000],"UG":["UGX",700000],"TZ":["TZS",500000],"ZM":["ZMW",4000],"SL":["SLE",4000],"GM":["GMD",15000],"ZW":["USD",200],"LR":["USD",200],"CAMPUS":["USD",499]};
  const FREE_MOCKS = 1;
  let lim = null, loading = null;

  const sync = () => window.AceSync;
  const signedIn = () => !!(sync() && sync().signedIn());
  const money = (minor, cur) => { try { return new Intl.NumberFormat(TX('en-GB', 'es-ES'), { style: 'currency', currency: cur, currencyDisplay: 'narrowSymbol', minimumFractionDigits: minor % 100 ? 2 : 0, maximumFractionDigits: minor % 100 ? 2 : 0 }).format(minor / 100); } catch (e) { return (minor / 100) + ' ' + cur; } };
  function monthPrice() { const p = MONTH[CAMPUS ? 'CAMPUS' : S.c]; return p ? money(p[1], p[0]) : ''; }

  function load(force) {
    if (!signedIn()) return Promise.resolve(null);
    if (loading && !force) return loading;
    loading = sync().rpc('my_limits').then(j => { lim = j; try { render(); } catch (e) { } return j; }).catch(() => { loading = null; return null; });
    return loading;
  }
  // free = a guest, or a signed-in account whose limits say no plan, trial or school licence (unknown counts as not free)
  const free = () => !signedIn() || (lim != null && !lim.paid);
  const paid = () => !!(lim && lim.paid);

  /* ---------- mock exams ---------- */
  const MK = 'ace-mocks';
  const localMocks = () => { try { return JSON.parse(localStorage.getItem(MK) || '{}') || {}; } catch (e) { return {}; } };
  const mockKey = s => (CAMPUS ? 'campus' : S.c) + '|' + s;
  function mocksUsed(s) { const l = localMocks()[mockKey(s)] || 0, sv = (lim && lim.mocks && lim.mocks[s]) || 0; return Math.max(l, sv); }
  function canMock(s) {
    if (!free()) return true;
    const n = lim && lim.free_mocks != null ? lim.free_mocks : FREE_MOCKS;
    if (mocksUsed(s) < n) return true;
    upsell('mock', { s }); return false;
  }
  function noteMock(s) { try { const m = localMocks(); m[mockKey(s)] = (m[mockKey(s)] || 0) + 1; localStorage.setItem(MK, JSON.stringify(m)); } catch (e) { } }

  /* ---------- AI responses ---------- */
  // after a successful AI call: keep the counter in step without another round trip
  function used(j) { if (lim && j && j.cap != null && lim.ai) { lim.ai.used = j.used; lim.ai.cap = j.cap; } if (j && j.kind && j.kind !== 'chat') load(true); }
  // after a refused AI call: a message in the app's language, and the upgrade sheet when a plan would help
  function fail(j) {
    if (!j || !j.code) return (j && j.error) || '';
    const cap = j.cap, k = j.kind || 'chat';
    let m = j.error || '';
    if (j.code === 'off') m = L('Your school has turned off AI help.', 'Tu centro ha desactivado la ayuda de IA.');
    else if (j.code === 'school') m = F('You have used all {n} AI questions your school allows for this period.', 'Has usado las {n} preguntas de IA que permite tu centro en este periodo.', { n: cap });
    else if (j.paid) m = j.code === 'tool'
      ? F('You have used today\'s {n} for this tool. It resets tomorrow.', 'Has usado los {n} de hoy de esta herramienta. Se renueva mañana.', { n: cap })
      : F('You have used today\'s {n} Ace messages. They reset tomorrow.', 'Has usado los {n} mensajes de Ace de hoy. Se renuevan mañana.', { n: cap });
    else { m = TITLE(k, cap); upsell(j.code === 'tool' ? k : 'chat', { cap }); }
    if (lim && lim.ai && j.code === 'daily') lim.ai.used = j.used;
    return m;
  }
  function TITLE(k, cap, s) {
    if (k === 'photo') return F('Free accounts get {n} photo question a day.', 'Las cuentas gratis tienen {n} pregunta con foto al día.', { n: cap != null ? cap : 1 });
    if (k === 'essay') return F('Free accounts get {n} essay or answer marking a week.', 'Las cuentas gratis tienen {n} corrección de redacción o respuesta a la semana.', { n: cap != null ? cap : 1 });
    if (k === 'pack') return F('Free accounts get {n} study packs a week.', 'Las cuentas gratis tienen {n} packs de estudio a la semana.', { n: cap != null ? cap : 2 });
    if (k === 'mock') return F('You have used your free mock exam for {s}.', 'Ya has usado tu simulacro gratis de {s}.', { s: s || '' });
    if (k === 'breakdown') return L('The topic-by-topic breakdown comes with a plan.', 'El desglose por temas viene con un plan.');
    return F('You have used your {n} free Ace messages for today.', 'Has usado tus {n} mensajes gratis de Ace de hoy.', { n: cap != null ? cap : 5 });
  }

  /* ---------- upgrade sheet ---------- */
  let box = null;
  function close() { if (box) { box.remove(); box = null; } }
  function upsell(kind, o) {
    o = o || {}; close();
    const price = monthPrice();
    const perks = [
      L('Up to 60 Ace messages a day', 'Hasta 60 mensajes de Ace al día'),
      L('20 photo questions and 15 essay markings a day', '20 preguntas con foto y 15 correcciones al día'),
      L('Unlimited mock exams with a topic-by-topic breakdown', 'Simulacros ilimitados con desglose por temas'),
      L('Study packs from your notes whenever you need them', 'Packs de estudio de tus apuntes cuando quieras'),
    ];
    box = document.createElement('div');
    box.className = 'scrim'; box.id = 'ace-upsell';
    box.innerHTML = `<button class="bdp" data-u="x" aria-label="${L('Close', 'Cerrar')}"></button><div class="sheet" role="dialog" aria-modal="true" aria-labelledby="up-h">
<h3 id="up-h" style="margin:0 0 6px">${esc(TITLE(kind, o.cap, o.s))}</h3>
<p class="note" style="margin:0 0 10px">${kind === 'chat' ? L('Your free messages come back tomorrow. With a plan you can keep going today.', 'Tus mensajes gratis vuelven mañana. Con un plan puedes seguir hoy.') : L('Everything else in Ace stays free: notes, lessons, quizzes, flashcards and the question bank.', 'Todo lo demás sigue gratis: apuntes, lecciones, tests, tarjetas y el banco de preguntas.')}</p>
<ul style="list-style:none;margin:0;padding:0;display:grid;gap:8px">${perks.map(p => `<li style="display:flex;gap:10px;align-items:flex-start;font-weight:600"><span aria-hidden="true" style="color:var(--green)">✓</span><span>${esc(p)}</span></li>`).join('')}</ul>
${price ? `<p style="margin:12px 0 4px;font-weight:700">${esc(F('From {p} a month', 'Desde {p} al mes', { p: price }))}</p><p class="note" style="margin:0 0 10px">${L('Cheaper by the term or the year, and a group plan for 4 people.', 'Más barato por trimestre o por año, y un plan de grupo para 4 personas.')}</p>` : ''}
${signedIn() ? `<button class="nx" data-u="plans">${L('See plans', 'Ver planes')}</button>` : `<a class="nx" style="display:block;text-align:center;text-decoration:none" href="../login/">${L('Create a free account', 'Crea una cuenta gratis')}</a><p class="note" style="text-align:center">${L('New accounts get a 7-day free trial.', 'Las cuentas nuevas tienen 7 días de prueba gratis.')}</p>`}
<button class="bb" style="width:100%;margin-top:8px" data-u="x">${L('Not now', 'Ahora no')}</button></div>`;
    box.addEventListener('click', e => {
      const b = e.target.closest('[data-u]'); if (!b) return;
      e.stopPropagation(); close();
      if (b.dataset.u === 'plans') { S.ai = null; const t = document.createElement('button'); t.hidden = true; t.dataset.a = 'tab'; t.dataset.v = 'plans'; document.body.appendChild(t); t.click(); t.remove(); }
    });
    document.addEventListener('keydown', function esc_(e) { if (e.key === 'Escape') { close(); document.removeEventListener('keydown', esc_); } });
    document.body.appendChild(box);
    const f = box.querySelector('.nx'); if (f) f.focus();
  }

  /* ---------- status line for the plans page ---------- */
  function status() {
    if (!lim) return '';
    const days = t => Math.max(0, Math.ceil((Date.parse(t) - Date.now()) / 864e5));
    if (lim.status === 'trialing' && lim.trial_ends_at && Date.parse(lim.trial_ends_at) > Date.now() && !lim.plan)
      return F('Free trial: {n} days left', 'Prueba gratis: quedan {n} días', { n: days(lim.trial_ends_at) });
    if (lim.paid) return lim.paid_until ? F('Plan active until {d}', 'Plan activo hasta {d}', { d: new Date(lim.paid_until).toLocaleDateString() }) : L('Plan active', 'Plan activo');
    return L('Free plan', 'Plan gratis');
  }
  function usage() {
    if (!lim || !lim.ai) return '';
    const row = (t, u, c) => `<div class="li"><span class="m"><b style="font-weight:600">${esc(t)}</b></span><span class="v">${u} / ${c}</span></div>`;
    return `<div class="lst">${row(L('Ace messages today', 'Mensajes de Ace hoy'), lim.ai.used, lim.ai.cap)}${row(L('Photo questions today', 'Preguntas con foto hoy'), lim.photo.used, lim.photo.cap)}${row(lim.essay.per === 'week' ? L('Essay markings this week', 'Correcciones esta semana') : L('Essay markings today', 'Correcciones hoy'), lim.essay.used, lim.essay.cap)}${row(lim.pack.per === 'week' ? L('Study packs this week', 'Packs de estudio esta semana') : L('Study packs today', 'Packs de estudio hoy'), lim.pack.used, lim.pack.cap)}</div>`;
  }

  window.AceTier = { load, free, paid, canMock, noteMock, used, fail, upsell, status, usage, close, lim: () => lim };
  // load once the session is known, and again when the app comes back to the foreground
  window.addEventListener('load', () => setTimeout(() => { if (sync()) sync().ready().then(ok => { if (ok) load(); }); }, 600));
  document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible' && signedIn()) load(true); });
})();
