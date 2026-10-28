"""Machine Learning Foundations, module 5: Neural networks and responsible practice."""
import numpy as np
from verify import Q
T1, T2, T3, T4 = ('Neurons, layers and activation functions', 'Training neural networks: loss, softmax and backpropagation', 'Model selection: cross-validation and hyperparameters', 'Fairness, explainability and deployment')
r = lambda v, d: round(float(v), d)
assert r(0.5 * 2 - 1 * 1 + 0.2, 6) == 0.2 and max(0, -2) == 0 and max(0, 3) == 3
params = lambda sizes: sum(a * b + b for a, b in zip(sizes, sizes[1:]))
assert params([4, 8, 3]) == 67 and params([784, 128, 10]) == 101770
w, x, y = 3, 2, 10; g = 2 * (w * x - y) * x
assert w * x == 6 and g == -16 and r(w - 0.01 * g, 6) == 3.16
Lf = lambda w: (w * x - y) ** 2; assert r((Lf(3 + 1e-6) - Lf(3 - 1e-6)) / 2e-6, 4) == -16
lg = np.array([2, 1, 0.]); p = np.exp(lg) / np.exp(lg).sum()
assert [r(v, 3) for v in p] == [0.665, 0.245, 0.090] and r(-np.log(p[0]), 3) == 0.408
assert 3 * 4 * 5 == 60 and 3 * 4 == 12 and r(0.30 / 0.60, 6) == 0.5 and 0.5 < 0.8

MODULE = {
    'title': 'Neural networks and responsible practice',
    'topics': [T1, T2, T3, T4],
    'overview': 'The final module introduces neural networks, the models behind modern image, speech and language systems: how artificial neurons and layers compute, how networks are trained with softmax, cross-entropy and backpropagation, how models and settings are chosen fairly, and how to deploy models that are fair, explainable and monitored.',
    'key_terms': ['Neuron', 'Weight', 'Activation function', 'ReLU', 'Hidden layer', 'Parameters', 'Softmax', 'Cross-entropy', 'Backpropagation', 'Chain rule', 'Hyperparameter', 'Grid search', 'Dropout', 'Fairness metric', 'Data drift'],
    'explanation': [
        'An artificial neuron computes a weighted sum of its inputs plus a bias and passes it through an activation function such as ReLU or the sigmoid. Stacking layers of neurons lets a network learn complex, non-linear functions; the number of parameters grows quickly with layer sizes.',
        'Networks are trained by gradient descent. For classification, a softmax output layer turns scores into probabilities and cross-entropy measures the loss; backpropagation uses the chain rule to compute every weight\'s gradient efficiently, layer by layer from the output back.',
        'Hyperparameters (learning rate, layer sizes, regularisation) are chosen by cross-validation, never on the test set. Before deployment, models must be checked for unfair effects on groups, explained to the people affected, documented, and monitored, because real-world data drift over time.'],
    'quick_facts': [
        'Neuron: a = f(w·x + b); ReLU(z) = max(0, z).',
        'Dense layer parameters = inputs × outputs + outputs.',
        'Softmax: pᵢ = e^(zᵢ)/Σe^(zⱼ); cross-entropy = −ln p(true class).',
        'Backpropagation = chain rule applied layer by layer.',
        'Four-fifths rule: selection-rate ratio below 0.8 signals possible adverse impact.'],
}

