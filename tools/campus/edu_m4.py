"""Foundations of Education, module 4: Assessment and evaluation."""
import statistics as st
from verify import Q
from nt import N, module
T1, T2, T3, T4 = ('Purposes and types of assessment', 'Validity, reliability and fairness', 'Constructing tests and marking schemes', 'Analysing and reporting scores')

S = [45, 52, 58, 60, 60, 64, 70, 75, 81, 85]
assert st.mean(S) == 65 and st.median(S) == 62 and st.mode(S) == 60 and max(S) - min(S) == 40
assert round(st.pstdev([2, 4, 4, 4, 5, 5, 7, 9]), 6) == 2
assert 0.4 * 50 == 20 and 0.3 * 50 == 15 and 0.2 * 50 == 10 and 0.1 * 50 == 5
assert 30 * 100 // 40 == 75 and 18 * 100 // 40 == 45
assert (72 - 60) / 8 == 1.5 and 0.3 * 70 + 0.7 * 60 == 63

MODULE = module('Assessment and evaluation', [T1, T2, T3, T4],
    'Assessment gathers evidence of what learners know and can do, so that teachers can help them learn and report their progress. This module covers the purposes and types of assessment, the qualities of good assessment, how to construct tests and marking schemes, and how to analyse and report scores.',
    ['Assessment', 'Evaluation', 'Formative assessment', 'Summative assessment', 'Continuous assessment', 'Validity', 'Reliability', 'Table of specifications', 'Marking scheme', 'Mean', 'Standard deviation', 'Item analysis'],
    ['Assessment for learning (formative) happens during teaching to guide the next steps; assessment of learning (summative) judges achievement at the end of a unit, term or course. Many systems combine continuous assessment with final examinations, as in WAEC and national examinations that use school-based scores.',
     'Good assessment is valid (measures what it is meant to measure), reliable (gives consistent results), fair to all groups of learners and practical. A table of specifications (test blueprint) ensures that a test covers topics and levels of thinking in the right proportions.',
     'Teachers summarise scores with the mean, median, mode, range and standard deviation, convert raw scores to percentages and standard scores, and use item analysis to improve questions. Results should be reported clearly to learners and parents with feedback on how to improve.'],
    ['Formative = for learning; summative = of learning.', 'Validity: measures the right thing; reliability: consistent.', 'A reliable test can be invalid; a valid test must be reliable.', 'Blueprint: topics × cognitive levels.', 'z = (score − mean) ÷ SD.'])

