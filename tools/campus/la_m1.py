"""Linear Algebra, module 1: Systems of linear equations."""
from verify import Q, sp
M = sp.Matrix
T1, T2, T3, T4 = ('Linear systems and their solutions', 'Gaussian elimination', 'Reduced row echelon form and rank', 'Homogeneous systems and parametric solutions')

MODULE = {
    'title': 'Systems of linear equations',
    'topics': [T1, T2, T3, T4],
    'overview': 'Linear algebra starts with a practical question: how do you solve many linear equations in many unknowns at once? This module turns systems into augmented matrices and solves them by row reduction, the method behind almost everything else in the course.',
    'key_terms': ['Linear equation', 'System', 'Augmented matrix', 'Row operation', 'Row echelon form', 'Pivot', 'Rank', 'Free variable', 'Homogeneous system'],
    'explanation': [
        'A linear system has either no solution, exactly one solution, or infinitely many. Geometrically, two lines in a plane can be parallel, cross once, or lie on top of each other. The same three cases hold in any number of dimensions.',
        'Writing only the coefficients and constants in an augmented matrix, and using three safe row operations, lets you solve any system in an organised way. The pivots and the rank of the matrix tell you which of the three cases you are in before you finish.',
        'In this course a matrix is written row by row with semicolons between rows: [1 2 ; 3 4] has first row 1 2 and second row 3 4. A vector is written as a column in brackets, for example (1, 2, 3).'],
    'quick_facts': [
        'A system has 0, 1 or infinitely many solutions, never exactly 2.',
        'The three row operations: swap rows, multiply a row by a non-zero number, add a multiple of one row to another.',
        'A row [0 0 0 | 5] means no solution.',
        'Number of free variables = number of unknowns − rank.',
        'A homogeneous system Ax = 0 always has the trivial solution x = 0.'],
}

