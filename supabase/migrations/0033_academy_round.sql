-- 0033: Ace Academy courses added this round (history-skills world-religions-ethics creative-writing translation-basics introduction-linguistics african-literature journalism-basics beginner-french beginner-spanish beginner-arabic beginner-swahili). Idempotent: safe to run again.
-- Course: History Skills. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('history-skills','History Skills','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='history-skills';
insert into public.course_keys(course,qid,answer,why) values
  ('history-skills','q1',1,'History is based on evidence.'),
  ('history-skills','q2',3,'The 1600s are the 17th century.'),
  ('history-skills','q3',0,'The 19th century ends with 1900.'),
  ('history-skills','q4',2,'There is no year 0.'),
  ('history-skills','q5',2,'1960 - 1884.'),
  ('history-skills','q6',0,'Created at the time.'),
  ('history-skills','q7',3,'It interprets the past.'),
  ('history-skills','q8',1,'Origin of the source.'),
  ('history-skills','q9',0,'Bias is evidence too.'),
  ('history-skills','q10',2,'Epics, genealogies and praise poetry.'),
  ('history-skills','q11',1,'Respect for participants.'),
  ('history-skills','q12',3,'Short-term catalyst.'),
  ('history-skills','q13',3,'History of history writing.'),
  ('history-skills','q14',1,'Point, evidence, explanation.');
insert into public.course_lessons(course,lesson_id,position) values
  ('history-skills','what-is-history',0),
  ('history-skills','chronology',1),
  ('history-skills','sources',2),
  ('history-skills','oral-history',3),
  ('history-skills','interpretation',4),
  ('history-skills','writing-history',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='history-skills' and lesson_id not in ('what-is-history','chronology','sources','oral-history','interpretation','writing-history');
-- Course: World Religions and Ethics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('world-religions-ethics','World Religions and Ethics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='world-religions-ethics';
insert into public.course_keys(course,qid,answer,why) values
  ('world-religions-ethics','q1',1,'Fair, accurate description.'),
  ('world-religions-ethics','q2',3,'Ancestors remain part of the community.'),
  ('world-religions-ethics','q3',0,'Names differ by people.'),
  ('world-religions-ethics','q4',2,'Community and mutual responsibility.'),
  ('world-religions-ethics','q5',2,'One God in three persons.'),
  ('world-religions-ethics','q6',0,'Shahada, salat, zakat, sawm, hajj.'),
  ('world-religions-ethics','q7',3,'Hebrew scripture.'),
  ('world-religions-ethics','q8',1,'Key idea in Hinduism and Buddhism.'),
  ('world-religions-ethics','q9',0,'Teachings of the Buddha.'),
  ('world-religions-ethics','q10',2,'Open to all.'),
  ('world-religions-ethics','q11',1,'Outcomes matter most.'),
  ('world-religions-ethics','q12',3,'Character-centred.'),
  ('world-religions-ethics','q13',3,'A regional human-rights treaty.'),
  ('world-religions-ethics','q14',1,'Understanding and cooperation.');
insert into public.course_lessons(course,lesson_id,position) values
  ('world-religions-ethics','studying-religion',0),
  ('world-religions-ethics','african-traditional',1),
  ('world-religions-ethics','abrahamic',2),
  ('world-religions-ethics','dharmic-other',3),
  ('world-religions-ethics','ethical-theories',4),
  ('world-religions-ethics','applied-dialogue',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='world-religions-ethics' and lesson_id not in ('studying-religion','african-traditional','abrahamic','dharmic-other','ethical-theories','applied-dialogue');
-- Course: Creative Writing. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('creative-writing','Creative Writing','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='creative-writing';
insert into public.course_keys(course,qid,answer,why) values
  ('creative-writing','q1',1,'"What if" questions spark plots.'),
  ('creative-writing','q2',3,'500 x 3.'),
  ('creative-writing','q3',0,'Desire and conflict drive interest.'),
  ('creative-writing','q4',2,'Action reveals feeling.'),
  ('creative-writing','q5',2,'Overused comparisons lose power.'),
  ('creative-writing','q6',0,'It launches the plot.'),
  ('creative-writing','q7',3,'The turning point.'),
  ('creative-writing','q8',1,'Because and therefore.'),
  ('creative-writing','q9',0,'The narrator is a character.'),
  ('creative-writing','q10',2,'Keeps speakers clear.'),
  ('creative-writing','q11',1,'5 + 7 + 5.'),
  ('creative-writing','q12',3,'Often 8 + 6.'),
  ('creative-writing','q13',3,'Fix structure before sentences.'),
  ('creative-writing','q14',1,'Copyright arises automatically in most countries.');
insert into public.course_lessons(course,lesson_id,position) values
  ('creative-writing','ideas-habits',0),
  ('creative-writing','character',1),
  ('creative-writing','show-setting',2),
  ('creative-writing','plot-structure',3),
  ('creative-writing','dialogue-voice',4),
  ('creative-writing','poetry-editing',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='creative-writing' and lesson_id not in ('ideas-habits','character','show-setting','plot-structure','dialogue-voice','poetry-editing');
-- Course: Translation and Interpreting Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('translation-basics','Translation and Interpreting Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='translation-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('translation-basics','q1',1,'Translation is written.'),
  ('translation-basics','q2',3,'Produces natural text.'),
  ('translation-basics','q3',0,'Translate the idiom''s meaning.'),
  ('translation-basics','q4',2,'A false friend.'),
  ('translation-basics','q5',2,'Useful for marketing and literature.'),
  ('translation-basics','q6',0,'Know purpose and audience.'),
  ('translation-basics','q7',3,'10 000 / 2500.'),
  ('translation-basics','q8',1,'2500 x 0.8.'),
  ('translation-basics','q9',0,'Reuse saves time and ensures consistency.'),
  ('translation-basics','q10',2,'Post-editing is needed.'),
  ('translation-basics','q11',1,'Real-time rendering.'),
  ('translation-basics','q12',3,'Fatigue reduces accuracy.'),
  ('translation-basics','q13',3,'Keeps communication direct.'),
  ('translation-basics','q14',1,'Protect client information.');
insert into public.course_lessons(course,lesson_id,position) values
  ('translation-basics','what-is-translation',0),
  ('translation-basics','meaning-equivalence',1),
  ('translation-basics','process',2),
  ('translation-basics','tools',3),
  ('translation-basics','interpreting',4),
  ('translation-basics','ethics-career',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='translation-basics' and lesson_id not in ('what-is-translation','meaning-equivalence','process','tools','interpreting','ethics-career');
-- Course: Introduction to Linguistics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('introduction-linguistics','Introduction to Linguistics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='introduction-linguistics';
insert into public.course_keys(course,qid,answer,why) values
  ('introduction-linguistics','q1',1,'It describes how language works.'),
  ('introduction-linguistics','q2',3,'International Phonetic Alphabet.'),
  ('introduction-linguistics','q3',0,'Vocal-cord vibration.'),
  ('introduction-linguistics','q4',2,'Written c, q and x.'),
  ('introduction-linguistics','q5',2,'Tone is part of the word.'),
  ('introduction-linguistics','q6',0,'They differ in one sound.'),
  ('introduction-linguistics','q7',3,'un + happy + ness.'),
  ('introduction-linguistics','q8',1,'ni + na + ku + penda.'),
  ('introduction-linguistics','q9',0,'m- (singular) versus wa- (plural).'),
  ('introduction-linguistics','q10',2,'Subject, verb, object.'),
  ('introduction-linguistics','q11',1,'Two possible structures.'),
  ('introduction-linguistics','q12',3,'A type of a broader category.'),
  ('introduction-linguistics','q13',3,'Meaning in context.'),
  ('introduction-linguistics','q14',1,'Africa''s largest family.');
insert into public.course_lessons(course,lesson_id,position) values
  ('introduction-linguistics','what-is-linguistics',0),
  ('introduction-linguistics','sounds',1),
  ('introduction-linguistics','words',2),
  ('introduction-linguistics','sentences',3),
  ('introduction-linguistics','meaning',4),
  ('introduction-linguistics','society-change',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='introduction-linguistics' and lesson_id not in ('what-is-linguistics','sounds','words','sentences','meaning','society-change');
-- Course: African Literature. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('african-literature','African Literature','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='african-literature';
insert into public.course_keys(course,qid,answer,why) values
  ('african-literature','q1',1,'Griots (jeliw) are oral historians.'),
  ('african-literature','q2',3,'Izibongo is Zulu and Xhosa praise poetry.'),
  ('african-literature','q3',0,'Published in 1958.'),
  ('african-literature','q4',2,'Celebrated Black identity in French.'),
  ('african-literature','q5',2,'Uganda, 1966.'),
  ('african-literature','q6',0,'Nigerian playwright and poet.'),
  ('african-literature','q7',3,'Disillusionment after independence.'),
  ('african-literature','q8',1,'An epistolary novel.'),
  ('african-literature','q9',0,'Set in Rhodesia (Zimbabwe).'),
  ('african-literature','q10',2,'By Chimamanda Ngozi Adichie.'),
  ('african-literature','q11',1,'He turned to Gĩkũyũ.'),
  ('african-literature','q12',3,'Born in Zanzibar.'),
  ('african-literature','q13',3,'A landmark of magical realism.'),
  ('african-literature','q14',1,'Analysis over summary.');
insert into public.course_lessons(course,lesson_id,position) values
  ('african-literature','oral-roots',0),
  ('african-literature','colonialism-response',1),
  ('african-literature','independence-disillusionment',2),
  ('african-literature','gender-voices',3),
  ('african-literature','language-debate',4),
  ('african-literature','reading-critically',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='african-literature' and lesson_id not in ('oral-roots','colonialism-response','independence-disillusionment','gender-voices','language-debate','reading-critically');
-- Course: Journalism Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('journalism-basics','Journalism Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='journalism-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('journalism-basics','q1',1,'Recent events matter more.'),
  ('journalism-basics','q2',3,'Readers must know it is a view.'),
  ('journalism-basics','q3',0,'Right of reply.'),
  ('journalism-basics','q4',2,'Invites detailed answers.'),
  ('journalism-basics','q5',2,'Readers get essentials quickly.'),
  ('journalism-basics','q6',0,'The key facts.'),
  ('journalism-basics','q7',3,'4 / 8.'),
  ('journalism-basics','q8',1,'30 / 120.'),
  ('journalism-basics','q9',0,'300 / 1 500 000 x 100 000.'),
  ('journalism-basics','q10',2,'Verification tool.'),
  ('journalism-basics','q11',1,'Misinformation is shared by mistake.'),
  ('journalism-basics','q12',3,'Avoid conflicts of interest.'),
  ('journalism-basics','q13',3,'Truth is a common defence.'),
  ('journalism-basics','q14',1,'Digital safety protects sources.');
insert into public.course_lessons(course,lesson_id,position) values
  ('journalism-basics','news-values',0),
  ('journalism-basics','reporting-interviewing',1),
  ('journalism-basics','writing-news',2),
  ('journalism-basics','verification',3),
  ('journalism-basics','ethics-law',4),
  ('journalism-basics','digital-data',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='journalism-basics' and lesson_id not in ('news-values','reporting-interviewing','writing-news','verification','ethics-law','digital-data');
-- Course: Beginner French. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('beginner-french','Beginner French','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='beginner-french';
insert into public.course_keys(course,qid,answer,why) values
  ('beginner-french','q1',1,'Bonjour is used during the day.'),
  ('beginner-french','q2',3,'Vous shows respect.'),
  ('beginner-french','q3',0,'s''appeler = to be called.'),
  ('beginner-french','q4',2,'Quatorze is 14.'),
  ('beginner-french','q5',2,'Four twenties.'),
  ('beginner-french','q6',0,'Sixty-ten.'),
  ('beginner-french','q7',3,'La maison.'),
  ('beginner-french','q8',1,'Adjective after the noun.'),
  ('beginner-french','q9',0,'Nous sommes.'),
  ('beginner-french','q10',2,'French uses avoir for age.'),
  ('beginner-french','q11',1,'Vous ending -ez.'),
  ('beginner-french','q12',3,'ne… pas around the verb.'),
  ('beginner-french','q13',3,'Combien = how much.'),
  ('beginner-french','q14',1,'Lundi, mardi, mercredi…');
insert into public.course_lessons(course,lesson_id,position) values
  ('beginner-french','greetings',0),
  ('beginner-french','pronunciation-numbers',1),
  ('beginner-french','nouns-articles',2),
  ('beginner-french','verbs',3),
  ('beginner-french','questions-negation',4),
  ('beginner-french','everyday-french',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='beginner-french' and lesson_id not in ('greetings','pronunciation-numbers','nouns-articles','verbs','questions-negation','everyday-french');
-- Course: Beginner Spanish. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('beginner-spanish','Beginner Spanish','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='beginner-spanish';
insert into public.course_keys(course,qid,answer,why) values
  ('beginner-spanish','q1',1,'Buenas noches is good evening or night.'),
  ('beginner-spanish','q2',3,'Spanish, French and Portuguese are official there.'),
  ('beginner-spanish','q3',0,'llamarse = to be called.'),
  ('beginner-spanish','q4',2,'Hola sounds like ola.'),
  ('beginner-spanish','q5',2,'Catorce is 14.'),
  ('beginner-spanish','q6',0,'Las casas.'),
  ('beginner-spanish','q7',3,'Adjective after the noun.'),
  ('beginner-spanish','q8',1,'A temporary state uses estar.'),
  ('beginner-spanish','q9',0,'Profession uses ser.'),
  ('beginner-spanish','q10',2,'-amos ending.'),
  ('beginner-spanish','q11',1,'Spanish uses tener for age.'),
  ('beginner-spanish','q12',3,'No before the verb.'),
  ('beginner-spanish','q13',3,'Cuánto = how much.'),
  ('beginner-spanish','q14',1,'Telling the time.');
insert into public.course_lessons(course,lesson_id,position) values
  ('beginner-spanish','greetings',0),
  ('beginner-spanish','pronunciation-numbers',1),
  ('beginner-spanish','nouns-articles',2),
  ('beginner-spanish','ser-estar-verbs',3),
  ('beginner-spanish','questions-negation',4),
  ('beginner-spanish','everyday-spanish',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='beginner-spanish' and lesson_id not in ('greetings','pronunciation-numbers','nouns-articles','ser-estar-verbs','questions-negation','everyday-spanish');
-- Course: Beginner Arabic. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('beginner-arabic','Beginner Arabic','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='beginner-arabic';
insert into public.course_keys(course,qid,answer,why) values
  ('beginner-arabic','q1',1,'Digits still run left to right.'),
  ('beginner-arabic','q2',3,'All consonants or long vowels.'),
  ('beginner-arabic','q3',0,'al-fuṣḥā.'),
  ('beginner-arabic','q4',2,'And upon you peace.'),
  ('beginner-arabic','q5',2,'ʿAfwan means you''re welcome.'),
  ('beginner-arabic','q6',0,'ism = name; -ī = my.'),
  ('beginner-arabic','q7',3,'Alif, wāw and yāʾ write long vowels.'),
  ('beginner-arabic','q8',1,'Shadda doubles consonants.'),
  ('beginner-arabic','q9',0,'No verb "to be" is needed.'),
  ('beginner-arabic','q10',2,'ṭāliba is a female student.'),
  ('beginner-arabic','q11',1,'Sun letters assimilate the l.'),
  ('beginner-arabic','q12',3,'1 wāḥid … 5 khamsa.'),
  ('beginner-arabic','q13',3,'Digits run left to right.'),
  ('beginner-arabic','q14',1,'ayna al-masjid? Where is the mosque?');
insert into public.course_lessons(course,lesson_id,position) values
  ('beginner-arabic','about-arabic',0),
  ('beginner-arabic','letters-sounds',1),
  ('beginner-arabic','greetings',2),
  ('beginner-arabic','pronouns-sentences',3),
  ('beginner-arabic','numbers',4),
  ('beginner-arabic','everyday',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='beginner-arabic' and lesson_id not in ('about-arabic','letters-sounds','greetings','pronouns-sentences','numbers','everyday');
-- Course: Beginner Swahili. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('beginner-swahili','Beginner Swahili','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='beginner-swahili';
insert into public.course_keys(course,qid,answer,why) values
  ('beginner-swahili','q1',1,'Also the East African Community.'),
  ('beginner-swahili','q2',3,'Nzuri means good.'),
  ('beginner-swahili','q3',0,'The elder replies Marahaba.'),
  ('beginner-swahili','q4',2,'Karibu means welcome.'),
  ('beginner-swahili','q5',2,'ki-TA-bu.'),
  ('beginner-swahili','q6',0,'Ten and five.'),
  ('beginner-swahili','q7',3,'KI-VI class.'),
  ('beginner-swahili','q8',1,'M-WA class for people.'),
  ('beginner-swahili','q9',0,'Adjective takes the class prefix.'),
  ('beginner-swahili','q10',2,'ni (I) + na (present) + soma.'),
  ('beginner-swahili','q11',1,'nitasoma = I will read.'),
  ('beginner-swahili','q12',3,'ku = you (object).'),
  ('beginner-swahili','q13',3,'Swahili time counts from about 6 a.m.'),
  ('beginner-swahili','q14',1,'Jumatatu is Monday.');
insert into public.course_lessons(course,lesson_id,position) values
  ('beginner-swahili','about-swahili',0),
  ('beginner-swahili','pronunciation-numbers',1),
  ('beginner-swahili','noun-classes',2),
  ('beginner-swahili','verbs',3),
  ('beginner-swahili','time-days',4),
  ('beginner-swahili','everyday',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='beginner-swahili' and lesson_id not in ('about-swahili','pronunciation-numbers','noun-classes','verbs','time-days','everyday');
