"""Academic Writing and Research Methods, module 4: Designing research."""
import math
from verify import Q
T1, T2, T3, T4 = ('The research process and research questions', 'Literature reviews', 'Quantitative, qualitative and mixed methods', 'Sampling')
assert 0.1 * 1200 == 120 and 0.6 * 120 == 72 and 120 - 72 == 48
assert 2000 / 100 == 20 and 180 / 600 * 100 == 30
assert 1 / math.sqrt(400) == 0.05 and round(1 / math.sqrt(1000) * 100, 1) == 3.2
assert 0.25 * 400 == 100

MODULE = {
    'title': 'Designing research',
    'topics': [T1, T2, T3, T4],
    'overview': 'Research answers questions systematically. This module covers the stages of a research project and how to write a good research question, how to review existing literature, how to choose between quantitative, qualitative and mixed methods, and how to select a sample that lets you draw sound conclusions.',
    'key_terms': ['Research question', 'Hypothesis', 'Literature review', 'Research gap', 'Quantitative research', 'Qualitative research', 'Mixed methods', 'Validity', 'Reliability', 'Population', 'Sample', 'Probability sampling', 'Sampling bias'],
    'explanation': [
        'A research project moves from a topic to a focused question, through a review of what is already known, to a design for collecting and analysing data, and finally to reporting. A good research question is clear, focused, researchable and significant.',
        'The literature review maps existing knowledge, identifies debates and gaps, and justifies the study. It synthesises sources by theme rather than summarising them one at a time.',
        'Quantitative research measures and counts, often to test hypotheses; qualitative research explores meanings and experiences in depth; mixed methods combine both. Sampling decides who or what is studied, and determines how far results can be generalised.'],
    'quick_facts': [
        'Good research questions are focused, researchable and significant.',
        'A literature review is organised by theme, not by source.',
        'Quantitative: numbers, measurement, generalisation. Qualitative: words, meaning, depth.',
        'Reliability = consistency; validity = measuring what you intend to measure.',
        'Probability samples (random, stratified, systematic) support generalisation.'],
}

