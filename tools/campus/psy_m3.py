"""Introduction to Psychology, module 3: Learning, memory and cognition."""
from verify import Q
T1, T2, T3, T4 = ('Classical conditioning', 'Operant and observational learning', 'Memory', 'Thinking, language and intelligence')
assert 10 / 8 * 100 == 125 and 12 / 12 * 100 == 100 and 9 / 12 * 100 == 75
assert len('1492 1776 1066'.split()) == 3 and len('149217761066') == 12

MODULE = {
    'title': 'Learning, memory and cognition',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module covers how experience changes behaviour (classical, operant and observational learning), how memories are encoded, stored and retrieved, and how we think, solve problems, use language and differ in intelligence.',
    'key_terms': ['Classical conditioning', 'Conditioned stimulus', 'Operant conditioning', 'Reinforcement', 'Punishment', 'Observational learning', 'Short-term memory', 'Long-term memory', 'Working memory', 'Heuristic', 'Cognitive bias', 'Intelligence quotient'],
    'explanation': [
        'Learning is a relatively lasting change in behaviour due to experience. In classical conditioning we learn to associate two stimuli; in operant conditioning we learn from the consequences of our actions; in observational learning we copy others.',
        'Memory involves encoding, storage and retrieval. Information passes from sensory memory to a limited short-term or working memory and, with processing, into long-term memory. Forgetting comes from decay, interference and retrieval failure, and memories are reconstructed rather than replayed.',
        'Thinking relies on concepts, algorithms and fast but fallible shortcuts called heuristics. Language develops rapidly in early childhood. Intelligence can be viewed as one general ability (g) or several, and is measured with standardised IQ tests.'],
    'quick_facts': [
        'Classical: UCS → UCR; after pairing, CS → CR.',
        'Reinforcement increases behaviour; punishment decreases it.',
        'Negative reinforcement removes something unpleasant (it is not punishment).',
        'Short-term memory holds about 7 ± 2 items for about 18 to 30 seconds without rehearsal.',
        'Ratio IQ = mental age ÷ chronological age × 100.'],
}

