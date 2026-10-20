/* Ace Teach: teacher tools, school / workspace admin, and the Ace founder console. */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, bar, pct, nm, ini, ago, daysAgo, csv, saveCsv, must, fn, toast, syllabus, examKey, subjectsOf, modulesOf, curEx, cls, isAdmin, isTutor, isPlat, cc, empty, CA, CN, today } = H;
const sb = () => T.sb, me = () => T.me;
const opt = (v, l, sel) => `<option value="${esc(v)}" ${sel ? 'selected' : ''}>${esc(l == null ? v : l)}</option>`;

/* ================= teacher tools ================= */
const AIT = { lessonplan: ['📋', 'Lesson plan', 'A ready-to-teach plan with timings, a worked example, checks and homework.'], worksheet: ['📄', 'Worksheet', '10 questions from easy to exam style, with an answer key.'], quizjson: ['⚡', 'Quiz questions', 'Multiple-choice questions you can run as a live quiz.'], comment: ['💬', 'Report comment', 'A short, specific report-card comment from your notes.'] };
V.ai = async () => {
  const [d, ek] = St.cls ? await curEx() : [await syllabus(), null], ek2 = ek || examKey(d), subjects = subjectsOf(d, ek2), tool = St.ait || 'lessonplan', s0 = St.ais || (cls() && cls().subject) || subjects[0], mods = modulesOf(d, ek2, subjects.includes(s0) ? s0 : subjects[0]);
  let h = `<div class="card"><h2>✨ AI planner</h2><p class="sub">Uses the ${esc(ek2 || '')} syllabus for ${esc(CN[cc()] || cc())}. Always read and adjust before using it with students.</p><div class="tabs">${Object.keys(AIT).map(k => `<button class="g ${k === tool ? 'on' : ''}" data-a="aitool" data-v="${k}">${AIT[k][0]} ${AIT[k][1]}</button>`).join('')}</div><p class="sub">${AIT[tool][2]}</p>
<form data-f="ai"><input type="hidden" name="mode" value="${tool}"><input type="hidden" name="exam" value="${esc(ek2 || '')}">`;
  if (tool !== 'comment') h += `<div class="row"><label>Subject<select name="subject" data-a="aisub">${subjects.map(x => opt(x, x, x === s0)).join('')}</select></label><label style="flex:2 1 260px">Topic<select name="topic">${mods.map((m, i) => `<optgroup label="${esc((i + 1) + '. ' + m.title)}">${(m.topics || []).map(t => opt(t)).join('')}</optgroup>`).join('')}</select></label>${tool === 'quizjson' ? `<label style="flex:0 1 110px">Questions<select name="n">${[5, 10, 15].map(n => opt(n, n, n === 10)).join('')}</select></label>` : ''}</div>`;
  h += `<label>${tool === 'comment' ? 'About the student (strengths, weaknesses, effort, marks)' : 'Anything else? (class level, time available, focus)'}<textarea name="extra" maxlength="1500" ${tool === 'comment' ? 'required' : ''} placeholder="${tool === 'lessonplan' ? 'e.g. 40-minute lesson, mixed ability, no projector' : tool === 'comment' ? 'e.g. Works hard, strong in algebra, careless with units, 64% in term test' : ''}"></textarea></label><button class="b">Generate</button></form></div>`;
  if (St.aiout) h += `<div class="card"><h2>${AIT[St.aiout.mode][1]}<span class="sp row" style="gap:6px"><button class="g" data-a="aicopy">Copy</button><button class="g" data-a="aiprint">Print</button>${St.aiout.qs ? `<button class="b" data-a="ailive">Run as live quiz</button>` : ''}</span></h2>${St.aiout.qs ? St.aiout.qs.map((q, i) => `<div class="qa"><b class="q">${i + 1}. ${esc(q.q)}</b><ol type="A" style="margin:6px 0">${q.o.map((o, j) => `<li style="${j === q.a ? 'font-weight:700;color:var(--green)' : ''}">${esc(o)}</li>`).join('')}</ol><small class="muted">${esc(q.e || '')}</small></div>`).join('') : `<div class="out md" id="aiout">${H.md(St.aiout.text)}</div>`}</div>`;
  return h;
};
A.aitool = el => { St.ait = el.dataset.v; St.aiout = null; T.go(); };
A.aisub = el => { St.ais = el.value; T.go(); };
F.ai = async (d, f) => {
  const b = f.querySelector('button.b'); b.textContent = 'Ace is writing…';
  const ask = d.mode === 'comment' ? `Write a report comment for this student: ${d.extra}` : d.mode === 'quizjson' ? `Write ${d.n || 10} multiple-choice questions on "${d.topic}" (${d.subject}). ${d.extra || ''}` : `${AIT[d.mode][1]} on "${d.topic}" (${d.subject}). ${d.extra || ''}`;
  const r = await fn('ai-tutor', { messages: [{ role: 'user', content: ask }], context: { mode: d.mode, country: (CN[cc()] || cc()).replace(/^\S+\s/, ''), exam: d.exam, subject: d.subject || (cls() && cls().subject) || '', topic: d.topic || '' } });
  let qs = null; if (d.mode === 'quizjson') { try { const j = JSON.parse((r.reply.match(/\[[\s\S]*\]/) || [''])[0]); qs = j.filter(q => q && q.q && Array.isArray(q.o) && q.o.length === 4 && q.a >= 0 && q.a < 4); } catch (e) { qs = null; } }
  St.aiout = { mode: d.mode, text: r.reply, qs: qs && qs.length ? qs : null }; T.go();
};
A.aicopy = () => { const t = St.aiout.qs ? St.aiout.qs.map((q, i) => `${i + 1}. ${q.q}\n${q.o.map((o, j) => 'ABCD'[j] + ') ' + o).join('\n')}\nAnswer: ${'ABCD'[q.a]}`).join('\n\n') : St.aiout.text; try { navigator.clipboard.writeText(t).then(() => toast('Copied.')); } catch (e) { toast('Select the text to copy.', true); } };
A.aiprint = () => window.print();
A.ailive = async () => { if (!St.cls) return toast('Choose a class first.', true); await T.makeLive(St.aiout.qs.map(q => ({ q: q.q, o: q.o })), St.aiout.qs.map(q => q.a)); St.view = 'live'; T.go(); };

