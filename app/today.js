/* Ace "Today" hub: daily-use features for secondary and university students.
   Loaded after the main app script. Needs the cloud (AceSync) for AI notes, revision and shared plans;
   the calculators, citation builder, focus timer and roadmap work offline and as a guest.
   Pure calculators live in AceX.calc so they can be unit-tested (see tools/test_calc.js). */
(function () {
  'use strict';
  /* ---------- pure calculators ---------- */
  const r2 = n => Math.round((n + Number.EPSILON) * 100) / 100;
  const SCALES = {
    ng5: { name: 'Nigeria / 5.0', max: 5, pts: { A: 5, B: 4, C: 3, D: 2, E: 1, F: 0 } },
    us4: { name: '4.0 scale', max: 4, pts: { A: 4, B: 3, C: 2, D: 1, F: 0 } }
  };
  const calc = {
    gpa(rows, scale) {
      const s = SCALES[scale]; let cr = 0, q = 0;
      rows.forEach(r => { const c = +r.credits, p = s.pts[String(r.grade || '').toUpperCase()]; if (c > 0 && p != null) { cr += c; q += c * p; } });
      return cr ? { gpa: r2(q / cr), credits: cr } : { gpa: null, credits: 0 };
    },
    nigClass(g) { return g == null ? '' : g >= 4.5 ? 'First Class' : g >= 3.5 ? 'Second Class Upper' : g >= 2.4 ? 'Second Class Lower' : g >= 1.5 ? 'Third Class' : g >= 1 ? 'Pass' : 'Fail'; },
    ukAvg(rows) { let cr = 0, s = 0; rows.forEach(r => { const c = +r.credits, m = +r.mark; if (c > 0 && m >= 0 && m <= 100 && r.mark !== '') { cr += c; s += c * m; } }); return cr ? { avg: r2(s / cr), credits: cr } : { avg: null, credits: 0 }; },
    ukClass(a) { return a == null ? '' : a >= 70 ? 'First' : a >= 60 ? 'Upper second (2:1)' : a >= 50 ? 'Lower second (2:2)' : a >= 40 ? 'Third' : 'Fail'; },
    // grade point you must average over the remaining credits to finish on `target`
    need(cur, doneCr, target, remCr, max) {
      if (!(remCr > 0)) return { need: null, possible: false };
      const n = (target * (doneCr + remCr) - cur * doneCr) / remCr;
      return { need: r2(Math.max(n, 0)), possible: n <= max + 1e-9 };
    },
    cite(f, style) {
      const au = (f.author || '').trim(), yr = (f.year || 'n.d.').trim(), ti = (f.title || '').trim();
      const apa = style === 'apa', end = s => /[.?!]$/.test(s) ? s : s + '.', it = s => /[.?!]$/.test(s) ? '*' + s.slice(0, -1) + '*' + s.slice(-1) : '*' + s + '*.';
      const head = au ? (apa ? end(au) + ' (' + yr + '). ' : au + ' (' + yr + ') ') : '';
      const pub = (f.publisher || '').trim(), url = (f.url || '').trim(), jr = (f.journal || '').trim();
      const vol = (f.volume || '').trim(), iss = (f.issue || '').trim(), pg = (f.pages || '').trim();
      if (f.type === 'article') {
        const loc = (vol ? '*' + vol + '*' : '') + (iss ? '(' + iss + ')' : '') + (pg ? ', ' + pg : '');
        return head + (apa ? end(ti) : '‘' + ti + '’,') + ' *' + jr + '*' + (loc ? (apa ? ', ' : ', ') + loc : '') + '.' + (url ? ' ' + url : '');
      }
      if (f.type === 'web') return head + it(ti) + ' ' + (pub ? end(pub) : '') + (url ? ' ' + (apa ? url : 'Available at: ' + url) : '');
      return head + it(ti) + (pub ? ' ' + end(pub) : '');
    }
  };

  /* ---------- state ---------- */
  const X = window.AceX = { calc, tt: { subject: '', text: '', busy: false, err: '', res: null, ans: {}, saved: false }, notes: null, due: null, plan: null,
    members: null, invite: null, err: '', gp: { scale: 'ng5', rows: [{ course: '', credits: '3', grade: 'A' }], mode: 'gpa', cur: '', done: '', target: '', rem: '' },
    ci: { style: 'apa', type: 'book', author: '', year: '', title: '', publisher: '', url: '', journal: '', volume: '', issue: '', pages: '' }, ft: { mode: 'focus', end: 0, left: 1500 }, loaded: '', goal: { course: '', uni: '', result: '', year: '' } };
  const C_ = () => C[S.c], es = () => UIL() === 'es', L = (a, b) => TX(a, b);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));
  const lvl = () => P.lvl || 'secondary';
  const back = (to, label) => `<div class="bk"><button class="bb" data-a="tab" data-v="${to || 'today'}">‹ ${label || L('Back', 'Atrás')}</button></div>`;
  const sync = () => window.AceSync;
  const signedIn = () => !!(sync() && sync().signedIn && sync().signedIn());
  const needSignIn = () => `<div class="card"><b>${L('Sign in to use this', 'Inicia sesión para usar esto')}</b><p class="note">${L('This part is saved to your account. Open the sign-in page, then come back here.', 'Esta parte se guarda en tu cuenta. Abre la página de acceso y vuelve aquí.')}</p><a class="btn" style="display:inline-block;text-decoration:none" href="${LOGIN()}">${L('Sign in', 'Entrar')}</a></div>`;
  const NAMES = { NG: 'Nigeria', GH: 'Ghana', SL: 'Sierra Leone', GM: 'The Gambia', KE: 'Kenya', ZM: 'Zambia', GB: 'United Kingdom', CA: 'Canada', ES: 'Spain', IE: 'Ireland', ZA: 'South Africa', UG: 'Uganda', TZ: 'Tanzania', LR: 'Liberia', MT: 'Malta', ZW: 'Zimbabwe', BW: 'Botswana', FR: 'France' };
  const hc = () => (typeof HOMECC === 'function' ? HOMECC() : S.c), cname = () => NAMES[hc()] || hc();
  const ex = () => C_().x[S.x % C_().x.length];
  const fail = e => { X.err = (e && (e.msg || e.message)) || L('Something went wrong. Try again.', 'Algo salió mal. Inténtalo de nuevo.'); };

  X.h = { L, esc, back, needSignIn, signedIn, sync, fail, cname, ex, dayKey: () => new Date().toISOString().slice(0, 10) };

  /* ---------- roadmap data ---------- */
  const ADM = {
    NG: 'JAMB UTME first, then the university’s own Post-UTME screening.',
    GH: 'Apply to your chosen university or its admissions portal with your WASSCE results.',
    SL: 'Apply to your chosen university with your WASSCE results; each institution sets its own deadlines.',
    GM: 'Apply to your chosen institution with your WASSCE results; each sets its own deadlines.',
    KE: 'KCSE results are used for placement through KUCCPS; self-sponsored students can also apply to universities directly.',
    ZM: 'Apply to your chosen university with your school certificate results; each sets its own deadlines.',
    GB: 'Apply through UCAS. Oxford, Cambridge, medicine, dentistry and veterinary have an earlier deadline than other courses.',
    CA: 'Apply through your province’s system (for example OUAC in Ontario) or directly to the university.',
    ES: 'Take the university access exam (PAU/EBAU, set by your region), then pre-enrol through your region’s system.',
    IE: 'Apply through the CAO using your Leaving Certificate results.',
    ZA: 'Apply directly to each university (many close in mid-year); your NSC results decide your Admission Point Score (APS), and NSFAS funds eligible students.',
    UG: "Apply to public universities through each university's own portal (Makerere and others) with your UACE results; government sponsorship is competitive, and private sponsorship is also available.",
    TZ: 'Apply to universities through the Central Admission System (CAS) run by TCU, using your ACSEE results.',
    LR: 'Apply to each university directly. Most ask for your WASSCE result and set their own entrance exam; the University of Liberia entrance exam tests English and Mathematics.',
    MT: 'Most degree courses at the University of Malta need the Matriculation Certificate (taken after two years of sixth form) plus SEC passes in English, Maltese and Mathematics or the subjects your course names. MCAST courses accept SEC results directly. Check the entry requirements of your course.',
    ZW: 'Apply directly to each university (for example UZ, NUST and MSU) through its own online portal. Your A Level points decide entry, and most degrees also need five O Level passes at grade C or better, including English Language and usually Mathematics.',
    BW: 'Apply directly to each institution (for example the University of Botswana, BIUST or BAC) after your BGCSE results. Entry depends on points from six BGCSE subjects, and government sponsorship is handled by the Department of Tertiary Education Financing (DTEF).',
    FR: 'Après le bac, tu formules tes vœux sur Parcoursup (inscription de janvier à mars, réponses à partir de juin). Chaque formation examine ton dossier : notes de Première et de Terminale, résultats des épreuves anticipées, projet de formation motivé. Vérifie le calendrier sur parcoursup.gouv.fr.'
  };
  function stages() {
    const c = C_(), exams = c.x.join(', ');
    return [
      { k: 'jun', t: L('Lower secondary', 'Secundaria inicial'), w: L('Foundation years', 'Años de base'),
        a: [L('Build strong habits in Maths and English: every later subject depends on them.', 'Construye buenos hábitos en Matemáticas e Inglés.'), L('Try every subject before choosing.', 'Prueba todas las asignaturas antes de elegir.'), L('Use the Daily Challenge to keep a streak.', 'Usa el reto diario para mantener la racha.')] },
      { k: 'sen', t: L('Senior secondary', 'Secundaria superior'), w: L('Choosing and preparing', 'Elegir y prepararse'),
        a: [L('Pick subjects that fit the course you want. Check the entry requirements for that course.', 'Elige asignaturas que encajen con tu carrera y revisa los requisitos.'), L('Log what your teacher teaches each day in Today, then revise it on schedule.', 'Anota cada día lo que enseña tu profesor en Hoy y repásalo.'), L('Take a mock exam every term.', 'Haz un simulacro cada trimestre.')] },
      { k: 'ex', t: L('Final exams', 'Exámenes finales'), w: exams,
        a: [L('Work through every topic in your exam with the question bank.', 'Trabaja cada tema con el banco de preguntas.'), L('Do timed mock exams and review every wrong answer.', 'Haz simulacros cronometrados y revisa cada fallo.'), L('Check the exam body’s official timetable and rules.', 'Consulta el calendario oficial del examen.')] },
      { k: 'adm', t: L('Apply to university', 'Acceso a la universidad'), w: L('After your results', 'Tras tus resultados'),
        a: [ADM[hc()] || '', L('Dates and rules change every year. Always confirm on the official site.', 'Las fechas cambian cada año. Confírmalas en el sitio oficial.'), L('Look for scholarships early and note their deadlines.', 'Busca becas pronto y anota sus plazos.')] },
      { k: 'u1', t: L('University: first year', 'Universidad: primer año'), w: L('Settle in', 'Adaptarse'),
        a: [L('Build a weekly timetable and use the focus timer.', 'Crea un horario semanal y usa el temporizador.'), L('Turn lecture notes into revision cards in Today.', 'Convierte tus apuntes en tarjetas en Hoy.'), L('Learn referencing early so you never lose marks for it.', 'Aprende a citar pronto.')] },
      { k: 'uf', t: L('University: later years', 'Universidad: años finales'), w: L('Specialise', 'Especializarse'),
        a: [L('Track your GPA and see what you need to reach your target.', 'Controla tu media y lo que necesitas para tu objetivo.'), L('Plan your project or dissertation early.', 'Planifica tu proyecto final pronto.'), L('Look for internships and placements.', 'Busca prácticas.')] },
      { k: 'grad', t: L('Graduation', 'Graduación'), w: L('Finish strong', 'Cerrar con fuerza'),
        a: [L('Confirm your final classification and requirements with your department.', 'Confirma tu calificación final con tu departamento.'), L('Update your CV and ask lecturers for references.', 'Actualiza tu CV y pide referencias.')] },
      { k: 'car', t: L('Career or further study', 'Carrera o posgrado'), w: L('Next step', 'Siguiente paso'),
        a: [L('Prepare your CV, cover letter and interview answers.', 'Prepara tu CV, carta y entrevistas.'), L('Explore postgraduate options and funding.', 'Explora posgrados y financiación.')] }
    ];
  }
  function topicStats() {
    let tot = 0, done = 0;
    Object.keys(TC || {}).forEach(s => Object.keys(TC[s] || {}).forEach(t => { tot++; if (P.done[s + '|' + t]) done++; }));
    return { tot, done };
  }

  /* ---------- views ---------- */
  function hub() {
    const c = C_(), lv = lvl(), st = topicStats(), due = X.due ? X.due.length : null;
    const chips = ['secondary', 'university'].map(k => `<button class="xchip ${lv === k ? 'on' : ''}" data-x="lvl" data-v="${k}">${k === 'secondary' ? L('Secondary school', 'Secundaria') : L('University', 'Universidad')}</button>`).join('');
    const tool = (e, t, s, tab) => `<button class="tc" data-a="tab" data-v="${tab}"><span class="e">${e}</span><b>${t}</b><small>${s}</small></button>`;
    return `<div class="pad"><h2 style="margin:0 0 4px;font-size:20px">${L('Today', 'Hoy')}</h2><p class="note" style="margin:0 0 10px">${L('Everything you need for today, not only for exam week.', 'Todo lo que necesitas hoy, no solo en época de exámenes.')}</p>
<div class="xchips">${chips}</div>
<button class="ban" data-a="tab" data-v="tt"><span class="ic">✍️</span><span><b>${L('What did my teacher teach today?', '¿Qué enseñó hoy mi profesor?')}</b><span>${L('Type it in. Ace makes notes and practice questions.', 'Escíbelo. Ace crea apuntes y preguntas.')}</span></span><em>›</em></button>
<button class="ban" data-a="tab" data-v="rev"><span class="ic">🔁</span><span><b>${L('Revision due', 'Repaso pendiente')}${due != null ? ': ' + due : ''}</b><span>${L('Short reviews at 1, 3, 7, 21 and 45 days make it stick.', 'Repasos cortos a 1, 3, 7, 21 y 45 días.')}</span></span><em>›</em></button>
<button class="ban" data-a="tab" data-v="road"><span class="ic">🗺️</span><span><b>${L('My road map', 'Mi hoja de ruta')}</b><span>${L('From secondary school to graduation', 'De la secundaria a la graduación')}${st.tot ? ' • ' + st.done + '/' + st.tot + ' ' + L('topics studied', 'temas estudiados') : ''}</span></span><em>›</em></button>
<div class="sh">${L('Study tools', 'Herramientas')}</div><div class="tg2">
${tool('⏱️', L('Focus timer', 'Temporizador'), L('25 min focus, 5 min break', '25 min enfoque, 5 descanso'), 'focus')}
${tool('🧮', L('GPA calculator', 'Calculadora de media'), L('Grades, class and target', 'Notas, clasificación, objetivo'), 'gpa')}
${tool('📚', L('Citation builder', 'Generador de citas'), 'APA / Harvard', 'cite')}
${tool('👪', L('Share my plan', 'Compartir plan'), L('Up to 4 people on one plan', 'Hasta 4 personas en un plan'), 'share')}
${tool('🏠', L('Family view', 'Vista familiar'), L('A link for parents to see progress', 'Enlace para que la familia vea tu progreso'), 'family')}
${tool('📝', L('Lecture notes', 'Apuntes'), L('Paste notes, get a study pack', 'Pega apuntes, recibe un paquete'), 'notes')}</div>
<div class="sh">${L('My school', 'Mi colegio')}</div><div class="tg2">
${tool('📣', L('From my teachers', 'De mis profesores'), L('Notices and messages', 'Avisos y mensajes'), 'inbox')}
${tool('📋', L('Class tasks', 'Tareas'), L('Set by your teacher', 'Puestas por tu profesor'), 'tasks')}
${tool('⚡', L('Live quiz', 'Quiz en vivo'), L('Join with a code', 'Entra con un código'), 'livej')}</div>
<div class="sh">${L('Learn and explore', 'Aprende y explora')}</div><div class="tg2">
${tool('🎓', L('Courses', 'Cursos'), L('Short courses with certificates', 'Cursos con certificado'), 'learn')}
${tool('🏛️', L('Universities', 'Universidades'), L('Courses and how to apply', 'Carreras y cómo acceder'), 'unis')}
${tool('💬', L('Study groups', 'Grupos de estudio'), L('Moderated, for your class or campus', 'Moderados, de tu clase o campus'), 'groups')}
${tool('⭐', L('Plans', 'Planes'), L('Upgrade, share, or use a code', 'Mejora, comparte o usa un código'), 'plans')}</div>
<button class="xlink" style="margin-top:12px" data-x="pushon">🔔 ${L('Turn on daily revision reminders', 'Activar recordatorios diarios')}</button>
${lv === 'university' ? `<p class="note">${L('University mode: set your institution and course on the road map page.', 'Modo universidad: indica tu institución y carrera en la hoja de ruta.')}</p>` : ''}</div>`;
  }

  function ttView() {
    const c = C_(), f = X.tt, subs = c.s || [];
    if (!signedIn()) return `<div class="pad">${back()}<h2>${L('What did my teacher teach today?', '¿Qué enseñó hoy mi profesor?')}</h2>${needSignIn()}</div>`;
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('What did my teacher teach today?', '¿Qué enseñó hoy mi profesor?')}</h2>`;
    if (!f.res) {
      h += `<label class="xl">${L('Subject', 'Asignatura')}<select class="xin" data-x-in="subject"><option value="">${L('Choose…', 'Elige…')}</option>${subs.map(s => `<option ${f.subject === s ? 'selected' : ''}>${esc(s)}</option>`).join('')}</select></label>
