/* Ace Teach: fee statements for school admins. Itemised term invoices with discounts and instalment plans,
   receipted payments (never edited, only voided with a reason), a statement per student, debtors and a receipts log.
   Totals are kept by the database (fees.amount = items, fees.paid = payments), so this file only reads and calls
   bill_students, record_payment and void_payment. Ace keeps the record; money is paid to the school directly. */
(function () {
'use strict';
const T = window.AceTeach, { V, A, F, St } = T, H = T.helpers;
const { esc, table, must, toast, csv, saveCsv, empty, nm } = H;
const sb = () => T.sb, me = () => T.me;
const opt = (v, l, sel) => `<option value="${esc(v)}" ${sel ? 'selected' : ''}>${esc(l == null ? v : l)}</option>`;
const METHOD = { cash: 'Cash', bank: 'Bank transfer', mobile_money: 'Mobile money', card: 'Card', cheque: 'Cheque', other: 'Other' };
const cents = v => Math.round((+v || 0) * 100);
const money = (v, cur) => (cur ? cur + ' ' : '') + (+v || 0).toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 2 });
const today = () => new Date().toISOString().slice(0, 10);
const day = d => d ? new Date(String(d).length === 10 ? d + 'T00:00:00' : d).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' }) : '';
const LEFT = ['withdrawn', 'transferred', 'graduated'];
const pairs = rows => `<div style="border:1px solid var(--border);border-radius:12px;overflow:hidden">${rows.map((r, i) => `<div style="display:flex;justify-content:space-between;gap:12px;padding:8px 12px;${i ? 'border-top:1px solid var(--border);' : ''}${r[2] ? 'font-weight:700;' : ''}"><span style="min-width:0">${r[0]}</span><span style="white-space:nowrap;font-variant-numeric:tabular-nums">${r[1]}</span></div>`).join('')}</div>`;
// same rule as public.fee_overdue(): due instalments minus paid, or the whole balance once the invoice is due
const overdue = (f, inst) => { const t = today(), mine = inst.filter(i => i.fee_id === f.id);
  const c = mine.length ? mine.filter(i => i.due_on <= t).reduce((s, i) => s + cents(i.amount), 0) - cents(f.paid) : (f.due_on && f.due_on <= t ? cents(f.amount) - cents(f.paid) : 0);
  return Math.max(0, c) / 100; };

/* print one document (statement or receipt) without the portal around it */
const css = document.createElement('style');
css.textContent = `#printdoc{display:none}@media print{body.pdoc>*:not(#printdoc){display:none!important}body.pdoc #printdoc{display:block;color:#000;font:13px/1.45 system-ui,sans-serif}#printdoc table{width:100%;border-collapse:collapse;margin:8px 0 14px}#printdoc th,#printdoc td{border-bottom:1px solid #bbb;padding:5px 6px;text-align:left}#printdoc td.n,#printdoc th.n{text-align:right}#printdoc h1{font-size:20px;margin:0}#printdoc .hd{display:flex;justify-content:space-between;gap:20px;border-bottom:2px solid #000;padding-bottom:8px;margin-bottom:12px}#printdoc .void td{text-decoration:line-through;color:#777}#printdoc .pb{break-after:page}}`;
document.head.appendChild(css);
function printDoc(html) {
  let d = document.getElementById('printdoc'); if (!d) { d = document.createElement('div'); d.id = 'printdoc'; document.body.appendChild(d); }
  d.innerHTML = html; document.body.classList.add('pdoc');
  const done = () => { document.body.classList.remove('pdoc'); window.removeEventListener('afterprint', done); };
  window.addEventListener('afterprint', done); window.print(); setTimeout(done, 1500);
}
H.printDoc = html => printDoc(html);
const head = (title, sub) => { const s = T.school || {}; return `<div class="hd"><div><h1>${esc(s.name || '')}</h1><div>${esc(title)}</div></div><div style="text-align:right">${sub}<br>Printed ${day(today())}</div></div>`; };

H.printHead = (t, sub) => head(t, sub);
async function load() {
  const [f, p] = await Promise.all([
    sb().from('fees').select('*').eq('school_id', me().school_id).order('created_at', { ascending: false }).limit(5000),
    sb().from('profiles').select('id,first_name,surname,class_id,admission_no,enrolment_status').eq('school_id', me().school_id).eq('role', 'student')]);
  const fees = must(f) || [], P = {}; (must(p) || []).forEach(x => P[x.id] = x);
  const inst = fees.length ? must(await sb().from('fee_instalments').select('fee_id,due_on,amount').in('fee_id', fees.map(x => x.id))) || [] : [];
  return { fees, P, inst };
}

