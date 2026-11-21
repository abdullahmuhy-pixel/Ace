/* Ace Teach: school calendar (terms plus events, holidays, exam weeks and closures) and the behaviour log
   (merits, concerns, incidents; welfare notes for school admins only). Rules are in Postgres RLS. */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, must, toast, csv, saveCsv, empty, nm, isAdmin, isTutor } = H;
const sb = () => T.sb, me = () => T.me;
const opt = (v, l, sel) => `<option value="${esc(v)}" ${sel ? 'selected' : ''}>${esc(l == null ? v : l)}</option>`;
const today = () => new Date().toISOString().slice(0, 10);
const addDays = (d, n) => new Date(new Date(d + 'T00:00:00Z').getTime() + n * 864e5).toISOString().slice(0, 10);
const day = (d, o) => d ? new Date(d + 'T00:00:00').toLocaleDateString(undefined, o || { weekday: 'short', day: 'numeric', month: 'short' }) : '';
const KIND = { event: ['Event', ''], holiday: ['Holiday', 'ok'], exam: ['Exams', 'w'], closure: ['School closed', 'bad'], meeting: ['Meeting', ''], deadline: ['Deadline', 'w'], term: ['Term', 'ok'] };
const admin = () => isAdmin() && !isTutor();

/* ---------- calendar ---------- */
V.calendar = async () => {
  if (!me().school_id) return `<div class="card">${empty('No school calendar', 'The calendar belongs to a school. Private tutors can use the Term planner.', '')}</div>`;
  const past = !!St.calpast, from = past ? addDays(today(), -180) : addDays(today(), -7), to = addDays(today(), 400);
  const [ev, te] = await Promise.all([
    sb().from('school_events').select('*').eq('school_id', me().school_id).lte('starts_on', to).gte('ends_on', from).order('starts_on'),
    sb().from('academic_terms').select('id,name,starts_on,ends_on').eq('school_id', me().school_id).gte('ends_on', from).order('starts_on')]);
  const items = (must(ev) || []).map(e => Object.assign({ t: 'e' }, e)).concat((must(te) || []).flatMap(t => [
    { t: 't', id: t.id, title: t.name + ' begins', kind: 'term', starts_on: t.starts_on, ends_on: t.starts_on },
    { t: 't', id: t.id, title: t.name + ' ends', kind: 'term', starts_on: t.ends_on, ends_on: t.ends_on }]).filter(x => x.starts_on >= from && x.starts_on <= to))
    .sort((a, b) => a.starts_on < b.starts_on ? -1 : a.starts_on > b.starts_on ? 1 : 0);
  const now = (te.data || []).find(t => t.starts_on <= today() && t.ends_on >= today());
  const left = now ? Math.round((new Date(now.ends_on) - new Date(today())) / 864e5) : null;
  const months = {}; items.forEach(x => { const k = x.starts_on.slice(0, 7); (months[k] = months[k] || []).push(x); });
  let h = `<div class="card"><h2>School calendar<span class="sp row" style="gap:6px"><button class="g" data-a="calpast">${past ? 'Hide past' : 'Show the last six months'}</button>${admin() ? '<button class="g" data-a="calcsv">Export CSV</button>' : ''}</span></h2><p class="sub">${now ? `Now: <b>${esc(now.name)}</b>, ${left} day${left === 1 ? '' : 's'} to the end of term.` : 'No term is running today.'} Students see everything except staff-only items in the app.</p></div>`;
  if (admin()) h += `<div class="card"><h2>Add to the calendar</h2><form data-f="caladd"><div class="row"><label style="flex:2 1 220px">What<input name="title" required maxlength="120" placeholder="Mid-term break"></label><label>Type<select name="kind">${Object.keys(KIND).filter(k => k !== 'term').map(k => opt(k, KIND[k][0])).join('')}</select></label></div>
<div class="row"><label>From<input name="starts_on" type="date" required></label><label>To (optional)<input name="ends_on" type="date"></label><label>Who sees it<select name="audience">${opt('everyone', 'Everyone')}${opt('staff', 'Staff only')}</select></label></div><label>Note (optional)<input name="note" maxlength="500"></label><button class="b">Add</button></form><p class="sub">Terms come from Results, Terms and grades.</p></div>`;
  h += Object.keys(months).length ? Object.keys(months).map(k => `<div class="card"><h2>${new Date(k + '-01T00:00:00').toLocaleDateString(undefined, { month: 'long', year: 'numeric' })}</h2><div class="lst">${months[k].map(x => `<div class="it" ${x.ends_on < today() ? 'style="opacity:.55"' : ''}><div class="m"><b>${esc(x.title)}</b><small>${day(x.starts_on)}${x.ends_on !== x.starts_on ? ' to ' + day(x.ends_on) : ''}${x.note ? ' • ' + esc(x.note) : ''}</small></div><span class="pill ${KIND[x.kind][1]}">${KIND[x.kind][0]}</span>${x.audience === 'staff' ? '<span class="pill">Staff</span>' : ''}${admin() && x.t === 'e' ? `<button class="g" data-a="caldel" data-id="${x.id}">Delete</button>` : ''}</div>`).join('')}</div></div>`).join('')
    : `<div class="card">${empty('Nothing on the calendar yet', admin() ? 'Add holidays, exam weeks and events above.' : 'Your school admin adds holidays, exam weeks and events.', '')}</div>`;
  St.calitems = items; return h;
};
A.calpast = () => { St.calpast = !St.calpast; T.go(); };
F.caladd = async d => { const e = d.ends_on || d.starts_on; if (e < d.starts_on) throw new Error('The end date is before the start date.');
  must(await sb().from('school_events').insert({ school_id: me().school_id, title: d.title.trim(), kind: d.kind, starts_on: d.starts_on, ends_on: e, audience: d.audience, note: d.note || null, created_by: me().id })); toast('Added to the calendar.'); T.go(); };
