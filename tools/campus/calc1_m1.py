"""Calculus I, module 1: Functions and limits."""
from verify import Q, x, h, sp

T1, T2, T3, T4 = ('Functions, domains and inverses', 'Limits and the limit laws',
                  'One-sided limits, infinite limits and asymptotes', 'Continuity and the Intermediate Value Theorem')

MODULE = {
    'title': 'Functions and limits',
    'topics': [T1, T2, T3, T4],
    'overview': 'Calculus is the mathematics of change, and every idea in it rests on the limit. This module makes sure your function skills are solid, then builds limits from the intuitive idea of "getting closer" to the laws you use to compute them, and finishes with continuity.',
    'key_terms': ['Function', 'Domain', 'Range', 'Composite function', 'Inverse function', 'Limit', 'One-sided limit', 'Asymptote', 'Continuity', 'Intermediate Value Theorem'],
    'explanation': [
        'A limit describes the value a function approaches as the input approaches some number, whether or not the function is actually defined there. That small shift, from "the value at" to "the value near", is what lets calculus talk about instantaneous speed and exact areas.',
        'Most limits you meet in a first course are computed with a few algebraic moves: substitute directly, and if that gives 0/0, factorise, rationalise or use a standard limit such as sin x / x → 1 before substituting again.',
        'Continuity ties the two ideas together. A function is continuous at a point when its limit there equals its value there, and continuous functions have useful guarantees such as the Intermediate Value Theorem.'],
    'quick_facts': [
        'Direct substitution works for polynomials and for rational functions wherever the denominator is not zero.',
        '0/0 is not an answer. It is a sign that more algebra is needed.',
        'lim x→0 (sin x)/x = 1 only when x is measured in radians.',
        'A two-sided limit exists only when both one-sided limits exist and are equal.',
        'Polynomials, eˣ, sin x and cos x are continuous for every real x.'],
}

