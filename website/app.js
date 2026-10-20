/* Ace Education site. Pages are rendered from SITE_DATA (built from the syllabus files) and the content in meta.js. */
const D = SITE_DATA, CCS = Object.keys(CM);
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const nf = n => Number(n).toLocaleString('en-US');
const $ = q => document.querySelector(q);

/* ---------- numbers computed from the data ---------- */
function tally(cc) {
  const v = D[cc]; let subs = 0, q = 0, t = 0, fc = 0;
  v.ex.forEach(e => e.s.forEach(s => { subs++; if (!s.sa) { q += s.q; t += s.t; fc += s.fc; } }));
  return {exams: v.ex.length, subs, q, t, fc, st: v.st};
}
const T = {}; CCS.forEach(cc => T[cc] = tally(cc));
const TOT = CCS.reduce((a, cc) => ({exams: a.exams + T[cc].exams, subs: a.subs + T[cc].subs, q: a.q + T[cc].q, t: a.t + T[cc].t, fc: a.fc + T[cc].fc}), {exams: 0, subs: 0, q: 0, t: 0, fc: 0});
const LIVE = FEATURES.filter(f => f[3] === 'Live').length;

/* ---------- state ---------- */
const S = {page: 'home', arg: null, hero: 'NG', picked: null, anim: true, snd: true, gfilter: 'All', ffilter: 'All', ex: {cc: 'NG', ex: 0, sub: 0, q: ''}, formDone: null, cq: {}};
const NAV = [['home','Home'],['countries','Countries'],['features','Features'],['syllabus','Syllabus'],['schools','Schools'],['guides','Guides'],['about','About'],['contact','Contact']];

const SLUG = {NG:'nigeria',GH:'ghana',SL:'sierra-leone',GM:'gambia',KE:'kenya',ZM:'zambia',GB:'united-kingdom',CA:'canada',ES:'spain',IE:'ireland',ZA:'south-africa',UG:'uganda',TZ:'tanzania',LR:'liberia',MT:'malta'};
const PAGES = ['countries','features','syllabus','schools','guides','about','contact','quote','privacy','terms'];
const pathFor = (page, arg) => page === 'home' ? './' : page === 'country' ? 'exam-prep-' + SLUG[arg] : page === 'guide' ? 'guide-' + arg : page;
function parseRoute(r) {
  r = String(r || '').replace(/\.html$/, '').replace(/\/+$/, '');
  if (!r || r === 'index') return ['home', null];
  let m = r.match(/^exam-prep-(.+)$/);
  if (m) { const cc = Object.keys(SLUG).find(k => SLUG[k] === m[1]); if (cc) return ['country', cc]; }
  m = r.match(/^guide-(.+)$/);
  if (m && GUIDES.some(g => g[0] === m[1])) return ['guide', m[1]];
  if (PAGES.includes(r)) return [r, null];
  return ['home', null];
}
function go(page, arg) {
  S.page = page; S.arg = arg || null; S.formDone = null;
  try { history.pushState(null, '', pathFor(page, arg)); } catch (e) {}
  render(); window.scrollTo(0, 0);
  try { document.title = routeMeta(S.page, S.arg).title; } catch (e) {}
}
function fromLocation() {
  let q = '', h = '';
  try { q = new URLSearchParams(location.search).get('route'); h = (location.hash || '').slice(1); } catch (e) {}
  if (q != null) { [S.page, S.arg] = parseRoute(q); return; }
  const m = h.match(/^(country|guide)-(.+)$/);                      // old #country-NG links still work
  if (m) { S.page = m[1]; S.arg = m[1] === 'country' ? m[2].toUpperCase() : m[2]; return; }
  if (h && (PAGES.includes(h))) { S.page = h; return; }
  let seg = ''; try { seg = location.pathname.split('/').pop(); } catch (e) {}
  [S.page, S.arg] = parseRoute(seg);
}
window.addEventListener('popstate', () => { fromLocation(); render(); });

