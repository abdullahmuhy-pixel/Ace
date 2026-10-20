/* Ace Teach: classroom views for teachers and tutors. */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, bar, pct, nm, ini, ago, daysAgo, csv, saveCsv, must, fn, toast, syllabus, examKey, subjectsOf, modulesOf, curEx, cls, isAdmin, isTutor, empty, CA, today } = H;
const sb = () => T.sb, me = () => T.me;
const insights = async () => (St._ins && St._ins.k === St.cls) ? St._ins.v : (St._ins = { k: St.cls, v: must(await sb().rpc('class_insights', { p_class: St.cls })) || [] }).v;
const fresh = () => { St._ins = null; };
const opt = (v, l, sel) => `<option value="${esc(v)}" ${sel ? 'selected' : ''}>${esc(l == null ? v : l)}</option>`;

/* ---------- overview ---------- */
V.overview = async () => {
  const c = cls(), s = await insights(), act = must(await sb().rpc('class_activity', { p_class: St.cls })) || [], subj = must(await sb().rpc('class_subject_perf', { p_class: St.cls })) || [];
  const active7 = s.filter(x => daysAgo(x.last_day) != null && daysAgo(x.last_day) <= 7).length, activeT = s.filter(x => daysAgo(x.last_day) === 0).length;
  const scores = s.filter(x => x.avg_pct_30d != null), avg = scores.length ? scores.reduce((n, x) => n + +x.avg_pct_30d, 0) / scores.length : null;
  const idle = s.filter(x => daysAgo(x.last_day) == null || daysAgo(x.last_day) >= 3), risk = s.filter(x => x.avg_pct_30d != null && +x.avg_pct_30d < 50);
  const tasks = must(await sb().from('tasks').select('id,title,due_on,kind').eq('class_id', St.cls).order('created_at', { ascending: false }).limit(4)) || [];
  const subs = tasks.length ? must(await sb().from('task_submissions').select('task_id,student_id,submitted_at,auto_score,mark').in('task_id', tasks.map(t => t.id))) || [] : [];
  const mx = Math.max(1, ...act.map(a => +a.attempts));
  if (!s.length) return `<div class="card"><h2>Get your students in</h2><p class="sub">Students join from their own Ace account with this code. They keep their progress, and you see their work while they are in your class.</p>
<div class="hero2"><span class="big">${esc(c.join_code)}</span><button class="b" data-a="copycode">Copy invitation</button>${isAdmin() ? `<button class="g" data-go="people">Create accounts for students without phones</button>` : ''}</div>
<ol class="sub" style="margin-top:14px;line-height:1.8"><li>Students open the Ace app (or sign up free).</li><li>Tools → My classes → enter <b>${esc(c.join_code)}</b>.</li><li>They appear here straight away.</li></ol></div>`;
  return `<div class="kpis"><div class="kpi p"><b>${s.length}</b><span>Students</span></div><div class="kpi g"><b>${active7}</b><span>Active this week</span></div><div class="kpi"><b>${activeT}</b><span>Active today</span></div><div class="kpi a"><b>${pct(avg)}</b><span>Class average (30 days)</span></div><div class="kpi r"><b>${idle.length}</b><span>Inactive 3+ days</span></div></div>
<div class="grid g2">
<div class="card"><h2>Needs attention</h2>${idle.length || risk.length ? `<div class="lst">${risk.slice(0, 5).map(x => `<div class="it"><span class="av">${esc(ini(x))}</span><div class="m"><b>${nm(x)}</b><small>Average ${pct(x.avg_pct_30d)} in the last 30 days</small></div><span class="pill bad">At risk</span><button class="g" data-a="stu" data-id="${x.student_id}">Open</button></div>`).join('')}${idle.filter(x => !risk.includes(x)).slice(0, 6).map(x => `<div class="it"><span class="av" style="background:var(--text3)">${esc(ini(x))}</span><div class="m"><b>${nm(x)}</b><small>Last practised ${ago(x.last_day)}</small></div><button class="g" data-a="nudge" data-id="${x.student_id}">Nudge</button></div>`).join('')}</div>` : empty('Everyone is on track', 'All students practised in the last 3 days and none is below 50%.')}</div>
<div class="card"><h2>Practice in the last 30 days</h2><div class="spark">${act.map(a => `<i class="${+a.attempts ? '' : 'z'}" style="height:${Math.round(+a.attempts * 100 / mx)}%" title="${esc(a.day)}: ${a.attempts} quizzes, ${a.active} students"></i>`).join('')}</div><div class="axis"><span>${esc((act[0] || {}).day || '')}</span><span>today</span></div>
<h2 style="margin-top:16px">By subject</h2>${subj.length ? subj.map(x => `<div class="row" style="align-items:center;margin-bottom:6px"><b style="flex:1;font:700 14px var(--fd)">${esc(x.subject)}</b><span class="muted" style="font-size:12px">${x.students} students</span><div style="width:120px">${bar(+x.avg_pct)}</div><b class="mono" style="width:44px;text-align:right">${pct(x.avg_pct)}</b></div>`).join('') : '<p class="muted">No quizzes yet.</p>'}</div>
<div class="card"><h2>Top this week<span class="sp"><button class="g" data-go="students">All students</button></span></h2><div class="lst">${s.slice().sort((a, b) => b.attempts_30d - a.attempts_30d || b.xp - a.xp).slice(0, 5).map((x, i) => `<div class="it"><b style="width:22px">${['🥇', '🥈', '🥉', '4', '5'][i]}</b><div class="m"><b>${nm(x)}</b><small>${x.attempts_30d} quizzes • 🔥 ${x.streak} • ${x.xp} XP</small></div><span class="pill ${barCls2(x.avg_pct_30d)}">${pct(x.avg_pct_30d)}</span></div>`).join('')}</div></div>
<div class="card"><h2>Recent work<span class="sp"><button class="g" data-go="work">Assign work</button></span></h2>${tasks.length ? `<div class="lst">${tasks.map(t => { const ss = subs.filter(x => x.task_id === t.id); return `<div class="it"><span>${KIND[t.kind] ? KIND[t.kind][0] : '📝'}</span><div class="m"><b>${esc(t.title)}</b><small>${ss.length}/${s.length} done${t.due_on ? ' • due ' + esc(t.due_on) : ''}</small></div>${bar(s.length ? ss.length * 100 / s.length : 0)}</div>`; }).join('')}</div>` : empty('No work set yet', 'Assign an Ace quiz on a topic. It is marked for you.', `<button class="b" data-go="work">Assign work</button>`)}</div>
</div>
${c.meet_url ? '' : `<div class="note">Teaching online? Add your Google Meet, Zoom or Teams link in <a href="#" data-go="library">Library</a> and students get a "Join live lesson" button.</div>`}`;
};
const barCls2 = v => v == null ? '' : +v < 50 ? 'bad' : +v < 70 ? 'w' : 'ok';
A.nudge = async el => { const c = cls(); const r = await sb().from('messages').insert({ school_id: c.school_id, sender_id: me().id, recipient_id: el.dataset.id, body: 'Hi! I noticed you have not practised for a few days. Ten minutes on Ace today will keep you on track. You can do it!' }); if (r.error) throw new Error(r.error.message); toast('Friendly reminder sent.'); el.disabled = true; };

