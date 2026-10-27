"""Differential Equations, module 1: First-order equations."""
from verify import Q, x, C, sp
T1, T2, T3, T4 = ('What a differential equation is', 'Separable equations', 'Linear equations and integrating factors', 'Exact equations and substitutions')
y = sp.Function('y')
D = lambda eq, ics=None: sp.dsolve(eq, y(x), ics=ics).rhs
d = lambda f: sp.diff(f, x)
assert sp.simplify(D(sp.Eq(y(x).diff(x), 3 * y(x)), {y(0): 2}) - 2 * sp.exp(3 * x)) == 0
assert sp.simplify(D(sp.Eq(y(x).diff(x), -2 * x * y(x)), {y(0): 1}) - sp.exp(-x ** 2)) == 0
assert sp.simplify(D(sp.Eq(y(x).diff(x), x / y(x)), {y(0): 2}) - sp.sqrt(x ** 2 + 4)) == 0
assert sp.simplify(D(sp.Eq(y(x).diff(x) + 2 * y(x), 4), {y(0): 0}) - (2 - 2 * sp.exp(-2 * x))) == 0
assert sp.simplify(D(sp.Eq(y(x).diff(x) - y(x), sp.exp(x)), {y(0): 3}) - (x + 3) * sp.exp(x)) == 0
assert sp.simplify(d(x ** 3 / 4 + C / x) + (x ** 3 / 4 + C / x) / x - x ** 2) == 0
assert sp.simplify(d(d(sp.sin(x))) + sp.sin(x)) == 0 and sp.simplify(d(sp.exp(2 * x)) - 2 * sp.exp(2 * x)) == 0
X, Y = sp.symbols('X Y')
M, N = 2 * X * Y + 3, X ** 2 + 4 * Y
assert sp.diff(M, Y) == sp.diff(N, X)
F = X ** 2 * Y + 3 * X + 2 * Y ** 2
assert sp.diff(F, X) == M and sp.diff(F, Y) == N
yy = x * sp.log(x) + C * x
assert sp.simplify(d(yy) - (x + yy) / x) == 0
assert sp.simplify(d(sp.log(sp.exp(x) + C)) - sp.exp(x - sp.log(sp.exp(x) + C))) == 0

MODULE = {
    'title': 'First-order equations',
    'topics': [T1, T2, T3, T4],
    'overview': 'A differential equation links an unknown function with its derivatives. This module covers the language of the subject and the main methods for first-order equations: separation of variables, integrating factors for linear equations, exact equations, and substitutions that turn hard equations into easy ones.',
    'key_terms': ['Differential equation', 'Order', 'Linear', 'Solution', 'General solution', 'Initial value problem', 'Separable', 'Integrating factor', 'Exact equation', 'Bernoulli equation', 'Homogeneous substitution'],
    'explanation': [
        'An ordinary differential equation (ODE) involves an unknown function y(x) and its derivatives. Its order is the highest derivative that appears. A solution is a function that makes the equation true; the general solution contains arbitrary constants, and an initial condition such as y(0) = 2 fixes them.',
        'First-order equations y′ = f(x, y) have no single method, so we classify first. If f splits into a function of x times a function of y, separate and integrate. If the equation is linear in y, multiply by an integrating factor. If it comes from a total derivative, it is exact.',
        'When none of these fits, a substitution often converts the equation into one that does: v = y/x for homogeneous equations, and v = y¹⁻ⁿ for Bernoulli equations. Always check a solution by substituting it back.'],
    'quick_facts': [
        'Order = highest derivative.',
        'Separable: dy/dx = g(x)h(y) ⇒ ∫dy/h(y) = ∫g(x)dx.',
        'Linear: y′ + P(x)y = Q(x); integrating factor μ = e^(∫P dx).',
        'Exact: M dx + N dy = 0 with ∂M/∂y = ∂N/∂x.',
        'Check every answer by substituting it back into the equation.'],
}