NOTES = {
 T1: N('Assessment is not only about marks. Used well, it is one of the most powerful tools teachers have for improving learning.',
   ['Assessment', 'Evaluation', 'Measurement', 'Formative assessment', 'Summative assessment', 'Diagnostic assessment', 'Continuous assessment', 'Feedback'],
   ['Measurement assigns numbers (a score of 34 out of 50); assessment is the wider process of collecting evidence about learning, by tests, observation, projects, portfolios or questioning; evaluation is judging the value or effectiveness of something, such as a programme or curriculum, using that evidence.',
    'Diagnostic assessment, before teaching, finds out what learners already know and their difficulties. Formative assessment during teaching, such as questioning, exit tickets, quizzes and reviewing drafts, gives feedback that learners use to improve; Black and Wiliam\'s review "Inside the Black Box" (1998) found that strong formative assessment raises achievement. Summative assessment, such as end-of-term exams and national certificates, records achievement for reports, promotion and selection.',
    'Continuous assessment (CA) collects scores from class tests, assignments and projects across the course and combines them with the final exam, for example 30% CA and 70% exam. It rewards steady work and covers skills a single exam misses, but it needs careful record keeping, moderation to keep standards comparable between schools, and protection against inflated marks.'],
   ['Measurement < assessment < evaluation', 'Diagnostic: before; formative: during; summative: after', 'Feedback must be used to count as formative', 'Final = CA weight × CA + exam weight × exam'],
   ['Identify when the assessment happens.', 'Identify its purpose.', 'Classify it.', 'Say how its results should be used.'],
   ('A student scores 70 in continuous assessment and 60 in the final exam. CA counts 30% and the exam 70%. What is the final score?',
    ['CA contribution = 0.3 × 70 = 21.', 'Exam contribution = 0.7 × 60 = 42.', 'Final = 21 + 42 = 63.'],
    '63', 'Check: 63 lies between 60 and 70, nearer 60 because the exam has more weight ✓.'),
   ['Equating assessment with testing.', 'Calling a mid-term exam "formative" when no feedback is used.', 'Confusing evaluation with measurement.', 'Adding CA and exam scores without weights.'],
   'Ghana\'s School-Based Assessment and Nigeria\'s continuous assessment in schools both combine classroom scores with external examinations.',
   'Define each type by its timing and purpose, and give a classroom example.',
   ['Measurement, assessment, evaluation.', 'Diagnostic, formative, summative.', 'Feedback.', 'Continuous assessment.']),
 T2: N('A score is only useful if it measures the right thing consistently and fairly.',
   ['Validity', 'Content validity', 'Construct validity', 'Predictive validity', 'Reliability', 'Test-retest reliability', 'Inter-rater reliability', 'Bias'],
   ['Validity is the extent to which a test measures what it claims to measure and supports the decisions made from it. Content validity: the test samples the syllabus fairly. Construct validity: it measures the intended ability, not something else (a maths test full of difficult English partly measures reading). Predictive validity: scores predict later performance, such as university success.',
    'Reliability is consistency. Test-retest reliability: similar scores on repeated testing. Inter-rater reliability: different markers give similar marks, improved by detailed marking schemes and moderation. Internal consistency: items in a test measure the same thing. Longer tests with clear items and objective scoring are usually more reliable. A test can be reliable but not valid (a bathroom scale that is always 2 kg too heavy is consistent but wrong), but it cannot be valid without being reliable.',
    'Fairness means the test does not disadvantage groups for reasons unrelated to what is measured, such as language, culture, gender or disability. Accommodations such as extra time, braille or large print keep the test fair without changing what it measures. Practicality covers cost, time and ease of administration.'],
   ['Validity: measures what it should', 'Reliability: consistent results', 'Reliable ≠ valid; valid ⇒ reliable', 'Moderation improves inter-rater reliability'],
   ['Name the quality in question.', 'Identify the threat.', 'Explain its effect on the score.', 'Suggest a fix.'],
   ('Two teachers mark the same essays. One gives an average of 62, the other 48, for the same scripts. What problem is this, and how can it be reduced?',
    ['The same work gets very different marks, so the marking is inconsistent.', 'This is a problem of inter-rater reliability.', 'Use a detailed marking scheme or rubric, train markers with sample scripts and moderate by second-marking a sample.'],
    'Poor inter-rater reliability; fix with a rubric, marker training and moderation.', 'The problem is named and specific fixes are given ✓.'),
   ['Using validity and reliability as synonyms.', 'Thinking a consistent test must be valid.', 'Ignoring language load as a threat to validity.', 'Treating accommodations as unfair advantages.'],
   'Examination bodies such as WAEC and KNEC train and coordinate examiners and check marking samples to keep marking reliable across thousands of scripts.',
   'Use the bathroom-scale example to explain the difference between reliability and validity.',
   ['Types of validity.', 'Types of reliability.', 'Relationship between them.', 'Fairness.']),
 T3: N('A good test is planned, not improvised. A blueprint and a marking scheme make tests fairer and more useful.',
   ['Table of specifications', 'Objective item', 'Multiple-choice item', 'Stem', 'Distractor', 'Essay item', 'Rubric', 'Marking scheme'],
   ['A table of specifications (test blueprint) is a grid of topics against cognitive levels, showing how many marks go to each cell, in proportion to teaching time and importance. For a 50-mark test, if topic A had 40% of teaching time, it should carry about 20 marks.',
    'Objective items (multiple choice, matching, true/false, short answer) can sample much content quickly and are marked reliably. A multiple-choice item has a stem (the question) and options: one key and plausible distractors based on common errors. Avoid clues such as the longest option always being correct, "all of the above", double negatives and grammatical mismatches between stem and options.',
    'Essay and structured items test organisation, argument and higher-order thinking but take longer to mark and are less reliable. Use clear command words (explain, compare, evaluate), state the marks, and prepare a marking scheme listing acceptable points and marks, or an analytic rubric with criteria and levels. Mark one question across all scripts before moving to the next to improve consistency.'],
   ['Blueprint: marks ∝ teaching time and importance', 'MCQ: stem + key + plausible distractors', 'Essay: rubric or marking scheme', 'Mark question by question'],
   ['List topics and weights.', 'Choose cognitive levels.', 'Allocate marks in a blueprint.', 'Write items and the marking scheme.'],
   ('A 50-mark test covers four topics taught for 40%, 30%, 20% and 10% of the time. Allocate marks.',
    ['Topic 1: 40% of 50 = 20 marks.', 'Topic 2: 30% of 50 = 15 marks.', 'Topic 3: 20% of 50 = 10 marks.', 'Topic 4: 10% of 50 = 5 marks.'],
    '20, 15, 10 and 5 marks.', 'Check: 20 + 15 + 10 + 5 = 50 ✓.'),
   ['Writing a test without a blueprint.', 'Using implausible distractors.', 'Vague essay questions without command words.', 'Marking essays without a scheme.'],
   'Examination bodies publish chief examiners\' reports that show typical errors, which teachers can use to write realistic distractors.',
   'In test-construction answers, show a small blueprint grid and one sample item with its marking points.',
   ['Blueprint.', 'Objective items and distractors.', 'Essay items and rubrics.', 'Marking practice.']),
 T4: N('Turning raw scores into useful information needs basic statistics and good item analysis.',
   ['Raw score', 'Percentage', 'Mean', 'Median', 'Mode', 'Range', 'Standard deviation', 'z-score', 'Difficulty index', 'Discrimination index'],
   ['For the scores 45, 52, 58, 60, 60, 64, 70, 75, 81, 85: the mean is 650 ÷ 10 = 65, the median is the average of the 5th and 6th scores, (60 + 64) ÷ 2 = 62, the mode is 60 and the range is 85 − 45 = 40. The standard deviation (SD) measures spread around the mean: a small SD means scores are close together.',
    'A z-score shows how many SDs a score is above or below the mean: z = (score − mean) ÷ SD. If a class mean is 60 and SD 8, a score of 72 has z = 1.5. z-scores let teachers compare performance across tests of different difficulty. Percentages convert raw scores to a common scale: 30 out of 40 is 75%.',
    'Item analysis improves tests. The difficulty index p is the proportion of candidates answering correctly (p = 0.9 is very easy; p = 0.2 is hard; about 0.3 to 0.7 is usually best). The discrimination index compares the upper and lower scoring groups: a good item is answered correctly more often by high scorers. Items with negative discrimination, or distractors chosen by no one, should be revised.'],
   ['Mean = sum ÷ n; median = middle; mode = most frequent', 'z = (x − mean) ÷ SD', 'Difficulty p = correct ÷ total', 'Discrimination: upper group − lower group'],
   ['Order the scores.', 'Calculate the measure asked for.', 'Interpret it in words.', 'Use it to make a teaching or test decision.'],
   ('In a class with mean 60 and standard deviation 8, Ama scores 72 in English. In maths, with mean 50 and SD 10, she scores 62. In which subject did she do better relative to the class?',
    ['English: z = (72 − 60) ÷ 8 = 1.5.', 'Maths: z = (62 − 50) ÷ 10 = 1.2.', '1.5 is greater than 1.2.'],
    'She did relatively better in English.', 'Both z-scores are compared on the same scale ✓.'),
   ['Using the mean when a few extreme scores distort it (the median may be better).', 'Forgetting to order scores before finding the median.', 'Comparing raw scores from tests of different difficulty.', 'Calling a high p value a hard item.'],
   'Standardised (scaled) scores in national examinations use the same idea as z-scores, so that results are comparable across papers and years.',
   'Show each step of a calculation and finish with an interpretation sentence.',
   ['Central tendency and range.', 'Standard deviation.', 'z-scores.', 'Item analysis.']),
}