/* ---------- students + student detail ---------- */
V.students = async () => {
  const s = await insights();
  return `<div class="card"><h2>${s.length} students<span class="sp"><input data-filter="#stu tbody tr" placeholder="Search" style="width:200px;margin:0"> <button class="g" data-a="csvstu">Export CSV</button></span></h2>
<div id="stu">${table(['Student', 'Last practised', 'Quizzes (30d)', 'Avg', 'Streak', 'XP', 'Topics', 'Attendance', ''], s.map(x => `<tr class="click" data-a="stu" data-id="${x.student_id}"><td><b>${nm(x)}</b><br><small class="muted">${esc(x.username || '')}${x.via === 'code' ? ' • joined with code' : ''}</small></td><td>${ago(x.last_day)}</td><td class="n">${x.attempts_30d}</td><td class="n"><span class="pill ${barCls2(x.avg_pct_30d)}">${pct(x.avg_pct_30d)}</span></td><td class="n">${x.streak}</td><td class="n">${x.xp}</td><td class="n">${x.topics_mastered}</td><td class="n">${pct(x.attendance_pct)}</td><td>›</td></tr>`), 'No students yet. Share your join code.')}</div></div>`;
};
A.csvstu = async () => { const s = await insights(); saveCsv('students.csv', csv([['Student', 'Username', 'Last practised', 'Quizzes 30d', 'Average %', 'Streak', 'XP', 'Topics mastered', 'Attendance %']].concat(s.map(x => [x.first_name + ' ' + x.surname, x.username, x.last_day, x.attempts_30d, x.avg_pct_30d, x.streak, x.xp, x.topics_mastered, x.attendance_pct])))); };
A.stu = async el => {
  const id = el.dataset.id, s = (await insights()).find(x => x.student_id === id); if (!s) return;
  const [qa, att, mk, sub] = await Promise.all([
    sb().from('quiz_attempts').select('subject,topic,kind,total,correct,created_at').eq('user_id', id).order('created_at', { ascending: false }).limit(40),
    sb().from('attendance').select('day,status').eq('student_id', id).eq('class_id', St.cls).order('day', { ascending: false }).limit(60),
    sb().from('marks').select('mark,comment,assessments(title,subject,max_mark,class_id)').eq('student_id', id),
    sb().from('task_submissions').select('submitted_at,auto_score,mark,tasks(title,class_id)').eq('student_id', id).order('submitted_at', { ascending: false }).limit(20)]);
  const Q = qa.data || [], bySub = {}; Q.forEach(a => { const b = bySub[a.subject] = bySub[a.subject] || [0, 0]; b[0] += a.total; b[1] += a.correct; });
  const d = document.createElement('div'); d.className = 'drawer';
  d.innerHTML = `<div><div class="row" style="align-items:center;margin-bottom:12px"><span class="av" style="width:48px;height:48px;font-size:16px">${esc(ini(s))}</span><div style="flex:1"><h2>${nm(s)}</h2><small class="muted">${esc(s.username || '')} ${s.student_number ? '• ' + esc(s.student_number) : ''}</small></div><button class="ib" data-a="closedr">✕</button></div>
<div class="kpis" style="grid-template-columns:repeat(3,1fr)"><div class="kpi p"><b>${s.xp}</b><span>XP</span></div><div class="kpi a"><b>🔥 ${s.streak}</b><span>Streak</span></div><div class="kpi g"><b>${pct(s.avg_pct_30d)}</b><span>Average (30d)</span></div></div>
<div class="card"><h2>By subject</h2>${Object.keys(bySub).filter(k => k !== 'daily').map(k => { const p = bySub[k][1] * 100 / bySub[k][0]; return `<div class="row" style="align-items:center;margin-bottom:6px"><b style="flex:1;font:700 14px var(--fd)">${esc(k)}</b><div style="width:110px">${bar(p)}</div><b class="mono" style="width:44px;text-align:right">${pct(p)}</b></div>`; }).join('') || '<p class="muted">No quizzes yet.</p>'}</div>
<div class="card"><h2>Recent quizzes</h2>${table(['When', 'Subject / topic', 'Score'], Q.slice(0, 12).map(a => `<tr><td>${esc(String(a.created_at).slice(0, 10))}</td><td>${esc(a.subject)}${a.topic ? '<br><small class="muted">' + esc(a.topic) + '</small>' : ''}</td><td class="n">${a.correct}/${a.total}</td></tr>`))}</div>
<div class="card"><h2>Marks and work</h2>${table(['Item', 'Result'], (mk.data || []).filter(m => m.assessments && m.assessments.class_id === St.cls).map(m => `<tr><td>${esc(m.assessments.title)} <small class="muted">${esc(m.assessments.subject)}</small></td><td class="n">${m.mark}/${m.assessments.max_mark}</td></tr>`).concat((sub.data || []).filter(x => x.tasks && x.tasks.class_id === St.cls).map(x => `<tr><td>${esc(x.tasks.title)}</td><td class="n">${x.mark != null ? x.mark : x.auto_score != null ? x.auto_score + '%' : 'handed in'}</td></tr>`)))}</div>
<div class="card"><h2>Attendance</h2><p>${pct(s.attendance_pct)} present over ${(att.data || []).length} recorded days.</p></div>
<div class="row"><button class="b" data-a="msgstu" data-id="${id}">Message</button>${s.via === 'school' ? `<button class="g" data-a="resetpw" data-id="${id}">Reset password</button>` : `<button class="g bad" data-a="removestu" data-id="${id}">Remove from class</button>`}</div></div>`;
  document.body.appendChild(d);
};
A.closedr = () => { const d = document.querySelector('.drawer'); if (d) d.remove(); };
A.msgstu = el => { A.closedr(); St.view = 'messages'; St.peer = el.dataset.id; T.go(); };
A.resetpw = async el => { const r = await fn('staff-reset-password', { student_id: el.dataset.id }); el.outerHTML = `<span class="code">${esc(r.temp_password)} <small>new temporary password</small></span>`; };
A.removestu = async el => { if (!el.dataset.sure) { el.dataset.sure = 1; el.textContent = 'Tap again to remove'; return; } must(await sb().from('class_members').delete().eq('class_id', St.cls).eq('student_id', el.dataset.id)); A.closedr(); fresh(); toast('Removed from the class.'); T.go(); };