V.fees = async () => {
  const tab = St.ftab || 'invoices', s = T.school || {};
  const tabs = `<div class="tabs noprint">${[['invoices', 'Invoices'], ['debtors', 'Who owes'], ['receipts', 'Receipts'], ['bill', 'Bill students'], ['fset', 'Settings']].map(t => `<button class="g ${tab === t[0] ? 'on' : ''}" data-a="ftab" data-v="${t[0]}">${t[1]}</button>`).join('')}</div>`;
  const note = `<div class="note">Ace keeps the fee record and prints statements and receipts. Families pay the school directly, not through Ace.</div>`;
  if (tab === 'bill') return note + tabs + billForm(s);
  if (tab === 'fset') return note + tabs + feeSettings(s);
  const { fees, P, inst } = await load(), C = {}; (St.classes || []).forEach(c => C[c.id] = c);
  if (tab === 'receipts') return note + tabs + await receipts(P);
  const terms = [...new Set(fees.map(x => x.term))], term = St.fterm && terms.includes(St.fterm) ? St.fterm : '';
  const show = fees.filter(x => !term || x.term === term);
  const curs = [...new Set(show.map(x => x.currency_code))], cur = curs.length === 1 ? curs[0] : '';
  const sum = k => show.reduce((n, x) => n + cents(x[k]), 0) / 100, od = show.reduce((n, x) => n + cents(overdue(x, inst)), 0) / 100;
  const kpis = `<div class="kpis"><div class="kpi"><b>${money(sum('amount'))}</b><span>Billed ${esc(cur)}</span></div><div class="kpi g"><b>${money(sum('paid'))}</b><span>Collected${sum('amount') ? ' (' + Math.round(100 * sum('paid') / sum('amount')) + '%)' : ''}</span></div><div class="kpi a"><b>${money(Math.max(0, sum('amount') - sum('paid')))}</b><span>Outstanding</span></div><div class="kpi r"><b>${money(od)}</b><span>Overdue now</span></div></div>${curs.length > 1 ? '<p class="muted">More than one currency is in use: choose a term to see totals in one currency.</p>' : ''}`;
  const filt = `<select data-a="fterm" style="margin:0;width:auto">${opt('', 'All terms', !term)}${terms.map(t => opt(t, t, t === term)).join('')}</select>`;
  if (!fees.length) return note + tabs + `<div class="card">${empty('No fees yet', 'Bill a class for a term to start. Each student gets an itemised invoice and a statement.', '<button class="b" data-a="ftab" data-v="bill">Bill students</button>')}</div>`;
  if (tab === 'debtors') {
    const by = {}; show.forEach(f => { const bal = cents(f.amount) - cents(f.paid); if (bal <= 0) return; const b = by[f.student_id] = by[f.student_id] || { bal: 0, od: 0, due: null, cur: f.currency_code, n: 0 };
      b.bal += bal; b.od += cents(overdue(f, inst)); b.n++; const nd = inst.filter(i => i.fee_id === f.id && i.due_on > today()).map(i => i.due_on).sort()[0] || (f.due_on > today() ? f.due_on : null); if (nd && (!b.due || nd < b.due)) b.due = nd; });
    const rows = Object.keys(by).map(id => Object.assign({ id }, by[id])).sort((a, b) => b.od - a.od || b.bal - a.bal);
    return note + tabs + kpis + `<div class="card"><h2>Who owes (${rows.length})<span class="sp row" style="gap:6px">${filt}<input data-filter="#dlist tbody tr" placeholder="Search" style="width:150px;margin:0"><button class="g" data-a="csvdebt">Export CSV</button></span></h2><p class="sub">Overdue first. Tap a student for their statement and to record a payment.</p><div id="dlist">${table(['Student', 'Class', 'Status', 'Balance', 'Overdue', 'Next due'], rows.map(r => { const p = P[r.id] || {}; return `<tr class="click" data-a="fstmt" data-id="${r.id}"><td><b>${p.first_name ? nm(p) : 'Removed student'}</b><br><small class="muted">${esc(p.admission_no || '')}</small></td><td>${esc((C[p.class_id] || {}).name || '–')}</td><td>${LEFT.includes(p.enrolment_status) ? `<span class="pill bad">Left</span>` : ''}</td><td class="n">${money(r.bal / 100, r.cur)}</td><td class="n">${r.od ? `<span class="pill bad">${money(r.od / 100)}</span>` : '<span class="muted">–</span>'}</td><td>${r.due ? day(r.due) : ''}</td></tr>`; }), 'Nobody owes anything. Well done.')}</div></div>`;
  }
  return note + tabs + kpis + `<div class="card"><h2>Invoices (${show.length})<span class="sp row" style="gap:6px">${filt}<input data-filter="#flist tbody tr" placeholder="Search" style="width:150px;margin:0"><button class="g" data-a="csvfees">Export CSV</button></span></h2><div id="flist">${table(['Student', 'Class', 'Term', 'Total', 'Paid', 'Balance', 'Overdue'], show.map(x => { const p = P[x.student_id] || {}, bal = (cents(x.amount) - cents(x.paid)) / 100, o = overdue(x, inst);
    return `<tr class="click" data-a="fstmt" data-id="${x.student_id}"><td><b>${p.first_name ? nm(p) : 'Removed student'}</b><br><small class="muted">${esc(p.admission_no || '')}</small></td><td>${esc((C[p.class_id] || {}).name || '–')}</td><td>${esc(x.term)}</td><td class="n">${money(x.amount, x.currency_code)}</td><td class="n">${money(x.paid)}</td><td class="n"><span class="pill ${bal <= 0 ? 'ok' : o ? 'bad' : 'w'}">${bal < 0 ? 'Credit ' + money(-bal) : money(bal)}</span></td><td class="n">${o ? money(o) : '–'}</td></tr>`; }))}</div></div>`;
};
A.ftab = el => { St.ftab = el.dataset.v; T.go(); };
A.fterm = el => { St.fterm = el.value; T.go(); };

