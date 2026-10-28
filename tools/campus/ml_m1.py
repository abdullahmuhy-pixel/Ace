"""Machine Learning Foundations, module 1: What machine learning is and how models are judged."""
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from verify import Q
T1, T2, T3, T4 = ('Types of machine learning', 'Training, validation and test data', 'Overfitting and the bias–variance trade-off', 'Measuring error in regression')
r = lambda v, d: round(float(v), d)
assert (0.7 * 10000, 0.15 * 10000) == (7000, 1500) and 1000 / 5 == 200 and 1000 - 200 == 800
y, p = np.array([3, 5, 7, 9]), np.array([2.5, 5.5, 7, 10])
assert mean_absolute_error(y, p) == 0.5 and mean_squared_error(y, p) == 0.375 and r(np.sqrt(0.375), 3) == 0.612 and r(r2_score(y, p), 3) == 0.925
assert np.mean((y - y.mean()) ** 2) == 5 and r(1 - 0.375 / 5, 3) == 0.925
assert 2 ** 10 == 1024 and 28 * 28 == 784

MODULE = {
    'title': 'What machine learning is and how models are judged',
    'topics': [T1, T2, T3, T4],
    'overview': 'Machine learning builds models that improve their predictions from data rather than following hand-written rules. This module sets out the main kinds of learning, why data must be split into training, validation and test sets, how models overfit or underfit, and how regression predictions are scored.',
    'key_terms': ['Machine learning', 'Feature', 'Label', 'Supervised learning', 'Unsupervised learning', 'Reinforcement learning', 'Training set', 'Validation set', 'Test set', 'Data leakage', 'Overfitting', 'Underfitting', 'Bias', 'Variance', 'Mean squared error'],
    'explanation': [
        'In supervised learning the data include the answer (a label) for each example, and the model learns to predict it from features: house prices from size and location (regression) or spam from email text (classification). Unsupervised learning finds structure without labels, such as customer segments. Reinforcement learning learns actions from rewards.',
        'A model is only useful if it works on new data. So data are split: the model learns from the training set, choices such as model complexity are tuned on a validation set (or by cross-validation), and the final score comes from a test set that was never used for any decision.',
        'A model that is too simple underfits (high bias); one that is too flexible memorises noise and overfits (high variance). Regression errors are measured by MAE, MSE, RMSE and R², each answering a slightly different question about the size of the mistakes.'],
    'quick_facts': [
        'Supervised: features → label; unsupervised: features only.',
        'Regression predicts numbers; classification predicts categories.',
        'Typical split: 70/15/15 or 80/20 with cross-validation.',
        'Low train error + high test error = overfitting.',
        'MSE = mean of squared errors; RMSE = √MSE; R² = 1 − MSE/Var(y).'],
}

