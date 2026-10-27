"""General Chemistry, module 2: Electrons, bonding and molecular shape."""
from verify import Q
T1, T2, T3, T4 = ('Electron configuration and periodic trends', 'Ionic, covalent and metallic bonding', 'Molecular shape and polarity', 'Intermolecular forces and physical properties')

# aufbau order check for configurations used in the course
ORDER = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p']
CAP = {'s': 2, 'p': 6, 'd': 10}


def config(z):
    out = []
    for o in ORDER:
        if z <= 0: break
        k = min(z, CAP[o[-1]]); out.append(f'{o}{k}'); z -= k
    return ' '.join(out)


assert config(11) == '1s2 2s2 2p6 3s1' and config(8) == '1s2 2s2 2p4' and config(17) == '1s2 2s2 2p6 3s2 3p5'
assert config(26) == '1s2 2s2 2p6 3s2 3p6 4s2 3d6'
assert round(3.16 - 0.93, 2) == 2.23

MODULE = {
    'title': 'Electrons, bonding and molecular shape',
    'topics': [T1, T2, T3, T4],
    'overview': 'The arrangement of electrons explains almost everything about an element\'s chemistry: where it sits in the periodic table, what bonds it forms, the shapes of its molecules and the properties of the substances it makes. This module moves from electron configuration to bonding, molecular shape and the forces between molecules.',
    'key_terms': ['Orbital', 'Electron configuration', 'Ionisation energy', 'Electronegativity', 'Ionic bond', 'Covalent bond', 'Lewis structure', 'VSEPR', 'Polarity', 'Hydrogen bond'],
    'explanation': [
        'Electrons occupy orbitals in shells and subshells (s, p, d) filled in order of increasing energy. Elements in the same group have the same outer-electron arrangement, which is why they behave alike. Trends such as atomic radius, ionisation energy and electronegativity follow from nuclear charge and shielding.',
        'Atoms bond to reach more stable electron arrangements. Metals transfer electrons to non-metals to form ions held by ionic bonds; non-metals share pairs of electrons in covalent bonds; metal atoms share a sea of delocalised electrons in metallic bonding.',
        'The shape of a molecule is set by repulsion between electron pairs around the central atom (VSEPR theory). Shape and electronegativity together decide polarity, and polarity decides the intermolecular forces that control boiling points and solubility.'],
    'quick_facts': [
        'Fill order: 1s 2s 2p 3s 3p 4s 3d 4p …',
        'Across a period: radius ↓, ionisation energy ↑, electronegativity ↑.',
        'Large electronegativity difference (about 1.7 or more): ionic; smaller: polar covalent.',
        'VSEPR: 4 pairs tetrahedral 109.5°; NH₃ 107°; H₂O 104.5°.',
        'Strength of attractions: hydrogen bonds > dipole–dipole > London dispersion (for similar sizes).'],
}

