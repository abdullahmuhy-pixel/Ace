"""Differential Equations, module 3: Second-order linear equations."""
import math
from verify import Q, x, t, sp
T1, T2, T3, T4 = ('Homogeneous equations with constant coefficients', 'Undetermined coefficients', 'Variation of parameters', 'Mechanical vibrations')
y = sp.Function('y')
D = lambda e, ics=None: sp.dsolve(e, y(x), ics=ics).rhs
L = lambda f, a, b, c: sp.simplify(a * sp.diff(f, x, 2) + b * sp.diff(f, x) + c * f)
assert sp.simplify(D(y(x).diff(x, 2) - y(x), {y(0): 2, y(x).diff(x).subs(x, 0): 0}) - (sp.exp(x) + sp.exp(-x))) == 0
assert sp.simplify(D(y(x).diff(x, 2) + 4 * y(x), {y(0): 1, y(x).diff(x).subs(x, 0): 4}) - (sp.cos(2 * x) + 2 * sp.sin(2 * x))) == 0
assert sp.solve(sp.Symbol('r') ** 2 - 5 * sp.Symbol('r') + 6) == [2, 3]
assert L((1 + x) * sp.exp(-x), 1, 2, 1) == 0 and L(sp.exp(x) * sp.cos(2 * x), 1, -2, 5) == 0
assert L(sp.Integer(-3), 1, 0, -1) == 3 and L(x ** 2 - 2, 1, 0, 1) == x ** 2
assert sp.simplify(L(sp.exp(3 * x) / 2, 1, -3, 2) - sp.exp(3 * x)) == 0
assert sp.simplify(L(x * sp.exp(x) / 2, 1, 0, -1) - sp.exp(x)) == 0
assert sp.simplify(L(x ** 2 * sp.exp(-x) / 2, 1, 2, 1) - sp.exp(-x)) == 0
assert sp.simplify(L(x * sp.sin(x) + sp.cos(x) * sp.log(sp.cos(x)), 1, 0, 1) - 1 / sp.cos(x)) == 0
assert sp.simplify(L(x * sp.exp(x) * sp.log(x), 1, -2, 1) - sp.exp(x) / x) == 0
assert sp.simplify(sp.wronskian([sp.exp(2 * x), sp.exp(3 * x)], x) - sp.exp(5 * x)) == 0 and sp.simplify(sp.wronskian([sp.cos(x), sp.sin(x)], x)) == 1
assert math.isclose(2 * math.pi / 4, math.pi / 2) and 2 * math.sqrt(16) == 8 and math.hypot(3, 4) == 5
assert round(2 * 9.8 / 0.49, 6) == 40 and round(math.sqrt(40 / 2), 2) == 4.47
assert sp.solve(sp.Symbol('r') ** 2 + 10 * sp.Symbol('r') + 16) == [-8, -2]

MODULE = {
    'title': 'Second-order linear equations',
    'topics': [T1, T2, T3, T4],
    'overview': 'Second-order linear equations describe springs, circuits and beams. This module solves the homogeneous constant-coefficient case with the characteristic equation, finds particular solutions by undetermined coefficients and variation of parameters, and applies everything to mechanical vibrations and resonance.',
    'key_terms': ['Characteristic equation', 'Fundamental set', 'Wronskian', 'Superposition', 'Particular solution', 'Undetermined coefficients', 'Resonance', 'Variation of parameters', 'Natural frequency', 'Damping', 'Overdamped', 'Critically damped', 'Underdamped'],
    'explanation': [
        'For ay″ + by′ + cy = 0, try y = eʳˣ. This gives the characteristic equation ar² + br + c = 0. Two real roots, a repeated root and complex roots give the three solution forms. Two independent solutions (non-zero Wronskian) combine into the general solution.',
        'For a non-homogeneous equation ay″ + by′ + cy = g(x), the general solution is y = y_h + y_p: the homogeneous solution plus any one particular solution. Guess y_p from the form of g (undetermined coefficients), or build it from y_h with variation of parameters, which works for any g.',
        'A mass on a spring obeys my″ + cy′ + ky = F(t). The roots of the characteristic equation decide whether the motion oscillates (underdamped), returns slowly (overdamped) or returns as fast as possible without oscillating (critically damped). Forcing at the natural frequency causes resonance.'],
    'quick_facts': [
        'ar² + br + c = 0: real r₁ ≠ r₂ ⇒ C₁e^(r₁x) + C₂e^(r₂x).',
        'Repeated r ⇒ (C₁ + C₂x)eʳˣ.',
        'r = α ± βi ⇒ e^(αx)(C₁cos βx + C₂sin βx).',
        'y = y_h + y_p.',
        'Natural frequency ω₀ = √(k/m); critical damping c = 2√(mk).'],
}

