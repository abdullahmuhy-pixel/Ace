"""Physics I: Mechanics, module 4: Momentum and collisions."""
from verify import Q
T1, T2, T3, T4 = ('Momentum and impulse', 'Conservation of momentum', 'Elastic and inelastic collisions', 'Explosions, recoil and centre of mass')
g = 9.8
r = lambda x, d: round(x + 0.0, d)
assert r(0.15 * 40, 6) == 6 and r(2000 * 0.01, 6) == 20
assert r(0.5 * (4 - (-6)), 6) == 5 and r(5 / 0.02, 6) == 250
assert 70 * 15 / 0.1 == 10500 and 70 * 15 / 0.5 == 2100
assert 2 * 3 / 3 == 2 and 0.5 * 2 * 9 == 9 and 0.5 * 3 * 4 == 6
assert 10000 * 4 / 16000 == 2.5
m1, u1, m2 = 1, 4, 3
v1 = (m1 - m2) / (m1 + m2) * u1; v2 = 2 * m1 / (m1 + m2) * u1
assert (v1, v2) == (-2, 2) and 0.5 * m1 * u1 ** 2 == 0.5 * m1 * v1 ** 2 + 0.5 * m2 * v2 ** 2
assert r(0.01 * 400 / 4, 6) == 1 and 1 * 6 / 2 == 3 and 40 * 3 / 60 == 2
assert (2 * 0 + 3 * 5) / 5 == 3
vb = 0.01 * 300 / 2.01
assert r(vb, 2) == 1.49 and r(vb ** 2 / (2 * g), 3) == 0.114

MODULE = {
    'title': 'Momentum and collisions',
    'topics': [T1, T2, T3, T4],
    'overview': 'Momentum is mass times velocity, and in any isolated system it is conserved. This module covers momentum and impulse, the conservation law, how collisions differ in what happens to kinetic energy, and explosions, recoil and the centre of mass.',
    'key_terms': ['Momentum', 'Impulse', 'Isolated system', 'Conservation of momentum', 'Elastic collision', 'Inelastic collision', 'Perfectly inelastic', 'Recoil', 'Explosion', 'Centre of mass'],
    'explanation': [
        'Momentum p = mv is a vector, measured in kg·m/s. A resultant force changes momentum: FΔt = Δp, the impulse. Spreading the change over a longer time reduces the force, which is the idea behind airbags and crumple zones.',
        'In an isolated system (no external resultant force), total momentum before an event equals total momentum after. This holds for every collision and explosion, whether or not kinetic energy is conserved.',
        'In elastic collisions kinetic energy is also conserved; in inelastic ones some becomes heat, sound and deformation. When objects stick together the loss is the largest possible. Explosions start with zero momentum, so the pieces move apart with equal and opposite momenta.'],
    'quick_facts': [
        'p = mv (kg·m/s), a vector.',
        'Impulse = FΔt = Δp (N·s).',
        'Isolated system: Σp before = Σp after.',
        'Elastic: KE conserved; inelastic: KE lost.',
        'Centre of mass: x̄ = Σmx/Σm.'],
}