NOTES = {
    T1: {
        'overview': 'Neural networks are built from simple units. Understanding one neuron and one layer makes the whole architecture clear.',
        'key_terms': ['Artificial neuron', 'Weights and bias', 'Activation function', 'Step function', 'Sigmoid', 'tanh', 'ReLU', 'Dense (fully connected) layer', 'Hidden layer', 'Parameters'],
        'explanation': [
            'A neuron with weights (0.5, −1), bias 0.2 and inputs (2, 1) computes z = 0.5 × 2 − 1 × 1 + 0.2 = 0.2. A perceptron applies a step function (output 1 if z > 0), so it outputs 1. Modern networks use smooth activations: sigmoid (0 to 1), tanh (−1 to 1) or ReLU, max(0, z), which gives 0 for z = −2 and 3 for z = 3.',
            'Without non-linear activations, stacked layers collapse into a single linear model. With them, a network with even one hidden layer can approximate very complicated functions (the universal approximation theorem), and deeper networks learn hierarchies of features, from edges to shapes to objects.',
            'A dense layer from a inputs to b outputs has a × b weights plus b biases. A 4-8-3 network has 4 × 8 + 8 + 8 × 3 + 3 = 67 parameters; a 784-128-10 digit classifier has 101 770. Large language models have billions, which is why they need vast data and computing power.'],
        'formulas_label': 'Formulas',
        'formulas': ['z = w·x + b; a = f(z)', 'ReLU(z) = max(0, z)', 'σ(z) = 1/(1 + e^(−z))', 'Dense layer parameters = a × b + b'],
        'steps': ['Compute the weighted sum plus bias.', 'Apply the activation.', 'Pass outputs to the next layer.', 'Count parameters layer by layer.'],
        'worked_example': {
            'problem': 'How many parameters does a fully connected 784-128-10 network have?',
            'steps': ['Layer 1: 784 × 128 + 128 = 100 480.', 'Layer 2: 128 × 10 + 10 = 1290.', 'Total = 100 480 + 1290 = 101 770.'],
            'answer': '101 770 parameters.',
            'check': 'Most parameters sit in the first layer because it has the most inputs ✓.'},
        'mistakes': ['Forgetting bias parameters.', 'Using only linear activations in hidden layers.', 'Thinking deeper is always better.', 'Confusing neurons with parameters.'],
        'real_world': 'Speech recognition on phones runs compact neural networks with a few million parameters on the device itself.',
        'exam_strategy': 'For parameter counts, write each layer as inputs × outputs + outputs and add.',
        'recap': ['Weighted sum + activation.', 'Non-linearity is essential.', 'Layers build features.', 'Count parameters.']},
    T2: {
        'overview': 'Networks learn by gradient descent on a loss. Softmax and cross-entropy handle classification, and backpropagation supplies the gradients.',
        'key_terms': ['Logits', 'Softmax', 'Cross-entropy', 'Forward pass', 'Backward pass', 'Chain rule', 'Gradient check', 'Vanishing gradients', 'Optimisers (momentum, Adam)'],
        'explanation': [
            'Softmax turns raw scores (logits) into probabilities: logits 2, 1, 0 give e² : e¹ : e⁰, normalised to about 0.665, 0.245 and 0.090. If the true class is the first, the cross-entropy loss is −ln 0.665 ≈ 0.408; perfect confidence in the right class gives loss 0.',
            'Backpropagation applies the chain rule. For a single linear neuron ŷ = wx with loss L = (ŷ − y)², dL/dw = 2(ŷ − y)x. With x = 2, y = 10 and w = 3: ŷ = 6, gradient = 2 × (−4) × 2 = −16, and a step with η = 0.01 moves w to 3.16. A numerical check, (L(w + h) − L(w − h))/2h, also gives −16, confirming the gradient.',
            'In deep networks, gradients are passed backwards through each layer, multiplying local derivatives. Sigmoid and tanh can make them vanish in deep stacks; ReLU activations, careful initialisation, normalisation layers and optimisers such as Adam make training deep networks practical.'],
        'formulas_label': 'Formulas',
        'formulas': ['Softmax: pᵢ = e^(zᵢ)/Σⱼe^(zⱼ)', 'Cross-entropy = −ln p(true class)', 'Chain rule: dL/dw = dL/dŷ × dŷ/dw', 'Numerical check: (L(w + h) − L(w − h))/(2h)'],
        'steps': ['Forward pass: compute predictions and loss.', 'Backward pass: compute gradients with the chain rule.', 'Update weights with an optimiser.', 'Repeat over mini-batches and epochs, monitoring validation loss.'],
        'worked_example': {
            'problem': 'A neuron ŷ = wx has w = 3. For x = 2, y = 10 and loss (ŷ − y)², find the gradient and the updated w with η = 0.01.',
            'steps': ['Forward: ŷ = 6; loss = 16.', 'dL/dw = 2(ŷ − y)x = 2 × (−4) × 2 = −16.', 'w ← 3 − 0.01 × (−16) = 3.16.'],
            'answer': 'Gradient −16; new w = 3.16.',
            'check': 'New prediction 6.32 is closer to 10, and the numerical gradient also gives −16 ✓.'},
        'mistakes': ['Applying softmax and then a sigmoid as well.', 'Forgetting the minus sign in cross-entropy.', 'Sign errors in the update step.', 'Ignoring validation loss while training.'],
        'real_world': 'Image classifiers that sort X-rays or identify plant diseases are trained exactly this way on labelled images.',
        'exam_strategy': 'Write the chain of derivatives explicitly, one factor per step, before multiplying.',
        'recap': ['Softmax probabilities.', 'Cross-entropy loss.', 'Chain-rule gradients.', 'Gradient checks.']},
    T3: {
        'overview': 'Choosing models and settings fairly is what separates real performance from wishful thinking.',
        'key_terms': ['Hyperparameter', 'Grid search', 'Random search', 'k-fold cross-validation', 'Nested cross-validation', 'Early stopping', 'Dropout', 'Baseline model'],
        'explanation': [
            'Parameters (weights) are learned; hyperparameters (learning rate, number of layers, regularisation strength, tree depth, k) are chosen by the analyst. Grid search tries every combination: 3 values of λ and 4 tree depths make 12 combinations, and with 5-fold cross-validation that is 60 model fits.',
            'Random search samples combinations at random and often finds good settings faster when only a few hyperparameters matter. Whatever the method, the test set stays locked away until the end; nested cross-validation gives an honest estimate when tuning and evaluation must share limited data.',
            'For neural networks, early stopping halts training when validation loss starts rising, and dropout randomly switches off neurons during training to prevent co-adaptation; both fight overfitting. Always compare against a simple baseline (logistic regression, a small tree or predicting the majority class) so that complexity has to earn its place.'],
        'formulas_label': 'Rules',
        'formulas': ['Grid size = product of options per hyperparameter', 'Fits = grid size × number of folds', 'Tune on validation folds; test once', 'Beat a simple baseline'],
        'steps': ['Define a baseline.', 'Choose hyperparameters and ranges.', 'Search with cross-validation.', 'Refit the best setting and evaluate once on the test set.'],
        'worked_example': {
            'problem': 'You grid-search 3 learning rates, 2 batch sizes and 2 dropout rates with 5-fold cross-validation. How many training runs?',
            'steps': ['Combinations = 3 × 2 × 2 = 12.', 'Each combination is trained 5 times.', 'Runs = 12 × 5 = 60.'],
            'answer': '60 training runs (plus one final refit).',
            'check': 'Adding a fourth option for any hyperparameter would multiply the work again ✓.'},
        'mistakes': ['Tuning on the test set.', 'Reporting the best cross-validation score as the final estimate after heavy tuning.', 'Searching huge grids without a baseline.', 'Confusing parameters with hyperparameters.'],
        'real_world': 'Machine-learning competitions keep a hidden test set because teams that tune on public leaderboards often drop sharply on the final ranking.',
        'exam_strategy': 'Count grid searches by multiplying options, then by folds.',
        'recap': ['Parameters vs hyperparameters.', 'Grid and random search.', 'Locked test set.', 'Baselines.']},
    T4: {
        'overview': 'A model that works in the lab can still harm people or fail quietly in use. Responsible ML covers fairness, explanation, documentation and monitoring.',
        'key_terms': ['Algorithmic bias', 'Protected attribute', 'Selection rate', 'Disparate impact', 'Four-fifths rule', 'Explainability', 'Feature importance', 'Model card', 'Data drift', 'Human oversight'],
        'explanation': [
            'Models learn patterns in historical data, including past discrimination. A loan model that approves 60% of applicants from group A but 30% from group B has a selection-rate ratio of 0.30/0.60 = 0.5, below the 0.8 "four-fifths" guideline, a warning sign that needs investigation. Removing the protected attribute is not enough, because other features (such as location) can act as proxies.',
            'Explainability helps people trust and challenge decisions: simple models can be read directly, and tools such as permutation importance and SHAP values show which features drive a complex model\'s predictions. Data-protection laws such as South Africa\'s POPIA and the EU\'s GDPR give people rights around automated decisions that significantly affect them.',
            'After deployment, monitor inputs and accuracy: data drift (customers, prices or sensors change) silently degrades models. Document models with model cards (purpose, data, metrics by group, limitations), keep humans in the loop for high-stakes decisions, and plan how to retrain or roll back.'],
        'formulas_label': 'Checks',
        'formulas': ['Selection-rate ratio = rate(group B)/rate(group A)', 'Ratio < 0.8 → possible adverse impact', 'Report metrics by group', 'Monitor drift and retrain'],
        'steps': ['Identify affected groups and possible harms.', 'Measure performance and selection rates by group.', 'Explain and document the model.', 'Monitor after deployment with human oversight.'],
        'worked_example': {
            'problem': 'A hiring screen passes 60 of 100 applicants from group A and 30 of 100 from group B. Apply the four-fifths rule.',
            'steps': ['Selection rates: A 0.60, B 0.30.', 'Ratio = 0.30/0.60 = 0.5.', '0.5 < 0.8.'],
            'answer': 'The ratio of 0.5 indicates possible adverse impact; investigate features, data and thresholds before use.',
            'check': 'Equal rates would give a ratio of 1 ✓.'},
        'mistakes': ['Assuming dropping a protected attribute removes bias.', 'Reporting only overall accuracy.', 'Deploying without monitoring.', 'Treating explanations as optional for high-stakes decisions.'],
        'real_world': 'Studies of commercial face-recognition systems found much higher error rates for darker-skinned women, prompting companies to change their data and testing.',
        'exam_strategy': 'For any deployment question, mention fairness by group, explanation, documentation and monitoring.',
        'recap': ['Bias from data.', 'Four-fifths rule.', 'Explain and document.', 'Monitor drift.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A neuron with weights (0.5, −1), bias 0.2 and inputs (2, 1) has z =', ['0.2', '1.2', '−0.8', '2.2'], 0, '1 − 1 + 0.2.', ans=0.2, num=True),
    Q(T1, 'ReLU(−2) equals:', ['0', '−2', '2', '0.12'], 0, 'max(0, z).', ans=0, num=True),
    Q(T1, 'A 4-8-3 fully connected network has how many parameters?', ['67', '56', '15', '96'], 0, '40 + 27.', ans=67, num=True),
    Q(T1, 'A 784-128-10 network has how many parameters?', ['101 770', '100 352', '922', '101 632'], 0, '100 480 + 1290.'),
    Q(T1, 'Without non-linear activations, a deep network is equivalent to:', ['a single linear model', 'a decision tree', 'k-means', 'a random forest'], 0, 'Linear maps compose.'),
    Q(T1, 'The output range of tanh is:', ['−1 to 1', '0 to 1', '0 to ∞', '−∞ to ∞'], 0, 'Centred at 0.'),
    # T2
    Q(T2, 'Softmax of logits 2, 1, 0 gives the first class a probability of about:', ['0.665', '0.5', '0.333', '0.9'], 0, 'e²/(e² + e + 1).', ans=0.665, num=True),
    Q(T2, 'If the first class is correct, the cross-entropy loss is about:', ['0.408', '0.665', '1.0', '0.09'], 0, '−ln 0.665.', ans=0.408, num=True),
    Q(T2, 'ŷ = wx, w = 3, x = 2, y = 10, loss (ŷ − y)². The gradient dL/dw is:', ['−16', '16', '−8', '−4'], 0, '2(6 − 10) × 2.', ans=-16, num=True),
    Q(T2, 'After one step with η = 0.01, w becomes:', ['3.16', '2.84', '3.016', '19'], 0, '3 + 0.16.', ans=3.16, num=True),
    Q(T2, 'Backpropagation computes gradients using:', ['the chain rule', 'random search', 'the normal equation', 'k-means'], 0, 'Layer by layer.'),
    Q(T2, 'Vanishing gradients are reduced by using:', ['ReLU activations and careful initialisation', 'more sigmoid layers', 'larger batches only', 'no bias terms'], 0, 'Keeps gradients alive.'),
    # T3
    Q(T3, 'Which is a hyperparameter?', ['the learning rate', 'a weight', 'a bias value', 'a gradient'], 0, 'Set by the analyst.'),
    Q(T3, 'Grid search over 3 values of λ and 4 depths has how many combinations?', ['12', '7', '64', '81'], 0, '3 × 4.', ans=12, num=True),
    Q(T3, 'With 5-fold cross-validation that grid needs how many fits?', ['60', '12', '17', '20'], 0, '12 × 5.', ans=60, num=True),
    Q(T3, 'Early stopping halts training when:', ['validation loss starts to rise', 'training loss reaches zero', 'the learning rate is zero', 'the test score is best'], 0, 'Sign of overfitting.'),
    Q(T3, 'Dropout helps by:', ['randomly disabling neurons during training to reduce overfitting', 'deleting training data', 'increasing the learning rate', 'removing the output layer'], 0, 'Regularisation.'),
    Q(T3, 'The test set should be used:', ['once, after all tuning is complete', 'to choose hyperparameters', 'during every epoch', 'never'], 0, 'Honest final estimate.'),
    # T4
    Q(T4, 'Group A approval 60%, group B 30%. The selection-rate ratio is:', ['0.5', '2', '0.3', '0.8'], 0, '0.30/0.60.', ans=0.5, num=True),
    Q(T4, 'Under the four-fifths rule, that ratio suggests:', ['possible adverse impact', 'perfect fairness', 'overfitting', 'data leakage'], 0, '0.5 < 0.8.'),
    Q(T4, 'Removing the protected attribute from the features:', ['may not remove bias because of proxy variables', 'always removes bias', 'is illegal', 'improves accuracy always'], 0, 'Proxies such as location.'),
    Q(T4, 'A gradual change in the data a deployed model receives is called:', ['data drift', 'dropout', 'regularisation', 'backpropagation'], 0, 'Monitor it.'),
    Q(T4, 'A model card documents:', ['purpose, data, performance by group and limitations', 'only the code', 'only the accuracy', 'the hardware used'], 0, 'Transparency.'),
    Q(T4, 'SHAP values and permutation importance are tools for:', ['explaining which features drive predictions', 'training faster', 'clustering', 'encrypting data'], 0, 'Explainability.'),
]

FLASH = [
    ['Artificial neuron', 'a = f(w·x + b).'],
    ['ReLU', 'max(0, z); the default hidden-layer activation.'],
    ['Dense layer parameters', 'inputs × outputs + outputs.'],
    ['Softmax and cross-entropy', 'Scores → probabilities; loss = −ln p(true class).'],
    ['Backpropagation', 'Chain rule from the output back through the layers.'],
    ['Hyperparameter search', 'Grid or random search with cross-validation; test once.'],
    ['Four-fifths rule', 'Selection-rate ratio below 0.8 flags possible adverse impact.'],
    ['Responsible deployment', 'Explain, document (model cards), monitor drift, keep humans in the loop.'],
]