/* ---------- billing ---------- */
function billForm(s) {
  const cur = s.fee_currency || (St.billcur || '');
  const row = (l, a) => `<div class="row bitem"><label style="flex:3 1 180px">Item<input name="il" maxlength="80" value="${esc(l)}"></label><label style="flex:1 1 110px">Amount<input name="ia" type="number" step="0.01" value="${esc(a)}"></label></div>`;
  return `<div class="card"><h2>Bill students for a term</h2><p class="sub">Each student gets an itemised invoice. Use a negative amount for a discount or bursary. Students already billed for the term, and students who have left, are skipped.</p>
<form data-f="billx"><div class="row"><label>Who<select name="who">${opt('all', 'Every current student')}${(St.classes || []).map(c => opt(c.id, 'Class ' + c.name + ' (' + c.grade + ')')).join('')}</select></label><label>Term<input name="term" required maxlength="40" placeholder="Term 1 2026/27"></label><label style="flex:0 1 110px">Currency<input name="currency" required maxlength="3" value="${esc(cur)}" placeholder="NGN" style="text-transform:uppercase"></label></div>
<div id="bitems">${row('Tuition', '')}${row('', '')}${row('', '')}</div><button class="g" type="button" data-a="bitem">Add a line</button>
<p id="btotal" class="sub" style="margin:10px 0">Total per student: 0</p>
<div class="row"><label>Pay in<select name="n" data-a="binst">${[1, 2, 3, 4].map(n => opt(n, n === 1 ? 'One payment' : n + ' instalments')).join('')}</select></label></div><div id="binst" class="row"><label>Due<input name="d0" type="date"></label></div>
<button class="b">Create invoices</button></form></div>`;
}
const billTotal = () => [...document.querySelectorAll('#bitems [name=ia]')].reduce((s, i) => s + cents(i.value), 0);
// split a total in cents into n parts that add up exactly; the last part takes the remainder
const split = (c, n) => { const base = Math.floor(c / n), out = Array(n).fill(base); out[n - 1] = c - base * (n - 1); return out; };
H.feeSplit = split;
const showSplit = () => { const n = +((document.querySelector('[name=n]') || {}).value || 1), parts = split(billTotal(), n), b = document.getElementById('binst'); if (!b) return;
  const old = [...b.querySelectorAll('input[type=date]')].map(i => i.value);
  b.innerHTML = parts.map((p, i) => `<label>${n > 1 ? 'Instalment ' + (i + 1) + ': ' + money(p / 100) : 'Due'}<input name="d${i}" type="date" value="${esc(old[i] || '')}" ${n > 1 ? 'required' : ''}></label>`).join('');
  const t = document.getElementById('btotal'); if (t) t.textContent = 'Total per student: ' + money(billTotal() / 100); };
