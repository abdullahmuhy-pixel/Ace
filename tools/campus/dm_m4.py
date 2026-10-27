"""Discrete Mathematics and Logic, module 4: Number theory and recurrences."""
import math
from verify import Q, n, sp
T1, T2, T3, T4 = ('Divisibility and modular arithmetic', 'GCD, the Euclidean algorithm and primes', 'Recurrence relations', 'Modular inverses and RSA')
assert 17 % 5 == 2 and -7 % 3 == 2 and pow(3, 100, 7) == 4 and (25 * 37) % 7 == 1 and pow(7, 2026, 10) == 9 and (4 * 6) % 7 == 3
assert 3 * 5 + 7 * -2 == 1 and math.gcd(252, 105) == 21 and math.lcm(12, 18) == 36 and 252 * -2 + 105 * 5 == 21 and pow(3, -1, 7) == 5
assert sp.factorint(360) == {2: 3, 3: 2, 5: 1} and sp.divisor_count(360) == 24 and sp.isprime(97) and not sp.isprime(91)
a = [0]
for _ in range(5): a.append(2 * a[-1] + 1)
assert a == [0, 1, 3, 7, 15, 31] and 2 ** 5 - 1 == 31
F = [0, 1]
for _ in range(9): F.append(F[-1] + F[-2])
assert F[10] == 55
b = [1, 4]
for _ in range(4): b.append(5 * b[-1] - 6 * b[-2])
assert b == [-(2 ** k) + 2 * 3 ** k for k in range(6)] and b[2] == 14
assert sp.totient(15) == 8 and pow(4, 3, 33) == 31 and pow(31, 7, 33) == 4 and pow(3, -1, 20) == 7 and pow(2, 10, 11) == 1

MODULE = {
    'title': 'Number theory and recurrences',
    'topics': [T1, T2, T3, T4],
    'overview': 'Integers have a rich structure that powers modern computing. This module covers modular arithmetic, greatest common divisors and primes, recurrence relations that describe step-by-step processes, and the modular inverses behind RSA encryption.',
    'key_terms': ['Divides', 'Remainder', 'Congruence', 'Modular arithmetic', 'GCD', 'LCM', 'Euclidean algorithm', 'Bézout identity', 'Prime', 'Fundamental theorem of arithmetic', 'Recurrence relation', 'Characteristic equation', 'Modular inverse', 'Euler\'s totient', 'RSA'],
    'explanation': [
        'Modular arithmetic works with remainders: a ≡ b (mod n) when n divides a − b. You can add, subtract and multiply and reduce at any step, which makes huge powers like 3¹⁰⁰ mod 7 easy.',
        'The Euclidean algorithm finds gcd(a, b) quickly by repeated division, and running it backwards writes the gcd as ax + by. Every integer above 1 factors uniquely into primes.',
        'Recurrences define sequences from earlier terms, like algorithm running times or Fibonacci numbers. Linear recurrences with constant coefficients are solved with a characteristic equation, just like differential equations. RSA encryption combines primes, Euler\'s totient and modular inverses.'],
    'quick_facts': [
        'a mod n is the remainder in 0, …, n − 1 (−7 mod 3 = 2).',
        'gcd(a, b) = gcd(b, a mod b).',
        'gcd(a, b) × lcm(a, b) = ab.',
        'aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ ⇒ r² = c₁r + c₂.',
        'RSA: n = pq, φ = (p − 1)(q − 1), ed ≡ 1 (mod φ).'],
}

