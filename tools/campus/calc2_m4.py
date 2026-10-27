"""Calculus II, module 4: Power series and Taylor series."""
from verify import Q, x, n, sp
T1, T2, T3, T4 = ('Power series and radius of convergence', 'Taylor and Maclaurin series', 'Taylor polynomials and the error bound', 'Differentiating and integrating power series')
ser = lambda f, k: sp.series(f, x, 0, k).removeO()

assert sp.expand(ser(sp.exp(x), 3) - (1 + x + x ** 2 / 2)) == 0
assert ser(sp.exp(2 * x), 4).coeff(x, 3) == sp.Rational(4, 3)
assert ser(sp.cos(x), 5) == 1 - x ** 2 / 2 + x ** 4 / 24
assert ser(sp.log(1 + x), 4) == x - x ** 2 / 2 + x ** 3 / 3
assert ser(sp.atan(x), 6) == x - x ** 3 / 3 + x ** 5 / 5
assert ser(1 / (1 - x) ** 2, 4) == 1 + 2 * x + 3 * x ** 2 + 4 * x ** 3
assert ser(sp.exp(-x ** 2), 6) == 1 - x ** 2 + x ** 4 / 2
assert round(float(ser(sp.sin(x), 4).subs(x, sp.Rational(1, 10))), 7) == 0.0998333
assert float(sp.E ** sp.Rational(1, 2) * sp.Rational(1, 8) / 6) < 0.035 and 2 * sp.Rational(1, 8) / 6 == sp.Rational(1, 24)

MODULE = {
    'title': 'Power series and Taylor series',
    'topics': [T1, T2, T3, T4],
    'overview': 'A power series is an "infinite polynomial". Inside its interval of convergence it behaves like a polynomial: you can differentiate and integrate it term by term. Taylor series write familiar functions such as eˣ, sin x and ln(1 + x) this way, and their partial sums (Taylor polynomials) are how calculators actually compute.',
    'key_terms': ['Power series', 'Radius of convergence', 'Interval of convergence', 'Taylor series', 'Maclaurin series', 'Taylor polynomial', 'Remainder', 'Lagrange error bound'],
    'explanation': [
        'A power series Σcₙ(x − a)ⁿ converges for x within a distance R of the centre a, and diverges outside it. The ratio test finds R; the two endpoints must be checked separately because the ratio test gives L = 1 there.',
        'If f has derivatives of every order at a, its Taylor series is Σ f⁽ⁿ⁾(a)(x − a)ⁿ/n!. With a = 0 it is called a Maclaurin series. Five Maclaurin series are worth memorising: 1/(1 − x), eˣ, sin x, cos x and ln(1 + x). Many others follow from them by substitution, differentiation or integration.',
        'Truncating a Taylor series after the xⁿ term gives the Taylor polynomial Tₙ(x). The Lagrange error bound tells you how close Tₙ is to f, which is the basis of every numerical approximation built on series.'],
    'quick_facts': [
        '1/(1 − x) = 1 + x + x² + …, |x| < 1.',
        'eˣ = Σxⁿ/n!, all x.',
        'sin x = x − x³/3! + x⁵/5! − …; cos x = 1 − x²/2! + x⁴/4! − …',
        'ln(1 + x) = x − x²/2 + x³/3 − …, −1 < x ≤ 1.',
        '|Rₙ(x)| ≤ M|x − a|ⁿ⁺¹/(n + 1)!, where M bounds |f⁽ⁿ⁺¹⁾|.'],
}

