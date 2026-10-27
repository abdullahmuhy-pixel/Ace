"""Differential Equations, module 5: Systems, stability, series and Fourier series."""
from verify import Q, x, n, sp
T1, T2, T3, T4 = ('Linear systems and eigenvalues', 'The phase plane and stability', 'Power series solutions', 'Introduction to Fourier series')
lam = sp.Symbol('lam')
ev = lambda M: sorted(sp.Matrix(M).eigenvals().keys(), key=lambda z: (sp.re(z), sp.im(z)))
assert ev([[1, 2], [2, 1]]) == [-1, 3] and ev([[-2, 1], [1, -2]]) == [-3, -1] and ev([[-1, 0], [0, -2]]) == [-2, -1]
assert ev([[0, 2], [-2, 0]]) == [-2 * sp.I, 2 * sp.I] and ev([[-1, 2], [-2, -1]]) == [-1 - 2 * sp.I, -1 + 2 * sp.I]
A = sp.Matrix([[1, 2], [2, 1]]); assert A * sp.Matrix([1, 1]) == 3 * sp.Matrix([1, 1]) and A * sp.Matrix([1, -1]) == -sp.Matrix([1, -1])
assert sp.Matrix([[0, 1], [-2, -3]]).eigenvals() == {-1: 1, -2: 1}
assert sp.Matrix([[3, 1], [2, -1]]).det() == -5
nn = sp.Symbol('nn', integer=True, positive=True)
b = lambda f, a, c: sp.simplify(sp.integrate(f * sp.sin(nn * x), (x, a, c)) / sp.pi)
assert sp.simplify(b(x, -sp.pi, sp.pi) - 2 * (-1) ** (nn + 1) / nn) == 0
assert sp.integrate(sp.Abs(x), (x, -sp.pi, sp.pi)) / sp.pi == sp.pi
sq = sp.simplify((sp.integrate(sp.sin(nn * x), (x, 0, sp.pi)) - sp.integrate(sp.sin(nn * x), (x, -sp.pi, 0))) / sp.pi)
assert sp.simplify(sq.subs(nn, 1) - 4 / sp.pi) == 0 and sq.subs(nn, 2) == 0 and sp.simplify(sq.subs(nn, 3) - 4 / (3 * sp.pi)) == 0
y = sp.Function('y')
assert sp.dsolve(y(x).diff(x, 2) + y(x), y(x), ics={y(0): 1, y(x).diff(x).subs(x, 0): 0}).rhs.series(x, 0, 6).removeO() == 1 - x ** 2 / 2 + x ** 4 / 24

MODULE = {
    'title': 'Systems, stability, series and Fourier series',
    'topics': [T1, T2, T3, T4],
    'overview': 'Real systems have several interacting quantities. This module solves linear systems x′ = Ax with eigenvalues, reads their behaviour from the phase plane, finds power series solutions when closed forms fail, and introduces Fourier series, which build periodic functions from sines and cosines.',
    'key_terms': ['System of ODEs', 'Eigenvalue', 'Eigenvector', 'Phase plane', 'Node', 'Saddle', 'Spiral', 'Centre', 'Stability', 'Power series', 'Recurrence relation', 'Ordinary point', 'Fourier series', 'Fourier coefficients'],
    'explanation': [
        'A linear system x′ = Ax is solved by vectors eˡᵗv where λ is an eigenvalue of A and v its eigenvector. Any higher-order equation can be rewritten as a first-order system, so this is the general framework.',
        'The eigenvalues also describe the picture: real negative ones give a stable node, opposite signs a saddle, complex ones spirals or centres. Engineers and ecologists use this to decide whether an equilibrium is safe.',
        'When coefficients vary, assume a power series y = Σaₙxⁿ and find a recurrence for the coefficients. For periodic forcing, Fourier series write a function as a sum of sines and cosines, the basis of signal processing.'],
    'quick_facts': [
        'x′ = Ax: x = c₁e^(λ₁t)v₁ + c₂e^(λ₂t)v₂.',
        'Saddle: real eigenvalues of opposite sign (det A < 0).',
        'Stable: all eigenvalues have negative real part (tr A < 0, det A > 0).',
        'Power series: substitute Σaₙxⁿ and match powers to get a recurrence.',
        'Fourier: f(x) = a₀/2 + Σ(aₙcos nx + bₙsin nx) on (−π, π).'],
}

