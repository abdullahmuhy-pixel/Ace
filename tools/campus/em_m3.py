"""Electricity and Magnetism, module 3: Magnetism."""
import math
from verify import Q
T1, T2, T3, T4 = ('Magnetic force on moving charges', 'Force on currents and motors', 'Biot–Savart and Ampère\'s law', 'Solenoids, toroids and magnetic materials')
e, mp, me, mu0 = 1.602e-19, 1.673e-27, 9.11e-31, 4e-7 * math.pi
r = lambda v, d: round(v, d)
assert r(e * 2e6 * 0.5 / 1e-13, 3) == 1.602 and r(mp * 2e6 / (e * 0.5), 4) == 0.0418 and r(me * 1e7 / (e * 1e-3), 4) == 0.0569
assert r(e * 1 / (2 * math.pi * mp) / 1e6, 1) == 15.2 and 1e4 / 0.02 == 5e5
assert r(0.4 * 5 * 0.2, 6) == 0.4 and r(0.4 * 5 * 0.2 * math.sin(math.radians(30)), 6) == 0.2 and r(100 * 0.2 * 2 * 0.01, 6) == 0.4
assert r(mu0 * 10 / (2 * math.pi * 0.05) * 1e6, 6) == 40 and r(mu0 * 5 / (2 * 0.1) * 1e5, 2) == 3.14
assert r(mu0 * 10 * 10 / (2 * math.pi * 0.1) * 1e4, 6) == 2 and r(mu0 * 500 / 0.25 * 3 * 1e3, 2) == 7.54 and r(mu0 * 500 * 3 / (2 * math.pi * 0.1) * 1e3, 6) == 3
assert r(mu0 * 10 / (2 * math.pi * 0.1) * 1e6, 6) == 20

MODULE = {
    'title': 'Magnetism',
    'topics': [T1, T2, T3, T4],
    'overview': 'Magnetic fields push on moving charges and currents, and currents create magnetic fields. This module covers the Lorentz force and circular orbits, forces and torques on wires (the basis of motors), the Biot–Savart and Ampère laws, and the fields of solenoids and toroids, plus how materials respond.',
    'key_terms': ['Magnetic field', 'Tesla', 'Lorentz force', 'Right-hand rule', 'Cyclotron motion', 'Velocity selector', 'Torque on a coil', 'Motor', 'Biot–Savart law', 'Ampère\'s law', 'Permeability of free space', 'Solenoid', 'Toroid', 'Ferromagnetism', 'Hall effect'],
    'explanation': [
        'A charge q moving with velocity v in a field B feels F = qvB sin θ, perpendicular to both v and B. This force does no work: it bends paths into circles of radius r = mv/(qB) but never changes speed.',
        'A current-carrying wire feels F = BIL sin θ, and a coil feels a torque τ = NBIA sin θ, which is how electric motors turn. Meters, loudspeakers and motors all use this force.',
        'Currents create fields. A long straight wire gives B = μ₀I/(2πr); a long solenoid gives a uniform B = μ₀nI inside. Ampère\'s law, ∮B·dl = μ₀I_enc, gives these quickly for symmetric cases, just as Gauss\'s law does for electric fields.'],
    'quick_facts': [
        'F = qvB sin θ; r = mv/(qB); f = qB/(2πm).',
        'Wire: F = BIL sin θ; coil torque τ = NBIA sin θ.',
        'Long wire: B = μ₀I/(2πr), μ₀ = 4π × 10⁻⁷ T·m/A.',
        'Parallel wires: F/L = μ₀I₁I₂/(2πd); same direction attract.',
        'Solenoid: B = μ₀nI; toroid B = μ₀NI/(2πr).'],
}

