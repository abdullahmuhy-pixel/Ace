"""Electricity and Magnetism, module 4: Electromagnetic induction."""
import math
from verify import Q
T1, T2, T3, T4 = ('Faraday\'s and Lenz\'s laws', 'Motional emf and generators', 'Inductance and RL circuits', 'Transformers and power transmission')
mu0 = 4e-7 * math.pi
r = lambda v, d: round(v, d)
assert r(0.5 * 0.02, 6) == 0.01 and r(200 * 0.01 / 0.05, 6) == 40 and r(50 * (0.5 - 0.1) * 0.01 / 0.2, 6) == 1
assert r(0.5 * 0.4 * 3, 6) == 0.6 and r(0.6 / 2, 6) == 0.3 and r(0.5 * 0.3 * 0.4, 6) == 0.06 and r(0.06 * 3, 6) == r(0.3 ** 2 * 2, 6) == 0.18
w = 2 * math.pi * 50; assert r(100 * 0.2 * 0.05 * w, 0) == 314 and r(100 * 0.2 * 0.05 * w / math.sqrt(2), 0) == 222
assert r(mu0 * 500 ** 2 * 1e-3 / 0.25 * 1e3, 2) == 1.26 and r(0.2 * 50, 6) == 10 and r(0.5 * 0.2 * 9, 6) == 0.9
assert r(0.2 / 10, 6) == 0.02 and 12 / 10 == 1.2 and r(1.2 * (1 - math.exp(-1)), 2) == 0.76
assert r(230 * 50 / 1000, 6) == 11.5 and r(2 * 11.5 / 230, 6) == 0.1 and 1e5 / 400 == 250 and 250 ** 2 * 0.5 == 31250 and 1e5 / 2e4 == 5 and 5 ** 2 * 0.5 == 12.5

MODULE = {
    'title': 'Electromagnetic induction',
    'topics': [T1, T2, T3, T4],
    'overview': 'A changing magnetic flux creates an emf. This one idea, Faraday\'s law, explains generators, induction cooktops, transformers and the national grid. The module covers Faraday\'s and Lenz\'s laws, motional emf and AC generators, self-inductance and RL circuits, and transformers.',
    'key_terms': ['Magnetic flux', 'Weber', 'Faraday\'s law', 'Lenz\'s law', 'Induced emf', 'Eddy currents', 'Motional emf', 'Generator', 'Self-inductance', 'Henry', 'Back emf', 'RL time constant', 'Transformer', 'Turns ratio', 'Transmission loss'],
    'explanation': [
        'Magnetic flux Φ = BA cos θ counts field lines through a loop. Faraday\'s law says the induced emf is ε = −N dΦ/dt; the minus sign is Lenz\'s law: the induced current opposes the change that caused it.',
        'Moving a rod through a field (ε = BLv) or rotating a coil (peak ε = NBAω) changes flux and generates electricity; this is how nearly all power stations work. A coil also opposes changes in its own current: its self-inductance L gives ε = −L dI/dt, and stores energy ½LI².',
        'A transformer uses a changing flux in an iron core to change AC voltages: Vₛ/Vₚ = Nₛ/Nₚ. Stepping the voltage up for long-distance transmission cuts the current, and the I²R losses fall by the square of that factor.'],
    'quick_facts': [
        'Φ = BA cos θ (Wb).',
        'ε = −N ΔΦ/Δt; Lenz: opposes the change.',
        'Motional ε = BLv; generator ε₀ = NBAω.',
        'ε = −L dI/dt; U = ½LI²; τ = L/R.',
        'Vₛ/Vₚ = Nₛ/Nₚ = Iₚ/Iₛ (ideal).'],
}

