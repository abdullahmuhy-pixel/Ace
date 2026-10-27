"""Calculus II, module 1: Techniques of integration."""
from verify import Q, x, sp
T1, T2, T3, T4 = ('Integration by parts', 'Trigonometric integrals', 'Trigonometric substitution', 'Partial fractions')
I = lambda f: sp.integrate(f, x)
DI = lambda f, a, b: sp.integrate(f, (x, a, b))


def anti(F, f):
    """Assert F is an antiderivative of f (checked by differentiating)."""
    assert sp.simplify(sp.diff(F, x) - f) == 0, (F, f)


# every antiderivative quoted in the notes and the unparsed options, checked by differentiation
anti(x * sp.sin(x) + sp.cos(x), x * sp.cos(x))
anti(sp.exp(x) * (x - 1), x * sp.exp(x))
anti(x * sp.log(x) - x, sp.log(x))
anti(x ** 2 * sp.log(x) / 2 - x ** 2 / 4, x * sp.log(x))
anti(sp.exp(x) * (sp.sin(x) - sp.cos(x)) / 2, sp.exp(x) * sp.sin(x))
anti(sp.sin(x) ** 3 / 3, sp.sin(x) ** 2 * sp.cos(x))
anti(x / 2 - sp.sin(2 * x) / 4, sp.sin(x) ** 2)
anti(sp.sin(x) - sp.sin(x) ** 3 / 3, sp.cos(x) ** 3)
anti(sp.tan(x) - x, sp.tan(x) ** 2)
anti(sp.asin(x / 3), 1 / sp.sqrt(9 - x ** 2))
anti(sp.atan(x / 2) / 2, 1 / (x ** 2 + 4))
anti(-sp.sqrt(4 - x ** 2) / (4 * x), 1 / (x ** 2 * sp.sqrt(4 - x ** 2)))
anti(2 * sp.log(x - 1) + sp.log(x + 2), (3 * x + 3) / ((x - 1) * (x + 2)))
anti(sp.log(x - 1) - sp.log(x), 1 / (x * (x - 1)))
anti(sp.log(x) - 1 / x, (x + 1) / x ** 2)
assert sp.apart((3 * x + 3) / ((x - 1) * (x + 2))) == 2 / (x - 1) + 1 / (x + 2)
assert sp.apart(1 / (x * (x - 1))) == 1 / (x - 1) - 1 / x
assert DI(x * sp.exp(x), 0, 1) == 1 and DI(sp.sqrt(1 - x ** 2), -1, 1) == sp.pi / 2

MODULE = {
    'title': 'Techniques of integration',
    'topics': [T1, T2, T3, T4],
    'overview': 'Calculus I gave you the basic antiderivatives and substitution. Calculus II adds the techniques that handle almost every integral you will meet in science and engineering: integration by parts, trigonometric integrals and substitutions, and partial fractions.',
    'key_terms': ['Integration by parts', 'LIATE', 'Reduction', 'Trigonometric identity', 'Trigonometric substitution', 'Partial fractions', 'Proper rational function'],
    'explanation': [
        'Choosing the technique is most of the work. Look for a function and its derivative (substitution), a product of unlike functions (parts), powers of sine, cosine, tangent or secant (trigonometric integrals), a square root of a quadratic such as √(a² − x²) (trigonometric substitution), or a ratio of polynomials (partial fractions).',
        'Each technique turns a hard integral into one or more easier ones. Integration by parts trades ∫u dv for ∫v du. A trigonometric substitution removes a square root using a Pythagorean identity. Partial fractions split a rational function into simple pieces that integrate to logarithms and arctangents.',
        'Always check an indefinite integral by differentiating it. It takes half a minute and catches sign errors, lost constants and wrong coefficients.'],
    'quick_facts': [
        '∫u dv = uv − ∫v du.',
        'LIATE: choose u from Logs, Inverse trig, Algebraic, Trig, Exponential, in that order.',
        'sin²x = (1 − cos 2x)/2 and cos²x = (1 + cos 2x)/2.',
        '√(a² − x²): x = a sin θ; √(a² + x²): x = a tan θ; √(x² − a²): x = a sec θ.',
        'Partial fractions need a proper fraction: divide first if the top degree ≥ the bottom degree.'],
}

