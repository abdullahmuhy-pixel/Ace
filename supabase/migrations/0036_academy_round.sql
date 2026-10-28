-- 0036: Ace Academy courses added this round (civil-engineering-basics electrical-engineering-basics mechanical-engineering-basics renewable-energy surveying-basics technical-drawing electrical-installation plumbing-basics carpentry-joinery welding-basics auto-mechanics). Idempotent: safe to run again.
-- Course: Civil Engineering Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('civil-engineering-basics','Civil Engineering Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='civil-engineering-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('civil-engineering-basics','q1',1,'Soils, rock and foundations.'),
  ('civil-engineering-basics','q2',3,'Steel reinforcement handles tension.'),
  ('civil-engineering-basics','q3',0,'5 x 4 x 0.15.'),
  ('civil-engineering-basics','q4',2,'1 + 2 + 4 = 7.'),
  ('civil-engineering-basics','q5',2,'Keep the water-cement ratio low.'),
  ('civil-engineering-basics','q6',0,'100 000 / 0.04.'),
  ('civil-engineering-basics','q7',3,'wL²/8.'),
  ('civil-engineering-basics','q8',1,'Moment depends on L².'),
  ('civil-engineering-basics','q9',0,'200 / 100.'),
  ('civil-engineering-basics','q10',2,'They crack buildings.'),
  ('civil-engineering-basics','q11',1,'3 / 150.'),
  ('civil-engineering-basics','q12',3,'Q = A x v.'),
  ('civil-engineering-basics','q13',3,'Drainage is vital.'),
  ('civil-engineering-basics','q14',1,'Prevent collapse.');
insert into public.course_lessons(course,lesson_id,position) values
  ('civil-engineering-basics','what-civil',0),
  ('civil-engineering-basics','materials',1),
  ('civil-engineering-basics','structures',2),
  ('civil-engineering-basics','soils-foundations',3),
  ('civil-engineering-basics','roads-water',4),
  ('civil-engineering-basics','site-safety-careers',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='civil-engineering-basics' and lesson_id not in ('what-civil','materials','structures','soils-foundations','roads-water','site-safety-careers');
-- Course: Electrical Engineering Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('electrical-engineering-basics','Electrical Engineering Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='electrical-engineering-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('electrical-engineering-basics','q1',1,'The rate of flow of charge.'),
  ('electrical-engineering-basics','q2',3,'I = V / R.'),
  ('electrical-engineering-basics','q3',0,'Series resistances add.'),
  ('electrical-engineering-basics','q4',2,'Product over sum.'),
  ('electrical-engineering-basics','q5',2,'Independent switching.'),
  ('electrical-engineering-basics','q6',0,'P = V x I.'),
  ('electrical-engineering-basics','q7',3,'6 kWh x R2.50.'),
  ('electrical-engineering-basics','q8',1,'Peak = rms x √2.'),
  ('electrical-engineering-basics','q9',0,'Losses go with I²R.'),
  ('electrical-engineering-basics','q10',2,'230 / 12.'),
  ('electrical-engineering-basics','q11',1,'½CV².'),
  ('electrical-engineering-basics','q12',3,'Used in rectifiers.'),
  ('electrical-engineering-basics','q13',3,'Earth-leakage protection.'),
  ('electrical-engineering-basics','q14',1,'Efficiencies multiply.');
insert into public.course_lessons(course,lesson_id,position) values
  ('electrical-engineering-basics','charge-current',0),
  ('electrical-engineering-basics','circuits',1),
  ('electrical-engineering-basics','power-energy',2),
  ('electrical-engineering-basics','ac-power',3),
  ('electrical-engineering-basics','components-electronics',4),
  ('electrical-engineering-basics','safety-careers',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='electrical-engineering-basics' and lesson_id not in ('charge-current','circuits','power-energy','ac-power','components-electronics','safety-careers');
-- Course: Mechanical Engineering Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('mechanical-engineering-basics','Mechanical Engineering Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='mechanical-engineering-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('mechanical-engineering-basics','q1',1,'F = ma.'),
  ('mechanical-engineering-basics','q2',3,'Work = force x distance.'),
  ('mechanical-engineering-basics','q3',0,'Power = work / time.'),
  ('mechanical-engineering-basics','q4',2,'Output / input.'),
  ('mechanical-engineering-basics','q5',2,'100 x 0.5 / 2.'),
  ('mechanical-engineering-basics','q6',0,'Ratio 4 : 1.'),
  ('mechanical-engineering-basics','q7',3,'Speed down, torque up.'),
  ('mechanical-engineering-basics','q8',1,'Force scales with area.'),
  ('mechanical-engineering-basics','q9',0,'10 000 / 0.0001.'),
  ('mechanical-engineering-basics','q10',2,'Common in shafts and axles.'),
  ('mechanical-engineering-basics','q11',1,'mcΔT.'),
  ('mechanical-engineering-basics','q12',3,'Particle to particle.'),
  ('mechanical-engineering-basics','q13',3,'Turning.'),
  ('mechanical-engineering-basics','q14',1,'Cheaper than breakdowns.');
insert into public.course_lessons(course,lesson_id,position) values
  ('mechanical-engineering-basics','what-mechanical',0),
  ('mechanical-engineering-basics','work-energy-power',1),
  ('mechanical-engineering-basics','machines',2),
  ('mechanical-engineering-basics','materials-stress',3),
  ('mechanical-engineering-basics','heat-fluids',4),
  ('mechanical-engineering-basics','design-manufacture',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='mechanical-engineering-basics' and lesson_id not in ('what-mechanical','work-energy-power','machines','materials-stress','heat-fluids','design-manufacture');
-- Course: Renewable Energy. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('renewable-energy','Renewable Energy','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='renewable-energy';
insert into public.course_keys(course,qid,answer,why) values
  ('renewable-energy','q1',1,'Naturally replenished.'),
  ('renewable-energy','q2',3,'100 x 8760 x 0.2.'),
  ('renewable-energy','q3',0,'CSP.'),
  ('renewable-energy','q4',2,'Power depends on v³.'),
  ('renewable-energy','q5',2,'0.4 x ½ρAv³.'),
  ('renewable-energy','q6',0,'Theoretical maximum.'),
  ('renewable-energy','q7',3,'ρgQHη.'),
  ('renewable-energy','q8',1,'In the Rift Valley.'),
  ('renewable-energy','q9',0,'Baseload.'),
  ('renewable-energy','q10',2,'Anaerobic digestion.'),
  ('renewable-energy','q11',1,'5 x 0.8.'),
  ('renewable-energy','q12',3,'Gravity storage.'),
  ('renewable-energy','q13',3,'Lifetime cost.'),
  ('renewable-energy','q14',1,'The cube law.');
insert into public.course_lessons(course,lesson_id,position) values
  ('renewable-energy','energy-transition',0),
  ('renewable-energy','solar',1),
  ('renewable-energy','wind',2),
  ('renewable-energy','hydro-geothermal',3),
  ('renewable-energy','bioenergy',4),
  ('renewable-energy','storage-grids',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='renewable-energy' and lesson_id not in ('energy-transition','solar','wind','hydro-geothermal','bioenergy','storage-grids');
-- Course: Surveying. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('surveying-basics','Surveying','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='surveying-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('surveying-basics','q1',1,'For land titles.'),
  ('surveying-basics','q2',3,'Prevents errors building up.'),
  ('surveying-basics','q3',0,'100 x cos 10°.'),
  ('surveying-basics','q4',2,'4 x 5 m.'),
  ('surveying-basics','q5',2,'50 / 2000 m.'),
  ('surveying-basics','q6',0,'BS - FS positive.'),
  ('surveying-basics','q7',3,'Add the rise.'),
  ('surveying-basics','q8',1,'The staff stands higher.'),
  ('surveying-basics','q9',0,'Add 180°.'),
  ('surveying-basics','q10',2,'√(40² + 30²).'),
  ('surveying-basics','q11',1,'40 x 30.'),
  ('surveying-basics','q12',3,'1 ha = 10 000 m².'),
  ('surveying-basics','q13',3,'With correction data.'),
  ('surveying-basics','q14',1,'Beacons mark boundaries.');
insert into public.course_lessons(course,lesson_id,position) values
  ('surveying-basics','intro',0),
  ('surveying-basics','distance-scale',1),
  ('surveying-basics','levelling',2),
  ('surveying-basics','angles-coordinates',3),
  ('surveying-basics','modern-tools',4),
  ('surveying-basics','setting-out-land',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='surveying-basics' and lesson_id not in ('intro','distance-scale','levelling','angles-coordinates','modern-tools','setting-out-land');
-- Course: Technical Drawing. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('technical-drawing','Technical Drawing','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='technical-drawing';
insert into public.course_keys(course,qid,answer,why) values
  ('technical-drawing','q1',1,'Each larger A size doubles the area.'),
  ('technical-drawing','q2',3,'Edges not visible in that view.'),
  ('technical-drawing','q3',0,'Long dash, short dash.'),
  ('technical-drawing','q4',2,'6000 / 50.'),
  ('technical-drawing','q5',2,'3600 / 100.'),
  ('technical-drawing','q6',0,'Enlarged five times.'),
  ('technical-drawing','q7',3,'R is radius.'),
  ('technical-drawing','q8',1,'Write real sizes.'),
  ('technical-drawing','q9',0,'Third angle puts it above.'),
  ('technical-drawing','q10',2,'They align horizontally.'),
  ('technical-drawing','q11',1,'Axes at 120° to each other.'),
  ('technical-drawing','q12',3,'Thin lines at 45°.'),
  ('technical-drawing','q13',3,'Showing doors and windows.'),
  ('technical-drawing','q14',1,'A digital building model.');
insert into public.course_lessons(course,lesson_id,position) values
  ('technical-drawing','purpose',0),
  ('technical-drawing','lines-tools',1),
  ('technical-drawing','scales',2),
  ('technical-drawing','projection',3),
  ('technical-drawing','pictorial-sections',4),
  ('technical-drawing','building-cad',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='technical-drawing' and lesson_id not in ('purpose','lines-tools','scales','projection','pictorial-sections','building-cad');
-- Course: Electrical Installation. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('electrical-installation','Electrical Installation','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='electrical-installation';
insert into public.course_keys(course,qid,answer,why) values
  ('electrical-installation','q1',1,'Safe isolation.'),
  ('electrical-installation','q2',3,'Earth leakage.'),
  ('electrical-installation','q3',0,'Each circuit''s wiring.'),
  ('electrical-installation','q4',2,'Old installations differ.'),
  ('electrical-installation','q5',2,'I = P / V.'),
  ('electrical-installation','q6',0,'600 + 120.'),
  ('electrical-installation','q7',3,'With 16 or 20 A breakers.'),
  ('electrical-installation','q8',1,'18 x 20 x 25 / 1000.'),
  ('electrical-installation','q9',0,'9 / 230.'),
  ('electrical-installation','q10',2,'Tighten every connection.'),
  ('electrical-installation','q11',1,'Metal parts do not stay live.'),
  ('electrical-installation','q12',3,'Often 500 V DC.'),
  ('electrical-installation','q13',3,'Unplug and test.'),
  ('electrical-installation','q14',1,'This endangers line workers.');
insert into public.course_lessons(course,lesson_id,position) values
  ('electrical-installation','safety-law',0),
  ('electrical-installation','supply-board',1),
  ('electrical-installation','circuits-loads',2),
  ('electrical-installation','cables-volt-drop',3),
  ('electrical-installation','earthing-testing',4),
  ('electrical-installation','fault-finding-solar',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='electrical-installation' and lesson_id not in ('safety-law','supply-board','circuits-loads','cables-volt-drop','earthing-testing','fault-finding-solar');
-- Course: Plumbing. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('plumbing-basics','Plumbing','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='plumbing-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('plumbing-basics','q1',1,'Know where it is.'),
  ('plumbing-basics','q2',3,'ρgh.'),
  ('plumbing-basics','q3',0,'Chemical welding.'),
  ('plumbing-basics','q4',2,'2 m³.'),
  ('plumbing-basics','q5',2,'2000 / 250.'),
  ('plumbing-basics','q6',0,'8 x 5 x 0.15.'),
  ('plumbing-basics','q7',3,'Prevents bursts.'),
  ('plumbing-basics','q8',1,'25 mm per metre.'),
  ('plumbing-basics','q9',0,'Water seal.'),
  ('plumbing-basics','q10',2,'Balance pressure.'),
  ('plumbing-basics','q11',1,'0.1 x 1440.'),
  ('plumbing-basics','q12',3,'A moving meter means a leak.'),
  ('plumbing-basics','q13',3,'Bin them instead.'),
  ('plumbing-basics','q14',1,'Find leaks early.');
insert into public.course_lessons(course,lesson_id,position) values
  ('plumbing-basics','water-supply',0),
  ('plumbing-basics','pipes-fittings',1),
  ('plumbing-basics','storage-hot',2),
  ('plumbing-basics','drainage',3),
  ('plumbing-basics','repairs',4),
  ('plumbing-basics','practice-careers',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='plumbing-basics' and lesson_id not in ('water-supply','pipes-fittings','storage-hot','drainage','repairs','practice-careers');
-- Course: Carpentry and Joinery. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('carpentry-joinery','Carpentry and Joinery','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='carpentry-joinery';
insert into public.course_keys(course,qid,answer,why) values
  ('carpentry-joinery','q1',1,'From conifers.'),
  ('carpentry-joinery','q2',3,'Reduces shrinkage and warping.'),
  ('carpentry-joinery','q3',0,'Use treated or resistant timber.'),
  ('carpentry-joinery','q4',2,'Crosscut saws cut across.'),
  ('carpentry-joinery','q5',2,'Blunt tools slip.'),
  ('carpentry-joinery','q6',0,'2400 - 2209.'),
  ('carpentry-joinery','q7',3,'Pythagoras.'),
  ('carpentry-joinery','q8',1,'0.05 x 0.1 x 3.'),
  ('carpentry-joinery','q9',0,'Tenon fits a mortise.'),
  ('carpentry-joinery','q10',2,'They resist pulling apart.'),
  ('carpentry-joinery','q11',1,'Especially near ends.'),
  ('carpentry-joinery','q12',3,'√(3² + 1.5²).'),
  ('carpentry-joinery','q13',3,'9 spaces, 10 members.'),
  ('carpentry-joinery','q14',1,'Gives a smooth finish.');
insert into public.course_lessons(course,lesson_id,position) values
  ('carpentry-joinery','timber',0),
  ('carpentry-joinery','tools-safety',1),
  ('carpentry-joinery','measuring',2),
  ('carpentry-joinery','joints',3),
  ('carpentry-joinery','roofs-site',4),
  ('carpentry-joinery','finishing-careers',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='carpentry-joinery' and lesson_id not in ('timber','tools-safety','measuring','joints','roofs-site','finishing-careers');
-- Course: Welding Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('welding-basics','Welding Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='welding-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('welding-basics','q1',1,'Shielded metal arc welding.'),
  ('welding-basics','q2',3,'Gas metal arc welding.'),
  ('welding-basics','q3',0,'With separate filler.'),
  ('welding-basics','q4',2,'Always use the correct filter.'),
  ('welding-basics','q5',2,'Ventilate and extract.'),
  ('welding-basics','q6',0,'Never a flame.'),
  ('welding-basics','q7',3,'About 40 A per mm.'),
  ('welding-basics','q8',1,'Thousands of psi.'),
  ('welding-basics','q9',0,'Moisture causes cracking.'),
  ('welding-basics','q10',2,'Gravity works against you.'),
  ('welding-basics','q11',1,'Often from damp electrodes.'),
  ('welding-basics','q12',3,'Too much current or long arc.'),
  ('welding-basics','q13',3,'V x A x 60 / speed / 1000.'),
  ('welding-basics','q14',1,'Non-destructive testing.');
insert into public.course_lessons(course,lesson_id,position) values
  ('welding-basics','what-welding',0),
  ('welding-basics','safety',1),
  ('welding-basics','equipment-electrodes',2),
  ('welding-basics','joints-positions',3),
  ('welding-basics','defects-quality',4),
  ('welding-basics','fabrication-careers',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='welding-basics' and lesson_id not in ('what-welding','safety','equipment-electrodes','joints-positions','defects-quality','fabrication-careers');
-- Course: Auto Mechanics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('auto-mechanics','Auto Mechanics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='auto-mechanics';
insert into public.course_keys(course,qid,answer,why) values
  ('auto-mechanics','q1',1,'Suck, squeeze, bang, blow.'),
  ('auto-mechanics','q2',3,'High compression ratios.'),
  ('auto-mechanics','q3',0,'π/4 x 8.6² x 8.6 x 4.'),
  ('auto-mechanics','q4',2,'(500 + 55) / 55.'),
  ('auto-mechanics','q5',2,'Wait until cool.'),
  ('auto-mechanics','q6',0,'Replace on schedule.'),
  ('auto-mechanics','q7',3,'12.0 V means discharged.'),
  ('auto-mechanics','q8',1,'From the alternator.'),
  ('auto-mechanics','q9',0,'Confirm with measurements.'),
  ('auto-mechanics','q10',2,'Do not drive.'),
  ('auto-mechanics','q11',1,'Aspect ratio.'),
  ('auto-mechanics','q12',3,'40 / 500 x 100.'),
  ('auto-mechanics','q13',3,'Jacks can slip.'),
  ('auto-mechanics','q14',1,'Only trained technicians.');
insert into public.course_lessons(course,lesson_id,position) values
  ('auto-mechanics','engine',0),
  ('auto-mechanics','systems',1),
  ('auto-mechanics','electrical',2),
  ('auto-mechanics','drivetrain-brakes',3),
  ('auto-mechanics','maintenance',4),
  ('auto-mechanics','future-careers',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='auto-mechanics' and lesson_id not in ('engine','systems','electrical','drivetrain-brakes','maintenance','future-careers');
