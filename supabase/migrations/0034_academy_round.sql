-- 0034: Ace Academy courses added this round (sociology-basics political-science human-geography development-economics anthropology-intro international-relations social-work-basics research-methods). Idempotent: safe to run again.
-- Course: Sociology Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('sociology-basics','Sociology Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='sociology-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('sociology-basics','q1',1,'C. Wright Mills''s idea.'),
  ('sociology-basics','q2',3,'Associated with Durkheim.'),
  ('sociology-basics','q3',0,'Meaning is created in interaction.'),
  ('sociology-basics','q4',2,'Family, school, peers, media.'),
  ('sociology-basics','q5',2,'Relativism seeks understanding in context.'),
  ('sociology-basics','q6',0,'Small, close and lasting.'),
  ('sociology-basics','q7',3,'Such as work versus family.'),
  ('sociology-basics','q8',1,'300 / 1200.'),
  ('sociology-basics','q9',0,'1 means one person has everything.'),
  ('sociology-basics','q10',2,'Disadvantages combine.'),
  ('sociology-basics','q11',1,'Labels shape identity.'),
  ('sociology-basics','q12',3,'Repair rather than punishment alone.'),
  ('sociology-basics','q13',3,'0.45 x 60 million.'),
  ('sociology-basics','q14',1,'Organised systems meeting social needs.');
insert into public.course_lessons(course,lesson_id,position) values
  ('sociology-basics','sociological-imagination',0),
  ('sociology-basics','culture-socialisation',1),
  ('sociology-basics','structure-institutions',2),
  ('sociology-basics','inequality',3),
  ('sociology-basics','deviance-control',4),
  ('sociology-basics','social-change',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='sociology-basics' and lesson_id not in ('sociological-imagination','culture-socialisation','structure-institutions','inequality','deviance-control','social-change');
-- Course: Introduction to Political Science. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('political-science','Introduction to Political Science','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='political-science';
insert into public.course_keys(course,qid,answer,why) values
  ('political-science','q1',1,'Legitimate power.'),
  ('political-science','q2',3,'Sources of legitimacy.'),
  ('political-science','q3',0,'Weber''s definition.'),
  ('political-science','q4',2,'Associated with Nkrumah and the AU.'),
  ('political-science','q5',2,'Courts resolve disputes.'),
  ('political-science','q6',0,'Fixed term and separate powers.'),
  ('political-science','q7',3,'A parliamentary feature.'),
  ('political-science','q8',1,'Devolved government.'),
  ('political-science','q9',0,'Plurality rule.'),
  ('political-science','q10',2,'Proportional allocation.'),
  ('political-science','q11',1,'Seats: A 2, B 2, C 1.'),
  ('political-science','q12',3,'12 / 20.'),
  ('political-science','q13',3,'Public opinion across Africa.'),
  ('political-science','q14',1,'Accountability institutions.');
insert into public.course_lessons(course,lesson_id,position) values
  ('political-science','power-state',0),
  ('political-science','ideologies',1),
  ('political-science','systems-government',2),
  ('political-science','elections',3),
  ('political-science','participation',4),
  ('political-science','democracy-governance',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='political-science' and lesson_id not in ('power-state','ideologies','systems-government','elections','participation','democracy-governance');
-- Course: Human Geography. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('human-geography','Human Geography','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='human-geography';
insert into public.course_keys(course,qid,answer,why) values
  ('human-geography','q1',1,'4 x 0.5 km.'),
  ('human-geography','q2',3,'27 per 1000.'),
  ('human-geography','q3',0,'70 / 2.7.'),
  ('human-geography','q4',2,'30 000 000 / 300 000.'),
  ('human-geography','q5',2,'43 / 57 x 100.'),
  ('human-geography','q6',0,'Many children.'),
  ('human-geography','q7',3,'It pushes people to leave.'),
  ('human-geography','q8',1,'A major income source.'),
  ('human-geography','q9',0,'Urban transport.'),
  ('human-geography','q10',2,'Extracting resources.'),
  ('human-geography','q11',1,'Services.'),
  ('human-geography','q12',3,'A broad development measure.'),
  ('human-geography','q13',3,'12 + 8 + 6.'),
  ('human-geography','q14',1,'Brundtland definition.');
insert into public.course_lessons(course,lesson_id,position) values
  ('human-geography','what-is-human-geography',0),
  ('human-geography','population',1),
  ('human-geography','migration',2),
  ('human-geography','urbanisation',3),
  ('human-geography','economic-geography',4),
  ('human-geography','resources-environment',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='human-geography' and lesson_id not in ('what-is-human-geography','population','migration','urbanisation','economic-geography','resources-environment');
-- Course: Development Economics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('development-economics','Development Economics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='development-economics';
insert into public.course_keys(course,qid,answer,why) values
  ('development-economics','q1',1,'450 000 000 000 / 50 000 000.'),
  ('development-economics','q2',3,'A dollar buys different amounts.'),
  ('development-economics','q3',0,'9 - 6.'),
  ('development-economics','q4',2,'5 - 2.7.'),
  ('development-economics','q5',2,'70 / 7.'),
  ('development-economics','q6',0,'70 / 2.'),
  ('development-economics','q7',3,'Solow''s insight.'),
  ('development-economics','q8',1,'From low to high productivity.'),
  ('development-economics','q9',0,'Self-reinforcing disadvantage.'),
  ('development-economics','q10',2,'A broad development measure.'),
  ('development-economics','q11',1,'4 x 8, ignoring compounding.'),
  ('development-economics','q12',3,'Banerjee, Duflo and Kremer.'),
  ('development-economics','q13',3,'Acemoglu and Robinson''s argument.'),
  ('development-economics','q14',1,'Diversification reduces risk.');
insert into public.course_lessons(course,lesson_id,position) values
  ('development-economics','measuring',0),
  ('development-economics','growth',1),
  ('development-economics','poverty-inequality',2),
  ('development-economics','human-capital',3),
  ('development-economics','agriculture-structural',4),
  ('development-economics','institutions-aid-trade',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='development-economics' and lesson_id not in ('measuring','growth','poverty-inequality','human-capital','agriculture-structural','institutions-aid-trade');
-- Course: Introduction to Anthropology. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('anthropology-intro','Introduction to Anthropology','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='anthropology-intro';
insert into public.course_keys(course,qid,answer,why) values
  ('anthropology-intro','q1',1,'Connecting parts of life across societies.'),
  ('anthropology-intro','q2',3,'Cultural, biological, archaeology, linguistic.'),
  ('anthropology-intro','q3',0,'Living among and observing people.'),
  ('anthropology-intro','q4',2,'Etic uses outside categories.'),
  ('anthropology-intro','q5',2,'Self-awareness in research.'),
  ('anthropology-intro','q6',0,'Belonging through the mother''s line.'),
  ('anthropology-intro','q7',3,'Gifts from the groom''s family.'),
  ('anthropology-intro','q8',1,'No exact return expected.'),
  ('anthropology-intro','q9',0,'The Gift.'),
  ('anthropology-intro','q10',2,'The in-between stage.'),
  ('anthropology-intro','q11',1,'A coherent explanatory system.'),
  ('anthropology-intro','q12',3,'About 3.2 million years old.'),
  ('anthropology-intro','q13',3,'Found in Morocco.'),
  ('anthropology-intro','q14',1,'Humans originated there.');
insert into public.course_lessons(course,lesson_id,position) values
  ('anthropology-intro','what-is-anthropology',0),
  ('anthropology-intro','fieldwork',1),
  ('anthropology-intro','kinship-family',2),
  ('anthropology-intro','economy-exchange',3),
  ('anthropology-intro','ritual-belief',4),
  ('anthropology-intro','human-origins',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='anthropology-intro' and lesson_id not in ('what-is-anthropology','fieldwork','kinship-family','economy-exchange','ritual-belief','human-origins');
-- Course: International Relations. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('international-relations','International Relations','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='international-relations';
insert into public.course_keys(course,qid,answer,why) values
  ('international-relations','q1',1,'Member states form IGOs.'),
  ('international-relations','q2',3,'Origins of the state system.'),
  ('international-relations','q3',0,'No world government.'),
  ('international-relations','q4',2,'Norms shape interests.'),
  ('international-relations','q5',2,'Each has one General Assembly vote.'),
  ('international-relations','q6',0,'China, France, Russia, UK, US.'),
  ('international-relations','q7',3,'15 members minus 5 permanent.'),
  ('international-relations','q8',1,'Successor to the OAU.'),
  ('international-relations','q9',0,'15 - 3.'),
  ('international-relations','q10',2,'People-centred security.'),
  ('international-relations','q11',1,'The ICC prosecutes individuals.'),
  ('international-relations','q12',3,'Protect people in war.'),
  ('international-relations','q13',3,'Often with policy conditions.'),
  ('international-relations','q14',1,'Complements hard power.');
insert into public.course_lessons(course,lesson_id,position) values
  ('international-relations','what-is-ir',0),
  ('international-relations','theories',1),
  ('international-relations','organisations',2),
  ('international-relations','conflict-security',3),
  ('international-relations','law-rights',4),
  ('international-relations','political-economy-diplomacy',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='international-relations' and lesson_id not in ('what-is-ir','theories','organisations','conflict-security','law-rights','political-economy-diplomacy');
-- Course: Social Work Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('social-work-basics','Social Work Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='social-work-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('social-work-basics','q1',1,'Dignity and worth.'),
  ('social-work-basics','q2',3,'Respecting autonomy.'),
  ('social-work-basics','q3',0,'Genograms show family trees.'),
  ('social-work-basics','q4',2,'Goals are set with clients.'),
  ('social-work-basics','q5',2,'Identify strengths as well as needs.'),
  ('social-work-basics','q6',0,'Active listening.'),
  ('social-work-basics','q7',3,'30 x 45 / 60.'),
  ('social-work-basics','q8',1,'Accurate, timely records.'),
  ('social-work-basics','q9',0,'Unmet basic needs.'),
  ('social-work-basics','q10',2,'Family-based care is preferred.'),
  ('social-work-basics','q11',1,'6 x 4.'),
  ('social-work-basics','q12',3,'Participation builds sustainability.'),
  ('social-work-basics','q13',3,'120 / 30.'),
  ('social-work-basics','q14',1,'Reflective practice.');
insert into public.course_lessons(course,lesson_id,position) values
  ('social-work-basics','values-ethics',0),
  ('social-work-basics','helping-process',1),
  ('social-work-basics','communication-skills',2),
  ('social-work-basics','children-families',3),
  ('social-work-basics','groups-communities',4),
  ('social-work-basics','policy-selfcare',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='social-work-basics' and lesson_id not in ('values-ethics','helping-process','communication-skills','children-families','groups-communities','policy-selfcare');
-- Course: Research Methods for the Social Sciences. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('research-methods','Research Methods for the Social Sciences','university',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='research-methods';
insert into public.course_keys(course,qid,answer,why) values
  ('research-methods','q1',1,'The question guides the method.'),
  ('research-methods','q2',3,'The presumed cause.'),
  ('research-methods','q3',0,'Turning concepts into measures.'),
  ('research-methods','q4',2,'Random selection.'),
  ('research-methods','q5',2,'1.96² x 0.25 / 0.05².'),
  ('research-methods','q6',0,'Smaller margins need bigger samples.'),
  ('research-methods','q7',3,'385 / 0.7.'),
  ('research-methods','q8',1,'Asks two things at once.'),
  ('research-methods','q9',0,'Explores shared views.'),
  ('research-methods','q10',2,'The first step towards themes.'),
  ('research-methods','q11',1,'Quantitative then qualitative.'),
  ('research-methods','q12',3,'45 / 80.'),
  ('research-methods','q13',3,'Protects participants.'),
  ('research-methods','q14',1,'Voluntary, informed participation.');
insert into public.course_lessons(course,lesson_id,position) values
  ('research-methods','designing-research',0),
  ('research-methods','quantitative',1),
  ('research-methods','qualitative',2),
  ('research-methods','mixed-methods',3),
  ('research-methods','analysis',4),
  ('research-methods','ethics-writing',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='research-methods' and lesson_id not in ('designing-research','quantitative','qualitative','mixed-methods','analysis','ethics-writing');
