/* Editable site content. Numbers about questions, topics and subjects are NOT written here: they come from SITE_DATA,
   which build.py reads from each country's syllabus file. */
const SITE_CONFIG = {
  appUrl: "app/",     // student app
  loginUrl: "login/",   // sign-in page
  email: "",            // public contact email, shown on the Contact page when set
  whatsapp: "",         // digits only with country code, e.g. 2348012345678
  telegram: "",         // full link
  formEndpoint: "",     // URL that accepts a JSON POST for quote and contact forms
  founder: null         // {name, role, bio} to show a founder section on About
};

const CM = {
NG:{name:'Nigeria',flag:'🇳🇬',lang:'English',levels:'SS1 – SS3',law:'Nigeria Data Protection Act 2023 (NDPA)',
 sys:'WASSCE and NECO SSCE for school leavers, and JAMB UTME for university admission.',
 intro:'Nigeria has the widest coverage: three exams with their own subject lists, built around the national exam bodies. Students can switch between WASSCE, NECO and UTME inside the app.',
 ex:{WASSCE:'WAEC senior school certificate, taken in SS3. Most universities ask for credit passes (C6 or better), usually including English and Mathematics.',
  NECO:'The National Examinations Council senior school certificate. It follows the same national curriculum. Where Ace has not yet written NECO-specific notes, the subject reuses the WASSCE content and says so.',
  UTME:'JAMB\'s computer-based admission test. Four subjects of 100 marks each give a score out of 400; English is compulsory.'},
 scale:'WASSCE/NECO: A1 to F9 (credit = C6 or better). UTME: 0 to 400.',
 next:['Subject-specific NECO notes where WASSCE content is reused today','A combined UTME mock (English plus three subjects, run as one sitting)','More UTME subjects']},
GH:{name:'Ghana',flag:'🇬🇭',lang:'English',levels:'SHS 1 – SHS 3',law:'Data Protection Act, 2012 (Act 843)',
 sys:'WASSCE at the end of senior high school and the BECE at the end of junior high school.',
 intro:'Ghana\'s subject list uses Ghana\'s own names, such as Core Mathematics and Social Studies, and the local currency (₵) in every money question.',
 ex:{WASSCE:'The West African Senior School Certificate Examination, taken at the end of SHS 3, with grades A1 to F9.',
  BECE:'The Basic Education Certificate Examination at the end of JHS 3. Results guide placement into senior high school.'},
 scale:'WASSCE: A1 to F9. BECE: grades 1 to 9 in each subject.',
 next:['Government and Elective Mathematics','More BECE subjects','Ghanaian Language options']},
SL:{name:'Sierra Leone',flag:'🇸🇱',lang:'English',levels:'SS1 – SS3',law:'national data-protection requirements',
 sys:'WASSCE for senior secondary, the BECE for junior secondary and the NPSE for primary.',
 intro:'Sierra Leone is the only country with all three levels: NPSE at the end of primary, BECE at the end of junior secondary and WASSCE at the end of senior secondary.',
 ex:{WASSCE:'The senior secondary certificate, taken in SS3, with grades A1 to F9.',
  BECE:'The Basic Education Certificate Examination at the end of junior secondary school (JSS 3).',
  NPSE:'The National Primary School Examination at the end of primary school (Class 6).'},
 scale:'WASSCE: A1 to F9.',
 next:['Government and Civic Education','More BECE and NPSE subjects','Local-language options']},
GM:{name:'The Gambia',flag:'🇬🇲',lang:'English',levels:'Grade 10 – 12',law:'national data-protection requirements',
 sys:'WASSCE at Grade 12 and the GABECE at the end of basic education.',
 intro:'The Gambia\'s content uses the dalasi (D) and Gambian context, with WASSCE for Grade 12 and GABECE for the end of basic education.',
 ex:{WASSCE:'The West African Senior School Certificate Examination, taken at the end of Grade 12.',
  GABECE:'The Gambia Basic Education Certificate Examination, taken at the end of Grade 9.'},
 scale:'WASSCE: A1 to F9.',
 next:['Integrated Science','Government and Civic Education','More GABECE subjects']},
KE:{name:'Kenya',flag:'🇰🇪',lang:'English',levels:'Form 3 – Form 4',law:'Data Protection Act, 2019',
 sys:'KCSE, set and marked by KNEC at the end of Form 4.',
 intro:'Kenya has its own exam body, KNEC, its own subjects (Business Studies, History and Government) and Kenya shillings (KSh) in the money questions. Kenya is moving to a competency-based curriculum, so check which system your class follows.',
 ex:{KCSE:'The Kenya Certificate of Secondary Education, taken at the end of Form 4. The mean grade runs from A (best) to E.'},
 scale:'KCSE: mean grade A to E, from 12 points down to 1.',
 next:['Home Science, Art and Design, Music','3-D geometry in Mathematics','CATs and joint mock formats']},
ZM:{name:'Zambia',flag:'🇿🇲',lang:'English',levels:'Grade 10 – 12',law:'Data Protection Act, 2021',
 sys:'ECZ Grade 12 school certificate examinations.',
 intro:'Zambia\'s content follows the Examinations Council of Zambia, with Civic Education and Geography as national subjects and kwacha (K) in every money question.',
 ex:{'ECZ Grade 12':'The Examinations Council of Zambia Grade 12 school certificate. Grades run from 1 (best) to 9.'},
 scale:'ECZ: grades 1 (distinction) to 9.',
 next:['Civic Education and remaining electives','Integrated Science','The ECZ Grade 9 examination']},
GB:{name:'United Kingdom',flag:'🇬🇧',lang:'English',levels:'Year 10 – Year 13',law:'UK GDPR and the Data Protection Act 2018',
 sys:'GCSE at 16 and A-Level at 18, set by AQA, Edexcel, OCR and WJEC.',
 intro:'The UK page covers GCSE and A-Level, written against the common content that the exam boards share. Always check your own board\'s specification for the details.',
 ex:{GCSE:'General Certificate of Secondary Education, graded 9 (highest) to 1. Boards include AQA, Edexcel, OCR and WJEC.',
  'A-Level':'Advanced Level qualifications for 16 to 18 year-olds, graded A* to E. Ace starts with Mathematics.'},
 scale:'GCSE: 9 to 1. A-Level: A* to E.',
 next:['AS-Level split','Scottish, Welsh and Northern Irish variants','Languages and arts A-Levels']},
CA:{name:'Canada',flag:'🇨🇦',lang:'English',levels:'Grade 11 – 12',law:'PIPEDA',
 sys:'The Ontario Secondary School Diploma (OSSD), from the Ontario Ministry of Education.',
 intro:'Canada starts with Ontario. Courses use Canadian examples, with 120 V mains in physics and 13% HST in the money questions.',
 ex:{OSSD:'The Ontario Secondary School Diploma. Marks are percentages, and each course mark is 70% classwork and 30% final evaluation.'},
 scale:'Percentage marks, with Ontario\'s achievement levels 1 to 4.',
 next:['Other provinces','Grade 9 and 10 courses','More Ontario and Alberta courses']},
ES:{name:'España',flag:'🇪🇸',lang:'Español',levels:'1º – 2º Bachillerato',law:'RGPD and the LOPDGDD',
 sys:'The EBAU / PAU university-entrance exam after 2º Bachillerato.',
 intro:'Spain\'s content is written in Spanish, and so is the app\'s interface for this country. The EBAU is also called PAU or EvAU depending on the region.',
 ex:{'EBAU / Selectividad':'The university-entrance exam, also called PAU or EvAU in some regions. The admission mark mixes the Bachillerato average (60%) with the exam (40%).'},
 scale:'EBAU: 0 to 14, from the general phase (0 to 10) plus the voluntary phase.',
 next:['Lengua Castellana y Literatura','Inglés','More Bachillerato subjects']},
IE:{name:'Ireland',flag:'🇮🇪',lang:'English',levels:'5th – 6th Year',law:'GDPR',
 sys:'The Leaving Certificate, run by the State Examinations Commission.',
 intro:'Ireland follows the Leaving Certificate, with euro (€) in the money questions and 23% VAT. Points for college come from a student\'s best six subjects.',
 ex:{'Leaving Certificate':'The two-year senior cycle exam from the State Examinations Commission. Subjects are taken at Higher or Ordinary level.'},
 scale:'H1 to H8 (Higher) and O1 to O8 (Ordinary), turned into CAO points.',
 next:['Junior Cycle','Other languages','More Leaving Certificate subjects']},
ZA:{name:'South Africa',flag:'🇿🇦',lang:'English',levels:'Grade 10 – 12',law:'POPIA',
 sys:'The National Senior Certificate (NSC, "matric"), set by the Department of Basic Education and quality-assured by Umalusi.',
 intro:'South Africa follows the CAPS curriculum for the NSC, with rand (R) in the money questions and 15% VAT. Universities use your Admission Point Score (APS) from your best subjects.',
 ex:{'NSC':'The Grade 12 final exams (the "matric" exams). Papers are set nationally by the Department of Basic Education.','Grade 11 exams':'Year-end exams in Grade 11, used for practice and for early university applications.'},
 scale:'Level 1 to 7: 7 is 80 to 100%, 6 is 70 to 79%, 5 is 60 to 69%, 4 is 50 to 59%, 3 is 40 to 49%, 2 is 30 to 39% and 1 is 0 to 29%.',
 next:['Afrikaans','Technical subjects','Grade 12 past-paper walkthroughs']},
UG:{name:'Uganda',flag:'🇺🇬',lang:'English',levels:'S1 – S6',law:'DPPA 2019',
 sys:'The Uganda Certificate of Education (UCE, S4) and the Uganda Advanced Certificate of Education (UACE, S6), set by UNEB.',
 intro:'Uganda follows the UNEB syllabuses, with Uganda shillings (USh) in the money questions and 18% VAT. UACE points decide university entry.',
 ex:{'UCE':'The S4 national exam (O-level) set by UNEB.','UACE':'The S6 national exam (A-level) set by UNEB. Principal subjects and Subsidiary subjects (General Paper, Subsidiary ICT, Subsidiary Mathematics).'},
 scale:'UCE: grades 1 (best) to 9 and a division. UACE: principal passes A to F and subsidiary O or F.',
 next:['Luganda','Fine Art','Remaining UCE and UACE electives']},
TZ:{name:'Tanzania',flag:'🇹🇿',lang:'English',levels:'Form 1 – 6',law:'PDPA 2022',
 sys:'The Certificate of Secondary Education Examination (CSEE, Form 4) and the Advanced Certificate of Secondary Education Examination (ACSEE, Form 6), set by NECTA.',
 intro:'Tanzania follows the NECTA and TIE syllabuses, with Tanzanian shillings (TSh) in the money questions and 18% VAT. ACSEE results go to the Central Admission System (CAS).',
 ex:{'CSEE':'The Form 4 national exam set by NECTA.','ACSEE':'The Form 6 national exam set by NECTA, graded A to F and S, with points used for admission.'},
 scale:'CSEE: divisions I to IV and 0 (grades A to F). ACSEE: grades A to F and S, with points for university.',
 next:['Fine Art','Remaining electives','Swahili-medium notes']}
};