NOTES = {
    T1: {
        'overview': 'Machine learning problems are grouped by what data are available and what the model must output.',
        'key_terms': ['Feature', 'Label (target)', 'Example (instance)', 'Supervised learning', 'Regression', 'Classification', 'Unsupervised learning', 'Clustering', 'Reinforcement learning', 'Model'],
        'explanation': [
            'Each example is described by features (inputs) and, in supervised learning, a label (the answer). A 28 × 28 pixel greyscale image of a handwritten digit has 784 features and a label from 0 to 9. The model is a function, learned from data, that maps features to a prediction.',
            'Supervised tasks: regression when the label is a number (predicting crop yield in tonnes per hectare), classification when it is a category (diagnosing whether a leaf has disease). Unsupervised tasks have no labels: clustering groups similar customers, and dimensionality reduction compresses many features into a few.',
            'Reinforcement learning trains an agent to choose actions that maximise reward over time, as in game playing or robot control. Many real systems mix approaches; for example, large language models are pre-trained on unlabelled text and then fine-tuned with labelled examples and feedback.'],
        'formulas_label': 'Summary',
        'formulas': ['Supervised: learn f(features) ≈ label', 'Regression: numeric label', 'Classification: categorical label', 'Unsupervised: structure without labels', 'Reinforcement: actions and rewards'],
        'steps': ['Ask what the output should be.', 'Check whether labels exist.', 'Classify the task (regression, classification, clustering …).', 'List the features available at prediction time.'],
        'worked_example': {
            'problem': 'A bank wants to predict whether a loan applicant will default, using past applicants whose outcomes are known. What type of ML task is this?',
            'steps': ['Past outcomes (default or not) are known: labels exist, so it is supervised.', 'The label is a category (default/no default).', 'So it is a binary classification problem.'],
            'answer': 'Supervised binary classification.',
            'check': 'If the bank instead wanted to group applicants into segments without outcomes, it would be unsupervised clustering ✓.'},
        'mistakes': ['Calling any prediction of categories "regression".', 'Using features that will not be available when predicting.', 'Thinking unsupervised learning needs labels.', 'Confusing the model with the algorithm that trains it.'],
        'real_world': 'Agricultural apps in East Africa use image classifiers to diagnose cassava diseases from photos taken by farmers.',
        'exam_strategy': 'Two questions classify any task: "Are there labels?" and "Is the output a number or a category?"',
        'recap': ['Features and labels.', 'Regression vs classification.', 'Unsupervised structure.', 'Reinforcement rewards.']},
    T2: {
        'overview': 'Models must be judged on data they have not seen. Splitting data properly, and avoiding leakage, is the foundation of honest evaluation.',
        'key_terms': ['Training set', 'Validation set', 'Test set', 'Generalisation', 'k-fold cross-validation', 'Data leakage', 'Stratified split', 'Time-based split'],
        'explanation': [
            'With 10 000 labelled examples, a 70/15/15 split gives 7000 training, 1500 validation and 1500 test examples. The model learns its parameters on the training set; you compare model types and settings on the validation set; the test set is used once, at the end, to estimate real-world performance.',
            'k-fold cross-validation uses data more efficiently: with 1000 examples and 5 folds, each fold of 200 takes a turn as validation while the model trains on the other 800, and the 5 scores are averaged. Stratified splits keep class proportions equal in each part; time series should be split by time (train on the past, test on the future).',
            'Data leakage happens when information from the test data, or from the future, sneaks into training: scaling features using the whole dataset before splitting, including a "loan written off" column when predicting default, or having the same patient in both training and test sets. Leakage gives impressive scores that collapse in use.'],
        'formulas_label': 'Rules',
        'formulas': ['Train: fit parameters', 'Validation: choose models and settings', 'Test: final, one-time estimate', 'k-fold: each fold validates once; average the k scores'],
        'steps': ['Split before any exploration that informs modelling.', 'Fit preprocessing on the training data only.', 'Tune on validation or cross-validation.', 'Report the test score once.'],
        'worked_example': {
            'problem': 'You have 1000 examples and use 5-fold cross-validation. How many examples are used for training and validation in each fold?',
            'steps': ['Each fold holds 1000/5 = 200 examples.', 'In each round one fold validates.', 'The other 4 folds, 800 examples, train the model.'],
            'answer': '800 for training and 200 for validation in each of the 5 rounds.',
            'check': 'Every example is used for validation exactly once ✓.'},
        'mistakes': ['Tuning on the test set.', 'Scaling or imputing with statistics from the full dataset.', 'Randomly shuffling time-series data.', 'Letting duplicates of the same person appear in train and test.'],
        'real_world': 'Medical AI studies have reported near-perfect accuracy that vanished in hospitals because the same patients\' scans were in both training and test sets.',
        'exam_strategy': 'When shown a suspiciously high score, look for leakage first.',
        'recap': ['Train, validate, test.', 'Cross-validation.', 'Stratify or split by time.', 'Avoid leakage.']},
    T3: {
        'overview': 'Every model balances being too simple against being too flexible. Recognising underfitting and overfitting is a core skill.',
        'key_terms': ['Underfitting', 'Overfitting', 'Model complexity', 'Bias', 'Variance', 'Irreducible error', 'Learning curve', 'Regularisation', 'Early stopping'],
        'explanation': [
            'Underfitting: the model is too simple to capture the pattern, so both training and test errors are high (high bias). Overfitting: the model fits noise in the training data, so training error is low but test error is much higher (high variance). A model with 2% training error and 18% test error is overfitting.',
            'Expected test error = bias² + variance + irreducible noise. Increasing complexity (a higher-degree polynomial, a deeper tree) lowers bias but raises variance; the best model sits in between, found by validation. A degree-1 line might underfit curved data, degree 3 fit well, and degree 15 wiggle through every point.',
            'Remedies for overfitting: more data, simpler models, regularisation (penalising large coefficients), early stopping and ensembles. Remedies for underfitting: richer features or a more flexible model. Learning curves (error against training-set size) show which problem you have.'],
        'formulas_label': 'Diagnosis',
        'formulas': ['High train and high test error → underfitting (bias)', 'Low train, high test error → overfitting (variance)', 'Test error ≈ bias² + variance + noise'],
        'steps': ['Compare training and validation errors.', 'Diagnose bias or variance.', 'Apply the matching remedy.', 'Re-check on validation data.'],
        'worked_example': {
            'problem': 'A model has 2% training error and 18% validation error. Diagnose it and suggest two fixes.',
            'steps': ['Training error is low, so the model can fit the data.', 'The large gap to validation error shows poor generalisation.', 'This is overfitting (high variance).'],
            'answer': 'Overfitting; fixes include more training data, regularisation, a simpler model or early stopping.',
            'check': 'If both errors had been about 18%, the diagnosis would be underfitting ✓.'},
        'mistakes': ['Judging a model by training error.', 'Adding complexity to cure overfitting.', 'Thinking more data always fixes underfitting.', 'Forgetting irreducible noise sets a floor on error.'],
        'real_world': 'Credit-scoring models are deliberately kept fairly simple so they generalise and can be explained to regulators.',
        'exam_strategy': 'Draw the U-shaped validation-error curve against complexity; it explains most bias–variance questions.',
        'recap': ['Underfit = bias.', 'Overfit = variance.', 'Trade-off.', 'Matching remedies.']},
    T4: {
        'overview': 'Regression models are scored by how far predictions fall from the truth. Different metrics emphasise different kinds of mistake.',
        'key_terms': ['Error (residual)', 'Mean absolute error', 'Mean squared error', 'Root mean squared error', 'R²', 'Baseline model', 'Outlier sensitivity'],
        'explanation': [
            'True values 3, 5, 7, 9 and predictions 2.5, 5.5, 7, 10 give errors 0.5, −0.5, 0, −1. MAE = (0.5 + 0.5 + 0 + 1)/4 = 0.5. MSE = (0.25 + 0.25 + 0 + 1)/4 = 0.375. RMSE = √0.375 ≈ 0.612, in the same units as y.',
            'R² compares the model with always predicting the mean. Here the variance of y (mean 6) is 5, so R² = 1 − 0.375/5 = 0.925: the model removes 92.5% of the squared error of the mean baseline. R² can be negative on test data if the model is worse than the mean.',
            'Squaring makes MSE and RMSE punish large errors heavily, which matters when big misses are costly; MAE treats all errors in proportion and is more robust to outliers. Always compare with a simple baseline, such as predicting the mean or last value.'],
        'formulas_label': 'Formulas',
        'formulas': ['MAE = (1/n)Σ|y − ŷ|', 'MSE = (1/n)Σ(y − ŷ)²', 'RMSE = √MSE', 'R² = 1 − Σ(y − ŷ)²/Σ(y − ȳ)²'],
        'steps': ['List the errors.', 'Compute MAE, MSE and RMSE.', 'Compute R² against the mean baseline.', 'Choose the metric that matches the cost of errors.'],
        'worked_example': {
            'problem': 'True values 3, 5, 7, 9; predictions 2.5, 5.5, 7, 10. Find MSE and R².',
            'steps': ['Squared errors: 0.25, 0.25, 0, 1; MSE = 1.5/4 = 0.375.', 'ȳ = 6; Σ(y − ȳ)²/n = (9 + 1 + 1 + 9)/4 = 5.', 'R² = 1 − 0.375/5 = 0.925.'],
            'answer': 'MSE = 0.375 and R² = 0.925.',
            'check': 'scikit-learn\'s mean_squared_error and r2_score give the same values ✓.'},
        'mistakes': ['Comparing RMSE values across different units.', 'Reporting R² from training data only.', 'Ignoring the baseline.', 'Using MSE when outliers dominate and MAE better reflects cost.'],
        'real_world': 'Electricity grid operators score demand forecasts with RMSE because large misses can cause blackouts.',
        'exam_strategy': 'Lay out a table of y, ŷ, error, |error| and error²; every metric comes from its columns.',
        'recap': ['MAE.', 'MSE and RMSE.', 'R² vs mean.', 'Use a baseline.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Predicting house prices from size and location is:', ['supervised regression', 'supervised classification', 'clustering', 'reinforcement learning'], 0, 'Numeric label.'),
    Q(T1, 'Grouping customers into segments without any labels is:', ['unsupervised learning', 'supervised regression', 'classification', 'reinforcement learning'], 0, 'No labels.'),
    Q(T1, 'A 28 × 28 greyscale image has how many pixel features?', ['784', '56', '28', '1568'], 0, '28 × 28.', ans=784, num=True),
    Q(T1, 'Predicting whether a loan will default from past outcomes is:', ['binary classification', 'regression', 'clustering', 'dimensionality reduction'], 0, 'Two categories.'),
    Q(T1, 'An agent learning to play a game from rewards uses:', ['reinforcement learning', 'unsupervised learning', 'regression', 'PCA'], 0, 'Actions and rewards.'),
    Q(T1, 'In supervised learning, the label is:', ['the answer the model must predict', 'any input column', 'the model\'s name', 'the test score'], 0, 'Target.'),
    # T2
    Q(T2, 'A 70/15/15 split of 10 000 examples gives a test set of:', ['1500', '7000', '3000', '150'], 0, '15%.', ans=1500, num=True),
    Q(T2, 'With 1000 examples and 5-fold cross-validation, each model trains on:', ['800 examples', '200 examples', '1000 examples', '500 examples'], 0, '4 folds.'),
    Q(T2, 'Model settings should be tuned on:', ['the validation set (or by cross-validation)', 'the test set', 'all the data', 'the training error'], 0, 'Keep test untouched.'),
    Q(T2, 'Scaling features with the mean and SD of the whole dataset before splitting causes:', ['data leakage', 'underfitting', 'faster training only', 'no problem'], 0, 'Test information leaks.'),
    Q(T2, 'For forecasting next month\'s sales, the data should be split:', ['by time, training on the past', 'randomly', 'alphabetically', 'by the label'], 0, 'No future peeking.'),
    Q(T2, 'A stratified split keeps:', ['class proportions the same in each part', 'the largest values in training', 'time order', 'duplicates together'], 0, 'Balanced classes.'),
    # T3
    Q(T3, 'Training error 2%, validation error 18% indicates:', ['overfitting', 'underfitting', 'a perfect model', 'leakage always'], 0, 'Large gap.'),
    Q(T3, 'Training and validation errors both high indicates:', ['underfitting (high bias)', 'overfitting', 'good generalisation', 'too much data'], 0, 'Too simple.'),
    Q(T3, 'Increasing model complexity usually:', ['lowers bias and raises variance', 'raises bias and lowers variance', 'lowers both', 'changes neither'], 0, 'Trade-off.'),
    Q(T3, 'Which helps reduce overfitting?', ['regularisation', 'adding more polynomial terms', 'training longer without checks', 'removing validation'], 0, 'Penalise complexity.'),
    Q(T3, 'Expected test error decomposes into bias², variance and:', ['irreducible noise', 'learning rate', 'accuracy', 'the number of features'], 0, 'Error floor.'),
    Q(T3, 'A degree-15 polynomial through 16 noisy points will most likely:', ['overfit', 'underfit', 'generalise perfectly', 'have high bias'], 0, 'Passes every point.'),
    # T4
    Q(T4, 'True 3, 5, 7, 9; predicted 2.5, 5.5, 7, 10. The MAE is:', ['0.5', '0.375', '0.612', '2'], 0, '2/4.', ans=0.5, num=True),
    Q(T4, 'The MSE is:', ['0.375', '0.5', '1.5', '0.612'], 0, '1.5/4.', ans=0.375, num=True),
    Q(T4, 'The RMSE is about:', ['0.612', '0.375', '0.141', '0.5'], 0, '√0.375.', ans=0.612, num=True),
    Q(T4, 'R² for those predictions is:', ['0.925', '0.375', '0.075', '5'], 0, '1 − 0.375/5.', ans=0.925, num=True),
    Q(T4, 'A negative R² on test data means the model is:', ['worse than predicting the mean', 'perfect', 'overfitting on training data only', 'impossible'], 0, 'Below baseline.'),
    Q(T4, 'Which metric is most sensitive to a few very large errors?', ['RMSE', 'MAE', 'median absolute error', 'accuracy'], 0, 'Squaring.'),
]

FLASH = [
    ['Supervised vs unsupervised', 'With labels vs without labels.'],
    ['Regression vs classification', 'Numeric output vs category output.'],
    ['Train/validation/test', 'Fit, tune, final one-time estimate.'],
    ['k-fold cross-validation', 'Each fold validates once; average scores.'],
    ['Data leakage', 'Test or future information entering training.'],
    ['Overfitting', 'Low training error, high test error (high variance).'],
    ['Underfitting', 'High errors on both (high bias).'],
    ['Regression metrics', 'MAE, MSE, RMSE = √MSE, R² = 1 − SSE/SST.'],
]
