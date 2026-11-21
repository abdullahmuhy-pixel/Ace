/* Ace Teach: management dashboard for school admins. One call to school_dashboard() returns every number for a
   term or a date range (enrolment, admissions, results, attendance, fees, behaviour, teacher workload), so the page
   and the CSV always agree. Charts are plain bars drawn to one scale per chart. */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, must, toast, csv, saveCsv, empty } = H;
const sb = () => T.sb, me = () => T.me;
const opt = (v, l, sel) => `<option value="${esc(v)}" ${sel ? 'selected' : ''}>${esc(l == null ? v : l)}</option>`;
const n1 = v => v == null ? '–' : (+v).toLocaleString(undefined, { maximumFractionDigits: 1 });
const pc = v => v == null ? '–' : n1(v) + '%';
const money = (v, c) => (c ? c + ' ' : '') + (+v || 0).toLocaleString(undefined, { maximumFractionDigits: 0 });
const day = d => d ? new Date(d + 'T00:00:00').toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' }) : '';
const STATUS = { active: 'Active', suspended: 'Suspended', withdrawn: 'Withdrawn', transferred: 'Transferred', graduated: 'Graduated' };
const APP = { submitted: 'New', reviewing: 'Reviewing', interview: 'Interview', waitlisted: 'Waiting list', accepted: 'Accepted', enrolled: 'Enrolled', declined: 'Declined', withdrawn: 'Withdrawn' };
// horizontal bar rows on one 0..max scale; colour by threshold when given
const hbars = (rows, max, fmt, warn, col) => `<div style="display:grid;gap:8px">${rows.map(r => { const w = max ? Math.max(0, Math.min(100, 100 * (+r.v || 0) / max)) : 0, bad = warn && r.v != null && +r.v < warn;
  return `<div style="display:grid;grid-template-columns:minmax(90px,30%) 1fr auto;gap:10px;align-items:center"><span style="min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" title="${esc(r.k)}">${esc(r.k)}</span><span style="height:12px;border-radius:6px;background:var(--border);overflow:hidden"><span style="display:block;height:100%;width:${w}%;border-radius:6px;background:var(${bad ? '--red' : col || '--green'})"></span></span><b style="font-variant-numeric:tabular-nums;min-width:52px;text-align:right">${fmt(r.v)}</b></div>`; }).join('')}</div>`;

