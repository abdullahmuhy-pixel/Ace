/* Ace Teach: school-management extras. What the school uses (everything, or school management only), family links
   the school creates for a student, and fee reminders to the families of students with overdue fees. */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, must, toast, fn, isAdmin, isTutor } = H;
const sb = () => T.sb, me = () => T.me;
const money = (v, c) => (c ? c + ' ' : '') + (+v || 0).toLocaleString(undefined, { maximumFractionDigits: 2 });
const day = d => d ? new Date(d).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' }) : '';
const famUrl = c => `${location.origin}${location.pathname.replace(/staff\/.*$/, '')}family/?c=${c}`;
const copy = (t, ok) => { try { navigator.clipboard.writeText(t).then(() => toast(ok || 'Copied.'), () => toast(t)); } catch (e) { toast(t); } };

/* ---------- what the school uses ---------- */
const settings0 = V.settings;
V.settings = async () => {
  const h = await settings0(), s = T.school;
  if (!isAdmin() || isTutor() || !s) return h;
  const sis = s.product === 'sis';
  return `<div class="card"><h2>What your school uses</h2><p class="sub">Choose school management only if your school wants admissions, records, fees, results, the calendar and behaviour without Ace's learning tools. Students can still study on Ace on their own.</p>
<form data-f="product"><label style="flex-direction:row;align-items:flex-start;gap:10px"><input type="radio" name="product" value="full" ${sis ? '' : 'checked'} style="width:auto;margin:3px 0 0"><span><b>Everything</b><br><small class="muted">Learning tools (assigned work, practice, live quizzes, pacing, AI planner) and school management.</small></span></label>
<label style="flex-direction:row;align-items:flex-start;gap:10px"><input type="radio" name="product" value="sis" ${sis ? 'checked' : ''} style="width:auto;margin:3px 0 0"><span><b>School management only</b><br><small class="muted">Dashboard, admissions, people, classes, timetables, fees, results, register, gradebook, behaviour, calendar, notices and parents. The family link shows only school information.</small></span></label>
<button class="b">Save</button></form></div>` + h;
};
F.product = async d => { const v = d.product === 'sis' ? 'sis' : 'full'; must(await sb().from('schools').update({ product: v }).eq('id', me().school_id)); T.school.product = v;
  toast(v === 'sis' ? 'Switched to school management only.' : 'Switched to everything.'); location.hash = 'settings'; location.reload(); };

/* ---------- family links made by the school (shown in the student's record card) ---------- */
H.loadFamilyLinks = async sid => {
  const box = document.getElementById('flinks'); if (!box) return;
  const { data, error } = await sb().rpc('student_family_links', { p_student: sid });
  if (error) { box.innerHTML = `<p class="muted">${esc(error.message)}</p>`; return; }
  const L = data || [];
  box.innerHTML = `<p class="sub">A family link lets a parent see this student's term reports, fees and receipts, the school calendar and shared merits, with no account. Share it by WhatsApp, SMS or email.</p>
${L.length ? `<div class="lst">${L.map(l => `<div class="it"><div class="m"><b><code>${esc(l.code)}</code> ${esc(l.label || '')}</b><small>${l.by_school ? 'Made by the school' : 'Made by the student'} • until ${day(l.expires_at)}${l.last_viewed ? ' • last opened ' + day(l.last_viewed) : ' • not opened yet'}</small></div><button class="g" type="button" data-a="flcopy" data-c="${esc(l.code)}">Copy link</button><button class="g" type="button" data-a="flstop" data-id="${l.id}" data-s="${sid}">Stop</button></div>`).join('')}</div>` : ''}
<form data-f="flnew" data-id="${sid}" class="row" style="margin-top:8px"><label>Label (optional)<input name="label" maxlength="40" placeholder="Mother"></label><button class="g">Make a family link</button></form>`;
};
F.flnew = async (d, f) => { const c = must(await sb().rpc('school_family_link', { p_student: f.dataset.id, p_label: d.label || null })); copy(famUrl(c), 'Link made and copied. Paste it into WhatsApp, SMS or email.'); H.loadFamilyLinks(f.dataset.id); };
A.flcopy = el => copy(famUrl(el.dataset.c), 'Family link copied.');
A.flstop = async el => { if (el.dataset.sure !== '1') { el.dataset.sure = '1'; el.textContent = 'Tap again'; return; } must(await sb().rpc('school_revoke_family_link', { p_id: el.dataset.id })); toast('Link stopped.'); H.loadFamilyLinks(el.dataset.s); };