NOTES = {
    T1: {
        'overview': 'A function assigns exactly one output to each input. Before you can differentiate anything, you need to read a function quickly: where it is defined, what values it can take, how functions combine, and when a function can be reversed.',
        'key_terms': ['Function', 'Domain', 'Range', 'Composite function f∘g', 'One-to-one', 'Inverse function f⁻¹', 'Even function', 'Odd function'],
        'explanation': [
            'The domain is the set of inputs the function accepts. In a first calculus course the domain is the largest set of real numbers for which the formula makes sense, so you remove anything that would divide by zero, take an even root of a negative number, or take the logarithm of a number that is not positive.',
            'The composite f∘g means "do g first, then f": (f∘g)(x) = f(g(x)). Order matters, and f(g(x)) is usually different from g(f(x)). Composites are the reason the chain rule exists, so it pays to see the inner and outer function in any formula.',
            'A function has an inverse only if it is one-to-one, meaning no two inputs give the same output. On a graph this is the horizontal line test. To find the inverse, write y = f(x), swap x and y, and solve for y. The graph of f⁻¹ is the reflection of the graph of f in the line y = x.',
            'Symmetry saves work. f is even when f(−x) = f(x), so its graph is symmetric about the y-axis (x², cos x). f is odd when f(−x) = −f(x), so its graph has rotational symmetry about the origin (x³, sin x).'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['(f∘g)(x) = f(g(x))', 'f(f⁻¹(x)) = x and f⁻¹(f(x)) = x', 'Even: f(−x) = f(x)    Odd: f(−x) = −f(x)', '√(expression) needs expression ≥ 0; ln(expression) needs expression > 0'],
        'steps': ['List every operation in the formula that has a restriction (division, even roots, logarithms).', 'Write the condition each one imposes and solve the inequalities.', 'Combine the conditions to state the domain, using interval notation.', 'For an inverse: check one-to-one, write y = f(x), swap x and y, solve for y.', 'Check your inverse by confirming f(f⁻¹(x)) = x.'],
        'worked_example': {
            'problem': 'Find the domain of f(x) = √(x − 3)/(x − 5) and the inverse of g(x) = (3x − 1)/2.',
            'steps': ['The square root needs x − 3 ≥ 0, so x ≥ 3.', 'The denominator needs x − 5 ≠ 0, so x ≠ 5.', 'Domain of f: [3, 5) ∪ (5, ∞).', 'For g, write y = (3x − 1)/2 and swap: x = (3y − 1)/2.', 'Solve: 2x = 3y − 1, so y = (2x + 1)/3.'],
            'answer': 'Domain of f is [3, 5) ∪ (5, ∞); g⁻¹(x) = (2x + 1)/3.',
            'check': 'g(g⁻¹(x)) = (3·(2x + 1)/3 − 1)/2 = (2x + 1 − 1)/2 = x. ✓'},
        'mistakes': ['Writing x > 3 instead of x ≥ 3: a square root of zero is allowed.', 'Treating f∘g as g∘f. Always work from the inside out.', 'Confusing f⁻¹(x) with 1/f(x). The inverse undoes f; the reciprocal does not.', 'Forgetting to check one-to-one before inverting x². You must restrict the domain first.'],
        'real_world': 'Exchange-rate conversions are inverse functions. If a bank turns pounds into naira with one formula, the formula that turns naira back into pounds (before fees) is its inverse.',
        'exam_strategy': 'Domain questions are quick marks: list restrictions in a column before combining them. For inverse questions, always finish with a one-line check that f(f⁻¹(x)) = x.',
        'recap': ['Domain: remove division by zero, negative even roots and non-positive logarithms.', 'f∘g means apply g first.', 'Inverse: swap x and y, then solve for y.', 'Even functions mirror in the y-axis; odd functions rotate about the origin.']},
    T2: {
        'overview': 'The limit lim x→a f(x) = L says that f(x) can be made as close to L as you like by taking x close enough to a, without x being equal to a. This topic turns that idea into a toolkit for computing limits.',
        'key_terms': ['Limit', 'Limit laws', 'Direct substitution', 'Indeterminate form 0/0', 'Factorising', 'Rationalising', 'Squeeze theorem'],
        'explanation': [
            'The value of f at a does not matter to the limit. The function (x² − 9)/(x − 3) is undefined at x = 3, yet as x gets close to 3 the outputs get close to 6. The limit captures that behaviour.',
            'The limit laws say limits respect arithmetic: the limit of a sum is the sum of the limits, and the same holds for differences, products, constant multiples and quotients (when the bottom limit is not zero). These laws are why direct substitution works for polynomials and rational functions where they are defined.',
            'When substitution gives 0/0, the expression hides a common factor. Factorise and cancel, or multiply by the conjugate when a square root is involved, then substitute again. The standard limit lim x→0 (sin x)/x = 1 handles many trigonometric cases.',
            'The squeeze theorem handles functions trapped between two others. If g(x) ≤ f(x) ≤ h(x) near a and both g and h tend to L, then f tends to L too. It is how we show x² sin(1/x) → 0 as x → 0.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['lim [f(x) ± g(x)] = lim f(x) ± lim g(x)', 'lim [f(x)·g(x)] = lim f(x) · lim g(x)', 'lim x→0 (sin x)/x = 1 (x in radians)', 'lim x→0 (sin kx)/x = k', 'a² − b² = (a − b)(a + b) for factorising and rationalising'],
        'steps': ['Try direct substitution first.', 'If you get a number, that is the limit (as long as the function is built from continuous pieces).', 'If you get 0/0, factorise and cancel, or multiply top and bottom by the conjugate.', 'If trigonometry is involved, rearrange towards (sin u)/u.', 'Substitute again and state the limit.'],
        'worked_example': {
            'problem': 'Evaluate lim x→4 (√x − 2)/(x − 4).',
            'steps': ['Direct substitution gives (2 − 2)/(4 − 4) = 0/0, so more work is needed.', 'Multiply top and bottom by the conjugate √x + 2.', 'Top: (√x − 2)(√x + 2) = x − 4.', 'So the expression becomes (x − 4)/((x − 4)(√x + 2)) = 1/(√x + 2) for x ≠ 4.', 'Substitute x = 4: 1/(2 + 2) = 1/4.'],
            'answer': 'The limit is 1/4.',
            'check': 'Try x = 4.01: (√4.01 − 2)/0.01 ≈ 0.2498, very close to 0.25. ✓'},
        'mistakes': ['Writing "= 0/0" as a final answer.', 'Cancelling terms that are added rather than factors, for example cancelling x in (x + 3)/x.', 'Using lim (sin x)/x = 1 with x in degrees.', 'Assuming the limit equals f(a) when f is not continuous at a.'],
        'real_world': 'A car\'s speedometer shows a limit. Average speed over shorter and shorter time intervals approaches the instantaneous speed, which is exactly the limit you will meet again in the derivative.',
        'exam_strategy': 'Write the result of direct substitution first, even if it is 0/0. Examiners award a method mark for recognising the indeterminate form and another for the correct algebraic step.',
        'recap': ['A limit is about values near a, not at a.', 'Substitute first; 0/0 means factorise or rationalise.', 'lim x→0 (sin x)/x = 1 in radians.', 'The squeeze theorem traps a function between two that share a limit.']},
    T3: {
        'overview': 'Some functions behave differently on each side of a point, and some grow without bound. One-sided and infinite limits describe these behaviours precisely and give you the asymptotes of a graph.',
        'key_terms': ['Left-hand limit', 'Right-hand limit', 'Infinite limit', 'Vertical asymptote', 'Limit at infinity', 'Horizontal asymptote', 'Dominant term'],
        'explanation': [
            'lim x→a⁻ f(x) is the value approached as x comes up to a from below, and lim x→a⁺ f(x) the value approached from above. The ordinary two-sided limit exists exactly when these two agree. For f(x) = |x|/x, the left-hand limit at 0 is −1 and the right-hand limit is 1, so the two-sided limit does not exist.',
            'If f(x) grows without bound as x → a, we write lim f(x) = ∞ (or −∞). The line x = a is then a vertical asymptote. For a rational function in lowest terms, vertical asymptotes sit where the denominator is zero. Check the sign of the expression just to the left and right to decide between +∞ and −∞.',
            'Limits at infinity describe end behaviour. For a rational function, divide top and bottom by the highest power of x in the denominator. If the degrees are equal, the limit is the ratio of the leading coefficients; if the top has lower degree, the limit is 0; if the top has higher degree, there is no horizontal asymptote.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['lim x→a f(x) = L ⇔ lim x→a⁻ f(x) = L and lim x→a⁺ f(x) = L', 'lim x→∞ 1/xⁿ = 0 for n > 0', 'Equal degrees: horizontal asymptote y = (leading coefficient of top)/(leading coefficient of bottom)', 'Vertical asymptote at x = a when the reduced denominator is 0 at a'],
        'steps': ['For a one-sided limit, picture or test values just on that side of a.', 'For a vertical asymptote, cancel common factors, then find zeros of the denominator.', 'Decide the sign of the function on each side to choose +∞ or −∞.', 'For limits at infinity, divide every term by the highest power of x in the denominator.', 'Let each 1/xⁿ term go to 0 and read off the limit.'],
        'worked_example': {
            'problem': 'Find the horizontal and vertical asymptotes of f(x) = (3x² + 1)/(2x² − 8).',
            'steps': ['Top and bottom are both degree 2, so divide by x²: (3 + 1/x²)/(2 − 8/x²).', 'As x → ±∞ this tends to 3/2, so y = 3/2 is the horizontal asymptote.', 'Denominator 2x² − 8 = 2(x − 2)(x + 2) is zero at x = 2 and x = −2.', 'The numerator is never zero, so nothing cancels.', 'Vertical asymptotes: x = 2 and x = −2.'],
            'answer': 'Horizontal asymptote y = 3/2; vertical asymptotes x = 2 and x = −2.',
            'check': 'f(100) = 30001/19992 ≈ 1.5007, close to 1.5. ✓'},
        'mistakes': ['Saying a two-sided limit exists when the one-sided limits differ.', 'Placing a vertical asymptote where a factor cancels. That is a hole, not an asymptote.', 'Dividing by the highest power of the numerator instead of the denominator, then misreading the result.', 'Writing "∞" without checking the sign on each side.'],
        'real_world': 'Average cost per item, total cost ÷ number made, falls towards a horizontal asymptote as production grows: the fixed costs are shared over more items until only the variable cost per item is left.',
        'exam_strategy': 'For asymptote questions, factorise the denominator first and cancel any common factors. Then state vertical asymptotes as equations (x = 2), not just numbers.',
        'recap': ['Two-sided limit exists only when left and right agree.', 'Vertical asymptotes: zeros of the reduced denominator.', 'Equal degrees give y = ratio of leading coefficients.', 'Lower degree on top gives y = 0.']},
    T4: {
        'overview': 'A function is continuous at a point when you can draw its graph through that point without lifting your pen. Continuity is the condition that makes limits easy and that powers the Intermediate Value Theorem.',
        'key_terms': ['Continuous at a point', 'Removable discontinuity', 'Jump discontinuity', 'Infinite discontinuity', 'Piecewise function', 'Intermediate Value Theorem (IVT)'],
        'explanation': [
            'f is continuous at a when three things hold: f(a) is defined, lim x→a f(x) exists, and the two are equal. If any of the three fails, f has a discontinuity at a.',
            'Discontinuities come in three kinds. A removable discontinuity is a hole: the limit exists but f(a) is missing or wrong, and redefining one value fixes it. A jump discontinuity has different one-sided limits. An infinite discontinuity sits at a vertical asymptote.',
            'For a piecewise function, continuity at the joining point means the left piece and the right piece meet at the same height. Set the two expressions equal at the joining point and solve for any unknown constant.',
            'The Intermediate Value Theorem says that if f is continuous on [a, b] and N is between f(a) and f(b), then f(c) = N for some c in (a, b). Its most common use: if f(a) and f(b) have opposite signs, f has a root between a and b.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Continuous at a: lim x→a f(x) = f(a)', 'Piecewise join at x = a: left expression at a = right expression at a', 'IVT: f continuous on [a, b], f(a) < 0 < f(b) ⇒ f(c) = 0 for some c in (a, b)'],
        'steps': ['Check f(a) is defined.', 'Find the left-hand and right-hand limits at a.', 'Compare them with each other and with f(a).', 'Name the type of discontinuity if one of the conditions fails.', 'For IVT, confirm continuity on the closed interval, then evaluate f at both ends.'],
        'worked_example': {
            'problem': 'Find k so that f(x) = kx + 1 for x < 2 and f(x) = x² for x ≥ 2 is continuous at x = 2.',
            'steps': ['Right-hand value: f(2) = 2² = 4, and the right-hand limit is also 4.', 'Left-hand limit: lim x→2⁻ (kx + 1) = 2k + 1.', 'Continuity needs 2k + 1 = 4.', 'Solve: 2k = 3, so k = 3/2.'],
            'answer': 'k = 3/2.',
            'check': 'With k = 3/2 the left piece gives (3/2)(2) + 1 = 4 at x = 2, matching x² = 4. ✓'},
        'mistakes': ['Checking only that f(a) exists, without checking the limit.', 'Using the IVT on a function that is not continuous on the whole interval, for example 1/x on [−1, 1].', 'Thinking the IVT tells you where the root is. It only tells you that one exists.', 'Forgetting that a removable discontinuity is still a discontinuity until f(a) is redefined.'],
        'real_world': 'If the temperature at 6 am was 18 °C and at noon it was 31 °C, the IVT guarantees that at some moment in between it was exactly 25 °C, because temperature changes continuously.',
        'exam_strategy': 'When asked to "show that a root exists", write three lines: f is continuous on [a, b] (say why), f(a) and f(b) have opposite signs (show the numbers), therefore by the IVT a root lies in (a, b).',
        'recap': ['Continuity: defined, limit exists, limit equals value.', 'Removable, jump and infinite are the three discontinuities.', 'Piecewise: match the pieces at the join.', 'IVT: sign change on a continuous function gives a root.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'What is the domain of f(x) = √(x − 3)/(x − 5)?', ['x ≥ 3 and x ≠ 5', 'x > 3 and x ≠ 5', 'x ≥ 3', 'All real x except 5'], 0, 'The square root needs x − 3 ≥ 0, so x ≥ 3, and the denominator needs x ≠ 5. Together: [3, 5) ∪ (5, ∞).'),
    Q(T1, 'If f(x) = 2x + 1 and g(x) = x², find (f∘g)(2).', ['25', '9', '10', '17'], 1, '(f∘g)(2) = f(g(2)) = f(4) = 2(4) + 1 = 9. The value 25 is (g∘f)(2), the other order.', ans=9),
    Q(T1, 'Find the inverse of f(x) = (3x − 1)/2.', ['(2x + 1)/3', '(2x − 1)/3', '2/(3x − 1)', '(3x + 1)/2'], 0, 'Swap x and y: x = (3y − 1)/2, so 2x = 3y − 1 and y = (2x + 1)/3.', ans=(2*x + 1)/3),
    Q(T1, 'Find f⁻¹(x) for f(x) = 1/(x − 2).', ['1/(x + 2)', 'x − 2', '1/x + 2', '2 − 1/x'], 2, 'Swap: x = 1/(y − 2), so y − 2 = 1/x and y = 1/x + 2.', ans=1/x + 2),
    Q(T1, 'Which function is even?', ['f(x) = x³ − x', 'f(x) = x⁴ − 3x²', 'f(x) = x² + x', 'f(x) = sin x'], 1, 'f(−x) = (−x)⁴ − 3(−x)² = x⁴ − 3x² = f(x), so it is even. x³ − x and sin x are odd; x² + x is neither.'),
    Q(T1, 'What is the range of f(x) = x² + 4 for all real x?', ['y ≥ 0', 'y ≥ 4', 'y > 4', 'All real numbers'], 1, 'x² ≥ 0 for every real x, so x² + 4 ≥ 4, and the value 4 is reached at x = 0.'),
    Q(T1, 'Why does f(x) = x² (all real x) have no inverse?', ['It is not continuous', 'It fails the horizontal line test', 'Its range is all real numbers', 'It is an odd function'], 1, 'f(2) = f(−2) = 4, so it is not one-to-one. Restricting to x ≥ 0 gives the inverse √x.'),
    # T2
    Q(T2, 'Evaluate lim x→3 (x² − 9)/(x − 3).', ['0', '3', '6', '9'], 2, 'Factorise: (x − 3)(x + 3)/(x − 3) = x + 3 for x ≠ 3. Substitute: 3 + 3 = 6.', ans=6),
    Q(T2, 'Evaluate lim x→2 (3x² − x + 4).', ['10', '12', '14', '16'], 2, 'A polynomial, so substitute: 3(4) − 2 + 4 = 14.', ans=14),
    Q(T2, 'Evaluate lim x→4 (√x − 2)/(x − 4).', ['1/2', '1/4', '0', '4'], 1, 'Multiply by the conjugate: the expression becomes 1/(√x + 2), which is 1/4 at x = 4.', ans=sp.Rational(1, 4)),
    Q(T2, 'Evaluate lim h→0 ((2 + h)² − 4)/h.', ['0', '2', '4', '8'], 2, '(4 + 4h + h² − 4)/h = 4 + h, which tends to 4. This is the derivative of x² at x = 2.', ans=4),
    Q(T2, 'Evaluate lim x→0 sin(5x)/x.', ['1', '5', '1/5', '0'], 1, 'Write it as 5 · sin(5x)/(5x). As x → 0, sin(5x)/(5x) → 1, so the limit is 5.', ans=5),
    Q(T2, 'Evaluate lim x→1 (x³ − 1)/(x − 1).', ['1', '2', '3', '0'], 2, 'x³ − 1 = (x − 1)(x² + x + 1), so the expression is x² + x + 1, which is 3 at x = 1.', ans=3),
    Q(T2, 'What is lim x→0 x² sin(1/x)?', ['0', '1', 'It does not exist', '∞'], 0, 'Since −1 ≤ sin(1/x) ≤ 1, we have −x² ≤ x² sin(1/x) ≤ x². Both bounds tend to 0, so by the squeeze theorem the limit is 0.'),
    # T3
    Q(T3, 'Find lim x→0⁺ 1/x.', ['0', '1', '+∞', '−∞'], 2, 'For small positive x, 1/x is large and positive, so it grows without bound.', ans=sp.oo),
    Q(T3, 'Find lim x→2⁻ 1/(x − 2).', ['+∞', '−∞', '0', '1/2'], 1, 'Just to the left of 2, x − 2 is a small negative number, so 1/(x − 2) is large and negative.', ans=-sp.oo),
    Q(T3, 'For f(x) = |x|/x, what is lim x→0⁻ f(x)?', ['1', '−1', '0', 'It is undefined'], 1, 'For x < 0, |x| = −x, so f(x) = −x/x = −1.', ans=-1),
    Q(T3, 'Find the horizontal asymptote of f(x) = (3x² + 1)/(2x² − 5).', ['y = 0', 'y = 3', 'y = 3/2', 'There is none'], 2, 'Equal degrees, so the asymptote is the ratio of leading coefficients: 3/2.', ans=sp.Rational(3, 2)),
    Q(T3, 'Where are the vertical asymptotes of f(x) = (x + 1)/(x² − 4)?', ['x = 4 only', 'x = −1', 'x = 2 and x = −2', 'x = 2 only'], 2, 'x² − 4 = (x − 2)(x + 2) is zero at ±2, and neither zero cancels with the numerator.'),
    Q(T3, 'Evaluate lim x→∞ (5x³ − x)/(2x³ + 7).', ['5/2', '0', '5', '∞'], 0, 'Divide by x³: (5 − 1/x²)/(2 + 7/x³) → 5/2.', ans=sp.Rational(5, 2)),
    Q(T3, 'Evaluate lim x→∞ (2x + 1)/(x² + 3).', ['2', '0', '1/3', '∞'], 1, 'The top has lower degree than the bottom, so the fraction tends to 0.', ans=0),
    # T4
    Q(T4, 'Find k so that f(x) = kx + 1 (x < 2), f(x) = x² (x ≥ 2) is continuous at x = 2.', ['1', '3/2', '2', '5/2'], 1, 'Match the pieces at x = 2: 2k + 1 = 4, so k = 3/2.', ans=sp.Rational(3, 2)),
    Q(T4, 'What kind of discontinuity does f(x) = (x² − 1)/(x − 1) have at x = 1?', ['Removable', 'Jump', 'Infinite', 'None: it is continuous'], 0, 'The expression equals x + 1 for x ≠ 1, so the limit is 2, but f(1) is undefined. That is a hole: a removable discontinuity.'),
    Q(T4, 'What value should f(2) take so that f(x) = (x² − 4)/(x − 2) becomes continuous at 2?', ['0', '2', '4', '−4'], 2, 'For x ≠ 2, f(x) = x + 2, which tends to 4. Defining f(2) = 4 removes the hole.', ans=4),
    Q(T4, 'f(x) = x³ + x − 1. Which interval must contain a root?', ['(−1, 0)', '(0, 1)', '(1, 2)', '(2, 3)'], 1, 'f(0) = −1 < 0 and f(1) = 1 > 0. f is a polynomial, so it is continuous, and the IVT gives a root in (0, 1).'),
    Q(T4, 'Why can the IVT not be used to find a root of f(x) = 1/x on [−1, 1]?', ['f(−1) and f(1) have the same sign', 'f is not continuous on [−1, 1]', 'f has no inverse', 'The interval is too short'], 1, 'f is undefined at 0, which is inside the interval, so the continuity condition fails. In fact 1/x has no root at all.'),
    Q(T4, 'Which function is continuous for every real x?', ['tan x', '1/(x − 3)', 'x² + sin x', '√x'], 2, 'Polynomials and sin x are continuous everywhere, and so is their sum. tan x and 1/(x − 3) have asymptotes, and √x is undefined for x < 0.'),
]

FLASH = [
    ['Domain restrictions', 'No division by zero, no even roots of negatives, no logarithms of numbers ≤ 0.'],
    ['(f∘g)(x)', 'f(g(x)): apply g first, then f.'],
    ['Finding an inverse', 'Write y = f(x), swap x and y, solve for y. Check f(f⁻¹(x)) = x.'],
    ['lim x→0 (sin x)/x', '1, with x in radians.'],
    ['0/0 from substitution', 'Indeterminate. Factorise, rationalise or use a standard limit, then substitute again.'],
    ['Two-sided limit exists when…', 'both one-sided limits exist and are equal.'],
    ['Horizontal asymptote, equal degrees', 'y = ratio of the leading coefficients.'],
    ['Continuity at a', 'f(a) defined, the limit at a exists, and the limit equals f(a).'],
    ['Intermediate Value Theorem', 'Continuous on [a, b] with f(a), f(b) of opposite signs ⇒ a root in (a, b).'],
]