const FEATURES = [
 // [icon, title, text, status, group]
 ['📘','Topic notes','An overview, key terms, a three-part explanation, formulas, a method, a worked example, common mistakes, a real-world link, exam strategy and a recap for every topic.','Live','Learn'],
 ['✅','Topic quizzes','Five questions at a time from the topic bank, scored at the end, with the working shown for every answer.','Live','Practise'],
 ['🔍','Topic question bank','Open any topic and practise every question written for it, or draw a random ten for the subject.','Live','Practise'],
 ['🃏','Flashcards','Curated definition and formula cards for each subject, plus cards made from each topic\'s questions.','Live','Practise'],
 ['⏱️','Timed mock exams','A paper drawn evenly from every module, with a countdown, a score by module and the topics to revise.','Live','Exam prep'],
 ['🤖','Ask Ace','An AI study buddy that knows which subject, topic and exam the student is on and explains step by step.','Live','Learn'],
 ['🔥','Daily challenge and streaks','Five questions a day, XP, and a streak that builds as the student keeps coming back.','Live','Habits'],
 ['🌍','Thirteen countries, one app','Switch country and the exams, subjects, currency and examples change with it. Spain also switches the interface to Spanish.','Live','Learn'],
 ['🎓','Choose your subjects','Students pick the subjects they actually take, and the app shows only those.','Live','Habits'],
 ['♿','Accessibility settings','Dark mode, high-contrast mode and a dyslexia-friendly font.','Live','Habits'],
 ['✍️','What my teacher taught today','The student types what was covered in class. Ace returns a summary, key terms, a worked example and practice questions, and schedules revision.','Backend ready','Daily use'],
 ['🔁','Spaced revision','Short reviews after 1, 3, 7, 21 and 45 days. A wrong answer brings the topic back tomorrow.','Backend ready','Daily use'],
 ['🗺️','Road map to graduation','From lower secondary to career, with the next steps at each stage and a saved goal for course and university.','Live','Daily use'],
 ['🏛️','University explorer','Courses and how admission works at leading universities in each of the thirteen countries, with links to each official site.','Live','University'],
 ['🧮','GPA, citation and focus tools','5.0, 4.0 and UK grade calculators with a "what do I need" planner, an APA and Harvard citation builder, and a focus timer.','Live','University'],
 ['📝','Lecture-note study packs','Paste your own lecture notes and get a summary, flashcards and practice questions.','Backend ready','University'],
 ['🎓','Certificate courses','33 short courses: study skills, coding (Python, JavaScript, SQL, HTML and CSS, Git), digital safety, AI literacy, business and money, public speaking and more. Quizzes are graded on the server and certificates can be verified by anyone.','Backend ready','Courses'],
 ['💬','Moderated study groups','Groups for a class, a school or a campus. No links or phone numbers, member reports, automatic hiding and teacher oversight for school groups.','Backend ready','Community'],
 ['👪','Share one plan with up to 3 others','One payer plus three members, each with their own account and privacy. Friends, classmates or siblings.','Backend ready','Accounts'],
 ['🧑‍🏫','Staff dashboard','Attendance, marks, tasks, notices, messages, live quizzes, parent digest, moderation, school settings and platform admin in one place.','Backend ready','Schools'],
 ['⚡','Live quiz','A teacher starts a quiz, students join with a code and answer on their phones. The answer key never reaches the student.','Backend ready','Schools'],
 ['🔔','Reminders and notices by push','Daily revision reminders and teacher notices delivered to the phone.','Backend ready','Habits'],
 ['🏠','Family view','A private link parents can open, with no account, to see streak, weekly practice and course progress. The student can stop it any time.','Backend ready','Accounts'],
 ['🔐','Username sign-in','Students sign in with a username their school gives them. No email needed.','Backend ready','Accounts'],
 ['📊','Weak Topic Radar','Finds the topics a student keeps getting wrong and points them at the next best practice.','Planned','Practise'],
 ['🧠','Tutor Mode','An AI that guides with questions instead of giving the answer.','Planned','Learn'],
 ['✍️','Essay and answer marking','Paste a written answer and get marks and feedback against the mark scheme.','Planned','Exam prep'],
 ['📐','Formula sheet','Every formula for the subject in one place, by topic.','Planned','Learn'],
 ['🗓️','Study planner and timetable','Exam dates, daily goals and a countdown that follow the national exam timetable.','Planned','Habits'],
 ['🧮','Grade calculator','Enter your marks and see what you need in the final exam for your target grade.','Planned','Exam prep'],
 ['📝','My notes','Write notes next to each topic and keep them with the subject.','Planned','Learn'],
 ['🍅','Pomodoro timer','A 25-minute focus timer that gives XP for finished sessions.','Planned','Habits'],
 ['👥','Study groups and class duel','Private groups with a leaderboard, and head-to-head quiz battles.','Planned','Habits']
];

