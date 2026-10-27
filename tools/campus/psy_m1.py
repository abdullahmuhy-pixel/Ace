"""Introduction to Psychology, module 1: Psychology as a science."""
import statistics as st
from verify import Q
T1, T2, T3, T4 = ('History and perspectives of psychology', 'Research methods', 'Descriptive statistics and correlation', 'Research ethics')
d = [4, 7, 7, 8, 9, 12, 16]
assert (st.mean(d), st.median(d), st.mode(d), max(d) - min(d)) == (9, 8, 7, 12)
assert 100 + 15 == 115 and 100 - 2 * 15 == 70
assert round(0.6 ** 2, 2) == 0.36

MODULE = {
    'title': 'Psychology as a science',
    'topics': [T1, T2, T3, T4],
    'overview': 'Psychology is the scientific study of behaviour and mental processes. This module traces how the subject developed, introduces the main perspectives, and covers the research methods, basic statistics and ethical rules that let psychologists test ideas rather than rely on common sense.',
    'key_terms': ['Behaviour', 'Mental processes', 'Structuralism', 'Functionalism', 'Behaviourism', 'Cognitive perspective', 'Hypothesis', 'Independent variable', 'Dependent variable', 'Correlation', 'Informed consent', 'Debriefing'],
    'explanation': [
        'Psychology began as a science in 1879, when Wilhelm Wundt opened the first psychology laboratory in Leipzig. Since then several perspectives have shaped the field: psychodynamic, behavioural, humanistic, cognitive, biological and sociocultural. Each asks different questions about the same behaviour.',
        'Psychologists test ideas with systematic methods. Experiments manipulate an independent variable to see its effect on a dependent variable and can show cause and effect. Correlational studies, surveys, observations and case studies describe relationships and behaviour but cannot prove causation on their own.',
        'Data are summarised with statistics such as the mean, median and standard deviation, and relationships with correlation coefficients. All research must follow ethical principles: informed consent, protection from harm, confidentiality, the right to withdraw and debriefing.'],
    'quick_facts': [
        'Wundt, 1879: first psychology laboratory.',
        'Experiment: manipulate IV, measure DV, control other variables.',
        'Correlation does not prove causation.',
        'r ranges from −1 to +1.',
        'Core ethics: consent, no harm, confidentiality, withdrawal, debriefing.'],
}

