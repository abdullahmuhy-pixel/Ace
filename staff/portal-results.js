/* Ace Teach: academic record for school admins. Terms and grade bands, term results compiled from the gradebook
   (editable before publishing), published term reports that students see in the app, and transcripts with a code
   anyone can check at /verify/. Rules live in Postgres (compile_term, publish_term, issue_transcript …). */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, must, toast, csv, saveCsv, empty, nm } = H;
const sb = () => T.sb, me = () => T.me;
const opt = (v, l, sel) => `<option value="${esc(v)}" ${sel ? 'selected' : ''}>${esc(l == null ? v : l)}</option>`;
const day = d => d ? new Date(String(d).length === 10 ? d + 'T00:00:00' : d).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' }) : '';
const num = v => v == null ? '–' : (+v).toLocaleString(undefined, { maximumFractionDigits: 1 });
const BANDS = [{ grade: 'A', min: 80 }, { grade: 'B', min: 70 }, { grade: 'C', min: 60 }, { grade: 'D', min: 50 }, { grade: 'E', min: 40 }, { grade: 'F', min: 0 }];
const ord = n => n + (['th', 'st', 'nd', 'rd'][(n % 100 - 20) % 10] || ['th', 'st', 'nd', 'rd'][n % 100] || 'th');
const verifyUrl = c => `${location.origin}${location.pathname.replace(/staff\/.*$/, '')}verify/?code=${c}`;

V.results = async () => {
  const tab = St.rtab || 'term';
  const tabs = `<div class="tabs">${[['term', 'Term results'], ['tr', 'Transcripts'], ['setup', 'Terms and grades']].map(t => `<button class="g ${tab === t[0] ? 'on' : ''}" data-a="rtab" data-v="${t[0]}">${t[1]}</button>`).join('')}</div>`;
  const terms = must(await sb().from('academic_terms').select('*').eq('school_id', me().school_id).order('starts_on', { ascending: false })) || [];
  if (tab === 'setup') return tabs + setup(terms);
  if (tab === 'tr') return tabs + await transcripts();
  if (!terms.length) return tabs + `<div class="card">${empty('Add your first term', 'Results are compiled per term from the gradebook, using the term dates.', '<button class="b" data-a="rtab" data-v="setup">Add a term</button>')}</div>`;
  const term = terms.find(t => t.id === St.rterm) || terms[0], cls = (St.classes || []).find(c => c.id === St.rclass) || (St.classes || [])[0];
  St.rterm = term.id; if (!cls) return tabs + `<div class="card">${empty('No classes yet', 'Create a class first.', '<button class="g" data-go="classes">Classes</button>')}</div>`;
  St.rclass = cls.id;
  const reps = must(await sb().from('term_reports').select('*').eq('term_id', term.id).eq('class_id', cls.id)) || [];
  const ids = reps.map(r => r.student_id);
  const [res, ps] = ids.length ? await Promise.all([sb().from('term_results').select('*').eq('term_id', term.id).in('student_id', ids), sb().from('profiles').select('id,first_name,surname,admission_no').in('id', ids)]) : [{ data: [] }, { data: [] }];
  const R = res.data || [], P = {}; (ps.data || []).forEach(p => P[p.id] = p);
  const subj = [...new Set(R.map(r => r.subject))].sort(), pub = reps.filter(r => r.published_at).length;
  St.rdata = { term, cls, reps, R, P, subj };
  reps.sort((a, b) => (a.position || 999) - (b.position || 999) || String((P[a.student_id] || {}).surname).localeCompare((P[b.student_id] || {}).surname));
  const cell = (sid, sj) => { const r = R.find(x => x.student_id === sid && x.subject === sj); return r ? `${num(r.score)}${r.grade ? ` <small class="muted">${esc(r.grade)}</small>` : ''}${r.source === 'manual' ? '<sup title="Entered by hand">*</sup>' : ''}` : '<span class="muted">–</span>'; };
  return tabs + `<div class="card"><h2>Term results</h2><div class="row"><label>Term<select data-a="rterm">${terms.map(t => opt(t.id, t.name, t.id === term.id)).join('')}</select></label><label>Class<select data-a="rclass">${St.classes.map(c => opt(c.id, c.name + ' (' + c.grade + ')', c.id === cls.id)).join('')}</select></label></div>
<p class="sub">${day(term.starts_on)} to ${day(term.ends_on)}. Compiling takes every gradebook mark from those dates (weighted, or equal weights where none are set) and the register. Hand-entered results (*) are kept. Students see a report in the app once it is published.</p>
<div class="row" style="gap:8px"><button class="b" data-a="rcompile">${reps.length ? 'Recompile from gradebook' : 'Compile from gradebook'}</button>${reps.length ? `<button class="g" data-a="rpub" data-v="${pub < reps.length ? 1 : 0}">${pub < reps.length ? 'Publish to students' : 'Unpublish'}</button><button class="g" data-a="rprint">Print reports</button><button class="g" data-a="rcsv">Export CSV</button>` : ''}</div>
${reps.length ? `<p class="sub" style="margin-top:10px">${pub ? `<span class="pill ok">Published</span> ${pub} of ${reps.length} reports. Published reports are locked; unpublish to change them.` : '<span class="pill w">Draft</span> Not visible to students yet. Tap a student to edit results and comments.'}</p>` : ''}</div>
${reps.length ? `<div class="card"><h2>${esc(cls.name)}: ${esc(term.name)}</h2>${table(['Pos.', 'Student'].concat(subj, ['Average', 'Attendance']), reps.map(r => `<tr class="click" data-a="redit" data-id="${r.student_id}"><td>${r.position ? ord(r.position) : '–'}</td><td><b>${P[r.student_id] ? nm(P[r.student_id]) : ''}</b>${r.published_at ? '' : ' <small class="muted">draft</small>'}</td>${subj.map(sj => `<td class="n">${cell(r.student_id, sj)}</td>`).join('')}<td class="n"><b>${num(r.average)}</b></td><td class="n">${r.attendance_pct == null ? '–' : Math.round(r.attendance_pct) + '%'}</td></tr>`))}</div>` : `<div class="card">${empty('Nothing compiled yet', 'Enter marks in the Gradebook during the term, then compile here.', '')}</div>`}`;
};
A.rtab = el => { St.rtab = el.dataset.v; T.go(); };
A.rterm = el => { St.rterm = el.value; T.go(); };
A.rclass = el => { St.rclass = el.value; T.go(); };
A.rcompile = async () => { const k = must(await sb().rpc('compile_term', { p_term: St.rterm, p_class: St.rclass })); toast(k ? k + ' students compiled.' : 'Nothing to compile: reports are published, or the class has no current students.'); T.go(); };
A.rpub = async el => { const on = el.dataset.v === '1', k = must(await sb().rpc('publish_term', { p_term: St.rterm, p_class: St.rclass, p_publish: on })); toast(on ? k + ' reports published. Students can see them in the app.' : k + ' reports unpublished.'); T.go(); };

