"""Physics I: Mechanics, module 3: Work, energy and power."""
import math
from verify import Q
T1, T2, T3, T4 = ('Work and kinetic energy', 'Potential energy and conservation of energy', 'Power and efficiency', 'Springs and elastic energy')
g = 9.8
r = lambda x, d: round(x + 0.0, d)
assert r(50 * 10 * math.cos(math.radians(60)), 6) == 250
assert 0.5 * 2 * 3 ** 2 == 9 and 0.5 * 1000 * 20 ** 2 == 200000
assert 0.5 * 1500 * 20 ** 2 / 6000 == 50
assert r(5 * g * 4, 1) == 196
assert r(math.sqrt(2 * g * 20), 1) == 19.8 and r(math.sqrt(2 * g * 0.45), 2) == 2.97
assert r(60 * g * 10 - 0.5 * 60 * 12 ** 2, 1) == 1560
assert 600 / 3 == 200 and r(70 * g * 5 / 7, 1) == 490 and 800 * 25 == 20000
assert r(20 * g * 3 / 2, 1) == 294 and r(294 / 400 * 100, 1) == 73.5 and 2 * 3 == 6
assert 200 * 0.05 == 10 and r(0.5 * 200 * 0.05 ** 2, 3) == 0.25
assert r(0.5 * g / 0.049, 6) == 100
assert r(0.5 * 400 * 0.1 ** 2, 6) == 2 and r(math.sqrt(2 * 2 / 0.05), 2) == 8.94
assert r(0.5 * 1000 * 0.2 ** 2, 6) == 20

MODULE = {
    'title': 'Work, energy and power',
    'topics': [T1, T2, T3, T4],
    'overview': 'Energy is the most useful bookkeeping tool in physics. This module defines work, kinetic and potential energy, shows how conservation of energy solves problems that would be hard with forces alone, and covers power, efficiency and elastic energy in springs.',
    'key_terms': ['Work', 'Joule', 'Kinetic energy', 'Work–energy theorem', 'Gravitational potential energy', 'Conservation of energy', 'Power', 'Watt', 'Efficiency', 'Hooke\'s law', 'Elastic potential energy'],
    'explanation': [
        'Work is done when a force moves its point of application: W = Fd cos θ. Work transfers energy, and the work done by the resultant force equals the change in kinetic energy (½mv²).',
        'Gravitational potential energy (mgh) and elastic potential energy (½kx²) are stored energy. When only these conservative forces do work, kinetic plus potential energy stays constant; friction transfers some energy to thermal energy.',
        'Power is the rate of doing work, P = W/t = Fv, measured in watts. Efficiency compares useful output with total input. Energy methods are often faster than forces because they ignore the path and only compare start and end.'],
    'quick_facts': [
        'W = Fd cos θ (J).',
        'KE = ½mv²; doubling speed gives four times the KE.',
        'ΔGPE = mgh near the Earth\'s surface.',
        'P = W/t = Fv (W).',
        'Hooke\'s law F = kx; elastic energy = ½kx².'],
}