V.sdash = async () => {
  if (!me().school_id) return '';
  const terms = must(await sb().from('academic_terms').select('id,name,starts_on,ends_on').eq('school_id', me().school_id).order('starts_on', { ascending: false })) || [];
  const mode = St.dmode || (terms.length ? 'term' : 'dates');
  const args = mode === 'term' && (St.dterm || terms[0]) ? { p_term: St.dterm || terms[0].id } : { p_from: St.dfrom || null, p_to: St.dto || null };
  const d = must(await sb().rpc('school_dashboard', args)); St.dash = d;
  const P = d.period, E = d.enrolment, R = d.results, AT = d.attendance, B = d.behaviour, AD = d.admissions;
  const months = E.months || [], mmax = Math.max(1, ...months.map(m => Math.max(m.joined, m.left)));
  const fee = (d.fees || [])[0];
  const kpi = (v, l, c) => `<div class="kpi ${c || ''}"><b>${v}</b><span>${l}</span></div>`;
  let h = `<div class="card noprint"><h2>School dashboard<span class="sp row" style="gap:6px"><button class="g" data-a="dcsv">Export CSV</button><button class="g" data-a="dprint">Print</button></span></h2>
<div class="row"><label>Period<select data-a="dmode">${opt('term', 'A term', mode === 'term')}${opt('dates', 'Dates', mode === 'dates')}</select></label>${mode === 'term' && terms.length ? `<label>Term<select data-a="dterm">${terms.map(t => opt(t.id, t.name, t.id === (St.dterm || terms[0].id))).join('')}</select></label>` : `<label>From<input type="date" data-a="dfrom" value="${esc(St.dfrom || P.from)}"></label><label>To<input type="date" data-a="dto" value="${esc(St.dto || P.to)}"></label>`}</div>
<p class="sub">${day(P.from)} to ${day(P.to)}.${terms.length ? '' : ' Add terms in Results to compare term by term.'}</p></div>`;
  h += `<div class="kpis">${kpi(E.current, 'Current students', 'p')}${kpi(pc(AT.rate), 'Attendance', AT.rate != null && AT.rate < 90 ? 'r' : 'g')}${kpi(pc(R.pass_rate), 'Pass rate' + (P.results_term ? ', ' + esc(P.results_term) : ''), R.pass_rate != null && R.pass_rate < 50 ? 'r' : 'g')}${kpi(fee ? Math.round(100 * fee.paid / Math.max(1, fee.billed)) + '%' : '–', 'Fees collected', 'a')}</div>`;
  // enrolment
  h += `<div class="grid g2"><div class="card"><h2>Enrolment</h2><p class="sub">${E.joined} joined and ${E.left} left in this period.</p>
<div style="display:flex;align-items:flex-end;gap:4px;height:120px;margin:12px 0 4px" role="img" aria-label="Students joining and leaving per month">${months.map(m => `<div style="flex:1;display:flex;gap:2px;align-items:flex-end;height:100%" title="${esc(m.month)}: ${m.joined} joined, ${m.left} left"><span style="flex:1;background:var(--green);border-radius:4px 4px 0 0;height:${100 * m.joined / mmax}%"></span><span style="flex:1;background:var(--red);border-radius:4px 4px 0 0;height:${100 * m.left / mmax}%"></span></div>`).join('')}</div>
<div style="display:flex;gap:4px;font-size:11px;color:var(--text3)">${months.map(m => `<span style="flex:1;text-align:center">${new Date(m.month + '-01T00:00:00').toLocaleDateString(undefined, { month: 'narrow' })}</span>`).join('')}</div>
<p class="sub" style="margin-top:8px"><span style="color:var(--green)">■</span> joined <span style="color:var(--red)">■</span> left, last 12 months, up to ${mmax} a month.</p>
<div class="row" style="gap:6px;flex-wrap:wrap">${Object.keys(E.by_status).map(k => `<span class="pill ${k === 'active' ? 'ok' : k === 'suspended' ? 'w' : ''}">${STATUS[k] || k} ${E.by_status[k]}</span>`).join('')}</div></div>
<div class="card"><h2>Students by class</h2>${E.by_class.length ? hbars(E.by_class.map(c => ({ k: c.class, v: c.students })), Math.max(1, ...E.by_class.map(c => c.students)), v => n1(v), null, '--primary') : '<p class="muted">No classes.</p>'}
${AD.received ? `<h3 style="margin-top:16px">Admissions</h3><p class="sub">${AD.received} application${AD.received === 1 ? '' : 's'} in this period: ${Object.keys(AD.by_status).map(k => (APP[k] || k) + ' ' + AD.by_status[k]).join(', ')}.</p>` : ''}</div></div>`;
  // results
  h += R.reports ? `<div class="grid g2"><div class="card"><h2>Pass rate by subject</h2><p class="sub">${esc(P.results_term || '')}: score of ${n1(P.pass_mark)} or more counts as a pass. Weakest first. ${R.published < R.reports ? `${R.reports - R.published} of ${R.reports} reports not yet published.` : ''}</p>${hbars(R.by_subject.map(s => ({ k: s.subject, v: s.pass_rate })), 100, pc, 50)}</div>
<div class="card"><h2>Results by class</h2>${table(['Class', 'Students', 'Average', 'Pass rate'], R.by_class.map(c => `<tr><td><b>${esc(c.class || '–')}</b></td><td class="n">${c.students}</td><td class="n">${n1(c.average)}</td><td class="n"><span class="pill ${c.pass_rate == null ? '' : c.pass_rate < 50 ? 'bad' : 'ok'}">${pc(c.pass_rate)}</span></td></tr>`))}<p class="sub">School average ${n1(R.average)}, pass rate ${pc(R.pass_rate)}.</p></div></div>`
    : `<div class="card">${empty('No term results yet', 'Compile a term in Results to see pass rates by subject and class.', '<button class="g" data-go="results">Results</button>')}</div>`;
  // attendance and behaviour
  h += `<div class="grid g2"><div class="card"><h2>Attendance by class</h2>${AT.by_class.length ? hbars(AT.by_class.map(c => ({ k: c.class, v: c.rate })), 100, pc, 90) + `<p class="sub" style="margin-top:10px">${AT.days_marked} days marked. <b>${AT.below_90}</b> student${AT.below_90 === 1 ? '' : 's'} below 90% (red bars are classes below 90%).</p>` : '<p class="muted">No register taken in this period.</p>'}</div>
<div class="card"><h2>Behaviour</h2><div class="row" style="gap:16px"><div><b style="font-size:24px;color:var(--green)">${B.merits}</b><br><small>merits</small></div><div><b style="font-size:24px;color:var(--red)">${B.concerns}</b><br><small>concerns and incidents</small></div><div><b style="font-size:24px">${B.students_3plus}</b><br><small>students with 3 or more</small></div></div>
${B.top_concerns.length ? `<h3 style="margin-top:14px">Most common concerns</h3>${hbars(B.top_concerns.map(c => ({ k: c.category, v: c.n })), Math.max(1, ...B.top_concerns.map(c => c.n)), v => n1(v), null, '--amber')}` : ''}</div></div>`;
  // fees
  h += (d.fees || []).length ? `<div class="card"><h2>Fees</h2>${table(['Currency', 'Billed', 'Collected', 'Outstanding', 'Overdue now', 'Collected in period'], d.fees.map(f => `<tr><td><b>${esc(f.currency)}</b></td><td class="n">${money(f.billed)}</td><td class="n">${money(f.paid)}</td><td class="n">${money(f.outstanding)}</td><td class="n"><span class="pill ${+f.overdue ? 'bad' : 'ok'}">${money(f.overdue)}</span></td><td class="n">${money(f.collected_in_period)}</td></tr>`))}
${d.fees.map(f => `<div style="display:flex;height:14px;border-radius:7px;overflow:hidden;margin-top:10px;background:var(--border)" role="img" aria-label="${esc(f.currency)}: ${Math.round(100 * f.paid / Math.max(1, f.billed))}% collected"><span style="width:${100 * f.paid / Math.max(1, f.billed)}%;background:var(--green)"></span><span style="width:${100 * f.overdue / Math.max(1, f.billed)}%;background:var(--red)"></span></div>`).join('')}<p class="sub"><span style="color:var(--green)">■</span> collected <span style="color:var(--red)">■</span> overdue; the rest is not due yet. Totals cover every invoice to date.</p></div>` : '';
  // teachers
  h += `<div class="card"><h2>Teacher workload</h2><p class="sub">Classes and students from teaching assignments, periods and hours a week from the timetable, and assessments and tasks set in this period.</p>${table(['Teacher', 'Subjects', 'Classes', 'Students', 'Periods / week', 'Hours / week', 'Assessments', 'Tasks'], d.teachers.map(t => `<tr><td><b>${esc(t.name)}</b>${t.role === 'school_admin' ? ' <small class="muted">admin</small>' : ''}</td><td>${esc(t.subjects || '–')}</td><td class="n">${t.classes}</td><td class="n">${t.students}</td><td class="n">${t.periods}</td><td class="n">${n1(t.hours)}</td><td class="n">${t.assessments}</td><td class="n">${t.tasks}</td></tr>`), 'No teachers yet.')}</div>`;
  return h;
};
A.dmode = el => { St.dmode = el.value; T.go(); };
A.dterm = el => { St.dterm = el.value; T.go(); };
A.dfrom = el => { St.dfrom = el.value; T.go(); };
A.dto = el => { St.dto = el.value; T.go(); };
A.dprint = () => window.print();
A.dcsv = () => {
  const d = St.dash; if (!d) return; const P = d.period, rows = [['Section', 'Item', 'Value']], add = (s, k, v) => rows.push([s, k, v == null ? '' : v]);
  add('Period', 'From', P.from); add('Period', 'To', P.to); add('Period', 'Results term', P.results_term); add('Period', 'Pass mark', P.pass_mark);
  add('Enrolment', 'Current students', d.enrolment.current); add('Enrolment', 'Joined in period', d.enrolment.joined); add('Enrolment', 'Left in period', d.enrolment.left);
  Object.keys(d.enrolment.by_status).forEach(k => add('Enrolment by status', STATUS[k] || k, d.enrolment.by_status[k]));
  d.enrolment.by_class.forEach(c => add('Students by class', c.class, c.students));
  d.enrolment.months.forEach(m => { add('Joined by month', m.month, m.joined); add('Left by month', m.month, m.left); });
  Object.keys(d.admissions.by_status).forEach(k => add('Applications', APP[k] || k, d.admissions.by_status[k]));
  add('Results', 'Average', d.results.average); add('Results', 'Pass rate %', d.results.pass_rate);
  d.results.by_subject.forEach(s => { add('Pass rate % by subject', s.subject, s.pass_rate); add('Average by subject', s.subject, s.average); });
  d.results.by_class.forEach(c => { add('Pass rate % by class', c.class, c.pass_rate); add('Average by class', c.class, c.average); });
  add('Attendance', 'Rate %', d.attendance.rate); add('Attendance', 'Days marked', d.attendance.days_marked); add('Attendance', 'Students below 90%', d.attendance.below_90);
  d.attendance.by_class.forEach(c => add('Attendance % by class', c.class, c.rate));
  (d.fees || []).forEach(f => ['billed', 'paid', 'outstanding', 'overdue', 'collected_in_period'].forEach(k => add('Fees ' + f.currency, k.replace(/_/g, ' '), f[k])));
  add('Behaviour', 'Merits', d.behaviour.merits); add('Behaviour', 'Concerns and incidents', d.behaviour.concerns); add('Behaviour', 'Students with 3 or more', d.behaviour.students_3plus);
  d.teachers.forEach(t => add('Teacher workload', t.name, `${t.classes} classes, ${t.students} students, ${t.periods} periods (${t.hours} h) a week, ${t.assessments} assessments, ${t.tasks} tasks`));
  saveCsv('school-dashboard-' + P.from + '-to-' + P.to + '.csv', csv(rows));
};
})();
