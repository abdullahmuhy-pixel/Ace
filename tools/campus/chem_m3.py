"""General Chemistry, module 3: Gases and thermochemistry."""
from verify import Q
from chem_common import R, r
T1, T2, T3, T4 = ('The gas laws', 'The ideal gas equation', 'Enthalpy changes and Hess\'s law', 'Calorimetry and bond enthalpies')

assert 100 * 2.0 / 50 == 4.0 and 3.0 * 400 / 300 == 4.0
v_stp = 0.500 * R * 273.15 / 101.325
assert r(v_stp, 1) == 11.2 and r(R * 273.15 / 101.325, 1) == 22.4 and r(R * 298.15 / 100, 1) == 24.8
n_gas = 150 * 2.00 / (R * 300)
assert r(n_gas, 3) == 0.120
comb = -393.5 + 2 * -285.8 - (-74.8)
assert r(comb, 1) == -890.3
q = 100 * 4.18 * 15
assert q == 6270 and r(-q / 1000 / 0.0200, 1) == -313.5
assert 436 + 243 - 2 * 432 == -185
assert 100 * 0.78 == 78 and r(0.21 * 101.3, 1) == 21.3

MODULE = {
    'title': 'Gases and thermochemistry',
    'topics': [T1, T2, T3, T4],
    'overview': 'Gases follow simple laws linking pressure, volume, temperature and amount, which makes them the easiest state of matter to describe mathematically. Chemical reactions also transfer energy. This module covers the gas laws and the ideal gas equation, then enthalpy changes, Hess\'s law, calorimetry and bond enthalpies.',
    'key_terms': ['Pressure', 'Kelvin', 'Boyle\'s law', 'Charles\'s law', 'Ideal gas equation', 'Molar volume', 'Enthalpy change', 'Exothermic', 'Endothermic', 'Hess\'s law', 'Specific heat capacity', 'Bond enthalpy'],
    'explanation': [
        'For a fixed amount of gas, pressure and volume are inversely related (Boyle), volume is proportional to absolute temperature (Charles), and these combine into PV = nRT. Temperatures must always be in kelvin (K = °C + 273.15).',
        'Reactions either release heat to the surroundings (exothermic, ΔH negative) or absorb it (endothermic, ΔH positive). Enthalpy is a state function, so the overall enthalpy change does not depend on the route: Hess\'s law lets us calculate ΔH for reactions that are hard to measure directly.',
        'Calorimetry measures heat flow from temperature changes using q = mcΔT. Bond enthalpies estimate ΔH as the energy needed to break bonds minus the energy released forming new ones.'],
    'quick_facts': [
        'PV = nRT with R = 8.314 J mol⁻¹ K⁻¹ (P in Pa, V in m³; or P in kPa, V in L).',
        'Molar volume ≈ 22.4 L at 0 °C and 1 atm; ≈ 24.8 L at 25 °C and 100 kPa.',
        'Exothermic: ΔH < 0; endothermic: ΔH > 0.',
        'q = mcΔT; c(water) = 4.18 J g⁻¹ K⁻¹.',
        'ΔH ≈ Σ(bonds broken) − Σ(bonds formed).'],
}

