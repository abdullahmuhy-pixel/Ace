"""Academic Writing and Research Methods, module 5: Collecting, analysing and reporting data."""
import statistics as st
from verify import Q
T1, T2, T3, T4 = ('Questionnaires and interviews', 'Analysing quantitative and qualitative data', 'Research ethics and data management', 'Writing and presenting a research report')
assert st.mean([5, 4, 4, 3, 2]) == 3.6 and st.median([5, 4, 4, 3, 2]) == 4
assert 45 / 150 * 100 == 30 and (50 - 40) / 40 * 100 == 25
assert 3 / 12 * 100 == 25

MODULE = {
    'title': 'Collecting, analysing and reporting data',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module completes the research cycle: designing good questionnaires and interviews, analysing numerical and textual data, handling participants and data ethically, and writing and presenting a clear research report.',
    'key_terms': ['Closed question', 'Open question', 'Likert scale', 'Leading question', 'Pilot study', 'Semi-structured interview', 'Descriptive statistics', 'Thematic analysis', 'Coding', 'Anonymity', 'Data protection', 'IMRaD', 'Abstract'],
    'explanation': [
        'Questionnaires gather standardised answers from many people; interviews explore views in depth. Clear, neutral, single-issue questions and a pilot test are essential for good data.',
        'Quantitative data are summarised with descriptive statistics, tables and charts, and tested with inferential statistics. Qualitative data are analysed by coding and identifying themes, supported by quotations.',
        'Ethical research protects participants and their data throughout. Research reports in most fields follow the IMRaD structure (introduction, methods, results and discussion), with an abstract, and findings are often presented orally or on posters.'],
    'quick_facts': [
        'Avoid leading, double-barrelled and ambiguous questions.',
        'Always pilot your instrument first.',
        'Thematic analysis: code the data, then group codes into themes.',
        'Anonymised data cannot be linked back to individuals.',
        'IMRaD: introduction, methods, results, discussion.'],
}

