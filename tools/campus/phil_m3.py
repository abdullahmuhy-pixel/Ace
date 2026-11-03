"""Introduction to Philosophy and Logic, module 3: Symbolic (propositional) logic."""
from itertools import product
from verify import Q
from nt import N, module
T1, T2, T3, T4 = ('Propositions and logical connectives', 'Truth tables', 'Tautologies, contradictions and equivalence', 'Valid argument forms and formal fallacies')

imp = lambda a, b: (not a) or b
rows = list(product([True, False], repeat=2))
assert [imp(p, q) for p, q in rows] == [True, False, True, True]
assert all((not (p and q)) == ((not p) or (not q)) for p, q in rows)                 # De Morgan
assert all(imp(p, q) == imp(not q, not p) for p, q in rows)                           # contraposition
assert all((p or not p) for p, _ in rows) and not any((p and not p) for p, _ in rows)
assert sum(1 for p, q, r in product([True, False], repeat=3) if (p and q) or r) == 5
assert 2 ** 3 == 8 and 2 ** 4 == 16
# modus ponens valid; affirming the consequent invalid
assert all(q for p, q in rows if imp(p, q) and p)
assert any(not p for p, q in rows if imp(p, q) and q)

MODULE = module('Symbolic logic', [T1, T2, T3, T4],
    'Symbolic logic replaces everyday words with symbols so that the form of an argument can be tested exactly. This module introduces propositional variables and connectives, builds truth tables, identifies tautologies and equivalences, and tests argument forms such as modus ponens, modus tollens and the formal fallacies.',
    ['Proposition', 'Propositional variable', 'Negation', 'Conjunction', 'Disjunction', 'Conditional', 'Biconditional', 'Truth table', 'Tautology', 'Contradiction', 'Modus ponens', 'Modus tollens'],
    ['A proposition is a statement that is true or false. Simple propositions are written as letters (p, q, r) and combined with connectives: not (¬), and (∧), or (∨), if...then (→) and if and only if (↔).',
     'A truth table lists every combination of truth values for the variables, 2ⁿ rows for n variables, and works out the value of a compound statement on each row. A tautology is true on every row, a contradiction false on every row, and two statements are equivalent if they match on every row.',
     'An argument form is valid if no row of the truth table makes all the premises true and the conclusion false. Modus ponens, modus tollens, hypothetical syllogism and disjunctive syllogism are valid; affirming the consequent and denying the antecedent are formal fallacies.'],
    ['p → q is false only when p is true and q is false.', 'n variables → 2ⁿ rows.', 'De Morgan: ¬(p ∧ q) ≡ ¬p ∨ ¬q.', 'p → q ≡ ¬q → ¬p (contrapositive).', 'Valid: no row with true premises and false conclusion.'])