<label class="xl">${L('What was taught?', '¿Qué se enseñó?')}<textarea class="xin" rows="5" maxlength="2000" data-x-in="text" placeholder="${L('e.g. Mr Bello taught simultaneous equations using elimination. We did two examples.', 'p. ej. Hoy vimos sistemas de ecuaciones por reducción.')}">${esc(f.text)}</textarea></label>
<button class="nx" data-x="ttgo" ${f.busy ? 'disabled' : ''}>${f.busy ? L('Ace is working…', 'Ace está trabajando…') : L('Make my study pack', 'Crear mi paquete de estudio')}</button>
${f.err ? `<p class="note" style="color:var(--red)">${esc(f.err)}</p>` : ''}
<p class="note">${L('Ace only knows what you type. Check the notes against your teacher’s explanation and your textbook.', 'Ace solo sabe lo que escribes. Compara con tu profesor y tu libro.')}</p>`;
      h += `<div class="sh">${L('Recent notes', 'Notas recientes')}</div>` + (X.notes == null ? `<p class="note">…</p>` : X.notes.length ? `<div class="lst">${X.notes.map(n => `<button class="li" data-x="opennote" data-v="${n.id}"><span class="m"><b>${esc(n.topic || n.subject)}</b><small>${esc(n.subject)} • ${esc(n.taught_on)}</small></span><span class="v">›</span></button>`).join('')}</div>` : `<p class="note">${L('No notes yet.', 'Aún no hay notas.')}</p>`);
    } else {
      const r = f.res;
      h += `<div class="card"><b>${esc(r.topic)}</b><p style="margin:6px 0 0;font-size:14px;line-height:1.5">${esc(r.summary)}</p></div>
