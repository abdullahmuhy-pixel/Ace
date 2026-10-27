"""Calculus II, module 5: Differential equations, parametric curves and polar coordinates."""
from verify import Q, x, t, sp
T1, T2, T3, T4 = ('Separable differential equations', 'First-order linear equations', 'Parametric curves', 'Polar coordinates')
th = sp.Symbol('theta')
y = sp.Function('y')

s1 = sp.dsolve(sp.Eq(y(x).diff(x), 2 * x * y(x)), y(x), ics={y(0): 3}).rhs
assert sp.simplify(s1 - 3 * sp.exp(x ** 2)) == 0 and s1.subs(x, 1) == 3 * sp.E
s2 = sp.dsolve(sp.Eq(y(x).diff(x) + 2 * y(x), 4), y(x), ics={y(0): 0}).rhs
assert sp.simplify(s2 - 2 * (1 - sp.exp(-2 * x))) == 0
s3 = sp.dsolve(sp.Eq(y(x).diff(x) + y(x) / x, x), y(x)).rhs
assert sp.simplify(sp.diff(s3, x) + s3 / x - x) == 0
assert sp.integrate((1 + sp.cos(th)) ** 2 / 2, (th, 0, 2 * sp.pi)) == 3 * sp.pi / 2
assert sp.integrate((2 * sp.cos(th)) ** 2 / 2, (th, -sp.pi / 2, sp.pi / 2)) == sp.pi
assert sp.integrate(sp.sqrt(sp.diff(sp.cos(t), t) ** 2 + sp.diff(sp.sin(t), t) ** 2), (t, 0, 2 * sp.pi)) == 2 * sp.pi

MODULE = {
    'title': 'Differential equations, parametric curves and polar coordinates',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module applies the integration skills of the course in two new settings. Differential equations describe how a quantity changes, and solving them predicts its future. Parametric and polar curves describe motion and shapes that are awkward or impossible to write as y = f(x).',
    'key_terms': ['Differential equation', 'Separable', 'Initial condition', 'Integrating factor', 'Exponential growth', 'Parametric equations', 'Polar coordinates', 'Cardioid'],
    'explanation': [
        'A differential equation links a function with its derivatives. A separable equation dy/dx = g(x)h(y) is solved by moving all the y terms to one side and the x terms to the other, then integrating both sides. A first-order linear equation dy/dx + P(x)y = Q(x) is solved by multiplying by an integrating factor. An initial condition picks the one solution you need from the family of solutions.',
        'Parametric equations x = f(t), y = g(t) trace a curve as t changes, like the position of a moving object at time t. Slopes come from dy/dx = (dy/dt)/(dx/dt) and lengths from ∫√((dx/dt)² + (dy/dt)²) dt.',
        'Polar coordinates (r, θ) locate a point by its distance from the origin and its angle. Circles centred at the origin, spirals and flower-shaped curves have simple polar equations. Area in polar form is A = ½∫r² dθ, because thin slices are sectors rather than rectangles.'],
    'quick_facts': [
        'Separable: ∫dy/h(y) = ∫g(x) dx.',
        'dP/dt = kP ⇒ P = P₀e^(kt).',
        'Linear: integrating factor μ = e^(∫P dx), then (μy)′ = μQ.',
        'Parametric slope: dy/dx = (dy/dt)/(dx/dt).',
        'x = r cos θ, y = r sin θ; polar area A = ½∫r² dθ.'],
}

