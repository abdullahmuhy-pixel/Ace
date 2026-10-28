"""Organic Chemistry, module 2: Alkanes, mechanisms and substitution."""
import math
from verify import Q
from oc_common import mass, r
T1, T2, T3, T4 = ('Alkanes, conformations and rings', 'Radical halogenation', 'Mechanisms, curly arrows and energy profiles', 'Nucleophilic substitution: SN1 and SN2')
R = 8.314
K = math.exp(7300 / (R * 298))
assert r(K, 0) == 19 and r(K / (1 + K) * 100, 0) == 95
assert r(2 * -393.5 + 3 * -285.8 - (-84.0), 0) == -1560 and r(mass('C3H8'), 2) == 44.09
p, s = 6 * 1, 2 * 3.8
assert r(p / (p + s) * 100, 0) == 44 and r(s / (p + s) * 100, 0) == 56 and r(2 * 82 / (6 + 2 * 82) * 100, 1) == 96.5
assert r(R * math.log(2) / (1 / 298 - 1 / 308) / 1000, 0) == 53 and r(-R * 298 * math.log(100) / 1000, 1) == -11.4
assert r(2e-3 * 0.1 * 0.2 * 1e5, 6) == 4 and r(math.log(2) / 1e-4, 0) == 6931 and r(math.log(2) / 1e-4 / 3600, 2) == 1.93
assert 2 * 2 == 4  # SN2: doubling both reactants quadruples the rate

MODULE = {
    'title': 'Alkanes, mechanisms and substitution',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module introduces how organic reactions happen. It starts with alkanes and the 3D shapes they adopt, then radical halogenation as a first mechanism, the language of curly arrows and energy profiles, and finally nucleophilic substitution, the SN1 and SN2 pathways that appear throughout organic chemistry.',
    'key_terms': ['Conformation', 'Newman projection', 'Staggered', 'Eclipsed', 'Chair conformation', 'Axial', 'Equatorial', 'Radical', 'Chain reaction', 'Nucleophile', 'Electrophile', 'Carbocation', 'Activation energy', 'SN2', 'SN1'],
    'explanation': [
        'Alkanes are saturated hydrocarbons, CₙH₂ₙ₊₂, that burn well but otherwise react sluggishly. Rotation about C–C bonds gives conformations: staggered forms are lower in energy than eclipsed ones, and cyclohexane adopts a strain-free chair in which bulky groups prefer equatorial positions.',
        'Reactions are described by mechanisms. A curly arrow shows a pair of electrons moving from a nucleophile (electron-rich) to an electrophile (electron-poor); half-headed arrows show single electrons in radical reactions. Energy profiles show the activation energy that sets the rate.',
        'Haloalkanes undergo nucleophilic substitution. SN2 is one concerted step: the nucleophile attacks from the back, the rate depends on both reactants and the carbon\'s configuration inverts. SN1 goes through a planar carbocation: the rate depends only on the substrate and the product is largely racemic. Tertiary substrates favour SN1; methyl and primary favour SN2.'],
    'quick_facts': [
        'Staggered < eclipsed in energy; anti < gauche for butane.',
        'Chair cyclohexane: large groups equatorial.',
        'Radical chain: initiation, propagation, termination.',
        'ΔG = −RT ln K; higher Ea = slower.',
        'SN2 rate = k[RX][Nu], inversion; SN1 rate = k[RX], racemisation.'],
}

