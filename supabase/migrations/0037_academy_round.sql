-- 0037: Ace Academy courses added this round (constitutional-law-basics human-rights criminal-law-basics public-administration procurement-basics legal-research). Idempotent: safe to run again.
-- Course: Constitutional Law Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('constitutional-law-basics','Constitutional Law Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='constitutional-law-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('constitutional-law-basics','q1',1,'It sets up institutions and protects rights.'),
  ('constitutional-law-basics','q2',3,'The constitution prevails.'),
  ('constitutional-law-basics','q3',0,'The courts.'),
  ('constitutional-law-basics','q4',2,'Parliament.'),
  ('constitutional-law-basics','q5',2,'Prevents abuse of power.'),
  ('constitutional-law-basics','q6',0,'Often realised progressively.'),
  ('constitutional-law-basics','q7',3,'The limitation test.'),
  ('constitutional-law-basics','q8',1,'Courts check other branches.'),
  ('constitutional-law-basics','q9',0,'Ordering a fresh poll.'),
  ('constitutional-law-basics','q10',2,'Power shared with states.'),
  ('constitutional-law-basics','q11',1,'Devolution.'),
  ('constitutional-law-basics','q12',3,'2/3 x 400.'),
  ('constitutional-law-basics','q13',3,'Public interest litigation.'),
  ('constitutional-law-basics','q14',1,'Adopted by the AU.');
insert into public.course_lessons(course,lesson_id,position) values
  ('constitutional-law-basics','what-constitution',0),
  ('constitutional-law-basics','separation-powers',1),
  ('constitutional-law-basics','bill-of-rights',2),
  ('constitutional-law-basics','courts-review',3),
  ('constitutional-law-basics','structure-amend',4),
  ('constitutional-law-basics','citizenship-participation',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='constitutional-law-basics' and lesson_id not in ('what-constitution','separation-powers','bill-of-rights','courts-review','structure-amend','citizenship-participation');
-- Course: Human Rights. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('human-rights','Human Rights','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='human-rights';
insert into public.course_keys(course,qid,answer,why) values
  ('human-rights','q1',1,'Because they are human.'),
  ('human-rights','q2',3,'By the UN General Assembly.'),
  ('human-rights','q3',0,'Health depends on water and food.'),
  ('human-rights','q4',2,'Adopted in 1966.'),
  ('human-rights','q5',2,'By the Human Rights Council.'),
  ('human-rights','q6',0,'Adopted in 1981.'),
  ('human-rights','q7',3,'Tanzania.'),
  ('human-rights','q8',1,'Adopted in 2003.'),
  ('human-rights','q9',0,'Community and duties.'),
  ('human-rights','q10',2,'Non-derogable.'),
  ('human-rights','q11',1,'Key refugee principle.'),
  ('human-rights','q12',3,'AU convention.'),
  ('human-rights','q13',3,'Exhaustion of local remedies.'),
  ('human-rights','q14',1,'Protect, respect, remedy.');
insert into public.course_lessons(course,lesson_id,position) values
  ('human-rights','what-rights',0),
  ('human-rights','international-system',1),
  ('human-rights','african-system',2),
  ('human-rights','key-rights',3),
  ('human-rights','vulnerable-groups',4),
  ('human-rights','remedies-advocacy',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='human-rights' and lesson_id not in ('what-rights','international-system','african-system','key-rights','vulnerable-groups','remedies-advocacy');
-- Course: Criminal Law Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('criminal-law-basics','Criminal Law Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='criminal-law-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('criminal-law-basics','q1',1,'Civil law: private disputes.'),
  ('criminal-law-basics','q2',3,'Laws must be knowable in advance.'),
  ('criminal-law-basics','q3',0,'The guilty act.'),
  ('criminal-law-basics','q4',2,'The guilty mind.'),
  ('criminal-law-basics','q5',2,'Such as a parent''s duty.'),
  ('criminal-law-basics','q6',0,'Repelling an unlawful attack.'),
  ('criminal-law-basics','q7',3,'Lack of capacity.'),
  ('criminal-law-basics','q8',1,'An incomplete crime.'),
  ('criminal-law-basics','q9',0,'More serious than theft.'),
  ('criminal-law-basics','q10',2,'A high standard.'),
  ('criminal-law-basics','q11',1,'Varies by country.'),
  ('criminal-law-basics','q12',3,'Release pending trial.'),
  ('criminal-law-basics','q13',3,'Fair trial rights.'),
  ('criminal-law-basics','q14',1,'Often for children.');
insert into public.course_lessons(course,lesson_id,position) values
  ('criminal-law-basics','purpose',0),
  ('criminal-law-basics','elements',1),
  ('criminal-law-basics','defences',2),
  ('criminal-law-basics','parties-attempts',3),
  ('criminal-law-basics','procedure',4),
  ('criminal-law-basics','sentencing-justice',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='criminal-law-basics' and lesson_id not in ('purpose','elements','defences','parties-attempts','procedure','sentencing-justice');
-- Course: Public Administration. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('public-administration','Public Administration','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='public-administration';
insert into public.course_keys(course,qid,answer,why) values
  ('public-administration','q1',1,'Implementation and management.'),
  ('public-administration','q2',3,'Different accountability.'),
  ('public-administration','q3',0,'Predictability and fairness.'),
  ('public-administration','q4',2,'From the 1980s.'),
  ('public-administration','q5',2,'A problem gains attention.'),
  ('public-administration','q6',0,'96 / 120.'),
  ('public-administration','q7',3,'Outcomes are results like fewer deaths.'),
  ('public-administration','q8',1,'Financial accountability.'),
  ('public-administration','q9',0,'40 / 500.'),
  ('public-administration','q10',2,'300 / 1500.'),
  ('public-administration','q11',1,'Like Kenya''s counties.'),
  ('public-administration','q12',3,'Citizens monitor services.'),
  ('public-administration','q13',3,'Diverts resources.'),
  ('public-administration','q14',1,'30 / 40.');
insert into public.course_lessons(course,lesson_id,position) values
  ('public-administration','what-pa',0),
  ('public-administration','theories',1),
  ('public-administration','policy-cycle',2),
  ('public-administration','finance-hr',3),
  ('public-administration','local-gov',4),
  ('public-administration','accountability-digital',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='public-administration' and lesson_id not in ('what-pa','theories','policy-cycle','finance-hr','local-gov','accountability-digital');
-- Course: Procurement Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('procurement-basics','Procurement Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='procurement-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('procurement-basics','q1',1,'Not simply cheapest.'),
  ('procurement-basics','q2',3,'Allows competition.'),
  ('procurement-basics','q3',0,'Advertised publicly.'),
  ('procurement-basics','q4',2,'Avoids competition.'),
  ('procurement-basics','q5',2,'High risk of abuse.'),
  ('procurement-basics','q6',0,'Fairness.'),
  ('procurement-basics','q7',3,'80 x 0.9.'),
  ('procurement-basics','q8',1,'80 x 0.75.'),
  ('procurement-basics','q9',0,'59.5 + 21.'),
  ('procurement-basics','q10',2,'Whole-life cost.'),
  ('procurement-basics','q11',1,'A red flag.'),
  ('procurement-basics','q12',3,'Investigate.'),
  ('procurement-basics','q13',3,'Integrity.'),
  ('procurement-basics','q14',1,'Submit on time.');
insert into public.course_lessons(course,lesson_id,position) values
  ('procurement-basics','what-procurement',0),
  ('procurement-basics','cycle-planning',1),
  ('procurement-basics','methods',2),
  ('procurement-basics','evaluation',3),
  ('procurement-basics','contracts',4),
  ('procurement-basics','integrity',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='procurement-basics' and lesson_id not in ('what-procurement','cycle-planning','methods','evaluation','contracts','integrity');
-- Course: Legal Research. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('legal-research','Legal Research','university',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='legal-research';
insert into public.course_keys(course,qid,answer,why) values
  ('legal-research','q1',1,'Top of the hierarchy.'),
  ('legal-research','q2',3,'Made under authority of an act.'),
  ('legal-research','q3',0,'Such as South Africa and Namibia.'),
  ('legal-research','q4',2,'Check against primary sources.'),
  ('legal-research','q5',2,'Legal Information Institutes.'),
  ('legal-research','q6',0,'Laws change over time.'),
  ('legal-research','q7',3,'Necessary for the decision.'),
  ('legal-research','q8',1,'Persuasive only.'),
  ('legal-research','q9',0,'Material differences.'),
  ('legal-research','q10',2,'Most authoritative first.'),
  ('legal-research','q11',1,'Issue, Rule, Application, Conclusion.'),
  ('legal-research','q12',3,'Busy readers need it first.'),
  ('legal-research','q13',3,'Check every authority.'),
  ('legal-research','q14',1,'Duty not to mislead the court.');
insert into public.course_lessons(course,lesson_id,position) values
  ('legal-research','sources',0),
  ('legal-research','finding-legislation',1),
  ('legal-research','reading-cases',2),
  ('legal-research','research-process',3),
  ('legal-research','writing-irac',4),
  ('legal-research','ethics-tools',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='legal-research' and lesson_id not in ('sources','finding-legislation','reading-cases','research-process','writing-irac','ethics-tools');