NOTES = {
 T1: N('Connectives combine simple statements into complex ones. Translating English correctly is the first step in formal logic.',
   ['Simple proposition', 'Compound proposition', 'Negation (¬)', 'Conjunction (∧)', 'Disjunction (∨)', 'Conditional (→)', 'Antecedent', 'Consequent'],
   ['Let p = "It is raining" and q = "The match is cancelled". Then ¬p is "It is not raining", p ∧ q is "It is raining and the match is cancelled", p ∨ q is "It is raining or the match is cancelled (or both)", p → q is "If it is raining, then the match is cancelled", and p ↔ q is "It is raining if and only if the match is cancelled".',
    'In logic, "or" is usually inclusive: p ∨ q is true when at least one is true. In p → q, p is the antecedent and q the consequent. English variants of the conditional include "q if p" (p → q), "p only if q" (p → q), "q provided that p" (p → q) and "unless p, q" (¬p → q, often written p ∨ q).',
    'Words such as "but", "although" and "however" translate as ∧, since they assert both parts. "Neither p nor q" is ¬p ∧ ¬q (equivalently ¬(p ∨ q)). "Not both p and q" is ¬(p ∧ q). Brackets show scope, just as in algebra: ¬(p ∧ q) is different from ¬p ∧ q.'],
   ['¬ not; ∧ and; ∨ or (inclusive); → if...then; ↔ iff', '"p only if q" = p → q', '"but" = ∧', '"neither p nor q" = ¬p ∧ ¬q'],
   ['Assign letters to simple statements.', 'Find the main connective.', 'Translate parts in brackets.', 'Check the result reads back correctly.'],
   ('Let p = "Ada studies" and q = "Ada passes". Symbolise: (a) Ada passes only if she studies. (b) Ada neither studies nor passes. (c) Ada studies but does not pass.',
    ['(a) "q only if p" = q → p.', '(b) "neither p nor q" = ¬p ∧ ¬q.', '(c) "but" = and: p ∧ ¬q.'],
    '(a) q → p, (b) ¬p ∧ ¬q, (c) p ∧ ¬q.', 'Reading each back gives the original sentence ✓.'),
   ['Translating "p only if q" as q → p.', 'Treating "or" as exclusive by default.', 'Forgetting brackets with negation.', 'Translating "but" as something other than ∧.'],
   'Computer programs and database searches use the same connectives: AND, OR and NOT in search engines work exactly like ∧, ∨ and ¬.',
   'Write the key for each letter, then translate; most errors come from "only if" and "unless".',
   ['Five connectives.', 'Antecedent and consequent.', 'Tricky English forms.', 'Scope and brackets.']),
 T2: N('Truth tables compute the truth value of any compound statement mechanically.',
   ['Truth value', 'Truth table', 'Row', 'Main connective', 'Truth-functional', 'Material conditional', 'Biconditional', 'Exclusive or'],
   ['A truth table has one column for each variable and one row for each combination of values: 2 rows for one variable, 4 for two, 8 for three, 16 for four (2ⁿ). Columns are filled systematically (for two variables: TT, TF, FT, FF).',
    'Basic tables: ¬p reverses the value. p ∧ q is true only when both are true. p ∨ q is false only when both are false. p → q is false only when p is true and q is false (true antecedent, false consequent); in all other rows it is true, which surprises beginners but matches "I never broke my promise unless the condition held and I did not deliver". p ↔ q is true when p and q have the same value.',
    'For a complex statement, work outward from the innermost brackets, writing a column for each sub-formula and finishing with the main connective. For example, (p ∧ q) ∨ r has 8 rows and is true on 5 of them: whenever r is true (4 rows) plus the row where p and q are true and r is false.'],
   ['Rows = 2ⁿ', 'p ∧ q: T only if both T', 'p ∨ q: F only if both F', 'p → q: F only if p T and q F'],
   ['Count variables and rows (2ⁿ).', 'Fill variable columns systematically.', 'Compute inner sub-formulas.', 'Compute the main connective.'],
   ('Complete the truth table for p → q.',
    ['Row 1: p T, q T → T.', 'Row 2: p T, q F → F.', 'Row 3: p F, q T → T.', 'Row 4: p F, q F → T.'],
    'T, F, T, T', 'Only the true-antecedent, false-consequent row is false ✓.'),
   ['Getting the conditional rows wrong when p is false.', 'Too few rows.', 'Computing the main connective before the parts.', 'Treating ∨ as exclusive.'],
   'Digital circuits are built from logic gates whose behaviour is defined by truth tables.',
   'Show every intermediate column; it makes errors easy to find and earns method marks.',
   ['2ⁿ rows.', 'Basic tables.', 'Conditional table.', 'Inside-out method.']),
 T3: N('Some statements are true in every case, some in none. Truth tables also show when two statements say the same thing.',
   ['Tautology', 'Contradiction', 'Contingency', 'Logical equivalence', 'De Morgan\'s laws', 'Contrapositive', 'Converse', 'Double negation'],
   ['A tautology is true on every row, for example p ∨ ¬p (the law of excluded middle). A contradiction is false on every row, for example p ∧ ¬p. A contingent statement is true on some rows and false on others.',
    'Two statements are logically equivalent (≡) if they have the same truth value on every row. Key equivalences: double negation ¬¬p ≡ p; De Morgan\'s laws ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q; the conditional p → q ≡ ¬p ∨ q; and the contrapositive p → q ≡ ¬q → ¬p.',
    'The converse (q → p) and inverse (¬p → ¬q) of a conditional are not equivalent to it. "If it is a mango, it is a fruit" is true, but its converse "if it is a fruit, it is a mango" is false. Confusing a conditional with its converse is a common error in reasoning and in reading laws.'],
   ['Tautology: always T; contradiction: always F', '¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q', 'p → q ≡ ¬q → ¬p', 'Converse q → p is not equivalent'],
   ['Build truth tables for both statements.', 'Compare their final columns row by row.', 'If identical, they are equivalent.', 'If a single column is all T or all F, classify it.'],
   ('Show that ¬(p ∧ q) is equivalent to ¬p ∨ ¬q.',
    ['Rows (p, q): TT, TF, FT, FF.', 'p ∧ q: T, F, F, F, so ¬(p ∧ q): F, T, T, T.', '¬p: F, F, T, T; ¬q: F, T, F, T; ¬p ∨ ¬q: F, T, T, T.'],
    'The final columns match (F, T, T, T), so the statements are equivalent.', 'This is De Morgan\'s law ✓.'),
   ['Treating a conditional and its converse as equivalent.', 'Applying De Morgan without switching ∧ and ∨.', 'Calling a contingent statement a tautology because it is often true.', 'Comparing only some rows.'],
   'Lawyers reading "a licence is required only if the vehicle carries passengers" must not assume the converse.',
   'Always show both full columns when proving equivalence.',
   ['Tautology, contradiction, contingency.', 'Equivalence.', 'De Morgan and contrapositive.', 'Converse is not equivalent.']),
 T4: N('Truth tables can test whether an argument form is valid. A few valid forms and two classic fallacies appear constantly.',
   ['Argument form', 'Modus ponens', 'Modus tollens', 'Hypothetical syllogism', 'Disjunctive syllogism', 'Affirming the consequent', 'Denying the antecedent', 'Formal fallacy'],
   ['Valid forms: modus ponens (p → q; p; therefore q); modus tollens (p → q; ¬q; therefore ¬p); hypothetical syllogism (p → q; q → r; therefore p → r); disjunctive syllogism (p ∨ q; ¬p; therefore q).',
    'Invalid forms (formal fallacies): affirming the consequent (p → q; q; therefore p) and denying the antecedent (p → q; ¬p; therefore ¬q). "If it rained, the ground is wet; the ground is wet; so it rained" is invalid: a burst pipe could wet the ground.',
    'Truth-table test: list the premises and conclusion as columns. If any row makes all premises true and the conclusion false, the form is invalid; otherwise it is valid. For affirming the consequent, the row p false, q true makes p → q and q true but the conclusion p false, so it is invalid.'],
   ['Modus ponens: p → q, p ∴ q', 'Modus tollens: p → q, ¬q ∴ ¬p', 'Affirming the consequent: invalid', 'Denying the antecedent: invalid'],
   ['Symbolise the argument.', 'Match it to a known form.', 'If unsure, build a truth table.', 'Look for a row with true premises and a false conclusion.'],
   ('Test: "If the generator has fuel, it runs. The generator does not run. So it has no fuel."',
    ['Let p = has fuel, q = runs. Form: p → q; ¬q; therefore ¬p.', 'This is modus tollens.', 'No row makes p → q and ¬q true while ¬p is false.'],
    'Valid (modus tollens).', 'The only row with ¬q true and p → q true has p false ✓.'),
   ['Calling affirming the consequent valid.', 'Mixing up modus ponens and modus tollens.', 'Thinking a valid form guarantees true premises.', 'Ignoring alternative causes.'],
   'Doctors use modus tollens when ruling out a diagnosis: if it were malaria, the test would be positive; the test is negative; so (probably) not malaria.',
   'Symbolise first, then name the form; if it is a fallacy, give a counterexample.',
   ['Four valid forms.', 'Two formal fallacies.', 'Truth-table test.', 'Counterexamples.']),
}