NOTES = {
    T1: {
        'overview': 'Systems of linear ODEs with constant coefficients are solved with eigenvalues and eigenvectors.',
        'key_terms': ['Coefficient matrix', 'Eigenvalue', 'Eigenvector', 'Characteristic polynomial', 'Fundamental solutions', 'Converting to a system'],
        'explanation': [
            'For x′ = Ax, try x = eˡᵗv: then Av = λv, so λ is an eigenvalue and v an eigenvector. For A = [1 2; 2 1], det(A − λI) = (1 − λ)² − 4 = 0 gives λ = 3 with v = (1, 1) and λ = −1 with v = (1, −1). The general solution is x = c₁e³ᵗ(1, 1) + c₂e^(−t)(1, −1).',
            'Complex eigenvalues λ = α ± βi give solutions with e^(αt)cos βt and e^(αt)sin βt, like rotation combined with growth or decay. For A = [0 2; −2 0], λ = ±2i: solutions rotate around the origin.',
            'Any nth-order equation becomes a system. For y″ + 3y′ + 2y = 0, set x₁ = y, x₂ = y′: then x₁′ = x₂ and x₂′ = −2x₁ − 3x₂, with matrix [0 1; −2 −3] whose eigenvalues −1 and −2 match the characteristic roots.'],
        'formulas_label': 'Formulas',
        'formulas': ['det(A − λI) = 0', 'Av = λv', 'x = c₁e^(λ₁t)v₁ + c₂e^(λ₂t)v₂ (distinct real λ)', 'For 2 × 2: λ² − (tr A)λ + det A = 0'],
        'steps': ['Find the eigenvalues from det(A − λI) = 0.', 'Find an eigenvector for each.', 'Write the general solution.', 'Use initial conditions for the constants.'],
        'worked_example': {
            'problem': 'Solve x′ = Ax with A = [1 2; 2 1].',
            'steps': ['λ² − 2λ − 3 = 0 ⇒ λ = 3, −1.', 'λ = 3: (A − 3I)v = 0 ⇒ v = (1, 1). λ = −1: v = (1, −1).', 'x = c₁e³ᵗ(1, 1) + c₂e^(−t)(1, −1).'],
            'answer': 'x = c₁e³ᵗ(1, 1) + c₂e^(−t)(1, −1).',
            'check': 'A(1, 1) = (3, 3) = 3(1, 1) ✓ and A(1, −1) = (−1, 1) = −(1, −1) ✓.'},
        'mistakes': ['Pairing an eigenvector with the wrong eigenvalue.', 'Arithmetic slips in the characteristic polynomial.', 'Forgetting the second solution.', 'Writing eigenvectors as rows and multiplying wrongly.'],
        'real_world': 'Drug concentrations in blood and tissue are modelled as a two-compartment linear system, solved exactly this way.',
        'exam_strategy': 'Check each eigenvector by multiplying it by A; it takes seconds and catches most errors.',
        'recap': ['eˡᵗv solutions.', 'Eigenvalues from det(A − λI).', 'Combine solutions.', 'Higher order → system.']},
    T2: {
        'overview': 'The phase plane plots solution trajectories (x₁, x₂). The eigenvalues classify the equilibrium at the origin.',
        'key_terms': ['Phase portrait', 'Equilibrium', 'Stable node', 'Unstable node', 'Saddle point', 'Spiral', 'Centre', 'Trace', 'Determinant'],
        'explanation': [
            'Real eigenvalues of the same sign give a node: both negative (e.g. −1, −2 or −1, −3) is a stable node, where all trajectories flow into the origin; both positive is unstable. Opposite signs (3 and −1) give a saddle, which is unstable.',
            'Complex eigenvalues α ± βi give spirals: α < 0 stable spiral (e.g. −1 ± 2i), α > 0 unstable spiral. Purely imaginary eigenvalues (±2i) give a centre: closed orbits that neither grow nor decay.',
            'For a 2 × 2 matrix, the trace and determinant decide quickly: det < 0 means a saddle; det > 0 with trace < 0 is stable; det > 0 with trace > 0 is unstable. For [3 1; 2 −1], det = −5, so the origin is a saddle.'],
        'formulas_label': 'Classification',
        'formulas': ['Real λ, same sign: node (stable if negative)', 'Real λ, opposite signs: saddle (unstable)', 'α ± βi: spiral (stable if α < 0)', '±βi: centre', 'det < 0 ⇒ saddle; det > 0, tr < 0 ⇒ stable'],
        'steps': ['Compute the trace and determinant.', 'Find the eigenvalues if needed.', 'Classify the equilibrium.', 'Sketch the trajectories.'],
        'worked_example': {
            'problem': 'Classify the origin for x′ = Ax with A = [−1 2; −2 −1].',
            'steps': ['tr A = −2, det A = 1 + 4 = 5.', 'λ² + 2λ + 5 = 0 ⇒ λ = −1 ± 2i.', 'Complex with negative real part: stable spiral.'],
            'answer': 'A stable spiral.',
            'check': 'det > 0 and tr < 0 confirm stability ✓.'},
        'mistakes': ['Calling a saddle stable because one eigenvalue is negative.', 'Confusing a centre with a stable spiral.', 'Using only the trace.', 'Mixing up the roles of trace and determinant.'],
        'real_world': 'Predator-prey populations near equilibrium circle in the phase plane, much like a centre, which is why fox and rabbit numbers rise and fall in cycles.',
        'exam_strategy': 'Compute det A first: if it is negative, you are done (saddle) without solving for eigenvalues.',
        'recap': ['Node, saddle, spiral, centre.', 'Sign of real parts decides stability.', 'det < 0 ⇒ saddle.', 'Trace-determinant shortcut.']},
    T3: {
        'overview': 'When coefficients are not constant, power series give solutions as infinite polynomials, built from a recurrence for the coefficients.',
        'key_terms': ['Power series', 'Ordinary point', 'Singular point', 'Recurrence relation', 'Radius of convergence', 'Index shift'],
        'explanation': [
            'At an ordinary point x = 0, assume y = Σaₙxⁿ, substitute, shift indices so every sum has xⁿ, and set each coefficient to zero. For y′ = y: (n + 1)aₙ₊₁ = aₙ, so aₙ = a₀/n! and y = a₀eˣ, as expected.',
            'For y″ + y = 0: (n + 2)(n + 1)aₙ₊₂ = −aₙ, so aₙ₊₂ = −aₙ/((n + 2)(n + 1)). With y(0) = 1, y′(0) = 0: y = 1 − x²/2 + x⁴/24 − … = cos x. For Airy\'s equation y″ − xy = 0: a₂ = 0 and aₙ₊₂ = aₙ₋₁/((n + 2)(n + 1)), a solution with no elementary formula.',
            'The series converges at least up to the nearest singular point (in the complex plane). For (1 + x²)y″ + … = 0, the singular points are ±i, so a series about 0 converges for |x| < 1.'],
        'formulas_label': 'Method',
        'formulas': ['y = Σaₙxⁿ, y′ = Σnaₙxⁿ⁻¹, y″ = Σn(n − 1)aₙxⁿ⁻²', 'Shift indices to match powers', 'Set each coefficient to zero ⇒ recurrence', 'Radius ≥ distance to nearest singular point'],
        'steps': ['Substitute the series and its derivatives.', 'Shift indices to align powers.', 'Write the recurrence.', 'Use a₀ = y(0), a₁ = y′(0) to build terms.'],
        'worked_example': {
            'problem': 'Find the first three non-zero terms of the series solution of y″ + y = 0 with y(0) = 1, y′(0) = 0.',
            'steps': ['Recurrence: aₙ₊₂ = −aₙ/((n + 2)(n + 1)), a₀ = 1, a₁ = 0.', 'a₂ = −1/2, a₄ = −a₂/12 = 1/24; odd terms are 0.', 'y = 1 − x²/2 + x⁴/24 − …'],
            'answer': '1 − x²/2 + x⁴/24.',
            'check': 'This is the start of the Maclaurin series of cos x, the known solution ✓.'},
        'mistakes': ['Shifting indices incorrectly.', 'Forgetting that a₀ and a₁ are free.', 'Assuming every equation has an elementary closed form.', 'Ignoring the radius of convergence.'],
        'real_world': 'Airy functions, defined by this kind of series, describe light near a rainbow\'s edge and quantum particles in a uniform field.',
        'exam_strategy': 'Write out the first few coefficients explicitly from the recurrence; examiners usually ask for terms up to x⁴ or x⁵.',
        'recap': ['Assume Σaₙxⁿ.', 'Shift and match powers.', 'Recurrence for aₙ.', 'Radius from singular points.']},
    T4: {
        'overview': 'A Fourier series writes a periodic function as a sum of sines and cosines of increasing frequency.',
        'key_terms': ['Periodic function', 'Fourier coefficients', 'Even function', 'Odd function', 'Square wave', 'Gibbs phenomenon', 'Convergence'],
        'explanation': [
            'On (−π, π): f(x) = a₀/2 + Σ(aₙcos nx + bₙsin nx), with aₙ = (1/π)∫f(x)cos nx dx and bₙ = (1/π)∫f(x)sin nx dx over (−π, π). Odd functions have only sine terms, even functions only cosine terms.',
            'For f(x) = x (odd): bₙ = 2(−1)ⁿ⁺¹/n, so x = 2(sin x − sin 2x/2 + sin 3x/3 − …). For f(x) = |x| (even): a₀ = (1/π)∫|x|dx = π, so the constant term is π/2.',
            'The square wave (−1 on (−π, 0), 1 on (0, π)) has bₙ = 4/(nπ) for odd n and 0 for even n. At a jump, the series converges to the midpoint, and partial sums overshoot by about 9% near the jump (the Gibbs phenomenon).'],
        'formulas_label': 'Formulas',
        'formulas': ['a₀ = (1/π)∫₋π^π f dx', 'aₙ = (1/π)∫₋π^π f cos nx dx', 'bₙ = (1/π)∫₋π^π f sin nx dx', 'Odd f ⇒ aₙ = 0; even f ⇒ bₙ = 0', 'At a jump: midpoint value'],
        'steps': ['Check for odd or even symmetry.', 'Compute only the needed coefficients.', 'Use integration by parts for x terms.', 'Write the first few terms.'],
        'worked_example': {
            'problem': 'Find the Fourier series of the square wave f = −1 on (−π, 0), 1 on (0, π).',
            'steps': ['f is odd, so aₙ = 0.', 'bₙ = (2/π)∫₀^π sin nx dx = 2(1 − (−1)ⁿ)/(nπ): 4/(nπ) for odd n, 0 for even n.', 'f = (4/π)(sin x + sin 3x/3 + sin 5x/5 + …).'],
            'answer': '(4/π)(sin x + sin 3x/3 + sin 5x/5 + …).',
            'check': 'At x = π/2: (4/π)(1 − 1/3 + 1/5 − …) = (4/π)(π/4) = 1 ✓.'},
        'mistakes': ['Forgetting the 1/2 on a₀.', 'Computing cosine terms for an odd function.', 'Sign errors with (−1)ⁿ.', 'Expecting convergence to f at a jump.'],
        'real_world': 'MP3 and JPEG compression keep the most important frequency components of sound and images, an idea rooted in Fourier series.',
        'exam_strategy': 'State the symmetry first ("f is odd, so aₙ = 0"); it halves the work and earns a mark.',
        'recap': ['Sines and cosines.', 'Symmetry saves work.', 'Coefficients by integrals.', 'Midpoint at jumps.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The eigenvalues of A = [1 2; 2 1] are:', ['3 and −1', '1 and 2', '3 and 1', '−3 and 1'], 0, 'λ² − 2λ − 3 = 0.', ans=(3, -1)),
    Q(T1, 'An eigenvector of A = [1 2; 2 1] for λ = 3 is:', ['(1, 1)', '(1, −1)', '(2, 1)', '(1, 2)'], 0, 'A(1, 1) = (3, 3).', ans=sp.Matrix([1, 1])),
    Q(T1, 'The general solution of x′ = Ax for that matrix is:', ['c₁e³ᵗ(1, 1) + c₂e^(−t)(1, −1)', 'c₁e³ᵗ(1, −1) + c₂e^(−t)(1, 1)', 'c₁eᵗ(1, 1) + c₂e²ᵗ(1, −1)', 'c₁e³ᵗ + c₂e^(−t)'], 0, 'Pair each eigenvalue with its eigenvector.'),
    Q(T1, 'Writing y″ + 3y′ + 2y = 0 as a system with x₁ = y, x₂ = y′ gives the matrix:', ['[0 1; −2 −3]', '[1 0; −3 −2]', '[0 1; 2 3]', '[−3 −2; 1 0]'], 0, 'x₂′ = −2x₁ − 3x₂.'),
    Q(T1, 'The eigenvalues of A = [0 2; −2 0] are:', ['±2i', '±2', '0 and 2', '2 and −2'], 0, 'λ² + 4 = 0.'),
    Q(T1, 'For a 2 × 2 matrix, the eigenvalues satisfy:', ['λ² − (tr A)λ + det A = 0', 'λ² + (tr A)λ − det A = 0', 'λ = tr A', 'λ² = det A'], 0, 'Characteristic polynomial.'),
    # T2
    Q(T2, 'Eigenvalues 3 and −1 give an equilibrium that is a:', ['saddle', 'stable node', 'centre', 'stable spiral'], 0, 'Opposite signs.'),
    Q(T2, 'Eigenvalues −1 and −3 give a:', ['stable node', 'unstable node', 'saddle', 'centre'], 0, 'Both negative.'),
    Q(T2, 'Eigenvalues −1 ± 2i give a:', ['stable spiral', 'unstable spiral', 'centre', 'saddle'], 0, 'Real part negative.'),
    Q(T2, 'Eigenvalues ±2i give a:', ['centre', 'stable spiral', 'saddle', 'node'], 0, 'Closed orbits.'),
    Q(T2, 'For A = [3 1; 2 −1], det A =', ['−5', '5', '1', '−1'], 0, '3(−1) − 1(2).', ans=-5),
    Q(T2, 'So the origin for that matrix is a:', ['saddle', 'stable node', 'centre', 'stable spiral'], 0, 'det < 0.'),
    # T3
    Q(T3, 'Substituting Σaₙxⁿ into y′ = y gives the recurrence:', ['aₙ₊₁ = aₙ/(n + 1)', 'aₙ₊₁ = (n + 1)aₙ', 'aₙ₊₁ = aₙ', 'aₙ₊₂ = −aₙ'], 0, '(n + 1)aₙ₊₁ = aₙ.'),
    Q(T3, 'For y″ + y = 0, the recurrence is aₙ₊₂ =', ['−aₙ/((n + 2)(n + 1))', 'aₙ/((n + 2)(n + 1))', '−aₙ/(n + 2)', 'aₙ₊₁/(n + 1)'], 0, '(n + 2)(n + 1)aₙ₊₂ + aₙ = 0.'),
    Q(T3, 'With y(0) = 1, y′(0) = 0, the series begins:', ['1 − x²/2 + x⁴/24', '1 + x²/2 + x⁴/24', 'x − x³/6', '1 − x + x²/2'], 0, 'This is cos x.', ans=1 - x ** 2 / 2 + x ** 4 / 24),
    Q(T3, 'In Airy\'s equation y″ − xy = 0, the coefficient a₂ is:', ['0', '1/2', 'a₀/2', 'a₁/6'], 0, 'No x⁰ term on the xy side.', ans=0),
    Q(T3, 'The series solution about 0 of (1 + x²)y″ + y = 0 converges at least for:', ['|x| < 1', '|x| < 2', 'all x', '|x| < 1/2'], 0, 'Singular points ±i at distance 1.'),
    Q(T3, 'In a power series solution of a second-order equation at an ordinary point, the free constants are:', ['a₀ and a₁', 'a₀ only', 'a₂ and a₃', 'none'], 0, 'They are y(0) and y′(0).'),
    # T4
    Q(T4, 'The Fourier series of an odd function contains only:', ['sine terms', 'cosine terms', 'the constant term', 'both sines and cosines'], 0, 'aₙ = 0.'),
    Q(T4, 'For f(x) = x on (−π, π), b₁ =', ['2', '1', '−2', 'π'], 0, '2(−1)ⁿ⁺¹/n at n = 1.', ans=2),
    Q(T4, 'For f(x) = x on (−π, π), b₂ =', ['−1', '1', '0', '−2'], 0, '2(−1)³/2.', ans=-1),
    Q(T4, 'For f(x) = |x| on (−π, π), a₀ =', ['π', 'π/2', '0', '2π'], 0, '(1/π)∫|x|dx.', ans=sp.pi),
    Q(T4, 'For the square wave (−1, then 1), b₃ =', ['4/(3π)', '4/π', '0', '1/3'], 0, '4/(nπ) for odd n.', ans=4 / (3 * sp.pi)),
    Q(T4, 'At a jump discontinuity, a Fourier series converges to:', ['the midpoint of the jump', 'the left value', 'the right value', 'zero'], 0, 'Average of the one-sided limits.'),
]

FLASH = [
    ['Eigenvalue method', 'x′ = Ax has solutions eˡᵗv with Av = λv.'],
    ['Saddle', 'Real eigenvalues of opposite sign; det A < 0; unstable.'],
    ['Stable node', 'Both eigenvalues real and negative.'],
    ['Spiral', 'Complex eigenvalues α ± βi; stable if α < 0.'],
    ['Centre', 'Purely imaginary eigenvalues; closed orbits.'],
    ['Power series method', 'Substitute Σaₙxⁿ, shift indices, solve the recurrence.'],
    ['Fourier coefficients', 'aₙ = (1/π)∫f cos nx dx, bₙ = (1/π)∫f sin nx dx.'],
    ['Gibbs phenomenon', 'Partial sums overshoot near a jump by about 9%.'],
]
