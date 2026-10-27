"""Introduction to Psychology, module 2: Biological bases of behaviour."""
from verify import Q
T1, T2, T3, T4 = ('Neurons and neurotransmission', 'The nervous system and the brain', 'Sensation and perception', 'Consciousness and sleep')
assert 0.02 * 100 == 2 and 0.02 * 500 == 10 and round(5 / 250, 2) == 0.02
assert round(8 * 60 / 90, 2) == 5.33 and 7.5 * 60 / 90 == 5

MODULE = {
    'title': 'Biological bases of behaviour',
    'topics': [T1, T2, T3, T4],
    'overview': 'Everything we think, feel and do depends on the nervous system. This module covers how neurons send signals, how the brain is organised, how our senses turn physical energy into experience, and what happens during consciousness and sleep.',
    'key_terms': ['Neuron', 'Action potential', 'Synapse', 'Neurotransmitter', 'Central nervous system', 'Cerebral cortex', 'Limbic system', 'Sensation', 'Perception', 'Transduction', 'Circadian rhythm', 'REM sleep'],
    'explanation': [
        'Neurons communicate with electrical impulses along their length and chemical messengers (neurotransmitters) across the gaps between them. Drugs and many psychological disorders act by changing this chemical signalling.',
        'The nervous system has a central part (brain and spinal cord) and a peripheral part. Different brain regions specialise in different jobs, from basic survival in the brainstem to planning and language in the cortex, although complex behaviour always involves many regions working together.',
        'Sensation is detecting physical energy; perception is organising and interpreting it, shaped by expectations and experience. Consciousness varies across the day, governed by a roughly 24-hour circadian rhythm and by sleep cycles of about 90 minutes.'],
    'quick_facts': [
        'Resting potential ≈ −70 mV; action potentials are all-or-none.',
        'Glutamate: main excitatory; GABA: main inhibitory neurotransmitter.',
        'Occipital lobe: vision; temporal: hearing; parietal: touch; frontal: planning and movement.',
        'Weber\'s law: just noticeable difference is a constant proportion of the stimulus.',
        'Sleep cycles last about 90 minutes; dreams are most vivid in REM.'],
}

