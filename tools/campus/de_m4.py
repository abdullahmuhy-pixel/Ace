"""Differential Equations, module 4: The Laplace transform."""
from verify import Q, t, sp
T1, T2, T3, T4 = ('Definition and basic transforms', 'Inverse transforms and partial fractions', 'Solving initial value problems', 'Step functions, impulses and convolution')
s = sp.Symbol('s')
tp, sp_ = sp.symbols('tp sp_', positive=True)
Lp = lambda f: sp.laplace_transform(f.subs(t, tp), tp, sp_, noconds=True).subs(sp_, s)
IL = lambda F: sp.simplify(sp.inverse_laplace_transform(F.subs(s, sp_), sp_, tp).subs(sp.Heaviside(tp), 1).subs(tp, t))
eq = lambda a, b: sp.simplify(a - b) == 0
assert eq(Lp(sp.Integer(1) + 0 * t), 1 / s) and eq(Lp(sp.exp(3 * t)), 1 / (s - 3)) and eq(Lp(t ** 2), 2 / s ** 3)
assert eq(Lp(sp.sin(2 * t)), 2 / (s ** 2 + 4)) and eq(Lp(sp.cos(3 * t)), s / (s ** 2 + 9)) and eq(Lp(sp.exp(2 * t) * sp.sin(t)), 1 / ((s - 2) ** 2 + 1))
assert eq(IL(1 / (s - 4)), sp.exp(4 * t)) and eq(IL(1 / (s ** 2 + 9)), sp.sin(3 * t) / 3) and eq(IL(1 / (s * (s + 1))), 1 - sp.exp(-t))
assert eq(IL((s + 1) / ((s + 1) ** 2 + 4)), sp.exp(-t) * sp.cos(2 * t)) and eq(IL(6 / s ** 4), t ** 3) and eq(IL(1 / ((s - 1) * (s - 2))), sp.exp(2 * t) - sp.exp(t))
# IVPs, solved by transforming: Y from the algebra, then invert
assert eq(IL(3 / (s + 2)), 3 * sp.exp(-2 * t))                              # y' + 2y = 0, y(0) = 3
assert eq(IL(1 / (s ** 2 + 1)), sp.sin(t))                                  # y'' + y = 0, y(0) = 0, y'(0) = 1
assert eq(IL(1 / (s * (s - 1))), sp.exp(t) - 1)                             # y' - y = 1, y(0) = 0
assert eq(IL((s - 3) / (s ** 2 - 3 * s + 2)), 2 * sp.exp(t) - sp.exp(2 * t))  # y'' - 3y' + 2y = 0, y(0) = 1, y'(0) = 0
assert eq(IL(2 / (s * (s + 2))), 1 - sp.exp(-2 * t))                        # y' + 2y = 2, y(0) = 0
yy = 2 * sp.exp(t) - sp.exp(2 * t)
assert eq(sp.diff(yy, t, 2) - 3 * sp.diff(yy, t) + 2 * yy, 0)
assert eq(sp.integrate(1, (sp.Symbol('w'), 0, t)), t) and eq(sp.integrate(sp.Symbol('w'), (sp.Symbol('w'), 0, t)), t ** 2 / 2)

MODULE = {
    'title': 'The Laplace transform',
    'topics': [T1, T2, T3, T4],
    'overview': 'The Laplace transform turns a differential equation into an algebra problem. This module covers the transform and its table, inverse transforms with partial fractions, solving initial value problems in one sweep, and handling switches and impulses with step and delta functions.',
    'key_terms': ['Laplace transform', 'Linearity', 'First shifting theorem', 'Transform of a derivative', 'Inverse transform', 'Partial fractions', 'Unit step function', 'Second shifting theorem', 'Dirac delta', 'Convolution', 'Transfer function'],
    'explanation': [
        'The Laplace transform of f(t) is F(s) = ∫₀^∞ e^(−st)f(t)dt. It is linear, and a short table covers most problems: L{1} = 1/s, L{tⁿ} = n!/sⁿ⁺¹, L{eᵃᵗ} = 1/(s − a), L{sin bt} = b/(s² + b²), L{cos bt} = s/(s² + b²).',
        'The key property is L{y′} = sY − y(0) and L{y″} = s²Y − sy(0) − y′(0). Transforming an equation with its initial conditions gives an algebraic equation for Y(s); solve it, split it into partial fractions and invert with the table.',
        'Step functions u(t − a) switch forces on and off, and the Dirac delta δ(t − a) models a sudden impulse. Their transforms, e^(−as)/s and e^(−as), make problems with switches no harder than smooth ones.'],
    'quick_facts': [
        'L{eᵃᵗf(t)} = F(s − a) (first shift).',
        'L{y′} = sY − y(0); L{y″} = s²Y − sy(0) − y′(0).',
        'L{u(t − a)f(t − a)} = e^(−as)F(s) (second shift).',
        'L{δ(t − a)} = e^(−as).',
        'L{f * g} = F(s)G(s).'],
}

