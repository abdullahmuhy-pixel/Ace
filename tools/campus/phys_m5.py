"""Physics I: Mechanics, module 5: Rotation, gravitation and oscillations."""
import math
from verify import Q
T1, T2, T3, T4 = ('Torque and equilibrium', 'Rotational dynamics and angular momentum', 'Gravitation and orbits', 'Simple harmonic motion')
g = 9.8
G, ME, RE = 6.67e-11, 5.97e24, 6.37e6
r = lambda x, d: round(x + 0.0, d)
assert 20 * 0.3 == 6 and r(20 * 0.3 * math.sin(math.radians(30)), 6) == 3
assert 30 * 2 == 40 * 1.5
Rr = 2 * g * 0.5 + 5 * g * 0.25
assert r(Rr, 2) == 22.05 and r(7 * g - Rr, 2) == 46.55
I = 0.5 * 2 * 0.5 ** 2
assert I == 0.25 and 1 / I == 4 and 4 * 3 == 12 and 0.5 * I * 12 ** 2 == 18
assert 4 * 2 / 1.6 == 5 and r(0.5 * 4 * 2 ** 2, 6) == 8 and r(0.5 * 1.6 * 5 ** 2, 6) == 20
assert r(G * 1000 * 1000 / 1 ** 2, 12) == 6.67e-5
assert r(G * ME / RE ** 2, 2) == 9.81
v_iss = math.sqrt(G * ME / 6.77e6)
assert r(v_iss / 1000, 2) == 7.67 and r(2 * math.pi * 6.77e6 / v_iss / 60, 0) == 92
assert 9.8 / 4 == 2.45
assert r(2 * math.pi * math.sqrt(0.5 / 50), 3) == 0.628 and r(2 * math.pi * math.sqrt(1 / g), 2) == 2.01
assert r(0.1 * 10, 6) == 1 and r(0.1 * 10 ** 2, 6) == 10 and r(1 / 0.628, 2) == 1.59

MODULE = {
    'title': 'Rotation, gravitation and oscillations',
    'topics': [T1, T2, T3, T4],
    'overview': 'Many objects turn, orbit or vibrate. This module extends Newton\'s laws to rotation (torque, moment of inertia and angular momentum), applies the law of gravitation to planets and satellites, and introduces simple harmonic motion in springs and pendulums.',
    'key_terms': ['Torque', 'Moment', 'Equilibrium', 'Moment of inertia', 'Angular acceleration', 'Angular momentum', 'Universal gravitation', 'Orbital speed', 'Simple harmonic motion', 'Period', 'Amplitude'],
    'explanation': [
        'Torque τ = rF sin θ is the turning effect of a force. An object is in equilibrium when the resultant force and the resultant torque are both zero, the basis of every bridge, crane and seesaw calculation.',
        'Rotation mirrors straight-line motion: τ = Iα replaces F = ma, rotational KE = ½Iω² replaces ½mv², and angular momentum L = Iω is conserved when no external torque acts.',
        'Newton\'s law of gravitation, F = GMm/r², explains g at the Earth\'s surface and the speeds of satellites. Simple harmonic motion, where the restoring force is proportional to displacement, describes springs, pendulums and many vibrations.'],
    'quick_facts': [
        'Torque τ = rF sin θ (N·m).',
        'Equilibrium: ΣF = 0 and Στ = 0.',
        'τ = Iα; L = Iω; rotational KE = ½Iω².',
        'F = GMm/r², G = 6.67 × 10⁻¹¹ N·m²/kg².',
        'Spring T = 2π√(m/k); pendulum T = 2π√(L/g).'],
}