${r.needs_detail ? `<p class="note">💡 ${esc(r.needs_detail)}</p>` : ''}
${(r.key_terms || []).length ? `<div class="sh">${L('Key terms', 'Términos clave')}</div><div class="lst">${r.key_terms.map(t => `<div class="li" style="display:block"><b>${esc(t.term)}</b><br><small>${esc(t.meaning)}</small></div>`).join('')}</div>` : ''}
${r.worked_example ? `<div class="sh">${L('Worked example', 'Ejemplo resuelto')}</div><div class="card" style="white-space:pre-wrap;font-size:14px">${esc(r.worked_example)}</div>` : ''}
${(r.questions || []).length ? `<div class="sh">${L('Practice', 'Práctica')}</div>${r.questions.map((q, qi) => { const a = f.ans[qi]; return `<div class="card" style="margin-bottom:10px"><b>${qi + 1}. ${esc(q.q)}</b>${q.options.map((o, oi) => `<button class="li xopt ${a != null && oi === q.answer ? 'ok' : a === oi ? 'bad' : ''}" data-x="tans" data-v="${qi}:${oi}" ${a != null ? 'disabled' : ''}>${'ABCD'[oi]}. ${esc(o)}</button>`).join('')}${a != null ? `<p class="note">${a === q.answer ? '✅ ' : '❌ '}${esc(q.why)}</p>` : ''}</div>`; }).join('')}` : ''}
<button class="nx" data-x="addrev" ${f.saved ? 'disabled' : ''}>${f.saved ? L('Added to revision', 'Añadido al repaso') : L('Add to my revision schedule', 'Añadir a mi repaso')}</button>
<button class="nx" style="background:var(--tint);color:var(--text);margin-top:8px" data-x="ttnew">${L('New note', 'Nueva nota')}</button>
${f.err ? `<p class="note" style="color:var(--red)">${esc(f.err)}</p>` : ''}`;
    }
    return h + '</div>';
  }

  function revView() {
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('Revision', 'Repaso')}</h2>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (X.due == null) return h + '<p class="note">…</p></div>';
    if (!X.due.length) return h + `<div class="emp"><span class="e">🎉</span><b>${L('Nothing due today', 'Nada pendiente hoy')}</b>${L('Add what you learn in class and Ace will schedule reviews.', 'Añade lo que aprendes y Ace programará repasos.')}</div></div>`;
    const it = X.due[0];
    return h + `<p class="note">${X.due.length} ${L('due', 'pendientes')}</p><div class="card"><small>${esc(it.subject)}</small><h3 style="margin:4px 0 8px">${esc(it.topic)}</h3><p class="note">${L('Try to explain this topic from memory, or solve one example. Then tell Ace how it went.', 'Intenta explicar el tema de memoria o resolver un ejemplo. Luego dinos qué tal.')}</p></div>
