"""Machine Learning Foundations, module 2: Linear models and gradient descent."""
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from verify import Q
T1, T2, T3, T4 = ('Linear regression as a learning problem', 'Gradient descent', 'Regularisation: ridge and lasso', 'Feature scaling and engineering')
r = lambda v, d: round(float(v), d)
x, y = np.array([1, 2, 3, 4.]), np.array([2, 4, 5, 8.])
X = np.c_[np.ones(4), x]; b0, w0 = np.linalg.solve(X.T @ X, X.T @ y)
assert r(b0, 6) == 0 and r(w0, 6) == 1.9 and r(LinearRegression().fit(x[:, None], y).coef_[0], 6) == 1.9 and r(w0 * 5 + b0, 6) == 9.5
assert r(np.mean((y - (w0 * x + b0)) ** 2), 3) == 0.175
w, seq = 0.0, []
for _ in range(3):
    w -= 0.1 * 2 * (w - 3); seq.append(r(w, 3))
assert seq == [0.6, 1.08, 1.464]
w, big = 0.0, []
for _ in range(3):
    w -= 1.1 * 2 * (w - 3); big.append(r(w, 3))
assert big == [6.6, -1.32, 8.184]
gw, gb = -2 * np.mean(y * x), -2 * np.mean(y)
assert (r(gw, 6), r(gb, 6)) == (-28.5, -9.5) and (r(-0.05 * gw, 3), r(-0.05 * gb, 3)) == (1.425, 0.475)
assert 1000 / 100 == 10
assert r(0.1 * (3 ** 2 + 4 ** 2), 6) == 2.5 and r(0.1 * (3 + 4), 6) == 0.7 and r(Ridge(alpha=1).fit(x[:, None], y).coef_[0], 3) == 1.583
assert (70 - 50) / 10 == 2 and (70 - 20) / (120 - 20) == 0.5 and PolynomialFeatures(2).fit_transform([[1, 2]]).shape == (1, 6)

MODULE = {
    'title': 'Linear models and gradient descent',
    'topics': [T1, T2, T3, T4],
    'overview': 'Linear models are the workhorses of machine learning and the clearest place to see how learning works. This module treats linear regression as minimising a loss, introduces gradient descent, the algorithm that trains almost every modern model, adds regularisation to control overfitting, and shows why scaling and engineering features matter.',
    'key_terms': ['Parameters', 'Weights', 'Bias term', 'Loss function', 'Mean squared error', 'Normal equation', 'Gradient', 'Learning rate', 'Epoch', 'Mini-batch', 'Convergence', 'Ridge (L2)', 'Lasso (L1)', 'Standardisation', 'One-hot encoding'],
    'explanation': [
        'A linear model predicts ŷ = w·x + b. Learning means choosing the weights w and bias b that minimise a loss, usually the mean squared error on the training data. For linear regression this has an exact solution (the normal equation), but most models need an iterative method.',
        'Gradient descent repeatedly moves the parameters a small step against the gradient of the loss: w ← w − η ∂L/∂w. The learning rate η controls the step: too small and training is slow; too large and it overshoots and diverges. Stochastic and mini-batch versions use small chunks of data per step.',
        'Regularisation adds a penalty for large weights to the loss: ridge (L2) shrinks all weights, lasso (L1) can set some exactly to zero and so selects features. Because penalties and gradient steps depend on the scale of each feature, features are usually standardised, and categorical or non-linear information is encoded as new features.'],
    'quick_facts': [
        'Linear model: ŷ = w·x + b; loss = MSE.',
        'Gradient step: w ← w − η × gradient.',
        'Too large η diverges; too small is slow.',
        'Ridge adds λΣw²; lasso adds λΣ|w|.',
        'Standardise: z = (x − mean)/SD; one-hot for categories.'],
}