NOTES = {
    T1: {
        'overview': 'Modular arithmetic is arithmetic with remainders, used in clocks, check digits and cryptography.',
        'key_terms': ['Division algorithm', 'Remainder', 'a mod n', 'Congruence ≡', 'Cycles of powers', 'Fermat\'s little theorem'],
        'explanation': [
            'For any integers a and n > 0, a = qn + r with 0 ≤ r < n; r = a mod n. So 17 mod 5 = 2, and −7 mod 3 = 2 (since −7 = −3 × 3 + 2).',
            'You may reduce before or after any addition or multiplication: (25 × 37) mod 7 = (4 × 2) mod 7 = 1. Powers cycle: 7¹, 7², 7³, 7⁴ end in 7, 9, 3, 1, so 7²⁰²⁶ ends in 9 (2026 ≡ 2 mod 4).',
            'Fermat\'s little theorem: if p is prime and p ∤ a, then aᵖ⁻¹ ≡ 1 (mod p). So 3⁶ ≡ 1 (mod 7), and 3¹⁰⁰ = 3⁹⁶ × 3⁴ ≡ 3⁴ = 81 ≡ 4 (mod 7). Similarly 2¹⁰ ≡ 1 (mod 11).'],
        'formulas_label': 'Rules',
        'formulas': ['a = qn + r, 0 ≤ r < n', '(a + b) mod n = ((a mod n) + (b mod n)) mod n', '(ab) mod n = ((a mod n)(b mod n)) mod n', 'Fermat: aᵖ⁻¹ ≡ 1 (mod p) for prime p ∤ a'],
        'steps': ['Reduce each number mod n first.', 'Look for a power that is ≡ 1 (a cycle).', 'Write the exponent as (cycle length) × q + r.', 'Compute the small remaining power.'],
        'worked_example': {
            'problem': 'Find 3¹⁰⁰ mod 7.',
            'steps': ['By Fermat, 3⁶ ≡ 1 (mod 7).', '100 = 6 × 16 + 4, so 3¹⁰⁰ ≡ 3⁴ (mod 7).', '3⁴ = 81 = 11 × 7 + 4, so 3¹⁰⁰ ≡ 4.'],
            'answer': '4.',
            'check': 'A computer gives pow(3, 100, 7) = 4 ✓.'},
        'mistakes': ['Giving negative remainders (−1 instead of n − 1).', 'Reducing exponents mod n instead of mod the cycle length.', 'Applying Fermat when p divides a.', 'Forgetting to reduce intermediate results.'],
        'real_world': 'ID numbers and barcodes use mod-10 or mod-11 check digits so that a single mistyped digit is detected.',
        'exam_strategy': 'Find the cycle of powers first; it turns any large-power question into a small one.',
        'recap': ['Remainders 0 to n − 1.', 'Reduce at every step.', 'Powers cycle.', 'Fermat\'s little theorem.']},
    T2: {
        'overview': 'The greatest common divisor and prime factorisation describe how integers share factors.',
        'key_terms': ['GCD', 'LCM', 'Euclidean algorithm', 'Bézout\'s identity', 'Prime', 'Composite', 'Prime factorisation', 'Number of divisors'],
        'explanation': [
            'The Euclidean algorithm repeats gcd(a, b) = gcd(b, a mod b): gcd(252, 105) → gcd(105, 42) → gcd(42, 21) → gcd(21, 0) = 21. Working backwards gives Bézout\'s identity: 21 = 252 × (−2) + 105 × 5.',
            'gcd(a, b) × lcm(a, b) = ab, so lcm(12, 18) = 12 × 18/6 = 36. A number p > 1 is prime if its only positive divisors are 1 and p: 97 is prime, 91 = 7 × 13 is not.',
            'The fundamental theorem of arithmetic: every integer > 1 is a product of primes in exactly one way. 360 = 2³ × 3² × 5, so it has (3 + 1)(2 + 1)(1 + 1) = 24 divisors.'],
        'formulas_label': 'Formulas',
        'formulas': ['gcd(a, b) = gcd(b, a mod b)', 'gcd(a, b) = ax + by (Bézout)', 'gcd × lcm = ab', 'n = p₁^e₁ … pₖ^eₖ ⇒ (e₁ + 1)…(eₖ + 1) divisors'],
        'steps': ['Divide and keep the remainder until it is 0.', 'The last non-zero remainder is the gcd.', 'Back-substitute for Bézout coefficients.', 'Factorise by trying primes up to √n.'],
        'worked_example': {
            'problem': 'Find gcd(252, 105) and write it as 252x + 105y.',
            'steps': ['252 = 2 × 105 + 42; 105 = 2 × 42 + 21; 42 = 2 × 21 + 0, so gcd = 21.', '21 = 105 − 2 × 42 = 105 − 2(252 − 2 × 105).', '= 5 × 105 − 2 × 252.'],
            'answer': 'gcd = 21 = 252(−2) + 105(5).',
            'check': '−504 + 525 = 21 ✓.'},
        'mistakes': ['Stopping at the wrong remainder.', 'Sign errors in back-substitution.', 'Thinking 1 is prime.', 'Testing divisibility beyond √n unnecessarily.'],
        'real_world': 'Reducing fractions to lowest terms and syncing repeating events (lcm of their periods) both use gcd and lcm.',
        'exam_strategy': 'Set out the Euclidean algorithm as a table of a = qb + r lines; back-substitution then reads off directly.',
        'recap': ['Euclid: repeated remainders.', 'Bézout identity.', 'gcd × lcm = ab.', 'Unique prime factorisation.']},
    T3: {
        'overview': 'A recurrence relation defines each term from earlier terms. Solving it gives a closed formula.',
        'key_terms': ['Recurrence relation', 'Initial conditions', 'Closed form', 'Linear homogeneous recurrence', 'Characteristic equation', 'Fibonacci sequence', 'Tower of Hanoi'],
        'explanation': [
            'Tower of Hanoi: moving n discs takes aₙ = 2aₙ₋₁ + 1 moves with a₀ = 0, giving 0, 1, 3, 7, 15, 31, …, so aₙ = 2ⁿ − 1 (31 moves for 5 discs). Fibonacci: Fₙ = Fₙ₋₁ + Fₙ₋₂ with F₀ = 0, F₁ = 1 gives F₁₀ = 55.',
            'For a linear homogeneous recurrence aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, try aₙ = rⁿ to get the characteristic equation r² = c₁r + c₂. For aₙ = 5aₙ₋₁ − 6aₙ₋₂: r² − 5r + 6 = 0, r = 2, 3, so aₙ = A·2ⁿ + B·3ⁿ.',
            'Initial conditions fix A and B: with a₀ = 1, a₁ = 4, A + B = 1 and 2A + 3B = 4, so B = 2, A = −1 and aₙ = 2·3ⁿ − 2ⁿ. Check: a₂ = 18 − 4 = 14, and 5 × 4 − 6 × 1 = 14 ✓.'],
        'formulas_label': 'Method',
        'formulas': ['aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ ⇒ r² − c₁r − c₂ = 0', 'Distinct roots: aₙ = Ar₁ⁿ + Br₂ⁿ', 'Repeated root r: aₙ = (A + Bn)rⁿ', 'Use initial terms for A, B'],
        'steps': ['Write the characteristic equation.', 'Find its roots.', 'Write the general solution.', 'Use initial conditions; check a later term.'],
        'worked_example': {
            'problem': 'Solve aₙ = 5aₙ₋₁ − 6aₙ₋₂ with a₀ = 1, a₁ = 4.',
            'steps': ['r² − 5r + 6 = 0 ⇒ r = 2, 3.', 'aₙ = A·2ⁿ + B·3ⁿ; A + B = 1, 2A + 3B = 4.', 'B = 2, A = −1: aₙ = 2·3ⁿ − 2ⁿ.'],
            'answer': 'aₙ = 2·3ⁿ − 2ⁿ.',
            'check': 'Terms 1, 4, 14, 46, 146 match the recurrence ✓.'},
        'mistakes': ['Sign errors when moving terms into the characteristic equation.', 'Forgetting the extra n in the repeated-root case.', 'Using the wrong initial index.', 'Not checking a term.'],
        'real_world': 'Divide-and-conquer algorithms such as merge sort are analysed with recurrences like T(n) = 2T(n/2) + n.',
        'exam_strategy': 'Always compute a₂ (or a₃) from both the recurrence and your formula; matching values confirm the answer.',
        'recap': ['Recurrences build terms.', 'Characteristic equation.', 'Fit initial conditions.', 'Check a term.']},
    T4: {
        'overview': 'Modular inverses let you "divide" in modular arithmetic. RSA uses them with large primes to encrypt messages.',
        'key_terms': ['Modular inverse', 'Euler\'s totient φ(n)', 'Euler\'s theorem', 'Public key', 'Private key', 'RSA', 'Encryption', 'Decryption'],
        'explanation': [
            'a has an inverse mod n (a number x with ax ≡ 1) exactly when gcd(a, n) = 1. The inverse of 3 mod 7 is 5, since 15 ≡ 1. Bézout\'s identity finds inverses in general: 3 × 5 + 7 × (−2) = 1 shows that 5 is the inverse of 3 mod 7.',
            'Euler\'s totient φ(n) counts the numbers from 1 to n coprime to n; for n = pq with p, q prime, φ(n) = (p − 1)(q − 1), so φ(15) = 8. Euler\'s theorem: a^φ(n) ≡ 1 (mod n) when gcd(a, n) = 1.',
            'RSA in miniature: p = 3, q = 11, n = 33, φ = 20. Choose e = 3 (coprime to 20); d = 7 since 3 × 7 = 21 ≡ 1 (mod 20). Public key (33, 3), private key 7. Encrypt m = 4: 4³ = 64 ≡ 31 (mod 33). Decrypt: 31⁷ ≡ 4 (mod 33). Real RSA uses primes with hundreds of digits, so factoring n is infeasible.'],
        'formulas_label': 'Formulas',
        'formulas': ['Inverse exists ⇔ gcd(a, n) = 1', 'φ(pq) = (p − 1)(q − 1)', 'Euler: a^φ(n) ≡ 1 (mod n)', 'RSA: c = mᵉ mod n, m = cᵈ mod n, ed ≡ 1 (mod φ(n))'],
        'steps': ['Check gcd(a, n) = 1.', 'Find the inverse by trial (small n) or Euclid.', 'For RSA, compute n, φ, choose e, find d.', 'Encrypt with e, decrypt with d.'],
        'worked_example': {
            'problem': 'With p = 3, q = 11 and e = 3, find d and encrypt and decrypt m = 4.',
            'steps': ['n = 33, φ = 2 × 10 = 20; d = 7 because 3 × 7 = 21 ≡ 1 (mod 20).', 'Encrypt: 4³ = 64 ≡ 31 (mod 33).', 'Decrypt: 31⁷ mod 33 = 4.'],
            'answer': 'd = 7; ciphertext 31; decrypts back to 4.',
            'check': 'Decryption recovers the original message ✓.'},
        'mistakes': ['Choosing e not coprime to φ(n).', 'Computing d mod n instead of mod φ(n).', 'Forgetting that inverses need gcd = 1.', 'Thinking φ(pq) = pq − 1.'],
        'real_world': 'Every secure website connection (the padlock in your browser) relies on public-key cryptography built on these ideas.',
        'exam_strategy': 'Show each RSA quantity on its own line (n, φ, e, d, c, m); examiners mark each step.',
        'recap': ['Inverse needs gcd 1.', 'φ(pq) = (p − 1)(q − 1).', 'd = e⁻¹ mod φ.', 'Encrypt mᵉ, decrypt cᵈ.']},
}

