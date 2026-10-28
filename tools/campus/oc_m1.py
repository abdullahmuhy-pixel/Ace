"""Organic Chemistry, module 1: Structure, bonding and naming."""
import math
from verify import Q
from oc_common import mass, dou, ALKANE_ISOMERS, r, pH
T1, T2, T3, T4 = ('Bonding, hybridisation and shape', 'Functional groups and naming', 'Isomerism and stereochemistry', 'Organic acids, bases and resonance')

# sigma/pi counts: ethene, ethyne, propenenitrile CH2=CH-C#N
bonds = lambda single, double, triple: (single + double + triple, double + 2 * triple)
assert bonds(4, 1, 0) == (5, 1) and bonds(2, 0, 1) == (3, 2) and bonds(4, 1, 1) == (6, 3)  # CH2=CH-C#N: 3 C-H + 1 C-C single
assert r(mass('C5H12'), 2) == 72.15 and r(mass('C2H6O'), 2) == 46.07 and r(mass('C3H6O'), 2) == 58.08
assert dou('C6H6') == 4 and dou('C4H8') == 1 and dou('C5H8') == 2 and dou('C6H12') == 1 and dou('C10H8') == 7 and dou('C4H9Br') == 0
assert ALKANE_ISOMERS[5] == 3 and ALKANE_ISOMERS[6] == 5 and ALKANE_ISOMERS[7] == 9 and ALKANE_ISOMERS[4] == 2
assert 2 ** 2 == 4 and 2 ** 4 == 16 and 2 ** 3 == 8
Ka = 10 ** -4.76
assert r(Ka * 1e5, 2) == 1.74 and r(pH(math.sqrt(Ka * 0.1)), 2) == 2.88 and r(4.76 + math.log10(0.2 / 0.1), 2) == 5.06
assert r(10 ** -2.87 / Ka, -1) == 80 and round(16 - 4.76) == 11

MODULE = {
    'title': 'Structure, bonding and naming',
    'topics': [T1, T2, T3, T4],
    'overview': 'Organic chemistry is the chemistry of carbon compounds. This module lays the foundations: how carbon bonds and what shapes result, how to recognise functional groups and name molecules by IUPAC rules, how the same atoms can be arranged as different isomers, including mirror-image forms, and how acidity and resonance explain much of organic reactivity.',
    'key_terms': ['Covalent bond', 'Hybridisation', 'Sigma bond', 'Pi bond', 'Functional group', 'IUPAC name', 'Homologous series', 'Structural isomer', 'Stereoisomer', 'Chiral centre', 'Enantiomer', 'E/Z isomerism', 'pKa', 'Conjugate base', 'Resonance'],
    'explanation': [
        'Carbon forms four bonds. Its orbitals hybridise to sp³ (tetrahedral, 109.5°), sp² (trigonal planar, 120°) or sp (linear, 180°). Single bonds are σ bonds; a double bond is one σ and one π; a triple bond is one σ and two π.',
        'Molecules are grouped by functional groups (alkene, alcohol, aldehyde, ketone, carboxylic acid, ester, amine and so on), which decide how they react. IUPAC names give the longest chain, the main functional group as a suffix, and substituents with locant numbers as prefixes.',
        'Isomers share a formula but differ in structure. Structural isomers differ in connectivity; stereoisomers differ only in 3D arrangement: E/Z about double bonds, and enantiomers (non-superimposable mirror images) around chiral carbons. Acidity is measured by pKa: the more stable the conjugate base, often because of resonance, the stronger the acid.'],
    'quick_facts': [
        'sp³ 109.5°, sp² 120°, sp 180°.',
        'Double bond = 1σ + 1π; triple = 1σ + 2π.',
        'Degrees of unsaturation = (2C + 2 + N − H − X)/2.',
        'n stereocentres → up to 2ⁿ stereoisomers.',
        'Lower pKa = stronger acid; ΔpKa of 1 = 10× in Ka.'],
}