NOTES = {
    T1: {
        'overview': 'Constant-coefficient homogeneous equations reduce to a quadratic: the characteristic equation.',
        'key_terms': ['Characteristic equation', 'Distinct real roots', 'Repeated root', 'Complex roots', 'Euler\'s formula', 'Wronskian', 'Linear independence'],
        'explanation': [
            'Substituting y = eʳˣ into ay″ + by′ + cy = 0 gives ar² + br + c = 0. For y″ − 5y′ + 6y = 0, r² − 5r + 6 = 0 gives r = 2, 3, so y = C₁e²ˣ + C₂e³ˣ.',
            'A repeated root r gives eʳˣ and xeʳˣ: for y″ + 2y′ + y = 0 (r = −1, twice), y = (C₁ + C₂x)e^(−x). Complex roots α ± βi give e^(αx)cos βx and e^(αx)sin βx: for y″ − 2y′ + 5y = 0 (r = 1 ± 2i), y = eˣ(C₁cos 2x + C₂sin 2x); for y″ + 4y = 0, y = C₁cos 2x + C₂sin 2x.',
            'Two solutions are independent when their Wronskian W = y₁y₂′ − y₁′y₂ is not zero: W(e²ˣ, e³ˣ) = e⁵ˣ and W(cos x, sin x) = 1. Initial conditions then fix C₁ and C₂: for y″ − y = 0 with y(0) = 2, y′(0) = 0, y = eˣ + e^(−x).'],
        'formulas_label': 'Three cases',
        'formulas': ['r₁ ≠ r₂ real: y = C₁e^(r₁x) + C₂e^(r₂x)', 'r repeated: y = (C₁ + C₂x)eʳˣ', 'r = α ± βi: y = e^(αx)(C₁cos βx + C₂sin βx)', 'W = y₁y₂′ − y₁′y₂'],
        'steps': ['Write the characteristic equation.', 'Solve for r and identify the case.', 'Write the general solution.', 'Use initial conditions for C₁ and C₂.'],
        'worked_example': {
            'problem': 'Solve y″ + 4y = 0 with y(0) = 1, y′(0) = 4.',
            'steps': ['r² + 4 = 0 ⇒ r = ±2i, so y = C₁cos 2x + C₂sin 2x.', 'y(0) = C₁ = 1.', 'y′ = −2C₁sin 2x + 2C₂cos 2x, y′(0) = 2C₂ = 4 ⇒ C₂ = 2. So y = cos 2x + 2sin 2x.'],
            'answer': 'y = cos 2x + 2 sin 2x.',
            'check': 'y″ = −4cos 2x − 8sin 2x = −4y ✓.'},
        'mistakes': ['Forgetting the x in the repeated-root case.', 'Writing e^(βx) instead of using α for complex roots.', 'Sign errors in the characteristic equation.', 'Applying y′(0) to the wrong derivative.'],
        'real_world': 'The same equation, with complex roots, describes the vibration of a guitar string and the current in an LC radio-tuning circuit.',
        'exam_strategy': 'State the case explicitly ("repeated root r = −1") before writing the solution; it shows the method.',
        'recap': ['Characteristic quadratic.', 'Three cases.', 'Wronskian ≠ 0.', 'Fix constants with ICs.']},
    T2: {
        'overview': 'Undetermined coefficients guesses the form of a particular solution from the forcing term g(x), then finds the coefficients.',
        'key_terms': ['Particular solution', 'Trial function', 'Superposition principle', 'Resonance (duplication)', 'Modification rule'],
        'explanation': [
            'Choose a trial y_p that looks like g and all its derivatives: a polynomial for a polynomial, Ae^(kx) for e^(kx), A cos ωx + B sin ωx for sines and cosines. For y″ + y = x², try Ax² + Bx + C: matching gives y_p = x² − 2. For y″ − 3y′ + 2y = e³ˣ, try Ae³ˣ: 9A − 9A + 2A = 1, so y_p = e³ˣ/2. For y″ − y = 3, y_p = −3.',
            'If the trial already solves the homogeneous equation, multiply it by x (and by x again if needed). For y″ − y = eˣ, eˣ is in y_h, so try Axeˣ: y_p = (x/2)eˣ. For y″ + 2y′ + y = e^(−x), both e^(−x) and xe^(−x) are in y_h, so try Ax²e^(−x): y_p = x²e^(−x)/2.',
            'For y″ + 4y = sin 2x, sin 2x and cos 2x are homogeneous solutions, so try x(A cos 2x + B sin 2x). If g is a sum, find a y_p for each part and add them (superposition).'],
        'formulas_label': 'Trial forms',
        'formulas': ['g = polynomial degree n ⇒ Aₙxⁿ + … + A₀', 'g = e^(kx) ⇒ Ae^(kx)', 'g = cos ωx or sin ωx ⇒ A cos ωx + B sin ωx', 'If the trial is in y_h, multiply by x (or x²)'],
        'steps': ['Find y_h first.', 'Write the trial y_p from g.', 'Modify by x if it overlaps y_h.', 'Substitute, match coefficients, add y_h.'],
        'worked_example': {
            'problem': 'Find a particular solution of y″ − y = eˣ.',
            'steps': ['y_h = C₁eˣ + C₂e^(−x) contains eˣ, so try y_p = Axeˣ.', 'y_p″ = A(x + 2)eˣ; y_p″ − y_p = 2Aeˣ.', '2A = 1 ⇒ A = 1/2: y_p = (x/2)eˣ.'],
            'answer': 'y_p = (x/2)eˣ.',
            'check': 'Substituting gives exactly eˣ ✓.'},
        'mistakes': ['Not checking overlap with y_h.', 'Using only A sin ωx for a sine forcing term.', 'Forgetting lower-degree terms in polynomial trials.', 'Adding y_h before finding coefficients.'],
        'real_world': 'Engineers predict the steady vibration of a machine driven by a rotating motor by finding y_p for a sinusoidal forcing term.',
        'exam_strategy': 'Always write y_h before guessing y_p; the overlap check is a common source of lost marks.',
        'recap': ['Trial from g.', 'Multiply by x on overlap.', 'Match coefficients.', 'y = y_h + y_p.']},
    T3: {
        'overview': 'Variation of parameters finds a particular solution for any forcing term, using the homogeneous solutions and the Wronskian.',
        'key_terms': ['Variation of parameters', 'Wronskian', 'Standard form', 'Non-constant coefficients'],
        'explanation': [
            'Write the equation in standard form y″ + p(x)y′ + q(x)y = g(x) with homogeneous solutions y₁, y₂. Then y_p = u₁y₁ + u₂y₂, where u₁′ = −y₂g/W and u₂′ = y₁g/W, with W = W(y₁, y₂).',
            'For y″ + y = sec x: y₁ = cos x, y₂ = sin x, W = 1. u₁′ = −sin x sec x = −tan x, so u₁ = ln|cos x|; u₂′ = cos x sec x = 1, so u₂ = x. Hence y_p = cos x ln|cos x| + x sin x, which undetermined coefficients cannot find.',
            'For y″ − 2y′ + y = eˣ/x: y₁ = eˣ, y₂ = xeˣ, W = e²ˣ. u₁′ = −1, u₂′ = 1/x, so y_p = −xeˣ + xeˣ ln x; the −xeˣ is part of y_h, leaving y_p = xeˣ ln x.'],
        'formulas_label': 'Formulas',
        'formulas': ['y_p = u₁y₁ + u₂y₂', 'u₁′ = −y₂g/W, u₂′ = y₁g/W', 'W = y₁y₂′ − y₁′y₂', 'Use standard form (coefficient of y″ = 1)'],
        'steps': ['Put the equation in standard form.', 'Find y₁, y₂ and W.', 'Integrate u₁′ and u₂′.', 'Form y_p and drop any part already in y_h.'],
        'worked_example': {
            'problem': 'Find a particular solution of y″ + y = sec x.',
            'steps': ['y₁ = cos x, y₂ = sin x, W = 1.', 'u₁ = ∫−tan x dx = ln|cos x|; u₂ = ∫1 dx = x.', 'y_p = cos x ln|cos x| + x sin x.'],
            'answer': 'y_p = x sin x + cos x ln|cos x|.',
            'check': 'Substitution gives y_p″ + y_p = sec x ✓.'},
        'mistakes': ['Not dividing by the coefficient of y″ first.', 'Swapping the signs of u₁′ and u₂′.', 'Wrong Wronskian.', 'Adding constants of integration (not needed for y_p).'],
        'real_world': 'Variation of parameters is how engineers handle forcing terms that are not simple sines or exponentials, such as the shock load on a car suspension.',
        'exam_strategy': 'Learn the u₁′ and u₂′ formulas exactly, with the minus sign on u₁′.',
        'recap': ['Works for any g.', 'Needs y₁, y₂, W.', 'Integrate u′s.', 'Standard form first.']},
    T4: {
        'overview': 'A mass on a spring is the classic second-order system. Damping and forcing produce decay, oscillation and resonance.',
        'key_terms': ['Hooke\'s law', 'Natural frequency', 'Period', 'Amplitude', 'Damping coefficient', 'Underdamped', 'Critically damped', 'Overdamped', 'Resonance'],
        'explanation': [
            'Newton\'s second law gives my″ + cy′ + ky = F(t). Without damping or forcing, y = C₁cos ω₀t + C₂sin ω₀t with natural frequency ω₀ = √(k/m) and period 2π/ω₀. For m = 1, k = 16: ω₀ = 4 and the period is π/2. The amplitude of 3cos 4t + 4sin 4t is √(3² + 4²) = 5.',
            'Find k from a static stretch: a 2 kg mass that stretches a spring 0.49 m gives k = mg/s = 2 × 9.8/0.49 = 40 N/m and ω₀ = √(40/2) ≈ 4.47 rad/s.',
            'With damping, the characteristic roots decide the behaviour: c² < 4mk underdamped (decaying oscillation), c² = 4mk critically damped, c² > 4mk overdamped. For m = 1, k = 16 critical damping is c = 8; with c = 10 the roots are −2 and −8 (overdamped). Undamped forcing at ω = ω₀ makes the amplitude grow without limit: resonance.'],
        'formulas_label': 'Formulas',
        'formulas': ['my″ + cy′ + ky = F(t)', 'ω₀ = √(k/m), period T = 2π/ω₀', 'Amplitude of A cos ωt + B sin ωt = √(A² + B²)', 'Critical damping: c = 2√(mk)', 'k = mg/s from a static stretch'],
        'steps': ['Find m, c, k (and k from the stretch if needed).', 'Write the characteristic equation.', 'Classify the damping.', 'Use initial conditions and interpret the motion.'],
        'worked_example': {
            'problem': 'A system has m = 1, k = 16. Find ω₀ and the period, the critical damping, and the type of motion when c = 10.',
            'steps': ['ω₀ = √16 = 4, period 2π/4 = π/2.', 'Critical c = 2√(1 × 16) = 8.', 'c = 10 > 8: r² + 10r + 16 = 0 ⇒ r = −2, −8: overdamped.'],
            'answer': 'ω₀ = 4, period π/2, critical c = 8; c = 10 is overdamped.',
            'check': 'Two negative real roots mean decay without oscillation ✓.'},
        'mistakes': ['Using k/m instead of √(k/m).', 'Confusing frequency (rad/s) with period.', 'Getting the damping inequality backwards.', 'Forgetting g when finding k from a stretch.'],
        'real_world': 'Car shock absorbers are tuned near critical damping so the car settles quickly after a bump without bouncing.',
        'exam_strategy': 'Compare c² with 4mk before solving: the classification tells you which solution form to write.',
        'recap': ['ω₀ = √(k/m).', 'Damping by c² vs 4mk.', 'Amplitude √(A² + B²).', 'Resonance at ω = ω₀.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The roots of the characteristic equation of y″ − 5y′ + 6y = 0 are:', ['2 and 3', '−2 and −3', '1 and 6', '5 and 6'], 0, 'r² − 5r + 6 = 0.', ans=(2, 3)),
    Q(T1, 'The general solution of y″ + 2y′ + y = 0 is:', ['(C₁ + C₂x)e^(−x)', 'C₁e^(−x) + C₂e^(−x)', 'C₁eˣ + C₂e^(−x)', 'C₁cos x + C₂sin x'], 0, 'Repeated root −1.'),
    Q(T1, 'The general solution of y″ − 2y′ + 5y = 0 is:', ['eˣ(C₁cos 2x + C₂sin 2x)', 'e²ˣ(C₁cos x + C₂sin x)', 'C₁eˣ + C₂e⁵ˣ', 'C₁cos 2x + C₂sin 2x'], 0, 'r = 1 ± 2i.'),
    Q(T1, 'Solve y″ − y = 0 with y(0) = 2, y′(0) = 0:', ['eˣ + e^(−x)', '2eˣ', '2e^(−x)', 'eˣ − e^(−x)'], 0, 'C₁ = C₂ = 1.', ans=sp.exp(x) + sp.exp(-x)),
    Q(T1, 'Solve y″ + 4y = 0 with y(0) = 1, y′(0) = 4:', ['cos 2x + 2sin 2x', 'cos 2x + 4sin 2x', '2cos 2x + sin 2x', 'cos x + 4sin x'], 0, 'C₂ = 4/2.', ans=sp.cos(2 * x) + 2 * sp.sin(2 * x)),
    Q(T1, 'The Wronskian W(e²ˣ, e³ˣ) is:', ['e^(5x)', 'e^(6x)', '0', 'e^(x)'], 0, 'e²ˣ·3e³ˣ − 2e²ˣ·e³ˣ.', ans=sp.exp(5 * x)),
    # T2
    Q(T2, 'A particular solution of y″ − y = 3 is:', ['−3', '3', '3x', '−3x'], 0, '0 − A = 3.', ans=-3),
    Q(T2, 'A particular solution of y″ + y = x² is:', ['x² − 2', 'x²', 'x² + 2', '2 − x²'], 0, 'Try Ax² + Bx + C.', ans=x ** 2 - 2),
    Q(T2, 'A particular solution of y″ − 3y′ + 2y = e³ˣ is:', ['e^(3x)/2', 'e^(3x)', 'e^(3x)/20', '2e^(3x)'], 0, '9A − 9A + 2A = 1.', ans=sp.exp(3 * x) / 2),
    Q(T2, 'A particular solution of y″ − y = eˣ is:', ['(x/2)e^x', 'e^x/2', 'xe^x', '2xe^x'], 0, 'Overlap: multiply by x.', ans=x * sp.exp(x) / 2),
    Q(T2, 'A particular solution of y″ + 2y′ + y = e^(−x) is:', ['x²e^(−x)/2', 'xe^(−x)', 'e^(−x)/4', 'x²e^(−x)'], 0, 'Double overlap: multiply by x².', ans=x ** 2 * sp.exp(-x) / 2),
    Q(T2, 'The correct trial for y″ + 4y = sin 2x is:', ['x(A cos 2x + B sin 2x)', 'A sin 2x', 'A cos 2x + B sin 2x', 'Ax sin 2x only'], 0, 'sin 2x is homogeneous.'),
    # T3
    Q(T3, 'The Wronskian W(cos x, sin x) is:', ['1', '0', 'cos 2x', '−1'], 0, 'cos² x + sin² x.', ans=1),
    Q(T3, 'In variation of parameters, u₁′ equals:', ['−y₂g/W', 'y₂g/W', 'y₁g/W', '−y₁g/W'], 0, 'With the minus sign.'),
    Q(T3, 'A particular solution of y″ + y = sec x is:', ['x sin x + cos x ln|cos x|', 'x cos x', 'sin x ln|sec x|', 'tan x'], 0, 'u₁ = ln|cos x|, u₂ = x.'),
    Q(T3, 'A particular solution of y″ − 2y′ + y = eˣ/x (x > 0) is:', ['xe^x ln x', 'e^x ln x', 'x²e^x', 'e^x/x'], 0, 'After dropping −xeˣ.', ans=x * sp.exp(x) * sp.log(x)),
    Q(T3, 'Variation of parameters is needed (rather than undetermined coefficients) for:', ['g(x) = tan x', 'g(x) = e^(2x)', 'g(x) = x³', 'g(x) = sin 3x'], 0, 'tan x has no finite trial form.'),
    Q(T3, 'Before applying the formulas, the equation must have:', ['coefficient 1 on y″', 'constant coefficients', 'zero forcing', 'real roots'], 0, 'Standard form.'),
    # T4
    Q(T4, 'For m = 1 and k = 16, the natural frequency ω₀ is:', ['4', '16', '1/4', '8'], 0, '√(k/m).', ans=4),
    Q(T4, 'Its period is:', ['π/2', '2π', 'π/4', '4π'], 0, '2π/4.', ans=sp.pi / 2),
    Q(T4, 'The amplitude of 3cos 4t + 4sin 4t is:', ['5', '7', '1', '12'], 0, '√(9 + 16).', ans=5),
    Q(T4, 'For m = 1, k = 16, critical damping occurs when c =', ['8', '4', '16', '32'], 0, '2√(mk).', ans=8),
    Q(T4, 'With m = 1, k = 16 and c = 10, the motion is:', ['overdamped', 'underdamped', 'critically damped', 'undamped'], 0, 'c² = 100 > 4mk = 64.'),
    Q(T4, 'A 2 kg mass stretches a spring 0.49 m (g = 9.8). The spring constant is:', ['40 N/m', '4.08 N/m', '19.6 N/m', '0.98 N/m'], 0, 'mg/s.'),
]

FLASH = [
    ['Characteristic equation', 'ar² + br + c = 0 from y = eʳˣ.'],
    ['Repeated root', 'y = (C₁ + C₂x)eʳˣ.'],
    ['Complex roots α ± βi', 'y = e^(αx)(C₁cos βx + C₂sin βx).'],
    ['General solution', 'y = y_h + y_p.'],
    ['Modification rule', 'Multiply the trial by x if it already solves the homogeneous equation.'],
    ['Variation of parameters', 'u₁′ = −y₂g/W, u₂′ = y₁g/W.'],
    ['Natural frequency', 'ω₀ = √(k/m).'],
    ['Critical damping', 'c = 2√(mk); c² < 4mk underdamped, > overdamped.'],
]
