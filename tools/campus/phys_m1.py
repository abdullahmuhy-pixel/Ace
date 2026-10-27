"""Physics I: Mechanics, module 1: Describing motion (kinematics)."""
import math
from verify import Q, sp
T1, T2, T3, T4 = ('Units, dimensions and vectors', 'Motion in one dimension', 'Projectile motion', 'Uniform circular motion')
g = 9.8
r = lambda x, d: round(x + 0.0, d)
assert (0 * 4 + 0.5 * 3 * 16, 0 + 3 * 4) == (24.0, 12) and r(20 ** 2 / (2 * g), 1) == 20.4
vx, vy = 20 * math.cos(math.radians(30)), 20 * math.sin(math.radians(30))
T = 2 * vy / g
assert (r(vx, 2), r(vy, 2), r(T, 2), r(vx * T, 1), r(vy ** 2 / (2 * g), 2)) == (17.32, 10.0, 2.04, 35.3, 5.1)
t_fall = math.sqrt(2 * 20 / g)
assert r(t_fall, 2) == 2.02 and r(15 * t_fall, 1) == 30.3
assert 10 ** 2 / 50 == 2 and r(2 * math.pi * 2 / 4, 2) == 3.14 and r(math.hypot(3, 4), 1) == 5.0 and r(math.degrees(math.atan2(4, 3)), 1) == 53.1
assert r(72 / 3.6, 0) == 20

MODULE = {
    'title': 'Describing motion (kinematics)',
    'topics': [T1, T2, T3, T4],
    'overview': 'Mechanics starts by describing motion precisely, before asking what causes it. This module sets up units and vectors, then the equations for motion with constant acceleration, projectiles moving in two dimensions, and objects moving in circles.',
    'key_terms': ['SI units', 'Vector', 'Scalar', 'Displacement', 'Velocity', 'Acceleration', 'SUVAT equations', 'Projectile', 'Centripetal acceleration', 'Period'],
    'explanation': [
        'Physics uses SI units (metre, kilogram, second) and checks equations with dimensions. Vectors such as displacement, velocity and force have size and direction; scalars such as distance, speed and mass have size only. Vectors are added head-to-tail or by components.',
        'For motion with constant acceleration, the five SUVAT equations link displacement s, initial velocity u, final velocity v, acceleration a and time t. Free fall near the Earth is constant acceleration of g ≈ 9.8 m/s² downwards.',
        'A projectile\'s horizontal and vertical motions are independent: horizontal velocity stays constant (ignoring air resistance) while vertical motion is free fall. Objects moving in a circle at constant speed still accelerate, towards the centre, because their direction keeps changing.'],
    'quick_facts': [
        'v = u + at; s = ut + ½at²; v² = u² + 2as; s = ½(u + v)t.',
        'g ≈ 9.8 m/s² downwards near the Earth\'s surface.',
        'Projectile: horizontal velocity constant; vertical acceleration −g.',
        'Range on level ground R = u² sin 2θ / g, maximum at 45°.',
        'Circular motion: a = v²/r towards the centre; v = 2πr/T.'],
}