/* ---------- search and AI metadata for every page ---------- */
const exNames = cc => D[cc].ex.map(e => e.k);
const joinAnd = a => a.length < 2 ? a.join('') : a.slice(0, -1).join(', ') + ' and ' + a[a.length - 1];
function countryFaq(cc) {
  const c = CM[cc], t = T[cc], ex = exNames(cc), first = D[cc].ex[0], subs = first.s.map(x => x.n);
  return [
    [`Which exams can I prepare for in ${c.name} with Ace Education?`, `${c.sys} Ace Education covers ${joinAnd(ex)} in ${c.name}, with ${t.subs} subjects and ${nf(t.q)} practice questions in total.`],
    [`How do I prepare for ${joinAnd(ex.slice(0, 3))} in ${c.name}?`, `Open a subject, read the topic notes, take the five-question quiz, then sit a timed mock exam when you have covered a module. Ace Education shows your weakest topics so you know what to revise next.`],
    [`Which ${first.k} subjects are covered in ${c.name}?`, `${subs.slice(0, 14).join(', ')}${subs.length > 14 ? ' and ' + (subs.length - 14) + ' more' : ''}.`],
    [`How is ${first.k} graded in ${c.name}?`, `${c.scale} Levels covered: ${c.levels}.`],
    [`Can I start studying for ${c.name} exams without a school code?`, `Yes. Anyone can create a student account on the sign-up page and choose their country, level and exam. Schools and centres can also join with a school code or ask us for a quote.`]
  ];
}
function routeMeta(page, arg) {
  const base = (typeof SITE_URL !== 'undefined' ? SITE_URL : ''), P = pathFor(page, arg), url = base + (P === './' ? '' : P);
  const org = {'@type': 'Organization', '@id': base + '#org', name: 'Ace Education', url: base || undefined, logo: base + 'og-image.png', description: 'Exam preparation and study app for secondary school and university students in Nigeria, Ghana, Sierra Leone, The Gambia, Kenya, Zambia, Uganda, Tanzania, South Africa, the UK, Canada, Ireland and Spain.'};
  const crumbs = items => ({'@type': 'BreadcrumbList', itemListElement: items.map((x, i) => ({'@type': 'ListItem', position: i + 1, name: x[0], item: base + x[1]}))});
  const faq = qa => ({'@type': 'FAQPage', mainEntity: qa.map(f => ({'@type': 'Question', name: f[0], acceptedAnswer: {'@type': 'Answer', text: f[1]}}))});
  const out = {path: P === './' ? '' : P, url, type: 'website', ld: []};
  if (page === 'home') {
    out.title = `Ace Education: Exam Prep and Study App for ${CCS.length} Countries`;
    out.description = `Free-to-start exam prep and study app for secondary school and university students: WASSCE, NECO, JAMB, KCSE, GCSE, A-Level, NSC, UCE, CSEE, Leaving Cert, OSSD and EBAU. ${nf(TOT.q)} practice questions, topic notes, flashcards and mock exams.`.replace('Free-to-start ', '');
    out.ld = [org, {'@type': 'WebSite', '@id': base + '#site', url: base || undefined, name: 'Ace Education', publisher: {'@id': base + '#org'}, inLanguage: ['en', 'es']},
      {'@type': 'SoftwareApplication', name: 'Ace Education', applicationCategory: 'EducationalApplication', operatingSystem: 'Web (any phone, tablet or computer browser)', description: out.description, url: base || undefined, publisher: {'@id': base + '#org'}},
      faq(FAQ.slice(0, 6))];
  } else if (page === 'country') {
    const c = CM[arg], t = T[arg], ex = exNames(arg), qa = countryFaq(arg);
    out.title = `${joinAnd(ex.slice(0, 3)).replace(' and ', ' & ')} Exam Prep in ${c.name} | Ace Education`;
    out.description = `${c.name} exam prep: ${ex.join(', ')}. ${t.subs} subjects, ${nf(t.q)} practice questions, ${nf(t.t)} topic notes, quizzes, flashcards and timed mock exams.`;
    out.lang = arg === 'ES' ? 'es-ES' : 'en-' + arg;
    out.faq = qa;
    out.ld = [org, crumbs([['Home', ''], ['Exam prep in ' + c.name, P]]), faq(qa), {'@type': 'WebPage', name: out.title, url, about: ex.map(e => ({'@type': 'Thing', name: e})), inLanguage: arg === 'ES' ? 'es' : 'en', isPartOf: {'@id': base + '#site'}}];
  } else if (page === 'guide') {
    const g = GUIDES.find(x => x[0] === arg);
    out.title = `${g[2]} | Ace Education Study Guides`; out.description = g[3]; out.type = 'article';
    out.ld = [org, crumbs([['Home', ''], ['Guides', 'guides'], [g[2], P]]), {'@type': 'Article', headline: g[2], description: g[3], author: {'@id': base + '#org'}, publisher: {'@id': base + '#org'}, mainEntityOfPage: url}];
  } else {
    const M = {
      countries: ['Exam Prep by Country: 13 Countries, 23 Exams | Ace Education', `Compare the exams Ace Education covers in ${CCS.length} countries: ${CCS.map(cc => CM[cc].name).join(', ')}. Grading scales, subjects and question counts for each.`],
      features: ['Features: Topic Notes, Quizzes, Flashcards, Mock Exams and AI Tutor | Ace Education', 'Everything in the Ace Education study app: topic notes, quizzes, a question bank, flashcards, timed mock exams, daily challenge, weak-topic radar, an AI study buddy and university guides.'],
      syllabus: ['Syllabus Explorer: Topics and Sample Questions for Every Subject | Ace Education', 'Browse every subject, module and topic Ace Education covers for each exam in each country, with real sample questions.'],
      schools: ['Ace Education for Schools: Class, Teacher and Admin Tools', 'Run exam preparation for a whole class or school: add students, assign topics and quizzes, read class results and control AI help. Built for schools and tutoring centres.'],
      quote: ['Get a School Quote | Ace Education', 'Tell us about your school, tutoring centre or organisation and we will send a plan that fits. Pricing is agreed per school or centre.'],
      guides: ['Study Guides: Revision, Mock Exams and Exam Stress | Ace Education', 'Plain-language guides on active recall, mock exams, six-week revision plans, maths habits, science practicals, comparing exam systems and managing exam stress.'],
      about: ['About Ace Education: Exam Prep Built for Each Country', 'Why we build exam preparation separately for each country, how content is written and checked, and where we are going next.'],
      contact: ['Contact Ace Education', 'Ask about the app, a school plan, a missing subject or a mistake you found. We reply within one business day.'],
      privacy: ['Privacy Policy | Ace Education', 'How Ace Education handles student data, what we collect, what we do not do, and the data-protection law we design for in each country.'],
      terms: ['Terms of Use | Ace Education', 'The terms for using the Ace Education study app and website.']
    }[page] || ['Ace Education', ''];
    out.title = M[0]; out.description = M[1];
    out.ld = [org, crumbs([['Home', ''], [M[0].split(' | ')[0], P]])];
    if (page === 'contact' || page === 'quote') out.ld.push(faq(FAQ.slice(0, 6)));
  }
  return out;
}

/* ---------- Ace the pencil, sound and confetti (same character as the student app) ---------- */
const ACE_SVG = `<svg viewBox="0 0 100 140" aria-hidden="true"><g class="a-all" stroke="#17123A" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<path class="a-arm-l" d="M27 70 L13 84" fill="none"/><circle class="a-arm-l" cx="12" cy="85" r="3.5" fill="#FFC72C"/>
<path class="a-arm-r" d="M73 70 L87 84" fill="none"/><circle class="a-arm-r" cx="88" cy="85" r="3.5" fill="#FFC72C"/>
<rect x="29" y="7" width="42" height="19" rx="9" fill="#FF8FB1"/>
<rect x="27" y="24" width="46" height="13" rx="2" fill="#CBD0EC"/><path d="M27 30.5h46" fill="none" stroke-width="2"/>
<path d="M27 37h46v61H27z" fill="#FFC72C"/><path d="M27 37h11v61H27z" fill="#F2AE12" stroke="none"/><path d="M62 37h11v61H62z" fill="#FFDB6E" stroke="none"/><path d="M27 37h46v61H27z" fill="none"/>
<path d="M27 98h46L50 133z" fill="#F7D9AE"/><path d="M42.6 121.6h14.8L50 133z" fill="#3B3358"/>
<g class="a-eyes"><ellipse cx="41" cy="60" rx="6" ry="7" fill="#fff"/><ellipse cx="59" cy="60" rx="6" ry="7" fill="#fff"/>
<g class="a-pupils" stroke="none" fill="#17123A"><circle cx="42" cy="61" r="3.3"/><circle cx="60" cy="61" r="3.3"/><circle cx="43.2" cy="59.6" r="1.1" fill="#fff"/><circle cx="61.2" cy="59.6" r="1.1" fill="#fff"/></g></g>
<g stroke="none" fill="#FF8FB1" opacity=".75"><ellipse cx="34" cy="73" rx="4" ry="2.6"/><ellipse cx="66" cy="73" rx="4" ry="2.6"/></g>
<path class="mo m-smile" d="M43 73 Q50 80 57 73" fill="none"/>
<path class="mo m-open" d="M42.5 71.5 Q50 86 57.5 71.5 Z" fill="#17123A"/>
<path class="mo m-oops" d="M44 77 Q50 71.5 56 77" fill="none"/>
<path class="mo m-think" d="M45 76 L56 73.5" fill="none"/>
<path class="brow" d="M35 50 L45 48.5 M55 48.5 L65 50" fill="none" stroke-width="2.5"/>
<g class="a-spark" fill="#FFC72C" stroke-width="2"><path d="M12 22l3 7 7 3-7 3-3 7-3-7-7-3 7-3z"/><path d="M86 12l2.4 5.6 5.6 2.4-5.6 2.4L86 28l-2.4-5.6L78 20l5.6-2.4z"/></g>
<path class="a-drop" d="M80 40 Q84 47 80 50 Q76 47 80 40z" fill="#8FD3FF" stroke-width="2"/>
</g></svg>`;
const PENCIL = '<svg class="pc" viewBox="0 0 100 140" aria-hidden="true"><g stroke="#17123A" stroke-width="5" stroke-linejoin="round"><rect x="29" y="7" width="42" height="19" rx="9" fill="#FF8FB1"/><rect x="27" y="24" width="46" height="13" rx="2" fill="#CBD0EC"/><path d="M27 37h46v61H27z" fill="#FFC72C"/><path d="M27 98h46L50 133z" fill="#F7D9AE"/><path d="M42.6 121.6h14.8L50 133z" fill="#3B3358"/></g><circle cx="42" cy="61" r="5" fill="#17123A"/><circle cx="60" cy="61" r="5" fill="#17123A"/></svg>';
const ace = mood => `<span class="ace" data-mood="${mood}">${ACE_SVG}</span>`;
let AC = null;
function tone(f, t0, d, v, type, to) { try { AC = AC || new (window.AudioContext || window.webkitAudioContext)(); const o = AC.createOscillator(), g = AC.createGain(), st = AC.currentTime + t0; o.type = type || 'sine'; o.frequency.setValueAtTime(f, st); if (to) o.frequency.exponentialRampToValueAtTime(to, st + d); g.gain.setValueAtTime(0.0001, st); g.gain.exponentialRampToValueAtTime(v || 0.1, st + 0.012); g.gain.exponentialRampToValueAtTime(0.0001, st + d); o.connect(g); g.connect(AC.destination); o.start(st); o.stop(st + d + 0.05); } catch (e) {} }
const SFX = {pick: () => S.snd && tone(620, 0, 0.09, 0.07, 'triangle', 880), ok: () => S.snd && [784, 988, 1319].forEach((f, i) => tone(f, i * 0.075, 0.32, 0.1)), no: () => S.snd && tone(220, 0, 0.22, 0.1, 'sawtooth', 130)};
function confetti(x, y) {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return; let c = document.getElementById('fxc'); if (!c) { c = document.createElement('canvas'); c.id = 'fxc'; document.body.appendChild(c); }
  const d = devicePixelRatio || 1, W = c.width = innerWidth * d, H = c.height = innerHeight * d, g = c.getContext('2d'), col = ['#3D35F5', '#FFC72C', '#12B886', '#FF5A5F', '#FF8FB1'];
  const P = Array.from({length: 60}, () => ({x: x * d, y: y * d, vx: (Math.random() - 0.5) * 13 * d, vy: (-Math.random() * 10 - 4) * d, r: (Math.random() * 5 + 4) * d, a: Math.random() * 6, c: col[Math.floor(Math.random() * 5)]})), t0 = performance.now();
  (function f(t) { const k = (t - t0) / 1000; g.clearRect(0, 0, W, H); P.forEach(p => { p.vy += 0.5 * d; p.x += p.vx; p.y += p.vy; p.a += 0.2; g.save(); g.translate(p.x, p.y); g.rotate(p.a); g.globalAlpha = Math.max(0, 1 - k / 1.6); g.fillStyle = p.c; g.fillRect(-p.r / 2, -p.r / 4, p.r, p.r / 2); g.restore(); }); if (k < 1.6) requestAnimationFrame(f); else g.clearRect(0, 0, W, H); })(t0);
}
const words = t => esc(t).split(/(\s+)/).map((w, i) => /^\s+$/.test(w) || !w ? w : `<span class="w" style="--d:${Math.min(i >> 1, 40)}">${w}</span>`).join('');

