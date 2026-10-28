"""Electricity and Magnetism, module 1: Electric charge, field and potential."""
import math
from verify import Q, sp
T1, T2, T3, T4 = ('Charge and Coulomb\'s law', 'The electric field', 'Gauss\'s law', 'Electric potential and energy')
k, e, e0, me = 8.99e9, 1.602e-19, 8.85e-12, 9.11e-31
r = lambda v, d: round(v, d)
assert r(k * 2e-6 * 3e-6 / 0.1 ** 2, 2) == 5.39 and r(2e-6 / e / 1e13, 2) == 1.25
F1 = k * 2e-6 * 3e-6 / 0.1 ** 2; assert r(F1 / 4, 2) == 1.35 and r(F1 * 4, 1) == 21.6
assert r(k * 5e-6 / 0.3 ** 2 / 1e5, 2) == 4.99 and r((k * 4e-6 + k * 1e-6) / 0.15 ** 2 / 1e6, 2) == 2.00
assert 12 / 0.004 == 3000 and r(1.602e-19 * 3000, 22) == 4.806e-16
assert r(1e-6 / e0 / 1e5, 2) == 1.13 and r(k * 10e-9 / 0.2 ** 2 / 1e3, 2) == 2.25 and r(10e-9 / (4 * math.pi * e0 * 0.2 ** 2) / 1e3, 2) == 2.25
assert r(k * 1e-9 / 0.1, 1) == 89.9 and r(k * 2e-6 / 0.5, -2) == 36000 and r(e * 100, 21) == 1.602e-17
assert r(math.sqrt(2 * e * 100 / me) / 1e6, 2) == 5.93 and r(k * 2e-6 * 3e-6 / 0.1, 3) == 0.539

MODULE = {
    'title': 'Electric charge, field and potential',
    'topics': [T1, T2, T3, T4],
    'overview': 'Electricity starts with charge. This module covers Coulomb\'s law for the force between charges, the electric field as a way to describe that force everywhere in space, Gauss\'s law for highly symmetric charge distributions, and electric potential and energy, which link fields to voltages.',
    'key_terms': ['Charge', 'Coulomb', 'Conservation of charge', 'Coulomb\'s law', 'Superposition', 'Electric field', 'Field lines', 'Electric flux', 'Gauss\'s law', 'Conductor', 'Electric potential', 'Volt', 'Potential energy', 'Electron-volt', 'Equipotential'],
    'explanation': [
        'Charge comes in positive and negative amounts, measured in coulombs; the electron carries −1.602 × 10⁻¹⁹ C. Like charges repel and unlike charges attract with a force F = kq₁q₂/r², where k = 8.99 × 10⁹ N·m²/C². Charge is conserved.',
        'The electric field E = F/q is the force per unit positive charge; a point charge creates E = kq/r² pointing away from positive charges. Fields from several charges add as vectors (superposition). For symmetric charge distributions, Gauss\'s law, Φ = q_enc/ε₀, gives the field almost instantly.',
        'The electric potential V is potential energy per unit charge, measured in volts: V = kq/r for a point charge. Moving a charge q through a potential difference ΔV changes its energy by qΔV, which is how particle accelerators and old TV tubes speed up electrons.'],
    'quick_facts': [
        'F = kq₁q₂/r², k = 8.99 × 10⁹ N·m²/C² = 1/(4πε₀).',
        'E = F/q; point charge E = kq/r².',
        'Gauss: Φ = ∮E·dA = q_enc/ε₀, ε₀ = 8.85 × 10⁻¹² C²/(N·m²).',
        'V = kq/r; uniform field E = V/d.',
        'ΔU = qΔV; 1 eV = 1.602 × 10⁻¹⁹ J.'],
}

