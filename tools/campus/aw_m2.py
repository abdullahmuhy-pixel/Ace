"""Academic Writing and Research Methods, module 2: Writing academic essays."""
from verify import Q
T1, T2, T3, T4 = ('The writing process and planning', 'Paragraphs and essay structure', 'Academic style and tone', 'Editing and proofreading')
assert 0.1 * 2000 == 200 and 2000 - 2 * 200 == 1600 and 1600 / 4 == 400
assert 2000 * 0.9 == 1800 and round(2000 * 1.1, 6) == 2200
assert 2350 - 2000 == 350 and round(350 / 2350 * 100, 1) == 14.9
assert 0.1 * 3000 == 300 and (3000 - 600) / 6 == 400

MODULE = {
    'title': 'Writing academic essays',
    'topics': [T1, T2, T3, T4],
    'overview': 'Academic writing is a process, not a single draft. This module covers understanding the task and planning, building clear paragraphs and essays, writing in an academic style, and editing and proofreading so that your work says exactly what you mean.',
    'key_terms': ['Task words', 'Thesis statement', 'Outline', 'Topic sentence', 'PEEL paragraph', 'Cohesion', 'Signposting', 'Hedging', 'Register', 'Revising', 'Editing', 'Proofreading'],
    'explanation': [
        'Good essays start with analysing the question: identify the task word (discuss, evaluate, compare), the topic and the limits. Research and planning come before drafting, and a clear thesis statement gives the whole essay direction.',
        'An essay has an introduction that sets out the context, thesis and plan; body paragraphs that each develop one point with evidence and analysis; and a conclusion that draws the argument together. Signposting and linking words guide the reader.',
        'Academic style is precise, objective and cautious, using hedging to avoid overclaiming. Revising improves content and structure; editing improves sentences and style; proofreading catches the final errors.'],
    'quick_facts': [
        'Underline the task word: discuss, analyse, evaluate, compare, explain.',
        'One paragraph, one main idea, opened by a topic sentence.',
        'PEEL: point, evidence, explanation, link.',
        'Introduction and conclusion: roughly 10% of the word count each.',
        'Revise (big picture) before you edit and proofread (detail).'],
}