/* edit one student's results and comments (drafts only) */
A.redit = el => {
  const D = St.rdata, sid = el.dataset.id, r = D.reps.find(x => x.student_id === sid), p = D.P[sid] || {}, mine = D.R.filter(x => x.student_id === sid), lock = !!r.published_at;
  const d = document.createElement('div'); d.className = 'drawer';
  d.innerHTML = `<div><div class="row" style="justify-content:space-between;align-items:flex-start"><div><h2 style="margin:0">${nm(p)}</h2><p class="sub" style="margin:4px 0 0">${esc(D.cls.name)} • ${esc(D.term.name)}${r.position ? ' • ' + ord(r.position) + ' of ' + r.class_size : ''}</p></div><button class="g" type="button" data-a="closedr">Close</button></div>
${lock ? '<p class="note">Published, so locked. Unpublish the class to make changes.</p>' : ''}
<form data-f="rsave" data-id="${sid}"><h3>Results</h3><p class="sub">Scores out of 100. The grade follows your grade bands. Changing a score marks it as entered by hand, so recompiling keeps it.</p>
${D.subj.concat(mine.map(m => m.subject)).filter((v, i, a) => a.indexOf(v) === i).map(sj => { const m = mine.find(x => x.subject === sj) || {}; return `<div class="row"><label style="flex:2 1 160px">${esc(sj)}${m.source === 'manual' ? ' <small class="muted">by hand</small>' : ''}<input name="s:${esc(sj)}" type="number" min="0" max="100" step="0.01" value="${m.score == null ? '' : m.score}" data-was="${m.score == null ? '' : m.score}" ${lock ? 'disabled' : ''}></label><label style="flex:1 1 80px">Grade<input value="${esc(m.grade || '')}" disabled></label></div>`; }).join('')}
${lock ? '' : `<div class="row"><label style="flex:2 1 160px">Add a subject<input name="newsub" maxlength="80" placeholder="e.g. Civic Education"></label><label style="flex:1 1 80px">Score<input name="newscore" type="number" min="0" max="100" step="0.01"></label></div>`}
<h3 style="margin-top:14px">Comments</h3><label>Class teacher<textarea name="teacher_comment" maxlength="1000" ${lock ? 'disabled' : ''}>${esc(r.teacher_comment || '')}</textarea></label><label>Head of school<textarea name="head_comment" maxlength="1000" ${lock ? 'disabled' : ''}>${esc(r.head_comment || '')}</textarea></label>
${lock ? '' : '<button class="b">Save</button>'}</form></div>`;
  document.body.appendChild(d);
};
F.rsave = async (d, f) => {
  const D = St.rdata, sid = f.dataset.id, rows = [];
  f.querySelectorAll('input[name^="s:"]').forEach(i => { if (i.value !== i.dataset.was && i.value !== '') rows.push({ subject: i.name.slice(2), score: Math.min(100, Math.max(0, +i.value)) }); });
  if (d.newsub && d.newscore !== '') rows.push({ subject: d.newsub.trim(), score: Math.min(100, Math.max(0, +d.newscore)) });
  if (rows.length) must(await sb().from('term_results').upsert(rows.map(x => ({ school_id: me().school_id, term_id: D.term.id, student_id: sid, subject: x.subject, score: x.score, source: 'manual', updated_by: me().id })), { onConflict: 'term_id,student_id,subject' }));
  must(await sb().from('term_reports').update({ teacher_comment: d.teacher_comment || null, head_comment: d.head_comment || null }).eq('term_id', D.term.id).eq('student_id', sid));
  if (rows.length) must(await sb().rpc('rank_term', { p_term: D.term.id, p_class: D.cls.id }));
  const dr = document.querySelector('.drawer'); if (dr) dr.remove(); toast('Saved.'); T.go();
};
A.rcsv = () => { const D = St.rdata; if (!D) return; saveCsv('results-' + D.cls.name + '-' + D.term.name + '.csv', csv([['Admission no.', 'Student', 'Position'].concat(D.subj, ['Average', 'Attendance %'])].concat(D.reps.map(r => { const p = D.P[r.student_id] || {}; return [p.admission_no, p.first_name + ' ' + p.surname, r.position].concat(D.subj.map(sj => { const x = D.R.find(y => y.student_id === r.student_id && y.subject === sj); return x ? x.score : ''; }), [r.average, r.attendance_pct]); })))); };
A.rprint = () => {
  const D = St.rdata; if (!D || !H.printDoc) return;
  H.printDoc(D.reps.map((r, i) => { const p = D.P[r.student_id] || {}, mine = D.R.filter(x => x.student_id === r.student_id).sort((a, b) => a.subject.localeCompare(b.subject));
    return `<div class="${i < D.reps.length - 1 ? 'pb' : ''}">${H.printHead('Term report: ' + D.term.name, esc(p.first_name + ' ' + p.surname) + (p.admission_no ? '<br>' + esc(p.admission_no) : ''))}
<p>Class ${esc(r.class_name || D.cls.name)}${r.position ? ` • Position ${ord(r.position)} of ${r.class_size}` : ''} • Average ${num(r.average)}${r.attendance_pct != null ? ' • Attendance ' + Math.round(r.attendance_pct) + '%' : ''}</p>
<table><tr><th>Subject</th><th class="n">Score</th><th class="n">Grade</th></tr>${mine.map(x => `<tr><td>${esc(x.subject)}</td><td class="n">${num(x.score)}</td><td class="n">${esc(x.grade || '')}</td></tr>`).join('')}</table>
${r.teacher_comment ? `<p><b>Class teacher:</b> ${esc(r.teacher_comment)}</p>` : ''}${r.head_comment ? `<p><b>Head of school:</b> ${esc(r.head_comment)}</p>` : ''}<p style="margin-top:36px">Signed ____________________ &nbsp; Date ______________</p></div>`; }).join(''));
};

