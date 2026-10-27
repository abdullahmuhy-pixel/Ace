"""Probability and Statistics, module 5: Hypothesis testing and regression."""
from math import erf, sqrt
import mpmath as mp
from verify import Q, sp
T1, T2, T3, T4 = ('Hypothesis testing: p-values and errors', 'Tests for a mean and a proportion', 'The chi-square test of independence', 'Correlation and linear regression')
R = sp.Rational


def Phi(z): return 0.5 * (1 + erf(z / sqrt(2)))


def tq(df, p): return float(mp.findroot(lambda t: mp.betainc(df / 2, 0.5, 0, df / (df + t * t), regularized=True) / 2 - (1 - p), 2))


def chi(df, p): return float(mp.findroot(lambda x: mp.gammainc(df / 2., 0, x / 2., regularized=True) - p, df + 1))


# checked numbers
assert round(2 * (1 - Phi(2)), 4) == 0.0455 and round(tq(24, 0.975), 3) == 2.064 and round(chi(1, 0.95), 3) == 3.841 and round(chi(2, 0.95), 3) == 5.991
X, Y = [1, 2, 3, 4, 5], [2, 4, 5, 4, 5]
mx, my = R(sum(X), 5), R(sum(Y), 5)
Sxy = sum((x - mx) * (y - my) for x, y in zip(X, Y)); Sxx = sum((x - mx) ** 2 for x in X); Syy = sum((y - my) ** 2 for y in Y)
b = Sxy / Sxx; a = my - b * mx; r = Sxy / sp.sqrt(Sxx * Syy)
assert (Sxy, Sxx, Syy, b, a) == (6, 10, 6, R(3, 5), R(11, 5)) and round(float(r), 4) == 0.7746 and r ** 2 == R(3, 5)
obs = [[30, 20], [20, 30]]
chi_stat = sum((o - 25) ** 2 / R(25) for row in obs for o in row)
assert chi_stat == 4

MODULE = {
    'title': 'Hypothesis testing and regression',
    'topics': [T1, T2, T3, T4],
    'overview': 'Hypothesis tests decide whether a pattern in a sample is strong enough to believe it exists in the population, and regression describes and predicts how one variable changes with another. Together they are the tools you will use most in project work and research methods.',
    'key_terms': ['Null hypothesis', 'Alternative hypothesis', 'Test statistic', 'p-value', 'Significance level', 'Type I error', 'Type II error', 'Chi-square', 'Correlation', 'Least-squares line'],
    'explanation': [
        'Every test follows the same five steps: state H₀ and H₁, choose a significance level α, compute a test statistic from the data, find the p-value (or compare with a critical value), and write a conclusion in context. The p-value is the probability of data at least this extreme if H₀ were true. A small p-value is evidence against H₀.',
        'The test you choose depends on the data: a z or t test for a mean, a z test for a proportion, and a chi-square test for the relationship between two categorical variables. Every test also has conditions (random sampling, independence, large enough counts) that must be checked before the result can be trusted.',
        'For two numerical variables, start with a scatter plot, then measure the strength of a linear relationship with the correlation r and fit the least-squares line ŷ = a + bx for prediction. Correlation is not causation, and predictions outside the range of the data are unreliable.'],
    'quick_facts': [
        'p-value < α: reject H₀; otherwise do not reject it (never "accept").',
        'Type I error: reject a true H₀ (probability α).',
        'Type II error: fail to reject a false H₀.',
        'Chi-square: expected = row total × column total ÷ grand total; df = (r − 1)(c − 1).',
        'Least squares: b = Sxy/Sxx and a = ȳ − b x̄; r² is the share of variation explained.'],
}

