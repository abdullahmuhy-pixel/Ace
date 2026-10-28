-- 0032: Ace Academy courses added this round (early-childhood-education inclusive-education curriculum-design educational-technology classroom-assessment online-tutoring educational-leadership). Idempotent: safe to run again.
-- Course: Early Childhood Education. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('early-childhood-education','Early Childhood Education','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='early-childhood-education';
insert into public.course_keys(course,qid,answer,why) values
  ('early-childhood-education','q1',1,'Including the early primary years.'),
  ('early-childhood-education','q2',3,'Small muscle control.'),
  ('early-childhood-education','q3',0,'Children develop at different speeds.'),
  ('early-childhood-education','q4',2,'Adult supports a learning goal.'),
  ('early-childhood-education','q5',2,'Open questions extend thinking.'),
  ('early-childhood-education','q6',0,'Strong first language helps.'),
  ('early-childhood-education','q7',3,'A foundation for reading.'),
  ('early-childhood-education','q8',1,'5 x 4.'),
  ('early-childhood-education','q9',0,'30 / 10.'),
  ('early-childhood-education','q10',2,'26 / 8 = 3.25, rounded up.'),
  ('early-childhood-education','q11',1,'Record facts, not judgements.'),
  ('early-childhood-education','q12',3,'Shows progress over time.'),
  ('early-childhood-education','q13',3,'Partnership with families matters.'),
  ('early-childhood-education','q14',1,'Every child has the right to participate.');
insert into public.course_lessons(course,lesson_id,position) values
  ('early-childhood-education','why-early-years',0),
  ('early-childhood-education','play-based-learning',1),
  ('early-childhood-education','literacy-numeracy',2),
  ('early-childhood-education','health-safety',3),
  ('early-childhood-education','observation-assessment',4),
  ('early-childhood-education','families-communities',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='early-childhood-education' and lesson_id not in ('why-early-years','play-based-learning','literacy-numeracy','health-safety','observation-assessment','families-communities');
-- Course: Inclusive and Special Needs Education. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('inclusive-education','Inclusive and Special Needs Education','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='inclusive-education';
insert into public.course_keys(course,qid,answer,why) values
  ('inclusive-education','q1',1,'A right under the UNCRPD.'),
  ('inclusive-education','q2',3,'Nearly 240 million children.'),
  ('inclusive-education','q3',0,'40 / 10.'),
  ('inclusive-education','q4',2,'Barriers disable people.'),
  ('inclusive-education','q5',2,'A specific learning difficulty.'),
  ('inclusive-education','q6',0,'Sensory issues are common and fixable.'),
  ('inclusive-education','q7',3,'Different ways to take in information.'),
  ('inclusive-education','q8',1,'How learning is shown.'),
  ('inclusive-education','q9',0,'120 x 1.25.'),
  ('inclusive-education','q10',2,'90 x 1.25.'),
  ('inclusive-education','q11',1,'Fair access to the same assessment.'),
  ('inclusive-education','q12',3,'Specific and measurable.'),
  ('inclusive-education','q13',3,'Find the reason and teach alternatives.'),
  ('inclusive-education','q14',1,'It helps access to text.');
insert into public.course_lessons(course,lesson_id,position) values
  ('inclusive-education','rights-models',0),
  ('inclusive-education','understanding-needs',1),
  ('inclusive-education','udl',2),
  ('inclusive-education','differentiation',3),
  ('inclusive-education','iep-collaboration',4),
  ('inclusive-education','behaviour-technology',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='inclusive-education' and lesson_id not in ('rights-models','understanding-needs','udl','differentiation','iep-collaboration','behaviour-technology');
-- Course: Curriculum Design. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('curriculum-design','Curriculum Design','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='curriculum-design';
insert into public.course_keys(course,qid,answer,why) values
  ('curriculum-design','q1',1,'Not in official documents.'),
  ('curriculum-design','q2',3,'Different from what was intended.'),
  ('curriculum-design','q3',0,'Observable actions can be assessed.'),
  ('curriculum-design','q4',2,'Producing something new.'),
  ('curriculum-design','q5',2,'Evaluation.'),
  ('curriculum-design','q6',0,'Start with the end goals.'),
  ('curriculum-design','q7',3,'Coherence between parts.'),
  ('curriculum-design','q8',1,'Revisiting builds understanding.'),
  ('curriculum-design','q9',0,'4 x 40 x 40.'),
  ('curriculum-design','q10',2,'6400 / 60.'),
  ('curriculum-design','q11',1,'28 + 24 + 18.'),
  ('curriculum-design','q12',3,'Assessment for learning.'),
  ('curriculum-design','q13',3,'Clear criteria improve work.'),
  ('curriculum-design','q14',1,'Relevance motivates.');
insert into public.course_lessons(course,lesson_id,position) values
  ('curriculum-design','what-is-curriculum',0),
  ('curriculum-design','aims-outcomes',1),
  ('curriculum-design','backward-design',2),
  ('curriculum-design','sequencing-time',3),
  ('curriculum-design','assessment-alignment',4),
  ('curriculum-design','relevance-review',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='curriculum-design' and lesson_id not in ('what-is-curriculum','aims-outcomes','backward-design','sequencing-time','assessment-alignment','relevance-review');
-- Course: Educational Technology. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('educational-technology','Educational Technology','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='educational-technology';
insert into public.course_keys(course,qid,answer,why) values
  ('educational-technology','q1',1,'Purpose first.'),
  ('educational-technology','q2',3,'The highest level.'),
  ('educational-technology','q3',0,'A direct replacement.'),
  ('educational-technology','q4',2,'Radio is cheap and widespread.'),
  ('educational-technology','q5',2,'12 x 25.'),
  ('educational-technology','q6',0,'60 x 40 / 1000.'),
  ('educational-technology','q7',3,'30 / 40.'),
  ('educational-technology','q8',1,'Short, focused segments.'),
  ('educational-technology','q9',0,'Blended learning.'),
  ('educational-technology','q10',2,'Accessibility benefits many.'),
  ('educational-technology','q11',1,'Verify outputs.'),
  ('educational-technology','q12',3,'Use it as a tutor.'),
  ('educational-technology','q13',3,'Critical evaluation.'),
  ('educational-technology','q14',1,'Posts can be permanent.');
insert into public.course_lessons(course,lesson_id,position) values
  ('educational-technology','purpose-samr',0),
  ('educational-technology','low-tech-access',1),
  ('educational-technology','digital-tools',2),
  ('educational-technology','designing-digital-lessons',3),
  ('educational-technology','ai-in-education',4),
  ('educational-technology','digital-citizenship',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='educational-technology' and lesson_id not in ('purpose-samr','low-tech-access','digital-tools','designing-digital-lessons','ai-in-education','digital-citizenship');
-- Course: Classroom Assessment Methods. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('classroom-assessment','Classroom Assessment Methods','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='classroom-assessment';
insert into public.course_keys(course,qid,answer,why) values
  ('classroom-assessment','q1',1,'It guides teaching during learning.'),
  ('classroom-assessment','q2',3,'Assessment of learning.'),
  ('classroom-assessment','q3',0,'Quick formative evidence.'),
  ('classroom-assessment','q4',2,'Whole-class evidence.'),
  ('classroom-assessment','q5',2,'50 x 0.2.'),
  ('classroom-assessment','q6',0,'Plausible distractors diagnose misconceptions.'),
  ('classroom-assessment','q7',3,'Improves reliability.'),
  ('classroom-assessment','q8',1,'660 / 10.'),
  ('classroom-assessment','q9',0,'(61 + 67) / 2.'),
  ('classroom-assessment','q10',2,'18 / 30.'),
  ('classroom-assessment','q11',1,'0.9 - 0.3.'),
  ('classroom-assessment','q12',3,'Consistency is reliability.'),
  ('classroom-assessment','q13',3,'Reliability is consistency.'),
  ('classroom-assessment','q14',1,'Equal opportunity to show learning.');
insert into public.course_lessons(course,lesson_id,position) values
  ('classroom-assessment','purposes',0),
  ('classroom-assessment','formative-techniques',1),
  ('classroom-assessment','designing-tests',2),
  ('classroom-assessment','marking-rubrics',3),
  ('classroom-assessment','analysing-results',4),
  ('classroom-assessment','validity-fairness',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='classroom-assessment' and lesson_id not in ('purposes','formative-techniques','designing-tests','marking-rubrics','analysing-results','validity-fairness');
-- Course: Online Tutoring. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('online-tutoring','Online Tutoring','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='online-tutoring';
insert into public.course_keys(course,qid,answer,why) values
  ('online-tutoring','q1',1,'Learners must hear clearly.'),
  ('online-tutoring','q2',3,'0.5 x 60.'),
  ('online-tutoring','q3',0,'Set purpose early.'),
  ('online-tutoring','q4',2,'5 + 10 + 30 + 10 + 5.'),
  ('online-tutoring','q5',2,'Retrieval reveals understanding.'),
  ('online-tutoring','q6',0,'Active learning.'),
  ('online-tutoring','q7',3,'4 x 120.'),
  ('online-tutoring','q8',1,'Plan from evidence.'),
  ('online-tutoring','q9',0,'Safeguarding.'),
  ('online-tutoring','q10',2,'Support learning, do not cheat.'),
  ('online-tutoring','q11',1,'Privacy matters.'),
  ('online-tutoring','q12',3,'250 x 15 x 4.'),
  ('online-tutoring','q13',3,'15 000 x 0.8.'),
  ('online-tutoring','q14',1,'Trust spreads by word of mouth.');
insert into public.course_lessons(course,lesson_id,position) values
  ('online-tutoring','setting-up',0),
  ('online-tutoring','session-structure',1),
  ('online-tutoring','engagement',2),
  ('online-tutoring','assessment-feedback',3),
  ('online-tutoring','safeguarding',4),
  ('online-tutoring','tutoring-business',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='online-tutoring' and lesson_id not in ('setting-up','session-structure','engagement','assessment-feedback','safeguarding','tutoring-business');
-- Course: Educational Leadership. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('educational-leadership','Educational Leadership','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='educational-leadership';
insert into public.course_keys(course,qid,answer,why) values
  ('educational-leadership','q1',1,'Leaders shape teaching conditions.'),
  ('educational-leadership','q2',3,'Builds capacity.'),
  ('educational-leadership','q3',0,'Focus drives results.'),
  ('educational-leadership','q4',2,'70 - 62.'),
  ('educational-leadership','q5',2,'8 / 62.'),
  ('educational-leadership','q6',0,'Collaborative professional growth.'),
  ('educational-leadership','q7',3,'Manageable development steps.'),
  ('educational-leadership','q8',1,'1 200 000 / 800.'),
  ('educational-leadership','q9',0,'800 / 25.'),
  ('educational-leadership','q10',2,'800 - 736.'),
  ('educational-leadership','q11',1,'Inquiry, not blame.'),
  ('educational-leadership','q12',3,'Openness strengthens accountability.'),
  ('educational-leadership','q13',3,'Every decision serves learners.'),
  ('educational-leadership','q14',1,'Involve and support staff.');
insert into public.course_lessons(course,lesson_id,position) values
  ('educational-leadership','roles',0),
  ('educational-leadership','vision-planning',1),
  ('educational-leadership','leading-learning',2),
  ('educational-leadership','people-resources',3),
  ('educational-leadership','data-decisions',4),
  ('educational-leadership','community-ethics',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='educational-leadership' and lesson_id not in ('roles','vision-planning','leading-learning','people-resources','data-decisions','community-ethics');