/* ---------- progress ---------- */
V.progress = async () => {
  const tp = must(await sb().rpc('class_topic_perf', { p_class: St.cls })) || [], sp = must(await sb().rpc('class_subject_perf', { p_class: St.cls })) || [];
  return `<div class="grid g2"><div class="card"><h2>Hardest topics</h2><p class="sub">From quizzes in the last 90 days. Assign a quiz or a lesson on a topic in one tap.</p>${tp.length ? tp.map(x => `<div class="it" style="margin-bottom:6px"><div class="m"><b>${esc(x.topic)}</b><small>${esc(x.subject)} • ${x.students} students • ${x.attempts} quizzes</small></div><div style="width:90px">${bar(+x.avg_pct)}</div><b class="mono">${pct(x.avg_pct)}</b><button class="g" data-a="assignTopic" data-s="${esc(x.subject)}" data-t="${esc(x.topic)}">Assign</button></div>`).join('') : empty('Not enough data yet', 'Topics appear here once students have done a few quizzes.')}</div>
<div class="card"><h2>Subjects</h2>${table(['Subject', 'Students', 'Attempts', 'Avg', ''], sp.map(x => `<tr><td>${esc(x.subject)}</td><td class="n">${x.students}</td><td class="n">${x.attempts}</td><td class="n">${pct(x.avg_pct)}</td><td style="width:120px">${bar(+x.avg_pct)}</td></tr>`))}</div></div>`;
};
A.assignTopic = el => { St.view = 'work'; St.pre = { kind: 'quiz', subject: el.dataset.s, topic: el.dataset.t }; T.go(); };

/* ---------- register (attendance) ---------- */
V.register = async () => {
  const s = await insights(), a = must(await sb().from('attendance').select('student_id,status').eq('class_id', St.cls).eq('day', St.day)) || [], m = {}; a.forEach(x => m[x.student_id] = x.status);
  const mon = St.month, mo = must(await sb().from('attendance').select('student_id,day,status').eq('class_id', St.cls).gte('day', mon + '-01').lte('day', mon + '-31')) || [];
  const days = [...new Set(mo.map(x => x.day))].length, byS = {}; mo.forEach(x => { const b = byS[x.student_id] = byS[x.student_id] || [0, 0]; b[1]++; if (x.status === 'present' || x.status === 'late') b[0]++; });
  const counts = { present: 0, absent: 0, late: 0, excused: 0 }; Object.values(m).forEach(v => counts[v]++);
  return `<div class="card"><h2>Register<span class="sp row" style="gap:6px"><input type="date" data-a="setday" value="${St.day}" max="${today()}" style="width:170px;margin:0"><button class="g" data-a="allpresent">Mark all present</button></span></h2>
<p class="sub">Tap a student to cycle present, absent, late, excused. ${counts.present} present • ${counts.absent} absent • ${counts.late} late • ${s.length - Object.keys(m).length} not marked</p>
<div class="att">${s.map(x => `<div class="ac ${m[x.student_id] || ''}" data-a="att" data-id="${x.student_id}" role="button" tabindex="0"><b>${nm(x)}</b><small>${m[x.student_id] || 'not marked'}</small></div>`).join('')}</div></div>
<div class="card"><h2>Month summary<span class="sp"><input type="month" data-a="setmonth" value="${mon}" style="width:170px;margin:0"></span></h2><p class="sub">${days} days recorded.</p>${table(['Student', 'Present or late', '%'], s.map(x => { const b = byS[x.student_id] || [0, 0]; return `<tr><td>${nm(x)}</td><td class="n">${b[0]}/${b[1]}</td><td class="n">${b[1] ? pct(b[0] * 100 / b[1]) : '–'}</td></tr>`; }))}</div>`;
};
const CYC = ['present', 'absent', 'late', 'excused'];
A.att = async el => { const cur = CYC.indexOf((el.className.match(/present|absent|late|excused/) || [''])[0]), nx = CYC[(cur + 1) % 4]; must(await sb().from('attendance').upsert({ class_id: St.cls, student_id: el.dataset.id, day: St.day, status: nx, noted_by: me().id })); el.className = 'ac ' + nx; el.querySelector('small').textContent = nx; };
A.allpresent = async () => { const s = await insights(); must(await sb().from('attendance').upsert(s.map(x => ({ class_id: St.cls, student_id: x.student_id, day: St.day, status: 'present', noted_by: me().id })))); toast('Everyone marked present.'); T.go(); };
A.setday = el => { St.day = el.value || today(); T.go(); };
A.setmonth = el => { St.month = el.value || today().slice(0, 7); T.go(); };