NOTES = {
    T1: {
        'overview': 'A hypothesis test weighs the evidence in a sample against a claim about the population. It starts by assuming the claim of "no effect" (the null hypothesis) and asks how surprising the data would be if that claim were true.',
        'key_terms': ['Null hypothesis H₀', 'Alternative hypothesis H₁', 'One-tailed', 'Two-tailed', 'p-value', 'Significance level α', 'Type I error', 'Type II error', 'Power'],
        'explanation': [
            'H₀ states no effect or no difference and always contains an equals sign, for example μ = 500. H₁ is what you are looking for evidence of: μ ≠ 500 (two-tailed), μ > 500 or μ < 500 (one-tailed). Choose H₁ before seeing the data, from the research question.',
            'The p-value is P(data at least as extreme as observed | H₀ true). If p < α (often 0.05) the result is statistically significant and we reject H₀. If p ≥ α we do not reject H₀. That is not proof that H₀ is true, only that the evidence is not strong enough.',
            'Two errors are possible. A Type I error rejects a true H₀ and happens with probability α. A Type II error fails to reject a false H₀. The power (1 − P(Type II)) increases with sample size and with the size of the real effect. Lowering α reduces Type I errors but increases Type II errors.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Test statistic = (estimate − hypothesised value) / SE', 'Reject H₀ if p-value < α', 'P(Type I error) = α', 'Power = 1 − P(Type II error)'],
        'steps': ['State H₀ and H₁ in symbols and words.', 'Choose α and check the conditions.', 'Compute the test statistic.', 'Find the p-value or the critical value.', 'Decide, then conclude in context.'],
        'worked_example': {
            'problem': 'A bottling plant claims a mean fill of 500 ml. σ = 40 ml. A sample of 64 bottles has x̄ = 510 ml. Test at the 5% level whether the mean differs from 500.',
            'steps': ['H₀: μ = 500; H₁: μ ≠ 500 (two-tailed), α = 0.05.', 'SE = 40/√64 = 5, so z = (510 − 500)/5 = 2.', 'p-value = 2 × (1 − Φ(2)) = 2 × 0.0228 = 0.0455.', '0.0455 < 0.05, so reject H₀.'],
            'answer': 'There is evidence at the 5% level that the mean fill differs from 500 ml (it appears to be higher).',
            'check': 'At the 1% level (p = 0.0455 > 0.01) we would not reject H₀, so the evidence is moderate rather than overwhelming.'},
        'mistakes': ['Writing H₀ in terms of the sample mean x̄ instead of the population mean μ.', 'Saying "accept H₀" or "H₀ is proved".', 'Reading the p-value as P(H₀ is true).', 'Choosing one-tailed after seeing which way the data point.'],
        'real_world': 'Courts work the same way: the defendant is presumed innocent (H₀) and convicted only on strong evidence. Convicting an innocent person is a Type I error; acquitting a guilty one is a Type II error.',
        'exam_strategy': 'End every test with a sentence in context that mentions the significance level, for example "At the 5% level there is sufficient evidence that…". Examiners rarely give the final mark for "reject H₀" alone.',
        'recap': ['H₀ has the equals sign; H₁ is the claim you want to show.', 'p < α: reject H₀.', 'Type I: reject a true H₀; Type II: miss a false one.', 'Conclude in context with the significance level.']},
    T2: {
        'overview': 'Tests for a single mean or proportion compare a sample estimate with a claimed value, measuring the gap in standard errors.',
        'key_terms': ['z test', 't test', 'One-sample test', 'Test for a proportion', 'Critical value', 'Degrees of freedom'],
        'explanation': [
            'For a mean with σ known, z = (x̄ − μ₀)/(σ/√n). When σ is unknown (the usual case) use t = (x̄ − μ₀)/(s/√n) with n − 1 degrees of freedom. The t test needs a random sample and either roughly normal data or a large n.',
            'For a proportion, use z = (p̂ − p₀)/√(p₀(1 − p₀)/n). Note that the standard error uses the hypothesised p₀, not p̂, because the test assumes H₀ is true. The condition is np₀ ≥ 10 and n(1 − p₀) ≥ 10.',
            'A two-tailed test at level α rejects when |test statistic| is larger than the critical value: 1.96 for z at 5%, or t* from the table. A two-tailed test at α rejects exactly when the (1 − α) confidence interval excludes μ₀, so tests and intervals tell the same story.'],
        'formulas_label': 'Formulas',
        'formulas': ['z = (x̄ − μ₀)/(σ/√n)', 't = (x̄ − μ₀)/(s/√n), df = n − 1', 'z = (p̂ − p₀)/√(p₀(1 − p₀)/n)', 'Two-tailed 5%: |z| > 1.96'],
        'steps': ['State H₀ and H₁ about μ or p.', 'Choose z or t and check the conditions.', 'Compute the test statistic.', 'Compare with the critical value or find the p-value.', 'Conclude in context.'],
        'worked_example': {
            'problem': 'A lecturer believes the mean score is 50. A random sample of 25 scripts gives x̄ = 52 and s = 5. Test H₀: μ = 50 against H₁: μ ≠ 50 at the 5% level.',
            'steps': ['σ is unknown, so use t with 24 degrees of freedom.', 't = (52 − 50)/(5/√25) = 2/1 = 2.0.', 'The two-tailed 5% critical value t₂₄ is 2.064.', '|2.0| < 2.064, so do not reject H₀.'],
            'answer': 'At the 5% level there is not enough evidence that the mean score differs from 50.',
            'check': 'With z the critical value 1.96 would have led to rejection. The extra uncertainty from estimating σ with s makes t more cautious.'},
        'mistakes': ['Using z when σ is unknown and n is small.', 'Using p̂ instead of p₀ in the standard error of a proportion test.', 'Comparing a one-tailed p-value with a two-tailed α.', 'Forgetting the absolute value in two-tailed comparisons.'],
        'real_world': 'Manufacturers test whether a production line still meets its target, for example mean battery life of 10 hours, and stop the line when a t test shows the mean has slipped.',
        'exam_strategy': 'State the distribution with its degrees of freedom ("t₂₄") and the critical value you compare with. If you use a calculator p-value, write it down to at least 3 significant figures.',
        'recap': ['σ known: z; σ unknown: t (df = n − 1).', 'Proportion SE uses p₀.', 'Two-tailed: compare |statistic| with the critical value.', 'Tests and confidence intervals agree.']},
    T3: {
        'overview': 'The chi-square test of independence asks whether two categorical variables are related, for example faculty and preferred study method, by comparing observed counts with the counts expected if there were no relationship.',
        'key_terms': ['Contingency table', 'Observed count', 'Expected count', 'Chi-square statistic', 'Degrees of freedom', 'Independence'],
        'explanation': [
            'H₀: the two variables are independent; H₁: they are associated. Under H₀ the expected count in each cell is (row total × column total) ÷ grand total. This spreads each row in the same proportions as the overall column totals.',
            'The statistic χ² = Σ(O − E)²/E adds up the squared gaps, scaled by the expected counts. A large χ² means the observed table is far from what independence predicts. Compare it with the critical value for (r − 1)(c − 1) degrees of freedom, for example 3.841 for 1 df and 5.991 for 2 df at the 5% level.',
            'The test needs counts (not percentages), independent observations, and expected counts of at least 5 in every cell. If some expected counts are too small, combine categories. A significant result shows association, not causation: look at which cells have the largest (O − E)²/E to describe the pattern.'],
        'formulas_label': 'Formulas',
        'formulas': ['E = (row total × column total) / grand total', 'χ² = Σ(O − E)²/E', 'df = (r − 1)(c − 1)', 'Critical values at 5%: 3.841 (1 df), 5.991 (2 df), 9.488 (4 df)'],
        'steps': ['State H₀ (independent) and H₁ (associated).', 'Compute every expected count and check each is ≥ 5.', 'Compute (O − E)²/E for each cell and add.', 'Compare with the critical value for (r − 1)(c − 1) df.', 'Conclude and describe the main source of the association.'],
        'worked_example': {
            'problem': '100 students were asked whether they prefer online or in-person classes. Of 50 first-years, 30 prefer online; of 50 final-years, 20 prefer online. Test for association at the 5% level.',
            'steps': ['Row and column totals are all 50, so every expected count is 50 × 50 / 100 = 25.', 'χ² = (30 − 25)²/25 + (20 − 25)²/25 + (20 − 25)²/25 + (30 − 25)²/25 = 4 × 1 = 4.0.', 'df = (2 − 1)(2 − 1) = 1, so the critical value is 3.841.', '4.0 > 3.841, so reject H₀.'],
            'answer': 'At the 5% level there is evidence that preference is associated with year of study: first-years lean towards online classes.',
            'check': 'Every expected count is 25 ≥ 5 ✓, and the result is only just significant, matching a p-value of about 0.046.'},
        'mistakes': ['Running the test on percentages instead of counts.', 'Using r × c instead of (r − 1)(c − 1) for the degrees of freedom.', 'Ignoring expected counts below 5.', 'Concluding that one variable causes the other.'],
        'real_world': 'Public health researchers use chi-square tests to check whether vaccination uptake differs between regions or age groups, which then guides where outreach campaigns go.',
        'exam_strategy': 'Lay out a table of O, E and (O − E)²/E for every cell. It makes the arithmetic checkable and shows which cells drive the result, which you need for the conclusion.',
        'recap': ['H₀: independent.', 'E = row × column ÷ total; all E ≥ 5.', 'χ² = Σ(O − E)²/E; df = (r − 1)(c − 1).', 'Association is not causation.']},
    T4: {
        'overview': 'Correlation measures how strongly two numerical variables move together along a straight line, and least-squares regression fits the line that predicts one from the other.',
        'key_terms': ['Scatter plot', 'Correlation coefficient r', 'Least-squares line', 'Slope', 'Intercept', 'Residual', 'r²', 'Extrapolation'],
        'explanation': [
            'The correlation r lies between −1 and 1. Its sign gives the direction and its size gives the strength of the linear relationship. r = 0 means no linear relationship, though there could still be a curved one. r has no units and is badly affected by outliers.',
            'The least-squares line ŷ = a + bx minimises the sum of squared residuals (y − ŷ). With Sxx = Σ(x − x̄)², Syy = Σ(y − ȳ)² and Sxy = Σ(x − x̄)(y − ȳ), the slope is b = Sxy/Sxx and the intercept is a = ȳ − b x̄. The line always passes through (x̄, ȳ). The slope is the predicted change in y for each one-unit increase in x.',
            'r² is the proportion of the variation in y explained by the linear relationship with x. Predict only within the range of the x data (interpolation). Extrapolating beyond it assumes the pattern continues, which it often does not. And remember that a strong correlation does not prove that x causes y: a third, lurking variable may drive both.'],
        'formulas_label': 'Formulas',
        'formulas': ['Sxy = Σ(x − x̄)(y − ȳ), Sxx = Σ(x − x̄)², Syy = Σ(y − ȳ)²', 'r = Sxy / √(Sxx Syy)', 'b = Sxy / Sxx, a = ȳ − b x̄', 'Residual = y − ŷ', 'r² = share of variation in y explained'],
        'steps': ['Plot the data and check the pattern is roughly linear.', 'Compute x̄, ȳ, Sxx, Syy and Sxy.', 'Find r, then b and a.', 'Interpret the slope and r² in context.', 'Predict only within the data range.'],
        'worked_example': {
            'problem': 'Hours studied (x) and quiz score (y) for 5 students: (1, 2), (2, 4), (3, 5), (4, 4), (5, 5). Find the regression line and r.',
            'steps': ['x̄ = 3 and ȳ = 4.', 'Sxy = (−2)(−2) + (−1)(0) + 0(1) + 1(0) + 2(1) = 6; Sxx = 10; Syy = 6.', 'b = 6/10 = 0.6 and a = 4 − 0.6 × 3 = 2.2.', 'r = 6/√(10 × 6) = 6/√60 ≈ 0.775.'],
            'answer': 'ŷ = 2.2 + 0.6x and r ≈ 0.775, a fairly strong positive relationship. Each extra hour predicts 0.6 more marks.',
            'check': 'The line passes through (3, 4) ✓, and r² = 0.6, so 60% of the variation in scores is explained by hours studied.'},
        'mistakes': ['Concluding causation from correlation.', 'Swapping x and y, which gives a different line.', 'Extrapolating far beyond the data.', 'Treating r = 0 as "no relationship at all" when the pattern may be curved.'],
        'real_world': 'Businesses regress sales on advertising spend to estimate the return on each extra unit of advertising, while being careful that seasons or prices are not driving both.',
        'exam_strategy': 'Interpret the slope in words with units ("each extra hour of study is associated with 0.6 more marks"), and add a sentence about causation or extrapolation when the question invites it.',
        'recap': ['r: direction and strength of a linear relationship.', 'b = Sxy/Sxx; a = ȳ − b x̄.', 'r² = proportion of variation explained.', 'No causation, no extrapolation.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A p-value is the probability of:', ['data at least as extreme as observed, if H₀ is true', 'H₀ being true', 'H₁ being true', 'making a Type II error'], 0, 'It is calculated assuming H₀, about the data, not about the hypotheses.'),
    Q(T1, 'A Type I error is:', ['rejecting H₀ when it is true', 'not rejecting H₀ when it is false', 'using the wrong test', 'a calculation mistake'], 0, 'Its probability is the significance level α.'),
    Q(T1, 'A test gives p = 0.03. At the 5% level you should:', ['reject H₀', 'accept H₀', 'not reject H₀', 'accept H₁ with certainty'], 0, '0.03 < 0.05, so the result is significant at 5%.'),
    Q(T1, 'A researcher wants to show a new method raises the mean above 60. The hypotheses are:', ['H₀: μ = 60, H₁: μ > 60', 'H₀: μ > 60, H₁: μ = 60', 'H₀: x̄ = 60, H₁: x̄ > 60', 'H₀: μ ≠ 60, H₁: μ = 60'], 0, 'H₀ holds the equals sign and is about the population mean μ.'),
    Q(T1, 'σ = 40, n = 64, x̄ = 510 and H₀: μ = 500. What is the z statistic?', ['2', '0.25', '10', '1.6'], 0, 'SE = 40/8 = 5; z = 10/5 = 2.', ans=2),
    Q(T1, 'Which change increases the power of a test?', ['A larger sample size', 'A smaller significance level', 'A smaller true effect', 'More variable data'], 0, 'A larger n shrinks the standard error, making real effects easier to detect.'),
    # T2
    Q(T2, 'n = 25, x̄ = 52, s = 5 and H₀: μ = 50. What is the t statistic?', ['2', '0.4', '10', '2.064'], 0, '(52 − 50)/(5/5) = 2.', ans=2),
    Q(T2, 'What is the two-tailed 5% critical value of t with 24 degrees of freedom?', ['2.064', '1.96', '1.711', '2.797'], 0, 't₂₄ with 0.025 in each tail is 2.064.', ans=tq(24, 0.975), num=True),
    Q(T2, 'H₀: p = 0.5. In a sample of 100, 60 say yes. What is the z statistic?', ['2', '1', '0.1', '10'], 0, 'SE = √(0.25/100) = 0.05, so z = 0.1/0.05 = 2.', ans=(R(6, 10) - R(1, 2)) / sp.sqrt(R(1, 4) / 100)),
    Q(T2, 'Find the two-tailed p-value for z = 2, to 4 d.p.', ['0.0455', '0.0228', '0.9772', '0.3173'], 0, '2 × (1 − Φ(2)) = 2 × 0.0228 = 0.0455.', ans=2 * (1 - Phi(2)), num=True),
    Q(T2, 'In a test for a proportion, the standard error uses:', ['the hypothesised p₀', 'the sample p̂', 'the average of p₀ and p̂', '0.5 always'], 0, 'The test assumes H₀ is true, so it uses p₀.'),
    Q(T2, 'A 95% CI for μ is (48.2, 55.8). A two-tailed 5% test of H₀: μ = 50 would:', ['not reject H₀', 'reject H₀', 'need more data to decide', 'reject H₁'], 0, '50 lies inside the interval, so it is a plausible value and H₀ is not rejected.'),
    # T3
    Q(T3, 'A table has row totals 60 and 40, column totals 70 and 30, and a grand total of 100. What is the expected count for row 1, column 1?', ['42', '60', '70', '35'], 0, '60 × 70 / 100 = 42.', ans=R(60 * 70, 100)),
    Q(T3, 'How many degrees of freedom does a 3 × 4 contingency table have?', ['6', '12', '7', '5'], 0, '(3 − 1)(4 − 1) = 6.', ans=6),
    Q(T3, 'Observed [[30, 20], [20, 30]] with every expected count 25. What is χ²?', ['4', '2', '1', '20'], 0, 'Each cell contributes 25/25 = 1, and there are 4 cells.', ans=chi_stat),
    Q(T3, 'The 5% critical value of χ² with 1 degree of freedom is:', ['3.841', '1.960', '5.991', '6.635'], 0, 'From the chi-square table (or calculator).', ans=chi(1, 0.95), num=True),
    Q(T3, 'Which condition must hold for the chi-square test?', ['Every expected count is at least 5', 'Every observed count is at least 5', 'The data are percentages', 'The variables are numerical'], 0, 'The approximation needs adequate expected counts.'),
    Q(T3, 'The null hypothesis of a chi-square test of independence is:', ['the two variables are independent', 'the two variables are associated', 'all cells are equal', 'the means are equal'], 0, 'H₀ is always "no association".'),
    # T4
    Q(T4, 'For (1, 2), (2, 4), (3, 5), (4, 4), (5, 5), what is the least-squares slope?', ['0.6', '1', '2.2', '0.775'], 0, 'b = Sxy/Sxx = 6/10 = 0.6.', ans=b),
    Q(T4, 'For the same data, what is the intercept a?', ['2.2', '4', '0.6', '3'], 0, 'a = ȳ − b x̄ = 4 − 0.6 × 3 = 2.2.', ans=a),
    Q(T4, 'For the same data, what is r to 3 d.p.?', ['0.775', '0.600', '0.360', '1.000'], 0, 'r = 6/√60 ≈ 0.775.', ans=r, num=True),
    Q(T4, 'r = 0.8. What proportion of the variation in y is explained by x?', ['0.64', '0.8', '0.89', '0.2'], 0, 'r² = 0.8² = 0.64, so 64%.', ans=R(64, 100)),
    Q(T4, 'Ice-cream sales and drowning deaths are positively correlated. The best explanation is:', ['a lurking variable such as hot weather', 'ice cream causes drowning', 'drowning causes ice-cream sales', 'the correlation must be an error'], 0, 'Hot weather increases both. Correlation alone does not show causation.'),
    Q(T4, 'Using ŷ = 2.2 + 0.6x, which prediction is least reliable if the data had x from 1 to 5?', ['x = 20', 'x = 2.5', 'x = 4', 'x = 3'], 0, 'x = 20 is far outside the data range, so it is extrapolation.'),
]

FLASH = [
    ['p-value', 'P(data at least this extreme | H₀ true). Small p: evidence against H₀.'],
    ['Type I error', 'Rejecting a true H₀; probability α.'],
    ['Type II error', 'Failing to reject a false H₀.'],
    ['One-sample t statistic', 't = (x̄ − μ₀)/(s/√n), df = n − 1.'],
    ['Expected count (chi-square)', 'Row total × column total ÷ grand total.'],
    ['Chi-square degrees of freedom', '(r − 1)(c − 1).'],
    ['Least-squares line', 'b = Sxy/Sxx, a = ȳ − b x̄; passes through (x̄, ȳ).'],
    ['r²', 'Proportion of the variation in y explained by the line.'],
]
