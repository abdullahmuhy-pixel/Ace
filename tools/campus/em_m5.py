"""Electricity and Magnetism, module 5: AC circuits and electromagnetic waves."""
import math
from verify import Q
T1, T2, T3, T4 = ('AC circuits and reactance', 'RLC circuits, resonance and power', 'Maxwell\'s equations', 'Electromagnetic waves')
pi, mu0, e0 = math.pi, 4e-7 * math.pi, 8.85e-12
r = lambda v, d: round(v, d)
assert r(230 * math.sqrt(2), 0) == 325 and r(1 / (2 * pi * 50 * 10e-6), 0) == 318 and r(2 * pi * 50 * 0.5, 0) == 157
XL, XC = 2 * pi * 50 * 0.5, 1 / (2 * pi * 50 * 10e-6); Z = math.hypot(100, XL - XC); I = 230 / Z
assert r(Z, 0) == 190 and r(I, 2) == 1.21 and r(math.degrees(math.atan((XL - XC) / 100)), 0) == -58 and r(100 / Z, 2) == 0.53 and r(I ** 2 * 100, 0) == 147
assert r(1 / (2 * pi * math.sqrt(0.5 * 10e-6)), 1) == 71.2 and 230 / 100 == 2.3 and r(1 / (4 * pi ** 2 * 1e16 * 0.25e-6) * 1e12, 1) == 10.1
assert r(1 / math.sqrt(mu0 * e0) / 1e8, 2) == 3.00 and 3e8 / 1e8 == 3 and r(3e8 / 2.4e9, 4) == 0.125 and r(300 / 3e8, 12) == 1e-6
assert r(100 / (4 * pi * 2 ** 2), 2) == 1.99 and r(3e8 / 5e-7 / 1e14, 6) == 6

MODULE = {
    'title': 'AC circuits and electromagnetic waves',
    'topics': [T1, T2, T3, T4],
    'overview': 'The final module covers alternating current: how resistors, capacitors and inductors respond to AC, resonance and power factor in RLC circuits, then Maxwell\'s four equations, which unite electricity and magnetism and predict electromagnetic waves travelling at the speed of light.',
    'key_terms': ['RMS value', 'Reactance', 'Impedance', 'Phase angle', 'Phasor', 'Resonance', 'Power factor', 'Q factor', 'Maxwell\'s equations', 'Displacement current', 'Electromagnetic wave', 'Speed of light', 'Electromagnetic spectrum', 'Intensity', 'Polarisation'],
    'explanation': [
        'AC voltages vary as V₀ sin ωt. Their RMS value, V₀/√2, gives the same heating as that DC voltage: South Africa\'s 230 V mains has peaks of about 325 V. Capacitors and inductors oppose AC by their reactance, X_C = 1/(ωC) and X_L = ωL, which depend on frequency.',
        'In a series RLC circuit the impedance Z = √(R² + (X_L − X_C)²). At resonance, f₀ = 1/(2π√(LC)), the reactances cancel and the current peaks; this is how radios tune to one station. Only the resistor uses power: P = I²R = VI cos φ.',
        'Maxwell completed the laws of electromagnetism by adding the displacement current. His equations predict waves of linked E and B fields travelling at c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s, which turned out to be light itself. Radio, microwaves, light and X-rays are all such waves.'],
    'quick_facts': [
        'V_rms = V₀/√2; 230 V RMS ≈ 325 V peak.',
        'X_C = 1/(2πfC); X_L = 2πfL.',
        'Z = √(R² + (X_L − X_C)²); tan φ = (X_L − X_C)/R.',
        'f₀ = 1/(2π√(LC)); P = I²R = V_rms I_rms cos φ.',
        'c = 1/√(μ₀ε₀) = fλ; E = cB.'],
}