NOTES = {
    T1: {
        'overview': 'The Laplace transform maps functions of t to functions of s. Learn the definition, the small table and the shifting rule.',
        'key_terms': ['Laplace transform', 'Improper integral', 'Linearity', 'Table of transforms', 'First shifting theorem', 'Exponential order'],
        'explanation': [
            'F(s) = ∫₀^∞ e^(−st)f(t)dt, defined for s large enough. From the definition: L{1} = 1/s and L{eᵃᵗ} = 1/(s − a) for s > a. For example L{e³ᵗ} = 1/(s − 3).',
            'Table entries: L{tⁿ} = n!/sⁿ⁺¹ (L{t²} = 2/s³), L{sin bt} = b/(s² + b²) (L{sin 2t} = 2/(s² + 4)), L{cos bt} = s/(s² + b²) (L{cos 3t} = s/(s² + 9)). Linearity lets you transform sums term by term.',
            'First shifting theorem: multiplying by eᵃᵗ shifts s to s − a. So L{e²ᵗ sin t} = 1/((s − 2)² + 1). The derivative rule L{y′} = sY − y(0) is what makes the transform useful for ODEs.'],
        'formulas_label': 'Table',
        'formulas': ['L{1} = 1/s', 'L{tⁿ} = n!/sⁿ⁺¹', 'L{eᵃᵗ} = 1/(s − a)', 'L{sin bt} = b/(s² + b²), L{cos bt} = s/(s² + b²)', 'L{eᵃᵗf(t)} = F(s − a)', 'L{y′} = sY − y(0)'],
        'steps': ['Split the function into table entries (linearity).', 'Apply the table.', 'Use the first shift for eᵃᵗ factors.', 'Simplify.'],
        'worked_example': {
            'problem': 'Find L{3 + 2e⁴ᵗ − sin 3t}.',
            'steps': ['L{3} = 3/s.', 'L{2e⁴ᵗ} = 2/(s − 4).', 'L{sin 3t} = 3/(s² + 9), so F = 3/s + 2/(s − 4) − 3/(s² + 9).'],
            'answer': '3/s + 2/(s − 4) − 3/(s² + 9).',
            'check': 'Each term matches a table entry; linearity allows term-by-term transforms ✓.'},
        'mistakes': ['Mixing up the sin and cos numerators.', 'L{tⁿ} = n!/sⁿ instead of sⁿ⁺¹.', 'Shifting the wrong way (s + a instead of s − a).', 'Transforming a product as a product of transforms.'],
        'real_world': 'Control engineers describe systems such as cruise control and autopilots by transfer functions in s, built from Laplace transforms.',
        'exam_strategy': 'Write the table you need at the top of your answer; most marks come from correct table use.',
        'recap': ['Definition as an integral.', 'Small table.', 'Linearity.', 'First shift.']},
    T2: {
        'overview': 'To get back to t, rewrite F(s) as a sum of table entries, usually with partial fractions and completing the square.',
        'key_terms': ['Inverse Laplace transform', 'Partial fractions', 'Cover-up method', 'Completing the square', 'Linear and quadratic factors'],
        'explanation': [
            'Simple inverses read straight from the table: L⁻¹{1/(s − 4)} = e⁴ᵗ, L⁻¹{6/s⁴} = t³, L⁻¹{1/(s² + 9)} = (1/3)sin 3t (adjust the constant to match b).',
            'Partial fractions split rational functions: 1/(s(s + 1)) = 1/s − 1/(s + 1), so the inverse is 1 − e^(−t). Similarly 1/((s − 1)(s − 2)) = 1/(s − 2) − 1/(s − 1), giving e²ᵗ − eᵗ.',
            'For an irreducible quadratic, complete the square and use the first shift: (s + 1)/((s + 1)² + 4) is a cosine shifted by −1, so its inverse is e^(−t)cos 2t.'],
        'formulas_label': 'Techniques',
        'formulas': ['Match constants: L⁻¹{1/(s² + b²)} = (1/b) sin bt', 'Partial fractions for distinct linear factors', 'Complete the square: s² + 2s + 5 = (s + 1)² + 4', 'First shift: F(s − a) ↔ eᵃᵗf(t)'],
        'steps': ['Factor the denominator.', 'Split into partial fractions.', 'Complete the square for quadratics.', 'Invert term by term.'],
        'worked_example': {
            'problem': 'Find L⁻¹{1/((s − 1)(s − 2))}.',
            'steps': ['1/((s − 1)(s − 2)) = A/(s − 1) + B/(s − 2).', 'Cover-up: A = 1/(1 − 2) = −1, B = 1/(2 − 1) = 1.', 'Inverse: −eᵗ + e²ᵗ.'],
            'answer': 'e²ᵗ − eᵗ.',
            'check': 'Transforming back gives 1/(s − 2) − 1/(s − 1) = 1/((s − 1)(s − 2)) ✓.'},
        'mistakes': ['Forgetting the 1/b factor for sines.', 'Not completing the square before inverting.', 'Wrong signs in the cover-up method.', 'Inverting each factor of a product separately.'],
        'real_world': 'The partial-fraction terms correspond to physical modes: each pole of F(s) is a decay rate or vibration frequency of the system.',
        'exam_strategy': 'Check partial fractions by recombining before inverting; it takes seconds and saves the whole answer.',
        'recap': ['Table in reverse.', 'Partial fractions.', 'Complete the square.', 'Adjust constants.']},
    T3: {
        'overview': 'The Laplace method solves an initial value problem in one pass: transform, solve for Y, invert.',
        'key_terms': ['Transform of derivatives', 'Subsidiary equation', 'Solving for Y(s)', 'Initial conditions built in'],
        'explanation': [
            'For y′ + 2y = 0, y(0) = 3: sY − 3 + 2Y = 0, so Y = 3/(s + 2) and y = 3e^(−2t). For y′ − y = 1, y(0) = 0: sY − Y = 1/s, Y = 1/(s(s − 1)), y = eᵗ − 1.',
            'Second order: L{y″} = s²Y − sy(0) − y′(0). For y″ + y = 0, y(0) = 0, y′(0) = 1: (s² + 1)Y = 1, so y = sin t.',
            'For y″ − 3y′ + 2y = 0 with y(0) = 1, y′(0) = 0: s²Y − s − 3(sY − 1) + 2Y = 0, so Y = (s − 3)/(s² − 3s + 2) = 2/(s − 1) − 1/(s − 2), and y = 2eᵗ − e²ᵗ. The initial conditions enter at the start, so no constants need fixing at the end.'],
        'formulas_label': 'Method',
        'formulas': ['L{y′} = sY − y(0)', 'L{y″} = s²Y − sy(0) − y′(0)', 'Solve the algebraic equation for Y', 'y = L⁻¹{Y}'],
        'steps': ['Transform both sides using the derivative rules.', 'Insert the initial conditions.', 'Solve for Y(s).', 'Use partial fractions and invert.'],
        'worked_example': {
            'problem': 'Solve y″ − 3y′ + 2y = 0, y(0) = 1, y′(0) = 0.',
            'steps': ['s²Y − s − 3(sY − 1) + 2Y = 0 ⇒ (s² − 3s + 2)Y = s − 3.', 'Y = (s − 3)/((s − 1)(s − 2)) = 2/(s − 1) − 1/(s − 2).', 'y = 2eᵗ − e²ᵗ.'],
            'answer': 'y = 2eᵗ − e²ᵗ.',
            'check': 'y(0) = 1 ✓, y′(0) = 2 − 2 = 0 ✓, and it satisfies the equation.'},
        'mistakes': ['Dropping the y(0) and y′(0) terms.', 'Sign errors in s²Y − sy(0) − y′(0).', 'Forgetting to transform the right-hand side.', 'Partial fraction slips.'],
        'real_world': 'Circuit simulators solve switching problems in electrical engineering with exactly this transform-solve-invert pipeline.',
        'exam_strategy': 'Write the transformed equation in full with the initial values substituted before simplifying.',
        'recap': ['Transform with ICs.', 'Solve for Y.', 'Partial fractions.', 'Invert.']},
    T4: {
        'overview': 'Step functions switch inputs on and off, the delta function models an instant impulse, and convolution expresses responses to general inputs.',
        'key_terms': ['Unit step function u(t − a)', 'Second shifting theorem', 'Dirac delta δ(t − a)', 'Impulse response', 'Convolution', 'Transfer function'],
        'explanation': [
            'u(t − a) is 0 for t < a and 1 for t ≥ a, with L{u(t − a)} = e^(−as)/s; for example L{u(t − 2)} = e^(−2s)/s. The second shift says L{u(t − a)f(t − a)} = e^(−as)F(s), so L⁻¹{e^(−s)/s²} = (t − 1)u(t − 1): a ramp starting at t = 1.',
            'The Dirac delta δ(t − a) is an infinitely brief unit impulse at t = a, with L{δ(t − a)} = e^(−as). For y′ + y = δ(t − 1), y(0) = 0: (s + 1)Y = e^(−s), so y = e^(−(t − 1))u(t − 1): nothing happens until the kick at t = 1, then the response decays.',
            'The convolution (f * g)(t) = ∫₀ᵗ f(τ)g(t − τ)dτ satisfies L{f * g} = F(s)G(s). For example 1 * 1 = t, matching (1/s)(1/s) = 1/s².'],
        'formulas_label': 'Formulas',
        'formulas': ['L{u(t − a)} = e^(−as)/s', 'L{u(t − a)f(t − a)} = e^(−as)F(s)', 'L{δ(t − a)} = e^(−as)', '(f * g)(t) = ∫₀ᵗ f(τ)g(t − τ)dτ, L{f * g} = FG'],
        'steps': ['Write the input with step or delta functions.', 'Transform using the shifting theorems.', 'Solve for Y.', 'Invert, keeping the e^(−as) factors as shifts.'],
        'worked_example': {
            'problem': 'Solve y′ + y = δ(t − 1), y(0) = 0.',
            'steps': ['Transform: sY + Y = e^(−s).', 'Y = e^(−s)/(s + 1).', 'L⁻¹{1/(s + 1)} = e^(−t), shifted by 1: y = e^(−(t − 1))u(t − 1).'],
            'answer': 'y = e^(−(t − 1))u(t − 1).',
            'check': 'y = 0 before t = 1, jumps to 1 at t = 1, then decays ✓.'},
        'mistakes': ['Forgetting to shift the function as well as multiplying by e^(−as).', 'Writing L{δ} = 1/s.', 'Thinking convolution is ordinary multiplication in t.', 'Dropping the step function in the final answer.'],
        'real_world': 'Testing a structure by striking it with a hammer measures its impulse response; engineers then predict its response to any load by convolution.',
        'exam_strategy': 'When you see e^(−as) in Y(s), invert the rest first, then shift t to t − a and multiply by u(t − a).',
        'recap': ['Steps switch inputs.', 'Delta is an impulse.', 'Second shift theorem.', 'Convolution ↔ product.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'L{e³ᵗ} =', ['1/(s − 3)', '1/(s + 3)', '3/s', 's/(s − 3)'], 0, 'Table.', ans=1 / (s - 3)),
    Q(T1, 'L{t²} =', ['2/s³', '1/s³', '2/s²', '1/s²'], 0, 'n!/sⁿ⁺¹.', ans=2 / s ** 3),
    Q(T1, 'L{sin 2t} =', ['2/(s² + 4)', 's/(s² + 4)', '2/(s² − 4)', '1/(s² + 4)'], 0, 'b/(s² + b²).', ans=2 / (s ** 2 + 4)),
    Q(T1, 'L{cos 3t} =', ['s/(s² + 9)', '3/(s² + 9)', 's/(s² − 9)', '1/(s² + 9)'], 0, 's/(s² + b²).', ans=s / (s ** 2 + 9)),
    Q(T1, 'L{e²ᵗ sin t} =', ['1/((s − 2)² + 1)', '1/((s + 2)² + 1)', '1/(s² + 1)', '2/((s − 2)² + 1)'], 0, 'First shift.', ans=1 / ((s - 2) ** 2 + 1)),
    Q(T1, 'L{y′} equals:', ['sY − y(0)', 'sY + y(0)', 'Y/s', 's²Y − y(0)'], 0, 'Derivative rule.'),
    # T2
    Q(T2, 'L⁻¹{1/(s − 4)} =', ['e^(4t)', 'e^(−4t)', '4t', 'sin 4t'], 0, 'Table.', ans=sp.exp(4 * t)),
    Q(T2, 'L⁻¹{1/(s² + 9)} =', ['sin(3t)/3', 'sin 3t', 'cos 3t', '3sin 3t'], 0, 'Adjust for b = 3.', ans=sp.sin(3 * t) / 3),
    Q(T2, 'L⁻¹{1/(s(s + 1))} =', ['1 − e^(−t)', '1 + e^(−t)', 'e^(−t)', 't e^(−t)'], 0, '1/s − 1/(s + 1).', ans=1 - sp.exp(-t)),
    Q(T2, 'L⁻¹{(s + 1)/((s + 1)² + 4)} =', ['e^(−t)cos(2t)', 'e^(t)cos(2t)', 'e^(−t)sin(2t)', 'cos(2t)'], 0, 'Shifted cosine.', ans=sp.exp(-t) * sp.cos(2 * t)),
    Q(T2, 'L⁻¹{6/s⁴} =', ['t³', '6t³', 't⁴', '6t⁴'], 0, '3! = 6.', ans=t ** 3),
    Q(T2, 'L⁻¹{1/((s − 1)(s − 2))} =', ['e^(2t) − e^(t)', 'e^(t) − e^(2t)', 'e^(t)e^(2t)', 'e^(3t)'], 0, 'Partial fractions.', ans=sp.exp(2 * t) - sp.exp(t)),
    # T3
    Q(T3, 'Solve y′ + 2y = 0, y(0) = 3 by Laplace:', ['3e^(−2t)', '3e^(2t)', '2e^(−3t)', 'e^(−2t)'], 0, 'Y = 3/(s + 2).', ans=3 * sp.exp(-2 * t)),
    Q(T3, 'L{y″} equals:', ['s²Y − sy(0) − y′(0)', 's²Y − y(0) − y′(0)', 's²Y + sy(0) + y′(0)', 'sY − y′(0)'], 0, 'Apply the rule twice.'),
    Q(T3, 'Solve y″ + y = 0, y(0) = 0, y′(0) = 1:', ['sin(t)', 'cos(t)', 'e^(t)', 't'], 0, 'Y = 1/(s² + 1).', ans=sp.sin(t)),
    Q(T3, 'Solve y′ − y = 1, y(0) = 0:', ['e^(t) − 1', 'e^(t)', '1 − e^(−t)', 't'], 0, 'Y = 1/(s(s − 1)).', ans=sp.exp(t) - 1),
    Q(T3, 'Solve y″ − 3y′ + 2y = 0, y(0) = 1, y′(0) = 0:', ['2e^(t) − e^(2t)', 'e^(t)', '2e^(2t) − e^(t)', 'e^(t) − e^(2t)'], 0, 'Y = 2/(s − 1) − 1/(s − 2).', ans=2 * sp.exp(t) - sp.exp(2 * t)),
    Q(T3, 'Solve y′ + 2y = 2, y(0) = 0:', ['1 − e^(−2t)', '1 + e^(−2t)', 'e^(−2t)', '2 − 2e^(−2t)'], 0, 'Y = 2/(s(s + 2)).', ans=1 - sp.exp(-2 * t)),
    # T4
    Q(T4, 'L{u(t − 2)} =', ['e^(−2s)/s', 'e^(2s)/s', '1/(s − 2)', 'e^(−2s)'], 0, 'Step at t = 2.', ans=sp.exp(-2 * s) / s),
    Q(T4, 'L{δ(t − 3)} =', ['e^(−3s)', 'e^(−3s)/s', '1/s', '3'], 0, 'Impulse at t = 3.', ans=sp.exp(-3 * s)),
    Q(T4, 'L⁻¹{e^(−s)/s²} =', ['(t − 1)u(t − 1)', 'tu(t − 1)', '(t − 1)²u(t − 1)', 'e^(−t)t'], 0, 'Shifted ramp.'),
    Q(T4, 'The solution of y′ + y = δ(t − 1), y(0) = 0 is:', ['e^(−(t − 1))u(t − 1)', 'e^(−t)', 'u(t − 1)', 'e^(−t)u(t − 1)'], 0, 'Y = e^(−s)/(s + 1).'),
    Q(T4, 'The convolution 1 * 1 equals:', ['t', '1', 't²/2', '2t'], 0, '∫₀ᵗ 1 dτ.', ans=t),
    Q(T4, 'L{f * g} equals:', ['F(s)G(s)', 'F(s) + G(s)', 'F(s)/G(s)', 'F(G(s))'], 0, 'Convolution theorem.'),
]

FLASH = [
    ['Laplace transform', 'F(s) = ∫₀^∞ e^(−st)f(t)dt.'],
    ['L{eᵃᵗ}', '1/(s − a).'],
    ['L{sin bt}, L{cos bt}', 'b/(s² + b²), s/(s² + b²).'],
    ['First shift', 'L{eᵃᵗf(t)} = F(s − a).'],
    ['Derivative rule', 'L{y′} = sY − y(0); L{y″} = s²Y − sy(0) − y′(0).'],
    ['Second shift', 'L{u(t − a)f(t − a)} = e^(−as)F(s).'],
    ['Dirac delta', 'L{δ(t − a)} = e^(−as).'],
    ['Convolution theorem', 'L{f * g} = F(s)G(s).'],
]
