"""Discrete Mathematics and Logic, module 3: Counting."""
import itertools as it
from math import comb, perm, factorial as fac
from verify import Q, x, sp
T1, T2, T3, T4 = ('The sum and product rules', 'Permutations and combinations', 'The binomial theorem and Pascal\'s triangle', 'The pigeonhole principle and inclusion–exclusion')
assert 3 * 4 == 12 and 10 ** 4 == 10000 and 36 ** 6 == 2176782336 and 26 ** 3 * 10 ** 3 == 17576000 and 2 ** 8 == 256 and 5 + 7 == 12
assert perm(5, 3) == 60 and comb(10, 3) == 120 and fac(6) // (fac(3) * fac(2)) == 60 and comb(4, 2) * comb(5, 1) == 30 and comb(12, 2) == 66 and fac(4) == 24
assert len(set(it.permutations('BANANA'))) == 60 and len([c for c in it.combinations_with_replacement(range(3), 10)]) == 66
assert sp.expand((1 + x) ** 7).coeff(x, 3) == 35 and sp.expand((2 * x + 1) ** 5).coeff(x, 2) == 40 and sum(comb(6, k) for k in range(7)) == 64
assert len(sp.Poly(sp.expand((x + sp.Symbol('w')) ** 4)).terms()) == 5 and comb(9, 4) == comb(8, 3) + comb(8, 4)
assert len([k for k in range(1, 101) if k % 2 == 0 or k % 3 == 0]) == 67 and 50 + 33 - 16 == 67
assert sum(1 for p in it.permutations(range(4)) if all(p[i] != i for i in range(4))) == 9 and -(-25 // 6) == 5
assert len([k for k in range(1, 101) if k % 2 and k % 3 and k % 5]) == 26

MODULE = {
    'title': 'Counting',
    'topics': [T1, T2, T3, T4],
    'overview': 'Counting without listing is the heart of probability, algorithm analysis and cryptography. This module covers the basic rules, permutations and combinations, the binomial theorem, and two powerful principles: pigeonhole and inclusion–exclusion.',
    'key_terms': ['Product rule', 'Sum rule', 'Permutation', 'Combination', 'Factorial', 'Arrangements with repetition', 'Stars and bars', 'Binomial coefficient', 'Pascal\'s triangle', 'Pigeonhole principle', 'Inclusion–exclusion', 'Derangement'],
    'explanation': [
        'If a task has stages, multiply the choices at each stage (product rule); if it splits into separate cases, add them (sum rule). These two rules, applied carefully, solve most counting problems.',
        'Permutations count ordered selections: P(n, r) = n!/(n − r)!. Combinations count unordered ones: C(n, r) = n!/(r!(n − r)!). Ask "does order matter?" and "can items repeat?" before choosing a formula.',
        'The binomial theorem expands (a + b)ⁿ with coefficients C(n, k), arranged in Pascal\'s triangle. The pigeonhole principle proves that something must repeat, and inclusion–exclusion counts unions without double counting.'],
    'quick_facts': [
        'Product rule: m ways then n ways ⇒ mn ways.',
        'P(n, r) = n!/(n − r)!, C(n, r) = n!/(r!(n − r)!).',
        'Words with repeated letters: n!/(n₁!n₂!…).',
        'Stars and bars: k identical items into n boxes: C(k + n − 1, n − 1).',
        '(a + b)ⁿ = Σ C(n, k)aⁿ⁻ᵏbᵏ.'],
}

NOTES = {
    T1: {
        'overview': 'The product and sum rules are the building blocks of all counting.',
        'key_terms': ['Product rule', 'Sum rule', 'Stage', 'Case', 'Bit string', 'Repetition allowed'],
        'explanation': [
            'Product rule: choosing a shirt (3 options) and then trousers (4 options) gives 3 × 4 = 12 outfits. Sum rule: choosing one book from 5 novels or 7 textbooks gives 5 + 7 = 12 choices.',
            'With repetition, each position is a stage: a 4-digit PIN has 10⁴ = 10 000 possibilities; a bit string of length 8 has 2⁸ = 256; a 6-character password from 26 letters and 10 digits has 36⁶ = 2 176 782 336.',
            'A number plate with 3 letters then 3 digits has 26³ × 10³ = 17 576 000 possibilities. Restrictions change the count at the restricted stages only: for example, a PIN that cannot start with 0 has 9 × 10³ = 9000 options.'],
        'formulas_label': 'Rules',
        'formulas': ['Product rule: n₁ × n₂ × … × nₖ', 'Sum rule (disjoint cases): n₁ + n₂ + …', 'Strings of length k from n symbols: nᵏ', 'Apply restrictions stage by stage'],
        'steps': ['Break the task into stages or cases.', 'Count the options at each stage.', 'Multiply across stages; add across disjoint cases.', 'Handle restrictions first.'],
        'worked_example': {
            'problem': 'How many 6-character passwords use only lowercase letters and digits?',
            'steps': ['Each position has 26 + 10 = 36 choices (sum rule).', 'Six positions (product rule).', '36⁶ = 2 176 782 336.'],
            'answer': '2 176 782 336.',
            'check': 'About 2 × 10⁹, which is why short passwords are easy to guess by computer ✓.'},
        'mistakes': ['Adding when you should multiply.', 'Forgetting that cases must not overlap for the sum rule.', 'Ignoring restrictions on the first position.', 'Using permutations when repetition is allowed.'],
        'real_world': 'Password strength rules are counting arguments: each extra character multiplies the number of possibilities by the size of the alphabet.',
        'exam_strategy': 'Draw boxes for each position and write the number of options in each; then multiply.',
        'recap': ['Multiply stages.', 'Add disjoint cases.', 'nᵏ with repetition.', 'Restrictions first.']},
    T2: {
        'overview': 'Permutations count ordered arrangements; combinations count selections where order does not matter.',
        'key_terms': ['Factorial', 'Permutation P(n, r)', 'Combination C(n, r)', 'Repeated letters', 'Circular arrangement', 'Stars and bars'],
        'explanation': [
            'Choosing a president, secretary and treasurer from 5 people (order matters): P(5, 3) = 5 × 4 × 3 = 60. Choosing a committee of 3 from 10 (order does not matter): C(10, 3) = 120.',
            'Arrangements of letters with repeats divide by the repeats: BANANA has 6!/(3! 2!) = 60 arrangements. Committees with conditions multiply combinations: 2 women from 4 and 1 man from 5 is C(4, 2) × C(5, 1) = 30. Five people around a round table: (5 − 1)! = 24 (rotations are the same).',
            'Stars and bars counts ways to share identical items: 10 identical sweets among 3 children is C(10 + 2, 2) = 66.'],
        'formulas_label': 'Formulas',
        'formulas': ['P(n, r) = n!/(n − r)!', 'C(n, r) = n!/(r!(n − r)!)', 'Repeated items: n!/(n₁!n₂!…)', 'Circular: (n − 1)!', 'Stars and bars: C(k + n − 1, n − 1)'],
        'steps': ['Ask: does order matter? Is repetition allowed?', 'Choose the matching formula.', 'Split conditions into products of combinations.', 'Check with a small case.'],
        'worked_example': {
            'problem': 'How many different arrangements of the letters of BANANA are there?',
            'steps': ['6 letters: 6! = 720 if all were different.', 'A appears 3 times, N twice: divide by 3! × 2! = 12.', '720/12 = 60.'],
            'answer': '60.',
            'check': 'A computer listing of all distinct permutations gives exactly 60 ✓.'},
        'mistakes': ['Using P when order does not matter.', 'Forgetting to divide by repeats.', 'Counting rotations as different around a table.', 'Adding instead of multiplying combinations in conditions.'],
        'real_world': 'Lotto odds are combinations: choosing 6 numbers from 52 gives C(52, 6) = 20 358 520 possible tickets.',
        'exam_strategy': 'Write "order matters" or "order doesn\'t matter" next to each count; it prevents the most common error.',
        'recap': ['Order matters: P.', 'Order doesn\'t: C.', 'Divide by repeats.', 'Stars and bars.']},
    T3: {
        'overview': 'Binomial coefficients count selections and also give the coefficients in expansions of (a + b)ⁿ.',
        'key_terms': ['Binomial theorem', 'Binomial coefficient', 'Pascal\'s triangle', 'Pascal\'s identity', 'Symmetry'],
        'explanation': [
            '(a + b)ⁿ = Σₖ C(n, k)aⁿ⁻ᵏbᵏ, with n + 1 terms. The coefficient of x³ in (1 + x)⁷ is C(7, 3) = 35. In (2x + 1)⁵, the x² term is C(5, 2)(2x)² = 10 × 4x² = 40x².',
            'Pascal\'s triangle builds the coefficients row by row: each entry is the sum of the two above it, which is Pascal\'s identity C(n, k) = C(n − 1, k − 1) + C(n − 1, k). The triangle is symmetric: C(n, k) = C(n, n − k).',
            'Setting a = b = 1 gives Σₖ C(n, k) = 2ⁿ: row 6 adds to 64, which is the number of subsets of a 6-element set.'],
        'formulas_label': 'Formulas',
        'formulas': ['(a + b)ⁿ = Σ C(n, k)aⁿ⁻ᵏbᵏ', 'C(n, k) = C(n − 1, k − 1) + C(n − 1, k)', 'C(n, k) = C(n, n − k)', 'Σ C(n, k) = 2ⁿ'],
        'steps': ['Identify a, b and n.', 'Write the general term C(n, k)aⁿ⁻ᵏbᵏ.', 'Choose k to get the required power.', 'Include the constants raised to powers.'],
        'worked_example': {
            'problem': 'Find the coefficient of x² in (2x + 1)⁵.',
            'steps': ['General term: C(5, k)(2x)ᵏ(1)⁵⁻ᵏ.', 'For x², k = 2: C(5, 2) × 2² = 10 × 4.', '= 40.'],
            'answer': '40.',
            'check': 'Expanding by computer gives 40x² ✓.'},
        'mistakes': ['Forgetting to raise the coefficient (2) to the power.', 'Off-by-one errors in k.', 'Thinking there are n terms instead of n + 1.', 'Mixing up rows of Pascal\'s triangle.'],
        'real_world': 'In probability, the binomial distribution P(X = k) = C(n, k)pᵏ(1 − p)ⁿ⁻ᵏ uses these coefficients directly.',
        'exam_strategy': 'Write the general term first; then the required k is a one-line equation.',
        'recap': ['General term.', 'Pascal\'s identity.', 'Symmetry.', 'Rows sum to 2ⁿ.']},
    T4: {
        'overview': 'The pigeonhole principle guarantees repeats; inclusion–exclusion counts unions exactly.',
        'key_terms': ['Pigeonhole principle', 'Generalised pigeonhole', 'Inclusion–exclusion', 'Derangement', 'Complement counting'],
        'explanation': [
            'If more than n objects go into n boxes, some box gets at least two. Among 13 people, two share a birth month; among 367 people, two share a birthday. Generalised: N objects in k boxes put at least ⌈N/k⌉ in some box: 25 objects in 6 boxes put at least 5 in one.',
            'Inclusion–exclusion: |A ∪ B| = |A| + |B| − |A ∩ B|. Numbers from 1 to 100 divisible by 2 or 3: 50 + 33 − 16 = 67. For three sets, add back the triple intersection: |A ∪ B ∪ C| = Σ|A| − Σ|A ∩ B| + |A ∩ B ∩ C|. So the numbers from 1 to 100 divisible by none of 2, 3, 5 number 26.',
            'A derangement is a permutation with no element in its original place. Inclusion–exclusion gives 9 derangements of 4 items: for example, 4 letters put into 4 envelopes all wrongly.'],
        'formulas_label': 'Formulas',
        'formulas': ['Pigeonhole: N > k ⇒ some box has ≥ 2', 'Generalised: some box has ≥ ⌈N/k⌉', '|A ∪ B ∪ C| = |A| + |B| + |C| − |A∩B| − |A∩C| − |B∩C| + |A∩B∩C|', 'Derangements Dₙ = n! Σ (−1)ᵏ/k!'],
        'steps': ['Identify the boxes and the objects.', 'Apply ⌈N/k⌉.', 'For unions, list single, pairwise and triple counts.', 'Use complements ("none of") when easier.'],
        'worked_example': {
            'problem': 'How many integers from 1 to 100 are divisible by 2 or 3?',
            'steps': ['Divisible by 2: 50; by 3: 33.', 'Divisible by both (by 6): 16.', '50 + 33 − 16 = 67.'],
            'answer': '67.',
            'check': 'A direct count by computer gives 67 ✓.'},
        'mistakes': ['Forgetting to subtract the overlap.', 'Forgetting to add back the triple intersection.', 'Using ⌊N/k⌋ instead of ⌈N/k⌉.', 'Applying pigeonhole when N ≤ k.'],
        'real_world': 'Pigeonhole explains why hash tables must handle collisions: with more possible keys than slots, two keys must share a slot.',
        'exam_strategy': 'For pigeonhole proofs, state clearly what the pigeons and the holes are; that is most of the marks.',
        'recap': ['N > k ⇒ repeat.', '⌈N/k⌉.', 'Inclusion–exclusion.', 'Derangements.']},
}

QUESTIONS = [
    # T1
    Q(T1, '3 shirts and 4 pairs of trousers give how many outfits?', ['12', '7', '81', '64'], 0, 'Product rule.', ans=12),
    Q(T1, 'How many 4-digit PINs are there (digits 0-9, repeats allowed)?', ['10000', '5040', '9999', '40'], 0, '10⁴.', ans=10000),
    Q(T1, 'How many bit strings of length 8 are there?', ['256', '16', '64', '8'], 0, '2⁸.', ans=256),
    Q(T1, 'Number plates with 3 letters then 3 digits:', ['17576000', '11232000', '1757600', '676000'], 0, '26³ × 10³.', ans=17576000),
    Q(T1, 'Choosing one book from 5 novels or 7 textbooks gives:', ['12', '35', '2', '7'], 0, 'Sum rule.', ans=12),
    Q(T1, 'A 4-digit PIN that cannot start with 0:', ['9000', '10000', '9999', '1000'], 0, '9 × 10³.', ans=9000),
    # T2
    Q(T2, 'President, secretary and treasurer from 5 people:', ['60', '10', '125', '15'], 0, 'P(5, 3).', ans=60),
    Q(T2, 'A committee of 3 from 10 people:', ['120', '720', '30', '1000'], 0, 'C(10, 3).', ans=120),
    Q(T2, 'Arrangements of the letters of BANANA:', ['60', '720', '120', '36'], 0, '6!/(3! 2!).', ans=60),
    Q(T2, 'Committees of 2 women (from 4) and 1 man (from 5):', ['30', '20', '60', '9'], 0, 'C(4, 2) × C(5, 1).', ans=30),
    Q(T2, 'Ways to share 10 identical sweets among 3 children:', ['66', '30', '120', '59049'], 0, 'C(12, 2).', ans=66),
    Q(T2, 'Ways to seat 5 people around a round table:', ['24', '120', '5', '60'], 0, '(5 − 1)!.', ans=24),
    # T3
    Q(T3, 'The coefficient of x³ in (1 + x)⁷ is:', ['35', '21', '7', '343'], 0, 'C(7, 3).', ans=35),
    Q(T3, 'The coefficient of x² in (2x + 1)⁵ is:', ['40', '10', '20', '80'], 0, 'C(5, 2) × 2².', ans=40),
    Q(T3, 'The entries of row 6 of Pascal\'s triangle sum to:', ['64', '32', '21', '36'], 0, '2⁶.', ans=64),
    Q(T3, 'How many terms does (x + y)⁴ have?', ['5', '4', '8', '16'], 0, 'n + 1.', ans=5),
    Q(T3, 'C(9, 4) equals:', ['C(8, 3) + C(8, 4)', 'C(8, 4) + C(8, 5)', 'C(9, 3) + C(9, 5)', '2C(8, 4)'], 0, 'Pascal\'s identity.'),
    Q(T3, 'C(n, k) always equals:', ['C(n, n − k)', 'C(n, k + 1)', 'C(n − k, k)', 'n!/k!'], 0, 'Symmetry.'),
    # T4
    Q(T4, 'The smallest group guaranteed to contain two people born in the same month has:', ['13 people', '12 people', '24 people', '366 people'], 0, '12 months + 1.'),
    Q(T4, '25 objects in 6 boxes: some box must contain at least:', ['5', '4', '6', '3'], 0, '⌈25/6⌉.', ans=5),
    Q(T4, 'Integers from 1 to 100 divisible by 2 or 3:', ['67', '83', '50', '66'], 0, '50 + 33 − 16.', ans=67),
    Q(T4, 'Integers from 1 to 100 divisible by none of 2, 3, 5:', ['26', '74', '30', '20'], 0, '100 − 74 by inclusion–exclusion.', ans=26),
    Q(T4, 'The number of derangements of 4 items is:', ['9', '24', '6', '11'], 0, '4!(1 − 1 + 1/2 − 1/6 + 1/24).', ans=9),
    Q(T4, 'For three sets, inclusion–exclusion adds back:', ['the triple intersection', 'the pairwise intersections', 'the complements', 'nothing'], 0, '+|A ∩ B ∩ C|.'),
]

FLASH = [
    ['Product rule', 'Stages multiply: m ways then n ways = mn.'],
    ['Sum rule', 'Disjoint cases add.'],
    ['Permutation', 'P(n, r) = n!/(n − r)!; order matters.'],
    ['Combination', 'C(n, r) = n!/(r!(n − r)!); order does not matter.'],
    ['Stars and bars', 'k identical items in n boxes: C(k + n − 1, n − 1).'],
    ['Binomial theorem', '(a + b)ⁿ = Σ C(n, k)aⁿ⁻ᵏbᵏ.'],
    ['Pigeonhole principle', 'N objects in k boxes: some box has at least ⌈N/k⌉.'],
    ['Derangement', 'Permutation with no element in its original place.'],
]