NOTES = {
    T1: {
        'overview': 'Linear regression in machine learning is framed as finding parameters that minimise a loss on training data.',
        'key_terms': ['Hypothesis function', 'Weight', 'Bias (intercept)', 'Loss function', 'Mean squared error', 'Normal equation', 'Vectorised form'],
        'explanation': [
            'The model ŷ = wx + b has two parameters. The MSE loss L(w, b) = (1/n)Σ(yᵢ − (wxᵢ + b))² measures how badly it fits. Training data x = 1, 2, 3, 4 with y = 2, 4, 5, 8 give the minimum at w = 1.9, b = 0, with training MSE 0.175. The prediction for x = 5 is 9.5.',
            'With many features, write ŷ = Xθ, where X has a column of 1s for the bias. Setting the gradient of the MSE to zero gives the normal equation θ = (XᵀX)⁻¹Xᵀy. It is exact but needs a matrix inverse, which is slow for very many features and fails if features are perfectly correlated.',
            'The same framing (model, loss, optimiser) describes nearly all of machine learning: logistic regression and neural networks just use different models and losses.'],
        'formulas_label': 'Formulas',
        'formulas': ['ŷ = wx + b (or Xθ)', 'MSE = (1/n)Σ(y − ŷ)²', 'Normal equation: θ = (XᵀX)⁻¹Xᵀy'],
        'steps': ['Write the model.', 'Choose the loss.', 'Minimise it (exactly or iteratively).', 'Evaluate on validation data.'],
        'worked_example': {
            'problem': 'Fit ŷ = wx + b to x = 1, 2, 3, 4 and y = 2, 4, 5, 8, and predict at x = 5.',
            'steps': ['x̄ = 2.5, ȳ = 4.75; Σ(x − x̄)(y − ȳ) = 9.5; Σ(x − x̄)² = 5.', 'w = 9.5/5 = 1.9; b = 4.75 − 1.9 × 2.5 = 0.', 'ŷ(5) = 9.5.'],
            'answer': 'ŷ = 1.9x; prediction 9.5.',
            'check': 'scikit-learn\'s LinearRegression gives the same slope, 1.9 ✓.'},
        'mistakes': ['Forgetting the column of 1s for the bias.', 'Evaluating only on training data.', 'Inverting XᵀX when features are collinear.', 'Confusing the ML "bias" term with statistical bias.'],
        'real_world': 'Ride-hailing apps estimate fares with linear models of distance and time as a starting point before more complex adjustments.',
        'exam_strategy': 'Write "model, loss, optimiser" for any ML method; it organises your answer.',
        'recap': ['Model + loss.', 'MSE.', 'Normal equation.', 'Same pattern everywhere.']},
    T2: {
        'overview': 'Gradient descent finds parameters by walking downhill on the loss surface, step by step.',
        'key_terms': ['Gradient', 'Learning rate', 'Iteration', 'Epoch', 'Batch, mini-batch and stochastic gradient descent', 'Convergence', 'Divergence', 'Local minimum'],
        'explanation': [
            'For L(w) = (w − 3)², the gradient is 2(w − 3). From w = 0 with learning rate 0.1: w becomes 0.6, then 1.08, then 1.464, approaching the minimum at 3. With learning rate 1.1 the steps overshoot: 6.6, −1.32, 8.184, diverging.',
            'For linear regression the gradients are ∂L/∂w = −(2/n)Σx(y − ŷ) and ∂L/∂b = −(2/n)Σ(y − ŷ). Starting from w = b = 0 on the data above, they are −28.5 and −9.5, so one step with η = 0.05 moves to w = 1.425, b = 0.475, already close to the best fit.',
            'Batch gradient descent uses all data per step; stochastic uses one example; mini-batch uses a few (e.g. 100). With 1000 examples and batches of 100, one epoch (a full pass) is 10 updates. Mini-batches are noisy but fast, and the noise can help escape poor regions of complex loss surfaces.'],
        'formulas_label': 'Formulas',
        'formulas': ['θ ← θ − η∇L(θ)', 'Linear regression: ∂L/∂w = −(2/n)Σx(y − ŷ)', '∂L/∂b = −(2/n)Σ(y − ŷ)', 'Updates per epoch = n/batch size'],
        'steps': ['Initialise the parameters.', 'Compute the gradient on a batch.', 'Update with the learning rate.', 'Repeat until the loss stops falling.'],
        'worked_example': {
            'problem': 'Minimise L(w) = (w − 3)² by gradient descent from w = 0 with η = 0.1. Give the first three values of w.',
            'steps': ['Gradient at 0: 2(0 − 3) = −6; w = 0 + 0.6 = 0.6.', 'Gradient: 2(0.6 − 3) = −4.8; w = 0.6 + 0.48 = 1.08.', 'Gradient: −3.84; w = 1.08 + 0.384 = 1.464.'],
            'answer': '0.6, 1.08, 1.464.',
            'check': 'The gap to 3 shrinks by a factor of 0.8 each step: 3, 2.4, 1.92, 1.536 ✓.'},
        'mistakes': ['Moving with the gradient instead of against it.', 'Using a learning rate so large that the loss grows.', 'Stopping after a fixed number of steps without checking the loss.', 'Confusing epochs with iterations.'],
        'real_world': 'Large language models are trained with variants of mini-batch gradient descent over trillions of words.',
        'exam_strategy': 'Show each update as old value − η × gradient; method marks follow the pattern.',
        'recap': ['Step against the gradient.', 'Learning-rate trade-off.', 'Batches and epochs.', 'Check convergence.']},
    T3: {
        'overview': 'Regularisation penalises complexity, trading a little training error for better generalisation.',
        'key_terms': ['Regularisation', 'Ridge (L2)', 'Lasso (L1)', 'Penalty strength λ', 'Shrinkage', 'Sparsity', 'Elastic net'],
        'explanation': [
            'Ridge loss = MSE + λΣw²; lasso loss = MSE + λΣ|w|. For weights 3 and −4 with λ = 0.1, the ridge penalty is 0.1 × (9 + 16) = 2.5 and the lasso penalty 0.1 × (3 + 4) = 0.7. The bias term is not usually penalised.',
            'Ridge shrinks all weights towards zero: on the four-point data, ridge with λ = 1 gives slope ≈ 1.583 instead of 1.9. Lasso can make weights exactly zero, removing features; elastic net mixes the two.',
            'λ is a hyperparameter chosen by validation: λ = 0 is ordinary regression (risk of overfitting); very large λ forces weights near zero (underfitting). Because the penalty depends on feature scale, standardise features before regularising.'],
        'formulas_label': 'Formulas',
        'formulas': ['Ridge: MSE + λΣw²', 'Lasso: MSE + λΣ|w|', 'λ = 0 → ordinary least squares', 'Large λ → weights → 0'],
        'steps': ['Standardise features.', 'Choose ridge, lasso or elastic net.', 'Tune λ by cross-validation.', 'Inspect which weights shrink or vanish.'],
        'worked_example': {
            'problem': 'A model has weights w₁ = 3 and w₂ = −4. Find the ridge and lasso penalties with λ = 0.1.',
            'steps': ['Ridge: λ(w₁² + w₂²) = 0.1 × 25.', '= 2.5.', 'Lasso: λ(|w₁| + |w₂|) = 0.1 × 7 = 0.7.'],
            'answer': 'Ridge penalty 2.5; lasso penalty 0.7.',
            'check': 'Ridge punishes the larger weight more (16 vs 9) ✓.'},
        'mistakes': ['Regularising unscaled features.', 'Penalising the bias term.', 'Choosing λ on the test set.', 'Expecting ridge to set weights exactly to zero.'],
        'real_world': 'Genomic studies with thousands of genes and few patients rely on lasso to pick out a handful of predictive genes.',
        'exam_strategy': 'Remember "L1 → sparsity, L2 → shrinkage".',
        'recap': ['Penalty on weights.', 'Ridge shrinks.', 'Lasso selects.', 'Tune λ.']},
    T4: {
        'overview': 'Models only see the numbers you give them. Scaling and engineering features often matter more than the choice of algorithm.',
        'key_terms': ['Standardisation', 'Min–max scaling', 'One-hot encoding', 'Ordinal encoding', 'Polynomial features', 'Interaction term', 'Log transform', 'Pipeline'],
        'explanation': [
            'Standardisation, z = (x − mean)/SD, puts features on a common scale: a value of 70 with mean 50 and SD 10 becomes 2. Min–max scaling maps to [0, 1]: 70 in a range of 20 to 120 becomes 0.5. Gradient descent, regularisation, k-NN and neural networks all work better with scaled features. Fit the scaler on training data only.',
            'Categorical features need encoding: one-hot encoding turns a province column with k categories into k indicator columns (or k − 1 for linear models with an intercept). Ordinal categories (small, medium, large) can be mapped to ordered numbers.',
            'Feature engineering adds information: polynomial features let linear models fit curves (degree 2 on two features gives 6 terms: 1, x₁, x₂, x₁², x₁x₂, x₂²); interactions capture effects that depend on each other; log transforms tame skewed values such as income; dates can be split into day of week and month. Pipelines bundle these steps so they are applied identically to training and new data.'],
        'formulas_label': 'Formulas',
        'formulas': ['z = (x − μ)/σ', 'Min–max: (x − min)/(max − min)', 'One-hot: k categories → k binary columns', 'Degree-2 terms for 2 features: 6'],
        'steps': ['Encode categories.', 'Transform skewed features.', 'Add useful interactions or polynomial terms.', 'Scale, fitting the scaler on training data inside a pipeline.'],
        'worked_example': {
            'problem': 'A feature has training mean 50 and SD 10; the training values range from 20 to 120. Standardise and min–max scale the value 70.',
            'steps': ['z = (70 − 50)/10 = 2.', 'Min–max: (70 − 20)/(120 − 20) = 50/100.', '= 0.5.'],
            'answer': 'z = 2; min–max value 0.5.',
            'check': 'The mean maps to z = 0 and the minimum to 0 under min–max ✓.'},
        'mistakes': ['Fitting scalers on the full dataset (leakage).', 'Encoding nominal categories as 1, 2, 3 for linear models.', 'Creating so many polynomial features that the model overfits.', 'Forgetting to apply the same transforms at prediction time.'],
        'real_world': 'In credit scoring, engineered features such as "months since last missed payment" often predict better than raw transaction data.',
        'exam_strategy': 'Mention "fit on training data, apply to test data" whenever you describe preprocessing.',
        'recap': ['Scale features.', 'One-hot categories.', 'Engineer useful terms.', 'Use pipelines.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'For x = 1, 2, 3, 4 and y = 2, 4, 5, 8, the least-squares slope is:', ['1.9', '2', '1.5', '0.5'], 0, '9.5/5.', ans=1.9, num=True),
    Q(T1, 'The model\'s prediction at x = 5 is:', ['9.5', '10', '8', '9'], 0, '1.9 × 5.', ans=9.5, num=True),
    Q(T1, 'Its training MSE is:', ['0.175', '0.7', '0.35', '0'], 0, 'Residuals 0.1, 0.2, −0.7, 0.4.', ans=0.175, num=True),
    Q(T1, 'The normal equation is:', ['θ = (XᵀX)⁻¹Xᵀy', 'θ = Xy', 'θ = y/X', 'θ = XᵀX'], 0, 'Set the gradient to zero.'),
    Q(T1, 'In the matrix form ŷ = Xθ, the bias is included by:', ['adding a column of 1s to X', 'adding 1 to y', 'removing a feature', 'scaling θ'], 0, 'Intercept column.'),
    Q(T1, 'Training a model means:', ['choosing parameters that minimise a loss on training data', 'testing it on new data', 'collecting labels', 'plotting the data'], 0, 'Optimisation.'),
    # T2
    Q(T2, 'Minimising (w − 3)² from w = 0 with η = 0.1, the first update gives w =', ['0.6', '6', '0.3', '3'], 0, '0 − 0.1 × (−6).', ans=0.6, num=True),
    Q(T2, 'The third value of w in that sequence is:', ['1.464', '1.08', '1.8', '2.4'], 0, '0.6, 1.08, 1.464.', ans=1.464, num=True),
    Q(T2, 'With η = 1.1 the values 6.6, −1.32, 8.184 show the algorithm is:', ['diverging', 'converging quickly', 'stuck', 'optimal'], 0, 'Step too large.'),
    Q(T2, 'Gradient descent updates parameters:', ['against the gradient', 'along the gradient', 'randomly', 'only at the end'], 0, 'Downhill.'),
    Q(T2, '1000 examples with mini-batches of 100 give how many updates per epoch?', ['10', '100', '1000', '1'], 0, '1000/100.', ans=10, num=True),
    Q(T2, 'From w = b = 0 on that data, ∂L/∂w is −28.5. One step with η = 0.05 gives w =', ['1.425', '−1.425', '28.5', '0.05'], 0, '0 − 0.05 × (−28.5).', ans=1.425, num=True),
    # T3
    Q(T3, 'Weights 3 and −4 with λ = 0.1 give a ridge penalty of:', ['2.5', '0.7', '0.25', '25'], 0, '0.1 × 25.', ans=2.5, num=True),
    Q(T3, 'The lasso penalty for the same weights is:', ['0.7', '2.5', '0.1', '−0.1'], 0, '0.1 × 7.', ans=0.7, num=True),
    Q(T3, 'Which regularisation can set weights exactly to zero?', ['lasso (L1)', 'ridge (L2)', 'neither', 'both always'], 0, 'Sparsity.'),
    Q(T3, 'Ridge with λ = 1 on the four-point data gives slope about 1.583 instead of 1.9. This shows:', ['shrinkage of weights', 'overfitting', 'a larger loss on all data', 'feature removal'], 0, 'L2 shrinks.'),
    Q(T3, 'λ = 0 in ridge regression gives:', ['ordinary least squares', 'all weights zero', 'lasso', 'an error'], 0, 'No penalty.'),
    Q(T3, 'The penalty strength λ should be chosen by:', ['validation or cross-validation', 'the test set', 'making the training error zero', 'guessing once'], 0, 'Hyperparameter.'),
    # T4
    Q(T4, 'With mean 50 and SD 10, the value 70 standardises to:', ['2', '0.5', '20', '7'], 0, '(70 − 50)/10.', ans=2, num=True),
    Q(T4, 'With range 20 to 120, min–max scaling maps 70 to:', ['0.5', '0.7', '2', '0.58'], 0, '50/100.', ans=0.5, num=True),
    Q(T4, 'One-hot encoding a feature with 9 provinces creates how many indicator columns?', ['9', '1', '8 always', '3'], 0, 'One per category (k − 1 if dropping one).', ans=9, num=True),
    Q(T4, 'Degree-2 polynomial features from 2 inputs (with the constant) give how many terms?', ['6', '4', '5', '3'], 0, '1, x₁, x₂, x₁², x₁x₂, x₂².', ans=6, num=True),
    Q(T4, 'A scaler should be fitted on:', ['the training data only', 'the test data', 'all data combined', 'the labels'], 0, 'Avoid leakage.'),
    Q(T4, 'A log transform is most useful for:', ['strongly right-skewed features such as income', 'binary features', 'already-scaled features', 'labels in classification'], 0, 'Compress large values.'),
]

FLASH = [
    ['Linear model', 'ŷ = w·x + b, trained by minimising MSE.'],
    ['Normal equation', 'θ = (XᵀX)⁻¹Xᵀy.'],
    ['Gradient descent', 'θ ← θ − η∇L.'],
    ['Learning rate', 'Too small: slow; too large: diverges.'],
    ['Epoch', 'One full pass through the training data.'],
    ['Ridge vs lasso', 'L2 shrinks all weights; L1 can zero some out.'],
    ['Standardisation', 'z = (x − mean)/SD, fitted on training data.'],
    ['One-hot encoding', 'k categories → k indicator columns.'],
]
