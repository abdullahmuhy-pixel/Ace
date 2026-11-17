/* Ace Teach: Admissions. Families apply on /apply/ without an account; school admins review, decide and enrol here.
   Reads go through RLS (applications, application_documents, application_events); every change goes through the
   admissions-manage edge function so it is logged and the family can be emailed. */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, must, fn, toast, csv, saveCsv, empty, isAdmin, isPlat } = H;
const sb = () => T.sb, me = () => T.me;
const opt = (v, l, sel) => `<option value="${esc(v)}" ${sel ? 'selected' : ''}>${esc(l == null ? v : l)}</option>`;
const STAGES = [['submitted', 'New', ''], ['reviewing', 'Reviewing', 'w'], ['interview', 'Interview', 'w'], ['waitlisted', 'Waiting list', 'w'], ['accepted', 'Accepted', 'ok'], ['enrolled', 'Enrolled', 'ok'], ['declined', 'Declined', 'bad'], ['withdrawn', 'Withdrawn', 'bad']];
const LBL = {}, PILL = {}; STAGES.forEach(s => { LBL[s[0]] = s[1]; PILL[s[0]] = s[2]; });
const NEXT = { submitted: ['reviewing', 'interview', 'waitlisted', 'accepted', 'declined'], reviewing: ['interview', 'waitlisted', 'accepted', 'declined'], interview: ['reviewing', 'waitlisted', 'accepted', 'declined'], waitlisted: ['reviewing', 'interview', 'accepted', 'declined'], accepted: ['waitlisted', 'declined'], declined: ['reviewing'], withdrawn: [], enrolled: [] };
const MSG = { interview: 'We would like to meet the applicant. Please come to the school on [day] at [time] and bring the original documents.', waitlisted: 'The class is full at the moment. We have put the application on our waiting list and will contact you if a place opens.', accepted: 'We are pleased to offer a place. We will contact you about fees and the first day.', declined: 'Thank you for applying. We are not able to offer a place this time.' };
const day = d => d ? new Date(d).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' }) : '';
const pill = s => `<span class="pill ${PILL[s] || ''}">${esc(LBL[s] || s)}</span>`;
const applyLink = () => `${location.origin}${location.pathname.replace(/staff\/.*$/, '')}apply/?s=${encodeURIComponent((T.school || {}).school_code || '')}`;
const list = s => String(s || '').split(/[\n,]/).map(x => x.trim()).filter(Boolean);

V.admissions = async () => {
  if (!isAdmin() && !isPlat()) return `<div class="card">${empty('For school admins', 'Ask your school admin to give you access.')}</div>`;
  if (St.appid) return detail(St.appid);
  const s = T.school || {};
  const apps = must(await sb().from('applications').select('id,reference,first_name,surname,grade_applied,start_term,status,created_at,updated_at,guardian_name,guardian_phone,guardian_email,applicant_email').eq('school_id', me().school_id).order('created_at', { ascending: false }).limit(1000)) || [];
  const docs = apps.length ? must(await sb().from('application_documents').select('application_id,uploaded_at').in('application_id', apps.map(a => a.id))) || [] : [];
  const D = {}; docs.forEach(d => { const x = D[d.application_id] = D[d.application_id] || [0, 0]; x[0]++; if (d.uploaded_at) x[1]++; });
  const n = {}; apps.forEach(a => n[a.status] = (n[a.status] || 0) + 1);
  const f = St.afilt || (n.submitted ? 'submitted' : 'open');
  const open = a => !['enrolled', 'declined', 'withdrawn'].includes(a.status);
  const show = apps.filter(a => f === 'all' ? true : f === 'open' ? open(a) : a.status === f);
  const tab = (k, l, c) => `<button class="g ${f === k ? 'on' : ''}" data-a="afilt" data-v="${k}">${esc(l)}${c != null ? ` <b>${c}</b>` : ''}</button>`;
  const kpi = (v, l, c) => `<div class="kpi ${c}"><b>${v}</b><span>${l}</span></div>`;
  const decided = apps.filter(a => ['accepted', 'enrolled', 'declined'].includes(a.status)).length;
  return `${s.admissions_open ? '' : `<div class="note">Online applications are <b>closed</b>. Open them in the settings below when you are ready to share the link.</div>`}
<div class="kpis">${kpi(apps.filter(open).length, 'Open applications', 'p')}${kpi(n.submitted || 0, 'New, not yet looked at', n.submitted ? 'a' : '')}${kpi((n.accepted || 0), 'Accepted, to enrol', 'g')}${kpi(n.enrolled || 0, 'Enrolled', 'g')}${kpi(decided ? Math.round(100 * ((n.accepted || 0) + (n.enrolled || 0)) / decided) + '%' : '–', 'Offer rate', '')}</div>
<div class="card"><h2>Applications<span class="sp row" style="gap:6px"><input data-filter="#alist tbody tr" placeholder="Search" style="width:170px;margin:0"><button class="g" data-a="acsv">Export CSV</button></span></h2>
<div class="tabs">${tab('open', 'All open', apps.filter(open).length)}${STAGES.map(x => tab(x[0], x[1], n[x[0]] || 0)).join('')}${tab('all', 'Everything', apps.length)}</div>
<div id="alist">${table(['Applicant', 'Class', 'Contact', 'Sent', 'Docs', 'Status'], show.map(a => { const d = D[a.id]; return `<tr class="click" data-a="aopen" data-id="${a.id}"><td><b>${esc(a.first_name + ' ' + a.surname)}</b><br><small class="muted">${esc(a.reference)}</small></td><td>${esc(a.grade_applied)}${a.start_term ? `<br><small class="muted">${esc(a.start_term)}</small>` : ''}</td><td><small>${esc(a.guardian_name || '')}<br>${esc(a.guardian_phone || a.guardian_email || a.applicant_email || '')}</small></td><td>${day(a.created_at)}</td><td>${d ? `<span class="pill ${d[1] === d[0] ? 'ok' : 'w'}">${d[1]}/${d[0]}</span>` : '<span class="muted">none</span>'}</td><td>${pill(a.status)}</td></tr>`; }), f === 'submitted' ? 'No new applications. Share your application link to receive some.' : 'Nothing in this list.')}</div></div>
${settings(s)}`;
};