document.addEventListener('input', e => { if (e.target.closest && e.target.closest('#bitems')) showSplit(); });
A.binst = () => showSplit();
A.bitem = () => { const d = document.createElement('div'); d.className = 'row bitem'; d.innerHTML = `<label style="flex:3 1 180px">Item<input name="il" maxlength="80"></label><label style="flex:1 1 110px">Amount<input name="ia" type="number" step="0.01"></label>`; document.getElementById('bitems').appendChild(d); };
F.billx = async (d, f) => {
  const items = [...f.querySelectorAll('.bitem')].map(r => ({ label: r.querySelector('[name=il]').value.trim(), amount: cents(r.querySelector('[name=ia]').value) / 100 })).filter(x => x.label || x.amount);
  if (!items.length) throw new Error('Add at least one item.');
  if (items.some(x => !x.label)) throw new Error('Give every amount a name.');
  const total = items.reduce((s, x) => s + cents(x.amount), 0); if (total < 0) throw new Error('The items add up to less than zero.');
  const n = +d.n || 1, parts = split(total, n), dates = parts.map((_, i) => d['d' + i]).filter(Boolean);
  if (n > 1 && dates.length < n) throw new Error('Give a due date for every instalment.');
  if (n > 1 && [...dates].sort().join() !== dates.join()) throw new Error('Put the instalments in date order.');
  const inst = n > 1 ? parts.map((c, i) => ({ due_on: dates[i], amount: c / 100 })) : (dates[0] && total > 0 ? [{ due_on: dates[0], amount: total / 100 }] : []);
  const q = sb().from('profiles').select('id').eq('school_id', me().school_id).eq('role', 'student').in('enrolment_status', ['active', 'suspended']);
  const ids = (must(await (d.who === 'all' ? q : q.eq('class_id', d.who))) || []).map(x => x.id);
  if (!ids.length) throw new Error('No current students in that class.');
  const k = must(await sb().rpc('bill_students', { p_students: ids, p_term: d.term.trim(), p_currency: d.currency.toUpperCase(), p_items: items, p_instalments: inst }));
  toast(k + ' invoice' + (k === 1 ? '' : 's') + ' created' + (k < ids.length ? ', ' + (ids.length - k) + ' already billed' : '') + '.'); St.ftab = 'invoices'; St.fterm = d.term.trim(); T.go();
};