NOTES = {
    T1: {
        'overview': 'A separable differential equation can be rearranged so all the y terms are on one side and all the x terms on the other. Integrating both sides gives the solution.',
        'key_terms': ['Differential equation', 'Separable', 'General solution', 'Particular solution', 'Initial condition', 'Exponential growth and decay'],
        'explanation': [
            'For dy/dx = g(x)h(y), write dy/h(y) = g(x) dx and integrate: ∫dy/h(y) = ∫g(x) dx + C. One constant is enough, because constants from both sides combine. Then solve for y if possible and use the initial condition to find C.',
            'The most important case is dy/dt = ky, meaning the rate of change is proportional to the amount present. The solution is y = y₀e^(kt): growth if k > 0 (populations, compound interest) and decay if k < 0 (radioactivity, drug clearance). The half-life is ln 2 / |k|.',
            'Newton\'s law of cooling dT/dt = −k(T − Tₛ) is also separable, giving T = Tₛ + (T₀ − Tₛ)e^(−kt). The temperature approaches the surroundings Tₛ exponentially.'],
        'formulas_label': 'Formulas',
        'formulas': ['dy/dx = g(x)h(y) ⇒ ∫dy/h(y) = ∫g(x) dx', 'dy/dt = ky ⇒ y = y₀e^(kt)', 'Half-life = ln 2 / |k|; doubling time = ln 2 / k', 'Cooling: T = Tₛ + (T₀ − Tₛ)e^(−kt)'],
        'steps': ['Separate: all y with dy, all x with dx.', 'Integrate both sides; add one constant.', 'Solve for y if you can.', 'Use the initial condition to find C.', 'Check by substituting back.'],
        'worked_example': {
            'problem': 'Solve dy/dx = 2xy with y(0) = 3.',
            'steps': ['Separate: dy/y = 2x dx.', 'Integrate: ln|y| = x² + C, so y = Ae^(x²).', 'y(0) = A = 3.'],
            'answer': 'y = 3e^(x²).',
            'check': 'dy/dx = 3e^(x²) × 2x = 2x y ✓, and y(0) = 3 ✓.'},
        'mistakes': ['Adding a constant to only one side and then forgetting it.', 'Writing e^(x² + C) as e^(x²) + C instead of Ae^(x²).', 'Losing the solution y = 0 when dividing by y.', 'Using the initial condition before integrating.'],
        'real_world': 'Doctors use exponential decay to set drug doses: if a drug\'s half-life is 6 hours, they can calculate when the level in the blood drops below the effective amount and the next dose is due.',
        'exam_strategy': 'Show the separated form as its own line before integrating. It is usually worth a mark, even if the integration goes wrong later.',
        'recap': ['Separate, integrate, then find C.', 'One constant is enough.', 'dy/dt = ky gives exponential growth or decay.', 'Check by substituting back.']},
    T2: {
        'overview': 'A first-order linear equation has the form dy/dx + P(x)y = Q(x). Multiplying by an integrating factor turns the left side into the derivative of a product, which can be integrated directly.',
        'key_terms': ['Linear equation', 'Standard form', 'Integrating factor', 'Product rule', 'Steady state'],
        'explanation': [
            'First write the equation in standard form, with the coefficient of dy/dx equal to 1. The integrating factor is μ(x) = e^(∫P dx); there is no need for a constant in this integral.',
            'Multiplying through by μ gives μy′ + μPy = μQ, and the left side is exactly (μy)′ by the product rule. Integrate: μy = ∫μQ dx + C, then divide by μ.',
            'Linear equations model inflow and outflow, such as a tank of salt water or the current in a circuit. The solution usually splits into a steady state (what happens in the long run) and a transient term that dies away.'],
        'formulas_label': 'Method',
        'formulas': ['Standard form: dy/dx + P(x)y = Q(x)', 'μ(x) = e^(∫P(x) dx)', '(μy)′ = μQ', 'y = (1/μ)(∫μQ dx + C)'],
        'steps': ['Put the equation in standard form.', 'Compute μ = e^(∫P dx).', 'Multiply through and write the left side as (μy)′.', 'Integrate both sides and include C.', 'Divide by μ and apply the initial condition.'],
        'worked_example': {
            'problem': 'Solve dy/dx + 2y = 4 with y(0) = 0.',
            'steps': ['P = 2, so μ = e^(2x).', '(e^(2x)y)′ = 4e^(2x), so e^(2x)y = 2e^(2x) + C and y = 2 + Ce^(−2x).', 'y(0) = 2 + C = 0, so C = −2.'],
            'answer': 'y = 2(1 − e^(−2x)).',
            'check': 'As x → ∞, y → 2, which is where dy/dx = 0 in the original equation (2y = 4) ✓.'},
        'mistakes': ['Finding μ before putting the equation in standard form.', 'Forgetting to multiply Q by μ.', 'Adding C after dividing by μ (it must be divided too).', 'Writing μ = e^P instead of e^(∫P dx).'],
        'real_world': 'In an electric circuit with a resistor and an inductor, the current obeys L di/dt + Ri = V. Its solution shows the current rising smoothly to V/R, which engineers use to design switching circuits.',
        'exam_strategy': 'Write "μ = e^(∫P dx) = …" explicitly, and show the step (μy)′ = μQ. These two lines carry most of the method marks.',
        'recap': ['Standard form first.', 'μ = e^(∫P dx).', '(μy)′ = μQ; integrate.', 'Divide by μ, including C.']},
    T3: {
        'overview': 'Parametric equations give x and y separately as functions of a parameter t. They describe motion and curves that are not graphs of functions, such as circles and loops.',
        'key_terms': ['Parameter', 'Parametric equations', 'Eliminating the parameter', 'Parametric derivative', 'Arc length', 'Velocity'],
        'explanation': [
            'x = cos t, y = sin t for 0 ≤ t ≤ 2π traces the unit circle anticlockwise. Eliminating the parameter (here using cos²t + sin²t = 1) gives the Cartesian equation x² + y² = 1, but the parametric form also tells you direction and speed.',
            'The slope is dy/dx = (dy/dt)/(dx/dt), provided dx/dt ≠ 0. The curve has a horizontal tangent where dy/dt = 0 and a vertical tangent where dx/dt = 0. The second derivative is d²y/dx² = (d/dt(dy/dx))/(dx/dt).',
            'Arc length is L = ∫√((dx/dt)² + (dy/dt)²) dt. For the unit circle this is ∫₀^(2π) 1 dt = 2π, the circumference. If t is time, √((dx/dt)² + (dy/dt)²) is the speed.'],
        'formulas_label': 'Formulas',
        'formulas': ['dy/dx = (dy/dt)/(dx/dt)', 'd²y/dx² = [d/dt(dy/dx)] / (dx/dt)', 'L = ∫√((dx/dt)² + (dy/dt)²) dt', 'Horizontal tangent: dy/dt = 0; vertical: dx/dt = 0'],
        'steps': ['Differentiate x and y with respect to t.', 'Divide to get dy/dx.', 'Substitute the value of t for a particular point.', 'For a length, integrate the speed.'],
        'worked_example': {
            'problem': 'For x = t², y = t³, find dy/dx at t = 2 and the tangent line there.',
            'steps': ['dx/dt = 2t and dy/dt = 3t², so dy/dx = 3t²/(2t) = 3t/2.', 'At t = 2: dy/dx = 3, and the point is (4, 8).', 'Tangent: y − 8 = 3(x − 4), so y = 3x − 4.'],
            'answer': 'dy/dx = 3 at (4, 8); tangent y = 3x − 4.',
            'check': 'Eliminating t gives y = x^(3/2) for t ≥ 0, with dy/dx = (3/2)x^(1/2) = (3/2)(2) = 3 at x = 4 ✓.'},
        'mistakes': ['Computing (dx/dt)/(dy/dt) instead of (dy/dt)/(dx/dt).', 'Using the parameter value as the x-coordinate.', 'Taking d²y/dx² as d/dt(dy/dx) without dividing by dx/dt.', 'Forgetting the curve may trace part of itself twice.'],
        'real_world': 'Projectile motion is parametric: x = v cos α t, y = v sin α t − ½gt². Game engines and ballistics software move objects frame by frame with exactly these equations.',
        'exam_strategy': 'Write the point (x, y) as well as the t-value before writing a tangent line. Using t in place of x is the most common lost mark.',
        'recap': ['dy/dx = (dy/dt)/(dx/dt).', 'Find (x, y) from t first.', 'Arc length integrates the speed.', 'Eliminate t for the Cartesian equation.']},
    T4: {
        'overview': 'Polar coordinates describe a point by its distance r from the origin and its angle θ from the positive x-axis. Many curves, including circles, spirals and cardioids, have much simpler equations in polar form.',
        'key_terms': ['Polar coordinates', 'Pole', 'Conversion', 'Cardioid', 'Rose curve', 'Polar area'],
        'explanation': [
            'Convert with x = r cos θ, y = r sin θ, r² = x² + y² and tan θ = y/x (choose θ in the right quadrant). The point (2, π/3) in polar form is (1, √3) in Cartesian form. One point has many polar names: (r, θ) and (r, θ + 2π) are the same point.',
            'Standard curves: r = a is a circle about the origin; θ = c is a line through the origin; r = 2a cos θ is a circle through the origin with centre (a, 0); r = a(1 + cos θ) is a heart-shaped cardioid; r = cos(nθ) is a rose.',
            'Area uses thin sectors of area ½r²dθ, so A = ½∫ r² dθ between the angles that trace the region once. The cardioid r = 1 + cos θ has area ½∫₀^(2π) (1 + cos θ)² dθ = 3π/2.'],
        'formulas_label': 'Formulas',
        'formulas': ['x = r cos θ, y = r sin θ', 'r² = x² + y², tan θ = y/x', 'Area: A = ½∫ₐᵇ r² dθ', 'r = 2a cos θ: circle, centre (a, 0), radius a'],
        'steps': ['Sketch the curve or make a table of r for key angles.', 'Find the angles that trace the region exactly once.', 'Set up ½∫r² dθ.', 'Expand and use double-angle identities to integrate.'],
        'worked_example': {
            'problem': 'Find the area enclosed by the cardioid r = 1 + cos θ.',
            'steps': ['The curve is traced once for 0 ≤ θ ≤ 2π.', 'A = ½∫₀^(2π) (1 + 2cos θ + cos²θ) dθ.', '∫cos θ over a full turn is 0 and ∫cos²θ = π, so A = ½(2π + 0 + π) = 3π/2.'],
            'answer': 'A = 3π/2 ≈ 4.71.',
            'check': 'The cardioid fits inside a circle of radius 2 (area 4π ≈ 12.6) and contains the unit circle (π ≈ 3.14) ✓.'},
        'mistakes': ['Forgetting the ½ in the area formula.', 'Using limits that trace the curve twice (r = 2cos θ is traced once for −π/2 ≤ θ ≤ π/2).', 'Taking θ = arctan(y/x) in the wrong quadrant.', 'Integrating r instead of r².'],
        'real_world': 'Radar and sonar report positions as a distance and a bearing, which are polar coordinates. Microphone pickup patterns are cardioids, which is where the name "cardioid microphone" comes from.',
        'exam_strategy': 'Always state the θ-limits with a reason, such as "the loop is traced once as θ goes from 0 to 2π". Wrong limits are the most common error in polar area questions.',
        'recap': ['x = r cos θ, y = r sin θ.', 'Learn the standard polar curves.', 'Area = ½∫r² dθ.', 'Choose limits that trace the region once.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Solve dy/dx = 2xy with y(0) = 3.', ['y = 3e^(x²)', 'y = 3e^(2x)', 'y = x² + 3', 'y = 3 + e^(x²)'], 0, 'dy/y = 2x dx gives ln|y| = x² + C, so y = Ae^(x²) with A = 3.', ans=s1),
    Q(T1, 'For y = 3e^(x²), what is y(1)?', ['3e', 'e³', '3', '3e²'], 0, '3e¹ = 3e.', ans=3 * sp.E),
    Q(T1, 'A population doubles every 5 years under dP/dt = kP. What is k?', ['ln 2 / 5', '5 ln 2', '2/5', 'ln 5 / 2'], 0, 'e^(5k) = 2 gives k = ln 2 / 5 ≈ 0.139.', ans=sp.log(2) / 5),
    Q(T1, 'Which equation is separable?', ['dy/dx = x²y', 'dy/dx = x + y', 'dy/dx = sin(xy)', 'dy/dx = x − y²x + y'], 0, 'x²y is a function of x times a function of y.'),
    Q(T1, 'A substance decays with k = −0.1 per year. What is its half-life, to 2 d.p.?', ['6.93 years', '10.00 years', '0.69 years', '5.00 years'], 0, 'ln 2 / 0.1 ≈ 6.93.'),
    Q(T1, 'The general solution of dy/dx = x/y is:', ['y² = x² + C', 'y = x + C', 'y = Cx', 'y² = x + C'], 0, 'y dy = x dx gives y²/2 = x²/2 + C, i.e. y² = x² + C.'),
    # T2
    Q(T2, 'The integrating factor for dy/dx + 2y = 4 is:', ['e^(2x)', 'e^(4x)', '2x', 'e^(−2x)'], 0, 'μ = e^(∫2 dx) = e^(2x).', ans=sp.exp(2 * x)),
    Q(T2, 'Solve dy/dx + 2y = 4 with y(0) = 0.', ['y = 2(1 − e^(−2x))', 'y = 4(1 − e^(−2x))', 'y = 2e^(−2x)', 'y = 2 + e^(−2x)'], 0, 'y = 2 + Ce^(−2x), and y(0) = 0 gives C = −2.', ans=s2),
    Q(T2, 'The integrating factor for dy/dx + y/x = x (x > 0) is:', ['x', '1/x', 'e^x', 'ln x'], 0, 'μ = e^(∫(1/x) dx) = e^(ln x) = x.', ans=x),
    Q(T2, 'The general solution of dy/dx + y/x = x (x > 0) is:', ['y = x²/3 + C/x', 'y = x²/2 + C', 'y = x³/3 + C', 'y = Cx + x²'], 0, '(xy)′ = x², so xy = x³/3 + C.'),
    Q(T2, 'Before finding μ for 2 dy/dx + 6y = 8, you should:', ['divide by 2 to get dy/dx + 3y = 4', 'use μ = e^(6x)', 'separate the variables', 'differentiate both sides'], 0, 'The coefficient of dy/dx must be 1 (standard form).'),
    Q(T2, 'For dy/dx + 2y = 4, the long-run (steady-state) value of y is:', ['2', '4', '0', '8'], 0, 'Set dy/dx = 0: 2y = 4.', ans=2),
    # T3
    Q(T3, 'For x = t², y = t³, dy/dx =', ['3t/2', '2/(3t)', '3t²', '2t'], 0, '(3t²)/(2t) = 3t/2.', ans=3 * t / 2),
    Q(T3, 'For x = t², y = t³, the slope at t = 2 is:', ['3', '6', '12', '2/3'], 0, '3(2)/2 = 3.', ans=3),
    Q(T3, 'x = cos t, y = sin t, 0 ≤ t ≤ 2π traces:', ['the unit circle', 'a line', 'a parabola', 'the curve y = x'], 0, 'cos²t + sin²t = 1.'),
    Q(T3, 'The length of x = cos t, y = sin t for 0 ≤ t ≤ 2π is:', ['2π', 'π', '4π', '1'], 0, 'The speed √(sin²t + cos²t) = 1, integrated over 2π.', ans=2 * sp.pi),
    Q(T3, 'A parametric curve has a vertical tangent where:', ['dx/dt = 0 and dy/dt ≠ 0', 'dy/dt = 0', 'dy/dx = 0', 't = 0'], 0, 'dy/dx = (dy/dt)/(dx/dt) is undefined there.'),
    Q(T3, 'Eliminating t from x = 2t + 1, y = 4t gives:', ['y = 2x − 2', 'y = 2x + 1', 'y = x − 1', 'y = 4x'], 0, 't = (x − 1)/2, so y = 2(x − 1).'),
    # T4
    Q(T4, 'The polar point (2, π/3) in Cartesian form is:', ['(1, √3)', '(√3, 1)', '(2, 1)', '(1, 2)'], 0, 'x = 2cos(π/3) = 1 and y = 2sin(π/3) = √3.'),
    Q(T4, 'The polar area formula is:', ['A = ½∫r² dθ', 'A = ∫r dθ', 'A = ∫r² dθ', 'A = π∫r² dθ'], 0, 'Each thin sector has area ½r² dθ.'),
    Q(T4, 'The area enclosed by r = 1 + cos θ is:', ['3π/2', 'π', '2π', '3π'], 0, '½∫₀^(2π) (1 + cos θ)² dθ = ½(2π + π).', ans=3 * sp.pi / 2),
    Q(T4, 'r = 2 cos θ is:', ['a circle with centre (1, 0) and radius 1', 'a circle with centre (0, 0) and radius 2', 'a cardioid', 'a line'], 0, 'r² = 2r cos θ gives x² + y² = 2x, i.e. (x − 1)² + y² = 1.'),
    Q(T4, 'The area enclosed by r = 2 cos θ is:', ['π', '2π', '4π', 'π/2'], 0, '½∫ from −π/2 to π/2 of 4cos²θ dθ = π, the area of a unit circle.', ans=sp.pi),
    Q(T4, 'The Cartesian point (−1, 1) has polar angle θ (0 ≤ θ < 2π):', ['3π/4', '−π/4', 'π/4', '7π/4'], 0, 'It is in the second quadrant; tan θ = −1 there gives 3π/4.'),
]

FLASH = [
    ['Separable equation', 'Separate dy and dx, integrate both sides, add one constant.'],
    ['Exponential model', 'dy/dt = ky ⇒ y = y₀e^(kt).'],
    ['Half-life', 'ln 2 / |k|.'],
    ['Integrating factor', 'μ = e^(∫P dx) for dy/dx + Py = Q; then (μy)′ = μQ.'],
    ['Parametric slope', 'dy/dx = (dy/dt)/(dx/dt).'],
    ['Parametric arc length', '∫√((dx/dt)² + (dy/dt)²) dt.'],
    ['Polar to Cartesian', 'x = r cos θ, y = r sin θ, r² = x² + y².'],
    ['Polar area', 'A = ½∫r² dθ over angles that trace the region once.'],
]