const SCHOOL = [
 ['👩‍🏫','Class teacher','Manage a class: add students, choose the subjects it studies, set targets and read who is falling behind.',
  ['Add students one by one or by bulk import','Choose the subjects each class sees','Set class targets for each subject','See which topics the class finds hard','Assign a topic or quiz and track completion']],
 ['📚','Subject teacher','One subject across several classes, without the class-admin work.',
  ['See quiz and mock results for your subject only','Teach several classes with one login','Read-only student lists','Assign topics from the syllabus']],
 ['🏫','School admin','The whole school in one view, with the controls a head teacher needs.',
  ['Create the school and invite staff','Cap the number of student slots','Control how much AI help students get','School-wide progress and attendance views','Renew or change the school\'s plan']]
];
const SCHOOL_STATUS = [
 ['Done','Database design with school, class, student, staff and subject tables, and row-level security so each school only sees its own data.'],
 ['Done','Server functions for creating a school, inviting staff, joining with a school code, bulk-creating student accounts, username sign-in, password reset and deleting an account.'],
 ['In build','Teacher, subject-teacher and admin dashboards on top of that backend. The staff sign-in screen exists as a preview and is not yet connected.'],
 ['Next','Continuous-assessment markbook, attendance, report cards and exports.']
];

const FAQ = [
 ['Which exams does Ace Education cover today?','Twenty-three exams across thirteen countries: WASSCE, NECO and UTME in Nigeria; WASSCE and BECE in Ghana; WASSCE, BECE and NPSE in Sierra Leone; WASSCE and GABECE in The Gambia; KCSE in Kenya; ECZ Grade 12 in Zambia; GCSE and A-Level in the UK; the OSSD and Alberta diploma exams in Canada; the PAU (EBAU) in Spain with regional content; the Leaving Certificate in Ireland; the NSC in South Africa; UCE and UACE in Uganda; and CSEE and ACSEE in Tanzania. The Countries page shows exactly which subjects each one has.'],
 ['Are the questions copied from past papers?','No. Topic lists follow each exam body\'s published syllabus, and the notes and questions are written for the app. We do not reproduce past papers or textbooks.'],
 ['Has a teacher checked the content?','Every note and question is checked by code (answers recomputed, duplicates and answer positions tested) and read through for local accuracy. A subject teacher\'s sign-off is the next stage, and until it happens the item carries a "needs review" label. The Countries page shows the review status for each country.'],
 ['How do you make sure the content is local?','Each country has its own file with its own exams, subjects, currency, tax rate and examples. A Kenyan student sees shillings and 16% VAT, a student in Ireland sees euro and 23% VAT, and a student in Canada sees 13% HST and 120 V mains.'],
 ['Is it free for students?','Students reach the app through their school or centre, or through a link from us. Prices are agreed per school or centre. See the Quote page.'],
 ['Does it work on a phone with little data?','The app is a web page that works in a phone browser with no download. Pages are text-first and light. A dedicated data-saver mode and offline use are on the roadmap.'],
 ['Is my data safe?','We collect only what the service needs, we do not sell data, and students or schools can ask for deletion at any time. The Privacy page lists the data-protection law that applies in each country.'],
 ['Can a school use it for a whole class?','The database and server functions for schools are built. The teacher and admin dashboards are being built on top of them, so schools can join the pilot list now.'],
 ['Which country is next?','The thirteen countries are open for content now. We add a country by adding a syllabus file, so new ones can follow quickly. Tell us which you need on the Contact page.']
];

