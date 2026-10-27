"""Cell Biology, module 4: Cell energetics."""
from verify import Q
T1, T2, T3, T4 = ('Energy, ATP and enzymes', 'Glycolysis, the link reaction and the Krebs cycle', 'Oxidative phosphorylation and fermentation', 'Photosynthesis')
assert 4 * 2 ** ((35 - 25) / 10) == 8
# per glucose
co2 = 2 + 2 * 2; nadh = 2 + 2 + 2 * 3; fadh2 = 2 * 1; atp_sub = 2 + 2 * 1
assert (co2, nadh, fadh2, atp_sub) == (6, 10, 2, 4)
assert nadh * 2.5 + fadh2 * 1.5 + atp_sub == 32
assert round(32 * 30.5 / 2870 * 100) == 34
assert round(3.6 / 8.0, 2) == 0.45
assert 6 * 3 == 18 and 6 * 2 == 12

MODULE = {
    'title': 'Cell energetics',
    'topics': [T1, T2, T3, T4],
    'overview': 'Cells need a constant supply of energy. This module covers enzymes and ATP, then follows glucose through aerobic respiration (glycolysis, the link reaction, the Krebs cycle and oxidative phosphorylation), anaerobic fermentation, and photosynthesis, which captures light energy to make the sugars in the first place.',
    'key_terms': ['ATP', 'Enzyme', 'Activation energy', 'Active site', 'Inhibitor', 'Glycolysis', 'Krebs cycle', 'NADH', 'Electron transport chain', 'Chemiosmosis', 'ATP synthase', 'Fermentation', 'Light-dependent reactions', 'Calvin cycle'],
    'explanation': [
        'ATP is the cell\'s energy currency: hydrolysing it to ADP and phosphate releases energy in small, usable amounts. Enzymes speed up the reactions that make and use ATP by lowering their activation energy.',
        'Aerobic respiration oxidises glucose to carbon dioxide and water in stages. Glycolysis in the cytoplasm splits glucose into pyruvate; the link reaction and Krebs cycle in the mitochondrial matrix release CO₂ and load electrons onto NAD and FAD; oxidative phosphorylation on the inner membrane uses those electrons to make most of the ATP, with oxygen as the final electron acceptor.',
        'Without oxygen, cells use fermentation to regenerate NAD so that glycolysis can continue, at a much lower ATP yield. Photosynthesis runs in the opposite direction: light-dependent reactions in the thylakoids make ATP and NADPH, and the Calvin cycle in the stroma uses them to fix CO₂ into sugar.'],
    'quick_facts': [
        'Respiration: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O (+ ATP).',
        'Glycolysis: net 2 ATP and 2 NADH per glucose, in the cytoplasm.',
        'Per glucose, aerobic respiration yields about 30 to 32 ATP.',
        'Oxygen is the final electron acceptor, forming water.',
        'Photosynthesis: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.'],
}

