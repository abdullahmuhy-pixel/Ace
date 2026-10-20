/* Ace Teach portal. One page for:
     - tutors and tutoring centres (schools.kind = 'tutor', owner is school_admin of their workspace)
     - school teachers and subject teachers
     - school admins
     - the Ace team (platform_admin): founder console
   Every rule is enforced by Postgres RLS and the edge functions; this page only shows what the database allows. */
(function () {
'use strict';
const CFG = window.ACE_CONFIG || {}, $ = s => document.querySelector(s), $$ = s => Array.from(document.querySelectorAll(s));
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));
const today = () => new Date().toISOString().slice(0, 10);
const STAFF = ['teacher', 'subject_teacher', 'school_admin', 'platform_admin'];
const FILES = { NG: 'nigeria-syllabus.html', GH: 'ghana-syllabus.html', SL: 'sierra-leone-syllabus.html', GM: 'gambia-syllabus.html', KE: 'kenya-syllabus.html', ZM: 'zambia-syllabus.html', GB: 'uk-syllabus.html', CA: 'canada-syllabus.html', ES: 'spain-syllabus.html', IE: 'ireland-syllabus.html', ZA: 'south-africa-syllabus.html', UG: 'uganda-syllabus.html', TZ: 'tanzania-syllabus.html', LR: 'liberia-syllabus.html', MT: 'malta-syllabus.html', ZW: 'zimbabwe-syllabus.html' };
const CN = { NG: '🇳🇬 Nigeria', GH: '🇬🇭 Ghana', SL: '🇸🇱 Sierra Leone', GM: '🇬🇲 The Gambia', KE: '🇰🇪 Kenya', ZM: '🇿🇲 Zambia', GB: '🇬🇧 United Kingdom', CA: '🇨🇦 Canada', ES: '🇪🇸 España', IE: '🇮🇪 Ireland', ZA: '🇿🇦 South Africa', UG: '🇺🇬 Uganda', TZ: '🇹🇿 Tanzania', LR: '🇱🇷 Liberia', MT: '🇲🇹 Malta', ZW: '🇿🇼 Zimbabwe' };
// How each country names marks earned during the year. Numbers are only given where they are a fixed national rule.
const CA = {
  NG: ['Continuous assessment (CA)', 'Tests, assignments and projects recorded through the term.', 'CA'],
  GH: ['Continuous assessment (SBA)', 'School-based assessment recorded through the term.', 'SBA'],
  SL: ['Continuous assessment (CA)', 'Tests and assignments recorded through the term.', 'CA'],
  GM: ['Continuous assessment (CA)', 'Tests and assignments recorded through the term.', 'CA'],
  LR: ['Continuous assessment (CA)', 'Tests and assignments recorded through the term.', 'CA'],
  KE: ['CATs (continuous assessment tests)', 'Termly CATs and assignments.', 'CATs'],
  ZM: ['School-based assessment (SBA)', 'Tests, projects and practicals recorded at school.', 'SBA'],
  ZA: ['SBA (school-based assessment)', 'In most NSC subjects SBA counts 25% of the final mark; the exam counts 75%.', 'SBA'],
  UG: ['Continuous assessment', 'Under the new lower-secondary curriculum, school-based assessment counts 20% of the UCE result.', 'CA'],
  TZ: ['Continuous assessment (CA)', 'Tests, assignments and projects recorded at school.', 'CA'],
  GB: ['Coursework / NEA', 'Non-exam assessment in the subjects that have it.', 'NEA'],
  IE: ['Classroom-Based Assessments', 'CBAs and additional assessment components.', 'CBA'],
  ES: ['Evaluación continua', 'Exámenes, trabajos y proyectos del curso.', 'EC'],
  CA: ['Term work', 'In Ontario, term work is 70% of the final grade and the final evaluation 30%.', 'Term work'],
  MT: ['Coursework', 'School-assessed work in the SEC subjects that have it.', 'Coursework'],
  ZW: ['School-based projects (SBP)', 'Projects done at school under the heritage-based curriculum, which replaced CALA.', 'SBP']
};
let sb, me, school, St = { view: '', cls: '', classes: [], day: today(), month: today().slice(0, 7), q: '' };
const SYL = {};

