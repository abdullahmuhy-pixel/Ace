"""Physics I: Mechanics, module 2: Forces and Newton's laws."""
import math
from verify import Q
T1, T2, T3, T4 = ('Newton\'s laws of motion', 'Weight, normal force, tension and friction', 'Inclined planes and connected objects', 'Forces in circular motion')
g = 9.8
r = lambda x, d: round(x + 0.0, d)
assert 1200 * 2.5 == 3000 and r(60 * g, 0) == 588
f = 0.3 * 10 * g
assert r(f, 1) == 29.4 and r((50 - f) / 10, 2) == 2.06
assert r(g * math.sin(math.radians(30)), 1) == 4.9 and r(5 * g * math.cos(math.radians(30)), 1) == 42.4
a_at = (5 - 3) * g / 8
assert r(a_at, 2) == 2.45 and r(3 * (g + a_at), 2) == 36.75
assert r(70 * (g + 2), 0) == 826 and r(70 * (g - 2), 0) == 546
assert 1000 * 10 ** 2 / 50 == 2000 and r(10 ** 2 / (50 * g), 3) == 0.204 and r(math.sqrt(0.5 * g * 40), 1) == 14.0
assert r(0.25 * 4 * g, 1) == 9.8

MODULE = {
    'title': 'Forces and Newton\'s laws',
    'topics': [T1, T2, T3, T4],
    'overview': 'Newton\'s three laws explain why objects move as they do. This module introduces the laws, the common forces met in mechanics problems, and the free-body-diagram method for solving problems on slopes, with ropes and pulleys, and in circular motion.',
    'key_terms': ['Force', 'Newton\'s first law', 'Inertia', 'Newton\'s second law', 'Newton\'s third law', 'Free-body diagram', 'Weight', 'Normal force', 'Tension', 'Friction', 'Centripetal force'],
    'explanation': [
        'Newton\'s first law: an object stays at rest or moves at constant velocity unless a resultant force acts. The second law: resultant force = mass × acceleration (F = ma). The third law: when A pushes on B, B pushes back on A with an equal and opposite force.',
        'Most problems use a handful of forces: weight (mg, downwards), the normal force from a surface (perpendicular to it), tension in strings and ropes, and friction (parallel to the surface, opposing sliding). Drawing a free-body diagram for each object is the most important step.',
        'Choosing axes along and perpendicular to the motion turns each problem into two simple equations. In circular motion, the resultant force must point towards the centre and equal mv²/r; it is supplied by real forces such as friction or tension, not by a separate "centripetal force".'],
    'quick_facts': [
        'ΣF = ma (vector equation).',
        'Weight W = mg, with g ≈ 9.8 N/kg.',
        'Kinetic friction f = μN; static friction up to μₛN.',
        'On a slope of angle θ: component of weight along the slope = mg sin θ; normal force = mg cos θ (no other perpendicular forces).',
        'Circular motion: ΣF towards the centre = mv²/r.'],
}

