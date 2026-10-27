"""Discrete Mathematics and Logic, module 2: Sets, functions and relations."""
import itertools as it
from verify import Q, x, sp
T1, T2, T3, T4 = ('Sets and set operations', 'Functions', 'Relations and equivalence relations', 'Partial orders and countability')
A, Bs = {1, 2, 3}, {2, 3, 4}
assert A & Bs == {2, 3} and A - Bs == {1} and A | Bs == {1, 2, 3, 4} and len(list(it.product(A, {1, 2, 3, 4}))) == 12
assert 20 + 15 - 5 == 30 and 2 ** 3 == 8 and 2 ** 5 == 32
assert 4 ** 3 == 64 and 4 * 3 * 2 == 24 and len([f for f in it.product(range(4), repeat=3) if len(set(f)) == 3]) == 24
assert sp.solve(sp.Eq(2 * x + 3, sp.Symbol('w')), x)[0] == (sp.Symbol('w') - 3) / 2
assert sp.expand((2 * x + 3).subs(x, x ** 2)) == 2 * x ** 2 + 3 and sp.expand(((2 * x + 3) ** 2)) == 4 * x ** 2 + 12 * x + 9
assert 2 ** 9 == 512 and 2 ** 6 == 64
assert len({k % 3 for k in range(-30, 30)}) == 3
divs = [d for d in range(1, 13) if 12 % d == 0]; assert divs == [1, 2, 3, 4, 6, 12]

MODULE = {
    'title': 'Sets, functions and relations',
    'topics': [T1, T2, T3, T4],
    'overview': 'Sets, functions and relations are the vocabulary of all of mathematics and of databases and programming. This module covers set operations and counting with them, functions and their properties, equivalence relations, partial orders, and the surprising fact that some infinite sets are bigger than others.',
    'key_terms': ['Set', 'Subset', 'Power set', 'Union', 'Intersection', 'Complement', 'Cartesian product', 'Function', 'Injective', 'Surjective', 'Bijective', 'Inverse', 'Composition', 'Relation', 'Equivalence relation', 'Partial order', 'Countable'],
    'explanation': [
        'A set is a collection of distinct objects. Union, intersection, difference and complement combine sets, and Venn diagrams make them visual. The power set of a set with n elements has 2ⁿ subsets.',
        'A function assigns each input exactly one output. It is injective if different inputs give different outputs, surjective if every possible output is reached, and bijective if both, in which case it has an inverse.',
        'A relation is any set of ordered pairs. Equivalence relations (reflexive, symmetric, transitive) split a set into classes, like integers by remainder mod 3. Partial orders (reflexive, antisymmetric, transitive) rank elements, like divisibility.'],
    'quick_facts': [
        '|A ∪ B| = |A| + |B| − |A ∩ B|.',
        '|P(A)| = 2ⁿ; |A × B| = |A| × |B|.',
        'Functions from an m-set to an n-set: nᵐ; injective ones: n(n − 1)…(n − m + 1).',
        'Equivalence: reflexive, symmetric, transitive.',
        'ℕ, ℤ and ℚ are countable; ℝ is uncountable (Cantor).'],
}