NOTES = {
    T1: {
        'overview': 'A linear equation has each unknown to the first power and no products of unknowns. A system is a set of such equations to be solved together, and its solution set is everything that satisfies all of them at once.',
        'key_terms': ['Linear equation', 'Coefficient', 'Solution set', 'Consistent', 'Inconsistent', 'Augmented matrix'],
        'explanation': [
            'Each linear equation in two unknowns is a line, and in three unknowns a plane. Solving the system means finding the points common to all of them. That is why there are only three possibilities: no common point (inconsistent), exactly one, or infinitely many.',
            'The augmented matrix keeps just the numbers. For x + 2y = 5 and 3x − y = 1 it is [1 2 5 ; 3 −1 1], with the last column holding the constants. Working with the matrix is faster and less error-prone than rewriting the letters every line.',
            'Before solving, decide whether an equation is linear. 3x − 2y + z = 4 is linear. xy = 4, x² + y = 1 and sin x + y = 0 are not, because the unknowns are multiplied together, squared or inside a function.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Linear: a₁x₁ + a₂x₂ + … + aₙxₙ = b', 'Consistent: at least one solution', 'Augmented matrix [A | b]', 'Number of solutions ∈ {0, 1, ∞}'],
        'steps': ['Check every equation is linear.', 'Line up the unknowns in the same order in every equation.', 'Write the coefficients and constants as an augmented matrix.', 'Solve by elimination (next topic).', 'Check the solution in every original equation.'],
        'worked_example': {
            'problem': 'Solve x + 2y = 5 and 3x − y = 1.',
            'steps': ['From the first equation, x = 5 − 2y.', 'Substitute: 3(5 − 2y) − y = 1, so 15 − 7y = 1.', 'So y = 2, and x = 5 − 4 = 1.'],
            'answer': 'x = 1, y = 2: the lines cross at (1, 2).',
            'check': '1 + 2(2) = 5 ✓ and 3(1) − 2 = 1 ✓.'},
        'mistakes': ['Calling xy = 3 a linear equation.', 'Thinking a system can have exactly two solutions.', 'Mixing up the order of the unknowns between equations when building the matrix.', 'Forgetting to check the answer in every equation, not just one.'],
        'real_world': 'A clinic mixes two supplements to reach exact amounts of iron and calcium. Each nutrient gives one linear equation, and solving the system gives the dose of each supplement.',
        'exam_strategy': 'Always check the final answer in every original equation. It takes seconds and catches sign slips that would otherwise cost the whole question.',
        'recap': ['Linear means unknowns to power 1, no products.', 'Solutions: none, one or infinitely many.', 'Augmented matrix = coefficients | constants.', 'Check answers in every equation.']},
    T2: {
        'overview': 'Gaussian elimination uses row operations to turn the augmented matrix into row echelon form, a staircase shape that can be solved from the bottom up by back substitution.',
        'key_terms': ['Elementary row operations', 'Row echelon form (REF)', 'Pivot', 'Back substitution', 'Equivalent systems'],
        'explanation': [
            'The three elementary row operations never change the solution set: swap two rows, multiply a row by a non-zero constant, and add a multiple of one row to another. Systems connected by row operations are called equivalent.',
            'Row echelon form means every non-zero row starts with a leading entry (a pivot) further to the right than the row above, and any all-zero rows are at the bottom. Below each pivot, every entry is zero.',
            'Work column by column: choose a pivot, use it to create zeros underneath, then move down and right. Once in echelon form, solve the last equation first and substitute upwards.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Rᵢ ↔ Rⱼ (swap)', 'Rᵢ → kRᵢ, k ≠ 0 (scale)', 'Rᵢ → Rᵢ + kRⱼ (replace)', 'REF: zeros below each pivot, pivots move right as you go down'],
        'steps': ['Write the augmented matrix.', 'Get a non-zero pivot at the top of the first column (swap if needed).', 'Use it to make every entry below it zero.', 'Repeat for the next column, one row down.', 'Back-substitute from the bottom row up.'],
        'worked_example': {
            'problem': 'Solve x + y + z = 6, 2x + 3y + z = 11, x − y + 2z = 5.',
            'steps': ['Augmented matrix [1 1 1 6 ; 2 3 1 11 ; 1 −1 2 5].', 'R₂ → R₂ − 2R₁ gives [0 1 −1 −1]; R₃ → R₃ − R₁ gives [0 −2 1 −1].', 'R₃ → R₃ + 2R₂ gives [0 0 −1 −3], so z = 3.', 'Row 2: y − z = −1, so y = 2. Row 1: x + 2 + 3 = 6, so x = 1.'],
            'answer': '(x, y, z) = (1, 2, 3).',
            'check': '2 + 6 + 3 = 11 ✓ and 1 − 2 + 6 = 5 ✓.'},
        'mistakes': ['Multiplying a row by 0, which destroys information.', 'Changing only part of a row when adding a multiple of another row.', 'Forgetting to apply the operation to the constants column.', 'Starting back substitution from the top instead of the bottom.'],
        'real_world': 'Engineering software solves systems with millions of unknowns, for stresses in a bridge or currents in a power grid, using refined versions of exactly this elimination process.',
        'exam_strategy': 'Write each row operation beside the matrix, for example R₂ → R₂ − 2R₁. If an arithmetic slip happens, the examiner can still award the method marks.',
        'recap': ['Three row operations keep the solutions the same.', 'Aim for a staircase of pivots.', 'Zeros below each pivot.', 'Back-substitute from the bottom.']},
    T3: {
        'overview': 'Reduced row echelon form goes one step further than echelon form so the solution can be read off directly. The number of pivots, the rank, tells you how many solutions to expect.',
        'key_terms': ['Reduced row echelon form (RREF)', 'Leading 1', 'Rank', 'Pivot column', 'Free variable', 'Consistency test'],
        'explanation': [
            'In RREF every pivot is 1 and is the only non-zero entry in its column. Every matrix has exactly one RREF, so it is a reliable final answer.',
            'The rank of a matrix is the number of pivots in its echelon form. For a system with n unknowns: if a row reads [0 … 0 | c] with c ≠ 0, there is no solution. Otherwise, if rank = n there is exactly one solution, and if rank < n there are infinitely many, with n − rank free variables.',
            'Free variables are the unknowns whose columns have no pivot. You may give them any value; the pivot variables are then determined by them.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['rank(A) = number of pivots', 'Inconsistent ⇔ rank(A) < rank([A | b])', 'Unique solution ⇔ rank(A) = rank([A | b]) = n', 'Free variables = n − rank(A)'],
        'steps': ['Reduce to echelon form.', 'Scale each pivot row so the pivot is 1.', 'Clear the entries above each pivot, working from the right.', 'Read off the solution, or spot an inconsistent row.', 'Count pivots to state the rank.'],
        'worked_example': {
            'problem': 'Find the rank of A = [1 2 3 ; 2 4 6 ; 1 1 1].',
            'steps': ['R₂ → R₂ − 2R₁ gives a zero row [0 0 0].', 'R₃ → R₃ − R₁ gives [0 −1 −2].', 'Swap R₂ and R₃: [1 2 3 ; 0 −1 −2 ; 0 0 0].', 'There are two pivots.'],
            'answer': 'rank(A) = 2.',
            'check': 'Row 2 is twice row 1, so at most two rows are independent, and rows 1 and 3 are clearly not multiples. ✓'},
        'mistakes': ['Counting non-zero entries instead of pivots.', 'Calling a system inconsistent because of a zero row [0 0 0 | 0]. That row is harmless.', 'Forgetting to clear entries above the pivots, which RREF requires.', 'Using rank of A alone to decide consistency without looking at the constants column.'],
        'real_world': 'In data science, the rank of a data matrix shows how many truly independent measurements you have. Two columns that always move together add no new information.',
        'exam_strategy': 'For "how many solutions" questions, compare rank(A), rank([A | b]) and the number of unknowns. Write the three numbers down and the answer follows.',
        'recap': ['RREF: leading 1s, zeros above and below.', 'Rank = number of pivots.', '[0 … 0 | c ≠ 0] means no solution.', 'Free variables = n − rank.']},
    T4: {
        'overview': 'When a system has infinitely many solutions, you describe them all with parameters. Homogeneous systems, with every constant equal to zero, are the cleanest place to practise this, and they lead directly to null spaces later.',
        'key_terms': ['Homogeneous system Ax = 0', 'Trivial solution', 'Non-trivial solution', 'Parameter', 'Parametric vector form'],
        'explanation': [
            'A homogeneous system always has the trivial solution x = 0. It has non-trivial solutions exactly when there is at least one free variable, which always happens when there are more unknowns than equations.',
            'To write the solution set, reduce to RREF, set each free variable equal to a parameter such as t or s, and solve for the pivot variables in terms of those parameters. Collecting terms gives parametric vector form, for example x = t(−2, 1, 0).',
            'For a non-homogeneous system Ax = b with infinitely many solutions, the general solution is one particular solution plus the general solution of Ax = 0.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Ax = 0 always has x = 0', 'More unknowns than equations ⇒ non-trivial solutions to Ax = 0', 'General solution = particular solution + homogeneous solution', 'x = t·v₁ + s·v₂ (parametric vector form)'],
        'steps': ['Reduce [A | 0] to RREF.', 'Identify the free variables (columns without pivots).', 'Set each free variable to a parameter.', 'Express the pivot variables in terms of the parameters.', 'Write the solution as a combination of vectors.'],
        'worked_example': {
            'problem': 'Solve x + 2y − z = 0 and 2x + 4y + z = 0.',
            'steps': ['R₂ → R₂ − 2R₁ gives 3z = 0, so z = 0.', 'Row 1: x + 2y = 0. y has no pivot, so let y = t.', 'Then x = −2t and z = 0.'],
            'answer': '(x, y, z) = t(−2, 1, 0), for any real t.',
            'check': 'With t = 1: −2 + 2 − 0 = 0 ✓ and −4 + 4 + 0 = 0 ✓.'},
        'mistakes': ['Forgetting that x = 0 is always a solution of a homogeneous system.', 'Choosing a pivot variable as the parameter.', 'Writing only one particular solution when infinitely many are asked for.', 'Losing a parameter when there are two free variables.'],
        'real_world': 'Balancing a chemical equation is a homogeneous system: the unknown coefficients must make every element balance, and the parameter is scaled to give the smallest whole numbers.',
        'exam_strategy': 'State clearly which variables are free before you write the parametric solution. Then check the answer by substituting the parameter value 1.',
        'recap': ['Ax = 0 always has the trivial solution.', 'Free variables give parameters.', 'More unknowns than equations ⇒ infinitely many solutions to Ax = 0.', 'General = particular + homogeneous.']},
}

A3 = M([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
QUESTIONS = [
    # T1
    Q(T1, 'Which equation is linear in x, y and z?', ['3x − 2y + z = 4', 'xy + z = 1', 'x² + y = 5', 'sin x + y = 0'], 0, 'Every unknown appears to the first power with no products or functions.'),
    Q(T1, 'How many solutions can a system of linear equations NOT have?', ['None', 'Exactly one', 'Exactly two', 'Infinitely many'], 2, 'If two different solutions exist, every point on the line through them is also a solution, so there are infinitely many.'),
    Q(T1, 'Solve x + 2y = 5 and 3x − y = 1. What is x + y?', ['3', '2', '4', '5'], 0, 'x = 1, y = 2, so x + y = 3.', ans=3),
    Q(T1, 'The lines 2x + y = 3 and 4x + 2y = 7 are:', ['parallel, so there is no solution', 'the same line', 'crossing once', 'perpendicular'], 0, 'The second left side is twice the first, but 7 ≠ 2 × 3, so the lines are parallel and never meet.'),
    Q(T1, 'Which augmented matrix represents x − y = 2 and 3x + 4y = 13?', ['[1 −1 2 ; 3 4 13]', '[1 1 2 ; 3 4 13]', '[1 −1 13 ; 3 4 2]', '[1 3 2 ; −1 4 13]'], 0, 'Each row lists the coefficients of x and y, then the constant.'),
    Q(T1, 'A system with at least one solution is called:', ['consistent', 'inconsistent', 'homogeneous', 'singular'], 0, 'Consistent means the solution set is not empty.'),
    # T2
    Q(T2, 'Which is NOT an elementary row operation?', ['Swap two rows', 'Multiply a row by 0', 'Add 3 times row 1 to row 2', 'Multiply a row by −2'], 1, 'Scaling by 0 wipes out an equation and can change the solutions. The scale factor must be non-zero.'),
    Q(T2, 'Solve x + y + z = 6, 2x + 3y + z = 11, x − y + 2z = 5. What is z?', ['1', '2', '3', '6'], 2, 'Elimination gives −z = −3, so z = 3 (and y = 2, x = 1).', ans=sp.linsolve(M([[1, 1, 1, 6], [2, 3, 1, 11], [1, -1, 2, 5]]), *sp.symbols('x y z')).args[0][2]),
    Q(T2, 'In [2 4 ; 1 5], which operation creates a zero below the first pivot?', ['R₂ → R₂ − ½R₁', 'R₂ → R₂ − 2R₁', 'R₁ → R₁ − 2R₂', 'R₂ → 2R₂'], 0, 'The entry below the pivot 2 is 1, and 1 − ½(2) = 0.'),
    Q(T2, 'After elimination a system becomes x + y = 4, y = 1. What is x?', ['3', '4', '5', '1'], 0, 'Back substitution: x = 4 − 1 = 3.', ans=3),
    Q(T2, 'Which matrix is in row echelon form?', ['[1 2 3 ; 0 1 4 ; 0 0 1]', '[0 1 2 ; 1 0 3 ; 0 0 1]', '[1 2 3 ; 0 0 1 ; 0 1 4]', '[1 2 3 ; 2 1 4 ; 0 0 1]'], 0, 'The pivots step to the right going down, with zeros below each pivot.'),
    Q(T2, 'Solve 2x + y = 7 and x − y = 2. What is y?', ['1', '2', '3', '−1'], 0, 'Add the equations: 3x = 9, so x = 3 and y = 1.', ans=1),
    # T3
    Q(T3, 'What is the rank of [1 2 3 ; 2 4 6 ; 1 1 1]?', ['1', '2', '3', '0'], 1, 'Row 2 is twice row 1, and rows 1 and 3 are independent, so there are two pivots.', ans=A3.rank()),
    Q(T3, 'An augmented matrix reduces to [1 0 2 ; 0 1 3 ; 0 0 5] (last column = constants, 2 unknowns). The system has:', ['no solution', 'exactly one solution', 'infinitely many solutions', 'exactly two solutions'], 0, 'The last row says 0x + 0y = 5, which is impossible.'),
    Q(T3, 'A consistent system has 4 unknowns and its coefficient matrix has rank 2. How many free variables are there?', ['2', '4', '6', '0'], 0, 'Free variables = unknowns − rank = 4 − 2 = 2.', ans=2),
    Q(T3, 'Which matrix is in reduced row echelon form?', ['[1 0 3 ; 0 1 −2]', '[1 2 3 ; 0 1 −2]', '[2 0 3 ; 0 1 −2]', '[1 0 3 ; 1 1 −2]'], 0, 'Each pivot is 1 and is the only non-zero entry in its column.'),
    Q(T3, 'What is the rank of the identity matrix I₃?', ['1', '2', '3', '9'], 2, 'I₃ already has three pivots, one in each row.', ans=sp.eye(3).rank()),
    Q(T3, 'For a square system Ax = b, which guarantees exactly one solution?', ['rank(A) equals the number of unknowns', 'A has a zero row', 'b = 0', 'A has more columns than rows'], 0, 'Full rank leaves no free variables and no inconsistent rows.'),
    # T4
    Q(T4, 'Every homogeneous system Ax = 0 has at least:', ['the solution x = 0', 'two solutions', 'no solution', 'infinitely many solutions'], 0, 'Setting every unknown to 0 makes every equation 0 = 0.'),
    Q(T4, 'Solve x + 2y − z = 0, 2x + 4y + z = 0. Which is the general solution?', ['t(−2, 1, 0)', 't(2, 1, 0)', 't(−2, 1, 1)', '(0, 0, 0) only'], 0, 'Elimination gives z = 0 and x = −2y. Let y = t.'),
    Q(T4, 'A homogeneous system has 3 equations and 5 unknowns. It must have:', ['infinitely many solutions', 'exactly one solution', 'no solution', 'exactly five solutions'], 0, 'The rank is at most 3, so there are at least 2 free variables.'),
    Q(T4, 'If Ax = b has a particular solution p, the general solution is:', ['p plus any solution of Ax = 0', 'p only', 'any solution of Ax = 0', 'p times any solution of Ax = 0'], 0, 'If Ap = b and Ah = 0, then A(p + h) = b.'),
    Q(T4, 'How many free variables does x − y + 2z = 0 have, as a system in x, y and z?', ['1', '2', '3', '0'], 1, 'One equation means rank 1, so 3 − 1 = 2 free variables (y and z).', ans=2),
    Q(T4, 'Which vector is a non-trivial solution of x + y + z = 0 and x − y = 0?', ['(1, 1, −2)', '(1, −1, 0)', '(0, 0, 0)', '(1, 1, 2)'], 0, 'x = y, and z = −x − y = −2x. With x = 1: (1, 1, −2).', ans=M([1, 1, -2])),
]

FLASH = [
    ['Number of solutions of a linear system', '0, 1 or infinitely many.'],
    ['Elementary row operations', 'Swap rows; multiply a row by k ≠ 0; add a multiple of one row to another.'],
    ['Row echelon form', 'Pivots step right going down, zeros below each pivot, zero rows at the bottom.'],
    ['RREF', 'REF with every pivot equal to 1 and zeros above and below each pivot.'],
    ['Rank', 'The number of pivots.'],
    ['Inconsistent row', '[0 … 0 | c] with c ≠ 0.'],
    ['Free variables', 'Number of unknowns − rank.'],
    ['Homogeneous system', 'Ax = 0; always has x = 0.'],
]
