"""Calculus I, module 4: Applications of the derivative."""
from verify import Q, x, sp

D = lambda f: sp.diff(f, x)
T1, T2, T3, T4 = ('Critical points and extreme values', 'The Mean Value Theorem and the shape of a graph', 'Optimisation', "L'Hôpital's rule and linear approximation")

MODULE = {
    'title': 'Applications of the derivative',
    'topics': [T1, T2, T3, T4],
    'overview': 'Derivatives answer practical questions: where is a quantity largest or smallest, where is a graph rising or bending, and what is the best design under a constraint. This module turns differentiation into a problem-solving tool.',
    'key_terms': ['Critical point', 'Local and absolute extrema', 'Closed interval method', 'Mean Value Theorem', 'Concavity', 'Point of inflection', 'Optimisation', "L'Hôpital's rule", 'Linear approximation'],
    'explanation': [
        'At a smooth peak or trough the tangent is horizontal, so f′ = 0 there. Points where f′ = 0 or f′ does not exist are the critical points, and they are the only interior candidates for maxima and minima.',
        'The sign of f′ tells you whether f is rising or falling, and the sign of f″ tells you which way the graph bends. Together they sketch a graph without plotting dozens of points.',
        'Optimisation problems put this to work: build a formula for the quantity to maximise or minimise, reduce it to one variable using the constraint, differentiate, and test the critical points. The same derivative ideas also give L\'Hôpital\'s rule for tricky limits and linear approximations for quick estimates.'],
    'quick_facts': [
        'Critical points: f′(x) = 0 or f′(x) undefined, with x in the domain.',
        'On a closed interval, the absolute extremes occur at critical points or at the endpoints.',
        'f′ > 0 means increasing; f″ > 0 means concave up.',
        'Second derivative test: f′(c) = 0 and f″(c) < 0 gives a local maximum.',
        "L'Hôpital's rule applies only to 0/0 or ∞/∞."],
}