NOTES = {
    T1: {
        'overview': 'ATP transfers energy within cells, and enzymes control the rate of every metabolic reaction.',
        'key_terms': ['ATP', 'ADP', 'Hydrolysis', 'Phosphorylation', 'Activation energy', 'Active site', 'Induced fit', 'Optimum', 'Q₁₀', 'Competitive inhibitor', 'Non-competitive inhibitor'],
        'explanation': [
            'ATP (adenosine triphosphate) is hydrolysed by ATPase to ADP + Pᵢ, releasing about 30.5 kJ/mol. The energy powers muscle contraction, active transport and synthesis. ATP is remade from ADP by phosphorylation during respiration and photosynthesis. It is a good energy currency because it releases energy in small amounts, in one step, and is quickly regenerated.',
            'Enzymes are biological catalysts, usually proteins. The substrate binds the active site, which changes shape slightly to fit it closely (induced fit), lowering the activation energy. Rate rises with temperature up to an optimum because molecules collide more often; above it the enzyme denatures. Q₁₀ ≈ 2 for many reactions: a rate of 4 units at 25 °C becomes about 8 units at 35 °C.',
            'Competitive inhibitors resemble the substrate and compete for the active site; adding more substrate overcomes them. Non-competitive inhibitors bind elsewhere (an allosteric site), change the shape of the active site and cannot be overcome by more substrate. Cells use end-product inhibition to switch off pathways when enough product has been made.'],
        'formulas_label': 'Key ideas',
        'formulas': ['ATP + H₂O → ADP + Pᵢ + energy (≈ 30.5 kJ/mol)', 'Q₁₀ = rate at (T + 10)/rate at T', 'Competitive: same site, overcome by more substrate', 'Non-competitive: other site, not overcome'],
        'steps': ['Identify what changes (temperature, pH, substrate, inhibitor).', 'Link to collisions or shape of the active site.', 'Predict the effect on rate.', 'Name the type of inhibition if relevant.'],
        'worked_example': {
            'problem': 'Adding much more substrate restores the rate of an inhibited enzyme reaction. What type of inhibitor is present? Explain.',
            'steps': ['Extra substrate wins the competition for the active site.', 'This only works if the inhibitor binds the active site itself.', 'So it is a competitive inhibitor.'],
            'answer': 'A competitive inhibitor.',
            'check': 'A non-competitive inhibitor changes the active site shape, so extra substrate would not help ✓.'},
        'mistakes': ['Saying enzymes are "killed" by heat.', 'Saying enzymes provide energy for reactions.', 'Confusing the two kinds of inhibitor.', 'Saying ATP stores large amounts of energy long-term.'],
        'real_world': 'Many medicines are enzyme inhibitors: aspirin inhibits cyclooxygenase, and statins inhibit HMG-CoA reductase to lower cholesterol.',
        'exam_strategy': 'For graph questions, describe first (with numbers from the graph), then explain using collisions and active-site shape.',
        'recap': ['ATP → ADP + Pᵢ releases energy.', 'Enzymes lower activation energy.', 'Optimum, then denaturation.', 'Competitive vs non-competitive.']},
    T2: {
        'overview': 'The first stages of respiration split glucose and strip it of high-energy electrons, which are carried by NADH and FADH₂ to the final stage.',
        'key_terms': ['Glycolysis', 'Pyruvate', 'NAD', 'NADH', 'Link reaction', 'Acetyl coenzyme A', 'Krebs cycle', 'Decarboxylation', 'Dehydrogenation', 'FAD', 'Substrate-level phosphorylation'],
        'explanation': [
            'Glycolysis happens in the cytoplasm and does not need oxygen. Glucose is phosphorylated (using 2 ATP), split into two 3-carbon molecules and oxidised to 2 pyruvate. It produces 4 ATP, so the net gain is 2 ATP, plus 2 NADH.',
            'In aerobic conditions, pyruvate enters the mitochondrial matrix. The link reaction removes CO₂ (decarboxylation) and hydrogen (dehydrogenation), forming acetyl coenzyme A and NADH. Per glucose: 2 CO₂ and 2 NADH.',
            'In the Krebs cycle, acetyl CoA (2C) joins oxaloacetate (4C) to form citrate (6C), which is broken back down to oxaloacetate. Each turn releases 2 CO₂ and makes 3 NADH, 1 FADH₂ and 1 ATP. Glucose gives two turns. Totals per glucose before oxidative phosphorylation: 6 CO₂, 10 NADH, 2 FADH₂ and 4 ATP.'],
        'formulas_label': 'Per glucose',
        'formulas': ['Glycolysis: net 2 ATP, 2 NADH, 2 pyruvate (cytoplasm)', 'Link reaction (×2): 2 CO₂, 2 NADH, 2 acetyl CoA (matrix)', 'Krebs cycle (×2): 4 CO₂, 6 NADH, 2 FADH₂, 2 ATP (matrix)', 'Totals: 6 CO₂, 10 NADH, 2 FADH₂, 4 ATP'],
        'steps': ['Locate the stage.', 'Count per pyruvate, then double for glucose.', 'Track carbon atoms as CO₂.', 'Track hydrogen carried by NAD and FAD.'],
        'worked_example': {
            'problem': 'How many molecules of CO₂ and NADH are produced per glucose by the link reaction and Krebs cycle together?',
            'steps': ['Link reaction: 1 CO₂ and 1 NADH per pyruvate; ×2 = 2 CO₂, 2 NADH.', 'Krebs cycle: 2 CO₂ and 3 NADH per turn; ×2 = 4 CO₂, 6 NADH.', 'Together: 6 CO₂ and 8 NADH.'],
            'answer': '6 CO₂ and 8 NADH (10 NADH including glycolysis).',
            'check': 'Glucose has 6 carbons and all of them leave as CO₂ ✓.'},
        'mistakes': ['Forgetting to double for two pyruvates.', 'Saying glycolysis needs oxygen.', 'Placing the Krebs cycle in the cytoplasm.', 'Saying glycolysis makes 4 ATP overall (it is 2 net).'],
        'real_world': 'The poison arsenite blocks pyruvate dehydrogenase in the link reaction, starving cells of acetyl CoA.',
        'exam_strategy': 'Keep a small table of products per stage; doubling errors are the most common lost marks.',
        'recap': ['Glycolysis: net 2 ATP, cytoplasm.', 'Link reaction makes acetyl CoA.', 'Krebs: 2 turns per glucose.', 'All 6 carbons leave as CO₂.']},
    T3: {
        'overview': 'Most ATP is made in the final stage, where electrons flow down a chain of carriers and power a proton gradient. Without oxygen, fermentation keeps glycolysis going.',
        'key_terms': ['Electron transport chain', 'Proton gradient', 'Chemiosmosis', 'ATP synthase', 'Final electron acceptor', 'Oxidative phosphorylation', 'Lactic acid fermentation', 'Alcoholic fermentation', 'Oxygen debt'],
        'explanation': [
            'NADH and FADH₂ give electrons to carrier proteins in the inner mitochondrial membrane. As electrons pass along the chain, energy is used to pump H⁺ from the matrix into the intermembrane space. Oxygen accepts the electrons at the end, combining with H⁺ to form water.',
            'H⁺ flows back into the matrix through ATP synthase, which uses that flow to make ATP from ADP and Pᵢ (chemiosmosis). Each NADH gives about 2.5 ATP and each FADH₂ about 1.5. Per glucose: 10 × 2.5 + 2 × 1.5 + 4 = 32 ATP at most; real yields are about 30 to 32. That captures 32 × 30.5 ≈ 976 of 2870 kJ/mol, about 34% efficiency; the rest is released as heat.',
            'Without oxygen, the chain stops and NAD cannot be regenerated, so glycolysis would stop. Fermentation regenerates NAD: animal muscles reduce pyruvate to lactate; yeast and plants make ethanol and CO₂. Only the 2 ATP from glycolysis are produced. Lactate is later converted back in the liver, using extra oxygen (the "oxygen debt").'],
        'formulas_label': 'Key ideas',
        'formulas': ['NADH ≈ 2.5 ATP; FADH₂ ≈ 1.5 ATP', 'Max ≈ 32 ATP per glucose (aerobic)', 'Anaerobic: 2 ATP per glucose', '½O₂ + 2H⁺ + 2e⁻ → H₂O', 'Efficiency ≈ 34%'],
        'steps': ['Count NADH and FADH₂ from earlier stages.', 'Convert to ATP with 2.5 and 1.5.', 'Add substrate-level ATP.', 'Compare with anaerobic yield.'],
        'worked_example': {
            'problem': 'Use 10 NADH, 2 FADH₂ and 4 substrate-level ATP to estimate the ATP yield per glucose and the efficiency (glucose 2870 kJ/mol, ATP 30.5 kJ/mol).',
            'steps': ['10 × 2.5 = 25 and 2 × 1.5 = 3.', 'Total = 25 + 3 + 4 = 32 ATP.', 'Efficiency = 32 × 30.5/2870 × 100 ≈ 34%.'],
            'answer': 'About 32 ATP, roughly 34% efficient.',
            'check': 'Aerobic respiration gives about 16 times the 2 ATP from fermentation, which matches the textbook comparison ✓.'},
        'mistakes': ['Saying oxygen is needed for glycolysis.', 'Saying fermentation makes ATP from pyruvate.', 'Forgetting oxygen forms water.', 'Quoting 38 ATP as the actual yield (it is an old theoretical maximum).'],
        'real_world': 'Cyanide blocks the last carrier of the electron transport chain, so cells cannot use oxygen; it is lethal within minutes.',
        'exam_strategy': 'Explain chemiosmosis in order: electrons flow → H⁺ pumped → gradient → H⁺ flows through ATP synthase → ATP.',
        'recap': ['ETC pumps H⁺.', 'ATP synthase makes ATP.', 'O₂ is the final acceptor.', 'Fermentation regenerates NAD.']},
    T4: {
        'overview': 'Photosynthesis captures light energy and stores it as chemical energy in sugars. It happens in two linked stages in the chloroplast.',
        'key_terms': ['Chlorophyll', 'Photosystem', 'Photolysis', 'Light-dependent reactions', 'Thylakoid', 'NADPH', 'Calvin cycle', 'Stroma', 'RuBisCO', 'RuBP', 'Limiting factor', 'Rf value'],
        'explanation': [
            'In the light-dependent reactions on the thylakoid membranes, chlorophyll absorbs light (mainly red and blue) and excites electrons. Water is split (photolysis) to replace them, releasing O₂. The electrons pass along a transport chain that pumps H⁺, so ATP synthase makes ATP, and they finally reduce NADP to NADPH.',
            'In the Calvin cycle in the stroma, the enzyme RuBisCO fixes CO₂ onto ribulose bisphosphate (RuBP). The products are reduced using ATP and NADPH to triose phosphate, some of which builds glucose while the rest regenerates RuBP. Making one glucose needs 6 CO₂ fixed, 18 ATP and 12 NADPH.',
            'The rate of photosynthesis is limited by whichever factor is in shortest supply: light intensity, CO₂ concentration or temperature. Greenhouses raise CO₂ and temperature to boost yields. Pigments can be separated by chromatography: a pigment that moves 3.6 cm when the solvent moves 8.0 cm has Rf = 0.45.'],
        'formulas_label': 'Key ideas',
        'formulas': ['6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂', 'Light-dependent (thylakoid): photolysis, ATP, NADPH, O₂', 'Calvin cycle (stroma): CO₂ + RuBP → sugar using ATP, NADPH', 'Per glucose: 6 CO₂, 18 ATP, 12 NADPH', 'Rf = distance moved by pigment ÷ distance moved by solvent'],
        'steps': ['Identify the stage and location.', 'List inputs and outputs.', 'Link the stages (ATP and NADPH).', 'Identify the limiting factor on a graph.'],
        'worked_example': {
            'problem': 'A plant is moved from bright light into darkness. Predict what happens to the levels of RuBP and GP (glycerate 3-phosphate) in the Calvin cycle.',
            'steps': ['In darkness, the light-dependent reactions stop, so ATP and NADPH run out.', 'GP cannot be reduced to triose phosphate, so GP builds up.', 'RuBP cannot be regenerated but is still used to fix CO₂, so RuBP falls.'],
            'answer': 'GP rises and RuBP falls.',
            'check': 'CO₂ fixation by RuBisCO does not need light directly, so it continues briefly ✓.'},
        'mistakes': ['Saying the oxygen comes from CO₂ (it comes from water).', 'Calling the Calvin cycle "dark reactions" that only happen at night.', 'Placing the Calvin cycle in the thylakoids.', 'Saying plants do not respire.'],
        'real_world': 'RuBisCO is probably the most abundant protein on Earth, yet it is slow and sometimes fixes oxygen by mistake; scientists are trying to engineer better versions to raise crop yields.',
        'exam_strategy': 'For limiting-factor graphs, say which factor limits on the rising part (the one on the x-axis) and suggest what limits at the plateau.',
        'recap': ['Light reactions: thylakoids.', 'O₂ from water.', 'Calvin cycle: stroma, RuBisCO.', 'Limiting factors set the rate.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Enzymes speed up reactions by:', ['lowering the activation energy', 'supplying energy', 'raising the temperature', 'changing the products'], 0, 'Catalysts.'),
    Q(T1, 'An enzyme reaction has rate 4 units at 25 °C and Q₁₀ = 2. At 35 °C the rate is about:', ['8 units', '6 units', '16 units', '4 units'], 0, '4 × 2.', ans=8),
    Q(T1, 'A competitive inhibitor:', ['binds the active site and is overcome by more substrate', 'binds elsewhere and is not overcome', 'denatures the enzyme', 'is the product of the reaction'], 0, 'Competes with substrate.'),
    Q(T1, 'Above the optimum temperature, rate falls because:', ['the enzyme denatures and the active site changes shape', 'molecules move more slowly', 'more substrate binds', 'ATP runs out'], 0, 'Bonds holding shape break.'),
    Q(T1, 'Hydrolysis of ATP produces:', ['ADP and inorganic phosphate', 'AMP and glucose', 'ADP and water', 'NADH'], 0, 'Releases energy.'),
    Q(T1, 'End-product inhibition is usually:', ['non-competitive', 'competitive', 'irreversible denaturation', 'caused by heat'], 0, 'Product binds an allosteric site.'),
    # T2
    Q(T2, 'Glycolysis takes place in the:', ['cytoplasm', 'mitochondrial matrix', 'inner mitochondrial membrane', 'nucleus'], 0, 'No oxygen needed.'),
    Q(T2, 'The net ATP gain from glycolysis per glucose is:', ['2', '4', '36', '0'], 0, '4 made, 2 used.', ans=2),
    Q(T2, 'How many CO₂ molecules are released per glucose in aerobic respiration?', ['6', '2', '4', '3'], 0, '2 in the link reaction, 4 in Krebs.', ans=6),
    Q(T2, 'Per glucose, the Krebs cycle turns:', ['twice', 'once', 'three times', 'six times'], 0, 'One per pyruvate.'),
    Q(T2, 'The link reaction converts pyruvate to:', ['acetyl coenzyme A', 'lactate', 'glucose', 'oxaloacetate'], 0, 'Plus CO₂ and NADH.'),
    Q(T2, 'The total NADH produced per glucose (all stages before the chain) is:', ['10', '2', '6', '8'], 0, '2 + 2 + 6.', ans=10),
    # T3
    Q(T3, 'The final electron acceptor in aerobic respiration is:', ['oxygen', 'NAD', 'pyruvate', 'carbon dioxide'], 0, 'Forms water.'),
    Q(T3, 'ATP synthase makes ATP using energy from:', ['H⁺ flowing down its gradient', 'oxygen directly', 'glucose directly', 'light'], 0, 'Chemiosmosis.'),
    Q(T3, 'Using 2.5 ATP per NADH and 1.5 per FADH₂, 10 NADH + 2 FADH₂ + 4 ATP gives:', ['32 ATP', '38 ATP', '28 ATP', '36 ATP'], 0, '25 + 3 + 4.'),
    Q(T3, 'The main purpose of fermentation is to:', ['regenerate NAD so glycolysis can continue', 'make extra ATP from pyruvate', 'produce oxygen', 'make glucose'], 0, 'NAD recycling.'),
    Q(T3, 'Yeast fermentation produces:', ['ethanol and carbon dioxide', 'lactate only', 'oxygen and water', 'glucose'], 0, 'Alcoholic fermentation.'),
    Q(T3, 'Anaerobic respiration yields how many ATP per glucose?', ['2', '32', '4', '0'], 0, 'Glycolysis only.', ans=2),
    # T4
    Q(T4, 'The oxygen released in photosynthesis comes from:', ['water', 'carbon dioxide', 'glucose', 'RuBP'], 0, 'Photolysis.'),
    Q(T4, 'The Calvin cycle takes place in the:', ['stroma', 'thylakoid membranes', 'cytoplasm', 'mitochondria'], 0, 'Light-independent stage.'),
    Q(T4, 'The enzyme that fixes CO₂ in the Calvin cycle is:', ['RuBisCO', 'ATP synthase', 'amylase', 'DNA polymerase'], 0, 'Fixes CO₂ onto RuBP.'),
    Q(T4, 'A pigment moves 3.6 cm while the solvent moves 8.0 cm. Its Rf value is:', ['0.45', '2.22', '4.4', '0.36'], 0, '3.6 ÷ 8.0.', ans=0.45, num=True),
    Q(T4, 'The light-dependent reactions supply the Calvin cycle with:', ['ATP and NADPH', 'CO₂ and water', 'glucose and oxygen', 'RuBP'], 0, 'Energy and reducing power.'),
    Q(T4, 'Making one glucose in the Calvin cycle requires how many CO₂ molecules?', ['6', '1', '3', '12'], 0, 'Six carbons.', ans=6),
]

FLASH = [
    ['ATP', 'Energy currency: ATP → ADP + Pᵢ releases about 30.5 kJ/mol.'],
    ['Competitive inhibitor', 'Binds the active site; overcome by more substrate.'],
    ['Glycolysis', 'Glucose → 2 pyruvate; net 2 ATP, 2 NADH; cytoplasm.'],
    ['Krebs cycle', 'Matrix; per turn 2 CO₂, 3 NADH, 1 FADH₂, 1 ATP.'],
    ['Chemiosmosis', 'H⁺ flows through ATP synthase to make ATP.'],
    ['Fermentation', 'Regenerates NAD without oxygen; 2 ATP per glucose.'],
    ['Photolysis', 'Light splits water, releasing O₂, H⁺ and electrons.'],
    ['Calvin cycle', 'Stroma; RuBisCO fixes CO₂ using ATP and NADPH.'],
]
