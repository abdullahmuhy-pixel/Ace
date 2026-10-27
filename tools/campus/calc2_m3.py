"""Calculus II, module 3: Sequences and series."""
from verify import Q, x, n, sp
T1, T2, T3, T4 = ('Sequences and their limits', 'Series: geometric, telescoping and the divergence test', 'The integral and comparison tests', 'The ratio test and alternating series')
S = lambda f, a=1: sp.summation(f, (n, a, sp.oo))
L = lambda f: sp.limit(f, n, sp.oo)

assert L((3 * n ** 2 + 1) / (n ** 2 - 2 * n)) == 3 and L((1 + 1 / n) ** n) == sp.E and L(sp.log(n) / n) == 0
assert S(sp.Rational(1, 3) ** n, 0) == sp.Rational(3, 2) and S(2 * sp.Rational(1, 2) ** (n - 1)) == 4
assert S(1 / (n * (n + 1))) == 1 and S(1 / n ** 2) == sp.pi ** 2 / 6 and S(n / 2 ** n) == 2
assert S(7 * sp.Rational(1, 10) ** n) == sp.Rational(7, 9)
assert S((-1) ** (n + 1) / n) == sp.log(2)
assert L((n + 1) / 2 ** (n + 1) / (n / 2 ** n)) == sp.Rational(1, 2)

MODULE = {
    'title': 'Sequences and series',
    'topics': [T1, T2, T3, T4],
    'overview': 'Can you add infinitely many numbers and get a finite answer? Sometimes. This module defines sequences and their limits, then infinite series and the tests that decide whether a series converges, which is the groundwork for the power series in the next module.',
    'key_terms': ['Sequence', 'Limit', 'Series', 'Partial sum', 'Geometric series', 'Divergence test', 'p-series', 'Comparison test', 'Ratio test', 'Alternating series'],
    'explanation': [
        'A sequence is an ordered list a₁, a₂, a₃, … and a series is the sum of its terms. A series converges if its partial sums Sₙ = a₁ + … + aₙ approach a finite limit. Geometric and telescoping series are the rare ones whose sum you can find exactly.',
        'For most series we can only decide whether they converge. Start with the divergence test: if aₙ does not tend to 0, the series diverges. If aₙ → 0, that proves nothing, and you need a sharper test.',
        'Choose the test from the form of aₙ: p-series and comparison for powers of n, the integral test when aₙ is easy to integrate, the ratio test for factorials and exponentials, and the alternating series test for signs that switch.'],
    'quick_facts': [
        'Geometric: Σarⁿ⁻¹ = a/(1 − r) if |r| < 1, otherwise divergent.',
        'Divergence test: aₙ ↛ 0 ⇒ Σaₙ diverges.',
        'p-series Σ1/nᵖ converges iff p > 1; the harmonic series Σ1/n diverges.',
        'Ratio test: L = lim|aₙ₊₁/aₙ|; L < 1 converges, L > 1 diverges, L = 1 inconclusive.',
        'Alternating series with |aₙ| decreasing to 0 converge.'],
}