NOTES = {
    T1: {
        'overview': 'Integration by parts is the product rule run backwards. It handles integrals of products such as x eˣ, x sin x and ln x, where one factor gets simpler when differentiated.',
        'key_terms': ['Integration by parts', 'u and dv', 'LIATE', 'Repeated parts', 'Tabular method'],
        'explanation': [
            'From (uv)′ = u′v + uv′ we get ∫u dv = uv − ∫v du. The aim is to choose u so that du is simpler than u, and dv so that v is easy to find. The LIATE order (Logarithmic, Inverse trigonometric, Algebraic, Trigonometric, Exponential) suggests which factor to take as u: the one that comes first.',
            'Some integrals need parts twice. For ∫x² eˣ dx, the first use leaves ∫2x eˣ dx, which needs parts again. For ∫eˣ sin x dx, two uses bring the original integral back on the right-hand side. Then you solve for it algebraically instead of going round in circles.',
            'A single function can be treated as a product with 1. ∫ln x dx uses u = ln x and dv = dx, giving x ln x − x + C. The same trick works for arctan x and arcsin x.'],
        'formulas_label': 'Formulas',
        'formulas': ['∫u dv = uv − ∫v du', 'Definite: ∫ₐᵇ u dv = [uv]ₐᵇ − ∫ₐᵇ v du', '∫ln x dx = x ln x − x + C', '∫x eˣ dx = eˣ(x − 1) + C'],
        'steps': ['Choose u by LIATE; the rest is dv.', 'Differentiate u to get du and integrate dv to get v.', 'Write uv − ∫v du.', 'Evaluate the new integral (repeat parts if needed).', 'Differentiate the answer to check it.'],
        'worked_example': {
            'problem': 'Find ∫x cos x dx.',
            'steps': ['Algebraic comes before trigonometric in LIATE, so u = x and dv = cos x dx.', 'Then du = dx and v = sin x.', '∫x cos x dx = x sin x − ∫sin x dx = x sin x + cos x + C.'],
            'answer': '∫x cos x dx = x sin x + cos x + C.',
            'check': 'd/dx (x sin x + cos x) = sin x + x cos x − sin x = x cos x ✓.'},
        'mistakes': ['Choosing u = cos x and dv = x dx, which makes the new integral harder.', 'Dropping the minus sign in uv − ∫v du.', 'Forgetting to apply the limits to the uv term in a definite integral.', 'Going round in circles on ∫eˣ sin x dx instead of solving for the integral.'],
        'real_world': 'Integration by parts gives the expected value of exponential waiting times, ∫t λe^(−λt) dt, and is used to compute the work done by a varying force and the Laplace transforms engineers use for circuits.',
        'exam_strategy': 'Write the four pieces u, du, dv and v in a small box before applying the formula. It makes the method clear to the marker and stops sign slips.',
        'recap': ['∫u dv = uv − ∫v du.', 'Choose u by LIATE.', 'Repeat parts, or solve for the integral if it returns.', 'Check by differentiating.']},
    T2: {
        'overview': 'Integrals of powers of sine, cosine, tangent and secant are solved with identities that either save one factor for a substitution or lower the powers.',
        'key_terms': ['Pythagorean identity', 'Double-angle identity', 'Power reduction', 'Odd power', 'Even power'],
        'explanation': [
            'For ∫sinᵐx cosⁿx dx, if one power is odd, save one factor of that function and convert the rest with sin²x + cos²x = 1. For ∫cos³x dx, write cos³x = (1 − sin²x) cos x and substitute u = sin x, giving sin x − sin³x/3 + C.',
            'If both powers are even, lower them with sin²x = (1 − cos 2x)/2 and cos²x = (1 + cos 2x)/2. So ∫sin²x dx = x/2 − sin 2x/4 + C. These identities appear constantly in physics, for example the average power of an alternating current.',
            'For tangent and secant, use tan²x = sec²x − 1, and the facts d/dx tan x = sec²x and d/dx sec x = sec x tan x. So ∫tan²x dx = ∫(sec²x − 1) dx = tan x − x + C.'],
        'formulas_label': 'Identities',
        'formulas': ['sin²x + cos²x = 1', 'sin²x = (1 − cos 2x)/2', 'cos²x = (1 + cos 2x)/2', 'tan²x = sec²x − 1', '∫sec²x dx = tan x + C'],
        'steps': ['Look at the powers.', 'Odd power: save one factor and convert the rest, then substitute.', 'Both even: use the power-reduction identities.', 'Tangent and secant: use tan²x = sec²x − 1.', 'Check by differentiating.'],
        'worked_example': {
            'problem': 'Find ∫sin²x cos x dx and ∫sin²x dx.',
            'steps': ['First integral: u = sin x and du = cos x dx, so ∫u² du = u³/3 = sin³x/3 + C.', 'Second integral: the power is even, so use sin²x = (1 − cos 2x)/2.', '∫(1 − cos 2x)/2 dx = x/2 − sin 2x/4 + C.'],
            'answer': '∫sin²x cos x dx = sin³x/3 + C and ∫sin²x dx = x/2 − sin 2x/4 + C.',
            'check': 'd/dx (x/2 − sin 2x/4) = 1/2 − cos 2x/2 = sin²x ✓.'},
        'mistakes': ['Writing ∫sin²x dx = sin³x/3 + C (there is no cos x to act as du).', 'Mixing up the signs in the double-angle identities.', 'Forgetting the factor 1/2 when integrating cos 2x.', 'Converting the saved factor too, so the substitution no longer works.'],
        'real_world': 'The root-mean-square voltage of mains electricity comes from averaging sin² over a cycle. That average is 1/2, which is why a 325 V peak supply is rated at about 230 V.',
        'exam_strategy': 'Write the identity you use on its own line before substituting it. If you misremember it, the method mark is still visible.',
        'recap': ['Odd power: save one factor, convert the rest.', 'Even powers: reduce with double-angle identities.', 'tan²x = sec²x − 1.', 'Differentiate to check.']},
    T3: {
        'overview': 'Integrals containing √(a² − x²), √(a² + x²) or √(x² − a²) can be simplified by substituting a trigonometric function for x, so that a Pythagorean identity removes the square root.',
        'key_terms': ['Trigonometric substitution', 'Reference triangle', 'Inverse sine', 'Inverse tangent', 'Back-substitution'],
        'explanation': [
            'Match the root to an identity. For √(a² − x²) let x = a sin θ, since a² − a² sin²θ = a² cos²θ. For √(a² + x²) let x = a tan θ, since a² + a² tan²θ = a² sec²θ. For √(x² − a²) let x = a sec θ, since a² sec²θ − a² = a² tan²θ.',
            'After integrating in θ, return to x with a reference triangle. If x = a sin θ, draw a right triangle with opposite side x and hypotenuse a. The adjacent side is then √(a² − x²), and every trigonometric ratio of θ can be read off.',
            'Two standard results come from these substitutions and are worth memorising: ∫dx/√(a² − x²) = arcsin(x/a) + C and ∫dx/(a² + x²) = (1/a) arctan(x/a) + C. For definite integrals you can change the limits to θ and avoid back-substitution entirely.'],
        'formulas_label': 'Substitutions and results',
        'formulas': ['√(a² − x²): x = a sin θ', '√(a² + x²): x = a tan θ', '√(x² − a²): x = a sec θ', '∫dx/√(a² − x²) = arcsin(x/a) + C', '∫dx/(a² + x²) = (1/a) arctan(x/a) + C'],
        'steps': ['Identify the form of the root and choose the substitution.', 'Replace x and dx, and simplify the root with the identity.', 'Integrate in θ.', 'Return to x with a reference triangle (or change the limits).', 'Check by differentiating.'],
        'worked_example': {
            'problem': 'Evaluate ∫ from −1 to 1 of √(1 − x²) dx.',
            'steps': ['Let x = sin θ, dx = cos θ dθ; x = −1 gives θ = −π/2 and x = 1 gives θ = π/2.', '√(1 − sin²θ) = cos θ (positive on this interval), so the integral becomes ∫cos²θ dθ.', '∫cos²θ dθ = θ/2 + sin 2θ/4; from −π/2 to π/2 this is π/4 − (−π/4) = π/2.'],
            'answer': '∫ from −1 to 1 of √(1 − x²) dx = π/2.',
            'check': 'The graph is the upper half of the unit circle, whose area is π × 1²/2 = π/2 ✓.'},
        'mistakes': ['Using x = a tan θ for √(a² − x²).', 'Forgetting to replace dx with a cos θ dθ (or the matching derivative).', 'Leaving the answer in θ for an indefinite integral.', 'Missing the 1/a in ∫dx/(a² + x²).'],
        'real_world': 'Trigonometric substitution gives the area of circular and elliptical sections, which engineers use for the volume of fuel in a cylindrical tank lying on its side at any depth.',
        'exam_strategy': 'Draw the reference triangle with all three sides labelled before back-substituting. Markers look for it, and it prevents wrong ratios.',
        'recap': ['a² − x²: sine; a² + x²: tangent; x² − a²: secant.', 'The identity removes the root.', 'Use a triangle to return to x.', 'arcsin and arctan results are standard.']},
    T4: {
        'overview': 'Partial fractions split a rational function (one polynomial over another) into a sum of simple fractions, each of which integrates to a logarithm, a power or an arctangent.',
        'key_terms': ['Rational function', 'Proper fraction', 'Long division', 'Linear factor', 'Repeated factor', 'Irreducible quadratic', 'Cover-up method'],
        'explanation': [
            'First make sure the fraction is proper: the degree of the top must be less than the degree of the bottom. If not, divide first, then decompose the remainder. Next factor the denominator fully.',
            'Each distinct linear factor (x − a) gives a term A/(x − a). A repeated factor (x − a)² gives A/(x − a) + B/(x − a)². An irreducible quadratic x² + bx + c gives (Ax + B)/(x² + bx + c). Find the constants by multiplying through and substituting convenient values of x (the cover-up method) or by comparing coefficients.',
            'Then integrate term by term: A/(x − a) gives A ln|x − a|, B/(x − a)² gives −B/(x − a), and a quadratic term gives a logarithm plus an arctangent after completing the square.'],
        'formulas_label': 'Forms',
        'formulas': ['(x − a): A/(x − a)', '(x − a)²: A/(x − a) + B/(x − a)²', 'x² + bx + c (irreducible): (Ax + B)/(x² + bx + c)', '∫A/(x − a) dx = A ln|x − a| + C'],
        'steps': ['Divide if the fraction is not proper.', 'Factor the denominator.', 'Write the partial-fraction form with unknown constants.', 'Find the constants (cover-up or compare coefficients).', 'Integrate each term and add.'],
        'worked_example': {
            'problem': 'Find ∫(3x + 3)/((x − 1)(x + 2)) dx.',
            'steps': ['Write (3x + 3)/((x − 1)(x + 2)) = A/(x − 1) + B/(x + 2), so 3x + 3 = A(x + 2) + B(x − 1).', 'x = 1: 6 = 3A, so A = 2. x = −2: −3 = −3B, so B = 1.', '∫[2/(x − 1) + 1/(x + 2)] dx = 2 ln|x − 1| + ln|x + 2| + C.'],
            'answer': '2 ln|x − 1| + ln|x + 2| + C.',
            'check': 'Recombine: 2(x + 2) + (x − 1) = 3x + 3 ✓.'},
        'mistakes': ['Decomposing an improper fraction without dividing first.', 'Using one term A/(x − a)² for a repeated factor and forgetting A/(x − a).', 'Using a constant on top of an irreducible quadratic instead of Ax + B.', 'Losing the absolute value bars in ln|x − a|.'],
        'real_world': 'Partial fractions are how engineers invert Laplace transforms to find the response of circuits and control systems, and how chemists integrate rate equations for reactions between two substances.',
        'exam_strategy': 'Recombine your fractions (or substitute one extra x value) to check the constants before integrating. A wrong constant spoils every later line.',
        'recap': ['Proper fraction first.', 'One term per factor; repeated and quadratic factors need extra terms.', 'Find constants by cover-up or coefficients.', 'Linear terms integrate to logarithms.']},
}

