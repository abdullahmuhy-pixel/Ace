"""Calculus I, module 3: Derivatives of special functions, implicit differentiation and related rates."""
from verify import Q, x, y, sp

D = lambda f: sp.diff(f, x)
T1, T2, T3, T4 = ('Derivatives of trigonometric functions', 'Exponential and logarithmic derivatives', 'Implicit differentiation', 'Related rates')

MODULE = {
    'title': 'More derivatives',
    'topics': [T1, T2, T3, T4],
    'overview': 'With the rules in place, this module adds the derivatives of the trigonometric, exponential and logarithmic functions, then shows how to differentiate equations that are not solved for y and how to link rates of change that depend on each other.',
    'key_terms': ['Radian measure', 'Natural exponential eˣ', 'Natural logarithm ln x', 'Implicit differentiation', 'Logarithmic differentiation', 'Related rates'],
    'explanation': [
        'The derivatives of sin x and cos x come from the standard limits lim (sin h)/h = 1 and lim (cos h − 1)/h = 0, which hold only in radians. Every other trigonometric derivative follows from these two using the quotient rule.',
        'The number e ≈ 2.71828 is chosen so that eˣ is its own derivative. Its inverse, ln x, then has derivative 1/x. With the chain rule these two results handle growth, decay and any expression with a variable exponent.',
        'Implicit differentiation treats y as an unknown function of x and differentiates both sides of an equation, attaching dy/dx every time y is differentiated. Related rates use the same idea with time as the variable.'],
    'quick_facts': [
        'd/dx sin x = cos x and d/dx cos x = −sin x (radians only).',
        'd/dx eˣ = eˣ and d/dx ln x = 1/x.',
        'd/dx aˣ = aˣ ln a.',
        'In implicit differentiation, d/dx (y²) = 2y·dy/dx.',
        'In related rates, substitute numbers only after differentiating.'],
}