NOTES = {
    T1: {
        'overview': 'Research follows a cycle of planning, doing and reporting. The research question drives every later choice.',
        'key_terms': ['Research process', 'Topic', 'Research problem', 'Research question', 'Hypothesis', 'Null hypothesis', 'Variables', 'FINER criteria', 'Research proposal'],
        'explanation': [
            'Typical stages: choose a topic, review the literature, define the problem and research question, choose a design and methods, obtain ethical approval, collect data, analyse it, and write up and share the findings. The process is often iterative: reading may refine your question.',
            'A good research question is focused and answerable with available time and resources. "What affects education in Africa?" is too broad. "How do secondary school students in Lusaka use mobile phones for homework?" is focused. The FINER criteria say a question should be Feasible, Interesting, Novel, Ethical and Relevant.',
            'Quantitative studies often state hypotheses: testable predictions about relationships between variables, such as "Students who sleep at least 7 hours score higher on morning tests." The null hypothesis states there is no effect or relationship; statistical tests assess whether the data give reason to reject it. Qualitative studies more often use open research questions instead.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Topic → problem → question → design → data → analysis → report', 'FINER: feasible, interesting, novel, ethical, relevant', 'Hypothesis: testable prediction', 'Null hypothesis: no effect or relationship'],
        'steps': ['Start with a broad topic.', 'Narrow by population, place, time and concept.', 'Phrase as a clear question.', 'Check it against FINER.'],
        'worked_example': {
            'problem': 'Narrow "unemployment" into a researchable question for a 10-week undergraduate project.',
            'steps': ['Choose a population: recent graduates.', 'Choose a place and time: one city, graduates from the past two years.', 'Choose a focus: job-search strategies.'],
            'answer': 'What job-search strategies do university graduates in Kumasi who finished in the last two years use, and which do they find most effective?',
            'check': 'The question is focused, feasible in 10 weeks and could be answered with interviews or a survey ✓.'},
        'mistakes': ['Choosing a question that is too broad.', 'Writing a question with an obvious yes/no answer.', 'Starting data collection before reviewing the literature.', 'Confusing the hypothesis with the null hypothesis.'],
        'real_world': 'Funding bodies judge research proposals largely on the clarity and significance of the research question.',
        'exam_strategy': 'When asked to evaluate a research question, comment on focus, feasibility and significance with a suggested improvement.',
        'recap': ['Research is a process.', 'Narrow the question.', 'FINER criteria.', 'Hypotheses are testable.']},
    T2: {
        'overview': 'A literature review shows what is known, where scholars disagree and what remains unknown, setting up your own study.',
        'key_terms': ['Literature review', 'Synthesis', 'Thematic organisation', 'Research gap', 'Systematic review', 'Meta-analysis', 'Narrative review', 'Search strategy', 'Literature matrix'],
        'explanation': [
            'The purposes of a literature review: to show you know the field, to identify key theories and findings, to reveal debates and contradictions, to find a gap your study can fill, and to justify your methods. It is an argument about the state of knowledge, not a list.',
            'Organise by theme, debate or method, not one source after another. A literature matrix (a table with columns for each source\'s aim, method, sample, findings and limitations) helps you see patterns across studies. Write with synthesis: "Several studies (Asante, 2019; Diallo, 2021) report…, whereas Nyirenda (2022) found…".',
            'A narrative review summarises literature selectively. A systematic review uses a pre-defined, transparent search and inclusion criteria to find all relevant studies on a question; a meta-analysis statistically combines their results. Systematic reviews and meta-analyses sit at the top of many evidence hierarchies.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Review = argument about what is known', 'Organise by theme, not by source', 'Literature matrix: aim, method, sample, findings, limits', 'Systematic review: transparent, exhaustive search', 'Meta-analysis: statistical combination of results'],
        'steps': ['Search systematically and record your search.', 'Read and fill a literature matrix.', 'Group sources into themes.', 'Write by theme, ending with the gap.'],
        'worked_example': {
            'problem': 'You have read eight studies on mobile learning. Five find benefits, two find no effect and one finds harm. All eight are from urban schools. How should your review present this?',
            'steps': ['Theme 1: evidence of benefits (five studies), with the conditions under which they occurred.', 'Theme 2: mixed or negative findings (three studies) and possible reasons, such as different designs or measures.', 'Gap: all studies are urban, so effects in rural schools are unknown, which your study will investigate.'],
            'answer': 'A thematic synthesis that highlights the debate and ends with the rural gap.',
            'check': 'The review leads logically to the research question rather than listing studies ✓.'},
        'mistakes': ['Summarising sources one by one.', 'Including only studies that agree with you.', 'Failing to identify a gap.', 'Using mostly outdated sources.'],
        'real_world': 'Cochrane systematic reviews guide medical treatment decisions worldwide by combining evidence from many trials.',
        'exam_strategy': 'End your literature review with a sentence that states the gap and how your study addresses it.',
        'recap': ['Review argues about knowledge.', 'Thematic, synthesised.', 'Matrix helps.', 'Finish with the gap.']},
    T3: {
        'overview': 'Choose methods that fit your question. Quantitative and qualitative approaches answer different kinds of questions; mixed methods combine their strengths.',
        'key_terms': ['Quantitative', 'Qualitative', 'Mixed methods', 'Experiment', 'Survey', 'Case study', 'Ethnography', 'Positivism', 'Interpretivism', 'Reliability', 'Validity', 'Generalisability', 'Triangulation'],
        'explanation': [
            'Quantitative research collects numerical data to measure, compare and test relationships, often with large samples, using experiments, surveys and structured observation. It aims for generalisable results and is linked to a positivist view that social reality can be measured objectively.',
            'Qualitative research collects words, images and observations to understand meanings, experiences and processes in depth, using interviews, focus groups, ethnography and document analysis, usually with smaller samples. It is linked to an interpretivist view that reality is shaped by people\'s understandings. Mixed methods combine both, for example a survey to find patterns and interviews to explain them; using several methods to check findings is triangulation.',
            'Quality criteria: reliability is consistency (would the same measure give the same results again?); validity is accuracy (does it measure what it claims to?). Internal validity is whether the design supports causal claims; external validity is whether results generalise. Qualitative researchers also talk about trustworthiness: credibility, transferability, dependability and confirmability.'],
        'formulas_label': 'Comparison',
        'formulas': ['Quantitative: numbers, large samples, testing, generalising', 'Qualitative: words, small samples, meaning, depth', 'Mixed methods: both; triangulation', 'Reliability = consistency; validity = accuracy'],
        'steps': ['Look at the research question\'s wording.', '"How many", "does X affect Y": quantitative.', '"How do people experience", "why": qualitative.', 'Both kinds of question: mixed methods.'],
        'worked_example': {
            'problem': 'Choose a method for: "How do first-generation university students in Malawi experience their first year?"',
            'steps': ['The question asks about experiences and meanings.', 'Depth matters more than numbers.', 'Semi-structured interviews with a small purposive sample suit it.'],
            'answer': 'A qualitative design with semi-structured interviews.',
            'check': 'If the question were "What percentage of first-generation students drop out?", a quantitative design would fit instead ✓.'},
        'mistakes': ['Treating qualitative research as "unscientific".', 'Choosing a method before the question.', 'Confusing reliability with validity.', 'Claiming qualitative findings generalise statistically to a population.'],
        'real_world': 'Health ministries combine large household surveys (quantitative) with community interviews (qualitative) to understand why people do or do not use services.',
        'exam_strategy': 'Justify method choice by quoting the key words of the research question.',
        'recap': ['Numbers vs meanings.', 'Mixed methods combine strengths.', 'Reliability vs validity.', 'Question drives method.']},
    T4: {
        'overview': 'Most research studies a sample rather than a whole population. How the sample is chosen decides how far the findings can be trusted and generalised.',
        'key_terms': ['Population', 'Sampling frame', 'Sample', 'Simple random sampling', 'Systematic sampling', 'Stratified sampling', 'Cluster sampling', 'Convenience sampling', 'Purposive sampling', 'Snowball sampling', 'Sampling bias', 'Response rate', 'Margin of error'],
        'explanation': [
            'The population is the whole group of interest; the sampling frame is the list from which the sample is drawn. Probability sampling gives each member a known chance of selection: simple random (everyone equally likely), systematic (every kth person: choosing 100 from 2000 means every 20th), stratified (sampling within subgroups in proportion) and cluster (randomly choosing whole groups such as schools).',
            'Stratified example: a 10% sample of 1200 students is 120. If 60% of students are women, the sample should contain 72 women and 48 men. Non-probability methods include convenience (whoever is available), purposive (chosen for specific characteristics, common in qualitative work) and snowball (participants recruit others, useful for hard-to-reach groups). These are quicker but risk bias.',
            'Sampling bias occurs when some groups are more likely to be included than others, such as an online survey that misses people without internet access. A low response rate can also bias results: 180 replies from 600 invitations is a 30% response rate. Larger random samples reduce random error; a rough guide is that the margin of error is about 1/√n, so 400 respondents give about ±5%.'],
        'formulas_label': 'Formulas',
        'formulas': ['Systematic interval k = population ÷ sample size', 'Stratified: sample in each stratum = stratum share × sample size', 'Response rate = responses ÷ invitations × 100%', 'Approximate margin of error ≈ 1/√n'],
        'steps': ['Define the population.', 'Choose a sampling method that fits the aim.', 'Calculate sample sizes per group if stratifying.', 'Identify possible bias.'],
        'worked_example': {
            'problem': 'A university has 1200 students, 60% women. You want a 10% stratified sample by gender. How many women and men should you select?',
            'steps': ['Total sample = 10% × 1200 = 120.', 'Women = 60% × 120 = 72.', 'Men = 120 − 72 = 48.'],
            'answer': '72 women and 48 men.',
            'check': '72 : 48 = 60% : 40%, matching the population ✓.'},
        'mistakes': ['Calling a convenience sample "random".', 'Generalising from a biased sample.', 'Ignoring non-response.', 'Thinking a huge biased sample beats a smaller random one.'],
        'real_world': 'Opinion polls of about 1000 randomly chosen people can estimate national opinion within about ±3 percentage points, if the sample is truly representative.',
        'exam_strategy': 'Always name a specific bias risk for the sampling method used and suggest how to reduce it.',
        'recap': ['Population, frame, sample.', 'Probability vs non-probability.', 'Stratify proportionally.', 'Watch for bias and non-response.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Which research question is best focused?', ['How do secondary students in Lusaka use mobile phones for homework?', 'What affects education in Africa?', 'Is technology good?', 'Why do people learn?'], 0, 'Clear population, place and focus.'),
    Q(T1, 'The null hypothesis states that:', ['there is no effect or relationship', 'the researcher\'s prediction is true', 'the data are wrong', 'the sample is biased'], 0, 'Tested statistically.'),
    Q(T1, 'In FINER, the "F" stands for:', ['feasible', 'factual', 'final', 'formal'], 0, 'Can it be done?'),
    Q(T1, 'A hypothesis is:', ['a testable prediction', 'a summary of results', 'a type of sample', 'a reference style'], 0, 'Prediction.'),
    Q(T1, 'Which usually comes first in the research process?', ['Reviewing the literature', 'Collecting data', 'Analysing results', 'Writing the conclusion'], 0, 'Know what is known.'),
    Q(T1, 'Before collecting data from people, researchers normally need:', ['ethical approval', 'a published paper', 'a large grant', 'a null result'], 0, 'Ethics committee.'),
    # T2
    Q(T2, 'A literature review should be organised mainly:', ['by theme or debate', 'one source at a time', 'alphabetically by author', 'by length of article'], 0, 'Synthesis.'),
    Q(T2, 'A research gap is:', ['something not yet known or studied', 'a missing reference', 'a page left blank', 'a low response rate'], 0, 'Justifies your study.'),
    Q(T2, 'A meta-analysis:', ['statistically combines results from many studies', 'is one large interview', 'reviews only one study', 'is a type of fallacy'], 0, 'Pooled analysis.'),
    Q(T2, 'A systematic review differs from a narrative review because it:', ['uses a transparent, pre-defined search and inclusion criteria', 'is shorter', 'includes only one study', 'uses no evidence'], 0, 'Rigour and transparency.'),
    Q(T2, 'A literature matrix is useful for:', ['comparing studies\' aims, methods and findings side by side', 'formatting references', 'choosing a font', 'calculating sample size'], 0, 'Spot patterns.'),
    Q(T2, 'A good literature review usually ends by:', ['stating the gap your study will address', 'listing every source again', 'repeating the title', 'giving the results'], 0, 'Leads to the question.'),
    # T3
    Q(T3, '"How do nurses experience night shifts?" is best answered with:', ['qualitative interviews', 'a randomised experiment', 'a census count', 'a meta-analysis only'], 0, 'Experiences and meanings.'),
    Q(T3, 'Reliability refers to:', ['consistency of a measure', 'whether it measures what it should', 'sample size', 'ethics'], 0, 'Same result again.'),
    Q(T3, 'Validity refers to:', ['whether a measure assesses what it claims to', 'how consistent it is', 'how quickly data are collected', 'the number of participants'], 0, 'Accuracy.'),
    Q(T3, 'Using several methods to check findings is called:', ['triangulation', 'stratification', 'patchwriting', 'replication bias'], 0, 'Converging evidence.'),
    Q(T3, 'Quantitative research typically:', ['collects numerical data to measure and test relationships', 'explores meanings with small samples', 'avoids statistics', 'uses only interviews'], 0, 'Numbers.'),
    Q(T3, 'A survey to find patterns followed by interviews to explain them is:', ['mixed methods', 'purely qualitative', 'purely quantitative', 'a literature review'], 0, 'Combines both.'),
    # T4
    Q(T4, 'A 10% stratified sample of 1200 students (60% women) should include how many women?', ['72', '120', '60', '48'], 0, '0.6 × 120.', ans=72),
    Q(T4, 'Choosing 100 people from a list of 2000 by systematic sampling means selecting every:', ['20th person', '100th person', '10th person', '200th person'], 0, '2000 ÷ 100.'),
    Q(T4, '180 replies from 600 invitations is a response rate of:', ['30%', '18%', '3.3%', '60%'], 0, '180/600.', ans=30),
    Q(T4, 'Participants recruiting other participants is:', ['snowball sampling', 'stratified sampling', 'cluster sampling', 'systematic sampling'], 0, 'Hard-to-reach groups.'),
    Q(T4, 'Interviewing whoever is available in the library is:', ['convenience sampling', 'simple random sampling', 'stratified sampling', 'cluster sampling'], 0, 'Easy but biased.'),
    Q(T4, 'Using the rule of thumb 1/√n, a random sample of 400 gives a margin of error of about:', ['±5%', '±1%', '±20%', '±0.25%'], 0, '1/20 = 0.05.'),
]

FLASH = [
    ['Research question', 'A clear, focused, researchable question that drives the study.'],
    ['Null hypothesis', 'States there is no effect or relationship.'],
    ['Literature review', 'Thematic synthesis of existing research that identifies a gap.'],
    ['Meta-analysis', 'Statistical combination of results from many studies.'],
    ['Reliability', 'Consistency of a measure.'],
    ['Validity', 'Whether a measure assesses what it claims to.'],
    ['Stratified sampling', 'Sampling within subgroups in proportion to the population.'],
    ['Sampling bias', 'Some groups more likely to be included than others.'],
]