NOTES = {
    T1: {
        'overview': 'Neurons are the cells that carry information. They fire electrical impulses and pass signals on chemically at synapses.',
        'key_terms': ['Dendrite', 'Cell body', 'Axon', 'Myelin sheath', 'Resting potential', 'Threshold', 'Action potential', 'All-or-none', 'Synapse', 'Neurotransmitter', 'Reuptake', 'Agonist', 'Antagonist'],
        'explanation': [
            'A neuron receives signals through its dendrites, integrates them in the cell body and sends an impulse along its axon. Many axons are wrapped in a fatty myelin sheath that speeds conduction; in multiple sclerosis the myelin is damaged and signals slow or fail.',
            'At rest the inside of a neuron is about −70 mV relative to the outside. If stimulation pushes it past a threshold (about −55 mV), sodium channels open and an action potential sweeps down the axon. The impulse is all-or-none: a stronger stimulus makes a neuron fire more often, not more strongly.',
            'At the synapse, the impulse triggers the release of neurotransmitters, which cross the gap and bind receptors on the next neuron, exciting or inhibiting it. They are then broken down or taken back up (reuptake). Key examples: acetylcholine (muscle movement, memory), dopamine (reward, movement; lost in Parkinson\'s disease), serotonin (mood, sleep), glutamate (main excitatory), GABA (main inhibitory) and endorphins (pain relief). Agonist drugs mimic or boost a neurotransmitter; antagonists block it. SSRIs, used for depression, block the reuptake of serotonin.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Dendrites → cell body → axon → terminals', 'Resting −70 mV; threshold ≈ −55 mV', 'All-or-none firing; intensity coded by firing rate', 'Agonist mimics; antagonist blocks'],
        'steps': ['Trace the signal along the neuron.', 'Describe what happens at the synapse.', 'Name the neurotransmitter involved.', 'Predict the effect of a drug.'],
        'worked_example': {
            'problem': 'SSRIs block the reuptake of serotonin. Explain how this could affect mood.',
            'steps': ['Normally serotonin is reabsorbed by the sending neuron after release.', 'Blocking reuptake leaves more serotonin in the synapse for longer.', 'More receptor activation is thought to help improve low mood over several weeks.'],
            'answer': 'More serotonin stays active in the synapse, increasing its effect.',
            'check': 'An SSRI acts like an agonist in effect, since it strengthens serotonin signalling ✓.'},
        'mistakes': ['Saying a stronger stimulus gives a bigger action potential.', 'Thinking neurons physically touch at synapses.', 'Calling all neurotransmitters excitatory.', 'Saying depression is "caused only" by low serotonin.'],
        'real_world': 'Curare, used on hunting arrows, blocks acetylcholine receptors at muscles and causes paralysis; it is an antagonist.',
        'exam_strategy': 'Use the sequence: impulse arrives → neurotransmitter released → crosses synapse → binds receptor → removed. Most marks come from the order.',
        'recap': ['Electrical within, chemical between.', 'All-or-none action potentials.', 'Neurotransmitters bind receptors.', 'Drugs act at synapses.']},
    T2: {
        'overview': 'The nervous system is organised into central and peripheral divisions. Brain regions specialise, but behaviour depends on networks.',
        'key_terms': ['Central nervous system', 'Peripheral nervous system', 'Somatic', 'Autonomic', 'Sympathetic', 'Parasympathetic', 'Brainstem', 'Cerebellum', 'Limbic system', 'Hippocampus', 'Amygdala', 'Hypothalamus', 'Cerebral cortex', 'Broca\'s area', 'Wernicke\'s area'],
        'explanation': [
            'The central nervous system is the brain and spinal cord; the peripheral nervous system connects it to the body. The somatic system controls voluntary movement; the autonomic system controls automatic functions. Its sympathetic branch prepares the body for "fight or flight" (faster heart, dilated pupils), and the parasympathetic branch calms it ("rest and digest").',
            'The brainstem controls breathing and heart rate; the cerebellum coordinates movement and balance. The limbic system includes the hippocampus (forming new memories), the amygdala (fear and emotion) and the hypothalamus (hunger, thirst, temperature, and hormones via the pituitary gland).',
            'The cerebral cortex has four lobes: frontal (planning, decision-making, personality, movement; includes Broca\'s area for speech production), parietal (touch and body position), temporal (hearing; includes Wernicke\'s area for language comprehension) and occipital (vision). Phineas Gage, whose frontal lobe was pierced by an iron rod in 1848, changed markedly in personality. Split-brain patients show that the left hemisphere usually dominates language.'],
        'formulas_label': 'Brain map',
        'formulas': ['Frontal: planning, personality, movement, Broca (speech production)', 'Parietal: touch, body position', 'Temporal: hearing, Wernicke (comprehension), memory', 'Occipital: vision', 'Hippocampus: new memories; amygdala: fear; hypothalamus: drives and hormones'],
        'steps': ['Identify the function lost or affected.', 'Match it to the region.', 'Use case evidence (Gage, H.M., split-brain).', 'Remember that regions work in networks.'],
        'worked_example': {
            'problem': 'After a stroke, a patient understands speech well but can only produce slow, halting words. Which area is likely damaged?',
            'steps': ['Comprehension is intact, so Wernicke\'s area (temporal lobe) is probably fine.', 'Speech production is impaired.', 'Speech production depends on Broca\'s area in the left frontal lobe.'],
            'answer': 'Broca\'s area, in the left frontal lobe.',
            'check': 'This pattern is called Broca\'s (expressive) aphasia ✓.'},
        'mistakes': ['Mixing up sympathetic and parasympathetic.', 'Placing vision in the frontal lobe.', 'Believing we use only 10% of our brains.', 'Confusing the hippocampus with the hypothalamus.'],
        'real_world': 'Brain scans such as fMRI show which regions become more active during tasks, but they reveal correlations, not the whole story of how the mind works.',
        'exam_strategy': 'Link each region to a case or study; examples make answers on brain function much stronger.',
        'recap': ['CNS and PNS.', 'Sympathetic vs parasympathetic.', 'Four cortical lobes.', 'Limbic system and emotion.']},
    T3: {
        'overview': 'Sensation detects physical energy from the world; perception organises and interprets it. What we perceive is a construction, not a copy.',
        'key_terms': ['Transduction', 'Absolute threshold', 'Just noticeable difference', 'Weber\'s law', 'Sensory adaptation', 'Rods', 'Cones', 'Bottom-up processing', 'Top-down processing', 'Gestalt principles', 'Depth cues', 'Perceptual set'],
        'explanation': [
            'Sense organs transduce physical energy into neural impulses: the retina turns light into signals, the cochlea turns sound vibrations into signals. Rods work in dim light; cones, packed in the fovea, detect colour and fine detail. The absolute threshold is the weakest stimulus detected half the time. Sensory adaptation reduces sensitivity to constant stimuli, which is why you stop noticing a clock ticking.',
            'Weber\'s law: the just noticeable difference (JND) is a constant proportion of the original stimulus. If the Weber fraction for weight is 0.02, you notice a 2 g change in a 100 g weight, but need 10 g for a 500 g weight.',
            'Perception combines bottom-up processing (building from sensory data) and top-down processing (using knowledge and expectations). Gestalt principles describe how we group what we see: proximity, similarity, closure and continuity, and figure–ground separation. Depth cues include binocular disparity (each eye sees a slightly different image) and monocular cues such as linear perspective and relative size. Perceptual set means expectations bias what we perceive, as when the same ambiguous symbol is read as "B" among letters and "13" among numbers.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Weber\'s law: JND = k × stimulus intensity', 'Rods: dim light; cones: colour and detail', 'Bottom-up: data-driven; top-down: knowledge-driven', 'Gestalt: proximity, similarity, closure, continuity'],
        'steps': ['Identify the sense and receptor.', 'Distinguish sensation from perception.', 'Apply Weber\'s law for thresholds.', 'Explain illusions with top-down processing.'],
        'worked_example': {
            'problem': 'A person can just tell 250 g from 255 g. Using Weber\'s law, what is the smallest difference they would notice from 500 g?',
            'steps': ['Weber fraction k = 5 ÷ 250 = 0.02.', 'JND at 500 g = 0.02 × 500.', '= 10 g.'],
            'answer': '10 g (so 510 g).',
            'check': 'The JND doubles when the standard doubles, as Weber\'s law predicts ✓.'},
        'mistakes': ['Treating sensation and perception as the same.', 'Saying rods detect colour.', 'Thinking the JND is a fixed amount.', 'Forgetting that expectations shape perception.'],
        'real_world': 'Shops raise prices in small steps that stay under the just noticeable difference, so customers are less likely to notice the increase.',
        'exam_strategy': 'For illusions, explain which assumption (such as depth or size constancy) the brain applies that leads it astray.',
        'recap': ['Transduction converts energy.', 'Weber\'s law: proportional JND.', 'Bottom-up and top-down.', 'Gestalt grouping.']},
    T4: {
        'overview': 'Consciousness is our awareness of ourselves and our surroundings. It changes through the day, and sleep is its most regular shift.',
        'key_terms': ['Consciousness', 'Circadian rhythm', 'Suprachiasmatic nucleus', 'Melatonin', 'NREM sleep', 'REM sleep', 'Sleep cycle', 'Insomnia', 'Narcolepsy', 'Sleep apnoea', 'Psychoactive drug'],
        'explanation': [
            'The circadian rhythm is a roughly 24-hour cycle of alertness, body temperature and hormones, set by the suprachiasmatic nucleus (SCN) in the hypothalamus and reset by daylight. As darkness falls, the pineal gland releases melatonin, which promotes sleep. Jet lag and shift work disturb this rhythm.',
            'Sleep runs in cycles of about 90 minutes, four to six per night (about 5 cycles in 7.5 hours). Each cycle passes through NREM stages N1 (light), N2 (sleep spindles) and N3 (deep, slow-wave sleep, important for physical restoration) and then REM sleep, when the brain is very active, the eyes move rapidly, most vivid dreams occur and the body\'s muscles are temporarily paralysed. Deep sleep dominates early in the night; REM periods lengthen towards morning.',
            'Most adults need 7 to 9 hours. Sleep deprivation harms attention, memory and mood. Disorders include insomnia (difficulty falling or staying asleep), narcolepsy (sudden attacks of sleep) and sleep apnoea (breathing stops repeatedly). Psychoactive drugs alter consciousness: depressants (alcohol) slow the nervous system, stimulants (caffeine, nicotine) speed it up, and hallucinogens distort perception.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Circadian rhythm ≈ 24 h, set by the SCN', 'Sleep cycle ≈ 90 min: N1 → N2 → N3 → REM', 'REM: vivid dreams, active brain, muscle paralysis', 'Adults need 7 to 9 hours'],
        'steps': ['Identify the stage or rhythm.', 'Describe its features.', 'Link to brain structures or hormones.', 'Apply to real situations (jet lag, exams).'],
        'worked_example': {
            'problem': 'A student sleeps 7.5 hours. Roughly how many sleep cycles is that, and when will most REM sleep occur?',
            'steps': ['7.5 h = 450 min.', '450 ÷ 90 = 5 cycles.', 'REM periods lengthen through the night, so most REM occurs in the later cycles, towards morning.'],
            'answer': 'About 5 cycles; most REM near morning.',
            'check': 'Cutting sleep short by waking early removes mostly REM, which matters for memory consolidation ✓.'},
        'mistakes': ['Saying the brain "switches off" in sleep.', 'Thinking dreams occur only in REM (they are most vivid there).', 'Confusing circadian rhythm with the sleep cycle.', 'Calling alcohol a stimulant.'],
        'real_world': 'Many countries\' road-safety campaigns warn that driving after 17 to 19 hours awake impairs performance about as much as being at the legal alcohol limit.',
        'exam_strategy': 'Draw a hypnogram (sleep stages across the night) if allowed; it shows cycles, deep sleep early and REM late at a glance.',
        'recap': ['24-hour circadian rhythm.', '90-minute sleep cycles.', 'REM: dreams and paralysis.', 'Drugs alter consciousness.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The resting potential of a neuron is about:', ['−70 mV', '+70 mV', '0 mV', '−5 mV'], 0, 'Inside negative.'),
    Q(T1, 'Action potentials are described as all-or-none, meaning:', ['a neuron either fires fully or not at all', 'all neurons fire together', 'stronger stimuli give bigger impulses', 'neurons fire only once'], 0, 'Intensity coded by rate.'),
    Q(T1, 'The fatty layer that speeds up conduction along axons is:', ['the myelin sheath', 'the dendrite', 'the synapse', 'the cell body'], 0, 'Damaged in MS.'),
    Q(T1, 'The main inhibitory neurotransmitter in the brain is:', ['GABA', 'glutamate', 'dopamine', 'acetylcholine'], 0, 'Calms activity.'),
    Q(T1, 'Parkinson\'s disease involves the loss of neurons that produce:', ['dopamine', 'serotonin', 'GABA', 'endorphins'], 0, 'Movement problems.'),
    Q(T1, 'A drug that blocks a neurotransmitter\'s receptors is:', ['an antagonist', 'an agonist', 'a reuptake inhibitor', 'a hormone'], 0, 'Blocks the effect.'),
    # T2
    Q(T2, 'The "fight or flight" response is controlled by the:', ['sympathetic nervous system', 'parasympathetic nervous system', 'somatic nervous system', 'cerebellum'], 0, 'Autonomic arousal.'),
    Q(T2, 'Vision is processed mainly in the:', ['occipital lobe', 'frontal lobe', 'temporal lobe', 'parietal lobe'], 0, 'Back of the brain.'),
    Q(T2, 'A patient understands speech but struggles to produce it. Damage is likely in:', ['Broca\'s area', 'Wernicke\'s area', 'the occipital lobe', 'the cerebellum'], 0, 'Left frontal lobe.'),
    Q(T2, 'The structure most important for forming new long-term memories is the:', ['hippocampus', 'amygdala', 'cerebellum', 'brainstem'], 0, 'Patient H.M.'),
    Q(T2, 'Phineas Gage\'s injury showed the role of the frontal lobe in:', ['personality and planning', 'vision', 'hearing', 'balance'], 0, 'Personality changed.'),
    Q(T2, 'The hypothalamus regulates:', ['hunger, thirst and body temperature', 'balance', 'vision', 'language comprehension'], 0, 'And hormones via the pituitary.'),
    # T3
    Q(T3, 'Converting physical energy into neural signals is called:', ['transduction', 'perception', 'adaptation', 'accommodation'], 0, 'Done by receptors.'),
    Q(T3, 'If the Weber fraction is 0.02, the just noticeable difference for a 500 g weight is:', ['10 g', '2 g', '25 g', '0.02 g'], 0, '0.02 × 500.', ans=10),
    Q(T3, 'Cones in the retina are responsible for:', ['colour vision and fine detail', 'vision in dim light', 'hearing', 'balance'], 0, 'Packed in the fovea.'),
    Q(T3, 'Using expectations and knowledge to interpret sensations is:', ['top-down processing', 'bottom-up processing', 'transduction', 'sensory adaptation'], 0, 'Concept-driven.'),
    Q(T3, 'We tend to group objects that are close together. This Gestalt principle is:', ['proximity', 'similarity', 'closure', 'continuity'], 0, 'Nearness.'),
    Q(T3, 'Ceasing to notice a constant smell after a while is:', ['sensory adaptation', 'perceptual set', 'transduction', 'top-down processing'], 0, 'Receptors respond less.'),
    # T4
    Q(T4, 'A typical sleep cycle lasts about:', ['90 minutes', '30 minutes', '4 hours', '10 minutes'], 0, 'Four to six per night.'),
    Q(T4, 'Vivid dreaming and temporary muscle paralysis occur mainly during:', ['REM sleep', 'N1 sleep', 'N3 sleep', 'wakefulness'], 0, 'Rapid eye movement.'),
    Q(T4, 'The circadian rhythm is controlled by the:', ['suprachiasmatic nucleus', 'amygdala', 'cerebellum', 'Broca\'s area'], 0, 'In the hypothalamus.'),
    Q(T4, 'Darkness triggers the release of which sleep-promoting hormone?', ['Melatonin', 'Adrenaline', 'Insulin', 'Cortisol'], 0, 'From the pineal gland.'),
    Q(T4, '7.5 hours of sleep is about how many 90-minute cycles?', ['5', '7', '3', '8'], 0, '450 ÷ 90.', ans=5),
    Q(T4, 'Alcohol is classed as a:', ['depressant', 'stimulant', 'hallucinogen', 'opioid'], 0, 'Slows the nervous system.'),
]

FLASH = [
    ['Action potential', 'All-or-none electrical impulse along an axon.'],
    ['Synapse', 'Gap where neurotransmitters pass signals between neurons.'],
    ['Agonist / antagonist', 'Agonist mimics a neurotransmitter; antagonist blocks it.'],
    ['Sympathetic system', 'Fight or flight; parasympathetic: rest and digest.'],
    ['Broca\'s area', 'Left frontal lobe; speech production.'],
    ['Weber\'s law', 'JND is a constant proportion of the stimulus.'],
    ['Top-down processing', 'Perception guided by knowledge and expectations.'],
    ['REM sleep', 'Active brain, vivid dreams, muscle paralysis.'],
]