A.caldel = async el => { if (el.dataset.sure !== '1') { el.dataset.sure = '1'; el.textContent = 'Tap again'; return; } must(await sb().from('school_events').delete().eq('id', el.dataset.id)); toast('Deleted.'); T.go(); };
A.calcsv = () => saveCsv('calendar.csv', csv([['Title', 'Type', 'From', 'To', 'Who sees it', 'Note']].concat((St.calitems || []).map(x => [x.title, KIND[x.kind][0], x.starts_on, x.ends_on, x.audience === 'staff' ? 'Staff' : 'Everyone', x.note || '']))));

/* ---------- behaviour ---------- */
const CATS = { merit: ['Effort', 'Helpfulness', 'Leadership', 'Excellent work', 'Improvement', 'Kindness'], concern: ['Homework', 'Lateness', 'Disruption', 'Uniform', 'Phone', 'Respect'], incident: ['Fighting', 'Bullying', 'Damage', 'Truancy', 'Cheating', 'Other'], welfare: ['Wellbeing', 'Family', 'Health', 'Attendance', 'Safeguarding', 'Other'] };
const KB = { merit: ['Merit', 'ok', 1], concern: ['Concern', 'w', -1], incident: ['Incident', 'bad', -3], welfare: ['Welfare note', '', 0] };
async function period() {
  if (St.bper) return St.bper;
  const t = me().school_id ? (must(await sb().from('academic_terms').select('name,starts_on,ends_on').eq('school_id', me().school_id).lte('starts_on', today()).gte('ends_on', today()).limit(1)) || [])[0] : null;
  return t ? { from: t.starts_on, to: t.ends_on, label: t.name } : { from: addDays(today(), -90), to: today(), label: 'Last 90 days' };
}
V.behaviour = async () => {
  const c = St.classes.find(x => x.id === St.cls); if (!c) return '';
  const p = await period();
  const [sum, ro] = await Promise.all([sb().rpc('class_behaviour', { p_class: c.id, p_from: p.from, p_to: p.to }), sb().rpc('class_roster', { p_class: c.id })]);
  const S = must(sum) || [], N = {}; (must(ro) || []).forEach(r => N[r.student_id] = r);
  const ids = S.map(x => x.student_id);
  const log = ids.length ? must(await sb().from('behaviour_entries').select('*').in('student_id', ids).gte('occurred_on', p.from).lte('occurred_on', p.to).order('occurred_on', { ascending: false }).order('created_at', { ascending: false }).limit(200)) || [] : [];
  St.blog = log; St.bnames = N;
  const tot = k => S.reduce((n, x) => n + +x[k], 0);
  S.sort((a, b) => String((N[a.student_id] || {}).surname).localeCompare((N[b.student_id] || {}).surname));
  return `<div class="kpis"><div class="kpi g"><b>${tot('merits')}</b><span>Merits</span></div><div class="kpi a"><b>${tot('concerns')}</b><span>Concerns and incidents</span></div><div class="kpi"><b>${S.filter(x => +x.concerns >= 3).length}</b><span>Students with 3 or more concerns</span></div></div>
<div class="card"><h2>${esc(c.name)}: behaviour<span class="sp"><small class="muted">${esc(p.label)}</small></span></h2><p class="sub">Tap Merit or Concern to record it. Entries you share with the family show in the student's app. ${admin() ? 'Welfare notes are for school admins only and never shared.' : 'Welfare concerns: tell your school admin.'}</p>
${table(['Student', 'Merits', 'Concerns', 'Points', 'Last'], S.map(x => { const r = N[x.student_id] || {}; return `<tr><td><b>${r.first_name ? nm(r) : ''}</b><div style="display:flex;gap:6px;margin-top:6px;white-space:nowrap"><button class="g" data-a="bnew" data-id="${x.student_id}" data-k="merit">+ Merit</button><button class="g" data-a="bnew" data-id="${x.student_id}" data-k="concern">Concern</button></div></td><td class="n">${x.merits}</td><td class="n">${+x.concerns ? `<span class="pill ${+x.concerns >= 3 ? 'bad' : 'w'}">${x.concerns}</span>` : 0}</td><td class="n">${x.points > 0 ? '+' : ''}${x.points}</td><td>${x.last_on ? day(x.last_on) : '–'}</td></tr>`; }), 'No students in this class yet.')}</div>
<div class="card"><h2>Log<span class="sp"><button class="g" data-a="bcsv">Export CSV</button></span></h2>${log.length ? `<div class="lst">${log.map(e => entry(e, N)).join('')}</div>` : '<p class="muted">Nothing recorded in this period.</p>'}</div>`;
};
const entry = (e, N) => { const r = N[e.student_id] || {}, mine = e.recorded_by === me().id && Date.now() - new Date(e.created_at) < 864e5;
  return `<div class="it"><div class="m"><b>${r.first_name ? nm(r) + ': ' : ''}${esc(e.category || KB[e.kind][0])}${e.points ? ` (${e.points > 0 ? '+' : ''}${e.points})` : ''}</b><small>${day(e.occurred_on)} • ${esc(e.description)}${e.action_taken ? ' • Action: ' + esc(e.action_taken) : ''}${e.visible_to_family ? ' • shared with family' : ''}</small></div><span class="pill ${KB[e.kind][1]}">${KB[e.kind][0]}</span>${mine || admin() ? `<button class="g" data-a="bdel" data-id="${e.id}">Delete</button>` : ''}</div>`; };