NOTES = {
    T1: {
        'overview': 'Coulomb\'s law gives the force between two point charges. It is an inverse-square law, like gravity, but can attract or repel.',
        'key_terms': ['Elementary charge', 'Coulomb', 'Conductor', 'Insulator', 'Induction', 'Coulomb\'s law', 'Inverse-square law', 'Superposition'],
        'explanation': [
            'All charges are whole multiples of e = 1.602 × 10⁻¹⁹ C. A charge of 2 μC is an excess of 2 × 10⁻⁶/1.602 × 10⁻¹⁹ ≈ 1.25 × 10¹³ electrons\' worth. Conductors let charges move freely; insulators do not.',
            'F = kq₁q₂/r². Charges of 2 μC and 3 μC, 0.1 m apart, repel with F = 8.99 × 10⁹ × 2 × 10⁻⁶ × 3 × 10⁻⁶/0.01 ≈ 5.39 N. Doubling the distance quarters the force (≈ 1.35 N); halving it multiplies the force by 4 (≈ 21.6 N).',
            'With several charges, compute each force separately and add them as vectors (superposition). By Newton\'s third law, the two charges feel equal and opposite forces whatever their sizes.'],
        'formulas_label': 'Formulas',
        'formulas': ['F = kq₁q₂/r²', 'k = 8.99 × 10⁹ N·m²/C²', 'e = 1.602 × 10⁻¹⁹ C', 'Net force = vector sum'],
        'steps': ['Convert μC and nC to C, cm to m.', 'Compute the size with Coulomb\'s law.', 'Find the direction (attract or repel).', 'Add vectors for several charges.'],
        'worked_example': {
            'problem': 'Find the force between +2 μC and +3 μC charges 10 cm apart.',
            'steps': ['q₁ = 2 × 10⁻⁶ C, q₂ = 3 × 10⁻⁶ C, r = 0.1 m.', 'F = 8.99 × 10⁹ × 6 × 10⁻¹²/0.01.', 'F ≈ 5.39 N, repulsive.'],
            'answer': 'About 5.39 N, repulsive.',
            'check': 'Both positive, so they repel ✓; doubling r would give a quarter of this.'},
        'mistakes': ['Forgetting to square r.', 'Not converting μC to C.', 'Adding forces as numbers instead of vectors.', 'Using the sign of the charge for direction inconsistently.'],
        'real_world': 'Photocopiers and laser printers use electrostatic attraction to place toner exactly where the image is.',
        'exam_strategy': 'Calculate the magnitude with positive values, then decide direction from a diagram; it avoids sign confusion.',
        'recap': ['Quantised charge.', 'Inverse-square force.', 'Like repel, unlike attract.', 'Superposition.']},
    T2: {
        'overview': 'The electric field describes the force a charge would feel at every point in space.',
        'key_terms': ['Electric field', 'Test charge', 'Field lines', 'Uniform field', 'Dipole', 'Superposition of fields'],
        'explanation': [
            'E = F/q, in N/C. A point charge gives E = kq/r², directed away from a positive charge and towards a negative one. At 0.3 m from 5 μC, E = 8.99 × 10⁹ × 5 × 10⁻⁶/0.09 ≈ 4.99 × 10⁵ N/C.',
            'Fields add as vectors. Midway between +4 μC and −1 μC that are 0.3 m apart, both fields point towards the negative charge, so their sizes add: E = k(4 + 1) × 10⁻⁶/0.15² ≈ 2.0 × 10⁶ N/C.',
            'Between large parallel plates the field is uniform: E = V/d. Plates 4 mm apart at 12 V give 3000 V/m (the same as N/C), and an electron there feels F = eE ≈ 4.8 × 10⁻¹⁶ N. Field lines start on positive charges, end on negative ones and never cross.'],
        'formulas_label': 'Formulas',
        'formulas': ['E = F/q', 'Point charge: E = kq/r²', 'Uniform field: E = V/d', 'F = qE'],
        'steps': ['Find each field\'s size with kq/r².', 'Draw its direction at the point.', 'Add components.', 'Use F = qE for a charge placed there.'],
        'worked_example': {
            'problem': 'Find the field midway between +4 μC and −1 μC placed 0.3 m apart.',
            'steps': ['Each is 0.15 m away.', 'Field from +4 μC points away from it, towards −1 μC; field from −1 μC points towards it: same direction.', 'E = 8.99 × 10⁹ × 5 × 10⁻⁶/0.0225 ≈ 2.0 × 10⁶ N/C.'],
            'answer': 'About 2.0 × 10⁶ N/C, towards the −1 μC charge.',
            'check': 'Same direction, so magnitudes add ✓.'},
        'mistakes': ['Subtracting fields that point the same way.', 'Using the test charge in E = kq/r².', 'Forgetting E is a vector.', 'Mixing V/m and V.'],
        'real_world': 'Sharks and some fish sense tiny electric fields from the muscles of their prey.',
        'exam_strategy': 'Draw arrows for each field at the point before doing any arithmetic.',
        'recap': ['E = F/q.', 'kq/r² for a point.', 'Vectors add.', 'E = V/d between plates.']},
    T3: {
        'overview': 'Gauss\'s law relates the electric flux through a closed surface to the charge inside, and gives fields quickly for symmetric charge distributions.',
        'key_terms': ['Electric flux', 'Gaussian surface', 'Enclosed charge', 'Spherical symmetry', 'Line charge', 'Plane of charge', 'Conductor in equilibrium'],
        'explanation': [
            'Flux Φ = ∮E·dA measures field lines through a surface. Gauss\'s law: Φ = q_enc/ε₀. Any closed surface around 1 μC has flux 10⁻⁶/8.85 × 10⁻¹² ≈ 1.13 × 10⁵ N·m²/C, whatever its shape.',
            'Choose a Gaussian surface matching the symmetry. Outside a uniformly charged sphere, the field is as if all the charge were at the centre: Q = 10 nC gives E ≈ 2.25 × 10³ N/C at r = 0.2 m. An infinite line charge gives E = λ/(2πε₀r); an infinite sheet E = σ/(2ε₀).',
            'In a conductor at equilibrium the field inside is zero and any excess charge sits on the surface. This is why a metal car protects passengers from lightning (a Faraday cage).'],
        'formulas_label': 'Formulas',
        'formulas': ['Φ = ∮E·dA = q_enc/ε₀', 'Sphere (outside): E = Q/(4πε₀r²)', 'Line: E = λ/(2πε₀r)', 'Sheet: E = σ/(2ε₀)', 'Conductor: E = 0 inside'],
        'steps': ['Identify the symmetry.', 'Choose a matching Gaussian surface.', 'Compute q_enc.', 'Solve Φ = E × area = q_enc/ε₀ for E.'],
        'worked_example': {
            'problem': 'A uniformly charged sphere carries 10 nC. Find E at 0.2 m from its centre (outside the sphere).',
            'steps': ['Gaussian sphere of radius 0.2 m: E × 4πr² = Q/ε₀.', 'E = Q/(4πε₀r²) = 10 × 10⁻⁹/(4π × 8.85 × 10⁻¹² × 0.04).', 'E ≈ 2.25 × 10³ N/C.'],
            'answer': 'About 2.25 × 10³ N/C.',
            'check': 'Same as kQ/r², as expected for a point charge ✓.'},
        'mistakes': ['Using charge outside the surface.', 'Applying Gauss\'s law without enough symmetry to pull E out of the integral.', 'Thinking flux depends on surface size.', 'Saying the field inside a charged conductor is non-zero.'],
        'real_world': 'Sensitive electronics are shielded in metal boxes because the field inside a conductor is zero.',
        'exam_strategy': 'State the Gaussian surface explicitly and why E is constant on it; that is the method mark.',
        'recap': ['Flux = q_enc/ε₀.', 'Use symmetry.', 'Sphere acts like a point.', 'Zero field in conductors.']},
    T4: {
        'overview': 'Electric potential is energy per unit charge. Potential differences (voltages) drive currents and accelerate charges.',
        'key_terms': ['Potential energy', 'Electric potential', 'Volt', 'Potential difference', 'Equipotential surface', 'Electron-volt', 'Work done by the field'],
        'explanation': [
            'The potential of a point charge is V = kq/r (a scalar, so potentials simply add). At 0.1 m from 1 nC, V ≈ 89.9 V; at 0.5 m from 2 μC, V ≈ 3.6 × 10⁴ V.',
            'The potential energy of two charges is U = kq₁q₂/r: for 2 μC and 3 μC at 0.1 m, U ≈ 0.539 J. Moving a charge q through ΔV changes its energy by qΔV: an electron accelerated through 100 V gains 100 eV = 1.602 × 10⁻¹⁷ J and reaches about 5.93 × 10⁶ m/s.',
            'The field points from high to low potential and E = −dV/dx; in a uniform field E = V/d. Equipotential surfaces are perpendicular to field lines, and moving along one takes no work.'],
        'formulas_label': 'Formulas',
        'formulas': ['V = kq/r', 'U = kq₁q₂/r', 'ΔU = qΔV', '½mv² = qV (from rest)', 'E = −dV/dx; uniform E = V/d'],
        'steps': ['Add potentials as scalars (with signs).', 'Use ΔU = qΔV for energy changes.', 'Use energy conservation for speeds.', 'Relate to the field with E = V/d.'],
        'worked_example': {
            'problem': 'An electron starts from rest and is accelerated through 100 V. Find its speed.',
            'steps': ['Energy gained: eV = 1.602 × 10⁻¹⁹ × 100 = 1.602 × 10⁻¹⁷ J.', '½mv² = 1.602 × 10⁻¹⁷ with m = 9.11 × 10⁻³¹ kg.', 'v = √(2 × 1.602 × 10⁻¹⁷/9.11 × 10⁻³¹) ≈ 5.93 × 10⁶ m/s.'],
            'answer': 'About 5.93 × 10⁶ m/s.',
            'check': 'Well below light speed (3 × 10⁸ m/s), so classical mechanics is fine ✓.'},
        'mistakes': ['Treating potential as a vector.', 'Confusing V (volts) with U (joules).', 'Dropping signs when adding potentials.', 'Using r² in V = kq/r.'],
        'real_world': 'X-ray tubes accelerate electrons through tens of thousands of volts; when they hit a metal target their energy becomes X-rays.',
        'exam_strategy': 'Use energy conservation (qV = ½mv²) rather than forces whenever speeds are asked for.',
        'recap': ['V = kq/r (scalar).', 'U = qV.', 'eV energies.', 'E = V/d.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The force between +2 μC and +3 μC charges 10 cm apart is about:', ['5.39 N', '0.539 N', '53.9 N', '5.39 × 10⁻⁶ N'], 0, 'kq₁q₂/r².', ans=5.39, num=True),
    Q(T1, 'If the distance between two charges doubles, the force becomes:', ['a quarter', 'half', 'double', 'four times'], 0, 'Inverse square.'),
    Q(T1, 'How many elementary charges make up 2 μC?', ['about 1.25 × 10¹³', 'about 1.25 × 10¹⁹', 'about 3.2 × 10⁻¹³', 'about 2 × 10⁶'], 0, '2 × 10⁻⁶/1.602 × 10⁻¹⁹.'),
    Q(T1, 'Two charges, one +1 μC and one +5 μC, exert forces on each other that are:', ['equal in size and opposite in direction', 'larger on the smaller charge', 'larger on the larger charge', 'in the same direction'], 0, 'Newton\'s third law.'),
    Q(T1, 'A positive and a negative charge:', ['attract', 'repel', 'do not interact', 'attract only if equal'], 0, 'Unlike charges attract.'),
    Q(T1, 'The value of k in Coulomb\'s law is about:', ['8.99 × 10⁹ N·m²/C²', '6.67 × 10⁻¹¹ N·m²/kg²', '8.85 × 10⁻¹² C²/(N·m²)', '1.6 × 10⁻¹⁹ C'], 0, 'k = 1/(4πε₀).'),
    # T2
    Q(T2, 'The field 0.3 m from a 5 μC charge is about:', ['5.0 × 10⁵ N/C', '1.5 × 10⁵ N/C', '5.0 × 10⁴ N/C', '1.7 × 10⁶ N/C'], 0, 'kq/r².'),
    Q(T2, 'Midway between +4 μC and −1 μC charges 0.3 m apart, the field is about:', ['2.0 × 10⁶ N/C', '1.2 × 10⁶ N/C', '1.6 × 10⁶ N/C', '0'], 0, 'Both fields point the same way.'),
    Q(T2, 'Plates 4 mm apart at 12 V produce a uniform field of:', ['3000 V/m', '48 V/m', '3 V/m', '0.048 V/m'], 0, 'V/d.'),
    Q(T2, 'The direction of the field of a negative point charge is:', ['towards the charge', 'away from the charge', 'tangential', 'zero'], 0, 'Lines end on negatives.'),
    Q(T2, 'Electric field lines:', ['never cross', 'form closed loops around charges', 'start on negative charges', 'are always parallel'], 0, 'One direction at each point.'),
    Q(T2, 'The unit N/C is equivalent to:', ['V/m', 'V', 'J/C', 'C/m'], 0, 'E = V/d.'),
    # T3
    Q(T3, 'The flux through any closed surface surrounding 1 μC is about:', ['1.13 × 10⁵ N·m²/C', '8.85 × 10⁻¹⁸ N·m²/C', '8.99 × 10³ N·m²/C', 'zero'], 0, 'q/ε₀.'),
    Q(T3, 'The field 0.2 m from the centre of a uniformly charged sphere carrying 10 nC is about:', ['2.25 × 10³ N/C', '4.5 × 10² N/C', '2.25 × 10⁵ N/C', '0'], 0, 'Like a point charge.'),
    Q(T3, 'Inside a conductor in electrostatic equilibrium, the field is:', ['zero', 'maximum', 'equal to σ/ε₀', 'radial'], 0, 'Charges rearrange.'),
    Q(T3, 'The field of an infinite plane of charge with surface density σ is:', ['σ/(2ε₀)', 'σ/ε₀', 'σ/(4πε₀r²)', 'σr'], 0, 'Independent of distance.'),
    Q(T3, 'If the charge inside a closed surface doubles, the flux:', ['doubles', 'halves', 'stays the same', 'quadruples'], 0, 'Φ ∝ q_enc.'),
    Q(T3, 'A Gaussian surface is chosen so that:', ['E is constant on it and can be taken out of the integral', 'it has no charge inside', 'it is always a cube', 'flux is zero'], 0, 'Symmetry.'),
    # T4
    Q(T4, 'The potential 0.1 m from a 1 nC charge is about:', ['89.9 V', '899 V', '8.99 V', '0.899 V'], 0, 'kq/r.', ans=89.9, num=True),
    Q(T4, 'The potential energy of 2 μC and 3 μC charges 0.1 m apart is about:', ['0.539 J', '5.39 J', '0.0539 J', '53.9 J'], 0, 'kq₁q₂/r.', ans=0.539, num=True),
    Q(T4, 'An electron accelerated through 100 V gains energy:', ['1.602 × 10⁻¹⁷ J', '1.602 × 10⁻¹⁹ J', '100 J', '1.602 × 10⁻²¹ J'], 0, 'eV.'),
    Q(T4, 'Its speed after starting from rest is about:', ['5.93 × 10⁶ m/s', '5.93 × 10⁸ m/s', '3.0 × 10⁸ m/s', '1.0 × 10⁴ m/s'], 0, '√(2eV/m).'),
    Q(T4, 'The potential 0.5 m from a 2 μC charge is about:', ['3.6 × 10⁴ V', '7.2 × 10⁴ V', '1.8 × 10⁴ V', '3.6 × 10³ V'], 0, 'kq/r.'),
    Q(T4, 'Moving a charge along an equipotential surface requires:', ['no work', 'maximum work', 'work equal to qE', 'negative work'], 0, 'ΔV = 0.'),
]

FLASH = [
    ['Coulomb\'s law', 'F = kq₁q₂/r², k = 8.99 × 10⁹ N·m²/C².'],
    ['Elementary charge', 'e = 1.602 × 10⁻¹⁹ C.'],
    ['Electric field', 'E = F/q; point charge kq/r²; uniform V/d.'],
    ['Gauss\'s law', 'Φ = q_enc/ε₀.'],
    ['Conductor in equilibrium', 'Zero field inside; excess charge on the surface.'],
    ['Electric potential', 'V = kq/r (scalar), in volts.'],
    ['Potential energy change', 'ΔU = qΔV.'],
    ['Electron-volt', '1 eV = 1.602 × 10⁻¹⁹ J.'],
]