/* ---------- shared pieces ---------- */
const btnGo = (page, label, cls = '', arg = '') => `<button class="btn ${cls}" data-go="${page}" data-arg="${arg}">${label}</button>`;
const appBtn = (label = 'Open the student app', cls = 'primary') => `<a class="btn ${cls}" href="${esc(SITE_CONFIG.appUrl)}" target="_blank" rel="noopener">${label}</a>`;
const head = (eyebrow, title, lede, c) => `<div class="hd ${c ? 'c' : ''}"><div class="eyebrow mono">${esc(eyebrow)}</div><h2>${title}</h2>${lede ? `<p class="lede">${lede}</p>` : ''}</div>`;
const pill = s => `<span class="pill ${s === 'Live' ? 'live' : s === 'Backend ready' ? 'back' : s === 'Planned' ? 'plan' : ''}">${esc(s)}</span>`;
const cMeta = cc => `${CM[cc].flag} ${CM[cc].name}`;

function qSheet(cc, key) {
  const smp = D[cc].sample; if (!smp) return '';
  const P = S.picked && S.picked.key === key ? S.picked : null, pick = P ? P.i : null, done = !!(P && P.done), ok = done && pick === smp.a;
  const mood = done ? (ok ? 'cheer' : 'oops') : 'think', anim = S.anim && !P;
  const msg = done ? (ok ? 'Yes! That\'s it.' : 'Not quite. Here\'s why.') : 'Have a go. I won\'t give you the answer, but I\'ll explain it after.';
  return `<div class="sheet ${anim ? 'in' : ''}"><div class="lsn-top"><span class="mono" style="flex:1">${esc(smp.ex)}, ${esc(smp.s)}. A real question from the app</span><button class="lsn-ic" data-act="snd" aria-label="${S.snd ? 'Mute sound' : 'Turn sound on'}">${S.snd ? '🔊' : '🔈'}</button></div>
  <div class="coach">${ace(mood)}<div class="say" aria-live="polite">${msg}</div></div>
  <p class="q">${anim ? words(smp.q) : esc(smp.q)}</p><div class="opts">${smp.o.map((o, i) => `<button class="opt ${done ? (i === smp.a ? 'good' : i === pick ? 'bad' : 'dim') : i === pick ? 'pk' : ''}" style="--i:${i}" data-act="pick" data-key="${key}" data-i="${i}" ${done ? 'disabled' : ''}><span class="b">${'ABCD'[i]}</span><span>${esc(o)}</span></button>`).join('')}</div>
  ${done ? `<div class="why ${ok ? 'good' : 'bad'}"><b>${ok ? '✓ Correct' : '✗ Not this one'}</b>${ok ? '' : `<p style="margin-bottom:.3rem"><strong>Answer: ${'ABCD'[smp.a]}. ${esc(smp.o[smp.a])}</strong></p>`}${esc(smp.e)}<p class="mono" style="margin-top:.5rem">Topic: ${esc(smp.t)}</p></div>` : `<button class="btn primary chk" data-act="check" data-key="${key}" ${pick === null ? 'disabled' : ''}>Check</button>`}</div>`;
}
function workedBlock(cc) {
  const w = D[cc].we; if (!w) return '';
  return `<div class="worked"><div class="mono">Worked example · ${esc(D[cc].sample.s)}</div><h3 style="margin:.4rem 0 .5rem">${esc(w.t)}</h3><p><b>${esc(w.p)}</b></p>${w.s.map(x => `<p>${esc(x)}</p>`).join('')}<p class="ans">${esc(w.a)}</p>${w.c ? `<p class="chk">${esc(w.c)}</p>` : ''}</div>`;
}
function statusLine(cc) {
  const [qt, qr, nt, nr] = D[cc].st;
  return `${nf(nt - nr)} of ${nf(nt)} notes and ${nf(qt - qr)} of ${nf(qt)} questions still need teacher review`;
}
function faqList(n) {
  return `<div class="faq">${FAQ.slice(0, n || FAQ.length).map(f => `<details><summary>${esc(f[0])}</summary><p>${esc(f[1])}</p></details>`).join('')}</div>`;
}
function countryCard(cc) {
  const t = T[cc], ex = D[cc].ex.map(e => e.k).join(' · ');
  return `<button class="card" data-go="country" data-arg="${cc}"><div class="ctry"><span class="fl">${CM[cc].flag}</span><b>${esc(CM[cc].name)}</b><small>${esc(ex)}</small></div><p>${esc(CM[cc].sys)}</p><div class="meta"><span>${t.subs} subjects</span><span>${nf(t.q)} questions</span><span>${nf(t.t)} topics</span></div></button>`;
}