/* ---------- fee reminders ---------- */
A.remind = async () => {
  const list = must(await sb().rpc('fee_reminder_list')) || [], week = Date.now() - 7 * 864e5;
  St.rlist = list;
  const d = document.createElement('div'); d.className = 'drawer';
  d.innerHTML = `<div><div class="row" style="justify-content:space-between;align-items:flex-start"><h2 style="margin:0">Remind families (${list.length})</h2><button class="g" type="button" data-a="closedr">Close</button></div>
<p class="sub">Each family gets what is due now, the balance, your payment details from Fee settings and a family link to the full statement. Families reminded in the last 7 days are unticked.</p>
${list.length ? `<form data-f="remindsend"><div class="lst">${list.map(r => { const recent = r.last_reminded && new Date(r.last_reminded).getTime() > week, em = (r.guardians || []).map(g => g.email).filter(Boolean), ph = (r.guardians || []).map(g => g.phone).filter(Boolean).concat(r.phone ? [r.phone] : []);
  return `<label class="it" style="flex-direction:row;align-items:center;gap:10px;cursor:pointer"><input type="checkbox" name="s" value="${r.student_id}" ${recent ? '' : 'checked'} style="width:auto;margin:0"><div class="m"><b>${esc(r.name)} • ${money(r.overdue, r.currency)} due</b><small>${esc(r.class || '')}${em.length ? ' • ' + esc(em.join(', ')) : ' • no guardian email'}${ph.length ? ' • ' + esc([...new Set(ph)].join(', ')) : ''}${r.last_reminded ? ' • reminded ' + day(r.last_reminded) : ''}</small></div></label>`; }).join('')}</div>
<label style="margin-top:12px">Add a line (optional)<textarea name="note" maxlength="600" placeholder="e.g. Please pay by Friday 28 November so your child can sit the end-of-term exams."></textarea></label>
<div class="row" style="gap:8px"><button class="b">Send by email</button><button class="g" type="button" data-a="remindcopy">Copy messages for WhatsApp or SMS</button></div></form><div id="remindout"></div>` : '<p class="muted">Nobody has fees due right now.</p>'}</div>`;
  document.body.appendChild(d);
};
const picked = () => [...document.querySelectorAll('form[data-f="remindsend"] input[name=s]:checked')].map(i => i.value);
const message = (r, note) => { const s = T.school || {}; return `Dear parent or guardian, this is a reminder from ${s.name} that ${money(r.overdue, r.currency)} of school fees for ${r.name}${r.class ? ' (' + r.class + ')' : ''} is now due. The balance on the account is ${money(r.balance, r.currency)}.${note ? ' ' + note : ''}${s.fee_note ? '\n' + s.fee_note : ''}\nIf you have already paid, thank you, and please ignore this message.`; };
F.remindsend = async d => {
  const ids = picked(); if (!ids.length) throw new Error('Tick at least one family.');
  const r = await fn('fee-reminders', { action: 'send', student_ids: ids, note: d.note || '' });
  const out = document.getElementById('remindout');
  if (r.mail_off) { out.innerHTML = `<div class="note" style="margin-top:12px">Email is not set up for Ace yet, so nothing was sent. Use <b>Copy messages for WhatsApp or SMS</b> instead.</div>`; return; }
  out.innerHTML = `<div class="note" style="margin-top:12px">Sent to ${r.sent} famil${r.sent === 1 ? 'y' : 'ies'}.${r.skipped ? ` ${r.skipped} skipped (reminded in the last 7 days).` : ''}${r.no_email ? ` ${r.no_email} had no guardian email: copy their message instead.` : ''}</div>`;
  toast('Reminders sent.');
};
A.remindcopy = async () => {
  const ids = picked(); if (!ids.length) return toast('Tick at least one family.', true);
  const f = document.querySelector('form[data-f="remindsend"]'), note = f ? f.note.value.trim() : '';
  const rows = (St.rlist || []).filter(r => ids.includes(r.student_id));
  const out = document.getElementById('remindout');
  out.innerHTML = `<div style="margin-top:12px"><p class="sub">Copy each message into WhatsApp or SMS, then tap <b>Mark as reminded</b> so the list remembers.</p>${rows.map((r, i) => { const ph = (r.guardians || []).map(g => g.phone).filter(Boolean).concat(r.phone ? [r.phone] : []);
    return `<div class="card" style="margin:8px 0;padding:12px"><b>${esc(r.name)}</b>${ph.length ? ` <small class="muted">${esc([...new Set(ph)].join(', '))}</small>` : ''}<p style="white-space:pre-wrap;margin:6px 0" id="rm${i}">${esc(message(r, note))}</p><button class="g" type="button" data-a="rmcopy" data-i="${i}">Copy</button></div>`; }).join('')}<button class="b" type="button" data-a="rmdone">Mark ${rows.length} as reminded</button></div>`;
  St.rcopy = ids;
};
A.rmcopy = el => copy(document.getElementById('rm' + el.dataset.i).textContent, 'Message copied.');
A.rmdone = async () => { const r = await fn('fee-reminders', { action: 'copied', student_ids: St.rcopy || [] }); toast(r.logged + ' marked as reminded.'); const d = document.querySelector('.drawer'); if (d) d.remove(); };
})();
