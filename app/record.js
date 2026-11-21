/* Ace "My results" for students whose school uses Ace: published term reports, school fees and transcripts.
   Schools publish these in /staff/. Students only ever see their own, published records (Postgres RLS). Loaded after class.js. */
(function () {
  'use strict';
  if (!window.AceX || !AceX.h) return;
  const { L, esc, back, needSignIn, signedIn, sync } = AceX.h, X = AceX;
  const R = window.AceR = { reps: null, res: [], terms: {}, fees: [], pays: [], tr: [], open: '', purpose: '', busy: false, err: '', ok: '' };
  const msg = e => (e && (e.msg || e.message)) || L('Something went wrong. Try again.', 'Algo salió mal.');
  const n1 = v => v == null ? '–' : (+v).toLocaleString(undefined, { maximumFractionDigits: 1 });
  const money = (v, c) => (c ? c + ' ' : '') + (+v || 0).toLocaleString(undefined, { maximumFractionDigits: 2 });
  const day = d => d ? new Date(String(d).length === 10 ? d + 'T00:00:00' : d).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' }) : '';
  const ord = n => n + (['th', 'st', 'nd', 'rd'][(n % 100 - 20) % 10] || ['th', 'st', 'nd', 'rd'][n % 100] || 'th');
  const verify = c => location.pathname.replace(/app\/.*$/, '') + 'verify/?code=' + c;

  function view() {
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('My results', 'Mis resultados')}</h2><p class="note" style="margin-top:0">${L('Term reports, fees and transcripts from your school.', 'Boletines, cuotas y certificados de tu colegio.')}</p>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (!R.reps) return h + (R.err ? `<p class="note" style="color:var(--red)">${esc(R.err)}</p>` : '<p class="note">…</p>') + '</div>';
    if (R.err) h += `<p class="note" style="color:var(--red)">${esc(R.err)}</p>`;
    if (R.ok) h += `<p class="note" style="color:var(--green)">${esc(R.ok)}</p>`;
    // term reports
    h += `<div class="sh">${L('Term reports', 'Boletines')}</div>`;
    if (!R.reps.length) h += `<p class="note">${L('Your school has not published a term report for you yet.', 'Tu colegio aún no ha publicado boletines.')}</p>`;
    h += R.reps.map(r => { const t = R.terms[r.term_id] || {}, mine = R.res.filter(x => x.term_id === r.term_id).sort((a, b) => a.subject.localeCompare(b.subject)), op = R.open === r.id;
      return `<div class="card" style="margin:8px 0"><button class="li" data-r="open" data-v="${r.id}" style="width:100%;border:0;background:none;padding:0"><span class="m"><b>${esc(t.name || '')}</b><small>${esc(r.class_name || '')} • ${L('Average', 'Media')} ${n1(r.average)}${r.position ? ' • ' + ord(r.position) + ' ' + L('of', 'de') + ' ' + r.class_size : ''}</small></span><span>${op ? '▴' : '▾'}</span></button>
${op ? `<table style="width:100%;border-collapse:collapse;margin-top:10px">${mine.map(x => `<tr style="border-top:1px solid var(--line)"><td style="padding:6px 0">${esc(x.subject)}</td><td style="text-align:right">${n1(x.score)}</td><td style="text-align:right;width:48px"><b>${esc(x.grade || '')}</b></td></tr>`).join('')}</table>
${r.attendance_pct != null ? `<p class="note">${L('Attendance', 'Asistencia')} ${Math.round(r.attendance_pct)}%</p>` : ''}${r.teacher_comment ? `<p style="margin:6px 0"><b>${L('Class teacher', 'Tutor')}:</b> ${esc(r.teacher_comment)}</p>` : ''}${r.head_comment ? `<p style="margin:6px 0"><b>${L('Head of school', 'Dirección')}:</b> ${esc(r.head_comment)}</p>` : ''}` : ''}</div>`; }).join('');
    // fees
    if (R.fees.length) {
      const bal = R.fees.reduce((s, f) => s + Math.round(f.amount * 100) - Math.round(f.paid * 100), 0) / 100, cur = R.fees[0].currency_code;
      h += `<div class="sh">${L('School fees', 'Cuotas')}</div><div class="card"><b>${bal > 0 ? L('Balance', 'Saldo') + ' ' + money(bal, cur) : bal < 0 ? L('In credit', 'A favor') + ' ' + money(-bal, cur) : L('All paid', 'Todo pagado')}</b>
${R.fees.map(f => `<p style="margin:8px 0 0">${esc(f.term)}: ${money(f.paid)} ${L('of', 'de')} ${money(f.amount, f.currency_code)}${f.due_on && +f.paid < +f.amount ? ` • ${L('due', 'vence')} ${day(f.due_on)}` : ''}</p>`).join('')}
${R.pays.length ? `<p class="note" style="margin-top:8px">${L('Last payment', 'Último pago')}: ${money(R.pays[0].amount)} ${day(R.pays[0].paid_on)} (${esc(R.pays[0].receipt_no)})</p>` : ''}<p class="note">${L('Pay the school directly. Ace only shows the record.', 'Paga al colegio directamente. Ace solo muestra el registro.')}</p></div>`;
    }
    // transcripts
    h += `<div class="sh">${L('Transcripts', 'Certificados de notas')}</div>`;
    h += R.tr.map(t => `<div class="card" style="margin:8px 0"><b>${t.status === 'issued' ? (t.revoked_at ? L('Withdrawn by the school', 'Retirado por el colegio') : L('Issued', 'Emitido') + ' ' + day(t.decided_at)) : t.status === 'requested' ? L('Requested', 'Solicitado') + ' ' + day(t.requested_at) : L('Declined', 'Rechazado')}</b>${t.purpose ? `<small> • ${esc(t.purpose)}</small>` : ''}
${t.status === 'issued' && !t.revoked_at ? `<p style="margin:6px 0">${L('Code', 'Código')} <b style="letter-spacing:.06em">${esc(t.code)}</b></p><a class="nx" style="display:inline-block;text-decoration:none" href="${esc(verify(t.code))}" target="_blank" rel="noopener">${L('Open, print or share', 'Abrir, imprimir o compartir')}</a>` : ''}${t.status === 'declined' && t.decline_reason ? `<p class="note">${esc(t.decline_reason)}</p>` : ''}</div>`).join('');
    const waiting = R.tr.some(t => t.status === 'requested');
    if (R.reps.length && !waiting) h += `<div class="card"><label class="xl">${L('What is it for? (optional)', '¿Para qué es? (opcional)')}<input class="xin" maxlength="200" data-r-in="purpose" value="${esc(R.purpose)}" placeholder="${L('University application', 'Solicitud a la universidad')}"></label><button class="nx" data-r="req" ${R.busy ? 'disabled' : ''}>${L('Ask my school for a transcript', 'Pedir certificado al colegio')}</button><p class="note">${L('Your school checks it and issues a transcript with a code that universities and employers can verify.', 'Tu colegio lo revisa y emite un certificado con un código verificable.')}</p></div>`;
    else if (!R.reps.length) h += `<p class="note">${L('You can ask for a transcript once your school publishes a term report.', 'Podrás pedirlo cuando tu colegio publique un boletín.')}</p>`;
    return h + '</div>';
  }

  const load = () => {
    R.err = '';
    const t = n => sync().table(n);
    return Promise.all([
      t('term_reports').then(q => q.select('id,term_id,class_name,average,position,class_size,attendance_pct,teacher_comment,head_comment').not('published_at', 'is', null)),
      t('term_results').then(q => q.select('term_id,subject,score,grade')),
      t('academic_terms').then(q => q.select('id,name,starts_on')),
      t('fees').then(q => q.select('id,term,amount,paid,currency_code,due_on').order('created_at')),
      t('fee_payments').then(q => q.select('amount,paid_on,receipt_no').is('voided_at', null).order('paid_on', { ascending: false }).limit(1)),
      t('transcripts').then(q => q.select('id,status,purpose,code,requested_at,decided_at,decline_reason,revoked_at').order('requested_at', { ascending: false }))
    ]).then(([a, b, c, d, e, f]) => {
      R.terms = {}; (c.data || []).forEach(x => R.terms[x.id] = x);
      R.reps = (a.data || []).sort((x, y) => String((R.terms[y.term_id] || {}).starts_on).localeCompare(String((R.terms[x.term_id] || {}).starts_on)));
      R.res = b.data || []; R.fees = d.data || []; R.pays = e.data || []; R.tr = f.data || [];
      if (!R.open && R.reps[0]) R.open = R.reps[0].id;
    }).catch(er => { R.reps = R.reps || []; R.err = msg(er); });
  };

  Object.assign(V, { myrec: view });
  X.loaders.myrec = load;
  document.addEventListener('input', e => { const k = e.target && e.target.dataset && e.target.dataset.rIn; if (k === 'purpose') R.purpose = e.target.value; });
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-r]'); if (!b) return; const a = b.dataset.r;
    if (a === 'open') { R.open = R.open === b.dataset.v ? '' : b.dataset.v; render(); }
    else if (a === 'req') { R.busy = true; R.err = R.ok = ''; render();
      sync().rpc('request_transcript', { p_purpose: R.purpose.trim() || null }).then(() => { R.ok = L('Request sent to your school.', 'Solicitud enviada.'); R.purpose = ''; return load(); })
        .catch(er => { R.err = msg(er); }).then(() => { R.busy = false; render(); }); }
  });
})();
