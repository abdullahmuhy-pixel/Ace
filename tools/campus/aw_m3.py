"""Academic Writing and Research Methods, module 3: Referencing and academic integrity."""
from verify import Q
T1, T2, T3, T4 = ('Why and when to reference', 'Referencing styles: APA and Harvard', 'Quoting, paraphrasing and summarising', 'Plagiarism, collusion and AI tools')

MODULE = {
    'title': 'Referencing and academic integrity',
    'topics': [T1, T2, T3, T4],
    'overview': 'Using other people\'s work honestly is the foundation of academic life. This module explains why and when to reference, how to cite and list sources in APA and Harvard styles, how to quote, paraphrase and summarise, and how to avoid plagiarism, collusion and misuse of AI tools.',
    'key_terms': ['Citation', 'Reference list', 'Common knowledge', 'APA style', 'Harvard style', 'et al.', 'DOI', 'Direct quotation', 'Paraphrase', 'Summary', 'Plagiarism', 'Collusion', 'Contract cheating', 'Academic integrity'],
    'explanation': [
        'Referencing gives credit to the authors whose ideas you use, shows the evidence behind your claims, lets readers find your sources and protects you from plagiarism. Every idea, fact, figure or wording taken from a source needs a citation, except common knowledge.',
        'Author–date styles such as APA and Harvard cite the author and year in the text and give full details in an alphabetical reference list. Numbered styles (such as IEEE and Vancouver) are common in engineering and medicine. Always follow the style your department requires, consistently.',
        'Use quotations sparingly; paraphrase and summarise in your own words and structure, still with a citation. Plagiarism, collusion, contract cheating and undisclosed use of AI where it is not allowed are breaches of academic integrity with serious penalties.'],
    'quick_facts': [
        'Cite ideas, data and wording, not just quotations.',
        'APA in-text: (Mensah, 2021, p. 14); three or more authors: (Mensah et al., 2021).',
        'Reference list: alphabetical by first author\'s surname.',
        'A paraphrase still needs a citation.',
        'Check your course rules before using AI tools, and never cite a reference you have not checked exists.'],
}

