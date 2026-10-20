/* Ace chat: a full chat interface for the AI tutor with saved conversations.
   - Every conversation is saved on the device (localStorage 'ace-chats') and, when the student is signed in,
     in Supabase table ai_chats (migration 0017), so chats follow them to other devices.
   - Entry points elsewhere in the app (Ask Ace buttons, "Ask about this question", AI tools) call AceChat.adopt(),
     which turns the old one-off context into a new saved chat and opens it.
   Loaded after the main script; registers V.chat. Click actions use data-h, inputs use data-h-in. */
(function () {
  'use strict';
  const KEY = 'ace-chats', MAX = 120, PORTAL = window.ACE_MODE === 'campus' ? 'campus' : 'school';
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));
  const es = () => !!(C[S.c] && C[S.c].l), L = (a, b) => es() ? b : a;
  const uid = () => (crypto.randomUUID ? crypto.randomUUID() : 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => { const r = Math.random() * 16 | 0; return (c === 'x' ? r : (r & 3 | 8)).toString(16) }));
  const signed = () => !!(window.AceSync && AceSync.signedIn && AceSync.signedIn());
  const MODES = {
    buddy: { i: '💬', n: () => L('Study buddy', 'Compañero'), ph: () => L('Ask Ace anything about your studies', 'Pregunta lo que quieras'), st: () => [L('Explain this topic simply: ', 'Explícame este tema: '), L('Quiz me on ', 'Hazme preguntas sobre '), L('What are the most common mistakes in ', 'Errores comunes en '), L('Make me a 30-minute revision plan for ', 'Hazme un plan de repaso de 30 minutos para ')] },
    tutor: { i: '🧠', n: () => L('Tutor mode', 'Modo tutor'), ph: () => L('What are you stuck on? Ace gives hints, not answers', '¿En qué te has atascado?'), st: () => [L('I am stuck on this question: ', 'Me he atascado en: '), L('Check my working: ', 'Revisa mi procedimiento: ')] },
    solver: { i: '🔬', n: () => L('Smart solver', 'Solucionador'), ph: () => L('Type a maths or science problem', 'Escribe un problema'), st: () => [L('Solve step by step: ', 'Resuelve paso a paso: '), L('Explain the formula for ', 'Explica la fórmula de ')] },
    essay: { i: '✍️', n: () => L('Essay feedback', 'Redacciones'), ph: () => L('Paste your essay or long answer', 'Pega tu redacción'), st: () => [], long: 1 },
    markscheme: { i: '✅', n: () => L('Mark my answer', 'Corrige mi respuesta'), ph: () => L('Paste the question, your answer and the mark scheme', 'Pega la pregunta y tu respuesta'), st: () => [], long: 1 },
    qgen: { i: '📄', n: () => L('Make questions', 'Crear preguntas'), ph: () => L('Paste your notes and Ace writes practice questions', 'Pega tus apuntes'), st: () => [], long: 1 }
  };
  const H = window.AceChat = { list: [], cur: null, q: '', busy: false, err: '', pane: 'list', menu: null, edit: null, draft: '', loaded: false };

  /* ---------- storage ---------- */
  function loadLocal() { try { H.list = JSON.parse(localStorage.getItem(KEY) || '[]') } catch (e) { H.list = [] } if (!Array.isArray(H.list)) H.list = [] }
  function saveLocal() {
    H.list.sort((a, b) => (b.pinned - a.pinned) || (b.updated > a.updated ? 1 : -1));
    const keep = H.list.slice(0, MAX);
    for (let n = keep.length; n > 0; n--) { try { localStorage.setItem(KEY, JSON.stringify(keep.slice(0, n))); return } catch (e) { /* quota: drop the oldest and retry */ } }
  }
  const row = c => ({ id: c.id, title: c.title.slice(0, 120), portal: c.portal, mode: c.mode, subject: (c.s || '').slice(0, 80) || null, exam: (c.ex || '').slice(0, 80) || null, topic: (c.topic || '').slice(0, 200) || null, extra: (c.extra || '').slice(0, 2000) || null, turns: c.turns.slice(-400).map((t, i, all) => Object.assign({ role: t.role, content: t.content, t: t.t }, t.img && all.slice(i).filter(x => x.img).length <= 12 ? { img: t.img } : {})), pinned: !!c.pinned, updated_at: c.updated });
  function push(c) { if (!signed()) return; AceSync.table('ai_chats').then(q => q.upsert(row(c))).then(r => { if (r && r.error) console.warn(r.error.message) }).catch(() => { }) }
  function drop(id) { if (!signed()) return; AceSync.table('ai_chats').then(q => q.delete().eq('id', id)).catch(() => { }) }
  function pull() {
    if (!signed() || H.pulling) return; H.pulling = true;
    AceSync.table('ai_chats').then(q => q.select('id,title,portal,mode,subject,exam,topic,extra,turns,pinned,created_at,updated_at').order('updated_at', { ascending: false }).limit(MAX)).then(r => {
      H.pulling = false; if (!r || r.error || !r.data) return;
      const byId = {}; H.list.forEach(c => byId[c.id] = c);
      r.data.forEach(d => {
        const loc = byId[d.id], up = new Date(d.updated_at).toISOString();
        if (!loc || up > loc.updated) byId[d.id] = { id: d.id, title: d.title, portal: d.portal, mode: d.mode, s: d.subject || '', ex: d.exam || '', topic: d.topic || '', extra: d.extra || '', turns: d.turns || [], pinned: d.pinned, created: d.created_at, updated: up };
      });
      // local chats the server has never seen (made while signed out or offline) are uploaded
      const remote = new Set(r.data.map(d => d.id)); Object.values(byId).forEach(c => { if (!remote.has(c.id) && c.turns.length) push(c) });
      H.list = Object.values(byId); saveLocal(); if (S.tab === 'chat') render();
    }).catch(() => { H.pulling = false });
  }

  /* ---------- chats ---------- */
  const find = id => H.list.find(c => c.id === id);
  const cur = () => find(H.cur);
  function blank(mode, ctx) {
    const c = C[S.c], now = new Date().toISOString();
    return Object.assign({ id: uid(), title: L('New chat', 'Chat nuevo'), portal: PORTAL, mode: MODES[mode] ? mode : 'buddy', s: '', ex: c.x[S.x % c.x.length], topic: '', extra: '', turns: [], pinned: false, created: now, updated: now }, ctx || {});
  }
  function newChat(mode, ctx) { const ch = blank(mode, ctx); H.list.unshift(ch); H.cur = ch.id; H.pane = 'conv'; H.err = ''; H.draft = ''; return ch }
  H.adopt = function (first) {
    const A = S.ai; S.ai = null; if (!A) return;
    const ctx = { s: /^(All subjects|Todas)$/.test(A.s || '') ? '' : (A.s || ''), ex: A.ex || '', topic: A.mode ? '' : (A.topic || ''), extra: A.extra || '' };
    const ch = newChat(A.mode || 'buddy', ctx);
    if (ctx.topic) ch.title = ctx.topic;
    S.tab = 'chat'; if (first) setTimeout(() => send(first), 0);
  };
  function titleFrom(t) { const s = t.replace(/\s+/g, ' ').trim(); return s.length > 48 ? s.slice(0, 46).replace(/\s\S*$/, '') + '…' : s }

  async function send(text) {
    const ch = cur(), att = H.att; text = String(text || '').trim(); if (!ch || (!text && !att) || H.busy) return;
    if (!text) text = L('Help me with the question in this photo.', 'Ayúdame con la pregunta de esta foto.');
    H.err = ''; H.att = null; const first = !ch.turns.length;
    ch.turns.push(Object.assign({ role: 'user', content: text, t: Date.now() }, att ? { img: att.thumb } : {}));
    if (first && (ch.title === 'New chat' || ch.title === 'Chat nuevo')) ch.title = titleFrom(text);
    ch.updated = new Date().toISOString(); saveLocal(); H.busy = true; H.draft = ''; paint(true);
    try {
      if (!(ACE_CFG.aiUrl && ACE_CFG.getToken)) throw { msg: L('Sign in to chat with Ace.', 'Inicia sesión para hablar con Ace.') };
      const tok = await ACE_CFG.getToken(); if (!tok) throw { msg: L('Sign in to chat with Ace.', 'Inicia sesión para hablar con Ace.') };
      const msgs = ch.turns.slice(-20).map(m => ({ role: m.role, content: m.content }));
      while (msgs.length && msgs[0].role !== 'user') msgs.shift();
      if (ch.extra && msgs.length) msgs[0] = { role: 'user', content: L('Context: ', 'Contexto: ') + ch.extra + '\n\n' + msgs[0].content };
      const r = await fetch(ACE_CFG.aiUrl, { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + tok }, body: JSON.stringify({ messages: msgs, image: att ? { media_type: att.media_type, data: att.data } : undefined, context: { country: C[S.c].n, exam: ch.ex, subject: ch.s || L('All subjects', 'Todas'), topic: ch.topic || MODES[ch.mode].n(), mode: ch.mode === 'buddy' ? '' : ch.mode, lang: C[S.c].l || 'en', level: PORTAL === 'campus' ? 'university' : 'secondary' } }) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) throw { msg: j.error || L('Ace could not answer. Try again.', 'Ace no pudo responder. Inténtalo de nuevo.') };
      ch.turns.push({ role: 'assistant', content: j.reply, t: Date.now() }); H.cap = j.cap == null ? null : { used: j.used, cap: j.cap };
      try { window.AceUI && AceUI.fx && AceUI.fx('pop') } catch (e) { }
    } catch (e) { H.err = (e && e.msg) || L('Ace could not answer. Try again.', 'Ace no pudo responder.'); H.retry = text; if (att) { H.att = att; ch.turns.pop(); H.retry = null; H.draft = text } }
    H.busy = false; ch.updated = new Date().toISOString(); saveLocal(); push(ch); paint(true);
  }

  /* ---------- rendering ---------- */
  function md(s) {
    const blocks = String(s || '').split(/```/);
    return blocks.map((b, i) => {
      if (i % 2) return `<pre class="cm-code"><code>${esc(b.replace(/^\w*\n/, ''))}</code></pre>`;
      const lines = esc(b).split('\n'); let out = '', list = '';
      const inl = t => t.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/(^|[\s(])\*(\S(?:[^*\n]*\S)?)\*(?=[\s.,!?;:)]|$)/g, '$1<i>$2</i>').replace(/`([^`\n]+)`/g, '<code>$1</code>');
      const close = () => { if (list) { out += `</${list}>`; list = '' } };
      lines.forEach(l => {
        let m;
        if ((m = l.match(/^\s*[-*•]\s+(.*)/))) { if (list !== 'ul') { close(); out += '<ul>'; list = 'ul' } out += `<li>${inl(m[1])}</li>` }
        else if ((m = l.match(/^\s*(\d+)[.)]\s+(.*)/))) { if (list !== 'ol') { close(); out += `<ol start="${m[1]}">`; list = 'ol' } out += `<li>${inl(m[2])}</li>` }
        else if ((m = l.match(/^#{1,6}\s*(.*)/))) { close(); out += `<p><b>${inl(m[1])}</b></p>` }
        else if (!l.trim()) close();
        else { close(); out += `<p>${inl(l)}</p>` }
      });
      close(); return out;
    }).join('');
  }
  const when = iso => {
    const d = new Date(iso), n = new Date(), day = 864e5, a = new Date(n.getFullYear(), n.getMonth(), n.getDate()), diff = (a - new Date(d.getFullYear(), d.getMonth(), d.getDate())) / day;
    return diff <= 0 ? L('Today', 'Hoy') : diff === 1 ? L('Yesterday', 'Ayer') : diff < 7 ? L('Previous 7 days', 'Últimos 7 días') : diff < 30 ? L('Previous 30 days', 'Últimos 30 días') : L('Older', 'Anteriores');
  };
  function sideHTML() {
    const q = H.q.trim().toLowerCase();
    const items = H.list.filter(c => c.turns.length || c.id === H.cur).filter(c => !q || (c.title + ' ' + c.turns.map(t => t.content).join(' ')).toLowerCase().includes(q));
    let grp = '', h = '';
    items.forEach(c => {
      const g = c.pinned ? L('Pinned', 'Fijados') : when(c.updated);
      if (g !== grp) { grp = g; h += `<div class="ch-grp">${g}</div>` }
      const on = c.id === H.cur, open = H.menu === c.id;
      h += `<div class="ch-it${on ? ' on' : ''}"><button class="ch-pick" data-h="open" data-v="${c.id}"><span class="ch-mi">${MODES[c.mode] ? MODES[c.mode].i : '💬'}</span><span class="ch-tt">${H.edit === c.id ? '' : esc(c.title)}</span></button>${H.edit === c.id ? `<input class="ch-ren" data-h-in="ren" data-v="${c.id}" value="${esc(c.title)}" maxlength="120" aria-label="${L('Chat name', 'Nombre del chat')}">` : ''}<button class="ch-dots" data-h="menu" data-v="${c.id}" aria-label="${L('Chat options', 'Opciones')}" aria-expanded="${open}">⋯</button>
${open ? `<div class="ch-menu" role="menu"><button data-h="rename" data-v="${c.id}">✏️ ${L('Rename', 'Renombrar')}</button><button data-h="pin" data-v="${c.id}">📌 ${c.pinned ? L('Unpin', 'Desfijar') : L('Pin', 'Fijar')}</button><button data-h="del" data-v="${c.id}" class="dz">🗑️ ${L('Delete', 'Eliminar')}</button></div>` : ''}</div>`;
    });
    return `<div class="ch-sh"><b>${L('Chats', 'Chats')}</b><button class="ch-new" data-h="new">＋ ${L('New chat', 'Chat nuevo')}</button></div>
<input class="ch-q" type="search" data-h-in="q" value="${esc(H.q)}" placeholder="${L('Search your chats', 'Buscar en tus chats')}" aria-label="${L('Search your chats', 'Buscar')}">
<div class="ch-list">${h || `<p class="ch-none">${q ? L('No chats match.', 'Sin resultados.') : L('Your chats will appear here.', 'Tus chats aparecerán aquí.')}</p>`}</div>
<p class="ch-sync">${signed() ? '☁️ ' + L('Saved to your account', 'Guardado en tu cuenta') : '📱 ' + L('Saved on this device. Sign in to keep them everywhere.', 'Guardado en este dispositivo. Inicia sesión para tenerlos en todas partes.')}</p>`;
  }
  function msgsHTML(ch) {
    if (!ch.turns.length && !H.busy) {
      const m = MODES[ch.mode], st = m.st();
      return `<div class="ch-empty"><span class="ace" data-mood="wave"></span><h2>${ch.topic ? esc(ch.topic) : L('What shall we work on?', '¿En qué trabajamos?')}</h2><p>${ch.extra ? L('Ask anything about this question.', 'Pregunta lo que quieras sobre esta pregunta.') : m.ph()}</p>
<button class="ch-snap" data-h="snap">📷 ${L('Snap a question', 'Haz una foto a una pregunta')}<small>${L('Take a photo of homework or a past paper and Ace explains it', 'Haz una foto a los deberes y Ace te lo explica')}</small></button>
${st.length ? `<div class="ch-starts">${st.map((s, i) => `<button data-h="start" data-v="${i}">${esc(s.replace(/[: ]+$/, ''))}${/[: ]$/.test(s) ? '…' : ''}</button>`).join('')}</div>` : ''}</div>`;
    }
    return ch.turns.map((t, i) => t.role === 'user' ? `<div class="cm me"><div class="cm-b">${t.img ? `<img class="cm-img" src="${t.img}" alt="${L('Photo of a question', 'Foto de una pregunta')}">` : ''}${esc(t.content).replace(/\n/g, '<br>')}</div></div>`
      : `<div class="cm ai"><span class="cm-av"><i class="aic"></i></span><div class="cm-w"><div class="cm-b">${md(t.content)}</div><div class="cm-act"><button data-h="copy" data-v="${i}">${L('Copy', 'Copiar')}</button><button data-h="read" data-v="${i}">🔊 ${L('Read aloud', 'Leer')}</button>${i === ch.turns.length - 1 ? `<button data-h="again" data-v="${i}">↻ ${L('Try again', 'Otra vez')}</button>` : ''}</div></div></div>`).join('')
      + (H.busy ? `<div class="cm ai"><span class="cm-av"><i class="aic"></i></span><div class="cm-w"><div class="cm-b cm-dots" aria-label="${L('Ace is thinking', 'Ace está pensando')}"><i></i><i></i><i></i></div></div></div>` : '')
      + (H.err ? `<div class="cm-err" role="alert">${esc(H.err)}${H.retry ? ` <button data-h="retry">${L('Try again', 'Reintentar')}</button>` : ''}${/Sign in|Inicia/.test(H.err) ? ` <a href="../login/${PORTAL === 'campus' ? '?next=campus' : ''}">${L('Sign in', 'Iniciar sesión')}</a>` : ''}</div>` : '');
  }
  function convHTML(ch) {
    const c = C[S.c], m = MODES[ch.mode], subs = c.s || [];
    return `<div class="ch-top"><button class="ch-back" data-h="list" aria-label="${L('All chats', 'Todos los chats')}">‹</button><div class="ch-tt2"><b>${esc(ch.title)}</b><small>${m.i} ${m.n()}${ch.s ? ' • ' + esc(ch.s) : ''}</small></div><button class="ch-new2" data-h="new" aria-label="${L('New chat', 'Chat nuevo')}">＋</button></div>
${ch.turns.length ? '' : `<div class="ch-cfg"><div class="ch-modes" role="radiogroup" aria-label="${L('Mode', 'Modo')}">${Object.keys(MODES).map(k => `<button role="radio" aria-checked="${ch.mode === k}" class="${ch.mode === k ? 'on' : ''}" data-h="mode" data-v="${k}">${MODES[k].i} ${MODES[k].n()}</button>`).join('')}</div>
<select class="ch-sub" data-h-in="sub" aria-label="${L('Subject', 'Asignatura')}"><option value="">${L('All subjects', 'Todas las asignaturas')}</option>${subs.map(s => `<option ${ch.s === s ? 'selected' : ''}>${esc(s)}</option>`).join('')}</select></div>`}
<div class="ch-msgs" id="ch-msgs" aria-live="polite">${msgsHTML(ch)}</div>
${H.att ? `<div class="ch-att"><img src="${H.att.thumb}" alt=""><span>${L('Photo ready. Add a question or just send it.', 'Foto lista. Añade una pregunta o envíala.')}</span><button data-h="unatt" aria-label="${L('Remove photo', 'Quitar foto')}">✕</button></div>` : ''}<div class="ch-comp"><label class="ch-cam" title="${L('Snap a question', 'Foto de una pregunta')}" aria-label="${L('Add a photo of a question', 'Añadir foto')}">📷<input type="file" accept="image/*" id="ch-file" hidden></label><textarea id="ch-in" data-h-in="draft" rows="1" maxlength="${m.long ? 5000 : 1500}" placeholder="${esc(m.ph())}" aria-label="${L('Message Ace', 'Escribe a Ace')}">${esc(H.draft)}</textarea><button class="ch-send" data-h="send" aria-label="${L('Send', 'Enviar')}" ${H.busy ? 'disabled' : ''}>➤</button></div>
${H.attBusy ? `<p class="ch-fine">${L('Preparing your photo…', 'Preparando la foto…')}</p>` : ''}<p class="ch-fine">${L('Ace can make mistakes. Check important answers with your notes or teacher.', 'Ace puede equivocarse. Comprueba las respuestas importantes.')}${H.cap ? ` • ${H.cap.used}/${H.cap.cap} ${L('today', 'hoy')}` : ''}</p>`;
  }
  function chatView() {
    if (!H.loaded) { H.loaded = true; loadLocal(); pull() }
    let ch = cur(); if (!ch) { const had = H.list.some(x => x.turns.length); ch = H.list.find(x => !x.turns.length) || newChat('buddy'); H.cur = ch.id; H.pane = had ? 'list' : 'conv' }
    setTimeout(H.after, 0);
    return `<div class="chat" data-pane="${H.pane}"><aside class="ch-side">${sideHTML()}</aside><section class="ch-main">${convHTML(ch)}</section></div>`;
  }
  function grow() { const t = document.getElementById('ch-in'); if (t) { t.style.height = 'auto'; t.style.height = Math.min(t.scrollHeight, 200) + 'px' } }
  function paint(scroll) {
    if (S.tab !== 'chat') return; const ch = cur(), m = document.getElementById('ch-msgs');
    if (!m || !ch) return render();
    m.innerHTML = msgsHTML(ch); try { fmtMath(m) } catch (e) { }
    const side = document.querySelector('.ch-side'); if (side) side.innerHTML = sideHTML();
    const tt = document.querySelector('.ch-tt2 b'); if (tt) tt.textContent = ch.title;
    const cfg = document.querySelector('.ch-cfg'); if (cfg && ch.turns.length) cfg.remove();
    const b = document.querySelector('.ch-send'); if (b) b.disabled = H.busy;
    const at = document.querySelector('.ch-att'); if (at && !H.att) at.remove();
    const i = document.getElementById('ch-in'); if (i && !H.draft) { i.value = ''; grow() }
    if (scroll) m.scrollTop = m.scrollHeight;
  }
  H.after = function () { if (S.tab !== 'chat') return; const m = document.getElementById('ch-msgs'); if (m) m.scrollTop = m.scrollHeight; grow(); if (H.pane === 'conv' && matchMedia('(min-width:900px)').matches) { const i = document.getElementById('ch-in'); if (i && document.activeElement === document.body) i.focus() } };

  /* ---------- events ---------- */
  document.addEventListener('click', e => {
    const b = e.target.closest && e.target.closest('[data-h]'); if (!b) { if (H.menu && !e.target.closest('.ch-menu')) { H.menu = null; paint() } return }
    const k = b.dataset.h, v = b.dataset.v, ch = cur();
    if (k === 'new') { const empty = H.list.find(x => !x.turns.length); if (empty) { H.cur = empty.id; H.pane = 'conv'; H.draft = '' } else newChat('buddy'); H.err = ''; render(); setTimeout(() => { const i = document.getElementById('ch-in'); if (i) i.focus() }, 30) }
    else if (k === 'open') { H.cur = v; H.pane = 'conv'; H.err = ''; H.retry = null; H.menu = null; H.draft = ''; render() }
    else if (k === 'list') { H.pane = 'list'; render() }
    else if (k === 'menu') { H.menu = H.menu === v ? null : v; paint() }
    else if (k === 'rename') { H.edit = v; H.menu = null; paint(); setTimeout(() => { const i = document.querySelector('.ch-ren'); if (i) { i.focus(); i.select() } }, 20) }
    else if (k === 'pin') { const c = find(v); if (c) { c.pinned = !c.pinned; saveLocal(); push(c) } H.menu = null; paint() }
    else if (k === 'del') {
      if (H.confirm !== v) { H.confirm = v; b.textContent = L('Tap again to delete', 'Toca otra vez para borrar'); return }
      H.confirm = null; H.list = H.list.filter(c => c.id !== v); saveLocal(); drop(v); if (H.cur === v) { H.cur = null; H.pane = 'list' } H.menu = null; render()
    }
    else if (k === 'mode' && ch && !ch.turns.length) { ch.mode = v; render() }
    else if (k === 'start' && ch) { const s = MODES[ch.mode].st()[+v]; const i = document.getElementById('ch-in'); H.draft = s; if (i) { i.value = s; i.focus(); i.setSelectionRange(s.length, s.length); grow() } if (!/[: ]$/.test(s)) send(s) }
    else if (k === 'send') { const i = document.getElementById('ch-in'); send(i ? i.value : H.draft) }
    else if (k === 'retry' && ch) { const t = H.retry; H.retry = null; if (ch.turns.length && ch.turns[ch.turns.length - 1].role === 'user') ch.turns.pop(); send(t) }
    else if (k === 'again' && ch) { const last = ch.turns.length - 1; if (ch.turns[last] && ch.turns[last].role === 'assistant') { ch.turns.pop(); const u = ch.turns.pop(); if (u) send(u.content) } }
    else if (k === 'snap') { const f = document.getElementById('ch-file'); if (f) f.click() }
    else if (k === 'unatt') { H.att = null; render() }
    else if (k === 'copy' && ch) { const t = (ch.turns[+v] || {}).content || ''; (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(() => toast(L('Copied', 'Copiado'))).catch(() => toast(L('Could not copy', 'No se pudo copiar'))) }
    else if (k === 'read' && ch) { try { AceUI.say(((ch.turns[+v] || {}).content || '').replace(/[*#`•]/g, '')) } catch (z) { } }
    else return;
    e.preventDefault();
  });
  document.addEventListener('input', e => {
    const el = e.target.closest && e.target.closest('[data-h-in]'); if (!el) return; const k = el.dataset.hIn, ch = cur();
    if (k === 'draft') { H.draft = el.value; grow() }
    else if (k === 'q') { H.q = el.value; const l = document.querySelector('.ch-list'); if (l) { const pos = el.selectionStart; document.querySelector('.ch-side').innerHTML = sideHTML(); const n = document.querySelector('.ch-q'); n.focus(); try { n.setSelectionRange(pos, pos) } catch (z) { } } }
    else if (k === 'sub' && ch) { ch.s = el.value; saveLocal() }
  });
  document.addEventListener('change', e => {
    if (e.target.id !== 'ch-file' || !e.target.files || !e.target.files[0]) return; const f = e.target.files[0]; e.target.value = '';
    if (!window.AceFiles) return; H.attBusy = true; H.err = ''; render();
    AceFiles.image(f).then(a => { H.att = a; H.attBusy = false; render(); const i = document.getElementById('ch-in'); if (i) i.focus() })
      .catch(er => { H.attBusy = false; H.err = (er && er.msg) || L('Ace could not open that photo.', 'No se pudo abrir la foto.'); render() });
  });
  document.addEventListener('keydown', e => {
    const el = e.target;
    if (el.id === 'ch-in' && e.key === 'Enter' && !e.shiftKey && !e.isComposing) { e.preventDefault(); send(el.value) }
    if (el.classList && el.classList.contains('ch-ren') && (e.key === 'Enter' || e.key === 'Escape')) { e.preventDefault(); el.blur() }
  });
  document.addEventListener('focusout', e => {
    const el = e.target; if (!el.classList || !el.classList.contains('ch-ren')) return;
    const c = find(el.dataset.v), t = el.value.trim(); if (c && t) { c.title = t.slice(0, 120); saveLocal(); push(c) } H.edit = null; setTimeout(paint, 0);
  });

  Object.assign(V, { chat: chatView });
  const r0 = window.render; window.render = function () { const out = r0.apply(this, arguments); document.documentElement.toggleAttribute('data-chat', S.tab === 'chat'); return out };
  loadLocal(); H.loaded = true;
  if (window.AceSync && AceSync.ready) AceSync.ready().then(ok => { if (ok) pull() }).catch(() => { });
})();