const GUIDES = [
 ['active-recall','Study tips','Active recall beats re-reading','Re-reading feels productive because the page looks familiar. Familiarity is not the same as being able to produce the answer on an exam paper.',
  ['Close the notes and write down everything you remember about the topic. Then open the notes and mark what you missed.','Turn each heading into a question. "What is the discriminant used for?" is better than rereading "Discriminant".','Use the topic quizzes in the app as the recall step. Wrong answers show the working, which is when learning happens.','Come back to the missed items the next day, then three days later, then a week later. Spacing the practice is what keeps it.'],'5 min'],
 ['mock-exams','Exam prep','How to use a mock exam properly','A mock is only useful if you sit it like the real thing and learn from it afterwards.',
  ['Pick a time with no phone and set the timer to the real exam length.','Sit the whole paper. If you leave a question, move on and come back, as you would in the hall.','Mark it straight away. For every wrong answer, write why: a knowledge gap, a method slip or a misread question.','Revise the weakest topics first and sit another mock two weeks later. Compare by module, not only the total.'],'6 min'],
 ['plan','Exam prep','Build a six-week revision plan','Start from the exam date and work backwards. A plan you can keep is better than a perfect plan you drop after three days.',
  ['List every subject and give each topic a rating: confident, shaky or lost.','Spend the first weeks on the lost topics, because they take longest to fix.','Plan two or three subjects a day and switch between them so none gets stale.','Keep the last week for mocks and light review, not new material.','Leave one half-day a week free for the things that go wrong.'],'6 min'],
 ['maths-habits','Subject guides','Five habits that win marks in Mathematics','Most lost marks in maths are method and presentation, not lack of ability.',
  ['Write each step on its own line. Examiners give method marks for working that is visible.','Check every answer: substitute back, estimate, or use another method.','Keep units and currency with every answer. A correct number with no unit often loses a mark.','Read the whole question twice, and underline what is actually being asked.','Practise by topic first, then mix topics, because the exam will not tell you which topic a question is from.'],'5 min'],
 ['science-practicals','Subject guides','Physics, Chemistry and Biology: from definitions to application','Science papers test whether you can apply an idea to a situation you have not seen.',
  ['Learn each definition word for word, then practise using it in a sentence about a real situation.','For calculations, write the formula, substitute with units, then answer with units.','In Chemistry, balance every equation and check the state symbols.','In Biology, learn process descriptions in order, and practise explaining why, not only what.'],'6 min'],
 ['exam-systems','Exam systems','How the thirteen exam systems compare','The thirteen countries in Ace Education test students in very different ways. Here is the quick difference.',
  ['West Africa (Nigeria, Ghana, Sierra Leone, The Gambia): WASSCE grades run A1 to F9, and a credit is C6 or better.','Kenya: KCSE gives a mean grade A to E, with 12 points for A.','Zambia: ECZ grades run from 1 (best) to 9.','UK: GCSE uses 9 to 1 and A-Level uses A* to E.','Canada: marks in Ontario are percentages.','Spain: the EBAU is marked 0 to 14 including the voluntary phase.','Ireland: Leaving Certificate grades H1 to H8 and O1 to O8 turn into CAO points.','South Africa: the NSC reports achievement levels 1 to 7, where level 7 is 80 to 100%.','Uganda: UCE grades run 1 (best) to 9, and UACE gives principal passes A to F.','Tanzania: CSEE uses divisions I to IV and 0, and ACSEE grades run A to F.'],'4 min'],
 ['exam-stress','Wellbeing','Managing exam stress','A little stress sharpens attention. Too much makes it hard to start. These habits help most students.',
  ['Sleep is part of revision. Memory is stored overnight, so cutting sleep to study usually backfires.','Break the work into small tasks that fit in 25 minutes. Starting is the hardest part.','Move for ten minutes between sessions. Walking is enough.','Talk to someone you trust. If worry is affecting your sleep or daily life for weeks, speak to a teacher, parent or a health professional.'],'5 min'],
 ['using-ace','Using Ace','Getting the most from Ace Education','Ace Education is built around a simple loop: learn a topic, test it, then sit a mock.',
  ['Open a subject and pick the first topic you are shaky on.','Read the notes, then take the five-question quiz.','Use Ask Ace when a step does not make sense. Ask it to explain, not to just give the answer.','When you have covered a module, sit the timed mock and read the module breakdown.','Come back every day for the daily challenge. A short daily habit beats a long weekly session.'],'4 min']
];

