/* Ace Teach: student records for school admins. Admission numbers, enrolment status with history, and a record
   card per student (details, guardians, application, attendance and fees at a glance). Status changes go through
   set_enrolment_status() so they are logged; leavers drop out of their classes but their record stays. */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, must, toast, csv, saveCsv, isAdmin, isTutor, isPlat, nm, pct } = H;
const sb = () => T.sb, me = () => T.me;
const opt = (v, l, sel) => `<option value="${esc(v)}" ${sel ? 'selected' : ''}>${esc(l == null ? v : l)}</option>`;
const STATUS = { active: ['Active', 'ok'], suspended: ['Suspended', 'w'], withdrawn: ['Withdrawn', 'bad'], transferred: ['Transferred', 'bad'], graduated: ['Graduated', ''] };
const LEAVING = ['withdrawn', 'transferred', 'graduated'];
const day = d => d ? new Date(String(d).length === 10 ? d + 'T00:00:00' : d).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' }) : '';
H.stuPill = s => { const x = STATUS[s || 'active'] || [s, '']; return `<span class="pill ${x[1]}">${esc(x[0])}</span>`; };
const closeDr = () => { const d = document.querySelector('.drawer'); if (d) d.remove(); };

/* ---------- the record card (a drawer over People) ---------- */
A.strec = async el => {
  const id = el.dataset.id || St.recid; St.recid = id;
  const p = must(await sb().from('profiles').select('id,first_name,surname,username,student_number,admission_no,enrolment_status,status_changed_at,class_id,contact_email,last_seen_at,created_at,exam_target').eq('id', id).maybeSingle());
  if (!p) return toast('Student not found.', true);
  St.bnames = Object.assign(St.bnames || {}, { [p.id]: p });
  const [rec, ev, gu, app, att, fees, beh] = await Promise.all([
    sb().from('student_records').select('*').eq('student_id', id).maybeSingle(),
    sb().from('enrolment_events').select('*').eq('student_id', id).order('created_at', { ascending: false }),
    sb().from('guardians').select('name,email,digest_opt_in,consent_at').eq('student_id', id),
    sb().from('applications').select('reference,created_at,guardian_name,guardian_phone').eq('student_id', id).maybeSingle(),
    sb().from('attendance').select('status').eq('student_id', id).gte('day', new Date(Date.now() - 90 * 864e5).toISOString().slice(0, 10)),
    sb().from('fees').select('term,amount,paid,currency_code').eq('student_id', id).order('term'),
    sb().from('behaviour_entries').select('*').eq('student_id', id).order('occurred_on', { ascending: false }).limit(15)
  ]);
  const r = rec.data || {}, C = {}; (St.classes || []).forEach(c => C[c.id] = c);
  const A3 = (att.data || []).filter(a => a.status !== 'excused'), present = A3.filter(a => a.status === 'present' || a.status === 'late').length;
  const F3 = fees.data || [], owed = F3.reduce((s, f) => s + Math.max(0, +f.amount - +f.paid), 0), cur = (F3[0] || {}).currency_code || '';
  const st = p.enrolment_status || 'active', who = {};
  const actors = [...new Set((ev.data || []).map(e => e.actor).filter(Boolean))];
  if (actors.length) (must(await sb().from('profiles').select('id,first_name,surname').in('id', actors)) || []).forEach(x => who[x.id] = x.first_name + ' ' + x.surname);
  const age = r.date_of_birth ? Math.floor((Date.now() - new Date(r.date_of_birth + 'T00:00:00').getTime()) / (365.2425 * 864e5)) : null;
  const kv = (k, v) => `<div><small class="muted">${k}</small><div><b>${v || '–'}</b></div></div>`;
  closeDr();
  const d = document.createElement('div'); d.className = 'drawer';
  d.innerHTML = `<div><div class="row" style="justify-content:space-between;align-items:flex-start"><div><h2 style="margin:0">${nm(p)}</h2><p class="sub" style="margin:4px 0 0">${H.stuPill(st)}${p.status_changed_at ? ` <small class="muted">since ${day(p.status_changed_at)}</small>` : ''}</p></div><button class="g" type="button" data-a="closedr">Close</button></div>
<div class="grid g2" style="gap:12px;margin:16px 0">${kv('Admission no.', esc(p.admission_no))}${kv('Class', esc((C[p.class_id] || {}).name || ''))}${kv('Ace username', esc(p.username))}${kv('Ace student no.', esc(p.student_number))}${kv('Attendance, last 90 days', A3.length ? pct(100 * present / A3.length) + ` <small class="muted">(${A3.length} days)</small>` : '')}${kv('Fees owed', F3.length ? (owed ? `<span style="color:var(--red)">${esc(cur)} ${owed.toLocaleString()}</span>` : 'Nothing owed') : '')}</div>
${app.data ? `<p class="note">Joined through an online application, ${esc(app.data.reference)} (${day(app.data.created_at)}).</p>` : ''}
<h3>Details</h3><form data-f="strec" data-id="${p.id}"><div class="row"><label>Date of birth<input name="date_of_birth" type="date" value="${esc(r.date_of_birth || '')}"></label><label>Gender<input name="gender" maxlength="30" value="${esc(r.gender || '')}"></label></div>
<div class="row"><label>Phone<input name="phone" maxlength="30" value="${esc(r.phone || '')}"></label><label>Admitted on<input name="admitted_on" type="date" value="${esc(r.admitted_on || '')}"></label></div>
<label>Address<input name="address" maxlength="300" value="${esc(r.address || '')}"></label><label>Previous school<input name="previous_school" maxlength="120" value="${esc(r.previous_school || '')}"></label>
<label>Notes (school admins and the student's teachers can read these)<textarea name="notes" maxlength="2000">${esc(r.notes || '')}</textarea></label>
${age != null ? `<p class="muted" style="margin:0 0 8px">Age ${age}.</p>` : ''}<button class="b">Save details</button></form>
<h3 style="margin-top:20px">Admission number</h3><form data-f="stadm" data-id="${p.id}" class="row"><label>Number<input name="no" maxlength="30" value="${esc(p.admission_no || '')}" style="text-transform:uppercase"></label><button class="g">Save number</button></form>
<h3 style="margin-top:20px">Status</h3><form data-f="ststatus" data-id="${p.id}"><div class="row"><label>Change to<select name="status">${Object.keys(STATUS).filter(k => k !== st).map(k => opt(k, STATUS[k][0])).join('')}</select></label><label>From<input name="effective" type="date" value="${new Date().toISOString().slice(0, 10)}"></label></div>
<label>Reason<input name="reason" maxlength="300" placeholder="e.g. Moved to another town; finished Form 4"></label><p class="sub">Withdrawn, transferred and graduated students leave their classes and stop using a seat; their record, marks and history stay. You can make them active again.</p><button class="b">Change status</button></form>
${r.left_on ? `<p class="muted">Left on ${day(r.left_on)}${r.leaving_reason ? ': ' + esc(r.leaving_reason) : ''}.</p>` : ''}
<h3 style="margin-top:20px">Guardians</h3>${(gu.data || []).length ? `<div class="lst">${gu.data.map(g => `<div class="it"><div class="m"><b>${esc(g.name || g.email)}</b><small>${esc(g.email)}${g.digest_opt_in && g.consent_at ? ' • weekly email on' : ''}</small></div></div>`).join('')}</div>` : `<p class="muted">None yet${app.data && app.data.guardian_phone ? `. From the application: ${esc(app.data.guardian_name || '')} ${esc(app.data.guardian_phone)}` : ''}. Add them in Parents.</p>`}
<h3 style="margin-top:20px">Behaviour and welfare</h3>${(beh.data || []).length && H.behaviourEntry ? `<div class="lst">${beh.data.map(e => H.behaviourEntry(e, {})).join('')}</div>` : '<p class="muted">Nothing recorded.</p>'}<p><button class="g" type="button" data-a="bnew" data-id="${p.id}" data-k="welfare">Add a welfare note</button></p>
<h3 style="margin-top:20px">History</h3><div class="lst">${(ev.data || []).map(e => `<div class="it"><div class="m"><b>${esc((STATUS[e.from_status] || [e.from_status || ''])[0])} → ${esc((STATUS[e.to_status] || [e.to_status])[0])}</b><small>${day(e.effective_on)} • ${esc(who[e.actor] || 'Staff')}${e.reason ? ' • ' + esc(e.reason) : ''}</small></div></div>`).join('') || `<p class="muted">On Ace since ${day(p.created_at)}. No status changes yet.</p>`}</div></div>`;
  document.body.appendChild(d);
};
F.strec = async (d, f) => {
  const row = { student_id: f.dataset.id, school_id: me().school_id, updated_by: me().id, updated_at: new Date().toISOString() };
  ['date_of_birth', 'gender', 'phone', 'admitted_on', 'address', 'previous_school', 'notes'].forEach(k => row[k] = d[k] || null);
  must(await sb().from('student_records').upsert(row, { onConflict: 'student_id' })); toast('Details saved.');
};
F.stadm = async (d, f) => { const n = must(await sb().rpc('set_admission_no', { p_student: f.dataset.id, p_no: d.no })); toast(n ? 'Admission number set to ' + n + '.' : 'Admission number removed.'); A.strec({ dataset: { id: f.dataset.id } }); T.go(); };
F.ststatus = async (d, f) => {
  const s = must(await sb().rpc('set_enrolment_status', { p_student: f.dataset.id, p_status: d.status, p_reason: d.reason || null, p_effective: d.effective || null }));
  if (T.fresh) T.fresh(); toast('Status changed to ' + STATUS[s][0].toLowerCase() + '.'); await T.go(); A.strec({ dataset: { id: f.dataset.id } });
};
A.csvstu = async () => {
  const p = must(await sb().from('profiles').select('id,first_name,surname,admission_no,student_number,username,class_id,enrolment_status,created_at').eq('school_id', me().school_id).eq('role', 'student').order('surname')) || [];
  const r = must(await sb().from('student_records').select('student_id,date_of_birth,gender,phone,address,admitted_on,left_on,leaving_reason').eq('school_id', me().school_id)) || [], R = {}, C = {};
  r.forEach(x => R[x.student_id] = x); (St.classes || []).forEach(c => C[c.id] = c);
  saveCsv('students.csv', csv([['Admission no.', 'First name', 'Surname', 'Class', 'Status', 'Date of birth', 'Gender', 'Phone', 'Address', 'Admitted on', 'Left on', 'Leaving reason', 'Ace username', 'Ace student no.']].concat(p.map(x => { const y = R[x.id] || {}; return [x.admission_no, x.first_name, x.surname, (C[x.class_id] || {}).name || '', (STATUS[x.enrolment_status] || [x.enrolment_status])[0], y.date_of_birth, y.gender, y.phone, y.address, y.admitted_on, y.left_on, y.leaving_reason, x.username, x.student_number]; }))));
};