/* ---------- statement ---------- */
A.fstmt = async el => {
  const id = el.dataset.id; St.fsid = id;
  const p = must(await sb().from('profiles').select('id,first_name,surname,admission_no,class_id,enrolment_status').eq('id', id).maybeSingle()) || {};
  const fees = must(await sb().from('fees').select('*').eq('student_id', id).order('created_at')) || [], ids = fees.map(f => f.id);
  const [it, ins, pay] = ids.length ? await Promise.all([sb().from('fee_items').select('*').in('fee_id', ids).order('created_at'), sb().from('fee_instalments').select('*').in('fee_id', ids).order('due_on'), sb().from('fee_payments').select('*').in('fee_id', ids).order('paid_on')]) : [{}, {}, {}];
  const I = it.data || [], N = ins.data || [], Y = pay.data || [], C = {}; (St.classes || []).forEach(c => C[c.id] = c);
  St.fdoc = { p, fees, I, N, Y };
  const bal = fees.reduce((s, f) => s + cents(f.amount) - cents(f.paid), 0) / 100, cur = (fees[0] || {}).currency_code || '';
  const open = fees.filter(f => cents(f.amount) > cents(f.paid));
  const d = document.querySelector('.drawer') || document.createElement('div'); d.className = 'drawer';
  d.innerHTML = `<div><div class="row" style="justify-content:space-between;align-items:flex-start"><div><h2 style="margin:0">${p.first_name ? nm(p) : 'Student'}</h2><p class="sub" style="margin:4px 0 0">${esc(p.admission_no || '')} ${esc((C[p.class_id] || {}).name || '')} • balance <b>${bal < 0 ? 'credit ' + money(-bal, cur) : money(bal, cur)}</b></p></div><div class="row" style="gap:6px"><button class="g" type="button" data-a="fprint">Print statement</button><button class="g" type="button" data-a="closedr">Close</button></div></div>
${fees.length ? `<h3 style="margin-top:16px">Record a payment</h3><form data-f="fpay"><div class="row"><label>Invoice<select name="fee">${(open.length ? open : fees).map(f => opt(f.id, f.term + ' (owes ' + money((cents(f.amount) - cents(f.paid)) / 100) + ')')).join('')}</select></label><label>Amount<input name="amount" type="number" min="0.01" step="0.01" required value="${open[0] ? (cents(open[0].amount) - cents(open[0].paid)) / 100 : ''}"></label></div>
<div class="row"><label>Date<input name="paid_on" type="date" value="${today()}" max="${today()}"></label><label>Method<select name="method">${Object.keys(METHOD).map(k => opt(k, METHOD[k])).join('')}</select></label><label>Reference<input name="reference" maxlength="80" placeholder="Bank or mobile money reference"></label></div><button class="b">Record and issue receipt</button></form>` : '<p class="muted">No invoices for this student yet.</p>'}
${fees.map(f => { const its = I.filter(x => x.fee_id === f.id), ns = N.filter(x => x.fee_id === f.id), ys = Y.filter(x => x.fee_id === f.id), b = (cents(f.amount) - cents(f.paid)) / 100;
  return `<div style="border-top:1px solid var(--border);margin-top:18px;padding-top:12px"><h3 style="margin:0 0 6px">${esc(f.term)} <small class="muted">${esc(f.currency_code)}</small><span class="sp" style="float:right"><span class="pill ${b <= 0 ? 'ok' : 'bad'}">${b <= 0 ? (b < 0 ? 'Credit ' + money(-b) : 'Paid') : 'Owes ' + money(b)}</span></span></h3>
${pairs(its.map(x => [esc(x.label), money(x.amount)]).concat([['Total', money(f.amount), 1]]))}
<form data-f="fitem" data-id="${f.id}" class="row"><label style="flex:3 1 160px">Add an item or discount<input name="label" maxlength="80" required placeholder="e.g. Sibling discount"></label><label style="flex:1 1 100px">Amount<input name="amount" type="number" step="0.01" required placeholder="-5000"></label><button class="g">Add</button></form>
${ns.length ? `<p class="sub" style="margin:10px 0 4px">Instalments</p>${pairs(ns.map(x => [day(x.due_on) + (x.due_on <= today() ? ' <small class="muted">(due)</small>' : ''), money(x.amount)]))}` : f.due_on ? `<p class="sub">Due ${day(f.due_on)}</p>` : ''}
<p class="sub" style="margin:10px 0 4px">Payments</p>${ys.length ? `<div class="lst">${ys.map(x => `<div class="it" ${x.voided_at ? 'style="opacity:.55"' : ''}><div class="m"><b>${x.voided_at ? `<s>${money(x.amount)}</s>` : money(x.amount)}</b><small>${esc(x.receipt_no)} • ${day(x.paid_on)} • ${METHOD[x.method] || esc(x.method)}${x.reference ? ' • ' + esc(x.reference) : ''}${x.voided_at ? ' • void: ' + esc(x.void_reason || '') : ''}</small></div>${x.voided_at ? '' : `<button class="g" data-a="freceipt" data-id="${x.id}">Receipt</button><button class="g" data-a="fvoid" data-id="${x.id}">Void</button>`}</div>`).join('')}</div>` : '<p class="muted">None yet.</p>'}</div>`; }).join('')}<div id="fvoidc"></div></div>`;
  if (!d.parentNode) document.body.appendChild(d);
};
F.fpay = async d => {
  const r = must(await sb().rpc('record_payment', { p_fee: d.fee, p_amount: cents(d.amount) / 100, p_paid_on: d.paid_on || null, p_method: d.method, p_reference: d.reference || null }));
  toast('Recorded. Receipt ' + r.receipt_no + '.'); await A.fstmt({ dataset: { id: St.fsid } }); A.freceipt({ dataset: { id: r.id } }, true); T.go();
};
F.fitem = async (d, f) => { must(await sb().from('fee_items').insert({ fee_id: f.dataset.id, label: d.label.trim(), amount: cents(d.amount) / 100 })); toast('Added.'); await A.fstmt({ dataset: { id: St.fsid } }); T.go(); };
A.fvoid = el => { const c = document.getElementById('fvoidc'); c.innerHTML = `<div class="card" style="margin-top:14px;border-color:var(--red)"><h3>Void this payment?</h3><p class="sub">The receipt stays on the record, crossed out, and the balance goes back up. Use this for a bounced cheque or a mistake.</p><form data-f="fvoidok" data-id="${el.dataset.id}"><label>Reason<input name="reason" required maxlength="300"></label><button class="b">Void payment</button> <button class="g" type="button" data-a="fvoidno">Keep it</button></form></div>`; c.scrollIntoView({ behavior: 'smooth' }); };
A.fvoidno = () => { document.getElementById('fvoidc').innerHTML = ''; };
F.fvoidok = async (d, f) => { must(await sb().rpc('void_payment', { p_payment: f.dataset.id, p_reason: d.reason })); toast('Payment voided.'); await A.fstmt({ dataset: { id: St.fsid } }); T.go(); };