NOTES = {
    T1: {
        'overview': 'Psychology grew from philosophy and physiology into a science with several complementary perspectives.',
        'key_terms': ['Wilhelm Wundt', 'Introspection', 'Structuralism', 'Functionalism', 'Psychodynamic', 'Behaviourism', 'Humanistic', 'Cognitive', 'Biological', 'Sociocultural', 'Biopsychosocial model'],
        'explanation': [
            'Wundt\'s laboratory (Leipzig, 1879) studied the mind through trained introspection; his student Titchener called the approach structuralism, the search for the basic elements of experience. William James in the USA favoured functionalism, asking what mental processes are for. Freud\'s psychodynamic approach stressed unconscious motives and early childhood experiences.',
            'Behaviourists such as John Watson and B. F. Skinner argued that psychology should study only observable behaviour and learning. Humanistic psychologists (Carl Rogers, Abraham Maslow) reacted by stressing free will and personal growth. From the 1950s the cognitive perspective studied thinking, memory and language, often comparing the mind to a computer.',
            'Today the biological perspective links behaviour to the brain, genes and hormones, and the sociocultural perspective stresses culture and social context. Most psychologists use a biopsychosocial model: depression, for example, can involve brain chemistry, negative thinking patterns and stressful life circumstances at once.'],
        'formulas_label': 'Perspectives',
        'formulas': ['Psychodynamic: unconscious conflicts (Freud)', 'Behavioural: learning from the environment (Watson, Skinner)', 'Humanistic: growth and free will (Rogers, Maslow)', 'Cognitive: thinking and information processing', 'Biological: brain, genes, hormones', 'Sociocultural: culture and social context'],
        'steps': ['Identify the key focus of each perspective.', 'Link each to a founder.', 'Apply several perspectives to one behaviour.', 'Combine them with the biopsychosocial model.'],
        'worked_example': {
            'problem': 'Explain how three perspectives would approach a student\'s fear of public speaking.',
            'steps': ['Behavioural: the fear was learned, perhaps after an embarrassing experience, and can be unlearned by gradual exposure.', 'Cognitive: the fear comes from thoughts such as "everyone will judge me", which can be challenged.', 'Biological: the fight-or-flight response releases adrenaline, causing a racing heart and shaky voice.'],
            'answer': 'Each perspective explains a different part of the same problem; together they give a fuller picture.',
            'check': 'Each answer names the perspective and its central idea, which is what examiners look for ✓.'},
        'mistakes': ['Equating psychology with Freud.', 'Thinking perspectives are mutually exclusive.', 'Confusing structuralism and functionalism.', 'Calling psychology "just common sense".'],
        'real_world': 'Modern treatment for anxiety often combines medication (biological) with cognitive behavioural therapy (cognitive and behavioural), reflecting several perspectives at once.',
        'exam_strategy': 'When asked to compare perspectives, use the same scenario for each so the differences stand out.',
        'recap': ['Wundt 1879.', 'Six main perspectives.', 'Each asks different questions.', 'Biopsychosocial integration.']},
    T2: {
        'overview': 'Research methods let psychologists test claims systematically. Different methods suit different questions.',
        'key_terms': ['Hypothesis', 'Operational definition', 'Independent variable', 'Dependent variable', 'Confounding variable', 'Random assignment', 'Control group', 'Placebo', 'Double-blind', 'Correlational study', 'Case study', 'Naturalistic observation', 'Sample', 'Population'],
        'explanation': [
            'A hypothesis is a testable prediction. Variables need operational definitions, saying exactly how they are measured: "stress" might be defined as a score on a stress questionnaire. In an experiment, the researcher manipulates the independent variable (IV) and measures the dependent variable (DV), holding other variables constant.',
            'Random assignment to groups spreads participants\' individual differences evenly so that confounding variables do not explain the result. A control group gets no treatment or a placebo. In a double-blind design, neither participants nor researchers know who is in which group, preventing expectation effects.',
            'Other methods: correlational studies measure how two variables relate; surveys collect self-reports from many people; naturalistic observation records behaviour in real settings; case studies examine one person in depth (such as H.M., whose memory was studied for decades). Results generalise only if the sample represents the population; random sampling helps.'],
        'formulas_label': 'Key ideas',
        'formulas': ['IV: manipulated; DV: measured', 'Random assignment controls participant differences', 'Random sampling supports generalisation', 'Only experiments establish cause and effect'],
        'steps': ['State the hypothesis.', 'Identify IV and DV and define them operationally.', 'Choose a method and design.', 'Identify possible confounds and controls.'],
        'worked_example': {
            'problem': 'A researcher tests whether caffeine improves memory. Students get either a caffeinated or a decaffeinated drink, then learn a list of 30 words. Identify the IV, DV and one control.',
            'steps': ['IV: whether the drink contains caffeine.', 'DV: the number of words recalled out of 30.', 'Controls: same drink taste, same list, same time of day; random assignment; ideally double-blind.'],
            'answer': 'IV caffeine (yes/no); DV words recalled; controls as listed.',
            'check': 'The decaffeinated drink acts as a placebo control, so expectation alone cannot explain any difference ✓.'},
        'mistakes': ['Swapping the IV and the DV.', 'Confusing random sampling with random assignment.', 'Claiming a case study proves something about everyone.', 'Leaving variables without operational definitions.'],
        'real_world': 'Drug trials use randomised, double-blind, placebo-controlled designs, the same logic as a psychology experiment.',
        'exam_strategy': 'Write the IV and DV in full operational form ("number of words correctly recalled in 2 minutes"), not one-word labels.',
        'recap': ['Hypothesis, IV, DV.', 'Random assignment, controls.', 'Double-blind removes expectations.', 'Choose the method for the question.']},
    T3: {
        'overview': 'Statistics summarise data and describe relationships. Understanding them lets you read psychology research critically.',
        'key_terms': ['Mean', 'Median', 'Mode', 'Range', 'Standard deviation', 'Normal distribution', 'Correlation coefficient', 'Positive correlation', 'Negative correlation', 'Statistical significance', 'p-value'],
        'explanation': [
            'Measures of central tendency: the mean (average), median (middle value) and mode (most common). For scores 4, 7, 7, 8, 9, 12, 16, the mean is 9, the median 8, the mode 7 and the range 12. The median resists extreme scores better than the mean. The standard deviation measures how spread out scores are around the mean.',
            'Many traits follow a normal distribution: about 68% of scores fall within 1 standard deviation of the mean and about 95% within 2. IQ tests are scaled to a mean of 100 and a standard deviation of 15, so about 68% of people score between 85 and 115 and about 95% between 70 and 130.',
            'A correlation coefficient r runs from −1 to +1. Positive: both variables rise together; negative: one rises as the other falls; 0: no linear relationship. Correlation does not show causation: ice-cream sales and drownings both rise in summer because of a third variable, hot weather. Inferential statistics test whether results are likely due to chance; p < 0.05 is the usual threshold for "statistically significant".'],
        'formulas_label': 'Formulas',
        'formulas': ['Mean = sum ÷ number of scores', 'Median: middle score when ordered', 'Normal: 68% within 1 SD, 95% within 2 SD', 'IQ: mean 100, SD 15', 'r from −1 to +1; correlation ≠ causation'],
        'steps': ['Order the data.', 'Calculate mean, median, mode and range.', 'Choose the best average for skewed data.', 'Describe correlations by direction and strength.'],
        'worked_example': {
            'problem': 'Seven students score 4, 7, 7, 8, 9, 12 and 16 on a 20-point memory test. Find the mean, median, mode and range. Which average best represents the data?',
            'steps': ['Sum = 63; mean = 63 ÷ 7 = 9.', 'Median (4th of 7) = 8; mode = 7; range = 16 − 4 = 12.', 'The 16 pulls the mean up, so the median (8) is a fairer summary.'],
            'answer': 'Mean 9, median 8, mode 7, range 12; median is best here.',
            'check': 'The mean is larger than the median, as expected for data skewed to the right ✓.'},
        'mistakes': ['Saying a correlation of −0.8 is weaker than +0.3.', 'Concluding causation from correlation.', 'Forgetting to order data before finding the median.', 'Thinking p < 0.05 means the result is important.'],
        'real_world': 'News headlines often claim "X causes Y" from correlational data; spotting third variables is one of the most useful skills psychology teaches.',
        'exam_strategy': 'When interpreting r, give both direction (positive or negative) and strength (weak, moderate, strong).',
        'recap': ['Mean, median, mode.', '68–95 rule.', 'r from −1 to +1.', 'Correlation is not causation.']},
    T4: {
        'overview': 'Ethical guidelines protect research participants. They were strengthened after controversial studies in the twentieth century.',
        'key_terms': ['Informed consent', 'Protection from harm', 'Confidentiality', 'Right to withdraw', 'Deception', 'Debriefing', 'Ethics committee', 'Animal research'],
        'explanation': [
            'Modern codes (such as those of the American Psychological Association and the British Psychological Society) require informed consent (participants know what they agree to), protection from physical and psychological harm, confidentiality of data, the right to withdraw at any time without penalty, and debriefing at the end. Ethics committees (institutional review boards) must approve studies before they begin.',
            'Deception is allowed only when the study could not be done otherwise, the risk is low, and participants are debriefed promptly. Children and others who cannot consent fully need consent from a parent or guardian as well as their own agreement.',
            'Controversial studies shaped these rules. Milgram\'s obedience studies caused participants serious stress; Zimbardo\'s Stanford prison study (1971) was stopped after six days; the Little Albert study conditioned fear in an infant. Animal research must minimise suffering, often summarised as the 3Rs: replace, reduce, refine.'],
        'formulas_label': 'Core principles',
        'formulas': ['Informed consent', 'Protection from harm', 'Confidentiality', 'Right to withdraw', 'Debriefing', 'Deception only when justified', 'Animals: replace, reduce, refine'],
        'steps': ['Identify the participants and risks.', 'Check each principle in turn.', 'Note any breach.', 'Suggest how the study could be made ethical.'],
        'worked_example': {
            'problem': 'A researcher secretly records students\' conversations in a café for a study and publishes quotes with their first names. Identify two ethical problems.',
            'steps': ['No informed consent: students did not know they were being recorded.', 'No confidentiality: first names were published.', 'Fix: observe only public behaviour without recording speech, or seek consent and anonymise data.'],
            'answer': 'Lack of consent and breach of confidentiality.',
            'check': 'Both issues match named principles in standard ethics codes ✓.'},
        'mistakes': ['Thinking deception is never allowed.', 'Confusing debriefing with consent.', 'Saying ethics only apply to experiments.', 'Forgetting animals are covered by ethics rules.'],
        'real_world': 'Before a university study can recruit you, an ethics committee will have reviewed its consent form, risks and data storage plan.',
        'exam_strategy': 'Name the specific principle that is broken and explain why, rather than writing "it is unethical".',
        'recap': ['Consent, harm, confidentiality.', 'Withdrawal and debriefing.', 'Deception needs justification.', 'Ethics committees approve research.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The first psychology laboratory was opened by Wilhelm Wundt in:', ['1879', '1900', '1850', '1913'], 0, 'Leipzig, Germany.'),
    Q(T1, 'Behaviourism focuses on:', ['observable behaviour and learning', 'unconscious conflicts', 'free will and self-actualisation', 'brain chemistry'], 0, 'Watson and Skinner.'),
    Q(T1, 'The humanistic perspective is most associated with:', ['Carl Rogers and Abraham Maslow', 'B. F. Skinner', 'Sigmund Freud', 'Wilhelm Wundt'], 0, 'Personal growth.'),
    Q(T1, 'Functionalism, associated with William James, asked:', ['what mental processes are for', 'what the basic elements of experience are', 'how the unconscious works', 'how genes affect behaviour'], 0, 'Purpose of the mind.'),
    Q(T1, 'The biopsychosocial model explains behaviour using:', ['biological, psychological and social factors together', 'only genes', 'only childhood experiences', 'only rewards and punishments'], 0, 'Integration.'),
    Q(T1, 'The cognitive perspective often compares the mind to:', ['a computer that processes information', 'a steam engine', 'a blank slate only', 'an iceberg'], 0, 'Information processing.'),
    # T2
    Q(T2, 'In an experiment, the variable the researcher manipulates is the:', ['independent variable', 'dependent variable', 'confounding variable', 'control variable'], 0, 'IV.'),
    Q(T2, 'Random assignment to groups helps to:', ['spread individual differences evenly between groups', 'make the sample represent the population', 'increase the sample size', 'remove the need for a control group'], 0, 'Controls participant variables.'),
    Q(T2, 'In a double-blind study:', ['neither participants nor researchers know who is in which group', 'only the participants are unaware', 'the study is repeated twice', 'two researchers score each result'], 0, 'Removes expectation effects.'),
    Q(T2, 'Which method can establish cause and effect?', ['A controlled experiment', 'A correlational study', 'A case study', 'A survey'], 0, 'Manipulation plus control.'),
    Q(T2, 'An operational definition:', ['states exactly how a variable will be measured', 'is the hypothesis', 'is a summary of results', 'describes the population'], 0, 'Makes variables measurable.'),
    Q(T2, 'A detailed study of one individual is a:', ['case study', 'survey', 'experiment', 'meta-analysis'], 0, 'For example H.M.'),
    # T3
    Q(T3, 'For the scores 4, 7, 7, 8, 9, 12, 16, the mean is:', ['9', '8', '7', '12'], 0, '63 ÷ 7.', ans=9),
    Q(T3, 'For the same scores, the median is:', ['8', '9', '7', '12'], 0, 'Middle of seven ordered scores.', ans=8),
    Q(T3, 'IQ has mean 100 and SD 15. About 68% of people score between:', ['85 and 115', '70 and 130', '90 and 110', '100 and 115'], 0, 'Within 1 SD.'),
    Q(T3, 'A correlation of r = −0.85 shows:', ['a strong negative relationship', 'a weak negative relationship', 'no relationship', 'that one variable causes the other'], 0, 'Strength from size, direction from sign.'),
    Q(T3, 'Ice-cream sales and drownings are positively correlated because:', ['a third variable (hot weather) affects both', 'ice cream causes drowning', 'drowning causes ice-cream sales', 'the correlation is negative'], 0, 'Correlation ≠ causation.'),
    Q(T3, 'The usual threshold for statistical significance in psychology is:', ['p < 0.05', 'p > 0.5', 'p = 1', 'p < 0.5'], 0, '5% chance level.'),
    # T4
    Q(T4, 'Informed consent means participants:', ['know what the study involves and agree to take part', 'are paid for their time', 'are told the results', 'cannot leave the study'], 0, 'Core principle.'),
    Q(T4, 'Explaining the true aims of a study to participants afterwards is called:', ['debriefing', 'consent', 'confidentiality', 'random assignment'], 0, 'Especially after deception.'),
    Q(T4, 'Participants\' right to withdraw means they can:', ['leave at any time without penalty', 'see other people\'s data', 'change the hypothesis', 'refuse debriefing only'], 0, 'Even mid-study.'),
    Q(T4, 'Deception in research is acceptable only when:', ['it is necessary, low-risk and followed by debriefing', 'the researcher wants it', 'participants are students', 'the results are important'], 0, 'Strict conditions.'),
    Q(T4, 'The 3Rs for animal research are:', ['replace, reduce, refine', 'record, report, review', 'random, repeat, reliable', 'reward, reinforce, repeat'], 0, 'Minimise animal use and suffering.'),
    Q(T4, 'The Stanford prison study (1971) was ended early because:', ['participants were suffering serious distress', 'it ran out of funding', 'too few people volunteered', 'the results were already clear'], 0, 'Stopped after six days.'),
]

FLASH = [
    ['Wundt (1879)', 'Opened the first psychology laboratory, in Leipzig.'],
    ['Behaviourism', 'Studies observable behaviour and learning (Watson, Skinner).'],
    ['Independent variable', 'The variable the researcher manipulates.'],
    ['Dependent variable', 'The variable that is measured.'],
    ['Random assignment', 'Placing participants in groups by chance to balance differences.'],
    ['Correlation coefficient', 'r from −1 to +1; shows direction and strength, not cause.'],
    ['Normal distribution', '68% within 1 SD; 95% within 2 SD.'],
    ['Debriefing', 'Explaining the study\'s true aims to participants afterwards.'],
]