NOTES = {
    T1: {
        'overview': 'The gas laws describe how the pressure, volume and temperature of a fixed amount of gas are related. They follow from gas particles moving rapidly and colliding with the container walls.',
        'key_terms': ['Pressure', 'Absolute temperature', 'Boyle\'s law', 'Charles\'s law', 'Gay-Lussac\'s law', 'Combined gas law', 'Dalton\'s law'],
        'explanation': [
            'Boyle\'s law: at constant temperature, P₁V₁ = P₂V₂. Halving the volume doubles the pressure, because particles hit the walls twice as often. Charles\'s law: at constant pressure, V₁/T₁ = V₂/T₂, with T in kelvin. Gay-Lussac\'s law: at constant volume, P₁/T₁ = P₂/T₂.',
            'These combine into P₁V₁/T₁ = P₂V₂/T₂. Temperatures must be absolute (kelvin), because at 0 °C a gas still has volume and pressure; only at 0 K would motion stop.',
            'Dalton\'s law of partial pressures: in a mixture, total pressure = sum of the partial pressures, and each partial pressure = mole fraction × total pressure. Air at 101.3 kPa is about 21% oxygen, so the oxygen partial pressure is about 21.3 kPa.'],
        'formulas_label': 'Formulas',
        'formulas': ['Boyle: P₁V₁ = P₂V₂ (constant T)', 'Charles: V₁/T₁ = V₂/T₂ (constant P)', 'Combined: P₁V₁/T₁ = P₂V₂/T₂', 'Dalton: P_total = ΣP_i; P_i = x_i × P_total', 'T(K) = T(°C) + 273.15'],
        'steps': ['List the initial and final conditions.', 'Convert temperatures to kelvin.', 'Choose the law for what is held constant.', 'Rearrange and solve.', 'Check the direction of change makes sense.'],
        'worked_example': {
            'problem': 'A gas occupies 3.0 L at 300 K. At constant pressure it is heated to 400 K. Find the new volume.',
            'steps': ['Charles\'s law: V₂ = V₁ × T₂/T₁.', 'V₂ = 3.0 × 400/300.', 'V₂ = 4.0 L.'],
            'answer': '4.0 L.',
            'check': 'Heating at constant pressure should expand the gas ✓.'},
        'mistakes': ['Using °C instead of K.', 'Applying Boyle\'s law when the temperature changes.', 'Inverting the ratio (V₂ = V₁ × T₁/T₂).', 'Forgetting that a mixture\'s total pressure is the sum of partial pressures.'],
        'real_world': 'Divers must breathe out while rising, because the air in their lungs expands as the water pressure falls (Boyle\'s law); holding the breath can damage the lungs.',
        'exam_strategy': 'Write all six quantities (P₁, V₁, T₁, P₂, V₂, T₂) in a list before substituting, and convert every temperature to kelvin first.',
        'recap': ['Boyle: P ∝ 1/V.', 'Charles: V ∝ T (kelvin).', 'Combined law.', 'Dalton: partial pressures add.']},
    T2: {
        'overview': 'The ideal gas equation PV = nRT links pressure, volume, temperature and the amount of gas. It describes most gases well at ordinary conditions.',
        'key_terms': ['Ideal gas', 'Gas constant R', 'Molar volume', 'STP', 'Kinetic theory', 'Real gases'],
        'explanation': [
            'PV = nRT, with R = 8.314 J mol⁻¹ K⁻¹. Units must match: with P in kPa and V in litres, R = 8.314 kPa L mol⁻¹ K⁻¹ works directly. With P in Pa, V must be in m³.',
            'The molar volume of any ideal gas is about 22.4 L at 0 °C and 1 atm (101.325 kPa), and about 24.8 L at 25 °C and 100 kPa. Because of this, equal volumes of gases at the same conditions contain equal numbers of molecules (Avogadro\'s law).',
            'The ideal gas model assumes particles have no volume and no attractions. Real gases deviate at high pressure (particle volume matters) and low temperature (attractions matter), which is why gases liquefy when cooled and compressed.'],
        'formulas_label': 'Formulas',
        'formulas': ['PV = nRT', 'R = 8.314 J mol⁻¹ K⁻¹ = 8.314 kPa L mol⁻¹ K⁻¹', 'n = PV/(RT)', 'Molar volume ≈ 22.4 L (0 °C, 1 atm); ≈ 24.8 L (25 °C, 100 kPa)', 'Density = PM/(RT)'],
        'steps': ['Convert units (kPa and L, or Pa and m³; T in K).', 'Rearrange PV = nRT for the unknown.', 'Substitute and calculate.', 'Check the size against the molar volume.'],
        'worked_example': {
            'problem': 'How many moles of gas are in a 2.00 L flask at 150 kPa and 300 K?',
            'steps': ['n = PV/(RT).', 'n = (150 × 2.00)/(8.314 × 300).', 'n = 300/2494.2 ≈ 0.120 mol.'],
            'answer': 'About 0.120 mol.',
            'check': 'At about 1.5 atm, 2 L holds roughly 1.5 × 2/24.6 ≈ 0.12 mol ✓.'},
        'mistakes': ['Mixing kPa with m³ or Pa with L.', 'Using °C instead of K.', 'Forgetting to convert mL to L.', 'Expecting ideal behaviour at very high pressure.'],
        'real_world': 'Car airbags inflate within milliseconds as a reaction produces nitrogen gas; engineers use PV = nRT to calculate how much reactant gives the right bag volume.',
        'exam_strategy': 'State the units you are using for R before substituting. Unit mismatch is the most common error in gas questions.',
        'recap': ['PV = nRT.', 'Match R to the units.', 'Molar volume ≈ 22.4 L or 24.8 L.', 'Real gases deviate at high P, low T.']},
    T3: {
        'overview': 'The enthalpy change ΔH measures the heat exchanged at constant pressure. Hess\'s law lets us combine known enthalpy changes to find unknown ones.',
        'key_terms': ['Enthalpy change', 'Exothermic', 'Endothermic', 'Standard enthalpy of formation', 'Standard enthalpy of combustion', 'Hess\'s law', 'State function'],
        'explanation': [
            'Exothermic reactions release heat (ΔH negative), such as combustion; endothermic reactions absorb heat (ΔH positive), such as dissolving ammonium nitrate. Standard values (ΔH°) refer to 100 kPa and usually 298 K.',
            'The standard enthalpy of formation ΔHf° is the change when one mole of a compound forms from its elements in their standard states; for an element in its standard state it is zero. Then ΔH°(reaction) = ΣΔHf°(products) − ΣΔHf°(reactants).',
            'Hess\'s law: because enthalpy is a state function, the total ΔH is the same whatever route is taken. Equations can be reversed (change the sign of ΔH) and multiplied (multiply ΔH) and added to give the target equation.'],
        'formulas_label': 'Formulas',
        'formulas': ['ΔH < 0 exothermic; ΔH > 0 endothermic', 'ΔH°rxn = ΣΔHf°(products) − ΣΔHf°(reactants)', 'Reverse an equation: change the sign of ΔH', 'ΔHf° of an element in its standard state = 0'],
        'steps': ['Write the target equation.', 'Find formation data (or given equations).', 'Apply products minus reactants, or combine equations.', 'Multiply by coefficients and watch signs.'],
        'worked_example': {
            'problem': 'Use ΔHf° values CO₂(g) −393.5, H₂O(l) −285.8 and CH₄(g) −74.8 kJ/mol to find ΔH for CH₄ + 2O₂ → CO₂ + 2H₂O(l).',
            'steps': ['Products: −393.5 + 2(−285.8) = −965.1 kJ.', 'Reactants: −74.8 + 2(0) = −74.8 kJ (O₂ is an element).', 'ΔH = −965.1 − (−74.8) = −890.3 kJ/mol.'],
            'answer': 'ΔH = −890.3 kJ/mol: strongly exothermic.',
            'check': 'Burning natural gas releases a lot of heat, as expected ✓.'},
        'mistakes': ['Reactants minus products instead of products minus reactants.', 'Forgetting the coefficients.', 'Giving O₂ a non-zero formation enthalpy.', 'Not changing the sign when reversing an equation.'],
        'real_world': 'Fuel energy contents on gas and paraffin labels come from combustion enthalpies; they let engineers compare fuels for cooking, heating and power stations.',
        'exam_strategy': 'Write "products − reactants" and a bracketed sum for each side with coefficients. Sign errors are where most marks are lost.',
        'recap': ['Exothermic ΔH < 0.', 'Products − reactants with ΔHf°.', 'Elements have ΔHf° = 0.', 'Hess: route does not matter.']},
    T4: {
        'overview': 'Calorimetry measures enthalpy changes in the laboratory from temperature changes. Bond enthalpies estimate them from the bonds broken and formed.',
        'key_terms': ['Calorimeter', 'Specific heat capacity', 'q = mcΔT', 'Bond enthalpy', 'Bonds broken', 'Bonds formed'],
        'explanation': [
            'Heat absorbed by water: q = mcΔT, where m is the mass of water, c = 4.18 J g⁻¹ K⁻¹ and ΔT is the temperature change. If the water warms, the reaction released heat, so ΔH for the reaction is negative: ΔH = −q ÷ n (per mole of the limiting reactant).',
            'Simple coffee-cup calorimeters lose heat to the surroundings, so measured values are usually smaller in size than data-book values. Insulation and a lid reduce the error.',
            'Bond enthalpy is the energy needed to break one mole of a bond in the gas phase. ΔH ≈ Σ(bonds broken) − Σ(bonds formed): breaking bonds costs energy, forming bonds releases it. For H₂ + Cl₂ → 2HCl: 436 + 243 − 2(432) = −185 kJ/mol. These are averages, so the answer is an estimate.'],
        'formulas_label': 'Formulas',
        'formulas': ['q = mcΔT', 'ΔH = −q ÷ n (if the solution warms)', 'ΔH ≈ Σ bonds broken − Σ bonds formed', 'c(water) = 4.18 J g⁻¹ K⁻¹'],
        'steps': ['Find the temperature change.', 'Calculate q = mcΔT (in J, then kJ).', 'Find moles of the limiting reactant.', 'ΔH = −q/n with the correct sign.', 'For bond enthalpies, list bonds broken and formed.'],
        'worked_example': {
            'problem': 'A reaction warms 100 g of water by 15.0 K. 0.0200 mol of the limiting reactant was used. Find ΔH.',
            'steps': ['q = 100 × 4.18 × 15.0 = 6270 J = 6.27 kJ.', 'The water warmed, so the reaction is exothermic.', 'ΔH = −6.27 ÷ 0.0200 = −313.5 kJ/mol.'],
            'answer': 'ΔH ≈ −314 kJ/mol.',
            'check': 'Heat losses mean the true value is probably slightly more negative.'},
        'mistakes': ['Forgetting the negative sign for an exothermic reaction.', 'Leaving q in J while dividing to get kJ/mol.', 'Using the mass of solid reactant instead of the water.', 'Doing bonds formed minus bonds broken.'],
        'real_world': 'Food energy values on nutrition labels were first measured by burning food in bomb calorimeters and measuring the heat released.',
        'exam_strategy': 'Show the sign reasoning in words ("temperature rose, so exothermic, so ΔH is negative"). Many marks are lost on the sign alone.',
        'recap': ['q = mcΔT.', 'ΔH = −q/n for warming.', 'Broken − formed for bond enthalpies.', 'Bond enthalpies give estimates.']},
}