QUESTIONS = [
    # T1
    Q(T1, '17 mod 5 =', ['2', '3', '5', '12'], 0, '17 = 3 × 5 + 2.', ans=2),
    Q(T1, '−7 mod 3 =', ['2', '−1', '1', '−7'], 0, '−7 = −3 × 3 + 2.', ans=2),
    Q(T1, '3¹⁰⁰ mod 7 =', ['4', '1', '3', '6'], 0, '3⁶ ≡ 1, so 3¹⁰⁰ ≡ 3⁴.', ans=4),
    Q(T1, '(25 × 37) mod 7 =', ['1', '2', '4', '0'], 0, '4 × 2 = 8 ≡ 1.', ans=1),
    Q(T1, 'The last digit of 7²⁰²⁶ is:', ['9', '7', '3', '1'], 0, 'Cycle 7, 9, 3, 1; 2026 ≡ 2 mod 4.', ans=9),
    Q(T1, 'By Fermat\'s little theorem, 2¹⁰ mod 11 =', ['1', '0', '2', '10'], 0, 'p = 11.', ans=1),
    # T2
    Q(T2, 'gcd(252, 105) =', ['21', '7', '105', '3'], 0, 'Euclidean algorithm.', ans=21),
    Q(T2, 'lcm(12, 18) =', ['36', '6', '216', '72'], 0, '12 × 18/6.', ans=36),
    Q(T2, 'In 21 = 252x + 105y, a valid pair is:', ['x = −2, y = 5', 'x = 2, y = −5', 'x = 1, y = 1', 'x = −5, y = 2'], 0, 'Back-substitution.'),
    Q(T2, 'The prime factorisation of 360 is:', ['2³ × 3² × 5', '2² × 3³ × 5', '2³ × 3 × 15', '6² × 10'], 0, '8 × 9 × 5.'),
    Q(T2, 'How many positive divisors does 360 have?', ['24', '12', '18', '36'], 0, '(3 + 1)(2 + 1)(1 + 1).', ans=24),
    Q(T2, 'Which number is prime?', ['97', '91', '87', '93'], 0, '91 = 7 × 13, 87 = 3 × 29, 93 = 3 × 31.'),
    # T3
    Q(T3, 'The Tower of Hanoi with 5 discs needs how many moves?', ['31', '32', '25', '15'], 0, '2⁵ − 1.', ans=31),
    Q(T3, 'The closed form of aₙ = 2aₙ₋₁ + 1, a₀ = 0 is:', ['2ⁿ − 1', '2ⁿ', 'n²', '2n − 1'], 0, '0, 1, 3, 7, 15, …', ans=2 ** n - 1),
    Q(T3, 'F₁₀ (with F₀ = 0, F₁ = 1) is:', ['55', '34', '89', '144'], 0, '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.', ans=55),
    Q(T3, 'The characteristic roots of aₙ = 5aₙ₋₁ − 6aₙ₋₂ are:', ['2 and 3', '−2 and −3', '1 and 6', '5 and 6'], 0, 'r² − 5r + 6 = 0.', ans=(2, 3)),
    Q(T3, 'With a₀ = 1, a₁ = 4, the solution is aₙ =', ['2·3ⁿ − 2ⁿ', '3ⁿ + 2ⁿ', '2ⁿ + 3', '4ⁿ'], 0, 'B = 2, A = −1.', ans=2 * 3 ** n - 2 ** n),
    Q(T3, 'For a repeated characteristic root r, the general solution is:', ['(A + Bn)rⁿ', 'Arⁿ + Brⁿ', 'Arⁿ', 'A + Bn'], 0, 'Extra factor n.'),
    # T4
    Q(T4, 'The inverse of 3 modulo 7 is:', ['5', '3', '2', '4'], 0, '3 × 5 = 15 ≡ 1.', ans=5),
    Q(T4, 'φ(15) =', ['8', '14', '15', '6'], 0, '(3 − 1)(5 − 1).', ans=8),
    Q(T4, 'An inverse of a mod n exists exactly when:', ['gcd(a, n) = 1', 'a < n', 'n is prime', 'a is even'], 0, 'Coprime.'),
    Q(T4, 'RSA with n = 33, φ = 20, e = 3 has private key d =', ['7', '3', '11', '13'], 0, '3 × 7 ≡ 1 (mod 20).', ans=7),
    Q(T4, 'Encrypting m = 4 with e = 3, n = 33 gives:', ['31', '64', '12', '4'], 0, '64 mod 33.', ans=31),
    Q(T4, 'RSA is secure because:', ['factoring a product of two huge primes is infeasible', 'modular arithmetic is secret', 'e is kept private', 'n is prime'], 0, 'Hard to recover p and q.'),
]

FLASH = [
    ['a mod n', 'Remainder of a on division by n, from 0 to n − 1.'],
    ['Fermat\'s little theorem', 'aᵖ⁻¹ ≡ 1 (mod p) for prime p not dividing a.'],
    ['Euclidean algorithm', 'gcd(a, b) = gcd(b, a mod b).'],
    ['Bézout\'s identity', 'gcd(a, b) = ax + by for some integers x, y.'],
    ['Fundamental theorem of arithmetic', 'Every integer > 1 factors uniquely into primes.'],
    ['Characteristic equation', 'aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ ⇒ r² = c₁r + c₂.'],
    ['Euler\'s totient', 'φ(pq) = (p − 1)(q − 1).'],
    ['RSA', 'c = mᵉ mod n; m = cᵈ mod n; ed ≡ 1 mod φ(n).'],
]
