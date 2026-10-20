"""Linear Algebra, module 4: Vectors and vector spaces."""
from verify import Q, sp
M = sp.Matrix
T1, T2, T3, T4 = ('Vectors, dot product, length and angle', 'Span and linear independence', 'Subspaces, basis and dimension', 'Null space, column space and rank–nullity')
u, v = M([1, 2, 2]), M([3, 0, 4])

MODULE = {
    'title': 'Vectors and vector spaces',
    'topics': [T1, T2, T3, T4],
    'overview': 'Vectors are the language of linear algebra. This module measures them (length, angle), combines them (span), asks when they repeat information (independence) and organises them into spaces with a basis and a dimension.',
    'key_terms': ['Vector', 'Dot product', 'Norm', 'Orthogonal', 'Linear combination', 'Span', 'Linear independence', 'Subspace', 'Basis', 'Dimension', 'Null space', 'Column space'],
    'explanation': [
        'The dot product turns two vectors into a number and measures how much they point the same way. It gives lengths, angles and the test for perpendicular (orthogonal) vectors.',
        'A set of vectors is linearly independent if none can be built from the others. A basis is an independent set that spans the whole space, and every basis of a space has the same number of vectors, its dimension.',
        'Every matrix comes with two key subspaces: the null space (solutions of Ax = 0) and the column space (all possible Ax). The rank–nullity theorem links their dimensions.'],
    'quick_facts': ['u · v = u₁v₁ + u₂v₂ + … + uₙvₙ.', '‖v‖ = √(v · v).', 'u ⊥ v ⇔ u · v = 0.', 'More than n vectors in Rⁿ are always dependent.', 'rank A + nullity A = number of columns.'],
}