/* ---------- admission numbering (Settings) ---------- */
const settings0 = V.settings;
V.settings = async () => {
  const h = await settings0(), s = T.school;
  if (!isAdmin() || isTutor() || !s) return h;
  const ex = s.admission_prefix ? s.admission_prefix + (s.admission_year ? '-' + new Date().getFullYear() : '') + '-' + String((s.admission_seq || 0) + 1).padStart(s.admission_digits || 4, '0') : '';
  return h + `<div class="card"><h2>Admission numbers</h2><p class="sub">Every new student gets the next number automatically, including students enrolled from Admissions.${ex ? ` The next one is <b>${esc(ex)}</b>.` : ' Set a prefix to start.'}</p>
<form data-f="admset"><div class="row"><label>Prefix (letters and digits)<input name="admission_prefix" maxlength="10" value="${esc(s.admission_prefix || '')}" placeholder="GRF" style="text-transform:uppercase"></label><label>Next number<input name="next" type="number" min="1" value="${(s.admission_seq || 0) + 1}"></label><label>Digits<select name="admission_digits">${[3, 4, 5, 6].map(n => opt(n, n, n === (s.admission_digits || 4))).join('')}</select></label></div>
<label style="flex-direction:row;align-items:center;gap:8px"><input type="checkbox" name="admission_year" ${s.admission_year !== false ? 'checked' : ''} style="width:auto;margin:0"> Include the year (GRF-${new Date().getFullYear()}-0001)</label><button class="b">Save</button> <button class="g" type="button" data-a="numberall">Number students who have none</button></form></div>`;
};
F.admset = async d => {
  const pre = String(d.admission_prefix || '').toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 10) || null, next = Math.max(1, parseInt(d.next, 10) || 1);
  const row = { admission_prefix: pre, admission_seq: next - 1, admission_digits: +d.admission_digits || 4, admission_year: !!d.admission_year };
  must(await sb().from('schools').update(row).eq('id', me().school_id)); Object.assign(T.school, row); toast('Saved.'); T.go();
};
A.numberall = async () => { const n = must(await sb().rpc('number_students', { p_school: me().school_id })); const s = must(await sb().from('schools').select('admission_seq').eq('id', me().school_id).single()); T.school.admission_seq = s.admission_seq; toast(n ? n + ' students numbered.' : 'Every student already has a number.'); T.go(); };
})();
