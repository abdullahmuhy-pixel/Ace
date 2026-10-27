"""Introduction to Psychology, module 5: Social psychology and mental health."""
from verify import Q
T1, T2, T3, T4 = ('Social cognition and attitudes', 'Social influence', 'Psychological disorders', 'Treatment and therapy')
assert round(26 / 40 * 100) == 65

MODULE = {
    'title': 'Social psychology and mental health',
    'topics': [T1, T2, T3, T4],
    'overview': 'People think, feel and act differently when others are involved. This module covers how we explain behaviour and form attitudes, how groups and authority influence us, how psychological disorders are defined and classified, and the main approaches to treating them.',
    'key_terms': ['Attribution', 'Fundamental attribution error', 'Cognitive dissonance', 'Prejudice', 'Conformity', 'Obedience', 'Bystander effect', 'DSM-5', 'Diathesis–stress model', 'Cognitive behavioural therapy', 'Psychotropic medication'],
    'explanation': [
        'Social cognition is how we make sense of other people. We explain behaviour by attributing it to personality or situation, often with predictable biases. Attitudes guide behaviour, but behaviour can also change attitudes, as cognitive dissonance shows.',
        'Classic studies by Asch, Milgram and Darley and Latané showed how strongly situations shape behaviour: people conform to groups, obey authority and fail to help when others are present. Knowing these effects helps people resist them.',
        'Psychological disorders are patterns of thought, feeling and behaviour that cause significant distress or impairment. They are classified using systems such as DSM-5 and ICD-11 and explained by combinations of biological, psychological and social factors. Effective treatments include psychological therapies, medication and often both together.'],
    'quick_facts': [
        'Fundamental attribution error: overestimating personality, underestimating situation when explaining others.',
        'Asch: people conformed on about a third of critical trials.',
        'Milgram: 65% obeyed to the maximum 450 V shock.',
        'Bystander effect: more bystanders, less helping (diffusion of responsibility).',
        'CBT targets unhelpful thoughts and behaviours; it is a first-line treatment for depression and anxiety.'],
}