H.behaviourEntry = entry;
A.bnew = el => {
  const sid = el.dataset.id, k = el.dataset.k, r = (St.bnames || {})[sid] || {}, kinds = admin() ? ['merit', 'concern', 'incident', 'welfare'] : ['merit', 'concern', 'incident'];
  const d = document.createElement('div'); d.className = 'drawer';
  d.innerHTML = `<div><div class="row" style="justify-content:space-between"><h2 style="margin:0">${r.first_name ? nm(r) : 'Student'}</h2><button class="g" type="button" data-a="closedr">Close</button></div>
<form data-f="badd" data-id="${sid}" style="margin-top:12px"><div class="row"><label>Type<select name="kind" data-a="bkind">${kinds.map(x => opt(x, KB[x][0], x === k)).join('')}</select></label><label>Points<input name="points" type="number" min="-10" max="10" value="${KB[k][2]}"></label><label>Date<input name="occurred_on" type="date" value="${today()}" max="${today()}"></label></div>
<label>Category<input name="category" maxlength="60" list="bcats" value="${esc(CATS[k][0])}"><datalist id="bcats">${CATS[k].map(c => `<option value="${esc(c)}">`).join('')}</datalist></label>
<label>What happened<textarea name="description" required maxlength="1000"></textarea></label><label>Action taken (optional)<input name="action_taken" maxlength="500" placeholder="e.g. Spoke to the student; parents called"></label>
<label style="flex-direction:row;align-items:center;gap:8px" id="bshare"><input type="checkbox" name="visible_to_family" ${k === 'merit' ? 'checked' : ''} style="width:auto;margin:0"> Show to the student and family in the app</label><button class="b">Save</button></form></div>`;
  document.body.appendChild(d);
};
A.bkind = el => { const f = el.form, k = el.value; f.points.value = KB[k][2]; f.category.value = CATS[k][0]; document.getElementById('bcats').innerHTML = CATS[k].map(c => `<option value="${esc(c)}">`).join('');
  const s = document.getElementById('bshare'); s.style.display = k === 'welfare' ? 'none' : 'flex'; f.visible_to_family.checked = k === 'merit'; };
