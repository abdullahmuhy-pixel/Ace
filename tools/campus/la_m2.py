"""Linear Algebra, module 2: Matrix algebra."""
from verify import Q, sp
M = sp.Matrix
T1, T2, T3, T4 = ('Matrix operations', 'Transpose and special matrices', 'The inverse of a matrix', 'Matrix equations and invertibility')

A = M([[1, 2], [3, 4]]); B = M([[0, 1], [1, 0]]); C2 = M([[2, 1], [5, 3]])

MODULE = {
    'title': 'Matrix algebra',
    'topics': [T1, T2, T3, T4],
    'overview': 'Matrices are more than tables of numbers: they can be added, multiplied and, sometimes, inverted. This module builds that algebra and shows how a whole linear system becomes the single equation Ax = b.',
    'key_terms': ['Matrix', 'Order (m × n)', 'Matrix product', 'Identity', 'Transpose', 'Symmetric', 'Inverse', 'Invertible', 'Singular'],
    'explanation': [
        'Matrix multiplication combines rows of the first matrix with columns of the second. It is defined only when the inner sizes match, and in general AB ≠ BA, which is the biggest surprise for students used to numbers.',
        'The inverse A⁻¹ plays the role of division: AA⁻¹ = I. Only square matrices with non-zero determinant (equivalently, full rank) have one.',
        'The Invertible Matrix Theorem ties the course together: for a square matrix, having an inverse, having full rank, having only the trivial solution to Ax = 0 and having non-zero determinant all mean the same thing.'],
    'quick_facts': ['(m × n)(n × p) gives m × p.', 'AB ≠ BA in general.', '(AB)ᵀ = BᵀAᵀ and (AB)⁻¹ = B⁻¹A⁻¹.', '[a b ; c d]⁻¹ = (1/(ad − bc))[d −b ; −c a].', 'A square matrix is invertible exactly when det A ≠ 0.'],
}