NOTES = {
    T1: {
        'overview': 'Finding the highest and lowest values of a function is one of the main reasons to learn calculus. Every candidate is either a critical point or an endpoint, so the search becomes a short list.',
        'key_terms': ['Critical number', 'Local maximum', 'Local minimum', 'Absolute maximum', 'Absolute minimum', 'Extreme Value Theorem', 'Closed interval method'],
        'explanation': [
            'A local maximum is a point higher than everything near it; an absolute maximum is the highest point on the whole domain. Fermat\'s theorem says that if f has a local extremum at an interior point c and f′(c) exists, then f′(c) = 0. The converse is false: x³ has f′(0) = 0 but no extremum there.',
            'The Extreme Value Theorem guarantees that a function continuous on a closed interval [a, b] attains an absolute maximum and an absolute minimum. To find them, use the closed interval method: evaluate f at every critical point inside the interval and at both endpoints, then pick the largest and smallest values.',
            'Critical points include places where f′ does not exist, such as the corner of |x| at 0 or the cusp of x^(2/3) at 0. Do not forget them when the derivative has a denominator.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Critical number c: f′(c) = 0 or f′(c) undefined, c in the domain', 'Closed interval method: compare f(a), f(b) and f(c) for each critical c', 'Fermat: local extremum at interior c and f′(c) exists ⇒ f′(c) = 0'],
        'steps': ['Differentiate f.', 'Solve f′(x) = 0 and note where f′ is undefined.', 'Keep only the critical numbers inside the interval.', 'Evaluate f at those points and at both endpoints.', 'The largest value is the absolute maximum; the smallest is the absolute minimum.'],
        'worked_example': {
            'problem': 'Find the absolute maximum and minimum of f(x) = x³ − 3x² + 1 on [−1, 4].',
            'steps': ['f′(x) = 3x² − 6x = 3x(x − 2), so the critical numbers are 0 and 2.', 'f(−1) = −1 − 3 + 1 = −3.', 'f(0) = 1 and f(2) = 8 − 12 + 1 = −3.', 'f(4) = 64 − 48 + 1 = 17.', 'Compare: largest 17, smallest −3.'],
            'answer': 'Absolute maximum 17 at x = 4; absolute minimum −3, reached at both x = −1 and x = 2.',
            'check': 'A quick sketch: the cubic dips to −3 at x = 2 and then rises steeply to 17 at the right end. ✓'},
        'mistakes': ['Forgetting to test the endpoints.', 'Including critical numbers that lie outside the interval.', 'Assuming every critical point is a maximum or minimum.', 'Ignoring points where f′ is undefined.'],
        'real_world': 'A farmer\'s profit from a crop depends on how much fertiliser is used. The closed interval method, with the endpoints set by the budget, finds the amount that gives the highest profit.',
        'exam_strategy': 'Put the candidate points and their f-values in a small table. It makes the comparison obvious and shows the examiner that you checked every candidate.',
        'recap': ['Critical points: f′ = 0 or undefined.', 'Closed interval: test critical points and endpoints.', 'f′(c) = 0 does not guarantee an extremum.', 'Continuous on [a, b] ⇒ absolute extremes exist.']},
    T2: {
        'overview': 'The Mean Value Theorem links the average rate of change over an interval to the instantaneous rate at some point inside it. From it come the tests that read a graph\'s shape from f′ and f″.',
        'key_terms': ["Rolle's theorem", 'Mean Value Theorem (MVT)', 'Increasing and decreasing', 'First derivative test', 'Concave up and down', 'Point of inflection', 'Second derivative test'],
        'explanation': [
            'The MVT says: if f is continuous on [a, b] and differentiable on (a, b), then f′(c) = (f(b) − f(a))/(b − a) for some c in (a, b). Somewhere the tangent is parallel to the chord. Rolle\'s theorem is the special case f(a) = f(b), which gives f′(c) = 0.',
            'A consequence of the MVT is the increasing/decreasing test: if f′ > 0 on an interval, f is increasing there; if f′ < 0, it is decreasing. The first derivative test classifies a critical point by the sign change of f′: from + to − is a local maximum, from − to + a local minimum, and no change means neither.',
            'f″ describes bending. If f″ > 0 the graph is concave up (a cup that holds water); if f″ < 0 it is concave down. A point where the concavity changes is a point of inflection. The second derivative test: if f′(c) = 0 and f″(c) > 0, c is a local minimum; if f″(c) < 0, a local maximum; if f″(c) = 0, the test gives no answer.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['MVT: f′(c) = (f(b) − f(a))/(b − a) for some c in (a, b)', 'f′ > 0 ⇒ increasing; f′ < 0 ⇒ decreasing', 'f″ > 0 ⇒ concave up; f″ < 0 ⇒ concave down', 'f′(c) = 0, f″(c) > 0 ⇒ local min; f″(c) < 0 ⇒ local max'],
        'steps': ['Find f′ and its zeros; mark them on a number line.', 'Test the sign of f′ in each interval to find where f increases or decreases.', 'Classify each critical point by the sign change.', 'Find f″ and its zeros; test signs to find concavity.', 'Points where f″ changes sign are inflection points.'],
        'worked_example': {
            'problem': 'For f(x) = x³ − 6x² + 9x + 2, find the intervals of increase and decrease, the local extrema, and the inflection point.',
            'steps': ['f′(x) = 3x² − 12x + 9 = 3(x − 1)(x − 3). Critical numbers 1 and 3.', 'f′ > 0 for x < 1, f′ < 0 for 1 < x < 3, f′ > 0 for x > 3.', 'So f increases on (−∞, 1) and (3, ∞) and decreases on (1, 3). Local max f(1) = 6; local min f(3) = 2.', 'f″(x) = 6x − 12 = 0 at x = 2, and f″ changes sign there.', 'Inflection point (2, f(2)) = (2, 4).'],
            'answer': 'Increasing on (−∞, 1) and (3, ∞), decreasing on (1, 3); local max (1, 6), local min (3, 2); inflection at (2, 4).',
            'check': 'f″(1) = −6 < 0 (max ✓) and f″(3) = 6 > 0 (min ✓). The inflection x = 2 lies midway between them, as for every cubic. ✓'},
        'mistakes': ['Calling every point where f″ = 0 an inflection point: x⁴ has f″(0) = 0 but no change of concavity.', 'Applying the MVT to a function with a corner or a gap in the interval.', 'Reading concave up as "increasing".', 'Concluding "neither" when the second derivative test gives f″(c) = 0. Use the first derivative test instead.'],
        'real_world': 'If a car travels 120 km in 1.5 hours, the MVT guarantees that at some instant its speed was exactly 80 km/h. Average-speed cameras on highways rely on exactly this reasoning.',
        'exam_strategy': 'Draw a sign chart for f′ and another for f″. Examiners expect the intervals stated explicitly, with the reasoning ("f′ > 0 on…") written alongside.',
        'recap': ['MVT: some tangent is parallel to the chord.', 'Sign of f′: rising or falling.', 'Sign of f″: concave up or down.', 'Inflection needs a change of concavity.']},
    T3: {
        'overview': 'Optimisation means finding the best value of a quantity, such as the largest area, the least material or the lowest cost, subject to a constraint. It is calculus at its most practical.',
        'key_terms': ['Objective function', 'Constraint', 'Feasible domain', 'Critical point', 'Justifying a maximum or minimum'],
        'explanation': [
            'Every optimisation problem has an objective (the quantity to make as large or small as possible) and a constraint (a condition that links the variables). Write both as equations. Use the constraint to express the objective in terms of one variable.',
            'Decide the realistic domain: lengths must be positive, and a cut cannot be wider than the sheet. Then differentiate, set the derivative to zero and solve.',
            'Always justify your answer. Use the second derivative test, a sign chart for the first derivative, or the closed interval method if the domain is closed. Finally, answer the question that was asked, with units: "the dimensions are 25 m by 25 m", not just "x = 25".'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Rectangle: A = xy, P = 2x + 2y', 'Open box from a square sheet of side L with squares x cut out: V = x(L − 2x)²', 'Cylinder: V = πr²h, surface area A = 2πr² + 2πrh', 'Profit = Revenue − Cost'],
        'steps': ['Draw a diagram and name the variables.', 'Write the objective function and the constraint.', 'Use the constraint to reduce the objective to one variable and state its domain.', 'Differentiate, set equal to zero and solve.', 'Justify that it is a maximum or minimum, then answer in words with units.'],
        'worked_example': {
            'problem': 'A farmer has 100 m of fencing for a rectangular pen. What dimensions give the largest area?',
            'steps': ['Let the sides be x and y. Constraint: 2x + 2y = 100, so y = 50 − x.', 'Objective: A = xy = x(50 − x) = 50x − x², with 0 < x < 50.', 'A′(x) = 50 − 2x = 0 gives x = 25.', 'A″(x) = −2 < 0, so x = 25 gives a maximum.', 'Then y = 25 and A = 625 m².'],
            'answer': 'A 25 m by 25 m square pen, with area 625 m².',
            'check': 'Nearby choices give less area: 24 × 26 = 624 m² and 20 × 30 = 600 m². ✓'},
        'mistakes': ['Differentiating before reducing to one variable.', 'Forgetting to check the endpoints of a closed domain.', 'Giving x = 25 without answering the question asked.', 'Accepting a critical point outside the realistic domain, such as a negative length.'],
        'real_world': 'Drink companies choose can dimensions to hold a fixed volume with as little aluminium as possible. Minimising surface area for a fixed volume is a classic optimisation, and it saves millions in materials.',
        'exam_strategy': 'Marks come in stages: constraint, one-variable objective, derivative, critical point, justification, final answer. Label each stage so that partial credit is easy to award.',
        'recap': ['Objective plus constraint.', 'Reduce to one variable and state the domain.', 'Differentiate, solve, justify.', 'Answer the actual question with units.']},
    T4: {
        'overview': 'Two quick uses of the derivative: L\'Hôpital\'s rule evaluates limits of the form 0/0 or ∞/∞, and linear approximation estimates function values with a tangent line.',
        'key_terms': ["L'Hôpital's rule", 'Indeterminate forms', 'Linearisation L(x)', 'Linear approximation', 'Differentials dy'],
        'explanation': [
            'If lim f(x)/g(x) gives 0/0 or ∞/∞, then lim f(x)/g(x) = lim f′(x)/g′(x), provided the new limit exists. Differentiate the top and bottom separately; this is not the quotient rule. You may apply it more than once.',
            'Other indeterminate forms must be rewritten first. A product 0 · ∞ becomes a fraction, such as x ln x = ln x/(1/x). Powers like 1^∞ are handled by taking logarithms.',
            'Near x = a the tangent line is close to the curve, so f(x) ≈ L(x) = f(a) + f′(a)(x − a). Choose a near the point you want and where f(a) is easy to compute: to estimate √4.1, use a = 4. The error is small when x is close to a.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ["L'Hôpital: lim f/g = lim f′/g′ for 0/0 or ∞/∞", 'Linearisation: L(x) = f(a) + f′(a)(x − a)', 'Differential: dy = f′(x)dx, so Δy ≈ f′(x)Δx', 'lim x→0⁺ x ln x = 0'],
        'steps': ['Substitute to confirm the form is 0/0 or ∞/∞.', 'Differentiate the numerator and the denominator separately.', 'Substitute again; repeat if still indeterminate.', 'For approximation, choose a nearby easy point a.', 'Compute f(a) and f′(a) and evaluate L(x).'],
        'worked_example': {
            'problem': "Evaluate lim x→0 (eˣ − 1 − x)/x², then estimate √4.1 with a linear approximation.",
            'steps': ['Substitution gives 0/0. Apply the rule: lim (eˣ − 1)/(2x), still 0/0.', 'Apply it again: lim eˣ/2 = 1/2.', 'For √4.1: f(x) = √x, a = 4, f(4) = 2, f′(x) = 1/(2√x), f′(4) = 1/4.', 'L(4.1) = 2 + (1/4)(0.1) = 2.025.'],
            'answer': 'The limit is 1/2, and √4.1 ≈ 2.025.',
            'check': 'A calculator gives √4.1 = 2.02485…, so the estimate is out by about 0.00015. ✓'},
        'mistakes': ["Using L'Hôpital's rule when the form is not indeterminate, for example lim x→1 x/(x + 1).", 'Applying the quotient rule instead of differentiating top and bottom separately.', 'Using a far-away point a for a linear approximation.', 'Forgetting to rewrite 0 · ∞ as a fraction first.'],
        'real_world': 'Engineers use linear approximation all the time: a small change Δr in a pipe\'s radius changes its cross-sectional area by about 2πr·Δr. Tolerances on machined parts are set this way.',
        'exam_strategy': "State the indeterminate form each time you apply L'Hôpital's rule, for example \"(0/0), so by L'Hôpital…\". Marks are often lost for applying it without showing the form.",
        'recap': ["L'Hôpital only for 0/0 or ∞/∞.", 'Differentiate top and bottom separately.', 'L(x) = f(a) + f′(a)(x − a).', 'Pick a close to x and easy to evaluate.']},
}

f1 = x**3 - 3*x**2 + 1
f2 = x**3 - 6*x**2 + 9*x + 2
QUESTIONS = [
    # T1
    Q(T1, 'What are the critical numbers of f(x) = x³ − 3x² + 1?', ['x = 0 and x = 2', 'x = 1 and x = 3', 'x = 0 only', 'x = −1 and x = 2'], 0, 'f′(x) = 3x² − 6x = 3x(x − 2), which is 0 at x = 0 and x = 2.'),
    Q(T1, 'What is the absolute maximum of f(x) = x³ − 3x² + 1 on [−1, 4]?', ['1', '17', '−3', '8'], 1, 'Candidates: f(−1) = −3, f(0) = 1, f(2) = −3, f(4) = 17. The largest is 17.', ans=max(f1.subs(x, v) for v in (-1, 0, 2, 4))),
    Q(T1, 'What is the absolute minimum of f(x) = x² − 4x + 7 on [0, 5]?', ['7', '3', '12', '0'], 1, 'f′ = 2x − 4 = 0 at x = 2. f(0) = 7, f(2) = 3, f(5) = 12, so the minimum is 3.', ans=3),
    Q(T1, 'f(x) = x³ has f′(0) = 0. What happens at x = 0?', ['A local maximum', 'A local minimum', 'Neither: it is a horizontal point of inflection', 'f is not differentiable there'], 2, 'f′(x) = 3x² ≥ 0 on both sides, so f keeps increasing through 0. A zero derivative does not guarantee an extremum.'),
    Q(T1, 'Which is a critical number of f(x) = x^(2/3)?', ['x = 1', 'x = 0', 'x = −1', 'There are none'], 1, 'f′(x) = (2/3)x^(−1/3) is undefined at x = 0, which is in the domain, so 0 is a critical number (a cusp and a minimum).'),
    Q(T1, 'Find the absolute maximum of f(x) = 2x³ − 3x² − 12x on [−2, 3].', ['7', '−20', '−9', '4'], 0, 'f′ = 6(x − 2)(x + 1). Values: f(−2) = −4, f(−1) = 7, f(2) = −20, f(3) = −9. The maximum is 7.', ans=max((2*x**3 - 3*x**2 - 12*x).subs(x, v) for v in (-2, -1, 2, 3))),
    # T2
    Q(T2, 'On which interval is f(x) = x³ − 6x² + 9x + 2 decreasing?', ['(−∞, 1)', '(1, 3)', '(3, ∞)', '(0, 2)'], 1, 'f′(x) = 3(x − 1)(x − 3) is negative between 1 and 3.'),
    Q(T2, 'Where is the point of inflection of f(x) = x³ − 6x² + 9x + 2?', ['(1, 6)', '(2, 4)', '(3, 2)', '(0, 2)'], 1, 'f″(x) = 6x − 12 = 0 at x = 2, and it changes sign there. f(2) = 8 − 24 + 18 + 2 = 4.'),
    Q(T2, 'For f(x) = x² on [1, 3], the MVT gives a point c where f′(c) equals the average rate of change. What is c?', ['1.5', '2', '2.5', '3'], 1, 'Average rate = (9 − 1)/2 = 4. f′(c) = 2c = 4, so c = 2.', ans=2),
    Q(T2, 'If f′(c) = 0 and f″(c) = −5, then at x = c the function has:', ['a local minimum', 'a local maximum', 'a point of inflection', 'no conclusion possible'], 1, 'Concave down with a horizontal tangent is a peak, so it is a local maximum.'),
    Q(T2, 'Where is f(x) = x⁴ − 4x³ concave down?', ['(0, 2)', '(−∞, 0)', '(2, ∞)', '(0, 3)'], 0, 'f″(x) = 12x² − 24x = 12x(x − 2), which is negative between 0 and 2.'),
    Q(T2, 'Is x = 0 a point of inflection of f(x) = x⁴?', ['Yes, because f″(0) = 0', 'No, because f″ does not change sign there', 'Yes, because f′(0) = 0', 'No, because f is not differentiable there'], 1, 'f″(x) = 12x² ≥ 0 on both sides of 0, so the graph is concave up throughout. f″ = 0 alone is not enough.'),
    # T3
    Q(T3, 'With 100 m of fencing, what is the largest rectangular area you can enclose?', ['500 m²', '625 m²', '2500 m²', '600 m²'], 1, 'A = x(50 − x) is largest at x = 25, giving 25 × 25 = 625 m².', ans=(x*(50 - x)).subs(x, 25)),
    Q(T3, 'Two positive numbers add up to 20. What is the largest possible product?', ['100', '96', '200', '75'], 0, 'P = x(20 − x), P′ = 20 − 2x = 0 at x = 10, so P = 100.', ans=100),
    Q(T3, 'Squares of side x are cut from the corners of a 12 cm by 12 cm sheet to make an open box. Which x gives the largest volume?', ['1 cm', '2 cm', '3 cm', '4 cm'], 1, 'V = x(12 − 2x)², V′ = (12 − 2x)(12 − 6x) = 0 at x = 2 (x = 6 gives V = 0). V(2) = 128 cm³.', ans=2),
    Q(T3, 'What is the largest volume of that box?', ['128 cm³', '100 cm³', '144 cm³', '108 cm³'], 0, 'V(2) = 2 × 8 × 8 = 128 cm³.', ans=(x*(12 - 2*x)**2).subs(x, 2)),
    Q(T3, 'A firm\'s profit in {{CUR}} thousands is P(q) = −2q² + 40q − 50 for q hundred units. How many hundred units maximise profit?', ['5', '10', '20', '40'], 1, 'P′(q) = −4q + 40 = 0 gives q = 10, and P″ = −4 < 0 confirms a maximum.', ans=10),
    Q(T3, 'Why must you justify a critical point in an optimisation problem?', ['Because the derivative might be wrong', 'Because a critical point could be a minimum, a maximum or neither', 'Because examiners like long answers', 'It is never necessary'], 1, 'f′ = 0 only finds candidates. A second derivative test, sign chart or endpoint comparison shows which kind of point it is.'),
    # T4
    Q(T4, "Evaluate lim x→0 (eˣ − 1 − x)/x² using L'Hôpital's rule.", ['0', '1/2', '1', '∞'], 1, 'Apply the rule twice: (eˣ − 1)/(2x), then eˣ/2 → 1/2.', ans=sp.limit((sp.exp(x) - 1 - x)/x**2, x, 0)),
    Q(T4, 'Evaluate lim x→0 (1 − cos x)/x².', ['0', '1', '1/2', '2'], 2, 'Rule once: sin x/(2x) → 1/2.', ans=sp.limit((1 - sp.cos(x))/x**2, x, 0)),
    Q(T4, 'Evaluate lim x→∞ (ln x)/x.', ['0', '1', '∞', 'e'], 0, 'This is ∞/∞. The rule gives (1/x)/1 → 0: logarithms grow slower than any power.', ans=0),
    Q(T4, 'Evaluate lim x→0⁺ x ln x.', ['0', '−∞', '1', '−1'], 0, 'Rewrite as ln x/(1/x), which is −∞/∞. The rule gives (1/x)/(−1/x²) = −x → 0.', ans=0),
    Q(T4, 'Use a linear approximation at a = 4 to estimate √4.1.', ['2.05', '2.025', '2.01', '2.1'], 1, 'L(x) = 2 + (1/4)(x − 4), so L(4.1) = 2.025. The true value is 2.02485…', ans=sp.Rational(2025, 1000)),
    Q(T4, 'The linearisation of f(x) = eˣ at a = 0 is:', ['L(x) = x', 'L(x) = 1 + x', 'L(x) = e + x', 'L(x) = 1 − x'], 1, 'f(0) = 1 and f′(0) = 1, so L(x) = 1 + x. Hence e^0.02 ≈ 1.02.', ans=1 + x),
    Q(T4, "Why can't L'Hôpital's rule be used for lim x→1 x/(x + 1)?", ['The limit does not exist', 'The form is not indeterminate: substitution gives 1/2', 'The functions are not differentiable', 'It can be used'], 1, 'Substituting gives 1/2 directly. Using the rule anyway would give 1/1 = 1, which is wrong.'),
]

FLASH = [
    ['Critical number', 'A point in the domain where f′ = 0 or f′ is undefined.'],
    ['Closed interval method', 'Evaluate f at the critical points and the endpoints; compare.'],
    ['Mean Value Theorem', 'f′(c) = (f(b) − f(a))/(b − a) for some c in (a, b).'],
    ['First derivative test', 'f′ changes + to −: local max. − to +: local min.'],
    ['Second derivative test', 'f′(c) = 0 and f″(c) < 0: max. f″(c) > 0: min.'],
    ['Point of inflection', 'Where the concavity changes, so f″ changes sign.'],
    ['Optimisation steps', 'Objective, constraint, one variable, differentiate, justify, answer with units.'],
    ["L'Hôpital's rule", 'For 0/0 or ∞/∞: lim f/g = lim f′/g′.'],
    ['Linearisation', 'L(x) = f(a) + f′(a)(x − a).'],
]
