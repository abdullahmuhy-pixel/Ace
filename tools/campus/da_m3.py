"""Introduction to Data Analysis, module 3: Sampling and statistical inference."""
import math
from scipy import stats
from verify import Q
T1, T2, T3, T4 = ('Sampling and bias', 'The normal distribution and the central limit theorem', 'Confidence intervals', 'Hypothesis tests and p-values')
r = lambda v, d: round(v + 0.0, d)
assert (0.6 * 500, 0.4 * 500) == (300, 200) and r(420 / 1200, 2) == 0.35 and 1 / math.sqrt(400) == 0.05
assert r(stats.norm.cdf(1.96), 3) == 0.975 and r(stats.norm.cdf(1) - stats.norm.cdf(-1), 3) == 0.683
assert r(1 - stats.norm.cdf(172, 165, 7), 4) == 0.1587 and r(stats.norm.cdf(179, 165, 7) - stats.norm.cdf(151, 165, 7), 3) == 0.954 and 12 / math.sqrt(36) == 2
assert (r(52 - 1.96 * 10 / math.sqrt(100), 2), r(52 + 1.96 * 1, 2)) == (50.04, 53.96) and r(stats.t.ppf(0.975, 99), 2) == 1.98 and r(stats.t.ppf(0.975, 24), 3) == 2.064
se = math.sqrt(0.42 * 0.58 / 600)
assert r(se, 4) == 0.0201 and r(1.96 * se * 100, 1) == 3.9 and (r((0.42 - 1.96 * se) * 100, 1), r((0.42 + 1.96 * se) * 100, 1)) == (38.1, 45.9)
assert math.ceil((1.96 / 0.03) ** 2 * 0.25) == 1068
t = (32.4 - 30) / (5 / math.sqrt(25))
assert r(t, 2) == 2.4 and r(2 * (1 - stats.t.cdf(t, 24)), 3) == 0.025 and r(stats.norm.ppf(0.95), 3) == 1.645

MODULE = {
    'title': 'Sampling and statistical inference',
    'topics': [T1, T2, T3, T4],
    'overview': 'Analysts rarely see a whole population, so they learn about it from samples. This module covers how to sample without bias, the normal distribution and the central limit theorem that make inference possible, confidence intervals for means and proportions, and hypothesis tests with p-values.',
    'key_terms': ['Population', 'Sample', 'Simple random sample', 'Stratified sample', 'Bias', 'Normal distribution', 'Standard normal', 'Central limit theorem', 'Standard error', 'Confidence interval', 'Margin of error', 'Null hypothesis', 'p-value', 'Significance level', 'Type I and II errors'],
    'explanation': [
        'A sample is useful only if it represents the population. Random selection protects against bias; convenience samples, self-selected online polls and high non-response can mislead badly no matter how large they are.',
        'Many measurements are roughly normal, and, by the central limit theorem, sample means are approximately normal for large enough samples even when the data are skewed. The spread of a sample mean is its standard error, σ/√n, which shrinks as the sample grows.',
        'A 95% confidence interval, estimate ± about 2 standard errors, gives a range of plausible values for a population quantity. A hypothesis test asks whether data are surprising under a null hypothesis: a small p-value is evidence against it, though it does not measure the size or importance of an effect.'],
    'quick_facts': [
        'Random sampling avoids selection bias; bigger samples do not cure bias.',
        'Normal: 68% within 1 SD, 95% within 1.96 SD.',
        'SE of mean = σ/√n; SE of proportion = √(p(1 − p)/n).',
        '95% CI ≈ estimate ± 1.96 SE (t for small samples).',
        'p < α → reject H₀; a p-value is not P(H₀ is true).'],
}