NOTES = {
    T1: {
        'overview': 'Physical quantities need units, and many need directions. SI units and vectors are the language of all of mechanics.',
        'key_terms': ['SI base units', 'Prefix', 'Dimensional analysis', 'Scalar', 'Vector', 'Components', 'Resultant'],
        'explanation': [
            'The SI base units used in mechanics are the metre (m), kilogram (kg) and second (s). Derived units combine them: velocity m/s, acceleration m/s², force N = kg·m/s². Prefixes scale units: kilo (10³), centi (10⁻²), milli (10⁻³), micro (10⁻⁶). 72 km/h = 72 000 m ÷ 3600 s = 20 m/s.',
            'Dimensional analysis checks that both sides of an equation have the same dimensions. In s = ut + ½at², each term has dimensions of length, a good sign the equation is correct.',
            'A vector can be split into perpendicular components: a vector of size A at angle θ to the x-axis has components A cos θ and A sin θ. Components add separately, and the resultant has size √(Aₓ² + A_y²) and direction tan⁻¹(A_y/Aₓ). A walk of 3 m east then 4 m north is a displacement of 5 m at about 53° north of east.'],
        'formulas_label': 'Formulas',
        'formulas': ['1 km/h = 1/3.6 m/s', 'Aₓ = A cos θ, A_y = A sin θ', '|A| = √(Aₓ² + A_y²)', 'θ = tan⁻¹(A_y/Aₓ)'],
        'steps': ['Convert all quantities to SI units.', 'Draw vectors and choose axes.', 'Resolve into components.', 'Add components and find the resultant.'],
        'worked_example': {
            'problem': 'A student walks 3 m east and then 4 m north. Find the displacement.',
            'steps': ['Components: x = 3 m, y = 4 m.', 'Size = √(3² + 4²) = 5 m.', 'Direction = tan⁻¹(4/3) ≈ 53.1° north of east.'],
            'answer': '5 m at about 53° north of east.',
            'check': 'The distance walked was 7 m, but the displacement (a vector) is only 5 m ✓.'},
        'mistakes': ['Adding vector magnitudes as if they were scalars.', 'Mixing km and m or hours and seconds.', 'Using sin where cos is needed for the component along the angle.', 'Confusing distance with displacement.'],
        'real_world': 'Pilots and ship navigators add velocity vectors (their own and the wind or current) to work out the heading needed to reach a destination.',
        'exam_strategy': 'Draw a labelled vector diagram before calculating; many marks are given for the correct components.',
        'recap': ['Work in SI units.', 'Vectors have direction.', 'Resolve with cos and sin.', 'Resultant by Pythagoras and tan⁻¹.']},
    T2: {
        'overview': 'For motion in a straight line with constant acceleration, five equations (SUVAT) relate displacement, velocities, acceleration and time.',
        'key_terms': ['Displacement', 'Velocity', 'Acceleration', 'SUVAT', 'Free fall', 'Displacement–time graph', 'Velocity–time graph'],
        'explanation': [
            'Velocity is the rate of change of displacement; acceleration is the rate of change of velocity. On a velocity–time graph, the gradient is acceleration and the area under the line is displacement.',
            'With constant acceleration: v = u + at; s = ut + ½at²; v² = u² + 2as; s = ½(u + v)t; s = vt − ½at². Choose the equation that contains the three known quantities and the one you want. A car starting from rest with a = 3 m/s² travels 24 m in 4 s and reaches 12 m/s.',
            'Free fall: near the Earth, ignoring air resistance, all objects accelerate downwards at g ≈ 9.8 m/s². Choose a positive direction and keep signs consistent: a ball thrown upwards at 20 m/s rises to v² = u² + 2as → 0 = 400 − 2(9.8)s, s ≈ 20.4 m.'],
        'formulas_label': 'SUVAT equations',
        'formulas': ['v = u + at', 's = ut + ½at²', 'v² = u² + 2as', 's = ½(u + v)t', 'g ≈ 9.8 m/s²'],
        'steps': ['Write down s, u, v, a, t, marking the known values.', 'Choose a positive direction.', 'Pick the equation without the unwanted variable.', 'Solve and check the sign and size.'],
        'worked_example': {
            'problem': 'A ball is thrown straight up at 20 m/s. How high does it go?',
            'steps': ['Take upwards as positive: u = 20 m/s, v = 0 at the top, a = −9.8 m/s².', 'v² = u² + 2as gives 0 = 400 − 19.6s.', 's = 400/19.6 ≈ 20.4 m.'],
            'answer': 'About 20.4 m.',
            'check': 'Time to the top is 20/9.8 ≈ 2.0 s, and average speed 10 m/s × 2.0 s ≈ 20 m ✓.'},
        'mistakes': ['Mixing sign conventions (g positive in one step, negative in another).', 'Using SUVAT when acceleration is not constant.', 'Confusing distance and displacement.', 'Thinking velocity is zero means acceleration is zero (at the top, a = −g).'],
        'real_world': 'Road-safety stopping distances are calculated with v² = u² + 2as: doubling the speed roughly quadruples the braking distance.',
        'exam_strategy': 'List s, u, v, a, t at the start of every kinematics question. It makes choosing the equation automatic.',
        'recap': ['Gradient of v–t is a; area is s.', 'Five SUVAT equations.', 'Free fall: a = 9.8 m/s² down.', 'Fix a sign convention.']},
    T3: {
        'overview': 'A projectile moves under gravity alone after launch. Its horizontal and vertical motions are independent, so each can be solved with one-dimensional equations.',
        'key_terms': ['Projectile', 'Horizontal component', 'Vertical component', 'Time of flight', 'Range', 'Maximum height'],
        'explanation': [
            'Resolve the launch velocity: uₓ = u cos θ and u_y = u sin θ. Horizontally there is no acceleration (ignoring air resistance), so x = uₓt. Vertically, a = −g, so the SUVAT equations apply.',
            'The time links the two directions. On level ground, time of flight T = 2u_y/g, range R = uₓT = u² sin 2θ / g (largest at 45°), and maximum height H = u_y²/(2g).',
            'For a horizontal launch from a height h, u_y = 0, so the fall time is t = √(2h/g) and the horizontal distance is uₓt. A stone thrown horizontally at 15 m/s from a 20 m cliff takes about 2.02 s to fall and lands about 30.3 m out.'],
        'formulas_label': 'Formulas',
        'formulas': ['uₓ = u cos θ, u_y = u sin θ', 'x = uₓt; y = u_y t − ½gt²', 'T = 2u sin θ / g (level ground)', 'R = u² sin 2θ / g', 'H = (u sin θ)²/(2g)'],
        'steps': ['Resolve the initial velocity.', 'Use vertical motion to find the time.', 'Use horizontal motion with that time.', 'Combine components if the final velocity is needed.'],
        'worked_example': {
            'problem': 'A ball is kicked at 20 m/s at 30° above level ground. Find the time of flight, range and maximum height.',
            'steps': ['uₓ = 20 cos 30° ≈ 17.32 m/s; u_y = 20 sin 30° = 10 m/s.', 'T = 2 × 10/9.8 ≈ 2.04 s; R = 17.32 × 2.04 ≈ 35.3 m.', 'H = 10²/(2 × 9.8) ≈ 5.10 m.'],
            'answer': 'Time ≈ 2.04 s, range ≈ 35.3 m, maximum height ≈ 5.10 m.',
            'check': 'R = u² sin 60°/g = 400 × 0.866/9.8 ≈ 35.3 m ✓.'},
        'mistakes': ['Applying g to the horizontal motion.', 'Using the full speed instead of a component.', 'Using the range formula when launch and landing heights differ.', 'Thinking the horizontal velocity is zero at the top (only the vertical component is).'],
        'real_world': 'Athletes and sports analysts use projectile motion to optimise throwing and jumping angles; air resistance and release height make the best angle a little below 45° in practice.',
        'exam_strategy': 'Split your working into two labelled columns, "horizontal" and "vertical", with time as the shared link.',
        'recap': ['Resolve the velocity.', 'Horizontal: constant velocity.', 'Vertical: free fall.', 'Time links the two.']},
    T4: {
        'overview': 'An object moving in a circle at constant speed is still accelerating, because its direction changes. The acceleration points towards the centre.',
        'key_terms': ['Uniform circular motion', 'Period T', 'Frequency f', 'Angular velocity ω', 'Centripetal acceleration', 'Radian'],
        'explanation': [
            'For an object going round a circle of radius r once every period T, the speed is v = 2πr/T. The frequency f = 1/T is the number of revolutions per second, and the angular velocity ω = 2π/T = v/r is measured in radians per second.',
            'Because the velocity direction keeps changing, there is a centripetal (centre-seeking) acceleration a = v²/r = ω²r, directed towards the centre. A car taking a bend of radius 50 m at 10 m/s has a centripetal acceleration of 2 m/s².',
            'Something must supply the force for this acceleration (friction, tension, gravity or a normal force), which is studied in the next module. If that force disappears, the object moves off in a straight line along the tangent, not outwards.'],
        'formulas_label': 'Formulas',
        'formulas': ['v = 2πr/T', 'f = 1/T', 'ω = 2π/T = v/r', 'a = v²/r = ω²r (towards the centre)'],
        'steps': ['Find the radius and the period or speed.', 'Compute v (or ω).', 'Use a = v²/r.', 'State that the direction is towards the centre.'],
        'worked_example': {
            'problem': 'A child on a roundabout sits 2 m from the centre and goes round once every 4 s. Find her speed and centripetal acceleration.',
            'steps': ['v = 2π × 2 / 4 = π ≈ 3.14 m/s.', 'a = v²/r = π²/2 ≈ 4.93 m/s².', 'The acceleration points towards the centre.'],
            'answer': 'v ≈ 3.14 m/s; a ≈ 4.93 m/s² towards the centre.',
            'check': 'Using ω = 2π/4 = π/2 rad/s: a = ω²r = (π²/4) × 2 ≈ 4.93 ✓.'},
        'mistakes': ['Saying there is no acceleration at constant speed.', 'Putting the acceleration outwards.', 'Using degrees instead of radians in ω.', 'Confusing frequency with angular velocity.'],
        'real_world': 'Road engineers bank curves and set speed limits on bends so that friction can supply the required centripetal force even when the road is wet.',
        'exam_strategy': 'Always state the direction of the acceleration ("towards the centre"); questions often award a separate mark for it.',
        'recap': ['v = 2πr/T.', 'a = v²/r towards the centre.', 'ω = v/r in rad/s.', 'No force: straight-line motion along the tangent.']},
}