/* ---------- pages ---------- */
function pHome() {
  return `<section class="hero"><div><div class="eyebrow mono">Exam prep in ${CCS.length} countries</div>
  <h1>Practise on questions written for the exam you will sit.</h1>
  <p class="lead">Ace Education is an exam prep and study app for secondary school and university students. It gives topic notes, quizzes, flashcards, timed mock exams and an AI study buddy for ${TOT.exams} exams in ${CCS.length} countries, including WASSCE, NECO, JAMB, BECE, KCSE, ECZ, UCE, CSEE, NSC, GCSE, A-Level, OSSD, the Leaving Cert and EBAU.</p>
  <div class="cta">${appBtn()}${btnGo('countries', 'See your country', '')}</div>
  <div class="facts"><div><b>${CCS.length}</b><span>countries open</span></div><div><b>${TOT.exams}</b><span>exams</span></div><div><b>${nf(TOT.q)}</b><span>practice questions</span></div><div><b>${nf(TOT.t)}</b><span>topic notes</span></div></div></div>
  <div><div class="chips" role="tablist" aria-label="Pick a country">${CCS.map(cc => `<button class="chip ${S.hero === cc ? 'on' : ''}" data-act="hero" data-cc="${cc}">${CM[cc].flag} ${cc}</button>`).join('')}</div>${qSheet(S.hero, 'hero')}</div></section>

  <section class="blk"><div class="wrap">${head('Countries', 'Built country by country, not translated from one.', 'Each country has its own exam bodies, subject list, currency, tax rate and examples. Pick a country to see what is open and what is coming.')}
  <div class="grid g3">${CCS.map(countryCard).join('')}</div></div></section>

  <section class="band"><div class="wrap"><section class="blk">${head('The student app', 'Learn a topic, test it, then sit a mock.', 'Every subject is split into modules and topics that follow the exam syllabus. Each topic works the same way, so students always know what to do next.')}
  <div class="split"><div class="grid g2">${FEATURES.filter(f => f[3] === 'Live').slice(0, 6).map(f => `<div class="card"><span class="ic">${f[0]}</span><h3>${esc(f[1])}</h3><p>${esc(f[2])}</p></div>`).join('')}</div>${workedBlock(S.hero)}</div>
  <div class="cta">${btnGo('features', 'All features', 'primary')}${btnGo('syllabus', 'Browse the syllabus')}</div></section></div></section>

  <section class="blk"><div class="wrap">${head('How content is made', 'Written from the syllabus, checked by code, then by teachers.')}
  <div class="grid g3"><div class="card"><span class="ic">📑</span><h3>Written from the syllabus</h3><p>Topic lists follow the published subject syllabus of each exam body. Notes and questions are written fresh for the app, not copied from past papers or textbooks.</p></div>
  <div class="card"><span class="ic">🧮</span><h3>Every number is recomputed</h3><p>Answers in mathematics, physics, chemistry, economics and accounting are worked out by a program before they go in. Duplicate options and answer positions are checked as well.</p></div>
  <div class="card"><span class="ic">🏷️</span><h3>Labelled until a teacher signs off</h3><p>New material carries a "needs review" label until a subject teacher approves it. That review is the next stage, and the label tells students where each item stands.</p></div></div></div></section>

  <section class="band"><div class="wrap"><section class="blk"><div class="split"><div>${head('For schools', 'Tools for teachers and school admins.', 'Any student can sign up and practise alone. Schools get a school code, a staff dashboard and class results, so a whole class can use Ace Education together.')}
  <ul class="ticks">${SCHOOL_STATUS.map(s => `<li><span><b>${esc(s[0])}.</b> ${esc(s[1])}</span></li>`).join('')}</ul><div class="cta">${btnGo('schools', 'See the school plan', 'primary')}${btnGo('quote', 'Get a quote')}</div></div>
  <div class="grid">${SCHOOL.map(r => `<div class="card"><h3><span class="ic">${r[0]}</span>${esc(r[1])}</h3><p>${esc(r[2])}</p></div>`).join('')}</div></div></section></div></section>

  <section class="blk"><div class="wrap">${head('Questions', 'Straight answers.')}${faqList(5)}<div class="cta">${btnGo('contact', 'Ask us something else')}</div></div></section>

  <section class="band"><div class="wrap"><section class="blk" style="text-align:center"><h2>Ready to practise?</h2><p class="lede" style="margin-inline:auto">Open the app, choose your country and your exam, and start with the first topic you are unsure about.</p><div class="cta" style="justify-content:center">${appBtn()}<a class="btn" href="${esc(SITE_CONFIG.loginUrl)}" target="_blank" rel="noopener">Sign in</a></div></section></div></section>`;
}

function pCountries() {
  return `<section class="blk"><div class="wrap">${head('Countries', `${CCS.length} countries, ${TOT.exams} exams.`, 'Pick a country for its exams, subjects, grading scale and a real question. More countries are added by adding a syllabus file, so the list grows without rebuilding the app.')}
  <div class="grid g3">${CCS.map(countryCard).join('')}</div>
  <div style="margin-top:3rem">${head('Exam systems side by side', 'How the exams compare.')}
  <div class="tw"><table class="tbl"><thead><tr><th>Country</th><th>Exams in Ace</th><th>Body</th><th>Grading</th><th>Levels</th><th>Language</th></tr></thead><tbody>${CCS.map(cc => `<tr><td><button class="lnk" data-go="country" data-arg="${cc}">${cMeta(cc)}</button></td><td>${esc(D[cc].ex.map(e => e.k).join(', '))}</td><td>${esc([...new Set(D[cc].ex.map(e => e.b))].join('; '))}</td><td>${esc(CM[cc].scale)}</td><td>${esc(CM[cc].levels)}</td><td>${esc(CM[cc].lang)}</td></tr>`).join('')}</tbody></table></div></div>
  <div style="margin-top:3rem">${head('Content status', 'What is in each country today.', 'These numbers are counted from each country\'s syllabus file when the site is built. "Needs review" means a subject teacher has not yet signed the item off.')}
  <div class="tw"><table class="tbl"><thead><tr><th>Country</th><th class="n">Exams</th><th class="n">Subjects</th><th class="n">Topics</th><th class="n">Questions</th><th class="n">Flashcards</th><th class="n">Notes needing review</th></tr></thead><tbody>${CCS.map(cc => { const t = T[cc], st = D[cc].st; return `<tr><td>${cMeta(cc)}</td><td class="n">${t.exams}</td><td class="n">${t.subs}</td><td class="n">${nf(t.t)}</td><td class="n">${nf(t.q)}</td><td class="n">${nf(t.fc)}</td><td class="n">${nf(st[2] - st[3])} of ${nf(st[2])}</td></tr>` }).join('')}<tr><td><b>Total</b></td><td class="n"><b>${TOT.exams}</b></td><td class="n"><b>${TOT.subs}</b></td><td class="n"><b>${nf(TOT.t)}</b></td><td class="n"><b>${nf(TOT.q)}</b></td><td class="n"><b>${nf(TOT.fc)}</b></td><td class="n"></td></tr></tbody></table></div>
  <p class="mono" style="margin-top:.7rem">Where a subject reuses another exam's content (for example some NECO subjects), it is counted once.</p></div></div></section>`;
}

