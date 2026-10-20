"""Linear Algebra, module 5: Linear transformations, eigenvalues and orthogonality."""
from verify import Q, sp
M = sp.Matrix
T1, T2, T3, T4 = ('Linear transformations and their matrices', 'Eigenvalues and eigenvectors', 'Diagonalisation', 'Orthogonality and projections')
A = M([[4, 1], [2, 3]])
lam = sp.Symbol('λ')

MODULE = {
    'title': 'Linear transformations and eigenvalues',
    'topics': [T1, T2, T3, T4],
    'overview': 'Matrices are machines that move vectors. This module reads a matrix as a transformation, finds the special directions it only stretches (eigenvectors), uses them to simplify powers of a matrix, and finishes with projections, the geometry behind least squares.',
    'key_terms': ['Linear transformation', 'Standard matrix', 'Eigenvalue', 'Eigenvector', 'Characteristic polynomial', 'Diagonalisable', 'Orthogonal projection', 'Orthonormal basis'],
    'explanation': [
        'A linear transformation T keeps addition and scaling: T(u + v) = T(u) + T(v) and T(cu) = cT(u). Every such T from Rⁿ to Rᵐ is multiplication by a matrix whose columns are the images of the standard basis vectors.',
        'An eigenvector is a non-zero vector that A only stretches: Av = λv. The eigenvalues are the roots of det(A − λI) = 0. When A has enough independent eigenvectors, A = PDP⁻¹ with D diagonal, and powers become easy.',
        'Orthogonal projection drops a vector onto a line or subspace at a right angle. It gives the closest point and is the idea behind least-squares fitting.'],
    'quick_facts': ['Columns of the standard matrix are T(e₁), …, T(eₙ).', 'Eigenvalues solve det(A − λI) = 0.', 'Sum of eigenvalues = trace; product = determinant.', 'n distinct eigenvalues ⇒ diagonalisable.', 'proj of y onto u = (y·u / u·u) u.'],
}