NOTES = {
    T1: {
        'overview': 'Work measures energy transferred by a force. The work–energy theorem links the total work to the change in an object\'s speed.',
        'key_terms': ['Work', 'Joule', 'Angle between force and displacement', 'Kinetic energy', 'Net work', 'Work–energy theorem'],
        'explanation': [
            'W = Fd cos θ, where θ is the angle between the force and the displacement. Pulling a crate 10 m with 50 N at 60° to the ground does 50 × 10 × cos 60° = 250 J of work. A force perpendicular to the motion (θ = 90°) does no work; a force opposite to the motion (such as friction) does negative work.',
            'Kinetic energy is KE = ½mv². A 2 kg ball at 3 m/s has 9 J; a 1000 kg car at 20 m/s has 200 kJ. Because of the v², doubling the speed multiplies KE by four, which is why braking distances rise so quickly with speed.',
            'The work–energy theorem says W_net = ΔKE. A 1500 kg car at 20 m/s braking with a constant 6000 N force stops when 6000 × d = ½ × 1500 × 20², giving d = 50 m. No need to find the acceleration or time.'],
        'formulas_label': 'Formulas',
        'formulas': ['W = Fd cos θ', 'KE = ½mv²', 'W_net = ΔKE = ½mv² − ½mu²', '1 J = 1 N·m'],
        'steps': ['List the forces that do work.', 'Find the work of each (watch the signs).', 'Add them to get W_net.', 'Set W_net = ΔKE and solve.'],
        'worked_example': {
            'problem': 'A 1500 kg car travelling at 20 m/s brakes with a constant force of 6000 N. How far does it travel before stopping?',
            'steps': ['Initial KE = ½ × 1500 × 20² = 300 000 J.', 'The braking force does negative work: −6000d.', '−6000d = 0 − 300 000, so d = 50 m.'],
            'answer': '50 m.',
            'check': 'Using kinematics: a = 6000/1500 = 4 m/s², and d = u²/(2a) = 400/8 = 50 m ✓.'},
        'mistakes': ['Forgetting cos θ when the force is at an angle.', 'Treating work as a vector (it is a scalar).', 'Using v instead of v² in KE.', 'Forgetting friction does negative work.'],
        'real_world': 'A car at 60 km/h has four times the kinetic energy of one at 30 km/h, so it needs roughly four times the braking distance.',
        'exam_strategy': 'If a question gives distances and speeds but not times, use energy; if it asks for time, use kinematics or momentum.',
        'recap': ['W = Fd cos θ.', 'KE = ½mv².', 'W_net = ΔKE.', 'Work is a scalar.']},
    T2: {
        'overview': 'Potential energy is energy stored because of position. When no energy is lost to friction, kinetic plus potential energy stays constant.',
        'key_terms': ['Gravitational potential energy', 'Reference level', 'Conservative force', 'Mechanical energy', 'Conservation of energy', 'Energy dissipated'],
        'explanation': [
            'Lifting a mass m through a height h stores ΔGPE = mgh. Raising 5 kg by 4 m stores 5 × 9.8 × 4 = 196 J. Only changes in GPE matter, so you can choose any convenient zero level.',
            'With no friction, mechanical energy (KE + PE) is conserved: ½mu² + mgh₁ = ½mv² + mgh₂. An object dropped from 20 m hits the ground at v = √(2gh) = √392 ≈ 19.8 m/s, whatever its mass. A pendulum released 0.45 m above its lowest point passes the bottom at √(2 × 9.8 × 0.45) ≈ 2.97 m/s.',
            'When friction acts, the total energy is still conserved but some becomes thermal energy: energy at the start = energy at the end + energy dissipated. A 60 kg sled sliding down a 10 m high slope that reaches the bottom at 12 m/s has lost 5880 − 4320 = 1560 J to friction.'],
        'formulas_label': 'Formulas',
        'formulas': ['ΔGPE = mgh', 'No friction: ½mu² + mgh₁ = ½mv² + mgh₂', 'From rest through height h: v = √(2gh)', 'With friction: E_start = E_end + energy dissipated'],
        'steps': ['Choose a zero level for height.', 'Write total energy at the start.', 'Write total energy at the end (plus losses).', 'Set them equal and solve.'],
        'worked_example': {
            'problem': 'A 60 kg sled starts from rest at the top of a slope 10 m high and reaches the bottom at 12 m/s. How much energy was dissipated by friction?',
            'steps': ['GPE at the top = 60 × 9.8 × 10 = 5880 J.', 'KE at the bottom = ½ × 60 × 12² = 4320 J.', 'Energy dissipated = 5880 − 4320 = 1560 J.'],
            'answer': '1560 J.',
            'check': 'Without friction the sled would reach √(2 × 9.8 × 10) ≈ 14 m/s; 12 m/s is less, consistent with losses ✓.'},
        'mistakes': ['Including mass in v = √(2gh) as though heavier objects fall faster.', 'Using the slope length instead of the vertical height in mgh.', 'Forgetting energy lost to friction.', 'Mixing up initial and final heights.'],
        'real_world': 'Hydroelectric dams convert the gravitational potential energy of stored water into electrical energy; the higher the dam, the more energy per litre.',
        'exam_strategy': 'Write an energy equation in words first ("GPE at top = KE at bottom + heat"), then substitute numbers.',
        'recap': ['ΔGPE = mgh.', 'Mechanical energy is conserved without friction.', 'v = √(2gh) is mass-independent.', 'Losses become thermal energy.']},
    T3: {
        'overview': 'Power is how quickly energy is transferred. Efficiency tells us how much of the input energy becomes useful output.',
        'key_terms': ['Power', 'Watt', 'Kilowatt-hour', 'P = Fv', 'Efficiency', 'Useful energy', 'Wasted energy'],
        'explanation': [
            'Power P = W/t, in watts (1 W = 1 J/s). Doing 600 J of work in 3 s is 200 W. A 70 kg student who runs up 5 m of stairs in 7 s develops mgh/t = 490 W.',
            'For a force moving an object at constant velocity, P = Fv. A car cruising at 25 m/s against 800 N of drag and friction needs 800 × 25 = 20 kW from its engine.',
            'Efficiency = useful output ÷ total input × 100%. A motor taking 400 W that lifts 20 kg by 3 m in 2 s gives a useful 294 W, so its efficiency is 73.5%. Electricity bills use the kilowatt-hour: a 2 kW heater for 3 hours uses 6 kWh.'],
        'formulas_label': 'Formulas',
        'formulas': ['P = W/t = ΔE/t', 'P = Fv (constant velocity)', 'Efficiency = useful output/total input × 100%', '1 kWh = 3.6 × 10⁶ J'],
        'steps': ['Find the energy transferred or work done.', 'Divide by the time.', 'For efficiency, compare useful with total.', 'Check units: W, J, s.'],
        'worked_example': {
            'problem': 'An electric motor takes 400 W from the supply and lifts a 20 kg load through 3 m in 2 s. Find its efficiency.',
            'steps': ['Useful work = mgh = 20 × 9.8 × 3 = 588 J.', 'Useful power = 588/2 = 294 W.', 'Efficiency = 294/400 × 100% = 73.5%.'],
            'answer': '73.5%.',
            'check': 'The answer is below 100%, as it must be; the rest is wasted as heat and sound ✓.'},
        'mistakes': ['Confusing power (W) with energy (J).', 'Forgetting to convert minutes or hours to seconds.', 'Getting an efficiency above 100%.', 'Treating kWh as a unit of power.'],
        'real_world': 'An LED bulb gives the same light as an old filament bulb at about one sixth of the power, because far less input energy is wasted as heat.',
        'exam_strategy': 'If the question involves a constant speed and a resistive force, P = Fv is the fastest route.',
        'recap': ['P = W/t.', 'P = Fv.', 'Efficiency ≤ 100%.', 'kWh is energy.']},
    T4: {
        'overview': 'Springs store energy when stretched or compressed. Hooke\'s law describes the force, and ½kx² gives the stored energy.',
        'key_terms': ['Hooke\'s law', 'Spring constant k', 'Extension', 'Limit of proportionality', 'Elastic potential energy', 'Force–extension graph'],
        'explanation': [
            'Hooke\'s law: F = kx, where x is the extension or compression and k is the spring constant in N/m. A 200 N/m spring stretched 0.05 m needs 10 N. Hanging a 0.5 kg mass that stretches a spring 0.049 m gives k = mg/x = 100 N/m.',
            'The area under a force–extension graph is the work done, so elastic energy = ½Fx = ½kx². The 200 N/m spring stretched 0.05 m stores 0.25 J. Doubling the compression stores four times the energy.',
            'Elastic energy converts to kinetic energy in launchers. A 400 N/m spring compressed 0.1 m stores 2 J; it can launch a 50 g ball at v = √(2E/m) = √80 ≈ 8.94 m/s (ignoring losses). Beyond the limit of proportionality, Hooke\'s law no longer holds.'],
        'formulas_label': 'Formulas',
        'formulas': ['F = kx', 'E = ½kx² = ½Fx', 'k = mg/x for a hanging mass', 'Spring launch: ½kx² = ½mv²'],
        'steps': ['Find k from a known force and extension.', 'Use F = kx for forces.', 'Use ½kx² for energy.', 'Convert to KE or GPE with conservation of energy.'],
        'worked_example': {
            'problem': 'A spring with k = 400 N/m is compressed by 0.10 m and used to launch a 0.050 kg ball horizontally. Find the launch speed.',
            'steps': ['Stored energy = ½ × 400 × 0.10² = 2.0 J.', 'All becomes KE: ½ × 0.050 × v² = 2.0.', 'v² = 80, v ≈ 8.94 m/s.'],
            'answer': 'About 8.94 m/s.',
            'check': 'Units: N/m × m² = N·m = J ✓, and J/kg = m²/s² ✓.'},
        'mistakes': ['Using the total length instead of the extension.', 'Using kx instead of ½kx² for energy.', 'Forgetting to convert cm to m.', 'Applying Hooke\'s law beyond the limit of proportionality.'],
        'real_world': 'A car\'s suspension springs store energy when the wheel hits a bump and return it, while dampers turn it into heat so the car does not keep bouncing.',
        'exam_strategy': 'Always convert extensions to metres before squaring; an error in centimetres is magnified 10 000 times.',
        'recap': ['F = kx.', 'E = ½kx².', 'Area under F–x graph = energy.', 'Use metres.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A 50 N force pulls a crate 10 m at 60° to the direction of motion. The work done is:', ['250 J', '500 J', '433 J', '5 J'], 0, '50 × 10 × cos 60°.', ans=250),
    Q(T1, 'The kinetic energy of a 2 kg ball moving at 3 m/s is:', ['9 J', '6 J', '18 J', '3 J'], 0, '½ × 2 × 9.', ans=9),
    Q(T1, 'If a car\'s speed doubles, its kinetic energy:', ['quadruples', 'doubles', 'halves', 'stays the same'], 0, 'KE ∝ v².'),
    Q(T1, 'A 1500 kg car at 20 m/s brakes with 6000 N. Its stopping distance is:', ['50 m', '100 m', '25 m', '5 m'], 0, 'Fd = ½mv².', ans=50),
    Q(T1, 'A force perpendicular to an object\'s motion does:', ['no work', 'positive work', 'negative work', 'maximum work'], 0, 'cos 90° = 0.'),
    Q(T1, 'The kinetic energy of a 1000 kg car at 20 m/s is:', ['200 kJ', '20 kJ', '10 kJ', '400 kJ'], 0, '½ × 1000 × 400 = 200 000 J.', ans=200),
    # T2
    Q(T2, 'The gain in GPE when 5 kg is lifted 4 m is:', ['196 J', '20 J', '49 J', '1.25 J'], 0, 'mgh.', ans=196),
    Q(T2, 'An object dropped from 20 m (no air resistance) hits the ground at about:', ['19.8 m/s', '392 m/s', '14.0 m/s', '9.8 m/s'], 0, '√(2gh).', ans=19.8, num=True),
    Q(T2, 'A pendulum released 0.45 m above its lowest point passes the bottom at about:', ['2.97 m/s', '8.82 m/s', '4.41 m/s', '0.94 m/s'], 0, '√(2 × 9.8 × 0.45).', ans=2.97, num=True),
    Q(T2, 'A 60 kg sled descends 10 m in height from rest and reaches 12 m/s. Energy dissipated:', ['1560 J', '4320 J', '5880 J', '600 J'], 0, '5880 − 4320.', ans=1560),
    Q(T2, 'Ignoring air resistance, a heavier ball dropped from the same height lands:', ['at the same speed', 'faster', 'slower', 'with less energy'], 0, 'v = √(2gh) has no m.'),
    Q(T2, 'In mgh, h is:', ['the vertical height change', 'the slope length', 'the distance travelled', 'the horizontal distance'], 0, 'Only vertical change matters.'),
    # T3
    Q(T3, '600 J of work is done in 3 s. The power is:', ['200 W', '1800 W', '0.005 W', '603 W'], 0, 'W/t.', ans=200),
    Q(T3, 'A 70 kg student climbs 5 m of stairs in 7 s. Power developed:', ['490 W', '50 W', '3430 W', '343 W'], 0, 'mgh/t.', ans=490),
    Q(T3, 'A car at a constant 25 m/s against 800 N of resistance needs engine power:', ['20 kW', '32 W', '20 W', '825 W'], 0, 'P = Fv = 20 000 W.'),
    Q(T3, 'A motor takes 400 W and gives 294 W of useful power. Its efficiency is:', ['73.5%', '136%', '26.5%', '106%'], 0, '294/400.', ans=73.5, num=True),
    Q(T3, 'A 2 kW heater runs for 3 hours. Energy used:', ['6 kWh', '0.67 kWh', '6 kW', '1.5 kWh'], 0, 'Power × time.'),
    Q(T3, 'The watt is equivalent to:', ['J/s', 'J·s', 'N·m', 'N/s'], 0, 'Energy per second.'),
    # T4
    Q(T4, 'A spring with k = 200 N/m is stretched 0.05 m. The force needed is:', ['10 N', '4000 N', '0.25 N', '200 N'], 0, 'F = kx.', ans=10),
    Q(T4, 'The energy stored in that spring is:', ['0.25 J', '0.5 J', '10 J', '5 J'], 0, '½ × 200 × 0.0025.', ans=0.25, num=True),
    Q(T4, 'A 0.5 kg mass stretches a spring by 0.049 m. Its spring constant is:', ['100 N/m', '10.2 N/m', '0.024 N/m', '24.5 N/m'], 0, 'k = mg/x = 4.9/0.049.'),
    Q(T4, 'A 400 N/m spring compressed 0.1 m launches a 0.05 kg ball. Launch speed (no losses):', ['8.94 m/s', '80 m/s', '2 m/s', '4.47 m/s'], 0, '½kx² = ½mv².', ans=8.94, num=True),
    Q(T4, 'Doubling a spring\'s compression multiplies its stored energy by:', ['4', '2', '½', '8'], 0, 'E ∝ x².', ans=4),
    Q(T4, 'A car spring with k = 1000 N/m compressed 20 cm stores:', ['20 J', '200 J', '20 000 J', '100 J'], 0, '½ × 1000 × 0.2² (convert cm to m).', ans=20),
]

FLASH = [
    ['Work', 'W = Fd cos θ, measured in joules.'],
    ['Kinetic energy', 'KE = ½mv².'],
    ['Work–energy theorem', 'Net work = change in kinetic energy.'],
    ['Gravitational PE', 'ΔGPE = mgh.'],
    ['Conservation of energy', 'Without friction, KE + PE stays constant.'],
    ['Power', 'P = W/t = Fv, in watts.'],
    ['Efficiency', 'Useful output ÷ total input × 100%.'],
    ['Hooke\'s law', 'F = kx; elastic energy ½kx².'],
]