F.badd = async (d, f) => {
  const k = d.kind, pts = Math.max(-10, Math.min(10, parseInt(d.points, 10) || 0));
  if ((k === 'merit' && pts < 0) || ((k === 'concern' || k === 'incident') && pts > 0)) throw new Error(k === 'merit' ? 'Merits take 0 or more points.' : 'Concerns and incidents take 0 or fewer points.');
  const st = must(await sb().from('profiles').select('school_id').eq('id', f.dataset.id).maybeSingle());
  must(await sb().from('behaviour_entries').insert({ school_id: st.school_id, student_id: f.dataset.id, kind: k, category: d.category || null, points: k === 'welfare' ? 0 : pts,
    description: d.description, action_taken: d.action_taken || null, visible_to_family: k !== 'welfare' && !!d.visible_to_family, occurred_on: d.occurred_on || today(), recorded_by: me().id }));
  const dr = f.closest('.drawer'); if (dr) dr.remove(); toast(KB[k][0] + ' recorded.');
  if (document.querySelector('.drawer') && St.recid === f.dataset.id && A.strec) { document.querySelector('.drawer').remove(); A.strec({ dataset: { id: f.dataset.id } }); } else T.go();
};
A.bdel = async el => { if (el.dataset.sure !== '1') { el.dataset.sure = '1'; el.textContent = 'Tap again'; return; } must(await sb().from('behaviour_entries').delete().eq('id', el.dataset.id)); toast('Deleted.'); T.go(); };
A.bcsv = () => { const N = St.bnames || {}; saveCsv('behaviour.csv', csv([['Date', 'Student', 'Type', 'Category', 'Points', 'What happened', 'Action', 'Shared with family']].concat((St.blog || []).map(e => { const r = N[e.student_id] || {}; return [e.occurred_on, r.first_name ? r.first_name + ' ' + r.surname : '', KB[e.kind][0], e.category, e.points, e.description, e.action_taken, e.visible_to_family ? 'Yes' : 'No']; })))); };
})();