/* ---------- report cards ---------- */
V.reportcards = async () => {
  const s = await T.insights(), c = cls(), as = must(await sb().from('assessments').select('*').eq('class_id', St.cls)) || [];
  const mk = as.length ? must(await sb().from('marks').select('assessment_id,student_id,mark').in('assessment_id', as.map(a => a.id))) || [] : [];
  const qa = s.length ? must(await sb().from('quiz_attempts').select('user_id,subject,total,correct').in('user_id', s.map(x => x.student_id)).neq('kind', 'daily').gte('created_at', new Date(Date.now() - 120 * 864e5).toISOString())) || [] : [];
  const term = St.term || '', who = St.rcs || 'all', list = who === 'all' ? s : s.filter(x => x.student_id === who), ca = (CA[cc()] || ['Continuous assessment'])[0];
  let h = `<div class="card noprint"><h2>Report cards</h2><p class="sub">Built from your gradebook (weighted ${esc(ca)}), Ace practice in the last 120 days and the register. Add a comment for each student, then print.</p><div class="row"><label>Student<select data-a="rcs">${opt('all', 'Whole class', who === 'all')}${s.map(x => opt(x.student_id, x.first_name + ' ' + x.surname, x.student_id === who)).join('')}</select></label><label>Term or period<input data-a="rcterm" value="${esc(term)}" placeholder="Term 1, 2026/27"></label><button class="b" data-a="aiprint">Print</button></div></div>`;
  h += list.map(x => {
    const subj = [...new Set(as.map(a => a.subject).concat(qa.filter(q => q.user_id === x.student_id).map(q => q.subject)))].sort();
    const rows = subj.map(sj => { const ws = as.filter(a => a.subject === sj && +a.weight > 0), got = ws.filter(a => mk.find(m => m.assessment_id === a.id && m.student_id === x.student_id)); const tw = got.reduce((n, a) => n + +a.weight, 0); const cav = tw ? got.reduce((n, a) => n + (+mk.find(m => m.assessment_id === a.id && m.student_id === x.student_id).mark) / a.max_mark * a.weight, 0) * 100 / tw : null; const q = qa.filter(z => z.user_id === x.student_id && z.subject === sj), qt = q.reduce((n, z) => n + z.total, 0), qc = q.reduce((n, z) => n + z.correct, 0); return `<tr><td>${esc(sj)}</td><td class="n">${pct(cav)}</td><td class="n">${qt ? pct(qc * 100 / qt) : '–'}</td><td class="n">${qt}</td></tr>`; });
    return `<div class="rc"><div class="row" style="align-items:center"><div style="flex:1"><h2>${nm(x)}</h2><div>${esc(c.name)}${term ? ' • ' + esc(term) : ''}</div></div><div style="text-align:right"><b>${esc(T.school ? T.school.name : '')}</b><br><small>${esc(CN[cc()] || '')}</small></div></div>
<table style="margin:14px 0"><thead><tr><th>Subject</th><th class="n">${esc(ca)}</th><th class="n">Practice accuracy</th><th class="n">Questions answered</th></tr></thead><tbody>${rows.join('') || '<tr><td colspan="4">No marks or practice yet.</td></tr>'}</tbody></table>
<p><b>Attendance:</b> ${pct(x.attendance_pct)} • <b>Study streak:</b> ${x.streak} days • <b>Topics mastered:</b> ${x.topics_mastered}</p>
<p style="margin-bottom:4px"><b>Teacher's comment</b> <button class="g noprint" data-a="aicomment" data-id="${x.student_id}">✨ Draft with AI</button></p><div contenteditable="true" data-rcc="${x.student_id}" style="min-height:60px;border:1px dashed #C9CCE8;border-radius:8px;padding:8px">${esc((St.rcc || {})[x.student_id] || '')}</div>
<p style="margin-top:18px">Signed: ____________________ &nbsp; Date: ______________</p></div>`;
  }).join('');
  return h;
};
A.rcs = el => { St.rcs = el.value; T.go(); };
A.rcterm = el => { St.term = el.value; };
document.addEventListener('input', e => { const t = e.target; if (t.dataset && t.dataset.rcc) { St.rcc = St.rcc || {}; St.rcc[t.dataset.rcc] = t.textContent; } });
A.aicomment = async el => {
  const s = (await T.insights()).find(x => x.student_id === el.dataset.id), box = document.querySelector(`[data-rcc="${el.dataset.id}"]`); box.textContent = 'Ace is writing…';
  const r = await fn('ai-tutor', { messages: [{ role: 'user', content: `First name: ${s.first_name}. Practice average last 30 days: ${pct(s.avg_pct_30d)}. Quizzes: ${s.attempts_30d}. Streak: ${s.streak} days. Topics mastered: ${s.topics_mastered}. Attendance: ${pct(s.attendance_pct)}.` }], context: { mode: 'comment', country: cc(), exam: cls().exam || '', subject: cls().subject || '' } });
  box.textContent = r.reply; St.rcc = St.rcc || {}; St.rcc[s.student_id] = r.reply;
};

/* ---------- term planner ---------- */
V.planner = async () => {
  const m = St.month || today().slice(0, 7), y = +m.slice(0, 4), mo = +m.slice(5, 7) - 1, first = new Date(Date.UTC(y, mo, 1)), days = new Date(Date.UTC(y, mo + 1, 0)).getUTCDate();
  const to = `${m}-${String(days).padStart(2, '0')}`;
  const [ts, as, pc] = await Promise.all([sb().from('tasks').select('title,due_on,kind').eq('class_id', St.cls).gte('due_on', m + '-01').lte('due_on', to), sb().from('assessments').select('title,held_on').eq('class_id', St.cls).gte('held_on', m + '-01').lte('held_on', to), sb().from('class_pacing').select('topic,planned_week,taught_on').eq('class_id', St.cls).gte('planned_week', m + '-01').lte('planned_week', to)]);
  const ev = {}; const add = (d, h) => (ev[d] = ev[d] || []).push(h);
  (ts.data || []).forEach(t => add(t.due_on, `<span class="ev t" title="${esc(t.title)}">📝 ${esc(t.title)}</span>`));
  (as.data || []).forEach(a => add(a.held_on, `<span class="ev a" title="${esc(a.title)}">📒 ${esc(a.title)}</span>`));
  (pc.data || []).forEach(p => add(p.planned_week, `<span class="ev" title="${esc(p.topic)}">🗺️ ${esc(p.topic)}</span>`));
  const lead = (first.getUTCDay() + 6) % 7, cells = [];
  for (let i = 0; i < lead; i++) cells.push('<div class="d o"></div>');
  for (let d = 1; d <= days; d++) { const k = `${m}-${String(d).padStart(2, '0')}`; cells.push(`<div class="d ${k === today() ? 't' : ''} ${ev[k] ? 'has' : ''}"><b>${d}</b>${(ev[k] || []).join('')}</div>`); }
  const mn = first.toLocaleDateString('en-GB', { month: 'long', year: 'numeric', timeZone: 'UTC' });
  return `<div class="card"><h2>${esc(mn)}<span class="sp row" style="gap:6px"><button class="g" data-a="mstep" data-v="-1">‹</button><input type="month" data-a="setmonth" value="${m}" style="width:160px;margin:0"><button class="g" data-a="mstep" data-v="1">›</button></span></h2><p class="sub">Work due (📝), assessments (📒) and planned topics (🗺️) for ${esc(cls().name)}. Plan topics on the Pacing page.</p>
<div class="cal">${['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map(x => `<div class="h">${x}</div>`).join('')}${cells.join('')}</div></div>`;
};
A.mstep = el => { const m = St.month || today().slice(0, 7), d = new Date(Date.UTC(+m.slice(0, 4), +m.slice(5, 7) - 1 + +el.dataset.v, 1)); St.month = d.toISOString().slice(0, 7); T.go(); };