QUESTIONS = [
    Q(T1, 'The symbol ∧ stands for:', ['and', 'or', 'not', 'if...then'], 0, 'Conjunction.'),
    Q(T1, '"p only if q" is symbolised as:', ['p → q', 'q → p', 'p ∧ q', 'p ↔ q'], 0, 'Only if introduces the consequent.'),
    Q(T1, '"Neither p nor q" is:', ['¬p ∧ ¬q', '¬p ∨ ¬q', '¬(p ∧ q)', 'p ∨ q'], 0, 'Both false.'),
    Q(T1, 'In logic, p ∨ q is true when:', ['at least one of p and q is true', 'exactly one is true', 'both are false', 'only p is true'], 0, 'Inclusive or.'),
    Q(T1, 'In p → q, p is called the:', ['antecedent', 'consequent', 'conclusion', 'connective'], 0, 'The "if" part.'),
    Q(T1, '"Ada studies but does not pass" (p = studies, q = passes) is:', ['p ∧ ¬q', 'p → ¬q', 'p ∨ ¬q', '¬p ∧ q'], 0, '"But" = and.'),
    Q(T2, 'A truth table for three variables has how many rows?', ['8', '6', '9', '3'], 0, '2³.', ans=8),
    Q(T2, 'p → q is false when:', ['p is true and q is false', 'p is false and q is true', 'both are false', 'both are true'], 0, 'Only one false row.'),
    Q(T2, 'p ∧ q is true when:', ['both p and q are true', 'either is true', 'both are false', 'p is false'], 0, 'Only one true row.'),
    Q(T2, 'p ↔ q is true when:', ['p and q have the same truth value', 'p and q differ', 'only p is true', 'only q is true'], 0, 'Biconditional.'),
    Q(T2, 'On how many of the 8 rows is (p ∧ q) ∨ r true?', ['5', '4', '3', '7'], 0, 'r true (4) + p, q true with r false (1).', ans=5),
    Q(T2, 'A truth table for four variables has how many rows?', ['16', '8', '4', '12'], 0, '2⁴.', ans=16),
    Q(T3, 'A statement that is true on every row of its truth table is a:', ['tautology', 'contradiction', 'contingency', 'fallacy'], 0, 'E.g. p ∨ ¬p.'),
    Q(T3, 'p ∧ ¬p is a:', ['contradiction', 'tautology', 'contingency', 'conditional'], 0, 'Always false.'),
    Q(T3, 'By De Morgan\'s law, ¬(p ∨ q) is equivalent to:', ['¬p ∧ ¬q', '¬p ∨ ¬q', 'p ∧ q', '¬p ∨ q'], 0, 'Switch ∨ to ∧.'),
    Q(T3, 'The contrapositive of p → q is:', ['¬q → ¬p', 'q → p', '¬p → ¬q', 'p ∧ ¬q'], 0, 'Equivalent to the original.'),
    Q(T3, 'The converse of "If it is a mango, it is a fruit" is:', ['If it is a fruit, it is a mango', 'If it is not a fruit, it is not a mango', 'If it is not a mango, it is not a fruit', 'It is a mango and a fruit'], 0, 'q → p, not equivalent.'),
    Q(T3, 'p → q is equivalent to:', ['¬p ∨ q', 'p ∨ ¬q', '¬p ∧ q', 'q → p'], 0, 'Material conditional.'),
    Q(T4, '"p → q; p; therefore q" is:', ['modus ponens', 'modus tollens', 'affirming the consequent', 'denying the antecedent'], 0, 'Valid.'),
    Q(T4, '"p → q; ¬q; therefore ¬p" is:', ['modus tollens', 'modus ponens', 'denying the antecedent', 'disjunctive syllogism'], 0, 'Valid.'),
    Q(T4, '"If it rained, the ground is wet. The ground is wet. So it rained." commits:', ['affirming the consequent', 'modus ponens', 'modus tollens', 'hypothetical syllogism'], 0, 'Invalid.'),
    Q(T4, '"p → q; ¬p; therefore ¬q" is:', ['denying the antecedent (invalid)', 'modus tollens (valid)', 'modus ponens (valid)', 'disjunctive syllogism (valid)'], 0, 'Formal fallacy.'),
    Q(T4, '"p ∨ q; ¬p; therefore q" is:', ['disjunctive syllogism', 'affirming the consequent', 'hypothetical syllogism', 'denying the antecedent'], 0, 'Valid.'),
    Q(T4, 'An argument form is invalid if its truth table has a row where:', ['all premises are true and the conclusion is false', 'all premises are false', 'the conclusion is true', 'every value is true'], 0, 'Definition of invalidity.'),
]

FLASH = [
    ['Connectives', '¬ not, ∧ and, ∨ or, → if...then, ↔ iff.'],
    ['Rows in a truth table', '2ⁿ for n variables.'],
    ['p → q false when', 'p true and q false.'],
    ['De Morgan', '¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q.'],
    ['Contrapositive', 'p → q ≡ ¬q → ¬p.'],
    ['Modus ponens', 'p → q, p ∴ q.'],
    ['Modus tollens', 'p → q, ¬q ∴ ¬p.'],
    ['Affirming the consequent', 'p → q, q ∴ p: invalid.'],
]