NOTES = {
    T1: {
        'overview': 'Writing works best as a process: understand the task, research, plan, draft, then revise.',
        'key_terms': ['Task word', 'Topic', 'Limiting words', 'Brainstorming', 'Mind map', 'Outline', 'Thesis statement', 'Drafting', 'Word count'],
        'explanation': [
            'Break the question into three parts: the task word (what to do), the topic (what to write about) and limiting words (scope). "Evaluate the impact of mobile banking on financial inclusion in Kenya since 2007" asks you to judge (evaluate), about mobile banking and financial inclusion, limited to Kenya and the period since 2007. "Describe" asks what; "explain" asks why or how; "discuss" asks for different views; "evaluate" asks for a judgement based on evidence; "compare" asks for similarities and differences.',
            'Brainstorm or mind-map ideas, research, then build an outline. A thesis statement is one or two sentences stating your main argument, such as "Mobile banking has greatly widened access to basic financial services in Kenya, although gaps remain for rural women and the very poor." Every paragraph should support or qualify it.',
            'Plan your word count. In a 2000-word essay, allow about 200 words for the introduction, 200 for the conclusion and 1600 for the body, for example four paragraphs of 400 words. Many universities accept 10% either side (1800 to 2200 words), but check your own rules.'],
        'formulas_label': 'Planning',
        'formulas': ['Question = task word + topic + limits', 'Describe (what), explain (why/how), discuss (views), evaluate (judge), compare (similar/different)', 'Introduction ≈ 10%, conclusion ≈ 10%, body ≈ 80%', 'Thesis: your answer to the question in one or two sentences'],
        'steps': ['Analyse the question.', 'Brainstorm and research.', 'Write a thesis and outline.', 'Draft, then revise.'],
        'worked_example': {
            'problem': 'Plan a 3000-word essay with an introduction, conclusion and six body paragraphs.',
            'steps': ['Introduction ≈ 10% = 300 words; conclusion ≈ 300 words.', 'Body = 3000 − 600 = 2400 words.', '2400 ÷ 6 = 400 words per body paragraph.'],
            'answer': '300 + 6 × 400 + 300 = 3000 words.',
            'check': 'The parts add up to the full word count ✓.'},
        'mistakes': ['Answering a different question from the one set.', 'Describing when the task asks you to evaluate.', 'Starting to draft without a plan.', 'Writing a thesis that is just a topic ("This essay is about mobile banking").'],
        'real_world': 'Professional reports and policy briefs follow the same process: understand the brief, research, outline the key message, then draft and revise.',
        'exam_strategy': 'In exams, spend the first five minutes analysing the question and jotting a quick plan; it saves time later and keeps the answer focused.',
        'recap': ['Task word, topic, limits.', 'Thesis gives direction.', 'Outline before drafting.', 'Budget the word count.']},
    T2: {
        'overview': 'Clear structure helps the reader follow your argument. Each part of an essay has a job.',
        'key_terms': ['Introduction', 'Thesis statement', 'Body paragraph', 'Topic sentence', 'PEEL', 'Evidence', 'Analysis', 'Transition', 'Signposting', 'Conclusion', 'Cohesion'],
        'explanation': [
            'The introduction moves from general context to your specific focus: background, a definition of key terms if needed, the thesis statement and a brief outline of how the essay will proceed. The conclusion summarises the main points, restates the thesis in light of the argument and may note implications or limits. It should not introduce new evidence.',
            'Each body paragraph develops one main idea. The PEEL structure works well: Point (topic sentence), Evidence (data, quotation or example, with a citation), Explanation (analyse how the evidence supports the point) and Link (back to the thesis or on to the next paragraph). Analysis is where most marks are earned: do not let quotations speak for themselves.',
            'Cohesion makes writing flow. Transition words show relationships: addition (furthermore, moreover), contrast (however, in contrast), cause and effect (therefore, as a result) and example (for instance). Signposting tells the reader where the essay is going ("This section examines…", "Turning to the economic effects…").'],
        'formulas_label': 'Structures',
        'formulas': ['Introduction: context → focus → thesis → outline', 'PEEL: point, evidence, explanation, link', 'Conclusion: summary → thesis restated → implications (no new evidence)', 'Transitions: however, therefore, furthermore, for instance'],
        'steps': ['Write a topic sentence.', 'Add cited evidence.', 'Explain and analyse it.', 'Link back to the thesis.'],
        'worked_example': {
            'problem': 'Turn this note into a PEEL paragraph outline: "Mobile money helps rural households cope with shocks (Jack and Suri, 2014)."',
            'steps': ['Point: Mobile money has made rural households more resilient to financial shocks.', 'Evidence: Jack and Suri (2014) found that Kenyan households using M-Pesa maintained consumption after shocks, while non-users cut back.', 'Explanation: Cheap transfers let relatives send help quickly over long distances. Link: This supports the thesis that mobile banking has widened access to financial security.'],
            'answer': 'A paragraph with a clear point, cited evidence, analysis and a link.',
            'check': 'Each PEEL element is present and the evidence is cited ✓.'},
        'mistakes': ['Packing several ideas into one paragraph.', 'Dropping in quotations without analysis.', 'Adding new evidence in the conclusion.', 'Using "however" when no contrast follows.'],
        'real_world': 'Journalists use a similar pattern: a clear opening line, supporting facts and quotes, and explanation of why it matters.',
        'exam_strategy': 'Start every body paragraph with a topic sentence that could stand alone as a mini-answer; examiners skim these first.',
        'recap': ['Intro: context to thesis.', 'PEEL paragraphs.', 'Analysis earns marks.', 'Transitions create flow.']},
    T3: {
        'overview': 'Academic style is clear, precise, objective and appropriately cautious. It is not about long words.',
        'key_terms': ['Register', 'Formality', 'Objectivity', 'Hedging', 'Boosters', 'Nominalisation', 'Passive voice', 'Concision', 'Inclusive language', 'Jargon'],
        'explanation': [
            'Use a formal register: avoid contractions ("does not" rather than "doesn\'t"), slang, rhetorical questions and vague words like "things" or "stuff". Be precise: "a 12% rise in enrolment between 2015 and 2020" is better than "a big increase".',
            'Academic claims are usually hedged to reflect the strength of evidence: "suggests", "may", "appears to", "is likely to", "in most cases". Overclaiming ("this proves that…") is a common weakness; reserve strong boosters ("clearly demonstrates") for very strong evidence. The passive voice ("the samples were analysed") can focus on the action, though many fields now accept "we" or "I" where appropriate.',
            'Concise writing cuts filler: "due to the fact that" becomes "because", "in order to" becomes "to". Long sentences are not more academic; aim for clarity. Use inclusive language (people with disabilities rather than outdated labels; gender-neutral terms where possible) and explain technical terms when first used.'],
        'formulas_label': 'Style checklist',
        'formulas': ['Formal: no contractions or slang', 'Precise: numbers, dates, specifics', 'Hedged: may, suggests, appears, likely', 'Concise: cut filler phrases', 'Inclusive and clearly defined terms'],
        'steps': ['Remove informal words.', 'Replace vague words with precise ones.', 'Check claims match the evidence (hedge if needed).', 'Cut unnecessary words.'],
        'worked_example': {
            'problem': 'Rewrite academically: "Loads of studies prove that social media is really bad for teenagers."',
            'steps': ['"Loads of" is informal and vague: specify ("Several recent studies").', '"Prove" overclaims: use "suggest".', '"Really bad" is vague: name the effect and population.'],
            'answer': 'Several recent studies suggest that heavy social media use may be associated with poorer sleep and lower well-being among adolescents.',
            'check': 'The new sentence is formal, precise and hedged, and does not claim causation ✓.'},
        'mistakes': ['Thinking longer words always sound more academic.', 'Using "prove" for correlational findings.', 'Writing contractions.', 'Using undefined jargon.'],
        'real_world': 'Scientific advice to governments uses careful hedging ("high confidence", "likely") so decision-makers understand how certain the evidence is.',
        'exam_strategy': 'Keep a list of hedging verbs (suggests, indicates, appears) and use them when interpreting evidence.',
        'recap': ['Formal and precise.', 'Hedge claims appropriately.', 'Be concise.', 'Inclusive language.']},
    T4: {
        'overview': 'Revising, editing and proofreading turn a draft into a finished piece. Each works at a different level.',
        'key_terms': ['Revising', 'Editing', 'Proofreading', 'Reverse outline', 'Read aloud', 'Feedback', 'Word limit', 'Subject–verb agreement', 'Run-on sentence', 'Sentence fragment'],
        'explanation': [
            'Revising looks at the big picture: does the essay answer the question, is the argument logical, is the structure clear, and is there enough evidence and analysis? A reverse outline (writing down the main point of each paragraph after drafting) quickly reveals gaps, repetition and paragraphs in the wrong order.',
            'Editing works at sentence level: clarity, concision, transitions and academic style. If you are over the word limit, editing is where you cut: an essay of 2350 words with a 2000-word limit must lose 350 words, about 15%. Cut repetition and filler first, then weaker points.',
            'Proofreading is the final check for errors in spelling, grammar, punctuation, formatting and references. Common grammar errors include subject–verb agreement ("The results of the study shows" should be "show"), run-on sentences (two sentences joined only by a comma) and fragments (incomplete sentences). Reading aloud, printing the text or changing the font helps you see what is really on the page rather than what you meant to write.'],
        'formulas_label': 'Three levels',
        'formulas': ['Revise: argument, structure, evidence', 'Edit: sentences, clarity, style, length', 'Proofread: spelling, grammar, punctuation, references', 'Order: revise → edit → proofread'],
        'steps': ['Leave time between drafting and revising.', 'Reverse-outline to check structure.', 'Edit for clarity and length.', 'Proofread last, ideally aloud.'],
        'worked_example': {
            'problem': 'Correct: "The data from the three surveys shows that students prefers online lectures, this is surprising."',
            'steps': ['"Data … show" (data is treated as plural in formal writing) and "students prefer" (plural subject).', 'The comma joins two sentences: a comma splice. Use a full stop or semicolon.', 'Make "this" clearer: "This finding is surprising."'],
            'answer': 'The data from the three surveys show that students prefer online lectures. This finding is surprising.',
            'check': 'Each verb now agrees with its subject, and the comma splice is gone ✓.'},
        'mistakes': ['Proofreading before revising the argument.', 'Relying only on a spell-checker.', 'Ignoring tutor feedback from earlier work.', 'Leaving no time between writing and checking.'],
        'real_world': 'Professional writers rarely publish a first draft; newspapers and journals have editors and proofreaders for exactly these stages.',
        'exam_strategy': 'Save the last five minutes of an exam to reread your answer for missing words and unclear sentences.',
        'recap': ['Revise the big picture.', 'Edit sentences.', 'Proofread last.', 'Read aloud.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'An essay question asks you to "evaluate". You should:', ['make a judgement based on evidence', 'only describe the topic', 'list facts without comment', 'give your opinion without evidence'], 0, 'Judge strengths and weaknesses.'),
    Q(T1, 'A thesis statement is:', ['a sentence or two stating your main argument', 'the essay title', 'the reference list', 'a summary of one source'], 0, 'Your answer to the question.'),
    Q(T1, 'In a 2000-word essay, about how many words should the introduction be?', ['200 words', '1000 words', '50 words', '600 words'], 0, 'About 10%.', ans=200),
    Q(T1, 'With a 10% allowance either side, a 2000-word essay may run up to:', ['2200 words', '2100 words', '2010 words', '3000 words'], 0, '2000 × 1.1.', ans=2200),
    Q(T1, '"Compare" asks you to:', ['identify similarities and differences', 'describe one thing only', 'give a definition', 'tell a story'], 0, 'Both sides.'),
    Q(T1, 'Which is the best thesis statement?', ['Mobile banking has widened access to financial services in Kenya, although gaps remain for the poorest.', 'This essay is about mobile banking.', 'Mobile banking is a topic many people discuss.', 'I will talk about money.'], 0, 'Takes a clear, arguable position.'),
    # T2
    Q(T2, 'In PEEL, the second "E" stands for:', ['explanation', 'evidence', 'example', 'ending'], 0, 'Point, evidence, explanation, link.'),
    Q(T2, 'A topic sentence:', ['states the main idea of a paragraph', 'lists references', 'ends the essay', 'is always a question'], 0, 'Opens the paragraph.'),
    Q(T2, 'A conclusion should NOT:', ['introduce new evidence', 'summarise the main points', 'restate the thesis', 'note implications'], 0, 'New evidence belongs in the body.'),
    Q(T2, 'Which transition signals contrast?', ['However', 'Furthermore', 'For instance', 'Therefore'], 0, 'Shows a different view.'),
    Q(T2, 'Most marks in a body paragraph usually come from:', ['analysis of the evidence', 'the length of quotations', 'the number of adjectives', 'repeating the question'], 0, 'Explain why it matters.'),
    Q(T2, '"This section examines the economic effects" is an example of:', ['signposting', 'hedging', 'a fallacy', 'plagiarism'], 0, 'Guides the reader.'),
    # T3
    Q(T3, 'Which sentence is most appropriately hedged?', ['The results suggest that sleep may affect memory.', 'The results prove sleep controls memory.', 'Sleep obviously fixes memory.', 'Everyone knows sleep matters.'], 0, 'Cautious claim.'),
    Q(T3, 'A more concise version of "due to the fact that" is:', ['because', 'in light of the circumstance that', 'owing to the fact that', 'as a result of the fact that'], 0, 'Cut filler.'),
    Q(T3, 'Academic writing generally avoids:', ['contractions and slang', 'evidence', 'precise numbers', 'citations'], 0, 'Formal register.'),
    Q(T3, '"A 12% rise in enrolment between 2015 and 2020" is better than "a big increase" because it is:', ['precise', 'longer', 'hedged', 'informal'], 0, 'Specific numbers.'),
    Q(T3, 'Words such as "may", "suggests" and "appears" are used for:', ['hedging', 'boosting', 'signposting', 'referencing'], 0, 'Express caution.'),
    Q(T3, 'Technical terms should be:', ['explained when first used', 'avoided completely', 'used as often as possible', 'written in capitals'], 0, 'Clarity.'),
    # T4
    Q(T4, 'Checking whether the argument answers the question and is well structured is:', ['revising', 'proofreading', 'formatting', 'referencing'], 0, 'Big-picture level.'),
    Q(T4, 'An essay of 2350 words has a 2000-word limit. How many words must be cut?', ['350 words', '235 words', '200 words', '150 words'], 0, '2350 − 2000.', ans=350),
    Q(T4, '"The results of the study shows" contains an error in:', ['subject–verb agreement', 'spelling', 'punctuation only', 'referencing'], 0, 'Results show.'),
    Q(T4, 'Two complete sentences joined only by a comma is a:', ['comma splice', 'fragment', 'hedge', 'thesis'], 0, 'A type of run-on.'),
    Q(T4, 'The best order of checking is:', ['revise, edit, proofread', 'proofread, edit, revise', 'edit, proofread, revise', 'proofread only'], 0, 'Big to small.'),
    Q(T4, 'A useful proofreading technique is:', ['reading your work aloud', 'only using a spell-checker', 'reading it immediately after writing', 'skimming the conclusion'], 0, 'Hear errors.'),
]

FLASH = [
    ['Task word', 'The instruction in a question: describe, explain, discuss, evaluate, compare.'],
    ['Thesis statement', 'One or two sentences stating your main argument.'],
    ['PEEL', 'Point, evidence, explanation, link.'],
    ['Topic sentence', 'Opening sentence stating a paragraph\'s main idea.'],
    ['Hedging', 'Cautious language: may, suggests, appears.'],
    ['Signposting', 'Phrases that tell the reader where the essay is going.'],
    ['Revising', 'Improving argument, structure and evidence.'],
    ['Comma splice', 'Two sentences joined only by a comma.'],
]