/* ---------- assign work ---------- */
const KIND = { quiz: ['📝', 'Ace quiz', 'Questions from the Ace bank on a topic, marked automatically.'], lesson: ['▶️', 'Ace lesson', 'The narrated lesson for a topic, with checkpoints.'], mock: ['⏱️', 'Ace mock exam', 'A full timed mock for a subject.'], written: ['✍️', 'Written work', 'Students type an answer; you mark it.'], reading: ['📖', 'Reading', 'Something to read, with optional notes.'], video: ['🎬', 'Video', 'A video link to watch.'], link: ['🔗', 'Link', 'Any web page or resource.'] };
V.work = async () => {
  const pre = St.pre || {}; St.pre = null;
  const ts = must(await sb().from('tasks').select('*').eq('class_id', St.cls).order('created_at', { ascending: false })) || [];
  const s = await insights(), subs = ts.length ? must(await sb().from('task_submissions').select('task_id,student_id,auto_score,mark,submitted_at').in('task_id', ts.map(t => t.id))) || [] : [];
  const [d, ek] = await curEx(), subjects = subjectsOf(d, ek), kind = St.wk || pre.kind || 'quiz', s0 = pre.subject || St.ws || (cls().subject && subjects.includes(cls().subject) ? cls().subject : subjects[0]);
  const mods = modulesOf(d, ek, s0), rubrics = kind === 'written' ? must(await sb().from('rubrics').select('id,title,criteria').order('title')) || [] : [];
  let h = `<div class="card"><h2>Assign work</h2><div class="tabs">${Object.keys(KIND).map(k => `<button class="g ${k === kind ? 'on' : ''}" data-a="wkind" data-v="${k}">${KIND[k][0]} ${KIND[k][1]}</button>`).join('')}</div><p class="sub">${KIND[kind][2]}</p><form data-f="task"><input type="hidden" name="kind" value="${kind}">`;
  if (['quiz', 'lesson', 'mock'].includes(kind)) {
    h += `<div class="row"><label>Exam<input value="${esc(ek || '')}" disabled></label><label>Subject<select name="subject" data-a="wsub">${subjects.map(x => opt(x, x, x === s0)).join('')}</select></label>${kind !== 'mock' ? `<label style="flex:2 1 260px">Topic<select name="topic">${mods.map((m, i) => `<optgroup label="${esc((i + 1) + '. ' + m.title)}">${(m.topics || []).map(t => opt(t, t, t === pre.topic)).join('')}</optgroup>`).join('')}</select></label>` : ''}${kind === 'quiz' ? `<label style="flex:0 1 110px">Questions<select name="n">${[5, 10, 15, 20].map(n => opt(n, n, n === 10)).join('')}</select></label>` : ''}</div>`;
    h += `<input type="hidden" name="exam" value="${esc(ek || '')}">`;
  }
  h += `<div class="row"><label style="flex:2 1 260px">Title<input name="title" maxlength="160" placeholder="${['quiz', 'lesson', 'mock'].includes(kind) ? 'Leave empty to use the topic name' : 'e.g. Essay: causes of inflation'}" ${['quiz', 'lesson', 'mock'].includes(kind) ? '' : 'required'}></label><label>Due<input name="due_on" type="date" min="${today()}"></label></div>`;
  if (['video', 'link', 'reading'].includes(kind)) h += `<label>Link${kind === 'reading' ? ' (optional)' : ''}<input name="link_url" type="url" placeholder="https://" ${kind === 'reading' ? '' : 'required'}></label>`;
  h += `<label>Instructions${['quiz', 'lesson', 'mock'].includes(kind) ? ' (optional)' : ''}<textarea name="body" maxlength="4000" placeholder="${kind === 'written' ? 'The question and what a good answer includes' : 'Anything students should know'}"></textarea></label>`;
  if (kind === 'written') h += `<label>Rubric (optional)<select name="rubric"><option value="">None</option>${rubrics.map(r => opt(r.id, r.title)).join('')}</select></label>`;
  h += `<button class="b">Assign to ${esc(cls().name)}</button></form></div>`;
  h += `<div class="card"><h2>Set work</h2>${ts.length ? `<div class="lst">${ts.map(t => { const ss = subs.filter(x => x.task_id === t.id), sc = ss.filter(x => x.auto_score != null || x.mark != null), av = ss.filter(x => x.auto_score != null); return `<div class="it"><span style="font-size:20px">${(KIND[t.kind] || KIND.written)[0]}</span><div class="m"><b>${esc(t.title)}</b><small>${(KIND[t.kind] || KIND.written)[1]}${t.due_on ? ' • due ' + esc(t.due_on) : ''} • ${ss.length}/${s.length} done${av.length ? ' • average ' + pct(av.reduce((n, x) => n + +x.auto_score, 0) / av.length) : ''}</small></div><div style="width:90px">${bar(s.length ? ss.length * 100 / s.length : 0)}</div><button class="g" data-a="opentask" data-id="${t.id}">Open</button></div>`; }).join('')}</div>` : empty('Nothing set yet', 'Start with an Ace quiz on the topic you taught this week.')}</div>`;
  if (St.task) h += await taskDetail(ts.find(t => t.id === St.task), s);
  return h;
};
async function taskDetail(t, s) {
  if (!t) return '';
  const sub = must(await sb().from('task_submissions').select('*').eq('task_id', t.id)) || [], by = {}; sub.forEach(x => by[x.student_id] = x);
  const rub = t.rubric && t.rubric.criteria ? t.rubric : null;
  return `<div class="card" id="taskd"><h2>${esc(t.title)}<span class="sp"><button class="g bad" data-a="deltask" data-id="${t.id}">Delete</button></span></h2>${t.body ? `<p style="white-space:pre-wrap">${esc(t.body)}</p>` : ''}
${s.map(x => { const r = by[x.student_id]; return `<form class="qa" data-f="marksub" data-sid="${x.student_id}" data-tid="${t.id}"><div class="row" style="align-items:center"><b style="flex:1">${nm(x)}</b>${r ? `<span class="pill ok">${r.auto_score != null ? 'Ace score ' + r.auto_score + '%' : 'Handed in'}</span><small class="muted">${esc(String(r.submitted_at).slice(0, 16).replace('T', ' '))}</small>` : '<span class="pill w">Not done</span>'}</div>
${r && r.body ? `<p style="white-space:pre-wrap;margin:8px 0">${esc(r.body)}</p>` : ''}${r ? `${rub ? `<div class="row">${rub.criteria.map((c, i) => `<label style="flex:1 1 120px">${esc(c.name)} (/${c.max})<input name="r${i}" type="number" min="0" max="${c.max}" step="any"></label>`).join('')}</div>` : ''}<div class="row"><label style="flex:0 1 120px">Mark<input name="mark" type="number" min="0" step="any" value="${r.mark == null ? '' : r.mark}"></label><label style="flex:3 1 220px">Feedback<input name="feedback" maxlength="2000" value="${esc(r.feedback || '')}"></label><button class="b">Save</button></div>` : ''}</form>`; }).join('')}</div>`;
}
A.wkind = el => { St.wk = el.dataset.v; T.go(); };
A.wsub = el => { St.ws = el.value; St.wk = (document.querySelector('form[data-f=task] [name=kind]') || {}).value || St.wk; T.go(); };
A.opentask = el => { St.task = el.dataset.id; St.after = () => { const t = document.getElementById('taskd'); if (t) t.scrollIntoView({ behavior: 'smooth' }); }; T.go(); };
A.deltask = async el => { if (!el.dataset.sure) { el.dataset.sure = 1; el.textContent = 'Tap again to delete'; return; } must(await sb().from('tasks').delete().eq('id', el.dataset.id)); St.task = ''; toast('Deleted.'); T.go(); };
F.task = async d => {
  const ace = ['quiz', 'lesson', 'mock'].includes(d.kind);
  const title = d.title || (d.kind === 'mock' ? `Mock exam: ${d.subject}` : d.kind === 'lesson' ? `Lesson: ${d.topic}` : d.kind === 'quiz' ? `Quiz: ${d.topic}` : '');
  let rubric = null; if (d.rubric) { const r = must(await sb().from('rubrics').select('title,criteria').eq('id', d.rubric).single()); rubric = r; }
  must(await sb().from('tasks').insert({ class_id: St.cls, kind: d.kind, title: title.slice(0, 160), subject: d.subject || null, body: d.body || null, due_on: d.due_on || null, link_url: d.link_url || null, rubric, created_by: me().id,
    topic_ref: ace ? { kind: d.kind, exam: d.exam, subject: d.subject, topic: d.kind === 'mock' ? null : d.topic, n: +d.n || 10 } : null }));
  St.wk = ''; toast('Assigned. Students see it in Tools → My classes → Class work.'); T.go();
};
F.marksub = async (d, f) => {
  let mark = d.mark === '' ? null : +d.mark; const parts = Object.keys(d).filter(k => /^r\d+$/.test(k) && d[k] !== '');
  if (parts.length && mark == null) mark = parts.reduce((n, k) => n + +d[k], 0);
  must(await sb().from('task_submissions').update({ mark, feedback: d.feedback || null }).eq('task_id', f.dataset.tid).eq('student_id', f.dataset.sid)); toast('Saved.');
};

