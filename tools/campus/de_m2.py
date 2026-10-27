"""Differential Equations, module 2: Modelling with first-order equations."""
from verify import Q, x, t, sp
T1, T2, T3, T4 = ('Growth, decay and Newton\'s law of cooling', 'Mixing problems', 'The logistic equation', 'Equilibria, direction fields and Euler\'s method')
y = sp.Function('y')
r = lambda v, d: round(float(v), d)
assert r(sp.log(2) / 5, 4) == 0.1386 and r(1000 * sp.exp(sp.Rational(1, 2)), 2) == 1648.72
kc = sp.log(sp.Rational(7, 4)) / 10
assert r(20 + 70 * sp.exp(-kc * 20), 1) == 42.9 and sp.simplify(20 + 70 * sp.exp(-kc * 20) - (20 + 70 * sp.Rational(16, 49))) == 0
A = sp.dsolve(sp.Eq(y(t).diff(t), 10 - y(t) / 20), y(t), ics={y(0): 0}).rhs
assert sp.simplify(A - 200 * (1 - sp.exp(-t / 20))) == 0 and r(A.subs(t, 20), 2) == 126.42 and sp.limit(A, t, sp.oo) == 200
P = 1000 / (1 + 9 * sp.exp(-t / 2))
assert sp.simplify(P.diff(t) - P / 2 * (1 - P / 1000)) == 0 and P.subs(t, 0) == 100 and r(2 * sp.log(9), 2) == 4.39
f = lambda yy: yy * (yy - 2)
assert sp.diff(f(x), x).subs(x, 0) == -2 and sp.diff(f(x), x).subs(x, 2) == 2
y1 = 1 + sp.Rational(1, 10) * (0 + 1); y2 = y1 + sp.Rational(1, 10) * (sp.Rational(1, 10) + y1)
assert y1 == sp.Rational(11, 10) and y2 == sp.Rational(61, 50) and r(2 * sp.exp(sp.Rational(1, 5)) - sp.Rational(6, 5), 4) == 1.2428

MODULE = {
    'title': 'Modelling with first-order equations',
    'topics': [T1, T2, T3, T4],
    'overview': 'First-order equations model growth, decay, cooling, mixing and populations. This module builds those models from rates of change, solves them, and uses qualitative tools (equilibria, direction fields) and Euler\'s method when a formula is hard or impossible to find.',
    'key_terms': ['Exponential growth', 'Half-life', 'Doubling time', 'Newton\'s law of cooling', 'Rate in − rate out', 'Concentration', 'Logistic equation', 'Carrying capacity', 'Equilibrium', 'Stability', 'Direction field', 'Euler\'s method'],
    'explanation': [
        'Modelling turns a sentence about rates into an equation: "grows at a rate proportional to its size" is y′ = ky; "cools at a rate proportional to the difference from the room" is T′ = −k(T − Tₐ); "salt in minus salt out" is A′ = rate in − rate out.',
        'Exponential models grow or decay without limit; the logistic model y′ = ry(1 − y/K) adds a carrying capacity K, giving the S-shaped curve seen in populations and the spread of new technologies.',
        'Often the shape of the solution matters more than a formula. Equilibria (where y′ = 0) and their stability tell you the long-run behaviour, direction fields show every solution at a glance, and Euler\'s method approximates solutions step by step.'],
    'quick_facts': [
        'y′ = ky ⇒ y = y₀eᵏᵗ; doubling time ln 2/k, half-life ln 2/k for decay.',
        'Cooling: T = Tₐ + (T₀ − Tₐ)e^(−kt).',
        'Mixing: dA/dt = (conc. in × rate in) − (A/V × rate out).',
        'Logistic: y = K/(1 + Ae^(−rt)), fastest growth at y = K/2.',
        'Euler: yₙ₊₁ = yₙ + h f(xₙ, yₙ).'],
}

