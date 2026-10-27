"""Academic Writing and Research Methods, module 1: Reading and thinking critically."""
from verify import Q
T1, T2, T3, T4 = ('Reading academic texts', 'Finding and evaluating sources', 'Critical thinking and arguments', 'Logical fallacies')
assert 40 / 5 * 20 == 160

MODULE = {
    'title': 'Reading and thinking critically',
    'topics': [T1, T2, T3, T4],
    'overview': 'University work starts with reading well and judging what you read. This module covers efficient reading strategies, how to find and evaluate scholarly sources, how arguments are built from claims, reasons and evidence, and the common fallacies that weaken them.',
    'key_terms': ['Skimming', 'Scanning', 'SQ3R', 'Primary source', 'Secondary source', 'Peer review', 'CRAAP test', 'Claim', 'Premise', 'Evidence', 'Deductive reasoning', 'Inductive reasoning', 'Fallacy'],
    'explanation': [
        'Academic texts are dense, so read with a purpose. Skim for the main idea, scan for specific information, and read closely only what matters. Active methods such as SQ3R and note-making turn reading into understanding.',
        'Not all sources are equal. Peer-reviewed journal articles and scholarly books are the backbone of academic work; websites and news need careful checking. Tools such as the CRAAP test help judge currency, relevance, authority, accuracy and purpose.',
        'Critical thinking means analysing arguments rather than accepting them. An argument has a claim supported by reasons and evidence. Good arguments are valid and well supported; fallacies are common errors in reasoning that make arguments look stronger than they are.'],
    'quick_facts': [
        'Skim for gist; scan for specific facts.',
        'SQ3R: survey, question, read, recite, review.',
        'Primary sources report original research or evidence; secondary sources interpret them.',
        'CRAAP: currency, relevance, authority, accuracy, purpose.',
        'Attack the argument, not the person (avoid ad hominem).'],
}