NOTES = {
    T1: {
        'overview': 'Alkanes have only single bonds, so their chemistry is mostly about shape (conformations) and combustion.',
        'key_terms': ['Saturated', 'Conformation', 'Newman projection', 'Torsional strain', 'Gauche', 'Anti', 'Ring strain', 'Chair', 'Axial', 'Equatorial', 'Ring flip'],
        'explanation': [
            'Looking down a C–C bond (a Newman projection), ethane\'s staggered conformation is about 12 kJ/mol lower than its eclipsed one because eclipsed bonds repel (torsional strain). In butane the anti form, with the two CH₃ groups 180° apart, is lowest; the gauche form (60°) is about 3.8 kJ/mol higher.',
            'Cyclohexane avoids ring strain by puckering into a chair with all angles near 109.5°. Each carbon has one axial (up or down) and one equatorial (around the ring) position, and a ring flip swaps them. A methyl group prefers equatorial by about 7.3 kJ/mol, so at 25 °C K = e^(7300/RT) ≈ 19: about 95% of molecules have it equatorial.',
            'Alkanes burn completely to CO₂ and water. For ethane, from enthalpies of formation, ΔcH = 2(−393.5) + 3(−285.8) − (−84.0) ≈ −1560 kJ/mol. Small rings such as cyclopropane are strained (60° angles) and more reactive.'],
        'formulas_label': 'Formulas',
        'formulas': ['Alkanes CₙH₂ₙ₊₂', 'Conformer ratio K = e^(ΔE/RT)', 'ΔcH = ΣΔfH(products) − ΣΔfH(reactants)'],
        'steps': ['Draw the Newman projection or chair.', 'Identify eclipsing, gauche and axial interactions.', 'Choose the lowest-energy arrangement.', 'Use K = e^(ΔE/RT) for populations.'],
        'worked_example': {
            'problem': 'Equatorial methylcyclohexane is 7.3 kJ/mol more stable than axial. What fraction is equatorial at 298 K?',
            'steps': ['K = e^(7300/(8.314 × 298)) ≈ e^2.95 ≈ 19.', 'Fraction equatorial = K/(1 + K) = 19/20.', '≈ 0.95.'],
            'answer': 'About 95% equatorial.',
            'check': 'A larger group (tert-butyl) would push this close to 100% ✓.'},
        'mistakes': ['Drawing cyclohexane flat.', 'Thinking conformers are different compounds.', 'Confusing axial and equatorial after a ring flip.', 'Forgetting to convert kJ to J in RT.'],
        'real_world': 'The chair shape of glucose, with almost every –OH equatorial, helps explain why it is the most common sugar in nature.',
        'exam_strategy': 'Draw chairs with three sets of parallel lines; neat chairs make axial and equatorial obvious.',
        'recap': ['Staggered is lower.', 'Anti beats gauche.', 'Chair with equatorial groups.', 'Combustion releases energy.']},
    T2: {
        'overview': 'Alkanes react with chlorine or bromine in UV light by a radical chain mechanism, the first full mechanism most students meet.',
        'key_terms': ['Homolytic fission', 'Radical', 'Initiation', 'Propagation', 'Termination', 'Selectivity', 'Primary, secondary, tertiary hydrogen'],
        'explanation': [
            'Initiation: UV light splits Cl₂ homolytically into two Cl• radicals. Propagation: Cl• + CH₄ → HCl + •CH₃, then •CH₃ + Cl₂ → CH₃Cl + Cl•, regenerating the radical so one photon can produce thousands of product molecules. Termination: two radicals combine (Cl• + •CH₃ → CH₃Cl, 2•CH₃ → C₂H₆).',
            'Radical stability follows 3° > 2° > 1° > methyl, so secondary and tertiary hydrogens are removed faster. In chlorination at 25 °C a 2° H reacts about 3.8 times faster than a 1° H. Propane has 6 primary and 2 secondary H, so the products are in the ratio 6 × 1 : 2 × 3.8, about 44% 1-chloropropane and 56% 2-chloropropane.',
            'Bromination is far more selective (2° : 1° about 82 : 1), giving about 96.5% 2-bromopropane, because the hydrogen-abstraction step by Br• is endothermic and its transition state resembles the radical (Hammond\'s postulate).'],
        'formulas_label': 'Formulas',
        'formulas': ['Product share ∝ (number of H) × (relative reactivity)', 'Cl: 1° : 2° : 3° ≈ 1 : 3.8 : 5', 'Br: 1° : 2° ≈ 1 : 82'],
        'steps': ['Write initiation, two propagation steps and termination.', 'Classify each type of hydrogen.', 'Multiply count by reactivity.', 'Convert to percentages.'],
        'worked_example': {
            'problem': 'Predict the product ratio for monochlorination of propane at 25 °C (2° H is 3.8 times as reactive as 1° H).',
            'steps': ['1° H: 6 × 1 = 6; 2° H: 2 × 3.8 = 7.6.', 'Total 13.6.', '1-chloro: 6/13.6 ≈ 44%; 2-chloro: 7.6/13.6 ≈ 56%.'],
            'answer': 'About 44% 1-chloropropane and 56% 2-chloropropane.',
            'check': 'Percentages add to 100 ✓; the more stable radical gives the major product despite fewer H ✓.'},
        'mistakes': ['Using full-headed arrows for radicals.', 'Forgetting that propagation regenerates the radical.', 'Ignoring the number of each type of H.', 'Thinking chlorination is highly selective.'],
        'real_world': 'Radical chain reactions of chlorine from CFCs destroy ozone in the stratosphere; one Cl atom can destroy thousands of O₃ molecules.',
        'exam_strategy': 'Check that propagation steps add up to the overall equation; radicals should cancel.',
        'recap': ['Three stages.', 'Radical stability 3° > 2° > 1°.', 'Count × reactivity.', 'Bromine is selective.']},
    T3: {
        'overview': 'Mechanisms explain reactions step by step. Curly arrows track electrons, and energy profiles explain rates and equilibria.',
        'key_terms': ['Nucleophile', 'Electrophile', 'Curly arrow', 'Heterolytic fission', 'Intermediate', 'Transition state', 'Activation energy', 'Carbocation stability', 'Hyperconjugation'],
        'explanation': [
            'A nucleophile (OH⁻, CN⁻, NH₃, H₂O) has a lone pair or π bond to donate; an electrophile (H⁺, a δ+ carbon, a carbocation) accepts it. A curly arrow starts at the electrons (a lone pair or bond) and ends where they go; heterolytic fission sends both bonding electrons to one atom.',
            'Energy profiles show reactants, transition states (energy maxima) and intermediates (minima). The activation energy controls rate: if the rate doubles between 298 K and 308 K, the Arrhenius equation gives Ea = R ln 2/(1/298 − 1/308) ≈ 53 kJ/mol. The free-energy change controls the position of equilibrium: K = 100 at 298 K means ΔG = −RT ln K ≈ −11.4 kJ/mol.',
            'Carbocations are stabilised by alkyl groups (inductive donation and hyperconjugation): 3° > 2° > 1° > methyl. This order explains SN1 reactivity, Markovnikov addition and rearrangements later in the course.'],
        'formulas_label': 'Formulas',
        'formulas': ['ΔG = −RT ln K', 'ln(k₂/k₁) = (Ea/R)(1/T₁ − 1/T₂)', 'Carbocation stability: 3° > 2° > 1° > CH₃⁺'],
        'steps': ['Identify the nucleophile and electrophile.', 'Draw arrows from electrons to the electron-poor atom.', 'Check charges and octets after each step.', 'Sketch the energy profile.'],
        'worked_example': {
            'problem': 'A reaction\'s rate doubles from 298 K to 308 K. Estimate its activation energy.',
            'steps': ['ln 2 = (Ea/8.314)(1/298 − 1/308).', '1/298 − 1/308 = 1.090 × 10⁻⁴ K⁻¹.', 'Ea = 8.314 × 0.693/1.090 × 10⁻⁴ ≈ 5.3 × 10⁴ J/mol.'],
            'answer': 'About 53 kJ/mol.',
            'check': 'Typical of many organic reactions, matching the "doubles every 10 °C" rule of thumb ✓.'},
        'mistakes': ['Drawing arrows from the electrophile to the nucleophile.', 'Confusing transition states with intermediates.', 'Thinking a negative ΔG means a fast reaction.', 'Leaving carbon with five bonds after an arrow.'],
        'real_world': 'Enzymes speed up reactions in your body by lowering activation energies, not by changing ΔG.',
        'exam_strategy': 'Every arrow must start from a lone pair, bond or negative charge; examiners deduct marks for arrows starting from atoms or positive charges.',
        'recap': ['Nucleophile → electrophile.', 'Ea sets rate.', 'ΔG sets equilibrium.', '3° carbocations are most stable.']},
    T4: {
        'overview': 'Nucleophilic substitution swaps a leaving group for a nucleophile. Two mechanisms, SN2 and SN1, differ in rate law, stereochemistry and preferred substrates.',
        'key_terms': ['Leaving group', 'SN2', 'Backside attack', 'Walden inversion', 'SN1', 'Rate-determining step', 'Racemisation', 'Steric hindrance', 'Polar aprotic solvent'],
        'explanation': [
            'SN2: the nucleophile attacks the carbon from the side opposite the leaving group in one step, inverting the configuration (R becomes S if priorities are unchanged). Rate = k[RX][Nu]: with k = 2.0 × 10⁻³ L mol⁻¹ s⁻¹, [RX] = 0.10 and [Nu] = 0.20 mol/L, the rate is 4.0 × 10⁻⁵ mol L⁻¹ s⁻¹; doubling both concentrations quadruples it. Bulky groups block backside attack, so methyl > 1° > 2°, and 3° essentially never react by SN2.',
            'SN1: the leaving group departs first, forming a planar carbocation (the slow step), which the nucleophile attacks from either face, giving a nearly racemic product. Rate = k[RX], independent of the nucleophile; as a first-order process, with k = 1.0 × 10⁻⁴ s⁻¹ the half-life is ln 2/k ≈ 6930 s, about 1.9 hours. Tertiary substrates and polar protic solvents favour SN1.',
            'Good leaving groups are weak bases: I⁻ > Br⁻ > Cl⁻ ≫ F⁻, and –OH must be protonated (to leave as water) before alcohols substitute. Strong, unhindered nucleophiles and polar aprotic solvents (acetone, DMSO) favour SN2.'],
        'formulas_label': 'Formulas',
        'formulas': ['SN2: rate = k[RX][Nu]', 'SN1: rate = k[RX]', 'First-order t½ = ln 2/k', 'Leaving groups: I⁻ > Br⁻ > Cl⁻ > F⁻'],
        'steps': ['Classify the substrate (methyl, 1°, 2°, 3°).', 'Judge the nucleophile and solvent.', 'Choose SN1 or SN2.', 'Predict the stereochemistry and rate law.'],
        'worked_example': {
            'problem': '(R)-2-bromobutane reacts with NaOH in acetone. Name the product and its configuration.',
            'steps': ['Secondary substrate, strong unhindered nucleophile, polar aprotic solvent: SN2.', 'Backside attack inverts the stereocentre.', 'OH replaces Br; priorities keep the same order (OH ranks first just as Br did).'],
            'answer': '(S)-butan-2-ol.',
            'check': 'Rate doubles if [OH⁻] doubles, as SN2 requires ✓.'},
        'mistakes': ['Predicting SN2 at a tertiary carbon.', 'Saying SN1 gives inversion.', 'Including the nucleophile in the SN1 rate law.', 'Treating OH⁻ as a good leaving group.'],
        'real_world': 'Many drugs, such as some anticancer alkylating agents, work by SN2 reactions with DNA bases.',
        'exam_strategy': 'Make a quick table: substrate, nucleophile, solvent, leaving group; three of the four usually point the same way.',
        'recap': ['SN2: one step, inversion.', 'SN1: carbocation, racemic.', '3° → SN1; 1° → SN2.', 'Weak bases leave well.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The lowest-energy conformation of butane is:', ['anti', 'gauche', 'eclipsed', 'fully eclipsed'], 0, 'CH₃ groups 180° apart.'),
    Q(T1, 'In chair methylcyclohexane the methyl group prefers to be:', ['equatorial', 'axial', 'planar', 'eclipsed'], 0, 'Avoids 1,3-diaxial strain.'),
    Q(T1, 'With a 7.3 kJ/mol preference at 298 K, the equatorial conformer is about:', ['95%', '50%', '75%', '99.9%'], 0, 'K ≈ 19.'),
    Q(T1, 'Staggered ethane is lower in energy than eclipsed because:', ['torsional strain is minimised', 'it has more bonds', 'the C–C bond is shorter', 'it is ionic'], 0, 'Bonds are furthest apart.'),
    Q(T1, 'From enthalpies of formation, ΔcH of ethane is about:', ['−1560 kJ/mol', '−890 kJ/mol', '−2220 kJ/mol', '−393 kJ/mol'], 0, '2(−393.5) + 3(−285.8) + 84.0.'),
    Q(T1, 'Cyclopropane is more reactive than cyclohexane because of:', ['ring strain', 'more hydrogens', 'aromaticity', 'hydrogen bonding'], 0, '60° angles.'),
    # T2
    Q(T2, 'The initiation step in chlorination of methane is:', ['Cl₂ → 2Cl•', 'Cl• + CH₄ → HCl + •CH₃', '•CH₃ + Cl• → CH₃Cl', 'CH₄ → C + 2H₂'], 0, 'UV splits Cl₂.'),
    Q(T2, 'Which step regenerates the chain carrier?', ['propagation', 'initiation', 'termination', 'none'], 0, 'Cl• is regenerated.'),
    Q(T2, 'Monochlorination of propane gives about what percentage of 2-chloropropane (2° : 1° reactivity 3.8 : 1)?', ['56%', '44%', '25%', '79%'], 0, '7.6/13.6.'),
    Q(T2, 'Monobromination of propane (2° : 1° = 82 : 1) gives about what percentage of 2-bromopropane?', ['96.5%', '56%', '82%', '75%'], 0, '164/170.'),
    Q(T2, 'The most stable alkyl radical is:', ['tertiary', 'secondary', 'primary', 'methyl'], 0, '3° > 2° > 1°.'),
    Q(T2, 'Radical mechanisms use arrows that are:', ['half-headed (fish-hook)', 'full-headed', 'double-headed', 'dashed'], 0, 'Single electrons.'),
    # T3
    Q(T3, 'A nucleophile is:', ['an electron-pair donor', 'an electron-pair acceptor', 'always positive', 'a radical'], 0, '"Nucleus-loving."'),
    Q(T3, 'If a rate doubles from 298 K to 308 K, Ea is about:', ['53 kJ/mol', '5.3 kJ/mol', '530 kJ/mol', '12 kJ/mol'], 0, 'Arrhenius.'),
    Q(T3, 'At 298 K, K = 100 corresponds to ΔG of about:', ['−11.4 kJ/mol', '+11.4 kJ/mol', '−4.9 kJ/mol', '−114 kJ/mol'], 0, '−RT ln K.'),
    Q(T3, 'The most stable carbocation is:', ['(CH₃)₃C⁺', 'CH₃CH₂⁺', 'CH₃⁺', '(CH₃)₂CH⁺'], 0, 'Tertiary.'),
    Q(T3, 'A curly arrow always starts at:', ['a lone pair, bond or negative charge', 'a positive charge', 'a nucleus', 'the electrophile'], 0, 'Electrons move.'),
    Q(T3, 'A transition state is:', ['an energy maximum that cannot be isolated', 'an energy minimum', 'a stable product', 'the same as an intermediate'], 0, 'Top of the barrier.'),
    # T4
    Q(T4, 'For SN2 with k = 2.0 × 10⁻³ L mol⁻¹ s⁻¹, [RX] = 0.10 M and [Nu] = 0.20 M, the rate is:', ['4.0 × 10⁻⁵ mol L⁻¹ s⁻¹', '2.0 × 10⁻⁴ mol L⁻¹ s⁻¹', '6.0 × 10⁻⁴ mol L⁻¹ s⁻¹', '4.0 × 10⁻⁴ mol L⁻¹ s⁻¹'], 0, 'k[RX][Nu].'),
    Q(T4, 'Doubling both [RX] and [Nu] in an SN2 reaction makes the rate:', ['four times faster', 'twice as fast', 'unchanged', 'eight times faster'], 0, 'Second order overall.'),
    Q(T4, 'An SN1 reaction with k = 1.0 × 10⁻⁴ s⁻¹ has a half-life of about:', ['1.9 hours', '19 hours', '6.9 minutes', '0.69 s'], 0, 'ln 2/k ≈ 6930 s.'),
    Q(T4, 'SN2 at a stereocentre gives:', ['inversion of configuration', 'racemisation', 'retention', 'no product'], 0, 'Backside attack.'),
    Q(T4, '2-bromo-2-methylpropane in water reacts mainly by:', ['SN1', 'SN2', 'radical substitution', 'no reaction'], 0, 'Tertiary substrate.'),
    Q(T4, 'The best leaving group is:', ['I⁻', 'Br⁻', 'Cl⁻', 'F⁻'], 0, 'Weakest base.'),
]

FLASH = [
    ['Newman projection', 'View down a C–C bond; staggered is lower than eclipsed.'],
    ['Chair cyclohexane', 'Large groups prefer equatorial positions.'],
    ['Radical chain', 'Initiation, propagation (regenerates radical), termination.'],
    ['Halogenation selectivity', 'Share ∝ number of H × reactivity; Br far more selective than Cl.'],
    ['Nucleophile and electrophile', 'Electron-pair donor and acceptor.'],
    ['Carbocation stability', '3° > 2° > 1° > methyl.'],
    ['SN2', 'One step, rate k[RX][Nu], inversion, methyl/1° best.'],
    ['SN1', 'Carbocation, rate k[RX], racemisation, 3° best.'],
]
