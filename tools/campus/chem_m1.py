"""General Chemistry, module 1: Atoms, moles and stoichiometry."""
from verify import Q
from chem_common import M, NA, r
T1, T2, T3, T4 = ('Atomic structure and isotopes', 'The mole and molar mass', 'Balanced equations and stoichiometry', 'Solutions and concentration')

h2o, co2, nacl, glu, ch4, caco3 = M({'H': 2, 'O': 1}), M({'C': 1, 'O': 2}), M({'Na': 1, 'Cl': 1}), M({'C': 6, 'H': 12, 'O': 6}), M({'C': 1, 'H': 4}), M({'Ca': 1, 'C': 1, 'O': 3})
assert (r(h2o, 2), r(co2, 2), r(nacl, 2), r(glu, 2), r(ch4, 2), r(caco3, 2)) == (18.02, 44.01, 58.44, 180.16, 16.04, 100.09)
cl_avg = 34.97 * 0.7578 + 36.97 * 0.2422
assert r(cl_avg, 2) == 35.45
n_w = 36 / h2o
assert r(n_w, 2) == 2.00 and r(n_w * NA / 1e24, 2) == 1.20
co2_mass = 32 / ch4 * co2
assert r(co2_mass, 1) == 87.8
conc = 5.85 / nacl / 0.250
assert r(conc, 3) == 0.400
assert r(0.400 * 0.0500, 4) == 0.0200 and r(2.0 * 50 / 250, 2) == 0.40
# limiting reagent: 2H2 + O2 -> 2H2O with 4.0 g H2 and 16.0 g O2
nH2, nO2 = 4.0 / M({'H': 2}), 16.0 / M({'O': 2})
assert nO2 < nH2 / 2 and r(2 * nO2 * h2o, 1) == 18.0
assert r(15.0 / 18.0 * 100, 1) == 83.3

MODULE = {
    'title': 'Atoms, moles and stoichiometry',
    'topics': [T1, T2, T3, T4],
    'overview': 'Chemistry is the study of matter and how it changes. This module starts with the structure of atoms, then introduces the mole, the chemist\'s way of counting particles by weighing them, and uses balanced equations to predict how much product a reaction makes. It ends with solutions and concentration, used in every laboratory.',
    'key_terms': ['Proton', 'Neutron', 'Electron', 'Isotope', 'Relative atomic mass', 'Mole', 'Avogadro constant', 'Molar mass', 'Limiting reagent', 'Concentration'],
    'explanation': [
        'Atoms contain a tiny nucleus of protons and neutrons surrounded by electrons. The number of protons (atomic number) defines the element; isotopes of an element differ in their number of neutrons. The relative atomic mass on the periodic table is a weighted average of the isotope masses.',
        'Because atoms are so small, chemists count them in moles: one mole is 6.022 × 10²³ particles. The molar mass in grams per mole equals the relative formula mass, so n = m ÷ M converts between mass and amount.',
        'A balanced equation gives the mole ratio in which substances react. With it you can calculate the mass of product from a given mass of reactant, find which reactant runs out first (the limiting reagent) and compare the actual yield with the theoretical yield.'],
    'quick_facts': [
        'Atomic number Z = protons; mass number A = protons + neutrons.',
        'n = m ÷ M; number of particles = n × 6.022 × 10²³.',
        'Mole ratios come from the balanced equation.',
        'Concentration c = n ÷ V (V in dm³ or L).',
        'Dilution: c₁V₁ = c₂V₂.'],
}