QUESTIONS = [
    Q(T1, 'Assessment used during teaching to give feedback that improves learning is:', ['formative', 'summative', 'diagnostic only', 'norm-referenced only'], 0, 'Assessment for learning.'),
    Q(T1, 'An end-of-year examination used for promotion is:', ['summative', 'formative', 'diagnostic', 'informal'], 0, 'Assessment of learning.'),
    Q(T1, 'A pre-test given to find out what learners already know is:', ['diagnostic assessment', 'summative assessment', 'moderation', 'evaluation of a programme'], 0, 'Before teaching.'),
    Q(T1, 'CA counts 30% and the exam 70%. A student scores 70 in CA and 60 in the exam. The final score is:', ['63', '65', '67', '130'], 0, '21 + 42.', ans=63),
    Q(T1, 'The 1998 review showing that formative assessment raises achievement was:', ['Inside the Black Box (Black and Wiliam)', 'Democracy and Education (Dewey)', 'The Concept of Law (Hart)', 'The Salamanca Statement'], 0, 'Assessment for learning.'),
    Q(T1, 'Judging the effectiveness of a whole programme is:', ['evaluation', 'measurement', 'a raw score', 'a distractor'], 0, 'Broader than assessment.'),
    Q(T2, 'A test that measures what it claims to measure is:', ['valid', 'reliable only', 'practical only', 'standardised'], 0, 'Validity.'),
    Q(T2, 'A test that gives consistent results is:', ['reliable', 'valid', 'biased', 'formative'], 0, 'Consistency.'),
    Q(T2, 'A bathroom scale that always reads 2 kg too heavy is:', ['reliable but not valid', 'valid but not reliable', 'both valid and reliable', 'neither consistent nor accurate'], 0, 'Consistent but wrong.'),
    Q(T2, 'A maths test with very hard English mainly threatens:', ['construct validity', 'test-retest reliability', 'practicality', 'scoring speed'], 0, 'Measures reading too.'),
    Q(T2, 'Second-marking a sample of scripts to align standards is called:', ['moderation', 'item analysis', 'blueprinting', 'diagnosis'], 0, 'Improves inter-rater reliability.'),
    Q(T2, 'Giving a candidate with low vision a large-print paper is an example of:', ['an accommodation that keeps the test fair', 'cheating', 'reducing validity', 'formative feedback'], 0, 'Removes an irrelevant barrier.'),
    Q(T3, 'A grid of topics against cognitive levels used to plan a test is a:', ['table of specifications', 'marking scheme', 'report card', 'rubric only'], 0, 'Test blueprint.'),
    Q(T3, 'In a multiple-choice item, the incorrect options are called:', ['distractors', 'stems', 'keys', 'rubrics'], 0, 'Should be plausible.'),
    Q(T3, 'A topic taught for 40% of the time in a 50-mark test should carry about:', ['20 marks', '40 marks', '10 marks', '25 marks'], 0, '40% × 50.', ans=20),
    Q(T3, 'Which is a weakness of essay items compared with objective items?', ['They are less reliable to mark', 'They cannot test higher-order thinking', 'They sample more content', 'They are quicker to mark'], 0, 'Marker judgement varies.'),
    Q(T3, 'To improve consistency, an examiner should mark:', ['one question across all scripts before the next', 'each script fully in turn without a scheme', 'only the first page', 'without reading the question'], 0, 'Question by question.'),
    Q(T3, 'Which is poor multiple-choice practice?', ['Making the correct option always the longest', 'Using plausible distractors', 'Writing a clear stem', 'Basing distractors on common errors'], 0, 'Gives a clue.'),
    Q(T4, 'For the scores 45, 52, 58, 60, 60, 64, 70, 75, 81, 85, the mean is:', ['65', '62', '60', '64'], 0, '650 ÷ 10.', ans=65),
    Q(T4, 'For the same scores, the median is:', ['62', '60', '65', '64'], 0, '(60 + 64) ÷ 2.', ans=62),
    Q(T4, 'A class mean is 60 with standard deviation 8. A score of 72 has a z-score of:', ['1.5', '12', '0.75', '−1.5'], 0, '(72 − 60) ÷ 8.', ans=1.5),
    Q(T4, '30 out of 40 as a percentage is:', ['75', '70', '30', '80'], 0, '30 ÷ 40 × 100.', ans=75),
    Q(T4, 'An item answered correctly by 90% of candidates has a difficulty index of 0.9, meaning it is:', ['very easy', 'very hard', 'ideal for discrimination', 'invalid'], 0, 'High p = easy.'),
    Q(T4, 'An item answered correctly more often by low scorers than by high scorers has:', ['negative discrimination and should be revised', 'perfect validity', 'ideal difficulty', 'high reliability'], 0, 'Faulty item.'),
]

FLASH = [
    ['Formative v summative', 'For learning (during) v of learning (after).'],
    ['Diagnostic assessment', 'Before teaching, to find prior knowledge and difficulties.'],
    ['Validity', 'Measures what it is supposed to measure.'],
    ['Reliability', 'Gives consistent results.'],
    ['Table of specifications', 'Blueprint of topics × cognitive levels.'],
    ['Distractor', 'A plausible wrong option in a multiple-choice item.'],
    ['z-score', '(score − mean) ÷ SD.'],
    ['Difficulty index', 'Proportion answering correctly; high = easy.'],
]