NOTES = {
    T1: {
        'overview': 'Questionnaires and interviews are the most common ways to collect data from people. Their quality depends on the questions you ask.',
        'key_terms': ['Closed question', 'Open question', 'Likert scale', 'Leading question', 'Double-barrelled question', 'Social desirability bias', 'Pilot study', 'Structured interview', 'Semi-structured interview', 'Focus group', 'Transcription'],
        'explanation': [
            'Closed questions give fixed options (yes/no, multiple choice, rating scales) and are easy to analyse; open questions let people answer in their own words and give richer data. A Likert scale asks how much people agree with a statement, typically from 1 (strongly disagree) to 5 (strongly agree).',
            'Avoid leading questions ("Don\'t you agree that fees are too high?"), double-barrelled questions that ask two things at once ("Is the library quiet and well stocked?"), jargon and vague terms ("often"). Social desirability bias means people give answers that make them look good, so keep questions neutral and assure anonymity. Always run a pilot study with a few people to find confusing questions before the main study.',
            'Structured interviews use fixed questions in a fixed order; semi-structured interviews use an interview guide with flexibility for follow-up probes ("Can you tell me more about that?"); unstructured interviews are conversational. Focus groups interview 6 to 10 people together, useful for exploring shared views. Interviews are usually recorded, with consent, and transcribed.'],
        'formulas_label': 'Question checklist',
        'formulas': ['One idea per question', 'Neutral wording (not leading)', 'Clear, simple language', 'Balanced response options', 'Pilot before use'],
        'steps': ['List what you need to know.', 'Write clear, neutral questions.', 'Choose closed or open formats.', 'Pilot and revise.'],
        'worked_example': {
            'problem': 'Improve this survey question: "Do you agree that the canteen food is expensive and unhealthy?"',
            'steps': ['It is leading ("Do you agree that…").', 'It is double-barrelled (price and health).', 'Split it into two neutral Likert items.'],
            'answer': '"Rate how much you agree: (a) The canteen food is good value for money. (b) The canteen food is healthy." (1 = strongly disagree to 5 = strongly agree)',
            'check': 'Each item now asks one thing and does not push the respondent towards an answer ✓.'},
        'mistakes': ['Asking two things in one question.', 'Using leading wording.', 'Skipping the pilot.', 'Using only open questions with a very large sample.'],
        'real_world': 'National censuses test their questionnaires in pilot surveys for years before the main count, rewording questions people misunderstand.',
        'exam_strategy': 'When asked to critique a question, name the specific problem (leading, double-barrelled) and rewrite it.',
        'recap': ['Closed vs open.', 'Neutral, single-issue questions.', 'Pilot first.', 'Semi-structured interviews allow probing.']},
    T2: {
        'overview': 'Analysis turns raw data into findings. Quantitative and qualitative data need different, equally careful approaches.',
        'key_terms': ['Descriptive statistics', 'Frequency table', 'Percentage', 'Mean', 'Median', 'Bar chart', 'Inferential statistics', 'Coding', 'Theme', 'Thematic analysis', 'Content analysis'],
        'explanation': [
            'Start quantitative analysis with descriptive statistics: frequencies, percentages, means, medians and standard deviations. If 45 of 150 respondents agree, that is 30%. For Likert responses 5, 4, 4, 3, 2, the mean is 3.6 and the median 4; many researchers report the median or the percentage agreeing for single Likert items. Use bar charts for categories, histograms for distributions and scatter plots for relationships between two variables.',
            'Inferential statistics test whether patterns are likely to hold in the wider population: t-tests compare two group means, chi-square tests compare frequencies across categories, and correlation measures association. Spreadsheet software, SPSS or R can run these. Report percentage changes correctly: a rise from 40 to 50 is 10 percentage points but a 25% increase.',
            'Qualitative analysis often uses thematic analysis (Braun and Clarke, 2006): become familiar with the data, generate initial codes (labels for meaningful segments), search for themes, review themes, define and name them, and write up. Support each theme with well-chosen quotations from participants. Content analysis counts how often categories appear in texts, bridging qualitative and quantitative approaches.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Percentage = part ÷ whole × 100', 'Percentage change = (new − old) ÷ old × 100', 'Percentage points: simple difference between percentages', 'Thematic analysis: familiarise → code → themes → review → define → write'],
        'steps': ['Clean and organise the data.', 'Describe (statistics or codes).', 'Analyse (tests or themes).', 'Interpret in light of the question.'],
        'worked_example': {
            'problem': 'Last year 40% of students used the library weekly; this year 50% do. Describe the change in two correct ways.',
            'steps': ['Difference = 50 − 40 = 10 percentage points.', 'Relative change = (50 − 40) ÷ 40 × 100 = 25%.', 'So the proportion rose by 10 percentage points, a 25% increase.'],
            'answer': 'Up 10 percentage points, or 25% higher.',
            'check': 'Saying "a 10% increase" would be wrong; it is 10 points ✓.'},
        'mistakes': ['Confusing percentage points with percentages.', 'Reporting means for categories like gender.', 'Listing quotations without themes.', 'Claiming causation from descriptive statistics.'],
        'real_world': 'Election coverage often confuses percentage points with percentage changes; getting this right is a mark of numerate reporting.',
        'exam_strategy': 'State the analysis method explicitly in your methods section ("thematic analysis following Braun and Clarke, 2006").',
        'recap': ['Describe before testing.', 'Points vs percent.', 'Code then theme.', 'Quotations support themes.']},
    T3: {
        'overview': 'Ethical research protects participants before, during and after a study, including how their data are stored and shared.',
        'key_terms': ['Informed consent', 'Participant information sheet', 'Voluntary participation', 'Right to withdraw', 'Anonymity', 'Confidentiality', 'Pseudonymisation', 'Vulnerable groups', 'Data protection law', 'Data management plan'],
        'explanation': [
            'Participants should receive an information sheet explaining the purpose, what taking part involves, risks and benefits, how data will be used and stored, and how to withdraw. They give informed consent, usually in writing. Participation must be voluntary, without pressure, which needs extra care when the researcher has power over participants (a lecturer surveying their own students).',
            'Anonymity means even the researcher cannot link data to individuals; confidentiality means the researcher knows who said what but does not reveal it. Pseudonymisation replaces names with codes or false names, with the key stored separately and securely. Vulnerable groups, such as children, need extra protections, including consent from parents or guardians.',
            'Data protection laws govern personal data: for example the EU and UK GDPR, Kenya\'s Data Protection Act (2019), Nigeria\'s Data Protection Act (2023) and South Africa\'s POPIA. A data management plan sets out how data will be stored securely (encrypted, password-protected), who can access them, how long they are kept and when they are destroyed.'],
        'formulas_label': 'Checklist',
        'formulas': ['Information sheet + informed consent', 'Voluntary, with right to withdraw', 'Anonymity vs confidentiality', 'Secure storage and data management plan', 'Follow national data protection law'],
        'steps': ['Identify risks to participants.', 'Plan consent and withdrawal.', 'Decide on anonymity or confidentiality.', 'Write a data management plan.'],
        'worked_example': {
            'problem': 'A student plans to interview classmates about cheating and store recordings on a shared laptop. Identify two ethical risks and solutions.',
            'steps': ['Risk 1: sensitive topic; participants could be identified. Solution: pseudonyms, remove identifying details, consent explaining confidentiality limits.', 'Risk 2: insecure storage. Solution: encrypted, password-protected storage accessible only to the researcher; delete recordings after transcription.', 'Also: get ethical approval and stress that participation is voluntary.'],
            'answer': 'Protect identities with pseudonyms and secure the data.',
            'check': 'The solutions address both participants\' identities and data storage ✓.'},
        'mistakes': ['Confusing anonymity with confidentiality.', 'Promising anonymity in face-to-face interviews.', 'Storing data on shared or unencrypted devices.', 'Pressuring friends or students to take part.'],
        'real_world': 'Organisations that leak personal data can face large fines under data protection laws, so universities train researchers in secure data handling.',
        'exam_strategy': 'Link every ethical risk you identify to a specific, practical solution.',
        'recap': ['Inform and get consent.', 'Voluntary and withdrawable.', 'Anonymity ≠ confidentiality.', 'Store data securely.']},
    T4: {
        'overview': 'A research report communicates what you did, what you found and why it matters. Most follow a standard structure.',
        'key_terms': ['IMRaD', 'Title', 'Abstract', 'Introduction', 'Methods', 'Results', 'Discussion', 'Limitations', 'Recommendations', 'Appendix', 'Poster', 'Oral presentation'],
        'explanation': [
            'IMRaD structure: the introduction gives background, the gap and the research question; methods describe design, participants, instruments, procedure and analysis in enough detail to repeat the study; results report findings without interpretation, using tables and figures; the discussion interprets findings, links them to the literature, notes limitations and suggests implications and future research. A conclusion and recommendations may follow.',
            'The abstract (often 150 to 250 words) summarises the purpose, methods, main findings and conclusion, and is written last. Tables and figures need numbered titles and must be referred to in the text. Appendices hold supporting material such as questionnaires and consent forms. Use past tense for what you did and found.',
            'Presentations need a clear story: question, method, key findings, so what. A rough guide is about one slide per minute, so a 10-minute talk needs around 10 slides, with few words and clear visuals. Posters present the same story visually: large title, short sections, graphs and a QR code or contact details for more information.'],
        'formulas_label': 'Report structure',
        'formulas': ['Title and abstract (written last)', 'Introduction: background, gap, question', 'Methods: design, participants, instruments, procedure, analysis', 'Results: findings only', 'Discussion: interpretation, literature, limitations, implications'],
        'steps': ['Draft methods and results first.', 'Write the discussion and introduction.', 'Write the abstract last.', 'Check tables, figures and references.'],
        'worked_example': {
            'problem': 'Sort these sentences into report sections: (a) "Twelve students were interviewed in March 2025." (b) "This finding supports Asante (2019)." (c) "68% of respondents used the library weekly."',
            'steps': ['(a) Describes what was done and with whom: methods.', '(b) Interprets a finding against the literature: discussion.', '(c) Reports a finding without interpretation: results.'],
            'answer': '(a) methods, (b) discussion, (c) results.',
            'check': 'Results report; discussion interprets: keeping these separate is a key report-writing skill ✓.'},
        'mistakes': ['Interpreting findings in the results section.', 'Writing the abstract first and not updating it.', 'Hiding limitations.', 'Overloading slides with text.'],
        'real_world': 'Nearly all scientific journals use the IMRaD structure, so learning it now prepares you to read and write published research.',
        'exam_strategy': 'If asked what belongs in a section, give two or three specific items; vague answers ("talk about the study") score poorly.',
        'recap': ['IMRaD.', 'Abstract last.', 'Results report, discussion interprets.', 'Present a clear story.']},
}

