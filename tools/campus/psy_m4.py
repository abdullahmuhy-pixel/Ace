"""Introduction to Psychology, module 4: Development, motivation and personality."""
from verify import Q
T1, T2, T3, T4 = ('Lifespan development', 'Motivation and emotion', 'Personality', 'Stress, coping and health')
assert 50 + 20 + 36 == 106 and 100 + 63 + 39 == 202

MODULE = {
    'title': 'Development, motivation and personality',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module follows how people change from infancy to old age, what drives behaviour and produces emotions, how psychologists describe and explain personality, and how stress affects health and how people cope.',
    'key_terms': ['Cognitive development', 'Schema', 'Attachment', 'Psychosocial stage', 'Hierarchy of needs', 'Yerkes–Dodson law', 'Theories of emotion', 'Big Five', 'Id, ego and superego', 'Self-efficacy', 'General adaptation syndrome', 'Coping'],
    'explanation': [
        'Development combines nature (genes, maturation) and nurture (experience). Piaget described stages of thinking, Vygotsky stressed social support, attachment research showed the importance of early relationships, and Erikson described challenges across the whole lifespan.',
        'Motivation explains why we act: biological drives, a need for optimal arousal, Maslow\'s hierarchy, and intrinsic or extrinsic rewards. Emotions combine bodily arousal, expression and interpretation, and different theories order these parts differently.',
        'Personality is a person\'s characteristic pattern of thinking, feeling and acting. Psychodynamic, trait, humanistic and social-cognitive approaches explain it differently. Stress triggers a predictable bodily response; long-term stress harms health, but appraisal and coping strategies make a big difference.'],
    'quick_facts': [
        'Piaget: sensorimotor, preoperational, concrete operational, formal operational.',
        'Ainsworth\'s strange situation classifies secure, avoidant and resistant attachment.',
        'Maslow: physiological → safety → belonging → esteem → self-actualisation.',
        'Big Five: openness, conscientiousness, extraversion, agreeableness, neuroticism (OCEAN).',
        'Selye\'s GAS: alarm → resistance → exhaustion.'],
}

