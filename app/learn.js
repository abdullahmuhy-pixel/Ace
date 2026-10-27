/* Ace "Learn" module: certificate courses, university explorer, moderated study groups, lecture-note summariser, plans and
   checkout, push opt-in. Loaded after today.js (uses AceX.h helpers). Server rules (grading, moderation, access) live in Postgres. */
(function () {
  'use strict';
  if (!window.AceX || !AceX.h) return;
  const { L, esc, back, needSignIn, signedIn, sync, fail, cname } = AceX.h;
  const X = AceX;
  const Lr = window.AceL = {
    idx: null, cq: { cat: 'all', q: '' }, slug: null, course: null, lesson: null, prog: {}, certs: [], quiz: { ans: {}, res: null, busy: false }, err: '',
    uni: { cc: null, data: {}, q: '', open: null }, grp: { mine: null, find: null, id: null, name: '', role: '', feed: null, roster: null, draft: '', showRoster: false, form: { name: '', desc: '', scope: 'class' } },
    nt: { subject: '', text: '', busy: false, res: null, ans: {}, flip: {}, saved: false, err: '' }, pl: { list: null, access: null, busy: '', promo: '' }
  };
  const cache = {};
  const getJSON = path => cache[path] ? Promise.resolve(cache[path]) : fetch(path).then(r => { if (!r.ok) throw { msg: L('Could not load this content. Check your connection.', 'No se pudo cargar. Revisa tu conexión.') }; return r.json(); }).then(j => (cache[path] = j));
  const go = (tab) => { S.tab = tab; X.loaded = ''; X.err = ''; Lr.err = ''; render(); };
  const msg = e => (e && (e.msg || e.message)) || L('Something went wrong. Try again.', 'Algo salió mal. Inténtalo de nuevo.');
  const err = () => (Lr.err || X.err) ? `<p class="note" style="color:var(--red)">${esc(Lr.err || X.err)}</p>` : '';
  const when = d => String(d || '').slice(0, 10);
  const doneOf = slug => signedIn() ? (Lr.prog[slug] || []) : ((P.cl || {})[slug] || []);

  /* ================= COURSES ================= */
  const CATS = [['study', 'Study and exams', 'Estudio y exámenes'], ['code', 'Code and tech', 'Código y tecnología'], ['digital', 'Digital skills and safety', 'Habilidades digitales'], ['business', 'Business and money', 'Negocios y dinero'], ['work', 'Work and community', 'Trabajo y comunidad'], ['think', 'Thinking, language, numbers', 'Pensamiento, lenguaje, números']];
  function courseList() {
    const lv = P.lvl || 'secondary', order = c => (c.level === lv ? 0 : c.level === 'all' ? 1 : 2), q = Lr.cq.q.trim().toLowerCase();
    const list = [...Lr.idx].filter(c => (Lr.cq.cat === 'all' || c.category === Lr.cq.cat) && (!q || (c.title + ' ' + c.summary).toLowerCase().includes(q))).sort((a, b) => order(a) - order(b));
    if (!list.length) return `<p class="note">${L('No course matches. Try another word.', 'Ningún curso coincide.')}</p>`;
    return list.map(c => {
      const d = doneOf(c.slug).length, cert = Lr.certs.find(x => x.course === c.slug);
      return `<button class="li card" style="display:block;width:100%;text-align:left;margin:8px 0" data-l="open" data-v="${esc(c.slug)}"><b>${esc(c.title)}</b>${cert ? ' <span class="xtag">' + L('Certified', 'Certificado') + '</span>' : ''}<br><small>${esc(c.summary)}</small><br><small>${c.lessons} ${L('lessons', 'lecciones')} • ~${c.hours} h${d ? ' • ' + d + '/' + c.lessons + ' ' + L('done', 'hechas') : ''}</small></button>`;
    }).join('');
  }
const claimCard = (slug, score) => `<div class="card" style="text-align:center"><b>${L('You passed! Your verified certificate comes with a plan.', '¡Aprobado! El certificado verificado viene con un plan.')}</b><p class="note">${L('Your pass is saved. Claim the certificate whenever you have a plan, a trial or a school licence.', 'Tu aprobado queda guardado. Reclama el certificado cuando tengas un plan, una prueba o licencia del centro.')}</p>${window.AceTier && AceTier.paid() ? `<button class="nx" data-l="claim" data-v="${esc(slug)}">${L('Claim my certificate', 'Reclamar mi certificado')}</button>` : `<button class="nx" data-a="upsell" data-v="cert">${L('See plans', 'Ver planes')}</button>`}</div>`;
  function learnView() {
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 4px">${L('Courses', 'Cursos')}</h2><p class="note" style="margin:0 0 8px">${L('Short courses you can finish in an evening. Pass the quiz to earn a certificate you can share and anyone can verify.', 'Cursos cortos. Aprueba el test y obtén un certificado verificable.')}</p>`;
    if (!Lr.idx) return h + (Lr.err ? err() : '<p class="note">…</p>') + '</div>';
    const lv = P.lvl || 'secondary', order = c => (c.level === lv ? 0 : c.level === 'all' ? 1 : 2);
    h += `<input class="xin" data-l-in="cq" placeholder="${L('Search courses, e.g. python, money', 'Buscar cursos')}" value="${esc(Lr.cq.q)}" style="margin:6px 0"><div class="xchips">${[['all', L('All', 'Todos')]].concat(CATS.map(c => [c[0], L(c[1], c[2])])).map(c => `<button class="xchip ${Lr.cq.cat === c[0] ? 'on' : ''}" data-l="ccat" data-v="${c[0]}">${esc(c[1])}</button>`).join('')}</div><div id="cres">${courseList()}</div>`;
    if ((Lr.unc || []).length) h += `<div class="sh">${L('Passed, certificate waiting', 'Aprobados, certificado pendiente')}</div>` + Lr.unc.map(u => `<div class="card" style="margin:8px 0"><b>${esc((Lr.idx.find(x => x.slug === u.course) || {}).title || u.course)}</b> <small>${u.score}%</small>${window.AceTier && AceTier.paid() ? ` <button class="xlink" data-l="claim" data-v="${esc(u.course)}">${L('Claim my certificate', 'Reclamar mi certificado')}</button>` : ` <button class="xlink" data-a="upsell" data-v="cert">${L('Get it with a plan', 'Consíguelo con un plan')}</button>`}</div>`).join('');
    if (Lr.certs.length) h += `<div class="sh">${L('My certificates', 'Mis certificados')}</div><div class="lst">${Lr.certs.map(c => `<a class="li" href="../verify/?code=${esc(c.code)}" target="_blank" rel="noopener"><span class="m"><b>${esc((Lr.idx.find(x => x.slug === c.course) || {}).title || c.course)}</b><small>${c.score}% • ${esc(when(c.issued_at))} • ${esc(c.code)}</small></span><span class="v">›</span></a>`).join('')}</div>`;
    return h + err() + '</div>';
  }
  function courseView() {
    const c = Lr.course;
    if (!c) return `<div class="pad">${back('learn')}${Lr.err ? err() : '<p class="note">…</p>'}</div>`;
    const done = doneOf(c.slug), all = done.length >= c.lessons.length, cert = Lr.certs.find(x => x.course === c.slug);
    return `<div class="pad">${back('learn')}<h2 style="margin:0 0 4px">${esc(c.title)}</h2><p class="note" style="margin:0 0 8px">${esc(c.summary)}</p>
<div class="lst">${c.lessons.map((l, i) => `<button class="li" data-l="lesson" data-v="${esc(l.id)}"><span class="e">${done.includes(l.id) ? '✅' : (i + 1)}</span><span class="m"><b>${esc(l.title)}</b><small>${l.minutes} min</small></span><span class="v">›</span></button>`).join('')}</div>
<button class="nx" style="margin-top:12px" data-l="quiz" ${all ? '' : 'disabled'}>${all ? L('Take the quiz', 'Hacer el test') : L('Finish all lessons to unlock the quiz', 'Termina las lecciones para el test')} (${c.quiz.length} ${L('questions', 'preguntas')}, ${L('pass mark', 'nota mínima')} ${c.pass_mark}%)</button>
${cert ? `<p class="note">🎓 ${L('Certificate', 'Certificado')}: <a href="../verify/?code=${esc(cert.code)}" target="_blank" rel="noopener">${esc(cert.code)}</a></p>` : ''}
${!signedIn() ? `<p class="note">${L('You can read the lessons as a guest. Sign in to save progress, take the quiz and earn the certificate.', 'Puedes leer como invitado. Inicia sesión para guardar y obtener el certificado.')}</p>` : ''}${err()}</div>`;
  }
  const block = b => b.p != null ? `<p style="line-height:1.6">${esc(b.p)}</p>` : b.h != null ? `<h3 style="margin:16px 0 4px">${esc(b.h)}</h3>` :
    b.list ? `<ul class="xul">${b.list.map(x => `<li>${esc(x)}</li>`).join('')}</ul>` : b.steps ? `<ol class="xul">${b.steps.map(x => `<li>${esc(x)}</li>`).join('')}</ol>` :
    b.tip != null ? `<div class="card" style="margin:10px 0">💡 ${esc(b.tip)}</div>` : b.code != null ? `<pre class="xcode"><code>${esc(b.code)}</code></pre>` : '';
  function lessonView() {
    const c = Lr.course; if (!c) return '';
    const i = c.lessons.findIndex(l => l.id === Lr.lesson), l = c.lessons[i]; if (!l) return `<div class="pad">${back('course')}</div>`;
    const done = doneOf(c.slug).includes(l.id), next = c.lessons[i + 1];
    return `<div class="pad">${back('course', c.title)}<small>${L('Lesson', 'Lección')} ${i + 1} / ${c.lessons.length} • ${l.minutes} min</small><h2 style="margin:4px 0 8px">${esc(l.title)}</h2>${l.body.map(block).join('')}
<button class="nx" data-l="done" data-v="${esc(l.id)}">${done ? L('Completed. Continue', 'Completada. Continuar') : L('Mark complete and continue', 'Marcar y continuar')}${next ? '' : ' → ' + L('quiz', 'test')}</button>${err()}</div>`;
  }
  function quizView() {
    const c = Lr.course, q = Lr.quiz; if (!c) return '';
    if (!signedIn()) return `<div class="pad">${back('course')}<h2>${esc(c.title)}</h2>${needSignIn()}</div>`;
    if (q.res) {
      const r = q.res;
      return `<div class="pad">${back('course', c.title)}<div class="emp"><span class="e">${r.passed ? '🎓' : '📚'}</span><b>${r.score}% (${r.correct}/${r.total})</b>${r.passed ? L('You passed!', '¡Aprobado!') : L('Pass mark is', 'La nota mínima es') + ' ' + r.pass_mark + '%. ' + L('Review the lessons and try again.', 'Repasa y vuelve a intentarlo.')}</div>
${r.passed && !r.code && r.locked ? claimCard(c.slug, r.score) : ''}${r.passed && r.code ? `<div class="card" style="text-align:center"><small>${L('Your certificate code', 'Tu código de certificado')}</small><div style="font-size:22px;font-weight:800;letter-spacing:.1em">${esc(r.code)}</div><a class="xlink" href="../verify/?code=${esc(r.code)}" target="_blank" rel="noopener">${L('Open certificate', 'Abrir certificado')}</a> <button class="xlink" data-x="copy" data-v="${esc(r.code)}">${L('Copy code', 'Copiar')}</button></div>` : ''}
<div class="sh">${L('Review', 'Revisión')}</div>${c.quiz.map((x, i) => { const rv = (r.review || []).find(y => y.qid === x.id) || {}; return `<div class="card" style="margin-bottom:8px"><b>${i + 1}. ${esc(x.q)}</b><p class="note">${rv.ok ? '✅ ' + L('Correct', 'Correcto') : '❌ ' + esc(rv.why || '')}</p></div>`; }).join('')}
<button class="nx" data-l="quizretry">${L('Back to the course', 'Volver al curso')}</button></div>`;
    }
    const n = Object.keys(q.ans).length;
    return `<div class="pad">${back('course', c.title)}<h2 style="margin:0 0 4px">${L('Quiz', 'Test')}</h2><p class="note">${n}/${c.quiz.length} ${L('answered', 'respondidas')}. ${L('5 attempts per day.', '5 intentos al día.')}</p>
${c.quiz.map((x, i) => `<div class="card" style="margin-bottom:10px"><b>${i + 1}. ${esc(x.q)}</b>${x.options.map((o, oi) => `<button class="li xopt ${q.ans[x.id] === oi ? 'ok' : ''}" data-l="ans" data-v="${esc(x.id)}:${oi}">${'ABCD'[oi]}. ${esc(o)}</button>`).join('')}</div>`).join('')}
<button class="nx" data-l="submit" ${n < c.quiz.length || q.busy ? 'disabled' : ''}>${q.busy ? '…' : L('Submit answers', 'Enviar respuestas')}</button>${err()}</div>`;
  }

  /* ================= UNIVERSITIES ================= */
  const CCS = ['NG', 'GH', 'SL', 'GM', 'KE', 'ZM', 'GB', 'CA', 'ES', 'IE', 'ZA', 'UG', 'TZ', 'LR', 'MT', 'ZW', 'BW', 'FR', 'IT'];
  const uniCC = () => Lr.uni.cc || (typeof HOMECC === 'function' ? HOMECC() : S.c);
  function uniResults() {
    const d = Lr.uni.data[uniCC()], q = Lr.uni.q.trim().toLowerCase(); if (!d) return '';
    if (q.length >= 2) {
      const hits = [];
      d.universities.forEach((u, ui) => u.faculties.forEach((f, fi) => f.courses.forEach((c, ci) => { if ((c.name + ' ' + f.name).toLowerCase().includes(q)) hits.push([u, f, c, ui + ':' + fi + ':' + ci]); })));
      if (!hits.length) return `<p class="note">${L('No course matches. Try a shorter word.', 'Sin resultados. Prueba otra palabra.')}</p>`;
      return `<div class="lst">${hits.slice(0, 40).map(([u, f, c, k]) => `<div class="li"><span class="m"><b>${esc(c.name)}</b><small>${esc(u.short)} • ${esc(f.name)}${c.years ? ' • ' + c.years + ' ' + L('yrs', 'años') : ''}</small></span><button class="xlink" data-l="goal" data-v="${k}">${L('My goal', 'Mi objetivo')}</button></div>`).join('')}</div>${hits.length > 40 ? `<p class="note">${L('Showing 40 of', 'Mostrando 40 de')} ${hits.length}.</p>` : ''}`;
    }
    return d.universities.map((u, ui) => { const open = Lr.uni.open === u.id; return `<div class="card" style="margin:10px 0"><button class="xlink" style="display:block;width:100%;text-align:left;padding:0" data-l="uopen" data-v="${esc(u.id)}"><b style="font-size:15px;color:var(--text)">${esc(u.name)}</b> <small style="color:var(--text3)">${esc(u.short)} • ${esc(u.city)} • ${esc(u.type)}</small></button>
${open ? `<p class="note"><a href="${esc(u.url)}" target="_blank" rel="noopener">${L('Official website', 'Web oficial')}</a>${u.admissions_url ? ` • <a href="${esc(u.admissions_url)}" target="_blank" rel="noopener">${L('Admissions', 'Admisiones')}</a>` : ''} • ${L('checked', 'revisado')} ${esc(u.verified_on)}</p>${u.faculties.map((f, fi) => `<div class="sh" style="margin:12px 0 6px">${esc(f.name)}</div><ul class="xul" style="margin:0">${f.courses.map((c, ci) => `<li>${esc(c.name)}${c.years ? ' <small>(' + c.years + ' ' + L('yrs', 'años') + ')</small>' : ''}${c.note ? ' <small>• ' + esc(c.note) + '</small>' : ''} <button class="xlink" data-l="goal" data-v="${ui}:${fi}:${ci}">${L('My goal', 'Mi objetivo')}</button></li>`).join('')}</ul>`).join('')}` : ''}</div>`; }).join('');
  }
  function unisView() {
    const cc = uniCC(), d = Lr.uni.data[cc];
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 4px">${L('Universities', 'Universidades')}</h2><div class="xchips">${CCS.map(k => `<button class="xchip ${k === cc ? 'on' : ''}" data-l="ucc" data-v="${k}">${k}</button>`).join('')}</div>`;
    if (!d) return h + (Lr.err ? err() : '<p class="note">…</p>') + '</div>';
    const a = d.admissions_overview;
    h += `<div class="card"><b>${L('How admission works', 'Cómo es el acceso')}</b><p class="note" style="font-size:13px;line-height:1.5">${esc(a.summary)}</p>${a.notes ? `<p class="note">${esc(a.notes)}</p>` : ''}<a href="${esc(a.official_url)}" target="_blank" rel="noopener">${L('Official source', 'Fuente oficial')}</a></div>
<input class="xin" data-l-in="uq" placeholder="${L('Search courses, e.g. nursing', 'Buscar carreras, p. ej. enfermería')}" value="${esc(Lr.uni.q)}" style="margin:10px 0"><div id="ures">${uniResults()}</div>
<p class="note">${L('This list is a starting point, not the full catalogue. Entry requirements, deadlines and fees change every year, so always confirm on the university’s own website. Last updated', 'Esta lista es un punto de partida. Requisitos, plazos y tasas cambian cada año: confirma siempre en la web de la universidad. Actualizado')} ${esc(d.updated)}.</p></div>`;
    return h;
  }

  /* ================= STUDY GROUPS ================= */
  const scopeName = s => ({ class: L('Class', 'Clase'), school: L('School', 'Colegio'), institution: L('Campus', 'Campus') }[s] || s);
  function groupsView() {
    const g = Lr.grp;
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 4px">${L('Study groups', 'Grupos de estudio')}</h2><p class="note" style="margin:0 0 8px">${L('Groups are only for your own class, school or campus. No links, e-mails or phone numbers. Members can report posts, and teachers can see school groups.', 'Solo para tu clase, colegio o campus. Sin enlaces, correos ni teléfonos. Los miembros pueden denunciar y los profesores ven los grupos del colegio.')}</p>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (!g.mine) return h + (Lr.err ? err() : '<p class="note">…</p>') + '</div>';
    const uni = (P.lvl || 'secondary') === 'university';
    h += `<div class="sh">${L('My groups', 'Mis grupos')}</div>` + (g.mine.length ? `<div class="lst">${g.mine.map(x => `<button class="li" data-l="gopen" data-v="${x.id}"><span class="m"><b>${esc(x.name)}</b><small>${scopeName(x.scope)} • ${x.members} ${L('members', 'miembros')}${x.role === 'mod' ? ' • ' + L('moderator', 'moderador') : ''}</small></span><span class="v">›</span></button>`).join('')}</div>` : `<p class="note">${L('You are not in a group yet.', 'Aún no estás en ningún grupo.')}</p>`);
    if ((g.find || []).length) h += `<div class="sh">${L('Groups you can join', 'Grupos disponibles')}</div><div class="lst">${g.find.map(x => `<div class="li"><span class="m"><b>${esc(x.name)}</b><small>${scopeName(x.scope)} • ${x.members} ${L('members', 'miembros')}</small></span><button class="xlink" data-l="gjoin" data-v="${x.id}">${L('Join', 'Unirse')}</button></div>`).join('')}</div>`;
    h += `<div class="sh">${L('Start a group', 'Crear un grupo')}</div><div class="card"><input class="xin" data-l-in="gname" maxlength="60" placeholder="${L('Group name', 'Nombre')}" value="${esc(g.form.name)}"><input class="xin" data-l-in="gdesc" maxlength="300" placeholder="${L('What is it for? (optional)', 'Para qué es (opcional)')}" value="${esc(g.form.desc)}">
<select class="xin" data-l-in="gscope">${(uni ? ['institution'] : ['class', 'school']).map(s => `<option value="${s}" ${g.form.scope === s ? 'selected' : ''}>${scopeName(s)}</option>`).join('')}</select><button class="nx" data-l="gcreate">${L('Create group', 'Crear grupo')}</button></div>${err()}</div>`;
    return h;
  }
  const isMod = () => Lr.grp.role === 'mod' || Lr.grp.staff;
  function feedHtml() {
    const g = Lr.grp; if (!g.feed) return '<p class="note">…</p>';
    if (!g.feed.length) return `<p class="note">${L('No posts yet. Start the conversation.', 'Aún no hay mensajes.')}</p>`;
    return g.feed.map(p => `<div class="card" style="margin:8px 0;${p.hidden ? 'opacity:.7;border-style:dashed' : ''}"><div style="display:flex;gap:8px"><b style="flex:1">${esc(p.author)}</b><small>${esc(String(p.created_at).slice(5, 16).replace('T', ' '))}</small></div>
<p style="margin:4px 0;line-height:1.5;white-space:pre-wrap">${p.hidden && !isMod() ? '' : esc(p.body)}</p>${p.hidden ? `<small>⚠ ${esc(p.hidden_reason || L('Hidden', 'Oculto'))}${p.reports ? ' • ' + p.reports + ' ' + L('reports', 'denuncias') : ''}</small>` : ''}
<div>${!p.mine ? `<button class="xlink" data-l="report" data-v="${p.id}">⚑ ${L('Report', 'Denunciar')}</button>` : ''}${isMod() ? (p.hidden ? `<button class="xlink" data-l="mod" data-v="${p.id}:restore">${L('Restore', 'Restaurar')}</button>` : `<button class="xlink" data-l="mod" data-v="${p.id}:hide">${L('Hide', 'Ocultar')}</button>`) + `<button class="xlink" data-l="mod" data-v="${p.id}:remove">${L('Remove', 'Eliminar')}</button>` : ''}</div></div>`).join('');
  }
  function groupView() {
    const g = Lr.grp;
    let h = `<div class="pad">${back('groups', L('Groups', 'Grupos'))}<div style="display:flex;align-items:center;gap:8px"><h2 style="margin:0;flex:1">${esc(g.name)}</h2><button class="xlink" data-l="grefresh">↻</button></div>
<textarea class="xin" rows="3" maxlength="1000" data-l-in="gdraft" placeholder="${L('Write a message (no links, e-mails or phone numbers)', 'Escribe un mensaje (sin enlaces, correos ni teléfonos)')}">${esc(g.draft)}</textarea><button class="nx" data-l="gpost">${L('Post', 'Publicar')}</button>${err()}
<div id="gfeed">${feedHtml()}</div>
<div style="display:flex;gap:8px;margin-top:12px"><button class="xlink" data-l="groster">${g.showRoster ? L('Hide members', 'Ocultar miembros') : L('Members', 'Miembros')}</button><button class="xlink" data-l="gleave">${L('Leave group', 'Salir')}</button>${isMod() ? `<button class="xlink" data-l="garchive">${L('Archive group', 'Archivar')}</button>` : ''}</div>`;
    if (g.showRoster && g.roster) h += `<div class="lst">${g.roster.map(m => `<div class="li"><span class="m"><b>${esc(m.display)}</b><small>${m.role === 'mod' ? L('moderator', 'moderador') : L('member', 'miembro')}${m.muted ? ' • ' + L('muted', 'silenciado') : ''}</small></span>${isMod() && m.role === 'member' ? `<button class="xlink" data-l="gmute" data-v="${m.user_id}">${L('Mute 24h', 'Silenciar 24h')}</button><button class="xlink" data-l="grm" data-v="${m.user_id}">${L('Remove', 'Quitar')}</button>` : ''}</div>`).join('')}</div>`;
    return h + '</div>';
  }
  let feedTimer = setInterval(() => {
    if (S.tab !== 'group' || document.hidden || !Lr.grp.id) return;
    sync().rpc('group_feed', { gid: Lr.grp.id }).then(r => { Lr.grp.feed = r || []; const e = document.getElementById('gfeed'); if (e) e.innerHTML = feedHtml(); }).catch(() => { });
  }, 20000);

  /* ================= LECTURE NOTES ================= */
  function notesView() {
    const n = Lr.nt, subs = (C[S.c].s || []);
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 4px">${L('Lecture notes to study pack', 'Apuntes a paquete de estudio')}</h2>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (!n.res) {
      return h + `<p class="note" style="margin:0 0 8px">${L('Upload a PDF, lecture slides or a Word file, take a photo of your notes, or paste them. Ace makes a summary, flashcards and practice questions from them.', 'Sube un PDF, diapositivas o un Word, haz una foto o pega tus apuntes. Ace crea resumen, tarjetas y preguntas.')}</p>
<div class="nup"><label class="bt nup-b">📄 ${L('Upload PDF, slides or Word', 'Subir PDF, diapositivas o Word')}<input type="file" id="nfile" accept=".pdf,.pptx,.docx,.txt,.md,application/pdf" hidden></label><label class="bt nup-b">📷 ${L('Photo of my notes', 'Foto de mis apuntes')}<input type="file" id="nphoto" accept="image/*" hidden></label></div>
${n.reading ? `<p class="note">⏳ ${L('Reading your file…', 'Leyendo tu archivo…')}</p>` : ''}${n.file ? `<p class="note">✅ ${esc(L('Read', 'Leído'))} ${esc(n.file.name)}${n.file.pages ? ' • ' + n.file.pages + ' ' + L(n.file.name.toLowerCase().endsWith('.pptx') ? 'slides' : 'pages', n.file.name.toLowerCase().endsWith('.pptx') ? 'diapositivas' : 'páginas') : ''}${n.file.cut ? ' • ' + L('Ace uses the first 16,000 characters', 'Ace usa los primeros 16.000 caracteres') : ''}. ${L('You can edit the text below.', 'Puedes editar el texto.')}</p>` : ''}
${n.img ? `<div class="ch-att" style="width:100%;margin:8px 0"><img src="${n.img.thumb}" alt=""><span>${L('Photo of your notes added.', 'Foto añadida.')}</span><button data-l="nunimg" aria-label="${L('Remove photo', 'Quitar foto')}">✕</button></div>` : ''}
<label class="xl">${L('Subject or course', 'Asignatura o curso')}<input class="xin" list="nsubs" data-l-in="nsubject" maxlength="80" value="${esc(n.subject)}"></label><datalist id="nsubs">${subs.map(s => `<option value="${esc(s)}">`).join('')}</datalist>
<label class="xl">${L('Your notes', 'Tus apuntes')} <span id="ncount" style="float:right;font-weight:400">${n.text.length}/16000</span><textarea class="xin" rows="9" maxlength="16000" data-l-in="ntext">${esc(n.text)}</textarea></label>
<button class="nx" data-l="ngo" ${n.busy ? 'disabled' : ''}>${n.busy ? L('Ace is working…', 'Ace está trabajando…') : L('Make my study pack', 'Crear paquete')}</button>${n.err ? `<p class="note" style="color:var(--red)">${esc(n.err)}</p>` : ''}
<p class="note">${L('Ace only uses what you paste, and can make mistakes. Check it against your lecturer’s material.', 'Ace solo usa lo que pegas y puede equivocarse. Comprueba con tu material.')}</p></div>`;
    }
    const r = n.res;
    return h + `<div class="card"><b>${esc(r.title)}</b><p style="margin:6px 0 0;font-size:14px;line-height:1.5">${esc(r.summary)}</p></div>${r.check ? `<p class="note">⚠ ${esc(r.check)}</p>` : ''}
<div class="sh">${L('Key points', 'Ideas clave')}</div><ul class="xul">${r.key_points.map(k => `<li>${esc(k)}</li>`).join('')}</ul>
<div class="sh">${L('Flashcards (tap to flip)', 'Tarjetas (toca para girar)')}</div>${r.flashcards.map((f, i) => `<button class="li card" style="display:block;width:100%;text-align:left;margin:6px 0" data-l="nflip" data-v="${i}">${n.flip[i] ? esc(f.back) : '<b>' + esc(f.front) + '</b>'}</button>`).join('')}
${r.questions.length ? `<div class="sh">${L('Practice', 'Práctica')}</div>${r.questions.map((q, qi) => { const a = n.ans[qi]; return `<div class="card" style="margin-bottom:10px"><b>${qi + 1}. ${esc(q.q)}</b>${q.options.map((o, oi) => `<button class="li xopt ${a != null && oi === q.answer ? 'ok' : a === oi ? 'bad' : ''}" data-l="nans" data-v="${qi}:${oi}" ${a != null ? 'disabled' : ''}>${'ABCD'[oi]}. ${esc(o)}</button>`).join('')}${a != null ? `<p class="note">${a === q.answer ? '✅ ' : '❌ '}${esc(q.why)}</p>` : ''}</div>`; }).join('')}` : ''}
<button class="nx" data-l="nrev" ${n.saved ? 'disabled' : ''}>${n.saved ? L('Added to revision', 'Añadido al repaso') : L('Add to my revision schedule', 'Añadir a mi repaso')}</button>
<button class="nx" style="background:var(--tint);color:var(--text);margin-top:8px" data-l="nnew">${L('New notes', 'Nuevos apuntes')}</button>${n.err ? `<p class="note" style="color:var(--red)">${esc(n.err)}</p>` : ''}</div>`;
  }

  document.addEventListener('change', e => {
    const id = e.target.id; if ((id !== 'nfile' && id !== 'nphoto') || !e.target.files || !e.target.files[0] || !window.AceFiles) return;
    const f = e.target.files[0], n = Lr.nt; e.target.value = ''; n.err = ''; n.reading = true; render();
    (id === 'nfile' ? AceFiles.text(f).then(r => { n.file = { name: r.name, pages: r.pages, cut: r.text.length > 16000 }; n.text = r.text.slice(0, 16000); if (!n.subject) n.subject = r.name.replace(/\.[^.]+$/, '').replace(/[_-]+/g, ' ').slice(0, 80); })
      : AceFiles.image(f).then(r => { n.img = r; }))
      .catch(er => { n.err = (er && er.msg) || L('Ace could not open that file.', 'No se pudo abrir el archivo.'); })
      .then(() => { n.reading = false; render(); });
  });

  /* ================= PLANS ================= */
  const money = (minor, cur) => { try { return new Intl.NumberFormat(TX('en-GB', 'es-ES'), { style: 'currency', currency: cur, currencyDisplay: 'narrowSymbol', minimumFractionDigits: minor % 100 ? 2 : 0, maximumFractionDigits: minor % 100 ? 2 : 0 }).format(minor / 100); } catch (e) { return (minor / 100).toFixed(2) + ' ' + cur; } };
  const per = p => ({ month: L('per month', 'al mes'), term: L('per term', 'por trimestre'), year: L('per year', 'al año') }[p] || p);
  function plansView() {
    const p = Lr.pl;
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 4px">${L('Plans', 'Planes')}</h2>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (!p.list) return h + (Lr.err ? err() : '<p class="note">…</p>') + '</div>';
    const T = window.AceTier, st = T && T.status();
    h += `<div class="card"><b>${st ? esc(st) : p.access ? '✅ ' + L('You have access', 'Tienes acceso') : L('Free plan', 'Plan gratis')}</b>${T && T.usage() ? `<div style="margin-top:8px">${T.usage()}</div>` : ''}</div>`;
    if (!p.access) h += `<div class="sh">${L('Free', 'Gratis')}</div><p class="note" style="margin:0 0 6px">${L('All notes, lessons, quizzes, flashcards and the question bank. Daily challenge, streaks, league and study tools. 5 Ace messages a day, 1 photo question a day, 1 essay marking and 2 study packs a week, and the first mock exam in each subject.', 'Todos los apuntes, lecciones, tests, tarjetas y el banco de preguntas. Reto diario, rachas, liga y herramientas. 5 mensajes de Ace al día, 1 pregunta con foto al día, 1 corrección y 2 packs de estudio a la semana, y el primer simulacro de cada asignatura.')}</p>
<div class="sh">${L('With a plan', 'Con un plan')}</div><p class="note" style="margin:0 0 6px">${L('Up to 60 Ace messages a day, 20 photo questions and 15 essay markings a day, unlimited mock exams with a topic-by-topic breakdown, and study packs whenever you need them.', 'Hasta 60 mensajes de Ace al día, 20 preguntas con foto y 15 correcciones al día, simulacros ilimitados con desglose por temas y packs de estudio cuando quieras.')}</p>`;
    const mo = p.list.find(x => x.period === 'month' && x.seats === 1), months = { month: 1, term: 3, year: 12 };
    const label = x => x.seats > 1 ? L('Group plan', 'Plan de grupo') : ({ month: L('Monthly', 'Mensual'), term: L('Termly (3 months)', 'Trimestral (3 meses)'), year: L('Yearly', 'Anual') }[x.period] || x.name);
    const save = x => { if (!mo || x.seats > 1 || x.period === 'month') return ''; const pc = Math.round((1 - x.amount_minor / (months[x.period] * mo.amount_minor)) * 100); return pc > 0 ? ` <span class="xtag">${esc(TXF('Save {n}%', 'Ahorra {n}%', { n: pc }))}</span>` : ''; };
    h += p.list.length ? p.list.map(x => `<div class="card" style="margin:10px 0"><b>${esc(label(x))}</b>${save(x)}${x.seats > 1 ? ` <span class="xtag">${L('Up to', 'Hasta')} ${x.seats} ${L('people', 'personas')}</span>` : ''}<div style="font-size:22px;font-weight:800;margin:6px 0">${esc(money(x.amount_minor, x.currency_code))} <small style="font-weight:400">${per(x.period)}</small></div>
<button class="nx" data-l="buy" data-v="${esc(x.code)}" ${p.busy ? 'disabled' : ''}>${p.busy === x.code ? '…' : L('Choose this plan', 'Elegir este plan')}</button>${x.seats > 1 ? `<p class="note">${L('After paying, invite people from Share my plan.', 'Tras pagar, invita desde Compartir plan.')}</p>` : ''}</div>`).join('') : `<p class="note">${L('No plans are on sale in your country yet.', 'Aún no hay planes en tu país.')}</p>`;
    h += `<div class="sh">${L('Have a code?', '¿Tienes un código?')}</div><div class="card"><input class="xin" data-l-in="promo" maxlength="32" placeholder="CODE" value="${esc(p.promo)}"><button class="nx" data-l="redeem">${L('Apply code', 'Aplicar código')}</button></div>
<p class="note">${L('Payments are processed by Flutterwave. Ace never sees your card details.', 'Los pagos los procesa Flutterwave. Ace no ve tu tarjeta.')}</p>${err()}</div>`;
    return h;
  }
  const loadScript = src => new Promise((ok, no) => { if (document.querySelector(`script[src="${src}"]`)) return ok(); const s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = () => no({ msg: L('Could not load the payment window.', 'No se pudo cargar el pago.') }); document.head.appendChild(s); });

  /* ================= PUSH ================= */
  const b64 = s => { const p = '='.repeat((4 - s.length % 4) % 4), r = atob((s + p).replace(/-/g, '+').replace(/_/g, '/')); return Uint8Array.from([...r].map(c => c.charCodeAt(0))); };
  X.h.push = async function () {
    try {
      if (!signedIn()) return toast(L('Sign in first.', 'Inicia sesión primero.'));
      const key = (window.ACE_CONFIG || {}).vapidPublicKey;
      if (!key) return toast(L('Reminders are not set up yet.', 'Los recordatorios aún no están activados.'));
      if (!('serviceWorker' in navigator) || !('PushManager' in window)) return toast(L('This browser cannot show reminders.', 'Este navegador no admite recordatorios.'));
      if ((await Notification.requestPermission()) !== 'granted') return toast(L('Reminders stay off.', 'Recordatorios desactivados.'));
      const reg = await navigator.serviceWorker.ready, sub = await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: b64(key) }), j = sub.toJSON();
      const q = await sync().table('push_subscriptions'), r = await q.upsert({ endpoint: j.endpoint, user_id: sync().uid(), p256dh: j.keys.p256dh, auth: j.keys.auth });
      if (r && r.error) throw { msg: r.error.message };
      toast(L('Reminders are on.', 'Recordatorios activados.'));
    } catch (e) { toast(msg(e)); }
  };

  /* ================= registry ================= */
  Object.assign(V, { learn: learnView, course: courseView, lesson: lessonView, cquiz: quizView, unis: unisView, groups: groupsView, group: groupView, notes: notesView, plans: plansView });
  const pub = f => { f.pub = true; return f; };
  Object.assign(X.loaders, {
    learn: pub(() => getJSON('courses/index.json').then(i => { Lr.idx = i; }).then(() => signedIn() ? Promise.all([sync().table('course_progress').then(q => q.select('course,lessons_done')), sync().table('certificates').then(q => q.select('course,code,score,issued_at')), sync().rpc('my_passed_uncertified').catch(() => [])]).then(([p, c, u]) => { Lr.prog = {}; (p.data || []).forEach(r => Lr.prog[r.course] = r.lessons_done); Lr.certs = c.data || []; Lr.unc = u || []; }) : null).catch(e => { Lr.err = msg(e); })),
    course: pub(() => getJSON('courses/' + Lr.slug + '.json').then(c => { Lr.course = c; return X.loaders.learn(); }).catch(e => { Lr.err = msg(e); })),
    unis: pub(() => getJSON('universities/' + uniCC() + '.json').then(d => { Lr.uni.data[uniCC()] = d; }).catch(e => { Lr.err = msg(e); })),
    groups: () => Promise.all([sync().rpc('my_groups'), sync().rpc('discover_groups')]).then(([m, f]) => { Lr.grp.mine = m || []; Lr.grp.find = f || []; Lr.grp.form.scope = (P.lvl || 'secondary') === 'university' ? 'institution' : Lr.grp.form.scope === 'institution' ? 'class' : Lr.grp.form.scope; }),
    group: () => sync().rpc('group_feed', { gid: Lr.grp.id }).then(r => { Lr.grp.feed = r || []; }),
    plans: () => Promise.all([sync().table('plans').then(q => q.select('code,name,currency_code,amount_minor,period,seats,country_code,audience').eq('active', true).order('amount_minor')), sync().rpc('has_access')]).then(([p, a]) => { Lr.pl.list = (p.data || []).filter(x => x.audience !== 'school').filter(x => CAMPUS ? /^campus_/.test(x.code) : !/^campus_/.test(x.code) && (!x.country_code || x.country_code === S.c)); try { AceTier.load(true); } catch (e) { } Lr.pl.access = !!a; })
  });
  X.loaders.lesson = null; delete X.loaders.lesson; X.loaders.cquiz = X.loaders.course;

  /* ================= events ================= */
  const rerun = p => p.then(() => render()).catch(e => { Lr.err = msg(e); render(); });
  document.addEventListener('input', e => {
    const t = e.target, k = t && t.dataset && t.dataset.lIn; if (!k) return;
    if (k === 'cq') { Lr.cq.q = t.value; const r = document.getElementById('cres'); if (r) r.innerHTML = courseList(); }
    else if (k === 'uq') { Lr.uni.q = t.value; const r = document.getElementById('ures'); if (r) r.innerHTML = uniResults(); }
    else if (k === 'ntext') { Lr.nt.text = t.value; const c = document.getElementById('ncount'); if (c) c.textContent = t.value.length + '/16000'; }
    else if (k === 'nsubject') Lr.nt.subject = t.value;
    else if (k === 'gname') Lr.grp.form.name = t.value; else if (k === 'gdesc') Lr.grp.form.desc = t.value; else if (k === 'gscope') Lr.grp.form.scope = t.value;
    else if (k === 'gdraft') Lr.grp.draft = t.value; else if (k === 'promo') Lr.pl.promo = t.value.toUpperCase();
  });
  document.addEventListener('change', e => { const t = e.target; if (t && t.dataset && t.dataset.lIn === 'gscope') Lr.grp.form.scope = t.value; });
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-l]'); if (!b) return; const a = b.dataset.l, v = b.dataset.v;
    // courses
    if (a === 'ccat') { Lr.cq.cat = v; render(); }
    else if (a === 'open') { Lr.slug = v; Lr.course = null; Lr.quiz = { ans: {}, res: null, busy: false }; go('course'); }
    else if (a === 'lesson') { Lr.lesson = v; S.tab = 'lesson'; render(); window.scrollTo(0, 0); }
    else if (a === 'done') {
      const c = Lr.course, i = c.lessons.findIndex(l => l.id === v), next = c.lessons[i + 1];
      const after = () => { if (next) { Lr.lesson = next.id; S.tab = 'lesson'; } else S.tab = 'course'; render(); window.scrollTo(0, 0); };
      if (signedIn()) sync().rpc('mark_lesson', { p_course: c.slug, p_lesson: v }).then(() => { const d = Lr.prog[c.slug] = Lr.prog[c.slug] || []; if (!d.includes(v)) d.push(v); after(); }).catch(er => { Lr.err = msg(er); render(); });
      else { P.cl = P.cl || {}; const d = P.cl[c.slug] = P.cl[c.slug] || []; if (!d.includes(v)) d.push(v); svP(); after(); }
    }
    else if (a === 'quiz') { Lr.quiz = { ans: {}, res: null, busy: false }; S.tab = 'cquiz'; render(); window.scrollTo(0, 0); }
    else if (a === 'ans') { const [q, o] = v.split(':'); Lr.quiz.ans[q] = +o; render(); }
    else if (a === 'submit') { Lr.quiz.busy = true; render(); sync().rpc('submit_course_quiz', { p_course: Lr.course.slug, p_answers: Lr.quiz.ans }).then(r => { Lr.quiz.busy = false; Lr.quiz.res = r; if (r.passed && r.code && !Lr.certs.find(x => x.course === Lr.course.slug)) Lr.certs.push({ course: Lr.course.slug, code: r.code, score: r.score, issued_at: new Date().toISOString() }); render(); window.scrollTo(0, 0); }).catch(er => { Lr.quiz.busy = false; Lr.err = msg(er); render(); }); }
    else if (a === 'quizretry') { Lr.quiz = { ans: {}, res: null, busy: false }; S.tab = 'course'; render(); }
    // universities
    else if (a === 'ucc') { Lr.uni.cc = v; Lr.uni.open = null; go('unis'); }
    else if (a === 'uopen') { Lr.uni.open = Lr.uni.open === v ? null : v; render(); }
    else if (a === 'goal') {
      const [ui, fi, ci] = v.split(':').map(Number), d = Lr.uni.data[uniCC()], u = d.universities[ui], c = u.faculties[fi].courses[ci];
      X.goal.course = c.name; X.goal.uni = u.name; P.goal2 = X.goal; svP(); toast(L('Saved as your goal. See it on your road map.', 'Guardado como objetivo. Mira tu hoja de ruta.'));
      if (signedIn()) sync().table('student_goals').then(q => q.upsert({ user_id: sync().uid(), target_course: c.name, target_university: u.name, target_country: uniCC(), updated_at: new Date().toISOString() })).catch(() => { });
    }
    // groups
    else if (a === 'gopen') { const g = Lr.grp.mine.find(x => x.id === v); Lr.grp.id = v; Lr.grp.name = g ? g.name : ''; Lr.grp.role = g ? g.role : ''; Lr.grp.feed = null; Lr.grp.roster = null; Lr.grp.showRoster = false; go('group'); }
    else if (a === 'gjoin') rerun(sync().rpc('join_group', { gid: v }).then(() => { X.loaded = ''; return X.loaders.groups(); }));
    else if (a === 'gcreate') { const f = Lr.grp.form; rerun(sync().rpc('create_group', { p_name: f.name, p_desc: f.desc || null, p_scope: f.scope }).then(() => { f.name = ''; f.desc = ''; return X.loaders.groups(); })); }
    else if (a === 'gpost') { const d = Lr.grp.draft; Lr.err = ''; rerun(sync().rpc('post_to_group', { gid: Lr.grp.id, p_body: d }).then(() => { Lr.grp.draft = ''; return X.loaders.group(); })); }
    else if (a === 'grefresh') rerun(X.loaders.group());
    else if (a === 'report') { rerun(sync().rpc('report_post', { pid: +v, p_reason: 'Reported by a member' }).then(() => toast(L('Thanks. A moderator will look at it.', 'Gracias. Un moderador lo revisará.')))); }
    else if (a === 'mod') { const [id, act] = v.split(':'); rerun(sync().rpc('moderate_post', { pid: +id, p_action: act }).then(() => X.loaders.group())); }
    else if (a === 'groster') { Lr.grp.showRoster = !Lr.grp.showRoster; if (Lr.grp.showRoster) rerun(sync().rpc('group_roster', { gid: Lr.grp.id }).then(r => { Lr.grp.roster = r || []; })); else render(); }
    else if (a === 'gmute') rerun(sync().rpc('mute_member', { gid: Lr.grp.id, uid: v, p_hours: 24 }).then(() => sync().rpc('group_roster', { gid: Lr.grp.id })).then(r => { Lr.grp.roster = r || []; }));
    else if (a === 'grm') rerun(sync().rpc('remove_member', { gid: Lr.grp.id, uid: v }).then(() => sync().rpc('group_roster', { gid: Lr.grp.id })).then(r => { Lr.grp.roster = r || []; }));
    else if (a === 'gleave') rerun(sync().rpc('leave_group', { gid: Lr.grp.id }).then(() => { S.tab = 'groups'; X.loaded = ''; }));
    else if (a === 'garchive') rerun(sync().rpc('archive_group', { gid: Lr.grp.id }).then(() => { S.tab = 'groups'; X.loaded = ''; }));
    // notes
    else if (a === 'ngo') {
      const n = Lr.nt; if (!n.subject.trim()) { n.err = L('Add a subject or course name.', 'Añade una asignatura.'); return render(); } if (!n.img && n.text.trim().length < 80) { n.err = L('Upload a file, add a photo or paste more of your notes.', 'Sube un archivo, añade una foto o pega más apuntes.'); return render(); }
      n.busy = true; n.err = ''; render();
      sync().fn('notes-pack', { subject: n.subject, notes: n.text, image: n.img ? { media_type: n.img.media_type, data: n.img.data } : undefined, exam: AceX.h.ex(), country: cname(), lang: UIL() }).then(r => { n.res = r; n.busy = false; n.ans = {}; n.flip = {}; n.saved = false; render(); window.scrollTo(0, 0); }).catch(er => { n.busy = false; n.err = msg(er); render(); });
    }
    else if (a === 'nflip') { Lr.nt.flip[v] = !Lr.nt.flip[v]; render(); }
    else if (a === 'nans') { const [q, o] = v.split(':').map(Number); Lr.nt.ans[q] = o; render(); }
    else if (a === 'nnew') { Object.assign(Lr.nt, { text: '', res: null, ans: {}, flip: {}, saved: false, err: '', file: null, img: null }); render(); }
    else if (a === 'nunimg') { Lr.nt.img = null; render(); }
    else if (a === 'nrev') { const n = Lr.nt; sync().rpc('add_revision', { p_exam: AceX.h.ex(), p_subject: n.subject, p_topic: n.res.title || n.subject, p_note: n.res.note_id || null }).then(() => { n.saved = true; toast(L('Added. First review is tomorrow.', 'Añadido. Primer repaso mañana.')); render(); }).catch(er => { n.err = msg(er); render(); }); }
    else if (a === 'claim') rerun(sync().rpc('claim_certificate', { p_course: v }).then(r => { Lr.unc = (Lr.unc || []).filter(x => x.course !== v); if (!Lr.certs.find(x => x.course === v)) Lr.certs.push({ course: v, code: r.code, score: r.score, issued_at: new Date().toISOString() }); if (Lr.quiz && Lr.quiz.res && Lr.course && Lr.course.slug === v) Lr.quiz.res.code = r.code; toast(L('Certificate issued.', 'Certificado emitido.')); }));
    // plans
    else if (a === 'buy') {
      const p = Lr.pl; p.busy = v; Lr.err = ''; render();
      sync().fn('checkout-start', { plan_code: v }).then(o => loadScript('https://checkout.flutterwave.com/v3.js').then(() => {
        p.busy = ''; render();
        window.FlutterwaveCheckout({ public_key: o.public_key, tx_ref: o.tx_ref, amount: o.amount, currency: o.currency, customer: o.customer, customizations: { title: o.title, description: o.description },
          callback: () => { toast(L('Payment received. Your access updates in a moment.', 'Pago recibido. Tu acceso se actualiza en breve.')); setTimeout(() => { X.loaded = ''; render(); }, 5000); }, onclose: () => { } });
      })).catch(er => { p.busy = ''; Lr.err = msg(er); render(); });
    }
    else if (a === 'redeem') rerun(sync().rpc('redeem_promo', { p_code: Lr.pl.promo }).then(r => { if (r && r.ok === false) throw { msg: TRL(r.error || 'This code is not valid.') }; toast(L('Code applied.', 'Código aplicado.')); Lr.pl.promo = ''; X.loaded = ''; }));
  });

  /* ================= small styles ================= */
  const st = document.createElement('style');
  st.textContent = `.xcode{background:var(--tint);border:1px solid var(--border);border-radius:10px;padding:12px;overflow-x:auto;font-size:13px;line-height:1.5}.xcode code{font-family:ui-monospace,Menlo,Consolas,monospace;white-space:pre}.xul li{margin:4px 0}.pad a.li{color:var(--text)}.pad a{color:var(--ink)}`;
  document.head.appendChild(st);
})();