/* ---------- rubrics ---------- */
V.rubrics = async () => {
  const r = must(await sb().from('rubrics').select('*').order('created_at', { ascending: false })) || [];
  return `<div class="card"><h2>New rubric</h2><p class="sub">One criterion per line: <code>Name | maximum marks</code>. Attach a rubric when you assign written work; marking adds the criteria up for you.</p><form data-f="rubric"><label>Title<input name="title" required maxlength="120" placeholder="Essay (40 marks)"></label><label>Criteria<textarea name="crit" required placeholder="Content and ideas | 20\nOrganisation | 10\nLanguage and grammar | 10"></textarea></label><button class="b">Save rubric</button></form></div>
<div class="card"><h2>Your rubrics</h2>${r.length ? r.map(x => `<div class="qa"><b class="q">${esc(x.title)}</b> <span class="pill">${(x.criteria || []).reduce((n, c) => n + (+c.max || 0), 0)} marks</span><ul>${(x.criteria || []).map(c => `<li>${esc(c.name)} <small class="muted">/${c.max}</small></li>`).join('')}</ul><button class="g bad" data-a="delrub" data-id="${x.id}">Delete</button></div>`).join('') : empty('No rubrics yet')}</div>`;
};
F.rubric = async d => { const criteria = d.crit.split('\n').map(l => l.trim()).filter(Boolean).map((l, i) => { const p = l.split('|').map(x => x.trim()); if (p.length < 2 || !p[0] || !(+p[1] > 0)) throw new Error('Line ' + (i + 1) + ' should be: Name | maximum marks'); return { name: p[0].slice(0, 80), max: +p[1] }; }); must(await sb().from('rubrics').insert({ title: d.title, criteria })); toast('Rubric saved.'); T.go(); };
A.delrub = async el => { must(await sb().from('rubrics').delete().eq('id', el.dataset.id)); T.go(); };

/* ---------- parents ---------- */
V.parents = async () => {
  const s = await T.insights(), ids = s.map(x => x.student_id), g = ids.length ? must(await sb().from('guardians').select('*').in('student_id', ids)) || [] : [], byS = {}; s.forEach(x => byS[x.student_id] = x);
  return `<div class="grid g2"><div class="card"><h2>Family view</h2><p class="sub">Students can share a read-only view of their progress with a parent from Today → Family view in the app. It shows streaks, practice by subject, attendance and courses, and the student can stop sharing at any time.</p><a class="g" href="../family/" target="_blank" rel="noopener" style="text-decoration:none;display:inline-block">Open the family page ↗</a></div>
<div class="card"><h2>Add a guardian for the weekly email</h2><form data-f="guardian"><label>Student<select name="student_id" required>${s.map(x => opt(x.student_id, x.first_name + ' ' + x.surname)).join('')}</select></label><div class="row"><label>Guardian name<input name="name" maxlength="80"></label><label>E-mail<input name="email" type="email" required></label></div><label class="chk"><input type="checkbox" name="consent"> The guardian agreed to receive the weekly digest</label><button class="b">Add</button></form></div></div>
<div class="card"><h2>Guardians<span class="sp"><button class="b" data-a="digest">Send this week's digest</button></span></h2>${table(['Student', 'Guardian', 'E-mail', 'Digest'], g.map(x => `<tr><td>${byS[x.student_id] ? nm(byS[x.student_id]) : ''}</td><td>${esc(x.name || '')}</td><td>${esc(x.email)}</td><td>${x.digest_opt_in && x.consent_at ? '<span class="pill ok">on</span>' : '<span class="pill">off</span>'}</td></tr>`))}<p class="muted">Emails go only to guardians who agreed. Sending needs the email service to be set up.</p></div>`;
};
F.guardian = async d => { must(await sb().from('guardians').insert({ student_id: d.student_id, name: d.name || null, email: d.email.toLowerCase(), digest_opt_in: !!d.consent, consent_at: d.consent ? new Date().toISOString() : null, created_by: me().id })); toast('Added.'); T.go(); };
A.digest = async () => { const r = await fn('send-parent-digest', { class_id: St.cls }); toast(`Digest sent to ${r.sent} guardian(s).`); };

/* ================= school / workspace admin ================= */
V.classes = async () => {
  const sum = must(await sb().rpc('school_summary')) || [], d = await syllabus(), exams = d ? Object.keys(d.exams) : [];
  return `<div class="card"><h2>New class</h2><p class="sub">${isTutor() ? 'One class per group you teach, for example "Saturday WASSCE Maths". Each class gets its own join code.' : 'Each class gets a join code. Students can also be added by you in People.'}</p><form data-f="newclass"><div class="row"><label style="flex:2 1 220px">Name<input name="name" required maxlength="40" placeholder="${isTutor() ? 'Saturday WASSCE Maths' : 'SS3A'}"></label><label>Level<input name="grade" required maxlength="20" placeholder="SS3"></label><label>Exam<select name="exam">${exams.map(x => opt(x)).join('')}</select></label><label>Subject (optional)<input name="subject" maxlength="80" placeholder="Mathematics"></label></div><button class="b">Create class</button></form></div>
<div class="card"><h2>Classes (${sum.length})</h2>${table(['Class', 'Level', 'Students', 'Active 7d', 'Avg', 'Teachers', 'Join code', ''], sum.map(x => `<tr><td><b>${esc(x.name)}</b></td><td>${esc(x.grade)}</td><td class="n">${x.students}</td><td class="n">${x.active_7d}</td><td class="n">${pct(x.avg_pct)}</td><td>${esc(x.teachers || (isTutor() ? 'You' : '–'))}</td><td><b style="font:800 15px var(--fd);letter-spacing:.12em">${esc(x.join_code || '')}</b></td><td style="white-space:nowrap"><button class="g" data-a="newcode" data-id="${x.class_id}">New code</button> <button class="g bad" data-a="archcls" data-id="${x.class_id}">Archive</button></td></tr>`), 'No classes yet.')}</div>`;
};
F.newclass = async d => { must(await sb().from('classes').insert({ school_id: me().school_id, name: d.name, grade: d.grade, exam: d.exam || null, subject: d.subject || null })); await H.loadClasses(); toast('Class created. Share its join code.'); T.go(); };
A.newcode = async el => { must(await sb().from('classes').update({ join_code: null }).eq('id', el.dataset.id)); await H.loadClasses(); toast('New join code made. The old code no longer works.'); T.go(); };
A.archcls = async el => { if (!el.dataset.sure) { el.dataset.sure = 1; el.textContent = 'Tap again'; return; } must(await sb().from('classes').update({ archived: true }).eq('id', el.dataset.id)); await H.loadClasses(); toast('Archived.'); T.go(); };