NOTES = {
    T1: {
        'overview': 'Reading at university is active. Strategies such as skimming, scanning and SQ3R help you understand more in less time.',
        'key_terms': ['Skimming', 'Scanning', 'Close reading', 'SQ3R', 'Abstract', 'Annotation', 'Note-making', 'Cornell notes'],
        'explanation': [
            'Before reading a journal article in full, read its abstract, introduction and conclusion, and look at headings, figures and tables. This skimming tells you whether it is relevant. Scanning is searching quickly for a specific item, such as a date, figure or keyword. Close reading is careful, critical reading of the parts that matter.',
            'SQ3R is a five-step method: Survey (skim the structure), Question (turn headings into questions), Read (to answer those questions), Recite (say or write the answers from memory) and Review (go over the material later). It works because it makes you think about the text and test your memory, not just highlight it.',
            'Make notes in your own words with the source details recorded at once, so you can reference properly later and avoid accidental plagiarism. Cornell notes divide the page into notes, cue questions and a summary. Plan your reading time realistically: 40 pages at 20 minutes per 5 pages is 160 minutes, close to 3 hours.'],
        'formulas_label': 'Strategies',
        'formulas': ['Skim: abstract, headings, conclusion', 'Scan: hunt for a specific fact', 'SQ3R: survey, question, read, recite, review', 'Record full source details with every note'],
        'steps': ['Decide your purpose for reading.', 'Skim to check relevance.', 'Read closely the useful sections.', 'Make notes in your own words with the reference.'],
        'worked_example': {
            'problem': 'You have a week to find evidence for an essay and a reading list of 12 journal articles. How should you approach them?',
            'steps': ['Skim each abstract and conclusion to sort them into "useful", "maybe" and "not relevant".', 'Read the useful ones closely using SQ3R, focusing on methods, findings and limitations.', 'Make notes in your own words, recording author, year, title and page numbers for quotations.'],
            'answer': 'Skim first to select, then read closely and make referenced notes.',
            'check': 'This avoids spending hours on articles you will not use ✓.'},
        'mistakes': ['Reading every article from start to finish.', 'Highlighting without making notes.', 'Copying sentences into notes without quotation marks.', 'Forgetting to record page numbers.'],
        'real_world': 'Researchers routinely read only the abstract of most papers they find; they save full reading for the few that matter most.',
        'exam_strategy': 'In timed reading tasks, read the questions first, then scan the text for the answers.',
        'recap': ['Skim, scan, close read.', 'SQ3R makes reading active.', 'Notes in your own words.', 'Record references as you go.']},
    T2: {
        'overview': 'Good academic work rests on good sources. Learn where to find them and how to judge their quality.',
        'key_terms': ['Primary source', 'Secondary source', 'Tertiary source', 'Peer review', 'Scholarly journal', 'Database', 'Boolean operators', 'Grey literature', 'CRAAP test', 'Predatory journal'],
        'explanation': [
            'Primary sources present original evidence: a research article reporting an experiment, a survey dataset, a historical letter or a law. Secondary sources interpret primary ones: review articles, textbooks and commentary. Tertiary sources, such as encyclopaedias, summarise further and are useful for orientation but rarely cited in university essays.',
            'Peer review means experts checked an article before publication. Find scholarly sources through library databases and Google Scholar, using Boolean operators: AND narrows a search ("malaria AND children"), OR broadens it ("teenager OR adolescent") and NOT excludes ("Java NOT coffee"). Quotation marks search for an exact phrase.',
            'Evaluate every source with the CRAAP test: Currency (is it recent enough?), Relevance (does it address your question?), Authority (who wrote it and are they qualified?), Accuracy (is it supported by evidence and peer-reviewed?) and Purpose (to inform, persuade or sell?). Beware predatory journals that publish anything for a fee without proper review.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Primary: original evidence; secondary: interpretation', 'AND narrows, OR broadens, NOT excludes', 'CRAAP: currency, relevance, authority, accuracy, purpose', 'Prefer peer-reviewed sources'],
        'steps': ['Turn your topic into keywords and synonyms.', 'Search databases with Boolean operators.', 'Filter by date and peer review.', 'Evaluate each source with CRAAP.'],
        'worked_example': {
            'problem': 'You are researching the effect of mobile money on small businesses in East Africa. Write a search string and say which result type you should prioritise.',
            'steps': ['Keywords: mobile money, small business, East Africa (and synonyms).', 'Search: ("mobile money" OR "M-Pesa") AND ("small business" OR SME) AND (Kenya OR Tanzania OR Uganda).', 'Prioritise recent peer-reviewed studies with original data (primary sources).'],
            'answer': 'A Boolean search as above, prioritising peer-reviewed primary studies.',
            'check': 'OR groups synonyms and AND combines concepts, which is the correct structure ✓.'},
        'mistakes': ['Citing Wikipedia as an academic source.', 'Using only the first page of Google results.', 'Assuming anything published is reliable.', 'Ignoring the date of the source.'],
        'real_world': 'During the COVID-19 pandemic many unreviewed preprints were reported as facts by the media; some were later corrected or withdrawn after peer review.',
        'exam_strategy': 'When asked to evaluate a source, work through each letter of CRAAP and give one specific point for each.',
        'recap': ['Primary vs secondary.', 'Peer review signals quality.', 'Boolean searching.', 'CRAAP test.']},
    T3: {
        'overview': 'Critical thinking means analysing and evaluating arguments. Every argument has a claim, reasons and evidence.',
        'key_terms': ['Argument', 'Claim (thesis)', 'Premise', 'Conclusion', 'Evidence', 'Assumption', 'Counter-argument', 'Deductive reasoning', 'Inductive reasoning', 'Validity', 'Soundness'],
        'explanation': [
            'An argument gives reasons (premises) for a conclusion (the claim). Evidence supports premises: data, examples, expert testimony and research findings. Unstated assumptions link reasons to claims and are often where arguments are weakest, so make them explicit.',
            'Deductive reasoning moves from general premises to a certain conclusion: "All mammals breathe air; whales are mammals; therefore whales breathe air." It is valid if the conclusion follows necessarily, and sound if it is valid and the premises are true. Inductive reasoning moves from specific observations to a probable generalisation: "Every swan I have seen is white, so all swans are white" (which black swans in Australia disprove).',
            'Strong academic writing anticipates counter-arguments and responds to them (rebuttal). The Toulmin model describes an argument as a claim, grounds (evidence), a warrant (the link), backing, a qualifier ("probably", "in most cases") and a rebuttal. Using qualifiers carefully, rather than overclaiming, is a mark of good academic style.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Argument = claim + reasons + evidence', 'Deductive: certain if valid and premises true (sound)', 'Inductive: probable generalisation', 'Toulmin: claim, grounds, warrant, backing, qualifier, rebuttal'],
        'steps': ['Identify the claim.', 'List the reasons and evidence.', 'Find hidden assumptions.', 'Test against counter-arguments.'],
        'worked_example': {
            'problem': 'Analyse: "Students who attend more lectures get higher marks, so lecture attendance should be compulsory."',
            'steps': ['Claim: attendance should be compulsory. Reason: attendance is linked with higher marks.', 'Hidden assumption: attending causes higher marks. But motivated students may both attend more and study more (correlation, not causation).', 'Counter-argument: compulsion may not create engagement; evidence would need to show causation.'],
            'answer': 'The argument rests on an unproven causal assumption.',
            'check': 'Identifying the assumption and offering an alternative explanation is the core of critical analysis ✓.'},
        'mistakes': ['Summarising instead of evaluating.', 'Treating inductive conclusions as certain.', 'Ignoring counter-arguments.', 'Confusing a valid argument with a true conclusion.'],
        'real_world': 'Courts weigh arguments in a similar way: claims must be supported by evidence, and the other side presents rebuttals.',
        'exam_strategy': 'When asked to "critically evaluate", always include strengths, weaknesses and a reasoned judgement.',
        'recap': ['Claims need reasons and evidence.', 'Find the assumptions.', 'Deductive vs inductive.', 'Address counter-arguments.']},
    T4: {
        'overview': 'A fallacy is a flaw in reasoning that makes an argument seem persuasive when it is not. Recognising fallacies protects your own writing too.',
        'key_terms': ['Ad hominem', 'Straw man', 'False dilemma', 'Slippery slope', 'Appeal to authority', 'Bandwagon', 'Hasty generalisation', 'Post hoc', 'Circular reasoning', 'Red herring'],
        'explanation': [
            'Ad hominem attacks the person rather than the argument ("You cannot trust her view on tax; she failed maths at school"). A straw man misrepresents an opponent\'s argument to make it easier to attack. A red herring distracts with an irrelevant point.',
            'A false dilemma presents only two options when more exist ("Either we ban cars or the city will choke"). A slippery slope claims one step will inevitably lead to extreme outcomes without evidence. Circular reasoning assumes what it is trying to prove.',
            'Hasty generalisation draws a broad conclusion from too few cases. Post hoc (ergo propter hoc) assumes that because B followed A, A caused B. An appeal to (inappropriate) authority relies on someone without relevant expertise, and the bandwagon fallacy argues something is true because many people believe it.'],
        'formulas_label': 'Common fallacies',
        'formulas': ['Ad hominem: attack the person', 'Straw man: distort the argument', 'False dilemma: only two options', 'Slippery slope: chain of unproven consequences', 'Hasty generalisation: too few cases', 'Post hoc: after, therefore because of'],
        'steps': ['Read the argument carefully.', 'Ask what the reasoning relies on.', 'Match it to a fallacy pattern.', 'Explain why the reasoning fails.'],
        'worked_example': {
            'problem': 'Identify the fallacy: "I wore my lucky shirt and we won the match, so the shirt helped us win."',
            'steps': ['The win followed wearing the shirt.', 'The speaker assumes the earlier event caused the later one.', 'There is no evidence of a causal link.'],
            'answer': 'Post hoc (false cause).',
            'check': 'It is not a hasty generalisation, because no general rule about many cases is being drawn ✓.'},
        'mistakes': ['Calling any personal criticism ad hominem (it must replace the argument).', 'Confusing straw man and red herring.', 'Thinking all appeals to experts are fallacies.', 'Naming a fallacy without explaining it.'],
        'real_world': 'Political debates and advertising are full of false dilemmas and bandwagon appeals; spotting them makes you a harder person to manipulate.',
        'exam_strategy': 'Name the fallacy and explain in one sentence how the reasoning fails; the explanation usually carries more marks than the name.',
        'recap': ['Attack arguments, not people.', 'Represent opponents fairly.', 'Look for missing options.', 'Correlation in time is not causation.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Reading quickly to get the general idea of a text is:', ['skimming', 'scanning', 'close reading', 'paraphrasing'], 0, 'Gist.'),
    Q(T1, 'Searching a text quickly for a specific date or figure is:', ['scanning', 'skimming', 'summarising', 'annotating'], 0, 'Targeted search.'),
    Q(T1, 'In SQ3R, the "S" stands for:', ['survey', 'summarise', 'skim', 'study'], 0, 'Survey, question, read, recite, review.'),
    Q(T1, 'The best first part of a journal article to read to judge its relevance is the:', ['abstract', 'reference list', 'acknowledgements', 'appendix'], 0, 'A short summary.'),
    Q(T1, 'Why should you record source details with every note?', ['To reference correctly and avoid accidental plagiarism', 'To make notes longer', 'Because lecturers count notes', 'To avoid reading the source'], 0, 'Good practice.'),
    Q(T1, 'At 20 minutes per 5 pages, reading 40 pages takes about:', ['160 minutes', '80 minutes', '200 minutes', '8 minutes'], 0, '8 × 20.', ans=160),
    # T2
    Q(T2, 'A research article reporting a new experiment is a:', ['primary source', 'secondary source', 'tertiary source', 'grey source'], 0, 'Original evidence.'),
    Q(T2, 'The search "teenager OR adolescent" will:', ['broaden the results to include either term', 'narrow the results', 'exclude both terms', 'search for the exact phrase'], 0, 'OR broadens.'),
    Q(T2, 'Peer review means:', ['experts evaluated the work before publication', 'the author\'s friends read it', 'it was published online', 'students wrote it'], 0, 'Quality check.'),
    Q(T2, 'In the CRAAP test, "A" for authority asks:', ['whether the author is qualified and credible', 'how recent the source is', 'whether it is relevant', 'how long it is'], 0, 'Who wrote it.'),
    Q(T2, 'A textbook that summarises many studies is usually a:', ['secondary source', 'primary source', 'predatory journal', 'dataset'], 0, 'Interprets primary sources.'),
    Q(T2, 'A journal that publishes almost anything for a fee without proper review is:', ['a predatory journal', 'a peer-reviewed journal', 'an open-access database', 'a tertiary source'], 0, 'Avoid it.'),
    # T3
    Q(T3, 'In an argument, the claim is supported by:', ['reasons and evidence', 'the title', 'the word count', 'the conclusion only'], 0, 'Structure of argument.'),
    Q(T3, 'Reasoning from specific observations to a probable general conclusion is:', ['inductive', 'deductive', 'circular', 'a straw man'], 0, 'Probable, not certain.'),
    Q(T3, 'A deductive argument that is valid and has true premises is:', ['sound', 'inductive', 'a fallacy', 'hasty'], 0, 'Valid + true premises.'),
    Q(T3, 'An unstated belief that links a reason to a claim is:', ['an assumption', 'evidence', 'a citation', 'a qualifier'], 0, 'Often the weak point.'),
    Q(T3, 'Words like "probably" or "in most cases" in the Toulmin model are:', ['qualifiers', 'warrants', 'rebuttals', 'grounds'], 0, 'Limit the claim.'),
    Q(T3, 'Responding to a likely objection in your essay is called:', ['rebuttal', 'skimming', 'paraphrasing', 'scanning'], 0, 'Addresses counter-arguments.'),
    # T4
    Q(T4, '"Ignore his climate argument; he drives a big car." This is:', ['ad hominem', 'straw man', 'false dilemma', 'slippery slope'], 0, 'Attacks the person.'),
    Q(T4, '"Either we cut all public spending or the economy will collapse." This is:', ['a false dilemma', 'post hoc', 'ad hominem', 'circular reasoning'], 0, 'Only two options offered.'),
    Q(T4, 'Misrepresenting an opponent\'s view to make it easier to attack is:', ['a straw man', 'a red herring', 'a bandwagon', 'an appeal to authority'], 0, 'Distortion.'),
    Q(T4, '"I met two rude people from that town, so everyone there is rude." This is:', ['hasty generalisation', 'false dilemma', 'post hoc', 'circular reasoning'], 0, 'Too few cases.'),
    Q(T4, '"If we allow phones in class, soon students will never listen to anything." This is:', ['a slippery slope', 'ad hominem', 'a straw man', 'post hoc'], 0, 'Unproven chain.'),
    Q(T4, '"Millions of people use this remedy, so it must work." This is:', ['the bandwagon fallacy', 'a false dilemma', 'a straw man', 'circular reasoning'], 0, 'Popularity ≠ truth.'),
]

FLASH = [
    ['Skimming', 'Reading quickly for the main idea.'],
    ['SQ3R', 'Survey, question, read, recite, review.'],
    ['Primary source', 'Original evidence or research.'],
    ['Peer review', 'Expert evaluation before publication.'],
    ['CRAAP test', 'Currency, relevance, authority, accuracy, purpose.'],
    ['Inductive reasoning', 'From specific cases to a probable generalisation.'],
    ['Ad hominem', 'Attacking the person instead of the argument.'],
    ['False dilemma', 'Presenting only two options when more exist.'],
]