NOTES = {
    T1: {
        'overview': 'We constantly explain others\' behaviour and form attitudes about people and groups. These processes are useful but biased.',
        'key_terms': ['Dispositional attribution', 'Situational attribution', 'Fundamental attribution error', 'Self-serving bias', 'Attitude', 'Cognitive dissonance', 'Stereotype', 'Prejudice', 'Discrimination', 'In-group bias', 'Contact hypothesis'],
        'explanation': [
            'We attribute behaviour either to the person (dispositional) or to the situation (situational). The fundamental attribution error is the tendency to over-emphasise personality when explaining others\' behaviour: if someone cuts in front of you in traffic, you think "rude driver" rather than "maybe they are rushing to hospital". The self-serving bias is crediting our successes to ourselves and blaming failures on the situation.',
            'Cognitive dissonance is the discomfort of holding inconsistent beliefs and actions. In Festinger and Carlsmith\'s 1959 study, participants paid $1 to tell someone a boring task was fun later rated it as more enjoyable than those paid $20; with too little payment to justify the lie, they changed their attitude instead.',
            'A stereotype is a generalised belief about a group, prejudice is a negative attitude, and discrimination is unfair behaviour. In-group bias favours "us" over "them". In Sherif\'s Robbers Cave study (1954), two groups of boys at a summer camp became hostile through competition, then reconciled when they had to cooperate on shared goals. The contact hypothesis says equal-status, cooperative contact reduces prejudice.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Dispositional vs situational attribution', 'Fundamental attribution error: blame the person, ignore the situation', 'Cognitive dissonance: change attitude to fit behaviour', 'Stereotype (belief) → prejudice (attitude) → discrimination (action)'],
        'steps': ['Identify the explanation being made.', 'Classify it as dispositional or situational.', 'Name the bias.', 'Suggest a fairer explanation.'],
        'worked_example': {
            'problem': 'A student who smokes knows smoking causes cancer. She starts saying "the risks are exaggerated". Explain using cognitive dissonance.',
            'steps': ['Belief ("smoking is harmful") conflicts with behaviour (smoking).', 'This inconsistency creates uncomfortable dissonance.', 'Rather than quit, she reduces dissonance by changing her belief to downplay the risk.'],
            'answer': 'She changes her attitude to reduce the conflict between belief and behaviour.',
            'check': 'Quitting would also reduce dissonance; changing the belief is the easier route, as the theory predicts ✓.'},
        'mistakes': ['Confusing prejudice (attitude) with discrimination (behaviour).', 'Getting the $1/$20 result backwards.', 'Thinking the fundamental attribution error applies to explaining ourselves.', 'Assuming contact alone always reduces prejudice.'],
        'real_world': 'Integrated sports teams and cooperative classroom methods such as the "jigsaw classroom" apply the contact hypothesis to reduce prejudice.',
        'exam_strategy': 'Define each term in one sentence, then apply it to the scenario; application marks are usually the larger share.',
        'recap': ['Person vs situation.', 'Fundamental attribution error.', 'Dissonance changes attitudes.', 'Cooperation reduces prejudice.']},
    T2: {
        'overview': 'Other people shape our behaviour through conformity, obedience and their mere presence.',
        'key_terms': ['Conformity', 'Normative influence', 'Informational influence', 'Obedience', 'Agentic state', 'Bystander effect', 'Diffusion of responsibility', 'Social facilitation', 'Social loafing', 'Groupthink'],
        'explanation': [
            'In Asch\'s line-judgement studies (1951), participants answered after confederates who gave obviously wrong answers. Participants conformed on about a third of critical trials, and about three-quarters conformed at least once. Normative influence is conforming to be liked; informational influence is conforming because others seem to know better. Conformity drops sharply if just one other person disagrees with the group.',
            'In Milgram\'s obedience study (1963), participants were told to give increasing electric shocks to a "learner" (a confederate who received no real shocks). 65% (26 of 40) continued to the maximum 450 V. Obedience fell when the experimenter gave orders by phone or when the learner was in the same room. Milgram suggested people enter an agentic state, seeing themselves as carrying out another\'s wishes.',
            'The bystander effect: people are less likely to help in an emergency when others are present, partly through diffusion of responsibility (Darley and Latané, 1968). Others\' presence also affects performance: social facilitation improves well-learned tasks, social loafing reduces individual effort in groups, and groupthink makes cohesive groups ignore alternatives to keep harmony.'],
        'formulas_label': 'Classic studies',
        'formulas': ['Asch (1951): conformity on about a third of critical trials', 'Milgram (1963): 65% obeyed to 450 V', 'Darley and Latané (1968): more bystanders, slower helping', 'Normative (to fit in) vs informational (to be right) influence'],
        'steps': ['Identify the type of influence.', 'Name the classic study.', 'Explain the mechanism.', 'Note factors that increase or decrease it.'],
        'worked_example': {
            'problem': 'A woman collapses in a busy station and dozens of people walk past. Explain why no one helps quickly.',
            'steps': ['Many bystanders are present.', 'Each assumes someone else will act (diffusion of responsibility).', 'People also look to others and, seeing no one react, interpret the situation as not an emergency (informational influence).'],
            'answer': 'The bystander effect, through diffusion of responsibility and social influence on interpretation.',
            'check': 'Pointing at one specific person ("You, call an ambulance") removes the diffusion, which is the standard advice ✓.'},
        'mistakes': ['Confusing conformity (peers) with obedience (authority).', 'Thinking participants in Milgram gave real shocks.', 'Saying the bystander effect means people are uncaring.', 'Forgetting that a single dissenter reduces conformity.'],
        'real_world': 'First-aid training teaches you to give direct instructions to named people in a crowd, a practical answer to the bystander effect.',
        'exam_strategy': 'Quote the key result with a number (Milgram 65%, Asch about one third); precise findings strengthen answers.',
        'recap': ['Asch: conformity.', 'Milgram: obedience.', 'Bystander effect.', 'Groups change performance.']},
    T3: {
        'overview': 'Psychological disorders involve significant distress or impairment. Classification helps diagnosis and research, and most disorders have several interacting causes.',
        'key_terms': ['Abnormality', 'DSM-5', 'ICD-11', 'Major depressive disorder', 'Bipolar disorder', 'Generalised anxiety disorder', 'Phobia', 'Obsessive-compulsive disorder', 'Post-traumatic stress disorder', 'Schizophrenia', 'Positive symptoms', 'Negative symptoms', 'Diathesis–stress model'],
        'explanation': [
            'Definitions of abnormality often use the "four Ds": deviance (unusual), distress, dysfunction (interference with daily life) and danger. Clinicians use classification systems: the American Psychiatric Association\'s DSM-5 (2013, text revision 2022) and the World Health Organization\'s ICD-11. Labels help treatment and research but can carry stigma.',
            'Major depressive disorder involves low mood or loss of interest for at least two weeks with symptoms such as changes in sleep and appetite, fatigue and feelings of worthlessness. Bipolar disorder includes episodes of mania as well as depression. Anxiety disorders include generalised anxiety disorder, panic disorder and specific phobias. OCD involves obsessions (intrusive thoughts) and compulsions (repetitive actions). PTSD follows trauma, with flashbacks, avoidance and hyperarousal.',
            'Schizophrenia involves positive symptoms (additions to normal experience, such as hallucinations and delusions) and negative symptoms (losses, such as flat emotion and reduced motivation). It is not "split personality". The diathesis–stress model explains many disorders as an interaction between a vulnerability (genes, early experiences) and stressful life events.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Four Ds: deviance, distress, dysfunction, danger', 'Depression: ≥ 2 weeks of low mood or loss of interest plus other symptoms', 'Schizophrenia: positive (hallucinations, delusions) vs negative (flat affect) symptoms', 'Diathesis (vulnerability) + stress → disorder'],
        'steps': ['Identify the key symptoms.', 'Match to a disorder category.', 'Apply the diathesis–stress model.', 'Remember diagnosis is for trained clinicians.'],
        'worked_example': {
            'problem': 'Identical twins share the same genes, yet when one develops schizophrenia the other often does not. What does this suggest?',
            'steps': ['If genes alone caused schizophrenia, identical twins would always share it.', 'They often do not, so environmental factors also matter.', 'This fits the diathesis–stress model: genetic vulnerability plus stress.'],
            'answer': 'Genes increase risk, but environment and stress also play a role.',
            'check': 'Concordance is still much higher for identical than for non-identical twins, showing genes matter too ✓.'},
        'mistakes': ['Calling schizophrenia "split personality".', 'Thinking unusual behaviour alone means a disorder.', 'Self-diagnosing from a list of symptoms.', 'Assuming one single cause for each disorder.'],
        'real_world': 'The World Health Organization lists depression among the leading causes of disability worldwide, which is why access to mental health care is a public-health priority.',
        'exam_strategy': 'Use correct terms (positive and negative symptoms, obsessions and compulsions) and avoid everyday labels like "crazy".',
        'recap': ['Four Ds.', 'DSM-5 and ICD-11.', 'Key disorder features.', 'Diathesis–stress.']},
    T4: {
        'overview': 'Treatments for psychological disorders include several kinds of talking therapy and biomedical treatments. Evidence shows many are effective.',
        'key_terms': ['Psychodynamic therapy', 'Free association', 'Client-centred therapy', 'Systematic desensitisation', 'Exposure therapy', 'Cognitive therapy', 'CBT', 'Antidepressants', 'Antipsychotics', 'Lithium', 'ECT', 'Therapeutic alliance'],
        'explanation': [
            'Psychodynamic therapy (from Freud\'s psychoanalysis) uses free association and interpretation to bring unconscious conflicts into awareness. Humanistic, client-centred therapy (Rogers) offers empathy, genuineness and unconditional positive regard so clients can grow. Behaviour therapies change learned responses: systematic desensitisation pairs relaxation with a gradually increasing feared stimulus, and exposure therapy is very effective for phobias and OCD.',
            'Cognitive therapies (Aaron Beck; Albert Ellis\'s rational emotive behaviour therapy) challenge unhelpful automatic thoughts, such as "I always fail". Cognitive behavioural therapy (CBT) combines changing thoughts and behaviours and is a first-line treatment for depression and anxiety disorders.',
            'Biomedical treatments include antidepressants (such as SSRIs), anti-anxiety drugs, antipsychotics for schizophrenia, and mood stabilisers such as lithium for bipolar disorder. Electroconvulsive therapy (ECT), given under anaesthetic, can help severe depression that has not responded to other treatment. Meta-analyses show therapy generally works, combined therapy and medication often works best for depression, and a strong therapeutic alliance predicts good outcomes across approaches.'],
        'formulas_label': 'Approaches',
        'formulas': ['Psychodynamic: insight into unconscious conflicts', 'Humanistic: empathy, unconditional positive regard', 'Behavioural: exposure, systematic desensitisation', 'Cognitive/CBT: challenge thoughts, change behaviour', 'Biomedical: SSRIs, antipsychotics, lithium, ECT'],
        'steps': ['Identify the disorder.', 'Choose an evidence-based treatment.', 'Explain how it works.', 'Evaluate benefits and limits.'],
        'worked_example': {
            'problem': 'Describe how systematic desensitisation could treat a fear of spiders.',
            'steps': ['Teach deep muscle relaxation.', 'Build a hierarchy from least to most feared (a picture of a spider → a spider in a jar → holding a spider).', 'Work up the hierarchy step by step while staying relaxed, until the fear response is replaced by calm.'],
            'answer': 'Gradual exposure paired with relaxation replaces fear with a calm response.',
            'check': 'It is based on classical conditioning: a new response (relaxation) is linked to the feared stimulus ✓.'},
        'mistakes': ['Thinking medication cures disorders permanently.', 'Saying CBT focuses on childhood memories.', 'Confusing systematic desensitisation with flooding.', 'Assuming ECT is used as a first treatment.'],
        'real_world': 'Many health services now offer guided online CBT, which has been shown to help mild to moderate depression and anxiety.',
        'exam_strategy': 'Match the treatment to its theory (CBT ← cognitive; desensitisation ← classical conditioning); explaining the link earns the higher marks.',
        'recap': ['Several therapy traditions.', 'CBT first-line for depression and anxiety.', 'Medication for many disorders.', 'Therapeutic alliance matters.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Explaining another person\'s behaviour by their personality while ignoring the situation is the:', ['fundamental attribution error', 'self-serving bias', 'bystander effect', 'halo effect'], 0, 'Over-emphasising dispositions.'),
    Q(T1, 'In Festinger and Carlsmith\'s study, who rated the boring task as most enjoyable?', ['Those paid $1', 'Those paid $20', 'Those paid nothing and not asked to lie', 'Everyone equally'], 0, 'Insufficient justification → dissonance.'),
    Q(T1, 'Prejudice is best described as:', ['a negative attitude towards a group', 'unfair behaviour towards a group', 'any generalisation about a group', 'favouring your own group'], 0, 'Discrimination is behaviour.'),
    Q(T1, 'Crediting your own success to ability but your failures to bad luck is the:', ['self-serving bias', 'fundamental attribution error', 'confirmation bias', 'groupthink'], 0, 'Protects self-esteem.'),
    Q(T1, 'In Sherif\'s Robbers Cave study, hostility between groups was reduced by:', ['working together on shared goals', 'more competition', 'separating the groups', 'giving prizes to one group'], 0, 'Superordinate goals.'),
    Q(T1, 'Changing an attitude to match behaviour, to reduce discomfort, is explained by:', ['cognitive dissonance', 'social loafing', 'the bystander effect', 'obedience'], 0, 'Festinger.'),
    # T2
    Q(T2, 'In Milgram\'s study, what percentage of participants went to the maximum 450 V?', ['65%', '10%', '35%', '100%'], 0, '26 of 40.', ans=65),
    Q(T2, 'In Asch\'s studies, participants conformed on about:', ['a third of critical trials', 'all critical trials', 'none of the critical trials', 'nine-tenths of critical trials'], 0, 'About 37% in the classic version.'),
    Q(T2, 'Conforming because you believe others know better is:', ['informational influence', 'normative influence', 'obedience', 'social loafing'], 0, 'Wanting to be right.'),
    Q(T2, 'People are less likely to help when many others are present. This is the:', ['bystander effect', 'social facilitation effect', 'halo effect', 'placebo effect'], 0, 'Diffusion of responsibility.'),
    Q(T2, 'Putting in less effort when working in a group is:', ['social loafing', 'social facilitation', 'groupthink', 'conformity'], 0, 'Individual effort hidden.'),
    Q(T2, 'Conformity in Asch-type studies drops sharply when:', ['one other person disagrees with the group', 'the group is larger', 'the task is harder', 'participants are paid more'], 0, 'A dissenter breaks unanimity.'),
    # T3
    Q(T3, 'Hallucinations and delusions are examples of:', ['positive symptoms of schizophrenia', 'negative symptoms of schizophrenia', 'symptoms of OCD', 'symptoms of phobia'], 0, 'Additions to normal experience.'),
    Q(T3, 'Repetitive actions performed to reduce anxiety from intrusive thoughts are characteristic of:', ['obsessive-compulsive disorder', 'bipolar disorder', 'schizophrenia', 'PTSD'], 0, 'Obsessions and compulsions.'),
    Q(T3, 'The diathesis–stress model explains disorders as:', ['vulnerability interacting with stressful events', 'caused only by genes', 'caused only by stress', 'learned only through conditioning'], 0, 'Interaction.'),
    Q(T3, 'Episodes of both mania and depression are characteristic of:', ['bipolar disorder', 'generalised anxiety disorder', 'specific phobia', 'OCD'], 0, 'Mood swings.'),
    Q(T3, 'The classification manual published by the American Psychiatric Association is the:', ['DSM-5', 'ICD-11', 'MMPI', 'SRRS'], 0, 'Diagnostic and Statistical Manual.'),
    Q(T3, 'Flashbacks, avoidance and hyperarousal after a traumatic event suggest:', ['PTSD', 'schizophrenia', 'bipolar disorder', 'a specific phobia'], 0, 'Post-traumatic stress disorder.'),
    # T4
    Q(T4, 'Systematic desensitisation is based mainly on:', ['classical conditioning', 'psychoanalysis', 'Maslow\'s hierarchy', 'trait theory'], 0, 'Relaxation paired with fear stimulus.'),
    Q(T4, 'Therapy that challenges unhelpful automatic thoughts and changes behaviour is:', ['cognitive behavioural therapy', 'psychoanalysis', 'client-centred therapy', 'ECT'], 0, 'CBT.'),
    Q(T4, 'Lithium is mainly used to treat:', ['bipolar disorder', 'phobias', 'insomnia', 'OCD'], 0, 'Mood stabiliser.'),
    Q(T4, 'Free association is a technique of:', ['psychodynamic therapy', 'behaviour therapy', 'CBT', 'drug therapy'], 0, 'Freud.'),
    Q(T4, 'Client-centred therapy emphasises:', ['empathy and unconditional positive regard', 'exposure to feared objects', 'medication', 'interpreting dreams'], 0, 'Carl Rogers.'),
    Q(T4, 'A factor that predicts good outcomes across many types of therapy is:', ['a strong therapeutic alliance', 'the length of the therapist\'s training only', 'the price of therapy', 'the use of a couch'], 0, 'Relationship between client and therapist.'),
]

FLASH = [
    ['Fundamental attribution error', 'Over-emphasising personality and ignoring the situation when explaining others.'],
    ['Cognitive dissonance', 'Discomfort from inconsistent beliefs and actions, often resolved by changing attitudes.'],
    ['Asch', 'Conformity to an obviously wrong group answer on about a third of trials.'],
    ['Milgram', '65% obeyed an authority figure to the maximum 450 V.'],
    ['Bystander effect', 'Less helping when more people are present.'],
    ['Diathesis–stress model', 'Vulnerability plus stress leads to disorder.'],
    ['Positive symptoms', 'Additions such as hallucinations and delusions.'],
    ['CBT', 'Changes unhelpful thoughts and behaviours; first-line for depression and anxiety.'],
]