const VALUES = [
 ['🎯','Local first','Every country gets its own exam bodies, subject list, currency and examples. We do not translate one syllabus thirteen times.'],
 ['🔍','Honest about quality','New content says "needs review" until a teacher signs it off. We would rather show you the status than hide it.'],
 ['🧮','Numbers checked by code','Worked answers in maths, science, economics and accounting are recomputed by a program before they go in.'],
 ['🔒','Privacy first','We collect only what the service needs, we do not sell data, and deletion is available on request.'],
 ['📱','Built for phones','A web page that works in a mobile browser with no install, light enough for limited data.'],
 ['🧘','Whole student','Wellbeing sits next to marks. Exam prep should not cost students their sleep.']
];

const COMPARE = [
 ['Written for each country\'s exam','yes','Partly','Rarely','No'],
 ['Subjects and examples follow the national syllabus','yes','Partly','Varies','Varies'],
 ['Local currency, tax rates and units in questions','yes','No','No','No'],
 ['Topic notes, quizzes and mocks in one place','yes','No','Notes only','No'],
 ['AI help that knows the topic and exam','yes','No','No','No'],
 ['School and teacher tools','Building','No','No','No'],
 ['Works in a phone browser with no install','yes','Yes','Yes','Yes'],
 ['Shows when content has been teacher-reviewed','yes','Rarely','Rarely','No']
];

const ROADMAP = [
 ['Now','Thirteen countries with their own exams, subjects and syllabus files','Student app with notes, quizzes, flashcards, mocks and Ask Ace','Database and server functions for schools'],
 ['Next','Teacher review of every subject, country by country','Teacher review of every university entry, and more universities per country','Formula sheets, study planner and exam timetables'],
 ['Later','More subjects and exams per country, starting with the gaps listed on each country page','Weak Topic Radar, Tutor Mode and answer marking','Data-saver and offline modes, and more countries']
];