/* ---------- terms and grade bands ---------- */
function setup(terms) {
  const b = (T.school || {}).grade_bands || BANDS;
  return `<div class="card"><h2>Terms</h2><p class="sub">Name each term and give its dates. Results use gradebook marks dated inside the term.</p>
${terms.length ? table(['Term', 'From', 'To', ''], terms.map(t => `<tr><td><b>${esc(t.name)}</b></td><td>${day(t.starts_on)}</td><td>${day(t.ends_on)}</td><td><button class="g" data-a="rtdel" data-id="${t.id}">Delete</button></td></tr>`)) : ''}
<form data-f="rterm" class="row" style="margin-top:12px"><label>Name<input name="name" required maxlength="40" placeholder="Term 1 2026/27"></label><label>From<input name="starts_on" type="date" required></label><label>To<input name="ends_on" type="date" required></label><button class="b">Add term</button></form></div>
<div class="card"><h2>Grade bands</h2><p class="sub">Highest first: a grade and the lowest score that earns it. For example WAEC style: A1 75, B2 70, B3 65, C4 60, C5 55, C6 50, D7 45, E8 40, F9 0.</p>
<form data-f="rbands"><label>Bands<input name="bands" maxlength="300" value="${esc(b.map(x => x.grade + ' ' + x.min).join(', '))}"></label><button class="b">Save bands</button> <button class="g" type="button" data-a="rbreset">Use A to F</button></form></div>`;
}
F.rterm = async d => { if (d.ends_on < d.starts_on) throw new Error('The term ends before it starts.'); must(await sb().from('academic_terms').insert({ school_id: me().school_id, name: d.name.trim(), starts_on: d.starts_on, ends_on: d.ends_on })); toast('Term added.'); T.go(); };
A.rtdel = async el => { const n = must(await sb().from('term_reports').select('id').eq('term_id', el.dataset.id).limit(1)) || []; if (n.length) return toast('This term has results. Delete is only for terms with none.', true); must(await sb().from('academic_terms').delete().eq('id', el.dataset.id)); toast('Deleted.'); T.go(); };
const parseBands = s => { const out = String(s).split(',').map(x => x.trim()).filter(Boolean).map(x => { const m = x.match(/^(\S{1,8})\s+(\d+(?:\.\d+)?)$/); if (!m) throw new Error('Write each band as a grade and a number, for example "A 80".'); return { grade: m[1], min: +m[2] }; });
  if (out.length < 2) throw new Error('Give at least two bands.'); for (let i = 1; i < out.length; i++) if (out[i].min >= out[i - 1].min) throw new Error('List the bands from highest to lowest.');
  if (out[out.length - 1].min !== 0) throw new Error('The lowest band must start at 0.'); return out; };