A.freceipt = (el, ask) => {
  const D = St.fdoc; if (!D) return; const y = D.Y.find(x => x.id === el.dataset.id); if (!y) return; const f = D.fees.find(x => x.id === y.fee_id) || {};
  const html = head('Receipt ' + y.receipt_no, day(y.paid_on)) + `<p>Received from <b>${esc(D.p.first_name + ' ' + D.p.surname)}</b>${D.p.admission_no ? ' (' + esc(D.p.admission_no) + ')' : ''} the sum of <b>${money(y.amount, f.currency_code)}</b> for ${esc(f.term)} fees, by ${esc((METHOD[y.method] || y.method).toLowerCase())}${y.reference ? ', reference ' + esc(y.reference) : ''}.</p><table><tr><th>Term total</th><td class="n">${money(f.amount)}</td></tr><tr><th>Paid to date</th><td class="n">${money(f.paid)}</td></tr><tr><th>Balance</th><td class="n">${money((cents(f.amount) - cents(f.paid)) / 100)}</td></tr></table><p style="margin-top:40px">Signed ____________________ for ${esc((T.school || {}).name || '')}</p>`;
  if (ask === true) { const c = document.getElementById('fvoidc'); if (c) { c.innerHTML = `<div class="note" style="margin-top:14px">Receipt ${esc(y.receipt_no)} is ready. <button class="g" data-a="freceipt" data-id="${y.id}">Print receipt</button></div>`; c.scrollIntoView({ behavior: 'smooth' }); } return; }
  printDoc(html);
};
A.fprint = () => {
  const D = St.fdoc; if (!D) return; const s = T.school || {};
  let run = 0; const lines = [];
  D.fees.forEach(f => { lines.push([f.created_at.slice(0, 10), 'Invoice: ' + f.term, cents(f.amount), 0]);
    D.Y.filter(y => y.fee_id === f.id && !y.voided_at).forEach(y => lines.push([y.paid_on, 'Payment, receipt ' + y.receipt_no, 0, cents(y.amount)])); });
  lines.sort((a, b) => a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0);
  const cur = (D.fees[0] || {}).currency_code || '';
  const html = head('Fee statement', esc(D.p.first_name + ' ' + D.p.surname) + (D.p.admission_no ? '<br>' + esc(D.p.admission_no) : '')) +
    `<table><tr><th>Date</th><th>Details</th><th class="n">Charged</th><th class="n">Paid</th><th class="n">Balance</th></tr>${lines.map(l => { run += l[2] - l[3]; return `<tr><td>${day(l[0])}</td><td>${esc(l[1])}</td><td class="n">${l[2] ? money(l[2] / 100) : ''}</td><td class="n">${l[3] ? money(l[3] / 100) : ''}</td><td class="n">${money(run / 100)}</td></tr>`; }).join('')}</table>
<p><b>Balance ${run < 0 ? 'in credit' : 'due'}: ${money(Math.abs(run) / 100, cur)}</b></p>${D.N.filter(n => n.due_on > today()).length ? `<p>Coming instalments: ${D.N.filter(n => n.due_on > today()).map(n => day(n.due_on) + ' ' + money(n.amount)).join('; ')}</p>` : ''}${s.fee_note ? `<p style="white-space:pre-wrap;border:1px solid #999;padding:8px">${esc(s.fee_note)}</p>` : ''}`;
  printDoc(html);
};

