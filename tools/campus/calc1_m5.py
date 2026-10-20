"""Calculus I, module 5: Integration."""
from verify import Q, x, sp

I = lambda f: sp.integrate(f, x)
DI = lambda f, a, b: sp.integrate(f, (x, a, b))
T1, T2, T3, T4, T5 = ('Antiderivatives and indefinite integrals', 'Riemann sums and the definite integral', 'The Fundamental Theorem of Calculus', 'Integration by substitution', 'Area between curves')

MODULE = {
    'title': 'Integration',
    'topics': [T1, T2, T3, T4, T5],
    'overview': 'Integration runs differentiation in reverse and, surprisingly, also measures area. The Fundamental Theorem of Calculus joins the two ideas and turns area problems into antiderivative problems.',
    'key_terms': ['Antiderivative', 'Indefinite integral', 'Constant of integration', 'Riemann sum', 'Definite integral', 'Fundamental Theorem of Calculus', 'Substitution', 'Area between curves'],
    'explanation': [
        'An antiderivative of f is any function F with F′ = f. Because constants differentiate to 0, antiderivatives come in families F(x) + C, written ∫f(x) dx.',
        'The definite integral ∫ₐᵇ f(x) dx is defined as the limit of Riemann sums: chop [a, b] into thin strips, add up height × width, and let the strips get infinitely thin. For a positive function it is the area under the curve.',
        'The Fundamental Theorem says these two ideas are the same: to compute ∫ₐᵇ f(x) dx, find any antiderivative F and calculate F(b) − F(a). Substitution, the chain rule in reverse, extends the antiderivatives you can find.'],
    'quick_facts': [
        '∫xⁿ dx = xⁿ⁺¹/(n + 1) + C for n ≠ −1.',
        '∫(1/x) dx = ln|x| + C.',
        '∫ₐᵇ f(x) dx = F(b) − F(a).',
        'Area below the x-axis counts as negative in a definite integral.',
        'd/dx ∫ₐˣ f(t) dt = f(x).'],
}