function settings(s) {
  return `<div class="card"><h2>Online applications<span class="sp"><span class="pill ${s.admissions_open ? 'ok' : 'bad'}">${s.admissions_open ? 'Open' : 'Closed'}</span></span></h2>
<p class="sub">Families fill in a form at your link, attach documents and get a reference to track their application. You decide here; nothing is shared with other schools.</p>
<div class="row" style="gap:8px;align-items:center;margin-bottom:12px"><code style="flex:1 1 260px;min-width:0;overflow-wrap:anywhere;background:var(--tint);padding:9px 12px;border-radius:10px">${esc(applyLink())}</code><button class="g" data-a="acopy">Copy link</button><a class="g" style="text-decoration:none" href="${esc(applyLink())}" target="_blank" rel="noopener">Open form ↗</a></div>
<form data-f="aset"><label style="flex-direction:row;align-items:center;gap:8px"><input type="checkbox" name="admissions_open" ${s.admissions_open ? 'checked' : ''} style="width:auto;margin:0"> Take applications online</label>
<label>Message on the form (dates, fees, what happens next)<textarea name="admissions_note" maxlength="800">${esc(s.admissions_note || '')}</textarea></label>
<div class="row"><label>Classes families can apply for (comma separated; empty = your class levels)<input name="admissions_grades" maxlength="400" value="${esc((s.admissions_grades || []).join(', '))}" placeholder="JSS1, SS1"></label>
<label>Documents to attach (comma separated, up to 5)<input name="admissions_docs" maxlength="400" value="${esc((s.admissions_docs || []).join(', '))}" placeholder="Birth certificate, Latest report card"></label></div>
<label>Also email new applications to (optional)<input name="admissions_email" type="email" maxlength="120" value="${esc(s.admissions_email || '')}"></label>
<button class="b">Save</button></form></div>`;
}
F.aset = async d => {
  const row = { admissions_open: !!d.admissions_open, admissions_note: d.admissions_note || null, admissions_grades: list(d.admissions_grades).slice(0, 30).map(x => x.slice(0, 40)),
    admissions_docs: list(d.admissions_docs).slice(0, 5).map(x => x.slice(0, 60)), admissions_email: d.admissions_email || null };
  must(await sb().from('schools').update(row).eq('id', me().school_id)); Object.assign(T.school, row);
  toast(row.admissions_open ? 'Saved. Your form is open.' : 'Saved. Your form is closed.'); T.go();
};
A.acopy = () => { const t = applyLink(); try { navigator.clipboard.writeText(t).then(() => toast('Link copied.'), () => toast(t)); } catch (e) { toast(t); } };
A.afilt = el => { St.afilt = el.dataset.v; T.go(); };
A.aopen = el => { St.appid = el.dataset.id; St.cred = null; window.scrollTo(0, 0); T.go(); };
A.aback = () => { St.appid = ''; St.cred = null; T.go(); };
A.acsv = async () => {
  const r = must(await sb().from('applications').select('reference,status,first_name,surname,date_of_birth,gender,grade_applied,start_term,previous_school,guardian_name,guardian_relation,guardian_email,guardian_phone,applicant_email,applicant_phone,created_at,updated_at').eq('school_id', me().school_id).order('created_at')) || [];
  const k = ['reference', 'status', 'first_name', 'surname', 'date_of_birth', 'gender', 'grade_applied', 'start_term', 'previous_school', 'guardian_name', 'guardian_relation', 'guardian_email', 'guardian_phone', 'applicant_email', 'applicant_phone', 'created_at', 'updated_at'];
  saveCsv('applications.csv', csv([k].concat(r.map(x => k.map(c => c === 'status' ? LBL[x.status] || x.status : x[c])))));
};