NOTES = {
    T1: {
        'overview': 'Electron configuration describes how electrons are arranged in shells and subshells. It explains the layout of the periodic table and the trends in atomic properties.',
        'key_terms': ['Shell', 'Subshell (s, p, d)', 'Orbital', 'Aufbau principle', 'Valence electrons', 'Atomic radius', 'Ionisation energy', 'Electronegativity'],
        'explanation': [
            'Subshells fill in order of energy: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p. An s subshell holds 2 electrons, p holds 6 and d holds 10. Sodium (11 electrons) is 1s² 2s² 2p⁶ 3s¹, with one valence electron, like every group 1 metal. Iron (26) is 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶.',
            'Across a period, protons are added while shielding changes little, so the effective nuclear charge rises: atoms get smaller, first ionisation energy rises, and electronegativity rises. Down a group, an extra shell is added each time: atoms get larger and outer electrons are easier to remove.',
            'Electronegativity is an atom\'s pull on bonding electrons. Fluorine is the most electronegative element (about 4.0); metals such as sodium have low values. These trends explain why group 1 metals react more vigorously going down the group while halogens react less vigorously.'],
        'formulas_label': 'Rules',
        'formulas': ['s holds 2, p holds 6, d holds 10', 'Order: 1s 2s 2p 3s 3p 4s 3d 4p', 'Across a period: radius ↓, IE ↑, EN ↑', 'Down a group: radius ↑, IE ↓, EN ↓'],
        'steps': ['Find the number of electrons (Z for a neutral atom).', 'Fill subshells in order.', 'Identify valence electrons and the group.', 'Use nuclear charge and shielding to explain trends.'],
        'worked_example': {
            'problem': 'Write the electron configuration of chlorine (Z = 17) and predict the charge of its ion.',
            'steps': ['Fill: 1s² 2s² 2p⁶ 3s² 3p⁵, which is 17 electrons.', 'It has 7 valence electrons (3s² 3p⁵), one short of a full shell.', 'It gains one electron to become Cl⁻.'],
            'answer': '1s² 2s² 2p⁶ 3s² 3p⁵; it forms Cl⁻.',
            'check': 'Cl⁻ has the same configuration as argon, a stable noble gas ✓.'},
        'mistakes': ['Filling 3d before 4s.', 'Putting more than 2 electrons in an s subshell.', 'Saying atoms get bigger across a period.', 'Confusing ionisation energy with electronegativity.'],
        'real_world': 'The trend that caesium loses its outer electron extremely easily is why it is used in photoelectric cells and atomic clocks.',
        'exam_strategy': 'Explain trends with the three ideas examiners look for: nuclear charge, distance of outer electrons and shielding.',
        'recap': ['Fill subshells in energy order.', 'Valence electrons decide the group.', 'Across: smaller, higher IE and EN.', 'Down: larger, lower IE and EN.']},
    T2: {
        'overview': 'Atoms bond by transferring or sharing electrons. The type of bonding (ionic, covalent or metallic) explains a substance\'s properties.',
        'key_terms': ['Ionic bond', 'Lattice', 'Covalent bond', 'Lone pair', 'Lewis structure', 'Polar covalent', 'Metallic bond', 'Delocalised electrons'],
        'explanation': [
            'Ionic bonding forms when a metal transfers electrons to a non-metal, creating oppositely charged ions held in a giant lattice. Ionic compounds have high melting points and conduct electricity when molten or dissolved, because the ions can move.',
            'Covalent bonding is the sharing of electron pairs between non-metals. Lewis structures show bonding pairs and lone pairs so that each atom (except hydrogen) usually has 8 outer electrons. Multiple bonds share 2 or 3 pairs (O=O, N≡N). When the atoms differ in electronegativity, the bond is polar, with partial charges δ+ and δ−.',
            'In metals, outer electrons are delocalised across a lattice of positive ions. This explains conductivity, malleability and high melting points. Bond type is a spectrum: an electronegativity difference above about 1.7 is mainly ionic (NaCl, difference 2.23), smaller differences are polar covalent, and zero is non-polar covalent.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Ionic: metal + non-metal, electron transfer', 'Covalent: non-metals, shared pairs', 'Metallic: delocalised electrons', 'ΔEN > ~1.7 mainly ionic; 0.4–1.7 polar covalent; < 0.4 non-polar'],
        'steps': ['Identify the elements (metal, non-metal).', 'Decide on transfer or sharing.', 'Draw ions or a Lewis structure.', 'Relate bonding to properties.'],
        'worked_example': {
            'problem': 'Draw the Lewis structure of ammonia, NH₃.',
            'steps': ['Valence electrons: N 5 + 3 × H 1 = 8 (4 pairs).', 'N forms three single bonds to H (3 pairs).', 'The remaining pair is a lone pair on N.'],
            'answer': 'N in the centre bonded to three H atoms, with one lone pair on N.',
            'check': 'N has 8 electrons around it and each H has 2 ✓.'},
        'mistakes': ['Calling a metal–non-metal compound covalent without reason.', 'Forgetting lone pairs in Lewis structures.', 'Saying ionic solids conduct electricity.', 'Giving hydrogen 8 electrons.'],
        'real_world': 'Table salt (ionic) dissolves and conducts in water, sugar (covalent) dissolves but does not conduct, and copper (metallic) conducts as a solid, which is why it is used in wiring.',
        'exam_strategy': 'Link structure to property in one sentence ("high melting point because strong electrostatic attraction between ions throughout the lattice").',
        'recap': ['Ionic: transfer, lattice.', 'Covalent: shared pairs, Lewis structures.', 'Metallic: delocalised electrons.', 'Bond type from ΔEN.']},
    T3: {
        'overview': 'The shape of a molecule depends on how electron pairs around the central atom repel each other. Shape and bond polarity decide whether the whole molecule is polar.',
        'key_terms': ['VSEPR', 'Electron domain', 'Bond angle', 'Linear', 'Trigonal planar', 'Tetrahedral', 'Trigonal pyramidal', 'Bent', 'Dipole moment'],
        'explanation': [
            'VSEPR (valence shell electron pair repulsion) theory: electron domains (bonds and lone pairs) around the central atom arrange themselves as far apart as possible. Two domains are linear (180°), three trigonal planar (120°), four tetrahedral (109.5°).',
            'Lone pairs repel more strongly than bonding pairs, squeezing bond angles. CH₄ (4 bonds) is tetrahedral at 109.5°; NH₃ (3 bonds, 1 lone pair) is trigonal pyramidal at about 107°; H₂O (2 bonds, 2 lone pairs) is bent at about 104.5°.',
            'A molecule is polar if it has polar bonds arranged so their dipoles do not cancel. CO₂ has polar C=O bonds but is linear, so the dipoles cancel and the molecule is non-polar. H₂O is bent, so its dipoles add and water is strongly polar.'],
        'formulas_label': 'Shapes',
        'formulas': ['2 domains: linear 180° (CO₂)', '3 domains: trigonal planar 120° (BF₃)', '4 domains: tetrahedral 109.5° (CH₄)', '3 bonds + 1 lone pair: pyramidal ~107° (NH₃)', '2 bonds + 2 lone pairs: bent ~104.5° (H₂O)'],
        'steps': ['Draw the Lewis structure.', 'Count electron domains around the central atom.', 'Choose the arrangement and name the shape from the atoms.', 'Check whether bond dipoles cancel.'],
        'worked_example': {
            'problem': 'Predict the shape and polarity of CO₂ and H₂O.',
            'steps': ['CO₂: carbon has two double-bond domains and no lone pairs, so it is linear.', 'The two C=O dipoles point in opposite directions and cancel: non-polar.', 'H₂O: oxygen has two bonds and two lone pairs, so it is bent (~104.5°) and its dipoles add: polar.'],
            'answer': 'CO₂ is linear and non-polar; H₂O is bent and polar.',
            'check': 'This explains why water dissolves salts and has a high boiling point for its size, while CO₂ is a gas.'},
        'mistakes': ['Ignoring lone pairs when naming the shape.', 'Saying a molecule with polar bonds must be polar.', 'Counting a double bond as two domains.', 'Giving NH₃ a bond angle of 109.5°.'],
        'real_world': 'Drug molecules work by fitting into proteins like keys into locks; their three-dimensional shape is as important as their atoms.',
        'exam_strategy': 'State the number of bonding pairs and lone pairs before naming the shape. Examiners award marks for that reasoning.',
        'recap': ['Electron pairs repel as far apart as possible.', 'Lone pairs squeeze angles.', 'Name the shape from the atoms.', 'Polarity needs non-cancelling dipoles.']},
    T4: {
        'overview': 'Intermolecular forces are attractions between molecules. They are much weaker than covalent bonds but control boiling points, solubility and many biological structures.',
        'key_terms': ['London dispersion forces', 'Dipole–dipole forces', 'Hydrogen bonding', 'Boiling point', 'Solubility', '"Like dissolves like"'],
        'explanation': [
            'London dispersion forces arise from temporary dipoles and exist between all molecules; they increase with the number of electrons (molecular size). Dipole–dipole forces act between polar molecules.',
            'Hydrogen bonding is an especially strong dipole–dipole attraction when H is bonded to N, O or F and is attracted to a lone pair on another N, O or F. It explains why water boils at 100 °C while H₂S, a heavier molecule, boils at about −60 °C.',
            'Boiling a molecular substance separates molecules, overcoming intermolecular forces but not breaking covalent bonds. Polar and hydrogen-bonding substances dissolve in water; non-polar substances such as oils dissolve in non-polar solvents ("like dissolves like").'],
        'formulas_label': 'Order of strength (similar size)',
        'formulas': ['Hydrogen bonding > dipole–dipole > London dispersion', 'Dispersion forces increase with molecular size', 'H-bonding needs H on N, O or F', 'Like dissolves like'],
        'steps': ['Decide whether the molecule is polar.', 'Check for H bonded to N, O or F.', 'Consider molecular size for dispersion forces.', 'Rank boiling points or predict solubility.'],
        'worked_example': {
            'problem': 'Explain why ethanol (C₂H₅OH) dissolves in water but hexane (C₆H₁₄) does not.',
            'steps': ['Ethanol has an O–H group that can hydrogen-bond with water.', 'Hexane is non-polar and attracts water only weakly by dispersion forces.', 'Water molecules hold together more strongly than they would bond to hexane.'],
            'answer': 'Ethanol mixes with water through hydrogen bonding; hexane does not because it is non-polar.',
            'check': 'Hexane dissolves well in other non-polar liquids, consistent with "like dissolves like".'},
        'mistakes': ['Saying covalent bonds break when water boils.', 'Calling any H-containing molecule hydrogen-bonded.', 'Ignoring dispersion forces, which can dominate for large molecules.', 'Confusing intermolecular with intramolecular forces.'],
        'real_world': 'Hydrogen bonds hold the two strands of DNA together and give proteins their shapes; they are strong enough to keep structure but weak enough to be unzipped when cells copy DNA.',
        'exam_strategy': 'When comparing boiling points, name the strongest intermolecular force in each substance, then compare.',
        'recap': ['Dispersion forces in all molecules.', 'Dipole–dipole in polar molecules.', 'H-bonding with N, O, F.', 'Like dissolves like.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The electron configuration of sodium (Z = 11) is:', ['1s² 2s² 2p⁶ 3s¹', '1s² 2s² 2p⁷', '1s² 2s² 2p⁶ 3p¹', '1s² 2s⁸ 3s¹'], 0, 'Fill 1s, 2s, 2p, then 3s.'),
    Q(T1, 'Which subshell fills just before 3d?', ['4s', '3p', '4p', '3s'], 0, '4s is lower in energy than 3d for these atoms.'),
    Q(T1, 'Across period 3 from sodium to chlorine, atomic radius:', ['decreases', 'increases', 'stays the same', 'first increases then decreases'], 0, 'Rising nuclear charge pulls electrons closer.'),
    Q(T1, 'The most electronegative element is:', ['fluorine', 'oxygen', 'chlorine', 'caesium'], 0, 'About 4.0 on the Pauling scale.'),
    Q(T1, 'Down group 1, first ionisation energy:', ['decreases', 'increases', 'is constant', 'becomes zero'], 0, 'Outer electrons are further away and more shielded.'),
    Q(T1, 'How many valence electrons does chlorine (1s² 2s² 2p⁶ 3s² 3p⁵) have?', ['7', '5', '17', '2'], 0, '3s² 3p⁵.', ans=7),
    # T2
    Q(T2, 'Sodium chloride is held together by:', ['ionic bonds in a lattice', 'covalent bonds', 'metallic bonds', 'hydrogen bonds'], 0, 'Metal + non-metal, electron transfer.'),
    Q(T2, 'The electronegativity difference in NaCl (3.16 − 0.93) is:', ['2.23', '4.09', '0.93', '3.16'], 0, 'Large difference: mainly ionic.'),
    Q(T2, 'How many lone pairs are on nitrogen in NH₃?', ['1', '0', '2', '3'], 0, '8 valence electrons: 3 bonding pairs, 1 lone pair.', ans=1),
    Q(T2, 'A triple bond is found in:', ['N₂', 'O₂', 'H₂', 'Cl₂'], 0, 'N≡N shares three pairs.'),
    Q(T2, 'Ionic compounds conduct electricity when:', ['molten or dissolved', 'solid', 'cooled', 'never'], 0, 'Ions must be free to move.'),
    Q(T2, 'Metals conduct electricity because of:', ['delocalised electrons', 'free ions in a solution', 'lone pairs', 'hydrogen bonds'], 0, 'Electrons move through the lattice.'),
    # T3
    Q(T3, 'The shape of CH₄ is:', ['tetrahedral', 'square planar', 'trigonal pyramidal', 'linear'], 0, 'Four bonding pairs, no lone pairs.'),
    Q(T3, 'The approximate H–O–H bond angle in water is:', ['104.5°', '109.5°', '120°', '180°'], 0, 'Two lone pairs squeeze the angle.'),
    Q(T3, 'The shape of NH₃ is:', ['trigonal pyramidal', 'trigonal planar', 'tetrahedral', 'bent'], 0, 'Three bonds and one lone pair.'),
    Q(T3, 'CO₂ is non-polar because:', ['its bond dipoles cancel in a linear shape', 'C=O bonds are non-polar', 'it has lone pairs on carbon', 'it is a gas'], 0, 'Equal and opposite dipoles.'),
    Q(T3, 'BF₃ (three bonds, no lone pairs on B) is:', ['trigonal planar, 120°', 'trigonal pyramidal', 'tetrahedral', 'bent'], 0, 'Three domains.'),
    Q(T3, 'Which molecule is polar?', ['H₂O', 'CO₂', 'CH₄', 'CCl₄'], 0, 'Its bent shape means the dipoles do not cancel.'),
    # T4
    Q(T4, 'Water boils far higher than H₂S mainly because of:', ['hydrogen bonding', 'its larger mass', 'ionic bonds', 'metallic bonding'], 0, 'O–H groups hydrogen-bond; S is not electronegative enough.'),
    Q(T4, 'Which forces exist between all molecules?', ['London dispersion forces', 'hydrogen bonds', 'ionic bonds', 'dipole–dipole forces'], 0, 'Temporary dipoles occur in every molecule.'),
    Q(T4, 'When water boils, what is overcome?', ['Hydrogen bonds between molecules', 'O–H covalent bonds', 'ionic bonds', 'nuclear forces'], 0, 'Molecules separate; they do not break apart.'),
    Q(T4, 'Hydrogen bonding requires H bonded to:', ['N, O or F', 'C', 'any non-metal', 'a metal'], 0, 'Only these are electronegative enough.'),
    Q(T4, 'Oil does not dissolve in water because:', ['oil is non-polar and water is polar', 'oil is ionic', 'water is non-polar', 'oil is denser'], 0, 'Like dissolves like.'),
    Q(T4, 'Among the halogens F₂, Cl₂, Br₂, I₂, the highest boiling point is:', ['I₂', 'F₂', 'Cl₂', 'Br₂'], 0, 'Most electrons, so the strongest dispersion forces.'),
]

FLASH = [
    ['Subshell capacities', 's 2, p 6, d 10.'],
    ['Periodic trend across a period', 'Radius ↓, ionisation energy ↑, electronegativity ↑.'],
    ['Ionic bond', 'Electron transfer, metal to non-metal; ions in a lattice.'],
    ['Polar covalent bond', 'Unequal sharing due to electronegativity difference.'],
    ['VSEPR', 'Electron pairs arrange as far apart as possible.'],
    ['Water\'s shape', 'Bent, about 104.5°, polar.'],
    ['Hydrogen bonding', 'H on N, O or F attracted to a lone pair on N, O or F.'],
    ['Like dissolves like', 'Polar dissolves polar; non-polar dissolves non-polar.'],
]
