"""Organic Chemistry, module 3: Elimination, alkenes, alkynes and alcohols."""
from verify import Q
from oc_common import mass, dou, r
T1, T2, T3, T4 = ('Elimination: E1 and E2', 'Alkenes and electrophilic addition', 'Alkynes and conjugated dienes', 'Alcohols and ethers')
n_rx = 13.7 / mass('C4H9Br')
assert r(n_rx, 3) == 0.100 and r(3.9 / (n_rx * mass('C4H8')) * 100, 0) == 70
assert r(-115.5 - (-119.7), 1) == 4.2 and r(mass('C6H10'), 2) == 82.14 and r(8.2 / mass('C6H10'), 3) == 0.100 and r(8.2 / mass('C6H10') * 24.5, 2) == 2.45
assert dou('C6H10') == 2 and dou('C4H6') == 2 and 38 - 25 == 13
assert r(4.6 / mass('C2H6O') * mass('C2H4O2'), 1) == 6.0 and r(mass('C2H6O'), 2) == 46.07

MODULE = {
    'title': 'Elimination, alkenes, alkynes and alcohols',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module covers how C=C and C≡C bonds are made and how they react. Elimination reactions (E1 and E2) create alkenes; alkenes and alkynes then add electrophiles across their π bonds; conjugated dienes add in special ways, including the Diels–Alder reaction; and alcohols link it all together through oxidation, dehydration and ether formation.',
    'key_terms': ['Elimination', 'E2', 'E1', 'Zaitsev\'s rule', 'Anti-periplanar', 'Electrophilic addition', 'Markovnikov\'s rule', 'Bromonium ion', 'Hydroboration', 'Alkyne', 'Acetylide', 'Conjugated diene', 'Diels–Alder', 'Oxidation of alcohols', 'Williamson ether synthesis'],
    'explanation': [
        'Elimination removes H and a leaving group from neighbouring carbons to form C=C. E2 happens in one step with a strong base and needs the H and leaving group anti-periplanar; E1 goes through a carbocation. Both usually favour the more substituted (Zaitsev) alkene, unless a bulky base gives the less substituted (Hofmann) product.',
        'Alkenes are nucleophiles: their π electrons attack electrophiles such as H⁺ and Br₂. HBr adds so that H goes to the carbon that already has more hydrogens (Markovnikov), because that forms the more stable carbocation. Alkynes do the same twice, and can be reduced selectively to cis or trans alkenes; conjugated dienes add 1,2 or 1,4 and undergo cycloadditions.',
        'Alcohols are classified as primary, secondary or tertiary. Primary alcohols oxidise to aldehydes and then carboxylic acids, secondary alcohols to ketones, and tertiary alcohols resist oxidation. Acid dehydrates alcohols to alkenes, and alkoxides plus haloalkanes give ethers.'],
    'quick_facts': [
        'E2: one step, anti-periplanar, rate = k[RX][base].',
        'Zaitsev: more substituted alkene is major.',
        'Markovnikov: H adds to the C with more H.',
        'Lindlar → cis alkene; Na/NH₃ → trans alkene.',
        '1° alcohol → aldehyde → acid; 2° → ketone; 3° no oxidation.'],
}