V.people = async () => {
  const p = must(await sb().from('profiles').select('id,first_name,surname,class_id,username,student_number,role,last_seen_at,contact_email').eq('school_id', me().school_id).order('surname').limit(1000)) || [];
  const ts = must(await sb().from('teacher_subjects').select('teacher_id,class_id,subject')) || [], C = {}; St.classes.forEach(c => C[c.id] = c);
  const staff = p.filter(x => x.role !== 'student'), studs = p.filter(x => x.role === 'student');
  const co = St.classes.map(c => opt(c.id, c.name + ' (' + c.grade + ')')).join('');
  return `<div class="grid g2"><div class="card"><h2>Create student accounts</h2><p class="sub">For students without their own email or phone. Each gets a username and a temporary password to print.${isTutor() ? ' Students who already use Ace should join with your class code instead.' : ''}</p><form data-f="bulk"><label>Class<select name="class_id">${co}</select></label><label>One student per line: First name Surname<textarea name="list" required placeholder="Ada Okafor\nTunde Bello"></textarea></label><button class="b">Create accounts</button></form><div id="creds"></div></div>
<div class="card"><h2>${isTutor() ? 'Add a teacher to your centre' : 'Invite a teacher'}</h2><form data-f="invite"><div class="row"><label>First name<input name="first_name" required></label><label>Surname<input name="surname" required></label></div><label>E-mail<input name="email" type="email" required></label><div class="row"><label>Role<select name="role"><option value="teacher">Class teacher</option><option value="subject_teacher">Subject teacher</option></select></label><label>Class<select name="class_id"><option value="">Assign later</option>${co}</select></label><label>Subject<input name="subject" maxlength="60"></label></div><button class="b">Send invitation</button></form></div></div>
<div class="card"><h2>Teachers (${staff.length})</h2>${table(['Name', 'Role', 'Classes', 'Last seen', ''], staff.map(x => `<tr><td><b>${nm(x)}</b><br><small class="muted">${esc(x.contact_email || '')}</small></td><td>${esc(x.role.replace('_', ' '))}</td><td>${ts.filter(t => t.teacher_id === x.id).map(t => `<span class="pill">${esc((C[t.class_id] || {}).name || '')} ${esc(t.subject)}</span>`).join(' ')}</td><td>${ago(x.last_seen_at)}</td><td>${x.role !== 'school_admin' ? `<button class="g" data-a="assign" data-id="${x.id}">Assign class</button>` : ''}</td></tr>`))}</div>
<div class="card"><h2>Students (${studs.length})<span class="sp row" style="gap:6px"><input data-filter="#plist tbody tr" placeholder="Search" style="width:180px;margin:0"><button class="g" data-a="promote">Move a whole class</button></span></h2><div id="plist">${table(['Name', 'Class', 'Username', 'Student no.', 'Last seen', 'Move to'], studs.map(x => `<tr><td>${nm(x)}</td><td>${esc((C[x.class_id] || {}).name || '–')}</td><td>${esc(x.username || '')}</td><td>${esc(x.student_number || '')}</td><td>${ago(x.last_seen_at)}</td><td><select data-a="movestu" data-id="${x.id}" style="margin:0;padding:5px 8px"><option value="">…</option>${co}</select></td></tr>`))}</div></div>`;
};
F.bulk = async d => { const list = d.list.split('\n').map(l => l.trim()).filter(Boolean).map(l => { const p = l.split(/\s+/); return { first_name: p[0], surname: p.slice(1).join(' ') || '-' }; });
  const r = await fn('bulk-create-students', { class_id: d.class_id, students: list }), rows = r.results || r.created || [];
  document.getElementById('creds').innerHTML = `<h3 style="margin-top:12px">Login details: shown once, print or copy now</h3>${table(['Name', 'Username', 'Temporary password'], rows.map(x => `<tr><td>${esc(x.first_name + ' ' + x.surname)}</td><td>${esc(x.username || '')}</td><td><b>${esc(x.temp_password || x.error || '')}</b></td></tr>`))}<button class="g noprint" data-a="aiprint" style="margin-top:8px">Print</button>`; T.fresh(); toast('Accounts created.'); };
F.invite = async d => { const body = { first_name: d.first_name, surname: d.surname, email: d.email, role: d.role }; if (d.class_id && d.subject) body.assignments = [{ class_id: d.class_id, subject: d.subject }]; await fn('invite-staff', body); toast('Invitation sent.'); };
A.movestu = async el => { if (!el.value) return; must(await sb().from('profiles').update({ class_id: el.value }).eq('id', el.dataset.id)); toast('Moved.'); T.fresh(); };
A.assign = async el => {
  const ts = must(await sb().from('teacher_subjects').select('class_id,subject').eq('teacher_id', el.dataset.id)) || [], C = {}; St.classes.forEach(c => C[c.id] = c);
  const d = document.createElement('div'); d.className = 'drawer';
  d.innerHTML = `<div><h2>Classes for this teacher</h2><div class="lst" style="margin:12px 0">${ts.map(t => `<div class="it"><div class="m"><b>${esc((C[t.class_id] || {}).name || '')}</b><small>${esc(t.subject)}</small></div><button class="g bad" data-a="unassign" data-t="${el.dataset.id}" data-c="${t.class_id}" data-s="${esc(t.subject)}">Remove</button></div>`).join('') || '<p class="muted">No classes yet.</p>'}</div>
<form data-f="assign" data-t="${el.dataset.id}"><label>Class<select name="class_id">${St.classes.map(c => opt(c.id, c.name + ' (' + c.grade + ')')).join('')}</select></label><label>Subject<input name="subject" required maxlength="60"></label><button class="b">Add</button> <button class="g" type="button" data-a="closedr">Close</button></form></div>`;
  document.body.appendChild(d);
};
F.assign = async (d, f) => { must(await sb().from('teacher_subjects').insert({ teacher_id: f.dataset.t, class_id: d.class_id, subject: d.subject })); A.closedr(); toast('Class added.'); T.go(); };
A.unassign = async el => { must(await sb().from('teacher_subjects').delete().eq('teacher_id', el.dataset.t).eq('class_id', el.dataset.c).eq('subject', el.dataset.s)); A.closedr(); toast('Removed.'); T.go(); };
A.promote = async () => {
  const co = St.classes.map(c => opt(c.id, c.name + ' (' + c.grade + ')')).join('');
  const d = document.createElement('div'); d.className = 'drawer'; d.innerHTML = `<div><h2>Move a whole class</h2><p class="sub">Use this at the start of a school year: every student in the first class moves to the second.</p><form data-f="promote"><label>From<select name="from">${co}</select></label><label>To<select name="to">${co}</select></label><button class="b">Move students</button> <button class="g" type="button" data-a="closedr">Cancel</button></form></div>`; document.body.appendChild(d);
};
F.promote = async d => { if (d.from === d.to) throw new Error('Choose two different classes.'); const r = await sb().from('profiles').update({ class_id: d.to }).eq('class_id', d.from).eq('role', 'student').select('id'); if (r.error) throw new Error(r.error.message); A.closedr && A.closedr(); toast((r.data || []).length + ' students moved.'); T.fresh(); T.go(); };

/* ---------- timetable (schools) ---------- */
V.timetable = async () => {
  const c0 = St.ttc || St.cls || (St.classes[0] || {}).id; if (!c0) return empty('Create a class first');
  const sl = must(await sb().from('timetable_slots').select('*').eq('class_id', c0).order('starts')) || [], DN = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'];
  return `<div class="card"><h2>Timetable<span class="sp"><select data-a="ttc" style="margin:0;width:auto">${St.classes.map(c => opt(c.id, c.name, c.id === c0)).join('')}</select></span></h2><form data-f="slot" class="row"><label>Day<select name="weekday">${DN.map((x, i) => opt(i + 1, x)).join('')}</select></label><label>Starts<input name="starts" type="time" required value="08:00"></label><label>Ends<input name="ends" type="time" required value="08:40"></label><label>Subject<input name="subject" required maxlength="80"></label><label>Room<input name="room" maxlength="40"></label><button class="b">Add</button></form></div>
<div class="card"><div class="tt">${DN.map((x, i) => `<div class="col"><b style="font:800 14px var(--fd)">${x}</b>${sl.filter(s => s.weekday === i + 1).map(s => `<div class="slot"><b>${esc(s.subject)}</b>${esc(String(s.starts).slice(0, 5))}–${esc(String(s.ends).slice(0, 5))}${s.room ? ' • ' + esc(s.room) : ''} <button class="g bad" data-a="delslot" data-id="${s.id}" style="padding:1px 6px;font-size:11px">✕</button></div>`).join('') || '<small class="muted">Free</small>'}</div>`).join('')}</div></div>`;
};
A.ttc = el => { St.ttc = el.value; T.go(); };
F.slot = async d => { const c0 = St.ttc || St.cls; must(await sb().from('timetable_slots').insert({ school_id: me().school_id, class_id: c0, weekday: +d.weekday, starts: d.starts, ends: d.ends, subject: d.subject, room: d.room || null })); T.go(); };
A.delslot = async el => { must(await sb().from('timetable_slots').delete().eq('id', el.dataset.id)); T.go(); };

