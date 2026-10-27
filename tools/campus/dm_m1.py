"""Discrete Mathematics and Logic, module 1: Logic and proof."""
import itertools as it
from verify import Q, n, sp
T1, T2, T3, T4 = ('Propositional logic', 'Predicates and quantifiers', 'Methods of proof', 'Mathematical induction')
imp = lambda p, q: (not p) or q
B = list(it.product([False, True], repeat=2)); B3 = list(it.product([False, True], repeat=3))
assert all(imp(p, q) == ((not p) or q) for p, q in B) and [imp(p, q) for p, q in B] == [True, True, False, True]
assert all((not (p and q)) == ((not p) or (not q)) for p, q in B) and all((not (p or q)) == ((not p) and (not q)) for p, q in B)
assert all(imp(p, q) == imp(not q, not p) for p, q in B) and not all(imp(p, q) == imp(q, p) for p, q in B)
assert all(imp(imp(p, q) and imp(q, r), imp(p, r)) for p, q, r in B3)
assert sum(1 for p, q, r in B3 if (p or q) and not r) == 3 and 2 ** 4 == 16
assert sum(range(1, 101)) == 5050 and sum(i * i for i in range(1, 11)) == 385 and sum(2 * i - 1 for i in range(1, 8)) == 49
assert sp.simplify(sp.summation(2 ** (n - 1), (n, 1, sp.Symbol('m'))) - (2 ** sp.Symbol('m') - 1)) == 0
assert all(any(x + yy == 0 for yy in range(-20, 21)) for x in range(-10, 11)) and not any(all(x + yy == 0 for x in range(-10, 11)) for yy in range(-20, 21))

MODULE = {
    'title': 'Logic and proof',
    'topics': [T1, T2, T3, T4],
    'overview': 'Discrete mathematics is the mathematics of computer science, and it starts with precise logic. This module covers propositional logic and truth tables, predicates and quantifiers, the standard methods of proof, and mathematical induction.',
    'key_terms': ['Proposition', 'Connective', 'Truth table', 'Implication', 'Contrapositive', 'Converse', 'Tautology', 'Logical equivalence', 'Predicate', 'Quantifier', 'Direct proof', 'Proof by contradiction', 'Counterexample', 'Induction'],
    'explanation': [
        'A proposition is a statement that is true or false. Connectives (not, and, or, if-then, if and only if) build compound statements, and truth tables decide when they are true. Two statements are logically equivalent when their truth tables match.',
        'Predicates such as P(x): "x is even" become propositions once x is fixed or quantified: ∀x P(x) ("for all x") or ∃x P(x) ("there exists x"). Negating a quantified statement swaps ∀ and ∃ and negates the predicate.',
        'Proofs establish statements for every case. Direct proof, contrapositive, contradiction and cases are the main tools; a single counterexample disproves a universal claim. Induction proves statements about all natural numbers in two steps: a base case and an inductive step.'],
    'quick_facts': [
        'p → q is false only when p is true and q is false.',
        'p → q ≡ ¬q → ¬p (contrapositive); the converse q → p is not equivalent.',
        'De Morgan: ¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q.',
        '¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x).',
        'Induction: prove P(1), then P(k) ⇒ P(k + 1).'],
}

