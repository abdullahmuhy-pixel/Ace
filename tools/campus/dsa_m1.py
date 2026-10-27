"""Data Structures and Algorithms, module 1: Analysing algorithms."""
import math
from verify import Q, n, sp
from py_common import check
T1, T2, T3, T4 = ('Big-O notation', 'Counting the work in loops and recursion', 'Recurrences and the master theorem', 'Space and amortised analysis')
assert sp.limit((3 * n ** 2 + 5 * n + 2) / n ** 2, n, sp.oo) == 3 and math.ceil(math.log2(1_000_000)) == 20
check('c=0\nfor i in range(10):\n    for j in range(10):\n        c+=1\nprint(c)', 100)
check('c=0\nfor i in range(10):\n    for j in range(i):\n        c+=1\nprint(c)', 45)
check('c=0\ni=1\nwhile i<1024:\n    i*=2\n    c+=1\nprint(c)', 10)
check('c=0\nfor i in range(10):\n    c+=1\nfor j in range(10):\n    c+=1\nprint(c)', 20)
check('calls=0\ndef f(k):\n    global calls\n    calls+=1\n    return k if k<2 else f(k-1)+f(k-2)\nf(10)\nprint(calls)', 177)
check('copies=0\ncap=1\nsize=0\nfor x in range(1000):\n    if size==cap:\n        copies+=size\n        cap*=2\n    size+=1\nprint(copies)', 1023)
assert (2 * 1000) ** 2 / 1000 ** 2 == 4 and round(2 * 2000 * math.log(2000) / (1000 * math.log(1000)), 1) == 4.4

MODULE = {
    'title': 'Analysing algorithms',
    'topics': [T1, T2, T3, T4],
    'overview': 'Before choosing a data structure or algorithm, we need to measure how its cost grows with the input. This module covers Big-O notation, counting operations in loops and recursion, solving recurrences with the master theorem, and analysing memory use and amortised cost.',
    'key_terms': ['Running time', 'Big-O', 'Big-Ω', 'Big-Θ', 'Growth rate', 'Nested loop', 'Logarithmic loop', 'Recursion tree', 'Recurrence', 'Master theorem', 'Space complexity', 'Amortised cost'],
    'explanation': [
        'We describe running time by how it grows with the input size n, ignoring constant factors and smaller terms: 3n² + 5n + 2 is O(n²). The common classes, from fastest to slowest growth, are O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ) and O(n!).',
        'Loops multiply: a loop inside a loop over n items costs n²; a loop that halves or doubles its variable runs about log₂ n times. Recursive algorithms are described by recurrences such as T(n) = 2T(n/2) + n, which the master theorem solves directly.',
        'Memory matters too: recursion uses stack space proportional to its depth. Some operations are expensive occasionally but cheap on average, like appending to a dynamic array; amortised analysis captures this average over a sequence of operations.'],
    'quick_facts': [
        'Drop constants and lower-order terms: 5n² + 100n = O(n²).',
        'Nested loops over n: O(n²); halving loop: O(log n).',
        'T(n) = 2T(n/2) + n ⇒ O(n log n); T(n) = T(n/2) + 1 ⇒ O(log n).',
        'Binary search on 1 000 000 items: about 20 comparisons.',
        'Dynamic array append: O(1) amortised.'],
}