/* ---------- fees (schools) ---------- */
V.fees = async () => {
  const term = St.fterm || '', f = must(await sb().from('fees').select('*').eq('school_id', me().school_id).order('term')) || [], p = must(await sb().from('profiles').select('id,first_name,surname,class_id').eq('school_id', me().school_id).eq('role', 'student')) || [], P = {}; p.forEach(x => P[x.id] = x);
  const terms = [...new Set(f.map(x => x.term))], show = f.filter(x => !term || x.term === term), cur = (show[0] || {}).currency_code || '';
  const tot = show.reduce((n, x) => n + +x.amount, 0), paid = show.reduce((n, x) => n + +x.paid, 0);
  return `<div class="note">Ace keeps a record of fees only. Payments are made to the school directly, not through Ace.</div><div class="card"><h2>Bill a class</h2><form data-f="bill" class="row"><label>Class<select name="class_id">${St.classes.map(c => opt(c.id, c.name)).join('')}</select></label><label>Term<input name="term" required maxlength="40" placeholder="Term 1 2026/27"></label><label>Amount<input name="amount" type="number" min="0" step="0.01" required></label><label style="flex:0 1 100px">Currency<input name="currency_code" required maxlength="3" placeholder="NGN" style="text-transform:uppercase"></label><label>Due<input name="due_on" type="date"></label><button class="b">Add for every student</button></form></div>
<div class="kpis" style="grid-template-columns:repeat(3,1fr)"><div class="kpi"><b>${tot.toLocaleString()}</b><span>Billed ${esc(cur)}</span></div><div class="kpi g"><b>${paid.toLocaleString()}</b><span>Paid</span></div><div class="kpi r"><b>${(tot - paid).toLocaleString()}</b><span>Outstanding</span></div></div>
<div class="card"><h2>Fees<span class="sp row" style="gap:6px"><select data-a="fterm" style="margin:0;width:auto">${opt('', 'All terms', !term)}${terms.map(t => opt(t, t, t === term)).join('')}</select><button class="g" data-a="csvfees">Export CSV</button></span></h2>${table(['Student', 'Term', 'Amount', 'Paid', 'Balance', 'Record payment'], show.map(x => `<tr><td>${P[x.student_id] ? nm(P[x.student_id]) : ''}</td><td>${esc(x.term)}</td><td class="n">${(+x.amount).toLocaleString()}</td><td class="n">${(+x.paid).toLocaleString()}</td><td class="n"><span class="pill ${+x.paid >= +x.amount ? 'ok' : 'bad'}">${(+x.amount - +x.paid).toLocaleString()}</span></td><td><input type="number" min="0" step="0.01" placeholder="Total paid" data-a="feepaid" data-id="${x.id}" style="margin:0;width:130px"></td></tr>`))}</div>`;
};
A.fterm = el => { St.fterm = el.value; T.go(); };
F.bill = async d => { const p = must(await sb().from('profiles').select('id').eq('school_id', me().school_id).eq('class_id', d.class_id).eq('role', 'student')) || []; if (!p.length) throw new Error('That class has no students yet.');
  must(await sb().from('fees').upsert(p.map(x => ({ school_id: me().school_id, student_id: x.id, term: d.term, amount: +d.amount, currency_code: d.currency_code.toUpperCase(), due_on: d.due_on || null })), { onConflict: 'student_id,term' })); toast(p.length + ' students billed.'); T.go(); };
A.feepaid = async el => { if (el.value === '') return; must(await sb().from('fees').update({ paid: +el.value }).eq('id', el.dataset.id)); toast('Payment recorded.'); T.go(); };
A.csvfees = async () => { const f = must(await sb().from('fees').select('term,amount,paid,currency_code,profiles(first_name,surname)').eq('school_id', me().school_id)) || []; saveCsv('fees.csv', csv([['Student', 'Term', 'Amount', 'Paid', 'Balance', 'Currency']].concat(f.map(x => [x.profiles ? x.profiles.first_name + ' ' + x.profiles.surname : '', x.term, x.amount, x.paid, x.amount - x.paid, x.currency_code])))); };

/* ---------- school / workspace report ---------- */
V.schoolrep = async () => {
  const sum = must(await sb().rpc('school_summary')) || [], tot = sum.reduce((n, x) => n + +x.students, 0), act = sum.reduce((n, x) => n + +x.active_7d, 0), av = sum.filter(x => x.avg_pct != null);
  return `<div class="kpis" style="grid-template-columns:repeat(4,1fr)"><div class="kpi p"><b>${sum.length}</b><span>Classes</span></div><div class="kpi"><b>${tot}</b><span>Students</span></div><div class="kpi g"><b>${act}</b><span>Active this week</span></div><div class="kpi a"><b>${av.length ? pct(av.reduce((n, x) => n + +x.avg_pct, 0) / av.length) : '–'}</b><span>Average score</span></div></div>
<div class="card"><h2>By class<span class="sp"><button class="g" data-a="csvschool">Export CSV</button></span></h2>${table(['Class', 'Level', 'Students', 'Active 7d', 'Engagement', 'Avg', ''], sum.map(x => `<tr><td><b>${esc(x.name)}</b></td><td>${esc(x.grade)}</td><td class="n">${x.students}</td><td class="n">${x.active_7d}</td><td style="width:120px">${bar(x.students ? x.active_7d * 100 / x.students : 0)}</td><td class="n">${pct(x.avg_pct)}</td><td><button class="g" data-a="opencls" data-id="${x.class_id}">Open</button></td></tr>`))}</div>`;
};
A.csvschool = async () => { const s = must(await sb().rpc('school_summary')) || []; saveCsv('school-report.csv', csv([['Class', 'Level', 'Students', 'Active 7d', 'Average %', 'Teachers']].concat(s.map(x => [x.name, x.grade, x.students, x.active_7d, x.avg_pct, x.teachers])))); };
A.opencls = el => { St.cls = el.dataset.id; St.view = 'overview'; T.go(); };