NOTES = {
    T1: {
        'overview': 'Referencing is how academic writing shows where ideas and evidence come from. Knowing when to cite is as important as knowing how.',
        'key_terms': ['Citation', 'In-text citation', 'Reference list', 'Bibliography', 'Common knowledge', 'Secondary citation', 'Evidence trail'],
        'explanation': [
            'Reasons to reference: to acknowledge the work of others; to support your claims with evidence; to let readers check and follow up your sources; to show the breadth of your reading; and to avoid plagiarism. Good referencing makes your work more persuasive, not less original.',
            'Cite whenever you use someone else\'s words, ideas, data, theories, images or distinctive arguments, whether you quote, paraphrase or summarise. You do not need to cite common knowledge: facts widely known and undisputed in your field, such as "Nairobi is the capital of Kenya" or "water boils at 100 °C at sea level". If in doubt, cite.',
            'A reference list includes only sources you have cited; a bibliography may also include background reading (check which your department wants). If you only read a source through another author, use a secondary citation, for example in APA: (Piaget, 1952, as cited in Smith, 2020), and list only Smith (2020), the source you actually read.'],
        'formulas_label': 'When to cite',
        'formulas': ['Quotation: cite with page number', 'Paraphrase or summary: cite', 'Data, figures, images: cite', 'Common knowledge: no citation needed', 'Not sure: cite'],
        'steps': ['Ask: did this come from a source?', 'Ask: is it common knowledge in my field?', 'If from a source, add an in-text citation.', 'Add the full reference to the list.'],
        'worked_example': {
            'problem': 'Which needs a citation? (a) Ghana gained independence in 1957. (b) A survey\'s figure for the share of young Ghanaians who use mobile money daily. (c) The theory that intelligence has multiple forms.',
            'steps': ['(a) Widely known historical fact: common knowledge.', '(b) A specific statistic from a survey: cite.', '(c) A theory developed by a specific person (Gardner): cite.'],
            'answer': '(b) and (c) need citations; (a) does not.',
            'check': 'Specific data and named theories always need citations ✓.'},
        'mistakes': ['Citing only direct quotations.', 'Thinking that citing makes work less original.', 'Listing sources you did not read as if you read them.', 'Treating anything found online as common knowledge.'],
        'real_world': 'Researchers and journalists who fail to credit sources have lost degrees, jobs and reputations; good referencing protects your credibility.',
        'exam_strategy': 'In open-book or take-home exams, apply the same referencing rules as in essays unless told otherwise.',
        'recap': ['Credit, evidence, traceability.', 'Cite ideas, data and words.', 'Common knowledge excepted.', 'If in doubt, cite.']},
    T2: {
        'overview': 'APA and Harvard are author–date referencing styles. Details differ, so consistency and following your department\'s guide matter most.',
        'key_terms': ['APA 7th edition', 'Harvard', 'Narrative citation', 'Parenthetical citation', 'et al.', 'DOI', 'Hanging indent', 'Sentence case', 'Numbered styles'],
        'explanation': [
            'APA (7th edition) in-text citations: parenthetical (Mensah, 2021) or narrative Mensah (2021). Add a page number for quotations: (Mensah, 2021, p. 14). Two authors: (Mensah & Okafor, 2021), or "Mensah and Okafor (2021)" in the sentence. Three or more authors: (Mensah et al., 2021) from the first citation. Quotations of 40 words or more are set as indented block quotes without quotation marks.',
            'APA reference list: alphabetical by first author\'s surname, with a hanging indent. A book: Achebe, C. (1958). Things fall apart. Heinemann. (with the title in italics and in sentence case). A journal article: Jack, W., & Suri, T. (2014). Risk sharing and transactions costs: Evidence from Kenya\'s mobile money revolution. American Economic Review, 104(1), 183–223. https://doi.org/10.1257/aer.104.1.183 (journal name and volume in italics). A DOI (digital object identifier) is a permanent link and should be included when available.',
            'Harvard is a family of author–date styles that varies between universities. A typical version: in text (Mensah 2021, p. 14) and in the list Mensah, K. (2021) Title of book. Accra: Publisher. Numbered styles such as IEEE and Vancouver use [1] or superscript numbers in the text and list sources in order of first citation. Reference managers such as Zotero or Mendeley format references automatically, but always check the output.'],
        'formulas_label': 'APA 7 patterns',
        'formulas': ['In text: (Author, Year) or Author (Year)', 'Quote: (Author, Year, p. X)', 'Two authors: (A & B, Year); 3+: (A et al., Year)', 'Book: Author, A. (Year). Title in italics. Publisher.', 'Article: Author, A., & Author, B. (Year). Title. Journal, vol(issue), pages. DOI'],
        'steps': ['Identify the source type.', 'Collect author, year, title, publisher or journal details, DOI.', 'Format in-text citation.', 'Format the reference-list entry.'],
        'worked_example': {
            'problem': 'Give the APA 7 in-text citation for a quotation from page 45 of a 2019 article by Wanjiru, Otieno and Banda.',
            'steps': ['Three or more authors: use the first author and et al.', 'Include the year.', 'Quotation: add the page number.'],
            'answer': '(Wanjiru et al., 2019, p. 45)',
            'check': 'APA 7 uses et al. from the first citation for three or more authors ✓.'},
        'mistakes': ['Mixing styles in one essay.', 'Using initials in in-text citations.', 'Ordering the reference list by date of use in an author–date style.', 'Leaving out page numbers for quotations.'],
        'real_world': 'Journals reject submissions with inconsistent referencing; learning one style well now saves time throughout your degree.',
        'exam_strategy': 'Learn one book and one journal article pattern by heart in your department\'s style; most sources are one of these.',
        'recap': ['Author–date in text.', 'et al. for 3+ authors (APA).', 'Alphabetical list with full details.', 'Be consistent.']},
    T3: {
        'overview': 'You can use sources by quoting, paraphrasing or summarising. Each needs a citation; paraphrase and summary show understanding best.',
        'key_terms': ['Direct quotation', 'Block quotation', 'Paraphrase', 'Summary', 'Patchwriting', 'Reporting verb', 'Synthesis'],
        'explanation': [
            'A direct quotation copies exact words inside quotation marks, with a page number. Use quotations when the precise wording matters: a definition, a striking phrase or a statement you will analyse. Too many quotations make an essay look like a collection of other people\'s voices.',
            'A paraphrase restates a specific passage in your own words and sentence structure, at about the same level of detail. A summary condenses the main ideas of a longer text into a much shorter version. Both need citations. Patchwriting, which swaps a few words for synonyms while keeping the original structure, counts as plagiarism.',
            'To paraphrase well: read the passage until you understand it, put it away, write from memory, then check against the original for accuracy and accidental copying. Use reporting verbs to show your stance: neutral (states, notes, describes), supportive (demonstrates, shows) or tentative (suggests, claims). Synthesis combines several sources to make a point ("Both Mensah (2021) and Okafor (2022) found…").'],
        'formulas_label': 'Three ways to use a source',
        'formulas': ['Quotation: exact words, quotation marks, page number', 'Paraphrase: own words and structure, similar length, citation', 'Summary: main ideas only, much shorter, citation', 'Patchwriting = plagiarism'],
        'steps': ['Understand the passage.', 'Write from memory in your own words.', 'Compare with the original.', 'Add the citation.'],
        'worked_example': {
            'problem': 'Original: "Access to clean water reduces child mortality by lowering the incidence of diarrhoeal disease" (Banda, 2020, p. 7). Write an acceptable paraphrase.',
            'steps': ['Identify the idea: clean water → less diarrhoea → fewer child deaths.', 'Rewrite with a new structure and words.', 'Add the citation.'],
            'answer': 'Banda (2020) explains that fewer children die where clean water is available, mainly because diarrhoeal illnesses become less common.',
            'check': 'The sentence structure and wording differ from the original, and the source is cited ✓.'},
        'mistakes': ['Changing a few words and calling it a paraphrase.', 'Forgetting to cite paraphrases.', 'Quoting long passages without analysis.', 'Misrepresenting the author\'s meaning.'],
        'real_world': 'Lawyers and civil servants constantly summarise long documents for decision-makers; summarising accurately is a valued professional skill.',
        'exam_strategy': 'Aim for mostly paraphrase and summary with a few well-chosen quotations; markers reward evidence of understanding.',
        'recap': ['Quote sparingly.', 'Paraphrase in your own structure.', 'Summarise main ideas.', 'Always cite.']},
    T4: {
        'overview': 'Academic integrity means honesty in your work. Plagiarism and other misconduct are taken seriously, but they are easy to avoid with good habits.',
        'key_terms': ['Academic integrity', 'Plagiarism', 'Self-plagiarism', 'Collusion', 'Contract cheating', 'Fabrication', 'Similarity report', 'Generative AI', 'Hallucinated reference', 'Disclosure'],
        'explanation': [
            'Plagiarism is presenting someone else\'s work or ideas as your own, with or without intent: copying text without quotation marks and citation, patchwriting, using images or data without credit, or reusing your own previously submitted work without permission (self-plagiarism). Collusion is unauthorised collaboration on individual work; contract cheating is getting someone else to do your work. Fabrication is inventing data or sources.',
            'Similarity-checking software (such as Turnitin) highlights text that matches other sources. A similarity percentage is not a verdict of plagiarism: quotations and references also match. Staff look at what matches and whether it is properly cited.',
            'Rules for generative AI tools vary between universities and even between assignments, so check the policy for each task. Where AI use is allowed, disclose it as required. Be aware that AI tools can produce confident but false information and invent references that do not exist ("hallucinated" citations); never cite a source you have not found and checked yourself. Good habits prevent problems: keep careful notes with sources, start early, and ask your lecturer when unsure.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Plagiarism: others\' work presented as yours', 'Collusion: unauthorised joint work', 'Contract cheating: someone else does it', 'Similarity % ≠ plagiarism verdict', 'AI: follow the task policy, disclose, verify everything'],
        'steps': ['Record sources while researching.', 'Cite every borrowed idea.', 'Check the policy on collaboration and AI.', 'Verify every reference exists.'],
        'worked_example': {
            'problem': 'Two students working on separate individual assignments share their drafts and copy each other\'s best paragraphs. Is this acceptable?',
            'steps': ['The assignments are individual.', 'Sharing and copying written work is unauthorised collaboration.', 'This is collusion, even if no outside source was copied.'],
            'answer': 'No: it is collusion.',
            'check': 'Discussing ideas may be allowed, but submitted wording must be your own ✓.'},
        'mistakes': ['Thinking unintentional plagiarism does not count.', 'Assuming a low similarity score means no plagiarism.', 'Citing AI-generated references without checking them.', 'Reusing an old essay for a new course without permission.'],
        'real_world': 'Several lawyers have been sanctioned by courts after submitting documents that cited non-existent cases generated by AI chatbots.',
        'exam_strategy': 'If you are unsure whether something is allowed, ask before submitting; "I did not know" is rarely accepted as a defence.',
        'recap': ['Honesty in all work.', 'Plagiarism includes patchwriting.', 'Collusion and contract cheating.', 'Check AI rules and verify sources.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Which does NOT usually need a citation?', ['Common knowledge such as "Nairobi is the capital of Kenya"', 'A statistic from a survey', 'A named theory', 'A paraphrased argument'], 0, 'Widely known facts.'),
    Q(T1, 'A paraphrase of another author\'s idea:', ['needs a citation', 'does not need a citation', 'needs quotation marks', 'is always plagiarism'], 0, 'The idea is still theirs.'),
    Q(T1, 'A reference list contains:', ['only the sources you cited', 'everything you have ever read', 'only books', 'only websites'], 0, 'A bibliography may include more.'),
    Q(T1, 'You read Piaget\'s idea only in Smith (2020). In APA you cite:', ['(Piaget, 1952, as cited in Smith, 2020)', '(Piaget, 1952)', '(Smith, 1952)', 'no citation'], 0, 'Secondary citation.'),
    Q(T1, 'One purpose of referencing is to:', ['let readers find and check your sources', 'make the essay longer', 'avoid writing your own ideas', 'impress with many names'], 0, 'Traceability.'),
    Q(T1, 'If you are unsure whether something is common knowledge, you should:', ['cite it', 'leave it out', 'put it in quotation marks', 'ignore the rule'], 0, 'Safer to cite.'),
    # T2
    Q(T2, 'APA 7 in-text citation for a quotation from page 14 of Mensah (2021):', ['(Mensah, 2021, p. 14)', '(Mensah 14, 2021)', '(K. Mensah, 2021)', '[14]'], 0, 'Author, year, page.'),
    Q(T2, 'In APA 7, a work by three or more authors is cited:', ['with the first author and "et al." from the first citation', 'with all names every time', 'with the last author only', 'with initials only'], 0, 'APA 7 rule.'),
    Q(T2, 'An APA reference list is ordered:', ['alphabetically by first author\'s surname', 'by date of publication', 'by order of citation', 'by length of title'], 0, 'Author–date style.'),
    Q(T2, 'A DOI is:', ['a permanent identifier for a digital document', 'a type of journal', 'the page number', 'a referencing style'], 0, 'Digital object identifier.'),
    Q(T2, 'In APA 7, quotations of how many words or more are set as block quotations?', ['40', '10', '100', '25'], 0, 'Indented, no quotation marks.', ans=40),
    Q(T2, 'Numbered referencing styles such as IEEE are common in:', ['engineering', 'all humanities subjects', 'no academic fields', 'only law'], 0, 'Also Vancouver in medicine.'),
    # T3
    Q(T3, 'A paraphrase should:', ['use your own words and sentence structure, with a citation', 'change only a few words', 'copy the original exactly', 'leave out the citation'], 0, 'Genuine rewording.'),
    Q(T3, 'Swapping a few words for synonyms while keeping the original structure is:', ['patchwriting, a form of plagiarism', 'a good paraphrase', 'a summary', 'a block quote'], 0, 'Not acceptable.'),
    Q(T3, 'A summary:', ['condenses the main ideas of a longer text', 'copies a passage word for word', 'is longer than the original', 'never needs a citation'], 0, 'Much shorter.'),
    Q(T3, 'Direct quotations are best used when:', ['the exact wording matters', 'you do not understand the text', 'you want to reach the word count', 'you cannot find the page'], 0, 'Definitions, striking phrases.'),
    Q(T3, 'Combining several sources to support a point is called:', ['synthesis', 'patchwriting', 'collusion', 'fabrication'], 0, 'Shows wide reading.'),
    Q(T3, 'A tentative reporting verb is:', ['suggests', 'demonstrates', 'proves', 'establishes'], 0, 'Shows caution.'),
    # T4
    Q(T4, 'Working together on an individual assignment without permission is:', ['collusion', 'synthesis', 'paraphrasing', 'peer review'], 0, 'Unauthorised collaboration.'),
    Q(T4, 'Paying someone else to write your essay is:', ['contract cheating', 'collusion', 'self-plagiarism', 'fair use'], 0, 'Serious misconduct.'),
    Q(T4, 'A similarity report of 18% means:', ['18% of the text matches other sources; staff must check whether it is cited', 'the work is 18% plagiarised', 'the essay failed', 'the essay is 82% original research'], 0, 'Not a verdict.'),
    Q(T4, 'Submitting an essay you wrote for a previous course without permission is:', ['self-plagiarism', 'acceptable recycling', 'collusion', 'synthesis'], 0, 'Reuse needs permission.'),
    Q(T4, 'Before citing a reference suggested by an AI tool, you should:', ['find and check that the source exists and says what is claimed', 'cite it directly', 'add "AI" to the title', 'paraphrase it without checking'], 0, 'AI can invent references.'),
    Q(T4, 'Inventing data for a research report is:', ['fabrication', 'paraphrasing', 'common knowledge', 'secondary citation'], 0, 'Serious misconduct.'),
]

FLASH = [
    ['Common knowledge', 'Widely known, undisputed facts that need no citation.'],
    ['Secondary citation', 'Citing a source you read about in another source (as cited in).'],
    ['APA in-text', '(Author, Year, p. X); et al. for three or more authors.'],
    ['DOI', 'Permanent digital object identifier for an article.'],
    ['Paraphrase', 'Restating a passage in your own words and structure, with a citation.'],
    ['Patchwriting', 'Swapping words but keeping the original structure: plagiarism.'],
    ['Collusion', 'Unauthorised collaboration on individual work.'],
    ['Hallucinated reference', 'A plausible but non-existent source invented by an AI tool.'],
]