NOTES = {
    T1: {
        'overview': 'Atoms are made of protons, neutrons and electrons. The number of protons defines the element, and isotopes are atoms of the same element with different numbers of neutrons.',
        'key_terms': ['Nucleus', 'Proton', 'Neutron', 'Electron', 'Atomic number', 'Mass number', 'Isotope', 'Relative atomic mass'],
        'explanation': [
            'Protons (charge +1, mass about 1 u) and neutrons (no charge, mass about 1 u) form the nucleus; electrons (charge −1, mass about 1/1836 u) occupy the space around it. A neutral atom has equal numbers of protons and electrons; ions have gained or lost electrons.',
            'The atomic number Z is the number of protons; the mass number A is protons + neutrons. Written as a symbol with A above and Z below, ³⁵Cl has 17 protons, 18 neutrons and 17 electrons. Isotopes have the same Z but different A, and they have the same chemical properties because chemistry depends on electrons.',
            'The relative atomic mass is the weighted average of the isotope masses using their natural abundances. Chlorine is about 75.8% chlorine-35 (mass 34.97) and 24.2% chlorine-37 (mass 36.97), giving 35.45. Mass spectrometry measures these abundances.'],
        'formulas_label': 'Formulas',
        'formulas': ['Z = number of protons', 'A = protons + neutrons', 'Neutrons = A − Z', 'Ar = Σ(isotope mass × fractional abundance)'],
        'steps': ['Read Z and A from the symbol.', 'Neutrons = A − Z; electrons = Z − charge.', 'For an average mass, multiply each isotope mass by its abundance and add.', 'Check the answer lies between the isotope masses.'],
        'worked_example': {
            'problem': 'Chlorine is 75.78% ³⁵Cl (34.97 u) and 24.22% ³⁷Cl (36.97 u). Calculate its relative atomic mass.',
            'steps': ['Contribution of ³⁵Cl = 34.97 × 0.7578 = 26.50.', 'Contribution of ³⁷Cl = 36.97 × 0.2422 = 8.95.', 'Sum = 35.45.'],
            'answer': 'Relative atomic mass of chlorine = 35.45.',
            'check': 'The answer is closer to 35 than 37 because chlorine-35 is more abundant ✓.'},
        'mistakes': ['Confusing mass number with relative atomic mass.', 'Forgetting to adjust electrons for an ion\'s charge.', 'Using percentages without converting to fractions.', 'Thinking isotopes have different chemical properties.'],
        'real_world': 'Carbon-14 dating and medical scans with radioactive isotopes such as technetium-99m rely on isotopes behaving chemically like the normal element while being detectable.',
        'exam_strategy': 'Lay out particle counts in a small table (protons, neutrons, electrons) for each species. Ions are where most marks are lost.',
        'recap': ['Z = protons; A = protons + neutrons.', 'Isotopes differ in neutrons.', 'Ar is a weighted average.', 'Ions: adjust electrons.']},
    T2: {
        'overview': 'The mole lets chemists count particles by weighing them. One mole contains 6.022 × 10²³ particles, and its mass in grams equals the substance\'s relative formula mass.',
        'key_terms': ['Mole', 'Avogadro constant', 'Molar mass', 'Relative formula mass', 'Empirical formula', 'Molecular formula'],
        'explanation': [
            'The molar mass M (g/mol) is found by adding relative atomic masses: H₂O = 2(1.008) + 16.00 = 18.02 g/mol. The amount in moles is n = m ÷ M, and the number of particles is n × 6.022 × 10²³.',
            'An empirical formula gives the simplest whole-number ratio of atoms. From percentage composition: divide each mass by the atomic mass to get moles, then divide by the smallest to get the ratio. The molecular formula is a whole-number multiple of the empirical formula, found from the molar mass.',
            'Percentage by mass of an element = (mass of that element in one mole ÷ molar mass) × 100. These calculations are the basis of fertiliser labels, drug doses and food analysis.'],
        'formulas_label': 'Formulas',
        'formulas': ['n = m ÷ M', 'N = n × 6.022 × 10²³', 'M = sum of atomic masses in the formula', '% by mass = (mass of element in formula ÷ M) × 100'],
        'steps': ['Calculate M from the formula.', 'Convert mass to moles with n = m ÷ M.', 'Convert moles to particles if needed.', 'Keep sensible significant figures.'],
        'worked_example': {
            'problem': 'How many moles and how many molecules are in 36.0 g of water?',
            'steps': ['M(H₂O) = 2(1.008) + 16.00 = 18.02 g/mol.', 'n = 36.0 ÷ 18.02 = 2.00 mol.', 'N = 2.00 × 6.022 × 10²³ = 1.20 × 10²⁴ molecules.'],
            'answer': '2.00 mol, or 1.20 × 10²⁴ molecules.',
            'check': '36 g is twice the molar mass, so 2 moles makes sense ✓.'},
        'mistakes': ['Using the atomic number instead of the atomic mass.', 'Forgetting subscripts (H₂O has two H atoms).', 'Multiplying mass by molar mass instead of dividing.', 'Rounding molar masses too early.'],
        'real_world': 'Pharmacists convert doses between grams and moles; some drug strengths are labelled in millimoles so that patients get the right number of active molecules.',
        'exam_strategy': 'Write units at every step (g, g/mol, mol). Unit cancelling catches most errors in mole calculations.',
        'recap': ['1 mol = 6.022 × 10²³ particles.', 'n = m ÷ M.', 'Add atomic masses for M.', 'Empirical from mole ratios.']},
    T3: {
        'overview': 'A balanced equation shows the mole ratio in which substances react. Stoichiometry uses it to calculate masses of reactants and products, the limiting reagent and the percentage yield.',
        'key_terms': ['Balanced equation', 'Coefficient', 'Mole ratio', 'Limiting reagent', 'Excess reagent', 'Theoretical yield', 'Percentage yield'],
        'explanation': [
            'Balance an equation by adjusting coefficients (never subscripts) so that each element has the same number of atoms on both sides. CH₄ + 2O₂ → CO₂ + 2H₂O means 1 mole of methane reacts with 2 moles of oxygen.',
            'The standard route is mass → moles → mole ratio → moles → mass. From 32.0 g of methane: n(CH₄) = 32.0 ÷ 16.04 = 1.995 mol, which gives 1.995 mol of CO₂, or 1.995 × 44.01 = 87.8 g.',
            'When amounts of two reactants are given, the limiting reagent is the one that runs out first; it decides how much product forms. The theoretical yield is the maximum product; percentage yield = actual ÷ theoretical × 100, usually below 100% because of side reactions and losses.'],
        'formulas_label': 'Method',
        'formulas': ['mass → n = m ÷ M', 'moles of product = moles of reactant × (ratio from equation)', 'mass = n × M', '% yield = actual ÷ theoretical × 100'],
        'steps': ['Write and balance the equation.', 'Convert given masses to moles.', 'Find the limiting reagent if two amounts are given.', 'Use the mole ratio.', 'Convert back to mass; compute % yield if asked.'],
        'worked_example': {
            'problem': '4.0 g of hydrogen reacts with 16.0 g of oxygen: 2H₂ + O₂ → 2H₂O. Which is limiting, and what mass of water forms?',
            'steps': ['n(H₂) = 4.0 ÷ 2.016 = 1.98 mol; n(O₂) = 16.0 ÷ 32.00 = 0.500 mol.', '1.98 mol of H₂ would need 0.99 mol of O₂, but only 0.500 mol is present: oxygen is limiting.', 'n(H₂O) = 2 × 0.500 = 1.00 mol; mass = 1.00 × 18.02 = 18.0 g.'],
            'answer': 'Oxygen is limiting; 18.0 g of water forms.',
            'check': 'Mass is conserved: 16.0 g O₂ + 2.0 g of H₂ used = 18.0 g ✓ (2.0 g of H₂ is left over).'},
        'mistakes': ['Changing subscripts to balance an equation.', 'Using masses directly in the ratio instead of moles.', 'Choosing the reagent with the smaller mass as limiting.', 'Forgetting to multiply by the ratio.'],
        'real_world': 'Fertiliser and cement plants use stoichiometry to set raw-material quantities; adding excess of the cheaper reactant pushes the expensive one to react completely.',
        'exam_strategy': 'Lay out the calculation in a table under the equation with rows for mass, molar mass and moles. It makes the mole ratio step explicit and easy to mark.',
        'recap': ['Balance with coefficients.', 'Always go through moles.', 'Limiting reagent decides the yield.', '% yield = actual ÷ theoretical × 100.']},
    T4: {
        'overview': 'Most reactions in the laboratory and in living things happen in solution. Concentration measures how much solute is dissolved in a given volume.',
        'key_terms': ['Solute', 'Solvent', 'Solution', 'Concentration (molarity)', 'Standard solution', 'Dilution', 'Titration'],
        'explanation': [
            'Molar concentration c = n ÷ V, with V in litres (dm³), so the units are mol/L (mol dm⁻³). Dissolving 5.85 g of NaCl (0.100 mol) in water to make 250 mL gives c = 0.100 ÷ 0.250 = 0.400 mol/L.',
            'Rearranging, n = c × V gives the amount in a measured volume: 50.0 mL of 0.400 mol/L solution contains 0.0200 mol. Mass concentration in g/L = c × M.',
            'Diluting does not change the amount of solute, so c₁V₁ = c₂V₂. Taking 50 mL of 2.0 mol/L acid and making it up to 250 mL gives 0.40 mol/L. Titrations combine concentration and stoichiometry to find an unknown concentration.'],
        'formulas_label': 'Formulas',
        'formulas': ['c = n ÷ V (V in L)', 'n = c × V', 'Mass concentration (g/L) = c × M', 'Dilution: c₁V₁ = c₂V₂', '1 L = 1 dm³ = 1000 mL'],
        'steps': ['Convert volumes to litres.', 'Find moles of solute.', 'Use c = n ÷ V or n = c × V.', 'For dilutions, use c₁V₁ = c₂V₂.'],
        'worked_example': {
            'problem': '5.85 g of NaCl is dissolved to make 250 mL of solution. Find its concentration.',
            'steps': ['M(NaCl) = 22.99 + 35.45 = 58.44 g/mol.', 'n = 5.85 ÷ 58.44 = 0.100 mol.', 'c = 0.100 ÷ 0.250 = 0.400 mol/L.'],
            'answer': '0.400 mol/L.',
            'check': 'A quarter of a litre containing a tenth of a mole: 0.1 × 4 = 0.4 mol per litre ✓.'},
        'mistakes': ['Using mL instead of L in c = n ÷ V.', 'Adding the volume of water instead of using the final volume.', 'Forgetting that dilution keeps moles constant.', 'Confusing mol/L with g/L.'],
        'real_world': 'Oral rehydration salts, which save many lives from diarrhoeal disease, must be mixed at the right concentration; too concentrated a solution can be harmful.',
        'exam_strategy': 'Convert every volume to litres on the first line of your working; most concentration errors are factors of 1000.',
        'recap': ['c = n ÷ V in litres.', 'n = c × V.', 'c₁V₁ = c₂V₂.', 'Watch mL vs L.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'How many neutrons does ³⁷Cl (Z = 17) have?', ['20', '17', '37', '54'], 0, 'A − Z = 37 − 17.', ans=20),
    Q(T1, 'How many electrons does Mg²⁺ (Z = 12) have?', ['10', '12', '14', '2'], 0, 'A 2+ ion has lost 2 electrons.', ans=10),
    Q(T1, 'Isotopes of an element differ in their number of:', ['neutrons', 'protons', 'electrons in a neutral atom', 'chemical properties'], 0, 'Same Z, different A.'),
    Q(T1, 'Chlorine is 75.78% mass 34.97 and 24.22% mass 36.97. Its relative atomic mass, to 2 d.p., is:', ['35.45', '35.97', '36.00', '35.00'], 0, 'Weighted average.', ans=r(cl_avg, 2)),
    Q(T1, 'The atomic number of an element is its number of:', ['protons', 'neutrons', 'nucleons', 'electron shells'], 0, 'It defines the element.'),
    Q(T1, 'Which particle has a negative charge and a very small mass?', ['Electron', 'Proton', 'Neutron', 'Nucleus'], 0, 'About 1/1836 of a proton\'s mass.'),
    # T2
    Q(T2, 'The molar mass of CO₂ (C = 12.01, O = 16.00) is:', ['44.01 g/mol', '28.01 g/mol', '32.00 g/mol', '60.01 g/mol'], 0, '12.01 + 2 × 16.00.'),
    Q(T2, 'How many moles are in 36.0 g of water (M = 18.02 g/mol), to 2 d.p.?', ['2.00', '0.50', '648', '18.0'], 0, '36.0 ÷ 18.02.', ans=r(n_w, 2)),
    Q(T2, 'The molar mass of glucose, C₆H₁₂O₆, to 2 d.p., is:', ['180.16 g/mol', '29.02 g/mol', '96.06 g/mol', '342.30 g/mol'], 0, '6(12.01) + 12(1.008) + 6(16.00).'),
    Q(T2, 'How many molecules are in 0.500 mol of a substance?', ['3.011 × 10²³', '6.022 × 10²³', '1.204 × 10²⁴', '0.500'], 0, '0.500 × 6.022 × 10²³.'),
    Q(T2, 'A compound is 40.0% C, 6.7% H and 53.3% O by mass. Its empirical formula is:', ['CH₂O', 'CHO', 'C₂H₄O', 'CH₄O'], 0, 'Mole ratio 3.33 : 6.65 : 3.33 = 1 : 2 : 1.'),
    Q(T2, 'The percentage by mass of oxygen in water (M = 18.02), to 1 d.p., is:', ['88.8%', '11.2%', '50.0%', '66.7%'], 0, '16.00 ÷ 18.02 × 100.'),
    # T3
    Q(T3, 'Balance: CH₄ + __O₂ → CO₂ + __H₂O.', ['2 and 2', '1 and 2', '2 and 1', '3 and 2'], 0, 'C: 1 each side; H: 4 = 2 × 2; O: 4 = 2 + 2.'),
    Q(T3, 'What mass of CO₂ forms from burning 32.0 g of CH₄ (M = 16.04; CO₂ = 44.01), to 1 d.p.?', ['87.8 g', '44.0 g', '64.0 g', '32.0 g'], 0, '1.995 mol CH₄ → 1.995 mol CO₂ → 87.8 g.'),
    Q(T3, '4.0 g H₂ and 16.0 g O₂ react (2H₂ + O₂ → 2H₂O). The limiting reagent is:', ['oxygen', 'hydrogen', 'water', 'neither'], 0, '0.500 mol O₂ needs only 1.00 mol H₂, but 1.98 mol is present.'),
    Q(T3, 'In that reaction, the mass of water formed is:', ['18.0 g', '20.0 g', '36.0 g', '9.0 g'], 0, '1.00 mol × 18.02 g/mol.'),
    Q(T3, 'Theoretical yield 18.0 g, actual yield 15.0 g. Percentage yield, to 1 d.p.:', ['83.3%', '120.0%', '16.7%', '75.0%'], 0, '15.0 ÷ 18.0 × 100.'),
    Q(T3, 'To balance an equation you may change:', ['coefficients only', 'subscripts', 'both', 'neither'], 0, 'Changing subscripts changes the substance.'),
    # T4
    Q(T4, '5.85 g NaCl (M = 58.44) is made up to 250 mL. The concentration is:', ['0.400 mol/L', '0.100 mol/L', '23.4 mol/L', '0.0234 mol/L'], 0, '0.100 mol ÷ 0.250 L.'),
    Q(T4, 'How many moles are in 50.0 mL of 0.400 mol/L solution?', ['0.0200 mol', '20.0 mol', '0.125 mol', '8.00 mol'], 0, '0.400 × 0.0500.'),
    Q(T4, '50 mL of 2.0 mol/L acid is diluted to 250 mL. The new concentration is:', ['0.40 mol/L', '10 mol/L', '0.80 mol/L', '2.0 mol/L'], 0, 'c₂ = 2.0 × 50 ÷ 250.'),
    Q(T4, 'In a dilution, which stays the same?', ['The number of moles of solute', 'The concentration', 'The volume', 'The mass of water'], 0, 'Only water is added.'),
    Q(T4, 'A 0.100 mol/L NaCl solution has a mass concentration of about:', ['5.84 g/L', '0.584 g/L', '58.4 g/L', '0.100 g/L'], 0, '0.100 × 58.44.'),
    Q(T4, '1 dm³ is equal to:', ['1 L = 1000 mL', '100 mL', '10 L', '1 mL'], 0, 'A cube 10 cm on each side.'),
]

FLASH = [
    ['Atomic number Z', 'Number of protons; defines the element.'],
    ['Isotopes', 'Same protons, different neutrons.'],
    ['The mole', '6.022 × 10²³ particles; n = m ÷ M.'],
    ['Empirical formula', 'Simplest whole-number ratio of atoms.'],
    ['Stoichiometry route', 'Mass → moles → mole ratio → moles → mass.'],
    ['Limiting reagent', 'The reactant that runs out first; it sets the yield.'],
    ['Concentration', 'c = n ÷ V with V in litres.'],
    ['Dilution', 'c₁V₁ = c₂V₂.'],
]