NOTES = {
    T1: {
        'overview': 'The shape of an organic molecule follows from how carbon\'s orbitals hybridise, and that shape governs physical properties and reactivity.',
        'key_terms': ['Valence', 'Lewis structure', 'Hybrid orbital', 'sp³, sp², sp', 'Sigma bond', 'Pi bond', 'Bond angle', 'Electronegativity', 'Polar bond'],
        'explanation': [
            'Carbon has four valence electrons and makes four bonds. In methane its 2s and three 2p orbitals mix into four sp³ hybrids pointing to the corners of a tetrahedron, 109.5° apart. In ethene each carbon is sp²: three hybrids in a plane at 120° and one unhybridised p orbital; in ethyne each carbon is sp, linear at 180°, with two p orbitals left.',
            'Head-on overlap gives σ bonds; sideways overlap of p orbitals gives π bonds, which are weaker and lie above and below the bond axis. Ethene has 5 σ bonds and 1 π bond; ethyne has 3 σ and 2 π. Propenenitrile, CH₂=CH–C≡N, has 6 σ and 3 π.',
            'Because π bonds block rotation, C=C double bonds are rigid. Electronegativity differences (O 3.4, N 3.0, C 2.6, H 2.2) make C–O and C–N bonds polar, with δ+ on carbon: that partly positive carbon is where nucleophiles attack.'],
        'formulas_label': 'Rules',
        'formulas': ['4 electron groups → sp³, 109.5°', '3 groups → sp², 120°', '2 groups → sp, 180°', 'Single = σ; double = σ + π; triple = σ + 2π'],
        'steps': ['Draw the Lewis structure.', 'Count electron groups (bonds + lone pairs) on each atom.', 'Assign hybridisation and angle.', 'Count σ and π bonds bond by bond.'],
        'worked_example': {
            'problem': 'Count the σ and π bonds in propenenitrile, CH₂=CH–C≡N, and give each carbon\'s hybridisation.',
            'steps': ['Bonds: 3 C–H (σ), C=C (σ + π), C–C (σ), C≡N (σ + 2π).', 'σ: 3 + 1 + 1 + 1 = 6; π: 1 + 2 = 3.', 'The two alkene carbons are sp²; the nitrile carbon is sp.'],
            'answer': '6 σ and 3 π bonds; sp², sp², sp.',
            'check': 'Every bond contains exactly one σ ✓; 6 bonds in all ✓.'},
        'mistakes': ['Counting a double bond as two σ bonds.', 'Forgetting lone pairs when counting electron groups.', 'Thinking π bonds allow free rotation.', 'Drawing carbon with five bonds.'],
        'real_world': 'The rigid sp² carbons in retinal flip from Z to E when light hits your eye, the first step in vision.',
        'exam_strategy': 'Mark each atom\'s hybridisation on the structure as you count; it prevents double counting.',
        'recap': ['Four bonds to carbon.', 'sp³/sp²/sp shapes.', 'σ and π.', 'Polar bonds make δ+ carbons.']},
    T2: {
        'overview': 'Functional groups are the reactive parts of molecules. IUPAC rules turn any structure into a unique name.',
        'key_terms': ['Functional group', 'Homologous series', 'Parent chain', 'Suffix', 'Prefix', 'Locant', 'Degree of unsaturation', 'Molecular formula'],
        'explanation': [
            'Key groups: alkene C=C (-ene), alkyne C≡C (-yne), alcohol –OH (-ol), haloalkane (halo-), ether R–O–R, aldehyde –CHO (-al), ketone C=O within a chain (-one), carboxylic acid –COOH (-oic acid), ester –COOR (-oate), amine –NH₂ (-amine), amide –CONH₂ (-amide). A homologous series (such as the alkanes CₙH₂ₙ₊₂) differs by CH₂ units.',
            'Naming: find the longest chain containing the main group, number from the end that gives that group the lowest locant, then add substituents alphabetically. CH₃CH(CH₃)CH₂CH₃ is 2-methylbutane (C₅H₁₂, M = 72.15 g/mol); CH₃COCH₃ is propanone (acetone, C₃H₆O); CH₃CH₂OH is ethanol (C₂H₆O, 46.07 g/mol).',
            'The degree of unsaturation (2C + 2 + N − H − X)/2 counts rings plus π bonds from a formula alone. C₄H₈ has 1 (an alkene or a ring); C₆H₆ has 4 (benzene: one ring and three C=C); C₁₀H₈ (naphthalene) has 7. Halogens count like H; oxygen is ignored.'],
        'formulas_label': 'Formulas',
        'formulas': ['Alkanes CₙH₂ₙ₊₂; alkenes and cycloalkanes CₙH₂ₙ', 'DoU = (2C + 2 + N − H − X)/2', 'Name = locants + prefixes + parent + suffix'],
        'steps': ['Identify the main functional group.', 'Find the longest chain containing it.', 'Number to give it the lowest locant.', 'Add substituents in alphabetical order with locants.'],
        'worked_example': {
            'problem': 'A compound has formula C₅H₈. How many rings or π bonds does it have, and what might it be?',
            'steps': ['DoU = (2 × 5 + 2 − 8)/2.', 'DoU = 4/2 = 2.', 'Two degrees: a diene, an alkyne, a cycloalkene or two rings.'],
            'answer': '2; for example pent-1-yne, penta-1,3-diene or cyclopentene.',
            'check': 'Pentane is C₅H₁₂; each degree removes two H: 12 − 4 = 8 ✓.'},
        'mistakes': ['Not choosing the longest chain.', 'Numbering from the wrong end.', 'Confusing aldehydes (-al) with alcohols (-ol).', 'Counting oxygen in the DoU formula.'],
        'real_world': 'Drug and food labels use IUPAC-style names, so a pharmacist can tell exactly which molecule is meant.',
        'exam_strategy': 'Compute the DoU first in structure problems; it tells you how many rings and double bonds to look for.',
        'recap': ['Functional groups decide reactivity.', 'Longest chain, lowest locants.', 'Alphabetical prefixes.', 'DoU from the formula.']},
    T3: {
        'overview': 'Isomers have the same formula but different arrangements. Stereoisomers differ only in 3D arrangement and can behave very differently in the body.',
        'key_terms': ['Structural (constitutional) isomer', 'Stereoisomer', 'E/Z isomer', 'Chiral centre', 'Enantiomer', 'Diastereomer', 'Racemic mixture', 'Cahn–Ingold–Prelog rules', 'Meso compound'],
        'explanation': [
            'Structural isomers differ in connectivity. C₄H₁₀ has 2 (butane and methylpropane), C₅H₁₂ has 3, C₆H₁₄ has 5 and C₇H₁₆ has 9; the number grows rapidly with chain length.',
            'E/Z isomers arise about C=C when each carbon carries two different groups: rank the groups on each carbon by atomic number (Cahn–Ingold–Prelog); Z ("zusammen") has the higher priorities on the same side, E on opposite sides.',
            'A carbon with four different groups is a chiral centre. Its mirror image is not superimposable: the pair are enantiomers, labelled R or S by CIP priorities and the direction 1 → 2 → 3 with the lowest priority pointing away. With n chiral centres there are at most 2ⁿ stereoisomers: 2 centres give up to 4; open-chain glucose, with 4, has 16. Fewer occur when a meso form has internal symmetry.'],
        'formulas_label': 'Rules',
        'formulas': ['Chiral centre: four different groups', 'Max stereoisomers = 2ⁿ', 'CIP: higher atomic number = higher priority', 'Clockwise (lowest at back) = R; anticlockwise = S'],
        'steps': ['Look for C=C with two different groups on each end (E/Z).', 'Look for carbons with four different groups (chiral).', 'Assign CIP priorities.', 'Assign E/Z or R/S.'],
        'worked_example': {
            'problem': 'A molecule has 3 chiral centres and no internal symmetry. How many stereoisomers can it have?',
            'steps': ['Each centre can be R or S.', 'Combinations: 2 × 2 × 2.', '2³ = 8.'],
            'answer': '8 stereoisomers (4 pairs of enantiomers).',
            'check': 'Each enantiomer pair flips all three centres ✓.'},
        'mistakes': ['Calling CH₂ or CH₃ carbons chiral.', 'Using cis/trans where E/Z is needed (more than two kinds of substituent).', 'Forgetting to put the lowest priority at the back for R/S.', 'Assuming 2ⁿ always (meso forms reduce it).'],
        'real_world': 'One enantiomer of ibuprofen relieves pain while the other is much less active; many drugs are now sold as single enantiomers.',
        'exam_strategy': 'Build or sketch a 3D model when assigning R/S; if the lowest priority points toward you, assign and then reverse.',
        'recap': ['Structural vs stereo.', 'E/Z by priorities.', 'Four different groups = chiral.', 'Up to 2ⁿ stereoisomers.']},
    T4: {
        'overview': 'Acidity explains a great deal of organic reactivity. The key question is always how stable the conjugate base is.',
        'key_terms': ['Brønsted acid', 'Conjugate base', 'Ka', 'pKa', 'Resonance', 'Inductive effect', 'Delocalisation', 'Henderson–Hasselbalch'],
        'explanation': [
            'pKa = −log Ka; lower pKa means a stronger acid. Typical values: carboxylic acids about 4 to 5 (ethanoic acid 4.76, Ka = 1.74 × 10⁻⁵), phenol 10, water 15.7, ethanol about 16. A 0.1 mol/L ethanoic acid solution has [H⁺] ≈ √(KaC) and pH ≈ 2.88.',
            'Resonance stabilises conjugate bases. In ethanoate the negative charge is shared equally between two oxygens (each C–O bond order 1.5), so ethanoic acid is far more acidic than ethanol, whose ethoxide ion keeps the charge on one oxygen: about 10¹¹ times in Ka.',
            'Electronegative groups near the acidic site pull electron density (the inductive effect) and stabilise the base: chloroethanoic acid (pKa 2.87) is about 80 times stronger than ethanoic acid. Buffers follow Henderson–Hasselbalch: with twice as much ethanoate as acid, pH = 4.76 + log 2 ≈ 5.06.'],
        'formulas_label': 'Formulas',
        'formulas': ['pKa = −log Ka', 'Weak acid: [H⁺] ≈ √(Ka C)', 'pH = pKa + log([A⁻]/[HA])', 'Ka ratio = 10^(ΔpKa)'],
        'steps': ['Draw the conjugate base.', 'Ask where the charge sits: electronegative atom, resonance, nearby electron-withdrawing groups.', 'More stable base → stronger acid.', 'Use pKa values for numbers.'],
        'worked_example': {
            'problem': 'How many times stronger is chloroethanoic acid (pKa 2.87) than ethanoic acid (pKa 4.76)?',
            'steps': ['ΔpKa = 4.76 − 2.87 = 1.89.', 'The Ka ratio is 10 raised to 1.89.', 'Ratio ≈ 78, roughly 80.'],
            'answer': 'About 80 times stronger.',
            'check': 'Lower pKa, so stronger ✓; Cl withdraws electrons and stabilises the anion ✓.'},
        'mistakes': ['Thinking a higher pKa is a stronger acid.', 'Forgetting that pKa is logarithmic.', 'Drawing resonance forms that move atoms rather than electrons.', 'Ignoring which atom carries the charge.'],
        'real_world': 'Aspirin is a carboxylic acid; its acidity affects where in the gut it is absorbed and why it can irritate the stomach.',
        'exam_strategy': 'In acidity ranking questions, always draw the conjugate bases and compare them, not the acids.',
        'recap': ['Lower pKa, stronger acid.', 'Resonance stabilises bases.', 'Inductive effects.', 'Henderson–Hasselbalch.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The bond angle around an sp³ carbon is about:', ['109.5°', '120°', '180°', '90°'], 0, 'Tetrahedral.'),
    Q(T1, 'The carbons in ethene are:', ['sp²', 'sp³', 'sp', 'sp³d'], 0, 'Three electron groups.'),
    Q(T1, 'Ethyne (HC≡CH) contains:', ['3 σ and 2 π bonds', '2 σ and 3 π bonds', '5 σ and 0 π bonds', '3 σ and 1 π bond'], 0, 'Triple = σ + 2π.'),
    Q(T1, 'Propenenitrile, CH₂=CH–C≡N, has how many π bonds?', ['3', '2', '6', '1'], 0, '1 in C=C, 2 in C≡N.', ans=3, num=True),
    Q(T1, 'Rotation about a C=C double bond is restricted because:', ['the π bond would have to break', 'the σ bond is too short', 'carbon is too heavy', 'of hydrogen bonding'], 0, 'Sideways p overlap.'),
    Q(T1, 'In a C–O bond, the carbon carries:', ['a partial positive charge', 'a partial negative charge', 'no charge', 'a full positive charge'], 0, 'O is more electronegative.'),
    # T2
    Q(T2, 'The functional group –CHO is:', ['an aldehyde', 'a ketone', 'an alcohol', 'a carboxylic acid'], 0, 'Suffix -al.'),
    Q(T2, 'CH₃CH(CH₃)CH₂CH₃ is named:', ['2-methylbutane', '3-methylbutane', 'pentane', '2-ethylpropane'], 0, 'Lowest locant.'),
    Q(T2, 'The degree of unsaturation of C₆H₆ is:', ['4', '3', '6', '1'], 0, '(12 + 2 − 6)/2.', ans=4, num=True),
    Q(T2, 'The degree of unsaturation of C₅H₈ is:', ['2', '1', '3', '4'], 0, '(10 + 2 − 8)/2.', ans=2, num=True),
    Q(T2, 'The molar mass of 2-methylbutane (C₅H₁₂) is about:', ['72.15 g/mol', '70.13 g/mol', '58.12 g/mol', '86.18 g/mol'], 0, '5 × 12.01 + 12 × 1.008.'),
    Q(T2, 'An ester\'s IUPAC name ends in:', ['-oate', '-ol', '-one', '-al'], 0, 'e.g. ethyl ethanoate.'),
    # T3
    Q(T3, 'How many structural isomers does C₅H₁₂ have?', ['3', '2', '5', '4'], 0, 'Pentane, methylbutane, dimethylpropane.', ans=3, num=True),
    Q(T3, 'How many structural isomers does C₆H₁₄ have?', ['5', '4', '6', '9'], 0, 'Hexanes.', ans=5, num=True),
    Q(T3, 'A chiral carbon has:', ['four different groups attached', 'a double bond', 'two identical groups', 'a lone pair'], 0, 'No internal mirror plane.'),
    Q(T3, 'A molecule with 3 chiral centres and no symmetry has at most:', ['8', '6', '3', '9'], 0, '2³.', ans=8, num=True),
    Q(T3, 'Enantiomers are:', ['non-superimposable mirror images', 'structural isomers', 'E/Z isomers', 'identical molecules'], 0, 'Mirror pair.'),
    Q(T3, 'In a Z alkene, the higher-priority groups are:', ['on the same side', 'on opposite sides', 'on the same carbon', 'absent'], 0, 'Zusammen = together.'),
    # T4
    Q(T4, 'Ethanoic acid has pKa 4.76. Its Ka is about:', ['1.74 × 10⁻⁵', '4.76 × 10⁻¹', '5.8 × 10⁴', '1.74 × 10⁻⁴'], 0, '10^−4.76.'),
    Q(T4, 'The pH of 0.10 mol/L ethanoic acid is about:', ['2.88', '1.00', '4.76', '3.88'], 0, '√(KaC).', ans=2.88, num=True),
    Q(T4, 'A buffer with [ethanoate]/[ethanoic acid] = 2 has pH about:', ['5.06', '4.46', '4.76', '6.76'], 0, '4.76 + log 2.', ans=5.06, num=True),
    Q(T4, 'Ethanoic acid is much more acidic than ethanol because:', ['its conjugate base is stabilised by resonance', 'it has more hydrogens', 'ethanol is ionic', 'it is a gas'], 0, 'Charge shared by two O.'),
    Q(T4, 'Which is the strongest acid?', ['chloroethanoic acid (pKa 2.87)', 'ethanoic acid (pKa 4.76)', 'phenol (pKa 10)', 'ethanol (pKa 16)'], 0, 'Lowest pKa.'),
    Q(T4, 'Chloroethanoic acid is stronger than ethanoic acid mainly because of:', ['the inductive effect of chlorine', 'hydrogen bonding', 'its higher molar mass', 'steric hindrance'], 0, 'Electron withdrawal.'),
]

FLASH = [
    ['Hybridisation and angle', 'sp³ 109.5°, sp² 120°, sp 180°.'],
    ['σ and π bonds', 'Double = σ + π; triple = σ + 2π.'],
    ['Degree of unsaturation', '(2C + 2 + N − H − X)/2 = rings + π bonds.'],
    ['IUPAC naming', 'Longest chain with main group; lowest locants; prefixes alphabetical.'],
    ['Chiral centre', 'Carbon with four different groups.'],
    ['Stereoisomer count', 'Up to 2ⁿ for n chiral centres.'],
    ['pKa', 'Lower pKa = stronger acid.'],
    ['Resonance and acidity', 'Delocalised conjugate base → stronger acid.'],
]
