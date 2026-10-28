"""Electricity and Magnetism, module 2: Capacitance, current and DC circuits."""
import math
from verify import Q
T1, T2, T3, T4 = ('Capacitors and dielectrics', 'Current, resistance and power', 'DC circuits and Kirchhoff\'s rules', 'RC circuits')
e0 = 8.85e-12
r = lambda v, d: round(v, d)
assert r(e0 * 0.01 / 1e-3 * 1e12, 1) == 88.5 and r(10e-6 * 12 * 1e6, 6) == 120 and r(0.5 * 10e-6 * 12 ** 2 * 1e4, 6) == 7.2
assert r(1 / (1 / 2 + 1 / 3), 6) == 1.2 and 2 + 3 == 5
assert r(1.68e-8 * 10 / 1e-6, 4) == 0.168 and 12 / 4 == 3 and 12 * 3 == 36 and 30 / 10 == 3 and r(2 * 3 * 2.5, 6) == 15
assert 12 / (5.5 + 0.5) == 2 and 12 - 2 * 0.5 == 11 and r(1 / (1 / 3 + 1 / 6), 6) == 2 and 2 + 4 + 6 == 12
Rp = 6 * 12 / 18; assert Rp == 4 and 12 / (4 + Rp) == 1.5 and 1.5 * Rp == 6 and 6 / 6 == 1 and 6 / 12 == 0.5 and 9 * 2 / 3 == 6
tau = 10e3 * 100e-6; assert r(tau, 9) == 1
assert r(12 * (1 - math.exp(-1)), 2) == 7.59 and r(12 * math.exp(-2), 2) == 1.62 and r(tau * math.log(2), 3) == 0.693
assert r(12 / 10e3 * 1e3, 6) == 1.2 and r(0.5 * 100e-6 * 144 * 1e3, 6) == 7.2 and r(1 - math.exp(-5), 3) == 0.993 and r(1 - math.exp(-1), 3) == 0.632