QUESTIONS = [
    # T1
    Q(T1, '∫x eˣ dx =', ['eˣ(x − 1) + C', 'x eˣ + C', 'eˣ(x + 1) + C', 'x² eˣ/2 + C'], 0, 'u = x, dv = eˣ dx: x eˣ − ∫eˣ dx = eˣ(x − 1) + C.', ans=I(x * sp.exp(x))),
    Q(T1, '∫ln x dx =', ['x ln x − x + C', '1/x + C', 'x ln x + C', '(ln x)²/2 + C'], 0, 'u = ln x, dv = dx: x ln x − ∫x(1/x) dx = x ln x − x + C.', ans=I(sp.log(x))),
    Q(T1, 'In ∫x² sin x dx, which choice of u follows LIATE?', ['u = x²', 'u = sin x', 'u = x² sin x', 'u = cos x'], 0, 'Algebraic comes before trigonometric, and x² simplifies when differentiated.'),
    Q(T1, 'Evaluate ∫ from 0 to 1 of x eˣ dx.', ['1', 'e', 'e − 1', '2e − 1'], 0, '[eˣ(x − 1)] from 0 to 1 = 0 − (−1) = 1.', ans=DI(x * sp.exp(x), 0, 1)),
    Q(T1, '∫x ln x dx =', ['(x²/2) ln x − x²/4 + C', 'x ln x − x + C', '(x²/2) ln x + C', 'ln x − x²/4 + C'], 0, 'u = ln x, dv = x dx: (x²/2) ln x − ∫(x/2) dx = (x²/2) ln x − x²/4 + C.', ans=I(x * sp.log(x))),
    Q(T1, 'Applying parts twice to ∫eˣ sin x dx gives:', ['eˣ(sin x − cos x)/2 + C', 'eˣ cos x + C', 'eˣ(sin x + cos x)/2 + C', '−eˣ cos x + C'], 0, 'The integral reappears after two steps: 2I = eˣ(sin x − cos x).', ans=I(sp.exp(x) * sp.sin(x))),
    # T2
    Q(T2, '∫sin²x cos x dx =', ['sin³x/3 + C', 'cos³x/3 + C', '−sin³x/3 + C', 'sin x cos²x + C'], 0, 'u = sin x, du = cos x dx: ∫u² du = u³/3.', ans=I(sp.sin(x) ** 2 * sp.cos(x))),
    Q(T2, '∫sin²x dx =', ['x/2 − sin 2x/4 + C', 'sin³x/3 + C', 'x/2 + sin 2x/4 + C', '−cos²x + C'], 0, 'Use sin²x = (1 − cos 2x)/2.', ans=I(sp.sin(x) ** 2)),
    Q(T2, '∫tan²x dx =', ['tan x − x + C', 'tan³x/3 + C', 'sec²x + C', 'tan x + x + C'], 0, 'tan²x = sec²x − 1, and ∫sec²x dx = tan x.', ans=I(sp.tan(x) ** 2)),
    Q(T2, '∫cos³x dx =', ['sin x − sin³x/3 + C', 'cos⁴x/4 + C', 'sin x + sin³x/3 + C', '3cos²x sin x + C'], 0, 'cos³x = (1 − sin²x) cos x; with u = sin x this is u − u³/3.', ans=I(sp.cos(x) ** 3)),
    Q(T2, 'Evaluate ∫ from 0 to π of sin²x dx.', ['π/2', 'π', '0', '1'], 0, '[x/2 − sin 2x/4] from 0 to π = π/2.', ans=DI(sp.sin(x) ** 2, 0, sp.pi)),
    Q(T2, 'For ∫sin⁵x cos²x dx, the best first step is:', ['save one sin x and write sin⁴x = (1 − cos²x)²', 'use cos²x = (1 + cos 2x)/2', 'substitute u = sin x', 'integrate by parts'], 0, 'The sine power is odd: save one sin x for du = −sin x dx with u = cos x.'),
    # T3
    Q(T3, 'Which substitution suits ∫√(9 − x²) dx?', ['x = 3 sin θ', 'x = 3 tan θ', 'x = 3 sec θ', 'x = 9 sin θ'], 0, 'a² − x² with a = 3: 9 − 9 sin²θ = 9 cos²θ.'),
    Q(T3, '∫dx/√(9 − x²) =', ['arcsin(x/3) + C', 'arctan(x/3) + C', '(1/3) arcsin(x/3) + C', 'arcsin(3x) + C'], 0, 'Standard result with a = 3.', ans=I(1 / sp.sqrt(9 - x ** 2))),
    Q(T3, '∫dx/(x² + 4) =', ['(1/2) arctan(x/2) + C', 'arctan(x/2) + C', '2 arctan(x/2) + C', 'ln(x² + 4) + C'], 0, '(1/a) arctan(x/a) with a = 2.', ans=I(1 / (x ** 2 + 4))),
    Q(T3, 'Evaluate ∫ from −1 to 1 of √(1 − x²) dx.', ['π/2', 'π', '2', '1'], 0, 'It is the area of a half unit circle.', ans=DI(sp.sqrt(1 - x ** 2), -1, 1)),
    Q(T3, 'With x = 2 tan θ, √(4 + x²) becomes:', ['2 sec θ', '2 cos θ', '2 tan θ', '4 sec²θ'], 0, '4 + 4 tan²θ = 4 sec²θ, whose root is 2 sec θ.'),
    Q(T3, 'If x = a sin θ, which is cos θ in terms of x?', ['√(a² − x²)/a', 'x/a', 'a/√(a² − x²)', 'x/√(a² − x²)'], 0, 'Opposite x, hypotenuse a, so the adjacent side is √(a² − x²).'),
    # T4
    Q(T4, 'Decompose (3x + 3)/((x − 1)(x + 2)).', ['2/(x − 1) + 1/(x + 2)', '1/(x − 1) + 2/(x + 2)', '3/(x − 1) + 3/(x + 2)', '2/(x − 1) − 1/(x + 2)'], 0, 'Cover-up: x = 1 gives A = 6/3 = 2; x = −2 gives B = −3/−3 = 1.'),
    Q(T4, '∫dx/(x(x − 1)) =', ['ln|x − 1| − ln|x| + C', 'ln|x| − ln|x − 1| + C', 'ln|x(x − 1)| + C', '1/(x − 1) − 1/x + C'], 0, '1/(x(x − 1)) = 1/(x − 1) − 1/x.'),
    Q(T4, 'The form for (2x + 1)/((x − 3)²(x + 1)) is:', ['A/(x − 3) + B/(x − 3)² + C/(x + 1)', 'A/(x − 3)² + B/(x + 1)', '(Ax + B)/(x − 3)² + C/(x + 1)', 'A/(x − 3) + B/(x + 1)'], 0, 'A repeated linear factor needs a term for each power.'),
    Q(T4, 'Before decomposing (x³ + 1)/(x² − 1), you must first:', ['divide, because the fraction is improper', 'complete the square', 'substitute u = x² − 1', 'integrate by parts'], 0, 'The top degree (3) is not less than the bottom degree (2).'),
    Q(T4, '∫(x + 1)/x² dx =', ['ln|x| − 1/x + C', 'ln|x| + 1/x + C', 'x²/2 − 1/x + C', '−1/x − 1/x² + C'], 0, '(x + 1)/x² = 1/x + 1/x², which integrates to ln|x| − 1/x.'),
    Q(T4, 'Evaluate ∫ from 2 to 3 of dx/(x(x − 1)), to 4 d.p.', ['0.2877', '0.6931', '0.4055', '1.0986'], 0, '[ln|x − 1| − ln|x|] from 2 to 3 = (ln 2 − ln 3) − (0 − ln 2) = ln(4/3) ≈ 0.2877.', ans=DI(1 / (x * (x - 1)), 2, 3), num=True),
]

FLASH = [
    ['Integration by parts', '∫u dv = uv − ∫v du.'],
    ['LIATE', 'Choose u from Logs, Inverse trig, Algebraic, Trig, Exponential.'],
    ['∫ln x dx', 'x ln x − x + C.'],
    ['sin²x', '(1 − cos 2x)/2.'],
    ['√(a² − x²)', 'Substitute x = a sin θ.'],
    ['∫dx/(a² + x²)', '(1/a) arctan(x/a) + C.'],
    ['Repeated factor (x − a)²', 'A/(x − a) + B/(x − a)².'],
    ['Improper rational function', 'Divide before using partial fractions.'],
]
