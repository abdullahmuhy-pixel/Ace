-- 0039: Ace Academy courses added this round (emotional-intelligence career-planning parenting-basics financial-literacy-teens memory-techniques). Idempotent: safe to run again.
-- Course: Emotional Intelligence. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('emotional-intelligence','Emotional Intelligence','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='emotional-intelligence';
insert into public.course_keys(course,qid,answer,why) values
  ('emotional-intelligence','q1',1,'It can be learned.'),
  ('emotional-intelligence','q2',3,'Also self-awareness, self-regulation, motivation and social skills.'),
  ('emotional-intelligence','q3',0,'Use them wisely.'),
  ('emotional-intelligence','q4',2,'Labelling helps.'),
  ('emotional-intelligence','q5',2,'Notice body cues.'),
  ('emotional-intelligence','q6',0,'Not hiding emotions.'),
  ('emotional-intelligence','q7',3,'Delay decisions.'),
  ('emotional-intelligence','q8',1,'Changes the emotional response.'),
  ('emotional-intelligence','q9',0,'Listen to understand.'),
  ('emotional-intelligence','q10',2,'Understanding is not agreement.'),
  ('emotional-intelligence','q11',1,'Describes your feeling and reason.'),
  ('emotional-intelligence','q12',3,'Decisions in anger go badly.'),
  ('emotional-intelligence','q13',3,'Disagree about ideas.'),
  ('emotional-intelligence','q14',1,'Small daily changes.');
insert into public.course_lessons(course,lesson_id,position) values
  ('emotional-intelligence','what-eq',0),
  ('emotional-intelligence','self-awareness',1),
  ('emotional-intelligence','self-regulation',2),
  ('emotional-intelligence','empathy',3),
  ('emotional-intelligence','relationships',4),
  ('emotional-intelligence','practice',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='emotional-intelligence' and lesson_id not in ('what-eq','self-awareness','self-regulation','empathy','relationships','practice');
-- Course: Career Planning. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('career-planning','Career Planning','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='career-planning';
insert into public.course_keys(course,qid,answer,why) values
  ('career-planning','q1',1,'Adjust as you grow.'),
  ('career-planning','q2',3,'Useful in many jobs.'),
  ('career-planning','q3',0,'Ideas, not rules.'),
  ('career-planning','q4',2,'Not asking for a job.'),
  ('career-planning','q5',2,'Trades and technical careers.'),
  ('career-planning','q6',0,'Avoid fake institutions.'),
  ('career-planning','q7',3,'12 000 / 12.'),
  ('career-planning','q8',1,'Specific, Measurable, Achievable, Relevant, Time-bound.'),
  ('career-planning','q9',0,'5 x 4 x 12.'),
  ('career-planning','q10',2,'20 x 0.25.'),
  ('career-planning','q11',1,'Verify first.'),
  ('career-planning','q12',3,'Network actively.'),
  ('career-planning','q13',3,'Reduce risk.'),
  ('career-planning','q14',1,'Look after wellbeing.');
insert into public.course_lessons(course,lesson_id,position) values
  ('career-planning','self-assessment',0),
  ('career-planning','explore',1),
  ('career-planning','pathways',2),
  ('career-planning','goals',3),
  ('career-planning','job-search',4),
  ('career-planning','growth',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='career-planning' and lesson_id not in ('self-assessment','explore','pathways','goals','job-search','growth');
-- Course: Parenting Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('parenting-basics','Parenting Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='parenting-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('parenting-basics','q1',1,'Critical for brain development.'),
  ('parenting-basics','q2',3,'Part of development.'),
  ('parenting-basics','q3',0,'Secure attachment.'),
  ('parenting-basics','q4',2,'"You kept trying."'),
  ('parenting-basics','q5',2,'Cooking, walking, driving.'),
  ('parenting-basics','q6',0,'Discipline means teaching.'),
  ('parenting-basics','q7',3,'Say what to do.'),
  ('parenting-basics','q8',1,'Stay calm and consistent.'),
  ('parenting-basics','q9',0,'Then with suitable foods.'),
  ('parenting-basics','q10',2,'Prevent poisoning.'),
  ('parenting-basics','q11',1,'Supervise near water.'),
  ('parenting-basics','q12',3,'Less is better for young children.'),
  ('parenting-basics','q13',3,'Play builds many skills.'),
  ('parenting-basics','q14',1,'Act to protect the child.');
insert into public.course_lessons(course,lesson_id,position) values
  ('parenting-basics','development',0),
  ('parenting-basics','connection',1),
  ('parenting-basics','positive-discipline',2),
  ('parenting-basics','health-safety',3),
  ('parenting-basics','learning-play',4),
  ('parenting-basics','parent-wellbeing',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='parenting-basics' and lesson_id not in ('development','connection','positive-discipline','health-safety','learning-play','parent-wellbeing');
-- Course: Financial Literacy for Teens. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('financial-literacy-teens','Financial Literacy for Teens','secondary',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='financial-literacy-teens';
insert into public.course_keys(course,qid,answer,why) values
  ('financial-literacy-teens','q1',1,'Wants are nice to have.'),
  ('financial-literacy-teens','q2',3,'300 / 20.'),
  ('financial-literacy-teens','q3',0,'20% of R500.'),
  ('financial-literacy-teens','q4',2,'Saving becomes automatic.'),
  ('financial-literacy-teens','q5',2,'R240 a month x 12.'),
  ('financial-literacy-teens','q6',0,'50 x 52.'),
  ('financial-literacy-teens','q7',3,'Members contribute regularly.'),
  ('financial-literacy-teens','q8',1,'1000 x 1.1³.'),
  ('financial-literacy-teens','q9',0,'1000 x 1.2⁴.'),
  ('financial-literacy-teens','q10',2,'Including fees.'),
  ('financial-literacy-teens','q11',1,'Keep it secret.'),
  ('financial-literacy-teens','q12',3,'New money pays old members.'),
  ('financial-literacy-teens','q13',3,'Spreads risk.'),
  ('financial-literacy-teens','q14',1,'Risk and return go together.');
insert into public.course_lessons(course,lesson_id,position) values
  ('financial-literacy-teens','money-basics',0),
  ('financial-literacy-teens','budgeting',1),
  ('financial-literacy-teens','saving-goals',2),
  ('financial-literacy-teens','interest-borrowing',3),
  ('financial-literacy-teens','digital-money',4),
  ('financial-literacy-teens','future',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='financial-literacy-teens' and lesson_id not in ('money-basics','budgeting','saving-goals','interest-borrowing','digital-money','future');
-- Course: Memory Techniques. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('memory-techniques','Memory Techniques','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='memory-techniques';
insert into public.course_keys(course,qid,answer,why) values
  ('memory-techniques','q1',1,'Take in, keep, bring back.'),
  ('memory-techniques','q2',3,'Newer research suggests about 4 chunks.'),
  ('memory-techniques','q3',0,'Ebbinghaus.'),
  ('memory-techniques','q4',2,'Creates false familiarity.'),
  ('memory-techniques','q5',2,'Testing yourself.'),
  ('memory-techniques','q6',0,'Reveals gaps.'),
  ('memory-techniques','q7',3,'Spreading reviews over time.'),
  ('memory-techniques','q8',1,'1 + 3 + 7 + 14 + 30.'),
  ('memory-techniques','q9',0,'Improves long-term learning.'),
  ('memory-techniques','q10',2,'Groups are easier to hold.'),
  ('memory-techniques','q11',1,'An acronym.'),
  ('memory-techniques','q12',3,'Method of loci.'),
  ('memory-techniques','q13',3,'Sleep consolidates memory.'),
  ('memory-techniques','q14',1,'Focused intervals.');
insert into public.course_lessons(course,lesson_id,position) values
  ('memory-techniques','how-memory',0),
  ('memory-techniques','active-recall',1),
  ('memory-techniques','spaced-repetition',2),
  ('memory-techniques','mnemonics',3),
  ('memory-techniques','memory-palace',4),
  ('memory-techniques','brain-health',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='memory-techniques' and lesson_id not in ('how-memory','active-recall','spaced-repetition','mnemonics','memory-palace','brain-health');