NOTES = {
    T1: {
        'overview': 'Matrices of the same size add entry by entry, and any matrix can be multiplied by a number. The matrix product is different: each entry is a row of the first matrix dotted with a column of the second.',
        'key_terms': ['Order m × n', 'Entry aᵢⱼ', 'Scalar multiple', 'Matrix product', 'Identity matrix I', 'Zero matrix'],
        'explanation': [
            'A matrix with m rows and n columns has order m × n, and aᵢⱼ is the entry in row i, column j. Addition and scalar multiplication work entry by entry and need matching sizes for addition.',
            'For AB to exist, the number of columns of A must equal the number of rows of B. The entry in row i, column j of AB is row i of A dotted with column j of B: multiply matching entries and add.',
            'Order matters. With A = [1 2 ; 3 4] and B = [0 1 ; 1 0], AB = [2 1 ; 4 3] swaps the columns of A, while BA = [3 4 ; 1 2] swaps its rows. The identity matrix I, with 1s on the diagonal and 0s elsewhere, satisfies AI = IA = A.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['(AB)ᵢⱼ = Σₖ aᵢₖbₖⱼ', '(m × n)(n × p) = m × p', 'A(B + C) = AB + AC', '(AB)C = A(BC)', 'AI = IA = A'],
        'steps': ['Check the sizes: inner numbers must match.', 'Write the size of the answer: outer numbers.', 'For each entry, take the matching row of the first and column of the second.', 'Multiply pairwise and add.', 'Double-check one entry by recomputing it.'],
        'worked_example': {
            'problem': 'Compute AB for A = [1 2 ; 3 4] and B = [0 1 ; 1 0].',
            'steps': ['Row 1 · column 1: 1·0 + 2·1 = 2. Row 1 · column 2: 1·1 + 2·0 = 1.', 'Row 2 · column 1: 3·0 + 4·1 = 4. Row 2 · column 2: 3·1 + 4·0 = 3.'],
            'answer': 'AB = [2 1 ; 4 3].',
            'check': 'B swaps coordinates, so multiplying on the right should swap the columns of A, which it does. ✓'},
        'mistakes': ['Multiplying entry by entry instead of rows by columns.', 'Assuming AB = BA.', 'Multiplying matrices whose inner sizes do not match.', 'Adding matrices of different sizes.'],
        'real_world': 'Every frame of a 3D game multiplies thousands of points by rotation and projection matrices. Graphics cards are, at heart, very fast matrix multipliers.',
        'exam_strategy': 'Write the order of each matrix above it before multiplying. It immediately shows whether the product exists and what size it is.',
        'recap': ['Inner sizes must match to multiply.', 'Entry = row · column.', 'AB ≠ BA in general.', 'AI = IA = A.']},
    T2: {
        'overview': 'The transpose flips a matrix over its main diagonal. It defines symmetric matrices and has a product rule that reverses order. Diagonal and triangular matrices are special shapes that make calculations easy.',
        'key_terms': ['Transpose Aᵀ', 'Symmetric (Aᵀ = A)', 'Skew-symmetric (Aᵀ = −A)', 'Diagonal matrix', 'Upper and lower triangular', 'Trace'],
        'explanation': [
            'The transpose turns rows into columns: (Aᵀ)ᵢⱼ = aⱼᵢ. An m × n matrix becomes n × m. Transposing twice returns the original.',
            'A square matrix is symmetric when Aᵀ = A, so it mirrors across the diagonal. AᵀA is always symmetric, which is why it appears in statistics and least squares.',
            'Diagonal matrices have zeros off the diagonal; their products and powers just multiply the diagonal entries. Triangular matrices have zeros on one side of the diagonal, and their determinant is the product of the diagonal. The trace is the sum of the diagonal entries.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['(Aᵀ)ᵀ = A', '(A + B)ᵀ = Aᵀ + Bᵀ', '(AB)ᵀ = BᵀAᵀ', 'Symmetric: Aᵀ = A', 'tr(A) = a₁₁ + a₂₂ + … + aₙₙ'],
        'steps': ['To transpose, write row 1 as column 1, row 2 as column 2, and so on.', 'To test symmetry, compare aᵢⱼ with aⱼᵢ for each pair.', 'For a transpose of a product, reverse the order.', 'For powers of a diagonal matrix, raise each diagonal entry to the power.'],
        'worked_example': {
            'problem': 'For A = [1 2 ; 3 4], find Aᵀ and the trace, and decide whether A is symmetric.',
            'steps': ['Rows become columns: Aᵀ = [1 3 ; 2 4].', 'Trace = 1 + 4 = 5.', 'a₁₂ = 2 but a₂₁ = 3, so A is not symmetric.'],
            'answer': 'Aᵀ = [1 3 ; 2 4], tr A = 5, not symmetric.',
            'check': '(Aᵀ)ᵀ = [1 2 ; 3 4] = A ✓.'},
        'mistakes': ['Writing (AB)ᵀ = AᵀBᵀ instead of BᵀAᵀ.', 'Calling a non-square matrix symmetric.', 'Forgetting that transposing changes the order from m × n to n × m.', 'Including off-diagonal entries in the trace.'],
        'real_world': 'A table of distances between cities is symmetric, because the distance from Lagos to Accra equals the distance from Accra to Lagos.',
        'exam_strategy': 'When a proof involves a transpose of a product, write the reversed order explicitly on its own line. It is the step most often marked.',
        'recap': ['Transpose swaps rows and columns.', '(AB)ᵀ = BᵀAᵀ.', 'Symmetric: Aᵀ = A.', 'Trace = sum of the diagonal.']},
    T3: {
        'overview': 'The inverse of a square matrix A is the matrix A⁻¹ with AA⁻¹ = A⁻¹A = I. For 2 × 2 matrices there is a quick formula; for larger ones you row-reduce [A | I].',
        'key_terms': ['Inverse A⁻¹', 'Invertible (non-singular)', 'Singular', 'Determinant of a 2 × 2', 'Gauss–Jordan method'],
        'explanation': [
            'For A = [a b ; c d], if ad − bc ≠ 0 then A⁻¹ = (1/(ad − bc))[d −b ; −c a]: swap the diagonal entries, change the signs of the other two, and divide by the determinant. If ad − bc = 0 the matrix is singular and has no inverse.',
            'For larger matrices, write [A | I] and row-reduce. If the left side becomes I, the right side is A⁻¹. If a zero row appears on the left, A is not invertible.',
            'Inverses reverse order: (AB)⁻¹ = B⁻¹A⁻¹. Think of putting on socks then shoes; you take off shoes first.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['AA⁻¹ = A⁻¹A = I', '[a b ; c d]⁻¹ = (1/(ad − bc))[d −b ; −c a]', '(AB)⁻¹ = B⁻¹A⁻¹', '(A⁻¹)ᵀ = (Aᵀ)⁻¹', '[A | I] → [I | A⁻¹]'],
        'steps': ['Compute det A = ad − bc (2 × 2).', 'If it is 0, stop: no inverse.', 'Swap a and d, negate b and c.', 'Divide every entry by the determinant.', 'Check AA⁻¹ = I.'],
        'worked_example': {
            'problem': 'Find the inverse of A = [2 1 ; 5 3].',
            'steps': ['det A = 2·3 − 1·5 = 1.', 'Swap and negate: [3 −1 ; −5 2].', 'Divide by 1.'],
            'answer': 'A⁻¹ = [3 −1 ; −5 2].',
            'check': 'AA⁻¹ = [6 − 5, −2 + 2 ; 15 − 15, −5 + 6] = [1 0 ; 0 1] ✓.'},
        'mistakes': ['Swapping b and c instead of a and d.', 'Forgetting to divide by the determinant.', 'Trying to invert a matrix with determinant 0.', 'Writing (AB)⁻¹ = A⁻¹B⁻¹.'],
        'real_world': 'Classic encryption methods such as the Hill cipher scramble a message by multiplying by a matrix. Only someone who knows the inverse matrix can unscramble it.',
        'exam_strategy': 'Always finish an inverse question by multiplying back to get I. It catches a wrong sign immediately, and examiners give credit for the check.',
        'recap': ['Inverse exists only if det ≠ 0.', '2 × 2: swap, negate, divide.', 'Larger: reduce [A | I].', '(AB)⁻¹ = B⁻¹A⁻¹.']},
    T4: {
        'overview': 'Any linear system can be written as Ax = b. When A is invertible, the solution is x = A⁻¹b. The Invertible Matrix Theorem lists the many conditions that are equivalent to being invertible.',
        'key_terms': ['Matrix equation Ax = b', 'Coefficient matrix', 'Invertible Matrix Theorem', 'Unique solution', 'Singular matrix'],
        'explanation': [
            'The system 2x + y = 4, 5x + 3y = 11 is the single equation Ax = b with A = [2 1 ; 5 3], x = (x, y) and b = (4, 11). If A is invertible, multiply both sides on the left by A⁻¹ to get x = A⁻¹b.',
            'For an n × n matrix A, these are equivalent: A is invertible; Ax = b has exactly one solution for every b; Ax = 0 has only the trivial solution; A has rank n; the RREF of A is I; det A ≠ 0; the columns of A are linearly independent.',
            'If any one fails, they all fail. So a single zero determinant tells you that Ax = 0 has non-trivial solutions and that the columns are dependent.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Ax = b, x = A⁻¹b (A invertible)', 'Invertible ⇔ rank n ⇔ det ≠ 0', 'Invertible ⇔ Ax = 0 has only x = 0', 'Solve AX = B by X = A⁻¹B, and XA = B by X = BA⁻¹'],
        'steps': ['Write the coefficient matrix A, unknown vector x and constant vector b.', 'Check A is invertible (det ≠ 0).', 'Find A⁻¹.', 'Multiply A⁻¹ by b on the left.', 'Check by computing Ax.'],
        'worked_example': {
            'problem': 'Solve 2x + y = 4 and 5x + 3y = 11 using an inverse.',
            'steps': ['A = [2 1 ; 5 3], so A⁻¹ = [3 −1 ; −5 2] from the previous topic.', 'x = A⁻¹b = (3·4 − 1·11, −5·4 + 2·11) = (1, 2).'],
            'answer': 'x = 1, y = 2.',
            'check': '2 + 2 = 4 ✓ and 5 + 6 = 11 ✓.'},
        'mistakes': ['Multiplying b on the left instead: bA⁻¹ is not defined for a column vector.', 'Using x = A⁻¹b when det A = 0.', 'Forgetting that XA = B needs X = BA⁻¹, not A⁻¹B.', 'Thinking a singular A means no solution for every b. Some b may still give infinitely many.'],
        'real_world': 'Economists use input–output models of the form x = (I − A)⁻¹d to work out how much each industry must produce to meet consumer demand d.',
        'exam_strategy': 'Name the theorem when you use it: "since det A ≠ 0, A is invertible, so the system has a unique solution". Reasoning sentences earn marks on their own.',
        'recap': ['Systems become Ax = b.', 'x = A⁻¹b when A is invertible.', 'Invertible ⇔ det ≠ 0 ⇔ rank n.', 'Multiply by the inverse on the correct side.']},
}

fm = lambda m: '[' + ' ; '.join(' '.join(str(v).replace('-', '−') for v in m.row(i)) for i in range(m.rows)) + ']'
QUESTIONS = [
    # T1
    Q(T1, 'Compute AB for A = [1 2 ; 3 4] and B = [0 1 ; 1 0].', [fm(A * B), fm(B * A), fm(A), '[0 2 ; 3 0]'], 0, 'Each entry is a row of A dotted with a column of B. Right-multiplying by B swaps the columns of A.', ans=A * B),
    Q(T1, 'For the same A and B, what is BA?', [fm(A * B), fm(B * A), fm(A.T), fm(A + B)], 1, 'Left-multiplying by B swaps the rows of A. AB ≠ BA.', ans=B * A),
    Q(T1, 'A is 2 × 3 and B is 3 × 4. What is the order of AB?', ['2 × 4', '3 × 3', '4 × 2', 'AB is not defined'], 0, 'The inner 3s match; the outer numbers give 2 × 4.'),
    Q(T1, 'A is 2 × 3 and B is 2 × 3. Which product is defined?', ['ABᵀ', 'AB', 'BA', 'None of them'], 0, 'Bᵀ is 3 × 2, so ABᵀ is (2 × 3)(3 × 2) = 2 × 2.'),
    Q(T1, 'Compute 3[1 −2 ; 0 4] − [2 1 ; 1 1].', ['[1 −7 ; −1 11]', '[1 −5 ; −1 11]', '[3 −6 ; 0 12]', '[1 −7 ; 1 11]'], 0, 'Entry by entry: 3 − 2 = 1, −6 − 1 = −7, 0 − 1 = −1, 12 − 1 = 11.', ans=3 * M([[1, -2], [0, 4]]) - M([[2, 1], [1, 1]])),
    Q(T1, 'What is A² for A = [1 1 ; 0 1]?', ['[1 2 ; 0 1]', '[1 1 ; 0 1]', '[2 2 ; 0 2]', '[1 0 ; 0 1]'], 0, 'Row 1 · column 2 = 1·1 + 1·1 = 2; the rest stay the same.', ans=M([[1, 1], [0, 1]]) ** 2),
    # T2
    Q(T2, 'What is the transpose of [1 2 3 ; 4 5 6]?', ['[1 4 ; 2 5 ; 3 6]', '[1 2 3 ; 4 5 6]', '[6 5 4 ; 3 2 1]', '[3 2 1 ; 6 5 4]'], 0, 'Rows become columns, so the 2 × 3 matrix becomes 3 × 2.', ans=M([[1, 2, 3], [4, 5, 6]]).T),
    Q(T2, 'Which matrix is symmetric?', ['[2 −1 ; −1 5]', '[2 1 ; −1 5]', '[0 1 ; 2 0]', '[1 2 3 ; 2 4 5]'], 0, 'a₁₂ = a₂₁ = −1, and it is square.'),
    Q(T2, '(AB)ᵀ equals:', ['BᵀAᵀ', 'AᵀBᵀ', 'BA', 'AB'], 0, 'Transposing a product reverses the order.'),
    Q(T2, 'What is the trace of [3 1 0 ; 2 −1 4 ; 7 5 6]?', ['8', '9', '10', '27'], 0, 'Sum of the diagonal: 3 + (−1) + 6 = 8.', ans=M([[3, 1, 0], [2, -1, 4], [7, 5, 6]]).trace()),
    Q(T2, 'If D = [2 0 ; 0 3], what is D³?', ['[8 0 ; 0 27]', '[6 0 ; 0 9]', '[8 0 ; 0 9]', '[2 0 ; 0 3]'], 0, 'Powers of a diagonal matrix power each diagonal entry: 2³ = 8 and 3³ = 27.', ans=M([[2, 0], [0, 3]]) ** 3),
    Q(T2, 'For any matrix A, the matrix AᵀA is always:', ['symmetric', 'diagonal', 'invertible', 'the identity'], 0, '(AᵀA)ᵀ = Aᵀ(Aᵀ)ᵀ = AᵀA.'),
    # T3
    Q(T3, 'Find the inverse of [2 1 ; 5 3].', [fm(C2.inv()), '[3 1 ; 5 2]', '[−3 1 ; 5 −2]', '[3 −5 ; −1 2]'], 0, 'det = 6 − 5 = 1; swap the diagonal and negate the off-diagonal entries.', ans=C2.inv()),
    Q(T3, 'Find the inverse of [4 2 ; 3 2].', ['[1 −1 ; −3/2 2]', '[2 −2 ; −3 4]', '[1/2 −1 ; −3/2 2]', '[1 −1 ; 3/2 2]'], 0, 'det = 8 − 6 = 2, so A⁻¹ = ½[2 −2 ; −3 4].', ans=M([[4, 2], [3, 2]]).inv()),
    Q(T3, 'Which matrix has no inverse?', ['[2 4 ; 1 2]', '[2 4 ; 1 3]', '[1 0 ; 0 1]', '[0 1 ; 1 0]'], 0, 'det = 2·2 − 4·1 = 0, so it is singular.'),
    Q(T3, '(AB)⁻¹ equals:', ['B⁻¹A⁻¹', 'A⁻¹B⁻¹', 'BA', '1/(AB)'], 0, '(AB)(B⁻¹A⁻¹) = A(BB⁻¹)A⁻¹ = AA⁻¹ = I.'),
    Q(T3, 'For which k is [k 2 ; 3 6] NOT invertible?', ['1', '2', '3', '6'], 0, 'det = 6k − 6 = 0 when k = 1.', ans=sp.solve(sp.Matrix([[sp.Symbol('k'), 2], [3, 6]]).det(), sp.Symbol('k'))[0]),
    Q(T3, 'The inverse of the identity matrix I is:', ['I', '0', '−I', 'It has none'], 0, 'I · I = I.'),
    # T4
    Q(T4, 'Solve 2x + y = 4, 5x + 3y = 11 using x = A⁻¹b. What is the solution?', ['(1, 2)', '(2, 0)', '(−1, 6)', '(1, 3)'], 0, 'A⁻¹ = [3 −1 ; −5 2]; A⁻¹(4, 11) = (12 − 11, −20 + 22) = (1, 2).', ans=C2.inv() * M([4, 11])),
    Q(T4, 'If det A = 0 for a square matrix A, then Ax = 0 has:', ['non-trivial solutions', 'only the solution x = 0', 'no solutions', 'exactly two solutions'], 0, 'det A = 0 means A is not invertible, so by the Invertible Matrix Theorem Ax = 0 has non-trivial solutions.'),
    Q(T4, 'Which statement is NOT equivalent to "the 3 × 3 matrix A is invertible"?', ['A has a zero row', 'rank A = 3', 'det A ≠ 0', 'the RREF of A is I'], 0, 'A zero row makes det A = 0, the opposite of being invertible.'),
    Q(T4, 'To solve XA = B for X (A invertible), use:', ['X = BA⁻¹', 'X = A⁻¹B', 'X = B − A', 'X = AB⁻¹'], 0, 'Multiply both sides on the right by A⁻¹.'),
    Q(T4, 'Solve [1 2 ; 3 5]x = (1, 2). What is x?', ['(−1, 1)', '(1, −1)', '(1, 0)', '(−1, 2)'], 0, 'A⁻¹ = (1/−1)[5 −2 ; −3 1] = [−5 2 ; 3 −1]; A⁻¹(1, 2) = (−5 + 4, 3 − 2) = (−1, 1).', ans=M([[1, 2], [3, 5]]).inv() * M([1, 2])),
    Q(T4, 'If the columns of a square matrix A are linearly independent, then:', ['A is invertible', 'det A = 0', 'Ax = b has no solution for some b', 'A is the identity'], 0, 'Independent columns give full rank, which is one of the equivalent conditions.'),
]

FLASH = [
    ['Matrix product size', '(m × n)(n × p) = m × p.'], ['Does AB = BA?', 'Not in general.'],
    ['(AB)ᵀ', 'BᵀAᵀ'], ['Symmetric matrix', 'Aᵀ = A.'], ['2 × 2 inverse', '[a b ; c d]⁻¹ = (1/(ad − bc))[d −b ; −c a].'],
    ['(AB)⁻¹', 'B⁻¹A⁻¹'], ['Finding A⁻¹ for large A', 'Row-reduce [A | I] to [I | A⁻¹].'],
    ['Invertible Matrix Theorem (core)', 'Invertible ⇔ rank n ⇔ det ≠ 0 ⇔ Ax = 0 only has x = 0.'],
]