NOTES = {
    T1: {
        'overview': 'Elimination competes with substitution. Strong bases, heat and hindered substrates push the balance towards forming alkenes.',
        'key_terms': ['β-hydrogen', 'E2', 'E1', 'Anti-periplanar', 'Zaitsev product', 'Hofmann product', 'Bulky base', 'Dehydrohalogenation'],
        'explanation': [
            'E2: a strong base removes a β-hydrogen while the leaving group departs, in one concerted step; rate = k[RX][base]. The H and leaving group must be anti-periplanar (180° apart), which in cyclohexanes means both must be axial.',
            'Zaitsev\'s rule: the more substituted, more stable alkene is the major product. 2-bromobutane with ethoxide gives mainly but-2-ene (trans more than cis) and some but-1-ene. A bulky base such as tert-butoxide removes the most accessible hydrogen and gives more of the less substituted (Hofmann) alkene.',
            'E1 shares the carbocation step of SN1 and competes with it, especially for tertiary substrates on heating. Yields are calculated as usual: 13.7 g of 2-bromobutane (0.100 mol) giving 3.9 g of butenes (M = 56.1 g/mol) is a 70% yield.'],
        'formulas_label': 'Rules',
        'formulas': ['E2 rate = k[RX][B⁻]', 'E1 rate = k[RX]', 'Strong base + heat → elimination', 'Bulky base → Hofmann; small base → Zaitsev'],
        'steps': ['Find the β-hydrogens.', 'Choose E2 or E1 from base strength and substrate.', 'Draw the possible alkenes.', 'Pick the major product (Zaitsev or Hofmann).'],
        'worked_example': {
            'problem': 'What is the major product when 2-bromo-2-methylbutane is heated with sodium ethoxide?',
            'steps': ['Tertiary substrate, strong base, heat: E2 elimination.', 'Possible alkenes: 2-methylbut-2-ene (trisubstituted) and 2-methylbut-1-ene (disubstituted).', 'Zaitsev: the more substituted alkene is favoured.'],
            'answer': '2-methylbut-2-ene.',
            'check': 'With bulky tert-butoxide, 2-methylbut-1-ene would become the major product ✓.'},
        'mistakes': ['Removing a hydrogen from the carbon bearing the leaving group (it must be β).', 'Ignoring the anti-periplanar requirement in rings.', 'Forgetting that substitution competes.', 'Choosing the Hofmann product with a small base.'],
        'real_world': 'Industrial plastics such as PVC are made from monomers produced by elimination reactions (vinyl chloride from 1,2-dichloroethane).',
        'exam_strategy': 'Ask "strong base? heat? bulky?" first; those three cues usually decide between SN2, E2, SN1 and E1.',
        'recap': ['β-hydrogens.', 'E2 anti-periplanar.', 'Zaitsev usually.', 'Bulky base → Hofmann.']},
    T2: {
        'overview': 'The π bond of an alkene is a source of electrons, so alkenes react with electrophiles by addition.',
        'key_terms': ['Electrophilic addition', 'Markovnikov\'s rule', 'Carbocation intermediate', 'Bromonium ion', 'Anti addition', 'Hydration', 'Hydroboration–oxidation', 'Hydrogenation', 'Ozonolysis'],
        'explanation': [
            'HBr adds in two steps: H⁺ adds to give the more stable carbocation, then Br⁻ attacks it. So propene gives mainly 2-bromopropane (Markovnikov). Acid-catalysed hydration (H₂O, H⁺) likewise puts –OH on the more substituted carbon. Hydroboration–oxidation (BH₃ then H₂O₂/OH⁻) gives the anti-Markovnikov alcohol with syn addition.',
            'Br₂ adds through a cyclic bromonium ion that bromide opens from the back, so the two Br atoms add anti. The orange colour of bromine water disappears: the classic test for C=C. Ozonolysis (O₃ then Zn or Me₂S) cuts the double bond into two carbonyl compounds.',
            'Catalytic hydrogenation (H₂ over Pt, Pd or Ni) adds 1 mol of H₂ per C=C: 8.2 g of cyclohexene (0.100 mol) takes up about 2.45 L of H₂ at 25 °C and 1 atm. Heats of hydrogenation compare alkene stabilities: trans-but-2-ene releases 4.2 kJ/mol less than cis, so trans is more stable.'],
        'formulas_label': 'Rules',
        'formulas': ['HX, H₂O/H⁺: Markovnikov', 'BH₃ then H₂O₂/OH⁻: anti-Markovnikov, syn', 'Br₂: anti addition', 'H₂/Pt: syn addition, 1 mol per C=C'],
        'steps': ['Identify the electrophile.', 'Form the more stable carbocation (or bridged ion).', 'Add the nucleophile.', 'Check regiochemistry and stereochemistry.'],
        'worked_example': {
            'problem': 'Predict the products of propene with (a) HBr and (b) BH₃ followed by H₂O₂/NaOH.',
            'steps': ['(a) H⁺ adds to C1, giving the secondary carbocation at C2; Br⁻ adds there.', '(b) Boron adds to the less hindered C1; oxidation replaces B with OH.', 'Products: (a) 2-bromopropane; (b) propan-1-ol.'],
            'answer': '2-bromopropane and propan-1-ol.',
            'check': '(a) is Markovnikov and (b) anti-Markovnikov, as expected ✓.'},
        'mistakes': ['Putting H on the more substituted carbon.', 'Forgetting that bromination is anti.', 'Mixing up hydration and hydroboration regiochemistry.', 'Forgetting carbocation rearrangements.'],
        'real_world': 'Margarine was historically made by partially hydrogenating vegetable oils, which also produced unhealthy trans fats as a side product.',
        'exam_strategy': 'Draw the carbocation explicitly; the regiochemistry follows from its stability.',
        'recap': ['π bond is nucleophilic.', 'Markovnikov.', 'Anti bromination.', 'Hydrogenation 1 mol H₂ per C=C.']},
    T3: {
        'overview': 'Alkynes have two π bonds and an acidic terminal hydrogen. Conjugated dienes have special reactions, including the Diels–Alder cycloaddition.',
        'key_terms': ['Terminal alkyne', 'Acetylide ion', 'Lindlar catalyst', 'Dissolving-metal reduction', 'Keto–enol tautomerism', 'Conjugated diene', '1,2- and 1,4-addition', 'Diels–Alder reaction'],
        'explanation': [
            'A terminal alkyne C–H (pKa about 25) is much more acidic than an alkene or alkane, because the sp carbon holds the negative charge close to its nucleus. NaNH₂ (conjugate acid NH₃, pKa about 38) deprotonates it essentially completely (K ≈ 10¹³), and the acetylide ion can then attack a primary haloalkane in an SN2 reaction, forming a new C–C bond.',
            'Reduction: H₂ with Pt gives the alkane; H₂ with Lindlar\'s catalyst gives the cis alkene; Na in liquid NH₃ gives the trans alkene. Hydration of an alkyne (H₂O, H₂SO₄, HgSO₄) gives an enol that tautomerises to a ketone. Hex-1-yne, C₆H₁₀, has 2 degrees of unsaturation, both in the triple bond.',
            'Conjugated dienes such as buta-1,3-diene (C₄H₆) are extra-stable because their π electrons are delocalised. HBr adds 1,2 (faster, the kinetic product) or 1,4 (more stable, the thermodynamic product). In the Diels–Alder reaction, a diene and an alkene (dienophile) combine in one step to form a cyclohexene ring.'],
        'formulas_label': 'Rules',
        'formulas': ['Alkyne C–H pKa ≈ 25', 'H₂/Lindlar → cis alkene', 'Na/NH₃(l) → trans alkene', 'Diene + dienophile → cyclohexene'],
        'steps': ['Decide whether the alkyne is terminal.', 'Choose reagent for the desired product.', 'For dienes, decide kinetic or thermodynamic control.', 'For Diels–Alder, draw the new ring and two new σ bonds.'],
        'worked_example': {
            'problem': 'Make cis-hex-3-ene starting from but-1-yne.',
            'steps': ['Deprotonate but-1-yne with NaNH₂ to give the acetylide.', 'React with bromoethane (SN2) to form hex-3-yne.', 'Reduce with H₂ and Lindlar\'s catalyst to the cis alkene.'],
            'answer': 'NaNH₂; CH₃CH₂Br; H₂/Lindlar.',
            'check': '4 + 2 = 6 carbons ✓; Lindlar gives cis ✓.'},
        'mistakes': ['Using a tertiary haloalkane with an acetylide (it eliminates).', 'Mixing up Lindlar (cis) and Na/NH₃ (trans).', 'Forgetting enol–keto tautomerism.', 'Drawing the Diels–Alder product with the wrong ring size.'],
        'real_world': 'Ethyne (acetylene) burns at over 3000 °C in oxygen, hot enough for welding and cutting steel.',
        'exam_strategy': 'For synthesis questions, count carbons first: acetylide alkylation is the standard way to add them.',
        'recap': ['Acidic terminal alkynes.', 'Lindlar cis, Na/NH₃ trans.', 'Kinetic vs thermodynamic.', 'Diels–Alder makes rings.']},
    T4: {
        'overview': 'Alcohols are central to synthesis. Their –OH group can be oxidised, eliminated, substituted or turned into ethers.',
        'key_terms': ['Primary, secondary, tertiary alcohol', 'Hydrogen bonding', 'Oxidation', 'Dichromate', 'PCC', 'Dehydration', 'Williamson ether synthesis', 'Lucas test'],
        'explanation': [
            'Hydrogen bonding gives alcohols high boiling points: ethanol (C₂H₆O) boils at 78 °C, while its isomer dimethyl ether boils at −24 °C. Small alcohols mix with water; solubility falls as the carbon chain grows.',
            'Oxidation with acidified dichromate (orange to green): primary alcohols give aldehydes and then carboxylic acids; secondary give ketones; tertiary do not react. PCC stops primary alcohols at the aldehyde. Complete oxidation of 4.6 g of ethanol (0.0998 mol) gives at most about 6.0 g of ethanoic acid.',
            'Heating with concentrated H₂SO₄ dehydrates alcohols to alkenes (E1 for 2° and 3°). Ethers are made by the Williamson synthesis: an alkoxide (RO⁻) attacks a primary haloalkane by SN2. Ethers are unreactive and make good solvents.'],
        'formulas_label': 'Rules',
        'formulas': ['1° → RCHO → RCOOH', '2° → R₂C=O', '3° → no oxidation', 'RO⁻ + R′CH₂X → ROCH₂R′ + X⁻'],
        'steps': ['Classify the alcohol.', 'Choose the reagent for the target.', 'Predict the product.', 'Check colour changes or tests.'],
        'worked_example': {
            'problem': '4.6 g of ethanol is fully oxidised to ethanoic acid. What is the maximum mass of acid?',
            'steps': ['n(ethanol) = 4.6/46.07 = 0.0998 mol.', '1 : 1 ratio, so n(acid) = 0.0998 mol.', 'm = 0.0998 × 60.05 ≈ 6.0 g.'],
            'answer': 'About 6.0 g.',
            'check': 'Acid is heavier per mole (60 vs 46 g/mol), so mass increases ✓.'},
        'mistakes': ['Saying tertiary alcohols oxidise.', 'Forgetting aldehydes oxidise further unless distilled off or PCC is used.', 'Using a tertiary haloalkane in a Williamson synthesis.', 'Confusing dehydration (elimination) with dehydrogenation.'],
        'real_world': 'Old roadside breathalysers used the orange-to-green colour change of dichromate oxidising ethanol in breath.',
        'exam_strategy': 'Draw a ladder: 1° alcohol → aldehyde → acid, 2° → ketone; most oxidation questions map onto it.',
        'recap': ['Hydrogen bonding.', 'Oxidation ladder.', 'Dehydration to alkenes.', 'Williamson ethers.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'In an E2 reaction the H and leaving group must be:', ['anti-periplanar', 'syn and eclipsed', 'on the same carbon', 'gauche'], 0, '180° apart.'),
    Q(T1, '2-bromo-2-methylbutane with hot sodium ethoxide gives mainly:', ['2-methylbut-2-ene', '2-methylbut-1-ene', '2-methylbutan-2-ol', '2-ethoxy-2-methylbutane'], 0, 'Zaitsev.'),
    Q(T1, 'With bulky potassium tert-butoxide the major alkene is usually:', ['the less substituted (Hofmann) alkene', 'the Zaitsev alkene', 'an alkyne', 'no alkene'], 0, 'Most accessible H.'),
    Q(T1, 'The rate law for E2 is:', ['rate = k[RX][base]', 'rate = k[RX]', 'rate = k[base]', 'rate = k'], 0, 'Bimolecular.'),
    Q(T1, '13.7 g of 2-bromobutane (0.100 mol) gives 3.9 g of butenes. The percentage yield is about:', ['70%', '28%', '56%', '39%'], 0, '3.9/5.61.'),
    Q(T1, 'Elimination is favoured over substitution by:', ['strong base and heat', 'weak nucleophiles and low temperature', 'primary substrates with iodide', 'water at room temperature'], 0, 'Heat favours E.'),
    # T2
    Q(T2, 'Propene + HBr gives mainly:', ['2-bromopropane', '1-bromopropane', '1,2-dibromopropane', 'propane'], 0, 'Markovnikov.'),
    Q(T2, 'Hydroboration–oxidation of propene gives:', ['propan-1-ol', 'propan-2-ol', 'propanal', 'propanone'], 0, 'Anti-Markovnikov.'),
    Q(T2, 'Bromine adds to cyclohexene with:', ['anti stereochemistry', 'syn stereochemistry', 'no stereochemistry', 'retention'], 0, 'Bromonium ion.'),
    Q(T2, 'Hydrogenating 8.2 g of cyclohexene (0.100 mol) uses about how much H₂ at 25 °C, 1 atm?', ['2.45 L', '4.9 L', '24.5 L', '0.245 L'], 0, '0.100 × 24.5 L.'),
    Q(T2, 'Trans-but-2-ene releases 4.2 kJ/mol less on hydrogenation than cis. This shows trans is:', ['more stable', 'less stable', 'equally stable', 'aromatic'], 0, 'Lower energy start.'),
    Q(T2, 'Bromine water turning colourless indicates:', ['a C=C double bond', 'an alcohol', 'an alkane', 'a carboxylic acid'], 0, 'Addition test.'),
    # T3
    Q(T3, 'Hex-3-yne with H₂ and Lindlar\'s catalyst gives:', ['cis-hex-3-ene', 'trans-hex-3-ene', 'hexane', 'hexan-3-one'], 0, 'Syn addition, stops at alkene.'),
    Q(T3, 'Hex-3-yne with Na in liquid NH₃ gives:', ['trans-hex-3-ene', 'cis-hex-3-ene', 'hexane', 'hex-1-yne'], 0, 'Dissolving metal.'),
    Q(T3, 'Terminal alkynes are deprotonated by NaNH₂ because:', ['the alkyne (pKa ≈ 25) is more acidic than NH₃ (pKa ≈ 38)', 'NH₃ is a strong acid', 'alkynes are aromatic', 'sodium is a catalyst'], 0, 'K ≈ 10¹³.'),
    Q(T3, 'The degree of unsaturation of hex-1-yne, C₆H₁₀, is:', ['2', '1', '3', '4'], 0, 'Triple bond = 2 π.', ans=2, num=True),
    Q(T3, 'The Diels–Alder reaction forms:', ['a six-membered ring', 'a four-membered ring', 'an alkyne', 'an aromatic ring directly'], 0, 'Diene + dienophile.'),
    Q(T3, 'The 1,4-addition product of HBr to buta-1,3-diene is favoured at:', ['higher temperature (thermodynamic control)', 'low temperature', 'any temperature equally', 'only with catalysts'], 0, 'More stable alkene.'),
    # T4
    Q(T4, 'Ethanol boils at 78 °C but dimethyl ether at −24 °C because ethanol:', ['forms hydrogen bonds', 'is heavier', 'is ionic', 'is aromatic'], 0, 'Same formula C₂H₆O.'),
    Q(T4, 'Oxidising propan-2-ol gives:', ['propanone', 'propanal', 'propanoic acid', 'no reaction'], 0, 'Secondary → ketone.'),
    Q(T4, 'Which alcohol does not react with acidified dichromate?', ['2-methylpropan-2-ol', 'ethanol', 'propan-2-ol', 'methanol'], 0, 'Tertiary.'),
    Q(T4, 'PCC oxidises a primary alcohol to:', ['an aldehyde', 'a carboxylic acid', 'a ketone', 'an alkene'], 0, 'Stops early.'),
    Q(T4, '4.6 g of ethanol fully oxidised gives at most about:', ['6.0 g of ethanoic acid', '4.6 g', '3.5 g', '9.2 g'], 0, '0.0998 × 60.05.'),
    Q(T4, 'In a Williamson ether synthesis the haloalkane should be:', ['primary', 'tertiary', 'aromatic', 'any type'], 0, 'SN2 step.'),
]

FLASH = [
    ['E2', 'One step, strong base, anti-periplanar H and leaving group.'],
    ['Zaitsev\'s rule', 'More substituted alkene is the major product.'],
    ['Markovnikov\'s rule', 'H adds to the carbon with more H; via the more stable carbocation.'],
    ['Hydroboration–oxidation', 'Anti-Markovnikov, syn addition of H and OH.'],
    ['Bromination of alkenes', 'Anti addition via a bromonium ion; decolourises bromine water.'],
    ['Alkyne reductions', 'Lindlar → cis; Na/NH₃ → trans; Pt/H₂ → alkane.'],
    ['Diels–Alder', 'Diene + dienophile → cyclohexene, one step.'],
    ['Alcohol oxidation', '1° → aldehyde → acid; 2° → ketone; 3° none.'],
]