/* ---------- gradebook ---------- */
V.grades = async () => {
  const ca = CA[H.cc()] || ['Continuous assessment', ''];
  const as = must(await sb().from('assessments').select('*').eq('class_id', St.cls).order('held_on', { ascending: false, nullsFirst: false })) || [];
  const s = await insights(), mk = as.length ? must(await sb().from('marks').select('assessment_id,student_id,mark').in('assessment_id', as.map(a => a.id))) || [] : [], M = {}; mk.forEach(x => M[x.assessment_id + '|' + x.student_id] = +x.mark);
  const subjects = [...new Set(as.map(a => a.subject))];
  let h = `<div class="card"><h2>New assessment</h2><p class="sub">${esc(ca[0])}: ${esc(ca[1])} Give items a weight to include them in the ${esc(ca[0])} total.</p><form data-f="asmt"><div class="row"><label style="flex:2 1 220px">Title<input name="title" required maxlength="120" placeholder="Test 1: Algebra"></label><label>Subject<input name="subject" required maxlength="60" value="${esc(cls().subject || '')}"></label><label>Type<select name="kind">${['test', 'task', 'oral', 'project', 'exam'].map(k => opt(k)).join('')}</select></label><label>Out of<input name="max_mark" type="number" min="1" step="any" value="100" required></label><label>Weight %<input name="weight" type="number" min="0" max="100" step="any" value="0"></label><label>Date<input name="held_on" type="date" value="${today()}"></label></div><button class="b">Add</button></form></div>`;
  if (St.asmt) { const a = as.find(x => x.id === St.asmt); if (a) h += `<div class="card" id="mk"><h2>${esc(a.title)} <span class="muted" style="font-size:14px">out of ${a.max_mark}</span></h2><form data-f="marks">${table(['Student', 'Mark', 'Comment'], s.map(x => `<tr><td>${nm(x)}</td><td style="width:120px"><input name="m_${x.student_id}" type="number" min="0" max="${a.max_mark}" step="any" value="${M[a.id + '|' + x.student_id] == null ? '' : M[a.id + '|' + x.student_id]}" style="margin:0"></td><td><input name="c_${x.student_id}" maxlength="500" style="margin:0"></td></tr>`))}<p><button class="b">Save marks</button></p></form></div>`; }
  h += `<div class="card"><h2>Gradebook<span class="sp"><button class="g" data-a="csvgrades">Export CSV</button></span></h2>${as.length ? `<div class="tw"><table><thead><tr><th>Student</th>${as.map(a => `<th class="n" title="${esc(a.subject)}"><button class="g" data-a="openasmt" data-id="${a.id}" style="padding:3px 8px">${esc(a.title.slice(0, 18))}</button><br><small>/${a.max_mark}${+a.weight ? ' • ' + a.weight + '%' : ''}</small></th>`).join('')}${subjects.map(sj => `<th class="n">${esc(ca[2] || 'CA')} ${esc(sj)}</th>`).join('')}</tr></thead><tbody>${s.map(x => `<tr><td>${nm(x)}</td>${as.map(a => { const v = M[a.id + '|' + x.student_id]; return `<td class="n">${v == null ? '<span class="muted">–</span>' : v}</td>`; }).join('')}${subjects.map(sj => { const ws = as.filter(a => a.subject === sj && +a.weight > 0 && M[a.id + '|' + x.student_id] != null); const tw = ws.reduce((n, a) => n + +a.weight, 0); return `<td class="n"><b>${tw ? pct(ws.reduce((n, a) => n + M[a.id + '|' + x.student_id] / a.max_mark * a.weight, 0) * 100 / tw) : '–'}</b></td>`; }).join('')}</tr>`).join('')}</tbody></table></div>` : empty('No assessments yet', 'Add a test above, then enter marks.')}</div>`;
  St._grades = { as, s, M, subjects };
  return h;
};
A.openasmt = el => { St.asmt = el.dataset.id; St.after = () => { const m = document.getElementById('mk'); if (m) m.scrollIntoView({ behavior: 'smooth' }); }; T.go(); };
A.csvgrades = () => { const g = St._grades; if (!g) return; saveCsv('gradebook.csv', csv([['Student'].concat(g.as.map(a => `${a.title} (/${a.max_mark})`))].concat(g.s.map(x => [x.first_name + ' ' + x.surname].concat(g.as.map(a => g.M[a.id + '|' + x.student_id])))))); };
F.asmt = async d => { must(await sb().from('assessments').insert({ class_id: St.cls, subject: d.subject, title: d.title, kind: d.kind, max_mark: +d.max_mark, weight: +d.weight || 0, held_on: d.held_on || null, created_by: me().id })); toast('Assessment added.'); T.go(); };
F.marks = async d => { const rows = []; Object.keys(d).forEach(k => { if (k.startsWith('m_') && d[k] !== '') rows.push({ assessment_id: St.asmt, student_id: k.slice(2), mark: +d[k], comment: d['c_' + k.slice(2)] || null }); }); if (!rows.length) return toast('Enter at least one mark.', true); must(await sb().from('marks').upsert(rows)); toast(rows.length + ' marks saved.'); St.asmt = ''; T.go(); };