/* ---------- receipts log ---------- */
async function receipts(P) {
  const from = St.rfrom || new Date(Date.now() - 30 * 864e5).toISOString().slice(0, 10), to = St.rto || today();
  const y = must(await sb().from('fee_payments').select('*').eq('school_id', me().school_id).gte('paid_on', from).lte('paid_on', to).order('paid_on', { ascending: false }).limit(5000)) || [];
  St.rlog = y; const ok = y.filter(x => !x.voided_at), by = {}; ok.forEach(x => by[x.method] = (by[x.method] || 0) + cents(x.amount));
  return `<div class="card"><h2>Receipts<span class="sp row" style="gap:6px"><input type="date" data-a="rfrom" value="${from}" style="margin:0;width:auto"><input type="date" data-a="rto" value="${to}" style="margin:0;width:auto"><button class="g" data-a="csvrec">Export CSV</button></span></h2>
<p class="sub">Collected ${money(ok.reduce((s, x) => s + cents(x.amount), 0) / 100)} in ${ok.length} payment${ok.length === 1 ? '' : 's'}${Object.keys(by).length ? ': ' + Object.keys(by).map(k => METHOD[k] + ' ' + money(by[k] / 100)).join(', ') : ''}.</p>
${table(['Receipt', 'Date', 'Student', 'Method', 'Amount'], y.map(x => { const p = P[x.student_id] || {}; return `<tr class="click" data-a="fstmt" data-id="${x.student_id}" ${x.voided_at ? 'style="opacity:.55"' : ''}><td>${esc(x.receipt_no)}</td><td>${day(x.paid_on)}</td><td>${p.first_name ? nm(p) : ''}</td><td>${METHOD[x.method] || ''}</td><td class="n">${x.voided_at ? '<s>' + money(x.amount) + '</s> void' : money(x.amount)}</td></tr>`; }), 'No payments in these dates.')}</div>`;
}
A.rfrom = el => { St.rfrom = el.value; T.go(); };
A.rto = el => { St.rto = el.value; T.go(); };

/* ---------- settings and exports ---------- */
function feeSettings(s) {
  return `<div class="card"><h2>Fee settings</h2><form data-f="fset"><label>Usual currency<input name="fee_currency" maxlength="3" value="${esc(s.fee_currency || '')}" placeholder="NGN" style="text-transform:uppercase;max-width:140px"></label>
<label>Printed at the bottom of every statement (bank details, how to pay, the bursar's phone)<textarea name="fee_note" maxlength="600">${esc(s.fee_note || '')}</textarea></label><button class="b">Save</button></form></div>`;
}
F.fset = async d => { const row = { fee_currency: (d.fee_currency || '').toUpperCase().replace(/[^A-Z]/g, '').slice(0, 3) || null, fee_note: d.fee_note || null };
  if (row.fee_currency && row.fee_currency.length !== 3) throw new Error('Use a three-letter currency code such as NGN.');
  must(await sb().from('schools').update(row).eq('id', me().school_id)); Object.assign(T.school, row); toast('Saved.'); };
A.csvfees = async () => { const { fees, P, inst } = await load(); saveCsv('invoices.csv', csv([['Admission no.', 'Student', 'Term', 'Currency', 'Total', 'Paid', 'Balance', 'Overdue', 'Due']].concat(fees.map(f => { const p = P[f.student_id] || {}; return [p.admission_no, p.first_name ? p.first_name + ' ' + p.surname : '', f.term, f.currency_code, f.amount, f.paid, (cents(f.amount) - cents(f.paid)) / 100, overdue(f, inst), f.due_on]; })))); };
A.csvdebt = async () => { const { fees, P, inst } = await load(), by = {}; fees.forEach(f => { const b = cents(f.amount) - cents(f.paid); if (b <= 0) return; const x = by[f.student_id] = by[f.student_id] || [0, 0, f.currency_code]; x[0] += b; x[1] += cents(overdue(f, inst)); });
  saveCsv('who-owes.csv', csv([['Admission no.', 'Student', 'Currency', 'Balance', 'Overdue']].concat(Object.keys(by).map(id => { const p = P[id] || {}; return [p.admission_no, p.first_name ? p.first_name + ' ' + p.surname : '', by[id][2], by[id][0] / 100, by[id][1] / 100]; })))); };
A.csvrec = () => saveCsv('receipts.csv', csv([['Receipt', 'Date', 'Method', 'Reference', 'Amount', 'Void reason']].concat((St.rlog || []).map(x => [x.receipt_no, x.paid_on, METHOD[x.method], x.reference, x.amount, x.void_reason || '']))));
})();