NOTES = {
    T1: {
        'overview': 'Propositional logic studies how the truth of compound statements depends on their parts.',
        'key_terms': ['Proposition', 'Negation ¬', 'Conjunction ∧', 'Disjunction ∨', 'Implication →', 'Biconditional ↔', 'Truth table', 'Tautology', 'Contradiction', 'Logical equivalence', 'De Morgan\'s laws'],
        'explanation': [
            'A truth table lists every combination of truth values; n variables need 2ⁿ rows (16 rows for 4 variables). The implication p → q is false only when p is true and q is false; this matches a promise: "if you pass, you get a bursary" is only broken if you pass and get nothing.',
            'Useful equivalences: p → q ≡ ¬p ∨ q; De Morgan\'s laws ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q. The contrapositive ¬q → ¬p is equivalent to p → q, but the converse q → p and the inverse ¬p → ¬q are not.',
            'A tautology is always true (p ∨ ¬p; ((p → q) ∧ (q → r)) → (p → r), the basis of chained reasoning); a contradiction is always false (p ∧ ¬p). Logic gates in computers implement these connectives directly.'],
        'formulas_label': 'Key equivalences',
        'formulas': ['p → q ≡ ¬p ∨ q', 'p → q ≡ ¬q → ¬p', '¬(p ∧ q) ≡ ¬p ∨ ¬q', '¬(p ∨ q) ≡ ¬p ∧ ¬q', 'p ↔ q ≡ (p → q) ∧ (q → p)'],
        'steps': ['List the variables; make 2ⁿ rows.', 'Add a column for each sub-expression.', 'Fill in using the connective rules.', 'Compare final columns to test equivalence.'],
        'worked_example': {
            'problem': 'Show that p → q and its contrapositive ¬q → ¬p are equivalent.',
            'steps': ['Rows (p, q): FF, FT, TF, TT.', 'p → q: T, T, F, T.', '¬q → ¬p: T, T, F, T. The columns match.'],
            'answer': 'They are logically equivalent.',
            'check': 'The converse q → p gives T, F, T, T, which differs, so it is not equivalent ✓.'},
        'mistakes': ['Thinking p → q is false when p is false.', 'Confusing the converse with the contrapositive.', 'Negating "and" as "and".', 'Missing rows in a truth table.'],
        'real_world': 'Database queries and search filters are built from AND, OR and NOT; De Morgan\'s laws let engines rewrite them efficiently.',
        'exam_strategy': 'For equivalence questions, a truth table is a guaranteed method; use algebraic laws only when you are confident.',
        'recap': ['2ⁿ rows.', 'p → q false only for T → F.', 'Contrapositive is equivalent.', 'De Morgan\'s laws.']},
    T2: {
        'overview': 'Predicates and quantifiers express statements about all or some members of a domain.',
        'key_terms': ['Predicate', 'Domain', 'Universal quantifier ∀', 'Existential quantifier ∃', 'Nested quantifiers', 'Negation of quantifiers', 'Counterexample'],
        'explanation': [
            'A predicate P(x) becomes true or false once x is chosen. ∀x P(x) means P holds for every x in the domain; ∃x P(x) means at least one x works. The domain matters: ∃x (x² = 2) is true over the reals but false over the integers.',
            'Negation swaps quantifiers: ¬∀x P(x) ≡ ∃x ¬P(x) and ¬∃x P(x) ≡ ∀x ¬P(x). The negation of "every student passed" is "some student did not pass", not "no student passed".',
            'Order matters in nested quantifiers. Over the integers, ∀x ∃y (x + y = 0) is true (take y = −x), but ∃y ∀x (x + y = 0) is false (no single y works for every x).'],
        'formulas_label': 'Rules',
        'formulas': ['¬∀x P(x) ≡ ∃x ¬P(x)', '¬∃x P(x) ≡ ∀x ¬P(x)', '∀x ∃y ≠ ∃y ∀x in general', 'One counterexample disproves ∀'],
        'steps': ['Identify the domain.', 'Translate the sentence into symbols.', 'To negate, move ¬ inwards, swapping ∀ and ∃.', 'Test with examples or a counterexample.'],
        'worked_example': {
            'problem': 'Negate: "For every ε > 0 there is a δ > 0 that works."',
            'steps': ['Symbols: ∀ε ∃δ W(ε, δ).', 'Negation: ∃ε ¬∃δ W(ε, δ) ≡ ∃ε ∀δ ¬W(ε, δ).', 'In words: "There is some ε > 0 for which no δ > 0 works."'],
            'answer': '∃ε ∀δ ¬W(ε, δ).',
            'check': 'Each quantifier flipped and the predicate negated ✓.'},
        'mistakes': ['Negating "all" as "none".', 'Swapping the order of nested quantifiers.', 'Ignoring the domain.', 'Trying to prove ∀ with examples.'],
        'real_world': 'Software specifications use quantifiers ("for every input, the program terminates"); verification tools check them automatically.',
        'exam_strategy': 'Write the symbolic form before negating; negating in words leads to errors.',
        'recap': ['∀ for all, ∃ there exists.', 'Negation swaps them.', 'Order matters.', 'Domain matters.']},
    T3: {
        'overview': 'A proof is a logical argument that a statement holds in every case. Choose the method that fits the statement.',
        'key_terms': ['Direct proof', 'Proof by contrapositive', 'Proof by contradiction', 'Proof by cases', 'Counterexample', 'Even and odd', 'Rational and irrational'],
        'explanation': [
            'Direct proof: assume p and deduce q. To prove "if n is odd then n² is odd": n = 2k + 1, so n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd.',
            'Contrapositive: to prove "if n² is even then n is even", prove instead "if n is odd then n² is odd", which we just did. Contradiction: assume the statement is false and derive an impossibility. The classic example: if √2 = a/b in lowest terms, then a² = 2b², so a is even, then b is even too, contradicting lowest terms.',
            'Proof by cases splits into exhaustive cases (n even or odd). To disprove "all primes are odd", one counterexample is enough: 2.'],
        'formulas_label': 'Methods',
        'formulas': ['Direct: p ⇒ … ⇒ q', 'Contrapositive: prove ¬q ⇒ ¬p', 'Contradiction: assume ¬statement, derive a false statement', 'Cases: cover every possibility', 'Disprove ∀ with one counterexample'],
        'steps': ['Write what is given and what is to be proved.', 'Choose a method (direct is the default).', 'Use definitions (even = 2k, odd = 2k + 1, rational = a/b).', 'End with a clear conclusion.'],
        'worked_example': {
            'problem': 'Prove: if n² is even, then n is even.',
            'steps': ['Use the contrapositive: if n is odd, then n² is odd.', 'n = 2k + 1 ⇒ n² = 2(2k² + 2k) + 1, which is odd.', 'So the contrapositive holds, and hence the original statement.'],
            'answer': 'Proved by contrapositive.',
            'check': 'A direct proof would need to "un-square", which is awkward; the contrapositive avoids that ✓.'},
        'mistakes': ['Proving the converse instead of the statement.', 'Using examples as proof of a universal claim.', 'Assuming what is to be proved.', 'Not stating the contradiction clearly.'],
        'real_world': 'Cryptography relies on proved theorems, such as the properties of primes, to guarantee that encryption can be reversed only with the key.',
        'exam_strategy': 'Start every proof by writing the definitions you will use (for example "n odd means n = 2k + 1 for some integer k").',
        'recap': ['Direct, contrapositive, contradiction, cases.', 'Use definitions.', 'Counterexamples disprove.', 'State the conclusion.']},
    T4: {
        'overview': 'Mathematical induction proves a statement for every natural number by a domino argument.',
        'key_terms': ['Base case', 'Inductive hypothesis', 'Inductive step', 'Strong induction', 'Summation formula'],
        'explanation': [
            'To prove P(n) for all n ≥ 1: (1) base case, show P(1); (2) inductive step, assume P(k) (the inductive hypothesis) and prove P(k + 1). Then P holds for every n, like an infinite row of dominoes.',
            'Example: 1 + 2 + … + n = n(n + 1)/2. Base: 1 = 1 × 2/2 ✓. Step: if 1 + … + k = k(k + 1)/2, then adding k + 1 gives k(k + 1)/2 + (k + 1) = (k + 1)(k + 2)/2 ✓. So 1 + … + 100 = 5050. Similarly the first n odd numbers sum to n² (the first 7 give 49), 1 + 2 + 4 + … + 2ⁿ⁻¹ = 2ⁿ − 1, and 1² + … + n² = n(n + 1)(2n + 1)/6 (385 for n = 10).',
            'Strong induction assumes P(1), …, P(k) to prove P(k + 1). It is natural for statements like "every integer n ≥ 2 is a product of primes", where k + 1 splits into smaller factors.'],
        'formulas_label': 'Results',
        'formulas': ['Σᵢ₌₁ⁿ i = n(n + 1)/2', 'Σᵢ₌₁ⁿ (2i − 1) = n²', 'Σᵢ₌₁ⁿ i² = n(n + 1)(2n + 1)/6', 'Σᵢ₌₀ⁿ⁻¹ 2ⁱ = 2ⁿ − 1'],
        'steps': ['Prove the base case.', 'State the inductive hypothesis P(k).', 'Prove P(k + 1) using P(k).', 'Conclude by the principle of induction.'],
        'worked_example': {
            'problem': 'Prove 1 + 3 + 5 + … + (2n − 1) = n².',
            'steps': ['Base n = 1: 1 = 1² ✓.', 'Assume 1 + 3 + … + (2k − 1) = k².', 'Then adding 2k + 1: k² + 2k + 1 = (k + 1)² ✓. By induction the formula holds for all n ≥ 1.'],
            'answer': 'Proved by induction.',
            'check': 'n = 7: 1 + 3 + 5 + 7 + 9 + 11 + 13 = 49 = 7² ✓.'},
        'mistakes': ['Skipping the base case.', 'Assuming P(k + 1) instead of proving it.', 'Not using the inductive hypothesis.', 'Checking a few values and calling it a proof.'],
        'real_world': 'Programmers prove loops correct with loop invariants, which is induction applied to the number of iterations.',
        'exam_strategy': 'Label the three parts clearly (Base case, Inductive hypothesis, Inductive step); each earns marks.',
        'recap': ['Base case.', 'Hypothesis P(k).', 'Prove P(k + 1).', 'Conclude.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'p → q is false exactly when:', ['p is true and q is false', 'p is false and q is true', 'both are false', 'both are true'], 0, 'A broken promise.'),
    Q(T1, 'The negation of p ∧ q is:', ['¬p ∨ ¬q', '¬p ∧ ¬q', 'p ∨ q', '¬p ∧ q'], 0, 'De Morgan.'),
    Q(T1, 'The contrapositive of p → q is:', ['¬q → ¬p', 'q → p', '¬p → ¬q', 'p → ¬q'], 0, 'Equivalent to the original.'),
    Q(T1, 'A truth table with 4 variables has how many rows?', ['16', '8', '4', '32'], 0, '2⁴.', ans=16),
    Q(T1, 'p → q is logically equivalent to:', ['¬p ∨ q', 'p ∨ ¬q', '¬p ∧ q', 'q → p'], 0, 'Check all four rows.'),
    Q(T1, 'For how many of the 8 rows is (p ∨ q) ∧ ¬r true?', ['3', '4', '2', '6'], 0, 'r false and not both p, q false.', ans=3),
    # T2
    Q(T2, '¬∀x P(x) is equivalent to:', ['∃x ¬P(x)', '∀x ¬P(x)', '¬∃x P(x)', '∃x P(x)'], 0, 'Swap and negate.'),
    Q(T2, 'The negation of "Every student passed" is:', ['Some student did not pass', 'No student passed', 'Every student failed', 'Some student passed'], 0, '∃ not passed.'),
    Q(T2, 'Over the integers, ∀x ∃y (x + y = 0) is:', ['true', 'false', 'neither', 'meaningless'], 0, 'y = −x.'),
    Q(T2, 'Over the integers, ∃y ∀x (x + y = 0) is:', ['false', 'true', 'true only for y = 0', 'meaningless'], 0, 'No single y works.'),
    Q(T2, '∃x (x² = 2) is true when the domain is:', ['the real numbers', 'the integers', 'the natural numbers', 'the rational numbers'], 0, '√2 is irrational.'),
    Q(T2, 'To disprove a statement of the form ∀x P(x), it is enough to:', ['find one counterexample', 'check ten examples', 'prove ∃x P(x)', 'prove the converse'], 0, 'One failing x.'),
    # T3
    Q(T3, 'To prove "if n² is even then n is even", the simplest method is:', ['contrapositive', 'direct proof', 'induction', 'a single example'], 0, 'Prove odd ⇒ odd.'),
    Q(T3, 'The classic proof that √2 is irrational uses:', ['contradiction', 'induction', 'a counterexample', 'a truth table'], 0, 'Assume a/b in lowest terms.'),
    Q(T3, 'A counterexample to "all primes are odd" is:', ['2', '3', '9', '1'], 0, '2 is prime and even.', ans=2),
    Q(T3, 'If n = 2k + 1, then n² equals:', ['2(2k² + 2k) + 1', '4k² + 1', '2k² + 1', '4k + 1'], 0, 'Expand (2k + 1)².'),
    Q(T3, 'Proving the converse q → p instead of p → q:', ['does not prove the original statement', 'proves it', 'proves the contrapositive', 'is a proof by contradiction'], 0, 'Converse is not equivalent.'),
    Q(T3, 'Proof by cases requires the cases to be:', ['exhaustive (covering every possibility)', 'equally likely', 'exactly two', 'disjoint only'], 0, 'No case may be missed.'),
    # T4
    Q(T4, '1 + 2 + … + 100 =', ['5050', '5000', '10100', '4950'], 0, '100 × 101/2.', ans=5050),
    Q(T4, 'The sum of the first 7 odd numbers is:', ['49', '42', '56', '64'], 0, 'n².', ans=49),
    Q(T4, '1² + 2² + … + 10² =', ['385', '355', '505', '100'], 0, '10 × 11 × 21/6.', ans=385),
    Q(T4, '1 + 2 + 4 + … + 2ⁿ⁻¹ =', ['2ⁿ − 1', '2ⁿ', '2ⁿ⁺¹ − 1', 'n²'], 0, 'Geometric sum.', ans=2 ** n - 1),
    Q(T4, 'In the inductive step you:', ['assume P(k) and prove P(k + 1)', 'assume P(k + 1)', 'check P(1) again', 'test several values'], 0, 'The domino step.'),
    Q(T4, '"Every integer n ≥ 2 is a product of primes" is most naturally proved by:', ['strong induction', 'a truth table', 'one example', 'contrapositive only'], 0, 'Uses smaller factors.'),
]

FLASH = [
    ['Implication p → q', 'False only when p is true and q is false.'],
    ['Contrapositive', '¬q → ¬p; equivalent to p → q.'],
    ['De Morgan\'s laws', '¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q.'],
    ['Tautology', 'A statement true in every row of its truth table.'],
    ['Negating quantifiers', '¬∀x P ≡ ∃x ¬P; ¬∃x P ≡ ∀x ¬P.'],
    ['Proof by contradiction', 'Assume the statement is false and derive an impossibility.'],
    ['Induction', 'Base case P(1); inductive step P(k) ⇒ P(k + 1).'],
    ['Gauss\'s sum', '1 + 2 + … + n = n(n + 1)/2.'],
]