NOTES = {
    T1: {
        'overview': 'Finding an antiderivative means asking "what did I differentiate to get this?". Each derivative rule you know becomes an integration rule when you read it backwards.',
        'key_terms': ['Antiderivative', 'Indefinite integral ∫f(x) dx', 'Constant of integration C', 'Integrand', 'Initial condition'],
        'explanation': [
            'If F′(x) = f(x), then F is an antiderivative of f. So is F + 5 and F − 100. The indefinite integral ∫f(x) dx = F(x) + C names the whole family, and the + C is part of the answer.',
            'The power rule reverses to ∫xⁿ dx = xⁿ⁺¹/(n + 1) + C: raise the power by one and divide by the new power. It fails only for n = −1, where ∫(1/x) dx = ln|x| + C instead. Integrals respect sums and constant multiples, so you integrate term by term.',
            'An initial condition such as F(0) = 3 picks out one member of the family. Integrate first, then substitute the condition to find C. This is how you recover position from velocity, or total cost from marginal cost.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['∫xⁿ dx = xⁿ⁺¹/(n + 1) + C (n ≠ −1)', '∫(1/x) dx = ln|x| + C', '∫eˣ dx = eˣ + C', '∫cos x dx = sin x + C, ∫sin x dx = −cos x + C', '∫sec²x dx = tan x + C'],
        'steps': ['Rewrite roots and fractions as powers of x.', 'Split into separate terms.', 'Integrate each term: raise the power by one and divide by the new power.', 'Add + C.', 'If an initial condition is given, substitute it to find C.'],
        'worked_example': {
            'problem': 'Find f(x) if f′(x) = 6x² − 4x + 1 and f(1) = 5.',
            'steps': ['Integrate term by term: f(x) = 2x³ − 2x² + x + C.', 'Use f(1) = 5: 2 − 2 + 1 + C = 5.', 'So C = 4.', 'f(x) = 2x³ − 2x² + x + 4.'],
            'answer': 'f(x) = 2x³ − 2x² + x + 4.',
            'check': 'f′(x) = 6x² − 4x + 1 ✓ and f(1) = 2 − 2 + 1 + 4 = 5 ✓.'},
        'mistakes': ['Leaving out + C on an indefinite integral.', 'Multiplying by the new power instead of dividing by it.', 'Using the power rule on 1/x and dividing by zero.', 'Writing ∫sin x dx = cos x: the sign is wrong.'],
        'real_world': 'If a tank fills at a rate of r(t) = 3t² litres per minute, integrating gives the volume in the tank. The initial condition is how much water was in it when you started the clock.',
        'exam_strategy': 'Differentiate your answer in your head to check it. It takes five seconds and catches nearly every sign and coefficient error.',
        'recap': ['∫xⁿ dx = xⁿ⁺¹/(n + 1) + C.', '∫1/x dx = ln|x| + C.', 'Always include + C.', 'Initial conditions fix C.']},
    T2: {
        'overview': 'The definite integral measures accumulated quantity, such as area, distance or total change. It is built from Riemann sums: many thin rectangles whose total area approaches the exact value.',
        'key_terms': ['Partition', 'Riemann sum', 'Left and right endpoint sums', 'Midpoint sum', 'Definite integral ∫ₐᵇ f(x) dx', 'Signed area'],
        'explanation': [
            'Divide [a, b] into n equal strips of width Δx = (b − a)/n. In each strip pick a sample point and build a rectangle with that height. The Riemann sum Σ f(xᵢ)Δx adds the rectangle areas. Using left endpoints, right endpoints or midpoints gives different estimates.',
            'As n → ∞ the strips become infinitely thin and the sum approaches a limit, the definite integral ∫ₐᵇ f(x) dx. For a continuous function the choice of sample point does not affect the limit.',
            'The definite integral measures signed area: regions above the x-axis count positive and regions below count negative. So ∫ from 0 to 2π of sin x dx = 0, even though the curve encloses a positive amount of area. Useful properties: ∫ₐᵃ f = 0, ∫ᵇₐ f = −∫ₐᵇ f, and ∫ₐᵇ f + ∫ᵇᶜ f = ∫ₐᶜ f.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Δx = (b − a)/n', 'Right sum Rₙ = Σᵢ₌₁ⁿ f(a + iΔx)·Δx', '∫ₐᵇ f(x) dx = lim n→∞ Σ f(xᵢ*)Δx', '∫ₐᵇ c dx = c(b − a)', '∫ₐᵇ f + ∫ᵇᶜ f = ∫ₐᶜ f'],
        'steps': ['Compute Δx = (b − a)/n.', 'List the sample points (left, right or midpoint).', 'Evaluate f at each sample point.', 'Multiply each value by Δx and add.', 'For the exact value, take the limit or use the Fundamental Theorem.'],
        'worked_example': {
            'problem': 'Estimate ∫ from 0 to 2 of x² dx with a right-endpoint sum using n = 4 strips.',
            'steps': ['Δx = (2 − 0)/4 = 0.5.', 'Right endpoints: 0.5, 1, 1.5, 2.', 'Heights: 0.25, 1, 2.25, 4, which add to 7.5.', 'R₄ = 7.5 × 0.5 = 3.75.'],
            'answer': 'R₄ = 3.75. (The exact value is 8/3 ≈ 2.67; right sums overestimate an increasing function.)',
            'check': 'The left sum is (0 + 0.25 + 1 + 2.25) × 0.5 = 1.75. The exact value lies between 1.75 and 3.75. ✓'},
        'mistakes': ['Using the wrong number of sample points, for example five right endpoints for four strips.', 'Forgetting to multiply by Δx.', 'Treating a definite integral as total area when part of the curve is below the axis.', 'Thinking a right sum is always an overestimate. That is true only for increasing functions.'],
        'real_world': 'A matatu\'s speed is recorded every 10 seconds. Adding speed × 10 s for each reading is a Riemann sum, an estimate of the distance travelled, the area under the speed–time graph.',
        'exam_strategy': 'Lay out a table with columns x, f(x) and f(x)·Δx. It keeps the arithmetic tidy and makes it easy to spot a missing strip.',
        'recap': ['Riemann sum: Σ height × width.', 'Integral: the limit as the strips get thin.', 'Area below the axis counts negative.', 'Right sums overestimate increasing functions.']},
    T3: {
        'overview': 'The Fundamental Theorem of Calculus (FTC) connects derivatives and integrals. It turns the limit of a Riemann sum into a two-line calculation and tells you how to differentiate an integral.',
        'key_terms': ['FTC part 1', 'FTC part 2', 'Accumulation function', 'Evaluation notation [F(x)]ₐᵇ', 'Net change theorem'],
        'explanation': [
            'Part 1: if f is continuous and g(x) = ∫ₐˣ f(t) dt, then g′(x) = f(x). The function that accumulates area under f has f as its rate of change. With the chain rule, d/dx ∫ₐ^(u(x)) f(t) dt = f(u(x))·u′(x).',
            'Part 2: if F is any antiderivative of f, then ∫ₐᵇ f(x) dx = F(b) − F(a). The constant C cancels, so you can leave it out. Write [F(x)]ₐᵇ, substitute the top limit, substitute the bottom limit, and subtract.',
            'The net change theorem reads Part 2 physically: the integral of a rate of change is the total change. Integrating velocity over [a, b] gives displacement; integrating marginal cost gives the change in total cost.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['d/dx ∫ₐˣ f(t) dt = f(x)', 'd/dx ∫ₐ^(u(x)) f(t) dt = f(u(x))·u′(x)', '∫ₐᵇ f(x) dx = F(b) − F(a)', '∫ₐᵇ F′(x) dx = F(b) − F(a) (net change)'],
        'steps': ['Find an antiderivative F of the integrand.', 'Write [F(x)] with the limits.', 'Compute F(b).', 'Compute F(a).', 'Subtract F(b) − F(a), taking care with negative signs.'],
        'worked_example': {
            'problem': 'Evaluate ∫ from 1 to 3 of (3x² − 2x) dx, and find d/dx ∫ from 0 to x² of cos t dt.',
            'steps': ['Antiderivative: F(x) = x³ − x².', 'F(3) = 27 − 9 = 18 and F(1) = 1 − 1 = 0.', 'So the integral is 18 − 0 = 18.', 'For the second part, FTC 1 with the chain rule: cos(x²) · 2x.'],
            'answer': '∫ from 1 to 3 of (3x² − 2x) dx = 18, and the derivative is 2x cos(x²).',
            'check': 'A midpoint sum with 100 strips gives 17.9998. ✓'},
        'mistakes': ['Computing F(a) − F(b) instead of F(b) − F(a).', 'Dropping brackets so that a minus sign applies to only part of F(a).', 'Forgetting the chain rule factor u′(x) when the upper limit is a function of x.', 'Substituting the limits into f instead of into F.'],
        'real_world': 'If water flows into a reservoir at r(t) cubic metres per hour, ∫ from 0 to 24 of r(t) dt is the total volume added in a day, whatever the flow pattern.',
        'exam_strategy': 'Always write the antiderivative in square brackets with the limits before substituting. Examiners give a mark for the correct antiderivative even if the arithmetic goes wrong.',
        'recap': ['FTC 1: differentiating an accumulation function gives back f.', 'FTC 2: ∫ₐᵇ f = F(b) − F(a).', 'No + C needed for definite integrals.', 'The integral of a rate is the net change.']},
    T4: {
        'overview': 'Substitution, also called u-substitution, is the chain rule in reverse. It handles integrals where one part of the integrand is the derivative of another part.',
        'key_terms': ['u-substitution', 'Inner function', 'du = g′(x) dx', 'Changing the limits', 'Back-substitution'],
        'explanation': [
            'The chain rule says d/dx F(g(x)) = F′(g(x))·g′(x). Reading it backwards, ∫f(g(x))g′(x) dx = F(g(x)) + C. To use it, spot an inner function g(x) whose derivative also appears (up to a constant) as a factor.',
            'Set u = g(x) and du = g′(x) dx. Replace everything in the integral with u and du. If you cannot remove every x, the substitution was not the right one. Integrate in u, then substitute back u = g(x).',
            'For a definite integral, either substitute back before using the original limits, or change the limits: when x = a, u = g(a), and when x = b, u = g(b). Changing the limits avoids back-substitution entirely.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['∫f(g(x))g′(x) dx = ∫f(u) du with u = g(x)', 'du = g′(x) dx', '∫ₐᵇ f(g(x))g′(x) dx = ∫ from g(a) to g(b) of f(u) du', '∫g′(x)/g(x) dx = ln|g(x)| + C'],
        'steps': ['Choose u, usually the inside of a bracket, root, exponent or denominator.', 'Find du = u′ dx and solve for dx or for the factor present.', 'Rewrite the whole integral in u.', 'Integrate with respect to u.', 'Substitute back (or use changed limits) and add + C for indefinite integrals.'],
        'worked_example': {
            'problem': 'Evaluate ∫ 2x(x² + 1)⁴ dx and ∫ from 0 to 1 of x e^(x²) dx.',
            'steps': ['First: u = x² + 1, du = 2x dx. The integral becomes ∫u⁴ du = u⁵/5 + C = (x² + 1)⁵/5 + C.', 'Second: u = x², du = 2x dx, so x dx = du/2.', 'Change the limits: x = 0 gives u = 0, x = 1 gives u = 1.', '∫ from 0 to 1 of (1/2)eᵘ du = (1/2)[eᵘ] from 0 to 1 = (e − 1)/2.'],
            'answer': '(x² + 1)⁵/5 + C and (e − 1)/2 ≈ 0.859.',
            'check': 'Differentiate (x² + 1)⁵/5: (5(x² + 1)⁴ · 2x)/5 = 2x(x² + 1)⁴ ✓.'},
        'mistakes': ['Leaving some x terms in the integral after substituting.', 'Forgetting to replace dx with du/u′.', 'Using the original x-limits with the u-integral.', 'Choosing u as the outer function rather than the inner one.'],
        'real_world': 'Drug concentration models often contain terms like t·e^(−t²). Substitution is how pharmacologists integrate them to find the total exposure to a medicine over time.',
        'exam_strategy': 'If a question says "use the substitution u = …", show the line du = … dx explicitly. That line is usually worth a mark on its own.',
        'recap': ['Substitution reverses the chain rule.', 'u = inner function; du = u′ dx.', 'Everything must be in u.', 'Change the limits for definite integrals.']},
    T5: {
        'overview': 'Integrals measure the area between two curves as well as the area under one. Subtract the lower curve from the upper curve and integrate between their intersection points.',
        'key_terms': ['Upper curve', 'Lower curve', 'Points of intersection', 'Area between curves', 'Splitting the interval'],
        'explanation': [
            'If f(x) ≥ g(x) on [a, b], the area between the curves is ∫ₐᵇ [f(x) − g(x)] dx. Each thin strip has height (top − bottom) and width dx, which is why the subtraction order matters.',
            'Usually the limits a and b are where the curves meet. Set f(x) = g(x) and solve. Then check which curve is on top by testing a point between the intersections.',
            'If the curves cross inside the interval, split it at each crossing so that each piece has a clear top and bottom, and add the pieces. For area under a single curve that dips below the x-axis, integrate |f(x)|, again by splitting at the zeros.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Area = ∫ₐᵇ [top − bottom] dx', 'Limits: solve f(x) = g(x)', 'Total area under f = ∫ₐᵇ |f(x)| dx'],
        'steps': ['Sketch the curves.', 'Find the intersection points by solving f(x) = g(x).', 'Test a point to see which curve is on top.', 'Integrate (top − bottom) between the intersection points.', 'Split the interval wherever the curves cross, and add.'],
        'worked_example': {
            'problem': 'Find the area enclosed by y = x and y = x².',
            'steps': ['Intersections: x = x² gives x(x − 1) = 0, so x = 0 and x = 1.', 'At x = 0.5: x = 0.5 and x² = 0.25, so y = x is on top.', 'Area = ∫ from 0 to 1 of (x − x²) dx = [x²/2 − x³/3] from 0 to 1.', '= 1/2 − 1/3 = 1/6.'],
            'answer': 'The enclosed area is 1/6 square units.',
            'check': 'The region sits inside the triangle under y = x, of area 1/2, and 1/6 < 1/2. ✓'},
        'mistakes': ['Subtracting in the wrong order, giving a negative area.', 'Guessing the limits instead of solving for the intersections.', 'Not splitting the interval when the curves cross.', 'Reporting a negative number as an area.'],
        'real_world': 'In economics, consumer surplus is the area between the demand curve and the price line: the total amount buyers would have paid above what they actually paid, in {{CUR}}.',
        'exam_strategy': 'A quick sketch, even a rough one, earns marks and prevents the top/bottom mix-up. State which curve is on top before integrating.',
        'recap': ['Area = ∫ (top − bottom) dx.', 'Limits are the intersection points.', 'Test a point to find the top curve.', 'Split where curves cross.']},
}

QUESTIONS = [
    # T1
    Q(T1, '∫(6x² − 4x + 1) dx =', ['2x³ − 2x² + x + C', '12x − 4 + C', '6x³ − 4x² + x + C', '2x³ − 4x² + x + C'], 0, 'Raise each power by one and divide: 6x³/3 − 4x²/2 + x + C.', ans=I(6*x**2 - 4*x + 1)),
    Q(T1, '∫ x^(1/2) dx =', ['(2/3)x^(3/2) + C', '(3/2)x^(3/2) + C', '(1/2)x^(−1/2) + C', 'x^(3/2) + C'], 0, 'n = 1/2, so xⁿ⁺¹/(n + 1) = x^(3/2)/(3/2) = (2/3)x^(3/2).', ans=I(sp.sqrt(x))),
    Q(T1, '∫ (1/x³) dx =', ['−1/(2x²) + C', '1/(4x⁴) + C', '−3/x⁴ + C', 'ln|x³| + C'], 0, 'Write x⁻³; integrate to x⁻²/(−2) = −1/(2x²).', ans=I(x**-3)),
    Q(T1, '∫ (3/x) dx =', ['3 ln|x| + C', '−3/x² + C', '3x⁰ + C', '(ln|x|)/3 + C'], 0, '∫(1/x) dx = ln|x| + C, and the constant 3 stays as a multiplier: 3 ln|x| + C. The power rule cannot be used, because it would divide by zero.'),
    Q(T1, '∫ (cos x + eˣ) dx =', ['sin x + eˣ + C', '−sin x + eˣ + C', 'sin x + xeˣ + C', '−cos x + eˣ + C'], 0, '∫cos x dx = sin x and ∫eˣ dx = eˣ.', ans=I(sp.cos(x) + sp.exp(x))),
    Q(T1, 'If f′(x) = 6x² − 4x + 1 and f(1) = 5, what is f(0)?', ['0', '4', '5', '1'], 1, 'f(x) = 2x³ − 2x² + x + C and f(1) = 1 + C = 5, so C = 4 and f(0) = 4.', ans=4),
    Q(T1, '∫ sin x dx =', ['cos x + C', '−cos x + C', 'sin x + C', '−sin x + C'], 1, 'd/dx(−cos x) = sin x, so ∫sin x dx = −cos x + C.', ans=I(sp.sin(x))),
    # T2
    Q(T2, 'Estimate ∫ from 0 to 2 of x² dx with a right-endpoint sum, n = 4.', ['3.75', '1.75', '2.75', '2.67'], 0, 'Δx = 0.5; heights at 0.5, 1, 1.5, 2 are 0.25, 1, 2.25, 4. Sum 7.5 × 0.5 = 3.75.', ans=sum(((sp.Rational(i, 2))**2 for i in range(1, 5))) * sp.Rational(1, 2)),
    Q(T2, 'The same integral with a left-endpoint sum, n = 4, gives:', ['1.75', '3.75', '2.5', '2'], 0, 'Left endpoints 0, 0.5, 1, 1.5 give heights 0, 0.25, 1, 2.25. Sum 3.5 × 0.5 = 1.75.', ans=sum(((sp.Rational(i, 2))**2 for i in range(0, 4))) * sp.Rational(1, 2)),
    Q(T2, 'What is ∫ from 0 to 2π of sin x dx?', ['0', '2', '4', '2π'], 0, 'The area above the axis on [0, π] cancels the equal area below the axis on [π, 2π].', ans=DI(sp.sin(x), 0, 2*sp.pi)),
    Q(T2, 'If ∫ from 0 to 3 of f(x) dx = 7 and ∫ from 3 to 5 of f(x) dx = 2, then ∫ from 0 to 5 of f(x) dx =', ['5', '9', '14', '−5'], 1, 'Adjacent intervals add: 7 + 2 = 9.', ans=9),
    Q(T2, '∫ from 2 to 2 of (x³ + 1) dx =', ['0', '9', '18', '1'], 0, 'An integral over an interval of zero width is 0.', ans=0),
    Q(T2, 'For an increasing function, a right-endpoint Riemann sum:', ['underestimates the integral', 'overestimates the integral', 'is always exact', 'can be either'], 1, 'Each rectangle uses the highest point of its strip, so the rectangles stick out above the curve.'),
    # T3
    Q(T3, 'Evaluate ∫ from 1 to 3 of (3x² − 2x) dx.', ['18', '20', '26', '16'], 0, '[x³ − x²] from 1 to 3 = (27 − 9) − (1 − 1) = 18.', ans=DI(3*x**2 - 2*x, 1, 3)),
    Q(T3, 'Evaluate ∫ from 0 to π of sin x dx.', ['0', '1', '2', 'π'], 2, '[−cos x] from 0 to π = (−(−1)) − (−1) = 2.', ans=DI(sp.sin(x), 0, sp.pi)),
    Q(T3, 'Evaluate ∫ from 1 to e of (1/x) dx.', ['1', 'e', '0', 'e − 1'], 0, '[ln x] from 1 to e = 1 − 0 = 1.', ans=DI(1/x, 1, sp.E)),
    Q(T3, 'd/dx ∫ from 0 to x of √(1 + t³) dt =', ['√(1 + x³)', '√(1 + x³) − 1', '3x²/(2√(1 + x³))', '0'], 0, 'FTC part 1: the derivative of the accumulation function is the integrand evaluated at x.'),
    Q(T3, 'd/dx ∫ from 0 to x² of cos t dt =', ['cos(x²)', '2x cos(x²)', 'sin(x²)', '2x sin(x²)'], 1, 'FTC part 1 with the chain rule: cos(x²) · 2x.', ans=sp.diff(sp.integrate(sp.cos(sp.Symbol('s')), (sp.Symbol('s'), 0, x**2)), x)),
    Q(T3, 'A car\'s velocity is v(t) = 2t + 3 m/s. How far does it travel from t = 0 to t = 4 s?', ['11 m', '28 m', '16 m', '19 m'], 1, 'Distance = ∫ from 0 to 4 of (2t + 3) dt = [t² + 3t] from 0 to 4 = 16 + 12 = 28 m.', ans=DI(2*x + 3, 0, 4)),
    # T4
    Q(T4, '∫ 2x(x² + 1)⁴ dx =', ['(x² + 1)⁵/5 + C', '(x² + 1)⁵ + C', '2(x² + 1)⁵/5 + C', 'x²(x² + 1)⁵/5 + C'], 0, 'u = x² + 1, du = 2x dx: ∫u⁴ du = u⁵/5 + C.', ans=(x**2 + 1)**5/5),
    Q(T4, 'Evaluate ∫ from 0 to 1 of x e^(x²) dx.', ['(e − 1)/2', 'e − 1', 'e/2', '(e + 1)/2'], 0, 'u = x², x dx = du/2, limits 0 to 1: (1/2)(e − 1).', ans=DI(x*sp.exp(x**2), 0, 1)),
    Q(T4, '∫ cos(3x) dx =', ['sin(3x) + C', '(1/3) sin(3x) + C', '3 sin(3x) + C', '−(1/3) sin(3x) + C'], 1, 'u = 3x, dx = du/3: (1/3) sin(3x) + C.', ans=I(sp.cos(3*x))),
    Q(T4, '∫ 2x/(x² + 5) dx =', ['ln(x² + 5) + C', '2 ln(x² + 5) + C', '1/(x² + 5) + C', 'x² ln(x² + 5) + C'], 0, 'The top is the derivative of the bottom, so the integral is ln|x² + 5| + C, and x² + 5 > 0.', ans=I(2*x/(x**2 + 5))),
    Q(T4, '∫ (2x + 3)⁶ dx =', ['(2x + 3)⁷/14 + C', '(2x + 3)⁷/7 + C', '2(2x + 3)⁷/7 + C', '6(2x + 3)⁵ + C'], 0, 'u = 2x + 3, dx = du/2: (1/2)·u⁷/7 = (2x + 3)⁷/14 + C.', ans=(2*x + 3)**7/14),
    Q(T4, 'For ∫ from 1 to 2 of 2x√(x² − 1) dx with u = x² − 1, the new limits are:', ['1 to 2', '0 to 3', '0 to 1', '1 to 4'], 1, 'x = 1 gives u = 0 and x = 2 gives u = 3.'),
    # T5
    Q(T5, 'Find the area enclosed by y = x and y = x².', ['1/6', '1/3', '1/2', '1/12'], 0, '∫ from 0 to 1 of (x − x²) dx = 1/2 − 1/3 = 1/6.', ans=DI(x - x**2, 0, 1)),
    Q(T5, 'Find the area between y = 4 − x² and the x-axis.', ['32/3', '16/3', '8', '64/3'], 0, 'Zeros at ±2. ∫ from −2 to 2 of (4 − x²) dx = [4x − x³/3] from −2 to 2 = 16/3 − (−16/3) = 32/3.', ans=DI(4 - x**2, -2, 2)),
    Q(T5, 'Where do y = x² and y = 2x meet?', ['x = 0 and x = 2', 'x = 0 and x = 1', 'x = 1 and x = 2', 'x = −2 and x = 2'], 0, 'x² = 2x gives x(x − 2) = 0.'),
    Q(T5, 'Find the area enclosed by y = x² and y = 2x.', ['4/3', '8/3', '2', '4'], 0, 'On [0, 2], 2x is on top: ∫(2x − x²) dx = [x² − x³/3] from 0 to 2 = 4 − 8/3 = 4/3.', ans=DI(2*x - x**2, 0, 2)),
    Q(T5, 'What is the total area between y = x³ and the x-axis for −1 ≤ x ≤ 1?', ['0', '1/4', '1/2', '1'], 2, 'The definite integral is 0 by symmetry, but area counts both parts as positive: 2 × ∫ from 0 to 1 of x³ dx = 2 × 1/4 = 1/2.', ans=DI(sp.Abs(x**3), -1, 1)),
    Q(T5, 'To find the area between two curves, you integrate:', ['bottom − top', 'top − bottom', 'top + bottom', 'top × bottom'], 1, 'Each strip has height (top curve − bottom curve), which is positive.'),
]

FLASH = [
    ['∫xⁿ dx', 'xⁿ⁺¹/(n + 1) + C, n ≠ −1.'], ['∫(1/x) dx', 'ln|x| + C'], ['∫eˣ dx', 'eˣ + C'],
    ['∫sin x dx', '−cos x + C'], ['∫cos x dx', 'sin x + C'],
    ['Riemann sum', 'Σ f(xᵢ)Δx with Δx = (b − a)/n.'],
    ['FTC part 1', 'd/dx ∫ₐˣ f(t) dt = f(x).'], ['FTC part 2', '∫ₐᵇ f(x) dx = F(b) − F(a).'],
    ['u-substitution', 'u = inner function, du = u′ dx; change the limits for definite integrals.'],
    ['Area between curves', '∫ₐᵇ (top − bottom) dx between the intersection points.'],
]
