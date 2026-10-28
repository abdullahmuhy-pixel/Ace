"""Introduction to Data Analysis, module 4: Relationships between variables."""
import numpy as np
from scipy import stats
from verify import Q
T1, T2, T3, T4 = ('Correlation', 'Simple linear regression', 'Multiple regression and interpretation', 'Categorical data and the chi-square test')
r = lambda v, d: round(float(v), d)
X, Y = np.array([1, 2, 3, 4, 5]), np.array([3, 5, 6, 8, 9])  # advertising (R thousand) and sales (R thousand)
rr = np.corrcoef(X, Y)[0, 1]; b, a = np.polyfit(X, Y, 1)
assert X.mean() == 3 and r(Y.mean(), 1) == 6.2 and r(((X - 3) * (Y - 6.2)).sum(), 6) == 15 and ((X - 3) ** 2).sum() == 10
assert r(rr, 3) == 0.993 and r(rr ** 2, 3) == 0.987 and r(b, 6) == 1.5 and r(a, 6) == 1.7 and r(a + b * 6, 6) == 10.7
assert [r(v, 6) for v in Y - (a + b * X)] == [-0.2, 0.3, -0.2, 0.3, -0.2]
assert 1500 + 85 * 60 - 300 * 5 == 5100 and 85 * 10 == 850
T = np.array([[40, 160], [60, 140]]); c = stats.chi2_contingency(T, correction=False)
assert r(c.statistic, 2) == 5.33 and r(c.pvalue, 3) == 0.021 and c.expected_freq.tolist() == [[50, 150], [50, 150]] and c.dof == 1
assert 40 / 200 == 0.2 and 60 / 200 == 0.3

MODULE = {
    'title': 'Relationships between variables',
    'topics': [T1, T2, T3, T4],
    'overview': 'Most analysis questions are about relationships: does advertising raise sales, does distance raise delivery times, does device type affect buying? This module covers correlation, fitting and interpreting a regression line, regression with several predictors, and testing association between categorical variables, always keeping in mind that association is not causation.',
    'key_terms': ['Scatter plot', 'Correlation coefficient r', 'Causation', 'Confounding variable', 'Regression line', 'Slope', 'Intercept', 'Residual', 'R²', 'Extrapolation', 'Multiple regression', 'Dummy variable', 'Contingency table', 'Expected count', 'Chi-square test'],
    'explanation': [
        'Correlation r measures the strength and direction of a linear relationship between two numerical variables, from −1 to +1. It says nothing about cause: a third, confounding variable may drive both.',
        'A regression line ŷ = a + bx predicts a response from an explanatory variable. The slope b is the predicted change in y per unit of x; residuals (actual − predicted) show what the line misses, and R² is the share of variation in y the line explains. Multiple regression adds predictors, and each coefficient then describes the effect of one variable holding the others constant.',
        'For two categorical variables, a contingency table compares observed counts with the counts expected if there were no association. The chi-square statistic adds up the squared differences, scaled by the expected counts, and a small p-value suggests the variables are related.'],
    'quick_facts': [
        'r between −1 and 1; measures linear association only.',
        'b = Σ(x − x̄)(y − ȳ)/Σ(x − x̄)²; a = ȳ − b x̄.',
        'Residual = observed − predicted; R² = share of variance explained.',
        'Coefficients in multiple regression hold other variables constant.',
        'Expected = row total × column total/grand total; χ² = Σ(O − E)²/E.'],
}