NOTES = {
    T1: {
        'overview': 'Set operations and counting rules underlie probability, databases and logic.',
        'key_terms': ['Element ∈', 'Subset ⊆', 'Empty set ∅', 'Union ∪', 'Intersection ∩', 'Difference A − B', 'Complement', 'Power set P(A)', 'Cartesian product A × B', 'Cardinality |A|'],
        'explanation': [
            'For A = {1, 2, 3} and B = {2, 3, 4}: A ∪ B = {1, 2, 3, 4}, A ∩ B = {2, 3}, A − B = {1}. The complement of A contains everything in the universal set that is not in A. De Morgan\'s laws hold for sets just as for logic: (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ.',
            'Inclusion–exclusion counts unions without double counting: if 20 students take maths, 15 take physics and 5 take both, then 20 + 15 − 5 = 30 take at least one.',
            'The power set P(A) is the set of all subsets: a 3-element set has 2³ = 8 subsets (including ∅ and itself), a 5-element set 32. The Cartesian product A × B is the set of ordered pairs (a, b); |A × B| = |A||B|, so {1, 2, 3} × {1, 2, 3, 4} has 12 pairs.'],
        'formulas_label': 'Formulas',
        'formulas': ['|A ∪ B| = |A| + |B| − |A ∩ B|', '|P(A)| = 2^|A|', '|A × B| = |A| × |B|', '(A ∪ B)ᶜ = Aᶜ ∩ Bᶜ, (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ'],
        'steps': ['List or describe each set.', 'Apply the operation element by element.', 'Use a Venn diagram for counting.', 'Use inclusion–exclusion to avoid double counting.'],
        'worked_example': {
            'problem': 'In a class, 20 take Maths, 15 take Physics and 5 take both. How many take at least one?',
            'steps': ['Let M and P be the sets.', '|M ∪ P| = |M| + |P| − |M ∩ P|.', '= 20 + 15 − 5 = 30.'],
            'answer': '30 students.',
            'check': 'A Venn diagram gives 15 maths only + 10 physics only + 5 both = 30 ✓.'},
        'mistakes': ['Adding without subtracting the overlap.', 'Forgetting ∅ and A itself are subsets.', 'Treating (a, b) and (b, a) as the same pair.', 'Confusing ∈ with ⊆.'],
        'real_world': 'SQL joins and filters are set operations: an INNER JOIN is an intersection on matching keys, a UNION combines result sets.',
        'exam_strategy': 'Draw a Venn diagram for any counting question with two or three sets.',
        'recap': ['∪, ∩, −, complement.', 'Inclusion–exclusion.', '2ⁿ subsets.', '|A × B| = |A||B|.']},
    T2: {
        'overview': 'Functions map each input to exactly one output. Their properties decide whether they can be reversed.',
        'key_terms': ['Domain', 'Codomain', 'Range', 'Injective (one-to-one)', 'Surjective (onto)', 'Bijective', 'Inverse function', 'Composition f ∘ g'],
        'explanation': [
            'f: A → B is injective if f(a₁) = f(a₂) forces a₁ = a₂, surjective if every b ∈ B is an output, and bijective if both. f(x) = 2x + 3 on the reals is bijective with inverse f⁻¹(x) = (x − 3)/2. f(x) = x² on the reals is neither injective (f(2) = f(−2)) nor surjective (−1 is never reached).',
            'Composition: (f ∘ g)(x) = f(g(x)). With f(x) = 2x + 3 and g(x) = x²: (f ∘ g)(x) = 2x² + 3, but (g ∘ f)(x) = (2x + 3)² = 4x² + 12x + 9. Composition is usually not commutative.',
            'Counting: there are nᵐ functions from an m-element set to an n-element set (64 from 3 elements to 4), and n(n − 1)…(n − m + 1) injective ones (4 × 3 × 2 = 24).'],
        'formulas_label': 'Key facts',
        'formulas': ['Injective: f(a₁) = f(a₂) ⇒ a₁ = a₂', 'Surjective: range = codomain', 'Bijective ⇔ invertible', 'Number of functions: nᵐ; injections: n!/(n − m)!'],
        'steps': ['Check injectivity: set f(a₁) = f(a₂) and solve.', 'Check surjectivity: solve f(x) = y for any y.', 'Find the inverse by swapping and solving.', 'Compose from the inside out.'],
        'worked_example': {
            'problem': 'Show f(x) = 2x + 3 (ℝ → ℝ) is bijective and find its inverse.',
            'steps': ['Injective: 2a + 3 = 2b + 3 ⇒ a = b.', 'Surjective: for any y, x = (y − 3)/2 gives f(x) = y.', 'Inverse: f⁻¹(x) = (x − 3)/2.'],
            'answer': 'Bijective; f⁻¹(x) = (x − 3)/2.',
            'check': 'f(f⁻¹(x)) = 2(x − 3)/2 + 3 = x ✓.'},
        'mistakes': ['Ignoring the codomain when judging surjectivity.', 'Assuming f ∘ g = g ∘ f.', 'Reading f ∘ g as "f first".', 'Calling x² invertible on all reals.'],
        'real_world': 'Hash functions in computing are deliberately not injective (collisions happen); encryption functions must be bijective so they can be decrypted.',
        'exam_strategy': 'State the domain and codomain explicitly; the same formula can be bijective on one and not on another.',
        'recap': ['Injective, surjective, bijective.', 'Bijective ⇔ inverse.', 'Composition order.', 'Count with nᵐ.']},
    T3: {
        'overview': 'Relations describe connections between elements. Equivalence relations group elements that are "the same" in some sense.',
        'key_terms': ['Relation', 'Reflexive', 'Symmetric', 'Antisymmetric', 'Transitive', 'Equivalence relation', 'Equivalence class', 'Partition', 'Congruence mod n'],
        'explanation': [
            'A relation R on A is a subset of A × A. It is reflexive if aRa for all a, symmetric if aRb ⇒ bRa, and transitive if aRb and bRc ⇒ aRc. On a 3-element set there are 2⁹ = 512 relations, of which 2⁶ = 64 are reflexive (the 3 diagonal pairs are forced).',
            'An equivalence relation is reflexive, symmetric and transitive. Congruence mod 3 (a ≡ b if 3 divides a − b) is one: it splits the integers into 3 equivalence classes, by remainder 0, 1 or 2.',
            'Equivalence classes form a partition: every element is in exactly one class. "Has the same birthday as" is an equivalence relation; "is a friend of" is usually not transitive, and "≤" is not symmetric.'],
        'formulas_label': 'Properties',
        'formulas': ['Reflexive: aRa', 'Symmetric: aRb ⇒ bRa', 'Transitive: aRb ∧ bRc ⇒ aRc', 'Equivalence = all three', 'Relations on an n-set: 2^(n²)'],
        'steps': ['Test each property with the definition.', 'Find a counterexample if a property fails.', 'For equivalence relations, list the classes.', 'Check the classes partition the set.'],
        'worked_example': {
            'problem': 'Show that a ≡ b (mod 3) is an equivalence relation on the integers and find its classes.',
            'steps': ['Reflexive: 3 | 0 = a − a. Symmetric: 3 | (a − b) ⇒ 3 | (b − a).', 'Transitive: 3 | (a − b) and 3 | (b − c) ⇒ 3 | (a − c).', 'Classes: [0] = {…, −3, 0, 3, …}, [1], [2].'],
            'answer': 'An equivalence relation with 3 classes.',
            'check': 'Every integer has exactly one remainder 0, 1 or 2 ✓.'},
        'mistakes': ['Confusing symmetric with antisymmetric.', 'Checking transitivity with only one example.', 'Forgetting reflexivity for every element.', 'Overlapping equivalence classes.'],
        'real_world': 'Clock arithmetic (mod 12 or mod 24) is congruence; all times that differ by 24 hours are "equivalent" on a clock face.',
        'exam_strategy': 'For each property, write either a one-line proof or a specific counterexample.',
        'recap': ['Reflexive, symmetric, transitive.', 'Equivalence classes partition.', 'Mod n gives n classes.', '2^(n²) relations.']},
    T4: {
        'overview': 'Partial orders rank elements where not every pair is comparable. Countability compares the sizes of infinite sets.',
        'key_terms': ['Partial order', 'Antisymmetric', 'Total order', 'Hasse diagram', 'Maximal and minimal elements', 'Countable', 'Uncountable', 'Cantor\'s diagonal argument'],
        'explanation': [
            'A partial order is reflexive, antisymmetric (aRb and bRa ⇒ a = b) and transitive. Divisibility on {1, 2, 3, 4, 6, 12} is a partial order: 2 | 4 but 2 and 3 are incomparable. A Hasse diagram draws it with 1 at the bottom and 12 at the top; 1 is the minimum and 12 the maximum.',
            'A total order makes every pair comparable, like ≤ on numbers. Topological sorting turns a partial order into a total order, as when scheduling tasks with prerequisites.',
            'A set is countable if its elements can be listed as a first, second, third, … ℕ, ℤ and even ℚ are countable. Cantor\'s diagonal argument shows the real numbers cannot be listed: any list misses a number built to differ from the nth entry in its nth digit. So some infinities are bigger than others.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Partial order: reflexive, antisymmetric, transitive', 'Total order: also every pair comparable', 'Countable: can be listed (bijection with ℕ or finite)', 'ℝ is uncountable (diagonal argument)'],
        'steps': ['Check the three partial-order properties.', 'Draw the Hasse diagram (omit loops and implied edges).', 'Identify maximal and minimal elements.', 'For countability, find a listing or use a diagonal argument.'],
        'worked_example': {
            'problem': 'For divisibility on {1, 2, 3, 4, 6, 12}, find the minimal and maximal elements and an incomparable pair.',
            'steps': ['1 divides everything: the only minimal element (the minimum).', '12 is divisible by everything: the only maximal element (the maximum).', '2 and 3: neither divides the other, so they are incomparable.'],
            'answer': 'Minimum 1, maximum 12; 2 and 3 are incomparable.',
            'check': 'These are exactly the divisors of 12, so 12 sits at the top ✓.'},
        'mistakes': ['Thinking every pair must be comparable in a partial order.', 'Drawing implied edges in a Hasse diagram.', 'Believing all infinite sets are the same size.', 'Assuming ℚ is uncountable because it is dense.'],
        'real_world': 'Build tools and course registration systems use partial orders of prerequisites, sorted topologically to find a valid order.',
        'exam_strategy': 'In Hasse diagrams, draw only the "covers" (no element in between); examiners penalise extra lines.',
        'recap': ['Partial vs total order.', 'Hasse diagrams.', 'Countable lists.', 'ℝ is uncountable.']},
}