NOTES = {
    T1: {
        'overview': 'Faraday\'s law: a changing magnetic flux through a circuit induces an emf. Lenz\'s law gives the direction.',
        'key_terms': ['Magnetic flux', 'Weber', 'Flux linkage', 'Faraday\'s law', 'Lenz\'s law', 'Eddy currents', 'Induction braking'],
        'explanation': [
            'Flux Φ = BA cos θ, in webers (Wb). A 0.02 m² loop perpendicular to 0.5 T has Φ = 0.01 Wb. Flux changes if B, A or the angle changes.',
            'ε = −N ΔΦ/Δt. A 200-turn coil whose flux drops from 0.01 Wb to 0 in 0.05 s has ε = 200 × 0.01/0.05 = 40 V. A 50-turn coil of area 0.01 m² in a field rising from 0.1 T to 0.5 T in 0.2 s gives 50 × 0.004/0.2 = 1 V.',
            'Lenz\'s law: the induced current\'s field opposes the change in flux. Push a magnet\'s north pole into a coil and the coil\'s near end becomes a north pole, repelling it. This is energy conservation; otherwise you would get energy for free. Eddy currents in metal plates resist motion, which is used in train brakes.'],
        'formulas_label': 'Formulas',
        'formulas': ['Φ = BA cos θ', 'ε = −N ΔΦ/Δt', 'I = ε/R (in a closed circuit)'],
        'steps': ['Find the initial and final flux.', 'Compute ΔΦ.', 'Multiply by N and divide by Δt.', 'Use Lenz\'s law for the direction.'],
        'worked_example': {
            'problem': 'A 50-turn coil of area 0.01 m² lies perpendicular to a field that rises from 0.1 T to 0.5 T in 0.2 s. Find the emf.',
            'steps': ['ΔΦ = ΔB × A = 0.4 × 0.01 = 0.004 Wb.', 'ε = NΔΦ/Δt = 50 × 0.004/0.2.', 'ε = 1 V.'],
            'answer': '1 V.',
            'check': 'Units: Wb/s = V ✓; faster change → larger emf ✓.'},
        'mistakes': ['Thinking a steady strong field induces emf.', 'Forgetting N.', 'Getting the Lenz direction backwards.', 'Using B instead of ΔB.'],
        'real_world': 'Induction cooktops use a rapidly changing field to induce eddy currents that heat the base of the pot directly.',
        'exam_strategy': 'For direction questions, write "flux increasing out of page → induced field into page" and then use the grip rule.',
        'recap': ['Φ = BA cos θ.', 'Change makes emf.', 'Lenz opposes.', 'Eddy currents.']},
    T2: {
        'overview': 'Moving conductors through fields, or rotating coils in them, convert mechanical energy into electrical energy.',
        'key_terms': ['Motional emf', 'Sliding rod', 'Magnetic drag', 'AC generator', 'Angular frequency', 'Peak and RMS values'],
        'explanation': [
            'A rod of length L moving at v across a field B has ε = BLv. With B = 0.5 T, L = 0.4 m and v = 3 m/s, ε = 0.6 V. In a 2 Ω circuit, I = 0.3 A, and the magnetic drag force BIL = 0.06 N.',
            'Energy balance: pushing the rod against the drag needs power Fv = 0.06 × 3 = 0.18 W, exactly the I²R = 0.3² × 2 = 0.18 W heating the circuit. The mechanical work becomes electrical energy.',
            'A coil of N turns rotating at angular frequency ω gives ε = NBAω sin ωt. With N = 100, B = 0.2 T, A = 0.05 m² and 50 Hz (ω ≈ 314 rad/s), the peak emf is about 314 V and the RMS value 314/√2 ≈ 222 V.'],
        'formulas_label': 'Formulas',
        'formulas': ['ε = BLv', 'F_drag = BIL', 'Generator: ε = NBAω sin ωt, ε₀ = NBAω', 'ω = 2πf; ε_rms = ε₀/√2'],
        'steps': ['Identify what moves and what changes.', 'Compute ε.', 'Find current with Ohm\'s law.', 'Check the energy balance.'],
        'worked_example': {
            'problem': 'A 100-turn coil of area 0.05 m² rotates at 50 Hz in a 0.2 T field. Find the peak and RMS emf.',
            'steps': ['ω = 2π × 50 ≈ 314 rad/s.', 'ε₀ = NBAω = 100 × 0.2 × 0.05 × 314 ≈ 314 V.', 'ε_rms = 314/√2 ≈ 222 V.'],
            'answer': 'About 314 V peak and 222 V RMS.',
            'check': 'Doubling the speed of rotation doubles the emf ✓.'},
        'mistakes': ['Using f instead of ω.', 'Confusing peak and RMS.', 'Ignoring the drag force.', 'Forgetting N.'],
        'real_world': 'Eskom\'s coal, nuclear and hydro stations all turn large generators; only the source of the turning differs.',
        'exam_strategy': 'An energy-balance check (Fv = I²R) is a quick way to confirm motional-emf answers.',
        'recap': ['ε = BLv.', 'Drag opposes motion.', 'ε₀ = NBAω.', 'RMS = peak/√2.']},
    T3: {
        'overview': 'A coil opposes changes in its own current. This self-inductance stores energy and makes current rise gradually in RL circuits.',
        'key_terms': ['Self-inductance', 'Henry', 'Back emf', 'Energy in an inductor', 'RL circuit', 'Time constant L/R'],
        'explanation': [
            'ε = −L dI/dt. A 0.2 H inductor with current changing at 50 A/s has a back emf of 10 V. A long solenoid has L = μ₀N²A/l: 500 turns, area 10⁻³ m², length 0.25 m gives about 1.26 mH.',
            'An inductor stores energy U = ½LI²: 0.2 H carrying 3 A stores 0.9 J. Breaking such a circuit suddenly makes dI/dt huge, so large voltages and sparks appear across switches.',
            'In an RL circuit the current rises as I = (ε/R)(1 − e^(−t/τ)) with τ = L/R. With 0.2 H, 10 Ω and 12 V, τ = 0.02 s and the final current is 1.2 A; after one τ it is about 0.76 A.'],
        'formulas_label': 'Formulas',
        'formulas': ['ε = −L dI/dt', 'Solenoid: L = μ₀N²A/l', 'U = ½LI²', 'τ = L/R', 'I = I_max(1 − e^(−t/τ))'],
        'steps': ['Find L or dI/dt.', 'Compute the emf or energy.', 'For RL circuits find τ = L/R and I_max = ε/R.', 'Substitute t/τ.'],
        'worked_example': {
            'problem': 'A 0.2 H inductor and 10 Ω resistor are connected to 12 V. Find τ and the current after one time constant.',
            'steps': ['τ = L/R = 0.2/10 = 0.02 s.', 'I_max = 12/10 = 1.2 A.', 'I(τ) = 1.2 × (1 − e⁻¹) ≈ 0.76 A.'],
            'answer': 'τ = 0.02 s; about 0.76 A.',
            'check': 'Same 63% landmark as an RC circuit ✓.'},
        'mistakes': ['Writing τ = LR or R/L.', 'Forgetting the square in N² for a solenoid.', 'Thinking an inductor opposes current itself (it opposes changes in current).', 'Forgetting the ½ in the energy.'],
        'real_world': 'Car ignition coils use a sudden collapse of current in an inductor to produce the thousands of volts a spark plug needs.',
        'exam_strategy': 'Notice the parallel with capacitors: ½CV² ↔ ½LI², τ = RC ↔ τ = L/R.',
        'recap': ['Back emf L dI/dt.', 'U = ½LI².', 'τ = L/R.', 'Current rises gradually.']},
    T4: {
        'overview': 'Transformers change AC voltages using mutual induction. They make long-distance power transmission efficient.',
        'key_terms': ['Mutual inductance', 'Primary coil', 'Secondary coil', 'Turns ratio', 'Step-up', 'Step-down', 'Laminated core', 'Transmission losses'],
        'explanation': [
            'Vₛ/Vₚ = Nₛ/Nₚ. A 230 V supply on a 1000-turn primary with a 50-turn secondary gives 11.5 V. An ideal transformer conserves power, VₚIₚ = VₛIₛ, so if the secondary draws 2 A the primary draws 0.1 A.',
            'Transformers need AC: a steady DC current makes no changing flux. Cores are laminated (thin insulated sheets) to reduce eddy-current losses.',
            'Sending 100 kW at 400 V needs 250 A; through 0.5 Ω of line that wastes I²R = 31 250 W, almost a third of the power. At 20 kV the current is only 5 A and the loss is 12.5 W. That is why grids transmit at hundreds of kilovolts.'],
        'formulas_label': 'Formulas',
        'formulas': ['Vₛ/Vₚ = Nₛ/Nₚ', 'Ideal: VₚIₚ = VₛIₛ', 'Line current I = P/V', 'Loss = I²R'],
        'steps': ['Use the turns ratio for the voltage.', 'Use power conservation for the currents.', 'For transmission, find I = P/V.', 'Compute the loss I²R.'],
        'worked_example': {
            'problem': '100 kW is transmitted through lines of total resistance 0.5 Ω. Compare losses at 400 V and at 20 kV.',
            'steps': ['At 400 V: I = 250 A; loss = 250² × 0.5 = 31 250 W.', 'At 20 kV: I = 5 A; loss = 25 × 0.5 = 12.5 W.', 'The voltage is 50 times higher, so the loss is 2500 times smaller.'],
            'answer': '31 250 W versus 12.5 W.',
            'check': '50² = 2500 and 31 250/2500 = 12.5 ✓.'},
        'mistakes': ['Inverting the turns ratio.', 'Thinking a transformer increases power.', 'Using a transformer on DC.', 'Using P = V²/R with the supply voltage instead of the line drop.'],
        'real_world': 'Phone chargers contain a small transformer (or switching circuit) that steps 230 V mains down to 5 V.',
        'exam_strategy': 'Voltage up means current down by the same factor; losses go as the square.',
        'recap': ['Turns ratio sets voltage.', 'Power conserved (ideal).', 'AC only.', 'High voltage, low loss.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The flux through a 0.02 m² loop perpendicular to 0.5 T is:', ['0.01 Wb', '0.1 Wb', '0.04 Wb', '25 Wb'], 0, 'BA.'),
    Q(T1, 'A 200-turn coil\'s flux falls from 0.01 Wb to 0 in 0.05 s. The emf is:', ['40 V', '0.2 V', '4 V', '400 V'], 0, 'NΔΦ/Δt.', ans=40, num=True),
    Q(T1, 'A 50-turn coil of area 0.01 m² sees B rise from 0.1 T to 0.5 T in 0.2 s. The emf is:', ['1 V', '1.25 V', '0.25 V', '5 V'], 0, '50 × 0.004/0.2.', ans=1, num=True),
    Q(T1, 'Lenz\'s law is a consequence of conservation of:', ['energy', 'charge', 'momentum', 'mass'], 0, 'Opposing the change.'),
    Q(T1, 'A strong magnet held still inside a coil induces:', ['no emf', 'a large emf', 'a steady current', 'an AC current'], 0, 'No change in flux.'),
    Q(T1, 'Pushing a north pole into a coil makes the near end of the coil:', ['a north pole', 'a south pole', 'neutral', 'alternately north and south'], 0, 'Repels the approach.'),
    # T2
    Q(T2, 'A 0.4 m rod moving at 3 m/s through 0.5 T generates:', ['0.6 V', '6 V', '0.06 V', '3.75 V'], 0, 'BLv.', ans=0.6, num=True),
    Q(T2, 'In a 2 Ω circuit the current is:', ['0.3 A', '1.2 A', '0.6 A', '3 A'], 0, 'ε/R.', ans=0.3, num=True),
    Q(T2, 'The magnetic drag on the rod is:', ['0.06 N', '0.6 N', '0.12 N', '0.3 N'], 0, 'BIL.', ans=0.06, num=True),
    Q(T2, 'A 100-turn, 0.05 m² coil rotating at 50 Hz in 0.2 T has peak emf about:', ['314 V', '50 V', '100 V', '222 V'], 0, 'NBAω.', ans=314, num=True),
    Q(T2, 'Its RMS emf is about:', ['222 V', '314 V', '157 V', '444 V'], 0, 'Peak/√2.', ans=222, num=True),
    Q(T2, 'Doubling a generator\'s rotation speed:', ['doubles its peak emf', 'halves it', 'leaves it unchanged', 'quadruples it'], 0, 'ε₀ ∝ ω.'),
    # T3
    Q(T3, 'A 0.2 H inductor with current changing at 50 A/s has back emf:', ['10 V', '250 V', '0.004 V', '100 V'], 0, 'L dI/dt.', ans=10, num=True),
    Q(T3, 'A 0.2 H inductor carrying 3 A stores:', ['0.9 J', '0.6 J', '1.8 J', '0.3 J'], 0, '½LI².', ans=0.9, num=True),
    Q(T3, 'The time constant of 0.2 H and 10 Ω is:', ['0.02 s', '2 s', '50 s', '0.2 s'], 0, 'L/R.', ans=0.02, num=True),
    Q(T3, 'With 12 V, after one time constant the current is about:', ['0.76 A', '1.2 A', '0.44 A', '0.6 A'], 0, '1.2(1 − e⁻¹).', ans=0.76, num=True),
    Q(T3, 'A 500-turn solenoid of area 10⁻³ m² and length 0.25 m has inductance about:', ['1.26 mH', '2.5 mH', '0.63 mH', '12.6 mH'], 0, 'μ₀N²A/l.'),
    Q(T3, 'An inductor opposes:', ['changes in current', 'all current', 'DC only', 'voltage'], 0, 'Back emf.'),
    # T4
    Q(T4, '230 V on a 1000-turn primary gives, with a 50-turn secondary:', ['11.5 V', '4600 V', '23 V', '115 V'], 0, 'Turns ratio.', ans=11.5, num=True),
    Q(T4, 'If the secondary draws 2 A, an ideal primary draws:', ['0.1 A', '40 A', '2 A', '1 A'], 0, 'Power balance.', ans=0.1, num=True),
    Q(T4, 'Sending 100 kW at 400 V through 0.5 Ω loses:', ['31 250 W', '12.5 W', '200 W', '125 W'], 0, '250² × 0.5.'),
    Q(T4, 'At 20 kV the same transmission loses:', ['12.5 W', '31 250 W', '5 W', '2.5 W'], 0, '5² × 0.5.'),
    Q(T4, 'Transformer cores are laminated to:', ['reduce eddy-current losses', 'increase resistance of the coils', 'store charge', 'reduce the turns ratio'], 0, 'Thin insulated sheets.'),
    Q(T4, 'Transformers do not work with steady DC because:', ['there is no changing flux', 'DC is too weak', 'the core melts', 'DC has no voltage'], 0, 'Faraday needs change.'),
]

FLASH = [
    ['Magnetic flux', 'Φ = BA cos θ, in webers.'],
    ['Faraday\'s law', 'ε = −N ΔΦ/Δt.'],
    ['Lenz\'s law', 'Induced current opposes the change in flux.'],
    ['Motional emf', 'ε = BLv.'],
    ['Generator peak emf', 'ε₀ = NBAω.'],
    ['Self-inductance', 'ε = −L dI/dt; U = ½LI².'],
    ['RL time constant', 'τ = L/R.'],
    ['Transformer', 'Vₛ/Vₚ = Nₛ/Nₚ; ideal VₚIₚ = VₛIₛ.'],
]