NOTES = {
    T1: {
        'overview': 'Torque measures how strongly a force turns an object about a pivot. Balancing torques solves seesaws, beams, levers and cranes.',
        'key_terms': ['Torque (moment)', 'Pivot', 'Lever arm', 'Principle of moments', 'Centre of gravity', 'Static equilibrium'],
        'explanation': [
            'τ = rF sin θ, where r is the distance from the pivot and θ is the angle between r and F. A 20 N force on a 0.3 m spanner, at right angles, gives 6 N·m; at 30° it gives only 3 N·m. Pushing nearer the hinge of a door is harder for the same reason.',
            'For static equilibrium, the resultant force is zero and the sum of clockwise torques equals the sum of anticlockwise torques about any point. A 30 kg child 2 m from a seesaw pivot balances a 40 kg child 1.5 m on the other side (60 = 60).',
            'For beams, take moments about one support to remove its unknown force. The weight of a uniform beam acts at its centre (its centre of gravity). A 1 m, 2 kg plank on two end supports, with 5 kg placed 0.25 m from the left, gives a right support force of 22.05 N and a left force of 46.55 N.'],
        'formulas_label': 'Formulas',
        'formulas': ['τ = rF sin θ', 'Equilibrium: ΣF = 0, Στ = 0', 'Σ clockwise moments = Σ anticlockwise moments', 'Uniform beam: weight acts at the midpoint'],
        'steps': ['Draw the object with all forces and distances.', 'Choose a pivot that removes an unknown.', 'Set clockwise = anticlockwise moments.', 'Use ΣF = 0 for the remaining force.'],
        'worked_example': {
            'problem': 'A uniform 1.0 m plank of mass 2 kg rests on supports at each end. A 5 kg mass sits 0.25 m from the left end. Find the support forces.',
            'steps': ['Moments about the left support: R × 1.0 = (2 × 9.8 × 0.5) + (5 × 9.8 × 0.25) = 9.8 + 12.25.', 'R = 22.05 N.', 'Vertical forces: L + R = 7 × 9.8 = 68.6 N, so L = 46.55 N.'],
            'answer': 'Left support 46.55 N; right support 22.05 N.',
            'check': 'The mass is nearer the left end, so the left support should carry more ✓.'},
        'mistakes': ['Using the distance along the force instead of the perpendicular distance.', 'Forgetting the beam\'s own weight.', 'Taking moments about a point but still including that point\'s force.', 'Mixing kg and N.'],
        'real_world': 'Tower cranes carry a heavy counterweight on the short arm so that the torques balance when lifting loads on the long arm.',
        'exam_strategy': 'Take moments about the support with the unknown force you do not need yet; it drops out of the equation.',
        'recap': ['τ = rF sin θ.', 'Balance torques and forces.', 'Beam weight at centre.', 'Pick a clever pivot.']},
    T2: {
        'overview': 'Rotating objects obey laws that mirror straight-line motion. Moment of inertia plays the role of mass, and angular momentum is conserved.',
        'key_terms': ['Angular velocity ω', 'Angular acceleration α', 'Moment of inertia I', 'τ = Iα', 'Rotational kinetic energy', 'Angular momentum'],
        'explanation': [
            'Moment of inertia I measures resistance to changes in rotation and depends on how mass is spread from the axis: I = Σmr². A solid disc has I = ½MR², so a 2 kg disc of radius 0.5 m has I = 0.25 kg·m². Applying 1 N·m of torque gives α = τ/I = 4 rad/s²; after 3 s from rest, ω = 12 rad/s.',
            'Rotational kinetic energy is ½Iω². That disc at 12 rad/s stores ½ × 0.25 × 144 = 18 J. Rolling objects share their energy between translation and rotation, which is why a solid ball beats a hollow one down a ramp.',
            'Angular momentum L = Iω is conserved when no external torque acts. A spinning skater who pulls in her arms reduces I from 4 to 1.6 kg·m², so ω rises from 2 to 5 rad/s. Her kinetic energy increases (8 J to 20 J) because her muscles do work pulling her arms in.'],
        'formulas_label': 'Formulas',
        'formulas': ['τ = Iα', 'Solid disc: I = ½MR²; point mass: I = mr²', 'Rotational KE = ½Iω²', 'L = Iω; I₁ω₁ = I₂ω₂ with no external torque', 'v = ωr; 1 rev = 2π rad'],
        'steps': ['Find I for the shape.', 'Use τ = Iα for angular acceleration.', 'Use rotational kinematics (ω = ω₀ + αt).', 'Use L = Iω conservation when the shape changes.'],
        'worked_example': {
            'problem': 'A skater spins at 2 rad/s with moment of inertia 4 kg·m². She pulls her arms in, reducing I to 1.6 kg·m². Find her new angular velocity and the change in kinetic energy.',
            'steps': ['L conserved: 4 × 2 = 1.6ω, so ω = 5 rad/s.', 'KE before = ½ × 4 × 2² = 8 J.', 'KE after = ½ × 1.6 × 5² = 20 J; KE increases by 12 J.'],
            'answer': '5 rad/s; KE rises by 12 J.',
            'check': 'Angular momentum: 8 = 8 ✓; the extra KE comes from the work her arms do.'},
        'mistakes': ['Thinking rotational KE is conserved when the skater pulls in her arms.', 'Using degrees or rpm instead of rad/s.', 'Using I = MR² for a solid disc.', 'Confusing angular momentum with linear momentum.'],
        'real_world': 'Divers tuck tightly to spin quickly and straighten out before entering the water to slow their rotation.',
        'exam_strategy': 'Convert rpm to rad/s first: multiply by 2π/60.',
        'recap': ['τ = Iα.', 'KE = ½Iω².', 'L = Iω conserved.', 'Work in rad/s.']},
    T3: {
        'overview': 'Every mass attracts every other mass. Newton\'s law of gravitation explains falling objects, the Moon\'s orbit and the speed of satellites.',
        'key_terms': ['Universal gravitation', 'G', 'Inverse-square law', 'Gravitational field strength', 'Orbital speed', 'Orbital period', 'Geostationary orbit'],
        'explanation': [
            'F = GMm/r², with G = 6.67 × 10⁻¹¹ N·m²/kg² and r measured between centres. Two 1000 kg masses 1 m apart attract with only 6.67 × 10⁻⁵ N, because G is tiny. Doubling the distance divides the force by four.',
            'At the Earth\'s surface, g = GM/R² = 6.67 × 10⁻¹¹ × 5.97 × 10²⁴/(6.37 × 10⁶)² ≈ 9.81 m/s². At twice the Earth\'s radius from the centre, g falls to a quarter: about 2.45 m/s².',
            'For a circular orbit, gravity provides the centripetal force: GMm/r² = mv²/r, so v = √(GM/r). The International Space Station, about 400 km up (r ≈ 6.77 × 10⁶ m), moves at about 7.67 km/s and completes an orbit in about 92 minutes. A geostationary satellite orbits once every 24 hours above the equator.'],
        'formulas_label': 'Formulas',
        'formulas': ['F = GMm/r²', 'g = GM/r²', 'Orbital speed v = √(GM/r)', 'Period T = 2πr/v', 'r from the centre: r = R + height'],
        'steps': ['Measure r from the centre of the planet.', 'Set gravity equal to mv²/r for orbits.', 'Solve for v, then T = 2πr/v.', 'Check orders of magnitude.'],
        'worked_example': {
            'problem': 'Find the orbital speed and period of a satellite 400 km above the Earth (R = 6.37 × 10⁶ m, M = 5.97 × 10²⁴ kg).',
            'steps': ['r = 6.37 × 10⁶ + 0.40 × 10⁶ = 6.77 × 10⁶ m.', 'v = √(6.67 × 10⁻¹¹ × 5.97 × 10²⁴/6.77 × 10⁶) ≈ 7670 m/s.', 'T = 2π × 6.77 × 10⁶/7670 ≈ 5550 s ≈ 92 min.'],
            'answer': 'About 7.67 km/s and 92 minutes.',
            'check': 'This matches the real ISS, which orbits about 16 times a day ✓.'},
        'mistakes': ['Using the height above the surface as r.', 'Forgetting to square r.', 'Thinking there is no gravity in orbit.', 'Including the satellite\'s mass in v = √(GM/r).'],
        'real_world': 'GPS satellites orbit at about 20 000 km, where gravity is weaker and they move more slowly, taking about 12 hours per orbit.',
        'exam_strategy': 'Write standard form carefully on your calculator; most errors here are powers of ten.',
        'recap': ['F = GMm/r².', 'Inverse-square law.', 'v = √(GM/r).', 'r from the centre.']},
    T4: {
        'overview': 'Simple harmonic motion (SHM) is a back-and-forth motion where the restoring force is proportional to the displacement. Springs and pendulums are the classic examples.',
        'key_terms': ['Simple harmonic motion', 'Amplitude', 'Period', 'Frequency', 'Angular frequency ω', 'Restoring force', 'Resonance'],
        'explanation': [
            'In SHM, a = −ω²x: the acceleration always points back to the centre and is largest at the extremes. Period T is the time for one full cycle; frequency f = 1/T; ω = 2πf. The period does not depend on the amplitude.',
            'A mass on a spring has T = 2π√(m/k). With m = 0.5 kg and k = 50 N/m, T = 2π × 0.1 ≈ 0.628 s (f ≈ 1.59 Hz). A simple pendulum (small swings) has T = 2π√(L/g); a 1 m pendulum has T ≈ 2.01 s. Quadrupling the length doubles the period, and the mass does not matter.',
            'Maximum speed v_max = Aω occurs at the centre; maximum acceleration a_max = Aω² occurs at the ends. With A = 0.1 m and ω = 10 rad/s, v_max = 1 m/s and a_max = 10 m/s². When a system is driven at its natural frequency, the amplitude grows large: resonance.'],
        'formulas_label': 'Formulas',
        'formulas': ['a = −ω²x', 'Spring: T = 2π√(m/k)', 'Pendulum: T = 2π√(L/g)', 'f = 1/T, ω = 2πf', 'v_max = Aω; a_max = Aω²'],
        'steps': ['Identify the system (spring or pendulum).', 'Find T or ω from the formula.', 'Use A and ω for maximum speed and acceleration.', 'Check: period independent of amplitude.'],
        'worked_example': {
            'problem': 'A 0.5 kg mass oscillates on a spring with k = 50 N/m and amplitude 0.1 m. Find the period, the maximum speed and the maximum acceleration.',
            'steps': ['ω = √(k/m) = √100 = 10 rad/s.', 'T = 2π/ω ≈ 0.628 s.', 'v_max = Aω = 0.1 × 10 = 1 m/s; a_max = Aω² = 0.1 × 100 = 10 m/s².'],
            'answer': 'T ≈ 0.628 s; v_max = 1 m/s; a_max = 10 m/s².',
            'check': 'Energy: ½kA² = ½ × 50 × 0.01 = 0.25 J = ½mv_max² = ½ × 0.5 × 1 ✓.'},
        'mistakes': ['Thinking a heavier pendulum bob swings more slowly.', 'Thinking a bigger amplitude gives a longer period.', 'Confusing f and ω.', 'Placing maximum speed at the ends instead of the centre.'],
        'real_world': 'Quartz watches keep time using a crystal that vibrates in SHM at exactly 32 768 Hz.',
        'exam_strategy': 'For "what happens to T if…" questions, look at what is under the square root: only m and k (spring) or L and g (pendulum) matter.',
        'recap': ['a = −ω²x.', 'T = 2π√(m/k), 2π√(L/g).', 'Period independent of amplitude.', 'v_max = Aω at centre.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A 20 N force acts at right angles 0.3 m from a pivot. The torque is:', ['6 N·m', '66.7 N·m', '0.015 N·m', '20.3 N·m'], 0, 'τ = rF.', ans=6),
    Q(T1, 'The same force at 30° to the spanner gives a torque of:', ['3 N·m', '5.2 N·m', '6 N·m', '10 N·m'], 0, 'rF sin 30°.', ans=3),
    Q(T1, 'A 30 kg child sits 2 m from a seesaw pivot. To balance, a 40 kg child sits:', ['1.5 m on the other side', '2.67 m on the other side', '2 m on the other side', '1.5 m on the same side'], 0, '30 × 2 = 40d.'),
    Q(T1, 'A 1 m, 2 kg uniform plank on end supports holds 5 kg 0.25 m from the left. The right support pushes with:', ['22.05 N', '46.55 N', '34.3 N', '68.6 N'], 0, 'Moments about the left support.', ans=22.05, num=True),
    Q(T1, 'A uniform beam\'s weight acts at:', ['its midpoint', 'its ends', 'the pivot', 'the heavier end'], 0, 'Centre of gravity.'),
    Q(T1, 'For static equilibrium:', ['the resultant force and resultant torque are both zero', 'only the resultant force is zero', 'only the resultant torque is zero', 'the object must be at the pivot'], 0, 'Both conditions.'),
    # T2
    Q(T2, 'A solid disc of mass 2 kg and radius 0.5 m has moment of inertia:', ['0.25 kg·m²', '0.5 kg·m²', '1 kg·m²', '0.125 kg·m²'], 0, '½MR².'),
    Q(T2, 'A torque of 1 N·m acts on that disc. Its angular acceleration is:', ['4 rad/s²', '0.25 rad/s²', '1 rad/s²', '2 rad/s²'], 0, 'α = τ/I.', ans=4),
    Q(T2, 'After 3 s from rest at 4 rad/s², the disc\'s rotational KE is:', ['18 J', '36 J', '1.5 J', '144 J'], 0, '½ × 0.25 × 12².', ans=18),
    Q(T2, 'A skater with I = 4 kg·m² spinning at 2 rad/s reduces I to 1.6 kg·m². Her new ω:', ['5 rad/s', '0.8 rad/s', '3.2 rad/s', '2 rad/s'], 0, 'I₁ω₁ = I₂ω₂.', ans=5),
    Q(T2, 'When the skater pulls her arms in, her rotational kinetic energy:', ['increases', 'stays the same', 'decreases', 'becomes zero'], 0, '8 J → 20 J; her muscles do work.'),
    Q(T2, '60 revolutions per minute equals:', ['2π rad/s', '60 rad/s', '1 rad/s', '120π rad/s'], 0, '1 rev/s × 2π.'),
    # T3
    Q(T3, 'If the distance between two masses doubles, the gravitational force becomes:', ['a quarter', 'half', 'double', 'four times'], 0, 'Inverse-square law.'),
    Q(T3, 'Using g = GM/R² with Earth\'s values gives about:', ['9.81 m/s²', '6.67 m/s²', '1.62 m/s²', '98.1 m/s²'], 0, '6.67 × 10⁻¹¹ × 5.97 × 10²⁴/(6.37 × 10⁶)².', ans=9.81, num=True),
    Q(T3, 'At twice the Earth\'s radius from its centre, g is about:', ['2.45 m/s²', '4.9 m/s²', '9.8 m/s²', '19.6 m/s²'], 0, '9.8/4.', ans=2.45, num=True),
    Q(T3, 'A satellite 400 km above the Earth orbits at about:', ['7.67 km/s', '0.4 km/s', '11.2 km/s', '30 km/s'], 0, '√(GM/r) with r = 6.77 × 10⁶ m.'),
    Q(T3, 'In v = √(GM/r), r is:', ['the distance from the planet\'s centre', 'the height above the surface', 'the satellite\'s radius', 'the planet\'s diameter'], 0, 'Centre to centre.'),
    Q(T3, 'An orbiting satellite\'s speed depends on:', ['the planet\'s mass and the orbit radius', 'the satellite\'s mass', 'the satellite\'s shape', 'nothing; all orbits have the same speed'], 0, 'v = √(GM/r).'),
    # T4
    Q(T4, 'A 0.5 kg mass on a 50 N/m spring has a period of about:', ['0.628 s', '6.28 s', '0.1 s', '1.59 s'], 0, '2π√(0.01).', ans=0.628, num=True),
    Q(T4, 'A 1 m simple pendulum (g = 9.8) has a period of about:', ['2.01 s', '1.00 s', '6.28 s', '0.32 s'], 0, '2π√(1/9.8).', ans=2.01, num=True),
    Q(T4, 'Quadrupling a pendulum\'s length makes its period:', ['double', 'four times', 'half', 'unchanged'], 0, 'T ∝ √L.'),
    Q(T4, 'With amplitude 0.1 m and ω = 10 rad/s, the maximum speed is:', ['1 m/s', '10 m/s', '0.01 m/s', '100 m/s'], 0, 'Aω.', ans=1),
    Q(T4, 'In SHM, maximum acceleration occurs:', ['at the extremes of the motion', 'at the centre', 'halfway out', 'nowhere; it is constant'], 0, 'a = −ω²x is largest when |x| is largest.'),
    Q(T4, 'Increasing the amplitude of a pendulum\'s (small) swings makes the period:', ['stay the same', 'longer', 'shorter', 'zero'], 0, 'Period independent of amplitude.'),
]

FLASH = [
    ['Torque', 'τ = rF sin θ, in N·m.'],
    ['Equilibrium', 'ΣF = 0 and Στ = 0.'],
    ['Moment of inertia', 'Rotational inertia; solid disc ½MR².'],
    ['Angular momentum', 'L = Iω, conserved with no external torque.'],
    ['Newton\'s gravitation', 'F = GMm/r².'],
    ['Orbital speed', 'v = √(GM/r).'],
    ['Simple harmonic motion', 'a = −ω²x; period independent of amplitude.'],
    ['Pendulum period', 'T = 2π√(L/g).'],
]