NOTES = {
    T1: {
        'overview': 'A linear transformation is a function between vector spaces that respects addition and scaling. In Rⁿ every one of them is a matrix, and the matrix can be read off from where the basis vectors go.',
        'key_terms': ['Linear transformation', 'Standard matrix', 'Image', 'Kernel', 'Rotation', 'Reflection', 'Composition'],
        'explanation': [
            'T is linear if T(u + v) = T(u) + T(v) and T(cu) = cT(u) for all vectors and scalars. A quick test: a linear map must send 0 to 0, so T(x, y) = (x + 1, y) is not linear.',
            'The standard matrix has columns T(e₁), T(e₂), …. For a rotation of the plane by θ anticlockwise, e₁ goes to (cos θ, sin θ) and e₂ goes to (−sin θ, cos θ), giving [cos θ −sin θ ; sin θ cos θ]. Reflection in the x-axis is [1 0 ; 0 −1].',
            'Doing S after T is the transformation with matrix BA (the matrix of the map applied first goes on the right). The kernel of T is the null space of its matrix; its range is the column space.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['T(u + v) = T(u) + T(v), T(cu) = cT(u)', 'A = [T(e₁) T(e₂) … T(eₙ)]', 'Rotation by θ: [cos θ −sin θ ; sin θ cos θ]', 'S after T has matrix BA', 'ker T = Nul A, range T = Col A'],
        'steps': ['Check T(0) = 0 as a quick linearity test.', 'Find T(e₁), T(e₂), … .', 'Place them as the columns of A.', 'Use Ax to compute T(x).', 'For compositions, multiply matrices with the first map on the right.'],
        'worked_example': {
            'problem': 'Find the matrix of the rotation by 90° anticlockwise and the image of (3, 1).',
            'steps': ['e₁ = (1, 0) goes to (0, 1); e₂ = (0, 1) goes to (−1, 0).', 'A = [0 −1 ; 1 0].', 'A(3, 1) = (0·3 − 1·1, 1·3 + 0·1) = (−1, 3).'],
            'answer': 'A = [0 −1 ; 1 0] and T(3, 1) = (−1, 3).',
            'check': 'Lengths match: ‖(3, 1)‖ = ‖(−1, 3)‖ = √10, and the dot product is −3 + 3 = 0, so the turn is 90° ✓.'},
        'mistakes': ['Putting T(eᵢ) in rows instead of columns.', 'Calling a map with a constant term linear.', 'Multiplying composition matrices in the wrong order.', 'Using clockwise and anticlockwise rotation matrices interchangeably.'],
        'real_world': 'Every movement in a 3D game, turning the camera, scaling a model, is a matrix applied to thousands of vertex vectors many times a second on the graphics card.',
        'exam_strategy': 'Draw the unit square and its image. Where e₁ and e₂ land is the whole matrix, and the picture catches sign errors.',
        'recap': ['Linear: preserves + and scaling.', 'Columns of A are T(e₁), T(e₂), … .', 'Linear maps send 0 to 0.', 'Composition = matrix product, first map on the right.']},
    T2: {
        'overview': 'An eigenvector of A is a non-zero vector whose direction A does not change; it is only stretched by the eigenvalue λ. These special directions reveal how A acts.',
        'key_terms': ['Eigenvalue λ', 'Eigenvector', 'Characteristic polynomial', 'Characteristic equation', 'Eigenspace', 'Trace'],
        'explanation': [
            'Av = λv with v ≠ 0. Rearranging gives (A − λI)v = 0, which has a non-zero solution only when A − λI is singular, so det(A − λI) = 0. This is the characteristic equation; its roots are the eigenvalues.',
            'For each eigenvalue, the eigenvectors are the non-zero solutions of (A − λI)v = 0, so you find them by row reduction. Together with 0 they form the eigenspace.',
            'Checks: the eigenvalues add up to the trace (the sum of the diagonal) and multiply to the determinant. A triangular matrix has its diagonal entries as eigenvalues. λ = 0 is an eigenvalue exactly when A is not invertible.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Av = λv, v ≠ 0', 'det(A − λI) = 0', '2 × 2: λ² − (tr A)λ + det A = 0', 'Σλ = tr A, Πλ = det A', 'Triangular: eigenvalues on the diagonal'],
        'steps': ['Form A − λI.', 'Expand det(A − λI) and set it to 0.', 'Solve for λ.', 'For each λ, solve (A − λI)v = 0.', 'Check with Av = λv and the trace/determinant rules.'],
        'worked_example': {
            'problem': 'Find the eigenvalues and eigenvectors of A = [4 1 ; 2 3].',
            'steps': ['det(A − λI) = (4 − λ)(3 − λ) − 2 = λ² − 7λ + 10.', 'Roots: λ = 2 and λ = 5.', 'λ = 5: A − 5I = [−1 1 ; 2 −2], so v = (1, 1).', 'λ = 2: A − 2I = [2 1 ; 2 1], so v = (1, −2).'],
            'answer': 'λ = 5 with v = (1, 1); λ = 2 with v = (1, −2).',
            'check': 'A(1, 1) = (5, 5) = 5(1, 1) ✓, and 2 + 5 = 7 = trace, 2 × 5 = 10 = det ✓.'},
        'mistakes': ['Giving the zero vector as an eigenvector.', 'Subtracting λ from every entry instead of only the diagonal.', 'Expecting the eigenvector to be unique. Any non-zero multiple works.', 'Forgetting to check Av = λv at the end.'],
        'real_world': 'Google\'s original PageRank scored web pages using the eigenvector for eigenvalue 1 of a huge matrix describing links between pages.',
        'exam_strategy': 'For 2 × 2 matrices write the characteristic polynomial straight from λ² − (trace)λ + det. It is faster and less error-prone than expanding.',
        'recap': ['Av = λv, v ≠ 0.', 'Eigenvalues: det(A − λI) = 0.', 'Eigenvectors: null space of A − λI.', 'Sum = trace, product = det.']},
    T3: {
        'overview': 'A matrix is diagonalisable when it has enough independent eigenvectors to form a basis. Then A = PDP⁻¹, and hard calculations such as A¹⁰ become easy.',
        'key_terms': ['Diagonalisable', 'A = PDP⁻¹', 'Eigenvector matrix P', 'Diagonal matrix D', 'Algebraic multiplicity', 'Geometric multiplicity'],
        'explanation': [
            'If A (n × n) has n linearly independent eigenvectors, put them as the columns of P and the matching eigenvalues on the diagonal of D in the same order. Then AP = PD, so A = PDP⁻¹.',
            'Powers are the big reward: Aᵏ = PDᵏP⁻¹, and Dᵏ just raises each diagonal entry to the power k.',
            'n distinct eigenvalues guarantee diagonalisability. With repeated eigenvalues it depends: [1 1 ; 0 1] has λ = 1 twice but only one independent eigenvector, so it is not diagonalisable.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['A = PDP⁻¹', 'Columns of P: eigenvectors; D: matching eigenvalues', 'Aᵏ = PDᵏP⁻¹', 'Dᵏ = diag(λ₁ᵏ, …, λₙᵏ)', 'n distinct eigenvalues ⇒ diagonalisable'],
        'steps': ['Find all eigenvalues.', 'Find a basis of each eigenspace.', 'If there are n independent eigenvectors in total, A is diagonalisable.', 'Form P from the eigenvectors and D from the eigenvalues in the same order.', 'Use Aᵏ = PDᵏP⁻¹ for powers.'],
        'worked_example': {
            'problem': 'Diagonalise A = [4 1 ; 2 3] and find A³.',
            'steps': ['From the previous topic: λ = 5 with (1, 1), λ = 2 with (1, −2).', 'P = [1 1 ; 1 −2], D = [5 0 ; 0 2].', 'P⁻¹ = (1/3)[2 1 ; 1 −1].', 'A³ = P[125 0 ; 0 8]P⁻¹ = [86 39 ; 78 47].'],
            'answer': 'A = PDP⁻¹ with P = [1 1 ; 1 −2], D = [5 0 ; 0 2]; A³ = [86 39 ; 78 47].',
            'check': 'A² = [18 7 ; 14 11], and A²·A = [86 39 ; 78 47] ✓.'},
        'mistakes': ['Listing eigenvalues in D in a different order from the eigenvectors in P.', 'Writing A = P⁻¹DP (the inverse is on the wrong side).', 'Assuming every matrix is diagonalisable.', 'Thinking a repeated eigenvalue always makes a matrix non-diagonalisable (the identity is diagonal).'],
        'real_world': 'Population models track age groups with a matrix applied year after year. Diagonalising it shows the long-run growth rate: the largest eigenvalue.',
        'exam_strategy': 'After finding P and D, check AP = PD. It needs no inverse and catches order mistakes in seconds.',
        'recap': ['A = PDP⁻¹ needs n independent eigenvectors.', 'Same order in P and D.', 'Aᵏ = PDᵏP⁻¹.', 'Distinct eigenvalues guarantee it.']},
    T4: {
        'overview': 'Orthogonal vectors are at right angles. Orthogonal projection finds the closest point on a line or subspace, and orthonormal bases make coordinates easy. These ideas lead to least squares.',
        'key_terms': ['Orthogonal set', 'Orthonormal set', 'Projection onto a line', 'Orthogonal complement', 'Gram–Schmidt', 'Orthogonal matrix'],
        'explanation': [
            'The projection of y onto the line through u is ŷ = (y·u / u·u)u. The leftover z = y − ŷ is orthogonal to u, and ‖z‖ is the shortest distance from y to the line.',
            'An orthogonal set of non-zero vectors is automatically independent. If it is also made of unit vectors it is orthonormal, and the coordinates of y are simply the dot products y·uᵢ.',
            'Gram–Schmidt turns any basis into an orthogonal one: keep the first vector, then subtract from each new vector its projections onto the ones already chosen. A square matrix with orthonormal columns is orthogonal: QᵀQ = I, so Q⁻¹ = Qᵀ.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['proj_u y = (y·u / u·u) u', 'z = y − proj_u y is orthogonal to u', 'Orthonormal: uᵢ·uⱼ = 0 (i ≠ j), ‖uᵢ‖ = 1', 'Gram–Schmidt: v₂ = x₂ − (x₂·v₁ / v₁·v₁)v₁', 'Orthogonal matrix: QᵀQ = I'],
        'steps': ['Compute y·u and u·u.', 'Scale u by their ratio to get the projection.', 'Subtract to get the orthogonal part.', 'Check the orthogonal part has dot product 0 with u.', 'For Gram–Schmidt, repeat with each new vector.'],
        'worked_example': {
            'problem': 'Project y = (7, 6) onto u = (4, 2), and find the distance from y to the line through u.',
            'steps': ['y·u = 28 + 12 = 40 and u·u = 16 + 4 = 20.', 'ŷ = 2(4, 2) = (8, 4).', 'z = y − ŷ = (−1, 2).', 'Distance = ‖z‖ = √5.'],
            'answer': 'ŷ = (8, 4); distance √5 ≈ 2.24.',
            'check': 'z·u = −4 + 4 = 0, so z is perpendicular to the line ✓.'},
        'mistakes': ['Dividing by ‖u‖ instead of u·u = ‖u‖².', 'Projecting u onto y when asked for y onto u.', 'Forgetting to subtract all earlier projections in Gram–Schmidt.', 'Calling a matrix orthogonal when its columns are orthogonal but not unit length.'],
        'real_world': 'Fitting the best straight line through scattered data (least squares) is a projection of the data vector onto the column space of a matrix. Spreadsheets do it every time you add a trendline.',
        'exam_strategy': 'Always finish a projection by checking that the leftover part is orthogonal to the line. One dot product confirms the whole answer.',
        'recap': ['proj = (y·u / u·u) u.', 'Leftover is perpendicular.', 'Orthogonal non-zero vectors are independent.', 'Orthogonal matrix: Q⁻¹ = Qᵀ.']},
}

P_ = M([[1, 1], [1, -2]]); D_ = sp.diag(5, 2)
QUESTIONS = [
    # T1
    Q(T1, 'Which map from R² to R² is linear?', ['T(x, y) = (2x, x + y)', 'T(x, y) = (x + 1, y)', 'T(x, y) = (x², y)', 'T(x, y) = (xy, 0)'], 0, 'It has no constants or products of variables; the others fail T(0) = 0 or scaling.'),
    Q(T1, 'What is the standard matrix of T(x, y) = (2x, x + y)?', ['[2 0 ; 1 1]', '[2 1 ; 0 1]', '[2 0 ; 0 1]', '[1 1 ; 2 0]'], 0, 'T(e₁) = (2, 1) and T(e₂) = (0, 1) are the columns.', ans=M([[2, 0], [1, 1]])),
    Q(T1, 'Rotating (3, 1) by 90° anticlockwise gives:', ['(−1, 3)', '(1, −3)', '(3, −1)', '(−3, 1)'], 0, '[0 −1 ; 1 0](3, 1) = (−1, 3).', ans=M([[0, -1], [1, 0]]) * M([3, 1])),
    Q(T1, 'What is the matrix of reflection in the x-axis?', ['[1 0 ; 0 −1]', '[−1 0 ; 0 1]', '[0 1 ; 1 0]', '[1 0 ; 0 1]'], 0, 'e₁ stays, e₂ flips to −e₂.', ans=M([[1, 0], [0, -1]])),
    Q(T1, 'T has matrix A = [1 2 ; 0 1]. Find T(1, 1).', ['(3, 1)', '(1, 3)', '(2, 1)', '(3, 2)'], 0, '(1 + 2, 0 + 1) = (3, 1).', ans=M([[1, 2], [0, 1]]) * M([1, 1])),
    Q(T1, 'T has a 3 × 5 matrix of rank 3. What is the dimension of its kernel?', ['2', '3', '5', '0'], 0, 'kernel = null space; nullity = 5 − 3.', ans=2),
    # T2
    Q(T2, 'What are the eigenvalues of A = [4 1 ; 2 3]?', ['2 and 5', '4 and 3', '1 and 6', '−2 and −5'], 0, 'λ² − 7λ + 10 = (λ − 2)(λ − 5).', ans=sorted(A.eigenvals().keys())),
    Q(T2, 'Which is an eigenvector of [4 1 ; 2 3] for λ = 5?', ['(1, 1)', '(1, −2)', '(1, 0)', '(2, 1)'], 0, 'A(1, 1) = (5, 5).', ans=M([1, 1])),
    Q(T2, 'What is the characteristic polynomial of [4 1 ; 2 3]?', ['λ² − 7λ + 10', 'λ² + 7λ + 10', 'λ² − 7λ + 14', 'λ² − 10λ + 7'], 0, 'λ² − (trace)λ + det = λ² − 7λ + 10.', ans=(A - lam * sp.eye(2)).det().expand()),
    Q(T2, 'What are the eigenvalues of [2 7 ; 0 −3]?', ['2 and −3', '2 and 7', '7 and −3', '−1 and 6'], 0, 'The matrix is triangular, so the eigenvalues are its diagonal entries.', ans=sorted(M([[2, 7], [0, -3]]).eigenvals().keys())),
    Q(T2, 'A 3 × 3 matrix has eigenvalues 1, 2 and 4. What is its determinant?', ['8', '7', '1', '0'], 0, 'det = product of eigenvalues = 8.', ans=8),
    Q(T2, 'If 0 is an eigenvalue of A, then A is:', ['not invertible', 'invertible', 'diagonal', 'symmetric'], 0, 'Av = 0v with v ≠ 0 means Ax = 0 has a non-trivial solution.'),
    # T3
    Q(T3, 'For A = [4 1 ; 2 3] with P = [1 1 ; 1 −2], what is D in A = PDP⁻¹?', ['[5 0 ; 0 2]', '[2 0 ; 0 5]', '[4 0 ; 0 3]', '[7 0 ; 0 10]'], 0, 'The columns of P are eigenvectors for 5 and then 2, in that order.', ans=P_.inv() * A * P_),
    Q(T3, 'Find A³ for A = [4 1 ; 2 3].', ['[86 39 ; 78 47]', '[64 1 ; 8 27]', '[125 0 ; 0 8]', '[18 7 ; 14 11]'], 0, 'A³ = PD³P⁻¹, or multiply directly.', ans=A ** 3),
    Q(T3, 'Is [1 1 ; 0 1] diagonalisable?', ['No', 'Yes', 'Only over the complex numbers', 'Only if inverted first'], 0, 'λ = 1 twice, but A − I = [0 1 ; 0 0] gives only one independent eigenvector.'),
    Q(T3, 'A 3 × 3 matrix has eigenvalues 1, 2 and 3. It is:', ['certainly diagonalisable', 'certainly not diagonalisable', 'diagonalisable only if symmetric', 'not invertible'], 0, 'Three distinct eigenvalues give three independent eigenvectors.'),
    Q(T3, 'If A = PDP⁻¹ with D = [2 0 ; 0 −1], then A⁴ = P D⁴ P⁻¹ where D⁴ is:', ['[16 0 ; 0 1]', '[16 0 ; 0 −1]', '[8 0 ; 0 −4]', '[2 0 ; 0 −1]'], 0, 'Raise each diagonal entry: 2⁴ = 16, (−1)⁴ = 1.', ans=sp.diag(2, -1) ** 4),
    Q(T3, 'Which order makes A = PDP⁻¹ correct?', ['Columns of P are eigenvectors in the same order as the eigenvalues in D', 'Rows of P are eigenvectors', 'D holds the eigenvectors', 'P holds the eigenvalues'], 0, 'AP = PD column by column means Avᵢ = λᵢvᵢ.'),
    # T4
    Q(T4, 'Project y = (7, 6) onto u = (4, 2).', ['(8, 4)', '(4, 2)', '(7, 6)', '(2, 1)'], 0, '(40/20)(4, 2) = (8, 4).', ans=(M([7, 6]).dot(M([4, 2])) / M([4, 2]).dot(M([4, 2]))) * M([4, 2])),
    Q(T4, 'What is the distance from (7, 6) to the line through (4, 2)?', ['√5', '5', '√10', '2'], 0, 'The leftover part is (−1, 2), with length √5.', ans=(M([7, 6]) - M([8, 4])).norm()),
    Q(T4, 'Which set is orthonormal?', ['(1, 0) and (0, 1)', '(1, 1) and (1, −1)', '(2, 0) and (0, 2)', '(1, 2) and (2, 1)'], 0, 'Perpendicular and both of length 1. (1, 1), (1, −1) are orthogonal but not unit length.'),
    Q(T4, 'If Q is an orthogonal matrix, then Q⁻¹ equals:', ['Qᵀ', 'Q', '−Q', 'det(Q)·Q'], 0, 'QᵀQ = I.'),
    Q(T4, 'Gram–Schmidt on x₁ = (1, 1), x₂ = (1, 0) gives v₂ =', ['(1/2, −1/2)', '(1, 0)', '(0, 1)', '(1, −1)'], 0, 'v₂ = (1, 0) − (1/2)(1, 1) = (1/2, −1/2).', ans=M([1, 0]) - sp.Rational(1, 2) * M([1, 1])),
    Q(T4, 'Orthogonal non-zero vectors are always:', ['linearly independent', 'linearly dependent', 'of length 1', 'eigenvectors'], 0, 'Dotting a zero combination with each vector forces every coefficient to 0.'),
]

FLASH = [
    ['Linear transformation', 'T(u + v) = T(u) + T(v) and T(cu) = cT(u).'], ['Standard matrix', 'Columns are T(e₁), …, T(eₙ).'],
    ['Rotation by θ', '[cos θ −sin θ ; sin θ cos θ]'], ['Eigenvector', 'Non-zero v with Av = λv.'],
    ['Characteristic equation', 'det(A − λI) = 0'], ['Trace and determinant', 'Sum of eigenvalues = trace; product = det.'],
    ['Diagonalisation', 'A = PDP⁻¹, eigenvectors in P, eigenvalues in D.'], ['Powers', 'Aᵏ = PDᵏP⁻¹'],
    ['Projection onto u', '(y·u / u·u) u'], ['Orthogonal matrix', 'QᵀQ = I, so Q⁻¹ = Qᵀ.'],
]