NOTES = {
    T1: {
        'overview': 'Classical conditioning is learning by association. A neutral stimulus comes to trigger a response after being paired with a stimulus that already causes it.',
        'key_terms': ['Unconditioned stimulus (UCS)', 'Unconditioned response (UCR)', 'Neutral stimulus', 'Conditioned stimulus (CS)', 'Conditioned response (CR)', 'Acquisition', 'Extinction', 'Spontaneous recovery', 'Generalisation', 'Discrimination'],
        'explanation': [
            'Ivan Pavlov noticed dogs salivating before food arrived. Food (UCS) naturally causes salivation (UCR). A bell (neutral stimulus) was rung just before food many times. Eventually the bell alone (now a CS) caused salivation (now a CR). This build-up is acquisition.',
            'If the CS is repeatedly presented without the UCS, the CR fades: extinction. After a rest, the CR may briefly return: spontaneous recovery. Generalisation means similar stimuli (a different bell) also trigger the CR; discrimination means learning to respond only to the specific CS.',
            'In 1920 Watson and Rayner conditioned "Little Albert", an infant, to fear a white rat by pairing it with a loud noise; the fear generalised to other furry objects. The study is now seen as unethical, but it showed how phobias can be learned. Classical conditioning also explains taste aversions and is used in therapy, for example systematic desensitisation for phobias.'],
        'formulas_label': 'The sequence',
        'formulas': ['Before: UCS → UCR; NS → no response', 'During: NS + UCS → UCR (repeated pairings)', 'After: CS → CR', 'CS without UCS repeatedly → extinction'],
        'steps': ['Find what naturally causes the response (UCS, UCR).', 'Find the neutral stimulus that gets paired with it.', 'Label CS and CR after learning.', 'Apply extinction, generalisation or discrimination.'],
        'worked_example': {
            'problem': 'Every time Thandi\'s phone plays a certain ringtone, her manager calls to criticise her, and her heart races. Now the ringtone alone makes her heart race. Label the parts.',
            'steps': ['UCS: the criticism; UCR: racing heart in response to criticism.', 'NS that becomes the CS: the ringtone.', 'CR: racing heart in response to the ringtone alone.'],
            'answer': 'UCS criticism, UCR racing heart, CS ringtone, CR racing heart to the ringtone.',
            'check': 'The response is the same behaviour (racing heart) but is labelled UCR or CR depending on what triggers it ✓.'},
        'mistakes': ['Labelling the response by what it is rather than what triggers it.', 'Confusing extinction with forgetting.', 'Presenting the NS after the UCS (it should come just before).', 'Mixing up generalisation and discrimination.'],
        'real_world': 'Advertisers pair products with attractive people and upbeat music so that positive feelings become associated with the product.',
        'exam_strategy': 'Always set out before, during and after conditioning, labelling each stimulus and response.',
        'recap': ['Learning by association.', 'UCS, UCR, CS, CR.', 'Extinction and spontaneous recovery.', 'Little Albert: learned fear.']},
    T2: {
        'overview': 'In operant conditioning, behaviour is shaped by its consequences. In observational learning, we learn by watching others.',
        'key_terms': ['Law of effect', 'Positive reinforcement', 'Negative reinforcement', 'Positive punishment', 'Negative punishment', 'Shaping', 'Schedules of reinforcement', 'Variable ratio', 'Modelling', 'Vicarious reinforcement'],
        'explanation': [
            'Thorndike\'s law of effect: behaviours followed by satisfying outcomes become more likely. B. F. Skinner studied this with the "Skinner box". "Positive" means adding something and "negative" means removing something; "reinforcement" increases behaviour and "punishment" decreases it. Positive reinforcement: praise for homework. Negative reinforcement: taking a painkiller removes a headache, so you take painkillers again. Positive punishment: a fine for speeding. Negative punishment: losing phone time for breaking a rule.',
            'Shaping reinforces successive approximations to a target behaviour, used in animal training. Schedules matter: continuous reinforcement gives fast learning; partial schedules give behaviour that lasts longer. Fixed ratio (a reward after every n responses), variable ratio (after an unpredictable number, as with slot machines, the most resistant to extinction), fixed interval (after a set time, like a monthly salary) and variable interval (after unpredictable times, like checking for messages).',
            'Albert Bandura\'s Bobo doll study (1961) showed that children who watched an adult attack an inflatable doll were more likely to act aggressively themselves. Observational learning needs attention, retention, reproduction and motivation. Seeing a model rewarded (vicarious reinforcement) increases imitation.'],
        'formulas_label': 'The 2 × 2 grid',
        'formulas': ['Positive reinforcement: add pleasant → behaviour ↑', 'Negative reinforcement: remove unpleasant → behaviour ↑', 'Positive punishment: add unpleasant → behaviour ↓', 'Negative punishment: remove pleasant → behaviour ↓', 'Variable ratio: most resistant to extinction'],
        'steps': ['Ask: is something added or removed?', 'Ask: does the behaviour increase or decrease?', 'Combine to name the consequence.', 'For schedules, ask: ratio or interval, fixed or variable?'],
        'worked_example': {
            'problem': 'A driver fastens her seat belt to stop the car\'s annoying beeping. Which type of consequence is this?',
            'steps': ['Something unpleasant (the beeping) is removed: negative.', 'Seat-belt use increases: reinforcement.', 'So it is negative reinforcement.'],
            'answer': 'Negative reinforcement.',
            'check': 'It is not punishment, because the behaviour (wearing the belt) becomes more likely ✓.'},
        'mistakes': ['Calling negative reinforcement a punishment.', 'Thinking "positive" means "good".', 'Assuming continuous reinforcement produces the most persistent behaviour.', 'Forgetting motivation in Bandura\'s model.'],
        'real_world': 'Social media apps use variable-ratio reinforcement: likes and messages arrive unpredictably, keeping users checking.',
        'exam_strategy': 'Draw the 2 × 2 grid (add/remove × increase/decrease) at the top of your answer and place each example in it.',
        'recap': ['Consequences shape behaviour.', 'Positive adds, negative removes.', 'Variable ratio resists extinction.', 'Bandura: learning by watching.']},
    T3: {
        'overview': 'Memory encodes, stores and retrieves information. Models describe its structure, and research shows memories are reconstructed and can be distorted.',
        'key_terms': ['Encoding', 'Storage', 'Retrieval', 'Multi-store model', 'Sensory memory', 'Short-term memory', 'Long-term memory', 'Chunking', 'Working memory model', 'Serial position effect', 'Interference', 'Reconstructive memory', 'Leading question'],
        'explanation': [
            'Atkinson and Shiffrin\'s multi-store model (1968) describes sensory memory (very brief), short-term memory (about 7 ± 2 items, roughly 18 to 30 seconds without rehearsal) and long-term memory (vast, potentially lifelong). Rehearsal moves information to long-term memory. Chunking increases short-term capacity: 149217761066 is 12 digits, but as the years 1492, 1776 and 1066 it is only 3 chunks.',
            'Baddeley and Hitch\'s working memory model (1974) splits short-term memory into a central executive that directs attention, a phonological loop (sounds and words), a visuospatial sketchpad (images and space) and, added in 2000, an episodic buffer. The serial position effect supports separate stores: we recall the first items (primacy, from long-term memory) and last items (recency, still in short-term memory) better than the middle.',
            'Forgetting has several causes: decay, interference (old learning disrupts new = proactive; new disrupts old = retroactive) and retrieval failure (missing cues). Memory is reconstructive. Loftus and Palmer (1974) showed films of car crashes; people asked how fast the cars were going when they "smashed" estimated higher speeds than those asked about cars that "contacted" each other, and were more likely to falsely report broken glass. This matters for eyewitness testimony.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Multi-store: sensory → STM → LTM', 'STM ≈ 7 ± 2 items, ≈ 18–30 s', 'Working memory: central executive, phonological loop, visuospatial sketchpad, episodic buffer', 'Primacy (LTM) and recency (STM)', 'Proactive: old disrupts new; retroactive: new disrupts old'],
        'steps': ['Identify the stage (encoding, storage, retrieval).', 'Match to a model component.', 'Explain forgetting with the right theory.', 'Use classic studies as evidence.'],
        'worked_example': {
            'problem': 'After moving house, Kwame keeps writing his old address on forms. Which type of forgetting is this, and why?',
            'steps': ['The old address (earlier learning) is getting in the way.', 'It disrupts recall of the new address (later learning).', 'Old disrupting new is proactive interference.'],
            'answer': 'Proactive interference.',
            'check': 'If the new address made him forget the old one, that would be retroactive ✓.'},
        'mistakes': ['Mixing up proactive and retroactive interference.', 'Thinking memory works like a video recording.', 'Saying short-term memory has unlimited capacity.', 'Confusing primacy and recency with their stores.'],
        'real_world': 'Police interview techniques such as the cognitive interview avoid leading questions and use context cues to reduce errors in eyewitness accounts.',
        'exam_strategy': 'Support each model with a study (serial position for multi-store; dual-task studies for working memory; Loftus and Palmer for reconstruction).',
        'recap': ['Encoding, storage, retrieval.', 'STM is small and brief.', 'Working memory has components.', 'Memory reconstructs.']},
    T4: {
        'overview': 'Cognition covers how we think, solve problems, make decisions and use language. Intelligence describes differences in these abilities.',
        'key_terms': ['Concept', 'Prototype', 'Algorithm', 'Heuristic', 'Availability heuristic', 'Representativeness heuristic', 'Confirmation bias', 'Functional fixedness', 'Critical period', 'General intelligence (g)', 'Multiple intelligences', 'Intelligence quotient', 'Flynn effect'],
        'explanation': [
            'Algorithms are step-by-step procedures that guarantee a solution; heuristics are mental shortcuts that are fast but can mislead. The availability heuristic judges likelihood by how easily examples come to mind (people overestimate plane crashes after news coverage). The representativeness heuristic judges by similarity to a prototype. Confirmation bias is seeking evidence that supports what we already believe; functional fixedness is failing to see new uses for familiar objects.',
            'Language develops from babbling (about 6 months) to first words (about 12 months) to two-word speech (about 18 to 24 months). Noam Chomsky proposed an inborn capacity for grammar; learning theorists stress imitation and reinforcement. Evidence suggests a critical (or sensitive) period: language is acquired most easily in early childhood.',
            'Spearman proposed a general intelligence factor (g) underlying all mental tasks. Gardner proposed multiple intelligences (such as linguistic, logical-mathematical, musical and interpersonal); Sternberg proposed analytical, creative and practical intelligence. Early IQ was mental age ÷ chronological age × 100: a child of 8 performing like a typical 10-year-old scores 125. Modern IQ tests use deviation scores (mean 100, SD 15). Average IQ scores rose over the twentieth century (the Flynn effect), showing environmental influences.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Ratio IQ = mental age ÷ chronological age × 100', 'Deviation IQ: mean 100, SD 15', 'Algorithm: guaranteed, slow; heuristic: fast, error-prone', 'Spearman g vs Gardner multiple intelligences'],
        'steps': ['Identify the thinking strategy or bias.', 'Explain why it leads to the outcome.', 'Calculate ratio IQ if given ages.', 'Compare theories of intelligence.'],
        'worked_example': {
            'problem': 'An 8-year-old performs on a test like a typical 10-year-old. Calculate the ratio IQ and comment.',
            'steps': ['Ratio IQ = mental age ÷ chronological age × 100.', '= 10 ÷ 8 × 100.', '= 125.'],
            'answer': '125, well above average (100).',
            'check': 'A child performing exactly at age level would score 100, so 125 is sensibly higher ✓.'},
        'mistakes': ['Confusing heuristics with algorithms.', 'Thinking IQ measures all forms of intelligence.', 'Using ratio IQ for adults (mental age stops rising).', 'Assuming IQ differences are purely genetic.'],
        'real_world': 'Doctors are trained to avoid the availability heuristic by working through a list of possible diagnoses rather than jumping to the most memorable recent case.',
        'exam_strategy': 'For bias questions, name the bias, define it in one line and apply it to the example given.',
        'recap': ['Algorithms vs heuristics.', 'Biases mislead judgement.', 'Critical period for language.', 'g vs multiple intelligences.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'In Pavlov\'s experiment, the food was the:', ['unconditioned stimulus', 'conditioned stimulus', 'conditioned response', 'neutral stimulus'], 0, 'Naturally causes salivation.'),
    Q(T1, 'After conditioning, the bell is the:', ['conditioned stimulus', 'unconditioned stimulus', 'unconditioned response', 'reinforcer'], 0, 'Learned trigger.'),
    Q(T1, 'Presenting the CS repeatedly without the UCS leads to:', ['extinction', 'acquisition', 'generalisation', 'shaping'], 0, 'The CR fades.'),
    Q(T1, 'Little Albert\'s fear of other furry objects as well as the rat shows:', ['stimulus generalisation', 'discrimination', 'extinction', 'spontaneous recovery'], 0, 'Similar stimuli trigger the CR.'),
    Q(T1, 'A previously extinguished response briefly reappears after a rest. This is:', ['spontaneous recovery', 'acquisition', 'shaping', 'discrimination'], 0, 'Returns after a pause.'),
    Q(T1, 'Classical conditioning involves learning:', ['associations between stimuli', 'from the consequences of behaviour', 'by watching models', 'through insight only'], 0, 'Pavlov.'),
    # T2
    Q(T2, 'Taking a painkiller to get rid of a headache, and so taking painkillers more often, is:', ['negative reinforcement', 'positive punishment', 'negative punishment', 'positive reinforcement'], 0, 'Removing an unpleasant state increases behaviour.'),
    Q(T2, 'Losing phone privileges for breaking a rule is:', ['negative punishment', 'negative reinforcement', 'positive punishment', 'positive reinforcement'], 0, 'Something pleasant is removed.'),
    Q(T2, 'Which schedule of reinforcement is most resistant to extinction?', ['Variable ratio', 'Fixed ratio', 'Fixed interval', 'Continuous'], 0, 'Slot machines.'),
    Q(T2, 'Reinforcing successive approximations to a target behaviour is called:', ['shaping', 'extinction', 'generalisation', 'modelling'], 0, 'Step by step.'),
    Q(T2, 'Bandura\'s Bobo doll study demonstrated:', ['observational learning', 'classical conditioning', 'insight learning', 'the law of effect'], 0, 'Children copied aggression.'),
    Q(T2, 'A monthly salary is an example of which schedule?', ['Fixed interval', 'Variable interval', 'Fixed ratio', 'Variable ratio'], 0, 'Set time.'),
    # T3
    Q(T3, 'The capacity of short-term memory is about:', ['7 ± 2 items', 'unlimited', '1 item', '100 items'], 0, 'Miller (1956).'),
    Q(T3, 'The digits 149217761066 grouped as 1492, 1776, 1066 form how many chunks?', ['3', '12', '4', '6'], 0, 'Three meaningful years.', ans=3),
    Q(T3, 'Better recall of the last few items of a list is the:', ['recency effect', 'primacy effect', 'proactive effect', 'Flynn effect'], 0, 'Still in STM.'),
    Q(T3, 'New learning disrupting the recall of older memories is:', ['retroactive interference', 'proactive interference', 'decay', 'chunking'], 0, 'New acts backwards.'),
    Q(T3, 'Loftus and Palmer\'s study showed that:', ['leading questions can distort eyewitness memory', 'STM holds 7 items', 'memory is like a video', 'dogs can be conditioned'], 0, '"Smashed" vs "contacted".'),
    Q(T3, 'In the working memory model, the component that directs attention is the:', ['central executive', 'phonological loop', 'visuospatial sketchpad', 'sensory register'], 0, 'Supervises the slave systems.'),
    # T4
    Q(T4, 'An 8-year-old with a mental age of 10 has a ratio IQ of:', ['125', '80', '100', '120'], 0, '10/8 × 100.', ans=125),
    Q(T4, 'Judging how likely an event is by how easily examples come to mind is the:', ['availability heuristic', 'representativeness heuristic', 'confirmation bias', 'functional fixedness'], 0, 'Memorable events seem common.'),
    Q(T4, 'Seeking only information that supports what you already believe is:', ['confirmation bias', 'functional fixedness', 'an algorithm', 'chunking'], 0, 'A cognitive bias.'),
    Q(T4, 'A step-by-step procedure that guarantees a solution is:', ['an algorithm', 'a heuristic', 'a prototype', 'insight'], 0, 'Slow but certain.'),
    Q(T4, 'Howard Gardner proposed:', ['multiple intelligences', 'a single general factor g', 'the IQ ratio formula', 'the Flynn effect'], 0, 'Musical, interpersonal, and others.'),
    Q(T4, 'The rise in average IQ scores over the twentieth century is called the:', ['Flynn effect', 'serial position effect', 'placebo effect', 'recency effect'], 0, 'Environmental influences.'),
]

FLASH = [
    ['Classical conditioning', 'Learning by association: NS paired with UCS becomes a CS.'],
    ['Extinction', 'CR fades when the CS appears repeatedly without the UCS.'],
    ['Negative reinforcement', 'Removing something unpleasant to increase behaviour.'],
    ['Variable ratio', 'Reward after an unpredictable number of responses; most persistent.'],
    ['Observational learning', 'Learning by watching models (Bandura).'],
    ['Chunking', 'Grouping items to increase short-term memory capacity.'],
    ['Proactive interference', 'Old learning disrupts recall of new learning.'],
    ['Availability heuristic', 'Judging likelihood by how easily examples come to mind.'],
]