H.parseBands = parseBands;
F.rbands = async d => { const b = parseBands(d.bands); must(await sb().from('schools').update({ grade_bands: b }).eq('id', me().school_id)); T.school.grade_bands = b; toast('Saved. Recompile a term to apply them.'); T.go(); };
A.rbreset = async () => { must(await sb().from('schools').update({ grade_bands: null }).eq('id', me().school_id)); T.school.grade_bands = null; toast('Back to A to F.'); T.go(); };

/* ---------- transcripts ---------- */
async function transcripts() {
  const tr = must(await sb().from('transcripts').select('id,student_id,status,purpose,code,requested_at,decided_at,decline_reason,revoked_at').eq('school_id', me().school_id).order('requested_at', { ascending: false }).limit(500)) || [];
  const st = must(await sb().from('profiles').select('id,first_name,surname,admission_no').eq('school_id', me().school_id).eq('role', 'student').order('surname')) || [], P = {}; st.forEach(p => P[p.id] = p);
  const req = tr.filter(t => t.status === 'requested'), done = tr.filter(t => t.status !== 'requested');
  const who = t => P[t.student_id] ? nm(P[t.student_id]) : 'Former student';
  return `<div class="card"><h2>Requests (${req.length})</h2>${req.length ? `<div class="lst">${req.map(t => `<div class="it"><div class="m"><b>${who(t)}</b><small>${day(t.requested_at)}${t.purpose ? ' • ' + esc(t.purpose) : ''}</small></div><button class="b" data-a="trissue" data-id="${t.student_id}">Issue</button><button class="g" data-a="trdecline" data-id="${t.id}">Decline</button></div>`).join('')}</div>` : '<p class="muted">No requests waiting. Students ask for a transcript in the app once their results are published.</p>'}<div id="trdc"></div></div>
<div class="card"><h2>Issue a transcript</h2><p class="sub">Uses every published term report of the student. Each transcript gets a code that anyone can check at Ace's verify page.</p><form data-f="trnew" class="row"><label>Student<select name="sid">${st.map(p => opt(p.id, p.first_name + ' ' + p.surname + (p.admission_no ? ' (' + p.admission_no + ')' : ''))).join('')}</select></label><label>Purpose (optional)<input name="purpose" maxlength="200" placeholder="University application"></label><button class="b">Issue</button></form></div>
<div class="card"><h2>Issued and declined</h2>${table(['Student', 'Date', 'Code', 'Status', ''], done.map(t => `<tr><td>${who(t)}${t.purpose ? `<br><small class="muted">${esc(t.purpose)}</small>` : ''}</td><td>${day(t.decided_at)}</td><td>${t.code ? `<code>${esc(t.code)}</code>` : ''}</td><td>${t.status === 'declined' ? `<span class="pill bad">Declined</span>${t.decline_reason ? `<br><small>${esc(t.decline_reason)}</small>` : ''}` : t.revoked_at ? '<span class="pill bad">Withdrawn</span>' : '<span class="pill ok">Valid</span>'}</td><td>${t.status === 'issued' && !t.revoked_at ? `<button class="g" data-a="trprint" data-id="${t.id}">Print</button> <button class="g" data-a="trrevoke" data-id="${t.id}">Withdraw</button>` : ''}</td></tr>`), 'None yet.')}</div>`;
}
const issue = async (sid, purpose) => { const t = must(await sb().rpc('issue_transcript', { p_student: sid, p_purpose: purpose || null })); toast('Transcript ' + t.code + ' issued.'); T.go(); };
A.trissue = el => issue(el.dataset.id);
F.trnew = d => issue(d.sid, d.purpose);
A.trdecline = el => { document.getElementById('trdc').innerHTML = `<form data-f="trdeclineok" data-id="${el.dataset.id}" style="margin-top:12px"><label>Reason (the student sees it)<input name="reason" maxlength="300" required placeholder="Fees must be cleared first"></label><button class="b">Decline request</button></form>`; };
F.trdeclineok = async (d, f) => { must(await sb().rpc('decide_transcript', { p_id: f.dataset.id, p_action: 'decline', p_reason: d.reason })); toast('Declined.'); T.go(); };
A.trrevoke = async el => { if (el.dataset.sure !== '1') { el.dataset.sure = '1'; el.textContent = 'Tap again to withdraw'; return; } must(await sb().rpc('decide_transcript', { p_id: el.dataset.id, p_action: 'revoke' })); toast('Withdrawn. The code now shows as no longer valid.'); T.go(); };
A.trprint = async (el, quiet) => {
  const t = must(await sb().from('transcripts').select('code,snapshot,decided_at').eq('id', el.dataset.id).maybeSingle()); if (!t || !t.snapshot || !H.printDoc) return;
  if (quiet === true) return; const s = t.snapshot;
  H.printDoc(H.printHead('Academic transcript', esc(s.name) + (s.admission_no ? '<br>' + esc(s.admission_no) : '')) +
    `<p>${s.date_of_birth ? 'Born ' + day(s.date_of_birth) + ' • ' : ''}${s.admitted_on ? 'Admitted ' + day(s.admitted_on) + ' • ' : ''}${s.left_on ? 'Left ' + day(s.left_on) + ' • ' : ''}Issued ${day(t.decided_at)}</p>` +
    (s.terms || []).map(x => `<h3 style="margin:14px 0 4px">${esc(x.term)}${x.class ? ' • ' + esc(x.class) : ''}</h3><table><tr><th>Subject</th><th class="n">Score</th><th class="n">Grade</th></tr>${(x.results || []).map(r => `<tr><td>${esc(r.subject)}</td><td class="n">${num(r.score)}</td><td class="n">${esc(r.grade || '')}</td></tr>`).join('')}</table><p>Average ${num(x.average)}${x.position ? ' • position ' + ord(x.position) + ' of ' + x.class_size : ''}${x.attendance_pct != null ? ' • attendance ' + Math.round(x.attendance_pct) + '%' : ''}</p>`).join('') +
    `<p style="margin-top:24px;border:1px solid #999;padding:8px">Verification code <b>${esc(t.code)}</b>. Check this transcript at ${esc(verifyUrl(t.code))}</p><p style="margin-top:30px">Signed ____________________ (Head of school) &nbsp; School stamp</p>`);
};
})();