/* ---------- curriculum pacing ---------- */
V.pacing = async () => {
  const [d, ek] = await curEx(), subjects = subjectsOf(d, ek), s0 = St.ps && subjects.includes(St.ps) ? St.ps : (cls().subject && subjects.includes(cls().subject) ? cls().subject : subjects[0]);
  const mods = modulesOf(d, ek, s0), rows = must(await sb().from('class_pacing').select('*').eq('class_id', St.cls).eq('subject', s0)) || [], P = {}; rows.forEach(r => P[r.topic] = r);
  const all = mods.reduce((n, m) => n + (m.topics || []).length, 0), done = rows.filter(r => r.taught_on).length;
  return `<div class="card"><h2>Curriculum pacing<span class="sp"><select data-a="psub" style="margin:0;width:auto">${subjects.map(x => opt(x, x, x === s0)).join('')}</select></span></h2><p class="sub">${esc(ek)} syllabus for ${esc(s0)}. Tick topics as you teach them; students see what has been covered. ${done} of ${all} taught.</p>${bar(all ? done * 100 / all : 0)}</div>
${mods.map((m, i) => { const t = m.topics || [], dn = t.filter(x => P[x] && P[x].taught_on).length; return `<div class="card"><h2>${i + 1}. ${esc(m.title)} <span class="pill ${dn === t.length && t.length ? 'ok' : ''}">${dn}/${t.length}</span></h2><div class="pace">${t.map(x => { const r = P[x]; return `<div class="pt ${r && r.taught_on ? 'done' : ''}"><input type="checkbox" data-a="ptick" data-s="${esc(s0)}" data-t="${esc(x)}" ${r && r.taught_on ? 'checked' : ''} aria-label="Taught"><b>${esc(x)}</b><input type="date" title="Planned week" data-a="pweek" data-s="${esc(s0)}" data-t="${esc(x)}" value="${r && r.planned_week ? r.planned_week : ''}"><button class="g" data-a="assignTopic" data-s="${esc(s0)}" data-t="${esc(x)}">Assign</button></div>`; }).join('')}</div></div>`; }).join('')}`;
};
A.psub = el => { St.ps = el.value; T.go(); };
A.ptick = async el => { must(await sb().from('class_pacing').upsert({ class_id: St.cls, subject: el.dataset.s, topic: el.dataset.t, taught_on: el.checked ? today() : null, updated_by: me().id, updated_at: new Date().toISOString() })); el.closest('.pt').classList.toggle('done', el.checked); };
A.pweek = async el => { must(await sb().from('class_pacing').upsert({ class_id: St.cls, subject: el.dataset.s, topic: el.dataset.t, planned_week: el.value || null, updated_by: me().id, updated_at: new Date().toISOString() })); toast('Planned.'); };