function pCountry(cc) {
  if (!CM[cc]) return pCountries();
  const c = CM[cc], t = T[cc], v = D[cc];
  const exs = v.ex.map((e, ei) => `<div class="card" style="gap:.8rem"><div style="display:flex;gap:.6rem;align-items:baseline;flex-wrap:wrap"><h3>${esc(e.k)}</h3><span class="mono">${esc(e.b)}</span></div><p>${esc(c.ex[e.k] || '')}</p>
  <div class="tw"><table class="tbl"><thead><tr><th>Subject</th><th class="n">Topics</th><th class="n">Questions</th><th class="n">Mock</th></tr></thead><tbody>${e.s.map((s, si) => `<tr><td><button class="lnk" data-act="explore" data-cc="${cc}" data-ei="${ei}" data-si="${si}">${esc(s.n)}</button>${s.sa ? ' <span class="pill">uses WASSCE content</span>' : ''}</td><td class="n">${s.t}</td><td class="n">${nf(s.q)}</td><td class="n">${s.mk[0] ? s.mk[0] + ' Qs · ' + s.mk[1] + ' min' : ''}</td></tr>`).join('')}</tbody></table></div></div>`).join('');
  return `<section class="blk"><div class="wrap"><div class="crumb"><a data-go="countries">Countries</a><span>/</span><span>${esc(c.name)}</span></div>
  <div class="hero" style="padding-top:0"><div><div class="eyebrow mono">${esc(c.lang)} · ${esc(c.levels)}</div><h1>${c.flag} ${esc(c.name)}</h1><p class="lead">${esc(c.intro)}</p><div class="cta">${appBtn('Open the app')}${btnGo('syllabus', 'Browse the syllabus', '')}</div></div>${qSheet(cc, 'c' + cc)}</div>
  <div class="stat4"><div><b>${t.exams}</b><span>${t.exams==1?'exam':'exams'}</span></div><div><b>${t.subs}</b><span>subjects</span></div><div><b>${nf(t.t)}</b><span>topics with notes</span></div><div><b>${nf(t.q)}</b><span>practice questions</span></div></div>
  <div style="margin-top:3rem">${head('Exams', c.sys)}<div class="grid">${exs}</div></div>
  <div class="split" style="margin-top:3rem;align-items:start"><div>${head('Grading and rules', 'Know the scale.')}<ul class="ticks"><li><span><b>Grading.</b> ${esc(c.scale)}</span></li><li><span><b>Levels covered.</b> ${esc(c.levels)}</span></li><li><span><b>Currency in questions.</b> ${esc(v.cur || 'n/a')}</span></li><li><span><b>Data protection.</b> ${esc(c.law)}</span></li></ul></div>${workedBlock(cc)}</div>
  <div style="margin-top:3rem" class="split"><div><h3>Content status</h3><p class="lede" style="font-size:1rem">${esc(statusLine(cc))}.</p></div><div><h3>Coming next in ${esc(c.name)}</h3><ul class="ticks">${c.next.map(n => `<li><span>${esc(n)}</span></li>`).join('')}</ul></div></div>
  <div style="margin-top:3rem">${head('Questions', 'Common questions about ' + c.name + '.')}<div class="faq">${countryFaq(cc).map(f => `<details><summary>${esc(f[0])}</summary><p>${esc(f[1])}</p></details>`).join('')}</div></div>
  <div class="cta" style="margin-top:2rem">${btnGo('contact', 'Ask for a subject')}${btnGo('quote', 'Get a school quote')}</div></div></section>`;
}

function pFeatures() {
  const groups = ['All', ...new Set(FEATURES.map(f => f[4]))], list = FEATURES.filter(f => S.ffilter === 'All' || f[4] === S.ffilter);
  return `<section class="blk"><div class="wrap">${head('Features', 'Everything in the app, and exactly where it stands.', `${LIVE} features are live. Others are marked "Backend ready" or "Planned" so nobody has to guess what works today.`)}
  <div class="tabs">${groups.map(g => `<button class="tab ${S.ffilter === g ? 'on' : ''}" data-act="ffilter" data-v="${esc(g)}">${esc(g)}</button>`).join('')}</div>
  <div class="grid g3">${list.map(f => `<div class="card"><h3><span class="ic">${f[0]}</span>${esc(f[1])}</h3><div>${pill(f[3])}</div><p>${esc(f[2])}</p></div>`).join('')}</div>
  <div style="margin-top:3rem">${head('How Ace compares', 'Compared with the usual alternatives.', 'A general view of the kinds of study tools students use. It is not a review of any named product.')}
  <div class="tw"><table class="tbl cmp"><thead><tr><th>What students need</th><th>Ace Education</th><th>Generic global study apps</th><th>Video lessons</th><th>Past-paper PDFs</th></tr></thead><tbody>${COMPARE.map(r => `<tr><td>${esc(r[0])}</td>${r.slice(1).map(x => `<td class="${x === 'yes' || x === 'Yes' ? 'y' : x === 'No' ? 'no' : x === 'Rarely' || x === 'Rarely' ? 'no' : 'pt'}">${x === 'yes' ? '✓ Yes' : esc(x)}</td>`).join('')}</tr>`).join('')}</tbody></table></div></div>
  <div class="cta">${appBtn()}${btnGo('schools', 'For schools')}</div></div></section>`;
}

function pSyllabus() {
  const E = S.ex, v = D[E.cc], e = v.ex[E.ex] || v.ex[0], s = e.s[E.sub] || e.s[0], q = E.q.trim().toLowerCase();
  const mods = s.m.map((m, i) => [m[0], m[1].filter(t => !q || t[0].toLowerCase().includes(q) || m[0].toLowerCase().includes(q)), i]).filter(m => m[1].length);
  return `<section class="blk"><div class="wrap">${head('Syllabus explorer', 'Every module and topic, for every exam.', 'Choose a country, an exam and a subject. This is the same structure the student app uses, read straight from each country\'s syllabus file.')}
  <div class="sel"><select aria-label="Country" data-act="exc">${CCS.map(cc => `<option value="${cc}" ${cc === E.cc ? 'selected' : ''}>${CM[cc].flag} ${esc(CM[cc].name)}</option>`).join('')}</select>
  <select aria-label="Exam" data-act="exe">${v.ex.map((x, i) => `<option value="${i}" ${i === E.ex ? 'selected' : ''}>${esc(x.k)}</option>`).join('')}</select>
  <select aria-label="Subject" data-act="exs">${e.s.map((x, i) => `<option value="${i}" ${i === E.sub ? 'selected' : ''}>${esc(x.n)}</option>`).join('')}</select>
  <input type="search" placeholder="Search topics" value="${esc(E.q)}" data-act="exq" aria-label="Search topics"></div>
  <div class="stat4" style="margin-bottom:1rem"><div><b>${s.m.length}</b><span>modules</span></div><div><b>${s.t}</b><span>topics</span></div><div><b>${nf(s.q)}</b><span>questions</span></div><div><b>${s.mk[0] ? s.mk[0] + ' / ' + s.mk[1] + ' min' : 'n/a'}</b><span>mock exam</span></div></div>
  ${s.p ? `<p class="note" style="margin-bottom:1rem"><b>Paper format.</b> ${esc(s.p)}</p>` : ''}${s.sa ? `<p class="note" style="margin-bottom:1rem">This subject reuses the WASSCE content and says so in the app until exam-specific notes are written.</p>` : ''}
  ${mods.length ? mods.map(m => `<details class="mod" ${q || m[2] === 0 ? 'open' : ''}><summary><span>${m[2] + 1}. ${esc(m[0])}</span><span class="ct">${m[1].length} topics</span></summary><ul>${m[1].map(t => `<li><span>${esc(t[0])}</span>${t[2] ? '<span class="pill live">notes</span>' : ''}<span class="q2">${t[1]} Qs</span></li>`).join('')}</ul></details>`).join('') : '<p class="note">No topic matches that search.</p>'}
  <div class="cta">${appBtn('Practise this in the app')}</div></div></section>`;
}

