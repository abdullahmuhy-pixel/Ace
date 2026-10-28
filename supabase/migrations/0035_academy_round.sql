-- 0035: Ace Academy courses added this round (physics-beginners chemistry-foundations cells-genetics environmental-science astronomy-basics algebra-basics intro-calculus climate-science). Idempotent: safe to run again.
-- Course: Physics for Beginners. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('physics-beginners','Physics for Beginners','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='physics-beginners';
insert into public.course_keys(course,qid,answer,why) values
  ('physics-beginners','q1',1,'120 / 1.5.'),
  ('physics-beginners','q2',3,'20 / 5.'),
  ('physics-beginners','q3',0,'The slope gives acceleration.'),
  ('physics-beginners','q4',2,'F = ma.'),
  ('physics-beginners','q5',2,'W = mg = 60 x 9.8.'),
  ('physics-beginners','q6',0,'Inertia.'),
  ('physics-beginners','q7',3,'½ x 1000 x 400.'),
  ('physics-beginners','q8',1,'4900 / 7.'),
  ('physics-beginners','q9',0,'v = fλ.'),
  ('physics-beginners','q10',2,'It needs a medium.'),
  ('physics-beginners','q11',1,'I = V / R.'),
  ('physics-beginners','q12',3,'Parallel branches.'),
  ('physics-beginners','q13',3,'500 / 250.'),
  ('physics-beginners','q14',1,'Q = mcΔT.');
insert into public.course_lessons(course,lesson_id,position) values
  ('physics-beginners','motion',0),
  ('physics-beginners','forces',1),
  ('physics-beginners','energy-power',2),
  ('physics-beginners','waves',3),
  ('physics-beginners','electricity',4),
  ('physics-beginners','matter-heat',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='physics-beginners' and lesson_id not in ('motion','forces','energy-power','waves','electricity','matter-heat');
-- Course: Chemistry Foundations. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('chemistry-foundations','Chemistry Foundations','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='chemistry-foundations';
insert into public.course_keys(course,qid,answer,why) values
  ('chemistry-foundations','q1',1,'It defines the element.'),
  ('chemistry-foundations','q2',3,'11 + 12.'),
  ('chemistry-foundations','q3',0,'Same element, different neutrons.'),
  ('chemistry-foundations','q4',2,'So they react similarly.'),
  ('chemistry-foundations','q5',2,'Two, eight, then one.'),
  ('chemistry-foundations','q6',0,'Na⁺ and Cl⁻ ions.'),
  ('chemistry-foundations','q7',3,'Non-metals share electrons.'),
  ('chemistry-foundations','q8',1,'4 H and 2 O on each side.'),
  ('chemistry-foundations','q9',0,'The acid is neutralised.'),
  ('chemistry-foundations','q10',2,'2 x 1.008 + 16.00.'),
  ('chemistry-foundations','q11',1,'36 / 18.02.'),
  ('chemistry-foundations','q12',3,'0.100 mol / 0.5 L.'),
  ('chemistry-foundations','q13',3,'10².'),
  ('chemistry-foundations','q14',1,'Prevents dangerous splashing.');
insert into public.course_lessons(course,lesson_id,position) values
  ('chemistry-foundations','atoms',0),
  ('chemistry-foundations','periodic-table',1),
  ('chemistry-foundations','bonding',2),
  ('chemistry-foundations','reactions',3),
  ('chemistry-foundations','moles',4),
  ('chemistry-foundations','acids-everyday',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='chemistry-foundations' and lesson_id not in ('atoms','periodic-table','bonding','reactions','moles','acids-everyday');
-- Course: Cells and Genetics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('cells-genetics','Cells and Genetics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='cells-genetics';
insert into public.course_keys(course,qid,answer,why) values
  ('cells-genetics','q1',1,'DNA floats in the cytoplasm.'),
  ('cells-genetics','q2',3,'The powerhouse of the cell.'),
  ('cells-genetics','q3',0,'For support and photosynthesis.'),
  ('cells-genetics','q4',2,'15 / 0.05.'),
  ('cells-genetics','q5',2,'Diffusion of water.'),
  ('cells-genetics','q6',0,'Requires energy.'),
  ('cells-genetics','q7',3,'23 pairs.'),
  ('cells-genetics','q8',1,'Gametes have 23.'),
  ('cells-genetics','q9',0,'A=T=30%; C=G=20%.'),
  ('cells-genetics','q10',2,'Genes code for proteins.'),
  ('cells-genetics','q11',1,'AA, Aa, Aa show dominant; aa recessive.'),
  ('cells-genetics','q12',3,'One of four combinations is SS.'),
  ('cells-genetics','q13',3,'Two of four combinations.'),
  ('cells-genetics','q14',1,'Privacy and consent matter.');
insert into public.course_lessons(course,lesson_id,position) values
  ('cells-genetics','cells',0),
  ('cells-genetics','cell-processes',1),
  ('cells-genetics','cell-division',2),
  ('cells-genetics','dna-proteins',3),
  ('cells-genetics','inheritance',4),
  ('cells-genetics','genetics-society',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='cells-genetics' and lesson_id not in ('cells','cell-processes','cell-division','dna-proteins','inheritance','genetics-society');
-- Course: Environmental Science. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('environmental-science','Environmental Science','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='environmental-science';
insert into public.course_keys(course,qid,answer,why) values
  ('environmental-science','q1',1,'Living and non-living parts together.'),
  ('environmental-science','q2',3,'They recycle nutrients.'),
  ('environmental-science','q3',0,'About 10% passes each step.'),
  ('environmental-science','q4',2,'The 10% rule.'),
  ('environmental-science','q5',2,'Part of the water cycle.'),
  ('environmental-science','q6',0,'Algae use up oxygen.'),
  ('environmental-science','q7',3,'Nature''s benefits to people.'),
  ('environmental-science','q8',1,'Endangered species trade.'),
  ('environmental-science','q9',0,'Smoke harms lungs.'),
  ('environmental-science','q10',2,'Prevent waste first.'),
  ('environmental-science','q11',1,'0.5 x 365.'),
  ('environmental-science','q12',3,'50 000 x 0.98¹⁰.'),
  ('environmental-science','q13',3,'Environmental impact assessment.'),
  ('environmental-science','q14',1,'Design out waste.');
insert into public.course_lessons(course,lesson_id,position) values
  ('environmental-science','ecosystems',0),
  ('environmental-science','cycles',1),
  ('environmental-science','biodiversity',2),
  ('environmental-science','pollution',3),
  ('environmental-science','resources-land',4),
  ('environmental-science','sustainability',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='environmental-science' and lesson_id not in ('ecosystems','cycles','biodiversity','pollution','resources-land','sustainability');
-- Course: Astronomy. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('astronomy-basics','Astronomy','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='astronomy-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('astronomy-basics','q1',1,'About 23.5° tilt.'),
  ('astronomy-basics','q2',3,'New moon to new moon.'),
  ('astronomy-basics','q3',0,'The Moon blocks the Sun.'),
  ('astronomy-basics','q4',2,'Jupiter and Saturn.'),
  ('astronomy-basics','q5',2,'About 150 million km.'),
  ('astronomy-basics','q6',0,'About 499 seconds.'),
  ('astronomy-basics','q7',3,'1.52^1.5.'),
  ('astronomy-basics','q8',1,'Hydrogen fuses into helium.'),
  ('astronomy-basics','q9',0,'About 9.46 x 10¹² km.'),
  ('astronomy-basics','q10',2,'The nearest star beyond the Sun.'),
  ('astronomy-basics','q11',1,'Colour indicates temperature.'),
  ('astronomy-basics','q12',3,'v = H₀d.'),
  ('astronomy-basics','q13',3,'4.6 billion is the solar system''s age.'),
  ('astronomy-basics','q14',1,'64 dishes in the Karoo.');
insert into public.course_lessons(course,lesson_id,position) values
  ('astronomy-basics','earth-sky',0),
  ('astronomy-basics','solar-system',1),
  ('astronomy-basics','gravity-orbits',2),
  ('astronomy-basics','stars',3),
  ('astronomy-basics','galaxies-universe',4),
  ('astronomy-basics','telescopes-africa',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='astronomy-basics' and lesson_id not in ('earth-sky','solar-system','gravity-orbits','stars','galaxies-universe','telescopes-africa');
-- Course: Algebra. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('algebra-basics','Algebra','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='algebra-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('algebra-basics','q1',1,'Collect like terms.'),
  ('algebra-basics','q2',3,'6x + 12 - 2x + 2.'),
  ('algebra-basics','q3',0,'x² - 2x + 3x - 6.'),
  ('algebra-basics','q4',2,'Difference of two squares.'),
  ('algebra-basics','q5',2,'3x = 15.'),
  ('algebra-basics','q6',0,'2x - 6 = x + 4.'),
  ('algebra-basics','q7',3,'2x > 6.'),
  ('algebra-basics','q8',1,'150 + 20x = 350.'),
  ('algebra-basics','q9',0,'2x + 4 = 30.'),
  ('algebra-basics','q10',2,'Add to eliminate y.'),
  ('algebra-basics','q11',1,'(x - 2)(x - 3) = 0.'),
  ('algebra-basics','q12',3,'Quadratic formula with √20.'),
  ('algebra-basics','q13',3,'b² - 4ac < 0.'),
  ('algebra-basics','q14',1,'Gradient 2, intercept 1.');
insert into public.course_lessons(course,lesson_id,position) values
  ('algebra-basics','expressions',0),
  ('algebra-basics','linear-equations',1),
  ('algebra-basics','word-problems',2),
  ('algebra-basics','simultaneous',3),
  ('algebra-basics','quadratics',4),
  ('algebra-basics','functions-graphs',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='algebra-basics' and lesson_id not in ('expressions','linear-equations','word-problems','simultaneous','quadratics','functions-graphs');
-- Course: Introduction to Calculus. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('intro-calculus','Introduction to Calculus','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='intro-calculus';
insert into public.course_keys(course,qid,answer,why) values
  ('intro-calculus','q1',1,'(9 - 1) / 2.'),
  ('intro-calculus','q2',3,'It simplifies to x + 2.'),
  ('intro-calculus','q3',0,'Power rule.'),
  ('intro-calculus','q4',2,'4 x 3 = 12, power drops to 3.'),
  ('intro-calculus','q5',2,'12 x 8.'),
  ('intro-calculus','q6',0,'Differentiate term by term.'),
  ('intro-calculus','q7',3,'The tangent is horizontal.'),
  ('intro-calculus','q8',1,'Area 625 m².'),
  ('intro-calculus','q9',0,'P''(x) = -4x + 40 = 0.'),
  ('intro-calculus','q10',2,'v = 3t².'),
  ('intro-calculus','q11',1,'a = 6t.'),
  ('intro-calculus','q12',3,'Reverse the power rule.'),
  ('intro-calculus','q13',3,'27/3.'),
  ('intro-calculus','q14',1,'Area under the velocity graph.');
insert into public.course_lessons(course,lesson_id,position) values
  ('intro-calculus','rates-limits',0),
  ('intro-calculus','derivatives',1),
  ('intro-calculus','optimisation',2),
  ('intro-calculus','motion',3),
  ('intro-calculus','integration',4),
  ('intro-calculus','applications',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='intro-calculus' and lesson_id not in ('rates-limits','derivatives','optimisation','motion','integration','applications');
-- Course: Climate Science. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('climate-science','Climate Science','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='climate-science';
insert into public.course_keys(course,qid,answer,why) values
  ('climate-science','q1',1,'Usually 30 years or more.'),
  ('climate-science','q2',3,'Greenhouse gases keep it near 15 °C.'),
  ('climate-science','q3',0,'Coal, oil and gas release CO₂.'),
  ('climate-science','q4',2,'140 / 280.'),
  ('climate-science','q5',2,'Short-lived but powerful.'),
  ('climate-science','q6',0,'Ocean acidification.'),
  ('climate-science','q7',3,'3.7 x 30 = 111 mm.'),
  ('climate-science','q8',1,'Intergovernmental Panel on Climate Change.'),
  ('climate-science','q9',0,'Low emissions, high vulnerability.'),
  ('climate-science','q10',2,'Agreed in 2015.'),
  ('climate-science','q11',1,'400 / 40.'),
  ('climate-science','q12',3,'90 x 12.'),
  ('climate-science','q13',3,'Adaptation means adjusting to impacts.'),
  ('climate-science','q14',1,'It reduces harm from climate impacts.');
insert into public.course_lessons(course,lesson_id,position) values
  ('climate-science','weather-climate',0),
  ('climate-science','causes',1),
  ('climate-science','evidence',2),
  ('climate-science','africa-impacts',3),
  ('climate-science','mitigation',4),
  ('climate-science','adaptation',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='climate-science' and lesson_id not in ('weather-climate','causes','evidence','africa-impacts','mitigation','adaptation');
