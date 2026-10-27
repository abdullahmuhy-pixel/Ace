"""Calculus II, module 2: Volumes, arc length and improper integrals."""
from verify import Q, x, sp
T1, T2, T3, T4 = ('Volumes by discs and washers', 'Volumes by cylindrical shells', 'Arc length and surface area', 'Improper integrals')
DI = lambda f, a, b: sp.integrate(f, (x, a, b))
pi = sp.pi

assert DI(pi * x, 0, 4) == 8 * pi
assert DI(pi * (x ** 2 - x ** 4), 0, 1) == 2 * pi / 15
assert DI(2 * pi * x * (2 * x - x ** 2), 0, 2) == 8 * pi / 3
assert DI(2 * pi * x * x ** 2, 0, 1) == pi / 2
assert sp.simplify(DI(sp.sqrt(1 + x), 0, 3) - sp.Rational(14, 3)) == 0
assert sp.simplify(DI(sp.sqrt(1 + sp.Rational(9, 4) * x), 0, 4) - sp.Rational(8, 27) * (10 * sp.sqrt(10) - 1)) == 0
assert sp.simplify(DI(2 * pi * x * sp.sqrt(2), 0, 1) - pi * sp.sqrt(2)) == 0
assert DI(x ** -2, 1, sp.oo) == 1 and DI(1 / sp.sqrt(x), 0, 1) == 2 and DI(sp.exp(-x), 0, sp.oo) == 1 and DI(1 / x, 1, sp.oo) == sp.oo

MODULE = {
    'title': 'Volumes, arc length and improper integrals',
    'topics': [T1, T2, T3, T4],
    'overview': 'Integration adds up thin slices. This module uses that idea to find volumes of solids of revolution, the length of curves and the area of curved surfaces, and then extends integrals to infinite intervals and to functions that blow up.',
    'key_terms': ['Solid of revolution', 'Disc', 'Washer', 'Cylindrical shell', 'Arc length', 'Surface area', 'Improper integral', 'Convergent', 'Divergent'],
    'explanation': [
        'Every application follows the same pattern: approximate a small piece (a thin disc, a thin shell, a short straight segment), write its size in terms of x and dx, and add the pieces with an integral. If you can draw the typical slice, you can write the integral.',
        'Discs and washers slice perpendicular to the axis of rotation; shells slice parallel to it. Choose whichever gives a simpler integral, usually the one that avoids solving for x in terms of y.',
        'An improper integral has an infinite limit or an integrand that becomes infinite. It is defined as a limit. If the limit is a finite number the integral converges; otherwise it diverges. The p-integrals ∫₁^∞ 1/xᵖ dx are the benchmark: they converge exactly when p > 1.'],
    'quick_facts': [
        'Disc: V = π∫r² dx; washer: V = π∫(R² − r²) dx.',
        'Shell: V = 2π∫(radius)(height) dx.',
        'Arc length: L = ∫√(1 + (dy/dx)²) dx.',
        'Surface area about the x-axis: S = 2π∫y√(1 + (dy/dx)²) dx.',
        '∫₁^∞ dx/xᵖ converges if p > 1; ∫₀¹ dx/xᵖ converges if p < 1.'],
}