function pSchools() {
  return `<section class="blk"><div class="wrap">${head('For schools and centres', 'A class, a school or a tutoring centre on one platform.', 'Teachers and administrators get their own tools, and students sign in with a username the school gives them. The database and server layer is built; the dashboards are being built on top of it.')}
  <div class="grid g3">${SCHOOL.map(r => `<div class="card"><h3><span class="ic">${r[0]}</span>${esc(r[1])}</h3><p>${esc(r[2])}</p><ul class="ticks">${r[3].map(x => `<li><span>${esc(x)}</span></li>`).join('')}</ul></div>`).join('')}</div>
  <div style="margin-top:3rem" class="split" ><div>${head('Status', 'What is done and what is next.')}<div class="time">${SCHOOL_STATUS.map(s => `<div><span class="pill ${s[0] === 'Done' ? 'live' : s[0] === 'In build' ? 'back' : 'plan'}">${esc(s[0])}</span><p style="margin-top:.4rem;color:var(--ink2)">${esc(s[1])}</p></div>`).join('')}</div></div>
  <div>${head('Getting a school started', 'Five steps.')}<ol class="steps">${['Request a quote and tell us the exams and number of learners.', 'We create your school and give you a school code.', 'Invite teachers, or let them join with the code.', 'Add students one by one or by bulk import. Each gets a username, so no email is needed.', 'Choose the subjects each class sees and start practising.'].map(x => `<li><span>${x}</span></li>`).join('')}</ol></div></div>
  <div style="margin-top:3rem">${head('More than a chatbot', 'A school needs more than a chatbot.')}
  <div class="grid g2"><div class="card"><h3>A study chatbot</h3><ul class="ticks"><li><span>Answers one question at a time</span></li><li><span>Knows nothing about your class</span></li><li><span>No student accounts or school records</span></li><li><span>No visibility for teachers</span></li></ul></div>
  <div class="card" style="border-color:var(--ink)"><h3>Ace Education for schools</h3><ul class="ticks"><li><span>A full syllabus, notes, quizzes and mocks for every subject</span></li><li><span>School, class and student accounts with strict separation between schools</span></li><li><span>Username sign-in for students</span></li><li><span>Bulk import and staff invitations</span></li></ul></div></div></div>
  <div class="cta">${btnGo('quote', 'Get a school quote', 'primary')}${btnGo('contact', 'Ask a question')}</div></div></section>`;
}

function formHtml(kind) {
  const q = kind === 'quote';
  return `<form class="form" data-form="${kind}" novalidate>
  ${q ? `<div class="row"><label>I am a<select name="type"><option>School</option><option>Tutoring centre</option><option>Organisation or NGO</option><option>Other</option></select></label><label>Number of learners<input name="learners" inputmode="numeric" placeholder="e.g. 250"></label></div>` : ''}
  <div class="row"><label>${q ? 'School or centre name' : 'Your name'}<input name="name" required></label><label>Email<input name="email" type="email" required></label></div>
  <div class="row"><label>Country<select name="country">${CCS.map(cc => `<option value="${cc}">${CM[cc].flag} ${esc(CM[cc].name)}</option>`).join('')}<option value="other">Another country</option></select></label><label>Phone or WhatsApp (optional)<input name="phone"></label></div>
  ${q ? `<label>Exams and grades<input name="exams" placeholder="e.g. WASSCE, SS1 to SS3"></label>` : ''}
  <label>${q ? 'Anything else we should know' : 'Message'}<textarea name="msg"></textarea></label>
  <div><button class="btn primary" type="submit">${q ? 'Request my quote' : 'Send message'}</button></div></form>`;
}
function pQuote() {
  return `<section class="blk"><div class="wrap"><div class="split" style="align-items:start"><div>${head('Get a quote', 'Every school is different, so is the quote.', 'We do not publish a one-size-fits-all price list. Tell us about your school or centre and we will come back with a plan that fits, usually within one business day.')}
  <ul class="ticks"><li><span>The full student app for every learner</span></li><li><span>Teacher, subject-teacher and admin tools as they are released</span></li><li><span>Mixed grades and groups for tutoring centres</span></li><li><span>Onboarding and support</span></li></ul>
  <div class="note" style="margin-top:1.2rem">Pricing is agreed per school or centre, based on learners and rollout. No price is shown here because none has been set yet.</div></div>
  <div class="card" style="gap:1rem"><h3>Request a quote</h3>${S.formDone && S.formDone.kind === 'quote' ? formDone() : formHtml('quote')}</div></div>
  <div style="margin-top:3rem">${head('Questions', 'Pricing and rollout.')}${faqList()}</div></div></section>`;
}
function formDone() {
  const f = S.formDone, mail = SITE_CONFIG.email;
  return `<div class="ok"><b>${f.sent ? 'Sent. Thank you.' : 'Almost done: one more step.'}</b><p style="margin-top:.4rem">${f.sent ? 'We will reply within one business day.' : 'This site is not connected to an inbox yet, so nothing was sent. Copy the request below and send it to us' + (mail ? ` at <b>${esc(mail)}</b>` : ' once a contact address is set') + '.'}</p>
  ${f.sent ? '' : `<div class="quote-box" id="qtext">${esc(f.text)}</div><button class="btn sm" data-act="copy">Copy request</button>`}</div>`;
}

function pGuides() {
  const cats = ['All', ...new Set(GUIDES.map(g => g[1]))], list = GUIDES.filter(g => S.gfilter === 'All' || g[1] === S.gfilter);
  return `<section class="blk"><div class="wrap">${head('Guides', 'Study smarter, in plain language.', 'Short guides on studying, exams and wellbeing that apply in every country we cover.')}
  <div class="tabs">${cats.map(c => `<button class="tab ${S.gfilter === c ? 'on' : ''}" data-act="gfilter" data-v="${esc(c)}">${esc(c)}</button>`).join('')}</div>
  <div class="grid g3">${list.map(g => `<button class="card" data-go="guide" data-arg="${g[0]}"><span class="mono">${esc(g[1])} · ${esc(g[5])} read</span><h3>${esc(g[2])}</h3><p>${esc(g[3])}</p></button>`).join('')}</div></div></section>`;
}
function pGuide(id) {
  const g = GUIDES.find(x => x[0] === id); if (!g) return pGuides();
  return `<section class="blk"><div class="wrap" style="max-width:760px"><div class="crumb"><a data-go="guides">Guides</a><span>/</span><span>${esc(g[1])}</span></div><div class="eyebrow mono">${esc(g[1])} · ${esc(g[5])} read</div><h1 style="font-size:clamp(1.8rem,4.4vw,2.8rem)">${esc(g[2])}</h1><p class="lede">${esc(g[3])}</p>
  <div class="art"><h2>What to do</h2><ol>${g[4].map(x => `<li>${esc(x)}</li>`).join('')}</ol></div>
  <div class="cta">${appBtn('Practise in the app')}${btnGo('guides', 'More guides')}</div></div></section>`;
}