NOTES = {
    T1: {
        'overview': 'The dot product is the basic measuring tool for vectors. From it come length, distance, the angle between vectors and the test for being perpendicular.',
        'key_terms': ['Dot product u · v', 'Norm ‖v‖', 'Unit vector', 'Angle θ', 'Orthogonal', 'Distance ‖u − v‖'],
        'explanation': [
            'Multiply matching components and add: (1, 2, 2) · (3, 0, 4) = 3 + 0 + 8 = 11. The result is a number (a scalar), not a vector.',
            'Length is ‖v‖ = √(v · v), so ‖(1, 2, 2)‖ = √9 = 3. Dividing by the length gives a unit vector in the same direction. The distance between two points is the length of their difference.',
            'The angle satisfies cos θ = (u · v)/(‖u‖‖v‖). A dot product of 0 means θ = 90°, so the vectors are orthogonal. A positive dot product means an acute angle; negative means obtuse.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['u · v = Σ uᵢvᵢ', '‖v‖ = √(v · v)', 'cos θ = (u · v)/(‖u‖ ‖v‖)', 'u ⊥ v ⇔ u · v = 0', 'Unit vector: v/‖v‖'],
        'steps': ['Multiply matching components.', 'Add the products for the dot product.', 'Square, add and square-root for a length.', 'Divide the dot product by the product of lengths for cos θ.', 'Use inverse cosine for the angle.'],
        'worked_example': {
            'problem': 'Find the angle between u = (1, 2, 2) and v = (3, 0, 4).',
            'steps': ['u · v = 3 + 0 + 8 = 11.', '‖u‖ = √9 = 3 and ‖v‖ = √25 = 5.', 'cos θ = 11/15.', 'θ = cos⁻¹(11/15) ≈ 42.8°.'],
            'answer': 'θ ≈ 42.8°.',
            'check': 'The dot product is positive, so the angle must be acute ✓.'},
        'mistakes': ['Giving the dot product as a vector.', 'Forgetting the square root in the length.', 'Using degrees and radians inconsistently.', 'Saying vectors are orthogonal because their lengths are equal.'],
        'real_world': 'Recommendation systems compare people as vectors of ratings. The cosine of the angle between two people\'s vectors measures how similar their tastes are.',
        'exam_strategy': 'Compute the dot product and both lengths on separate lines before dividing. Leave cos θ as an exact fraction until the final step.',
        'recap': ['Dot product: multiply and add.', 'Length = √(v · v).', 'cos θ = u·v / (‖u‖‖v‖).', 'u · v = 0 means perpendicular.']},
    T2: {
        'overview': 'A linear combination adds scaled copies of vectors. The span is every vector you can make this way. Independence asks whether any vector in a set is redundant.',
        'key_terms': ['Linear combination', 'Span', 'Linear independence', 'Linear dependence', 'Trivial combination'],
        'explanation': [
            'A linear combination of v₁, …, vₖ is c₁v₁ + … + cₖvₖ. Asking whether b is in the span of the vᵢ is the same as asking whether the system with augmented matrix [v₁ … vₖ | b] is consistent.',
            'Vectors are linearly independent when the only way to make c₁v₁ + … + cₖvₖ = 0 is with every cᵢ = 0. Put the vectors as columns of a matrix A: they are independent exactly when Ax = 0 has only the trivial solution, that is when every column has a pivot.',
            'Shortcuts: two vectors are dependent exactly when one is a multiple of the other; a set containing the zero vector is dependent; more than n vectors in Rⁿ must be dependent; n vectors in Rⁿ are independent exactly when the determinant of the matrix they form is non-zero.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Span{v₁, …, vₖ} = {c₁v₁ + … + cₖvₖ}', 'Independent ⇔ c₁v₁ + … + cₖvₖ = 0 only for all cᵢ = 0', 'Independent ⇔ every column of [v₁ … vₖ] has a pivot', 'n vectors in Rⁿ: independent ⇔ det ≠ 0'],
        'steps': ['Write the vectors as the columns of a matrix.', 'Row-reduce.', 'Count pivots: a pivot in every column means independent.', 'For span questions, add b as an extra column and check consistency.', 'For n vectors in Rⁿ, a determinant is often quickest.'],
        'worked_example': {
            'problem': 'Are (1, 2, 3), (4, 5, 6) and (7, 8, 9) independent?',
            'steps': ['Form A with these columns.', 'det A = 1(45 − 48) − 4(18 − 24) + 7(12 − 15) = −3 + 24 − 21 = 0.', 'So A has a free column.'],
            'answer': 'They are dependent. In fact (7, 8, 9) = 2(4, 5, 6) − (1, 2, 3).',
            'check': '2(4, 5, 6) − (1, 2, 3) = (8 − 1, 10 − 2, 12 − 3) = (7, 8, 9) ✓.'},
        'mistakes': ['Concluding independence because no vector is an obvious multiple of another (three vectors can be dependent without that).', 'Forgetting that any set containing 0 is dependent.', 'Confusing "spans R³" with "independent". Four vectors can span R³ but cannot be independent.', 'Row-reducing rows instead of columns when the question is about the vectors as columns.'],
        'real_world': 'In a set of survey questions, a question that is a combination of others adds no new information. Independence tests are how analysts trim redundant measurements.',
        'exam_strategy': 'For "show these vectors are independent", reduce the matrix and point at a pivot in every column. One clear sentence of reasoning beats pages of algebra.',
        'recap': ['Span = all linear combinations.', 'Independent = no redundant vector.', 'Pivot in every column ⇔ independent.', 'n vectors in Rⁿ: check the determinant.']},
    T3: {
        'overview': 'A subspace is a set of vectors that is closed under addition and scaling, such as a line or plane through the origin. A basis is a minimal spanning set, and its size is the dimension.',
        'key_terms': ['Subspace', 'Closed under addition', 'Closed under scalar multiplication', 'Basis', 'Dimension', 'Standard basis'],
        'explanation': [
            'A subset H of Rⁿ is a subspace if it contains the zero vector, and sums and scalar multiples of vectors in H stay in H. Lines and planes through the origin qualify; a line that misses the origin does not.',
            'A basis of a subspace is a linearly independent set that spans it. The standard basis of R³ is (1, 0, 0), (0, 1, 0), (0, 0, 1). Every basis of the same space has the same number of vectors, the dimension: R³ has dimension 3, a plane through the origin has dimension 2.',
            'In an n-dimensional space, any n independent vectors automatically form a basis, and so do any n vectors that span the space.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Subspace test: 0 ∈ H, u + v ∈ H, cu ∈ H', 'Basis = independent + spanning', 'dim Rⁿ = n', 'n independent vectors in an n-dimensional space form a basis'],
        'steps': ['Check the zero vector is in the set.', 'Check closure under addition with general vectors.', 'Check closure under scalar multiplication.', 'For a basis, check independence and spanning (or count, if the dimension is known).', 'State the dimension as the number of basis vectors.'],
        'worked_example': {
            'problem': 'Find a basis and the dimension of the plane x + y − z = 0 in R³.',
            'steps': ['Solve for x: x = −y + z, with y = s and z = t free.', '(x, y, z) = s(−1, 1, 0) + t(1, 0, 1).', 'These two vectors are not multiples of each other, so they are independent.'],
            'answer': 'Basis {(−1, 1, 0), (1, 0, 1)}; dimension 2.',
            'check': 'Both vectors satisfy the equation: −1 + 1 − 0 = 0 ✓ and 1 + 0 − 1 = 0 ✓.'},
        'mistakes': ['Calling a line or plane that misses the origin a subspace.', 'Giving a spanning set that is not independent as a basis.', 'Thinking a space has only one basis. It has infinitely many, all of the same size.', 'Confusing the dimension of a subspace with the n in Rⁿ.'],
        'real_world': 'Compressing images works by expressing each picture in a clever basis where most coefficients are tiny, so only a few numbers need storing. That is the idea behind JPEG.',
        'exam_strategy': 'To prove something is not a subspace, one counterexample is enough: show the zero vector is missing, or give two specific vectors whose sum leaves the set.',
        'recap': ['Subspace: contains 0, closed under + and scaling.', 'Basis = independent + spanning.', 'Dimension = size of any basis.', 'Lines and planes through 0 are subspaces.']},
    T4: {
        'overview': 'Every matrix has a null space (all solutions of Ax = 0) and a column space (all vectors Ax). Their dimensions add up to the number of columns, the rank–nullity theorem.',
        'key_terms': ['Null space Nul A', 'Nullity', 'Column space Col A', 'Rank', 'Rank–nullity theorem', 'Pivot columns'],
        'explanation': [
            'Nul A is the set of all x with Ax = 0. Its dimension, the nullity, is the number of free variables. A basis comes from writing the general solution in parametric vector form.',
            'Col A is the span of the columns of A, so it is the set of all b for which Ax = b is consistent. A basis is given by the pivot columns of the original A (not of the reduced matrix), and its dimension is the rank.',
            'Because every column is either a pivot column or a free column, rank A + nullity A = n, the number of columns. So a 3 × 5 matrix of rank 3 has nullity 2.'],
        'formulas_label': 'Formulas & definitions',
        'formulas': ['Nul A = {x : Ax = 0}', 'Col A = span of the columns of A', 'rank A = dim Col A = number of pivots', 'nullity A = dim Nul A = number of free variables', 'rank A + nullity A = n (columns)'],
        'steps': ['Row-reduce A.', 'Pivot columns of the ORIGINAL A form a basis for Col A.', 'Write the solution of Ax = 0 in parametric form for a basis of Nul A.', 'Count pivots (rank) and free variables (nullity).', 'Check rank + nullity = number of columns.'],
        'worked_example': {
            'problem': 'For A = [1 2 3 ; 2 4 6], find rank, nullity and a basis for Nul A.',
            'steps': ['R₂ → R₂ − 2R₁ gives [1 2 3 ; 0 0 0]: one pivot, so rank 1.', 'x₁ = −2x₂ − 3x₃ with x₂ = s, x₃ = t free.', 'x = s(−2, 1, 0) + t(−3, 0, 1).'],
            'answer': 'rank 1, nullity 2, Nul A has basis {(−2, 1, 0), (−3, 0, 1)}.',
            'check': 'rank + nullity = 1 + 2 = 3 = number of columns ✓.'},
        'mistakes': ['Taking pivot columns of the reduced matrix as the basis for Col A.', 'Using the number of rows instead of columns in rank–nullity.', 'Forgetting that Nul A lives in Rⁿ (columns) while Col A lives in Rᵐ (rows).', 'Giving the zero vector as a basis for a non-trivial null space.'],
        'real_world': 'In network flow, for water pipes or road traffic, the null space of the network matrix describes all the ways flow can circulate without changing what enters or leaves.',
        'exam_strategy': 'Rank–nullity is a quick check on any null-space calculation. If your basis has the wrong number of vectors, you will spot it before the examiner does.',
        'recap': ['Nul A: solutions of Ax = 0.', 'Col A: span of the columns.', 'Basis of Col A: pivot columns of the original matrix.', 'rank + nullity = number of columns.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Compute (1, 2, 2) · (3, 0, 4).', ['11', '8', '7', '(3, 0, 8)'], 0, '1·3 + 2·0 + 2·4 = 11.', ans=u.dot(v)),
    Q(T1, 'What is the length of (1, 2, 2)?', ['3', '5', '9', '√5'], 0, '√(1 + 4 + 4) = √9 = 3.', ans=u.norm()),
    Q(T1, 'For which k are (2, k) and (3, −6) orthogonal?', ['1', '−1', '4', '0'], 0, '6 − 6k = 0, so k = 1.', ans=sp.solve(M([2, sp.Symbol('k')]).dot(M([3, -6])), sp.Symbol('k'))[0]),
    Q(T1, 'What is cos θ for u = (1, 2, 2) and v = (3, 0, 4)?', ['11/15', '11/9', '3/5', '15/11'], 0, '11/(3 × 5).', ans=u.dot(v) / (u.norm() * v.norm())),
    Q(T1, 'Which is the unit vector in the direction of (3, 4)?', ['(3/5, 4/5)', '(3/7, 4/7)', '(1, 1)', '(3/25, 4/25)'], 0, 'Divide by the length 5.', ans=M([3, 4]) / 5),
    Q(T1, 'What is the distance between (1, 1) and (4, 5)?', ['5', '7', '25', '√7'], 0, 'The difference is (3, 4), with length 5.', ans=(M([4, 5]) - M([1, 1])).norm()),
    # T2
    Q(T2, 'Are (1, 2, 3), (4, 5, 6) and (7, 8, 9) linearly independent?', ['No, they are dependent', 'Yes', 'Only if scaled', 'It cannot be decided'], 0, 'The determinant of the matrix they form is 0; in fact (7, 8, 9) = 2(4, 5, 6) − (1, 2, 3).'),
    Q(T2, 'Any set of 4 vectors in R³ is:', ['linearly dependent', 'linearly independent', 'a basis of R³', 'orthogonal'], 0, 'A 3 × 4 matrix has at most 3 pivots, so one column must be free.'),
    Q(T2, 'Is (5, 7) in the span of (1, 1) and (1, 2)? If so, which combination gives it?', ['3(1, 1) + 2(1, 2)', '2(1, 1) + 3(1, 2)', '5(1, 1) + 1(1, 2)', 'It is not in the span'], 0, 'Solve a + b = 5, a + 2b = 7: b = 2, a = 3.'),
    Q(T2, 'For which k are (1, 2) and (3, k) linearly dependent?', ['6', '3', '−6', '2'], 0, 'det [1 3 ; 2 k] = k − 6 = 0 when k = 6.', ans=6),
    Q(T2, 'A set containing the zero vector is always:', ['linearly dependent', 'linearly independent', 'a basis', 'orthogonal'], 0, '1·0 = 0 is a non-trivial combination giving 0.'),
    Q(T2, 'What is the span of (1, 0, 0) and (0, 1, 0) in R³?', ['The xy-plane (z = 0)', 'All of R³', 'The x-axis', 'A single point'], 0, 'Combinations a(1, 0, 0) + b(0, 1, 0) = (a, b, 0).'),
    # T3
    Q(T3, 'Which set is a subspace of R²?', ['The line y = 2x', 'The line y = 2x + 1', 'The first quadrant', 'The circle x² + y² = 1'], 0, 'y = 2x passes through 0 and is closed under addition and scaling.'),
    Q(T3, 'What is the dimension of the plane x + y − z = 0 in R³?', ['2', '1', '3', '0'], 0, 'One equation in three unknowns leaves two free variables.', ans=3 - M([[1, 1, -1]]).rank()),
    Q(T3, 'How many vectors are in every basis of R⁴?', ['4', '3', '5', 'It depends on the basis'], 0, 'Every basis of Rⁿ has exactly n vectors.', ans=4),
    Q(T3, 'Which pair is a basis of R²?', ['(1, 2) and (2, 1)', '(1, 2) and (2, 4)', '(0, 0) and (1, 1)', '(3, 3) and (−1, −1)'], 0, 'det [1 2 ; 2 1] = −3 ≠ 0, so they are independent, and two independent vectors in R² form a basis.'),
    Q(T3, 'A basis for the plane x + y − z = 0 is:', ['{(−1, 1, 0), (1, 0, 1)}', '{(1, 1, 1)}', '{(1, 1, −1), (2, 2, −2)}', '{(1, 0, 0), (0, 1, 0), (0, 0, 1)}'], 0, 'Both vectors lie in the plane and are independent; the dimension is 2.'),
    Q(T3, 'The zero vector must belong to:', ['every subspace', 'no subspace', 'only R³', 'only lines'], 0, 'Closure under scaling by 0 forces 0 into the set.'),
    # T4
    Q(T4, 'What is the nullity of A = [1 2 3 ; 2 4 6]?', ['2', '1', '3', '0'], 0, 'rank 1, so nullity = 3 − 1 = 2.', ans=len(M([[1, 2, 3], [2, 4, 6]]).nullspace())),
    Q(T4, 'A 4 × 6 matrix has rank 4. What is its nullity?', ['2', '4', '6', '0'], 0, 'rank + nullity = 6 columns, so nullity = 2.', ans=2),
    Q(T4, 'Which vector is in the null space of [1 2 3 ; 2 4 6]?', ['(−2, 1, 0)', '(1, 2, 3)', '(2, 1, 0)', '(1, 1, 1)'], 0, '1(−2) + 2(1) + 3(0) = 0, and the second row is twice the first.', ans=M([-2, 1, 0])),
    Q(T4, 'A basis for Col A is given by:', ['the pivot columns of the original A', 'the pivot columns of the reduced matrix', 'the non-zero rows of the reduced matrix', 'all the columns of A'], 0, 'Row operations change the column space, so use the original columns in the pivot positions.'),
    Q(T4, 'What is the rank of [1 0 2 ; 0 1 3 ; 1 1 5]?', ['2', '3', '1', '0'], 0, 'Row 3 = row 1 + row 2, so there are two pivots.', ans=M([[1, 0, 2], [0, 1, 3], [1, 1, 5]]).rank()),
    Q(T4, 'If Ax = 0 has only the trivial solution for a 5 × 3 matrix A, the rank of A is:', ['3', '5', '0', '2'], 0, 'Nullity 0, so rank = 3 − 0 = 3.', ans=3),
]

FLASH = [
    ['Dot product', 'u · v = Σ uᵢvᵢ, a number.'], ['Length', '‖v‖ = √(v · v)'], ['Angle', 'cos θ = u·v/(‖u‖‖v‖)'],
    ['Orthogonal', 'u · v = 0'], ['Linearly independent', 'Only the trivial combination gives 0; pivot in every column.'],
    ['Subspace test', 'Contains 0; closed under addition and scalar multiplication.'], ['Basis', 'An independent spanning set.'],
    ['Dimension', 'The number of vectors in any basis.'], ['Rank–nullity', 'rank A + nullity A = number of columns.'],
    ['Basis for Col A', 'Pivot columns of the original matrix.'],
]