NOTES = {
    T1: {
        'overview': 'A power series in x converges on an interval centred at a. The radius of convergence R measures how far from the centre it still converges.',
        'key_terms': ['Power series', 'Centre', 'Radius of convergence', 'Interval of convergence', 'Endpoint check'],
        'explanation': [
            'Apply the ratio test to |cₙ₊₁(x − a)ⁿ⁺¹ / cₙ(x − a)ⁿ|. The limit has the form |x − a| × K, and the series converges when this is less than 1, so R = 1/K. If K = 0 the series converges for every x (R = ∞); if K = ∞ it converges only at x = a (R = 0).',
            'At the endpoints a ± R the ratio test gives exactly 1 and decides nothing. Substitute each endpoint and test the resulting number series with the tests from module 3. For example Σxⁿ/n has R = 1: at x = −1 it is the alternating harmonic series (converges) and at x = 1 the harmonic series (diverges), so the interval is [−1, 1).',
            'Three examples worth knowing: Σxⁿ/3ⁿ has R = 3 (it is geometric with r = x/3); Σxⁿ/n! has R = ∞ (it is eˣ); Σn! xⁿ has R = 0.'],
        'formulas_label': 'Formulas',
        'formulas': ['Σcₙ(x − a)ⁿ, centre a', 'Ratio test: lim|cₙ₊₁/cₙ| × |x − a| < 1', 'R = 1 / lim|cₙ₊₁/cₙ|', 'Check the endpoints separately'],
        'steps': ['Write the ratio |aₙ₊₁/aₙ| including the x terms.', 'Take the limit as n → ∞.', 'Solve "limit < 1" for |x − a| to get R.', 'Test each endpoint as a number series.', 'State the interval with the right brackets.'],
        'worked_example': {
            'problem': 'Find the interval of convergence of Σₙ₌₁^∞ xⁿ/n.',
            'steps': ['|aₙ₊₁/aₙ| = |x|ⁿ⁺¹/(n + 1) × n/|x|ⁿ = |x| × n/(n + 1) → |x|.', 'Converges for |x| < 1, so R = 1.', 'x = 1: Σ1/n diverges. x = −1: Σ(−1)ⁿ/n converges by the alternating series test.'],
            'answer': 'The interval of convergence is [−1, 1).',
            'check': 'This series is −ln(1 − x), which is defined for x < 1 and blows up at x = 1, consistent with the interval.'},
        'mistakes': ['Forgetting to check the endpoints.', 'Leaving |x| out of the ratio.', 'Giving R as the whole interval width instead of the half-width.', 'Thinking the series must behave the same way at both endpoints.'],
        'real_world': 'Engineers expand transfer functions as power series to analyse stability; the radius of convergence tells them for which frequencies the approximation is valid.',
        'exam_strategy': 'Present the endpoint checks as two separate labelled lines ("x = 1: …", "x = −1: …"), each with the test you used.',
        'recap': ['Ratio test gives R.', 'Endpoints need their own tests.', 'R = ∞ for eˣ-type series, R = 0 for n!xⁿ.', 'Write the interval with correct brackets.']},
    T2: {
        'overview': 'The Taylor series of a function rebuilds it from its derivatives at one point. Around x = 0 it is called the Maclaurin series.',
        'key_terms': ['Taylor series', 'Maclaurin series', 'Derivatives at a point', 'Standard series', 'Substitution'],
        'explanation': [
            'If f(x) = Σcₙ(x − a)ⁿ, differentiating n times and setting x = a gives cₙ = f⁽ⁿ⁾(a)/n!. So f(x) = f(a) + f′(a)(x − a) + f″(a)(x − a)²/2! + … This is the Taylor series of f about a.',
            'The standard Maclaurin series are: eˣ = 1 + x + x²/2! + x³/3! + …; sin x = x − x³/3! + x⁵/5! − … (odd powers); cos x = 1 − x²/2! + x⁴/4! − … (even powers); 1/(1 − x) = 1 + x + x² + …; ln(1 + x) = x − x²/2 + x³/3 − …',
            'New series come from old ones by substitution. Replacing x by −x² in eˣ gives e^(−x²) = 1 − x² + x⁴/2! − …, which is how the area under the normal curve is computed. Replacing x by 2x in eˣ gives e²ˣ, whose x³ coefficient is 2³/3! = 4/3.'],
        'formulas_label': 'Standard series',
        'formulas': ['f(x) = Σ f⁽ⁿ⁾(a)(x − a)ⁿ / n!', 'eˣ = 1 + x + x²/2! + x³/3! + …', 'sin x = x − x³/3! + x⁵/5! − …', 'cos x = 1 − x²/2! + x⁴/4! − …', 'ln(1 + x) = x − x²/2 + x³/3 − …'],
        'steps': ['Check whether a standard series can be adapted by substitution.', 'Otherwise find f(a), f′(a), f″(a), … and look for a pattern.', 'Write cₙ = f⁽ⁿ⁾(a)/n!.', 'State the interval where the series is valid.'],
        'worked_example': {
            'problem': 'Find the first three non-zero terms of the Maclaurin series of e^(−x²).',
            'steps': ['Start from eᵘ = 1 + u + u²/2! + …', 'Substitute u = −x²: 1 + (−x²) + (−x²)²/2 + …', 'Simplify: 1 − x² + x⁴/2 − …'],
            'answer': 'e^(−x²) = 1 − x² + x⁴/2 − …',
            'check': 'At x = 0.1: 1 − 0.01 + 0.00005 = 0.99005, and e^(−0.01) ≈ 0.99005 ✓.'},
        'mistakes': ['Forgetting the n! in the denominator.', 'Mixing the sin and cos series (sin has the odd powers).', 'Substituting −x² but squaring the sign wrongly.', 'Using the ln(1 + x) series outside −1 < x ≤ 1.'],
        'real_world': 'Physicists replace sin θ by θ for small angles, which comes straight from the sine series. It turns the pendulum equation into one that can be solved exactly and gives the familiar period 2π√(L/g).',
        'exam_strategy': 'If a question says "hence", it wants substitution into a series you have just found, not a fresh set of derivatives. Using the shortcut saves a lot of time.',
        'recap': ['cₙ = f⁽ⁿ⁾(a)/n!.', 'Learn the five standard series.', 'Build new series by substitution.', 'Always note the interval of validity.']},
    T3: {
        'overview': 'A Taylor polynomial is a finite piece of a Taylor series. It approximates the function near the centre, and the Lagrange error bound says how good the approximation is.',
        'key_terms': ['Taylor polynomial', 'Degree', 'Remainder', 'Lagrange error bound', 'Linear and quadratic approximation'],
        'explanation': [
            'Tₙ(x) = Σₖ₌₀ⁿ f⁽ᵏ⁾(a)(x − a)ᵏ/k! matches f and its first n derivatives at a. T₁ is the tangent line (linear approximation); T₂ also matches the curvature.',
            'The remainder Rₙ(x) = f(x) − Tₙ(x) satisfies |Rₙ(x)| ≤ M|x − a|ⁿ⁺¹/(n + 1)!, where M is the largest value of |f⁽ⁿ⁺¹⁾| between a and x. The bound shrinks quickly when x is close to a and n is large.',
            'For alternating series such as sin x at small x, the simpler alternating error bound also works: the error is at most the size of the first omitted term. sin(0.1) ≈ 0.1 − 0.1³/6 = 0.0998333, with error below 0.1⁵/120 ≈ 8 × 10⁻⁸.'],
        'formulas_label': 'Formulas',
        'formulas': ['Tₙ(x) = Σₖ₌₀ⁿ f⁽ᵏ⁾(a)(x − a)ᵏ / k!', 'Rₙ(x) = f(x) − Tₙ(x)', '|Rₙ(x)| ≤ M|x − a|ⁿ⁺¹ / (n + 1)!', 'Linear approximation: f(x) ≈ f(a) + f′(a)(x − a)'],
        'steps': ['Find the derivatives at a up to order n.', 'Build Tₙ and evaluate it at x.', 'Find M, a bound for |f⁽ⁿ⁺¹⁾| between a and x.', 'Compute the error bound.'],
        'worked_example': {
            'problem': 'Use T₂ for eˣ about 0 to estimate e^0.5, and bound the error.',
            'steps': ['T₂(x) = 1 + x + x²/2, so T₂(0.5) = 1 + 0.5 + 0.125 = 1.625.', 'f‴(x) = eˣ ≤ e^0.5 < 2 on [0, 0.5], so take M = 2.', '|R₂| ≤ 2 × 0.5³/3! = 2 × 0.125/6 = 1/24 ≈ 0.042.'],
            'answer': 'e^0.5 ≈ 1.625, with error at most about 0.042.',
            'check': 'The true value is e^0.5 ≈ 1.6487, so the actual error is about 0.024, inside the bound ✓.'},
        'mistakes': ['Using (x − a)ⁿ instead of (x − a)ⁿ⁺¹ in the error bound.', 'Taking M from the n-th derivative instead of the (n + 1)-th.', 'Using a Taylor polynomial far from its centre.', 'Forgetting the factorial in the error bound.'],
        'real_world': 'GPS receivers and phone sensors linearise complex equations around the current estimate (a first-order Taylor polynomial) many times a second, which is how fast navigation is possible.',
        'exam_strategy': 'State M clearly with a reason ("eˣ is increasing, so on [0, 0.5] its maximum is e^0.5 < 2"). Unjustified bounds lose marks.',
        'recap': ['Tₙ matches f and n derivatives at a.', '|Rₙ| ≤ M|x − a|ⁿ⁺¹/(n + 1)!.', 'Alternating series: error ≤ next term.', 'Accuracy is best near the centre.']},
    T4: {
        'overview': 'Inside its interval of convergence, a power series can be differentiated and integrated term by term. This turns a few known series into many new ones.',
        'key_terms': ['Term-by-term differentiation', 'Term-by-term integration', 'Constant of integration', 'Arctangent series', 'Non-elementary integral'],
        'explanation': [
            'If f(x) = Σcₙxⁿ with radius R, then f′(x) = Σncₙxⁿ⁻¹ and ∫f(x) dx = C + Σcₙxⁿ⁺¹/(n + 1), both with the same radius R (endpoints may change).',
            'Differentiating 1/(1 − x) = 1 + x + x² + … gives 1/(1 − x)² = 1 + 2x + 3x² + 4x³ + … Integrating 1/(1 + x²) = 1 − x² + x⁴ − … gives arctan x = x − x³/3 + x⁵/5 − …, and at x = 1 this gives π/4 = 1 − 1/3 + 1/5 − …',
            'Series integrate functions that have no elementary antiderivative. ∫e^(−x²) dx has no closed form, but integrating 1 − x² + x⁴/2 − … term by term gives x − x³/3 + x⁵/10 − …, which can be evaluated to any accuracy.'],
        'formulas_label': 'Formulas',
        'formulas': ['d/dx Σcₙxⁿ = Σncₙxⁿ⁻¹', '∫Σcₙxⁿ dx = C + Σcₙxⁿ⁺¹/(n + 1)', '1/(1 − x)² = Σ(n + 1)xⁿ', 'arctan x = x − x³/3 + x⁵/5 − …, |x| ≤ 1'],
        'steps': ['Start from a known series.', 'Differentiate or integrate each term.', 'Find the constant (set x = 0) when integrating.', 'Keep the radius; recheck the endpoints.'],
        'worked_example': {
            'problem': 'Find the Maclaurin series of arctan x from the series for 1/(1 + x²).',
            'steps': ['1/(1 + x²) = 1 − x² + x⁴ − x⁶ + … for |x| < 1 (geometric with r = −x²).', 'Integrate term by term: arctan x = C + x − x³/3 + x⁵/5 − …', 'arctan 0 = 0, so C = 0.'],
            'answer': 'arctan x = x − x³/3 + x⁵/5 − x⁷/7 + …',
            'check': 'Differentiating gives back 1 − x² + x⁴ − … ✓.'},
        'mistakes': ['Forgetting the constant of integration.', 'Differentiating the constant term into something non-zero.', 'Assuming the endpoints behave the same after integrating.', 'Using the series outside its radius of convergence.'],
        'real_world': 'Series like the arctangent series are how π has been computed to trillions of digits, using faster-converging variants such as Machin\'s formula.',
        'exam_strategy': 'When asked for "the first three non-zero terms", write exactly three terms plus "…". Extra terms waste time and can introduce errors.',
        'recap': ['Differentiate and integrate term by term.', 'Same radius; check endpoints again.', 'Remember the constant C.', 'Series give integrals with no closed form.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'What is the radius of convergence of Σ xⁿ/3ⁿ?', ['3', '1/3', '1', '∞'], 0, 'It is geometric with r = x/3, so it needs |x| < 3.', ans=3),
    Q(T1, 'What is the interval of convergence of Σₙ₌₁^∞ xⁿ/n?', ['[−1, 1)', '(−1, 1)', '[−1, 1]', '(−1, 1]'], 0, 'R = 1; it converges at x = −1 (alternating harmonic) and diverges at x = 1 (harmonic).'),
    Q(T1, 'What is the radius of convergence of Σ xⁿ/n!?', ['∞', '1', '0', 'e'], 0, 'The ratio |x|/(n + 1) → 0 < 1 for every x.'),
    Q(T1, 'What is the radius of convergence of Σ n! xⁿ?', ['0', '1', '∞', '1/e'], 0, 'The ratio (n + 1)|x| → ∞ for every x ≠ 0.', ans=0),
    Q(T1, 'Σ (x − 2)ⁿ/2ⁿ converges for:', ['0 < x < 4', '−2 < x < 2', '1 < x < 3', 'all x'], 0, 'Geometric with |x − 2|/2 < 1, so |x − 2| < 2.'),
    Q(T1, 'Why must endpoints be checked separately?', ['The ratio test gives L = 1 there', 'Power series always diverge at endpoints', 'The radius changes at endpoints', 'Endpoints are outside the interval'], 0, 'At |x − a| = R the ratio test is inconclusive.'),
    # T2
    Q(T2, 'The Maclaurin series of eˣ up to x² is:', ['1 + x + x²/2', '1 + x + x²', 'x + x²/2', '1 − x + x²/2'], 0, 'Every derivative of eˣ at 0 is 1, so cₙ = 1/n!.', ans=1 + x + x ** 2 / 2),
    Q(T2, 'The coefficient of x³ in the Maclaurin series of e²ˣ is:', ['4/3', '8', '2/3', '1/6'], 0, '2³/3! = 8/6 = 4/3.', ans=sp.Rational(4, 3)),
    Q(T2, 'The Maclaurin series of cos x up to x⁴ is:', ['1 − x²/2 + x⁴/24', 'x − x³/6', '1 + x²/2 + x⁴/24', '1 − x² + x⁴'], 0, 'Even powers with alternating signs and factorials.', ans=1 - x ** 2 / 2 + x ** 4 / 24),
    Q(T2, 'The first three non-zero terms of e^(−x²) are:', ['1 − x² + x⁴/2', '1 − x + x²/2', '1 + x² + x⁴/2', '1 − x² + x⁴'], 0, 'Substitute u = −x² into 1 + u + u²/2.', ans=1 - x ** 2 + x ** 4 / 2),
    Q(T2, 'ln(1 + x) up to x³ is:', ['x − x²/2 + x³/3', 'x + x²/2 + x³/3', '1 + x − x²/2', 'x − x²/2 + x³/6'], 0, 'Alternating signs with denominators n (not n!).', ans=x - x ** 2 / 2 + x ** 3 / 3),
    Q(T2, 'In a Taylor series about a, the coefficient of (x − a)ⁿ is:', ['f⁽ⁿ⁾(a)/n!', 'f⁽ⁿ⁾(a)', 'f(a)/n!', 'n! f⁽ⁿ⁾(a)'], 0, 'Differentiate n times and set x = a.'),
    # T3
    Q(T3, 'Using T₂ for eˣ about 0, e^0.5 ≈', ['1.625', '1.5', '1.6487', '1.75'], 0, '1 + 0.5 + 0.125 = 1.625.', ans=sp.Rational(13, 8)),
    Q(T3, 'With sin x ≈ x − x³/6, sin(0.1) ≈ (to 7 d.p.)', ['0.0998333', '0.1166667', '0.0833333', '0.0900000'], 0, '0.1 − 0.001/6 = 0.0998333.', ans=ser(sp.sin(x), 4).subs(x, sp.Rational(1, 10)), num=True),
    Q(T3, 'For T₂ of eˣ on [0, 0.5], using M = 2, the Lagrange error bound is:', ['1/24', '1/48', '1/8', '1/6'], 0, 'M|x|³/3! = 2 × 0.125/6 = 1/24.', ans=sp.Rational(1, 24)),
    Q(T3, 'The linear approximation to √x at x = 4 gives √4.1 ≈', ['2.025', '2.05', '2.1', '2.0025'], 0, 'f(4) = 2 and f′(4) = 1/4, so 2 + 0.1/4 = 2.025.', ans=sp.Rational(2025, 1000)),
    Q(T3, 'In |Rₙ| ≤ M|x − a|ⁿ⁺¹/(n + 1)!, M bounds:', ['|f⁽ⁿ⁺¹⁾| between a and x', '|f⁽ⁿ⁾(a)|', '|f(x)|', '|Tₙ(x)|'], 0, 'The next derivative after the last one used.'),
    Q(T3, 'Which approximation of e^0.1 has the smallest error?', ['T₃(0.1)', 'T₁(0.1)', 'T₂(0.1)', 'T₀(0.1)'], 0, 'Higher degree near the centre gives a smaller error.'),
    # T4
    Q(T4, 'Differentiating 1 + x + x² + x³ + … gives the series for:', ['1/(1 − x)²', 'ln(1 − x)', '1/(1 + x)', 'eˣ'], 0, 'd/dx 1/(1 − x) = 1/(1 − x)².'),
    Q(T4, 'The series for 1/(1 − x)² up to x³ is:', ['1 + 2x + 3x² + 4x³', '1 + x + x² + x³', '2 + 3x + 4x²', '1 − 2x + 3x² − 4x³'], 0, 'Term by term: d/dx xⁿ = nxⁿ⁻¹.', ans=1 + 2 * x + 3 * x ** 2 + 4 * x ** 3),
    Q(T4, 'arctan x up to x⁵ is:', ['x − x³/3 + x⁵/5', 'x − x³/6 + x⁵/120', 'x + x³/3 + x⁵/5', '1 − x² + x⁴'], 0, 'Integrate 1 − x² + x⁴.', ans=x - x ** 3 / 3 + x ** 5 / 5),
    Q(T4, 'Setting x = 1 in the arctangent series gives:', ['π/4 = 1 − 1/3 + 1/5 − …', 'π = 1 + 1/3 + 1/5 + …', 'ln 2 = 1 − 1/2 + 1/3 − …', 'e = 1 + 1 + 1/2 + …'], 0, 'arctan 1 = π/4.'),
    Q(T4, '∫e^(−x²) dx as a series (C = 0), up to x⁵, is:', ['x − x³/3 + x⁵/10', 'x − x³/3 + x⁵/5', '1 − x² + x⁴/2', 'x − x³ + x⁵/2'], 0, 'Integrate 1 − x² + x⁴/2 term by term.', ans=sp.integrate(1 - x ** 2 + x ** 4 / 2, x)),
    Q(T4, 'When a power series is integrated term by term, the radius of convergence:', ['stays the same', 'doubles', 'halves', 'becomes infinite'], 0, 'Only the behaviour at the endpoints can change.'),
]

FLASH = [
    ['Radius of convergence', 'From the ratio test: R = 1/lim|cₙ₊₁/cₙ|; check endpoints separately.'],
    ['Taylor coefficient', 'cₙ = f⁽ⁿ⁾(a)/n!.'],
    ['eˣ', '1 + x + x²/2! + x³/3! + … for all x.'],
    ['sin x', 'x − x³/3! + x⁵/5! − …'],
    ['cos x', '1 − x²/2! + x⁴/4! − …'],
    ['ln(1 + x)', 'x − x²/2 + x³/3 − …, −1 < x ≤ 1.'],
    ['Lagrange error bound', '|Rₙ| ≤ M|x − a|ⁿ⁺¹/(n + 1)!.'],
    ['arctan x', 'x − x³/3 + x⁵/5 − …, from integrating 1/(1 + x²).'],
]