function pAbout() {
  const f = SITE_CONFIG.founder;
  return `<section class="blk"><div class="wrap">${head('About', 'Exam preparation that fits the exam you will actually sit.', 'Students across West Africa, East and Southern Africa, Europe and North America prepare for very different exams. Most study tools treat them as one. We build for each.')}
  <div class="grid g3">${VALUES.map(v => `<div class="card"><h3><span class="ic">${v[0]}</span>${esc(v[1])}</h3><p>${esc(v[2])}</p></div>`).join('')}</div>
  <div style="margin-top:3rem;align-items:start" class="split"><div>${head('How a subject is made', 'From syllabus to student.')}<ol class="steps">${['Take the topic list from the exam body\'s published syllabus and group it into modules.', 'Write the notes: overview, key terms, explanation, formulas, method, worked example, mistakes, real-world link, strategy and recap.', 'Write at least five questions per topic with a wrong-answer explanation for each option that matters.', 'Recompute every number in code, and test for duplicate options, answer positions and leftover content from other countries.', 'Mark everything "needs review" until a subject teacher signs it off.'].map(x => `<li><span>${x}</span></li>`).join('')}</ol></div>
  <div><div class="stat4" style="grid-template-columns:repeat(2,minmax(0,1fr))"><div><b>${CCS.length}</b><span>countries</span></div><div><b>${TOT.exams}</b><span>exams</span></div><div><b>${nf(TOT.q)}</b><span>questions</span></div><div><b>${nf(TOT.t)}</b><span>topic notes</span></div></div></div></div>
  <div style="margin-top:3rem">${head('Roadmap', 'Where we are going.')}<div class="grid g3">${ROADMAP.map(r => `<div class="card"><h3>${esc(r[0])}</h3><ul class="ticks">${r.slice(1).map(x => `<li><span>${esc(x)}</span></li>`).join('')}</ul></div>`).join('')}</div></div>
  ${f ? `<div style="margin-top:3rem" class="card"><h3>${esc(f.name)}</h3><span class="mono">${esc(f.role)}</span><p>${esc(f.bio)}</p></div>` : ''}
  <div class="cta">${appBtn()}${btnGo('contact', 'Talk to us')}</div></div></section>`;
}

function pContact() {
  const c = SITE_CONFIG, ch = [];
  if (c.email) ch.push(['✉️', 'Email', c.email, `<a class="btn sm" href="mailto:${esc(c.email)}">Send email</a>`]);
  if (c.whatsapp) ch.push(['💬', 'WhatsApp', '+' + c.whatsapp, `<a class="btn sm" href="https://wa.me/${esc(c.whatsapp)}" target="_blank" rel="noopener">Chat now</a>`]);
  if (c.telegram) ch.push(['📣', 'Telegram', 'Community group', `<a class="btn sm" href="${esc(c.telegram)}" target="_blank" rel="noopener">Join</a>`]);
  return `<section class="blk"><div class="wrap"><div class="split" style="align-items:start"><div>${head('Contact', 'Get in touch.', 'Questions about the app, a school plan, a subject you need or a mistake you found? We reply within one business day.')}
  ${ch.length ? `<div class="grid">${ch.map(x => `<div class="card"><h3><span class="ic">${x[0]}</span>${x[1]}</h3><p>${esc(x[2])}</p><div>${x[3]}</div></div>`).join('')}</div>` : ''}
  <div class="card" style="margin-top:1rem"><h3><span class="ic">🧐</span>Found a mistake?</h3><p>Tell us the country, exam, subject, topic and what is wrong. Every report goes to the content review list.</p></div>
  <div class="card" style="margin-top:1rem"><h3><span class="ic">🌍</span>Need your country?</h3><p>Tell us the exam and the subjects. A new country is a new syllabus file, so it can move fast.</p></div></div>
  <div class="card" style="gap:1rem"><h3>Send a message</h3>${S.formDone && S.formDone.kind === 'contact' ? formDone() : formHtml('contact')}</div></div>
  <div style="margin-top:3rem">${head('Common questions', 'Quick answers.')}${faqList()}</div></div></section>`;
}

function pPrivacy() {
  return `<section class="blk"><div class="wrap" style="max-width:860px">${head('Privacy', 'How we handle student data.', 'Plain-language summary. This is a working draft and a lawyer in each country should review it before launch.')}
  <div class="art"><h2>What we collect</h2><ol><li>Account details a school or student gives us: a username, a display name, class and school.</li><li>Study activity: which topics were opened, quiz answers and scores, streaks and XP.</li><li>Messages a student sends to Ask Ace, so the tutor can answer in context.</li></ol>
  <h2>What we do not do</h2><ol><li>We do not sell personal data.</li><li>We do not show advertising to students.</li><li>We do not need a student's email address to sign in when the school uses usernames.</li></ol>
  <h2>Control and deletion</h2><ol><li>A student, parent or school can ask for data to be deleted. The app has a "delete my data" option.</li><li>Schools only see their own students. The database separates schools by design.</li></ol>
  <h2>The law where you live</h2></div>
  <div class="tw"><table class="tbl"><thead><tr><th>Country</th><th>Data-protection law we design for</th></tr></thead><tbody>${CCS.map(cc => `<tr><td>${cMeta(cc)}</td><td>${esc(CM[cc].law)}</td></tr>`).join('')}</tbody></table></div>
  <p class="mono" style="margin-top:1rem">Where a country has no single named law above, we follow the same minimal-collection rules and apply the stricter local rule once confirmed.</p></div></section>`;
}

function pTerms() {
  return `<section class="blk"><div class="wrap" style="max-width:860px">${head('Terms', 'Terms of use.', 'Plain-language summary. This is a working draft and a lawyer should review it before you rely on it.')}
  <div class="art"><h2>Using Ace Education</h2><ol><li>Ace Education is a study aid. It does not replace your teacher, your school or the official syllabus and timetable of your exam body.</li><li>Look after your password and do not share your account. Tell us if you think someone else has used it.</li><li>Be kind in study groups and messages. We may remove content and accounts that break this rule.</li></ol>
  <h2>Accuracy</h2><ol><li>Notes and questions are written for the app and checked, but some items are still marked "needs review". Always confirm important facts against your syllabus and teacher.</li><li>Answers from Ace, the AI study buddy, can be wrong. Check them, especially for marks and exam rules.</li></ol>
  <h2>Exam bodies</h2><ol><li>WAEC, NECO, JAMB, KNEC, ECZ, UNEB, NECTA, Umalusi, AQA, Edexcel, OCR, WJEC and other exam bodies are named only to say which exam a subject follows. Ace Education is not affiliated with them.</li></ol>
  <h2>Schools and accounts</h2><ol><li>Schools are responsible for their staff and student accounts. A school or student can ask us to delete an account at any time.</li><li>We may change or stop parts of the service. We will try to give notice of big changes.</li></ol></div>
  <p class="mono" style="margin-top:1rem">Questions about these terms? Use the <a data-go="contact">contact page</a>.</p></div></section>`;
}