NOTES = {
    T1: {
        'overview': 'How data are collected decides what they can tell you. A biased sample gives a confident but wrong answer.',
        'key_terms': ['Population', 'Sampling frame', 'Simple random sample', 'Stratified sample', 'Cluster sample', 'Convenience sample', 'Selection bias', 'Non-response bias', 'Survivorship bias'],
        'explanation': [
            'The population is everyone (or everything) you want to know about; the sampling frame is the list you can actually sample from. In a simple random sample every member has an equal chance. A stratified sample samples separately within groups: if 60% of a province\'s households are urban and 40% rural, a stratified sample of 500 takes 300 urban and 200 rural households. Cluster samples pick whole groups (villages, schools) to save travel.',
            'Bias is systematic error. Selection bias: the frame or method misses people (a phone survey misses households without phones). Non-response bias: if only 420 of 1200 invited people reply (35%), the responders may differ from the rest. Survivorship bias: studying only firms that survived hides the ones that failed.',
            'Size reduces random error, not bias: the margin of error for a proportion is roughly 1/√n, about 5% for n = 400, but a huge biased sample is still wrong. Famous election polls have failed this way.'],
        'formulas_label': 'Formulas',
        'formulas': ['Stratum sample = total sample × stratum share', 'Response rate = responses/invited', 'Rough margin of error ≈ 1/√n'],
        'steps': ['Define the population.', 'Check the sampling frame covers it.', 'Choose a random design (simple, stratified, cluster).', 'Plan to maximise response and record who was missed.'],
        'worked_example': {
            'problem': 'A survey of 500 households should reflect a province that is 60% urban and 40% rural. How should the sample be allocated?',
            'steps': ['Use proportional stratified sampling.', 'Urban: 0.60 × 500 = 300.', 'Rural: 0.40 × 500 = 200.'],
            'answer': '300 urban and 200 rural households, each chosen at random within its stratum.',
            'check': '300 + 200 = 500 ✓.'},
        'mistakes': ['Thinking a big sample cannot be biased.', 'Using volunteers and calling it random.', 'Ignoring who did not respond.', 'Confusing stratified (sample within every group) with cluster (sample some groups).'],
        'real_world': 'National household surveys use stratified cluster designs so that every province and both urban and rural areas are represented.',
        'exam_strategy': 'For any study, ask who could not have been selected and who chose not to answer.',
        'recap': ['Population vs frame.', 'Random designs.', 'Types of bias.', 'Size does not fix bias.']},
    T2: {
        'overview': 'The normal distribution and the central limit theorem explain why sample averages behave predictably.',
        'key_terms': ['Normal distribution', 'Standard normal (Z)', 'z-table', 'Sampling distribution', 'Central limit theorem', 'Standard error'],
        'explanation': [
            'A normal distribution is symmetric and bell-shaped, fixed by its mean μ and SD σ. Convert to the standard normal with z = (x − μ)/σ. If adult heights have μ = 165 cm and σ = 7 cm, a height of 172 cm has z = 1 and P(X > 172) ≈ 0.159; about 95.4% of heights lie between 151 and 179 cm (within 2 SDs). P(Z < 1.96) = 0.975, so 95% lies within ±1.96 SD.',
            'The sampling distribution of the mean describes how x̄ varies from sample to sample. Its centre is μ and its SD, the standard error, is σ/√n: with σ = 12 and n = 36, SE = 2. Quadrupling n halves the SE.',
            'Central limit theorem: for reasonably large n (often 30 or more), x̄ is approximately normal whatever the shape of the population. That is why intervals and tests for means work even for skewed data such as incomes, provided the sample is large and random.'],
        'formulas_label': 'Formulas',
        'formulas': ['z = (x − μ)/σ', 'P(−1 < Z < 1) ≈ 0.683; P(−1.96 < Z < 1.96) = 0.95', 'SE(x̄) = σ/√n', 'x̄ ≈ Normal(μ, σ/√n) for large n'],
        'steps': ['Standardise with z.', 'Use a table or software for probabilities.', 'For sample means, use SE = σ/√n instead of σ.', 'Check the CLT conditions (random, large enough n).'],
        'worked_example': {
            'problem': 'Heights are normal with mean 165 cm and SD 7 cm. What proportion are taller than 172 cm?',
            'steps': ['z = (172 − 165)/7 = 1.', 'P(Z > 1) = 1 − 0.8413.', '= 0.1587.'],
            'answer': 'About 15.9%.',
            'check': 'Half of the 31.7% outside ±1 SD lies above, 15.9% ✓.'},
        'mistakes': ['Using σ instead of σ/√n for sample means.', 'Thinking the CLT makes the data themselves normal.', 'Forgetting to subtract from 1 for "greater than".', 'Applying normal results to small, very skewed samples.'],
        'real_world': 'Factories set quality-control limits on average weights of packets using the standard error of sample means.',
        'exam_strategy': 'Write "X" or "x̄" clearly: questions about one value use σ; questions about averages use σ/√n.',
        'recap': ['Bell curve.', 'z-scores.', 'SE = σ/√n.', 'CLT.']},
    T3: {
        'overview': 'A confidence interval gives a range of plausible values for a population mean or proportion, with a stated level of confidence.',
        'key_terms': ['Point estimate', 'Confidence level', 'Critical value', 't distribution', 'Degrees of freedom', 'Margin of error', 'Confidence interval for a proportion', 'Sample size planning'],
        'explanation': [
            'A 95% confidence interval for a mean: x̄ ± t* × s/√n, with t* from the t distribution with n − 1 degrees of freedom. For n = 100, x̄ = 52 and s = 10: SE = 1 and t* ≈ 1.98 (z* = 1.96 gives 50.04 to 53.96, nearly the same). For n = 25, t* ≈ 2.064 is noticeably bigger than 1.96.',
            'For a proportion: p̂ ± 1.96√(p̂(1 − p̂)/n). If 42% of 600 surveyed customers prefer a new product, SE ≈ 0.0201, the margin of error is about 3.9 points and the interval is 38.1% to 45.9%.',
            'Interpretation: the method captures the true value in 95% of samples; it does not mean a 95% probability for this particular interval. To plan a survey with a 3-point margin of error at 95%, n = (1.96/0.03)² × 0.25 ≈ 1067.1, so 1068 respondents (using p = 0.5, the worst case).'],
        'formulas_label': 'Formulas',
        'formulas': ['Mean: x̄ ± t* s/√n', 'Proportion: p̂ ± z*√(p̂(1 − p̂)/n)', 'z* = 1.96 for 95%, 1.645 for 90%', 'n = (z*/E)² p(1 − p)'],
        'steps': ['Compute the estimate.', 'Compute the standard error.', 'Choose the critical value (t* or z*).', 'Form estimate ± margin and interpret in context.'],
        'worked_example': {
            'problem': 'In a survey, 252 of 600 customers (42%) prefer a new product. Find a 95% confidence interval.',
            'steps': ['SE = √(0.42 × 0.58/600) ≈ 0.0201.', 'Margin = 1.96 × 0.0201 ≈ 0.039.', 'Interval: 0.42 ± 0.039 = 0.381 to 0.459.'],
            'answer': 'About 38.1% to 45.9%.',
            'check': 'The whole interval is below 50%, so a majority preference is not plausible ✓.'},
        'mistakes': ['Saying there is a 95% chance the true value is in this interval.', 'Using z* for small samples when σ is unknown.', 'Forgetting to round sample sizes up.', 'Ignoring bias: intervals only cover random error.'],
        'real_world': 'Polls reported "plus or minus 3 percentage points" are quoting a 95% margin of error from roughly 1000 respondents.',
        'exam_strategy': 'Always end with a sentence in context: "We are 95% confident the mean delivery time is between …".',
        'recap': ['Estimate ± margin.', 't for means, z for proportions.', 'Interpret the method.', 'Plan n from E.']},
    T4: {
        'overview': 'A hypothesis test asks whether the data are too surprising to be explained by chance under a default assumption.',
        'key_terms': ['Null hypothesis H₀', 'Alternative hypothesis H₁', 'Test statistic', 'p-value', 'Significance level α', 'One- and two-sided tests', 'Type I error', 'Type II error', 'Power', 'Statistical vs practical significance'],
        'explanation': [
            'A courier claims a mean delivery time of 30 minutes. A random sample of 25 deliveries has x̄ = 32.4 and s = 5. H₀: μ = 30; H₁: μ ≠ 30. t = (32.4 − 30)/(5/√25) = 2.4 with 24 degrees of freedom; the two-sided p-value is about 0.025.',
            'The p-value is the probability, if H₀ were true, of a result at least this extreme. At α = 0.05, p = 0.025 < 0.05, so reject H₀: the data suggest deliveries take longer than claimed. The p-value is not the probability that H₀ is true.',
            'Errors: a Type I error rejects a true H₀ (probability α); a Type II error fails to reject a false H₀; power = 1 − P(Type II) grows with sample size and effect size. With huge samples, trivial differences become "significant", so always report the effect size and a confidence interval as well.'],
        'formulas_label': 'Formulas',
        'formulas': ['t = (x̄ − μ₀)/(s/√n), df = n − 1', 'Reject H₀ if p < α', 'P(Type I) = α; power = 1 − β', 'One-sided 5% z cut-off = 1.645'],
        'steps': ['State H₀ and H₁ in context.', 'Check conditions (random, roughly normal or large n).', 'Compute the test statistic and p-value.', 'Decide and conclude in context, with an effect size.'],
        'worked_example': {
            'problem': 'Test the claim μ = 30 minutes using n = 25, x̄ = 32.4, s = 5, at α = 0.05.',
            'steps': ['SE = 5/√25 = 1; t = 2.4/1 = 2.4.', 'df = 24; two-sided p ≈ 0.025.', '0.025 < 0.05, so reject H₀.'],
            'answer': 'Reject the claim: the mean delivery time appears to exceed 30 minutes (by about 2.4 minutes).',
            'check': 'The 95% CI, 32.4 ± 2.064 × 1 = 30.3 to 34.5, excludes 30, consistent with the test ✓.'},
        'mistakes': ['Saying "accept H₀" instead of "fail to reject".', 'Reading p as the probability H₀ is true.', 'Choosing a one-sided test after seeing the data.', 'Equating significance with importance.'],
        'real_world': 'Regulators require drug trials to pre-register their hypotheses and α so that results cannot be cherry-picked afterwards.',
        'exam_strategy': 'Write the conclusion in context and include the p-value, the decision and the direction of the effect.',
        'recap': ['H₀ vs H₁.', 'p-value meaning.', 'Type I and II errors.', 'Report effect sizes.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A province is 60% urban. A proportional stratified sample of 500 includes how many urban households?', ['300', '200', '250', '60'], 0, '0.6 × 500.', ans=300, num=True),
    Q(T1, '420 of 1200 invited people respond. The response rate is:', ['35%', '42%', '65%', '28.6%'], 0, '420/1200.'),
    Q(T1, 'An online poll that anyone can join mainly suffers from:', ['self-selection bias', 'too small a sample', 'measurement error only', 'no bias'], 0, 'Volunteers differ.'),
    Q(T1, 'Increasing the size of a biased sample:', ['does not remove the bias', 'removes the bias', 'always increases bias', 'makes it random'], 0, 'Only random error shrinks.'),
    Q(T1, 'The rough margin of error for a proportion with n = 400 is:', ['5%', '2.5%', '20%', '0.25%'], 0, '1/√400.'),
    Q(T1, 'Studying only companies still trading today illustrates:', ['survivorship bias', 'non-response bias', 'stratification', 'cluster sampling'], 0, 'Failures are missing.'),
    # T2
    Q(T2, 'Heights ~ Normal(165, 7). P(height > 172) is about:', ['0.159', '0.341', '0.841', '0.05'], 0, 'z = 1.'),
    Q(T2, 'About what proportion of a normal distribution lies within ±1.96 SD?', ['95%', '68%', '99.7%', '90%'], 0, 'Definition of 1.96.'),
    Q(T2, 'With σ = 12 and n = 36, the standard error of the mean is:', ['2', '12', '0.33', '6'], 0, '12/6.', ans=2, num=True),
    Q(T2, 'Quadrupling the sample size makes the standard error:', ['half as large', 'a quarter as large', 'twice as large', 'unchanged'], 0, '√4 = 2.'),
    Q(T2, 'The central limit theorem says that for large random samples:', ['the sample mean is approximately normal', 'the data become normal', 'the SD becomes zero', 'bias disappears'], 0, 'About x̄.'),
    Q(T2, 'P(Z < 1.96) is about:', ['0.975', '0.95', '0.025', '0.5'], 0, 'One tail 2.5%.'),
    # T3
    Q(T3, 'n = 100, x̄ = 52, s = 10. Using 1.96, the 95% CI is:', ['50.04 to 53.96', '42.2 to 61.8', '51.0 to 53.0', '48.0 to 56.0'], 0, '52 ± 1.96 × 1.'),
    Q(T3, '42% of 600 customers prefer a product. The 95% margin of error is about:', ['3.9 percentage points', '2.0 points', '7.8 points', '0.4 points'], 0, '1.96 × 0.0201.'),
    Q(T3, 'The 95% CI for that proportion is about:', ['38.1% to 45.9%', '40% to 44%', '34.2% to 49.8%', '42% to 50%'], 0, '0.42 ± 0.039.'),
    Q(T3, 'For a 3-point margin of error at 95% (p = 0.5), you need about:', ['1068 respondents', '334', '600', '2500'], 0, '(1.96/0.03)² × 0.25.'),
    Q(T3, 'For n = 25, the 95% t critical value (df 24) is about:', ['2.064', '1.96', '1.645', '2.576'], 0, 't is wider than z.', ans=2.064, num=True),
    Q(T3, 'A correct interpretation of a 95% confidence interval is:', ['95% of intervals built this way contain the true value', 'there is a 95% chance this interval contains the value', '95% of the data lie in it', 'the sample mean is 95% accurate'], 0, 'Property of the method.'),
    # T4
    Q(T4, 'H₀: μ = 30, n = 25, x̄ = 32.4, s = 5. The t statistic is:', ['2.4', '0.48', '12', '2.064'], 0, '2.4/(5/5).', ans=2.4, num=True),
    Q(T4, 'Its two-sided p-value (df 24) is about 0.025. At α = 0.05 you:', ['reject H₀', 'fail to reject H₀', 'accept H₀', 'need a bigger α'], 0, 'p < α.'),
    Q(T4, 'A p-value is:', ['the probability of data this extreme if H₀ were true', 'the probability H₀ is true', 'the probability H₁ is true', 'the effect size'], 0, 'Conditional on H₀.'),
    Q(T4, 'Rejecting a true null hypothesis is a:', ['Type I error', 'Type II error', 'power failure', 'sampling bias'], 0, 'Probability α.'),
    Q(T4, 'Power increases when:', ['the sample size increases', 'α is made smaller', 'the effect is smaller', 'data are more variable'], 0, 'More information.'),
    Q(T4, 'With a very large sample, a tiny difference can be:', ['statistically significant but practically unimportant', 'never significant', 'always important', 'a Type II error'], 0, 'Report effect sizes.'),
]

FLASH = [
    ['Stratified sample', 'Random sample within each group, often proportional.'],
    ['Bias vs random error', 'Bigger samples shrink random error, not bias.'],
    ['Standard normal', '68% within ±1, 95% within ±1.96.'],
    ['Standard error', 'σ/√n for means; √(p(1 − p)/n) for proportions.'],
    ['Central limit theorem', 'Sample means are approximately normal for large n.'],
    ['95% CI', 'Estimate ± critical value × SE.'],
    ['p-value', 'P(data this extreme | H₀ true); small → evidence against H₀.'],
    ['Type I and II errors', 'Reject true H₀ (α); miss a false H₀ (β).'],
]
