/* Ace Campus: the university portal. Same engine as the school app (lessons, practice, finals, AI, streaks),
   switched on by window.ACE_MODE === 'campus' (set by campus/index.html, which tools/build_campus.py generates).
   Loaded before the main app script; setup() runs right after C is defined, boot() just before the first render.
   Course content comes from campus-syllabus.html (built by tools/campus/build.py). The student's home country
   stays in localStorage 'ace-country' and decides currency, GPA scale and the university list. */
(function () {
  'use strict';
  if (window.ACE_MODE !== 'campus') return;
  const KEY = 'ace-campus';
  const CUR = { NG: '₦', GH: '₵', SL: 'Le', GM: 'D', KE: 'KSh', ZM: 'K', GB: '£', CA: '$', ES: '€', IE: '€', ZA: 'R', UG: 'USh', TZ: 'TSh', LR: 'L$', MT: '€', ZW: 'US$', BW: 'P', FR: '€' };
  const SCALE = { NG: ['gpa', 'ng5'], GB: ['uk', 'ng5'], IE: ['uk', 'ng5'], MT: ['uk', 'ng5'], KE: ['uk', 'ng5'] };
  const FAC = [['health', /medic|health|nurs|pharm|dent|clinic|surg|anatom|physiother|radiograph|optom|public health/i], ['eng', /engineer|technolog|architect|survey/i],
    ['comp', /comput|software|informat|data|cyber|\bit\b|ict/i], ['law', /\blaw\b|legal|jurisprud/i], ['biz', /business|econom|account|financ|manag|commerce|market|bank|actuar|insur/i],
    ['edu', /educat|teach/i], ['sci', /science|math|physic|chemi|biolog|statist|geolog|agric|biochem|microbio|zoolog|botan/i],
    ['soc', /social|psycholog|sociolog|politic|international|geograph|communicat|mass|criminolog|anthropolog/i], ['arts', /arts|humanit|histor|language|literat|music|theatre|philosoph|relig|english|french|fine/i]];
  const facOf = s => { for (const [k, re] of FAC) if (re.test(s || '')) return k; return ''; };
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));
  const load = () => { try { return JSON.parse(localStorage.getItem(KEY) || '{}') } catch (e) { return {} } };
  const st = Object.assign({ uni: '', uniId: '', prog: '', fac: '', year: 'Year 1', want: {}, sem: { name: '', courses: [], tasks: [] } }, load());
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(st)) } catch (e) { } };
  const home = () => { try { const v = localStorage.getItem('ace-country'); return v && v !== 'UN' && C[v] ? v : 'NG' } catch (e) { return 'NG' } };
  const day = s => s ? new Date(s + 'T09:00:00') : null;
  const daysTo = s => { const d = day(s); return d ? Math.ceil((d - new Date(todayStr() + 'T09:00:00')) / 864e5) : null };
  const nextExam = () => { const xs = (st.sem.courses || []).filter(c => c.exam && daysTo(c.exam) >= 0).sort((a, b) => a.exam < b.exam ? -1 : 1); return xs[0] || null };
  const fmtD = s => s ? day(s).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }) : '';
  const signedIn = () => !!(window.AceSync && AceSync.signedIn && AceSync.signedIn());
  const A = window.AceCampus = { st, save, home, facOf, cat: [], facs: {}, U: { list: null, cc: '', q: '', err: '' } };

  /* ---------- wiring (called from the main script) ---------- */
  A.setup = function () {
    const hc = home();
    C.UN = { n: C[hc].n, f: '🎓', b: 'Ace Campus', x: ['First-year core'], s: ['Calculus I', 'Linear Algebra'], t: 'gb', d: (nextExam() || {}).exam || '', u: C[hc].u, p: C[hc].p, tl: 'campus', home: hc };
    LV.UN = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5', 'Year 6', 'Postgraduate'];
    ACE_CFG.syllabusFiles.UN = 'campus-syllabus.html';
    T.campus = Object.assign({}, T.en, { nav: ['Home', 'Courses', 'Practice', 'Today', 'Tools'], sub: 'My courses', all: 'All courses', g1: 'Answer 20 questions', dc: 'Daily challenge', dcs: '10 questions from your courses', dn: 'Ace Campus follows the common first-year syllabus. Your own course outline decides what is examined.' });
    document.documentElement.classList.add('campus');
    if (!P.s.UN) P.s.UN = null;
  };
  A.pre = function (d) { d.currency = CUR[home()] || '$'; A.cat = d.catalogue || []; A.facs = d.faculties || {}; return d };
  A.setHome = function (cc, quiet) {
    if (!C[cc] || cc === 'UN') return;
    try { localStorage.setItem('ace-country', cc) } catch (e) { }
    C.UN.n = C[cc].n; C.UN.home = cc; C.UN.p = C[cc].p; delete ACE_CACHE.UN; A.U.list = null;
    if (window.AceX && AceX.gp) { const s = SCALE[cc] || ['gpa', 'us4']; AceX.gp.mode = s[0]; AceX.gp.scale = s[1] }
    if (S.c === 'UN') useCountry('UN'); if (!quiet) render();
  };
  A.boot = function () {
    ICN.unshift([/calculus|algebra|probab|statist|differential|discrete/i, '📐'], [/python|programming|algorithm|machine learning|data analysis/i, '💻'], [/accounting/i, '🧾']);
    const subj0 = V.subj;
    Object.assign(V, { home: homeView, onb: onbView, sem: semView, subj: (c, t, ex) => S.sub != null ? subj0(c, t, ex) : coursesView(c, t, ex), tools: toolsView });
    setTimeout(() => { if (window.AceX && AceX.gp) { const s = SCALE[home()] || ['gpa', 'us4']; AceX.gp.mode = s[0]; AceX.gp.scale = s[1] } }, 0);
    P.lvl = 'university';
    if (!P.conb) S.tab = 'onb';
  };
  A.syncLevel = function () {
    if (!signedIn() || !AceSync.rpc) return;
    try { AceSync.rpc('set_my_level', { p_level: 'university', p_institution: st.uni || null, p_programme: st.prog || null, p_year: Math.max(1, parseInt(String(st.year).replace(/\D/g, '')) || 1) }) } catch (e) { }
  };
  function updDate() { C.UN.d = (nextExam() || {}).exam || '' }

  /* ---------- home ---------- */
  function homeView(c, t, ex) {
    const nm = (c.u || 'Guest').split(' ')[0], hr = new Date().getHours(), hi = hr < 12 ? 'Good morning' : hr < 18 ? 'Good afternoon' : 'Good evening';
    const st_ = ST(), td = todayStr(); if (P.dqd !== td) { P.dqd = td; P.dq0 = st_.q; svP() }
    const done = Math.max(0, st_.q - (P.dq0 || 0)), gp = Math.min(100, Math.round(done / (P.goal || 20) * 100));
    const nx = nextExam(), dl = nx ? daysTo(nx.exam) : null;
    const tasks = (st.sem.tasks || []).filter(x => !x.done && x.due).sort((a, b) => a.due < b.due ? -1 : 1).slice(0, 4);
    const tiles = c.s.map((s, i) => selOK(c, s) ? stile(c, t, ex, s, i) : '').filter(Boolean).join('');
    const where = [st.uni, st.prog, st.year].filter(Boolean).map(esc).join(' • ') || 'Tell Ace where you study';
    const bub = nx ? `${dl === 0 ? 'Your ' + esc(nx.n) + ' exam is today. You have got this.' : dl + ' days to ' + esc(nx.n) + '. A little every day adds up.'}` : 'Add your exam dates and I will plan around them.';
    const soon = A.cat.filter(x => x.status === 'soon' && (!st.fac || x.faculties.includes(st.fac))).slice(0, 3);
    return `<section class="hh cp-hh"><div class="hh-txt"><p class="hh-hi">${hi},</p><h1>${esc(nm)}</h1><button class="tg" data-k="edit">🏛️ ${where} ▾</button></div>
<div class="hh-cd">${nx ? `<b id="cd0">000</b><span>days to ${esc(nx.n)}</span><small>${fmtD(nx.exam)}${nx.code ? ' • ' + esc(nx.code) : ''}</small>` : `<b class="cp-q">?</b><span>No exam dates yet</span><small><a data-a="tab" data-v="sem" style="color:inherit;text-decoration:underline;cursor:pointer">Plan my semester</a></small>`}</div>
<div class="hh-ace"><div class="say">${bub}</div><span class="ace" data-mood="wave"></span></div></section>
<div class="pad hm"><div class="hm-main">${signedIn() ? '' : `<a class="ban lt" style="text-decoration:none;margin-top:4px" href="../login/?next=campus"><span class="ic">🔐</span><span><b>Sign in to save your progress</b><span>Continue with Google or email. It follows you across devices.</span></span><em>›</em></a>`}
<button class="dly ${S.playedToday ? 'done' : ''}" data-a="tab" data-v="daily"><span class="di">${S.playedToday ? '✅' : '🎯'}</span><span><b>${t.dc}</b><span>${S.playedToday ? 'Done for today. A new set unlocks tomorrow.' : t.dcs}</span><span class="dots">${'<i></i>'.repeat(10)}</span></span><em>›</em></button>${window.AceF ? AceF.banner() : ''}${window.AceL ? AceL.homeCard(c) : ''}
<div class="sh">This week</div>${tasks.length ? `<div class="lst">${tasks.map(x => { const d = daysTo(x.due); return `<button class="li" data-a="tab" data-v="sem"><span class="e">${d < 0 ? '⚠️' : d <= 2 ? '⏰' : '📌'}</span><span class="m"><b>${esc(x.t)}</b><small>${esc(x.c || 'General')} • ${d < 0 ? 'overdue by ' + (-d) + (d === -1 ? ' day' : ' days') : d === 0 ? 'due today' : 'due in ' + d + (d === 1 ? ' day' : ' days')}</small></span><span class="v">${fmtD(x.due)}</span></button>` }).join('')}</div>` : `<button class="emp2 cp-add" data-a="tab" data-v="sem">No deadlines yet. Add assignments, tests and lab reports to see them here.</button>`}
<div class="sh">${t.sub}<a data-a="tab" data-v="subj">${t.all}</a></div><div class="sg">${tiles || `<div class="emp2" style="grid-column:1/-1">${ACE_LOADED.UN ? 'Choose your courses on the Courses tab.' : 'Loading your courses…'}</div>`}</div>
${soon.length ? `<div class="sh">On the way for you</div><div class="lst">${soon.map(x => `<div class="li"><span class="e">${ic(x.name)}</span><span class="m"><b>${esc(x.name)}</b><small>${esc(x.track)} • being written now</small></span><button class="bb cp-w" data-k="want" data-v="${esc(x.name)}">${st.want[x.name] ? '✓ Saved' : 'Notify me'}</button></div>`).join('')}</div>` : ''}</div>
<div class="hm-side"><div class="sh">Today's goal</div><div class="card goal2"><div class="gr" style="--p:${gp}"><span>${done >= P.goal ? '✓' : done}</span></div><div><b>Answer ${P.goal} questions</b><small>${Math.min(done, P.goal)} of ${P.goal} done today</small></div></div><button class="nx" data-a="tab" data-v="quiz">Practise</button>
<div class="sh">Semester</div><div class="lst"><button class="li" data-a="tab" data-v="sem"><span class="e">📆</span><span class="m"><b>Semester planner</b><small>${(st.sem.courses || []).length ? st.sem.courses.length + ' courses • ' + credits() + ' credits' : 'Courses, exam dates and deadlines'}</small></span>›</button><button class="li" data-a="tab" data-v="gpa"><span class="e">🧮</span><span class="m"><b>CGPA calculator</b><small>Your GPA and the grades you need</small></span>›</button><button class="li" data-a="aigen" data-v="buddy"><span class="e"><i class="aic"></i></span><span class="m"><b>Ask Ace</b><small>Step-by-step help with any course</small></span>›</button><button class="li" data-a="tab" data-v="notes"><span class="e">📝</span><span class="m"><b>Lecture notes to study pack</b><small>Paste notes, get questions and a summary</small></span>›</button></div></div></div>`;
  }
  const credits = () => (st.sem.courses || []).reduce((n, c) => n + (+c.cr || 0), 0);

  /* ---------- courses catalogue ---------- */
  function coursesView(c, t, ex) {
    const live = c.s, f = st.fac, soon = A.cat.filter(x => x.status === 'soon'), mine = soon.filter(x => f && x.faculties.includes(f)), rest = soon.filter(x => !mine.includes(x));
    const row = x => `<div class="li"><span class="e">${ic(x.name)}</span><span class="m"><b>${esc(x.name)}</b><small>${esc(x.track)}${x.faculties.length ? ' • ' + x.faculties.map(k => esc(A.facs[k] || k)).slice(0, 3).join(', ') : ''}</small></span><button class="bb cp-w" data-k="want" data-v="${esc(x.name)}">${st.want[x.name] ? '✓ Saved' : 'Notify me'}</button></div>`;
    return `<div class="pad"><div class="pg-h"><h1>Courses</h1><p>University courses, one at a time, written and checked by Ace</p></div>
<div class="sg sg-all">${live.map((s, i) => selOK(c, s) ? stile(c, t, ex, s, i) : '').join('') || `<div class="emp2" style="grid-column:1/-1">${ACE_LOADED.UN ? 'No course selected.' : 'Loading courses…'}</div>`}</div>
${typeof offBtn === 'function' ? offBtn() : ''}<p class="note">Each live course has narrated lessons, notes, practice for every topic, flashcards and a timed course final.</p>
${mine.length ? `<div class="sh">Coming next for ${esc(A.facs[f] || 'you')}</div><div class="lst">${mine.map(row).join('')}</div>` : ''}
${rest.length ? `<div class="sh">Also on the way</div><div class="lst">${rest.map(row).join('')}</div>` : ''}
<p class="note">Tap "Notify me" and the course will be at the top of your list when it goes live.</p></div>`;
  }

  /* ---------- tools ---------- */
  function toolsView(c) {
    const S_ = [['My study', [['🗓️', 'My study plan', 'Daily steps to exam day, built around your weak topics', '', 1, 'tab:plan'], ['📕', 'Mistakes notebook', 'Every question you missed, ready to redo', '', 0, 'tab:mist'], ['🏆', 'Weekly league', 'Earn XP and climb the table', '', 0, 'tab:league'], ['👯', 'Study friends', 'Friend streaks and friendly nudges', 'NEW', 0, 'tab:friends'], ['🏅', 'Achievements', 'Badges and your level', '', 0, 'tab:ach']]],
      ['Semester', [['📆', 'Semester planner', 'Courses, credits, exam dates and every deadline in one place', '', 1, 'tab:sem'], ['🧮', 'CGPA calculator', 'Your GPA, class of degree and what you need', '', 0, 'tab:gpa'], ['📝', 'Lecture notes', 'Paste notes, get a study pack', '', 0, 'tab:notes'], ['📚', 'Citation builder', 'APA and Harvard references', '', 0, 'tab:cite'], ['⏱️', 'Focus timer', 'Study 25 minutes, rest 5', '', 0, 'tab:focus']]],
      ['AI tools', [['<i class="aic"></i>', 'Ace, your study partner', 'Ask anything from your courses and get step-by-step help', '✨ AI', 1, 'ai:buddy'], ['🧠', 'Tutor mode', 'Hints first, so you work it out yourself', 'AI', 0, 'ai:tutor'], ['🔬', 'Smart solver', 'Worked solutions for maths and science', 'AI', 0, 'ai:solver'], ['✍️', 'Essay feedback', 'Paste a draft and get specific feedback', 'AI', 0, 'ai:essay'], ['📄', 'Question generator', 'Paste lecture notes, get practice questions', 'AI', 0, 'ai:qgen']]],
      ['Practice', [['📋', 'Course finals', 'Timed exams built from each course', '', 1, 'tab:quiz'], ['🃏', 'Flashcards', 'Definitions and formulas', '', 0, 'tab:flash'], ['⚡', 'Daily challenge', '10 questions a day keeps the streak going', '🔥', 0, 'tab:daily'], ['🎯', 'Weak topics', 'Your lowest-scoring topics', '', 0, 'tab:radar']]],
      ['Community', [['👥', 'Study groups', 'Moderated groups for your course and campus', '', 0, 'tab:groups'], ['🧑‍🏫', 'My classes', 'Join a lecturer\'s or tutor\'s class with a code', '', 0, 'tab:classes']]],
      ['Other Ace portals', [['🎓', 'Ace Academy', 'Certificate courses for skills and careers', '', 0, 'link:../academy/'], ['🏫', 'Ace for school', 'WAEC, KCSE, GCSE and other school exams', '', 0, 'link:../app/']]]];
    return `<div class="pad">` + S_.map(([h, l]) => { const odd = l.reduce((s, z) => s + (z[4] ? 2 : 1), 0) % 2 == 1; return `<div class="sh" style="margin-top:6px">${h}</div><div class="tg2" style="margin-bottom:16px">${l.map((a, ix) => { if (odd && ix == l.length - 1 && !a[4]) a = a.slice(), a[4] = 1; const [k, v] = a[5].split(':'), inner = `<span class="e">${a[0]}</span><b>${a[1]}</b><small>${a[2]}</small>${a[3] ? `<em>${a[3]}</em>` : ''}`; if (k == 'link') return `<a class="tc ${a[4] ? 'w' : ''}" href="${v}" style="text-decoration:none;color:inherit">${inner}</a>`; return `<button class="tc ${a[4] ? 'w' : ''}" ${k == 'ai' ? `data-a="aigen" data-v="${v}"` : `data-a="tab" data-v="${v}"`}>${inner}</button>` }).join('')}</div>` }).join('') + '</div>';
  }

  /* ---------- semester planner ---------- */
  const GR = { ng5: ['A', 'B', 'C', 'D', 'E', 'F'], us4: ['A', 'B', 'C', 'D', 'F'] };
  function semView(c) {
    const m = st.sem, sc = (window.AceX && AceX.gp && AceX.gp.mode === 'uk') ? 'uk' : ((window.AceX && AceX.gp && AceX.gp.scale) || 'ng5');
    const opts = A.cat.map(x => `<option value="${esc(x.name)}">`).join('');
    const inp = (p, v, ph, cls, type) => `<input class="xin ${cls || ''}" data-k-in="${p}" value="${esc(v)}" placeholder="${ph}" ${type ? `type="${type}"` : 'maxlength="60"'} ${p.endsWith('.n') ? 'list="cp-courses"' : ''}>`;
    let proj = '';
    if (m.courses.length && window.AceX && AceX.calc) {
      if (sc === 'uk') { const a = AceX.calc.ukAvg(m.courses.map(x => ({ credits: x.cr, mark: x.tg }))); proj = a.avg == null ? '' : `<b>${a.avg}%</b><small>projected average • ${AceX.calc.ukClass(a.avg)}</small>` }
      else { const a = AceX.calc.gpa(m.courses.map(x => ({ credits: x.cr, grade: x.tg })), sc); proj = a.gpa == null ? '' : `<b>${a.gpa.toFixed(2)}</b><small>projected GPA on the ${sc === 'ng5' ? '5.0' : '4.0'} scale${sc === 'ng5' ? ' • ' + AceX.calc.nigClass(a.gpa) : ''}</small>` }
    }
    const tasks = m.tasks.map((x, i) => [x, i]).sort((a, b) => (a[0].done - b[0].done) || ((a[0].due || '9') < (b[0].due || '9') ? -1 : 1));
    const cr = credits(), hrs = cr * 2;
    return `<div class="pad"><div class="bk"><button class="bb" data-a="tab" data-v="home">‹ Back</button></div><h2 style="margin:0 0 4px">Semester planner</h2><p class="note" style="margin:0 0 10px">Saved on this device. Exam dates feed the countdown on your home page.</p>
<datalist id="cp-courses">${opts}</datalist>
<label class="xl">Semester${inp('name', m.name, 'e.g. First semester 2026/27')}</label>
<div class="sh">Courses this semester</div>
${m.courses.map((x, i) => `<div class="card cp-c"><div class="cp-r">${inp('c.' + i + '.n', x.n, 'Course name')}${inp('c.' + i + '.code', x.code, 'Code', 'xs')}</div>
<div class="cp-r"><label class="xl">Credits${inp('c.' + i + '.cr', x.cr, '3', 'xs', 'number')}</label><label class="xl">Exam date${inp('c.' + i + '.exam', x.exam, '', '', 'date')}</label><label class="xl">${sc === 'uk' ? 'Target %' : 'Target grade'}${sc === 'uk' ? inp('c.' + i + '.tg', x.tg, '65', 'xs', 'number') : `<select class="xin xs" data-k-in="c.${i}.tg">${GR[sc].map(g => `<option ${x.tg === g ? 'selected' : ''}>${g}</option>`).join('')}</select>`}</label></div>
<div class="cp-r">${x.exam && daysTo(x.exam) >= 0 ? `<small class="note">${daysTo(x.exam)} days to the exam</small>` : '<span></span>'}<button class="xlink" data-k="cdel" data-v="${i}">Remove</button></div></div>`).join('')}
<button class="bt" style="width:100%" data-k="cadd">+ Add a course</button>
${m.courses.length ? `<div class="card cp-sum"><div><b>${cr}</b><small>credits</small></div><div><b>~${hrs} h</b><small>private study a week (a common rule of thumb is 2 hours per credit)</small></div>${proj ? `<div>${proj}</div>` : ''}</div>` : ''}
<div class="sh">Deadlines</div>
${tasks.map(([x, i]) => { const d = daysTo(x.due); return `<div class="card cp-t ${x.done ? 'dn' : ''}"><button class="sw" role="switch" aria-checked="${!!x.done}" data-k="tdone" data-v="${i}" aria-label="Done"></button><div class="cp-tm">${inp('t.' + i + '.t', x.t, 'Assignment, test or lab report')}<div class="cp-r"><select class="xin" data-k-in="t.${i}.c"><option value="">General</option>${m.courses.filter(z => z.n).map(z => `<option ${x.c === z.n ? 'selected' : ''}>${esc(z.n)}</option>`).join('')}</select>${inp('t.' + i + '.due', x.due, '', '', 'date')}</div>${x.due && !x.done ? `<small class="note" ${d < 0 ? 'style="color:var(--red)"' : ''}>${d < 0 ? 'Overdue by ' + (-d) + ' days' : d === 0 ? 'Due today' : 'Due in ' + d + ' days'}</small>` : ''}</div><button class="xlink" data-k="tdel" data-v="${i}" aria-label="Delete">✕</button></div>` }).join('')}
<button class="bt" style="width:100%" data-k="tadd">+ Add a deadline</button>
<p class="note">Grade boundaries differ between universities. Check your student handbook.</p></div>`;
  }

  /* ---------- onboarding ---------- */
  function uniList() {
    const cc = home(); if (A.U.cc === cc && A.U.list) return A.U.list;
    if (A.U.cc !== cc) { A.U.cc = cc; A.U.list = null; fetch('universities/' + cc + '.json').then(r => r.ok ? r.json() : Promise.reject()).then(d => { A.U.list = d.universities || []; if (S.tab === 'onb') render() }).catch(() => { A.U.list = []; if (S.tab === 'onb') render() }) }
    return null;
  }
  function onbView(c, t) {
    const o = S.ob || (S.ob = { i: 0 }), N = 6, L = (a) => a; let main = '', msg = '', mood = 'wave', foot = '';
    const opt = (k, v, on, icn, b, sm, i) => `<button class="op ${on ? 'pk' : ''}" style="--i:${Math.min(i, 8)}" data-k="${k}" data-v="${esc(v)}"><i>${icn}</i><span><b>${b}</b>${sm ? `<small class="ob-s">${sm}</small>` : ''}</span></button>`;
    const next = (dis, lbl) => `<div class="ls-foot"><button class="nx" data-k="on" ${dis ? 'disabled' : ''}>${lbl || 'Continue'}</button></div>`;
    if (o.i == 0) { msg = 'Hi! I\'m Ace. University moves fast, so let\'s set you up in under a minute.'; main = `<h2 class="qtext">Welcome to Ace Campus</h2><div class="stg"><p class="pl-p">Interactive lessons for your university courses, practice for every topic, timed course finals, and the tools for running a semester: deadlines, exam dates and your CGPA.</p></div>`; foot = next(0, 'Let\'s go') }
    else if (o.i == 1) { mood = 'think'; msg = 'Which country is your university in? I\'ll use its currency and grading.'; main = `<h2 class="qtext">Where do you study?</h2><div class="ob-c">${Object.keys(C).filter(k => k !== 'UN').map((k, i) => `<button class="op ${k === home() ? 'pk' : ''}" style="--i:${Math.min(i, 8)}" data-k="ocb" data-v="${k}"><i>${C[k].f}</i><span>${C[k].n}</span></button>`).join('')}</div>`; foot = next() }
    else if (o.i == 2) {
      mood = 'think'; msg = 'Pick your university, or type it if it isn\'t listed yet.'; const L_ = uniList(), q = A.U.q.trim().toLowerCase();
      const rows = L_ ? L_.filter(u => !q || (u.name + ' ' + (u.short || '') + ' ' + (u.city || '')).toLowerCase().includes(q)) : [];
      main = `<h2 class="qtext">Your university</h2><input class="xin" id="cp-uq" data-k-in="uq" value="${esc(A.U.q)}" placeholder="Search or type your university" autocomplete="off" style="margin-bottom:10px"><div class="ops" id="cp-ul">${L_ == null ? '<p class="note">Loading universities…</p>' : rows.map((u, i) => opt('ouni', u.id, st.uniId === u.id, '🏛️', esc(u.name), esc([u.short, u.city].filter(Boolean).join(' • ')), i)).join('') + (A.U.q.trim() && !rows.some(u => u.name.toLowerCase() === q) ? opt('ounit', A.U.q.trim(), st.uni === A.U.q.trim() && !st.uniId, '✏️', 'Use "' + esc(A.U.q.trim()) + '"', 'My university is not in the list', rows.length) : '')}</div>`;
      foot = next(!st.uni)
    }
    else if (o.i == 3) {
      mood = 'think'; msg = 'What are you studying? This decides which courses I suggest first.'; const u = (A.U.list || []).find(x => x.id === st.uniId);
      const facs = u ? u.faculties : [];
      main = `<h2 class="qtext">Your programme</h2><input class="xin" data-k-in="prog" value="${esc(st.prog)}" placeholder="e.g. Computer Science, Nursing, Accounting" maxlength="80" style="margin-bottom:10px">${facs.length ? facs.map(f => `<div class="sh" style="margin:12px 0 6px">${esc(f.name)}</div><div class="chips cp-chips">${f.courses.map(cs => `<button class="${st.prog === cs.name ? 'on' : ''}" data-k="oprog" data-v="${esc(cs.name)}" data-f="${esc(f.name)}">${esc(cs.name)}</button>`).join('')}</div>`).join('') : `<div class="chips cp-chips">${Object.keys(A.facs).map(k => `<button class="${st.fac === k ? 'on' : ''}" data-k="ofac" data-v="${k}">${esc(A.facs[k])}</button>`).join('')}</div><p class="note">Pick the area closest to your programme.</p>`}`;
      foot = next(!st.prog && !st.fac)
    }
    else if (o.i == 4) { mood = 'think'; msg = 'Which year are you in?'; main = `<h2 class="qtext">Your year</h2><div class="ops g2">${LV.UN.map((y, i) => opt('oyr', y, st.year === y, y === 'Postgraduate' ? '🎓' : String(i + 1), y, '', i)).join('')}</div>`; foot = next() }
    else if (o.i == 5) {
      mood = 'idle'; msg = 'Here are the courses for you. More arrive one at a time, each fully checked.';
      const sel = P.s.UN || c.s;
      main = `<h2 class="qtext">Your courses</h2><div class="ops">${c.s.map((s, i) => opt('ocs', s, sel.includes(s), ic(s), esc(s), 'Live now • lessons, practice and a course final', i)).join('')}</div>${A.cat.filter(x => x.status === 'soon' && (!st.fac || x.faculties.includes(st.fac))).slice(0, 5).map(x => `<div class="li ob-t"><span class="e">${ic(x.name)}</span><span class="m"><b>${esc(x.name)}</b><small>Coming soon</small></span><button class="bb cp-w" data-k="want" data-v="${esc(x.name)}">${st.want[x.name] ? '✓ Saved' : 'Notify me'}</button></div>`).join('')}`;
      foot = next(!sel.length)
    }
    else { mood = 'cheer'; msg = 'All set. Start with a lesson, or put your exam dates in first.'; main = `<h2 class="qtext">Ready when you are</h2><div class="stg"><p class="pl-p">${esc([st.uni, st.prog, st.year].filter(Boolean).join(' • '))}</p></div>`; foot = `<div class="ls-foot ob-f"><button class="nx" data-k="oend" data-v="subj">▶ Start ${esc((P.s.UN || c.s)[0] || 'learning')}</button><button class="bb" data-k="oend" data-v="sem">📆 Plan my semester</button></div>` }
    return `<div class="ls ob" data-key="cob|${o.i}" data-st=""><div class="ls-top">${o.i ? `<button class="ls-x" data-k="ob" aria-label="Back">‹</button>` : '<span class="ls-x" style="visibility:hidden"></span>'}${segs(N + 1, o.i, null, Array(N + 1).fill(1), true)}<button class="ls-ic ob-skip" data-k="oend" data-v="home">Skip</button></div><div class="ls-body">${lsSide(L, mood, msg, false)}<div class="ls-main">${main}</div></div>${foot}</div>`;
  }

  /* ---------- events ---------- */
  const setPath = (p, v) => { const m = st.sem; const [k, i, f] = p.split('.'); if (k === 'name') m.name = v; else if (k === 'c' && m.courses[+i]) m.courses[+i][f] = f === 'cr' ? v.replace(/[^\d.]/g, '') : v; else if (k === 't' && m.tasks[+i]) m.tasks[+i][f] = v; save(); updDate() };
  document.addEventListener('input', e => {
    const el = e.target.closest && e.target.closest('[data-k-in]'); if (!el) return; const p = el.dataset.kIn, v = el.value;
    if (p === 'uq') { A.U.q = v; const pos = el.selectionStart; render(); const n = document.getElementById('cp-uq'); if (n) { n.focus(); try { n.setSelectionRange(pos, pos) } catch (z) { } } return }
    if (p === 'prog') { st.prog = v; st.fac = facOf(v) || st.fac; save(); const b = document.querySelector('.ls-foot .nx'); if (b) b.disabled = !st.prog && !st.fac; return }
    setPath(p, v); if (el.tagName === 'SELECT' || el.type === 'date') render();
  });
  // no re-render on 'change': a blur-triggered render would replace the field the student just tapped
  document.addEventListener('click', e => {
    const b = e.target.closest && e.target.closest('[data-k]'); if (!b) return; const k = b.dataset.k, v = b.dataset.v, o = S.ob || (S.ob = { i: 0 }); let goTop = false;
    if (k === 'on') { o.i++; goTop = true }
    else if (k === 'ob') { o.i = Math.max(0, o.i - 1); goTop = true }
    else if (k === 'ocb') { A.setHome(v, true); st.uni = ''; st.uniId = ''; save() }
    else if (k === 'ouni') { const u = (A.U.list || []).find(x => x.id === v); if (u) { st.uniId = u.id; st.uni = u.name; save() } }
    else if (k === 'ounit') { st.uniId = ''; st.uni = v; save() }
    else if (k === 'oprog') { st.prog = v; st.fac = facOf(v) || facOf(b.dataset.f) || st.fac; save() }
    else if (k === 'ofac') { st.fac = v; if (!st.prog) st.prog = ''; save() }
    else if (k === 'oyr') { st.year = v; save() }
    else if (k === 'ocs') { const cur = (P.s.UN || C.UN.s).slice(), i = cur.indexOf(v); if (i >= 0) cur.splice(i, 1); else cur.push(v); P.s.UN = cur; svP() }
    else if (k === 'oend') { P.conb = 1; P.lvl = 'university'; if (!P.s.UN) P.s.UN = null; svP(); A.syncLevel(); S.ob = null; S.tab = v === 'subj' ? 'subj' : v; if (v === 'subj') { const i = C.UN.s.indexOf((P.s.UN || C.UN.s)[0]); S.sub = i >= 0 ? i : null } goTop = true }
    else if (k === 'edit') { P.conb = 0; S.ob = { i: 1 }; S.tab = 'onb'; goTop = true }
    else if (k === 'want') { if (st.want[v]) delete st.want[v]; else st.want[v] = todayStr(); save(); toast(st.want[v] ? 'Saved. It will be at the top of your list when it goes live.' : 'Removed.') }
    else if (k === 'cadd') { st.sem.courses.push({ n: '', code: '', cr: '3', exam: '', tg: (window.AceX && AceX.gp && AceX.gp.mode === 'uk') ? '65' : 'A' }); save() }
    else if (k === 'cdel') { st.sem.courses.splice(+v, 1); save(); updDate() }
    else if (k === 'tadd') { st.sem.tasks.push({ t: '', c: '', due: '', done: false }); save() }
    else if (k === 'tdel') { st.sem.tasks.splice(+v, 1); save() }
    else if (k === 'tdone') { const x = st.sem.tasks[+v]; if (x) { x.done = !x.done; save(); if (x.done && window.AceUI && AceUI.fx) try { AceUI.fx('ok') } catch (z) { } } }
    else return;
    e.preventDefault(); render(); if (goTop) window.scrollTo(0, 0);
  });
})();