QUESTIONS = [
    # T1
    Q(T1, '"Is the library quiet and well stocked?" is a poor question because it is:', ['double-barrelled', 'open', 'a Likert item', 'too short'], 0, 'Two issues in one.'),
    Q(T1, '"Don\'t you agree that fees are too high?" is:', ['a leading question', 'a neutral question', 'an open question', 'a pilot question'], 0, 'Pushes towards an answer.'),
    Q(T1, 'Testing a questionnaire on a few people before the main study is a:', ['pilot study', 'meta-analysis', 'focus group', 'census'], 0, 'Finds problems early.'),
    Q(T1, 'An interview using a guide with flexibility for follow-up questions is:', ['semi-structured', 'structured', 'a closed questionnaire', 'a census'], 0, 'Allows probing.'),
    Q(T1, 'Answering in a way that makes you look good is:', ['social desirability bias', 'sampling bias', 'confirmation bias', 'recall bias only'], 0, 'Reduce with anonymity.'),
    Q(T1, 'A rating scale from "strongly disagree" to "strongly agree" is a:', ['Likert scale', 'open question', 'focus group', 'Boolean search'], 0, 'Common survey format.'),
    # T2
    Q(T2, 'If 45 of 150 respondents agree, the percentage agreeing is:', ['30%', '45%', '15%', '3.3%'], 0, '45/150.', ans=30),
    Q(T2, 'The mean of the Likert responses 5, 4, 4, 3, 2 is:', ['3.6', '4', '3', '18'], 0, '18/5.', ans=3.6, num=True),
    Q(T2, 'Weekly library use rises from 40% to 50%. This is a rise of:', ['10 percentage points (a 25% increase)', '10% exactly', '25 percentage points', '50%'], 0, 'Points vs percent.'),
    Q(T2, 'In thematic analysis, labelling meaningful segments of data is called:', ['coding', 'sampling', 'piloting', 'triangulating'], 0, 'Codes become themes.'),
    Q(T2, 'A t-test is used to:', ['compare the means of two groups', 'count themes', 'choose a sample', 'format references'], 0, 'Inferential test.'),
    Q(T2, 'The best chart for comparing categories such as faculties is usually a:', ['bar chart', 'scatter plot', 'line graph of time', 'histogram'], 0, 'Discrete categories.'),
    # T3
    Q(T3, 'Anonymity means:', ['no one, including the researcher, can link data to individuals', 'the researcher knows identities but keeps them private', 'names are published', 'participants cannot withdraw'], 0, 'Confidentiality is different.'),
    Q(T3, 'Replacing names with codes and storing the key separately is:', ['pseudonymisation', 'anonymisation', 'triangulation', 'fabrication'], 0, 'Reversible with the key.'),
    Q(T3, 'Kenya\'s main data protection law is the:', ['Data Protection Act 2019', 'GDPR 2018', 'POPIA 2013', 'Data Protection Act 2023'], 0, 'Nigeria\'s is 2023.'),
    Q(T3, 'A participant information sheet explains:', ['the study\'s purpose, risks, data use and how to withdraw', 'the results', 'only the researcher\'s name', 'the marking scheme'], 0, 'Basis of informed consent.'),
    Q(T3, 'Extra care with consent is needed when a lecturer surveys their own students because:', ['students may feel pressured to take part', 'students cannot read', 'it is illegal', 'students always lie'], 0, 'Power imbalance.'),
    Q(T3, 'A data management plan sets out:', ['how data are stored, accessed, kept and destroyed', 'the research question', 'the reference style', 'the sample size only'], 0, 'Secure handling.'),
    # T4
    Q(T4, 'IMRaD stands for:', ['introduction, methods, results and discussion', 'ideas, methods, references and data', 'introduction, materials, review and design', 'inquiry, measures, results and debate'], 0, 'Standard structure.'),
    Q(T4, 'The abstract is usually written:', ['last', 'first', 'before the research starts', 'only for posters'], 0, 'Summarises the whole.'),
    Q(T4, '"This finding supports Asante (2019)" belongs in the:', ['discussion', 'results', 'methods', 'abstract only'], 0, 'Interpretation.'),
    Q(T4, '"Twelve students were interviewed in March" belongs in the:', ['methods', 'discussion', 'results', 'introduction'], 0, 'What was done.'),
    Q(T4, 'Using about one slide per minute, a 10-minute talk needs about:', ['10 slides', '30 slides', '2 slides', '60 slides'], 0, 'Rough guide.'),
    Q(T4, 'Limitations of a study are normally discussed in the:', ['discussion', 'abstract only', 'title', 'reference list'], 0, 'Honest appraisal.'),
]

FLASH = [
    ['Double-barrelled question', 'Asks about two things at once.'],
    ['Pilot study', 'Small trial run to test instruments and procedures.'],
    ['Semi-structured interview', 'Guide of questions with flexibility for probes.'],
    ['Percentage points', 'Simple difference between two percentages.'],
    ['Thematic analysis', 'Coding data and grouping codes into themes.'],
    ['Anonymity vs confidentiality', 'Anonymous: unlinkable; confidential: known but not revealed.'],
    ['IMRaD', 'Introduction, methods, results, discussion.'],
    ['Abstract', 'Short summary of purpose, methods, findings and conclusion, written last.'],
]