async function detail(id) {
  const a = must(await sb().from('applications').select('*').eq('id', id).maybeSingle());
  if (!a) { St.appid = ''; return `<div class="card">${empty('Application not found', '', '<button class="g" data-a="aback">Back to applications</button>')}</div>`; }
  const docs = must(await sb().from('application_documents').select('id,kind,file_name,size_bytes,uploaded_at').eq('application_id', id).order('created_at')) || [];
  const ev = must(await sb().from('application_events').select('*').eq('application_id', id).order('created_at', { ascending: false })) || [];
  const ids = [...new Set(ev.map(e => e.actor).filter(Boolean))], who = {};
  if (ids.length) (must(await sb().from('profiles').select('id,first_name,surname').in('id', ids)) || []).forEach(p => who[p.id] = p.first_name + ' ' + p.surname);
  const kv = (k, v) => v ? `<div><small class="muted">${k}</small><div>${esc(v)}</div></div>` : '';
  const age = a.date_of_birth ? Math.floor((Date.now() - new Date(a.date_of_birth + 'T00:00:00').getTime()) / (365.2425 * 864e5)) : null;
  const next = NEXT[a.status] || [];
  const best = (T.St.classes || []).find(c => String(c.grade).toLowerCase() === String(a.grade_applied).toLowerCase());
  let h = `<div class="row" style="margin-bottom:12px"><button class="g" data-a="aback">← All applications</button></div>
<div class="card"><h2>${esc(a.first_name + ' ' + a.surname)}<span class="sp">${pill(a.status)}</span></h2><p class="sub">${esc(a.reference)} • applied ${day(a.created_at)} for ${esc(a.grade_applied)}${a.start_term ? ', starting ' + esc(a.start_term) : ''}</p>
<div class="grid g3" style="gap:12px">${kv('Date of birth', a.date_of_birth ? day(a.date_of_birth) + (age != null ? ` (age ${age})` : '') : '')}${kv('Gender', a.gender)}${kv('Previous school', a.previous_school)}${kv('Exam target', a.exam_target)}${kv('Student email', a.applicant_email)}${kv('Student phone', a.applicant_phone)}</div>
<h3 style="margin:16px 0 8px">Parent or guardian</h3><div class="grid g3" style="gap:12px">${kv('Name', a.guardian_name)}${kv('Relationship', a.guardian_relation)}${kv('Email', a.guardian_email)}${kv('Phone', a.guardian_phone)}${kv('Address', a.address)}</div>
${a.message ? `<h3 style="margin:16px 0 6px">From the family</h3><p style="white-space:pre-wrap;margin:0">${esc(a.message)}</p>` : ''}</div>
<div class="grid g2"><div class="card"><h2>Documents (${docs.length})</h2>${docs.length ? `<div class="lst">${docs.map(d => `<div class="it"><div class="m"><b>${esc(d.kind)}</b><small>${esc(d.file_name)} • ${Math.max(1, Math.round(d.size_bytes / 1024))} KB</small></div>${d.uploaded_at ? `<button class="g" data-a="adoc" data-id="${d.id}">Open</button>` : '<span class="pill bad">Not received</span>'}</div>`).join('')}</div>` : '<p class="muted">No documents attached.</p>'}</div>
<div class="card"><h2>Internal note</h2><p class="sub">Only school admins see this.</p><form data-f="anote" data-id="${a.id}"><textarea name="note" maxlength="2000" placeholder="Interview notes, sibling at the school, fees discussed…">${esc(a.staff_note || '')}</textarea><button class="b">Save note</button></form></div></div>`;
  if (next.length) h += `<div class="card"><h2>Decide</h2><form data-f="astatus" data-id="${a.id}"><div class="row"><label>Move to<select name="status" data-a="amsg">${next.map(s => opt(s, LBL[s])).join('')}</select></label></div>
<label>Message to the family (shown on their status page${a.guardian_email || a.applicant_email ? ' and emailed' : ''})<textarea name="message" id="amsg" maxlength="1500">${esc(MSG[next[0]] || '')}</textarea></label>
${a.guardian_email || a.applicant_email ? `<label style="flex-direction:row;align-items:center;gap:8px"><input type="checkbox" name="notify" checked style="width:auto;margin:0"> Email the family</label>` : `<p class="muted">No email address was given: phone the family on ${esc(a.guardian_phone || a.applicant_phone || 'the number given')}.</p>`}
<label>Internal reason (optional, not shared)<input name="note" maxlength="300"></label><button class="b">Save decision</button></form></div>`;
  if (a.status === 'accepted') h += `<div class="card"><h2>Enrol</h2><p class="sub">Creates the student's Ace account in a class, with a student number. ${a.guardian_email ? 'The guardian is added for the weekly progress email (it starts once they agree).' : ''}</p>
${(T.St.classes || []).length ? `<form data-f="aenrol" data-id="${a.id}"><div class="row"><label>Class<select name="class_id">${T.St.classes.map(c => opt(c.id, c.name + ' (' + c.grade + ')', best && c.id === best.id)).join('')}</select></label></div>${a.guardian_email || a.applicant_email ? `<label style="flex-direction:row;align-items:center;gap:8px"><input type="checkbox" name="email_family" style="width:auto;margin:0"> Email the login details to the family</label>` : ''}<button class="b">Enrol and create account</button></form>` : empty('No classes yet', 'Create a class first.', '<button class="g" data-go="classes">Classes</button>')}</div>`;
  if (St.cred && St.cred.id === a.id) h += `<div class="card" style="border-color:var(--green)"><h2>Account created: shown once</h2>${table(['Name', 'Username', 'Temporary password', 'Student no.'], [`<tr><td>${esc(a.first_name + ' ' + a.surname)}</td><td>${esc(St.cred.username)}</td><td><b>${esc(St.cred.temp_password)}</b></td><td>${esc(St.cred.student_number)}</td></tr>`])}<p class="sub">${St.cred.emailed ? 'Also emailed to the family.' : 'Print or copy this now.'} Ace asks for a new password at the first sign-in.</p><button class="g noprint" data-a="aiprint">Print</button></div>`;
  h += `<div class="card"><h2>History</h2><div class="lst">${ev.map(e => `<div class="it"><div class="m"><b>${e.from_status ? esc(LBL[e.from_status] || e.from_status) + ' → ' : ''}${esc(LBL[e.to_status] || e.to_status || 'Updated')}</b><small>${day(e.created_at)} • ${e.actor ? esc(who[e.actor] || 'Staff') : 'Family'}</small>${e.message ? `<div style="margin-top:4px;white-space:pre-wrap">${esc(e.message)}</div>` : ''}${e.note ? `<div class="muted" style="margin-top:4px">Internal: ${esc(e.note)}</div>` : ''}</div></div>`).join('')}</div></div>`;
  return h;
}
A.amsg = el => { const t = document.getElementById('amsg'); if (t) t.value = MSG[el.value] || ''; };
A.adoc = async el => { const r = await fn('admissions-manage', { action: 'doc_url', document_id: el.dataset.id }); window.open(r.url, '_blank', 'noopener'); };
F.anote = async (d, f) => { await fn('admissions-manage', { action: 'note', application_id: f.dataset.id, note: d.note }); toast('Note saved.'); };
F.astatus = async (d, f) => { const r = await fn('admissions-manage', { action: 'status', application_id: f.dataset.id, status: d.status, message: d.message, note: d.note, notify: !!d.notify }); toast('Moved to ' + (LBL[r.status] || r.status) + (r.emailed ? '. Family emailed.' : '.')); T.go(); };
F.aenrol = async (d, f) => { const r = await fn('admissions-manage', { action: 'enrol', application_id: f.dataset.id, class_id: d.class_id, email_family: !!d.email_family }); St.cred = Object.assign({ id: f.dataset.id }, r); if (T.fresh) T.fresh(); toast('Enrolled.'); T.go(); };
})();
