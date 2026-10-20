/* Study friends: add a friend with their private code, see their streak and whether they studied today,
   keep a friend streak going together, and send one friendly nudge a day. Backed by migration 0018.
   Registers V.friends and AceF.banner() (the "X nudged you" card on the home page). Actions use data-f. */
(function () {
  'use strict';
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));
  const es = () => UIL() === 'es', L = (a, b) => TX(a, b);
  const signed = () => !!(window.AceSync && AceSync.signedIn && AceSync.signedIn());
  const F = window.AceF = { list: null, code: '', add: '', busy: false, err: '', ok: '', nudges: null, confirm: null };
  const rpc = (n, a) => AceSync.rpc(n, a);
  const msg = e => (e && (e.msg || e.message)) || L('Something went wrong. Try again.', 'Algo salió mal.');
  function load() {
    if (!signed()) return Promise.resolve();
    return Promise.all([rpc('my_friends'), F.code ? F.code : rpc('my_friend_code')]).then(([l, c]) => { F.list = l || []; F.code = c || F.code; })
      .catch(e => { F.err = msg(e); F.list = F.list || []; });
  }
  F.banner = function () {
    if (!signed()) return '';
    if (F.nudges === null) { F.nudges = []; rpc('my_nudges').then(r => { F.nudges = (r || []).map(x => x.name); if (F.nudges.length && S.tab === 'home') render(); }).catch(() => { }); return ''; }
    if (!F.nudges.length || S.playedToday) return '';
    const who = F.nudges.length === 1 ? esc(F.nudges[0]) : esc(F.nudges.slice(0, -1).join(', ')) + L(' and ', ' y ') + esc(F.nudges.slice(-1)[0]);
    return `<button class="ban lt fr-ban" data-a="tab" data-v="daily"><span class="ic">👋</span><span><b>${who} ${L('nudged you to study today', 'te recuerda estudiar hoy')}</b><span>${L('Do today’s challenge to keep your friend streak going.', 'Haz el reto de hoy para mantener vuestra racha.')}</span></span><em>›</em></button>`;
  };
  function view() {
    const back = `<div class="bk"><button class="bb" data-a="tab" data-v="tools">‹ ${L('Back', 'Atrás')}</button></div>`;
    let h = `<div class="pad">${back}<h2 style="margin:0 0 4px">${L('Study friends', 'Amigos de estudio')}</h2><p class="note" style="margin:0 0 12px">${L('Study with friends to stay on track. Friends see only your first name, your streak and whether you studied today.', 'Estudia con amigos. Solo ven tu nombre, tu racha y si has estudiado hoy.')}</p>`;
    if (!signed()) return h + `<div class="emp2">${L('Sign in to add friends.', 'Inicia sesión para añadir amigos.')}</div><a class="nx" style="display:block;text-align:center;text-decoration:none" href="${LOGIN()}">${L('Sign in', 'Iniciar sesión')}</a></div>`;
    if (F.list === null) { load().then(() => { if (S.tab === 'friends') render(); }); return h + `<p class="note">${L('Loading…', 'Cargando…')}</p></div>`; }
    const inc = F.list.filter(f => f.status === 'pending' && f.incoming), out = F.list.filter(f => f.status === 'pending' && !f.incoming), acc = F.list.filter(f => f.status === 'accepted');
    h += `<div class="card fr-code"><small>${L('Your friend code', 'Tu código de amigo')}</small><b>${esc(F.code.replace(/(.{4})/, '$1 '))}</b><div class="fr-cb"><button class="bb" data-f="copy">${L('Copy', 'Copiar')}</button>${navigator.share ? `<button class="bb" data-f="share">${L('Share', 'Compartir')}</button>` : ''}</div><p class="note" style="margin:6px 0 0">${L('Share it only with people you know.', 'Compártelo solo con personas que conoces.')}</p></div>
<div class="fr-add"><input class="xin" data-f-in="add" value="${esc(F.add)}" placeholder="${L('Friend’s code, e.g. K7M2 QX9A', 'Código de tu amigo')}" maxlength="12" autocapitalize="characters" aria-label="${L('Friend’s code', 'Código')}"><button class="nx" data-f="add" ${F.busy ? 'disabled' : ''}>${L('Add', 'Añadir')}</button></div>${F.err ? `<p class="note" style="color:var(--red)">${esc(F.err)}</p>` : ''}${F.ok ? `<p class="note" style="color:var(--green)">${esc(F.ok)}</p>` : ''}`;
    if (inc.length) h += `<div class="sh">${L('Friend requests', 'Solicitudes')}</div><div class="lst">${inc.map(f => `<div class="li"><span class="e">🙋</span><span class="m"><b>${esc(f.name)}</b><small>${L('wants to study with you', 'quiere estudiar contigo')}</small></span><button class="bb" data-f="yes" data-v="${f.friend_id}">${L('Accept', 'Aceptar')}</button><button class="bb" data-f="no" data-v="${f.friend_id}">✕</button></div>`).join('')}</div>`;
    h += `<div class="sh">${L('Friends', 'Amigos')} (${acc.length})</div>`;
    h += acc.length ? `<div class="lst">${acc.map(f => `<div class="li fr-row"><span class="e">${f.studied_today ? '✅' : '⏳'}</span><span class="m"><b>${esc(f.name)}</b><small>🔥 ${f.streak} • ${f.studied_today ? L('studied today', 'ha estudiado hoy') : L('not yet today', 'aún no hoy')} • ${f.week_xp} XP ${L('this week', 'esta semana')}</small>${f.friend_streak ? `<small class="fr-st">🤝 ${f.friend_streak} ${f.friend_streak === 1 ? L('day together', 'día juntos') : L('days together', 'días juntos')}</small>` : ''}${f.nudged_me ? `<small class="fr-st">👋 ${L('nudged you today', 'te ha recordado hoy')}</small>` : ''}</span>
${f.studied_today ? '' : `<button class="bb" data-f="nudge" data-v="${f.friend_id}" ${f.nudged_today ? 'disabled' : ''}>${f.nudged_today ? L('Nudged', 'Enviado') : '👋 ' + L('Nudge', 'Recordar')}</button>`}<button class="bb fr-x" data-f="rm" data-v="${f.friend_id}" aria-label="${L('Remove friend', 'Quitar amigo')}">${F.confirm === f.friend_id ? L('Remove?', '¿Quitar?') : '⋯'}</button></div>`).join('')}</div>`
      : `<div class="emp2">${L('No friends yet. Share your code, or add a friend’s code above. Studying with a friend makes it much easier to keep going.', 'Aún no tienes amigos. Comparte tu código o añade el de un amigo.')}</div>`;
    if (out.length) h += `<div class="sh">${L('Waiting for them to accept', 'Pendientes')}</div><div class="lst">${out.map(f => `<div class="li"><span class="e">✉️</span><span class="m"><b>${esc(f.name)}</b><small>${L('Request sent', 'Solicitud enviada')}</small></span><button class="bb" data-f="no" data-v="${f.friend_id}">${L('Cancel', 'Cancelar')}</button></div>`).join('')}</div>`;
    return h + `<p class="note">${L('A friend streak counts the days in a row you both studied. A nudge is a friendly reminder; you can send one a day to each friend.', 'Una racha de amigos cuenta los días seguidos en que ambos estudiasteis.')}</p></div>`;
  }
  const act = p => { F.busy = true; F.err = ''; F.ok = ''; render(); return p.then(() => load()).catch(e => { F.err = msg(e); }).then(() => { F.busy = false; render(); }); };
  document.addEventListener('click', e => {
    const b = e.target.closest && e.target.closest('[data-f]'); if (!b) return; const k = b.dataset.f, v = b.dataset.v; e.preventDefault();
    if (k === 'copy') (navigator.clipboard ? navigator.clipboard.writeText(F.code) : Promise.reject()).then(() => toast(L('Code copied', 'Código copiado'))).catch(() => toast(F.code));
    else if (k === 'share') navigator.share({ text: L('Study with me on Ace. My friend code is ', 'Estudia conmigo en Ace. Mi código es ') + F.code, url: location.origin + location.pathname }).catch(() => { });
    else if (k === 'add') { const c = F.add.trim(); if (!c) return; act(rpc('add_friend', { p_code: c }).then(r => { if (typeof r === 'string' && r.startsWith('error:')) throw { msg: TRL(r.slice(6)) }; F.add = ''; F.ok = r === 'accepted' ? L('You are now friends.', 'Ya sois amigos.') : r === 'already' ? L('You are already friends.', 'Ya sois amigos.') : L('Request sent. It shows up when they accept.', 'Solicitud enviada.'); })).then(() => { if (F.ok) F.err = ''; }); }
    else if (k === 'yes') act(rpc('respond_friend', { p_other: v, p_accept: true }));
    else if (k === 'no') act(rpc('respond_friend', { p_other: v, p_accept: false }));
    else if (k === 'nudge') act(rpc('nudge_friend', { p_other: v }).then(() => { toast(L('Nudge sent 👋', 'Recordatorio enviado 👋')); }));
    else if (k === 'rm') { if (F.confirm !== v) { F.confirm = v; render(); return; } F.confirm = null; act(rpc('remove_friend', { p_other: v })); }
  });
  document.addEventListener('input', e => { const el = e.target.closest && e.target.closest('[data-f-in]'); if (el) F.add = el.value; });
  document.addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.dataset && e.target.dataset.fIn === 'add') { const b = document.querySelector('[data-f=add]'); if (b) b.click(); } });
  Object.assign(V, { friends: view });
})();
