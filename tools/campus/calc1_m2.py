"""Calculus I, module 2: The derivative."""
from verify import Q, x, h, sp

D = lambda f: sp.diff(f, x)
T1, T2, T3, T4 = ('The derivative as a limit', 'Power, constant and sum rules', 'Product and quotient rules', 'The chain rule')

MODULE = {
    'title': 'The derivative',
    'topics': [T1, T2, T3, T4],
    'overview': 'The derivative measures instantaneous rate of change: the slope of a curve at a single point. You will meet it first as a limit, then learn the rules that let you differentiate almost any formula in a line or two.',
    'key_terms': ['Derivative', 'Difference quotient', 'Tangent line', 'Differentiable', 'Power rule', 'Product rule', 'Quotient rule', 'Chain rule'],
    'explanation': [
        'The slope of a secant line through (a, f(a)) and (a + h, f(a + h)) is the average rate of change over that interval. Letting h shrink to 0 turns the secant into the tangent and the average rate into the instantaneous rate. That limit is the derivative f′(a).',
        'Computing every derivative from the limit would be slow, so we prove a few rules once and use them forever: the power rule for xⁿ, linearity for sums and constant multiples, the product and quotient rules for products and fractions, and the chain rule for functions inside functions.',
        'Choosing the right rule is most of the skill. Look at the last operation you would do if you evaluated the expression with a calculator: if it is a multiplication use the product rule, a division the quotient rule, and applying a function to something the chain rule.'],
    'quick_facts': [
        'f′(a) is the slope of the tangent line to y = f(x) at x = a.',
        'd/dx (xⁿ) = nxⁿ⁻¹ for every real n.',
        'The derivative of a constant is 0.',
        '(uv)′ = u′v + uv′, not u′v′.',
        'Chain rule: differentiate the outside, keep the inside, multiply by the derivative of the inside.'],
}