NOTES = {
    T1: {
        'overview': 'Rotating a region about an axis sweeps out a solid. Slicing it perpendicular to the axis gives circular discs, or washers if there is a hole, and integrating their areas gives the volume.',
        'key_terms': ['Axis of rotation', 'Disc', 'Washer', 'Outer radius R', 'Inner radius r'],
        'explanation': [
            'If the region under y = f(x) from a to b is rotated about the x-axis, each thin slice is a disc of radius f(x) and thickness dx, with volume π[f(x)]² dx. So V = π∫ₐᵇ [f(x)]² dx.',
            'If the region lies between two curves, the slice is a washer: a disc with a hole. With outer radius R(x) and inner radius r(x), V = π∫(R² − r²) dx. Note this is R² − r², not (R − r)².',
            'For rotation about the y-axis, slice horizontally and integrate in y, with radii written as functions of y. For a different axis, such as y = −1, measure each radius as a distance from that line.'],
        'formulas_label': 'Formulas',
        'formulas': ['Disc: V = π∫ₐᵇ [f(x)]² dx', 'Washer: V = π∫ₐᵇ (R² − r²) dx', 'About the y-axis: V = π∫ [g(y)]² dy', 'Radius = distance from the axis'],
        'steps': ['Sketch the region and the axis.', 'Draw a typical slice perpendicular to the axis.', 'Write the outer and inner radii.', 'Find the limits where the curves meet.', 'Integrate π(R² − r²).'],
        'worked_example': {
            'problem': 'The region between y = x and y = x² for 0 ≤ x ≤ 1 is rotated about the x-axis. Find the volume.',
            'steps': ['On [0, 1], x ≥ x², so the outer radius is R = x and the inner radius is r = x².', 'V = π∫₀¹ (x² − x⁴) dx.', '= π[x³/3 − x⁵/5]₀¹ = π(1/3 − 1/5) = 2π/15.'],
            'answer': 'V = 2π/15 ≈ 0.419 cubic units.',
            'check': 'The cone from rotating y = x alone has volume π/3 ≈ 1.05; removing the inner solid leaves less, which fits.'},
        'mistakes': ['Using (R − r)² instead of R² − r².', 'Forgetting π.', 'Swapping the outer and inner radius and getting a negative volume.', 'Measuring the radius from the x-axis when the axis is y = k.'],
        'real_world': 'Manufacturers compute the volume of turned parts (vases, bottles, nozzles) this way from the profile curve, and use it for material cost and capacity.',
        'exam_strategy': 'Draw one typical washer with R and r labelled. Many examiners award a mark for the correct integral even before it is evaluated.',
        'recap': ['Slice perpendicular to the axis.', 'Disc: π∫f²; washer: π∫(R² − r²).', 'Radius = distance from the axis.', 'Check with a known shape.']},
    T2: {
        'overview': 'The shell method slices parallel to the axis of rotation. Each slice becomes a thin cylindrical shell, which often avoids having to solve for x in terms of y.',
        'key_terms': ['Cylindrical shell', 'Shell radius', 'Shell height', 'Thickness', 'Choice of method'],
        'explanation': [
            'Rotate a thin vertical strip at position x about the y-axis. It sweeps out a shell with radius x, height f(x) and thickness dx. Unrolled, the shell is roughly a flat sheet of size 2πx by f(x) by dx, so its volume is 2πx f(x) dx.',
            'Adding the shells gives V = 2π∫ₐᵇ x f(x) dx for rotation about the y-axis. For a region between two curves, the height is top minus bottom. For an axis x = k, the radius is |x − k|.',
            'Use shells when the washer method would need inverse functions. Rotating y = 2x − x² about the y-axis by washers would require solving a quadratic for x; with shells it is one polynomial integral.'],
        'formulas_label': 'Formulas',
        'formulas': ['About the y-axis: V = 2π∫ₐᵇ x f(x) dx', 'General: V = 2π∫(radius)(height) dx', 'Axis x = k: radius = |x − k|', 'Height = top curve − bottom curve'],
        'steps': ['Sketch the region and draw a strip parallel to the axis.', 'Write the shell radius (distance to the axis).', 'Write the shell height.', 'Integrate 2π × radius × height.'],
        'worked_example': {
            'problem': 'The region under y = 2x − x² and above the x-axis is rotated about the y-axis. Find the volume.',
            'steps': ['The curve meets the axis at x = 0 and x = 2.', 'Radius x, height 2x − x², so V = 2π∫₀² x(2x − x²) dx = 2π∫₀² (2x² − x³) dx.', '= 2π[2x³/3 − x⁴/4]₀² = 2π(16/3 − 4) = 8π/3.'],
            'answer': 'V = 8π/3 ≈ 8.38 cubic units.',
            'check': 'The washer method would need x in terms of y from a quadratic, a sign that shells were the right choice.'},
        'mistakes': ['Using π instead of 2π.', 'Using the height as the radius.', 'Integrating in y with vertical strips.', 'Forgetting to subtract the lower curve in the height.'],
        'real_world': 'Shells model anything built in concentric layers, such as the volume of material in a tree trunk or a coiled cable drum.',
        'exam_strategy': 'If a question lets you choose, say which method you are using and why ("shells avoid solving for x"). It shows understanding and earns credit.',
        'recap': ['Strip parallel to the axis.', 'V = 2π∫(radius)(height).', 'Radius = distance to the axis.', 'Choose the method that avoids inverses.']},
    T3: {
        'overview': 'Arc length adds up tiny straight segments along a curve. Rotating those segments gives the area of a curved surface.',
        'key_terms': ['Arc length', 'Differential ds', 'Surface of revolution', 'Smooth curve'],
        'explanation': [
            'A short piece of curve is close to a straight segment with horizontal change dx and vertical change dy. By Pythagoras its length is ds = √(dx² + dy²) = √(1 + (dy/dx)²) dx. Adding them gives L = ∫ₐᵇ √(1 + (f′(x))²) dx.',
            'Only special curves give integrals you can do by hand; most need numerical methods. Exam questions are built so that 1 + (f′)² is a perfect square or simplifies, for example y = (2/3)x^(3/2), where 1 + (f′)² = 1 + x.',
            'Rotating the curve about the x-axis, each segment sweeps a thin band of circumference 2πy and width ds. So the surface area is S = 2π∫ y √(1 + (f′)²) dx. For a sphere of radius r this formula gives 4πr².'],
        'formulas_label': 'Formulas',
        'formulas': ['L = ∫ₐᵇ √(1 + (dy/dx)²) dx', 'Parametric: L = ∫√((dx/dt)² + (dy/dt)²) dt', 'S = 2π∫ₐᵇ y √(1 + (dy/dx)²) dx', 'ds = √(1 + (dy/dx)²) dx'],
        'steps': ['Differentiate y.', 'Square the derivative and add 1.', 'Simplify the square root if you can.', 'Integrate between the limits.', 'For surface area, multiply by 2πy first.'],
        'worked_example': {
            'problem': 'Find the length of y = (2/3)x^(3/2) from x = 0 to x = 3.',
            'steps': ['dy/dx = x^(1/2), so 1 + (dy/dx)² = 1 + x.', 'L = ∫₀³ √(1 + x) dx = [(2/3)(1 + x)^(3/2)]₀³.', '= (2/3)(8 − 1) = 14/3.'],
            'answer': 'L = 14/3 ≈ 4.67.',
            'check': 'The straight line from (0, 0) to (3, 2√3 ≈ 3.46) has length √(9 + 12) ≈ 4.58, slightly less than the curve, as it must be.'},
        'mistakes': ['Forgetting the 1 under the square root.', 'Writing √(1 + f′) instead of √(1 + (f′)²).', 'Using 2πx instead of 2πy for rotation about the x-axis.', 'Taking √(a + b) = √a + √b.'],
        'real_world': 'Arc length gives the length of cable needed for a hanging power line or suspension bridge, whose shape is a catenary curve.',
        'exam_strategy': 'Simplify 1 + (f′)² fully before integrating; a perfect square is usually hidden there on purpose.',
        'recap': ['ds = √(1 + (f′)²) dx.', 'L = ∫ds.', 'S = 2π∫y ds about the x-axis.', 'A curve is never shorter than the chord.']},
    T4: {
        'overview': 'An improper integral has an infinite interval or an integrand that becomes infinite. It is defined as a limit, and it either converges to a number or diverges.',
        'key_terms': ['Improper integral', 'Convergent', 'Divergent', 'p-integral', 'Comparison test', 'Vertical asymptote'],
        'explanation': [
            '∫ₐ^∞ f(x) dx means the limit of ∫ₐᵗ f(x) dx as t → ∞. If the limit exists and is finite, the integral converges. ∫₁^∞ 1/x² dx = lim(1 − 1/t) = 1, so an infinitely long region can have a finite area.',
            'If f becomes infinite at a point in the interval, split the integral there and take a one-sided limit. ∫₀¹ 1/√x dx = lim(2 − 2√t) as t → 0⁺ = 2, which converges. But ∫₀¹ 1/x dx diverges.',
            'The p-integrals are the benchmark. ∫₁^∞ dx/xᵖ converges if and only if p > 1, and ∫₀¹ dx/xᵖ converges if and only if p < 1. The comparison test then decides harder cases: if 0 ≤ f ≤ g and ∫g converges, so does ∫f; if ∫f diverges, so does ∫g.'],
        'formulas_label': 'Definitions',
        'formulas': ['∫ₐ^∞ f dx = lim(t→∞) ∫ₐᵗ f dx', '∫₁^∞ dx/xᵖ: converges iff p > 1 (value 1/(p − 1))', '∫₀¹ dx/xᵖ: converges iff p < 1', '∫₀^∞ e^(−ax) dx = 1/a for a > 0'],
        'steps': ['Identify the problem point (an infinite limit or an asymptote).', 'Replace it with t and write the limit.', 'Integrate normally.', 'Take the limit and decide: converges or diverges.', 'For harder integrands, compare with a p-integral.'],
        'worked_example': {
            'problem': 'Decide whether ∫₁^∞ 1/x² dx and ∫₁^∞ 1/x dx converge.',
            'steps': ['∫₁ᵗ x⁻² dx = 1 − 1/t → 1 as t → ∞, so the first converges to 1.', '∫₁ᵗ 1/x dx = ln t → ∞ as t → ∞, so the second diverges.', 'These are p-integrals with p = 2 > 1 and p = 1, matching the rule.'],
            'answer': '∫₁^∞ 1/x² dx = 1 (converges); ∫₁^∞ 1/x dx diverges.',
            'check': '1/x² falls to zero much faster than 1/x, which is why the area under it stays finite.'},
        'mistakes': ['Treating ∞ as a number and substituting it directly.', 'Missing an asymptote inside the interval, such as ∫₋₁¹ 1/x² dx.', 'Thinking "the function goes to zero" is enough for convergence (1/x is the counterexample).', 'Reversing the p-test conditions for the two kinds of improper integral.'],
        'real_world': 'Improper integrals give the escape velocity of a rocket (the work to move it from the Earth\'s surface to infinity is finite) and the total probability under distributions such as the exponential and the normal.',
        'exam_strategy': 'Always write the limit explicitly with t. Writing "= 1/∞ = 0" loses the method mark even when the final answer is right.',
        'recap': ['Improper means an infinite limit or an infinite integrand.', 'Define it with a limit.', 'p-test: p > 1 at infinity, p < 1 near 0.', 'Compare with a known integral.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The region under y = √x for 0 ≤ x ≤ 4 is rotated about the x-axis. The volume is:', ['8π', '16π', '4π', '32π/3'], 0, 'π∫₀⁴ x dx = π × 8.', ans=DI(pi * x, 0, 4)),
    Q(T1, 'The region between y = x and y = x² (0 ≤ x ≤ 1) is rotated about the x-axis. The volume is:', ['2π/15', 'π/6', 'π/30', '2π/3'], 0, 'π∫₀¹ (x² − x⁴) dx = π(1/3 − 1/5).', ans=DI(pi * (x ** 2 - x ** 4), 0, 1)),
    Q(T1, 'For a washer with outer radius R and inner radius r, the slice area is:', ['π(R² − r²)', 'π(R − r)²', '2π(R − r)', 'πR² + πr²'], 0, 'Area of the big disc minus the hole.'),
    Q(T1, 'Rotating y = x for 0 ≤ x ≤ 3 about the x-axis gives a cone. Its volume is:', ['9π', '27π', '3π', '18π'], 0, 'π∫₀³ x² dx = π × 9, matching (1/3)πr²h = (1/3)π(9)(3).', ans=DI(pi * x ** 2, 0, 3)),
    Q(T1, 'The region under y = 1 for 0 ≤ x ≤ 2 is rotated about y = −1. The radius of a slice is:', ['2', '1', '3', '0'], 0, 'The distance from y = 1 to the axis y = −1 is 2.'),
    Q(T1, 'Rotating y = eˣ for 0 ≤ x ≤ 1 about the x-axis gives volume:', ['π(e² − 1)/2', 'π(e − 1)', 'π(e² − 1)', 'πe²/2'], 0, 'π∫₀¹ e²ˣ dx = π[e²ˣ/2]₀¹.', ans=DI(pi * sp.exp(2 * x), 0, 1)),
    # T2
    Q(T2, 'The region under y = 2x − x² is rotated about the y-axis. By shells the volume is:', ['8π/3', '16π/15', '4π/3', '8π'], 0, '2π∫₀² x(2x − x²) dx = 2π(16/3 − 4).', ans=DI(2 * pi * x * (2 * x - x ** 2), 0, 2)),
    Q(T2, 'The region under y = x² for 0 ≤ x ≤ 1 is rotated about the y-axis. The volume is:', ['π/2', 'π/5', 'π/4', 'π'], 0, '2π∫₀¹ x · x² dx = 2π/4.', ans=DI(2 * pi * x ** 3, 0, 1)),
    Q(T2, 'The shell-method volume element for rotation about the y-axis is:', ['2πx f(x) dx', 'π[f(x)]² dx', '2πf(x) dx', 'πx² dx'], 0, 'Circumference 2πx × height f(x) × thickness dx.'),
    Q(T2, 'Rotating about the line x = 3 with vertical strips at position x (x < 3), the shell radius is:', ['3 − x', 'x', 'x − 3', '3'], 0, 'The radius is the distance from x to the axis x = 3.'),
    Q(T2, 'When is the shell method usually easier than washers for rotation about the y-axis?', ['When y = f(x) is hard to solve for x', 'When the region is a rectangle', 'When rotating about the x-axis', 'Never'], 0, 'Shells integrate in x and need no inverse function.'),
    Q(T2, 'The region under y = 1/x for 1 ≤ x ≤ 3 is rotated about the y-axis. The volume is:', ['4π', '2π', '2π ln 3', '6π'], 0, '2π∫₁³ x(1/x) dx = 2π × 2.', ans=DI(2 * pi * x / x, 1, 3)),
    # T3
    Q(T3, 'The length of y = (2/3)x^(3/2) from 0 to 3 is:', ['14/3', '7/3', '2√3', '16/3'], 0, '∫₀³ √(1 + x) dx = (2/3)(8 − 1).', ans=sp.Rational(14, 3)),
    Q(T3, 'The arc-length integrand for y = f(x) is:', ['√(1 + (f′(x))²)', '√(1 + f′(x))', '1 + (f′(x))²', '√(1 + f(x)²)'], 0, 'From ds² = dx² + dy².'),
    Q(T3, 'The length of y = 2x + 1 from x = 0 to x = 3 is:', ['3√5', '9', '√10', '6'], 0, '∫₀³ √(1 + 4) dx = 3√5, the length of the straight segment.', ans=3 * sp.sqrt(5)),
    Q(T3, 'Rotating y = x (0 ≤ x ≤ 1) about the x-axis gives a surface area of:', ['√2 π', '2π', '√2 π/2', '2√2 π'], 0, '2π∫₀¹ x√2 dx = √2 π.', ans=pi * sp.sqrt(2)),
    Q(T3, 'The length of y = x^(3/2) from 0 to 4 is:', ['(8/27)(10√10 − 1)', '(8/27)(10√10)', '8', '(4/9)(10√10 − 1)'], 0, '1 + (3/2 x^(1/2))² = 1 + 9x/4; integrate to (8/27)(1 + 9x/4)^(3/2).', ans=sp.Rational(8, 27) * (10 * sp.sqrt(10) - 1)),
    Q(T3, 'Applying S = 2π∫y ds to a sphere of radius r gives:', ['4πr²', '2πr²', 'πr²', '(4/3)πr³'], 0, 'For y = √(r² − x²), y ds = r dx, so S = 2π∫₋ᵣʳ r dx = 4πr².'),
    # T4
    Q(T4, '∫₁^∞ 1/x² dx =', ['1', '∞ (diverges)', '1/2', '2'], 0, 'lim(1 − 1/t) = 1.', ans=DI(x ** -2, 1, sp.oo)),
    Q(T4, 'Which integral diverges?', ['∫₁^∞ 1/x dx', '∫₁^∞ 1/x² dx', '∫₀^∞ e^(−x) dx', '∫₀¹ 1/√x dx'], 0, 'ln t → ∞. The others converge to 1, 1 and 2.'),
    Q(T4, '∫₀¹ 1/√x dx =', ['2', '1', '∞ (diverges)', '1/2'], 0, 'lim(2 − 2√t) as t → 0⁺ = 2; here p = 1/2 < 1.', ans=DI(1 / sp.sqrt(x), 0, 1)),
    Q(T4, '∫₀^∞ e^(−2x) dx =', ['1/2', '2', '1', '∞'], 0, 'lim[−e^(−2x)/2] from 0 to t = 1/2.', ans=DI(sp.exp(-2 * x), 0, sp.oo)),
    Q(T4, '∫₁^∞ dx/xᵖ converges when:', ['p > 1', 'p ≥ 1', 'p < 1', 'p > 0'], 0, 'At p = 1 it is the divergent ∫1/x.'),
    Q(T4, 'Why is ∫₋₁¹ 1/x² dx improper?', ['The integrand is infinite at x = 0, inside the interval', 'The limits are infinite', 'The function is negative', 'It is not improper'], 0, 'Split at 0: each half diverges, so the integral diverges (it is not −2).'),
]

FLASH = [
    ['Disc method', 'V = π∫[f(x)]² dx.'],
    ['Washer method', 'V = π∫(R² − r²) dx.'],
    ['Shell method', 'V = 2π∫(radius)(height) dx.'],
    ['Arc length', 'L = ∫√(1 + (dy/dx)²) dx.'],
    ['Surface area (x-axis)', 'S = 2π∫y√(1 + (dy/dx)²) dx.'],
    ['Improper integral', 'Defined as a limit; converges if the limit is finite.'],
    ['p-test at infinity', '∫₁^∞ dx/xᵖ converges iff p > 1.'],
    ['p-test near 0', '∫₀¹ dx/xᵖ converges iff p < 1.'],
]