NOTES = {
    T1: {
        'overview': 'Correlation summarises how closely two numerical variables follow a straight-line pattern.',
        'key_terms': ['Scatter plot', 'Positive and negative association', 'Correlation coefficient r', 'Linear vs non-linear', 'Outlier influence', 'Confounding', 'Spurious correlation'],
        'explanation': [
            'Always plot first. A scatter plot shows direction (positive or negative), form (linear or curved), strength and unusual points. r summarises a linear pattern: +1 is a perfect upward line, −1 a perfect downward line, 0 no linear relationship.',
            'For advertising spend x = 1, 2, 3, 4, 5 (R thousand) and sales y = 3, 5, 6, 8, 9 (R thousand), r ≈ 0.993: a very strong positive linear relationship. r has no units and does not change if you switch x and y or rescale them.',
            'r can mislead: a curved relationship can have r near 0, and a single outlier can create or destroy a strong r. Correlation is not causation: ice-cream sales and drownings both rise in summer because of a confounder (hot weather). To show causation you need a randomised experiment or very careful study design.'],
        'formulas_label': 'Formulas',
        'formulas': ['r = Σ(zₓ z_y)/(n − 1)', '−1 ≤ r ≤ 1', 'r² = share of variance explained by the line'],
        'steps': ['Plot the data.', 'Describe direction, form, strength and outliers.', 'Compute r only if the pattern is roughly linear.', 'Consider confounders before suggesting causes.'],
        'worked_example': {
            'problem': 'Advertising (1 to 5) and sales (3, 5, 6, 8, 9) have r ≈ 0.993. Can we conclude advertising causes sales?',
            'steps': ['r shows a very strong positive linear association.', 'The data are observational: other factors (season, promotions) may have changed too.', 'Only an experiment, randomly varying advertising, would show causation.'],
            'answer': 'No; the association is strong but causation is not established.',
            'check': 'A randomised test of advertising levels would address confounding ✓.'},
        'mistakes': ['Using r for curved patterns.', 'Saying r = 0 means no relationship of any kind.', 'Treating correlation as causation.', 'Ignoring influential outliers.'],
        'real_world': 'Health researchers found coffee drinking correlated with heart disease until they adjusted for smoking, a confounder.',
        'exam_strategy': 'In any correlation question, add one sentence on possible confounders; it is usually worth a mark.',
        'recap': ['Plot first.', 'r from −1 to 1.', 'Linear only.', 'Not causation.']},
    T2: {
        'overview': 'A regression line summarises how a response changes with an explanatory variable and can be used for prediction.',
        'key_terms': ['Explanatory and response variables', 'Least squares', 'Slope', 'Intercept', 'Prediction', 'Residual', 'Residual plot', 'R²', 'Extrapolation'],
        'explanation': [
            'Least squares chooses the line that minimises the sum of squared residuals. For the advertising data, x̄ = 3 and ȳ = 6.2, Σ(x − x̄)(y − ȳ) = 15 and Σ(x − x̄)² = 10, so b = 1.5 and a = 6.2 − 1.5 × 3 = 1.7: ŷ = 1.7 + 1.5x.',
            'Interpretation: each extra R1000 of advertising is associated with about R1500 more sales. The intercept (sales with no advertising) is meaningful only if x = 0 is within or near the data. Predicting at x = 6 gives 10.7, a mild extrapolation; predicting far outside the data range is risky.',
            'Residuals are −0.2, 0.3, −0.2, 0.3, −0.2: small and patternless, so the line fits well. R² = r² ≈ 0.987: about 98.7% of the variation in sales is explained by advertising. A curved pattern in a residual plot means a straight line is the wrong model.'],
        'formulas_label': 'Formulas',
        'formulas': ['ŷ = a + bx', 'b = Σ(x − x̄)(y − ȳ)/Σ(x − x̄)² = r s_y/sₓ', 'a = ȳ − b x̄', 'Residual = y − ŷ', 'R² = r² (simple regression)'],
        'steps': ['Compute means.', 'Compute b, then a.', 'Interpret the slope in context with units.', 'Check residuals and R²; avoid extrapolation.'],
        'worked_example': {
            'problem': 'Fit the least-squares line to x = 1, 2, 3, 4, 5 and y = 3, 5, 6, 8, 9, and predict y at x = 6.',
            'steps': ['x̄ = 3, ȳ = 6.2; Σ(x − x̄)(y − ȳ) = 6.4 + 1.2 + 0 + 1.8 + 5.6 = 15; Σ(x − x̄)² = 10.', 'b = 15/10 = 1.5; a = 6.2 − 4.5 = 1.7.', 'ŷ(6) = 1.7 + 1.5 × 6 = 10.7.'],
            'answer': 'ŷ = 1.7 + 1.5x; prediction 10.7 (R thousand).',
            'check': 'The line passes through (x̄, ȳ) = (3, 6.2) ✓; residuals sum to zero ✓.'},
        'mistakes': ['Swapping x and y (the line changes).', 'Interpreting the slope without units.', 'Extrapolating far beyond the data.', 'Ignoring a curved residual pattern.'],
        'real_world': 'Utilities forecast electricity demand from temperature using regression, then plan which power stations to run.',
        'exam_strategy': 'Use the template: "For each additional [unit of x], [y] is predicted to change by [b units], on average."',
        'recap': ['Least squares.', 'Slope interpretation.', 'Residuals.', 'R² and extrapolation.']},
    T3: {
        'overview': 'Multiple regression uses several predictors at once, letting analysts separate overlapping effects.',
        'key_terms': ['Multiple regression', 'Coefficient', 'Holding other variables constant', 'Dummy (indicator) variable', 'Adjusted R²', 'Multicollinearity', 'Overfitting', 'Omitted-variable bias'],
        'explanation': [
            'A fitted model for monthly rent (R) is: rent = 1500 + 85 × area (m²) − 300 × distance (km to the city centre). For a 60 m² flat 5 km out, predicted rent = 1500 + 5100 − 1500 = R5100. Each extra m² adds R85 holding distance constant; 10 extra m² adds R850.',
            'Categorical predictors enter as dummy variables (1 if a flat has parking, 0 if not); the coefficient is the average difference between the groups, holding the other predictors fixed. A model with k categories needs k − 1 dummies.',
            'Pitfalls: correlated predictors (multicollinearity) make coefficients unstable; adding many predictors raises R² even when they are useless, so use adjusted R² and test on new data; leaving out an important variable biases the others (omitted-variable bias). Coefficients still describe associations, not causes, unless the design supports causation.'],
        'formulas_label': 'Formulas',
        'formulas': ['ŷ = b₀ + b₁x₁ + b₂x₂ + …', 'bⱼ = change in ŷ per unit xⱼ, others fixed', 'k categories → k − 1 dummies', 'Adjusted R² penalises extra predictors'],
        'steps': ['Write the fitted equation.', 'Interpret each coefficient "holding the others constant".', 'Substitute values to predict.', 'Check fit on new data and watch for collinearity.'],
        'worked_example': {
            'problem': 'Using rent = 1500 + 85 × area − 300 × distance, predict rent for 60 m² at 5 km.',
            'steps': ['85 × 60 = 5100.', '300 × 5 = 1500.', '1500 + 5100 − 1500 = 5100.'],
            'answer': 'About R5100 per month.',
            'check': 'Moving 1 km closer adds R300, giving R5400 at 4 km ✓.'},
        'mistakes': ['Interpreting a coefficient without "holding others constant".', 'Using k dummies for k categories.', 'Judging a model only by R² on the same data.', 'Calling coefficients causal effects.'],
        'real_world': 'Property websites estimate house values with multiple regression on size, location, age and features.',
        'exam_strategy': 'When interpreting, name the units of both the predictor and the response, and add "holding the other variables constant".',
        'recap': ['Several predictors.', 'Ceteris paribus.', 'Dummies.', 'Overfitting and collinearity.']},
    T4: {
        'overview': 'When both variables are categorical, compare observed counts with the counts expected under no association.',
        'key_terms': ['Contingency table', 'Row and column percentages', 'Expected count', 'Chi-square statistic', 'Degrees of freedom', 'Independence', 'Simpson\'s paradox'],
        'explanation': [
            'An online shop records device and whether a visit led to a purchase: mobile 40 yes, 160 no; desktop 60 yes, 140 no. Conversion rates: mobile 40/200 = 20%, desktop 60/200 = 30%.',
            'Expected counts if device and purchase were independent: row total × column total/grand total = 200 × 100/400 = 50 purchases for each device (and 150 non-purchases). χ² = Σ(O − E)²/E = 2 × [(10²/50) + (10²/150)] ≈ 5.33 with (2 − 1)(2 − 1) = 1 degree of freedom, giving p ≈ 0.021: evidence that conversion differs by device.',
            'Conditions: random data and expected counts of at least 5 in each cell. Beware Simpson\'s paradox: an association can reverse when a third variable (such as product category) is taken into account, so look at subgroups too.'],
        'formulas_label': 'Formulas',
        'formulas': ['E = (row total × column total)/grand total', 'χ² = Σ(O − E)²/E', 'df = (rows − 1)(columns − 1)', 'Expected counts ≥ 5'],
        'steps': ['Build the contingency table.', 'Compare row percentages.', 'Compute expected counts and χ².', 'Find the p-value and conclude in context.'],
        'worked_example': {
            'problem': 'Test whether purchase depends on device: mobile 40/160, desktop 60/140 (yes/no).',
            'steps': ['Expected: 50 yes and 150 no for each device.', 'χ² = (10²/50) × 2 + (10²/150) × 2 = 4 + 1.33 = 5.33.', 'df = 1; p ≈ 0.021 < 0.05.'],
            'answer': 'Reject independence: desktop visitors convert more often (30% vs 20%).',
            'check': 'All expected counts are well above 5 ✓.'},
        'mistakes': ['Running chi-square on percentages instead of counts.', 'Forgetting the expected-count condition.', 'Concluding causation from a chi-square test.', 'Ignoring Simpson\'s paradox.'],
        'real_world': 'Marketing teams use contingency tables to compare sign-up rates across channels, regions and devices.',
        'exam_strategy': 'Always show at least one expected-count calculation and the degrees of freedom.',
        'recap': ['Row percentages.', 'Expected counts.', 'χ² and df.', 'Check subgroups.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'r for advertising 1–5 and sales 3, 5, 6, 8, 9 is about:', ['0.993', '0.5', '−0.993', '1.5'], 0, 'Very strong positive.', ans=0.993, num=True),
    Q(T1, 'A correlation of −0.85 indicates:', ['a strong negative linear relationship', 'no relationship', 'a weak positive relationship', 'causation'], 0, 'Sign and size.'),
    Q(T1, 'A curved U-shaped relationship can have r close to:', ['0', '1', '−1', '0.5 always'], 0, 'r measures linear patterns.'),
    Q(T1, 'Ice-cream sales and drownings are correlated because of:', ['a confounding variable (hot weather)', 'ice cream causing drowning', 'drowning causing ice-cream sales', 'measurement error'], 0, 'Lurking variable.'),
    Q(T1, 'Changing sales from rand to thousands of rand changes r:', ['not at all', 'by a factor of 1000', 'to its negative', 'to zero'], 0, 'r has no units.'),
    Q(T1, 'To show that advertising causes sales, the best design is:', ['a randomised experiment', 'a larger observational sample', 'a higher r', 'a pie chart'], 0, 'Controls confounders.'),
    # T2
    Q(T2, 'For that data the least-squares slope is:', ['1.5', '1.7', '0.993', '6.2'], 0, '15/10.', ans=1.5, num=True),
    Q(T2, 'The intercept is:', ['1.7', '1.5', '3', '6.2'], 0, '6.2 − 1.5 × 3.', ans=1.7, num=True),
    Q(T2, 'The prediction at x = 6 is:', ['10.7', '9', '10.2', '11.5'], 0, '1.7 + 9.', ans=10.7, num=True),
    Q(T2, 'The residual for the point (2, 5) is:', ['0.3', '−0.3', '4.7', '0.2'], 0, '5 − 4.7.', ans=0.3, num=True),
    Q(T2, 'R² ≈ 0.987 means:', ['about 98.7% of the variation in sales is explained by the line', 'the slope is 0.987', '98.7% of points lie on the line', 'advertising causes 98.7% of sales'], 0, 'Variance explained.'),
    Q(T2, 'Predicting sales at an advertising spend of 50 from data between 1 and 5 is:', ['risky extrapolation', 'interpolation', 'always accurate', 'a residual'], 0, 'Far outside the data.'),
    # T3
    Q(T3, 'rent = 1500 + 85 × area − 300 × distance. Predict rent for 60 m² at 5 km.', ['R5100', 'R6600', 'R3600', 'R8100'], 0, '1500 + 5100 − 1500.'),
    Q(T3, 'In that model, 10 extra m² (same distance) adds:', ['R850', 'R85', 'R3000', 'R8500'], 0, '85 × 10.'),
    Q(T3, 'The coefficient −300 on distance means:', ['each extra km is associated with R300 less rent, holding area constant', 'rent falls by 300%', 'distance causes rent', 'rent is R300 at the centre'], 0, 'Ceteris paribus.'),
    Q(T3, 'A categorical predictor with 4 categories needs how many dummy variables?', ['3', '4', '1', '2'], 0, 'k − 1.', ans=3, num=True),
    Q(T3, 'Adding many useless predictors will usually:', ['raise R² but not improve predictions on new data', 'lower R²', 'remove bias', 'prove causation'], 0, 'Overfitting.'),
    Q(T3, 'Leaving out an important predictor can cause:', ['omitted-variable bias', 'perfect fit', 'zero residuals', 'a smaller sample'], 0, 'Other coefficients absorb it.'),
    # T4
    Q(T4, 'Mobile: 40 purchases out of 200 visits. The conversion rate is:', ['20%', '40%', '25%', '80%'], 0, '40/200.'),
    Q(T4, 'The expected number of mobile purchases under independence (100 purchases out of 400 visits overall) is:', ['50', '40', '60', '25'], 0, '200 × 100/400.', ans=50, num=True),
    Q(T4, 'The chi-square statistic for that 2 × 2 table is about:', ['5.33', '2.67', '10.0', '0.021'], 0, '4 + 1.33.', ans=5.33, num=True),
    Q(T4, 'Its degrees of freedom are:', ['1', '2', '3', '4'], 0, '(2 − 1)(2 − 1).', ans=1, num=True),
    Q(T4, 'With p ≈ 0.021, at α = 0.05 you conclude:', ['purchase and device appear to be associated', 'they are independent', 'mobile causes fewer purchases', 'the test is invalid'], 0, 'Reject independence.'),
    Q(T4, 'An association that reverses when a third variable is considered is called:', ['Simpson\'s paradox', 'multicollinearity', 'extrapolation', 'a Type II error'], 0, 'Check subgroups.'),
]

FLASH = [
    ['Correlation r', 'Strength and direction of a linear relationship, −1 to 1.'],
    ['Correlation vs causation', 'Confounders can create association; experiments test causes.'],
    ['Least-squares slope', 'b = Σ(x − x̄)(y − ȳ)/Σ(x − x̄)².'],
    ['Intercept', 'a = ȳ − b x̄.'],
    ['Residual', 'Observed − predicted.'],
    ['R²', 'Share of variation in y explained by the model.'],
    ['Multiple regression coefficient', 'Change in ŷ per unit, holding other predictors constant.'],
    ['Chi-square test', 'χ² = Σ(O − E)²/E, E = row × column/total.'],
]