<button class="nx" data-x="revok" data-v="${it.id}">✅ ${L('I remembered it', 'Lo recordé')}</button>
<button class="nx" style="background:var(--tint);color:var(--text);margin-top:8px" data-x="revno" data-v="${it.id}">🔁 ${L('Not yet. Show me tomorrow', 'Aún no. Mañana')}</button>${X.err ? `<p class="note" style="color:var(--red)">${esc(X.err)}</p>` : ''}</div>`;
  }

  function roadView() {
    const st = stages(), lv = lvl(), cur = P.stage != null ? P.stage : (lv === 'university' ? 4 : 1), ts = topicStats(), g = X.goal;
    const pct = Math.round((cur + 1) / st.length * 100);
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 4px">${L('My road map', 'Mi hoja de ruta')}</h2><p class="note" style="margin:0 0 8px">${esc(cname())} • ${L('secondary school to graduation', 'de la secundaria a la graduación')}</p>
<div style="height:8px;background:var(--border);border-radius:6px"><i style="display:block;height:8px;border-radius:6px;width:${pct}%;background:var(--primary)"></i></div>
${ts.tot ? `<p class="note">${L('Readiness for', 'Preparación para')} ${esc(ex())}: ${ts.done} / ${ts.tot} ${L('topics studied', 'temas estudiados')} (${Math.round(ts.done / ts.tot * 100)}%)</p>` : ''}`;
    h += st.map((s, i) => `<div class="card" style="margin:10px 0;${i === cur ? 'border-color:var(--primary);background:var(--tint)' : ''}"><div style="display:flex;gap:8px;align-items:center"><b style="flex:1">${i + 1}. ${esc(s.t)}</b>${i === cur ? `<span class="xtag">${L('You are here', 'Estás aquí')}</span>` : `<button class="xlink" data-x="stage" data-v="${i}">${L('I’m here', 'Estoy aquí')}</button>`}</div><small>${esc(s.w)}</small>${i === cur || i === cur + 1 ? `<ul class="xul">${s.a.filter(Boolean).map(a => `<li>${esc(a)}</li>`).join('')}</ul>` : ''}</div>`).join('');
    h += `<div class="sh">${L('My goal', 'Mi objetivo')}</div><div class="card">
<label class="xl">${L('Course I want to study', 'Carrera que quiero estudiar')}<input class="xin" data-x-in="goal.course" value="${esc(g.course)}" maxlength="120"></label>
<label class="xl">${L('University', 'Universidad')}<input class="xin" data-x-in="goal.uni" value="${esc(g.uni)}" maxlength="120"></label>
<label class="xl">${L('Result I need (from the university’s own page)', 'Nota necesaria (de la web de la universidad)')}<input class="xin" data-x-in="goal.result" value="${esc(g.result)}" maxlength="120"></label>
<label class="xl">${L('Year I want to start', 'Año de inicio')}<input class="xin" inputmode="numeric" data-x-in="goal.year" value="${esc(g.year)}" maxlength="4"></label>
<button class="nx" data-x="savegoal">${L('Save my goal', 'Guardar objetivo')}</button>
<p class="note">${L('Entry requirements change. Ace shows what you enter; always confirm with the university.', 'Los requisitos cambian. Confírmalos con la universidad.')}</p></div>`;
    if (lv === 'university') h += `<div class="card" style="margin-top:10px"><label class="xl">${L('My institution', 'Mi institución')}<input class="xin" data-x-in="goal.inst" value="${esc(X.goal.inst || '')}" maxlength="120"></label><label class="xl">${L('Year of study', 'Curso')}<select class="xin" data-x-in="goal.syear">${[1, 2, 3, 4, 5, 6].map(n => `<option ${String(X.goal.syear || 1) === String(n) ? 'selected' : ''}>${n}</option>`).join('')}</select></label></div>`;
    return h + '</div>';
  }

  function shareView() {
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 4px">${L('Share my plan', 'Compartir mi plan')}</h2><p class="note" style="margin:0 0 8px">${L('A group plan covers you and up to 3 other people. Each person keeps their own account, progress and privacy.', 'Un plan grupal cubre a ti y hasta 3 personas más. Cada uno mantiene su cuenta y privacidad.')}</p>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    const p = X.plan;
    if (!p) return h + '<p class="note">…</p></div>';
    if (p.kind === 'owner') {
      h += `<div class="card"><b>${esc(p.plan_name || '')}</b><p class="note">${L('Seats used', 'Plazas usadas')}: ${1 + p.used} / ${p.seats} • ${L('invites waiting', 'invitaciones pendientes')}: ${p.pending}<br>${L('Renews or ends', 'Se renueva o termina')}: ${p.expires ? esc(String(p.expires).slice(0, 10)) : '-'}</p></div>
<button class="nx" data-x="mkinv" ${1 + p.used + p.pending >= p.seats ? 'disabled' : ''}>${L('Create an invite code', 'Crear código de invitación')}</button>`;
      if (X.invite) h += `<div class="card" style="margin-top:10px;text-align:center"><small>${L('Send this code. It works once and expires in 7 days.', 'Envía este código. Sirve una vez y caduca en 7 días.')}</small><div style="font-size:26px;font-weight:800;letter-spacing:.12em;margin:6px 0">${esc(X.invite)}</div><button class="xlink" data-x="copy" data-v="${esc(X.invite)}">${L('Copy', 'Copiar')}</button></div>`;
      h += `<div class="sh">${L('Members', 'Miembros')}</div>` + ((X.members || []).length ? `<div class="lst">${X.members.map(m => `<div class="li"><span class="m"><b>${esc(m.first_name)} ${esc(m.surname)}</b><small>${esc(m.level || '')} • ${L('joined', 'desde')} ${esc(String(m.joined_at).slice(0, 10))}</small></span><button class="xlink" data-x="rm" data-v="${m.member_id}">${L('Remove', 'Quitar')}</button></div>`).join('')}</div><p class="note">${L('You see names and join dates only. Scores and notes stay private.', 'Solo ves nombres y fechas. Las notas y resultados son privados.')}</p>` : `<p class="note">${L('No members yet.', 'Aún no hay miembros.')}</p>`);
    } else if (p.kind === 'member') {
      h += `<div class="card"><b>${L('You are using a shared plan', 'Usas un plan compartido')}</b><p class="note">${esc(p.plan_name || '')} • ${L('until', 'hasta')} ${p.expires ? esc(String(p.expires).slice(0, 10)) : '-'}</p></div><button class="nx" style="background:var(--tint);color:var(--text)" data-x="leave">${L('Leave this plan', 'Salir del plan')}</button><p class="note">${L('After leaving you can join another plan only after 30 days.', 'Tras salir, solo podrás unirte a otro plan después de 30 días.')}</p>`;
    } else {
      h += `<div class="card"><b>${L('Join with a code', 'Unirse con un código')}</b><input class="xin" style="text-transform:uppercase" data-x-in="joincode" maxlength="8" placeholder="ABCD1234" value="${esc(X.joincode || '')}"><button class="nx" data-x="join">${L('Join', 'Unirse')}</button></div><p class="note">${L('Want to pay once for yourself and up to 3 friends or siblings? Group plans are coming to checkout soon.', '¿Quieres pagar una vez por ti y hasta 3 personas? Los planes grupales llegarán pronto.')}</p>`;
    }
    return h + (X.err ? `<p class="note" style="color:var(--red)">${esc(X.err)}</p>` : '') + '</div>';
  }

  function familyView() {
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 4px">${L('Share progress with family', 'Compartir progreso con la familia')}</h2><p class="note" style="margin:0 0 8px">${L('Make a link a parent or guardian can open without an account. It shows your first name, streak, questions this week, subjects and course progress. It never shows your messages, notes or group posts. You can stop it any time.', 'Crea un enlace que un familiar abre sin cuenta. Muestra tu nombre, racha, preguntas de la semana, asignaturas y cursos. Nunca muestra mensajes, notas ni grupos. Puedes detenerlo cuando quieras.')}</p>`;
    if (!signedIn()) return h + needSignIn() + '</div>';
    if (!X.fam) return h + '<p class="note">…</p></div>';
    const act = X.fam.filter(l => !l.revoked_at && new Date(l.expires_at) > new Date());
    h += `<button class="nx" data-x="mkfam" ${act.length >= 3 ? 'disabled' : ''}>${L('Create a family link', 'Crear enlace familiar')}</button>`;
    const base = location.href.replace(/app\/.*$/, '') + 'family/?c=';
    h += act.map(l => `<div class="card" style="margin-top:10px"><b>${esc(l.label || L('Family link', 'Enlace familiar'))}</b><p class="note" style="word-break:break-all;margin:4px 0">${esc(base + l.code)}</p><p class="note" style="margin:0 0 6px">${L('Expires', 'Caduca')} ${esc(String(l.expires_at).slice(0, 10))}${l.last_viewed ? ' • ' + L('last opened', 'abierto') + ' ' + esc(String(l.last_viewed).slice(0, 10)) : ''}</p><button class="xlink" data-x="copy" data-v="${esc(base + l.code)}">${L('Copy link', 'Copiar')}</button> <button class="xlink" data-x="stopfam" data-v="${l.id}">${L('Stop sharing', 'Dejar de compartir')}</button></div>`).join('');
    if (!act.length) h += `<p class="note" style="margin-top:10px">${L('No active links.', 'Sin enlaces activos.')}</p>`;
    return h + (X.err ? `<p class="note" style="color:var(--red)">${esc(X.err)}</p>` : '') + '</div>';
  }

  function gpaView() {
    const g = X.gp, uk = g.mode === 'uk', sc = SCALES[g.scale];
    let h = `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('GPA calculator', 'Calculadora de media')}</h2><div class="xchips">
<button class="xchip ${g.mode === 'gpa' ? 'on' : ''}" data-x="gmode" data-v="gpa">${L('Grade points', 'Puntos')}</button><button class="xchip ${uk ? 'on' : ''}" data-x="gmode" data-v="uk">${L('UK % average', 'Media % (UK)')}</button><button class="xchip ${g.mode === 'need' ? 'on' : ''}" data-x="gmode" data-v="need">${L('What do I need?', '¿Qué necesito?')}</button></div>`;
    if (g.mode === 'need') {
      const r = calc.need(+g.cur, +g.done, +g.target, +g.rem, sc.max), has = +g.rem > 0 && g.target !== '' && g.cur !== '' && g.done !== '';
      h += `<label class="xl">${L('Scale', 'Escala')}<select class="xin" data-x-in="gp.scale"><option value="ng5" ${g.scale === 'ng5' ? 'selected' : ''}>5.0</option><option value="us4" ${g.scale === 'us4' ? 'selected' : ''}>4.0</option></select></label>
<label class="xl">${L('Current GPA', 'Media actual')}<input class="xin" inputmode="decimal" data-x-in="gp.cur" value="${esc(g.cur)}"></label><label class="xl">${L('Credits completed', 'Créditos hechos')}<input class="xin" inputmode="numeric" data-x-in="gp.done" value="${esc(g.done)}"></label>
<label class="xl">${L('Target final GPA', 'Media objetivo')}<input class="xin" inputmode="decimal" data-x-in="gp.target" value="${esc(g.target)}"></label><label class="xl">${L('Credits remaining', 'Créditos restantes')}<input class="xin" inputmode="numeric" data-x-in="gp.rem" value="${esc(g.rem)}"></label>
<button class="nx" data-x="redraw">${L('Calculate', 'Calcular')}</button>`;
      if (has) h += `<div class="card" style="margin-top:10px;text-align:center">${r.possible ? `<small>${L('You need an average of', 'Necesitas una media de')}</small><div style="font-size:28px;font-weight:800">${r.need}</div><small>${L('over your remaining credits', 'en tus créditos restantes')}</small>` : `<b>${L('That target is out of reach with the credits left.', 'Ese objetivo no es alcanzable con los créditos que quedan.')}</b><p class="note">${L('Try a lower target.', 'Prueba un objetivo menor.')}</p>`}</div>`;
      return h + '</div>';
    }
    if (!uk) h += `<label class="xl">${L('Scale', 'Escala')}<select class="xin" data-x-in="gp.scale"><option value="ng5" ${g.scale === 'ng5' ? 'selected' : ''}>5.0 (A=5 … F=0)</option><option value="us4" ${g.scale === 'us4' ? 'selected' : ''}>4.0 (A=4 … F=0)</option></select></label>`;
    h += g.rows.map((r, i) => `<div class="xrow"><input class="xin" placeholder="${L('Course', 'Asignatura')}" data-x-in="row.${i}.course" value="${esc(r.course)}" maxlength="40"><input class="xin xs" inputmode="numeric" placeholder="${L('Credits', 'Cr.')}" data-x-in="row.${i}.credits" value="${esc(r.credits)}" maxlength="2">${uk ? `<input class="xin xs" inputmode="numeric" placeholder="%" data-x-in="row.${i}.mark" value="${esc(r.mark || '')}" maxlength="3">` : `<select class="xin xs" data-x-in="row.${i}.grade">${Object.keys(sc.pts).map(k => `<option ${r.grade === k ? 'selected' : ''}>${k}</option>`).join('')}</select>`}<button class="xlink" data-x="rowdel" data-v="${i}" aria-label="remove">✕</button></div>`).join('');
    h += `<button class="xlink" data-x="rowadd">+ ${L('Add course', 'Añadir')}</button>`;
    if (uk) { const a = calc.ukAvg(g.rows); h += `<div class="card" style="margin-top:10px;text-align:center"><small>${L('Weighted average', 'Media ponderada')}</small><div style="font-size:28px;font-weight:800">${a.avg == null ? '-' : a.avg + '%'}</div><b>${calc.ukClass(a.avg)}</b></div>`; }
    else { const a = calc.gpa(g.rows, g.scale); h += `<div class="card" style="margin-top:10px;text-align:center"><small>GPA</small><div style="font-size:28px;font-weight:800">${a.gpa == null ? '-' : a.gpa.toFixed(2)}</div>${g.scale === 'ng5' ? `<b>${calc.nigClass(a.gpa)}</b>` : ''}<p class="note">${a.credits} ${L('credits', 'créditos')}</p></div>`; }
    return h + `<p class="note">${L('Grade boundaries differ between universities. Check yours.', 'Los límites varían entre universidades. Compruébalos.')}</p></div>`;
  }

  function citeView() {
    const f = X.ci, out = (f.title || f.author) ? calc.cite(f, f.style) : '';
    const inp = (k, l, ph) => `<label class="xl">${l}<input class="xin" data-x-in="ci.${k}" value="${esc(f[k])}" placeholder="${ph || ''}" maxlength="300"></label>`;
    return `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('Citation builder', 'Generador de citas')}</h2><div class="xchips">
${['apa', 'harvard'].map(k => `<button class="xchip ${f.style === k ? 'on' : ''}" data-x="cstyle" data-v="${k}">${k.toUpperCase()}</button>`).join('')}
${['book', 'article', 'web'].map(k => `<button class="xchip ${f.type === k ? 'on' : ''}" data-x="ctype" data-v="${k}">${{ book: L('Book', 'Libro'), article: L('Article', 'Artículo'), web: 'Web' }[k]}</button>`).join('')}</div>
${inp('author', L('Author (Surname, Initial.)', 'Autor (Apellido, I.)'), 'Okafor, C.')}${inp('year', L('Year', 'Año'), '2021')}${inp('title', L('Title', 'Título'))}
${f.type === 'article' ? inp('journal', L('Journal', 'Revista')) + inp('volume', L('Volume', 'Volumen')) + inp('issue', L('Issue', 'Número')) + inp('pages', L('Pages', 'Páginas'), '45–67') : inp('publisher', f.type === 'web' ? L('Website name', 'Sitio web') : L('Publisher', 'Editorial'))}
${f.type !== 'book' ? inp('url', 'URL', 'https://') : ''}
<button class="nx" data-x="redraw">${L('Update', 'Actualizar')}</button>
${out ? `<div class="card" style="margin-top:10px;font-size:14px;line-height:1.5" id="cout">${esc(out).replace(/\*([^*]+)\*/g, '<i>$1</i>')}</div><button class="xlink" data-x="copy" data-v="${esc(out.replace(/\*/g, ''))}">${L('Copy', 'Copiar')}</button>` : ''}
<p class="note">${L('Check the format against your department’s guide.', 'Compara con la guía de tu departamento.')}</p></div>`;
  }

  const mmss = s => String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
  function focusView() {
    const f = X.ft, left = f.end ? Math.max(0, Math.round((f.end - Date.now()) / 1000)) : f.left, run = !!f.end;
    return `<div class="pad">${back()}<h2 style="margin:0 0 6px">${L('Focus timer', 'Temporizador')}</h2><div class="xchips">
<button class="xchip ${f.mode === 'focus' ? 'on' : ''}" data-x="fmode" data-v="focus">${L('Focus 25', 'Enfoque 25')}</button><button class="xchip ${f.mode === 'break' ? 'on' : ''}" data-x="fmode" data-v="break">${L('Break 5', 'Descanso 5')}</button></div>
<div class="card" style="text-align:center;margin:12px 0"><div id="ftt" style="font-size:54px;font-weight:800;font-variant-numeric:tabular-nums">${mmss(left)}</div></div>
<button class="nx" data-x="ftgo">${run ? L('Pause', 'Pausa') : L('Start', 'Empezar')}</button>
<p class="note">${L('Minutes focused today', 'Minutos de enfoque hoy')}: ${focusToday()}</p></div>`;
  }
  const dayKey = () => new Date().toISOString().slice(0, 10);
  function focusToday() { try { const o = JSON.parse(localStorage.getItem('ace-focus') || '{}'); return o.d === dayKey() ? o.m : 0; } catch (e) { return 0; } }
  function focusAdd(m) { try { localStorage.setItem('ace-focus', JSON.stringify({ d: dayKey(), m: focusToday() + m })); } catch (e) { } }
  setInterval(() => {
    const f = X.ft; if (!f.end) return; const left = Math.max(0, Math.round((f.end - Date.now()) / 1000)), e = document.getElementById('ftt');
    if (e) e.textContent = mmss(left);
    if (left <= 0) { if (f.mode === 'focus') focusAdd(25); toast(f.mode === 'focus' ? L('Focus session done. Take a break.', 'Sesión terminada. Descansa.') : L('Break over. Ready?', 'Descanso terminado.')); f.mode = f.mode === 'focus' ? 'break' : 'focus'; f.left = f.mode === 'focus' ? 1500 : 300; f.end = 0; if (S.tab === 'focus') render(); }
  }, 1000);

  /* ---------- register views ---------- */
  Object.assign(V, { today: hub, tt: ttView, rev: revView, road: roadView, share: shareView, family: familyView, gpa: gpaView, cite: citeView, focus: focusView });

  /* ---------- data loading when a view opens ---------- */
  const nap = () => sync() ? sync().ready() : Promise.resolve(false);
  X.loaders = {
    tt: () => sync().table('class_notes').then(q => q.select('id,subject,topic,taught_on,summary,entered_text').order('created_at', { ascending: false }).limit(8)).then(r => { X.notes = r.data || []; }),
    rev: () => sync().table('revision_items').then(q => q.select('id,subject,topic,due_on').is('done_at', null).lte('due_on', dayKey()).order('due_on')).then(r => { X.due = r.data || []; }),
    share: () => Promise.all([sync().rpc('my_plan_status'), sync().rpc('my_group_members')]).then(([p, m]) => { X.plan = (p && p[0]) || { kind: 'none' }; X.members = m || []; }),
    family: () => sync().table('family_links').then(q => q.select('id,label,code,expires_at,revoked_at,last_viewed').order('created_at', { ascending: false })).then(r => { X.fam = r.data || []; }),
    today: () => sync().table('revision_items').then(q => q.select('id').is('done_at', null).lte('due_on', dayKey())).then(r => { X.due = r.data || []; }),
    road: () => sync().table('student_goals').then(q => q.select('*').maybeSingle()).then(r => { const d = r.data; if (d) X.goal = Object.assign(X.goal, { course: d.target_course || '', uni: d.target_university || '', result: d.target_result || '', year: d.target_year || '' }); })
  };
  const load = tab => X.loaders[tab] ? X.loaders[tab]() : null;
  const _render = window.render;
  window.render = function () {
    _render();
    const tab = S.tab, needs = !!X.loaders[tab];
    if (needs && X.loaded !== tab) {
      X.loaded = tab; X.err = '';
      nap().then(ok => (ok && signedIn()) || (X.loaders[tab] && X.loaders[tab].pub) ? load(tab) : null).then(() => { if (S.tab === tab) _render(); }).catch(e => { fail(e); if (S.tab === tab) _render(); });
    } else if (!needs) X.loaded = '';
  };

  /* ---------- input + clicks ---------- */
  function setPath(p, v) {
    if (p === 'subject' || p === 'text') X.tt[p] = v;
    else if (p === 'joincode') X.joincode = v.toUpperCase();
    else if (p.indexOf('goal.') === 0) { X.goal[p.slice(5)] = v; if (p === 'goal.inst' || p === 'goal.syear') { /* saved with the goal */ } }
    else if (p.indexOf('gp.') === 0) { X.gp[p.slice(3)] = v; if (p === 'gp.scale') { X.gp.rows.forEach(r => { if (!SCALES[v].pts[r.grade]) r.grade = 'A'; }); render(); } }
    else if (p.indexOf('ci.') === 0) X.ci[p.slice(3)] = v;
    else if (p.indexOf('row.') === 0) { const [, i, k] = p.split('.'); X.gp.rows[+i][k] = v; if (X.gp.mode !== 'need') liveGpa(); }
  }
  function liveGpa() { const card = document.querySelector('#v .card:last-of-type'); if (card && S.tab === 'gpa') { /* re-render is fine: rows keep focus loss minimal on change events */ } }
  document.addEventListener('input', e => { const t = e.target; if (t && t.dataset && t.dataset.xIn && t.tagName !== 'SELECT') setPath(t.dataset.xIn, t.value); });
  document.addEventListener('change', e => { const t = e.target; if (t && t.dataset && t.dataset.xIn) { setPath(t.dataset.xIn, t.value); if (S.tab === 'gpa' || S.tab === 'cite') render(); } });

  const done = () => render();
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-x]'); if (!b) return; const a = b.dataset.x, v = b.dataset.v;
    const run = p => { X.err = ''; p.then(done).catch(err => { fail(err); done(); }); };
    if (a === 'lvl') { P.lvl = v; svP(); sync() && sync().signedIn() && sync().rpc('set_my_level', { p_level: v, p_institution: X.goal.inst || null, p_programme: X.goal.course || null, p_year: v === 'university' ? +(X.goal.syear || 1) : null }).catch(() => { }); if (P.stage == null) { } render(); }
    else if (a === 'stage') { P.stage = +v; svP(); render(); }
    else if (a === 'ttgo') {
      const f = X.tt; if (!f.subject) { f.err = L('Choose a subject.', 'Elige una asignatura.'); return render(); } if (f.text.trim().length < 10) { f.err = L('Tell Ace a little more.', 'Cuenta un poco más.'); return render(); }
      f.busy = true; f.err = ''; render();
      sync().fn('taught-today', { subject: f.subject, text: f.text, exam: ex(), country: cname(), lang: UIL() }).then(r => { f.res = r; f.ans = {}; f.saved = false; f.busy = false; f.noteId = r.note_id; X.notes = null; X.loaded = ''; render(); }).catch(err => { f.busy = false; f.err = (err && err.msg) || L('Try again.', 'Inténtalo de nuevo.'); render(); });
    }
    else if (a === 'ttnew') { Object.assign(X.tt, { text: '', res: null, ans: {}, saved: false, err: '' }); X.loaded = ''; render(); }
    else if (a === 'opennote') { const n = (X.notes || []).find(x => x.id === v); if (n && n.summary) { Object.assign(X.tt, { res: n.summary, subject: n.subject, text: n.entered_text, ans: {}, saved: false, noteId: n.id }); render(); } else toast(L('No study pack for this note yet.', 'Esta nota aún no tiene paquete.')); }
    else if (a === 'tans') { const [q, o] = v.split(':').map(Number); X.tt.ans[q] = o; render(); }
    else if (a === 'addrev') { const f = X.tt; run(sync().rpc('add_revision', { p_exam: ex(), p_subject: f.subject, p_topic: (f.res && f.res.topic) || f.subject, p_note: f.noteId || null }).then(() => { f.saved = true; toast(L('Added. First review is tomorrow.', 'Añadido. Primer repaso mañana.')); })); }
    else if (a === 'revok' || a === 'revno') { run(sync().rpc('complete_revision', { p_id: v, p_correct: a === 'revok' }).then(d => { X.due = X.due.filter(i => i.id !== v); toast(a === 'revok' ? (d ? L('Next review: ', 'Próximo repaso: ') + d : L('Mastered!', '¡Dominado!')) : L('See you tomorrow.', 'Hasta mañana.')); })); }
    else if (a === 'savegoal') { const g = X.goal; P.goal2 = g; svP(); run(sync().signedIn() ? sync().table('student_goals').then(q => q.upsert({ user_id: sync().uid(), target_course: g.course || null, target_university: g.uni || null, target_result: g.result || null, target_year: +g.year || null, target_country: S.c, updated_at: new Date().toISOString() })).then(r => { if (r.error) throw { msg: r.error.message }; toast(L('Goal saved.', 'Objetivo guardado.')); }) : Promise.resolve().then(() => toast(L('Saved on this device. Sign in to keep it in your account.', 'Guardado en este dispositivo.')))); }
    else if (a === 'mkinv') { run(sync().rpc('create_invite', { p_relation: 'friend' }).then(c => { X.invite = c; X.loaded = ''; return load('share'); })); }
    else if (a === 'join') { run(sync().rpc('join_plan', { p_code: X.joincode || '' }).then(r => { if (typeof r === 'string' && r.startsWith('error:')) throw { msg: TRL(r.slice(6)) }; X.joincode = ''; toast(L('You joined the plan.', 'Te has unido al plan.')); return load('share'); })); }
    else if (a === 'leave') { run(sync().rpc('leave_or_remove', {}).then(() => { toast(L('You left the plan.', 'Has salido del plan.')); return load('share'); })); }
    else if (a === 'rm') { run(sync().rpc('leave_or_remove', { p_member: v }).then(() => load('share'))); }
    else if (a === 'pushon') { X.h.push && X.h.push(); }
    else if (a === 'mkfam') { run(sync().rpc('create_family_link', { p_label: null }).then(() => load('family'))); }
    else if (a === 'stopfam') { run(sync().rpc('revoke_family_link', { p_id: v }).then(() => load('family'))); }
    else if (a === 'copy') { try { navigator.clipboard.writeText(v).then(() => toast(L('Copied', 'Copiado'))).catch(() => toast(v)); } catch (x) { toast(v); } }
    else if (a === 'gmode') { X.gp.mode = v; render(); }
    else if (a === 'rowadd') { X.gp.rows.push({ course: '', credits: '3', grade: 'A' }); render(); }
    else if (a === 'rowdel') { if (X.gp.rows.length > 1) X.gp.rows.splice(+v, 1); render(); }
    else if (a === 'cstyle') { X.ci.style = v; render(); } else if (a === 'ctype') { X.ci.type = v; render(); }
    else if (a === 'redraw') render();
    else if (a === 'fmode') { X.ft.mode = v; X.ft.end = 0; X.ft.left = v === 'focus' ? 1500 : 300; render(); }
    else if (a === 'ftgo') { const f = X.ft; if (f.end) { f.left = Math.max(1, Math.round((f.end - Date.now()) / 1000)); f.end = 0; } else f.end = Date.now() + f.left * 1000; render(); }
  });

  /* ---------- small styles ---------- */
  const st = document.createElement('style');
  st.textContent = `.xchips{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}.xchip{border:1px solid var(--border);background:var(--surface);color:var(--text);border-radius:99px;padding:8px 14px;font-weight:600;font-size:13px}.xchip.on{background:var(--primary-dark);color:#fff;border-color:var(--primary-dark)}
.xl{display:block;font-size:12px;font-weight:600;color:var(--text2);margin:10px 0 0}.xin{display:block;width:100%;box-sizing:border-box;margin-top:4px;padding:10px;border:1px solid var(--border);border-radius:10px;background:var(--surface);color:var(--text);font:inherit;font-size:14px}
.xlink{border:0;background:none;color:var(--ink);font-weight:700;font-size:13px;padding:6px 4px}.xtag{font-size:11px;font-weight:700;background:var(--primary-dark);color:#fff;border-radius:99px;padding:3px 9px}
.xul{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.5}.xrow{display:flex;gap:6px;align-items:center;margin-top:8px}.xrow .xin{margin-top:0}.xrow .xs{width:64px;flex:none}
.xopt{border:1px solid var(--border);border-radius:10px;margin-top:8px;font-size:14px}.xopt.ok{background:#d9f5e3;border-color:#2e9e5b;color:#0b3d1f}.xopt.bad{background:#fde2e2;border-color:#d64545;color:#5c1111}`;
  document.head.appendChild(st);
  if (P.goal2) Object.assign(X.goal, P.goal2);
})();