MODULE = {
    'title': 'Capacitance, current and DC circuits',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module moves from static charge to circuits: capacitors that store charge and energy, current and resistance (Ohm\'s law and electrical power), Kirchhoff\'s rules for analysing networks, and RC circuits whose voltages rise and fall exponentially.',
    'key_terms': ['Capacitance', 'Farad', 'Dielectric', 'Current', 'Ampere', 'Resistance', 'Resistivity', 'Ohm\'s law', 'Power', 'EMF', 'Internal resistance', 'Series', 'Parallel', 'Kirchhoff\'s rules', 'Time constant'],
    'explanation': [
        'A capacitor stores charge Q = CV. For parallel plates C = ε₀A/d, and the stored energy is ½CV². Capacitors in parallel add; in series their reciprocals add.',
        'Current is the rate of flow of charge, I = Q/t. Ohm\'s law V = IR links voltage and current; resistance depends on the material: R = ρL/A. Power P = VI = I²R = V²/R, and energy bought from the utility is measured in kilowatt-hours.',
        'Kirchhoff\'s junction rule (charge conservation) and loop rule (energy conservation) solve any DC network. An RC circuit charges or discharges with time constant τ = RC: after one τ a charging capacitor reaches about 63% of its final voltage.'],
    'quick_facts': [
        'Q = CV; C = κε₀A/d; U = ½CV².',
        'Capacitors: parallel C₁ + C₂; series 1/C = 1/C₁ + 1/C₂.',
        'V = IR; R = ρL/A; P = VI = I²R = V²/R.',
        'Resistors: series R₁ + R₂; parallel 1/R = 1/R₁ + 1/R₂.',
        'RC: τ = RC; charging V = V₀(1 − e^(−t/τ)); discharging V = V₀e^(−t/τ).'],
}

NOTES = {
    T1: {
        'overview': 'A capacitor is two conductors separated by an insulator. It stores charge and energy in its electric field.',
        'key_terms': ['Capacitance', 'Farad', 'Parallel-plate capacitor', 'Dielectric constant', 'Stored energy', 'Series and parallel capacitors'],
        'explanation': [
            'Capacitance C = Q/V, in farads (F). For parallel plates C = ε₀A/d: plates of area 0.01 m² 1 mm apart give C = 8.85 × 10⁻¹² × 0.01/0.001 = 8.85 × 10⁻¹¹ F = 88.5 pF. Real capacitors reach μF or more by using huge areas and thin insulators.',
            'A 10 μF capacitor charged to 12 V holds Q = CV = 120 μC and stores U = ½CV² = 7.2 × 10⁻⁴ J. Filling the gap with a dielectric of constant κ multiplies C by κ.',
            'In parallel, capacitors share the same voltage and capacitances add (2 μF and 3 μF give 5 μF). In series, they carry the same charge and 1/C = 1/C₁ + 1/C₂ (2 μF and 3 μF give 1.2 μF), smaller than either.'],
        'formulas_label': 'Formulas',
        'formulas': ['C = Q/V', 'C = κε₀A/d', 'U = ½CV² = Q²/(2C)', 'Parallel: C = C₁ + C₂', 'Series: 1/C = 1/C₁ + 1/C₂'],
        'steps': ['Convert μF, nF and pF to farads.', 'Combine capacitors step by step.', 'Use Q = CV for charge.', 'Use ½CV² for energy.'],
        'worked_example': {
            'problem': 'A 10 μF capacitor is connected to a 12 V battery. Find its charge and stored energy.',
            'steps': ['Q = CV = 10 × 10⁻⁶ × 12 = 1.2 × 10⁻⁴ C = 120 μC.', 'U = ½CV² = 0.5 × 10 × 10⁻⁶ × 144.', 'U = 7.2 × 10⁻⁴ J.'],
            'answer': '120 μC and 7.2 × 10⁻⁴ J.',
            'check': 'U = ½QV = 0.5 × 1.2 × 10⁻⁴ × 12 = 7.2 × 10⁻⁴ J ✓.'},
        'mistakes': ['Combining capacitors with the resistor rules (they are the other way round).', 'Forgetting the ½ in the energy.', 'Not converting μF.', 'Thinking a dielectric reduces capacitance.'],
        'real_world': 'A camera flash charges a capacitor slowly from a small battery, then dumps its energy into the flash tube in a millisecond.',
        'exam_strategy': 'Remember "capacitors are opposite to resistors" for series and parallel rules.',
        'recap': ['Q = CV.', 'C = κε₀A/d.', 'U = ½CV².', 'Parallel adds.']},
    T2: {
        'overview': 'Current is moving charge. Resistance limits it, and power measures how fast electrical energy is converted.',
        'key_terms': ['Current', 'Ampere', 'Ohm\'s law', 'Resistance', 'Resistivity', 'Ohmic conductor', 'Power', 'Kilowatt-hour'],
        'explanation': [
            'I = Q/t: 30 C passing in 10 s is 3 A. Conventional current flows from + to −, opposite to the electrons\' motion.',
            'Ohm\'s law V = IR: 12 V across 4 Ω drives 3 A. Resistance R = ρL/A: 10 m of copper wire (ρ = 1.68 × 10⁻⁸ Ω·m) with a 1 mm² cross-section has R = 0.168 Ω. Longer and thinner wires resist more.',
            'Power P = VI = I²R = V²/R; the 12 V, 3 A example dissipates 36 W. Utilities bill energy in kWh: a 2 kW heater used for 3 hours uses 6 kWh, which costs R15 at R2.50 per kWh.'],
        'formulas_label': 'Formulas',
        'formulas': ['I = Q/t', 'V = IR', 'R = ρL/A', 'P = VI = I²R = V²/R', 'Energy = Pt (kWh = kW × h)'],
        'steps': ['Identify the known quantities.', 'Pick the formula that links them.', 'Keep units in SI (or kW and h for bills).', 'Check the answer is sensible.'],
        'worked_example': {
            'problem': 'A 2 kW kettle-style heater runs for 3 hours. Electricity costs R2.50 per kWh. Find the cost.',
            'steps': ['Energy = 2 kW × 3 h = 6 kWh.', 'Cost = 6 × R2.50.', 'Cost = R15.'],
            'answer': 'R15.',
            'check': 'In joules: 2000 × 10 800 s = 2.16 × 10⁷ J = 6 kWh ✓ (1 kWh = 3.6 × 10⁶ J).'},
        'mistakes': ['Using watts and seconds for a bill in kWh.', 'Thinking current is used up in a resistor.', 'Confusing resistivity (material) with resistance (object).', 'Forgetting to convert mm² to m².'],
        'real_world': 'Thick cables are used for stoves and geysers because a lower resistance wastes less power as heat (I²R).',
        'exam_strategy': 'Choose the power formula that uses the quantities you are given rather than computing an extra step.',
        'recap': ['I = Q/t.', 'V = IR.', 'R = ρL/A.', 'P = VI.']},
    T3: {
        'overview': 'Real circuits combine resistors and sources. Series and parallel rules handle simple ones; Kirchhoff\'s rules handle any network.',
        'key_terms': ['Series', 'Parallel', 'Equivalent resistance', 'EMF', 'Internal resistance', 'Terminal voltage', 'Junction rule', 'Loop rule', 'Voltage divider'],
        'explanation': [
            'Series resistors add: 2 + 4 + 6 = 12 Ω. In parallel, 1/R = 1/R₁ + 1/R₂: 3 Ω and 6 Ω give 2 Ω, less than the smallest. A voltage divider splits voltage in proportion to resistance: 9 V across 1 kΩ and 2 kΩ in series puts 6 V across the 2 kΩ.',
            'A real battery has an EMF ε and internal resistance r: I = ε/(R + r). A 12 V battery with r = 0.5 Ω driving 5.5 Ω gives I = 2 A and terminal voltage 12 − 2 × 0.5 = 11 V.',
            'Kirchhoff\'s junction rule: currents into a junction equal currents out. Loop rule: the voltage changes around any closed loop sum to zero. Example: 12 V feeding 4 Ω in series with 6 Ω ∥ 12 Ω (= 4 Ω) gives 1.5 A in total; 6 V across the pair splits into 1 A and 0.5 A, which add back to 1.5 A.'],
        'formulas_label': 'Formulas',
        'formulas': ['Series: R = R₁ + R₂ + …', 'Parallel: 1/R = 1/R₁ + 1/R₂ + …', 'I = ε/(R + r)', 'V_terminal = ε − Ir', 'ΣI_in = ΣI_out; ΣΔV = 0 round a loop'],
        'steps': ['Reduce series and parallel groups.', 'Find the total current.', 'Work back to find each branch voltage and current.', 'For non-reducible networks, write junction and loop equations and solve.'],
        'worked_example': {
            'problem': 'A 12 V source drives 4 Ω in series with 6 Ω and 12 Ω in parallel. Find the current in each resistor.',
            'steps': ['6 ∥ 12 = 72/18 = 4 Ω; total 8 Ω.', 'I = 12/8 = 1.5 A through the 4 Ω.', 'Voltage across the pair = 1.5 × 4 = 6 V; 6 Ω carries 1 A, 12 Ω carries 0.5 A.'],
            'answer': '1.5 A, 1 A and 0.5 A.',
            'check': 'Junction: 1 + 0.5 = 1.5 ✓; loop: 6 + 6 = 12 V ✓.'},
        'mistakes': ['Adding parallel resistances directly.', 'Forgetting internal resistance.', 'Sign errors going round a loop.', 'Assuming parallel branches carry equal current.'],
        'real_world': 'House wiring is parallel so each appliance gets the full mains voltage and can be switched separately.',
        'exam_strategy': 'Always check your currents at a junction and voltages round a loop; it catches most errors.',
        'recap': ['Series add.', 'Parallel reciprocal.', 'Internal resistance.', 'Kirchhoff checks.']},
    T4: {
        'overview': 'When a capacitor charges or discharges through a resistor, voltages and currents change exponentially with time constant τ = RC.',
        'key_terms': ['Time constant', 'Charging', 'Discharging', 'Exponential decay', 'Half-life', 'Initial current'],
        'explanation': [
            'τ = RC: 10 kΩ with 100 μF gives τ = 1 s. When charging from a 12 V supply, V = 12(1 − e^(−t/τ)); after one τ it reaches 63.2%, about 7.59 V, and after 5τ it is above 99%.',
            'At the instant of switching on, the uncharged capacitor acts like a wire, so the initial current is V/R = 12/10 000 = 1.2 mA. The current then decays as I₀e^(−t/τ).',
            'Discharging, V = V₀e^(−t/τ): after 2τ, 12 V falls to 12e⁻² ≈ 1.62 V. The voltage halves every τ ln 2 ≈ 0.693τ. When full, the capacitor stores ½CV² = 7.2 mJ.'],
        'formulas_label': 'Formulas',
        'formulas': ['τ = RC', 'Charging: V = V₀(1 − e^(−t/τ))', 'Discharging: V = V₀e^(−t/τ)', 'I = I₀e^(−t/τ), I₀ = V₀/R', 't½ = τ ln 2'],
        'steps': ['Compute τ = RC.', 'Choose the charging or discharging formula.', 'Substitute t/τ.', 'Use ln to solve for a time.'],
        'worked_example': {
            'problem': 'A 100 μF capacitor charges through 10 kΩ from 12 V. Find its voltage after 1 s.',
            'steps': ['τ = 10⁴ × 10⁻⁴ = 1 s.', 'V = 12(1 − e⁻¹) = 12 × 0.632.', 'V ≈ 7.59 V.'],
            'answer': 'About 7.59 V.',
            'check': 'Between 0 and 12 V, and 63% of the way after one time constant ✓.'},
        'mistakes': ['Using the discharge formula for charging.', 'Forgetting τ has units of seconds (Ω × F = s).', 'Thinking the capacitor ever reaches 100% exactly.', 'Not converting μF and kΩ.'],
        'real_world': 'Windscreen-wiper delays and many timer circuits set their interval with an RC time constant.',
        'exam_strategy': 'Learn the landmarks: 63% at τ, 37% remaining at τ, about 99% after 5τ.',
        'recap': ['τ = RC.', '63% at one τ.', 'Exponential decay.', 'I₀ = V/R.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Parallel plates of area 0.01 m² separated by 1 mm have capacitance about:', ['88.5 pF', '8.85 pF', '885 pF', '8.85 μF'], 0, 'ε₀A/d.', ans=88.5, num=True),
    Q(T1, 'A 10 μF capacitor at 12 V holds charge:', ['120 μC', '1.2 μC', '0.83 μC', '1200 μC'], 0, 'Q = CV.', ans=120, num=True),
    Q(T1, 'The energy it stores is:', ['7.2 × 10⁻⁴ J', '1.44 × 10⁻³ J', '6.0 × 10⁻⁵ J', '7.2 × 10⁻² J'], 0, '½CV².'),
    Q(T1, '2 μF and 3 μF in series give:', ['1.2 μF', '5 μF', '6 μF', '0.83 μF'], 0, 'Reciprocals add.', ans=1.2, num=True),
    Q(T1, '2 μF and 3 μF in parallel give:', ['5 μF', '1.2 μF', '6 μF', '2.5 μF'], 0, 'Add.', ans=5, num=True),
    Q(T1, 'Inserting a dielectric with κ = 3 into a capacitor:', ['triples its capacitance', 'divides it by 3', 'leaves it unchanged', 'makes it zero'], 0, 'C = κε₀A/d.'),
    # T2
    Q(T2, '30 C passes a point in 10 s. The current is:', ['3 A', '300 A', '0.33 A', '40 A'], 0, 'Q/t.', ans=3, num=True),
    Q(T2, '10 m of copper wire with 1 mm² cross-section (ρ = 1.68 × 10⁻⁸ Ω·m) has resistance:', ['0.168 Ω', '16.8 Ω', '1.68 × 10⁻⁷ Ω', '0.0168 Ω'], 0, 'ρL/A.', ans=0.168, num=True),
    Q(T2, '12 V across 4 Ω drives a current of:', ['3 A', '48 A', '0.33 A', '8 A'], 0, 'V/R.', ans=3, num=True),
    Q(T2, 'The power dissipated is:', ['36 W', '48 W', '12 W', '3 W'], 0, 'VI.', ans=36, num=True),
    Q(T2, 'A 2 kW heater used for 3 h at R2.50 per kWh costs:', ['R15', 'R6', 'R7.50', 'R150'], 0, '6 kWh × R2.50.'),
    Q(T2, 'Doubling the length of a wire (same material and thickness) makes its resistance:', ['double', 'half', 'four times', 'unchanged'], 0, 'R ∝ L.'),
    # T3
    Q(T3, '3 Ω and 6 Ω in parallel give:', ['2 Ω', '9 Ω', '4.5 Ω', '18 Ω'], 0, 'Product over sum.', ans=2, num=True),
    Q(T3, 'A 12 V battery with r = 0.5 Ω drives 5.5 Ω. The current is:', ['2 A', '2.18 A', '24 A', '1.5 A'], 0, 'ε/(R + r).', ans=2, num=True),
    Q(T3, 'Its terminal voltage is:', ['11 V', '12 V', '1 V', '10 V'], 0, 'ε − Ir.', ans=11, num=True),
    Q(T3, '9 V across 1 kΩ and 2 kΩ in series puts across the 2 kΩ:', ['6 V', '3 V', '4.5 V', '9 V'], 0, 'Divider.', ans=6, num=True),
    Q(T3, 'Kirchhoff\'s junction rule expresses conservation of:', ['charge', 'energy', 'momentum', 'power'], 0, 'Current in = out.'),
    Q(T3, '12 V feeds 4 Ω in series with 6 Ω ∥ 12 Ω. The current in the 12 Ω resistor is:', ['0.5 A', '1 A', '1.5 A', '0.25 A'], 0, '6 V/12 Ω.', ans=0.5, num=True),
    # T4
    Q(T4, 'The time constant of 10 kΩ and 100 μF is:', ['1 s', '0.1 s', '10 s', '100 s'], 0, 'RC.', ans=1, num=True),
    Q(T4, 'After one time constant a charging capacitor (12 V supply) reaches about:', ['7.59 V', '4.41 V', '6 V', '12 V'], 0, '63.2%.', ans=7.59, num=True),
    Q(T4, 'A capacitor discharging from 12 V has after 2τ about:', ['1.62 V', '4.41 V', '3 V', '0.6 V'], 0, '12e⁻².', ans=1.62, num=True),
    Q(T4, 'The initial charging current through 10 kΩ from 12 V is:', ['1.2 mA', '12 mA', '0.12 mA', '120 mA'], 0, 'V/R.', ans=1.2, num=True),
    Q(T4, 'The voltage of a discharging capacitor halves every:', ['0.693τ', 'τ', '2τ', '0.5τ'], 0, 'τ ln 2.'),
    Q(T4, 'After 5 time constants a charging capacitor is about:', ['99% charged', '63% charged', '50% charged', '86% charged'], 0, '1 − e⁻⁵ ≈ 0.993.'),
]

FLASH = [
    ['Capacitance', 'C = Q/V; parallel plates C = κε₀A/d.'],
    ['Capacitor energy', 'U = ½CV².'],
    ['Capacitor combinations', 'Parallel add; series reciprocals add.'],
    ['Ohm\'s law', 'V = IR.'],
    ['Resistivity', 'R = ρL/A.'],
    ['Electrical power', 'P = VI = I²R = V²/R.'],
    ['Kirchhoff\'s rules', 'Junction: currents balance; loop: voltages sum to zero.'],
    ['RC time constant', 'τ = RC; 63% charged after τ.'],
]
