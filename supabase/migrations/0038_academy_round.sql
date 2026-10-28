-- 0038: Ace Academy courses added this round (video-editing music-production fashion-design-basics content-creation podcasting animation-basics interior-design-intro). Idempotent: safe to run again.
-- Course: Video Editing. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('video-editing','Video Editing','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='video-editing';
insert into public.course_keys(course,qid,answer,why) values
  ('video-editing','q1',1,'Viewers feel it rather than notice it.'),
  ('video-editing','q2',3,'The hook.'),
  ('video-editing','q3',0,'Portrait frame.'),
  ('video-editing','q4',2,'25 x 60.'),
  ('video-editing','q5',2,'8 x 600 / 8.'),
  ('video-editing','q6',0,'Avoid losing work.'),
  ('video-editing','q7',3,'They also hide edits.'),
  ('video-editing','q8',1,'The shape of the letter J.'),
  ('video-editing','q9',0,'Avoids looking like a mistake.'),
  ('video-editing','q10',2,'Peak around -6 dB.'),
  ('video-editing','q11',1,'Use licensed music.'),
  ('video-editing','q12',3,'Grading creates a style.'),
  ('video-editing','q13',3,'Inclusive and effective.'),
  ('video-editing','q14',1,'Check sound and spelling.');
insert into public.course_lessons(course,lesson_id,position) values
  ('video-editing','storytelling',0),
  ('video-editing','setup',1),
  ('video-editing','cutting',2),
  ('video-editing','sound',3),
  ('video-editing','colour-graphics',4),
  ('video-editing','export-career',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='video-editing' and lesson_id not in ('storytelling','setup','cutting','sound','colour-graphics','export-career');
-- Course: Music Production. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('music-production','Music Production','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='music-production';
insert into public.course_keys(course,qid,answer,why) values
  ('music-production','q1',1,'60 / 120.'),
  ('music-production','q2',3,'2 s per bar.'),
  ('music-production','q3',0,'Digital audio workstation.'),
  ('music-production','q4',2,'44 100 x 16 x 2.'),
  ('music-production','q5',2,'Less sensitive.'),
  ('music-production','q6',0,'Natural groove.'),
  ('music-production','q7',3,'Avoid copyright claims.'),
  ('music-production','q8',1,'Breath blasts.'),
  ('music-production','q9',0,'Composite take.'),
  ('music-production','q10',2,'Anchor the mix.'),
  ('music-production','q11',1,'Evens out loud and quiet.'),
  ('music-production','q12',3,'10 log₁₀ 2.'),
  ('music-production','q13',3,'Prevents disputes.'),
  ('music-production','q14',1,'Such as SAMRO, MCSK or COSON.');
insert into public.course_lessons(course,lesson_id,position) values
  ('music-production','foundations',0),
  ('music-production','daw',1),
  ('music-production','beats-arrangement',2),
  ('music-production','recording',3),
  ('music-production','mixing',4),
  ('music-production','release-business',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='music-production' and lesson_id not in ('foundations','daw','beats-arrangement','recording','mixing','release-business');
-- Course: Fashion Design Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('fashion-design-basics','Fashion Design Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='fashion-design-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('fashion-design-basics','q1',1,'Woven strips.'),
  ('fashion-design-basics','q2',3,'Cultural respect.'),
  ('fashion-design-basics','q3',0,'Such as A-line.'),
  ('fashion-design-basics','q4',2,'Lead the eye up and down.'),
  ('fashion-design-basics','q5',2,'Natural and absorbent.'),
  ('fashion-design-basics','q6',0,'At 45° to the grain.'),
  ('fashion-design-basics','q7',3,'4 x 1.5.'),
  ('fashion-design-basics','q8',1,'Added to body measurements.'),
  ('fashion-design-basics','q9',0,'92 + 6.'),
  ('fashion-design-basics','q10',2,'Test fit first.'),
  ('fashion-design-basics','q11',1,'For ready-to-wear.'),
  ('fashion-design-basics','q12',3,'Flat seams.'),
  ('fashion-design-basics','q13',3,'300 x 1.5.'),
  ('fashion-design-basics','q14',1,'20 x R150.');
insert into public.course_lessons(course,lesson_id,position) values
  ('fashion-design-basics','fashion-world',0),
  ('fashion-design-basics','elements-principles',1),
  ('fashion-design-basics','textiles',2),
  ('fashion-design-basics','measure-pattern',3),
  ('fashion-design-basics','construction',4),
  ('fashion-design-basics','business',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='fashion-design-basics' and lesson_id not in ('fashion-world','elements-principles','textiles','measure-pattern','construction','business');
-- Course: Content Creation. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('content-creation','Content Creation','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='content-creation';
insert into public.course_keys(course,qid,answer,why) values
  ('content-creation','q1',1,'Focus attracts the right audience.'),
  ('content-creation','q2',3,'Reels, TikTok, Shorts.'),
  ('content-creation','q3',0,'Direct contact.'),
  ('content-creation','q4',2,'Viewers decide fast.'),
  ('content-creation','q5',2,'Sound matters.'),
  ('content-creation','q6',0,'Keep ideas flowing.'),
  ('content-creation','q7',3,'450 / 10 000.'),
  ('content-creation','q8',1,'30 / 1200.'),
  ('content-creation','q9',0,'Check retention.'),
  ('content-creation','q10',2,'Per sale.'),
  ('content-creation','q11',1,'100 x R150.'),
  ('content-creation','q12',3,'Required and builds trust.'),
  ('content-creation','q13',3,'Respect dignity and privacy.'),
  ('content-creation','q14',1,'Creators are targets.');
insert into public.course_lessons(course,lesson_id,position) values
  ('content-creation','foundations',0),
  ('content-creation','platforms',1),
  ('content-creation','creating',2),
  ('content-creation','consistency-analytics',3),
  ('content-creation','monetisation',4),
  ('content-creation','ethics-safety',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='content-creation' and lesson_id not in ('foundations','platforms','creating','consistency-analytics','monetisation','ethics-safety');
-- Course: Podcasting. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('podcasting','Podcasting','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='podcasting';
insert into public.course_keys(course,qid,answer,why) values
  ('podcasting','q1',1,'Regular publishing.'),
  ('podcasting','q2',3,'Test the concept''s depth.'),
  ('podcasting','q3',0,'Less sensitive to the room.'),
  ('podcasting','q4',2,'Less echo.'),
  ('podcasting','q5',2,'150 x 30.'),
  ('podcasting','q6',0,'Open questions.'),
  ('podcasting','q7',3,'Written consent.'),
  ('podcasting','q8',1,'Platform recommendation.'),
  ('podcasting','q9',0,'128 x 1800 / 8.'),
  ('podcasting','q10',2,'Submit once.'),
  ('podcasting','q11',1,'Build habit.'),
  ('podcasting','q12',3,'300 / 2000.'),
  ('podcasting','q13',3,'Can lead to lawsuits.'),
  ('podcasting','q14',1,'Sustainable production.');
insert into public.course_lessons(course,lesson_id,position) values
  ('podcasting','planning',0),
  ('podcasting','equipment',1),
  ('podcasting','hosting-interviews',2),
  ('podcasting','editing',3),
  ('podcasting','publishing',4),
  ('podcasting','business-ethics',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='podcasting' and lesson_id not in ('planning','equipment','hosting-interviews','editing','publishing','business-ethics');
-- Course: Animation Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('animation-basics','Animation Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='animation-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('animation-basics','q1',1,'Persistence of vision.'),
  ('animation-basics','q2',3,'Real objects.'),
  ('animation-basics','q3',0,'24 x 10.'),
  ('animation-basics','q4',2,'Each drawing held two frames.'),
  ('animation-basics','q5',2,'Keys.'),
  ('animation-basics','q6',0,'Spacing controls speed.'),
  ('animation-basics','q7',3,'Preparing for action.'),
  ('animation-basics','q8',1,'Parts keep moving.'),
  ('animation-basics','q9',0,'Curved paths.'),
  ('animation-basics','q10',2,'Tests pacing.'),
  ('animation-basics','q11',1,'So mouths match dialogue.'),
  ('animation-basics','q12',3,'12 x 30.'),
  ('animation-basics','q13',3,'Modelling to rendering.'),
  ('animation-basics','q14',1,'Judge spacing.');
insert into public.course_lessons(course,lesson_id,position) values
  ('animation-basics','what-animation',0),
  ('animation-basics','frames-timing',1),
  ('animation-basics','principles',2),
  ('animation-basics','pipeline',3),
  ('animation-basics','tools',4),
  ('animation-basics','portfolio-careers',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='animation-basics' and lesson_id not in ('what-animation','frames-timing','principles','pipeline','tools','portfolio-careers');
-- Course: Interior Design Introduction. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('interior-design-intro','Interior Design Introduction','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='interior-design-intro';
insert into public.course_keys(course,qid,answer,why) values
  ('interior-design-intro','q1',1,'Function and feeling.'),
  ('interior-design-intro','q2',3,'Draw the eye upward.'),
  ('interior-design-intro','q3',0,'4 x 3.5.'),
  ('interior-design-intro','q4',2,'Less feels cramped.'),
  ('interior-design-intro','q5',2,'Efficient cooking.'),
  ('interior-design-intro','q6',0,'Reflect more light.'),
  ('interior-design-intro','q7',3,'A small pop of colour.'),
  ('interior-design-intro','q8',1,'37 x 2 / 10.'),
  ('interior-design-intro','q9',0,'Allow for cutting.'),
  ('interior-design-intro','q10',2,'For activities.'),
  ('interior-design-intro','q11',1,'300 x 14.'),
  ('interior-design-intro','q12',3,'Cosy feel.'),
  ('interior-design-intro','q13',3,'For surprises.'),
  ('interior-design-intro','q14',1,'Fewer harmful fumes.');
insert into public.course_lessons(course,lesson_id,position) values
  ('interior-design-intro','what-interior',0),
  ('interior-design-intro','elements-principles',1),
  ('interior-design-intro','space-planning',2),
  ('interior-design-intro','colour-materials',3),
  ('interior-design-intro','lighting',4),
  ('interior-design-intro','budget-practice',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='interior-design-intro' and lesson_id not in ('what-interior','elements-principles','space-planning','colour-materials','lighting','budget-practice');
