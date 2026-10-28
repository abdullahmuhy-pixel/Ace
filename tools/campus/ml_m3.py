"""Machine Learning Foundations, module 3: Classification."""
import math
from sklearn.metrics import roc_auc_score
from verify import Q
T1, T2, T3, T4 = ('Logistic regression', 'Confusion matrices and classification metrics', 'Thresholds, ROC curves and AUC', 'k-nearest neighbours and decision trees')
r = lambda v, d: round(float(v), d)
sig = lambda z: 1 / (1 + math.exp(-z))
assert r(sig(-3 + 0.8 * 5), 3) == 0.731 and sig(0) == 0.5 and r(math.exp(0.8), 2) == 2.23 and r(-math.log(0.9), 3) == 0.105 and r(-math.log(0.1), 3) == 2.303
assert -3 / 0.8 == -3.75 + 0 and 3 / 0.8 == 3.75
TP, FP, FN, TN = 80, 20, 40, 860; P, R = TP / (TP + FP), TP / (TP + FN)
assert (TP + TN) / 1000 == 0.94 and P == 0.8 and r(R, 3) == 0.667 and r(2 * P * R / (P + R), 3) == 0.727 and r(TN / (TN + FP), 3) == 0.977 and (FP + TN) / 1000 == 0.88
assert r(roc_auc_score([0, 0, 1, 1, 0, 1], [0.1, 0.4, 0.35, 0.8, 0.2, 0.7]), 3) == 0.889
g = 1 - (0.4 ** 2 + 0.6 ** 2); H = -(0.4 * math.log2(0.4) + 0.6 * math.log2(0.6))
gl, gr = 1 - (0.7 ** 2 + 0.3 ** 2), 1 - (0.1 ** 2 + 0.9 ** 2)
assert r(g, 6) == 0.48 and r(H, 3) == 0.971 and (r(gl, 6), r(gr, 6)) == (0.42, 0.18) and r(0.5 * gl + 0.5 * gr, 6) == 0.3 and r(g - 0.3, 6) == 0.18
assert math.dist((1, 2), (4, 6)) == 5 and abs(1 - 4) + abs(2 - 6) == 7

MODULE = {
    'title': 'Classification',
    'topics': [T1, T2, T3, T4],
    'overview': 'Classification models predict categories: spam or not, disease or healthy, which digit is in an image. This module covers logistic regression and its probability outputs, how to judge classifiers with confusion matrices, precision and recall, how decision thresholds and ROC curves trade one kind of error for another, and two intuitive non-linear methods: k-nearest neighbours and decision trees.',
    'key_terms': ['Sigmoid function', 'Log-odds', 'Log loss', 'Decision boundary', 'Confusion matrix', 'True positive', 'False positive', 'Precision', 'Recall', 'F1 score', 'Class imbalance', 'Threshold', 'ROC curve', 'AUC', 'Gini impurity'],
    'explanation': [
        'Logistic regression passes a linear score through the sigmoid, σ(z) = 1/(1 + e^(−z)), to give a probability between 0 and 1. It is trained by minimising log loss, which punishes confident wrong predictions heavily.',
        'A confusion matrix counts true and false positives and negatives. Accuracy can mislead when classes are imbalanced, so analysts also use precision (how many flagged cases are real), recall (how many real cases are flagged) and their harmonic mean, F1.',
        'Moving the decision threshold trades precision against recall; the ROC curve shows the trade-off across all thresholds and AUC summarises it. k-nearest neighbours classifies by majority vote of the closest training points, and decision trees split the data with yes/no questions chosen to make the groups purer.'],
    'quick_facts': [
        'σ(z) = 1/(1 + e^(−z)); σ(0) = 0.5.',
        'Log loss for a true positive = −ln p.',
        'Precision = TP/(TP + FP); recall = TP/(TP + FN).',
        'F1 = 2PR/(P + R); AUC = P(random positive scores above random negative).',
        'Gini = 1 − Σpᵢ²; entropy = −Σpᵢ log₂ pᵢ.'],
}

