"""Linear Algebra, module 3: Determinants."""
from verify import Q, sp
M = sp.Matrix
T1, T2, T3 = ('Computing determinants', 'Properties of determinants', "Cramer's rule, area and volume")
D3 = M([[2, 0, 1], [1, 3, 2], [1, 1, 1]])

MODULE = {
    'title': 'Determinants',
    'topics': [T1, T2, T3],
    'overview': 'The determinant is a single number attached to a square matrix. It tells you whether the matrix is invertible, how it scales area and volume, and it gives a formula for solving small systems.',
    'key_terms': ['Determinant', 'Minor', 'Cofactor', 'Cofactor expansion', 'Triangular matrix', "Cramer's rule", 'Area scale factor'],
    'explanation': [
        'For a 2 × 2 matrix, det [a b ; c d] = ad − bc. For larger matrices, expand along any row or column using cofactors, choosing the row or column with the most zeros.',
        'Row operations change the determinant in predictable ways, so the fastest method for big matrices is to row-reduce to triangular form and multiply the diagonal.',
        'Geometrically, |det A| is the factor by which A scales area (in 2D) or volume (in 3D). A determinant of 0 means the matrix squashes space flat, which is exactly why it has no inverse.'],
    'quick_facts': ['det [a b ; c d] = ad − bc.', 'Triangular matrix: det = product of the diagonal.', 'Swapping two rows changes the sign.', 'det(AB) = det A · det B.', 'det(kA) = kⁿ det A for an n × n matrix.'],
}