NOTES = {
    T1: {
        'overview': 'Quantities that change at a rate proportional to their size grow or decay exponentially. Newton\'s law of cooling is the same idea applied to a temperature difference.',
        'key_terms': ['Proportional rate', 'Growth constant', 'Doubling time', 'Half-life', 'Continuous compounding', 'Ambient temperature'],
        'explanation': [
            'y′ = ky has solution y = y₀eᵏᵗ. Doubling time is ln 2/k: a population that doubles every 5 years has k = ln 2/5 ≈ 0.1386 per year, and after 15 years it is 2³ = 8 times larger. For decay (k < 0), the half-life is ln 2/|k|. Carbon-14 has a half-life of about 5730 years, so after 11 460 years a quarter remains.',
            'Money compounded continuously at rate r grows as A = A₀eʳᵗ: R1000 at 5% for 10 years becomes 1000e^0.5 ≈ R1648.72.',
            'Newton\'s law of cooling: T′ = −k(T − Tₐ), so T = Tₐ + (T₀ − Tₐ)e^(−kt). Coffee at 90 °C in a 20 °C room that is 60 °C after 10 minutes has e^(−10k) = 40/70 = 4/7. After 20 minutes: T = 20 + 70(4/7)² ≈ 42.9 °C.'],
        'formulas_label': 'Formulas',
        'formulas': ['y = y₀eᵏᵗ', 'Doubling time = ln 2/k; half-life = ln 2/|k|', 'A = A₀eʳᵗ (continuous compounding)', 'T = Tₐ + (T₀ − Tₐ)e^(−kt)'],
        'steps': ['Write the rate equation from the words.', 'Solve (separable).', 'Use the data to find the constant k.', 'Answer the question (time, value) and check units.'],
        'worked_example': {
            'problem': 'Coffee at 90 °C is placed in a 20 °C room. After 10 minutes it is 60 °C. What is its temperature after 20 minutes?',
            'steps': ['T = 20 + 70e^(−kt).', 'At t = 10: 60 = 20 + 70e^(−10k), so e^(−10k) = 4/7.', 'At t = 20: e^(−20k) = (4/7)², T = 20 + 70 × 16/49 ≈ 42.9 °C.'],
            'answer': 'About 42.9 °C.',
            'check': 'The second 10 minutes drop is smaller (60 → 42.9 vs 90 → 60), as cooling slows when the gap closes ✓.'},
        'mistakes': ['Using T′ = −kT instead of −k(T − Tₐ).', 'Forgetting that k must come from data.', 'Confusing half-life with the decay constant.', 'Mixing time units.'],
        'real_world': 'Forensic scientists estimate time of death by applying Newton\'s law of cooling to body temperature.',
        'exam_strategy': 'Avoid finding k as a decimal when ratios work: e^(−20k) = (e^(−10k))² keeps the arithmetic exact.',
        'recap': ['y′ = ky ⇒ exponential.', 'Doubling and half-life use ln 2.', 'Cooling depends on the gap.', 'Find k from data.']},
    T2: {
        'overview': 'Mixing problems track the amount of a substance in a tank: the rate of change equals the rate it flows in minus the rate it flows out.',
        'key_terms': ['Amount A(t)', 'Concentration', 'Inflow rate', 'Outflow rate', 'Well-mixed', 'Steady state'],
        'explanation': [
            'If brine of concentration cᵢₙ flows in at rate rᵢₙ and the well-mixed solution flows out at rate rₒᵤₜ, then dA/dt = cᵢₙrᵢₙ − (A/V)rₒᵤₜ, where V is the volume (constant when rᵢₙ = rₒᵤₜ).',
            'A tank holds 100 L of pure water. Brine with 2 g/L of salt flows in at 5 L/min and the mixture flows out at 5 L/min. Then dA/dt = 10 − A/20, a linear (and separable) equation with A(0) = 0. Its solution is A = 200(1 − e^(−t/20)).',
            'After 20 minutes, A = 200(1 − e^(−1)) ≈ 126.42 g. In the long run A → 200 g, which is the concentration of the incoming brine (2 g/L) times the volume (100 L), as expected.'],
        'formulas_label': 'Formulas',
        'formulas': ['dA/dt = (rate in) − (rate out)', 'rate in = cᵢₙ × rᵢₙ', 'rate out = (A/V) × rₒᵤₜ', 'V(t) = V₀ + (rᵢₙ − rₒᵤₜ)t if rates differ'],
        'steps': ['Define A(t) and its units.', 'Write rate in and rate out.', 'Solve with A(0).', 'Check the long-run value makes sense.'],
        'worked_example': {
            'problem': 'A 100 L tank of pure water receives 2 g/L brine at 5 L/min and drains at 5 L/min. Find the salt after 20 minutes.',
            'steps': ['dA/dt = 2 × 5 − (A/100) × 5 = 10 − A/20, A(0) = 0.', 'Solution: A = 200(1 − e^(−t/20)).', 'A(20) = 200(1 − e^(−1)) ≈ 126.42 g.'],
            'answer': 'About 126.4 g.',
            'check': 'Long-run A → 200 g = 2 g/L × 100 L ✓.'},
        'mistakes': ['Using the inflow concentration for the outflow.', 'Forgetting the volume changes when the rates differ.', 'Mixing litres and millilitres.', 'Missing the initial amount.'],
        'real_world': 'Pharmacologists use the same model for a drug infused into the bloodstream while the kidneys clear it.',
        'exam_strategy': 'Check units in each term (g/min); a units mismatch exposes most setup errors.',
        'recap': ['In minus out.', 'Out uses A/V.', 'Linear first-order.', 'Long run = input concentration × volume.']},
    T3: {
        'overview': 'The logistic equation adds limited resources to exponential growth: growth slows as the population approaches the carrying capacity.',
        'key_terms': ['Logistic equation', 'Carrying capacity', 'Intrinsic growth rate', 'Inflection point', 'S-curve'],
        'explanation': [
            'y′ = ry(1 − y/K). When y is small, it behaves like y′ ≈ ry (exponential). As y approaches K, the factor (1 − y/K) shrinks the growth rate to zero. Equilibria are y = 0 and y = K.',
            'The solution is y = K/(1 + Ae^(−rt)) with A = (K − y₀)/y₀. For r = 0.5, K = 1000 and y₀ = 100: A = 9 and y = 1000/(1 + 9e^(−0.5t)).',
            'Growth is fastest at y = K/2 (the inflection point of the S-curve). In the example, y = 500 when 9e^(−0.5t) = 1, so t = 2 ln 9 ≈ 4.39.'],
        'formulas_label': 'Formulas',
        'formulas': ['y′ = ry(1 − y/K)', 'y = K/(1 + Ae^(−rt)), A = (K − y₀)/y₀', 'Fastest growth at y = K/2', 'Equilibria: 0 (unstable), K (stable)'],
        'steps': ['Identify r and K.', 'Compute A from y₀.', 'Write the solution.', 'Solve for times or values as needed.'],
        'worked_example': {
            'problem': 'A population follows y′ = 0.5y(1 − y/1000) with y(0) = 100. When is it growing fastest?',
            'steps': ['y = 1000/(1 + 9e^(−0.5t)).', 'Fastest growth at y = 500.', '1 + 9e^(−0.5t) = 2 ⇒ e^(−0.5t) = 1/9 ⇒ t = 2 ln 9 ≈ 4.39.'],
            'answer': 'At t ≈ 4.39, when the population is 500.',
            'check': 'Differentiating confirms y′ = 0.5y(1 − y/1000), and y(0) = 1000/10 = 100 ✓.'},
        'mistakes': ['Forgetting that y = K is stable and y = 0 unstable.', 'Getting A upside down.', 'Thinking growth is fastest at the start.', 'Using exponential growth beyond its limits.'],
        'real_world': 'The spread of mobile phones and other new technologies often follows an S-curve: slow start, rapid uptake, then saturation.',
        'exam_strategy': 'Memorise y = K/(1 + Ae^(−rt)); deriving it with partial fractions takes time you may not have.',
        'recap': ['Growth limited by K.', 'S-shaped solution.', 'Fastest at K/2.', 'y → K.']},
    T4: {
        'overview': 'When a formula is hard to find, qualitative and numerical methods still describe the solutions.',
        'key_terms': ['Autonomous equation', 'Equilibrium solution', 'Stable', 'Unstable', 'Phase line', 'Direction field', 'Euler\'s method', 'Step size'],
        'explanation': [
            'For an autonomous equation y′ = f(y), equilibria are the roots of f(y) = 0. An equilibrium is stable if nearby solutions move towards it: f′(y*) < 0, and unstable if f′(y*) > 0. For y′ = y(y − 2), the equilibria are 0 (f′ = −2, stable) and 2 (f′ = 2, unstable).',
            'A direction field draws a short line of slope f(x, y) at many points; solution curves follow the lines. It shows the shape of every solution without solving anything.',
            'Euler\'s method steps along the tangent line: yₙ₊₁ = yₙ + h f(xₙ, yₙ). For y′ = x + y, y(0) = 1, h = 0.1: y₁ = 1 + 0.1(0 + 1) = 1.1, y₂ = 1.1 + 0.1(0.1 + 1.1) = 1.22. The exact value is y(0.2) = 2e^0.2 − 1.2 ≈ 1.2428, so Euler underestimates here; smaller steps reduce the error roughly in proportion to h.'],
        'formulas_label': 'Formulas',
        'formulas': ['Equilibria: f(y*) = 0', 'Stable if f′(y*) < 0; unstable if f′(y*) > 0', 'Euler: yₙ₊₁ = yₙ + h f(xₙ, yₙ), xₙ₊₁ = xₙ + h', 'Euler error ∝ h'],
        'steps': ['Find equilibria from f(y) = 0.', 'Classify with the sign of f′.', 'For Euler, tabulate xₙ, yₙ, f(xₙ, yₙ).', 'Compare with exact values when possible.'],
        'worked_example': {
            'problem': 'Use Euler\'s method with h = 0.1 to estimate y(0.2) for y′ = x + y, y(0) = 1.',
            'steps': ['Step 1: f(0, 1) = 1, y₁ = 1 + 0.1 × 1 = 1.1.', 'Step 2: f(0.1, 1.1) = 1.2, y₂ = 1.1 + 0.1 × 1.2 = 1.22.', 'Exact: y = 2eˣ − x − 1, y(0.2) ≈ 1.2428.'],
            'answer': 'y(0.2) ≈ 1.22 (error about 0.023).',
            'check': 'The solution curves upward (y″ > 0), so tangent steps fall below it: an underestimate is expected ✓.'},
        'mistakes': ['Using f(xₙ₊₁, yₙ₊₁) instead of f(xₙ, yₙ).', 'Forgetting to advance x.', 'Getting stability backwards.', 'Rounding too early.'],
        'real_world': 'Every computer simulation of motion, from games to spacecraft, uses refined versions of Euler\'s step-by-step idea.',
        'exam_strategy': 'Set Euler\'s method out as a table with columns n, xₙ, yₙ, f(xₙ, yₙ); it avoids slips and earns method marks.',
        'recap': ['Equilibria from f = 0.', 'Stability from f′.', 'Direction fields show shapes.', 'Euler steps along tangents.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A population doubles every 5 years. Its growth constant k is about:', ['0.1386 per year', '0.2 per year', '0.693 per year', '5 per year'], 0, 'k = ln 2/5 ≈ 0.1386.'),
    Q(T1, 'That population after 15 years is how many times its starting size?', ['8', '3', '6', '15'], 0, 'Three doublings.', ans=8),
    Q(T1, 'R1000 compounded continuously at 5% for 10 years grows to about:', ['R1648.72', 'R1500.00', 'R1628.89', 'R2000.00'], 0, '1000e^0.5.'),
    Q(T1, 'After two half-lives, the fraction of a radioactive sample remaining is:', ['1/4', '1/2', '1/8', '0'], 0, '(1/2)².', ans=sp.Rational(1, 4)),
    Q(T1, 'Coffee: 90 °C at t = 0, 60 °C at t = 10 min, room 20 °C. At t = 20 min it is about:', ['42.9 °C', '30 °C', '50 °C', '36.0 °C'], 0, '20 + 70(4/7)².'),
    Q(T1, 'Newton\'s law of cooling says the rate of cooling is proportional to:', ['the difference between the object\'s and the surroundings\' temperature', 'the object\'s temperature', 'time', 'the square of the temperature'], 0, 'T′ = −k(T − Tₐ).'),
    # T2
    Q(T2, 'A 100 L tank: 2 g/L brine in at 5 L/min, out at 5 L/min. The equation for the salt A is:', ['dA/dt = 10 − A/20', 'dA/dt = 10 − A/100', 'dA/dt = 2 − A/20', 'dA/dt = 10 + A/20'], 0, '2 × 5 − (A/100) × 5.'),
    Q(T2, 'Starting from pure water, the salt after 20 minutes is about:', ['126.42 g', '200 g', '100 g', '73.58 g'], 0, '200(1 − e^(−1)).'),
    Q(T2, 'In the long run, the salt in the tank approaches:', ['200 g', '100 g', '10 g', 'infinity'], 0, '2 g/L × 100 L.', ans=200),
    Q(T2, 'The rate at which salt leaves the tank is:', ['(A/V) × outflow rate', 'inflow concentration × outflow rate', 'A × V', 'zero'], 0, 'Well-mixed concentration out.'),
    Q(T2, 'The salt equation A′ = 10 − A/20 is:', ['linear and separable', 'nonlinear', 'second order', 'exact only'], 0, 'Both methods work.'),
    Q(T2, 'If inflow is 6 L/min and outflow 4 L/min starting at 100 L, the volume after t minutes is:', ['100 + 2t', '100 − 2t', '100', '100 + 6t'], 0, 'Net gain 2 L/min.', ans=100 + 2 * t),
    # T3
    Q(T3, 'For y′ = 0.5y(1 − y/1000), the carrying capacity is:', ['1000', '0.5', '500', '2000'], 0, 'K = 1000.', ans=1000),
    Q(T3, 'With y(0) = 100, the solution is y =', ['1000/(1 + 9e^(−0.5t))', '1000/(1 + 10e^(−0.5t))', '100e^(0.5t)', '1000(1 − e^(−0.5t))'], 0, 'A = (1000 − 100)/100 = 9.', ans=P),
    Q(T3, 'The population grows fastest when y equals:', ['500', '1000', '100', '0'], 0, 'K/2.', ans=500),
    Q(T3, 'It reaches 500 at t ≈', ['4.39', '2.20', '9.00', '1.39'], 0, '2 ln 9.', ans=2 * sp.log(9), num=True),
    Q(T3, 'Which equilibrium of the logistic equation is stable?', ['y = K', 'y = 0', 'both', 'neither'], 0, 'Solutions approach K.'),
    Q(T3, 'For small y, logistic growth is approximately:', ['exponential', 'linear', 'constant', 'decreasing'], 0, '1 − y/K ≈ 1.'),
    # T4
    Q(T4, 'The equilibria of y′ = y(y − 2) are:', ['0 and 2', '0 only', '2 only', '−2 and 0'], 0, 'f(y) = 0.'),
    Q(T4, 'For y′ = y(y − 2), the equilibrium y = 0 is:', ['stable', 'unstable', 'semi-stable', 'not an equilibrium'], 0, 'f′(0) = −2 < 0.'),
    Q(T4, 'Euler\'s method with h = 0.1 for y′ = x + y, y(0) = 1 gives y(0.1) ≈', ['1.1', '1.0', '1.2', '1.11'], 0, '1 + 0.1 × 1.', ans=sp.Rational(11, 10)),
    Q(T4, 'One more step gives y(0.2) ≈', ['1.22', '1.21', '1.2', '1.24'], 0, '1.1 + 0.1 × 1.2.', ans=sp.Rational(61, 50)),
    Q(T4, 'Halving the step size in Euler\'s method roughly:', ['halves the error', 'quarters the error', 'doubles the error', 'leaves the error unchanged'], 0, 'First-order method.'),
    Q(T4, 'A direction field shows:', ['the slope of solutions at many points', 'the exact solution formula', 'only equilibria', 'the integrating factor'], 0, 'Short tangent lines.'),
]

FLASH = [
    ['Exponential model', 'y′ = ky ⇒ y = y₀eᵏᵗ.'],
    ['Half-life', 'ln 2/|k|: time for a decaying quantity to halve.'],
    ['Newton\'s law of cooling', 'T′ = −k(T − Tₐ); T = Tₐ + (T₀ − Tₐ)e^(−kt).'],
    ['Mixing equation', 'dA/dt = rate in − (A/V) × rate out.'],
    ['Logistic equation', 'y′ = ry(1 − y/K); S-curve approaching K.'],
    ['Carrying capacity', 'The stable long-run level K.'],
    ['Stability test', 'Equilibrium y* stable if f′(y*) < 0.'],
    ['Euler\'s method', 'yₙ₊₁ = yₙ + h f(xₙ, yₙ).'],
]