NOTES = {
    T1: {
        'overview': 'Developmental psychology studies how we change across the lifespan in thinking, relationships and identity.',
        'key_terms': ['Schema', 'Assimilation', 'Accommodation', 'Object permanence', 'Egocentrism', 'Conservation', 'Zone of proximal development', 'Scaffolding', 'Attachment', 'Strange situation', 'Psychosocial stage'],
        'explanation': [
            'Jean Piaget proposed four stages. Sensorimotor (0–2 years): learning through senses and actions; object permanence develops. Preoperational (2–7): symbolic thought and language, but egocentrism and no conservation (a child thinks a tall thin glass holds more than a short wide one with the same water). Concrete operational (7–11): logical thinking about concrete objects; conservation is mastered. Formal operational (11+): abstract and hypothetical reasoning. Children build schemas by assimilation (fitting new information in) and accommodation (changing the schema).',
            'Lev Vygotsky stressed social interaction: the zone of proximal development is the gap between what a child can do alone and with help, and scaffolding is support that is gradually withdrawn. Harlow\'s monkeys preferred a soft cloth "mother" to a wire one that gave milk, showing comfort matters more than food for attachment. Bowlby saw attachment as an evolved bond; Ainsworth\'s strange situation classifies infants as secure (the majority), insecure-avoidant or insecure-resistant, with a disorganised type added later.',
            'Erik Erikson described eight psychosocial stages across life, each with a central conflict: trust vs mistrust in infancy, identity vs role confusion in adolescence, intimacy vs isolation in young adulthood, generativity vs stagnation in middle age, and integrity vs despair in old age. In older adulthood, processing speed tends to slow but knowledge and vocabulary often remain stable or grow.'],
        'formulas_label': 'Piaget\'s stages',
        'formulas': ['Sensorimotor (0–2): object permanence', 'Preoperational (2–7): symbols, egocentrism, no conservation', 'Concrete operational (7–11): conservation, logic about concrete things', 'Formal operational (11+): abstract reasoning'],
        'steps': ['Identify the age and the behaviour.', 'Match to the stage or theory.', 'Name the concept shown.', 'Compare with another theorist.'],
        'worked_example': {
            'problem': 'A 4-year-old says a row of 5 spread-out coins has "more" than a row of 5 coins pushed close together. Explain using Piaget.',
            'steps': ['At 4, the child is in the preoperational stage.', 'They have not yet mastered conservation: the idea that quantity stays the same when appearance changes.', 'They focus on one feature (the length of the row), not the number.'],
            'answer': 'Lack of conservation, typical of the preoperational stage.',
            'check': 'By about 7 (concrete operational) the child would say both rows have the same number ✓.'},
        'mistakes': ['Treating Piaget\'s ages as exact.', 'Confusing assimilation and accommodation.', 'Thinking attachment depends mainly on feeding.', 'Saying development stops in adulthood.'],
        'real_world': 'Good teaching uses scaffolding: a teacher gives hints and worked examples at first, then steps back as students grow more confident.',
        'exam_strategy': 'Pair each theory with its key study or example (Harlow\'s monkeys, the conservation task, the strange situation).',
        'recap': ['Piaget: four stages.', 'Vygotsky: ZPD and scaffolding.', 'Attachment: comfort and responsiveness.', 'Erikson: lifespan conflicts.']},
    T2: {
        'overview': 'Motivation is what starts and directs behaviour. Emotion combines physical arousal, expression and conscious feeling.',
        'key_terms': ['Drive-reduction theory', 'Homeostasis', 'Arousal theory', 'Yerkes–Dodson law', 'Maslow\'s hierarchy', 'Intrinsic motivation', 'Extrinsic motivation', 'James–Lange theory', 'Cannon–Bard theory', 'Two-factor theory', 'Basic emotions'],
        'explanation': [
            'Drive-reduction theory says biological needs (food, water) create drives that push us to restore homeostasis. Arousal theory adds that we seek an optimal level of arousal. The Yerkes–Dodson law says performance is best at moderate arousal: too little and we are bored, too much and we panic, and the best level is lower for difficult tasks.',
            'Maslow\'s hierarchy places physiological needs at the base, then safety, love and belonging, esteem, and self-actualisation at the top; lower needs generally must be met before higher ones motivate us. Intrinsic motivation comes from enjoyment of the task; extrinsic motivation comes from external rewards, and large external rewards can sometimes reduce intrinsic interest.',
            'Theories of emotion order the parts differently. James–Lange: we feel afraid because we notice our body trembling (arousal comes first). Cannon–Bard: arousal and emotion happen at the same time. Schachter–Singer two-factor theory: emotion = physical arousal + a cognitive label based on the situation. Paul Ekman found facial expressions for six basic emotions (happiness, sadness, fear, anger, surprise, disgust) recognised across cultures.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Yerkes–Dodson: moderate arousal → best performance', 'Maslow: physiological → safety → belonging → esteem → self-actualisation', 'James–Lange: arousal → emotion', 'Cannon–Bard: arousal and emotion together', 'Schachter–Singer: arousal + label = emotion'],
        'steps': ['Identify the need or arousal level.', 'Apply the matching theory.', 'For emotion, order arousal, label and feeling.', 'Compare theories.'],
        'worked_example': {
            'problem': 'Your heart pounds on a rickety bridge, and you decide you are attracted to the person beside you. Which theory explains this best?',
            'steps': ['There is physical arousal from the bridge.', 'You look for a reason and label it using the situation (the attractive person).', 'Emotion = arousal + cognitive label: the two-factor theory.'],
            'answer': 'Schachter–Singer two-factor theory.',
            'check': 'This matches the classic "shaky bridge" study (Dutton and Aron, 1974) ✓.'},
        'mistakes': ['Saying more arousal always improves performance.', 'Treating Maslow\'s levels as strictly rigid.', 'Mixing up James–Lange and Cannon–Bard.', 'Assuming rewards always increase motivation.'],
        'real_world': 'Before exams, a little nervousness helps focus (moderate arousal), but panic harms recall; breathing exercises bring arousal back towards the optimum.',
        'exam_strategy': 'For emotion theories, draw a simple flow chart of the order of events for each; it makes comparisons quick and clear.',
        'recap': ['Drives restore homeostasis.', 'Moderate arousal is best.', 'Maslow\'s pyramid.', 'Three classic emotion theories.']},
    T3: {
        'overview': 'Personality theories explain why people differ consistently in how they think, feel and behave.',
        'key_terms': ['Id', 'Ego', 'Superego', 'Defence mechanism', 'Repression', 'Projection', 'Trait', 'Big Five', 'Unconditional positive regard', 'Self-concept', 'Reciprocal determinism', 'Self-efficacy', 'Projective test', 'Personality inventory'],
        'explanation': [
            'Freud proposed three parts: the id (instinctive desires, pleasure principle), the superego (internalised morals) and the ego (the realistic mediator). Defence mechanisms protect the ego from anxiety: repression (pushing memories into the unconscious), denial, projection (seeing your own unwanted feelings in others) and displacement (redirecting anger to a safer target). His ideas are influential but hard to test scientifically.',
            'Trait theories describe stable characteristics. The Big Five (OCEAN) are openness, conscientiousness, extraversion, agreeableness and neuroticism; they are measured with self-report inventories, are fairly stable in adulthood and are partly heritable (twin studies suggest roughly 40 to 50%). Conscientiousness predicts job and academic performance.',
            'Humanistic theorists like Carl Rogers stressed the self-concept and the need for unconditional positive regard to grow. Social-cognitive theorists like Bandura stressed reciprocal determinism (behaviour, thoughts and environment influence each other) and self-efficacy (belief in one\'s ability to succeed). Assessment ranges from projective tests (such as the Rorschach inkblots) to structured inventories (such as the MMPI), which are more reliable.'],
        'formulas_label': 'Approaches',
        'formulas': ['Psychodynamic: id, ego, superego; defence mechanisms', 'Trait: Big Five (OCEAN)', 'Humanistic: self-concept, unconditional positive regard', 'Social-cognitive: reciprocal determinism, self-efficacy'],
        'steps': ['Identify the approach from the key terms.', 'Explain the behaviour with that approach.', 'Name the assessment method used.', 'Evaluate testability.'],
        'worked_example': {
            'problem': 'After a bad day at work, Ama shouts at her younger brother rather than her boss. Name and explain the defence mechanism.',
            'steps': ['The anger is caused by the boss.', 'Expressing it to the boss is risky, so it is redirected.', 'It is aimed at a safer target: displacement.'],
            'answer': 'Displacement.',
            'check': 'Projection would mean seeing her own anger in someone else instead; here she directs it elsewhere ✓.'},
        'mistakes': ['Confusing the ego with the superego.', 'Mixing up projection and displacement.', 'Writing the Big Five without neuroticism or with "intelligence".', 'Thinking personality never changes.'],
        'real_world': 'Many employers use Big Five-based questionnaires in recruitment, especially to estimate conscientiousness.',
        'exam_strategy': 'Remember the Big Five with OCEAN, and give a one-line description of each trait.',
        'recap': ['Freud: id, ego, superego.', 'Big Five (OCEAN).', 'Rogers: positive regard.', 'Bandura: self-efficacy.']},
    T4: {
        'overview': 'Stress is the process of appraising and responding to threatening or challenging events. Long-term stress affects physical and mental health.',
        'key_terms': ['Stressor', 'General adaptation syndrome', 'HPA axis', 'Cortisol', 'Primary appraisal', 'Secondary appraisal', 'Life events', 'Daily hassles', 'Problem-focused coping', 'Emotion-focused coping', 'Social support', 'Type A behaviour'],
        'explanation': [
            'Hans Selye\'s general adaptation syndrome has three stages: alarm (the body mobilises, with adrenaline from the sympathetic system), resistance (the body copes, with high cortisol released through the hypothalamic–pituitary–adrenal (HPA) axis) and exhaustion (resources run down, raising the risk of illness). Long-term high cortisol suppresses the immune system.',
            'Lazarus argued stress depends on appraisal: in primary appraisal we judge whether a situation is threatening; in secondary appraisal we judge whether we can cope. Holmes and Rahe\'s Social Readjustment Rating Scale gives life events scores (death of a spouse 100, marriage 50, change to a different line of work 36, change in residence 20); totals above about 300 in a year are linked to higher illness risk. Daily hassles also add up.',
            'Problem-focused coping tackles the stressor (making a study timetable); emotion-focused coping manages the feelings (talking to a friend, exercise, relaxation). Social support is one of the strongest protective factors. Early research linked competitive, hostile "Type A" behaviour with heart disease; later work suggests hostility is the key ingredient.'],
        'formulas_label': 'Key ideas',
        'formulas': ['GAS: alarm → resistance → exhaustion', 'HPA axis releases cortisol', 'Stress = appraisal of demands vs resources', 'SRRS: sum life change units; > 300 = high risk', 'Coping: problem-focused vs emotion-focused'],
        'steps': ['Identify the stressor and stage.', 'Describe the bodily response.', 'Apply appraisal or life-event scoring.', 'Recommend a coping strategy.'],
        'worked_example': {
            'problem': 'In one year Daniel gets married (50), changes to a different line of work (36) and moves house (20). Calculate his SRRS score and comment.',
            'steps': ['Add the life change units: 50 + 36 + 20.', '= 106.', 'This is below 150, the threshold usually treated as low risk.'],
            'answer': '106: relatively low risk on this scale.',
            'check': 'Even positive events like marriage count, because the scale measures change, not unhappiness ✓.'},
        'mistakes': ['Thinking only negative events are stressful.', 'Confusing adrenaline (fast) with cortisol (slower, longer-lasting).', 'Saying emotion-focused coping is always worse.', 'Treating the SRRS as proof that events cause illness.'],
        'real_world': 'Students often catch colds during exam periods; studies have found reduced immune activity in students under exam stress.',
        'exam_strategy': 'Link physiology (HPA, cortisol) to health outcomes (immune suppression) explicitly; examiners reward the causal chain.',
        'recap': ['Alarm, resistance, exhaustion.', 'Cortisol via HPA axis.', 'Appraisal shapes stress.', 'Coping and support protect.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A child who understands that a ball still exists when hidden has developed:', ['object permanence', 'conservation', 'egocentrism', 'abstract reasoning'], 0, 'Sensorimotor stage.'),
    Q(T1, 'Piaget\'s preoperational stage covers roughly ages:', ['2 to 7', '0 to 2', '7 to 11', '11 and over'], 0, 'Symbolic thought, no conservation.'),
    Q(T1, 'Harlow\'s monkeys preferred the cloth mother, showing that attachment depends on:', ['comfort', 'food', 'size', 'colour'], 0, 'Contact comfort.'),
    Q(T1, 'Vygotsky\'s zone of proximal development is:', ['what a child can do with help but not yet alone', 'what a child can do alone', 'the age of formal operations', 'a type of attachment'], 0, 'Guided learning.'),
    Q(T1, 'According to Erikson, the main conflict of adolescence is:', ['identity vs role confusion', 'trust vs mistrust', 'integrity vs despair', 'intimacy vs isolation'], 0, 'Finding oneself.'),
    Q(T1, 'Ainsworth\'s procedure for assessing attachment is the:', ['strange situation', 'Bobo doll study', 'conservation task', 'visual cliff'], 0, 'Separation and reunion.'),
    # T2
    Q(T2, 'The Yerkes–Dodson law states that performance is best at:', ['moderate arousal', 'very high arousal', 'very low arousal', 'zero arousal'], 0, 'Inverted U.'),
    Q(T2, 'At the base of Maslow\'s hierarchy are:', ['physiological needs', 'esteem needs', 'self-actualisation', 'belonging needs'], 0, 'Food, water, sleep.'),
    Q(T2, 'Doing a puzzle because you enjoy it is:', ['intrinsic motivation', 'extrinsic motivation', 'drive reduction', 'negative reinforcement'], 0, 'From within.'),
    Q(T2, 'The theory that emotion = physical arousal + a cognitive label is:', ['Schachter–Singer two-factor theory', 'James–Lange theory', 'Cannon–Bard theory', 'drive-reduction theory'], 0, 'Two factors.'),
    Q(T2, '"We feel afraid because we tremble" summarises the:', ['James–Lange theory', 'Cannon–Bard theory', 'two-factor theory', 'arousal theory'], 0, 'Arousal first.'),
    Q(T2, 'Ekman\'s research found that basic facial expressions of emotion are:', ['recognised across cultures', 'learned only in Western cultures', 'impossible to read', 'different in every country'], 0, 'Universal expressions.'),
    # T3
    Q(T3, 'In Freud\'s theory, the part of personality that acts as a moral conscience is the:', ['superego', 'id', 'ego', 'libido'], 0, 'Internalised rules.'),
    Q(T3, 'Redirecting anger from a powerful person to a safer target is:', ['displacement', 'projection', 'repression', 'denial'], 0, 'Defence mechanism.'),
    Q(T3, 'Which is NOT one of the Big Five traits?', ['Intelligence', 'Conscientiousness', 'Neuroticism', 'Agreeableness'], 0, 'OCEAN.'),
    Q(T3, 'Carl Rogers argued that healthy growth needs:', ['unconditional positive regard', 'strict punishment', 'a strong superego', 'high cortisol'], 0, 'Humanistic.'),
    Q(T3, 'Belief in one\'s ability to succeed at a task is:', ['self-efficacy', 'self-actualisation', 'neuroticism', 'projection'], 0, 'Bandura.'),
    Q(T3, 'The Rorschach inkblot test is an example of a:', ['projective test', 'self-report inventory', 'IQ test', 'brain scan'], 0, 'Interprets ambiguous images.'),
    # T4
    Q(T4, 'The order of Selye\'s general adaptation syndrome is:', ['alarm, resistance, exhaustion', 'resistance, alarm, exhaustion', 'exhaustion, alarm, resistance', 'alarm, exhaustion, resistance'], 0, 'GAS.'),
    Q(T4, 'Long-term stress raises which hormone through the HPA axis?', ['Cortisol', 'Melatonin', 'Insulin', 'Oxytocin'], 0, 'From the adrenal cortex.'),
    Q(T4, 'SRRS scores: marriage 50, change to a different line of work 36, change in residence 20. The total is:', ['106', '86', '70', '56'], 0, '50 + 36 + 20.', ans=106),
    Q(T4, 'Making a revision timetable to deal with exam stress is:', ['problem-focused coping', 'emotion-focused coping', 'denial', 'displacement'], 0, 'Tackles the stressor.'),
    Q(T4, 'In Lazarus\'s model, judging whether you can cope with a stressor is:', ['secondary appraisal', 'primary appraisal', 'the alarm stage', 'displacement'], 0, 'Assessing resources.'),
    Q(T4, 'Chronic stress can increase illness mainly because cortisol:', ['suppresses the immune system', 'increases sleep', 'improves digestion', 'reduces heart rate'], 0, 'Immune suppression.'),
]

FLASH = [
    ['Conservation', 'Quantity stays the same despite changes in appearance (Piaget).'],
    ['Zone of proximal development', 'What a learner can do with help but not yet alone.'],
    ['Secure attachment', 'Infant uses carer as a safe base and is comforted on reunion.'],
    ['Yerkes–Dodson law', 'Performance peaks at moderate arousal.'],
    ['Two-factor theory', 'Emotion = arousal + cognitive label.'],
    ['Big Five', 'Openness, conscientiousness, extraversion, agreeableness, neuroticism.'],
    ['Displacement', 'Redirecting feelings to a safer target.'],
    ['General adaptation syndrome', 'Alarm, resistance, exhaustion (Selye).'],
]