NOTES = {
    T1: {
        'overview': 'Determinants of 2 × 2 matrices take one line. For 3 × 3 and larger, cofactor expansion breaks the job into smaller determinants.',
        'key_terms': ['Minor Mᵢⱼ', 'Cofactor Cᵢⱼ = (−1)^(i+j) Mᵢⱼ', 'Sign pattern', 'Cofactor expansion', 'Triangular matrix'],
        'explanation': [
            'The minor Mᵢⱼ is the determinant left after deleting row i and column j. The cofactor attaches a sign from the chessboard pattern [+ − + ; − + − ; + − +].',
            'Expanding along row 1: det A = a₁₁C₁₁ + a₁₂C₁₂ + a₁₃C₁₃. You can expand along any row or column and get the same answer, so pick the one with the most zeros to save work.',
            'For a triangular matrix every expansion collapses to the product of the diagonal entries. That makes triangular form the target when computing large determinants by row reduction.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['det [a b ; c d] = ad − bc', 'Cᵢⱼ = (−1)^(i+j) Mᵢⱼ', 'det A = Σⱼ aᵢⱼCᵢⱼ (any row i)', 'Triangular: det = a₁₁a₂₂…aₙₙ'],
        'steps': ['Choose the row or column with the most zeros.', 'For each entry, delete its row and column to find the minor.', 'Apply the sign from the chessboard pattern.', 'Multiply each entry by its cofactor and add.', 'Check with a second row or column if time allows.'],
        'worked_example': {
            'problem': 'Find det A for A = [2 0 1 ; 1 3 2 ; 1 1 1].',
            'steps': ['Expand along row 1 (it has a zero).', '2 × det [3 2 ; 1 1] = 2(3 − 2) = 2.', '0 × (…) = 0.', '+1 × det [1 3 ; 1 1] = 1(1 − 3) = −2.', 'Total: 2 + 0 − 2 = 0.'],
            'answer': 'det A = 0, so A is not invertible.',
            'check': 'Column 3 is the average of columns 1 and 2: (2 + 0)/2 = 1, (1 + 3)/2 = 2, (1 + 1)/2 = 1. Dependent columns always give det 0 ✓.'},
        'mistakes': ['Forgetting the alternating signs of the cofactors.', 'Deleting the wrong row or column for a minor.', 'Computing bc − ad instead of ad − bc.', 'Using the "diagonal rule" for 3 × 3 matrices on a 4 × 4 matrix, where it does not work.'],
        'real_world': 'Physics uses 3 × 3 determinants for the cross product of two vectors, which gives the torque on a spanner and the force on a current-carrying wire in a magnetic field.',
        'exam_strategy': 'State which row or column you expand along. If the matrix has a row or column with two zeros, use it: there is then only one minor to compute.',
        'recap': ['2 × 2: ad − bc.', 'Cofactor = signed minor.', 'Expand along the row with most zeros.', 'Triangular: multiply the diagonal.']},
    T2: {
        'overview': 'Determinants behave predictably under row operations and products. These properties make large determinants quick to compute and connect the determinant to invertibility.',
        'key_terms': ['Row swap', 'Row scaling', 'Row replacement', 'det(AB)', 'det(Aᵀ)', 'det(A⁻¹)'],
        'explanation': [
            'Swapping two rows multiplies the determinant by −1. Multiplying one row by k multiplies the determinant by k. Adding a multiple of one row to another leaves it unchanged. So you can row-reduce to triangular form while keeping track of these factors.',
            'The determinant respects products: det(AB) = det A · det B. From this, det(A⁻¹) = 1/det A, and A is invertible exactly when det A ≠ 0. Also det(Aᵀ) = det A, so everything said about rows holds for columns too.',
            'Multiplying the whole n × n matrix by k scales every row, so det(kA) = kⁿ det A. A matrix with two equal rows, or a zero row, has determinant 0.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Swap rows: det → −det', 'Scale a row by k: det → k·det', 'Add a multiple of a row: det unchanged', 'det(AB) = det A · det B', 'det(kA) = kⁿ det A; det(A⁻¹) = 1/det A; det(Aᵀ) = det A'],
        'steps': ['Row-reduce towards triangular form.', 'Record each swap (×−1) and each scaling (×k).', 'Multiply the diagonal of the triangular matrix.', 'Undo the recorded factors to get det of the original.', 'Use product rules for questions about AB, A⁻¹ or kA.'],
        'worked_example': {
            'problem': 'A is 3 × 3 with det A = 4. Find det(2A), det(A⁻¹) and det(AᵀA).',
            'steps': ['det(2A) = 2³ · 4 = 32.', 'det(A⁻¹) = 1/4.', 'det(AᵀA) = det Aᵀ · det A = 4 · 4 = 16.'],
            'answer': '32, 1/4 and 16.',
            'check': 'det(2A) uses 2³ because each of the three rows is multiplied by 2. ✓'},
        'mistakes': ['Writing det(2A) = 2 det A for a 3 × 3 matrix.', 'Thinking det(A + B) = det A + det B. It does not.', 'Forgetting the sign change when swapping rows during reduction.', 'Dividing a row by k without multiplying the determinant back by k.'],
        'real_world': 'Scientific software computes determinants of large matrices by reduction to triangular form, exactly as here, because cofactor expansion would take longer than the age of the universe for a 30 × 30 matrix.',
        'exam_strategy': 'Questions like "det(3A⁻¹Bᵀ)" are pure property questions. Break them into factors and apply one rule per line.',
        'recap': ['Swap: sign flips.', 'Scale a row by k: det × k.', 'Row replacement: no change.', 'det(AB) = det A det B; det(kA) = kⁿ det A.']},
    T3: {
        'overview': "Cramer's rule solves a square system with a formula of determinants. The same determinants measure how a matrix scales areas and volumes.",
        'key_terms': ["Cramer's rule", 'Aᵢ (column i replaced by b)', 'Area of a parallelogram', 'Volume of a parallelepiped', 'Orientation'],
        'explanation': [
            "If det A ≠ 0, the system Ax = b has the unique solution xᵢ = det Aᵢ / det A, where Aᵢ is A with column i replaced by b. It is neat for 2 × 2 and 3 × 3 systems and for showing how a solution depends on the data.",
            'The parallelogram spanned by vectors u and v in the plane has area |det [u v]|, with u and v as columns. In 3D, three vectors span a box-like shape whose volume is |det [u v w]|.',
            'A linear transformation with matrix A multiplies every area by |det A|. A negative determinant also flips orientation, like a mirror image.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['xᵢ = det Aᵢ / det A', 'Area(u, v) = |det [u v]|', 'Volume(u, v, w) = |det [u v w]|', 'Area of image = |det A| × original area'],
        'steps': ['Compute det A and check it is not 0.', 'Replace column i of A by b to form Aᵢ.', 'Compute det Aᵢ.', 'Divide: xᵢ = det Aᵢ / det A.', 'For area or volume, put the vectors as columns and take the absolute value of the determinant.'],
        'worked_example': {
            'problem': "Use Cramer's rule to solve 3x + 2y = 7 and x − y = −1.",
            'steps': ['det A = 3(−1) − 2(1) = −5.', 'A₁ = [7 2 ; −1 −1]: det = −7 + 2 = −5, so x = 1.', 'A₂ = [3 7 ; 1 −1]: det = −3 − 7 = −10, so y = 2.'],
            'answer': 'x = 1, y = 2.',
            'check': '3 + 4 = 7 ✓ and 1 − 2 = −1 ✓.'},
        'mistakes': ['Replacing a row instead of a column with b.', "Using Cramer's rule when det A = 0.", 'Giving a negative area. Take the absolute value.', 'Mixing up which column belongs to which unknown.'],
        'real_world': 'Map software and GPS use determinants to compute the area of irregular plots of land from the coordinates of their corners (the surveyor\'s or shoelace formula).',
        'exam_strategy': "Lay out det A, det A₁, det A₂ in a column before dividing. If det A = 0, say so and switch to elimination.",
        'recap': ["Cramer: xᵢ = det Aᵢ / det A.", 'Needs det A ≠ 0.', 'Area = |det| of the column vectors.', 'Transformations scale area by |det A|.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'det [4 3 ; 2 5] =', ['14', '26', '−14', '22'], 0, '4·5 − 3·2 = 20 − 6 = 14.', ans=M([[4, 3], [2, 5]]).det()),
    Q(T1, 'det [2 0 1 ; 1 3 2 ; 1 1 1] =', ['0', '2', '−2', '4'], 0, 'Expanding along row 1: 2(3 − 2) − 0 + 1(1 − 3) = 0.', ans=D3.det()),
    Q(T1, 'det [3 1 2 ; 0 4 5 ; 0 0 2] =', ['24', '9', '20', '0'], 0, 'Upper triangular: 3 · 4 · 2 = 24.', ans=M([[3, 1, 2], [0, 4, 5], [0, 0, 2]]).det()),
    Q(T1, 'The cofactor C₁₂ of [1 2 3 ; 4 5 6 ; 7 8 10] is:', ['2', '−2', '−6', '6'], 0, 'M₁₂ = det [4 6 ; 7 10] = 40 − 42 = −2, and the sign for (1, 2) is −, so C₁₂ = 2.', ans=M([[1, 2, 3], [4, 5, 6], [7, 8, 10]]).cofactor(0, 1)),
    Q(T1, 'det [1 2 3 ; 4 5 6 ; 7 8 10] =', ['−3', '3', '0', '−1'], 0, 'Row 1 expansion: 1(50 − 48) − 2(40 − 42) + 3(32 − 35) = 2 + 4 − 9 = −3.', ans=M([[1, 2, 3], [4, 5, 6], [7, 8, 10]]).det()),
    Q(T1, 'Which row or column makes det [5 0 2 ; 1 0 3 ; 4 7 6] quickest to compute?', ['Column 2', 'Row 1', 'Row 3', 'Column 3'], 0, 'Column 2 has two zeros, so only one cofactor (for the 7) is needed.'),
    # T2
    Q(T2, 'A is 3 × 3 with det A = 4. What is det(2A)?', ['32', '8', '16', '64'], 0, 'det(2A) = 2³ det A = 8 · 4 = 32.', ans=32),
    Q(T2, 'If det A = 5, what is det(A⁻¹)?', ['1/5', '5', '−5', '25'], 0, 'det(A⁻¹) = 1/det A.', ans=sp.Rational(1, 5)),
    Q(T2, 'Swapping two rows of a matrix with determinant 7 gives determinant:', ['−7', '7', '0', '1/7'], 0, 'Each swap changes the sign.', ans=-7),
    Q(T2, 'If det A = 3 and det B = −2, then det(AB) =', ['−6', '1', '6', '−1'], 0, 'det(AB) = det A · det B.', ans=-6),
    Q(T2, 'Adding 4 times row 1 to row 2 of a matrix with determinant 10 gives:', ['10', '40', '14', '0'], 0, 'Row replacement does not change the determinant.', ans=10),
    Q(T2, 'Which statement is true for all n × n matrices A and B?', ['det(AB) = det(BA)', 'det(A + B) = det A + det B', 'det(2A) = 2 det A', 'det(Aᵀ) = −det A'], 0, 'det(AB) = det A det B = det B det A = det(BA).'),
    # T3
    Q(T3, "Use Cramer's rule on 3x + 2y = 7, x − y = −1. What is y?", ['2', '1', '−2', '3'], 0, 'det A = −5 and det A₂ = det [3 7 ; 1 −1] = −10, so y = 2.', ans=M([[3, 7], [1, -1]]).det() / M([[3, 2], [1, -1]]).det()),
    Q(T3, "In Cramer's rule, A₂ is formed by:", ['replacing column 2 of A with b', 'replacing row 2 of A with b', 'deleting row 2 and column 2', 'multiplying column 2 by b'], 0, 'Each unknown xᵢ uses A with column i replaced by the constants.'),
    Q(T3, 'What is the area of the parallelogram spanned by (3, 1) and (1, 2)?', ['5', '7', '−5', '6'], 0, '|det [3 1 ; 1 2]| = |6 − 1| = 5.', ans=abs(M([[3, 1], [1, 2]]).det())),
    Q(T3, 'A transformation has det A = −3. A shape of area 4 is mapped to a shape of area:', ['12', '−12', '4/3', '7'], 0, 'Areas scale by |det A| = 3; the minus sign only flips orientation.', ans=12),
    Q(T3, 'What is the volume of the box spanned by (1, 0, 0), (0, 2, 0) and (1, 1, 3)?', ['6', '3', '5', '0'], 0, 'det [1 0 1 ; 0 2 1 ; 0 0 3] = 1 · 2 · 3 = 6 (triangular).', ans=abs(M([[1, 0, 1], [0, 2, 1], [0, 0, 3]]).det())),
    Q(T3, "When can Cramer's rule NOT be used?", ['When det A = 0', 'When b = 0', 'When A is 2 × 2', 'When the answer is negative'], 0, 'The formula divides by det A.'),
]

FLASH = [
    ['det of 2 × 2', 'ad − bc'], ['Cofactor', 'Cᵢⱼ = (−1)^(i+j) Mᵢⱼ'], ['Triangular determinant', 'Product of the diagonal.'],
    ['Row swap effect', 'Multiplies det by −1.'], ['det(kA), n × n', 'kⁿ det A'], ['det(AB)', 'det A · det B'],
    ["Cramer's rule", 'xᵢ = det Aᵢ / det A, with column i replaced by b.'], ['Area from a determinant', '|det [u v]|'],
]
