/* Ace "My school" module for students whose school uses Ace: teacher notices and messages, class tasks, live quiz.
   Teachers create these in /staff/. All access rules are enforced by Postgres RLS. Loaded after learn.js. */
(function () {
  'use strict';
  if (!window.AceX || !AceX.h) return;
  const { L, esc, back, needSignIn, signedIn, sync } = AceX.h, X = AceX;
  const Cl = window.AceC = { prof: null, ann: null, msgs: null, teachers: [], peer: '', draft: '', tasks: null, subs: {}, task: '', body: '', live: { code: '', s: null, mine: {}, err: '', timer: 0 }, err: '' };
  const msg = e => (e && (e.msg || e.message)) || L('Something went wrong. Try again.', 'Algo salió mal.');
  const err = () => Cl.err ? `<p class="note" style="color:var(--red)">${esc(Cl.err)}</p>` : '';
  const hasSchool = () => !!(Cl.prof && Cl.prof.school_id);
  const noSchool = () => `<div class="card"><b>${L('This is for students whose school uses Ace.', 'Para estudiantes de colegios que usan Ace.')}</b><p class="note">${L('Ask your school to set you up, or join with your school code on the sign-in page.', 'Pide a tu colegio que te dé acceso.')}</p></div>`;
  const rerun = p => p.then(() => render()).catch(e => { Cl.err = msg(e); render(); });
  const loadProf = () => sync().table('profiles').then(q => q.select('id,class_id,school_id,first_name').eq('id', sync().uid()).maybeSingle()).then(r => { Cl.prof = r.data || {}; });

  function inboxView() {
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('From my teachers', 'De mis profesores')}</h2>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (!Cl.ann) return h + (Cl.err ? err() : '<p class="note">…</p>') + '</div>';
    if (!hasSchool()) return h + noSchool() + '</div>';
    h += `<div class="sh">${L('Notices', 'Avisos')}</div>` + (Cl.ann.length ? Cl.ann.map(a => `<div class="card" style="margin:8px 0"><b>${esc(a.title)}</b><p style="margin:4px 0;white-space:pre-wrap;line-height:1.5">${esc(a.body)}</p><small>${esc(String(a.created_at).slice(0, 10))}</small></div>`).join('') : `<p class="note">${L('No notices.', 'Sin avisos.')}</p>`);
    h += `<div class="sh">${L('Messages', 'Mensajes')}</div><label class="xl">${L('Talk to', 'Hablar con')}<select class="xin" data-c-in="peer"><option value="">${L('Choose a teacher', 'Elige un profesor')}</option>${Cl.teachers.map(t => `<option value="${t.teacher_id}" ${Cl.peer === t.teacher_id ? 'selected' : ''}>${esc(t.first_name + ' ' + t.surname)} (${esc(t.subject)})</option>`).join('')}</select></label>`;
    if (Cl.peer) {
      const th = (Cl.msgs || []).filter(m => m.sender_id === Cl.peer || m.recipient_id === Cl.peer);
      h += `<div class="card" style="margin-top:8px">${th.map(m => `<p style="margin:6px 0;${m.sender_id === sync().uid() ? 'text-align:right' : ''}"><span class="xtag" style="background:var(--tint);color:var(--text);white-space:pre-wrap">${esc(m.body)}</span><br><small>${esc(String(m.created_at).slice(5, 16).replace('T', ' '))}</small></p>`).join('') || `<p class="note">${L('No messages yet.', 'Sin mensajes.')}</p>`}
<textarea class="xin" rows="2" maxlength="2000" data-c-in="draft" placeholder="${L('Write a message to your teacher', 'Escribe a tu profesor')}">${esc(Cl.draft)}</textarea><button class="nx" data-c="send">${L('Send', 'Enviar')}</button></div><p class="note">${L('Messages go to your teacher only. Be polite and keep it about school.', 'Solo los ve tu profesor.')}</p>`;
    }
    return h + err() + '</div>';
  }
  function tasksView() {
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('Class tasks', 'Tareas de clase')}</h2>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (!Cl.tasks) return h + (Cl.err ? err() : '<p class="note">…</p>') + '</div>';
    if (!hasSchool()) return h + noSchool() + '</div>';
    if (Cl.task) {
      const t = Cl.tasks.find(x => x.id === Cl.task), s = Cl.subs[Cl.task];
      if (t) return h.replace(back(), `<div class="bk"><button class="bb" data-c="tback">\u2039 ${L('Tasks', 'Tareas')}</button></div>`) + `<div class="card"><b>${esc(t.title)}</b> ${t.subject ? '<small>' + esc(t.subject) + '</small>' : ''}<p style="white-space:pre-wrap;line-height:1.5">${esc(t.body || '')}</p><small>${t.due_on ? L('Due', 'Fecha') + ' ' + esc(t.due_on) : ''}</small></div>
${s && s.mark != null ? `<div class="card"><b>${L('Mark', 'Nota')}: ${esc(s.mark)}</b>${s.feedback ? `<p style="margin:4px 0">${esc(s.feedback)}</p>` : ''}</div>` : ''}
<textarea class="xin" rows="6" maxlength="8000" data-c-in="body" placeholder="${L('Type your answer', 'Escribe tu respuesta')}">${esc(Cl.body)}</textarea><button class="nx" data-c="submit">${s ? L('Update my answer', 'Actualizar') : L('Submit', 'Enviar')}</button>${s ? `<p class="note">${L('Submitted', 'Enviado')} ${esc(String(s.submitted_at).slice(0, 16).replace('T', ' '))}</p>` : ''}${err()}</div>`;
    }
    return h + (Cl.tasks.length ? `<div class="lst">${Cl.tasks.map(t => { const s = Cl.subs[t.id]; return `<button class="li" data-c="topen" data-v="${t.id}"><span class="m"><b>${esc(t.title)}</b><small>${t.due_on ? L('Due', 'Fecha') + ' ' + esc(t.due_on) + ' • ' : ''}${s ? (s.mark != null ? L('Marked', 'Corregida') + ' ' + esc(s.mark) : L('Submitted', 'Enviada')) : L('Not submitted', 'Sin enviar')}</small></span><span class="v">›</span></button>`; }).join('')}</div>` : `<p class="note">${L('No tasks right now.', 'Sin tareas.')}</p>`) + err() + '</div>';
  }
  function liveView() {
    const l = Cl.live;
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('Live quiz', 'Quiz en vivo')}</h2>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (!l.s) return h + `<div class="card"><label class="xl">${L('Enter the code from your teacher', 'Introduce el código de tu profesor')}<input class="xin" data-c-in="lcode" maxlength="8" style="text-transform:uppercase;letter-spacing:.2em;font-size:20px" value="${esc(l.code)}"></label><button class="nx" data-c="ljoin">${L('Join', 'Entrar')}</button>${l.err ? `<p class="note" style="color:var(--red)">${esc(l.err)}</p>` : ''}</div></div>`;
    const s = l.s, qs = s.questions || [], mine = Object.keys(l.mine).length, ok = Object.values(l.mine).filter(x => x.correct).length;
    if (s.state === 'lobby') return h + `<div class="emp"><span class="e">⏳</span><b>${L('Waiting for your teacher to start', 'Esperando al profesor')}</b></div></div>`;
    if (s.state === 'ended') return h + `<div class="emp"><span class="e">🏁</span><b>${ok} / ${qs.length}</b>${L('Quiz finished. Well done!', 'Quiz terminado.')}</div><button class="nx" data-c="lleave">${L('Done', 'Listo')}</button></div>`;
    const q = qs[s.current_index], a = l.mine[s.current_index];
    if (!q) return h + '</div>';
    return h + `<small>${L('Question', 'Pregunta')} ${s.current_index + 1} / ${qs.length}</small><div class="card"><b>${esc(q.q)}</b>${q.o.map((o, i) => `<button class="li xopt ${a && a.choice === i ? (a.correct === true ? 'ok' : a.correct === false ? 'bad' : 'ok') : ''}" data-c="lans" data-v="${i}" ${a ? 'disabled' : ''}>${'ABCD'[i]}. ${esc(o)}</button>`).join('')}</div>${a ? `<p class="note">${L('Answer sent. Wait for the next question.', 'Respuesta enviada. Espera la siguiente.')}</p>` : ''}${l.err ? `<p class="note" style="color:var(--red)">${esc(l.err)}</p>` : ''}</div>`;
  }
  const poll = () => {
    const l = Cl.live; if (S.tab !== 'livej' || !l.s) return;
    sync().table('live_sessions').then(q => q.select('id,state,current_index,questions').eq('id', l.s.id).maybeSingle())
      .then(r => { if (!r.data) return; const changed = JSON.stringify([r.data.state, r.data.current_index]) !== JSON.stringify([l.s.state, l.s.current_index]); l.s = r.data; return sync().table('live_answers').then(q => q.select('q_index,choice,correct').eq('session_id', l.s.id)).then(a => { (a.data || []).forEach(x => l.mine[x.q_index] = x); if (changed) render(); }); }).catch(() => { });
  };
  setInterval(poll, 2500);

  Object.assign(V, { inbox: inboxView, tasks: tasksView, livej: liveView });
  Object.assign(X.loaders, {
    inbox: () => loadProf().then(() => hasSchool() ? Promise.all([sync().table('announcements').then(q => q.select('title,body,created_at,class_id').order('created_at', { ascending: false }).limit(20)), sync().table('messages').then(q => q.select('id,sender_id,recipient_id,body,created_at,read_at').order('created_at', { ascending: true }).limit(200)), sync().rpc('my_teachers')]).then(([a, m, t]) => { Cl.ann = a.data || []; Cl.msgs = m.data || []; Cl.teachers = t || []; }) : (Cl.ann = [])),
    tasks: () => loadProf().then(() => hasSchool() ? Promise.all([sync().table('tasks').then(q => q.select('*').order('created_at', { ascending: false }).limit(50)), sync().table('task_submissions').then(q => q.select('task_id,body,submitted_at,mark,feedback'))]).then(([t, s]) => { Cl.tasks = t.data || []; Cl.subs = {}; (s.data || []).forEach(x => Cl.subs[x.task_id] = x); }) : (Cl.tasks = [])),
    livej: () => loadProf()
  });

  document.addEventListener('input', e => {
    const t = e.target, k = t && t.dataset && t.dataset.cIn; if (!k) return;
    if (k === 'draft') Cl.draft = t.value; else if (k === 'body') Cl.body = t.value; else if (k === 'lcode') Cl.live.code = t.value.toUpperCase();
  });
  document.addEventListener('change', e => { const t = e.target; if (t && t.dataset && t.dataset.cIn === 'peer') { Cl.peer = t.value; render(); if (Cl.peer) sync().table('messages').then(q => q.update({ read_at: new Date().toISOString() }).eq('recipient_id', sync().uid()).eq('sender_id', Cl.peer).is('read_at', null)).catch(() => { }); } });
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-c]'); if (!b) return; const a = b.dataset.c, v = b.dataset.v; Cl.err = '';
    if (a === 'send') { const body = Cl.draft.trim(); if (!body) return; rerun(sync().table('messages').then(q => q.insert({ school_id: Cl.prof.school_id, sender_id: sync().uid(), recipient_id: Cl.peer, body })).then(r => { if (r.error) throw { msg: r.error.message }; Cl.msgs.push({ sender_id: sync().uid(), recipient_id: Cl.peer, body, created_at: new Date().toISOString() }); Cl.draft = ''; })); }
    else if (a === 'tback') { Cl.task = ''; render(); }
    else if (a === 'topen') { Cl.task = v; Cl.body = (Cl.subs[v] && Cl.subs[v].body) || ''; render(); }
    else if (a === 'submit') { const id = Cl.task, body = Cl.body.trim(); if (!body) { Cl.err = L('Write your answer first.', 'Escribe tu respuesta.'); return render(); } rerun(sync().table('task_submissions').then(q => q.upsert({ task_id: id, student_id: sync().uid(), body, submitted_at: new Date().toISOString() })).then(r => { if (r.error) throw { msg: r.error.message }; Cl.subs[id] = Object.assign({}, Cl.subs[id], { task_id: id, body, submitted_at: new Date().toISOString() }); toast(L('Submitted.', 'Enviado.')); })); }
    else if (a === 'ljoin') { const l = Cl.live; l.err = ''; sync().table('live_sessions').then(q => q.select('id,state,current_index,questions').eq('code', l.code.trim().toUpperCase()).maybeSingle()).then(r => { if (!r.data) { l.err = L('No quiz with that code for your class.', 'No hay quiz con ese código.'); return render(); } l.s = r.data; l.mine = {}; render(); }).catch(er => { l.err = msg(er); render(); }); }
    else if (a === 'lans') { const l = Cl.live, qi = l.s.current_index; l.mine[qi] = { q_index: qi, choice: +v, correct: null }; render(); sync().table('live_answers').then(q => q.insert({ session_id: l.s.id, student_id: sync().uid(), q_index: qi, choice: +v })).then(r => { if (r.error) { delete l.mine[qi]; l.err = r.error.message; render(); } }).catch(er => { delete l.mine[qi]; l.err = msg(er); render(); }); }
    else if (a === 'lleave') { Cl.live = { code: '', s: null, mine: {}, err: '' }; render(); }
  });
})();
