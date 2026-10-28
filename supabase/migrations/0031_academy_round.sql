-- 0031: Ace Academy courses added this round (nursing-fundamentals pharmacology-basics nutrition-dietetics mental-health-awareness medical-terminology maternal-child-health infection-prevention-control health-records-informatics). Idempotent: safe to run again.
-- Course: Nursing Fundamentals. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('nursing-fundamentals','Nursing Fundamentals','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='nursing-fundamentals';
insert into public.course_keys(course,qid,answer,why) values
  ('nursing-fundamentals','q1',1,'Collect information first.'),
  ('nursing-fundamentals','q2',3,'Patients decide about their own care.'),
  ('nursing-fundamentals','q3',0,'18 x 4.'),
  ('nursing-fundamentals','q4',2,'Count without the patient noticing.'),
  ('nursing-fundamentals','q5',2,'(120 + 160) / 3.'),
  ('nursing-fundamentals','q6',0,'Lower values need assessment.'),
  ('nursing-fundamentals','q7',3,'Clean hands before and after contact.'),
  ('nursing-fundamentals','q8',1,'For example name and date of birth.'),
  ('nursing-fundamentals','q9',0,'2400 - 1900.'),
  ('nursing-fundamentals','q10',2,'The others suggest overload.'),
  ('nursing-fundamentals','q11',1,'Plus medicine, dose, route, time and documentation.'),
  ('nursing-fundamentals','q12',3,'Never give a medicine you are unsure about.'),
  ('nursing-fundamentals','q13',3,'Situation, background, assessment, recommendation.'),
  ('nursing-fundamentals','q14',1,'Record promptly and accurately.');
insert into public.course_lessons(course,lesson_id,position) values
  ('nursing-fundamentals','role-ethics',0),
  ('nursing-fundamentals','vital-signs',1),
  ('nursing-fundamentals','hygiene-safety',2),
  ('nursing-fundamentals','fluid-balance',3),
  ('nursing-fundamentals','medicines',4),
  ('nursing-fundamentals','communication-documentation',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='nursing-fundamentals' and lesson_id not in ('role-ethics','vital-signs','hygiene-safety','fluid-balance','medicines','communication-documentation');
-- Course: Pharmacology Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('pharmacology-basics','Pharmacology Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='pharmacology-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('pharmacology-basics','q1',1,'Generic names describe the active ingredient.'),
  ('pharmacology-basics','q2',3,'Absorption, distribution, metabolism, excretion.'),
  ('pharmacology-basics','q3',0,'Liver enzymes change most drugs.'),
  ('pharmacology-basics','q4',2,'Four half-lives: 200, 100, 50, 25, 12.5.'),
  ('pharmacology-basics','q5',2,'About 97% after 5 half-lives.'),
  ('pharmacology-basics','q6',0,'Agonists activate receptors.'),
  ('pharmacology-basics','q7',3,'Small changes can cause toxicity.'),
  ('pharmacology-basics','q8',1,'Viruses are unaffected by antibiotics.'),
  ('pharmacology-basics','q9',0,'Misuse selects resistant microbes.'),
  ('pharmacology-basics','q10',2,'500 / 250.'),
  ('pharmacology-basics','q11',1,'375 / 250 x 5.'),
  ('pharmacology-basics','q12',3,'10 x 18.'),
  ('pharmacology-basics','q13',3,'1000 / 8.'),
  ('pharmacology-basics','q14',1,'Drug-herb interactions occur.');
insert into public.course_lessons(course,lesson_id,position) values
  ('pharmacology-basics','what-are-medicines',0),
  ('pharmacology-basics','pharmacokinetics',1),
  ('pharmacology-basics','pharmacodynamics',2),
  ('pharmacology-basics','drug-classes',3),
  ('pharmacology-basics','dose-calculations',4),
  ('pharmacology-basics','adverse-effects',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='pharmacology-basics' and lesson_id not in ('what-are-medicines','pharmacokinetics','pharmacodynamics','drug-classes','dose-calculations','adverse-effects');
-- Course: Nutrition and Dietetics Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('nutrition-dietetics','Nutrition and Dietetics Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='nutrition-dietetics';
insert into public.course_keys(course,qid,answer,why) values
  ('nutrition-dietetics','q1',1,'Carbohydrate and protein give about 4.'),
  ('nutrition-dietetics','q2',3,'240 + 80 + 135.'),
  ('nutrition-dietetics','q3',0,'135 / 455.'),
  ('nutrition-dietetics','q4',2,'Complementary plant proteins.'),
  ('nutrition-dietetics','q5',2,'0.8 x 60.'),
  ('nutrition-dietetics','q6',0,'Unsaturated fats support heart health.'),
  ('nutrition-dietetics','q7',3,'Iodine supports thyroid and brain development.'),
  ('nutrition-dietetics','q8',1,'Vitamin A supports vision.'),
  ('nutrition-dietetics','q9',0,'Then complementary foods with continued breastfeeding.'),
  ('nutrition-dietetics','q10',2,'About one teaspoon.'),
  ('nutrition-dietetics','q11',1,'Sodium x 2.5.'),
  ('nutrition-dietetics','q12',3,'70 / 3.0625.'),
  ('nutrition-dietetics','q13',3,'Mid-upper-arm circumference.'),
  ('nutrition-dietetics','q14',1,'Prevents cross-contamination.');
insert into public.course_lessons(course,lesson_id,position) values
  ('nutrition-dietetics','nutrients-energy',0),
  ('nutrition-dietetics','macronutrients',1),
  ('nutrition-dietetics','micronutrients',2),
  ('nutrition-dietetics','balanced-diets',3),
  ('nutrition-dietetics','assessment-disease',4),
  ('nutrition-dietetics','food-safety-careers',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='nutrition-dietetics' and lesson_id not in ('nutrients-energy','macronutrients','micronutrients','balanced-diets','assessment-disease','food-safety-careers');
-- Course: Mental Health Awareness. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('mental-health-awareness','Mental Health Awareness','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='mental-health-awareness';
insert into public.course_keys(course,qid,answer,why) values
  ('mental-health-awareness','q1',1,'It exists on a continuum.'),
  ('mental-health-awareness','q2',3,'About 970 million people.'),
  ('mental-health-awareness','q3',0,'40 / 8.'),
  ('mental-health-awareness','q4',2,'Lasting change affecting daily life.'),
  ('mental-health-awareness','q5',2,'Seek medical assessment.'),
  ('mental-health-awareness','q6',0,'Put the person first.'),
  ('mental-health-awareness','q7',3,'It discourages help-seeking.'),
  ('mental-health-awareness','q8',1,'Listening builds trust.'),
  ('mental-health-awareness','q9',0,'Safety comes first.'),
  ('mental-health-awareness','q10',2,'Research shows asking is safe.'),
  ('mental-health-awareness','q11',1,'Focus on safety.'),
  ('mental-health-awareness','q12',3,'Healthy routines build resilience.'),
  ('mental-health-awareness','q13',3,'Supportive environments help.'),
  ('mental-health-awareness','q14',1,'Awareness is not diagnosis.');
insert into public.course_lessons(course,lesson_id,position) values
  ('mental-health-awareness','understanding',0),
  ('mental-health-awareness','common-conditions',1),
  ('mental-health-awareness','stigma-culture',2),
  ('mental-health-awareness','supporting-someone',3),
  ('mental-health-awareness','crisis',4),
  ('mental-health-awareness','wellbeing',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='mental-health-awareness' and lesson_id not in ('understanding','common-conditions','stigma-culture','supporting-someone','crisis','wellbeing');
-- Course: Medical Terminology. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('medical-terminology','Medical Terminology','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='medical-terminology';
insert into public.course_keys(course,qid,answer,why) values
  ('medical-terminology','q1',1,'Gastritis is stomach inflammation.'),
  ('medical-terminology','q2',3,'-ectomy means removal.'),
  ('medical-terminology','q3',0,'tachy- = fast.'),
  ('medical-terminology','q4',2,'hepat = liver; -megaly = enlargement.'),
  ('medical-terminology','q5',2,'Also ren/o.'),
  ('medical-terminology','q6',0,'hyper- + glyc + -emia.'),
  ('medical-terminology','q7',3,'dys- + -pnea.'),
  ('medical-terminology','q8',1,'Further from where the limb attaches.'),
  ('medical-terminology','q9',0,'Supine is on the back.'),
  ('medical-terminology','q10',2,'Symptoms are reported; signs are observed.'),
  ('medical-terminology','q11',1,'Benign tumours do not invade.'),
  ('medical-terminology','q12',3,'Write units in full.'),
  ('medical-terminology','q13',3,'Latin plural.'),
  ('medical-terminology','q14',1,'Use plain language.');
insert into public.course_lessons(course,lesson_id,position) values
  ('medical-terminology','word-parts',0),
  ('medical-terminology','body-systems',1),
  ('medical-terminology','directions-positions',2),
  ('medical-terminology','diagnosis-procedures',3),
  ('medical-terminology','abbreviations-safety',4),
  ('medical-terminology','plurals-communication',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='medical-terminology' and lesson_id not in ('word-parts','body-systems','directions-positions','diagnosis-procedures','abbreviations-safety','plurals-communication');
-- Course: Maternal and Child Health. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('maternal-child-health','Maternal and Child Health','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='maternal-child-health';
insert into public.course_keys(course,qid,answer,why) values
  ('maternal-child-health','q1',1,'With the first in the first 12 weeks.'),
  ('maternal-child-health','q2',3,'Add 280 days.'),
  ('maternal-child-health','q3',0,'Possible pre-eclampsia.'),
  ('maternal-child-health','q4',2,'Postpartum haemorrhage.'),
  ('maternal-child-health','q5',2,'It helps the uterus contract.'),
  ('maternal-child-health','q6',0,'Early breastfeeding protects the baby.'),
  ('maternal-child-health','q7',3,'Skin-to-skin warmth and feeding.'),
  ('maternal-child-health','q8',1,'Needs urgent assessment.'),
  ('maternal-child-health','q9',0,'Then add complementary foods.'),
  ('maternal-child-health','q10',2,'Long-term undernutrition.'),
  ('maternal-child-health','q11',1,'Rehydration and zinc.'),
  ('maternal-child-health','q12',3,'Needs urgent referral.'),
  ('maternal-child-health','q13',3,'45 / 12 000 x 100 000.'),
  ('maternal-child-health','q14',1,'540 / 12 000 x 1000.');
insert into public.course_lessons(course,lesson_id,position) values
  ('maternal-child-health','antenatal-care',0),
  ('maternal-child-health','birth-postnatal',1),
  ('maternal-child-health','newborn-care',2),
  ('maternal-child-health','feeding-growth',3),
  ('maternal-child-health','immunisation-illness',4),
  ('maternal-child-health','family-planning-indicators',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='maternal-child-health' and lesson_id not in ('antenatal-care','birth-postnatal','newborn-care','feeding-growth','immunisation-illness','family-planning-indicators');
-- Course: Infection Prevention and Control. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('infection-prevention-control','Infection Prevention and Control','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='infection-prevention-control';
insert into public.course_keys(course,qid,answer,why) values
  ('infection-prevention-control','q1',1,'Breaking any link stops spread.'),
  ('infection-prevention-control','q2',3,'Infection status is often unknown.'),
  ('infection-prevention-control','q3',0,'Five key moments around patient care.'),
  ('infection-prevention-control','q4',2,'Soap and water takes 40 to 60 seconds.'),
  ('infection-prevention-control','q5',2,'85 / 120.'),
  ('infection-prevention-control','q6',0,'Clean hands before and after gloves.'),
  ('infection-prevention-control','q7',3,'TB spreads through airborne particles.'),
  ('infection-prevention-control','q8',1,'Critical items.'),
  ('infection-prevention-control','q9',0,'5 / 10 = 0.5%.'),
  ('infection-prevention-control','q10',2,'Dirt blocks disinfectants.'),
  ('infection-prevention-control','q11',1,'Never recap by hand.'),
  ('infection-prevention-control','q12',3,'Prompt assessment for prophylaxis.'),
  ('infection-prevention-control','q13',3,'12 / 800.'),
  ('infection-prevention-control','q14',1,'12 / 4000 x 1000.');
insert into public.course_lessons(course,lesson_id,position) values
  ('infection-prevention-control','chain-of-infection',0),
  ('infection-prevention-control','hand-hygiene',1),
  ('infection-prevention-control','ppe-precautions',2),
  ('infection-prevention-control','cleaning-sterilisation',3),
  ('infection-prevention-control','waste-sharps',4),
  ('infection-prevention-control','surveillance-programmes',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='infection-prevention-control' and lesson_id not in ('chain-of-infection','hand-hygiene','ppe-precautions','cleaning-sterilisation','waste-sharps','surveillance-programmes');
-- Course: Health Records and Informatics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('health-records-informatics','Health Records and Informatics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='health-records-informatics';
insert into public.course_keys(course,qid,answer,why) values
  ('health-records-informatics','q1',1,'Records carry information forward.'),
  ('health-records-informatics','q2',3,'Records must not be dishonestly altered.'),
  ('health-records-informatics','q3',0,'International Classification of Diseases, by WHO.'),
  ('health-records-informatics','q4',2,'Data drive planning.'),
  ('health-records-informatics','q5',2,'46 / 50.'),
  ('health-records-informatics','q6',0,'40 / 50.'),
  ('health-records-informatics','q7',3,'2700 / 3000.'),
  ('health-records-informatics','q8',1,'2700 / 450.'),
  ('health-records-informatics','q9',0,'18 / 450.'),
  ('health-records-informatics','q10',2,'Open-source health information system.'),
  ('health-records-informatics','q11',1,'Interoperability.'),
  ('health-records-informatics','q12',3,'Individual accountability.'),
  ('health-records-informatics','q13',3,'It needs extra protection.'),
  ('health-records-informatics','q14',1,'Unique identification.');
insert into public.course_lessons(course,lesson_id,position) values
  ('health-records-informatics','purpose-records',0),
  ('health-records-informatics','coding-classification',1),
  ('health-records-informatics','his-indicators',2),
  ('health-records-informatics','ehr-digital',3),
  ('health-records-informatics','privacy-security',4),
  ('health-records-informatics','records-management',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='health-records-informatics' and lesson_id not in ('purpose-records','coding-classification','his-indicators','ehr-digital','privacy-security','records-management');