NOTES = {
    T1: {
        'overview': 'In AC circuits, capacitors and inductors limit current through reactance, which depends on frequency, and they shift the phase of current relative to voltage.',
        'key_terms': ['Alternating current', 'Peak value', 'RMS value', 'Capacitive reactance', 'Inductive reactance', 'Phase', 'Phasor'],
        'explanation': [
            'V = V₀ sin ωt with ω = 2πf. RMS values give the equivalent DC heating: V_rms = V₀/√2. Mains at 230 V RMS and 50 Hz peaks at about 325 V.',
            'A capacitor\'s reactance X_C = 1/(2πfC) falls as frequency rises: 10 μF at 50 Hz gives about 318 Ω. An inductor\'s X_L = 2πfL rises with frequency: 0.5 H at 50 Hz gives about 157 Ω. Capacitors block DC and pass high frequencies; inductors do the reverse.',
            'In a resistor, current and voltage are in phase. In a capacitor the current leads the voltage by 90°; in an inductor it lags by 90° (memory aid: "CIVIL": in C, I before V; in L, V before I). Phasors, rotating arrows, make these phase relations easy to add.'],
        'formulas_label': 'Formulas',
        'formulas': ['V_rms = V₀/√2, I_rms = I₀/√2', 'X_C = 1/(2πfC)', 'X_L = 2πfL', 'I_rms = V_rms/X'],
        'steps': ['Convert peak to RMS if needed.', 'Compute ω = 2πf.', 'Find X_C or X_L.', 'Use I = V/X.'],
        'worked_example': {
            'problem': 'Find the reactance of a 10 μF capacitor at 50 Hz and the RMS current from 230 V mains.',
            'steps': ['X_C = 1/(2π × 50 × 10 × 10⁻⁶) ≈ 318 Ω.', 'I = 230/318.', 'I ≈ 0.72 A.'],
            'answer': 'About 318 Ω and 0.72 A.',
            'check': 'At higher frequency X_C falls and the current rises ✓.'},
        'mistakes': ['Mixing peak and RMS values.', 'Using f where ω is needed (or vice versa).', 'Thinking a capacitor passes DC.', 'Getting lead and lag backwards.'],
        'real_world': 'Loudspeaker crossovers use capacitors to send high frequencies to the tweeter and inductors to send low frequencies to the woofer.',
        'exam_strategy': 'Check whether the question gives peak or RMS values before doing anything else.',
        'recap': ['RMS = peak/√2.', 'X_C falls with f.', 'X_L rises with f.', 'CIVIL.']},
    T2: {
        'overview': 'A series RLC circuit combines resistance and both reactances into an impedance. At resonance the reactances cancel.',
        'key_terms': ['Impedance', 'Phase angle', 'Resonant frequency', 'Power factor', 'Average power', 'Q factor', 'Tuning circuit'],
        'explanation': [
            'Z = √(R² + (X_L − X_C)²). With R = 100 Ω, L = 0.5 H and C = 10 μF at 50 Hz, X_L ≈ 157 Ω and X_C ≈ 318 Ω, so Z ≈ 190 Ω. On 230 V, I ≈ 1.21 A, and tan φ = (X_L − X_C)/R gives φ ≈ −58° (the circuit is capacitive, so the current leads).',
            'Only resistors dissipate energy: P = I²R ≈ 147 W here, or equivalently P = V_rms I_rms cos φ, where cos φ ≈ 0.53 is the power factor. Utilities penalise large industrial loads with low power factors because they draw current without delivering useful power.',
            'At resonance X_L = X_C, so f₀ = 1/(2π√(LC)) ≈ 71.2 Hz for this circuit; then Z = R and the current reaches its maximum, 2.3 A. Radios tune by adjusting C: 0.25 μH with about 10.1 pF resonates at 100 MHz, in the FM band.'],
        'formulas_label': 'Formulas',
        'formulas': ['Z = √(R² + (X_L − X_C)²)', 'tan φ = (X_L − X_C)/R', 'f₀ = 1/(2π√(LC))', 'P = I²R = V_rms I_rms cos φ', 'Power factor = cos φ = R/Z'],
        'steps': ['Compute X_L and X_C.', 'Find Z and I = V/Z.', 'Find φ and cos φ.', 'Compute P = I²R.'],
        'worked_example': {
            'problem': 'Find the resonant frequency of L = 0.5 H and C = 10 μF, and the current at resonance on 230 V with R = 100 Ω.',
            'steps': ['LC = 5 × 10⁻⁶ s².', 'f₀ = 1/(2π√(5 × 10⁻⁶)) ≈ 71.2 Hz.', 'At resonance Z = R, so I = 230/100 = 2.3 A.'],
            'answer': 'About 71.2 Hz; 2.3 A.',
            'check': 'At 71.2 Hz, 2πfL ≈ 224 Ω and 1/(2πfC) ≈ 224 Ω ✓.'},
        'mistakes': ['Adding R, X_L and X_C directly.', 'Forgetting the 2π in f₀.', 'Thinking capacitors or inductors consume average power.', 'Assuming the power factor is 1.'],
        'real_world': 'Wireless phone chargers use matched resonant coils so energy transfers efficiently at one frequency.',
        'exam_strategy': 'Draw the impedance triangle (R horizontal, X_L − X_C vertical); Z and φ come straight from it.',
        'recap': ['Impedance triangle.', 'Resonance: Z = R.', 'P = I²R.', 'Power factor cos φ.']},
    T3: {
        'overview': 'Maxwell\'s four equations summarise all of classical electromagnetism and reveal that light is an electromagnetic wave.',
        'key_terms': ['Gauss\'s law for E', 'Gauss\'s law for B', 'Faraday\'s law', 'Ampère–Maxwell law', 'Displacement current', 'Magnetic monopole'],
        'explanation': [
            'Gauss\'s law: ∮E·dA = q_enc/ε₀ (charges create electric fields). Gauss\'s law for magnetism: ∮B·dA = 0 (no magnetic monopoles; field lines always close).',
            'Faraday\'s law: ∮E·dl = −dΦ_B/dt (changing magnetic flux creates an electric field). Ampère–Maxwell law: ∮B·dl = μ₀I + μ₀ε₀ dΦ_E/dt (currents and changing electric flux create magnetic fields).',
            'Maxwell\'s addition, the displacement current ε₀ dΦ_E/dt, fixed a problem with charging capacitors (no current crosses the gap, yet a field circles it). With it, a changing E makes B and a changing B makes E, so the fields can sustain each other as a wave travelling at 1/√(μ₀ε₀) ≈ 3.00 × 10⁸ m/s.'],
        'formulas_label': 'Formulas',
        'formulas': ['∮E·dA = q_enc/ε₀', '∮B·dA = 0', '∮E·dl = −dΦ_B/dt', '∮B·dl = μ₀I + μ₀ε₀ dΦ_E/dt', 'c = 1/√(μ₀ε₀)'],
        'steps': ['Identify which equation describes the situation.', 'Decide whether it involves a surface (flux) or a loop (circulation).', 'Apply symmetry.', 'Interpret physically.'],
        'worked_example': {
            'problem': 'Show that 1/√(μ₀ε₀) gives the speed of light.',
            'steps': ['μ₀ε₀ = 4π × 10⁻⁷ × 8.85 × 10⁻¹² ≈ 1.112 × 10⁻¹⁷ s²/m².', '√(μ₀ε₀) ≈ 3.335 × 10⁻⁹ s/m.', '1/√(μ₀ε₀) ≈ 3.00 × 10⁸ m/s.'],
            'answer': 'About 3.00 × 10⁸ m/s, the measured speed of light.',
            'check': 'Two constants measured with charges and currents predict the speed of light ✓.'},
        'mistakes': ['Mixing up which equation has the zero (∮B·dA = 0).', 'Forgetting the displacement current term.', 'Confusing flux (surface) with circulation (loop).', 'Thinking magnetic monopoles have been found.'],
        'real_world': 'Every antenna, from cellphone masts to Wi-Fi routers, is designed with Maxwell\'s equations.',
        'exam_strategy': 'Learn the four in words first ("charges make E; no monopoles; changing B makes E; currents and changing E make B").',
        'recap': ['Gauss E.', 'Gauss B = 0.', 'Faraday.', 'Ampère–Maxwell.']},
    T4: {
        'overview': 'Electromagnetic waves are linked, perpendicular E and B fields travelling at c. They range from radio waves to gamma rays.',
        'key_terms': ['Transverse wave', 'Wave equation c = fλ', 'Electromagnetic spectrum', 'E = cB', 'Intensity', 'Inverse-square law', 'Radiation pressure', 'Polarisation'],
        'explanation': [
            'E and B are perpendicular to each other and to the direction of travel, with E = cB. A wave with E = 300 V/m has B = 1 μT. In vacuum all EM waves travel at c ≈ 3 × 10⁸ m/s and c = fλ: FM radio at 100 MHz has λ = 3 m; Wi-Fi at 2.4 GHz has λ = 12.5 cm; green light at 500 nm has f = 6 × 10¹⁴ Hz.',
            'The spectrum, in order of increasing frequency: radio, microwaves, infrared, visible, ultraviolet, X-rays, gamma rays. Higher frequency means more energy per photon, which is why UV and X-rays can damage cells.',
            'Waves carry energy: intensity I = P/(4πr²) from a point source, so a 100 W isotropic source gives about 1.99 W/m² at 2 m. They also carry momentum (radiation pressure I/c), the idea behind solar sails. Polarising filters transmit only one direction of E.'],
        'formulas_label': 'Formulas',
        'formulas': ['c = fλ', 'E = cB', 'I = P/(4πr²)', 'Radiation pressure = I/c (absorbed)', 'Malus: I = I₀ cos²θ'],
        'steps': ['Convert MHz, GHz and nm.', 'Use c = fλ.', 'Use E = cB for field amplitudes.', 'Use the inverse-square law for intensity.'],
        'worked_example': {
            'problem': 'Find the wavelength of 2.4 GHz Wi-Fi signals.',
            'steps': ['λ = c/f.', 'λ = 3 × 10⁸/2.4 × 10⁹.', 'λ = 0.125 m.'],
            'answer': '12.5 cm.',
            'check': 'Microwave ovens use a similar frequency; their door mesh holes are much smaller than 12.5 cm, which blocks the waves ✓.'},
        'mistakes': ['Forgetting to convert GHz or nm.', 'Thinking EM waves need a medium.', 'Getting the spectrum order wrong.', 'Using 1/r instead of 1/r² for intensity.'],
        'real_world': 'GPS, satellite TV, cellphones, X-ray machines and the light you read by are all electromagnetic waves.',
        'exam_strategy': 'Memorise the spectrum order with a mnemonic and the landmark values: visible light 400–700 nm.',
        'recap': ['c = fλ.', 'E = cB.', 'Spectrum order.', 'Inverse-square intensity.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The peak value of 230 V RMS mains is about:', ['325 V', '163 V', '230 V', '460 V'], 0, '× √2.', ans=325, num=True),
    Q(T1, 'The reactance of 10 μF at 50 Hz is about:', ['318 Ω', '3.14 Ω', '0.0031 Ω', '1590 Ω'], 0, '1/(2πfC).', ans=318, num=True),
    Q(T1, 'The reactance of 0.5 H at 50 Hz is about:', ['157 Ω', '25 Ω', '314 Ω', '0.0064 Ω'], 0, '2πfL.', ans=157, num=True),
    Q(T1, 'As frequency increases, a capacitor\'s reactance:', ['decreases', 'increases', 'stays the same', 'becomes infinite'], 0, 'X_C ∝ 1/f.'),
    Q(T1, 'In a pure inductor the current:', ['lags the voltage by 90°', 'leads the voltage by 90°', 'is in phase', 'lags by 180°'], 0, 'CIVIL.'),
    Q(T1, 'A capacitor in a DC circuit, once charged:', ['blocks current', 'passes maximum current', 'acts as a short circuit', 'has zero reactance'], 0, 'Infinite reactance at f = 0.'),
    # T2
    Q(T2, 'R = 100 Ω, X_L = 157 Ω, X_C = 318 Ω in series have impedance about:', ['190 Ω', '575 Ω', '261 Ω', '100 Ω'], 0, '√(100² + 161²).', ans=190, num=True),
    Q(T2, 'On 230 V the current is about:', ['1.21 A', '2.3 A', '0.40 A', '0.72 A'], 0, 'V/Z.', ans=1.21, num=True),
    Q(T2, 'The average power is about:', ['147 W', '279 W', '230 W', '0 W'], 0, 'I²R.', ans=147, num=True),
    Q(T2, 'The resonant frequency of 0.5 H and 10 μF is about:', ['71.2 Hz', '50 Hz', '447 Hz', '22.5 Hz'], 0, '1/(2π√(LC)).', ans=71.2, num=True),
    Q(T2, 'At resonance a series RLC circuit\'s impedance equals:', ['R', 'zero', 'X_L + X_C', 'infinity'], 0, 'Reactances cancel.'),
    Q(T2, 'The power factor of a circuit is:', ['cos φ = R/Z', 'tan φ', 'Z/R', 'X_L/X_C'], 0, 'Fraction of VI used.'),
    # T3
    Q(T3, 'Gauss\'s law for magnetism, ∮B·dA = 0, means:', ['there are no magnetic monopoles', 'magnetic fields are zero', 'currents make no field', 'flux is always maximum'], 0, 'Field lines close.'),
    Q(T3, 'Faraday\'s law says a changing magnetic flux produces:', ['an electric field', 'a magnetic monopole', 'a charge', 'a current only in metals'], 0, '∮E·dl = −dΦ_B/dt.'),
    Q(T3, 'Maxwell\'s displacement current is proportional to:', ['the rate of change of electric flux', 'the magnetic flux', 'the charge enclosed', 'the resistance'], 0, 'ε₀ dΦ_E/dt.'),
    Q(T3, '1/√(μ₀ε₀) is approximately:', ['3.00 × 10⁸ m/s', '3.00 × 10⁶ m/s', '9.0 × 10¹⁶ m/s', '1.0 × 10⁸ m/s'], 0, 'The speed of light.'),
    Q(T3, 'Which equation states that electric charges create electric fields?', ['Gauss\'s law', 'Faraday\'s law', 'Gauss\'s law for magnetism', 'Lenz\'s law'], 0, '∮E·dA = q/ε₀.'),
    Q(T3, 'Maxwell\'s equations showed that light is:', ['an electromagnetic wave', 'a stream of electrons', 'a sound wave', 'a magnetic monopole'], 0, 'Predicted speed matched c.'),
    # T4
    Q(T4, 'The wavelength of 100 MHz FM radio is:', ['3 m', '30 m', '0.3 m', '300 m'], 0, 'c/f.', ans=3, num=True),
    Q(T4, 'The wavelength of 2.4 GHz Wi-Fi is:', ['12.5 cm', '1.25 cm', '125 cm', '8 cm'], 0, 'c/f.'),
    Q(T4, 'A wave with E = 300 V/m has a magnetic field of:', ['1 μT', '3 μT', '9 × 10¹⁰ T', '300 T'], 0, 'E/c.', ans=1, num=True),
    Q(T4, 'A 100 W point source gives an intensity at 2 m of about:', ['1.99 W/m²', '25 W/m²', '3.98 W/m²', '0.50 W/m²'], 0, 'P/(4πr²).'),
    Q(T4, 'Which has the highest frequency?', ['gamma rays', 'X-rays', 'visible light', 'microwaves'], 0, 'Top of the spectrum.'),
    Q(T4, 'In an EM wave, E and B are:', ['perpendicular to each other and to the direction of travel', 'parallel to each other', 'parallel to the direction of travel', 'out of phase by 90° and parallel'], 0, 'Transverse.'),
]

FLASH = [
    ['RMS value', 'V_rms = V₀/√2.'],
    ['Capacitive reactance', 'X_C = 1/(2πfC).'],
    ['Inductive reactance', 'X_L = 2πfL.'],
    ['Impedance', 'Z = √(R² + (X_L − X_C)²).'],
    ['Resonance', 'f₀ = 1/(2π√(LC)); Z = R.'],
    ['Power factor', 'cos φ = R/Z; P = V_rms I_rms cos φ.'],
    ['Maxwell\'s equations', 'Gauss E, Gauss B (= 0), Faraday, Ampère–Maxwell.'],
    ['EM waves', 'c = fλ = 1/√(μ₀ε₀); E = cB.'],
]