NOTES = {
    T1: {
        'overview': 'A sequence converges if its terms settle down to one number as n grows. The limit laws, dominant terms and a few standard limits handle almost every case.',
        'key_terms': ['Sequence', 'Convergent', 'Divergent', 'Limit laws', 'Squeeze theorem', 'Monotone'],
        'explanation': [
            'aₙ → L means the terms get as close to L as you like once n is large enough. For rational expressions, divide top and bottom by the highest power of n: (3n² + 1)/(n² − 2n) → 3 because the n² terms dominate.',
            'Some standard limits: 1/nᵖ → 0 for p > 0; rⁿ → 0 if |r| < 1; (1 + 1/n)ⁿ → e; ln n / n → 0; and n!/nⁿ → 0. Growth order from slow to fast is: ln n, powers of n, exponentials aⁿ (a > 1), n!, nⁿ.',
            'The squeeze theorem handles oscillating terms. Since −1/n ≤ (−1)ⁿ/n ≤ 1/n and both bounds tend to 0, (−1)ⁿ/n → 0. A bounded, monotone sequence always converges, which is useful when no formula is available.'],
        'formulas_label': 'Standard limits',
        'formulas': ['1/nᵖ → 0 for p > 0', 'rⁿ → 0 for |r| < 1', '(1 + 1/n)ⁿ → e', 'ln n / n → 0', 'Growth: ln n ≪ nᵖ ≪ aⁿ ≪ n! ≪ nⁿ'],
        'steps': ['Identify the dominant term on top and bottom.', 'Divide through by it, or use a standard limit.', 'Use the squeeze theorem for oscillating factors.', 'If the terms do not settle, the sequence diverges.'],
        'worked_example': {
            'problem': 'Find lim (3n² + 1)/(n² − 2n) as n → ∞.',
            'steps': ['Divide top and bottom by n²: (3 + 1/n²)/(1 − 2/n).', 'As n → ∞, 1/n² → 0 and 2/n → 0.', 'The limit is 3/1 = 3.'],
            'answer': 'The sequence converges to 3.',
            'check': 'At n = 100: 30001/9800 ≈ 3.06, close to 3 ✓.'},
        'mistakes': ['Confusing a sequence converging with the series of its terms converging.', 'Dividing by the wrong power of n.', 'Thinking (1 + 1/n)ⁿ → 1 because 1 + 1/n → 1.', 'Treating oscillating sequences such as (−1)ⁿ as convergent.'],
        'real_world': 'Iterative algorithms (Newton\'s method, machine-learning training loops) produce sequences of approximations, and programmers stop when successive terms are close enough to the limit.',
        'exam_strategy': 'Show the division by the dominant term as a separate line. A bare answer "3" often earns nothing if the working is missing.',
        'recap': ['Divide by the dominant power.', 'Know the standard limits and growth order.', 'Squeeze oscillating terms.', 'Bounded and monotone ⇒ convergent.']},
    T2: {
        'overview': 'A series adds the terms of a sequence. Geometric series and telescoping series have exact sums. For any series, terms that do not shrink to zero mean divergence.',
        'key_terms': ['Partial sum', 'Geometric series', 'Common ratio', 'Telescoping series', 'Divergence test', 'Harmonic series'],
        'explanation': [
            'The geometric series a + ar + ar² + … has partial sums a(1 − rⁿ)/(1 − r). If |r| < 1, rⁿ → 0 and the sum is a/(1 − r); if |r| ≥ 1 the series diverges. Repeating decimals are geometric: 0.777… = 7/10 + 7/100 + … = (7/10)/(1 − 1/10) = 7/9.',
            'A telescoping series cancels when written out. Since 1/(n(n + 1)) = 1/n − 1/(n + 1), the partial sum is 1 − 1/(n + 1), which tends to 1. Partial fractions are often the key to spotting this.',
            'Divergence test: if lim aₙ ≠ 0 (or does not exist), Σaₙ diverges. The converse is false. The harmonic series Σ1/n has aₙ → 0 but still diverges, because grouping its terms gives 1 + 1/2 + (1/3 + 1/4) + … > 1 + 1/2 + 1/2 + 1/2 + …'],
        'formulas_label': 'Formulas',
        'formulas': ['Sₙ = a₁ + a₂ + … + aₙ', 'Geometric: Σₙ₌₁^∞ arⁿ⁻¹ = a/(1 − r) for |r| < 1', '1/(n(n + 1)) = 1/n − 1/(n + 1)', 'aₙ ↛ 0 ⇒ divergent'],
        'steps': ['Check the divergence test first.', 'Is it geometric? Find a and r and check |r| < 1.', 'Is it telescoping? Use partial fractions and write out Sₙ.', 'Otherwise use a convergence test (next topics).'],
        'worked_example': {
            'problem': 'Find Σₙ₌₁^∞ 1/(n(n + 1)).',
            'steps': ['Partial fractions: 1/(n(n + 1)) = 1/n − 1/(n + 1).', 'Sₙ = (1 − 1/2) + (1/2 − 1/3) + … + (1/n − 1/(n + 1)) = 1 − 1/(n + 1).', 'As n → ∞, Sₙ → 1.'],
            'answer': 'The series converges to 1.',
            'check': 'S₄ = 1/2 + 1/6 + 1/12 + 1/20 = 0.8 = 1 − 1/5 ✓.'},
        'mistakes': ['Concluding convergence because aₙ → 0.', 'Using a/(1 − r) when |r| ≥ 1.', 'Getting the first term wrong when the index starts at 0 instead of 1.', 'Cancelling terms in a telescoping series without writing out the partial sum.'],
        'real_world': 'Geometric series give the present value of a perpetuity, a payment that continues forever, and the total effect of the money multiplier in banking when each loan is partly re-deposited.',
        'exam_strategy': 'For a geometric series, write "a = …, r = …, |r| < 1 so it converges" before using the formula. The condition is part of the answer.',
        'recap': ['Geometric: a/(1 − r) if |r| < 1.', 'Telescoping: write out Sₙ and cancel.', 'aₙ ↛ 0 ⇒ diverges.', 'aₙ → 0 is not enough (harmonic series).']},
    T3: {
        'overview': 'For series with positive terms, the integral test and the comparison tests decide convergence by relating the series to an integral or to a series you already know, usually a p-series.',
        'key_terms': ['Integral test', 'p-series', 'Direct comparison test', 'Limit comparison test', 'Positive series'],
        'explanation': [
            'Integral test: if f is positive, continuous and decreasing with f(n) = aₙ, then Σaₙ and ∫₁^∞ f(x) dx either both converge or both diverge. This proves the p-series result: Σ1/nᵖ converges if and only if p > 1. The integral\'s value is not the sum of the series.',
            'Direct comparison: if 0 ≤ aₙ ≤ bₙ and Σbₙ converges, so does Σaₙ. If aₙ ≥ bₙ ≥ 0 and Σbₙ diverges, so does Σaₙ. The comparison must point the right way to conclude anything.',
            'Limit comparison is easier in practice: if aₙ, bₙ > 0 and aₙ/bₙ → c with 0 < c < ∞, the two series behave the same way. Choose bₙ by keeping only the dominant terms: for (2n + 1)/(n³ + 5), compare with 2n/n³ = 2/n², which converges.'],
        'formulas_label': 'Tests',
        'formulas': ['Integral test: Σf(n) and ∫₁^∞ f(x) dx behave alike', 'p-series: Σ1/nᵖ converges iff p > 1', 'Direct: 0 ≤ aₙ ≤ bₙ, Σbₙ converges ⇒ Σaₙ converges', 'Limit: aₙ/bₙ → c, 0 < c < ∞ ⇒ same behaviour'],
        'steps': ['Check the terms are positive.', 'Keep the dominant terms to guess a comparison series.', 'Use limit comparison (or direct comparison with the right inequality).', 'Or apply the integral test if f is easy to integrate.', 'State the conclusion and the test used.'],
        'worked_example': {
            'problem': 'Does Σ (2n + 1)/(n³ + 5) converge?',
            'steps': ['For large n the terms behave like 2n/n³ = 2/n², so compare with bₙ = 1/n².', 'aₙ/bₙ = n²(2n + 1)/(n³ + 5) = (2n³ + n²)/(n³ + 5) → 2.', '0 < 2 < ∞ and Σ1/n² converges (p = 2 > 1), so the series converges by limit comparison.'],
            'answer': 'It converges.',
            'check': 'The terms fall off like 2/n², the same rate as a convergent p-series.'},
        'mistakes': ['Comparing in the wrong direction (being smaller than a divergent series proves nothing).', 'Using the integral test on a function that is not decreasing.', 'Thinking the integral equals the sum of the series.', 'Forgetting that p = 1 (the harmonic series) diverges.'],
        'real_world': 'Computer scientists use the same comparisons to analyse algorithms: the cost of hashing or searching is often a series whose growth is bounded by a p-series or by ln n.',
        'exam_strategy': 'Always name the comparison series and why it converges or diverges ("Σ1/n² converges as a p-series with p = 2 > 1"). The test only works if that reason is stated.',
        'recap': ['Integral test links a series to ∫f.', 'p-series: p > 1 converges.', 'Comparison must point the right way.', 'Limit comparison: keep the dominant terms.']},
    T4: {
        'overview': 'The ratio test handles series with factorials and exponentials. Alternating series, whose signs switch, need their own test and introduce the difference between absolute and conditional convergence.',
        'key_terms': ['Ratio test', 'Root test', 'Alternating series test', 'Absolute convergence', 'Conditional convergence', 'Error bound'],
        'explanation': [
            'Ratio test: let L = lim |aₙ₊₁/aₙ|. If L < 1 the series converges absolutely; if L > 1 it diverges; if L = 1 the test says nothing. It is ideal for n!, aⁿ and nᵏaⁿ. For Σn/2ⁿ the ratio is (n + 1)/(2n) → 1/2 < 1, so it converges (to 2).',
            'Alternating series test: if bₙ > 0 decreases to 0, then Σ(−1)ⁿ⁺¹bₙ converges. The alternating harmonic series 1 − 1/2 + 1/3 − … converges (to ln 2) even though Σ1/n diverges. Stopping after n terms leaves an error no bigger than the next term bₙ₊₁.',
            'A series converges absolutely if Σ|aₙ| converges, and absolute convergence implies convergence. If Σaₙ converges but Σ|aₙ| does not, the convergence is conditional, as for the alternating harmonic series. Conditionally convergent series are delicate: rearranging their terms can change the sum.'],
        'formulas_label': 'Tests',
        'formulas': ['Ratio: L = lim|aₙ₊₁/aₙ|; L < 1 converges, L > 1 diverges, L = 1 inconclusive', 'Root: L = lim |aₙ|^(1/n), same conclusions', 'Alternating: bₙ ↓ 0 ⇒ Σ(−1)ⁿbₙ converges', 'Error after n terms ≤ bₙ₊₁'],
        'steps': ['Factorials or exponentials: use the ratio test.', 'Alternating signs: check that bₙ decreases to 0.', 'Test Σ|aₙ| to decide absolute or conditional convergence.', 'If L = 1, switch to another test.'],
        'worked_example': {
            'problem': 'Test Σₙ₌₁^∞ n/2ⁿ for convergence.',
            'steps': ['aₙ₊₁/aₙ = ((n + 1)/2ⁿ⁺¹) × (2ⁿ/n) = (n + 1)/(2n).', 'As n → ∞, this tends to 1/2.', 'L = 1/2 < 1, so the series converges by the ratio test.'],
            'answer': 'It converges (its sum is in fact 2).',
            'check': 'The first terms 1/2 + 2/4 + 3/8 + 4/16 + 5/32 already add to about 1.78, approaching 2.'},
        'mistakes': ['Concluding "converges" or "diverges" when L = 1.', 'Using the ratio test on p-series, where it always gives L = 1.', 'Forgetting to check that bₙ is decreasing in the alternating series test.', 'Saying a conditionally convergent series converges absolutely.'],
        'real_world': 'Error bounds for alternating series tell calculators and software how many terms of a series are needed to compute values such as ln 2 or π to a guaranteed number of decimal places.',
        'exam_strategy': 'Simplify aₙ₊₁/aₙ completely (cancel factorials: (n + 1)!/n! = n + 1) before taking the limit, and state the value of L and the conclusion together.',
        'recap': ['Ratio test for factorials and exponentials.', 'L = 1 tells you nothing.', 'Alternating: decreasing to 0 ⇒ converges.', 'Absolute ⇒ convergent; conditional is weaker.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'lim (3n² + 1)/(n² − 2n) as n → ∞ =', ['3', '1', '0', '∞'], 0, 'Divide by n²: (3 + 1/n²)/(1 − 2/n) → 3.', ans=L((3 * n ** 2 + 1) / (n ** 2 - 2 * n))),
    Q(T1, 'lim (1 + 1/n)ⁿ as n → ∞ =', ['e', '1', '∞', '2'], 0, 'This standard limit defines e.', ans=sp.E),
    Q(T1, 'Which sequence diverges?', ['(−1)ⁿ', '(−1)ⁿ/n', '1/n²', '(0.9)ⁿ'], 0, '(−1)ⁿ alternates between −1 and 1 and never settles.'),
    Q(T1, 'lim (ln n)/n as n → ∞ =', ['0', '1', '∞', 'e'], 0, 'Powers of n grow faster than ln n.', ans=L(sp.log(n) / n)),
    Q(T1, 'lim (5n + 2)/(2n³ − 1) as n → ∞ =', ['0', '5/2', '∞', '2'], 0, 'The bottom has the higher power.', ans=L((5 * n + 2) / (2 * n ** 3 - 1))),
    Q(T1, 'Which grows fastest as n → ∞?', ['n!', '2ⁿ', 'n¹⁰', 'ln n'], 0, 'Growth order: ln n ≪ n¹⁰ ≪ 2ⁿ ≪ n!.'),
    # T2
    Q(T2, 'Σₙ₌₀^∞ (1/3)ⁿ =', ['3/2', '1/2', '3', '2/3'], 0, 'a = 1, r = 1/3: 1/(1 − 1/3) = 3/2.', ans=S(sp.Rational(1, 3) ** n, 0)),
    Q(T2, 'Σₙ₌₁^∞ 1/(n(n + 1)) =', ['1', '1/2', '2', 'diverges'], 0, 'It telescopes: Sₙ = 1 − 1/(n + 1) → 1.', ans=S(1 / (n * (n + 1)))),
    Q(T2, 'The repeating decimal 0.777… equals:', ['7/9', '7/10', '77/100', '7/11'], 0, '(7/10)/(1 − 1/10) = 7/9.', ans=sp.Rational(7, 9)),
    Q(T2, 'What does the divergence test say about Σ n/(n + 1)?', ['It diverges, because the terms tend to 1', 'It converges, because the terms are less than 1', 'Nothing', 'It converges to 1'], 0, 'aₙ → 1 ≠ 0.'),
    Q(T2, 'Σₙ₌₁^∞ 2(1/2)ⁿ⁻¹ =', ['4', '2', '1', '8'], 0, 'a = 2, r = 1/2: 2/(1 − 1/2) = 4.', ans=S(2 * sp.Rational(1, 2) ** (n - 1))),
    Q(T2, 'Σ 3(5/4)ⁿ:', ['diverges, because |r| ≥ 1', 'converges to 12', 'converges to −12', 'converges to 15'], 0, 'r = 5/4 > 1, so the terms grow.'),
    # T3
    Q(T3, 'Σ 1/n² converges because it is a p-series with:', ['p = 2 > 1', 'p = 2 < 3', 'terms tending to 0', 'a ratio less than 1'], 0, 'p-series converge exactly when p > 1. (Its sum is π²/6.)'),
    Q(T3, 'Which series diverges?', ['Σ 1/√n', 'Σ 1/n³', 'Σ 1/n^1.5', 'Σ 1/(n² + 1)'], 0, 'p = 1/2 ≤ 1.'),
    Q(T3, 'To test Σ (2n + 1)/(n³ + 5), the best comparison series is:', ['Σ 1/n²', 'Σ 1/n', 'Σ 1/n³', 'Σ 2ⁿ'], 0, 'The dominant terms give 2n/n³ = 2/n².'),
    Q(T3, 'If 0 ≤ aₙ ≤ 1/n for all n, what can you conclude about Σaₙ?', ['Nothing from this comparison', 'It converges', 'It diverges', 'It equals Σ 1/n'], 0, 'Being smaller than a divergent series proves nothing.'),
    Q(T3, 'The integral test applied to Σ 1/(n ln n) (n ≥ 2) uses ∫ dx/(x ln x) = ln(ln x). The series:', ['diverges', 'converges to 1', 'converges to ln 2', 'cannot be tested'], 0, 'ln(ln t) → ∞ as t → ∞, so the integral and the series diverge.'),
    Q(T3, 'Σ 1/(n² + n) converges. Which reason is valid?', ['1/(n² + n) ≤ 1/n² and Σ1/n² converges', '1/(n² + n) → 0', '1/(n² + n) ≥ 1/n³', 'It is geometric'], 0, 'A direct comparison in the correct direction.'),
    # T4
    Q(T4, 'For Σ n/2ⁿ, the ratio-test limit L is:', ['1/2', '1', '2', '0'], 0, '(n + 1)/(2n) → 1/2.', ans=sp.Rational(1, 2)),
    Q(T4, 'Σ n/2ⁿ (from n = 1) has sum:', ['2', '1', '4', 'it diverges'], 0, 'A standard result, for example from differentiating a geometric series.', ans=S(n / 2 ** n)),
    Q(T4, 'For Σ 1/n, the ratio test gives L = 1. This means:', ['the ratio test is inconclusive', 'the series converges', 'the series diverges', 'the sum is 1'], 0, 'L = 1 gives no information; the harmonic series in fact diverges.'),
    Q(T4, '1 − 1/2 + 1/3 − 1/4 + … :', ['converges conditionally', 'converges absolutely', 'diverges', 'converges to 0'], 0, 'It converges (to ln 2) by the alternating series test, but Σ1/n diverges.'),
    Q(T4, 'The alternating harmonic series sums to:', ['ln 2', '1', 'π/4', 'e'], 0, 'A standard result from the Maclaurin series of ln(1 + x).', ans=sp.log(2)),
    Q(T4, 'Approximating Σ(−1)ⁿ⁺¹/n² by its first 3 terms, the error is at most:', ['1/16', '1/9', '1/4', '1/3'], 0, 'The error is at most the next term, 1/4² = 1/16.', ans=sp.Rational(1, 16)),
]

FLASH = [
    ['Geometric series sum', 'a/(1 − r), valid only for |r| < 1.'],
    ['Divergence test', 'If aₙ ↛ 0, Σaₙ diverges. aₙ → 0 proves nothing.'],
    ['Harmonic series', 'Σ1/n diverges.'],
    ['p-series', 'Σ1/nᵖ converges iff p > 1.'],
    ['Limit comparison', 'aₙ/bₙ → c, 0 < c < ∞: both converge or both diverge.'],
    ['Ratio test', 'L = lim|aₙ₊₁/aₙ|: < 1 converges, > 1 diverges, = 1 inconclusive.'],
    ['Alternating series test', 'bₙ decreasing to 0 ⇒ Σ(−1)ⁿbₙ converges; error ≤ next term.'],
    ['Conditional convergence', 'Σaₙ converges but Σ|aₙ| diverges.'],
]