QUESTIONS = [
    # T1
    Q(T1, '20 students take Maths, 15 Physics, 5 both. How many take at least one?', ['30', '35', '40', '25'], 0, '20 + 15 − 5.', ans=30),
    Q(T1, 'A set with 3 elements has how many subsets?', ['8', '6', '3', '9'], 0, '2³.', ans=8),
    Q(T1, 'For A = {1, 2, 3}, B = {2, 3, 4}, A − B is:', ['{1}', '{4}', '{2, 3}', '{1, 4}'], 0, 'In A, not in B.'),
    Q(T1, 'For A = {1, 2, 3}, B = {2, 3, 4}, A ∩ B is:', ['{2, 3}', '{1, 2, 3, 4}', '{1}', '∅'], 0, 'In both.'),
    Q(T1, '|A × B| for |A| = 3 and |B| = 4 is:', ['12', '7', '81', '64'], 0, '3 × 4.', ans=12),
    Q(T1, 'The complement of A ∪ B equals:', ['Aᶜ ∩ Bᶜ', 'Aᶜ ∪ Bᶜ', 'A ∩ B', 'A − B'], 0, 'De Morgan for sets.'),
    # T2
    Q(T2, 'f(x) = x² from ℝ to ℝ is:', ['neither injective nor surjective', 'bijective', 'injective only', 'surjective only'], 0, 'f(2) = f(−2); −1 not reached.'),
    Q(T2, 'The inverse of f(x) = 2x + 3 is:', ['(x − 3)/2', '(x + 3)/2', '2x − 3', 'x/2 − 3'], 0, 'Swap and solve.', ans=(x - 3) / 2),
    Q(T2, 'With f(x) = 2x + 3 and g(x) = x², (f ∘ g)(x) =', ['2x² + 3', '4x² + 12x + 9', '2x + 3x²', '(2x + 3)x²'], 0, 'f(g(x)).', ans=2 * x ** 2 + 3),
    Q(T2, 'How many functions are there from a 3-element set to a 4-element set?', ['64', '81', '12', '24'], 0, '4³.', ans=64),
    Q(T2, 'How many of them are injective?', ['24', '64', '12', '4'], 0, '4 × 3 × 2.', ans=24),
    Q(T2, 'A function has an inverse exactly when it is:', ['bijective', 'injective only', 'surjective only', 'continuous'], 0, 'Both properties needed.'),
    # T3
    Q(T3, 'An equivalence relation must be:', ['reflexive, symmetric and transitive', 'reflexive, antisymmetric and transitive', 'symmetric only', 'transitive only'], 0, 'Definition.'),
    Q(T3, 'Congruence mod 3 splits the integers into how many classes?', ['3', '2', 'infinitely many', '1'], 0, 'Remainders 0, 1, 2.', ans=3),
    Q(T3, 'How many relations are there on a 3-element set?', ['512', '64', '9', '27'], 0, '2^(3²).', ans=512),
    Q(T3, 'How many of them are reflexive?', ['64', '512', '8', '6'], 0, '6 free off-diagonal pairs.', ans=64),
    Q(T3, 'The relation ≤ on the integers is not:', ['symmetric', 'reflexive', 'transitive', 'antisymmetric'], 0, '1 ≤ 2 but not 2 ≤ 1.'),
    Q(T3, 'The equivalence classes of an equivalence relation:', ['partition the set', 'always overlap', 'are all the same size', 'are always infinite'], 0, 'Each element in exactly one.'),
    # T4
    Q(T4, 'A partial order is reflexive, transitive and:', ['antisymmetric', 'symmetric', 'total', 'injective'], 0, 'aRb and bRa ⇒ a = b.'),
    Q(T4, 'Under divisibility on {1, 2, 3, 4, 6, 12}, which pair is incomparable?', ['2 and 3', '2 and 4', '3 and 6', '1 and 12'], 0, 'Neither divides the other.'),
    Q(T4, 'In that poset, the maximum element is:', ['12', '6', '4', '1'], 0, 'Divisible by all.', ans=12),
    Q(T4, 'Which set is uncountable?', ['ℝ', 'ℚ', 'ℤ', 'ℕ'], 0, 'Cantor\'s diagonal argument.'),
    Q(T4, 'Cantor\'s diagonal argument shows that:', ['the real numbers cannot be listed', 'the rationals are uncountable', 'every infinite set is countable', 'ℕ is finite'], 0, 'Some infinities are larger.'),
    Q(T4, 'Turning a partial order of prerequisites into a valid sequence is called:', ['topological sorting', 'diagonalisation', 'induction', 'partitioning'], 0, 'Used in scheduling.'),
]

FLASH = [
    ['Inclusion–exclusion (2 sets)', '|A ∪ B| = |A| + |B| − |A ∩ B|.'],
    ['Power set', 'All subsets; 2ⁿ of them for an n-element set.'],
    ['Injective', 'Different inputs give different outputs.'],
    ['Surjective', 'Every element of the codomain is an output.'],
    ['Bijective', 'Injective and surjective; has an inverse.'],
    ['Equivalence relation', 'Reflexive, symmetric, transitive; classes partition the set.'],
    ['Partial order', 'Reflexive, antisymmetric, transitive.'],
    ['Uncountable', 'Cannot be listed, like ℝ (Cantor).'],
]