NOTES = {
    T1: {
        'overview': 'Momentum combines mass and velocity. Impulse, the product of force and time, tells us how much momentum changes.',
        'key_terms': ['Momentum', 'Impulse', 'Newton\'s second law in momentum form', 'Force–time graph', 'Contact time', 'Rebound'],
        'explanation': [
            'p = mv. A 0.15 kg cricket ball at 40 m/s has momentum 6 kg·m/s. Because velocity has a direction, momentum does too: choose a positive direction and give velocities the opposite way a minus sign.',
            'Newton\'s second law can be written F = Δp/Δt, so the impulse FΔt equals the change in momentum. A 2000 N force acting for 0.01 s gives an impulse of 20 N·s. On a force–time graph, the impulse is the area under the curve.',
            'Rebounds double up the change. A 0.5 kg ball hits a wall at 6 m/s and bounces back at 4 m/s: Δp = 0.5 × (4 − (−6)) = 5 kg·m/s. If contact lasts 0.02 s, the average force is 250 N. A 70 kg passenger stopped from 15 m/s in 0.1 s feels 10 500 N; an airbag stretching that to 0.5 s cuts it to 2100 N.'],
        'formulas_label': 'Formulas',
        'formulas': ['p = mv', 'Impulse J = FΔt = Δp', 'F = Δp/Δt', 'Δp = m(v − u)'],
        'steps': ['Choose a positive direction.', 'Write initial and final momenta with signs.', 'Find Δp = p_final − p_initial.', 'Divide by Δt for the average force.'],
        'worked_example': {
            'problem': 'A 0.5 kg ball hits a wall at 6 m/s and rebounds at 4 m/s. Contact lasts 0.02 s. Find the impulse and the average force from the wall.',
            'steps': ['Take away from the wall as positive: u = −6 m/s, v = +4 m/s.', 'Δp = 0.5 × (4 − (−6)) = 5 kg·m/s.', 'F = 5/0.02 = 250 N, directed away from the wall.'],
            'answer': 'Impulse 5 N·s; average force 250 N.',
            'check': 'Forgetting the sign change would give only 1 kg·m/s; a rebound always changes momentum more than stopping does ✓.'},
        'mistakes': ['Ignoring the direction change in a rebound.', 'Treating momentum as a scalar.', 'Mixing up impulse and force.', 'Using grams instead of kilograms.'],
        'real_world': 'Gymnasts land on thick mats and bend their knees to increase the stopping time and reduce the force on their joints.',
        'exam_strategy': 'Always state your positive direction at the start; it removes most sign errors.',
        'recap': ['p = mv.', 'FΔt = Δp.', 'Longer Δt, smaller F.', 'Rebounds: watch the sign.']},
    T2: {
        'overview': 'In an isolated system, total momentum never changes. This single law solves collisions, coupling and recoil problems.',
        'key_terms': ['Isolated system', 'External force', 'Internal force', 'Total momentum', 'Coupling', 'Before-and-after diagram'],
        'explanation': [
            'Forces between objects inside a system are equal and opposite (Newton\'s third law), so they change each object\'s momentum by equal and opposite amounts. The total stays the same if no external resultant force acts.',
            'Draw a before-and-after diagram with masses and velocities, then write Σp before = Σp after. A 2 kg trolley at 3 m/s hits a stationary 1 kg trolley and they stick: 2 × 3 = 3v, so v = 2 m/s.',
            'Railway wagons work the same way: a 10 000 kg wagon at 4 m/s couples with a stationary 6000 kg wagon, and they move off together at 40 000/16 000 = 2.5 m/s. Friction during the brief collision is small compared with the collision forces, so we treat the system as isolated.'],
        'formulas_label': 'Formulas',
        'formulas': ['m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂', 'Sticking together: m₁u₁ + m₂u₂ = (m₁ + m₂)v'],
        'steps': ['Draw before and after diagrams.', 'Choose a positive direction.', 'Write total momentum before and after.', 'Solve for the unknown velocity.', 'Interpret the sign of the answer.'],
        'worked_example': {
            'problem': 'A 10 000 kg railway wagon moving at 4 m/s collides with and couples to a stationary 6000 kg wagon. Find their common speed.',
            'steps': ['Momentum before = 10 000 × 4 + 0 = 40 000 kg·m/s.', 'After: (10 000 + 6000)v = 16 000v.', 'v = 40 000/16 000 = 2.5 m/s.'],
            'answer': '2.5 m/s in the original direction.',
            'check': 'The combined wagon is slower than 4 m/s but still moving forwards, as expected ✓.'},
        'mistakes': ['Forgetting the mass of the stationary object after coupling.', 'Dropping minus signs for objects moving the other way.', 'Assuming kinetic energy is conserved too.', 'Applying conservation when a large external force acts.'],
        'real_world': 'Forensic investigators use skid marks and conservation of momentum to work out how fast cars were travelling before a crash.',
        'exam_strategy': 'Give your final velocity with a direction; a negative answer means the object moves opposite to your positive direction.',
        'recap': ['Σp before = Σp after.', 'Holds when external forces are negligible.', 'Draw before and after.', 'Signs give direction.']},
    T3: {
        'overview': 'Momentum is conserved in every collision, but kinetic energy is not. The type of collision depends on what happens to kinetic energy.',
        'key_terms': ['Elastic collision', 'Inelastic collision', 'Perfectly inelastic', 'Kinetic energy loss', 'Ballistic pendulum'],
        'explanation': [
            'In an elastic collision, total kinetic energy is unchanged (approximately true for snooker balls and gas molecules). In an inelastic collision, some kinetic energy becomes heat, sound and deformation. When objects stick together, the collision is perfectly inelastic and the kinetic energy lost is the most possible.',
            'For the 2 kg trolley at 3 m/s that sticks to a 1 kg trolley: KE before = 9 J, KE after = ½ × 3 × 2² = 6 J, so 3 J is lost. For a head-on elastic collision of a 1 kg ball at 4 m/s with a stationary 3 kg ball, the results are v₁ = −2 m/s and v₂ = +2 m/s; check: 8 J before, 2 + 6 = 8 J after.',
            'A ballistic pendulum measures bullet speeds: a 0.01 kg bullet at 300 m/s embeds in a 2 kg block (momentum conserved, v ≈ 1.49 m/s), then the block swings up (energy conserved, h = v²/2g ≈ 0.114 m). Use momentum for the collision and energy for the swing, never energy across the collision.'],
        'formulas_label': 'Formulas',
        'formulas': ['Always: Σp conserved', 'Elastic: ΣKE conserved too', 'Elastic, m₂ at rest: v₁ = (m₁ − m₂)u₁/(m₁ + m₂), v₂ = 2m₁u₁/(m₁ + m₂)', 'KE lost = KE before − KE after'],
        'steps': ['Use momentum conservation to find velocities.', 'Compute KE before and after.', 'Compare to classify the collision.', 'For two-stage problems, switch laws at the right moment.'],
        'worked_example': {
            'problem': 'A 2 kg trolley at 3 m/s collides with a stationary 1 kg trolley and they stick together. Find their final speed and the kinetic energy lost.',
            'steps': ['Momentum: 2 × 3 = 3v, so v = 2 m/s.', 'KE before = ½ × 2 × 3² = 9 J.', 'KE after = ½ × 3 × 2² = 6 J; lost = 3 J.'],
            'answer': '2 m/s; 3 J lost (a third of the original KE).',
            'check': 'KE after is less than before, as it must be for an inelastic collision ✓.'},
        'mistakes': ['Assuming KE is conserved in all collisions.', 'Using energy conservation through a sticking collision.', 'Forgetting to square velocities in KE.', 'Thinking momentum is lost when objects stick.'],
        'real_world': 'Car crumple zones make collisions more inelastic on purpose: the car absorbs kinetic energy by deforming, rather than passing it to the passengers.',
        'exam_strategy': 'To classify a collision, always calculate total KE before and after and say which is larger.',
        'recap': ['Momentum always conserved.', 'Elastic: KE conserved.', 'Sticking: maximum KE loss.', 'Momentum for impact, energy for the swing.']},
    T4: {
        'overview': 'Explosions and recoil are collisions in reverse: objects start together and fly apart. The centre of mass of an isolated system moves as if all its mass were at one point.',
        'key_terms': ['Explosion', 'Recoil', 'Zero total momentum', 'Centre of mass', 'Rocket propulsion'],
        'explanation': [
            'If a system starts at rest, its total momentum is zero, so afterwards the momenta of the parts must add to zero. A 4 kg rifle firing a 0.01 kg bullet at 400 m/s recoils at 0.01 × 400/4 = 1 m/s. A 3 kg object at rest that splits into 1 kg at 6 m/s and 2 kg must send the 2 kg piece off at 3 m/s the other way.',
            'Two ice skaters pushing apart work the same way: if a 40 kg skater moves off at 3 m/s, a 60 kg partner moves the other way at 2 m/s. The lighter one always moves faster. Explosions release stored chemical or elastic energy, so the kinetic energy afterwards is greater than before.',
            'The centre of mass is the average position of the mass: x̄ = Σmx/Σm. For 2 kg at x = 0 and 3 kg at x = 5 m, x̄ = 15/5 = 3 m. With no external force, the centre of mass of a system keeps moving at constant velocity, even during an explosion; this is why fireworks spread out symmetrically around a falling centre.'],
        'formulas_label': 'Formulas',
        'formulas': ['From rest: m₁v₁ + m₂v₂ = 0', 'Recoil speed: V = mv/M', 'x̄ = Σmᵢxᵢ/Σmᵢ'],
        'steps': ['Note the initial total momentum (often zero).', 'Write the momenta of the pieces after.', 'Set the sum equal to the initial total.', 'Find the unknown speed and direction.'],
        'worked_example': {
            'problem': 'A 4 kg rifle fires a 0.01 kg bullet at 400 m/s. Find the rifle\'s recoil velocity.',
            'steps': ['Momentum before = 0.', '0 = 0.01 × 400 + 4V.', 'V = −4/4 = −1 m/s.'],
            'answer': '1 m/s, opposite to the bullet.',
            'check': 'Bullet and rifle have equal and opposite momenta of 4 kg·m/s ✓.'},
        'mistakes': ['Forgetting the recoil is in the opposite direction.', 'Thinking KE is conserved in an explosion (it increases).', 'Using total mass instead of the remaining mass.', 'Placing the centre of mass at the midpoint regardless of masses.'],
        'real_world': 'Rockets push exhaust gas backwards at high speed; by conservation of momentum, the rocket gains forward momentum even in empty space.',
        'exam_strategy': 'For "from rest" problems, write 0 = m₁v₁ + m₂v₂ immediately; it is usually worth a method mark.',
        'recap': ['From rest: total momentum zero.', 'Lighter piece moves faster.', 'Explosions increase KE.', 'x̄ = Σmx/Σm.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The momentum of a 0.15 kg ball moving at 40 m/s is:', ['6 kg·m/s', '267 kg·m/s', '0.0038 kg·m/s', '40.15 kg·m/s'], 0, 'p = mv.', ans=6),
    Q(T1, 'A 2000 N force acts for 0.01 s. The impulse is:', ['20 N·s', '200 000 N·s', '0.2 N·s', '2000 N·s'], 0, 'FΔt.', ans=20),
    Q(T1, 'A 0.5 kg ball hits a wall at 6 m/s and rebounds at 4 m/s. The change in momentum is:', ['5 kg·m/s', '1 kg·m/s', '2 kg·m/s', '10 kg·m/s'], 0, '0.5 × (4 − (−6)).', ans=5),
    Q(T1, 'If that contact lasts 0.02 s, the average force is:', ['250 N', '50 N', '100 N', '500 N'], 0, '5/0.02.', ans=250),
    Q(T1, 'An airbag reduces the force on a passenger mainly by:', ['increasing the stopping time', 'reducing the change in momentum', 'reducing the passenger\'s mass', 'increasing the speed'], 0, 'F = Δp/Δt.'),
    Q(T1, 'The unit N·s is equivalent to:', ['kg·m/s', 'J', 'W', 'kg·m/s²'], 0, 'Impulse equals change in momentum.'),
    # T2
    Q(T2, 'A 2 kg trolley at 3 m/s hits a stationary 1 kg trolley and they stick. Their speed is:', ['2 m/s', '3 m/s', '1.5 m/s', '6 m/s'], 0, '6 = 3v.', ans=2),
    Q(T2, 'A 10 000 kg wagon at 4 m/s couples to a stationary 6000 kg wagon. Common speed:', ['2.5 m/s', '4 m/s', '6.67 m/s', '1.5 m/s'], 0, '40 000/16 000.', ans=2.5),
    Q(T2, 'Momentum is conserved in a system when:', ['no external resultant force acts', 'no internal forces act', 'kinetic energy is conserved', 'the objects stick together'], 0, 'Isolated system.'),
    Q(T2, 'Momentum is conserved in collisions because the forces the objects exert on each other are:', ['equal and opposite', 'zero', 'in the same direction', 'larger on the lighter object'], 0, 'Newton\'s third law.'),
    Q(T2, 'A 3 kg ball at 2 m/s meets a 1 kg ball moving at 2 m/s the opposite way. They stick. Final velocity:', ['1 m/s in the 3 kg ball\'s direction', '2 m/s', '0', '1 m/s in the 1 kg ball\'s direction'], 0, '(6 − 2)/4 = 1 m/s.'),
    Q(T2, 'In a collision, total momentum is:', ['the same before and after', 'always lost', 'always gained', 'converted to heat'], 0, 'Conservation law.'),
    # T3
    Q(T3, 'In the 2 kg + 1 kg sticking collision (3 m/s → 2 m/s), the KE lost is:', ['3 J', '9 J', '6 J', '0 J'], 0, '9 − 6.', ans=3),
    Q(T3, 'In an elastic collision:', ['both momentum and kinetic energy are conserved', 'only kinetic energy is conserved', 'only momentum is conserved', 'neither is conserved'], 0, 'Definition.'),
    Q(T3, 'A 1 kg ball at 4 m/s hits a stationary 3 kg ball elastically, head-on. The 3 kg ball moves off at:', ['2 m/s', '4 m/s', '1 m/s', '1.33 m/s'], 0, '2m₁u₁/(m₁ + m₂) = 8/4.', ans=2),
    Q(T3, 'When two objects stick together after colliding, the collision is:', ['perfectly inelastic', 'elastic', 'super-elastic', 'an explosion'], 0, 'Maximum KE loss.'),
    Q(T3, 'A 0.01 kg bullet at 300 m/s embeds in a 2 kg block at rest. The block moves off at about:', ['1.49 m/s', '1.50 m/s', '150 m/s', '0.67 m/s'], 0, '3/2.01 ≈ 1.493 (the bullet adds to the mass).'),
    Q(T3, 'For a ballistic pendulum, you use conservation of energy:', ['for the swing after the impact', 'for the impact itself', 'for both stages', 'for neither stage'], 0, 'KE is lost in the impact.'),
    # T4
    Q(T4, 'A 4 kg rifle fires a 0.01 kg bullet at 400 m/s. Its recoil speed is:', ['1 m/s', '4 m/s', '0.1 m/s', '400 m/s'], 0, '0.01 × 400/4.', ans=1),
    Q(T4, 'A 3 kg object at rest splits; 1 kg moves at 6 m/s. The 2 kg piece moves at:', ['3 m/s the opposite way', '6 m/s the opposite way', '3 m/s the same way', '2 m/s the opposite way'], 0, '1 × 6 = 2v.'),
    Q(T4, 'Two skaters (40 kg and 60 kg) push apart. The 40 kg skater moves at 3 m/s; the 60 kg skater moves at:', ['2 m/s', '3 m/s', '4.5 m/s', '1.5 m/s'], 0, '120/60.', ans=2),
    Q(T4, 'In an explosion, total kinetic energy:', ['increases', 'stays the same', 'decreases', 'becomes zero'], 0, 'Stored energy is released.'),
    Q(T4, 'Masses of 2 kg at x = 0 and 3 kg at x = 5 m. The centre of mass is at:', ['x = 3 m', 'x = 2.5 m', 'x = 2 m', 'x = 5 m'], 0, '15/5.', ans=3),
    Q(T4, 'A rocket accelerates in empty space because:', ['it pushes exhaust gas backwards, gaining forward momentum', 'the exhaust pushes on the air', 'gravity pulls it forwards', 'momentum is not conserved in space'], 0, 'Conservation of momentum.'),
]

FLASH = [
    ['Momentum', 'p = mv, a vector in kg·m/s.'],
    ['Impulse', 'FΔt = Δp, in N·s.'],
    ['Conservation of momentum', 'In an isolated system, total momentum is constant.'],
    ['Elastic collision', 'Momentum and kinetic energy both conserved.'],
    ['Inelastic collision', 'Momentum conserved; kinetic energy lost.'],
    ['Perfectly inelastic', 'Objects stick together; maximum KE loss.'],
    ['Recoil', 'From rest: m₁v₁ = −m₂v₂.'],
    ['Centre of mass', 'x̄ = Σmx/Σm.'],
]