NOTES = {
    T1: {
        'overview': 'Newton\'s three laws link force and motion. They are the foundation of classical mechanics, from bicycles to rockets.',
        'key_terms': ['Resultant force', 'Inertia', 'Equilibrium', 'F = ma', 'Newton (unit)', 'Action–reaction pair'],
        'explanation': [
            'First law: with no resultant force, velocity does not change. Inertia is the tendency of an object to keep its state of motion; mass measures inertia. An object at rest or moving at constant velocity is in equilibrium (ΣF = 0).',
            'Second law: ΣF = ma. A resultant force of 1 N gives a 1 kg mass an acceleration of 1 m/s². Forces are vectors, so add them with directions before using the law. A 1200 kg car accelerating at 2.5 m/s² needs a resultant force of 3000 N.',
            'Third law: forces come in pairs, equal in size, opposite in direction and acting on different objects. The Earth pulls you down with your weight and you pull the Earth up with an equal force. Weight and the normal force on a book on a table are not a third-law pair: they act on the same object.'],
        'formulas_label': 'Laws',
        'formulas': ['First law: ΣF = 0 ⇒ constant velocity', 'Second law: ΣF = ma', 'Third law: F_AB = −F_BA (on different objects)', '1 N = 1 kg·m/s²'],
        'steps': ['Identify the object.', 'Draw its free-body diagram.', 'Find the resultant force.', 'Apply ΣF = ma along each axis.'],
        'worked_example': {
            'problem': 'A 1200 kg car accelerates from rest to 15 m/s in 6 s. What resultant force acts on it?',
            'steps': ['a = (15 − 0)/6 = 2.5 m/s².', 'ΣF = ma = 1200 × 2.5.', 'ΣF = 3000 N in the direction of motion.'],
            'answer': '3000 N.',
            'check': 'The engine force must be larger than 3000 N, because friction and air resistance also act backwards.'},
        'mistakes': ['Thinking a moving object needs a resultant force to keep moving at constant velocity.', 'Using one force instead of the resultant in F = ma.', 'Calling weight and normal force a third-law pair.', 'Forgetting forces are vectors.'],
        'real_world': 'Seat belts work because of the first law: in a crash the car stops but your body keeps moving until the belt applies a force.',
        'exam_strategy': 'Draw a free-body diagram even when not asked. Examiners often award marks for it, and it prevents missing forces.',
        'recap': ['No resultant force: constant velocity.', 'ΣF = ma.', 'Third-law pairs act on different objects.', 'Use the resultant.']},
    T2: {
        'overview': 'A few forces appear in almost every mechanics problem: weight, the normal force, tension and friction.',
        'key_terms': ['Weight', 'Mass', 'Normal force', 'Tension', 'Static friction', 'Kinetic friction', 'Coefficient of friction μ', 'Apparent weight'],
        'explanation': [
            'Weight W = mg is the gravitational force on a mass, with g ≈ 9.8 N/kg at the Earth\'s surface; a 60 kg person weighs about 588 N. Mass (kg) is the same everywhere; weight changes with g.',
            'The normal force is the push of a surface, perpendicular to it. It is not always equal to mg: in a lift accelerating upwards at 2 m/s², a 70 kg person feels N = m(g + a) ≈ 826 N, more than their weight. Tension is the pull of a string or rope, the same throughout a light string over a smooth pulley.',
            'Friction opposes sliding. Static friction can take any value up to μₛN to prevent motion; once sliding, kinetic friction is f = μₖN. A 10 kg block on a level floor with μₖ = 0.3 has f = 0.3 × 98 = 29.4 N; pushing with 50 N gives a = (50 − 29.4)/10 ≈ 2.06 m/s².'],
        'formulas_label': 'Formulas',
        'formulas': ['W = mg', 'Kinetic friction f = μₖN', 'Static friction f ≤ μₛN', 'Lift: N = m(g + a) going up, m(g − a) going down'],
        'steps': ['Draw all forces on the object.', 'Find N from the perpendicular direction.', 'Compute friction from N.', 'Apply ΣF = ma along the motion.'],
        'worked_example': {
            'problem': 'A 10 kg block is pushed across a level floor by a 50 N horizontal force. μₖ = 0.3. Find its acceleration.',
            'steps': ['N = mg = 10 × 9.8 = 98 N.', 'Friction = 0.3 × 98 = 29.4 N.', 'a = (50 − 29.4)/10 ≈ 2.06 m/s².'],
            'answer': 'About 2.06 m/s².',
            'check': 'A push smaller than the friction force could not make the block speed up, so 50 N > 29.4 N is consistent ✓.'},
        'mistakes': ['Confusing mass and weight.', 'Assuming N = mg when there are other vertical forces or an incline.', 'Using μ × m instead of μ × N.', 'Making friction act in the direction of motion.'],
        'real_world': 'Anti-lock brakes keep tyres just below sliding, because static friction can exceed kinetic friction and gives shorter stopping distances.',
        'exam_strategy': 'Write "N = …" from the perpendicular equation before you calculate friction; most friction errors come from the wrong N.',
        'recap': ['W = mg.', 'N is perpendicular and not always mg.', 'f = μN.', 'Friction opposes sliding.']},
    T3: {
        'overview': 'Slopes and connected objects are solved with the same method: free-body diagrams, sensible axes and ΣF = ma for each object.',
        'key_terms': ['Inclined plane', 'Resolving forces', 'Connected particles', 'Pulley', 'Atwood machine', 'System'],
        'explanation': [
            'On a slope of angle θ, take axes along and perpendicular to the slope. The weight splits into mg sin θ down the slope and mg cos θ into the slope. Without friction, a block slides with a = g sin θ; on a 30° slope that is 4.9 m/s². The normal force is mg cos θ (42.4 N for a 5 kg block at 30°).',
            'For objects joined by a light, inextensible string, they share the same acceleration and the tension is the same at both ends (over a smooth pulley). Write ΣF = ma for each object, then solve the simultaneous equations.',
            'An Atwood machine has masses m₁ and m₂ hanging over a pulley: a = (m₂ − m₁)g/(m₁ + m₂). With 3 kg and 5 kg, a = 2 × 9.8/8 = 2.45 m/s² and the tension is T = m₁(g + a) = 36.75 N.'],
        'formulas_label': 'Formulas',
        'formulas': ['Along a slope: mg sin θ', 'Perpendicular: N = mg cos θ', 'Frictionless slope: a = g sin θ', 'Atwood: a = (m₂ − m₁)g/(m₁ + m₂)', 'Tension: T = m₁(g + a) for the rising mass'],
        'steps': ['Draw a free-body diagram for each object.', 'Choose axes along the motion.', 'Write ΣF = ma for each object.', 'Solve for a and T together.', 'Check the limits (for example equal masses give a = 0).'],
        'worked_example': {
            'problem': 'Masses of 3 kg and 5 kg hang over a light, smooth pulley. Find the acceleration and the tension.',
            'steps': ['For 5 kg (moving down): 5g − T = 5a. For 3 kg (moving up): T − 3g = 3a.', 'Adding: 2g = 8a, so a = 2.45 m/s².', 'T = 3(9.8 + 2.45) = 36.75 N.'],
            'answer': 'a = 2.45 m/s²; T ≈ 36.8 N.',
            'check': 'T lies between the two weights (29.4 N and 49 N), as it must ✓.'},
        'mistakes': ['Swapping sin and cos on a slope.', 'Using different accelerations for connected objects.', 'Forgetting tension acts on both objects.', 'Taking N = mg on a slope.'],
        'real_world': 'Lifts use a counterweight like an Atwood machine, so the motor only has to provide the difference between the car and the counterweight.',
        'exam_strategy': 'Write one ΣF = ma equation per object in the same direction of motion, then add them to eliminate T.',
        'recap': ['Resolve weight along and across the slope.', 'Connected objects share a.', 'One equation per object.', 'Check limiting cases.']},
    T4: {
        'overview': 'For an object to move in a circle, a resultant force must point towards the centre. Real forces such as friction, tension and gravity provide it.',
        'key_terms': ['Centripetal force', 'Resultant force', 'Friction on a bend', 'Banked curve', 'Vertical circle', 'Apparent weightlessness'],
        'explanation': [
            'Applying ΣF = ma with a = v²/r gives ΣF = mv²/r towards the centre. For a 1000 kg car on a 50 m bend at 10 m/s, the inward force needed is 2000 N, supplied by friction between tyres and road.',
            'On a flat bend, the maximum speed is set by the friction limit: μmg = mv²/r gives v = √(μgr). With μ = 0.5 and r = 40 m, v = 14 m/s. Banking the road lets part of the normal force point inwards, allowing higher speeds.',
            'In a vertical circle, the required inward force changes around the loop. At the top of a loop, weight and the normal force both point down towards the centre; at the bottom, the normal force must exceed the weight. Astronauts in orbit feel weightless because they and their craft are in free fall together, with gravity providing exactly the centripetal force.'],
        'formulas_label': 'Formulas',
        'formulas': ['ΣF (towards centre) = mv²/r', 'Flat bend: v_max = √(μgr)', 'Minimum μ = v²/(rg)', 'Top of loop: N + mg = mv²/r'],
        'steps': ['Identify the real forces acting.', 'Find the component towards the centre.', 'Set it equal to mv²/r.', 'Solve for the unknown.'],
        'worked_example': {
            'problem': 'A 1000 kg car takes a flat bend of radius 50 m at 10 m/s. Find the friction force needed and the minimum coefficient of friction.',
            'steps': ['F = mv²/r = 1000 × 100/50 = 2000 N.', 'Friction must supply this: μmg ≥ 2000.', 'μ ≥ 2000/(1000 × 9.8) ≈ 0.204.'],
            'answer': 'Friction of 2000 N; μ must be at least about 0.20.',
            'check': 'Dry tarmac has μ around 0.7, so the car is safe; on ice (μ ≈ 0.1) it would skid.'},
        'mistakes': ['Adding "centripetal force" as an extra force on the diagram.', 'Thinking an outward force acts on the object (there is no centrifugal force in an inertial frame).', 'Forgetting that weight points to the centre at the top of a vertical loop.', 'Using r as a diameter.'],
        'real_world': 'Racing tracks are banked on curves so cars can corner faster than friction alone would allow.',
        'exam_strategy': 'Name the force that provides the centripetal force in your answer ("friction between the tyres and road provides the centripetal force").',
        'recap': ['ΣF inwards = mv²/r.', 'Real forces supply it.', 'v_max = √(μgr) on a flat bend.', 'Orbit: free fall around the planet.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A 1200 kg car accelerates at 2.5 m/s². The resultant force is:', ['3000 N', '480 N', '1202.5 N', '300 N'], 0, 'F = ma.'),
    Q(T1, 'An object moves at constant velocity. The resultant force on it is:', ['zero', 'in the direction of motion', 'opposite to the motion', 'equal to its weight'], 0, 'Newton\'s first law.'),
    Q(T1, 'Newton\'s third-law pair forces act on:', ['different objects', 'the same object', 'only moving objects', 'only objects in contact'], 0, 'Equal and opposite, on different bodies.'),
    Q(T1, 'A resultant force of 12 N acts on a 4 kg mass. Its acceleration is:', ['3 m/s²', '48 m/s²', '0.33 m/s²', '16 m/s²'], 0, 'a = F/m.'),
    Q(T1, 'Mass is a measure of:', ['inertia', 'weight', 'volume', 'speed'], 0, 'Resistance to changes in motion.'),
    Q(T1, 'A book rests on a table. The third-law partner of the Earth\'s pull on the book is:', ['the book\'s pull on the Earth', 'the table\'s push on the book', 'the book\'s push on the table', 'friction'], 0, 'Gravitational forces between the same two bodies.'),
    # T2
    Q(T2, 'The weight of a 60 kg person (g = 9.8 N/kg) is about:', ['588 N', '60 N', '6.1 N', '600 kg'], 0, 'W = mg.'),
    Q(T2, 'A 10 kg block on a level floor, μₖ = 0.3. The friction force is:', ['29.4 N', '3 N', '98 N', '0.3 N'], 0, 'μN = 0.3 × 98.'),
    Q(T2, 'Pushed by 50 N, that block accelerates at about:', ['2.06 m/s²', '5.00 m/s²', '7.94 m/s²', '0.48 m/s²'], 0, '(50 − 29.4)/10.'),
    Q(T2, 'A 70 kg person stands in a lift accelerating upwards at 2 m/s². The normal force is about:', ['826 N', '686 N', '546 N', '140 N'], 0, 'N = m(g + a).'),
    Q(T2, 'The same person when the lift accelerates downwards at 2 m/s²:', ['546 N', '826 N', '686 N', '0 N'], 0, 'N = m(g − a).'),
    Q(T2, 'Kinetic friction acts:', ['opposite to the direction of sliding', 'in the direction of motion', 'perpendicular to the surface', 'upwards'], 0, 'It opposes relative motion.'),
    # T3
    Q(T3, 'A block slides down a frictionless 30° slope. Its acceleration is:', ['4.9 m/s²', '9.8 m/s²', '8.5 m/s²', '0 m/s²'], 0, 'g sin 30°.'),
    Q(T3, 'The normal force on a 5 kg block on a 30° slope is about:', ['42.4 N', '24.5 N', '49 N', '5 N'], 0, 'mg cos 30°.'),
    Q(T3, 'Masses of 3 kg and 5 kg hang over a smooth pulley. The acceleration is:', ['2.45 m/s²', '9.8 m/s²', '4.9 m/s²', '1.25 m/s²'], 0, '(5 − 3)g/8.'),
    Q(T3, 'In that system the tension is about:', ['36.75 N', '29.4 N', '49 N', '78.4 N'], 0, '3(9.8 + 2.45).'),
    Q(T3, 'Two equal masses hang over a smooth pulley. Their acceleration is:', ['0', 'g', 'g/2', '2g'], 0, 'The weights balance.'),
    Q(T3, 'On a slope, the component of weight along the slope is:', ['mg sin θ', 'mg cos θ', 'mg tan θ', 'mg'], 0, 'θ is the slope angle.'),
    # T4
    Q(T4, 'A 1000 kg car takes a 50 m radius bend at 10 m/s. The inward force needed is:', ['2000 N', '200 N', '500 N', '20000 N'], 0, 'mv²/r.'),
    Q(T4, 'The minimum coefficient of friction for that bend is about:', ['0.20', '2.0', '0.05', '0.50'], 0, 'v²/(rg) = 100/490.'),
    Q(T4, 'With μ = 0.5 and r = 40 m, the maximum safe speed on a flat bend is:', ['14 m/s', '20 m/s', '196 m/s', '4.4 m/s'], 0, '√(μgr) = √196.'),
    Q(T4, 'For a car on a flat bend, the centripetal force is provided by:', ['friction between tyres and road', 'the engine', 'a centrifugal force', 'the car\'s weight'], 0, 'Friction points towards the centre.'),
    Q(T4, 'Astronauts in orbit feel weightless because:', ['they and their craft are in free fall together', 'there is no gravity in space', 'their mass is zero', 'the craft is too far from the Earth'], 0, 'Gravity is still about 90% of its surface value at the space station.'),
    Q(T4, 'A 0.25 kg ball on a string moves in a horizontal circle of radius 1 m with speed 2 m/s (ignore gravity). The tension is:', ['1 N', '0.5 N', '2 N', '4 N'], 0, 'mv²/r = 0.25 × 4/1.'),
]

FLASH = [
    ['Newton\'s first law', 'No resultant force: constant velocity.'],
    ['Newton\'s second law', 'ΣF = ma.'],
    ['Newton\'s third law', 'Equal and opposite forces on different objects.'],
    ['Weight', 'W = mg; g ≈ 9.8 N/kg.'],
    ['Kinetic friction', 'f = μₖN, opposing sliding.'],
    ['Slope components', 'Along: mg sin θ; normal force: mg cos θ.'],
    ['Atwood machine', 'a = (m₂ − m₁)g/(m₁ + m₂).'],
    ['Circular motion force', 'ΣF towards the centre = mv²/r.'],
]