QUESTIONS = [
    # T1
    Q(T1, '2.0 L of gas at 100 kPa is allowed to expand at constant temperature until the pressure is 50 kPa. The new volume is:', ['4.0 L', '1.0 L', '2.0 L', '8.0 L'], 0, 'P₁V₁ = P₂V₂.'),
    Q(T1, '3.0 L of gas at 300 K is heated to 400 K at constant pressure. The new volume is:', ['4.0 L', '2.25 L', '3.0 L', '7.0 L'], 0, 'V₂ = 3.0 × 400/300.'),
    Q(T1, '25 °C in kelvin is about:', ['298 K', '248 K', '25 K', '273 K'], 0, '25 + 273.15.', ans=298),
    Q(T1, 'Air at 101.3 kPa is 21% oxygen. The partial pressure of oxygen, to 1 d.p., is:', ['21.3 kPa', '80.0 kPa', '101.3 kPa', '4.8 kPa'], 0, '0.21 × 101.3.'),
    Q(T1, 'At constant temperature, halving the volume of a gas:', ['doubles the pressure', 'halves the pressure', 'leaves pressure unchanged', 'doubles the temperature'], 0, 'Boyle\'s law.'),
    Q(T1, 'Why must gas-law temperatures be in kelvin?', ['Volume and pressure are proportional to absolute temperature', 'Kelvin numbers are larger', 'Celsius cannot be negative', 'It is a convention only'], 0, '0 °C is not zero motion.'),
    # T2
    Q(T2, 'How many moles are in 2.00 L of gas at 150 kPa and 300 K (R = 8.314), to 3 d.p.?', ['0.120 mol', '1.20 mol', '0.0120 mol', '12.0 mol'], 0, 'n = PV/RT = 300/2494.'),
    Q(T2, 'The volume of 0.500 mol of an ideal gas at 0 °C and 101.325 kPa, to 1 d.p., is:', ['11.2 L', '22.4 L', '5.6 L', '24.8 L'], 0, 'Half of 22.4 L.'),
    Q(T2, 'The molar volume at 25 °C and 100 kPa is about:', ['24.8 L', '22.4 L', '8.3 L', '1.0 L'], 0, '8.314 × 298.15/100.'),
    Q(T2, 'Real gases behave least ideally at:', ['high pressure and low temperature', 'low pressure and high temperature', 'room conditions', 'any temperature above 0 °C'], 0, 'Particle volume and attractions matter.'),
    Q(T2, 'Equal volumes of different gases at the same temperature and pressure contain:', ['equal numbers of molecules', 'equal masses', 'equal densities', 'different numbers of molecules'], 0, 'Avogadro\'s law.'),
    Q(T2, 'In PV = nRT with P in kPa and V in L, R equals:', ['8.314 kPa L mol⁻¹ K⁻¹', '0.08206 kPa L mol⁻¹ K⁻¹', '8314 kPa L mol⁻¹ K⁻¹', '1'], 0, '1 kPa L = 1 J.'),
    # T3
    Q(T3, 'Using ΔHf°: CO₂ −393.5, H₂O(l) −285.8, CH₄ −74.8 kJ/mol, ΔH for CH₄ + 2O₂ → CO₂ + 2H₂O is:', ['−890.3 kJ/mol', '−604.5 kJ/mol', '−754.1 kJ/mol', '+890.3 kJ/mol'], 0, '(−393.5 − 571.6) − (−74.8).'),
    Q(T3, 'An exothermic reaction has:', ['ΔH < 0', 'ΔH > 0', 'ΔH = 0', 'no heat change'], 0, 'Heat flows out to the surroundings.'),
    Q(T3, 'The standard enthalpy of formation of O₂(g) is:', ['0', '−393.5 kJ/mol', '+249 kJ/mol', '−285.8 kJ/mol'], 0, 'Elements in their standard state are zero.'),
    Q(T3, 'If A → B has ΔH = −50 kJ, then B → A has ΔH =', ['+50 kJ', '−50 kJ', '0', '−100 kJ'], 0, 'Reversing changes the sign.'),
    Q(T3, 'Hess\'s law works because enthalpy is a:', ['state function', 'path function', 'rate', 'concentration'], 0, 'It depends only on the start and end states.'),
    Q(T3, 'Dissolving ammonium nitrate in water makes the water colder. The process is:', ['endothermic', 'exothermic', 'neither', 'a combustion'], 0, 'It absorbs heat from the water.'),
    # T4
    Q(T4, 'A reaction warms 100 g of water by 15.0 K (c = 4.18). The heat absorbed by the water is:', ['6270 J', '627 J', '62.7 J', '1500 J'], 0, '100 × 4.18 × 15.0.', ans=6270),
    Q(T4, 'If 0.0200 mol reacted to release that heat, ΔH (kJ/mol, to 1 d.p.) is:', ['−313.5', '+313.5', '−6.3', '−125.4'], 0, '−6.27 ÷ 0.0200.', ans=-313.5),
    Q(T4, 'Bond enthalpies H–H 436, Cl–Cl 243, H–Cl 432 kJ/mol. ΔH for H₂ + Cl₂ → 2HCl is:', ['−185 kJ/mol', '+185 kJ/mol', '−247 kJ/mol', '+247 kJ/mol'], 0, '(436 + 243) − 2(432).'),
    Q(T4, 'Breaking chemical bonds:', ['absorbs energy', 'releases energy', 'has no energy change', 'always produces light'], 0, 'Energy is needed to separate bonded atoms.'),
    Q(T4, 'Measured enthalpy changes from a simple cup calorimeter are usually too small in size because:', ['heat is lost to the surroundings', 'water has no heat capacity', 'thermometers read too high', 'reactions are too fast'], 0, 'Insulation is imperfect.'),
    Q(T4, 'Estimates from average bond enthalpies are approximate because:', ['bond strengths vary between molecules', 'bonds never break', 'energy is not conserved', 'all bonds are equal'], 0, 'Data-book values are averages.'),
]

FLASH = [
    ['Boyle\'s law', 'P₁V₁ = P₂V₂ at constant temperature.'],
    ['Charles\'s law', 'V₁/T₁ = V₂/T₂ at constant pressure (kelvin).'],
    ['Ideal gas equation', 'PV = nRT; R = 8.314.'],
    ['Molar volume', '≈ 22.4 L at 0 °C, 1 atm; ≈ 24.8 L at 25 °C, 100 kPa.'],
    ['ΔH from formation data', 'ΣΔHf°(products) − ΣΔHf°(reactants).'],
    ['Hess\'s law', 'ΔH is independent of the route.'],
    ['Calorimetry', 'q = mcΔT; ΔH = −q/n if the water warms.'],
    ['Bond enthalpy method', 'ΔH ≈ bonds broken − bonds formed.'],
]