QUESTIONS = [
    # T1
    Q(T1, '72 km/h in m/s is:', ['20 m/s', '72 m/s', '259 m/s', '2 m/s'], 0, '72 ÷ 3.6.'),
    Q(T1, 'Which is a vector?', ['Velocity', 'Speed', 'Mass', 'Time'], 0, 'It has magnitude and direction.'),
    Q(T1, '3 m east then 4 m north. The size of the displacement is:', ['5 m', '7 m', '1 m', '12 m'], 0, '√(9 + 16).'),
    Q(T1, 'The x-component of a 10 N force at 60° to the x-axis is:', ['5 N', '8.66 N', '10 N', '0 N'], 0, '10 cos 60°.'),
    Q(T1, 'The SI unit of force, the newton, equals:', ['kg·m/s²', 'kg·m/s', 'kg/s²', 'm/s²'], 0, 'F = ma.'),
    Q(T1, 'The direction of the 3 m east, 4 m north displacement is about:', ['53° north of east', '37° north of east', '45° north of east', 'due north'], 0, 'tan⁻¹(4/3).'),
    # T2
    Q(T2, 'A car starts from rest with a = 3 m/s². Its speed after 4 s is:', ['12 m/s', '24 m/s', '7 m/s', '0.75 m/s'], 0, 'v = u + at.'),
    Q(T2, 'The same car\'s displacement after 4 s is:', ['24 m', '12 m', '48 m', '6 m'], 0, 's = ½at² = ½ × 3 × 16.'),
    Q(T2, 'A ball thrown up at 20 m/s rises to about:', ['20.4 m', '2.04 m', '40.8 m', '10.2 m'], 0, 'v² = u² − 2gs.'),
    Q(T2, 'The gradient of a velocity–time graph gives:', ['acceleration', 'displacement', 'speed', 'force'], 0, 'Rate of change of velocity.'),
    Q(T2, 'The area under a velocity–time graph gives:', ['displacement', 'acceleration', 'jerk', 'force'], 0, 'Velocity × time.'),
    Q(T2, 'At the top of its flight, a ball thrown straight up has:', ['zero velocity and acceleration g downwards', 'zero acceleration', 'zero velocity and zero acceleration', 'maximum speed'], 0, 'Gravity still acts.'),
    # T3
    Q(T3, 'A ball is kicked at 20 m/s at 30°. The horizontal component of velocity is about:', ['17.3 m/s', '10.0 m/s', '20.0 m/s', '11.5 m/s'], 0, '20 cos 30°.'),
    Q(T3, 'Its time of flight on level ground, to 2 d.p., is:', ['2.04 s', '1.02 s', '3.53 s', '4.08 s'], 0, '2 × 10/9.8.'),
    Q(T3, 'Its range, to 1 d.p., is:', ['35.3 m', '17.7 m', '40.8 m', '20.4 m'], 0, '17.32 × 2.04.'),
    Q(T3, 'A stone is thrown horizontally at 15 m/s from a 20 m cliff. It lands about how far out?', ['30.3 m', '15.0 m', '20.0 m', '45.0 m'], 0, 't = √(40/9.8) ≈ 2.02 s; 15 × 2.02.'),
    Q(T3, 'Ignoring air resistance, the range on level ground is greatest at a launch angle of:', ['45°', '30°', '60°', '90°'], 0, 'sin 2θ is largest at 2θ = 90°.'),
    Q(T3, 'During a projectile\'s flight (no air resistance), its horizontal velocity:', ['stays constant', 'increases', 'decreases', 'becomes zero at the top'], 0, 'No horizontal force.'),
    # T4
    Q(T4, 'A car takes a bend of radius 50 m at 10 m/s. Its centripetal acceleration is:', ['2 m/s²', '0.2 m/s²', '5 m/s²', '500 m/s²'], 0, 'v²/r = 100/50.', ans=2),
    Q(T4, 'A child 2 m from the centre goes round once every 4 s. Her speed, to 2 d.p., is:', ['3.14 m/s', '0.50 m/s', '1.57 m/s', '6.28 m/s'], 0, '2π × 2/4 = π.'),
    Q(T4, 'The centripetal acceleration points:', ['towards the centre of the circle', 'away from the centre', 'along the tangent', 'upwards'], 0, 'Centre-seeking.'),
    Q(T4, 'An object moves in a circle at constant speed. Its acceleration is:', ['non-zero, because its direction changes', 'zero', 'along its velocity', 'always g'], 0, 'Velocity is a vector.'),
    Q(T4, 'If the string of a whirled stone breaks, the stone moves:', ['along the tangent in a straight line', 'straight outwards', 'towards the centre', 'in a smaller circle'], 0, 'No more centripetal force.'),
    Q(T4, 'A wheel turns at 2 revolutions per second. Its angular velocity is:', ['4π rad/s', '2 rad/s', 'π rad/s', '2π rad/s'], 0, 'ω = 2πf.'),
]

FLASH = [
    ['Vector vs scalar', 'Vectors have direction (velocity, force); scalars do not (speed, mass).'],
    ['Components', 'Aₓ = A cos θ, A_y = A sin θ.'],
    ['SUVAT', 'v = u + at; s = ut + ½at²; v² = u² + 2as; s = ½(u + v)t.'],
    ['Free fall', 'a = g ≈ 9.8 m/s² downwards.'],
    ['Projectile independence', 'Horizontal: constant velocity. Vertical: free fall.'],
    ['Range on level ground', 'R = u² sin 2θ / g, maximum at 45°.'],
    ['Circular speed', 'v = 2πr/T.'],
    ['Centripetal acceleration', 'a = v²/r towards the centre.'],
]