/* ---------- shell ---------- */
function header() {
  return `<header><div class="bar"><button class="brand" data-go="home" aria-label="Ace Education home">${PENCIL}Ace Education</button>
  <nav class="main" id="nav">${NAV.map(n => `<a data-go="${n[0]}" class="${S.page === n[0] || (S.page === 'country' && n[0] === 'countries') || (S.page === 'guide' && n[0] === 'guides') ? 'on' : ''}">${n[1]}</a>`).join('')}<a data-go="quote" class="${S.page === 'quote' ? 'on' : ''}">Get a quote</a></nav>
  <a class="btn sm hide-s" href="${esc(SITE_CONFIG.loginUrl)}" target="_blank" rel="noopener">Sign in</a><a class="btn sm primary hide-s" href="${esc(SITE_CONFIG.appUrl)}" target="_blank" rel="noopener">Student app</a>
  <button class="icon" id="theme" aria-label="Toggle theme">🌓</button><button class="icon menu" id="menu" aria-label="Menu">☰</button></div></header>`;
}
function footer() {
  return `<footer><div class="fgrid"><div><button class="brand" data-go="home" style="margin-bottom:.7rem">${PENCIL}Ace Education</button><p style="color:var(--ink2);font-size:.9rem;max-width:34ch">Exam preparation for secondary schools in ${CCS.length} countries, built around each country's own exams.</p></div>
  <div><h4>Product</h4><a data-go="features">Features</a><a data-go="syllabus">Syllabus explorer</a><a data-go="schools">For schools</a><a href="${esc(SITE_CONFIG.appUrl)}" target="_blank" rel="noopener">Student app</a><a href="${esc(SITE_CONFIG.loginUrl)}" target="_blank" rel="noopener">Sign in</a></div>
  <div><h4>Countries</h4>${CCS.map(cc => `<a data-go="country" data-arg="${cc}">${cMeta(cc)}</a>`).join('')}</div>
  <div><h4>Company</h4><a data-go="about">About</a><a data-go="guides">Guides</a><a data-go="quote">Get a quote</a><a data-go="contact">Contact</a><a data-go="privacy">Privacy</a><a data-go="terms">Terms</a></div></div>
  <div class="fine">© Ace Education. Content carries a "needs review" label until a subject teacher signs it off. Exam names belong to their exam bodies; Ace Education is not affiliated with them.</div></footer>`;
}
function render() {
  const P = S.page;
  const body = P === 'home' ? pHome() : P === 'countries' ? pCountries() : P === 'country' ? pCountry(S.arg) : P === 'features' ? pFeatures() : P === 'syllabus' ? pSyllabus() : P === 'schools' ? pSchools() : P === 'quote' ? pQuote() : P === 'guides' ? pGuides() : P === 'guide' ? pGuide(S.arg) : P === 'about' ? pAbout() : P === 'contact' ? pContact() : P === 'privacy' ? pPrivacy() : P === 'terms' ? pTerms() : pHome();
  const keep = document.activeElement && document.activeElement.dataset && document.activeElement.dataset.act === 'exq';
  $('#root').innerHTML = header() + `<main class="wrap">${body}</main>` + footer() + `<div class="mbar"><a class="btn primary" href="${esc(SITE_CONFIG.appUrl)}" target="_blank" rel="noopener">Open the app</a><a class="btn" href="${esc(SITE_CONFIG.loginUrl)}" target="_blank" rel="noopener">Sign in</a></div>`;
  anchorize();
  S.anim = false;
  if (keep) { const i = $('input[data-act="exq"]'); if (i) { i.focus(); i.setSelectionRange(i.value.length, i.value.length); } }
}

/* Turn every in-site button into a real link so search engines and AI crawlers can follow it. */
function anchorize() {
  document.querySelectorAll('[data-go]').forEach(el => {
    const href = pathFor(el.dataset.go, el.dataset.arg || null);
    if (el.tagName === 'A') { el.setAttribute('href', href); return; }
    const a = document.createElement('a');
    for (const at of el.attributes) a.setAttribute(at.name, at.value);
    a.setAttribute('href', href); a.innerHTML = el.innerHTML;
    el.replaceWith(a);
  });
}

/* ---------- events ---------- */
document.addEventListener('click', e => {
  const g = e.target.closest('[data-go]');
  if (g) { if (e.metaKey || e.ctrlKey || e.shiftKey || e.button) return; e.preventDefault(); go(g.dataset.go, g.dataset.arg); return; }
  const a = e.target.closest('[data-act]'); if (a) {
    const k = a.dataset.act;
    if (k === 'hero') { S.hero = a.dataset.cc; S.picked = null; S.anim = true; render(); }
    else if (k === 'snd') { S.snd = !S.snd; render(); }
    else if (k === 'check') { const P = S.picked; if (!P || P.key !== a.dataset.key) return; P.done = true; const smp = D[S.page === 'country' ? S.arg : S.hero].sample, ok = P.i === smp.a; render(); if (ok) { SFX.ok(); const g = document.querySelector('.opt.good'); if (g) { const r = g.getBoundingClientRect(); confetti(r.left + r.width / 2, r.top + r.height / 2); } } else SFX.no(); }
    else if (k === 'pick') { if (S.picked && S.picked.done) return; S.picked = {key: a.dataset.key, i: +a.dataset.i}; SFX.pick(); render(); }
    else if (k === 'ffilter') { S.ffilter = a.dataset.v; render(); }
    else if (k === 'gfilter') { S.gfilter = a.dataset.v; render(); }
    else if (k === 'explore') { S.ex = {cc: a.dataset.cc, ex: +a.dataset.ei, sub: +a.dataset.si, q: ''}; go('syllabus'); }
    else if (k === 'copy') { const t = $('#qtext').textContent; try { navigator.clipboard.writeText(t).then(() => { a.textContent = 'Copied'; }, () => sel()); } catch (x) { sel(); } function sel() { const r = document.createRange(); r.selectNodeContents($('#qtext')); const s = getSelection(); s.removeAllRanges(); s.addRange(r); a.textContent = 'Press copy on your device'; } }
    return;
  }
  if (e.target.closest('#theme')) { const r = document.documentElement, d = r.dataset.theme === 'dark' || (!r.dataset.theme && matchMedia('(prefers-color-scheme:dark)').matches); r.dataset.theme = d ? 'light' : 'dark'; return; }
  if (e.target.closest('#menu')) { $('#nav').classList.toggle('open'); return; }
});
document.addEventListener('change', e => {
  const k = e.target.dataset && e.target.dataset.act; if (!k) return;
  if (k === 'exc') { S.ex = {cc: e.target.value, ex: 0, sub: 0, q: S.ex.q}; render(); }
  else if (k === 'exe') { S.ex.ex = +e.target.value; S.ex.sub = 0; render(); }
  else if (k === 'exs') { S.ex.sub = +e.target.value; render(); }
});
document.addEventListener('input', e => { if (e.target.dataset && e.target.dataset.act === 'exq') { S.ex.q = e.target.value; render(); } });
document.addEventListener('submit', e => {
  const f = e.target.closest('[data-form]'); if (!f) return; e.preventDefault();
  const d = Object.fromEntries(new FormData(f).entries()), kind = f.dataset.form;
  if (!d.name || !/^\S+@\S+\.\S+$/.test(d.email || '')) { alert_(f, 'Please add your name and a valid email.'); return; }
  const text = (kind === 'quote' ? 'QUOTE REQUEST\n' : 'MESSAGE\n') + Object.entries(d).filter(x => x[1]).map(x => x[0] + ': ' + x[1]).join('\n');
  const done = sent => { S.formDone = {kind, sent, text}; render(); };
  if (SITE_CONFIG.formEndpoint) fetch(SITE_CONFIG.formEndpoint, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({kind, ...d})}).then(r => done(r.ok), () => done(false));
  else done(false);
});
function alert_(f, m) { let n = f.querySelector('.err'); if (!n) { n = document.createElement('p'); n.className = 'note err'; f.prepend(n); } n.textContent = m; }
fromLocation(); render(); try { document.title = routeMeta(S.page, S.arg).title; } catch (e) {}