/* ---------- live quiz ---------- */
V.live = async () => {
  const ss = must(await sb().from('live_sessions').select('id,code,state,current_index,questions,created_at').eq('class_id', St.cls).order('created_at', { ascending: false }).limit(10)) || [];
  const [d, ek] = await curEx(), subjects = subjectsOf(d, ek), s0 = St.ls || cls().subject || subjects[0], mods = modulesOf(d, ek, subjects.includes(s0) ? s0 : subjects[0]);
  let h = `<div class="grid g2"><div class="card"><h2>From the Ace question bank</h2><form data-f="livebank"><div class="row"><label>Subject<select name="subject" data-a="lsub">${subjects.map(x => opt(x, x, x === s0)).join('')}</select></label><label style="flex:0 1 110px">Questions<select name="n">${[5, 10, 15, 20].map(n => opt(n, n, n === 10)).join('')}</select></label></div><label>Topic<select name="topic"><option value="">Mixed: whole subject</option>${mods.map((m, i) => `<optgroup label="${esc((i + 1) + '. ' + m.title)}">${(m.topics || []).map(t => opt(t)).join('')}</optgroup>`).join('')}</select></label><button class="b">Create live quiz</button></form></div>
<div class="card"><h2>Write your own</h2><form data-f="live"><label>One per line: <code>Question | A | B | C | D | correct letter</code><textarea name="qs" required placeholder="What is 7 x 8? | 54 | 56 | 58 | 64 | B"></textarea></label><button class="b">Create live quiz</button></form></div></div>
<div class="card"><h2>Your live quizzes</h2><p class="sub">Students open Tools → Live class quiz in the app and enter the code. Show the code on the board.</p>${table(['Code', 'Questions', 'State', ''], ss.map(x => `<tr><td><b style="font:800 20px var(--fd);letter-spacing:.14em">${esc(x.code)}</b></td><td class="n">${(x.questions || []).length}</td><td><span class="pill ${x.state === 'running' ? 'ok' : ''}">${esc(x.state)}</span> ${x.state === 'running' ? 'Q' + (x.current_index + 1) : ''}</td><td>${x.state === 'lobby' ? `<button class="b" data-a="livest" data-id="${x.id}" data-s="running">Start</button>` : ''}${x.state === 'running' ? `<button class="b" data-a="livenext" data-id="${x.id}">Next question</button> <button class="g bad" data-a="livest" data-id="${x.id}" data-s="ended">End</button>` : ''} <button class="g" data-a="livescores" data-id="${x.id}">Scores</button></td></tr>`))}</div>`;
  if (St.live) { const ans = must(await sb().from('live_answers').select('student_id,correct').eq('session_id', St.live)) || [], s = await insights(), sc = {}; ans.forEach(a => { const b = sc[a.student_id] = sc[a.student_id] || { c: 0, n: 0 }; b.n++; if (a.correct) b.c++; });
    h += `<div class="card"><h2>Scores<span class="sp"><button class="g" data-a="refresh">Refresh</button></span></h2>${table(['Student', 'Correct', 'Answered'], s.filter(x => sc[x.student_id]).sort((a, b) => sc[b.student_id].c - sc[a.student_id].c).map(x => `<tr><td>${nm(x)}</td><td class="n">${sc[x.student_id].c}</td><td class="n">${sc[x.student_id].n}</td></tr>`))}</div>`; }
  return h;
};
A.lsub = el => { St.ls = el.value; T.go(); };
A.refresh = () => T.go();
A.livest = async el => { must(await sb().from('live_sessions').update({ state: el.dataset.s, current_index: 0 }).eq('id', el.dataset.id)); St.live = el.dataset.id; T.go(); };
A.livenext = async el => { const s = must(await sb().from('live_sessions').select('current_index,questions').eq('id', el.dataset.id).single()); const n = s.current_index + 1; must(await sb().from('live_sessions').update(n >= s.questions.length ? { state: 'ended' } : { current_index: n }).eq('id', el.dataset.id)); T.go(); };
A.livescores = el => { St.live = el.dataset.id; T.go(); };
async function makeLive(qs, keys) {
  if (!qs.length || qs.length > 40) throw new Error('Use between 1 and 40 questions.');
  const code = Array.from(crypto.getRandomValues(new Uint8Array(6))).map(x => 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'[x % 32]).join('');
  const s = must(await sb().from('live_sessions').insert({ class_id: St.cls, host_id: me().id, code, questions: qs }).select('id').single());
  must(await sb().from('live_keys').insert({ session_id: s.id, answers: keys })); toast('Live quiz ready. Code: ' + code); St.live = ''; T.go();
}
T.makeLive = makeLive;
F.live = async d => { const qs = [], keys = []; d.qs.split('\n').map(l => l.trim()).filter(Boolean).forEach((l, i) => { const p = l.split('|').map(x => x.trim()); const k = 'ABCD'.indexOf((p[5] || '').toUpperCase()); if (p.length !== 6 || p.slice(0, 5).some(x => !x) || k < 0) throw new Error('Line ' + (i + 1) + ' should be: Question | A | B | C | D | correct letter'); qs.push({ q: p[0], o: p.slice(1, 5) }); keys.push(k); }); await makeLive(qs, keys); };
F.livebank = async d => {
  const [D, ek] = await curEx(), pool = []; modulesOf(D, ek, d.subject).forEach(m => (m.questions || []).forEach(q => { if (q.type === 'mcq' && q.o && q.o.length === 4 && (!d.topic || q.topic === d.topic)) pool.push(q); }));
  if (!pool.length) throw new Error('No multiple-choice questions for that choice yet.');
  for (let i = pool.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [pool[i], pool[j]] = [pool[j], pool[i]]; }
  const cur = (D && D.currency) || '', fix = x => String(x).split('{{CUR}}').join(cur);
  const pick = pool.slice(0, +d.n || 10); await makeLive(pick.map(q => ({ q: fix(q.q), o: q.o.map(fix) })), pick.map(q => q.a));
};

/* ---------- Q&A board ---------- */
V.qna = async () => {
  const q = must(await sb().from('class_questions').select('*').eq('class_id', St.cls).order('created_at', { ascending: false }).limit(60)) || [], s = await insights(), N = {}; s.forEach(x => N[x.student_id] = x);
  const open = q.filter(x => !x.answer && !x.hidden), done = q.filter(x => x.answer || x.hidden);
  const one = x => `<div class="qa"><div class="row" style="align-items:center"><b class="q" style="flex:1">${esc(x.body)}</b>${x.hidden ? '<span class="pill w">hidden</span>' : ''}</div><small class="muted">${N[x.author_id] ? nm(N[x.author_id]) : 'Student'} • ${esc(String(x.created_at).slice(0, 10))}${x.subject ? ' • ' + esc(x.subject) : ''}</small>${x.answer ? `<div class="a">${esc(x.answer)}</div>` : ''}<form data-f="answer" data-id="${x.id}" class="row" style="margin-top:8px"><label style="flex:1 1 280px;margin:0"><textarea name="answer" maxlength="3000" placeholder="Answer for the whole class" style="min-height:60px">${esc(x.answer || '')}</textarea></label><button class="b">${x.answer ? 'Update' : 'Answer'}</button><button class="g" type="button" data-a="aiqa" data-q="${esc(x.body)}">✨ Draft</button><button class="g" type="button" data-a="hideq" data-id="${x.id}" data-v="${x.hidden ? '' : '1'}">${x.hidden ? 'Show' : 'Hide'}</button></form></div>`;
  return `<div class="card"><h2>Waiting for an answer (${open.length})</h2><p class="sub">Students ask from Tools → My classes. Answers are visible to the whole class, so one answer helps everyone.</p>${open.map(one).join('') || empty('No open questions', 'Encourage students to ask here instead of messaging one by one.')}</div>${done.length ? `<div class="card"><h2>Answered</h2>${done.map(one).join('')}</div>` : ''}`;
};
F.answer = async (d, f) => { must(await sb().from('class_questions').update({ answer: d.answer || null }).eq('id', f.dataset.id)); toast('Answer posted.'); T.go(); };
A.hideq = async el => { must(await sb().from('class_questions').update({ hidden: !!el.dataset.v }).eq('id', el.dataset.id)); T.go(); };
A.aiqa = async el => { const ta = el.closest('form').querySelector('textarea'); ta.value = 'Ace is drafting…'; const c = cls(); const r = await fn('ai-tutor', { messages: [{ role: 'user', content: 'A student in my class asked: "' + el.dataset.q + '". Write a clear answer I can post for the whole class, with a short worked example if useful.' }], context: { mode: 'answer', country: (H.CN[H.cc()] || H.cc()).replace(/^\S+\s/, ''), exam: c.exam || '', subject: c.subject || '', topic: '' } }).catch(e => ({ reply: '' , err: e.message })); ta.value = r.reply || ''; if (r.err) toast(r.err, true); };

/* ---------- library + live lesson link ---------- */
V.library = async () => {
  const c = cls(), r = must(await sb().from('class_resources').select('*').eq('class_id', St.cls).order('created_at', { ascending: false })) || [];
  return `<div class="grid g2"><div class="card"><h2>Live lesson link</h2><p class="sub">Your Google Meet, Zoom or Teams link. Students get a "Join live lesson" button in My classes.</p><form data-f="meet" class="row"><label style="flex:1 1 260px">Link<input name="meet_url" type="url" placeholder="https://meet.google.com/…" value="${esc(c.meet_url || '')}"></label><button class="b">Save</button></form></div>
<div class="card"><h2>Share a resource</h2><form data-f="res"><div class="row"><label style="flex:2 1 220px">Title<input name="title" required maxlength="140"></label><label>Type<select name="kind">${[['link', 'Link'], ['video', 'Video'], ['note', 'Note'], ['file', 'File link']].map(k => opt(k[0], k[1])).join('')}</select></label></div><label>Link (https)<input name="url" type="url" placeholder="https://"></label><label>Note (optional)<textarea name="body" maxlength="6000"></textarea></label><button class="b">Share with ${esc(c.name)}</button></form></div></div>
<div class="card"><h2>Library (${r.length})</h2>${r.length ? `<div class="lst">${r.map(x => `<div class="it"><span style="font-size:20px">${{ link: '🔗', video: '🎬', note: '📝', file: '📎' }[x.kind]}</span><div class="m"><b>${esc(x.title)}</b><small>${x.url ? `<a href="${esc(x.url)}" target="_blank" rel="noopener">${esc(x.url.slice(0, 60))}</a>` : esc((x.body || '').slice(0, 90))}</small></div><button class="g bad" data-a="delres" data-id="${x.id}">Remove</button></div>`).join('')}</div>` : empty('Nothing shared yet', 'Share past questions you wrote, video explanations or reading.')}</div>`;
};
F.meet = async d => { must(await sb().from('classes').update({ meet_url: d.meet_url || null }).eq('id', St.cls)); await H.loadClasses(); toast('Saved.'); T.go(); };
F.res = async d => { if (!d.url && !d.body) throw new Error('Add a link or a note.'); must(await sb().from('class_resources').insert({ class_id: St.cls, title: d.title, kind: d.kind, url: d.url || null, body: d.body || null, created_by: me().id })); toast('Shared.'); T.go(); };
A.delres = async el => { must(await sb().from('class_resources').delete().eq('id', el.dataset.id)); T.go(); };

/* ---------- notices ---------- */
V.notices = async () => {
  const an = must(await sb().from('announcements').select('*').or(`class_id.eq.${St.cls},class_id.is.null`).order('created_at', { ascending: false }).limit(30)) || [];
  return `<div class="card"><h2>New notice</h2><form data-f="notice"><label>Title<input name="title" required maxlength="140"></label><label>Message<textarea name="body" required maxlength="4000"></textarea></label><div class="row" style="align-items:center"><label style="flex:0 1 220px">Send to<select name="scope"><option value="class">${esc(cls().name)}</option>${isAdmin() && !isTutor() ? '<option value="school">Whole school</option>' : ''}</select></label><label class="chk"><input type="checkbox" name="push"> Also send a phone notification</label></div><button class="b">Post</button></form></div>
<div class="card"><h2>Recent notices</h2>${an.length ? an.map(x => `<div class="qa"><b class="q">${esc(x.title)}</b> <span class="pill">${x.class_id ? 'Class' : 'School'}</span><p style="white-space:pre-wrap;margin:6px 0">${esc(x.body)}</p><small class="muted">${esc(String(x.created_at).slice(0, 16).replace('T', ' '))}</small></div>`).join('') : empty('No notices yet')}</div>`;
};
F.notice = async d => { const c = cls(), school = d.scope === 'school';
  must(await sb().from('announcements').insert({ school_id: c.school_id, class_id: school ? null : St.cls, title: d.title, body: d.body, created_by: me().id }));
  if (d.push && !school) { try { const r = await fn('send-push', { class_id: St.cls, title: d.title, body: d.body.slice(0, 120) }); toast(`Posted. ${r.sent} notification(s) sent.`); } catch (e) { toast('Posted, but notifications failed: ' + e.message, true); } } else toast('Posted.');
  T.go(); };

/* ---------- messages ---------- */
V.messages = async () => {
  const s = await insights(), un = must(await sb().from('messages').select('sender_id').eq('recipient_id', me().id).is('read_at', null)) || [], cnt = {}; un.forEach(x => cnt[x.sender_id] = (cnt[x.sender_id] || 0) + 1);
  let h = `<div class="grid g2" style="grid-template-columns:minmax(0,1fr) minmax(0,2fr)"><div class="card"><h2>Students</h2><input data-filter="#mlist .it" placeholder="Search" style="margin:0 0 10px"><div class="lst" id="mlist">${s.map(x => `<button class="it" style="text-align:left;${St.peer === x.student_id ? 'border-color:var(--primary)' : ''}" data-a="peer" data-id="${x.student_id}"><span class="av">${esc(ini(x))}</span><div class="m"><b>${nm(x)}</b><small>${ago(x.last_day)}</small></div>${cnt[x.student_id] ? `<span class="pill bad">${cnt[x.student_id]} new</span>` : ''}</button>`).join('')}</div></div><div class="card">`;
  if (!St.peer) h += empty('Choose a student', 'Messages are private between you and the student.');
  else { const p = St.peer, th = must(await sb().from('messages').select('*').or(`and(sender_id.eq.${me().id},recipient_id.eq.${p}),and(sender_id.eq.${p},recipient_id.eq.${me().id})`).order('created_at', { ascending: true }).limit(150)) || [];
    await sb().from('messages').update({ read_at: new Date().toISOString() }).eq('recipient_id', me().id).eq('sender_id', p).is('read_at', null);
    const who = s.find(x => x.student_id === p);
    h += `<h2>${who ? nm(who) : ''}</h2><div style="max-height:52vh;overflow:auto;display:grid;gap:6px;margin-bottom:10px">${th.map(x => `<div style="justify-self:${x.sender_id === me().id ? 'end' : 'start'};max-width:80%;background:${x.sender_id === me().id ? 'var(--btn)' : 'var(--tint)'};color:${x.sender_id === me().id ? '#fff' : 'var(--text)'};border-radius:14px;padding:8px 12px;white-space:pre-wrap">${esc(x.body)}<br><small style="opacity:.7">${esc(String(x.created_at).slice(5, 16).replace('T', ' '))}</small></div>`).join('') || '<p class="muted">No messages yet.</p>'}</div>
<form data-f="msg" class="row"><label style="flex:1;margin:0"><input name="body" required maxlength="2000" autocomplete="off" placeholder="Write a message"></label><button class="b">Send</button></form>`; }
  return h + '</div></div>';
};
A.peer = el => { St.peer = el.dataset.id; T.go(); };
F.msg = async d => { const c = cls(); must(await sb().from('messages').insert({ school_id: c.school_id, sender_id: me().id, recipient_id: St.peer, body: d.body })); T.go(); };

T.insights = insights; T.fresh = fresh; T.KIND = KIND;
})();