NOTES = {
    T1: {
        'overview': 'The derivative of f at a is the limit of the difference quotient as h → 0. It gives the slope of the tangent line, the instantaneous rate of change, and the velocity when f is position.',
        'key_terms': ['Secant line', 'Tangent line', 'Difference quotient', 'Derivative f′(x)', 'Leibniz notation dy/dx', 'Differentiable', 'Instantaneous rate of change'],
        'explanation': [
            'The difference quotient (f(a + h) − f(a))/h is the slope of the line through two points on the curve, h apart. As h → 0 the two points merge and the slope becomes the slope of the tangent. If this limit exists, f is differentiable at a.',
            'Treating a as a variable gives the derivative function f′(x). Leibniz notation dy/dx reminds you that the derivative is a limit of Δy/Δx. Both notations mean the same thing.',
            'Once you know f′(a), the tangent line at a is y − f(a) = f′(a)(x − a). This line is the best straight-line approximation to f near a, an idea you will use again in linear approximation.',
            'Differentiability is stronger than continuity. Every differentiable function is continuous, but |x| is continuous at 0 and not differentiable there: the slopes from the left (−1) and right (1) disagree, which shows up as a corner.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['f′(x) = lim h→0 (f(x + h) − f(x))/h', 'Average rate of change on [a, b] = (f(b) − f(a))/(b − a)', 'Tangent line at a: y − f(a) = f′(a)(x − a)', 'Normal line at a has slope −1/f′(a)'],
        'steps': ['Write f(x + h) by substituting x + h everywhere x appears.', 'Form f(x + h) − f(x) and simplify until every term has a factor h.', 'Divide by h and cancel.', 'Let h → 0.', 'For a tangent line, evaluate f(a) and f′(a) and use y − f(a) = f′(a)(x − a).'],
        'worked_example': {
            'problem': 'Use the definition to find f′(x) for f(x) = x² + 3x, then find the tangent line at x = 1.',
            'steps': ['f(x + h) = (x + h)² + 3(x + h) = x² + 2xh + h² + 3x + 3h.', 'f(x + h) − f(x) = 2xh + h² + 3h.', 'Divide by h: 2x + h + 3.', 'Let h → 0: f′(x) = 2x + 3.', 'At x = 1: f(1) = 4 and f′(1) = 5, so the tangent is y − 4 = 5(x − 1), that is y = 5x − 1.'],
            'answer': 'f′(x) = 2x + 3; tangent at x = 1 is y = 5x − 1.',
            'check': 'The power rule gives d/dx(x² + 3x) = 2x + 3, the same result. ✓'},
        'mistakes': ['Writing f(x) + h instead of f(x + h).', 'Letting h → 0 before cancelling the h in the denominator, which gives 0/0.', 'Using the average rate of change when the question asks for the instantaneous rate.', 'Assuming a continuous function must be differentiable.'],
        'real_world': 'A delivery rider\'s app records distance every second. The average speed over one second is a difference quotient; the speed shown on the screen is the derivative of distance with respect to time.',
        'exam_strategy': 'If a question says "from first principles" or "using the definition", the rules earn no marks. Show the expansion of f(x + h), the cancellation of h, and the limit, each on its own line.',
        'recap': ['f′(x) is the limit of the difference quotient.', 'It is the slope of the tangent line.', 'Tangent: y − f(a) = f′(a)(x − a).', 'Differentiable ⇒ continuous, not the other way round.']},
    T2: {
        'overview': 'Three rules handle every polynomial and many other functions: the power rule, the constant multiple rule and the sum rule. Together they let you differentiate term by term.',
        'key_terms': ['Power rule', 'Constant rule', 'Constant multiple rule', 'Sum and difference rule', 'Negative and fractional powers', 'Higher derivatives'],
        'explanation': [
            'The power rule says d/dx (xⁿ) = nxⁿ⁻¹: bring the power down in front and reduce it by one. It works for every real power, which is why you should rewrite roots and reciprocals as powers first: √x = x^(1/2) and 1/x² = x⁻².',
            'Constants behave simply. The derivative of a constant on its own is 0, because a horizontal line has slope 0. A constant multiplying a function stays as it is: d/dx (5x³) = 5 · 3x² = 15x².',
            'Derivatives respect addition and subtraction, so you can differentiate a long polynomial one term at a time. Differentiating again gives the second derivative f″(x), which measures how the slope itself is changing; for a position function it is acceleration.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['d/dx (xⁿ) = nxⁿ⁻¹', 'd/dx (c) = 0', 'd/dx (c·f) = c·f′', 'd/dx (f ± g) = f′ ± g′', '√x = x^(1/2), 1/xⁿ = x⁻ⁿ'],
        'steps': ['Rewrite roots and fractions as powers of x.', 'Split the expression into separate terms.', 'Apply the power rule to each term, keeping constant multipliers.', 'Drop constant terms (their derivative is 0).', 'Rewrite negative and fractional powers in the form the question uses.'],
        'worked_example': {
            'problem': 'Differentiate y = 4x³ − 2√x + 5/x.',
            'steps': ['Rewrite: y = 4x³ − 2x^(1/2) + 5x⁻¹.', 'Differentiate 4x³: 12x².', 'Differentiate −2x^(1/2): −2 · (1/2)x^(−1/2) = −x^(−1/2).', 'Differentiate 5x⁻¹: −5x⁻².', 'So dy/dx = 12x² − 1/√x − 5/x².'],
            'answer': 'dy/dx = 12x² − 1/√x − 5/x².',
            'check': 'At x = 1 the slope is 12 − 1 − 5 = 6. A numerical check with h = 0.001 gives about 6.0. ✓'},
        'mistakes': ['Differentiating 1/x² as 1/(2x). Rewrite it as x⁻² first: the answer is −2x⁻³.', 'Reducing a negative power the wrong way: x⁻¹ becomes −x⁻², not −x⁰.', 'Keeping a constant term instead of dropping it.', 'Forgetting to multiply by the coefficient: d/dx (3x⁴) = 12x³, not 4x³.'],
        'real_world': 'If a company\'s revenue in {{CUR}} is R(q) = 50q − 0.1q² for q items, then R′(q) = 50 − 0.2q is the marginal revenue: roughly the extra revenue from selling one more item.',
        'exam_strategy': 'Write the rewritten power form as a separate line before differentiating. It is where most errors happen, and it earns a method mark on its own.',
        'recap': ['Power rule: bring the power down, reduce it by one.', 'Rewrite roots and reciprocals as powers first.', 'Constants on their own vanish; multipliers stay.', 'Differentiate sums term by term.']},
    T3: {
        'overview': 'Products and quotients need their own rules, because the derivative of a product is not the product of the derivatives. These two rules are among the most used tools in the course.',
        'key_terms': ['Product rule', 'Quotient rule', 'u and v notation', 'Simplifying derivatives'],
        'explanation': [
            'For y = uv, the product rule is y′ = u′v + uv′: differentiate the first and keep the second, then keep the first and differentiate the second, and add. A quick test shows why the naive guess fails: x · x = x² has derivative 2x, but (1)(1) = 1.',
            'For y = u/v, the quotient rule is y′ = (u′v − uv′)/v². The minus sign makes the order matter: it always starts with the derivative of the top. A memory aid: "low d-high minus high d-low, over low squared".',
            'Before using the quotient rule, check whether simplifying first is easier. (x³ + x)/x is just x² + 1 for x ≠ 0, and differentiating that takes one line. If the denominator is a constant, treat the fraction as a constant multiple instead.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['(uv)′ = u′v + uv′', '(u/v)′ = (u′v − uv′)/v²', '(uvw)′ = u′vw + uv′w + uvw′'],
        'steps': ['Identify u and v and write them down.', 'Find u′ and v′ separately.', 'Substitute into the rule, keeping brackets.', 'Expand and collect like terms in the numerator.', 'Leave the denominator of a quotient as v² unless asked to expand it.'],
        'worked_example': {
            'problem': 'Differentiate y = (x² − 1)/(x² + 1).',
            'steps': ['u = x² − 1, so u′ = 2x. v = x² + 1, so v′ = 2x.', 'y′ = (2x(x² + 1) − (x² − 1)(2x))/(x² + 1)².', 'Numerator: 2x³ + 2x − 2x³ + 2x = 4x.', 'So y′ = 4x/(x² + 1)².'],
            'answer': 'dy/dx = 4x/(x² + 1)².',
            'check': 'At x = 0 the slope is 0, which fits: y has its minimum value −1 at x = 0. ✓'},
        'mistakes': ['Writing (uv)′ = u′v′.', 'Reversing the order in the quotient rule numerator, which flips the sign of the answer.', 'Forgetting to square the denominator.', 'Dropping brackets when substituting, so that only part of a factor gets multiplied.'],
        'real_world': 'Average cost per item is C(q)/q. The quotient rule tells you whether producing one more item raises or lowers the average cost, which is how firms find their most efficient scale.',
        'exam_strategy': 'Lay out u, u′, v and v′ in a small table before you substitute. Examiners can then award method marks even if a slip appears in the simplification.',
        'recap': ['Product: u′v + uv′.', 'Quotient: (u′v − uv′)/v², derivative of the top first.', 'Simplify first when you can.', 'Show u, u′, v, v′ clearly.']},
    T4: {
        'overview': 'The chain rule differentiates composite functions, a function applied to another function. It is the rule you will use most often, because almost every realistic formula has something inside something else.',
        'key_terms': ['Composite function', 'Inner function', 'Outer function', 'Chain rule', 'Leibniz form dy/dx = dy/du · du/dx'],
        'explanation': [
            'If y = f(g(x)), then y′ = f′(g(x)) · g′(x). In words: differentiate the outer function, leaving the inside alone, then multiply by the derivative of the inside.',
            'In Leibniz notation, set u = g(x) so that y = f(u). Then dy/dx = dy/du · du/dx. The du terms look as if they cancel, which makes the rule easy to remember, though it is a theorem rather than cancellation.',
            'Chains can be long. For sin²(3x) = (sin 3x)², the outermost layer is squaring, then sine, then 3x. Peel one layer at a time from the outside in, multiplying by each inner derivative: 2 sin(3x) · cos(3x) · 3.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['d/dx f(g(x)) = f′(g(x))·g′(x)', 'dy/dx = (dy/du)(du/dx)', 'd/dx [g(x)]ⁿ = n[g(x)]ⁿ⁻¹·g′(x)', 'd/dx √(g(x)) = g′(x)/(2√(g(x)))'],
        'steps': ['Identify the outer function and the inner function.', 'Differentiate the outer function, keeping the inner function unchanged inside it.', 'Differentiate the inner function.', 'Multiply the two results.', 'Repeat for any further layers, then simplify.'],
        'worked_example': {
            'problem': 'Differentiate y = (3x² + 1)⁵ and y = √(x³ + 2).',
            'steps': ['First: outer is u⁵, inner is u = 3x² + 1 with u′ = 6x.', 'dy/dx = 5(3x² + 1)⁴ · 6x = 30x(3x² + 1)⁴.', 'Second: write y = (x³ + 2)^(1/2). Outer derivative: (1/2)(x³ + 2)^(−1/2).', 'Inner derivative: 3x².', 'dy/dx = 3x²/(2√(x³ + 2)).'],
            'answer': 'dy/dx = 30x(3x² + 1)⁴ and dy/dx = 3x²/(2√(x³ + 2)).',
            'check': 'At x = 0 the first slope is 0, which fits: (3x² + 1)⁵ has its minimum at x = 0. ✓'},
        'mistakes': ['Forgetting to multiply by the derivative of the inside, the single most common calculus error.', 'Changing the inside when differentiating the outside, for example writing 5(6x)⁴.', 'Stopping after one layer of a multi-layer chain.', 'Treating sin(x²) as if it were (sin x)².'],
        'real_world': 'If the area of an oil spill depends on its radius, and the radius grows with time, the chain rule gives the rate at which the area grows: dA/dt = dA/dr · dr/dt. Related rates problems are built on this.',
        'exam_strategy': 'Underline or name the inner function before you start. In long questions the chain rule is often combined with the product or quotient rule; decide which rule is outermost and apply that one first.',
        'recap': ['Differentiate outside, keep inside, multiply by inside′.', 'dy/dx = dy/du · du/dx.', 'Work layer by layer from the outside in.', 'sin(x²) and sin²x are different functions.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Using the definition, the derivative of f(x) = x² + 3x is:', ['2x + 3', 'x + 3', '2x', '2x + 3h'], 0, '(f(x + h) − f(x))/h = 2x + h + 3, which tends to 2x + 3 as h → 0.', ans=D(x**2 + 3*x)),
    Q(T1, 'What is the average rate of change of f(x) = x³ on [1, 3]?', ['9', '13', '26', '27'], 1, '(f(3) − f(1))/(3 − 1) = (27 − 1)/2 = 13.', ans=13),
    Q(T1, 'The tangent line to y = x² at x = 3 is:', ['y = 6x − 9', 'y = 6x + 9', 'y = 3x', 'y = 9x − 18'], 0, 'f(3) = 9 and f′(3) = 6, so y − 9 = 6(x − 3), giving y = 6x − 9.', ans=6*x - 9),
    Q(T1, 'lim h→0 ((3 + h)² − 9)/h represents f′(3) for f(x) = x². Its value is:', ['3', '6', '9', '0'], 1, 'Expanding gives (6h + h²)/h = 6 + h → 6.', ans=sp.limit(((3 + h)**2 - 9)/h, h, 0)),
    Q(T1, 'At which point is f(x) = |x| not differentiable?', ['x = 1', 'x = 0', 'x = −1', 'It is differentiable everywhere'], 1, 'At x = 0 the left slope is −1 and the right slope is 1, so the limit of the difference quotient does not exist. The graph has a corner.'),
    Q(T1, 'Using the definition, f′(x) for f(x) = 1/x is:', ['1/x²', '−1/x²', '−1/x', 'ln x'], 1, '(1/(x + h) − 1/x)/h = −h/(x(x + h)h) = −1/(x(x + h)) → −1/x².', ans=D(1/x)),
    Q(T1, 'The normal to y = x² at x = 1 has slope:', ['2', '−2', '1/2', '−1/2'], 3, 'The tangent slope is f′(1) = 2. The normal is perpendicular, so its slope is −1/2.', ans=sp.Rational(-1, 2)),
    # T2
    Q(T2, 'Differentiate y = 4x³ − 2√x + 5/x.', ['12x² − 1/√x − 5/x²', '12x² − 2/√x + 5/x²', '12x² − 1/√x + 5/x²', '4x² − √x − 5/x²'], 0, 'Rewrite as 4x³ − 2x^(1/2) + 5x⁻¹ and use the power rule term by term.', ans=D(4*x**3 - 2*sp.sqrt(x) + 5/x)),
    Q(T2, 'If f(x) = 7x⁵ − 3x² + 9, then f′(x) =', ['35x⁴ − 6x', '35x⁴ − 6x + 9', '7x⁴ − 3x', '35x⁵ − 6x²'], 0, 'Power rule on each term; the constant 9 has derivative 0.', ans=D(7*x**5 - 3*x**2 + 9)),
    Q(T2, 'The derivative of y = 1/x² is:', ['−2/x³', '1/(2x)', '−1/x', '2/x³'], 0, 'Write y = x⁻². Then dy/dx = −2x⁻³ = −2/x³.', ans=D(1/x**2)),
    Q(T2, 'The derivative of y = x^(3/2) is:', ['(3/2)√x', '(2/3)x^(5/2)', '(3/2)x^(1/2)·x', '3√x'], 0, 'Power rule: (3/2)x^(1/2) = (3/2)√x.', ans=D(x**sp.Rational(3, 2))),
    Q(T2, 'For s(t) = t³ − 6t² (metres, seconds), the acceleration at t = 2 is:', ['0 m/s²', '−12 m/s²', '6 m/s²', '12 m/s²'], 0, 'v = s′ = 3t² − 12t and a = s″ = 6t − 12, so a(2) = 0.'),
    Q(T2, 'At what x does y = x² − 8x + 3 have a horizontal tangent?', ['x = 8', 'x = 4', 'x = −4', 'x = 3'], 1, 'dy/dx = 2x − 8 = 0 gives x = 4.', ans=4),
    # T3
    Q(T3, 'Differentiate y = x² sin x.', ['2x cos x', '2x sin x + x² cos x', '2x sin x − x² cos x', 'x² cos x'], 1, 'Product rule: (x²)′ sin x + x²(sin x)′ = 2x sin x + x² cos x.', ans=D(x**2*sp.sin(x))),
    Q(T3, 'Differentiate y = (x² − 1)/(x² + 1).', ['4x/(x² + 1)²', '−4x/(x² + 1)²', '1', '4x/(x² + 1)'], 0, 'Quotient rule: (2x(x² + 1) − (x² − 1)2x)/(x² + 1)² = 4x/(x² + 1)².', ans=D((x**2 - 1)/(x**2 + 1))),
    Q(T3, 'Differentiate y = (2x + 1)(x³ − x).', ['8x³ + 3x² − 4x − 1', '6x²', '8x³ + 3x² − 1', '2(3x² − 1)'], 0, 'u′v + uv′ = 2(x³ − x) + (2x + 1)(3x² − 1) = 8x³ + 3x² − 4x − 1.', ans=D((2*x + 1)*(x**3 - x))),
    Q(T3, 'Differentiate y = x/(x + 1).', ['1/(x + 1)²', '−1/(x + 1)²', '1', 'x/(x + 1)²'], 0, '((x + 1) − x)/(x + 1)² = 1/(x + 1)².', ans=D(x/(x + 1))),
    Q(T3, 'If f(2) = 3, f′(2) = −1, g(2) = 4 and g′(2) = 5, find (fg)′(2).', ['11', '−5', '19', '−4'], 0, '(fg)′(2) = f′(2)g(2) + f(2)g′(2) = (−1)(4) + 3(5) = 11.', ans=11),
    Q(T3, 'Using the same values (f(2) = 3, f′(2) = −1, g(2) = 4, g′(2) = 5), find (f/g)′(2).', ['−19/16', '19/16', '−11/16', '−1/5'], 0, '(f′g − fg′)/g² = ((−1)(4) − 3(5))/16 = −19/16.', ans=sp.Rational(-19, 16)),
    # T4
    Q(T4, 'Differentiate y = (3x² + 1)⁵.', ['5(3x² + 1)⁴', '30x(3x² + 1)⁴', '5(6x)⁴', '6x(3x² + 1)⁵'], 1, 'Outer: 5u⁴; inner derivative 6x. Multiply: 30x(3x² + 1)⁴.', ans=D((3*x**2 + 1)**5)),
    Q(T4, 'Differentiate y = √(x³ + 2).', ['3x²/(2√(x³ + 2))', '1/(2√(x³ + 2))', '3x²√(x³ + 2)', '(3/2)x√(x³ + 2)'], 0, 'Outer: (1/2)u^(−1/2); inner derivative 3x².', ans=D(sp.sqrt(x**3 + 2))),
    Q(T4, 'Differentiate y = sin(x²).', ['cos(x²)', '2x cos(x²)', '2 sin x cos x', '2x cos x'], 1, 'Outer derivative cos(x²), inner derivative 2x.', ans=D(sp.sin(x**2))),
    Q(T4, 'Differentiate y = sin²(3x).', ['6 sin(3x) cos(3x)', '2 sin(3x) cos(3x)', '3 cos²(3x)', '6 cos(3x)'], 0, 'Three layers: 2 sin(3x) · cos(3x) · 3 = 6 sin(3x) cos(3x).', ans=D(sp.sin(3*x)**2)),
    Q(T4, 'Differentiate y = 1/(2x − 5)³.', ['−6/(2x − 5)⁴', '−3/(2x − 5)⁴', '6/(2x − 5)⁴', '−6/(2x − 5)²'], 0, 'Write (2x − 5)⁻³. Derivative: −3(2x − 5)⁻⁴ · 2 = −6/(2x − 5)⁴.', ans=D(1/(2*x - 5)**3)),
    Q(T4, 'If y = u³ and u = 2x + 1, what is dy/dx when x = 1?', ['18', '27', '54', '9'], 2, 'dy/du = 3u² = 3(3)² = 27 at x = 1, and du/dx = 2, so dy/dx = 54.', ans=54),
    Q(T4, 'Differentiate y = cos(5x − 2).', ['−sin(5x − 2)', '−5 sin(5x − 2)', '5 sin(5x − 2)', '−5 cos(5x − 2)'], 1, 'Outer derivative −sin(5x − 2), inner derivative 5.', ans=D(sp.cos(5*x - 2))),
]

FLASH = [
    ['Definition of f′(x)', 'lim h→0 (f(x + h) − f(x))/h.'],
    ['Tangent line at x = a', 'y − f(a) = f′(a)(x − a).'],
    ['Power rule', 'd/dx (xⁿ) = nxⁿ⁻¹, for every real n.'],
    ['d/dx (1/x)', '−1/x²'],
    ['d/dx √x', '1/(2√x)'],
    ['Product rule', '(uv)′ = u′v + uv′.'],
    ['Quotient rule', '(u/v)′ = (u′v − uv′)/v².'],
    ['Chain rule', 'd/dx f(g(x)) = f′(g(x))·g′(x).'],
    ['Differentiable vs continuous', 'Differentiable implies continuous. |x| at 0 is continuous but not differentiable.'],
]