NOTES = {
    T1: {
        'overview': 'The six trigonometric functions have derivatives you should know by heart. Combined with the chain rule, they let you differentiate any oscillating quantity: waves, alternating current, tides and seasons.',
        'key_terms': ['Radians', 'sin x and cos x', 'tan x', 'sec x, csc x, cot x', 'Standard trigonometric limits'],
        'explanation': [
            'd/dx sin x = cos x and d/dx cos x = −sin x. You can check the signs against the graphs: at x = 0, sin x is rising with slope 1, and cos 0 = 1; cos x is at its peak there, so its slope is 0 = −sin 0.',
            'The rest follow from the quotient rule. tan x = sin x/cos x gives (cos²x + sin²x)/cos²x = 1/cos²x = sec²x. In the same way d/dx sec x = sec x tan x, d/dx csc x = −csc x cot x and d/dx cot x = −csc²x. The functions starting with "c" all carry a minus sign.',
            'These formulas need x in radians. In degrees, d/dx sin x° = (π/180) cos x°, which is why calculus always works in radians. With the chain rule, d/dx sin(kx) = k cos(kx), and similar results hold for the other functions.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['d/dx sin x = cos x', 'd/dx cos x = −sin x', 'd/dx tan x = sec²x', 'd/dx sec x = sec x tan x', 'd/dx csc x = −csc x cot x', 'd/dx cot x = −csc²x'],
        'steps': ['Decide which rule is outermost: product, quotient or chain.', 'Replace each trigonometric function by its derivative from the table.', 'Multiply by the derivative of any inner function.', 'Simplify with identities such as sin²x + cos²x = 1 if useful.'],
        'worked_example': {
            'problem': 'Differentiate y = x tan x and find the slope of y = sin x + cos x at x = π/4.',
            'steps': ['Product rule on x tan x: (1)(tan x) + x(sec²x).', 'So dy/dx = tan x + x sec²x.', 'For y = sin x + cos x, dy/dx = cos x − sin x.', 'At x = π/4: cos(π/4) − sin(π/4) = √2/2 − √2/2 = 0.'],
            'answer': 'd/dx (x tan x) = tan x + x sec²x; the slope of sin x + cos x at π/4 is 0.',
            'check': 'sin x + cos x = √2 sin(x + π/4) has its maximum √2 at x = π/4, so a slope of 0 there is right. ✓'},
        'mistakes': ['Writing d/dx cos x = sin x, without the minus sign.', 'Working in degrees.', 'Forgetting the chain rule factor: d/dx sin(3x) = 3 cos(3x).', 'Confusing sec²x with sec(x²).'],
        'real_world': 'Mains electricity in most countries alternates as V = V₀ sin(2π·50t). Its derivative tells engineers how fast the voltage is changing, which matters for designing chargers and motors.',
        'exam_strategy': 'Learn the six derivatives as two groups: sin, tan, sec (positive) and cos, cot, csc (negative), with each "co-" function mirroring its partner.',
        'recap': ['sin → cos, cos → −sin.', 'tan → sec²; sec → sec tan.', 'The "co" functions take a minus sign.', 'Radians only.']},
    T2: {
        'overview': 'Exponentials model anything that grows or decays by a fixed percentage, and logarithms undo them. Their derivatives are simple, and they open the door to logarithmic differentiation for awkward products and powers.',
        'key_terms': ['e', 'eˣ', 'ln x', 'aˣ', 'logₐ x', 'Logarithmic differentiation', 'Exponential growth and decay'],
        'explanation': [
            'eˣ is the only exponential whose slope at every point equals its height: d/dx eˣ = eˣ. With the chain rule, d/dx e^(g(x)) = g′(x)e^(g(x)), so d/dx e^(3x) = 3e^(3x) and d/dx e^(x²) = 2x e^(x²).',
            'Because ln x is the inverse of eˣ, its derivative is 1/x for x > 0. With the chain rule, d/dx ln(g(x)) = g′(x)/g(x). Logarithm laws often simplify the work first: ln(x³√(x + 1)) = 3 ln x + (1/2) ln(x + 1).',
            'Other bases convert to e. Since aˣ = e^(x ln a), its derivative is aˣ ln a. Since logₐ x = ln x/ln a, its derivative is 1/(x ln a).',
            'For functions like xˣ, where the variable is in both the base and the exponent, neither the power rule nor the exponential rule applies. Take ln of both sides, differentiate implicitly and multiply back: this is logarithmic differentiation.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['d/dx eˣ = eˣ', 'd/dx e^(g(x)) = g′(x)e^(g(x))', 'd/dx ln x = 1/x', 'd/dx ln(g(x)) = g′(x)/g(x)', 'd/dx aˣ = aˣ ln a', 'ln(ab) = ln a + ln b, ln(aⁿ) = n ln a'],
        'steps': ['Simplify logarithms with the laws of logs before differentiating.', 'Apply the eˣ or ln x rule, multiplying by the derivative of the inside.', 'For variable bases and exponents, take ln of both sides.', 'Differentiate both sides, remembering (1/y)·dy/dx on the left.', 'Multiply through by y and substitute the original expression back.'],
        'worked_example': {
            'problem': 'Differentiate y = xˣ for x > 0.',
            'steps': ['Take logarithms: ln y = x ln x.', 'Differentiate both sides: (1/y) dy/dx = ln x + x · (1/x) = ln x + 1.', 'Multiply by y: dy/dx = y(ln x + 1).', 'Substitute back: dy/dx = xˣ(ln x + 1).'],
            'answer': 'dy/dx = xˣ(1 + ln x).',
            'check': 'At x = 1: y = 1 and the slope is 1 · (0 + 1) = 1. A numerical check, (1.001^1.001 − 1)/0.001 ≈ 1.001, agrees. ✓'},
        'mistakes': ['Using the power rule on eˣ, giving xeˣ⁻¹.', 'Forgetting the chain rule factor: d/dx e^(5x) = 5e^(5x), not e^(5x).', 'Writing d/dx ln(3x) = 1/(3x). The 3 cancels: it is 1/x.', 'Treating 2ˣ like x²: the derivative of 2ˣ is 2ˣ ln 2, not x·2ˣ⁻¹.'],
        'real_world': 'A savings account with continuously compounded interest holds A = P·e^(rt). Its derivative, rP·e^(rt) = rA, shows the balance grows at a rate proportional to itself, the defining feature of exponential growth.',
        'exam_strategy': 'If a logarithm contains a product, quotient or power, expand it with log laws first. It turns a messy quotient-rule question into a sum of simple terms.',
        'recap': ['eˣ is its own derivative.', 'ln x has derivative 1/x.', 'aˣ has derivative aˣ ln a.', 'Variable in base and exponent: use logarithmic differentiation.']},
    T3: {
        'overview': 'Some curves, such as circles, are given by an equation in x and y that is hard or impossible to solve for y. Implicit differentiation finds dy/dx directly from the equation.',
        'key_terms': ['Explicit function', 'Implicit equation', 'Implicit differentiation', 'dy/dx in terms of x and y', 'Tangent to an implicit curve'],
        'explanation': [
            'Treat y as a function of x that you cannot see. Differentiate both sides of the equation with respect to x. Any term containing only x is differentiated normally. Any term containing y uses the chain rule, so it picks up a factor dy/dx: d/dx (y³) = 3y²·dy/dx.',
            'Terms with both x and y need the product rule: d/dx (xy) = y + x·dy/dx. After differentiating, collect all dy/dx terms on one side, factorise and divide.',
            'The answer usually contains both x and y. To find the slope at a point, substitute both coordinates. Check that the point actually lies on the curve first.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['d/dx (yⁿ) = nyⁿ⁻¹·dy/dx', 'd/dx (xy) = y + x·dy/dx', 'd/dx (sin y) = cos y·dy/dx', 'Circle x² + y² = r²: dy/dx = −x/y'],
        'steps': ['Differentiate every term on both sides with respect to x.', 'Attach dy/dx each time you differentiate a y.', 'Move all dy/dx terms to one side and everything else to the other.', 'Factorise out dy/dx and divide.', 'Substitute the point to get a numerical slope.'],
        'worked_example': {
            'problem': 'Find the slope of the curve x² + xy + y² = 7 at the point (1, 2).',
            'steps': ['Check the point: 1 + 2 + 4 = 7 ✓.', 'Differentiate: 2x + (y + x·dy/dx) + 2y·dy/dx = 0.', 'Collect: dy/dx (x + 2y) = −2x − y.', 'So dy/dx = −(2x + y)/(x + 2y).', 'At (1, 2): dy/dx = −(2 + 2)/(1 + 4) = −4/5.'],
            'answer': 'The slope at (1, 2) is −4/5.',
            'check': 'Solving for y near x = 1 and differencing numerically gives a slope of about −0.8. ✓'},
        'mistakes': ['Forgetting the dy/dx on terms containing y.', 'Differentiating xy as x·dy/dx only, missing the product rule.', 'Differentiating the constant on the right as anything other than 0.', 'Substituting a point that is not on the curve.'],
        'real_world': 'Economists draw indifference curves such as xy = 100, where x and y are quantities of two goods. Implicit differentiation gives the slope, the rate at which a consumer will trade one good for the other.',
        'exam_strategy': 'Write the differentiated equation in full before rearranging. Many marks are lost by rearranging in your head and dropping a dy/dx term.',
        'recap': ['Differentiate both sides with respect to x.', 'Every y term gets a dy/dx.', 'Use the product rule on xy terms.', 'Collect, factorise, divide.']},
    T4: {
        'overview': 'In a related rates problem two or more quantities change with time and are linked by an equation. Knowing how fast one changes, you find how fast another changes at a particular moment.',
        'key_terms': ['Rate of change with respect to time', 'dV/dt, dr/dt', 'Linking equation', 'Implicit differentiation in t', 'Instant of interest'],
        'explanation': [
            'Every quantity that changes is a function of time t. Write an equation that links them, such as V = (4/3)πr³ for a balloon. Differentiate both sides with respect to t using the chain rule: dV/dt = 4πr²·dr/dt.',
            'Substitute the values at the instant you care about only after differentiating. If you put in r = 5 before differentiating, r becomes a constant and its rate of change disappears.',
            'Draw a diagram, label the changing lengths with letters (not numbers), and list what you know and what you want, each as a derivative with units. Signs matter: a quantity that is decreasing has a negative rate.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Chain rule in time: d/dt f(r) = f′(r)·dr/dt', 'Sphere: V = (4/3)πr³, A = 4πr²', 'Circle: A = πr²', 'Cone: V = (1/3)πr²h', 'Pythagoras: x² + y² = z²'],
        'steps': ['Draw and label a diagram with variables for every changing quantity.', 'Write the given rate and the wanted rate as derivatives with units.', 'Find an equation linking the variables.', 'Differentiate both sides with respect to t.', 'Substitute the values at the instant and solve for the unknown rate.'],
        'worked_example': {
            'problem': 'A spherical balloon is inflated at 100 cm³/s. How fast is the radius increasing when the radius is 5 cm?',
            'steps': ['Given dV/dt = 100 cm³/s. Want dr/dt when r = 5.', 'Link: V = (4/3)πr³.', 'Differentiate in t: dV/dt = 4πr²·dr/dt.', 'Substitute: 100 = 4π(25)·dr/dt = 100π·dr/dt.', 'So dr/dt = 1/π ≈ 0.318 cm/s.'],
            'answer': 'The radius is increasing at 1/π ≈ 0.32 cm/s.',
            'check': 'Units: (cm³/s)/(cm²) = cm/s. ✓ The rate is small because the surface area 100π cm² is large.'},
        'mistakes': ['Substituting the given value before differentiating.', 'Ignoring the sign of a decreasing quantity.', 'Leaving out units, or mixing cm and m.', 'Using an equation that only holds at one instant, instead of one that holds at all times.'],
        'real_world': 'Air-traffic controllers use related rates: from a plane\'s speed and height, the rate at which its distance from a radar station changes follows from Pythagoras differentiated in time.',
        'exam_strategy': 'Set out "Given", "Find" and "When" lines before any calculus. Examiners award marks for the correct linking equation and its derivative even if the final arithmetic slips.',
        'recap': ['Everything that changes is a function of t.', 'Link the variables, then differentiate in t.', 'Substitute values last.', 'Rates have units and signs.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Differentiate y = x tan x.', ['tan x + x sec²x', 'sec²x', 'x sec²x', 'tan x + sec²x'], 0, 'Product rule: (1)tan x + x(sec²x).', ans=D(x*sp.tan(x))),
    Q(T1, 'Differentiate y = cos(3x).', ['−sin(3x)', '−3 sin(3x)', '3 sin(3x)', 'sin(3x)'], 1, 'd/dx cos u = −sin u · u′, with u′ = 3.', ans=D(sp.cos(3*x))),
    Q(T1, 'The derivative of sec x is:', ['sec x tan x', 'sec²x', '−csc x cot x', 'tan²x'], 0, 'Write sec x = 1/cos x. The quotient rule gives sin x/cos²x = sec x tan x.', ans=D(sp.sec(x))),
    Q(T1, 'The derivative of cot x is:', ['csc²x', '−csc²x', '−sec²x', '−cot x csc x'], 1, 'cot x = cos x/sin x gives (−sin²x − cos²x)/sin²x = −csc²x.', ans=D(sp.cot(x))),
    Q(T1, 'What is the slope of y = sin x + cos x at x = π/4?', ['√2', '0', '1', '−√2'], 1, 'dy/dx = cos x − sin x, which is √2/2 − √2/2 = 0 at π/4.', ans=0),
    Q(T1, 'Differentiate y = sin x cos x.', ['cos²x − sin²x', '−sin x cos x', 'cos²x + sin²x', '2 sin x cos x'], 0, 'Product rule: cos x · cos x + sin x · (−sin x) = cos²x − sin²x, which equals cos 2x.', ans=D(sp.sin(x)*sp.cos(x))),
    Q(T1, 'Why must x be in radians for d/dx sin x = cos x?', ['Because sin x is periodic', 'Because lim h→0 (sin h)/h = 1 only in radians', 'Because degrees are not real numbers', 'It works equally well in degrees'], 1, 'The derivation uses lim (sin h)/h = 1, which is true only for h in radians. In degrees an extra factor π/180 appears.'),
    # T2
    Q(T2, 'Differentiate y = e^(3x).', ['e^(3x)', '3e^(3x)', '3xe^(3x − 1)', 'e^(3x)/3'], 1, 'Chain rule: e^(3x) times the derivative of 3x, which is 3.', ans=D(sp.exp(3*x))),
    Q(T2, 'Differentiate y = e^(x²).', ['2xe^(x²)', 'e^(x²)', 'x²e^(x² − 1)', '2e^(x²)'], 0, 'Inner function x² has derivative 2x.', ans=D(sp.exp(x**2))),
    Q(T2, 'Differentiate y = ln(3x).', ['1/(3x)', '3/x', '1/x', 'ln 3/x'], 2, 'Chain rule: 3/(3x) = 1/x. Or note ln(3x) = ln 3 + ln x.', ans=D(sp.log(3*x))),
    Q(T2, 'Differentiate y = ln(x² + 1).', ['1/(x² + 1)', '2x/(x² + 1)', '2x ln(x² + 1)', '2/(x² + 1)'], 1, 'd/dx ln g = g′/g, with g′ = 2x.', ans=D(sp.log(x**2 + 1))),
    Q(T2, 'Differentiate y = 2ˣ.', ['x·2ˣ⁻¹', '2ˣ', '2ˣ ln 2', '2ˣ/ln 2'], 2, '2ˣ = e^(x ln 2), so the derivative is ln 2 · 2ˣ.', ans=D(2**x)),
    Q(T2, 'Differentiate y = xˣ (x > 0).', ['x·xˣ⁻¹', 'xˣ ln x', 'xˣ(1 + ln x)', 'xˣ'], 2, 'ln y = x ln x, so y′/y = ln x + 1 and y′ = xˣ(1 + ln x).', ans=D(x**x)),
    Q(T2, 'Differentiate y = x²eˣ.', ['2xeˣ', 'eˣ(x² + 2x)', 'x²eˣ', '2xeˣ + eˣ'], 1, 'Product rule: 2x·eˣ + x²·eˣ = eˣ(x² + 2x).', ans=D(x**2*sp.exp(x))),
    # T3
    Q(T3, 'For the circle x² + y² = 25, dy/dx equals:', ['−x/y', 'x/y', '−y/x', '2x + 2y'], 0, '2x + 2y·dy/dx = 0, so dy/dx = −x/y.'),
    Q(T3, 'Find the slope of x² + xy + y² = 7 at (1, 2).', ['−4/5', '4/5', '−5/4', '−1'], 0, '2x + y + x·y′ + 2y·y′ = 0 gives y′ = −(2x + y)/(x + 2y) = −4/5 at (1, 2).', ans=sp.Rational(-4, 5)),
    Q(T3, 'If y³ + x = 9, then dy/dx =', ['−1/(3y²)', '1/(3y²)', '−3y²', '(9 − x)/3'], 0, '3y²·dy/dx + 1 = 0, so dy/dx = −1/(3y²).'),
    Q(T3, 'Differentiate xy = 6 implicitly. dy/dx =', ['−y/x', 'y/x', '−x/y', '6/x'], 0, 'Product rule: y + x·dy/dx = 0, so dy/dx = −y/x.'),
    Q(T3, 'Find the slope of the circle x² + y² = 25 at (3, 4).', ['3/4', '−3/4', '−4/3', '4/3'], 1, 'dy/dx = −x/y = −3/4.', ans=sp.Rational(-3, 4)),
    Q(T3, 'If sin y = x, what is dy/dx?', ['cos y', '1/cos y', '−1/sin y', 'sin y'], 1, 'cos y·dy/dx = 1, so dy/dx = 1/cos y. This is how the derivative of arcsin x is found.'),
    # T4
    Q(T4, 'A balloon\'s volume grows at 100 cm³/s. How fast is the radius growing when r = 5 cm?', ['1/π cm/s', '4π cm/s', '1/(4π) cm/s', '100/π cm/s'], 0, 'dV/dt = 4πr²·dr/dt, so 100 = 100π·dr/dt and dr/dt = 1/π cm/s.', ans=1/sp.pi),
    Q(T4, 'The radius of a circle grows at 2 cm/s. How fast is the area growing when r = 10 cm?', ['20π cm²/s', '40π cm²/s', '4π cm²/s', '200π cm²/s'], 1, 'A = πr², so dA/dt = 2πr·dr/dt = 2π(10)(2) = 40π cm²/s.', ans=40*sp.pi),
    Q(T4, 'A 10 m ladder slides down a wall. Its foot moves away at 1 m/s. How fast does the top slide down when the foot is 6 m from the wall?', ['3/4 m/s', '4/3 m/s', '1 m/s', '6/10 m/s'], 0, 'x² + y² = 100 gives 2x·x′ + 2y·y′ = 0. With x = 6, y = 8 and x′ = 1: y′ = −6/8 = −3/4, so the top slides down at 3/4 m/s.', ans=sp.Rational(3, 4)),
    Q(T4, 'A cube\'s edge grows at 0.5 cm/s. How fast is its volume growing when the edge is 4 cm?', ['8 cm³/s', '24 cm³/s', '48 cm³/s', '32 cm³/s'], 1, 'V = s³, so dV/dt = 3s²·ds/dt = 3(16)(0.5) = 24 cm³/s.', ans=24),
    Q(T4, 'In a related rates problem, when should you substitute the values at the given instant?', ['Before writing the linking equation', 'Before differentiating', 'After differentiating', 'It makes no difference'], 2, 'Substituting first turns a changing quantity into a constant, so its rate would wrongly become 0.'),
    Q(T4, 'A square\'s side shrinks at 3 cm/s. How fast is the area changing when the side is 5 cm?', ['−30 cm²/s', '30 cm²/s', '−15 cm²/s', '−75 cm²/s'], 0, 'A = s², so dA/dt = 2s·ds/dt = 2(5)(−3) = −30 cm²/s. The area is decreasing.', ans=-30),
]

FLASH = [
    ['d/dx sin x', 'cos x'], ['d/dx cos x', '−sin x'], ['d/dx tan x', 'sec²x'], ['d/dx sec x', 'sec x tan x'],
    ['d/dx eˣ', 'eˣ'], ['d/dx ln x', '1/x (x > 0)'], ['d/dx aˣ', 'aˣ ln a'],
    ['Implicit differentiation', 'Differentiate both sides in x; every y term picks up dy/dx.'],
    ['Logarithmic differentiation', 'Take ln of both sides, differentiate implicitly, multiply by y.'],
    ['Related rates order', 'Link the variables, differentiate in t, then substitute the instant.'],
]