NOTES = {
    T1: {
        'overview': 'Differential equations describe how things change. Before solving them, learn to read them: order, linearity, and what counts as a solution.',
        'key_terms': ['Ordinary differential equation', 'Order', 'Linear', 'Nonlinear', 'Solution', 'General solution', 'Particular solution', 'Initial value problem'],
        'explanation': [
            'The order is the highest derivative: y″ + 3y′ = x is second order. An equation is linear if y and its derivatives appear only to the first power and are not multiplied together or inside other functions: y″ + xy = sin x is linear, while y′ = y² and y″ + sin y = 0 are nonlinear.',
            'To check a solution, substitute it. For y = e²ˣ in y′ − 2y = 0: y′ = 2e²ˣ, so 2e²ˣ − 2e²ˣ = 0 ✓. For y = sin x in y″ + y = 0: y″ = −sin x, so −sin x + sin x = 0 ✓.',
            'The simplest equations are pure integrations. y′ = 6x gives y = 3x² + C, a family of curves. An initial value problem (IVP) picks one: with y(0) = 5 and y′ = 2x, y = x² + 5. A first-order equation has one arbitrary constant; an nth-order equation has n.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Order: highest derivative', 'Linear: aₙ(x)y⁽ⁿ⁾ + … + a₁(x)y′ + a₀(x)y = g(x)', 'nth order ⇒ n arbitrary constants', 'IVP: equation + initial condition(s)'],
        'steps': ['Identify the order.', 'Decide linear or nonlinear.', 'To verify, differentiate the proposed solution and substitute.', 'Use initial conditions to find the constants.'],
        'worked_example': {
            'problem': 'Solve the IVP y′ = 2x, y(0) = 5, and verify.',
            'steps': ['Integrate: y = x² + C.', 'y(0) = 0 + C = 5, so C = 5.', 'y = x² + 5; check: y′ = 2x ✓ and y(0) = 5 ✓.'],
            'answer': 'y = x² + 5.',
            'check': 'Substituting back satisfies both the equation and the condition ✓.'},
        'mistakes': ['Confusing order with the highest power.', 'Calling y′ = y² linear.', 'Forgetting the constant of integration.', 'Not checking a solution by substitution.'],
        'real_world': 'Weather forecasting models are huge systems of differential equations describing how air pressure, temperature and wind change.',
        'exam_strategy': 'Classify every equation (order, linear, separable, exact) before choosing a method; it saves time and prevents wrong methods.',
        'recap': ['Order and linearity.', 'Verify by substitution.', 'General vs particular.', 'IVPs fix constants.']},
    T2: {
        'overview': 'Separable equations are the easiest to solve: put all the y terms on one side, all the x terms on the other, and integrate.',
        'key_terms': ['Separable equation', 'Separation of variables', 'Implicit solution', 'Explicit solution', 'Equilibrium solution'],
        'explanation': [
            'An equation dy/dx = g(x)h(y) is separable. Write dy/h(y) = g(x) dx and integrate both sides. For y′ = 3y: dy/y = 3 dx, so ln|y| = 3x + c and y = Ce³ˣ. With y(0) = 2, y = 2e³ˣ.',
            'For y′ = −2xy with y(0) = 1: dy/y = −2x dx gives ln|y| = −x² + c, so y = e^(−x²). For y′ = x/y with y(0) = 2: y dy = x dx gives y²/2 = x²/2 + c, so y² = x² + 4 and, since y(0) > 0, y = √(x² + 4).',
            'Dividing by h(y) can lose solutions where h(y) = 0: for y′ = 3y, y = 0 is also a solution (the C = 0 case). Some answers stay implicit, for example when the y-integral cannot be solved for y. For y′ = eˣ⁻ʸ: eʸ dy = eˣ dx, so eʸ = eˣ + C and y = ln(eˣ + C).'],
        'formulas_label': 'Method',
        'formulas': ['dy/dx = g(x)h(y) ⇒ ∫dy/h(y) = ∫g(x)dx', 'y′ = ky ⇒ y = Ceᵏˣ', 'Check h(y) = 0 for lost equilibrium solutions'],
        'steps': ['Check that the right side factors as g(x)h(y).', 'Separate the variables.', 'Integrate both sides (one constant is enough).', 'Use the initial condition; solve for y if possible.'],
        'worked_example': {
            'problem': 'Solve dy/dx = x/y with y(0) = 2.',
            'steps': ['Separate: y dy = x dx.', 'Integrate: y²/2 = x²/2 + c, so y² = x² + K.', 'y(0) = 2 gives K = 4; take the positive root: y = √(x² + 4).'],
            'answer': 'y = √(x² + 4).',
            'check': 'y′ = x/√(x² + 4) = x/y ✓, and y(0) = 2 ✓.'},
        'mistakes': ['Adding a constant on both sides separately (one is enough).', 'Forgetting the absolute value in ln|y|.', 'Choosing the wrong square-root sign.', 'Losing equilibrium solutions.'],
        'real_world': 'Radioactive decay, y′ = −ky, is separable; its solution y = y₀e^(−kt) is how carbon dating estimates the age of fossils.',
        'exam_strategy': 'Write the separated form explicitly before integrating; examiners give a method mark for it.',
        'recap': ['Factor as g(x)h(y).', 'Separate and integrate.', 'Apply the condition.', 'Watch for h(y) = 0.']},
    T3: {
        'overview': 'Linear first-order equations are solved by multiplying by an integrating factor that turns the left side into the derivative of a product.',
        'key_terms': ['Linear first-order equation', 'Standard form', 'Integrating factor', 'Product rule in reverse', 'Transient', 'Steady state'],
        'explanation': [
            'Write the equation in standard form y′ + P(x)y = Q(x). Multiply by μ(x) = e^(∫P dx); then the left side is (μy)′, so μy = ∫μQ dx + C.',
            'For y′ + 2y = 4: μ = e²ˣ, (e²ˣy)′ = 4e²ˣ, e²ˣy = 2e²ˣ + C, so y = 2 + Ce^(−2x). With y(0) = 0, C = −2 and y = 2 − 2e^(−2x): the term −2e^(−2x) dies away (transient) and y approaches the steady state 2.',
            'For y′ + y/x = x² (x > 0): μ = e^(ln x) = x, so (xy)′ = x³ and y = x³/4 + C/x. For y′ − y = eˣ: μ = e^(−x), (e^(−x)y)′ = 1, so y = (x + C)eˣ; with y(0) = 3, y = (x + 3)eˣ.'],
        'formulas_label': 'Formulas',
        'formulas': ['Standard form: y′ + P(x)y = Q(x)', 'μ(x) = e^(∫P(x)dx)', 'y = (1/μ)[∫μQ dx + C]'],
        'steps': ['Divide to get standard form (coefficient of y′ equal to 1).', 'Find μ = e^(∫P dx) (no constant needed).', 'Multiply through; the left side is (μy)′.', 'Integrate and divide by μ; apply conditions.'],
        'worked_example': {
            'problem': 'Solve y′ + 2y = 4 with y(0) = 0.',
            'steps': ['P = 2, so μ = e²ˣ.', '(e²ˣy)′ = 4e²ˣ ⇒ e²ˣy = 2e²ˣ + C ⇒ y = 2 + Ce^(−2x).', 'y(0) = 2 + C = 0 ⇒ C = −2: y = 2 − 2e^(−2x).'],
            'answer': 'y = 2 − 2e^(−2x).',
            'check': 'y′ = 4e^(−2x); y′ + 2y = 4e^(−2x) + 4 − 4e^(−2x) = 4 ✓.'},
        'mistakes': ['Not dividing to make the coefficient of y′ equal to 1 first.', 'Forgetting to multiply Q by μ.', 'Adding the constant after dividing by μ.', 'Sign errors in P.'],
        'real_world': 'An RC electrical circuit obeys a linear first-order equation; the capacitor voltage approaches the supply voltage exactly like y approaches 2 above.',
        'exam_strategy': 'Always state μ explicitly and show (μy)′ = μQ; it is the core method mark.',
        'recap': ['Standard form first.', 'μ = e^(∫P dx).', '(μy)′ = μQ.', 'Transient + steady state.']},
    T4: {
        'overview': 'Some equations are total derivatives of a function F(x, y) (exact equations). Others become separable or linear after a clever substitution.',
        'key_terms': ['Exact equation', 'Potential function', 'Exactness test', 'Homogeneous equation', 'Substitution v = y/x', 'Bernoulli equation'],
        'explanation': [
            'M(x, y)dx + N(x, y)dy = 0 is exact if ∂M/∂y = ∂N/∂x. Then there is F with F_x = M and F_y = N, and the solution is F(x, y) = C. For (2xy + 3)dx + (x² + 4y)dy = 0: M_y = 2x = N_x ✓. Integrate M in x: F = x²y + 3x + g(y); F_y = x² + g′(y) = x² + 4y, so g = 2y². Solution: x²y + 3x + 2y² = C.',
            'A homogeneous equation dy/dx = f(y/x) becomes separable with v = y/x (so y = vx, y′ = v + xv′). For dy/dx = (x + y)/x = 1 + v: v + xv′ = 1 + v, so v′ = 1/x, v = ln|x| + C and y = x ln|x| + Cx.',
            'A Bernoulli equation y′ + P(x)y = Q(x)yⁿ becomes linear with v = y¹⁻ⁿ. For y′ + y = y² (n = 2), v = 1/y gives v′ − v = −1, a linear equation.'],
        'formulas_label': 'Formulas',
        'formulas': ['Exact test: ∂M/∂y = ∂N/∂x', 'Solution: F(x, y) = C with F_x = M, F_y = N', 'Homogeneous: v = y/x, y′ = v + xv′', 'Bernoulli: v = y¹⁻ⁿ'],
        'steps': ['Test exactness first.', 'If exact, integrate M in x, then fix g(y) using N.', 'If y′ = f(y/x), substitute v = y/x.', 'If Bernoulli, substitute v = y¹⁻ⁿ and solve the linear equation.'],
        'worked_example': {
            'problem': 'Solve (2xy + 3)dx + (x² + 4y)dy = 0.',
            'steps': ['M_y = 2x, N_x = 2x: exact.', 'F = ∫(2xy + 3)dx = x²y + 3x + g(y).', 'F_y = x² + g′(y) = x² + 4y ⇒ g = 2y². So x²y + 3x + 2y² = C.'],
            'answer': 'x²y + 3x + 2y² = C.',
            'check': 'F_x = 2xy + 3 = M ✓, F_y = x² + 4y = N ✓.'},
        'mistakes': ['Skipping the exactness test.', 'Integrating N in x by mistake.', 'Forgetting g(y) when integrating M.', 'Using y′ = v′x instead of v + xv′.'],
        'real_world': 'Exact equations appear in thermodynamics, where quantities like internal energy are "state functions" whose small changes form exact differentials.',
        'exam_strategy': 'Write "exact since M_y = N_x = …" as the first line; without it, the method is not justified.',
        'recap': ['Test M_y = N_x.', 'Find the potential F.', 'v = y/x for homogeneous.', 'v = y¹⁻ⁿ for Bernoulli.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The order of y″ + 3y′ = x is:', ['2', '1', '3', '0'], 0, 'Highest derivative is y″.', ans=2),
    Q(T1, 'Which equation is nonlinear?', ['y′ = y²', 'y″ + xy = sin x', 'y′ + 2y = eˣ', 'x²y″ + y = 0'], 0, 'y appears squared.'),
    Q(T1, 'Which function solves y′ − 2y = 0?', ['e²ˣ', 'e^(−2x)', '2x', 'x²'], 0, 'y′ = 2e²ˣ = 2y.'),
    Q(T1, 'The general solution of y′ = 6x is:', ['y = 3x² + C', 'y = 6 + C', 'y = 6x² + C', 'y = x³ + C'], 0, 'Integrate.', ans=3 * x ** 2),
    Q(T1, 'The solution of y′ = 2x with y(0) = 5 is:', ['y = x² + 5', 'y = x² − 5', 'y = 2x + 5', 'y = 5x²'], 0, 'C = 5.', ans=x ** 2 + 5),
    Q(T1, 'How many arbitrary constants does the general solution of a third-order ODE have?', ['3', '1', '2', '0'], 0, 'One per order.', ans=3),
    # T2
    Q(T2, 'Solve y′ = 3y with y(0) = 2:', ['y = 2e^(3x)', 'y = 3e^(2x)', 'y = 2e^(−3x)', 'y = e^(3x) + 1'], 0, 'y = Ce³ˣ, C = 2.', ans=2 * sp.exp(3 * x)),
    Q(T2, 'Solve y′ = −2xy with y(0) = 1:', ['y = e^(−x²)', 'y = e^(x²)', 'y = e^(−2x)', 'y = 1 − x²'], 0, 'ln y = −x².', ans=sp.exp(-x ** 2)),
    Q(T2, 'Solve y′ = x/y with y(0) = 2 (y > 0):', ['y = √(x² + 4)', 'y = x + 2', 'y = √(x² + 2)', 'y = 2eˣ'], 0, 'y² = x² + 4.', ans=sp.sqrt(x ** 2 + 4)),
    Q(T2, 'The general solution of y′ = eˣ⁻ʸ is:', ['y = ln(eˣ + C)', 'y = eˣ + C', 'y = x + C', 'y = ln(x) + C'], 0, 'eʸ dy = eˣ dx.', ans=sp.log(sp.exp(x) + C)),
    Q(T2, 'Which equation is separable?', ['y′ = x²y', 'y′ = x + y', 'y′ = sin(xy)', 'y′ = x² + y²'], 0, 'x²y = g(x)h(y).'),
    Q(T2, 'When separating y′ = 3y by dividing by y, the solution that can be lost is:', ['y = 0', 'y = 3', 'y = e³ˣ', 'y = x'], 0, 'The equilibrium solution.'),
    # T3
    Q(T3, 'The integrating factor for y′ + 2y = 4 is:', ['e^(2x)', 'e^(−2x)', '2x', 'e^(4x)'], 0, 'e^(∫2 dx).', ans=sp.exp(2 * x)),
    Q(T3, 'Solve y′ + 2y = 4 with y(0) = 0:', ['y = 2 − 2e^(−2x)', 'y = 2 + 2e^(−2x)', 'y = 4 − 4e^(−2x)', 'y = 2e^(−2x)'], 0, 'y = 2 + Ce^(−2x), C = −2.', ans=2 - 2 * sp.exp(-2 * x)),
    Q(T3, 'For x > 0, the general solution of y′ + y/x = x² is:', ['y = x³/4 + C/x', 'y = x³/3 + C', 'y = x²/4 + Cx', 'y = x⁴/4 + C/x'], 0, 'μ = x, (xy)′ = x³.', ans=x ** 3 / 4 + C / x),
    Q(T3, 'Solve y′ − y = eˣ with y(0) = 3:', ['y = (x + 3)eˣ', 'y = 3eˣ', 'y = (3x + 1)eˣ', 'y = eˣ + 2'], 0, 'μ = e^(−x), (e^(−x)y)′ = 1.', ans=(x + 3) * sp.exp(x)),
    Q(T3, 'The integrating factor for y′ + 3x²y = sin x is:', ['e^(x³)', 'e^(3x²)', 'e^(6x)', 'x³'], 0, '∫3x² dx = x³.', ans=sp.exp(x ** 3)),
    Q(T3, 'As x → ∞, y = 2 − 2e^(−2x) tends to:', ['2', '0', '−2', '∞'], 0, 'The transient dies away.', ans=2),
    # T4
    Q(T4, '(2xy + 3)dx + (x² + 4y)dy = 0 is exact because:', ['∂M/∂y = ∂N/∂x = 2x', 'M = N', '∂M/∂x = ∂N/∂y', 'it is linear'], 0, 'Exactness test.'),
    Q(T4, 'Its solution is:', ['x²y + 3x + 2y² = C', 'x²y + 2y² = C', '2xy + 3 = C', 'x² + 4y = C'], 0, 'F_x = M, F_y = N.'),
    Q(T4, 'Is y dx + 2x dy = 0 exact?', ['No: ∂M/∂y = 1 but ∂N/∂x = 2', 'Yes', 'Yes, because it is separable', 'Only for x > 0'], 0, 'Test fails.'),
    Q(T4, 'The substitution for dy/dx = f(y/x) is:', ['v = y/x', 'v = xy', 'v = y²', 'v = x + y'], 0, 'Homogeneous equation.'),
    Q(T4, 'The general solution of dy/dx = (x + y)/x (x > 0) is:', ['y = x ln x + Cx', 'y = x + C', 'y = ln x + C', 'y = Cx'], 0, 'v′ = 1/x.', ans=x * sp.log(x) + C * x),
    Q(T4, 'For the Bernoulli equation y′ + y = y², the substitution is:', ['v = 1/y', 'v = y²', 'v = y/x', 'v = ln y'], 0, 'v = y¹⁻ⁿ with n = 2.'),
]

FLASH = [
    ['Order', 'Highest derivative in the equation.'],
    ['Linear ODE', 'y and its derivatives appear only to the first power, not multiplied together.'],
    ['Separable', 'dy/dx = g(x)h(y); separate and integrate.'],
    ['Integrating factor', 'μ = e^(∫P dx) for y′ + Py = Q.'],
    ['Exact equation', 'M dx + N dy = 0 with M_y = N_x; solution F = C.'],
    ['Homogeneous substitution', 'v = y/x for dy/dx = f(y/x).'],
    ['Bernoulli equation', 'y′ + Py = Qyⁿ; v = y¹⁻ⁿ makes it linear.'],
    ['Initial value problem', 'ODE plus conditions that fix the constants.'],
]
