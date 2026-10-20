/* Ace learner tools for students who study on their own: study plan to exam day, mistakes notebook,
   saved questions, achievements, weekly league, wellbeing check-in and "My classes" (join a teacher's class
   with a code). Local-first: everything except the league and classes works signed out and offline.
   Loaded after class.js and before ui.js. */
(function () {
  'use strict';
  if (!window.AceX || !AceX.h) return;
  const { L, esc, back, needSignIn, signedIn, sync } = AceX.h;
  const C_ = () => C[S.c], ex = () => C_().x[S.x % C_().x.length];
  const todayKey = () => new Date().toISOString().slice(0, 10);
  const get = (k, d) => { try { const v = JSON.parse(localStorage.getItem(k) || 'null'); return v == null ? d : v; } catch (e) { return d; } };
  const put = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { } };
  const hash = s => { let h = 2166136261; for (const ch of String(s)) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); } return (h >>> 0).toString(36); };
  const subIdx = s => C_().s.indexOf(s);
  const fmtD = d => new Date(d + 'T12:00:00').toLocaleDateString(TX('en-GB','es'), { weekday: 'short', day: 'numeric', month: 'short' });
  const addDays = (d, n) => { const x = new Date(d + 'T12:00:00'); x.setDate(x.getDate() + n); return x.toISOString().slice(0, 10); };
  const err = m => `<p class="note" style="color:var(--red)">${esc(m)}</p>`;

  /* ================= mistakes notebook + saved questions ================= */
  const MK = 'ace-mist', SK = 'ace-saved';
  const pack = (q, s) => ({ id: hash(q[3]), s, mi: q[0], t: q[1], q: q[3], o: q[4], a: q[5], e: q[6] });
  const Mist = window.AceMist = {
    all: () => get(MK, []),
    add(q, s, chosen) {
      if (!q || q[2] || !q[4] || !q[4].length) return;
      const L0 = Mist.all(), p = pack(q, s), f = L0.find(x => x.id === p.id);
      if (f) { f.n = (f.n || 1) + 1; f.c = chosen; f.at = Date.now(); } else L0.unshift(Object.assign(p, { c: chosen, n: 1, at: Date.now() }));
      put(MK, L0.slice(0, 400));
    },
    got(q) { const id = hash(q[3]), L0 = Mist.all(), f = L0.find(x => x.id === id); if (!f) return; f.ok = (f.ok || 0) + 1; put(MK, f.ok >= 2 ? L0.filter(x => x.id !== id) : L0); },
    remove(id) { put(MK, Mist.all().filter(x => x.id !== id)); },
    saved: () => get(SK, []),
    isSaved: q => !!(q && Mist.saved().some(x => x.id === hash(q[3]))),
    save(q, s) { if (!q) return false; const L0 = Mist.saved(), id = hash(q[3]); if (L0.some(x => x.id === id)) { put(SK, L0.filter(x => x.id !== id)); return false; } L0.unshift(Object.assign(pack(q, s), { at: Date.now(), th: q[2] ? 1 : 0, mk: q[7], ms: q[8] })); put(SK, L0.slice(0, 300)); return true; }
  };
  const asItem = m => [m.mi || 0, m.t, 0, m.q, m.o, m.a, m.e, 0, []];
  function redo(list, s) { if (!list.length) return; S.sub = subIdx(s) >= 0 ? subIdx(s) : S.sub; qStart({ s, items: shuf(list.map(asItem)).slice(0, 15), ret: 'mist', mode: 'practice' }); }

  function mistView() {
    const tab = S.mt || 'm', M = Mist.all(), SV = Mist.saved();
    let h = `<div class="pad">${back('tools')}<div class="pg-h"><h1>${L('Mistakes notebook', 'Cuaderno de errores')}</h1><p>${L('Every question you get wrong lands here. Get it right twice and it leaves.', 'Cada pregunta que fallas llega aquí. Acierta dos veces y desaparece.')}</p></div>
<div class="seg2"><button class="${tab === 'm' ? 'on' : ''}" data-l="mt" data-v="m">📕 ${L('Mistakes', 'Errores')} <b>${M.length}</b></button><button class="${tab === 's' ? 'on' : ''}" data-l="mt" data-v="s">⭐ ${L('Saved', 'Guardadas')} <b>${SV.length}</b></button></div>`;
    const list = tab === 'm' ? M : SV;
    if (!list.length) return h + `<div class="emp"><span class="ace" data-mood="${tab === 'm' ? 'cheer' : 'idle'}" style="width:70px"></span><b>${tab === 'm' ? L('No mistakes waiting', 'No hay errores pendientes') : L('Nothing saved yet', 'Nada guardado aún')}</b>${tab === 'm' ? L('Practise a topic. Anything you miss will be kept here for you.', 'Practica un tema. Lo que falles quedará aquí.') : L('Tap ☆ on any question in a lesson to keep it here.', 'Toca ☆ en una pregunta para guardarla aquí.')}</div></div>`;
    const by = {}; list.forEach(m => (by[m.s] = by[m.s] || []).push(m));
    Object.keys(by).forEach(s => {
      const g = by[s], mcq = g.filter(m => m.o && m.o.length);
      h += `<div class="sh">${ic(s)} ${esc(s)} <small style="margin-left:6px;color:var(--text3);font:700 13px var(--fb)">${g.length}</small>${mcq.length ? `<a data-l="redo" data-v="${esc(s)}" data-k="${tab}">${L('Redo these', 'Repetir')} ›</a>` : ''}</div><div class="mlist">`;
      h += g.slice(0, 40).map(m => `<details class="mcard"><summary><span class="mt">${esc(m.t || '')}</span><b>${esc(m.q)}</b>${m.n > 1 ? `<em>×${m.n}</em>` : ''}</summary>${m.o && m.o.length ? `<ol type="A">${m.o.map((o, i) => `<li class="${i === m.a ? 'ok' : i === m.c ? 'no' : ''}">${esc(o)}</li>`).join('')}</ol>` : ''}${m.e ? `<p class="mx">${esc(m.e)}</p>` : ''}${m.ms && m.ms.length ? `<p class="mx">${m.ms.map(esc).join('<br>')}</p>` : ''}<button class="bb" data-l="${tab === 'm' ? 'mdel' : 'sdel'}" data-v="${m.id}">${tab === 'm' ? L('I understand it now', 'Ya lo entiendo') : L('Remove', 'Quitar')}</button></details>`).join('') + '</div>';
    });
    return h + '</div>';
  }

  /* ================= study plan to exam day ================= */
  const PL = () => P.plan || null;
  function topicsFor(s) {
    const R = SYLX(s); if (!R) return [];
    const T = TC[s] || {}, out = [];
    R.m.forEach((m, mi) => m[1].forEach((tp, ti) => out.push({ s, mi, ti, tp, notes: !!T[tp] })));
    return out;
  }
  function buildPlan() {
    const p = PL(); if (!p || !ACE_LOADED[S.c]) return null;
    const subs = (p.subs || []).filter(s => QB[s] || TC[s]); if (!subs.length) return { days: [], total: 0 };
    const acc = k => { const e = ST().t[k]; return e && e[0] >= 3 ? e[1] / e[0] : null; };
    const queues = subs.map(s => topicsFor(s).filter(x => !P.done[s + '|' + x.tp] || (acc(s + '|' + x.tp) != null && acc(s + '|' + x.tp) < 0.6)));
    const weak = subs.flatMap(s => topicsFor(s).filter(x => acc(s + '|' + x.tp) != null && acc(s + '|' + x.tp) < 0.6));
    const total = queues.reduce((n, q) => n + q.length, 0);
    const per = Math.max(1, Math.round((p.min || 30) / 15)), end = p.exam || C_().d, rev = addDays(end, -14);
    const days = []; let d = todayKey(), qi = 0, wi = 0, mi = 0;
    for (let guard = 0; d < end && guard < 400; guard++, d = addDays(d, 1)) {
      const wd = new Date(d + 'T12:00:00').getDay(); if (!(p.days || [1, 2, 3, 4, 5, 6]).includes(wd)) continue;
      const items = [];
      if (d >= rev) {
        if (wd === 6 || wd === 0) { const s = subs[mi++ % subs.length]; items.push({ k: 'mock', s }); }
        else { items.push({ k: 'mist' }); const w = weak[wi++ % Math.max(1, weak.length)]; if (w) items.push(Object.assign({ k: 'prac' }, w)); }
      } else {
        for (let n = 0; n < per; n++) {
          let x = null;
          for (let tries = 0; tries < queues.length && !x; tries++) { const q = queues[qi++ % queues.length]; if (q.length) x = q.shift(); }
          if (!x) { const w = weak[wi++ % Math.max(1, weak.length)]; if (w) x = w; else break; }
          items.push(Object.assign({ k: x.notes ? 'lesson' : 'prac' }, x));
        }
        if (wd === 6 && days.length % 2 === 0) items.push({ k: 'daily' });
      }
      days.push({ d, items: items.map(it => Object.assign(it, { key: d + '|' + it.k + '|' + (it.s || '') + '|' + (it.tp || '') })) });
    }
    return { days, total, per, end };
  }
  const isDone = it => !!(P.pd && P.pd[it.key]) || (it.k === 'lesson' && P.done[it.s + '|' + it.tp]);
  const itemLabel = it => it.k === 'lesson' ? ['▶️', L('Lesson', 'Lección') + ': ' + it.tp, it.s] : it.k === 'prac' ? ['✏️', L('Practise', 'Practica') + ': ' + it.tp, it.s] : it.k === 'mock' ? ['⏱️', L('Mock exam', 'Simulacro') + ': ' + it.s, L('Exam conditions', 'Condiciones de examen')] : it.k === 'mist' ? ['📕', L('Redo your mistakes', 'Repite tus errores'), L('From your notebook', 'De tu cuaderno')] : ['🎯', L('Daily challenge', 'Reto diario'), L('10 questions', '10 preguntas')];
  const itemRow = (it, today) => { const [e, b, sm] = itemLabel(it), dn = isDone(it); return `<div class="pli ${dn ? 'dn' : ''}"><span class="e">${dn ? '✅' : e}</span><span class="m"><b>${esc(b)}</b><small>${esc(sm)}</small></span>${today && !dn ? `<button class="play" data-l="pgo" data-v="${esc(it.key)}">${L('Start', 'Empezar')}</button>` : `<button class="pchk" data-l="ptick" data-v="${esc(it.key)}" aria-label="${L('Mark done', 'Marcar hecho')}">${dn ? '✓' : '○'}</button>`}</div>`; };
  function planSetup() {
    const c = C_(), p = PL() || {}, subs = p.subs || c.s.filter(s => selOK(c, s) && QB[s]).slice(0, 6), days = p.days || [1, 2, 3, 4, 5, 6];
    const DN = ({ es: ['D', 'L', 'M', 'X', 'J', 'V', 'S'], fr: ['Di', 'Lu', 'Ma', 'Me', 'Je', 'Ve', 'Sa'] })[c.l] || ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'];
    return `<div class="card plset"><label class="xl">${L('Exam date', 'Fecha del examen')}<input class="xin" type="date" data-l-in="exam" value="${esc(p.exam || c.d)}"></label>
<p class="xl">${L('Days I can study', 'Días que puedo estudiar')}</p><div class="xchips">${[1, 2, 3, 4, 5, 6, 0].map(d => `<button class="xchip ${days.includes(d) ? 'on' : ''}" data-l="pday" data-v="${d}">${DN[d]}</button>`).join('')}</div>
<p class="xl">${L('Time per study day', 'Tiempo por día')}</p><div class="xchips">${[15, 30, 45, 60, 90].map(m => `<button class="xchip ${(p.min || 30) === m ? 'on' : ''}" data-l="pmin" data-v="${m}">${m} min</button>`).join('')}</div>
<p class="xl">${L('Subjects in my plan', 'Asignaturas del plan')}</p><div class="xchips">${c.s.filter(s => QB[s] || TC[s]).map(s => `<button class="xchip ${subs.includes(s) ? 'on' : ''}" data-l="psub" data-v="${esc(s)}">${ic(s)} ${esc(s)}</button>`).join('')}</div>
<button class="nx" data-l="psave">${PL() ? L('Update my plan', 'Actualizar mi plan') : L('Make my plan', 'Crear mi plan')}</button></div>`;
  }
  function planView() {
    let h = `<div class="pad">${back('home')}<div class="pg-h"><h1>${L('My study plan', 'Mi plan de estudio')}</h1><p>${L('Small daily steps to exam day, built around what you find hardest.', 'Pasos diarios hasta el examen, centrados en lo que más te cuesta.')}</p></div>`;
    if (!ACE_LOADED[S.c]) return h + `<div class="emp2">${L('Loading your subjects…', 'Cargando tus asignaturas…')}</div></div>`;
    if (!PL() || S.pedit) { S.pdraft = S.pdraft || Object.assign({}, PL() || {}); return h + planSetup() + '</div>'; }
    const B = buildPlan(), p = PL(), left = Math.max(0, Math.floor((new Date(p.exam + 'T09:00:00') - Date.now()) / 864e5));
    const studied = p.subs.reduce((n, s) => n + topicsFor(s).filter(x => P.done[s + '|' + x.tp]).length, 0), all = p.subs.reduce((n, s) => n + topicsFor(s).length, 0);
    const today = B.days.find(d => d.d === todayKey()), next = B.days.filter(d => d.d > todayKey()).slice(0, 6);
    const pct = all ? Math.round(studied * 100 / all) : 0;
    h += `<div class="plhd"><div><b>${left}</b><span>${L('days to go', 'días')}</span></div><div><b>${studied}/${all}</b><span>${L('topics studied', 'temas estudiados')}</span></div><div class="gr2" style="--p:${pct}"><span>${pct}%</span></div></div>`;
    h += `<div class="sh">${L('Today', 'Hoy')} <small style="margin-left:6px;color:var(--text3);font:700 13px var(--fb)">${fmtD(todayKey())}</small></div>`;
    h += today ? `<div class="pll">${today.items.map(it => itemRow(it, true)).join('')}</div>` : `<div class="emp2">${L('Rest day. Enjoy it, or do the daily challenge to keep your streak.', 'Día de descanso. O haz el reto diario para mantener tu racha.')}</div>`;
    h += `<div class="sh">${L('Coming up', 'Próximos días')}</div>` + next.map(d => `<details class="pld"><summary><b>${fmtD(d.d)}</b><span>${d.items.length} ${L('items', 'tareas')}</span></summary><div class="pll">${d.items.map(it => itemRow(it, false)).join('')}</div></details>`).join('');
    if (B.total === 0) h += `<p class="note">${L('You have studied every topic in this plan. It now repeats your weakest topics and mocks.', 'Has estudiado todos los temas; ahora repasa tus puntos débiles y simulacros.')}</p>`;
    return h + `<button class="bb" style="width:100%;margin-top:14px" data-l="pedit">⚙️ ${L('Change my plan', 'Cambiar mi plan')}</button><p class="note">${L('The last two weeks before your exam switch to mock exams and revision.', 'Las dos últimas semanas son de simulacros y repaso.')}</p></div>`;
  }
  function launch(it) {
    const c = C_(), s = it.s; S.planKey = it.key;
    if (it.k === 'daily') { S.tab = 'daily'; S.dg = null; return; }
    if (it.k === 'mist') { S.tab = 'mist'; S.mt = 'm'; P.pd = P.pd || {}; P.pd[it.key] = 1; svP(); return; }
    const si = subIdx(s); if (si < 0) return toast(L('That subject is not in your exam list.', 'Esa asignatura no está en tu lista.'));
    S.sub = si;
    if (it.k === 'mock') { const n = mockCfg(s), t0 = Date.now(); qStart({ s, items: mockItems(s), mode: 'mock', ret: 'plan', dur: n.min * 60, t0, deadline: t0 + n.min * 60000 }); return; }
    if (it.k === 'lesson') { const T0 = (TC[s] || {})[it.tp]; if (T0) { const T = Object.assign({ __t: it.tp }, T0); S.pl = { s, mi: it.mi, ti: it.ti, T, steps: plSteps(T, s, it.mi), i: 0, r: 1, q: {}, auto: false, qn: 0, qok: 0, ret: 'plan' }; S.tab = 'play'; return; } }
    const items = (QB[s] || []).filter(x => x[0] == it.mi && x[1] == it.tp && !x[2]);
    qStart({ s, items: shuf(items).slice(0, 10), ret: 'plan', mode: 'practice', sp: { mi: it.mi, tp: it.tp } });
  }

  /* ================= achievements ================= */
  const lvl = xp => Math.floor(Math.sqrt(xp / 50)) + 1, lvlXP = n => 50 * (n - 1) * (n - 1);
  function badges() {
    const q = ST().q, acc = q ? ST().c / q : 0, d = Object.keys(P.done).length, lc = P.lc || 0, mk = P.mk || 0, st = Math.max(S.streak, P.bestStreak || 0);
    const B = (ic, t, s, v, n) => ({ ic, t, s, v: Math.min(v, n), n, ok: v >= n });
    return [
      B('🌱', L('First steps', 'Primeros pasos'), L('Answer your first question', 'Responde tu primera pregunta'), q, 1),
      B('✏️', L('Getting going', 'En marcha'), L('Answer 50 questions', 'Responde 50 preguntas'), q, 50),
      B('📚', L('Committed', 'Constante'), L('Answer 250 questions', 'Responde 250 preguntas'), q, 250),
      B('⚙️', L('Question machine', 'Máquina de preguntas'), L('Answer 1,000 questions', 'Responde 1.000 preguntas'), q, 1000),
      B('👑', L('Legend', 'Leyenda'), L('Answer 5,000 questions', 'Responde 5.000 preguntas'), q, 5000),
      B('🔥', L('On fire', 'En racha'), L('3-day streak', 'Racha de 3 días'), st, 3),
      B('📆', L('Week strong', 'Semana completa'), L('7-day streak', 'Racha de 7 días'), st, 7),
      B('🏔️', L('Unstoppable', 'Imparable'), L('30-day streak', 'Racha de 30 días'), st, 30),
      B('▶️', L('Good listener', 'Buen oyente'), L('Finish a narrated lesson', 'Termina una lección'), lc, 1),
      B('🎬', L('Binge learner', 'Maratón'), L('Finish 25 lessons', 'Termina 25 lecciones'), lc, 25),
      B('🧭', L('Explorer', 'Explorador'), L('Study 10 topics', 'Estudia 10 temas'), d, 10),
      B('🗺️', L('Cartographer', 'Cartógrafo'), L('Study 100 topics', 'Estudia 100 temas'), d, 100),
      B('⏱️', L('Exam ready', 'Listo para el examen'), L('Sit a full mock exam', 'Haz un simulacro'), mk, 1),
      B('🏁', L('Mock veteran', 'Veterano'), L('Sit 10 mock exams', 'Haz 10 simulacros'), mk, 10),
      B('🎯', L('Sharpshooter', 'Puntería'), L('80% accuracy over 100+ questions', '80% de acierto en 100+ preguntas'), q >= 100 ? Math.round(acc * 100) : 0, 80),
      B('💯', L('Perfect day', 'Día perfecto'), L('Score 10/10 in a daily challenge', '10/10 en un reto diario'), P.perfect || 0, 1),
      B('📕', L('Learning from mistakes', 'Aprender de los errores'), L('Clear 20 questions from your notebook', 'Supera 20 errores del cuaderno'), P.mclear || 0, 20),
      B('🗓️', L('Planner', 'Planificador'), L('Make a study plan', 'Crea un plan de estudio'), PL() ? 1 : 0, 1)
    ];
  }
  function achView() {
    const b = badges(), got = b.filter(x => x.ok).length, lv = lvl(S.xp), a = lvlXP(lv), z = lvlXP(lv + 1), p = Math.round((S.xp - a) * 100 / Math.max(1, z - a));
    return `<div class="pad">${back('tools')}<div class="pg-h"><h1>${L('Achievements', 'Logros')}</h1><p>${got} ${L('of', 'de')} ${b.length} ${L('unlocked', 'desbloqueados')}</p></div>
<div class="lvc"><span class="ace" data-mood="${got ? 'cheer' : 'idle'}"></span><div><b>${L('Level', 'Nivel')} ${lv}</b><small>${S.xp} XP • ${z - S.xp} XP ${L('to level', 'para el nivel')} ${lv + 1}</small><div class="pb"><i style="width:${p}%"></i></div></div></div>
<div class="bdg">${b.map(x => `<div class="bd ${x.ok ? 'ok' : ''}"><span>${x.ic}</span><b>${esc(x.t)}</b><small>${esc(x.s)}</small>${x.ok ? '' : `<div class="pb"><i style="width:${Math.round(x.v * 100 / x.n)}%"></i></div>`}</div>`).join('')}</div></div>`;
  }

  /* ================= weekly league ================= */
  const LG = window.AceLg = { rows: null, err: '', busy: false };
  function leagueView() {
    let h = `<div class="pad">${back('tools')}<div class="pg-h"><h1>${L('Weekly league', 'Liga semanal')}</h1><p>${TXF('Learners in {c} this week. Earn XP from lessons, practice and the daily challenge. Resets every Monday.', 'Estudiantes de {c} esta semana. Gana XP con lecciones y práctica. Se reinicia cada lunes.', { c: C_().n })}</p></div>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (LG.err) return h + err(LG.err) + '</div>';
    if (!LG.rows) return h + `<div class="emp2">${L('Loading the table…', 'Cargando la tabla…')}</div></div>`;
    const me = LG.rows.find(r => r.me);
    if (!LG.rows.length) return h + `<div class="emp"><span class="ace" data-mood="wave" style="width:70px"></span><b>${L('Be the first on the board this week', 'Sé el primero esta semana')}</b>${L('Finish a lesson or a quiz and your XP shows up here.', 'Termina una lección o un test y tu XP aparecerá aquí.')}</div></div>`;
    h += `<div class="lgb">${LG.rows.map(r => `<div class="lgr ${r.me ? 'me' : ''} ${r.rank <= 3 ? 'top' : ''}"><span class="rk">${r.rank <= 3 ? ['🥇', '🥈', '🥉'][r.rank - 1] : r.rank}</span><b>${esc(r.name)}${r.me ? ' (' + L('you', 'tú') + ')' : ''}</b><span class="xp">${r.xp} XP</span></div>`).join('')}</div>`;
    if (!me) h += `<p class="note">${L('Earn some XP this week to join the table.', 'Gana XP esta semana para entrar en la tabla.')}</p>`;
    return h + `<button class="bb" style="width:100%;margin-top:12px" data-l="lghide">${L('Hide me from the league', 'Ocultarme de la liga')}</button><p class="note">${L('Only your first name and surname initial are shown.', 'Solo se muestra tu nombre y la inicial del apellido.')}</p></div>`;
  }

  /* ================= wellbeing check-in ================= */
  const MOODS = [['😣', 'Overwhelmed', 'Agobiado'], ['😟', 'Worried', 'Preocupado'], ['😐', 'Okay', 'Normal'], ['🙂', 'Good', 'Bien'], ['😄', 'Great', 'Genial']];
  const TIPS = {
    0: [['Breathe first', 'Respira primero', 'Try the breathing circle below for one minute. Then pick just one small task.', 'Prueba el círculo de respiración un minuto. Luego elige una sola tarea pequeña.'], ['Talk to someone', 'Habla con alguien', 'Tell a parent, teacher, friend or school counsellor how you feel. You do not have to carry it alone.', 'Cuéntale a un familiar, profesor o amigo cómo te sientes. No tienes que cargarlo solo.']],
    1: [['Shrink the task', 'Haz la tarea más pequeña', 'Do one 10-minute topic, not a whole subject. Small wins calm the mind.', 'Haz un tema de 10 minutos, no una asignatura entera.'], ['Write the worry down', 'Escribe la preocupación', 'Name it in one line below. Worries are smaller on paper.', 'Escríbela en una línea abajo. En papel parece más pequeña.']],
    2: [['Keep it steady', 'Mantén el ritmo', 'Do today\'s plan, then stop. Rest is part of revision.', 'Haz el plan de hoy y para. Descansar también es repasar.']],
    3: [['Use the good day', 'Aprovecha el buen día', 'Try a topic you have been avoiding while you feel strong.', 'Prueba un tema que has evitado mientras te sientes bien.']],
    4: [['Pass it on', 'Compártelo', 'Explain a topic to a friend. Teaching is the fastest way to remember.', 'Explica un tema a un amigo. Enseñar ayuda a recordar.']]
  };
  function wellView() {
    const W = get('ace-well', {}), t = W[todayKey()], days = Object.keys(W).sort().slice(-14);
    let h = `<div class="pad">${back('tools')}<div class="pg-h"><h1>${L('Wellbeing check-in', 'Cómo estás hoy')}</h1><p>${L('Private to this device. Nobody else sees it.', 'Privado en este dispositivo. Nadie más lo ve.')}</p></div>`;
    h += `<div class="card"><b>${L('How are you feeling today?', '¿Cómo te sientes hoy?')}</b><div class="moods">${MOODS.map((m, i) => `<button class="${t && t.m === i ? 'on' : ''}" data-l="mood" data-v="${i}"><span>${m[0]}</span><small>${C_().l ? m[2] : m[1]}</small></button>`).join('')}</div>
<label class="xl">${L('Hours of sleep last night', 'Horas de sueño anoche')}<input class="xin" type="number" min="0" max="14" step="0.5" data-l-in="sleep" value="${t && t.s != null ? t.s : ''}"></label>
<label class="xl">${L('Anything on your mind? (optional)', '¿Algo en mente? (opcional)')}<textarea class="xin" rows="2" maxlength="280" data-l-in="wnote">${esc((t && t.n) || '')}</textarea></label></div>`;
    if (t) { h += `<div class="sh">${L('For today', 'Para hoy')}</div>` + (TIPS[t.m] || []).map(x => `<div class="card" style="margin-bottom:8px"><b>${TX(x[0], x[1])}</b><p style="margin:4px 0 0">${TX(x[2], x[3])}</p></div>`).join(''); if (t.s != null && t.s < 7) h += `<p class="note">${L('Teenagers need 8 to 10 hours of sleep. Sleep is when memory is stored, so an early night is revision too.', 'Los adolescentes necesitan de 8 a 10 horas de sueño. Dormir también es repasar.')}</p>`; }
    h += `<div class="sh">${L('One-minute breathing', 'Respiración de un minuto')}</div><div class="breath"><div class="bc"><span>${L('Breathe in', 'Inspira')}</span></div><p class="note">${L('In for 4, hold for 4, out for 4, hold for 4. Follow the circle.', 'Inspira 4, mantén 4, espira 4, mantén 4. Sigue el círculo.')}</p></div>`;
    if (days.length > 1) h += `<div class="sh">${L('Last two weeks', 'Últimas dos semanas')}</div><div class="mtrend">${days.map(d => `<div><span>${MOODS[W[d].m][0]}</span><small>${d.slice(8)}</small></div>`).join('')}</div>`;
    return h + `<p class="note">${L('If you ever feel unsafe or can\'t cope, talk to a trusted adult today or contact a local helpline.', 'Si alguna vez no te sientes seguro o no puedes más, habla hoy con un adulto de confianza o llama a una línea de ayuda local.')}</p></div>`;
  }

  /* ================= my classes (join with a code) ================= */
  const CL = window.AceCls = { list: null, code: '', err: '', ok: '', busy: false };
  const loadClasses = () => sync().rpc('my_classes').then(r => { CL.list = r || []; }).catch(e => { CL.err = (e && (e.msg || e.message)) || L('Could not load your classes.', 'No se pudieron cargar tus clases.'); });
  function classesView() {
    let h = `<div class="pad">${back('tools')}<div class="pg-h"><h1>${L('My classes', 'Mis clases')}</h1><p>${L('Join a class from a teacher or tutor with their code. You keep your own account and progress.', 'Únete a la clase de un profesor con su código. Conservas tu cuenta y tu progreso.')}</p></div>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    h += `<div class="card"><label class="xl">${L('Class code', 'Código de clase')}<input class="xin code" maxlength="8" data-l-in="ccode" value="${esc(CL.code)}" placeholder="ABC123" autocapitalize="characters"></label><button class="nx" data-l="cjoin" ${CL.busy ? 'disabled' : ''}>${CL.busy ? '…' : L('Join class', 'Unirme')}</button>${CL.err ? err(CL.err) : ''}${CL.ok ? `<p class="note" style="color:var(--green)">${esc(CL.ok)}</p>` : ''}</div>`;
    if (!CL.list) return h + `<div class="emp2">…</div></div>`;
    h += CL.list.length ? `<div class="sh">${L('Your classes', 'Tus clases')}</div><div class="lst">${CL.list.map(k => `<button class="li" data-l="copen" data-v="${k.class_id}"><span class="e">${k.kind === 'tutor' ? '🧑‍🏫' : '🏫'}</span><span class="m"><b>${esc(k.name)}</b><small>${esc([k.subject, k.teachers, k.school].filter(Boolean).join(' • '))}</small></span><span class="v">›</span></button>`).join('')}</div>
<div class="row3" style="grid-template-columns:1fr 1fr 1fr;margin-top:12px"><button class="bt" data-a="tab" data-v="tasks">📝 ${L('Class work', 'Tareas')}</button><button class="bt" data-a="tab" data-v="inbox">💬 ${L('Messages', 'Mensajes')}</button><button class="bt" data-a="tab" data-v="livej">⚡ ${L('Live quiz', 'Quiz en vivo')}</button></div>` : `<div class="emp"><span class="ace" data-mood="wave" style="width:70px"></span><b>${L('No classes yet', 'Aún no tienes clases')}</b>${L('Studying on your own works perfectly. Join a class only if a teacher gives you a code.', 'Estudiar por tu cuenta funciona perfectamente.')}</div>`;
    return h + '</div>';
  }


  /* one class: live lesson link, resources, topics covered and the Q&A board */
  const CK = window.AceCk = { id: '', c: null, res: [], qs: [], pace: 0, ask: '', err: '' };
  const loadClass = id => Promise.all([
    sync().table('classes').then(q => q.select('id,name,subject,exam,meet_url').eq('id', id).maybeSingle()),
    sync().table('class_resources').then(q => q.select('title,kind,url,body,created_at').eq('class_id', id).order('created_at', { ascending: false }).limit(50)),
    sync().table('class_questions').then(q => q.select('id,body,answer,author_id,created_at').eq('class_id', id).order('created_at', { ascending: false }).limit(60)),
    sync().table('class_pacing').then(q => q.select('topic,taught_on').eq('class_id', id).not('taught_on', 'is', null))
  ]).then(([c, r, q, p]) => { CK.c = c.data; CK.res = r.data || []; CK.qs = q.data || []; CK.pace = (p.data || []).length; CK.paceList = (p.data || []).map(x => x.topic); }).catch(e => { CK.err = (e && (e.msg || e.message)) || 'Error'; });
  function classView() {
    const k = (CL.list || []).find(x => x.class_id === CK.id) || {}, c = CK.c;
    let h = `<div class="pad"><div class="bk"><button class="bb" data-a="tab" data-v="classes">‹ ${L('My classes', 'Mis clases')}</button></div><div class="pg-h"><h1>${esc(k.name || (c && c.name) || '')}</h1><p>${esc([k.subject, k.teachers].filter(Boolean).join(' • '))}</p></div>`;
    if (!c) return h + (CK.err ? err(CK.err) : `<div class="emp2">…</div>`) + '</div>';
    if (c.meet_url) h += `<a class="dly" style="text-decoration:none" href="${esc(c.meet_url)}" target="_blank" rel="noopener"><span class="di">🎥</span><span><b>${L('Join live lesson', 'Entrar a la clase en vivo')}</b><span>${L('Opens your teacher\'s meeting link', 'Abre el enlace de tu profesor')}</span></span><em>›</em></a>`;
    h += `<div class="row3" style="grid-template-columns:1fr 1fr 1fr;margin-top:12px"><button class="bt" data-a="tab" data-v="tasks">📝 ${L('Class work', 'Tareas')}</button><button class="bt" data-a="tab" data-v="inbox">💬 ${L('Messages', 'Mensajes')}</button><button class="bt" data-a="tab" data-v="livej">⚡ ${L('Live quiz', 'Quiz en vivo')}</button></div>`;
    if (CK.pace) h += `<div class="sh">${L('Topics covered in class', 'Temas vistos en clase')} <small style="margin-left:6px;color:var(--text3);font:700 13px var(--fb)">${CK.pace}</small></div><div class="chips">${CK.paceList.slice(0, 30).map(t => `<span>${esc(t)}</span>`).join('')}</div>`;
    h += `<div class="sh">${L('Ask your teacher', 'Pregunta a tu profesor')}</div><div class="card"><textarea class="xin" rows="2" maxlength="1000" data-l-in="ask" placeholder="${L('Your question for the whole class', 'Tu pregunta para toda la clase')}">${esc(CK.ask)}</textarea><button class="nx" data-l="ask">${L('Ask', 'Preguntar')}</button><p class="note">${L('Answers are shared with the whole class.', 'Las respuestas se comparten con toda la clase.')}</p></div>`;
    h += CK.qs.map(q => `<div class="mcard" style="margin-bottom:8px"><b style="font:700 15px var(--fd)">${esc(q.body)}</b>${q.answer ? `<p class="mx" style="background:var(--ok-bg);border-radius:12px;padding:10px;color:var(--text)">${esc(q.answer)}</p>` : `<p class="note">${L('Waiting for an answer', 'Esperando respuesta')}</p>`}</div>`).join('');
    if (CK.res.length) h += `<div class="sh">${L('Library', 'Biblioteca')}</div><div class="lst">${CK.res.map(r => r.url ? `<a class="li" href="${esc(r.url)}" target="_blank" rel="noopener"><span class="e">${{ link: '🔗', video: '🎬', note: '📝', file: '📎' }[r.kind] || '🔗'}</span><span class="m"><b>${esc(r.title)}</b>${r.body ? `<small>${esc(r.body.slice(0, 120))}</small>` : ''}</span><span class="v">↗</span></a>` : `<details class="li" style="display:block"><summary><b>📝 ${esc(r.title)}</b></summary><p style="white-space:pre-wrap">${esc(r.body || '')}</p></details>`).join('')}</div>`;
    return h + `<button class="lo" data-l="cleave" data-v="${CK.id}">${L('Leave this class', 'Salir de esta clase')}</button></div>`;
  }

  /* ================= assigned Ace work from a teacher ================= */
  function launchTask(t) {
    const c = C_(), r = t.topic_ref || {}, s = r.subject;
    if (r.exam) { const xi = c.x.findIndex(x => x === r.exam || exk(x) === exk(r.exam)); if (xi >= 0 && xi !== S.x % c.x.length) { S.x = xi; aceEx(S.c); } }
    const si = subIdx(s); if (!s || si < 0 || !(QB[s] || TC[s])) { toast(L('This work is for a subject that is not open for your exam yet.', 'Esta tarea es de una asignatura no disponible para tu examen.')); return false; }
    S.sub = si; S.taskRun = t.id;
    const R = SYLX(s); let mi = -1, ti = -1; if (R && r.topic) R.m.forEach((m, i) => { const j = m[1].indexOf(r.topic); if (j >= 0 && mi < 0) { mi = i; ti = j; } });
    if (t.kind === 'mock') { const n = mockCfg(s), t0 = Date.now(); qStart({ s, items: mockItems(s), mode: 'mock', ret: 'tasks', dur: n.min * 60, t0, deadline: t0 + n.min * 60000, task: t.id }); return true; }
    if (t.kind === 'lesson' && mi >= 0) { const T0 = (TC[s] || {})[r.topic]; if (T0) { const T = Object.assign({ __t: r.topic }, T0); S.pl = { s, mi, ti, T, steps: plSteps(T, s, mi), i: 0, r: 1, q: {}, auto: false, qn: 0, qok: 0, task: t.id, ret: 'tasks' }; S.tab = 'play'; return true; } }
    const items = mi >= 0 ? quizItems(s, mi, r.topic) : shuf((QB[s] || []).filter(x => !x[2])).slice(0, r.n || 10);
    qStart({ s, items, mode: 'quiz', ret: 'tasks', sp: mi >= 0 ? { mi, tp: r.topic } : undefined, task: t.id }); return true;
  }
  function taskDone(id, pct, label) {
    if (!id || !signedIn()) return;
    sync().table('task_submissions').then(q => q.upsert({ task_id: id, student_id: sync().uid(), body: label, auto_score: Math.max(0, Math.min(100, Math.round(pct))), submitted_at: new Date().toISOString() }))
      .then(r => { if (r && r.error) throw r.error; toast(L('Sent to your teacher', 'Enviado a tu profesor')); if (window.AceC && AceC.subs) AceC.subs[id] = Object.assign(AceC.subs[id] || {}, { auto_score: Math.round(pct), body: label, submitted_at: new Date().toISOString() }); })
      .catch(() => toast(L('Could not send your score. Check your connection.', 'No se pudo enviar tu nota.')));
  }

  /* ================= hooks called by the core app ================= */
  window.AceL = {
    badgeCount: () => badges().filter(x => x.ok).length,
    level: () => lvl(S.xp),
    launchTask,
    finished(kind, sc, n, task) {           // a quiz, practice set, mock or lesson just finished
      if (S.planKey) { P.pd = P.pd || {}; P.pd[S.planKey] = 1; S.planKey = null; }
      if (kind === 'lesson') P.lc = (P.lc || 0) + 1;
      if (kind === 'mock') P.mk = (P.mk || 0) + 1;
      if (S.streak > (P.bestStreak || 0)) P.bestStreak = S.streak;
      svP();
      if (task) taskDone(task, n ? sc * 100 / n : 100, kind === 'lesson' ? L('Finished the lesson in Ace', 'Lección terminada en Ace') : `${L('Scored', 'Nota')} ${sc}/${n} ${L('in Ace', 'en Ace')}`);
      S.taskRun = null;
    },
    homeCard(c) {
      const p = PL(); let h = CL.banner ? `<div class="card" style="margin-top:12px;border-color:var(--yellow);background:#FFF4D1;color:#5A3A00"><b>📢 ${esc(CL.banner)}</b></div>` : '';
      if (p && ACE_LOADED[S.c]) { const B = buildPlan(), d = B && B.days.find(x => x.d === todayKey()); if (d) { const left = d.items.filter(it => !isDone(it)).length; h += `<button class="plc" data-a="tab" data-v="plan"><span class="e">🗓️</span><span class="m"><b>${left ? TXF('Today\'s plan: {n} left', 'Plan de hoy: quedan {n}', { n: left }) : L("Today's plan is done", 'Plan de hoy completado')}</b><small>${esc(itemLabel(d.items.find(it => !isDone(it)) || d.items[0])[1])}</small></span><em>›</em></button>`; } }
      else h += `<button class="plc nw2" data-a="tab" data-v="plan"><span class="e">🗓️</span><span class="m"><b>${L('Make a study plan to exam day', 'Crea tu plan hasta el examen')}</b><small>${L('Two minutes to set up. Ace does the rest.', 'Dos minutos y Ace hace el resto.')}</small></span><em>›</em></button>`;
      const m = Mist.all().length;
      return h + `<div class="hq"><button data-a="tab" data-v="mist"><span>📕</span><b>${m}</b><small>${L('Mistakes', 'Errores')}</small></button><button data-a="tab" data-v="league"><span>🏆</span><b>${L('League', 'Liga')}</b><small>${L('This week', 'Esta semana')}</small></button><button data-a="tab" data-v="ach"><span>🏅</span><b>${L('Lv', 'Nv')} ${lvl(S.xp)}</b><small>${L('Achievements', 'Logros')}</small></button><button data-a="tab" data-v="well"><span>💚</span><b>${L('Check in', 'Cómo estás')}</b><small>${L('Wellbeing', 'Bienestar')}</small></button></div>`;
    }
  };

  Object.assign(V, { plan: planView, mist: mistView, ach: achView, league: leagueView, well: wellView, classes: classesView, cls1: classView });
  Object.assign(AceX.loaders, {
    league: () => { LG.err = ''; LG.rows = null; return signedIn() ? sync().rpc('weekly_league').then(r => { LG.rows = r || []; }).catch(e => { LG.err = (e && (e.msg || e.message)) || 'Error'; }) : null; },
    classes: () => { CL.err = ''; return signedIn() ? loadClasses() : null; },
    cls1: () => { CK.c = null; CK.err = ''; return signedIn() && CK.id ? Promise.all([CL.list ? null : loadClasses(), loadClass(CK.id)]) : null; }
  });

  try { const sy = sync(); if (sy && sy.ready) sy.ready().then(ok => ok ? sy.table('platform_config').then(q => q.select('banner').eq('id', 'global').maybeSingle()) : null).then(r => { if (r && r.data && r.data.banner) { CL.banner = r.data.banner; if (S.tab === 'home') render(); } }).catch(() => { }); } catch (e) { }
  document.addEventListener('input', e => {
    const t = e.target, k = t && t.dataset && t.dataset.lIn; if (!k) return;
    if (k === 'ccode') CL.code = t.value.toUpperCase();
    else if (k === 'ask') CK.ask = t.value;
    else if (k === 'exam') { S.pdraft = S.pdraft || Object.assign({}, PL() || {}); S.pdraft.exam = t.value; }
    else if (k === 'sleep' || k === 'wnote') { const W = get('ace-well', {}), d = todayKey(); W[d] = W[d] || { m: 2 }; if (k === 'sleep') W[d].s = t.value === '' ? null : +t.value; else W[d].n = t.value.slice(0, 280); put('ace-well', W); }
  });
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-l]'); if (!b) return; const a = b.dataset.l, v = b.dataset.v, c = C_();
    const D = () => (S.pdraft = S.pdraft || Object.assign({}, PL() || {}));
    if (a === 'mt') S.mt = v;
    else if (a === 'mdel') { Mist.remove(v); P.mclear = (P.mclear || 0) + 1; svP(); }
    else if (a === 'sdel') { put(SK, Mist.saved().filter(x => x.id !== v)); }
    else if (a === 'redo') { const list = (b.dataset.k === 's' ? Mist.saved() : Mist.all()).filter(m => m.s === v && m.o && m.o.length); redo(list, v); }
    else if (a === 'pday') { const d = D(); d.days = d.days || (PL() && PL().days) || [1, 2, 3, 4, 5, 6]; const n = +v; d.days = d.days.includes(n) ? d.days.filter(x => x !== n) : d.days.concat(n); }
    else if (a === 'pmin') { D().min = +v; }
    else if (a === 'psub') { const d = D(); d.subs = d.subs || (PL() && PL().subs) || c.s.filter(s => selOK(c, s) && QB[s]).slice(0, 6); d.subs = d.subs.includes(v) ? d.subs.filter(x => x !== v) : d.subs.concat(v); }
    else if (a === 'psave') { const d = D(); P.plan = { exam: d.exam || (PL() && PL().exam) || c.d, days: (d.days && d.days.length ? d.days : (PL() && PL().days) || [1, 2, 3, 4, 5, 6]), min: d.min || (PL() && PL().min) || 30, subs: (d.subs && d.subs.length ? d.subs : (PL() && PL().subs) || c.s.filter(s => selOK(c, s) && QB[s]).slice(0, 6)), made: todayKey() }; S.pedit = false; S.pdraft = null; svP(); toast(L('Your plan is ready', 'Tu plan está listo')); }
    else if (a === 'pedit') { S.pedit = true; S.pdraft = Object.assign({}, PL() || {}); }
    else if (a === 'ptick') { P.pd = P.pd || {}; if (P.pd[v]) delete P.pd[v]; else P.pd[v] = 1; svP(); }
    else if (a === 'pgo') { const B = buildPlan(), it = B && B.days.flatMap(d => d.items).find(x => x.key === v); if (it) launch(it); }
    else if (a === 'mood') { const W = get('ace-well', {}), d = todayKey(); W[d] = Object.assign(W[d] || {}, { m: +v }); put('ace-well', W); }
    else if (a === 'lghide') { sync().table('profiles').then(q => q.update({ league_hidden: true }).eq('id', sync().uid())).then(() => { toast(L('You are hidden from the league', 'Ya no apareces en la liga')); AceX.loaders.league().then(() => render()); }); return; }
    else if (a === 'cjoin') { const code = CL.code.trim(); if (code.length < 5) { CL.err = L('Enter the code your teacher gave you.', 'Introduce el código de tu profesor.'); return render(); } CL.busy = true; CL.err = ''; CL.ok = ''; render(); sync().rpc('join_class', { p_code: code }).then(r => { CL.busy = false; const d = r || {}; CL.ok = (d.teachers ? TXF('You joined {a} with {b}.', 'Te uniste a {a}.', { a: d.name, b: d.teachers }) : TXF('You joined {a}.', 'Te uniste a {a}.', { a: d.name })); CL.code = ''; return loadClasses(); }).catch(er => { CL.busy = false; CL.err = (er && (er.msg || er.message)) || 'Error'; }).then(() => render()); return; }
    else if (a === 'cleave') { if (b.dataset.sure !== '1') { b.dataset.sure = '1'; b.textContent = L('Tap again to leave', 'Toca otra vez para salir'); return; } sync().rpc('leave_class', { p_class: v }).then(() => loadClasses()).then(() => { S.tab = 'classes'; render(); }); return; }
    else if (a === 'copen') { CK.id = v; S.tab = 'cls1'; }
    else if (a === 'ask') { const body = CK.ask.trim(); if (body.length < 3) return; sync().table('class_questions').then(q => q.insert({ class_id: CK.id, author_id: sync().uid(), body })).then(r => { if (r.error) throw r.error; CK.ask = ''; toast(L('Question sent to your teacher', 'Pregunta enviada')); return loadClass(CK.id); }).catch(e => toast((e && (e.msg || e.message)) || 'Error')).then(() => render()); return; }
    else return;
    render();
  });
})();