/* ---------- settings ---------- */
const money = (minor, cur) => { try { return new Intl.NumberFormat('en-GB', { style: 'currency', currency: cur, currencyDisplay: 'narrowSymbol', minimumFractionDigits: minor % 100 ? 2 : 0, maximumFractionDigits: minor % 100 ? 2 : 0 }).format(minor / 100); } catch (e) { return (minor / 100) + ' ' + cur; } };
const fdate = d => new Date(d).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
// Settings > Plan: the free plan (1 class, 40 students), the 30-day school trial, and the per-student licence
function planCard(p) {
  if (!p) return '';
  const left = d => Math.max(0, Math.ceil((Date.parse(d) - Date.now()) / 864e5));
  const paid = p.licensed && p.status === 'active', trial = p.licensed && p.status === 'trialing';
  let h = `<div class="card"><h2>Plan</h2>`;
  if (paid) h += `<p><b>Licence active until ${esc(fdate(p.paid_until))}</b></p><p class="muted">${p.students} of ${p.seats || '–'} students in use. Every student in your ${isTutor() ? 'classes' : 'school'} gets Ace with up to 60 AI messages a day, unlimited mock exams and verified certificates.</p>`;
  else if (trial) h += `<p><b>Free trial: ${left(p.trial_ends_at)} days left</b></p><p class="muted">Everything is switched on during the trial. After it ends, the free plan allows ${p.free_classes} active class of up to ${p.free_class_size} students, and students go back to their own free limits.</p>`;
  else h += `<p><b>Free plan</b></p><p class="muted">${p.free_classes} active class of up to ${p.free_class_size} students. You have ${p.classes} active class${p.classes === 1 ? '' : 'es'} and ${p.students} students. Students use their own free AI limits (5 messages a day).</p>`;
  if (!isAdmin()) return h + '</div>';
  if (!p.plan) return h + `<p class="muted">Licences are not on sale in your country yet. Contact us for a quote.</p></div>`;
  const per = money(p.plan.per_student, p.plan.currency), n0 = Math.max(p.min_students, p.students || 0);
  if (paid) h += `<form data-f="buylic" data-add="1" class="row"><label>Add students<input name="students" type="number" min="1" max="20000" value="10" required></label><button class="b">Add and pay</button></form><p class="muted">${per} per student per year, charged only for the months left on your licence.</p>`;
  else h += `<form data-f="buylic" class="row"><label>Students<input name="students" type="number" min="${p.min_students}" max="20000" value="${n0}" required data-per="${p.plan.per_student}" data-cur="${esc(p.plan.currency)}"></label><button class="b">Buy a 1-year licence</button></form><p class="muted">${per} per student per year, at least ${p.min_students} students. Payments are processed by Flutterwave.</p>`;
  return h + '</div>';
}
F.buylic = async (d, f) => {
  const o = await fn('checkout-start', { plan_code: St.plan.plan.code, students: +d.students, add: !!f.dataset.add });
  await new Promise((ok, no) => { if (window.FlutterwaveCheckout) return ok(); const s = document.createElement('script'); s.src = 'https://checkout.flutterwave.com/v3.js'; s.onload = ok; s.onerror = () => no(new Error('Could not load the payment window.')); document.head.appendChild(s); });
  window.FlutterwaveCheckout({ public_key: o.public_key, tx_ref: o.tx_ref, amount: o.amount, currency: o.currency, customer: o.customer, customizations: { title: o.title, description: o.description },
    callback: () => { toast('Payment received. Your licence updates in a moment.'); setTimeout(() => T.go(), 6000); }, onclose: () => { } });
};
V.settings = async () => {
  const s = T.school;
  St.plan = s ? (await sb().rpc('my_school_plan')).data : null;
  return `${planCard(St.plan)}${isAdmin() && s ? `<div class="card"><h2>${isTutor() ? 'Workspace' : 'School'}</h2><form data-f="wsname" class="row"><label style="flex:2 1 260px">Name<input name="name" required maxlength="120" value="${esc(s.name)}"></label><button class="b">Save</button></form><p class="muted">Code ${esc(s.school_code)} • ${esc(CN[s.country_code] || s.country_code)}</p></div>
<div class="card"><h2>AI help for your students</h2><form data-f="aiset" class="row"><label>Mode<select name="ai_mode">${[['full', 'Full'], ['limited', 'Limited'], ['off', 'Off']].map(k => opt(k[0], k[1], s.ai_mode === k[0])).join('')}</select></label><label>Questions per period<input name="ai_cap" type="number" min="0" max="500" value="${s.ai_cap == null ? '' : s.ai_cap}"></label><label>Period<select name="ai_period">${['daily', 'weekly'].map(k => opt(k, k, s.ai_period === k)).join('')}</select></label><button class="b">Save</button></form></div>` : ''}
<div class="card"><h2>My profile</h2><form data-f="myname" class="row"><label>First name<input name="first_name" required maxlength="60" value="${esc(me().first_name)}"></label><label>Surname<input name="surname" required maxlength="60" value="${esc(me().surname)}"></label><button class="b">Save</button></form></div>
<div class="card"><h2>Change password</h2><form data-f="pw" class="row"><label>New password (8+ characters)<input name="pw" type="password" minlength="8" required autocomplete="new-password"></label><button class="b">Change</button></form></div>
<div class="card"><h2>Appearance</h2><button class="g" data-a="theme">Switch light / dark</button></div>`;
};
F.wsname = async d => { must(await sb().from('schools').update({ name: d.name }).eq('id', me().school_id)); T.school.name = d.name; toast('Saved.'); location.reload(); };
F.aiset = async d => { must(await sb().from('schools').update({ ai_mode: d.ai_mode, ai_cap: d.ai_cap === '' ? null : +d.ai_cap, ai_period: d.ai_period }).eq('id', me().school_id)); toast('Saved.'); };
F.myname = async d => { must(await sb().from('profiles').update({ first_name: d.first_name, surname: d.surname }).eq('id', me().id)); toast('Saved.'); };
F.pw = async d => { const r = await sb().auth.updateUser({ password: d.pw }); if (r.error) throw new Error(r.error.message); toast('Password changed.'); };
A.theme = () => { const r = document.documentElement, dark = r.dataset.theme === 'dark' || (!r.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches); r.dataset.theme = dark ? 'light' : 'dark'; try { localStorage.setItem('ace-teach-theme', r.dataset.theme); } catch (e) { } };
try { const t = localStorage.getItem('ace-teach-theme'); if (t) document.documentElement.dataset.theme = t; } catch (e) { }