NOTES = {
    T1: {
        'overview': 'Logistic regression is the standard first model for binary classification, giving interpretable probabilities.',
        'key_terms': ['Sigmoid', 'Probability output', 'Log-odds (logit)', 'Odds ratio', 'Decision boundary', 'Log loss (cross-entropy)', 'Softmax'],
        'explanation': [
            'The model computes z = w·x + b, then p = σ(z) = 1/(1 + e^(−z)). For a model with z = −3 + 0.8x (x = hours of study, predicting passing), x = 5 gives z = 1 and p ≈ 0.731. The decision boundary (p = 0.5, z = 0) is at x = 3.75 hours.',
            'Coefficients act on log-odds: ln(p/(1 − p)) = z. Each extra hour multiplies the odds of passing by e^0.8 ≈ 2.23. This makes logistic regression easy to explain.',
            'Training minimises log loss: for an example whose true class is 1, the loss is −ln p. Predicting p = 0.9 costs 0.105; predicting p = 0.1 costs 2.303, punishing confident mistakes. For more than two classes, the softmax function generalises the sigmoid.'],
        'formulas_label': 'Formulas',
        'formulas': ['p = σ(z) = 1/(1 + e^(−z))', 'ln(p/(1 − p)) = w·x + b', 'Odds ratio per unit = e^w', 'Log loss = −[y ln p + (1 − y) ln(1 − p)]'],
        'steps': ['Compute z = w·x + b.', 'Apply the sigmoid.', 'Compare p with the threshold.', 'Interpret coefficients as odds ratios.'],
        'worked_example': {
            'problem': 'A model gives z = −3 + 0.8x. Find the probability of passing after 5 hours and the decision boundary.',
            'steps': ['z = −3 + 4 = 1.', 'p = 1/(1 + e⁻¹) ≈ 0.731.', 'Boundary: z = 0 → x = 3/0.8 = 3.75 hours.'],
            'answer': 'p ≈ 0.731; the model predicts "pass" above 3.75 hours.',
            'check': 'At x = 3.75, p = σ(0) = 0.5 ✓.'},
        'mistakes': ['Treating the output z as a probability.', 'Interpreting coefficients as changes in probability rather than log-odds.', 'Using MSE instead of log loss.', 'Forgetting the threshold need not be 0.5.'],
        'real_world': 'Hospitals use logistic-regression risk scores to estimate the probability that a patient will be readmitted.',
        'exam_strategy': 'Remember σ(0) = 0.5: the decision boundary is always where the linear score equals zero.',
        'recap': ['Sigmoid to probability.', 'Log-odds.', 'Odds ratios.', 'Log loss.']},
    T2: {
        'overview': 'Different mistakes have different costs. The confusion matrix and the metrics built from it show exactly which mistakes a classifier makes.',
        'key_terms': ['True positive (TP)', 'False positive (FP)', 'False negative (FN)', 'True negative (TN)', 'Accuracy', 'Precision', 'Recall (sensitivity)', 'Specificity', 'F1 score', 'Class imbalance'],
        'explanation': [
            'A fraud model is tested on 1000 transactions: TP = 80, FP = 20, FN = 40, TN = 860. Accuracy = (80 + 860)/1000 = 0.94. But only 120 transactions were fraud, so a model that always says "not fraud" scores 0.88 accuracy while catching nothing.',
            'Precision = 80/(80 + 20) = 0.80: when the model flags fraud, it is right 80% of the time. Recall = 80/(80 + 40) ≈ 0.667: it catches two-thirds of the fraud. Specificity = 860/880 ≈ 0.977. F1 = 2PR/(P + R) ≈ 0.727 balances precision and recall.',
            'Which metric matters depends on costs: missing cancer (FN) is worse than a false alarm, so recall matters most in screening; wrongly blocking a customer\'s card (FP) annoys customers, so precision matters there. With imbalanced classes, report precision, recall and F1, not just accuracy.'],
        'formulas_label': 'Formulas',
        'formulas': ['Accuracy = (TP + TN)/n', 'Precision = TP/(TP + FP)', 'Recall = TP/(TP + FN)', 'Specificity = TN/(TN + FP)', 'F1 = 2PR/(P + R)'],
        'steps': ['Fill in the confusion matrix.', 'Compute accuracy and the majority-class baseline.', 'Compute precision, recall and F1.', 'Choose the metric that matches the costs.'],
        'worked_example': {
            'problem': 'TP = 80, FP = 20, FN = 40, TN = 860. Find precision, recall and F1.',
            'steps': ['Precision = 80/100 = 0.80.', 'Recall = 80/120 ≈ 0.667.', 'F1 = 2 × 0.8 × 0.667/(0.8 + 0.667) ≈ 0.727.'],
            'answer': 'Precision 0.80, recall 0.667, F1 ≈ 0.727.',
            'check': 'F1 lies between precision and recall, nearer the smaller ✓.'},
        'mistakes': ['Swapping precision and recall.', 'Reporting only accuracy on imbalanced data.', 'Ignoring the majority-class baseline.', 'Mislabelling FP and FN.'],
        'real_world': 'Banks tune fraud detectors to balance recall (catching fraud) against precision (not blocking honest customers).',
        'exam_strategy': 'Precision divides by the predicted positives (column); recall by the actual positives (row).',
        'recap': ['Four cells.', 'Accuracy can mislead.', 'Precision vs recall.', 'F1 balances.']},
    T3: {
        'overview': 'A classifier outputs scores; the threshold turns them into decisions. ROC curves show performance across all thresholds.',
        'key_terms': ['Decision threshold', 'True positive rate', 'False positive rate', 'ROC curve', 'AUC', 'Precision–recall curve', 'Calibration'],
        'explanation': [
            'Lowering the threshold flags more cases: recall rises and precision usually falls. Raising it does the reverse. The best threshold depends on the relative costs of false positives and false negatives, not on a default of 0.5.',
            'The ROC curve plots the true positive rate (recall) against the false positive rate (1 − specificity) as the threshold varies. A random classifier follows the diagonal (AUC 0.5); a perfect one hugs the top-left corner (AUC 1).',
            'AUC equals the probability that a randomly chosen positive gets a higher score than a randomly chosen negative. For labels 0, 0, 1, 1, 0, 1 with scores 0.1, 0.4, 0.35, 0.8, 0.2, 0.7, 8 of the 9 positive–negative pairs are correctly ordered: AUC = 8/9 ≈ 0.889. For rare positives, precision–recall curves are often more informative.'],
        'formulas_label': 'Formulas',
        'formulas': ['TPR = TP/(TP + FN)', 'FPR = FP/(FP + TN)', 'AUC = P(score⁺ > score⁻)', 'Random classifier: AUC = 0.5'],
        'steps': ['Get predicted scores on validation data.', 'Vary the threshold and record TPR and FPR.', 'Plot the ROC curve and compute AUC.', 'Pick the threshold that minimises expected cost.'],
        'worked_example': {
            'problem': 'Labels 0, 0, 1, 1, 0, 1 have scores 0.1, 0.4, 0.35, 0.8, 0.2, 0.7. Compute AUC by counting pairs.',
            'steps': ['Positives: 0.35, 0.8, 0.7; negatives: 0.1, 0.4, 0.2; 9 pairs.', '0.35 beats 0.1 and 0.2 but not 0.4 (2); 0.8 and 0.7 beat all three (6).', 'AUC = 8/9.'],
            'answer': 'AUC ≈ 0.889.',
            'check': 'scikit-learn\'s roc_auc_score gives 0.889 ✓.'},
        'mistakes': ['Assuming 0.5 is always the right threshold.', 'Reading AUC as accuracy.', 'Choosing the threshold on the test set.', 'Using ROC alone for very rare positives.'],
        'real_world': 'Medical screening tests choose thresholds that give high sensitivity, accepting more false alarms that follow-up tests resolve.',
        'exam_strategy': 'For "what happens if the threshold is lowered?", answer for both recall and precision.',
        'recap': ['Threshold trade-off.', 'ROC: TPR vs FPR.', 'AUC as ranking.', 'Cost-based thresholds.']},
    T4: {
        'overview': 'k-nearest neighbours and decision trees capture non-linear patterns with simple, intuitive rules.',
        'key_terms': ['k-nearest neighbours', 'Euclidean distance', 'Manhattan distance', 'Majority vote', 'Decision tree', 'Split', 'Gini impurity', 'Entropy', 'Information gain', 'Pruning', 'Random forest'],
        'explanation': [
            'k-NN stores the training data and classifies a new point by majority vote among its k nearest neighbours. Euclidean distance between (1, 2) and (4, 6) is √(9 + 16) = 5; Manhattan distance is 3 + 4 = 7. Small k overfits, large k underfits, and features must be scaled or one feature will dominate the distances.',
            'A decision tree asks a sequence of yes/no questions, choosing at each node the split that most increases purity. Gini impurity is 1 − Σpᵢ²: a node with 40% "yes" and 60% "no" has Gini 0.48 (entropy 0.971 bits). Splitting it into two equal halves with 70% and 10% "yes" gives Gini 0.42 and 0.18, average 0.30, a reduction of 0.18.',
            'Deep trees overfit; limit depth, require a minimum number of samples per leaf, or prune. Random forests average many trees grown on bootstrapped samples with random feature subsets, which greatly reduces variance and is a strong default for tabular data.'],
        'formulas_label': 'Formulas',
        'formulas': ['Euclidean d = √Σ(aᵢ − bᵢ)²', 'Manhattan d = Σ|aᵢ − bᵢ|', 'Gini = 1 − Σpᵢ²', 'Entropy = −Σpᵢ log₂ pᵢ', 'Gain = parent impurity − weighted child impurity'],
        'steps': ['Scale features (for k-NN).', 'Choose k or tree depth by validation.', 'For trees, compute impurity before and after candidate splits.', 'Choose the split with the largest reduction.'],
        'worked_example': {
            'problem': 'A node has 100 samples, 40 "yes". A split gives two nodes of 50 with 35 and 5 "yes". Find the Gini reduction.',
            'steps': ['Parent Gini = 1 − (0.4² + 0.6²) = 0.48.', 'Left: 1 − (0.7² + 0.3²) = 0.42; right: 1 − (0.1² + 0.9²) = 0.18; weighted average 0.30.', 'Reduction = 0.48 − 0.30 = 0.18.'],
            'answer': 'The split reduces Gini impurity by 0.18.',
            'check': 'Both children are purer than the parent (0.42 and 0.18 < 0.48) ✓.'},
        'mistakes': ['Using k-NN on unscaled features.', 'Choosing k = 1 and trusting its training accuracy.', 'Growing trees until every leaf is pure.', 'Forgetting to weight child impurities by size.'],
        'real_world': 'Random forests are widely used to predict crop yields and customer churn because they handle mixed, messy tabular data well.',
        'exam_strategy': 'Lay out impurity calculations in a small table: node, size, class proportions, Gini.',
        'recap': ['k-NN votes.', 'Distances need scaling.', 'Gini and entropy.', 'Prune or use forests.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'σ(0) equals:', ['0.5', '0', '1', 'e'], 0, '1/(1 + 1).', ans=0.5, num=True),
    Q(T1, 'With z = −3 + 0.8x, the probability at x = 5 is about:', ['0.731', '0.5', '0.269', '1'], 0, 'σ(1).', ans=0.731, num=True),
    Q(T1, 'The decision boundary of that model (p = 0.5) is at x =', ['3.75', '5', '0.8', '3'], 0, 'z = 0.', ans=3.75, num=True),
    Q(T1, 'Each extra unit of x multiplies the odds by e^0.8, about:', ['2.23', '0.8', '1.8', '0.45'], 0, 'Odds ratio.', ans=2.23, num=True),
    Q(T1, 'For a true positive predicted with p = 0.1, the log loss is about:', ['2.303', '0.105', '0.9', '0.1'], 0, '−ln 0.1.', ans=2.303, num=True),
    Q(T1, 'Logistic regression coefficients describe changes in:', ['log-odds', 'probability directly', 'accuracy', 'the threshold'], 0, 'Linear in the logit.'),
    # T2
    Q(T2, 'TP = 80, FP = 20, FN = 40, TN = 860. Accuracy is:', ['0.94', '0.80', '0.667', '0.88'], 0, '940/1000.', ans=0.94, num=True),
    Q(T2, 'Precision is:', ['0.80', '0.667', '0.94', '0.977'], 0, '80/100.', ans=0.8, num=True),
    Q(T2, 'Recall is about:', ['0.667', '0.80', '0.94', '0.333'], 0, '80/120.', ans=0.667, num=True),
    Q(T2, 'F1 is about:', ['0.727', '0.733', '0.80', '0.667'], 0, '2PR/(P + R).', ans=0.727, num=True),
    Q(T2, 'A model that always predicts "not fraud" on that data has accuracy:', ['0.88', '0.94', '0.12', '0.5'], 0, '880 negatives.', ans=0.88, num=True),
    Q(T2, 'In cancer screening, the most important metric is usually:', ['recall', 'precision', 'accuracy', 'specificity only'], 0, 'Missing cases is costly.'),
    # T3
    Q(T3, 'Lowering the decision threshold usually:', ['increases recall and decreases precision', 'increases both', 'decreases recall', 'has no effect'], 0, 'More flagged.'),
    Q(T3, 'An ROC curve plots:', ['true positive rate against false positive rate', 'precision against recall', 'loss against epochs', 'accuracy against threshold only'], 0, 'TPR vs FPR.'),
    Q(T3, 'A random classifier has AUC:', ['0.5', '0', '1', '0.25'], 0, 'Diagonal.', ans=0.5, num=True),
    Q(T3, 'Labels 0, 0, 1, 1, 0, 1 with scores 0.1, 0.4, 0.35, 0.8, 0.2, 0.7 give AUC:', ['8/9 ≈ 0.889', '2/3', '1', '0.5'], 0, '8 of 9 pairs ordered.'),
    Q(T3, 'AUC can be interpreted as:', ['the probability a random positive scores above a random negative', 'the accuracy at threshold 0.5', 'the precision', 'the error rate'], 0, 'Ranking quality.'),
    Q(T3, 'The best threshold should be chosen by:', ['the relative costs of errors, on validation data', 'always using 0.5', 'maximising training accuracy', 'the test set'], 0, 'Cost-based.'),
    # T4
    Q(T4, 'The Euclidean distance between (1, 2) and (4, 6) is:', ['5', '7', '25', '3.5'], 0, '√(9 + 16).', ans=5, num=True),
    Q(T4, 'The Manhattan distance between them is:', ['7', '5', '12', '4'], 0, '3 + 4.', ans=7, num=True),
    Q(T4, 'A node with 40% yes and 60% no has Gini impurity:', ['0.48', '0.5', '0.24', '0.971'], 0, '1 − 0.16 − 0.36.', ans=0.48, num=True),
    Q(T4, 'Splitting it into equal halves with 70% and 10% yes reduces Gini by:', ['0.18', '0.30', '0.48', '0.06'], 0, '0.48 − 0.30.', ans=0.18, num=True),
    Q(T4, 'k-NN needs feature scaling because:', ['distances are dominated by large-scale features', 'it uses gradient descent', 'it needs probabilities', 'trees require it'], 0, 'Distance-based.'),
    Q(T4, 'Random forests reduce overfitting mainly by:', ['averaging many decorrelated trees', 'using one very deep tree', 'removing all features', 'increasing k'], 0, 'Variance reduction.'),
]

FLASH = [
    ['Sigmoid', 'σ(z) = 1/(1 + e^(−z)); maps scores to probabilities.'],
    ['Log-odds', 'ln(p/(1 − p)) = w·x + b; e^w is the odds ratio.'],
    ['Precision', 'TP/(TP + FP): how many flagged are real.'],
    ['Recall', 'TP/(TP + FN): how many real are flagged.'],
    ['F1', '2PR/(P + R).'],
    ['ROC and AUC', 'TPR vs FPR; AUC = P(positive ranked above negative).'],
    ['k-NN', 'Majority vote of k nearest points; scale features.'],
    ['Gini impurity', '1 − Σpᵢ²; trees choose splits that reduce it most.'],
]