NOTES = {
    T1: {
        'overview': 'A magnetic field exerts a force on a moving charge perpendicular to its velocity, producing circular or helical paths.',
        'key_terms': ['Tesla', 'Lorentz force', 'Right-hand rule', 'Radius of orbit', 'Cyclotron frequency', 'Velocity selector', 'Mass spectrometer'],
        'explanation': [
            'F = qvB sin θ. A proton (1.602 × 10⁻¹⁹ C) at 2 × 10⁶ m/s perpendicular to 0.5 T feels F = 1.602 × 10⁻¹³ N. The direction comes from the right-hand rule for positive charges; reverse it for electrons. A charge moving parallel to B feels no force.',
            'Because the force is always perpendicular to v, it provides centripetal force: qvB = mv²/r, so r = mv/(qB). That proton circles with r = 1.673 × 10⁻²⁷ × 2 × 10⁶/(1.602 × 10⁻¹⁹ × 0.5) ≈ 4.18 cm. The frequency f = qB/(2πm) does not depend on speed: about 15.2 MHz for a proton in 1 T, which is the principle of the cyclotron.',
            'Crossed E and B fields let through only particles with v = E/B, since electric and magnetic forces then cancel. With E = 10⁴ V/m and B = 0.02 T, v = 5 × 10⁵ m/s. Followed by a magnetic field, this forms a mass spectrometer.'],
        'formulas_label': 'Formulas',
        'formulas': ['F = qvB sin θ', 'r = mv/(qB)', 'f = qB/(2πm), T = 2πm/(qB)', 'Velocity selector: v = E/B'],
        'steps': ['Find the component of v perpendicular to B.', 'Compute F = qvB.', 'Set qvB = mv²/r for orbits.', 'Use the right-hand rule (reversed for negative charges).'],
        'worked_example': {
            'problem': 'A proton moves at 2 × 10⁶ m/s perpendicular to a 0.5 T field. Find the radius of its path.',
            'steps': ['r = mv/(qB).', 'r = 1.673 × 10⁻²⁷ × 2 × 10⁶/(1.602 × 10⁻¹⁹ × 0.5).', 'r ≈ 0.0418 m.'],
            'answer': 'About 4.18 cm.',
            'check': 'Units: kg·m/s/(C·T) = m ✓; a faster proton would make a larger circle ✓.'},
        'mistakes': ['Thinking the magnetic force changes a charge\'s speed.', 'Forgetting to reverse the direction for electrons.', 'Using v parallel to B.', 'Thinking the period depends on speed.'],
        'real_world': 'Auroras form when charged particles from the Sun spiral along Earth\'s magnetic field lines into the upper atmosphere near the poles.',
        'exam_strategy': 'Write qvB = mv²/r explicitly; most orbit questions start there.',
        'recap': ['F ⊥ v and B.', 'No work done.', 'r = mv/(qB).', 'v = E/B selector.']},
    T2: {
        'overview': 'Since current is moving charge, a wire carrying current in a magnetic field feels a force. A coil feels a torque, which drives motors.',
        'key_terms': ['Force on a wire', 'Magnetic moment', 'Torque on a coil', 'DC motor', 'Commutator', 'Loudspeaker', 'Galvanometer'],
        'explanation': [
            'F = BIL sin θ. A 0.2 m wire carrying 5 A across a 0.4 T field feels 0.4 N; at 30° to the field it feels half that, 0.2 N. Fleming\'s left-hand rule (or the right-hand rule) gives the direction.',
            'A rectangular coil of N turns and area A feels a torque τ = NBIA sin θ, where θ is the angle between the field and the coil\'s normal. With N = 100, B = 0.2 T, I = 2 A and A = 0.01 m², the maximum torque is 0.4 N·m.',
            'In a DC motor a commutator reverses the current every half turn so the torque keeps turning the coil the same way. Loudspeakers use the force on a coil in a permanent magnet\'s field to move a cone.'],
        'formulas_label': 'Formulas',
        'formulas': ['F = BIL sin θ', 'τ = NBIA sin θ', 'Magnetic moment μ = NIA', 'τ = μB sin θ'],
        'steps': ['Find the angle between wire (or normal) and field.', 'Compute the size.', 'Find the direction by a hand rule.', 'For coils, maximum torque occurs when the plane of the coil is parallel to B.'],
        'worked_example': {
            'problem': 'A 100-turn coil of area 0.01 m² carries 2 A in a 0.2 T field. Find the maximum torque.',
            'steps': ['τ_max = NBIA.', 'τ = 100 × 0.2 × 2 × 0.01.', 'τ = 0.4 N·m.'],
            'answer': '0.4 N·m.',
            'check': 'Magnetic moment NIA = 2 A·m²; × 0.2 T = 0.4 ✓.'},
        'mistakes': ['Using the wrong angle for the coil (normal versus plane).', 'Forgetting N turns.', 'Thinking a wire parallel to B feels a force.', 'Mixing left- and right-hand rules.'],
        'real_world': 'Every electric car, drill and ceiling fan uses magnetic forces on current-carrying coils.',
        'exam_strategy': 'Say which angle you are using; examiners deliberately describe the coil\'s plane rather than its normal.',
        'recap': ['F = BIL sin θ.', 'τ = NBIA sin θ.', 'Commutator.', 'Motors and speakers.']},
    T3: {
        'overview': 'Currents create magnetic fields. The Biot–Savart law gives the field of any current; Ampère\'s law gives it quickly when there is symmetry.',
        'key_terms': ['Biot–Savart law', 'Permeability μ₀', 'Field of a long wire', 'Field at the centre of a loop', 'Ampère\'s law', 'Force between wires'],
        'explanation': [
            'A long straight wire produces circular field lines with B = μ₀I/(2πr), μ₀ = 4π × 10⁻⁷ T·m/A. 10 A gives 40 μT at 5 cm, comparable with Earth\'s field (about 25 to 65 μT). The right-hand grip rule gives the direction.',
            'From Biot–Savart, the field at the centre of a circular loop of radius R is μ₀I/(2R): 5 A in a 0.1 m loop gives about 3.14 × 10⁻⁵ T. Ampère\'s law ∮B·dl = μ₀I_enc reproduces the wire result instantly by taking a circle around the wire.',
            'Two parallel wires attract if their currents are in the same direction and repel if opposite: F/L = μ₀I₁I₂/(2πd). Two 10 A currents 0.1 m apart give 2 × 10⁻⁴ N per metre. This force was once used to define the ampere.'],
        'formulas_label': 'Formulas',
        'formulas': ['Long wire: B = μ₀I/(2πr)', 'Loop centre: B = μ₀I/(2R)', 'Ampère: ∮B·dl = μ₀I_enc', 'F/L = μ₀I₁I₂/(2πd)'],
        'steps': ['Identify the symmetry.', 'Choose an Ampèrian loop along field lines.', 'Find I_enc.', 'Solve for B.'],
        'worked_example': {
            'problem': 'Find the force per metre between two parallel wires 0.1 m apart, each carrying 10 A in the same direction.',
            'steps': ['Field of one wire at the other: B = μ₀ × 10/(2π × 0.1) = 2 × 10⁻⁵ T.', 'F/L = BI = 2 × 10⁻⁵ × 10.', 'F/L = 2 × 10⁻⁴ N/m, attractive.'],
            'answer': '2 × 10⁻⁴ N per metre, attractive.',
            'check': 'Same-direction currents attract ✓.'},
        'mistakes': ['Using 4π instead of 2π for the wire.', 'Confusing the loop formula with the wire formula.', 'Getting attraction and repulsion reversed.', 'Not converting cm to m.'],
        'real_world': 'Compass readings near power cables can be off because the current creates a field comparable to Earth\'s.',
        'exam_strategy': 'μ₀/(2π) = 2 × 10⁻⁷ exactly; using it makes wire calculations quick.',
        'recap': ['B = μ₀I/(2πr).', 'Loop μ₀I/(2R).', 'Ampère\'s law.', 'Parallel currents attract.']},
    T4: {
        'overview': 'Solenoids and toroids produce strong, controlled magnetic fields. Magnetic materials can greatly enhance them.',
        'key_terms': ['Solenoid', 'Turns per metre', 'Toroid', 'Electromagnet', 'Ferromagnetism', 'Domains', 'Relative permeability', 'Hall effect'],
        'explanation': [
            'A long solenoid has a nearly uniform field inside, B = μ₀nI, with n = turns per metre. 500 turns on 0.25 m (n = 2000 per metre) carrying 3 A gives B ≈ 7.54 × 10⁻³ T. Outside, the field is nearly zero.',
            'A toroid (a doughnut-shaped coil) confines its field: B = μ₀NI/(2πr). 500 turns, 3 A at r = 0.1 m give 3 × 10⁻³ T. Both results follow from Ampère\'s law.',
            'Ferromagnetic materials such as iron have domains that line up with an applied field, multiplying B by their relative permeability (hundreds to thousands). That is why electromagnets have iron cores. The Hall effect, a voltage across a current-carrying strip in a field, is used in sensors to measure B.'],
        'formulas_label': 'Formulas',
        'formulas': ['Solenoid: B = μ₀nI, n = N/L', 'Toroid: B = μ₀NI/(2πr)', 'With a core: B = μᵣμ₀nI'],
        'steps': ['Find n = N/L.', 'Apply B = μ₀nI.', 'Multiply by μᵣ for a core.', 'Use the right-hand grip rule for direction.'],
        'worked_example': {
            'problem': 'A solenoid 0.25 m long has 500 turns and carries 3 A. Find the field inside.',
            'steps': ['n = 500/0.25 = 2000 turns per metre.', 'B = 4π × 10⁻⁷ × 2000 × 3.', 'B ≈ 7.54 × 10⁻³ T.'],
            'answer': 'About 7.5 mT.',
            'check': 'Doubling the current would double B ✓.'},
        'mistakes': ['Using total turns N instead of n = N/L.', 'Thinking the field outside a solenoid is strong.', 'Using the solenoid formula for a short coil.', 'Forgetting μᵣ for iron cores.'],
        'real_world': 'MRI scanners use superconducting solenoids producing 1.5 to 3 T, tens of thousands of times Earth\'s field.',
        'exam_strategy': 'Check whether the question gives N and L, or n directly.',
        'recap': ['B = μ₀nI.', 'Toroid confines field.', 'Iron cores amplify.', 'Hall-effect sensors.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A proton at 2 × 10⁶ m/s perpendicular to 0.5 T feels a force of:', ['1.6 × 10⁻¹³ N', '1.6 × 10⁻¹⁹ N', '6.4 × 10⁻¹³ N', '0'], 0, 'qvB.'),
    Q(T1, 'The radius of that proton\'s path is about:', ['4.18 cm', '41.8 cm', '0.418 cm', '2.09 cm'], 0, 'mv/(qB).'),
    Q(T1, 'An electron at 10⁷ m/s in a 1 mT field circles with radius about:', ['5.7 cm', '57 cm', '0.57 cm', '5.7 m'], 0, 'mv/(qB).'),
    Q(T1, 'The magnetic force on a moving charge:', ['does no work', 'always speeds it up', 'acts along its velocity', 'acts along B'], 0, 'Perpendicular to v.'),
    Q(T1, 'A velocity selector with E = 10⁴ V/m and B = 0.02 T passes particles at:', ['5 × 10⁵ m/s', '200 m/s', '2 × 10⁶ m/s', '5 × 10³ m/s'], 0, 'E/B.'),
    Q(T1, 'The cyclotron frequency of a charged particle:', ['does not depend on its speed', 'grows with its speed', 'falls with its speed', 'depends only on the radius'], 0, 'qB/(2πm).'),
    # T2
    Q(T2, 'A 0.2 m wire carrying 5 A perpendicular to 0.4 T feels:', ['0.4 N', '4 N', '0.04 N', '10 N'], 0, 'BIL.', ans=0.4, num=True),
    Q(T2, 'The same wire at 30° to the field feels:', ['0.2 N', '0.35 N', '0.4 N', '0.1 N'], 0, 'sin 30° = ½.', ans=0.2, num=True),
    Q(T2, 'A 100-turn coil of area 0.01 m² with 2 A in 0.2 T has maximum torque:', ['0.4 N·m', '4 N·m', '0.004 N·m', '40 N·m'], 0, 'NBIA.', ans=0.4, num=True),
    Q(T2, 'A wire parallel to a magnetic field feels:', ['no force', 'maximum force', 'a force along the wire', 'a torque only'], 0, 'sin 0 = 0.'),
    Q(T2, 'In a DC motor, the commutator:', ['reverses the current every half turn', 'stores charge', 'increases the field', 'smooths the voltage'], 0, 'Keeps the torque one way.'),
    Q(T2, 'A loudspeaker works because:', ['a current-carrying coil in a magnetic field feels a force', 'charges repel', 'capacitors discharge', 'resistance heats the cone'], 0, 'BIL force.'),
    # T3
    Q(T3, 'The field 5 cm from a long wire carrying 10 A is:', ['40 μT', '4 μT', '400 μT', '20 μT'], 0, 'μ₀I/(2πr).', ans=40, num=True),
    Q(T3, 'The field at the centre of a 0.1 m radius loop carrying 5 A is about:', ['3.14 × 10⁻⁵ T', '1.0 × 10⁻⁵ T', '6.28 × 10⁻⁵ T', '3.14 × 10⁻⁷ T'], 0, 'μ₀I/(2R).'),
    Q(T3, 'Two parallel wires carrying 10 A each, 0.1 m apart, feel a force per metre of:', ['2 × 10⁻⁴ N/m', '2 × 10⁻⁵ N/m', '4 × 10⁻⁴ N/m', '1 × 10⁻⁴ N/m'], 0, 'μ₀I₁I₂/(2πd).'),
    Q(T3, 'Wires carrying currents in opposite directions:', ['repel', 'attract', 'feel no force', 'twist'], 0, 'Opposite currents repel.'),
    Q(T3, 'Doubling the distance from a long wire makes the field:', ['half as large', 'a quarter as large', 'twice as large', 'unchanged'], 0, 'B ∝ 1/r.'),
    Q(T3, 'Ampère\'s law relates the line integral of B to:', ['the current enclosed', 'the charge enclosed', 'the flux of E', 'the voltage'], 0, '∮B·dl = μ₀I_enc.'),
    # T4
    Q(T4, 'A 0.25 m solenoid with 500 turns carrying 3 A has an internal field of about:', ['7.54 mT', '1.88 mT', '0.754 mT', '75.4 mT'], 0, 'μ₀nI, n = 2000/m.', ans=7.54, num=True),
    Q(T4, 'A toroid of 500 turns with 3 A has, at r = 0.1 m, a field of:', ['3 mT', '6 mT', '1.5 mT', '30 mT'], 0, 'μ₀NI/(2πr).', ans=3, num=True),
    Q(T4, 'The field outside a long ideal solenoid is:', ['nearly zero', 'the same as inside', 'twice the inside value', 'infinite'], 0, 'Field lines spread out.'),
    Q(T4, 'Electromagnets use iron cores because iron:', ['multiplies the field greatly', 'conducts electricity', 'is cheap only', 'reduces the current'], 0, 'High relative permeability.'),
    Q(T4, 'In the solenoid formula B = μ₀nI, n is:', ['turns per metre', 'total turns', 'the number of layers', 'the current density'], 0, 'n = N/L.'),
    Q(T4, 'The Hall effect is used to:', ['measure magnetic fields', 'store charge', 'step up voltages', 'measure resistance only'], 0, 'Hall sensors.'),
]

FLASH = [
    ['Lorentz force', 'F = qvB sin θ, perpendicular to v and B.'],
    ['Orbit radius', 'r = mv/(qB).'],
    ['Velocity selector', 'v = E/B.'],
    ['Force on a wire', 'F = BIL sin θ.'],
    ['Torque on a coil', 'τ = NBIA sin θ.'],
    ['Field of a long wire', 'B = μ₀I/(2πr).'],
    ['Ampère\'s law', '∮B·dl = μ₀I_enc.'],
    ['Solenoid field', 'B = μ₀nI, n turns per metre.'],
]