/* ================= founder console (platform_admin) ================= */
V.dash = async () => {
  const o = must(await sb().rpc('platform_overview')) || {}, sg = o.signups || [], mx = Math.max(1, ...sg.map(x => x.n));
  return `<div class="kpis"><div class="kpi p"><b>${o.students || 0}</b><span>Students (${o.independent || 0} independent)</span></div><div class="kpi"><b>${o.tutors || 0}</b><span>Tutors and centres</span></div><div class="kpi"><b>${o.schools || 0}</b><span>Schools</span></div><div class="kpi g"><b>${o.active_7d || 0}</b><span>Active this week</span></div><div class="kpi a"><b>${(o.answers_7d || 0).toLocaleString()}</b><span>Answers this week</span></div></div>
<div class="grid g2"><div class="card"><h2>Sign-ups, last 30 days</h2><div class="spark">${sg.map(x => `<i class="${x.n ? '' : 'z'}" style="height:${Math.round(x.n * 100 / mx)}%" title="${esc(x.day)}: ${x.n}"></i>`).join('')}</div><div class="axis"><span>${esc((sg[0] || {}).day || '')}</span><span>today</span></div><p class="muted" style="margin-top:10px">${o.active_today || 0} active today • ${o.teachers || 0} school teachers • ${o.classes || 0} classes • ${o.ai_7d || 0} AI questions this week</p></div>
<div class="card"><h2>By country</h2>${table(['Country', 'Students', 'Staff'], (o.by_country || []).map(x => `<tr><td>${esc(CN[x.cc] || x.cc)}</td><td class="n">${x.students}</td><td class="n">${x.teachers}</td></tr>`))}</div>
<div class="card"><h2>Revenue</h2>${(o.revenue || []).length ? table(['Currency', 'Payments', 'Total'], o.revenue.map(x => `<tr><td>${esc(x.currency)}</td><td class="n">${x.count}</td><td class="n">${(+x.total).toLocaleString()}</td></tr>`)) : '<p class="muted">No payments yet. Payments start once Flutterwave and Stripe are connected.</p>'}</div></div>`;
};
V.schools = async () => {
  const k = St.sk || 'all', s = must(await sb().from('schools').select('*').order('created_at', { ascending: false }).limit(500)) || [], countries = must(await sb().from('countries').select('code,name').order('name')) || [];
  const show = s.filter(x => k === 'all' || x.kind === k);
  return `<div class="card"><h2>Onboard a school</h2><form data-f="school"><div class="row"><label style="flex:2 1 220px">School name<input name="name" required maxlength="120"></label><label>Country<select name="country_code">${countries.map(c => opt(c.code, c.name)).join('')}</select></label><label>Region<input name="region" maxlength="80"></label></div><div class="row"><label>Admin first name<input name="admin_first" required></label><label>Admin surname<input name="admin_surname" required></label><label>Admin e-mail<input name="admin_email" type="email" required></label></div><button class="b">Create school and invite admin</button></form></div>
<div class="card"><h2>${show.length} workspaces<span class="sp tabs" style="margin:0">${[['all', 'All'], ['school', 'Schools'], ['tutor', 'Tutors']].map(t => `<button class="g ${k === t[0] ? 'on' : ''}" data-a="sk" data-v="${t[0]}">${t[1]}</button>`).join('')}</span></h2>${table(['Name', 'Type', 'Country', 'Code', 'Created', 'Active', ''], show.map(x => `<tr><td><b>${esc(x.name)}</b></td><td><span class="pill">${x.kind === 'tutor' ? 'Tutor' : 'School'}</span></td><td>${esc(x.country_code)}</td><td>${esc(x.school_code)}</td><td>${esc(String(x.created_at).slice(0, 10))}</td><td>${x.active ? '<span class="pill ok">yes</span>' : '<span class="pill bad">no</span>'}</td><td><button class="g" data-a="schoolact" data-id="${x.id}" data-v="${x.active ? '' : '1'}">${x.active ? 'Deactivate' : 'Activate'}</button></td></tr>`))}</div>`;
};
A.sk = el => { St.sk = el.dataset.v; T.go(); };
F.school = async d => { await fn('create-school', d); toast('School created. The admin has been invited.'); T.go(); };
A.schoolact = async el => { must(await sb().from('schools').update({ active: !!el.dataset.v }).eq('id', el.dataset.id)); T.go(); };
V.users = async () => {
  const q = St.uq || '', r = St.ur || 'all';
  let qy = sb().from('profiles').select('id,first_name,surname,role,account_type,country_code,username,contact_email,created_at,last_seen_at,school_id').order('created_at', { ascending: false }).limit(200);
  if (r !== 'all') qy = r === 'tutor' ? qy.eq('account_type', 'tutor') : qy.eq('role', r);
  if (q) qy = qy.or(`first_name.ilike.%${q.replace(/[%,()]/g, '')}%,surname.ilike.%${q.replace(/[%,()]/g, '')}%,username.ilike.%${q.replace(/[%,()]/g, '')}%,contact_email.ilike.%${q.replace(/[%,()]/g, '')}%`);
  const p = must(await qy) || [];
  return `<div class="card"><h2>People<span class="sp row" style="gap:6px"><input data-a="uq" value="${esc(q)}" placeholder="Name, username or email" style="width:220px;margin:0"><select data-a="ur" style="margin:0;width:auto">${[['all', 'Everyone'], ['student', 'Students'], ['tutor', 'Tutors'], ['teacher', 'Teachers'], ['school_admin', 'Admins']].map(k => opt(k[0], k[1], r === k[0])).join('')}</select></span></h2>${table(['Name', 'Type', 'Country', 'Login', 'Joined', 'Last seen'], p.map(x => `<tr><td><b>${nm(x)}</b></td><td>${esc(x.account_type === 'tutor' ? 'tutor' : x.role.replace('_', ' '))}${x.role === 'student' && !x.school_id ? ' <span class="pill">independent</span>' : ''}</td><td>${esc(x.country_code)}</td><td>${esc(x.username || x.contact_email || '')}</td><td>${esc(String(x.created_at).slice(0, 10))}</td><td>${ago(x.last_seen_at)}</td></tr>`))}<p class="muted">Showing the newest 200 that match.</p></div>`;
};
A.uq = el => { St.uq = el.value.trim(); T.go(); };
A.ur = el => { St.ur = el.value; T.go(); };
V.money = async () => {
  const p = must(await sb().from('plans').select('*').order('country_code', { nullsFirst: true }).order('amount_minor')) || [], pr = must(await sb().from('promo_codes').select('*').order('code')) || [], pay = must(await sb().from('payments').select('created_at,provider,amount_minor,currency_code,status,plan_code').order('created_at', { ascending: false }).limit(50)) || [], countries = must(await sb().from('countries').select('code,name').order('name')) || [];
  return `<div class="card"><h2>Add or update a plan</h2><p class="sub">Use an existing code to change a plan. Prices in normal units, for example 2500 for ₦2,500.</p><form data-f="plan"><div class="row"><label>Code<input name="code" required pattern="[a-z0-9_-]{2,40}" placeholder="family-month"></label><label>Name<input name="name" required></label><label>Country<select name="country_code"><option value="">Any country</option>${countries.map(c => opt(c.code, c.name)).join('')}</select></label><label style="flex:0 1 90px">Currency<input name="currency_code" required maxlength="3" style="text-transform:uppercase"></label><label>Price<input name="price" type="number" min="0" step="0.01" required></label><label>Billing<select name="period"><option>month</option><option>term</option><option>year</option></select></label><label>People<select name="seats"><option>1</option><option>2</option><option>3</option><option selected>4</option></select></label><label>For<select name="audience"><option>student</option><option>school</option><option>tutor</option></select></label></div><button class="b">Save plan</button></form></div>
<div class="card"><h2>Plans</h2>${table(['Code', 'Name', 'Country', 'Price', 'People', 'For', 'On sale', ''], p.map(x => `<tr><td>${esc(x.code)}</td><td>${esc(x.name)}</td><td>${esc(x.country_code || 'any')}</td><td>${(x.amount_minor / 100).toFixed(2)} ${esc(x.currency_code)} / ${esc(x.period)}</td><td class="n">${x.seats}</td><td>${esc(x.audience)}</td><td>${x.active ? 'yes' : 'no'}</td><td><button class="g" data-a="planact" data-id="${esc(x.code)}" data-v="${x.active ? '' : '1'}">${x.active ? 'Take off sale' : 'Put on sale'}</button></td></tr>`))}</div>
<div class="card"><h2>Promo codes</h2><form data-f="promo" class="row"><label>Code<input name="code" required pattern="[A-Za-z0-9_-]{3,32}"></label><label>Type<select name="kind"><option value="trial_extension">Extend trial</option><option value="free_days">Free days</option></select></label><label>Days<input name="value" type="number" min="1" max="365" value="7" required></label><label>Max uses<input name="max_uses" type="number" min="1"></label><label>Expires<input name="expires_at" type="date"></label><button class="b">Add</button></form>${table(['Code', 'Type', 'Days', 'Used', 'Max', 'Active', ''], pr.map(x => `<tr><td>${esc(x.code)}</td><td>${esc(x.kind)}</td><td class="n">${x.value}</td><td class="n">${x.used_count}</td><td class="n">${x.max_uses || '–'}</td><td>${x.active ? 'yes' : 'no'}</td><td><button class="g" data-a="promoact" data-id="${esc(x.code)}" data-v="${x.active ? '' : '1'}">${x.active ? 'Disable' : 'Enable'}</button></td></tr>`))}</div>
<div class="card"><h2>Latest payments</h2>${table(['When', 'Provider', 'Plan', 'Amount', 'Status'], pay.map(x => `<tr><td>${esc(String(x.created_at).slice(0, 16).replace('T', ' '))}</td><td>${esc(x.provider)}</td><td>${esc(x.plan_code || '')}</td><td class="n">${(x.amount_minor / 100).toFixed(2)} ${esc(x.currency_code)}</td><td>${esc(x.status)}</td></tr>`), 'No payments yet.')}</div>`;
};
F.plan = async d => { must(await sb().from('plans').upsert({ code: d.code, name: d.name, country_code: d.country_code || null, currency_code: d.currency_code.toUpperCase(), amount_minor: Math.round(parseFloat(d.price) * 100), period: d.period, audience: d.audience, seats: +d.seats, active: true })); toast('Plan saved.'); T.go(); };
A.planact = async el => { must(await sb().from('plans').update({ active: !!el.dataset.v }).eq('code', el.dataset.id)); T.go(); };
F.promo = async d => { must(await sb().from('promo_codes').insert({ code: d.code, kind: d.kind, value: +d.value, max_uses: d.max_uses ? +d.max_uses : null, expires_at: d.expires_at ? d.expires_at + 'T23:59:59Z' : null })); toast('Code added.'); T.go(); };
A.promoact = async el => { must(await sb().from('promo_codes').update({ active: !!el.dataset.v }).eq('code', el.dataset.id)); T.go(); };
V.creators = async () => {
  const c = must(await sb().from('creator_profiles').select('user_id,handle,display_name,headline,country_code,status,fee_pct,created_at').order('created_at', { ascending: false }).limit(200)) || [];
  return `<div class="card"><h2>Creator applications</h2><p class="sub">People who want to sell lessons on the marketplace. Approve to let them publish.</p>${table(['Creator', 'Country', 'Status', 'Fee %', ''], c.map(x => `<tr><td><b>${esc(x.display_name)}</b> <small class="muted">@${esc(x.handle)}</small><br><small>${esc(x.headline || '')}</small></td><td>${esc(x.country_code || '')}</td><td><span class="pill ${x.status === 'approved' ? 'ok' : x.status === 'pending' ? 'w' : 'bad'}">${esc(x.status)}</span></td><td class="n">${x.fee_pct == null ? 'default' : x.fee_pct}</td><td style="white-space:nowrap">${x.status !== 'approved' ? `<button class="g" data-a="crev" data-id="${x.user_id}" data-v="approved">Approve</button> ` : ''}${x.status !== 'rejected' ? `<button class="g bad" data-a="crev" data-id="${x.user_id}" data-v="${x.status === 'approved' ? 'suspended' : 'rejected'}">${x.status === 'approved' ? 'Suspend' : 'Reject'}</button>` : ''}</td></tr>`), 'No applications yet.')}</div>`;
};
A.crev = async el => { must(await sb().rpc('review_creator', { p_user: el.dataset.id, p_decision: el.dataset.v })); toast('Updated.'); T.go(); };
V.config = async () => {
  const c = must(await sb().from('platform_config').select('*').eq('id', 'global').single());
  return `<div class="card"><h2>Broadcast banner</h2><p class="sub">Shown at the top of the student app for everyone. Leave empty to hide it.</p><form data-f="banner"><label>Banner text<input name="banner" maxlength="300" value="${esc(c.banner || '')}" placeholder="Mock exam week: try a full mock this Saturday!"></label><button class="b">Save banner</button></form></div>
<div class="card"><h2>Platform settings</h2><form data-f="config"><div class="row"><label>Default AI questions per day<input name="ai_default_cap" type="number" min="0" value="${c.ai_default_cap}"></label><label>Free trial days<input name="trial_days" type="number" min="0" max="60" value="${c.trial_days}"></label></div><label class="chk"><input type="checkbox" name="maintenance" ${c.maintenance ? 'checked' : ''}> Maintenance mode</label><button class="b">Save</button></form></div>`;
};
F.banner = async d => { must(await sb().from('platform_config').update({ banner: d.banner || null, updated_at: new Date().toISOString() }).eq('id', 'global')); toast('Banner saved.'); };
F.config = async d => { must(await sb().from('platform_config').update({ ai_default_cap: +d.ai_default_cap, trial_days: +d.trial_days, maintenance: !!d.maintenance, updated_at: new Date().toISOString() }).eq('id', 'global')); toast('Saved.'); };
V.reports = async () => {
  const r = must(await sb().from('content_reports').select('*').order('created_at', { ascending: false }).limit(80)) || [], e = must(await sb().from('app_errors').select('*').order('created_at', { ascending: false }).limit(40)) || [];
  return `<div class="card"><h2>Content reports</h2>${table(['When', 'Where', 'Report', 'Status'], r.map(x => `<tr><td>${esc(String(x.created_at).slice(0, 10))}</td><td>${esc([x.country_code, x.exam, x.subject, x.topic].filter(Boolean).join(' / '))}<br><span class="pill">${esc(x.item || '')}</span></td><td>${esc(x.note)}</td><td><select data-a="repst" data-id="${x.id}" style="margin:0">${['open', 'fixed', 'rejected'].map(k => opt(k, k, x.status === k)).join('')}</select></td></tr>`))}</div>
<div class="card"><h2>Recent app errors</h2>${table(['When', 'Page', 'Message'], e.map(x => `<tr><td>${esc(String(x.created_at).slice(0, 16).replace('T', ' '))}</td><td>${esc(x.page || '')}</td><td>${esc(x.message || '')}</td></tr>`))}</div>`;
};
A.repst = async el => { must(await sb().from('content_reports').update({ status: el.value }).eq('id', el.dataset.id)); toast('Updated.'); };
V.mod = async () => {
  const q = must(await sb().rpc('mod_queue')) || [];
  return `<div class="card"><h2>Study-group moderation</h2><p class="sub">Reported or hidden posts. Three separate reports hide a post automatically.</p>${table(['Group', 'Author', 'Post', 'Reports', ''], q.map(x => `<tr><td>${esc(x.group_name)}</td><td>${esc(x.author)}</td><td>${esc(x.body)}<br><span class="pill">${x.hidden ? 'hidden' : 'visible'}</span></td><td class="n">${x.reports}</td><td style="white-space:nowrap">${x.hidden ? `<button class="g" data-a="modp" data-id="${x.post_id}" data-v="restore">Restore</button>` : `<button class="g" data-a="modp" data-id="${x.post_id}" data-v="hide">Hide</button>`} <button class="g bad" data-a="modp" data-id="${x.post_id}" data-v="remove">Remove</button></td></tr>`), 'Nothing to review.')}</div>`;
};
A.modp = async el => { must(await sb().rpc('moderate_post', { pid: +el.dataset.id, p_action: el.dataset.v })); T.go(); };
})();