NOTES = {
    T1: {
        'overview': 'Big-O notation describes how an algorithm\'s cost grows, which matters far more than its speed on small inputs.',
        'key_terms': ['Asymptotic analysis', 'Big-O (upper bound)', 'Big-Ω (lower bound)', 'Big-Θ (tight bound)', 'Dominant term', 'Growth classes'],
        'explanation': [
            'f(n) = O(g(n)) means that for large n, f(n) ≤ c·g(n) for some constant c. We keep only the dominant term and drop constants: 3n² + 5n + 2 = O(n²), because 3n² dominates as n grows. Θ means the bound is tight (both upper and lower).',
            'Growth order: 1 < log n < n < n log n < n² < n³ < 2ⁿ < n!. An O(n²) algorithm takes about 4 times as long when the input doubles; an O(n log n) one only slightly more than twice as long.',
            'Logarithms appear whenever a problem is halved repeatedly: binary search on 1 000 000 sorted items needs about log₂(10⁶) ≈ 20 comparisons, compared with up to 1 000 000 for a linear scan.'],
        'formulas_label': 'Growth classes',
        'formulas': ['O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)', 'f = O(g): f ≤ c·g for large n', 'Doubling n: O(n) ×2, O(n²) ×4, O(n³) ×8', 'log₂(10⁶) ≈ 20'],
        'steps': ['Find the dominant term.', 'Drop constant factors.', 'Name the growth class.', 'Compare algorithms by class, not by small-n timings.'],
        'worked_example': {
            'problem': 'An O(n²) algorithm takes 2 seconds for n = 1000. Estimate the time for n = 2000.',
            'steps': ['Time ≈ c·n².', 'Doubling n multiplies n² by 4.', '2 s × 4 = 8 s.'],
            'answer': 'About 8 seconds.',
            'check': 'An O(n log n) algorithm would take only about 4.4 s; this is why growth rate matters ✓.'},
        'mistakes': ['Keeping constants (O(3n)).', 'Thinking O(n log n) is slower than O(n²).', 'Confusing O (upper bound) with Θ (exact).', 'Judging by tiny inputs.'],
        'real_world': 'Search engines handle billions of pages only because their core operations run in O(log n) or O(1) time.',
        'exam_strategy': 'Memorise the growth order line; many multiple-choice questions just test it.',
        'recap': ['Dominant term only.', 'Drop constants.', 'Know the order.', 'Logs come from halving.']},
    T2: {
        'overview': 'To find the running time of code, count how many times the innermost operation runs.',
        'key_terms': ['Sequential code', 'Nested loops', 'Dependent loops', 'Logarithmic loops', 'Recursive calls', 'Recursion tree'],
        'explanation': [
            'Sequential blocks add: two separate loops of n run 2n times = O(n). Nested loops multiply: two loops of n run n² times (100 for n = 10). A dependent inner loop "for j in range(i)" runs 0 + 1 + … + (n − 1) = n(n − 1)/2 times (45 for n = 10), still O(n²).',
            'A loop whose variable doubles (i = 1, 2, 4, …) or halves runs about log₂ n times: up to 1024 it runs 10 times. A loop of n containing a halving loop costs O(n log n).',
            'Recursive code is analysed by counting calls. Naive recursive Fibonacci calls itself twice per level, so the number of calls grows exponentially: computing F(10) makes 177 calls. Storing results (memoisation) brings this down to O(n).'],
        'formulas_label': 'Patterns',
        'formulas': ['Sequential: add', 'Nested: multiply', 'Σᵢ₌₀ⁿ⁻¹ i = n(n − 1)/2 = O(n²)', 'Doubling/halving loop: O(log n)', 'Naive Fibonacci: O(φⁿ), φ ≈ 1.618'],
        'steps': ['Find the most deeply nested operation.', 'Count iterations of each loop.', 'Multiply nested counts, add sequential ones.', 'Simplify to Big-O.'],
        'worked_example': {
            'problem': 'How many times does c += 1 run in: for i in range(n): for j in range(i): c += 1?',
            'steps': ['For i = 0, 1, …, n − 1 the inner loop runs i times.', 'Total = 0 + 1 + … + (n − 1) = n(n − 1)/2.', 'For n = 10: 45. Big-O: O(n²).'],
            'answer': 'n(n − 1)/2 times; O(n²).',
            'check': 'Running the code for n = 10 prints 45 ✓.'},
        'mistakes': ['Thinking a dependent inner loop makes it O(n).', 'Missing the log in doubling loops.', 'Adding nested loops instead of multiplying.', 'Underestimating naive recursion.'],
        'real_world': 'Comparing every pair of users to find duplicates is O(n²): fine for 1000 users, impossible for 100 million, which is why companies use hashing instead.',
        'exam_strategy': 'Write the iteration count of each loop beside it in the code before combining them.',
        'recap': ['Add sequential.', 'Multiply nested.', 'Doubling ⇒ log.', 'Count recursive calls.']},
    T3: {
        'overview': 'Divide-and-conquer algorithms have running times described by recurrences. The master theorem solves the common ones.',
        'key_terms': ['Recurrence', 'Divide and conquer', 'Recursion tree', 'Master theorem', 'Subproblems', 'Combine cost'],
        'explanation': [
            'For T(n) = aT(n/b) + f(n): a subproblems, each of size n/b, plus f(n) work to split and combine. Compare f(n) with n^(log_b a). If f grows slower, T = Θ(n^(log_b a)); if they match, T = Θ(n^(log_b a) log n); if f grows faster (and is regular), T = Θ(f(n)).',
            'Merge sort: T(n) = 2T(n/2) + n. Here n^(log₂2) = n matches f(n) = n, so T = Θ(n log n). Binary search: T(n) = T(n/2) + 1, with n⁰ = 1 matching, so Θ(log n).',
            'T(n) = 4T(n/2) + n: n^(log₂4) = n² grows faster than n, so Θ(n²). T(n) = 2T(n/2) + 1: n¹ beats 1, so Θ(n). Recurrences that subtract, like T(n) = T(n − 1) + n, are not covered by the master theorem; unrolling gives n + (n − 1) + … = Θ(n²).'],
        'formulas_label': 'Master theorem (T(n) = aT(n/b) + f(n))',
        'formulas': ['Compare f(n) with n^(log_b a)', 'f smaller: Θ(n^(log_b a))', 'f equal: Θ(n^(log_b a) log n)', 'f larger: Θ(f(n))', 'T(n) = T(n − 1) + n ⇒ Θ(n²)'],
        'steps': ['Identify a, b and f(n).', 'Compute n^(log_b a).', 'Compare it with f(n).', 'Pick the case and state Θ.'],
        'worked_example': {
            'problem': 'Solve T(n) = 4T(n/2) + n.',
            'steps': ['a = 4, b = 2, f(n) = n.', 'n^(log₂4) = n².', 'n grows slower than n², so T(n) = Θ(n²).'],
            'answer': 'Θ(n²).',
            'check': 'The recursion tree has 4ᵏ nodes at level k doing n/2ᵏ work each: the bottom level dominates with about n² work ✓.'},
        'mistakes': ['Computing log_b a upside down.', 'Applying the master theorem to T(n − 1) recurrences.', 'Forgetting the log factor when the terms match.', 'Mixing up a and b.'],
        'real_world': 'Fast multiplication algorithms (Karatsuba, used in big-number libraries) beat the schoolbook O(n²) method by solving T(n) = 3T(n/2) + n, giving about n^1.585.',
        'exam_strategy': 'Write "a = …, b = …, f(n) = …, n^(log_b a) = …" as the first line every time.',
        'recap': ['a, b, f(n).', 'Compare with n^(log_b a).', 'Three cases.', 'Subtractive recurrences: unroll.']},
    T4: {
        'overview': 'Algorithms also use memory, and some operations are expensive rarely but cheap on average.',
        'key_terms': ['Space complexity', 'Auxiliary space', 'In-place algorithm', 'Call stack', 'Recursion depth', 'Amortised analysis', 'Dynamic array', 'Doubling strategy'],
        'explanation': [
            'Space complexity counts extra memory. An n × n matrix uses Θ(n²) space. An in-place algorithm uses O(1) extra space. Recursion uses stack space proportional to its maximum depth: recursive factorial(n) uses O(n) stack, which is why very deep recursion can crash with a stack overflow.',
            'A dynamic array (like a Python list) doubles its capacity when full. A single append that triggers a resize copies every element, O(n), but resizes are rare: appending 1000 items copies only 1 + 2 + 4 + … + 512 = 1023 elements in total, fewer than 2n.',
            'So the amortised cost per append is O(1). Amortised analysis averages over a sequence of operations, which gives a guaranteed bound on the total, unlike an average over random inputs.'],
        'formulas_label': 'Key facts',
        'formulas': ['n × n matrix: Θ(n²) space', 'Recursion: O(depth) stack space', 'Doubling array: total copies < 2n', 'Append: O(1) amortised, O(n) worst case'],
        'steps': ['Count the largest extra data structures.', 'Add the maximum recursion depth.', 'For amortised cost, sum over n operations and divide by n.', 'Distinguish worst-case per operation from amortised.'],
        'worked_example': {
            'problem': 'A dynamic array starts with capacity 1 and doubles when full. How many element copies happen while appending 1000 items?',
            'steps': ['Resizes happen at sizes 1, 2, 4, …, 512.', 'Copies: 1 + 2 + 4 + … + 512 = 1023.', 'Per append: about 1, so O(1) amortised.'],
            'answer': '1023 copies.',
            'check': 'Simulating the array in code gives 1023 ✓.'},
        'mistakes': ['Ignoring recursion stack space.', 'Saying each append is O(1) in the worst case.', 'Confusing amortised with average-case.', 'Growing arrays by a constant instead of doubling (O(n²) total).'],
        'real_world': 'Python lists, Java ArrayLists and C++ vectors all grow by a constant factor for exactly this amortised O(1) append.',
        'exam_strategy': 'When asked for amortised cost, compute the total cost of n operations explicitly, then divide by n.',
        'recap': ['Count extra memory.', 'Stack depth counts.', 'Doubling arrays.', 'Amortised O(1).']},
}

