-- 0029: Ace Academy courses added this round (marketing-fundamentals sales-negotiation business-law-basics agile-scrum leadership-management business-communication retail-trade-management import-export-basics). Idempotent: safe to run again.
-- Course: Marketing Fundamentals. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('marketing-fundamentals','Marketing Fundamentals','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='marketing-fundamentals';
insert into public.course_keys(course,qid,answer,why) values
  ('marketing-fundamentals','q1',1,'People is one of the extra service Ps.'),
  ('marketing-fundamentals','q2',3,'Then you target and position.'),
  ('marketing-fundamentals','q3',0,'It concerns attitudes and lifestyle.'),
  ('marketing-fundamentals','q4',2,'2 000 000 x 0.3 x 500.'),
  ('marketing-fundamentals','q5',2,'Primary research collects new data.'),
  ('marketing-fundamentals','q6',0,'40 x 1.5.'),
  ('marketing-fundamentals','q7',3,'20 / 60.'),
  ('marketing-fundamentals','q8',1,'12 000 / 20.'),
  ('marketing-fundamentals','q9',0,'Skimming starts high.'),
  ('marketing-fundamentals','q10',2,'10 000 x 0.02.'),
  ('marketing-fundamentals','q11',1,'20 000 / 200.'),
  ('marketing-fundamentals','q12',3,'Attribution guides spending.'),
  ('marketing-fundamentals','q13',3,'Loyalty raises lifetime value.'),
  ('marketing-fundamentals','q14',1,'Hidden fees mislead customers.');
insert into public.course_lessons(course,lesson_id,position) values
  ('marketing-fundamentals','marketing-concept',0),
  ('marketing-fundamentals','stp',1),
  ('marketing-fundamentals','research-customers',2),
  ('marketing-fundamentals','pricing',3),
  ('marketing-fundamentals','promotion-digital',4),
  ('marketing-fundamentals','brand-loyalty',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='marketing-fundamentals' and lesson_id not in ('marketing-concept','stp','research-customers','pricing','promotion-digital','brand-loyalty');
-- Course: Sales and Negotiation Skills. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('sales-negotiation','Sales and Negotiation Skills','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='sales-negotiation';
insert into public.course_keys(course,qid,answer,why) values
  ('sales-negotiation','q1',1,'Listen first, then solve.'),
  ('sales-negotiation','q2',3,'It avoids wasting time on unlikely buyers.'),
  ('sales-negotiation','q3',0,'200 x 0.2 x 0.25.'),
  ('sales-negotiation','q4',2,'15 / 0.25 / 0.2.'),
  ('sales-negotiation','q5',2,'30 000 + 6000 + 1000.'),
  ('sales-negotiation','q6',0,'It explores the consequences.'),
  ('sales-negotiation','q7',3,'Benefits sell; features explain.'),
  ('sales-negotiation','q8',1,'Understand before responding.'),
  ('sales-negotiation','q9',0,'30 / 20 = 1.5.'),
  ('sales-negotiation','q10',2,'It gives you walk-away power.'),
  ('sales-negotiation','q11',1,'The overlap of acceptable prices.'),
  ('sales-negotiation','q12',3,'Give something only to get something.'),
  ('sales-negotiation','q13',3,'Return to discovery.'),
  ('sales-negotiation','q14',1,'Hidden fees mislead customers.');
insert into public.course_lessons(course,lesson_id,position) values
  ('sales-negotiation','sales-process',0),
  ('sales-negotiation','pipeline',1),
  ('sales-negotiation','discovery-presenting',2),
  ('sales-negotiation','objections',3),
  ('sales-negotiation','negotiation',4),
  ('sales-negotiation','closing-ethics',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='sales-negotiation' and lesson_id not in ('sales-process','pipeline','discovery-presenting','objections','negotiation','closing-ethics');
-- Course: Business Law Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('business-law-basics','Business Law Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='business-law-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('business-law-basics','q1',1,'Shareholders risk only their investment.'),
  ('business-law-basics','q2',3,'The shortfall can fall on the owner.'),
  ('business-law-basics','q3',0,'The director promises to pay personally.'),
  ('business-law-basics','q4',2,'Companies and Intellectual Property Commission.'),
  ('business-law-basics','q5',2,'CAC.'),
  ('business-law-basics','q6',0,'1000 x 0.15.'),
  ('business-law-basics','q7',3,'1150 x 15 / 115.'),
  ('business-law-basics','q8',1,'Pay-as-you-earn.'),
  ('business-law-basics','q9',0,'Spending it causes serious problems.'),
  ('business-law-basics','q10',2,'Trademarks identify the source of goods or services.'),
  ('business-law-basics','q11',1,'No registration is usually needed.'),
  ('business-law-basics','q12',3,'Keep it confidential.'),
  ('business-law-basics','q13',3,'Data minimisation and lawful purpose.'),
  ('business-law-basics','q14',1,'An arbitrator decides; a mediator facilitates.');
insert into public.course_lessons(course,lesson_id,position) values
  ('business-law-basics','business-structures',0),
  ('business-law-basics','registration-compliance',1),
  ('business-law-basics','tax-basics',2),
  ('business-law-basics','employment-consumer',3),
  ('business-law-basics','intellectual-property',4),
  ('business-law-basics','data-disputes',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='business-law-basics' and lesson_id not in ('business-structures','registration-compliance','tax-basics','employment-consumer','intellectual-property','data-disputes');
-- Course: Agile and Scrum Essentials. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('agile-scrum','Agile and Scrum Essentials','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='agile-scrum';
insert into public.course_keys(course,qid,answer,why) values
  ('agile-scrum','q1',1,'Agile values adaptation.'),
  ('agile-scrum','q2',3,'The product owner maximises value.'),
  ('agile-scrum','q3',0,'It is a short daily check.'),
  ('agile-scrum','q4',2,'Inspect the product and adapt.'),
  ('agile-scrum','q5',2,'It focuses on process.'),
  ('agile-scrum','q6',0,'It states user, need and benefit.'),
  ('agile-scrum','q7',3,'Epics are broken down.'),
  ('agile-scrum','q8',1,'72 / 3.'),
  ('agile-scrum','q9',0,'120 / 24.'),
  ('agile-scrum','q10',2,'40 - 28.'),
  ('agile-scrum','q11',1,'Less WIP shortens cycle time.'),
  ('agile-scrum','q12',3,'12 / 3.'),
  ('agile-scrum','q13',3,'Points are team-relative.'),
  ('agile-scrum','q14',1,'Hidden defects build up.');
insert into public.course_lessons(course,lesson_id,position) values
  ('agile-scrum','agile-mindset',0),
  ('agile-scrum','scrum-framework',1),
  ('agile-scrum','backlog-stories',2),
  ('agile-scrum','estimation-velocity',3),
  ('agile-scrum','kanban-flow',4),
  ('agile-scrum','retros-scaling',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='agile-scrum' and lesson_id not in ('agile-mindset','scrum-framework','backlog-stories','estimation-velocity','kanban-flow','retros-scaling');
-- Course: Leadership and Management Essentials. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('leadership-management','Leadership and Management Essentials','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='leadership-management';
insert into public.course_keys(course,qid,answer,why) values
  ('leadership-management','q1',1,'Plan, organise, lead, control.'),
  ('leadership-management','q2',3,'48 / 6.'),
  ('leadership-management','q3',0,'Clear fast instructions are needed.'),
  ('leadership-management','q4',2,'Adapt to the person and task.'),
  ('leadership-management','q5',2,'Hygiene factors only prevent dissatisfaction.'),
  ('leadership-management','q6',0,'Effort, performance and reward must link.'),
  ('leadership-management','q7',3,'4 + 1.8 + 1.4.'),
  ('leadership-management','q8',1,'3 + 2.7 + 1.6.'),
  ('leadership-management','q9',0,'Responsibility needs authority.'),
  ('leadership-management','q10',2,'12 x 50.'),
  ('leadership-management','q11',1,'Conflict emerges, then norms form.'),
  ('leadership-management','q12',3,'Safety enables learning.'),
  ('leadership-management','q13',3,'Visible progress reduces resistance.'),
  ('leadership-management','q14',1,'Integrity sets the example.');
insert into public.course_lessons(course,lesson_id,position) values
  ('leadership-management','management-basics',0),
  ('leadership-management','leadership-styles',1),
  ('leadership-management','motivation',2),
  ('leadership-management','decisions-delegation',3),
  ('leadership-management','teams-conflict',4),
  ('leadership-management','change-ethics',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='leadership-management' and lesson_id not in ('management-basics','leadership-styles','motivation','decisions-delegation','teams-conflict','change-ethics');
-- Course: Business Communication Skills. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('business-communication','Business Communication Skills','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='business-communication';
insert into public.course_keys(course,qid,answer,why) values
  ('business-communication','q1',1,'Audience, purpose and action guide the message.'),
  ('business-communication','q2',3,'1200 / 240.'),
  ('business-communication','q3',0,'5 x 50.'),
  ('business-communication','q4',2,'Main point first.'),
  ('business-communication','q5',2,'It says what and when.'),
  ('business-communication','q6',0,'Tone and listening matter.'),
  ('business-communication','q7',3,'It summarises the finished findings.'),
  ('business-communication','q8',1,'Lead with the reader''s needs.'),
  ('business-communication','q9',0,'8 x 300 x 1.5.'),
  ('business-communication','q10',2,'Minutes drive follow-up.'),
  ('business-communication','q11',1,'Situation, behaviour, impact.'),
  ('business-communication','q12',3,'Understand before responding.'),
  ('business-communication','q13',3,'Idioms translate poorly.'),
  ('business-communication','q14',1,'Summaries reveal misunderstandings.');
insert into public.course_lessons(course,lesson_id,position) values
  ('business-communication','principles',0),
  ('business-communication','writing',1),
  ('business-communication','reports-proposals',2),
  ('business-communication','meetings',3),
  ('business-communication','presenting-feedback',4),
  ('business-communication','cross-cultural',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='business-communication' and lesson_id not in ('principles','writing','reports-proposals','meetings','presenting-feedback','cross-cultural');
-- Course: Retail and Trade Management. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('retail-trade-management','Retail and Trade Management','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='retail-trade-management';
insert into public.course_keys(course,qid,answer,why) values
  ('retail-trade-management','q1',1,'Convenience is its selling point.'),
  ('retail-trade-management','q2',3,'It increases exposure to other items.'),
  ('retail-trade-management','q3',0,'50 / 100.'),
  ('retail-trade-management','q4',2,'50 / 150.'),
  ('retail-trade-management','q5',2,'120 - 100.'),
  ('retail-trade-management','q6',0,'2 000 000 x 0.015.'),
  ('retail-trade-management','q7',3,'Errors are easiest to fix immediately.'),
  ('retail-trade-management','q8',1,'600 000 / 150 000.'),
  ('retail-trade-management','q9',0,'80 / 100.'),
  ('retail-trade-management','q10',2,'300 / 1200.'),
  ('retail-trade-management','q11',1,'300 x 300.'),
  ('retail-trade-management','q12',3,'1200 x 0.3 x 300.'),
  ('retail-trade-management','q13',3,'Reconcile daily.'),
  ('retail-trade-management','q14',1,'Fake confirmations are a common scam.');
insert into public.course_lessons(course,lesson_id,position) values
  ('retail-trade-management','retail-basics',0),
  ('retail-trade-management','merchandising',1),
  ('retail-trade-management','pricing-margins',2),
  ('retail-trade-management','stock-control',3),
  ('retail-trade-management','sales-service',4),
  ('retail-trade-management','cash-digital',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='retail-trade-management' and lesson_id not in ('retail-basics','merchandising','pricing-margins','stock-control','sales-service','cash-digital');
-- Course: Import and Export Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('import-export-basics','Import and Export Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='import-export-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('import-export-basics','q1',1,'A continental free trade area.'),
  ('import-export-basics','q2',3,'Goods must originate in member countries.'),
  ('import-export-basics','q3',0,'Harmonized System codes.'),
  ('import-export-basics','q4',2,'The seller''s duty ends once goods are on board.'),
  ('import-export-basics','q5',2,'10 000 + 1200 + 150.'),
  ('import-export-basics','q6',0,'11 350 x 0.2.'),
  ('import-export-basics','q7',3,'13 620 x 0.15.'),
  ('import-export-basics','q8',1,'25 x 1.3.'),
  ('import-export-basics','q9',0,'The exporter is paid before shipping.'),
  ('import-export-basics','q10',2,'Banks check documents strictly.'),
  ('import-export-basics','q11',1,'10 000 x 19.'),
  ('import-export-basics','q12',3,'It removes currency uncertainty.'),
  ('import-export-basics','q13',3,'Needed for preferential duties.'),
  ('import-export-basics','q14',1,'Payment-diversion fraud is common.');
insert into public.course_lessons(course,lesson_id,position) values
  ('import-export-basics','why-trade',0),
  ('import-export-basics','markets-classification',1),
  ('import-export-basics','incoterms-costing',2),
  ('import-export-basics','payments-finance',3),
  ('import-export-basics','documents-customs',4),
  ('import-export-basics','risks-compliance',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='import-export-basics' and lesson_id not in ('why-trade','markets-classification','incoterms-costing','payments-finance','documents-customs','risks-compliance');