/* ---------- small helpers ---------- */
function toast(m, bad) { const t = $('#toast'); t.textContent = m; t.className = 'show' + (bad ? ' bad' : ''); clearTimeout(toast.t); toast.t = setTimeout(() => t.className = '', 4200); }
const must = r => { if (r && r.error) throw new Error(r.error.message); return r ? r.data : null; };
const guard = f => async (...a) => { try { return await f(...a); } catch (e) { toast((e && e.message) || String(e), true); console.error(e); } };
async function fn(name, body) {
  const { data } = await sb.auth.getSession(); const tok = data.session && data.session.access_token;
  const r = await fetch(CFG.supabaseUrl.replace(/\/$/, '') + '/functions/v1/' + name, { method: 'POST', headers: { 'Content-Type': 'application/json', apikey: CFG.supabaseAnonKey, Authorization: 'Bearer ' + tok }, body: JSON.stringify(body) });
  const j = await r.json().catch(() => ({})); if (!r.ok) throw new Error(j.error || 'Something went wrong.'); return j;
}
const nm = s => esc((s.first_name || '') + ' ' + (s.surname || ''));
const ini = s => ((s.first_name || '?')[0] + (s.surname || '')[0] || '').toUpperCase();
const pct = v => v == null ? '–' : Math.round(v) + '%';
const barCls = v => v == null ? '' : v < 50 ? 'lo' : v < 70 ? 'mid' : '';
const bar = v => `<div class="bar ${barCls(v)}"><i style="width:${Math.max(0, Math.min(100, v || 0))}%"></i></div>`;
const table = (head, rows, empty) => `<div class="tw"><table><thead><tr>${head.map(x => `<th${/^(XP|Streak|Score|%|Avg|Marks?|Out of|Weight|Students|Attempts|Active|Paid|Amount|Due|Balance|Answered)/.test(x) ? ' class="n"' : ''}>${x}</th>`).join('')}</tr></thead><tbody>${rows.join('') || `<tr><td colspan="${head.length}" class="muted">${empty || 'Nothing here yet.'}</td></tr>`}</tbody></table></div>`;
const csv = rows => rows.map(r => r.map(c => '"' + String(c == null ? '' : c).replace(/"/g, '""') + '"').join(',')).join('\n');
function saveCsv(name, text) { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([text], { type: 'text/csv' })); a.download = name; document.body.appendChild(a); a.click(); a.remove(); }
const daysAgo = d => d ? Math.floor((Date.now() - new Date(d).getTime()) / 864e5) : null;
const ago = d => { const n = daysAgo(d); return n == null ? 'never' : n <= 0 ? 'today' : n === 1 ? 'yesterday' : n + ' days ago'; };
const cls = () => St.classes.find(c => c.id === St.cls) || null;
const isAdmin = () => me && me.role === 'school_admin';
const isTutor = () => school && school.kind === 'tutor';
const isPlat = () => me && me.role === 'platform_admin';
const cc = () => (school && school.country_code) || (me && me.country_code) || 'NG';
const md = t => esc(t).split(/\n{2,}/).map(b => { const L0 = b.split('\n'); if (L0.every(l => /^\s*([-*•]|\d+[.)])\s+/.test(l))) { const ol = /^\s*\d/.test(L0[0]); return `<${ol ? 'ol' : 'ul'}>${L0.map(l => `<li>${l.replace(/^\s*([-*•]|\d+[.)])\s+/, '')}</li>`).join('')}</${ol ? 'ol' : 'ul'}>`; } const h = b.match(/^(#{1,4})\s+(.*)$/); if (h && L0.length === 1) return `<h${Math.min(4, h[1].length + 1)}>${h[2]}</h${Math.min(4, h[1].length + 1)}>`; return `<p>${b.replace(/\n/g, '<br>')}</p>`; }).join('').replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/^<p>#{1,4}\s+/gm, '<p>');
const empty = (t, s, extra) => `<div class="empty"><b>${t}</b>${s || ''}${extra ? '<div style="margin-top:12px">' + extra + '</div>' : ''}</div>`;

/* ---------- the country syllabus (same file the student app uses) ---------- */
async function syllabus(code) {
  code = code || cc(); if (SYL[code]) return SYL[code];
  const f = FILES[code]; if (!f) return null;
  const html = await (await fetch('../app/' + f)).text();
  const el = new DOMParser().parseFromString(html, 'text/html').getElementById('syllabus-data');
  return (SYL[code] = el ? JSON.parse(el.textContent) : null);
}
function examKey(d, label) {
  if (!d) return null; const ks = Object.keys(d.exams); if (!label) return ks[0];
  const L = String(label).toLowerCase();
  return ks.find(k => k.toLowerCase() === L) || ks.find(k => L.includes(k.toLowerCase()) || k.toLowerCase().includes(L)) || ks[0];
}
function subjectsOf(d, ek) { const e = d && d.exams[ek]; if (!e) return []; return Object.keys(e.subjects).filter(s => { const x = e.subjects[s]; return (x.modules && x.modules.length) || x.same_as; }); }
function modulesOf(d, ek, s) { const e = d && d.exams[ek]; if (!e) return []; let x = e.subjects[s]; if (x && !x.modules && x.same_as) x = (d.exams[x.same_as].subjects || {})[s]; return (x && x.modules) || []; }
const curEx = async () => { const d = await syllabus(); const c = cls(); return [d, examKey(d, c && c.exam)]; };

/* ---------- navigation by role ---------- */
function navFor() {
  if (isPlat()) return [['Console', [['dash', '📊', 'Dashboard'], ['schools', '🏫', 'Schools and tutors'], ['users', '👥', 'People'], ['money', '💰', 'Plans and revenue'], ['creators', '🎬', 'Creators'], ['config', '📢', 'Broadcast and config'], ['reports', '🧾', 'Reports and errors'], ['mod', '🛡️', 'Moderation']]]];
  const g = [['Teaching', [['overview', '📊', 'Overview'], ['students', '👥', isTutor() ? 'My students' : 'My class'], ['progress', '📈', 'Progress'], ['register', '📅', 'Register']]],
    ['Classroom', [['work', '📝', 'Assign work'], ['grades', '📒', 'Gradebook'], ['pacing', '🗺️', 'Pacing'], ['live', '⚡', 'Live quiz'], ['qna', '💬', 'Q&A board'], ['library', '📚', 'Library'], ['notices', '📢', 'Notices'], ['messages', '✉️', 'Messages']]],
    ['Tools', [['ai', '✨', 'AI planner'], ['reportcards', '📄', 'Report cards'], ['planner', '🗓️', 'Term planner'], ['rubrics', '📐', 'Rubrics'], ['parents', '👪', 'Parents']]]];
  if (isAdmin()) g.push([isTutor() ? 'My workspace' : 'School', [['classes', '🏛️', 'Classes'], ['people', '🧑‍🏫', isTutor() ? 'Students and teachers' : 'People'], ...(isTutor() ? [] : [['timetable', '🕒', 'Timetables'], ['fees', '💳', 'Fees']]), ['schoolrep', '📋', isTutor() ? 'Workspace report' : 'School report'], ['mod', '🛡️', 'Moderation'], ['settings', '⚙️', 'Settings']]]);
  else g.push(['Account', [['settings', '⚙️', 'Settings']]]);
  return g;
}
const DOCK = () => isPlat() ? ['dash', 'schools', 'users', 'money'] : ['overview', 'students', 'work', 'messages'];
const NEEDS_CLASS = new Set(['overview', 'students', 'progress', 'register', 'work', 'grades', 'pacing', 'live', 'qna', 'library', 'notices', 'messages', 'reportcards', 'planner', 'parents']);
const TITLES = {};
function drawNav() {
  const groups = navFor(); groups.forEach(g => g[1].forEach(i => TITLES[i[0]] = i[2]));
  const item = i => `<button class="ni ${St.view === i[0] ? 'on' : ''}" data-go="${i[0]}"><i>${i[1]}</i><span>${i[2]}</span>${St.badges && St.badges[i[0]] ? `<em>${St.badges[i[0]]}</em>` : ''}</button>`;
  $('#nav').innerHTML = groups.map(g => `<div class="ng">${g[0]}</div>` + g[1].map(item).join('')).join('');
  $('#morelist').innerHTML = groups.map(g => `<div class="ng">${g[0]}</div>` + g[1].map(item).join('')).join('');
  const all = {}; groups.forEach(g => g[1].forEach(i => all[i[0]] = i));
  const SH = { overview: 'Home', students: 'Students', work: 'Assign', messages: 'Messages', dash: 'Home', schools: 'Schools', users: 'People', money: 'Money' };
  $('#dock').innerHTML = DOCK().map(k => all[k]).filter(Boolean).map(i => `<button class="${St.view === i[0] ? 'on' : ''}" data-go="${i[0]}"><i>${i[1]}</i>${SH[i[0]] || i[2]}</button>`).join('') + `<button data-more><i>☰</i>More</button>`;
}
function drawTop() {
  const c = cls(), t = TITLES[St.view] || '';
  let h = `<h1>${esc(t)}</h1>`;
  if (!isPlat() && NEEDS_CLASS.has(St.view)) {
    h += St.classes.length ? `<div class="clsw"><select data-cls aria-label="Class">${St.classes.map(k => `<option value="${k.id}" ${k.id === St.cls ? 'selected' : ''}>${esc(k.name)}${k.subject ? ' • ' + esc(k.subject) : ''}</option>`).join('')}</select>${c && c.join_code ? `<span class="code" title="Students join with this code">${esc(c.join_code)} <small>join code</small></span><button class="ib" data-a="copycode" aria-label="Copy join code">⧉</button>` : ''}</div>` : '';
  }
  h += `<a class="g" href="../app/" target="_blank" rel="noopener" style="text-decoration:none">Student app ↗</a>`;
  $('#top').innerHTML = h;
}

/* ---------- boot ---------- */
async function boot() {
  if (!CFG.supabaseUrl || !CFG.supabaseAnonKey || !window.supabase) { $('#view').innerHTML = '<div class="card"><b>Not connected yet.</b><p class="muted">Fill in config.js with the Supabase URL and anon key.</p></div>'; return; }
  sb = window.supabase.createClient(CFG.supabaseUrl, CFG.supabaseAnonKey, { auth: { storage: { getItem(k) { try { const a = localStorage.getItem(k); return a != null ? a : sessionStorage.getItem(k); } catch (e) { return null; } }, setItem(k, v) { try { if (sessionStorage.getItem(k) != null && localStorage.getItem(k) == null) sessionStorage.setItem(k, v); else localStorage.setItem(k, v); } catch (e) { } }, removeItem(k) { try { localStorage.removeItem(k); sessionStorage.removeItem(k); } catch (e) { } } }, persistSession: true, autoRefreshToken: true } });
  const { data } = await sb.auth.getSession();
  if (!data.session) { $('#view').innerHTML = `<div class="card" style="max-width:520px"><h2>Sign in to Ace Teach</h2><p class="sub">For teachers, tutors and school staff.</p><a class="b" style="display:inline-block;text-decoration:none" href="../login/?next=staff">Sign in</a> <a class="g" style="text-decoration:none;margin-left:6px" href="../login/?role=tutor">Create a teacher account</a></div>`; return; }
  me = must(await sb.from('profiles').select('*').eq('id', data.session.user.id).single());
  if (!STAFF.includes(me.role)) { $('#view').innerHTML = `<div class="card" style="max-width:560px"><h2>This area is for teachers and tutors</h2><p class="sub">You are signed in with a student account. Students use the Ace app.</p><a class="b" style="text-decoration:none;display:inline-block" href="../app/">Open the student app</a></div>`; return; }
  if (me.school_id) school = must(await sb.from('schools').select('*').eq('id', me.school_id).maybeSingle());
  await loadClasses();
  $('#ws').innerHTML = isPlat() ? `<b>Ace team</b><small>Founder console</small><span class="rb">Platform admin</span>` : `<b>${esc(school ? school.name : '')}</b><small>${esc(CN[cc()] || cc())}</small><span class="rb">${isTutor() ? (isAdmin() ? 'Tutor' : 'Teacher') : me.role === 'school_admin' ? 'School admin' : me.role === 'subject_teacher' ? 'Subject teacher' : 'Teacher'}</span>`;
  $('#me').innerHTML = `<span class="av">${esc(ini(me))}</span><div><b>${nm(me)}</b><small>${esc(me.contact_email || me.username || '')}</small></div><button class="ib" data-a="signout" aria-label="Sign out" title="Sign out">⎋</button>`;
  const h = (location.hash || '').slice(1);
  St.view = h && TITLES_OK(h) ? h : isPlat() ? 'dash' : (St.classes.length ? 'overview' : (isAdmin() ? 'classes' : 'overview'));
  try { const fc = localStorage.getItem('ace-first-code'); if (fc) { localStorage.removeItem('ace-first-code'); toast('Your first class is ready. Share the code ' + fc + ' with your students.'); } } catch (e) { }
  go();
}
const TITLES_OK = k => { navFor().forEach(g => g[1].forEach(i => TITLES[i[0]] = i[2])); return !!TITLES[k]; };
async function loadClasses() {
  if (isPlat()) { St.classes = []; return; }
  if (isAdmin()) St.classes = must(await sb.from('classes').select('id,name,grade,school_id,join_code,subject,exam,meet_url,archived').eq('school_id', me.school_id).eq('archived', false).order('name'));
  else { const ts = must(await sb.from('teacher_subjects').select('class_id,subject,classes(id,name,grade,school_id,join_code,subject,exam,meet_url,archived)').eq('teacher_id', me.id)); const seen = {}; ts.forEach(t => { if (t.classes && !t.classes.archived && !seen[t.class_id]) seen[t.class_id] = Object.assign({}, t.classes, { subject: t.classes.subject || t.subject }); }); St.classes = Object.values(seen).sort((a, b) => a.name.localeCompare(b.name)); }
  if (!St.classes.find(c => c.id === St.cls)) St.cls = (St.classes[0] || {}).id || '';
}
const go = guard(async function () {
  drawNav(); drawTop(); $('#more').hidden = true;
  try { history.replaceState(null, '', '#' + St.view); } catch (e) { }
  const v = $('#view'); v.innerHTML = '<div class="loading">Loading…</div>';
  if (NEEDS_CLASS.has(St.view) && !St.cls) { v.innerHTML = noClass(); return; }
  const html = await (V[St.view] || V.overview)();
  v.innerHTML = html; if (St.after) { const f = St.after; St.after = null; f(); }
});
const noClass = () => `<div class="card" style="max-width:640px">${empty('No class yet', isAdmin() ? 'Create your first class. You get a join code to share with students.' : 'Your school admin has not given you a class yet.', isAdmin() ? `<button class="b" data-go="classes">Create a class</button>` : '')}</div>`;

/* ---------- views, actions (data-a) and forms (data-f) are filled in by the other portal files ---------- */
const V = {}, A = {}, F = {};
A.signout = async () => { await sb.auth.signOut(); location.href = '../login/'; };
A.copycode = () => { const c = cls(); if (!c) return; const t = `Join my class "${c.name}" on Ace Education: open ${location.origin}${location.pathname.replace(/staff\/.*$/, '')}app/ , go to Tools, My classes, and enter the code ${c.join_code}`; try { navigator.clipboard.writeText(t).then(() => toast('Join code copied with instructions.'), () => toast('Code: ' + c.join_code)); } catch (e) { toast('Code: ' + c.join_code); } };
document.addEventListener('click', guard(async e => {
  const g = e.target.closest('[data-go]'); if (g) { St.view = g.dataset.go; St.sel = St.sub = St.task = St.asmt = St.live = St.peer = St.stu = ''; window.scrollTo(0, 0); return go(); }
  if (e.target.closest('[data-more]')) { $('#more').hidden = false; return; }
  if (e.target.closest('[data-close]') || e.target.id === 'more') { $('#more').hidden = true; return; }
  if (e.target.classList && e.target.classList.contains('drawer')) { e.target.remove(); return; }
  const a = e.target.closest('[data-a]'); if (a && a.tagName !== 'SELECT' && a.tagName !== 'INPUT' && A[a.dataset.a]) { e.preventDefault(); return A[a.dataset.a](a, e); }
}));
document.addEventListener('change', guard(async e => {
  const t = e.target;
  if (t.matches('[data-cls]')) { St.cls = t.value; St.sel = St.sub = St.task = St.asmt = St.live = St.peer = St.stu = ''; return go(); }
  if (t.matches('[data-a]') && (t.tagName === 'SELECT' || t.tagName === 'INPUT') && A[t.dataset.a]) return A[t.dataset.a](t, e);
}));
document.addEventListener('input', e => { const t = e.target; if (t.matches && t.matches('[data-filter]')) { const q = t.value.toLowerCase(); $$(t.dataset.filter).forEach(r => r.hidden = q && !r.textContent.toLowerCase().includes(q)); } });
document.addEventListener('submit', guard(async e => {
  const f = e.target.closest('form[data-f]'); if (!f) return; e.preventDefault();
  const d = {}; new FormData(f).forEach((v, k) => d[k] = typeof v === 'string' ? v.trim() : v); f.querySelectorAll('input[type=checkbox]').forEach(c => d[c.name] = c.checked);
  const btn = f.querySelector('button.b,button[type=submit]'); if (btn) btn.disabled = true;
  try { await F[f.dataset.f](d, f); } finally { if (btn) btn.disabled = false; }
}));
window.AceTeach = { V, A, F, St, go, get sb() { return sb; }, get me() { return me; }, get school() { return school; }, helpers: { esc, table, bar, pct, nm, ini, ago, daysAgo, csv, saveCsv, must, fn, toast, guard, syllabus, examKey, subjectsOf, modulesOf, curEx, cls, isAdmin, isTutor, isPlat, cc, empty, CA, CN, today, loadClasses, md } };
window.addEventListener('load', () => guard(boot)());
})();