QUESTIONS = [
    # T1
    Q(T1, '3n² + 5n + 2 is:', ['O(n²)', 'O(n)', 'O(n³)', 'O(1)'], 0, 'Dominant term.'),
    Q(T1, 'Which grows fastest?', ['2ⁿ', 'n³', 'n log n', 'n²'], 0, 'Exponential beats polynomial.'),
    Q(T1, 'An O(n²) algorithm takes 2 s for n = 1000. For n = 2000 it takes about:', ['8 s', '4 s', '16 s', '2 s'], 0, 'Doubling n ×4.'),
    Q(T1, 'Binary search on 1 000 000 sorted items needs about how many comparisons?', ['20', '1000', '500000', '100'], 0, 'log₂ 10⁶.', ans=20),
    Q(T1, 'Which list is in increasing order of growth?', ['log n, n, n log n, n²', 'n, log n, n², n log n', 'n log n, n, log n, n²', 'n², n log n, n, log n'], 0, 'Standard order.'),
    Q(T1, 'f(n) = Θ(g(n)) means g is:', ['both an upper and a lower bound', 'only an upper bound', 'only a lower bound', 'the exact running time in seconds'], 0, 'Tight bound.'),
    # T2
    Q(T2, 'for i in range(10): for j in range(10): c += 1 — how many times does c += 1 run?', ['100', '20', '10', '55'], 0, '10 × 10.', ans=100),
    Q(T2, 'for i in range(10): for j in range(i): c += 1 — how many times?', ['45', '55', '100', '10'], 0, '0 + 1 + … + 9.', ans=45),
    Q(T2, 'i = 1; while i < 1024: i *= 2 — how many iterations?', ['10', '1024', '512', '11'], 0, 'log₂ 1024.', ans=10),
    Q(T2, 'Two separate (not nested) loops of n iterations are:', ['O(n)', 'O(n²)', 'O(2ⁿ)', 'O(log n)'], 0, 'They add: 2n.'),
    Q(T2, 'Naive recursive Fibonacci makes how many calls to compute F(10)?', ['177', '10', '55', '89'], 0, 'Counted by running the code.', ans=177),
    Q(T2, 'A loop over n containing a doubling loop up to n is:', ['O(n log n)', 'O(n²)', 'O(log n)', 'O(n)'], 0, 'n × log n.'),
    # T3
    Q(T3, 'T(n) = 2T(n/2) + n solves to:', ['Θ(n log n)', 'Θ(n)', 'Θ(n²)', 'Θ(log n)'], 0, 'Merge sort.'),
    Q(T3, 'T(n) = T(n/2) + 1 solves to:', ['Θ(log n)', 'Θ(n)', 'Θ(1)', 'Θ(n log n)'], 0, 'Binary search.'),
    Q(T3, 'T(n) = 4T(n/2) + n solves to:', ['Θ(n²)', 'Θ(n log n)', 'Θ(n)', 'Θ(n⁴)'], 0, 'n^(log₂4) = n².'),
    Q(T3, 'T(n) = 2T(n/2) + 1 solves to:', ['Θ(n)', 'Θ(log n)', 'Θ(n log n)', 'Θ(1)'], 0, 'n¹ dominates 1.'),
    Q(T3, 'T(n) = T(n − 1) + n solves to:', ['Θ(n²)', 'Θ(n)', 'Θ(n log n)', 'Θ(2ⁿ)'], 0, 'n + (n − 1) + … + 1.'),
    Q(T3, 'In the master theorem, f(n) is compared with:', ['n^(log_b a)', 'n^(log_a b)', 'a·b', 'log n'], 0, 'Critical exponent.'),
    # T4
    Q(T4, 'Appending 1000 items to a doubling array starting at capacity 1 copies how many elements?', ['1023', '1000', '2000', '512'], 0, '1 + 2 + … + 512.', ans=1023),
    Q(T4, 'The amortised cost of appending to a doubling dynamic array is:', ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'], 0, 'Copies average out.'),
    Q(T4, 'Recursive factorial(n) uses stack space:', ['O(n)', 'O(1)', 'O(log n)', 'O(n²)'], 0, 'n frames deep.'),
    Q(T4, 'An n × n matrix needs space:', ['Θ(n²)', 'Θ(n)', 'Θ(2n)', 'Θ(log n)'], 0, 'n² entries.'),
    Q(T4, 'An in-place sorting algorithm uses extra space:', ['O(1)', 'O(n)', 'O(n²)', 'O(n log n)'], 0, 'Constant extra memory.'),
    Q(T4, 'Growing an array by a fixed 10 slots each time makes n appends cost:', ['O(n²) in total', 'O(n) in total', 'O(log n) in total', 'O(1) in total'], 0, 'Copies grow linearly each resize.'),
]

FLASH = [
    ['Big-O', 'Upper bound on growth, ignoring constants and lower terms.'],
    ['Growth order', '1 < log n < n < n log n < n² < 2ⁿ < n!.'],
    ['Nested loops', 'Multiply iteration counts.'],
    ['Doubling loop', 'Runs about log₂ n times.'],
    ['Master theorem', 'T(n) = aT(n/b) + f(n): compare f with n^(log_b a).'],
    ['Merge sort recurrence', 'T(n) = 2T(n/2) + n ⇒ Θ(n log n).'],
    ['Recursion space', 'Stack space proportional to recursion depth.'],
    ['Amortised O(1)', 'Dynamic array append: rare O(n) resizes average out.'],
]
