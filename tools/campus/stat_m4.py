"""Probability and Statistics, module 4: The normal distribution, sampling and confidence intervals."""
from math import erf, sqrt, ceil
import mpmath as mp
from verify import Q, sp
T1, T2, T3, T4 = ('The normal distribution and z-scores', 'Sampling distributions and the Central Limit Theorem', 'Confidence intervals for a mean', 'Confidence intervals for a proportion')
R = sp.Rational


def Phi(z): return 0.5 * (1 + erf(z / sqrt(2)))


def zq(p): return float(mp.findroot(lambda z: 0.5 * (1 + mp.erf(z / mp.sqrt(2))) - p, 0))


def tq(df, p): return float(mp.findroot(lambda t: mp.betainc(df / 2, 0.5, 0, df / (df + t * t), regularized=True) / 2 - (1 - p), 2))


# checked numbers
assert round(Phi(1.25), 4) == 0.8944 and round(Phi(1.25) - Phi(-1.25), 4) == 0.7887 and round(1 - Phi(1.5), 4) == 0.0668
assert round(zq(0.9), 3) == 1.282 and round(zq(0.975), 2) == 1.96 and round(zq(0.95), 3) == 1.645 and round(zq(0.995), 3) == 2.576
assert round(170 + 8 * zq(0.9), 1) == 180.3
assert round(tq(15, 0.975), 3) == 2.131 and round(tq(9, 0.975), 3) == 2.262 and round(tq(24, 0.975), 3) == 2.064
pse = sqrt(0.3 * 0.7 / 400)
assert round(1.96 * pse, 4) == 0.0449 and ceil((1.96 / 0.03) ** 2 * 0.25) == 1068

MODULE = {
    'title': 'Normal distribution, sampling and confidence intervals',
    'topics': [T1, T2, T3, T4],
    'overview': 'The normal distribution is the most important model in statistics, because sample means behave normally even when the data do not. This module moves from z-scores to sampling distributions and the Central Limit Theorem, and then to confidence intervals: ranges that capture a population mean or proportion with a stated level of confidence.',
    'key_terms': ['Normal distribution', 'z-score', 'Standard error', 'Central Limit Theorem', 'Confidence interval', 'Margin of error', 't distribution', 'Degrees of freedom'],
    'explanation': [
        'Any normal distribution can be converted to the standard normal Z ~ N(0, 1) with z = (x − μ)/σ, so one table (or one calculator function) covers them all. The 68–95–99.7 rule gives quick estimates: about 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean.',
        'A statistic such as x̄ varies from sample to sample. Its distribution is the sampling distribution, and its standard deviation is called the standard error. The Central Limit Theorem says that for large enough n, x̄ is approximately normal with mean μ and standard error σ/√n, whatever the shape of the population.',
        'A confidence interval is estimate ± margin of error, where the margin is a critical value times the standard error. The confidence level describes the method: 95% of intervals built this way would capture the true parameter.'],
    'quick_facts': [
        'z = (x − μ)/σ.',
        '68–95–99.7 rule for 1, 2, 3 standard deviations.',
        'SE of x̄ = σ/√n; SE of p̂ = √(p̂(1 − p̂)/n).',
        'Critical z: 90% → 1.645, 95% → 1.96, 99% → 2.576.',
        'Unknown σ: use s and t with n − 1 degrees of freedom.'],
}

NOTES = {
    T1: {
        'overview': 'The normal distribution is the symmetric bell curve described by its mean μ and standard deviation σ. Converting values to z-scores lets you find any normal probability, or work backwards from a probability to a value.',
        'key_terms': ['Normal distribution', 'Standard normal', 'z-score', 'Φ(z)', 'Inverse normal', '68–95–99.7 rule'],
        'explanation': [
            'X ~ N(μ, σ²) is symmetric about μ, and σ sets the width. Many measurements (heights, measurement errors, test scores on large exams) are close to normal. The total area under the curve is 1, and areas are probabilities.',
            'The z-score z = (x − μ)/σ counts how many standard deviations x lies from the mean. Then P(X < x) = Φ(z), where Φ is the standard normal cumulative probability from tables or a calculator. Use symmetry and 1 − Φ for areas to the right: P(Z > z) = 1 − Φ(z) and Φ(−z) = 1 − Φ(z).',
            'Inverse problems run the other way: given a probability, find z from the table, then convert back with x = μ + zσ. For example, the top 10% starts at z ≈ 1.282.'],
        'formulas_label': 'Formulas',
        'formulas': ['z = (x − μ)/σ', 'P(X < x) = Φ(z)', 'P(Z > z) = 1 − Φ(z), and Φ(−z) = 1 − Φ(z)', 'x = μ + zσ', 'About 68%, 95%, 99.7% within 1, 2, 3σ'],
        'steps': ['Sketch the curve and shade the area you need.', 'Convert each x to z.', 'Use Φ, with symmetry or the complement as needed.', 'For inverse problems, find z first, then x = μ + zσ.', 'Check the answer against your sketch.'],
        'worked_example': {
            'problem': 'Heights of adult men in a city are N(170, 8²) in cm. Find the proportion between 160 cm and 180 cm, and the height that marks the tallest 10%.',
            'steps': ['z for 180: (180 − 170)/8 = 1.25; z for 160: −1.25.', 'P(−1.25 < Z < 1.25) = Φ(1.25) − Φ(−1.25) = 0.8944 − 0.1056 = 0.7887.', 'Tallest 10%: Φ(z) = 0.90 gives z ≈ 1.282, so x = 170 + 1.282 × 8 ≈ 180.3 cm.'],
            'answer': 'About 78.9% are between 160 and 180 cm; the tallest 10% are above about 180.3 cm.',
            'check': '±1.25σ should hold a little more than the 68% inside ±1σ, and 78.9% does.'},
        'mistakes': ['Dividing by the variance σ² instead of σ.', 'Forgetting to subtract from 1 for an area to the right.', 'Using a positive z for a value below the mean.', 'Answering an inverse question with z instead of converting back to x.'],
        'real_world': 'Clothing firms use the normal distribution of body measurements to decide how many of each size to produce, so few customers fall outside the range of sizes offered.',
        'exam_strategy': 'Always draw a quick bell curve with the mean marked and the region shaded. It catches nearly every left/right and plus/minus error.',
        'recap': ['z = (x − μ)/σ.', 'Left areas from Φ; right areas are 1 − Φ.', 'Inverse: z first, then x = μ + zσ.', '68–95–99.7 rule for quick checks.']},
    T2: {
        'overview': 'Different samples give different means. The sampling distribution of x̄ describes that variation, and the Central Limit Theorem explains why it is close to normal, which is what makes most of inferential statistics work.',
        'key_terms': ['Sampling distribution', 'Standard error', 'Central Limit Theorem', 'Sample size', 'Law of large numbers'],
        'explanation': [
            'If samples of size n are taken from a population with mean μ and standard deviation σ, the sample mean x̄ has mean μ (it is unbiased) and standard deviation σ/√n, called the standard error. Larger samples give less variable means, but precision grows only with √n: to halve the standard error you need four times the sample size.',
            'The Central Limit Theorem says that for large n (a common rule of thumb is n ≥ 30), x̄ is approximately N(μ, σ²/n) even if the population is skewed. If the population is itself normal, x̄ is exactly normal for any n.',
            'The same idea applies to proportions: the sample proportion p̂ has mean p and standard error √(p(1 − p)/n), and it is approximately normal when np and n(1 − p) are both at least about 10.'],
        'formulas_label': 'Formulas',
        'formulas': ['E(x̄) = μ', 'SE(x̄) = σ/√n', 'For large n: x̄ ≈ N(μ, σ²/n)', 'z = (x̄ − μ)/(σ/√n)', 'SE(p̂) = √(p(1 − p)/n)'],
        'steps': ['Identify μ, σ and n.', 'Compute the standard error σ/√n.', 'Justify normality (normal population or large n).', 'Convert x̄ to z using the standard error, not σ.'],
        'worked_example': {
            'problem': 'Daily spending by students has mean 50 and standard deviation 12 (in local currency units), and is right-skewed. For a random sample of 36 students, find P(x̄ > 53).',
            'steps': ['SE = 12/√36 = 2.', 'n = 36 is large, so by the CLT x̄ ≈ N(50, 2²) despite the skew.', 'z = (53 − 50)/2 = 1.5, so P(x̄ > 53) = 1 − Φ(1.5) = 1 − 0.9332 = 0.0668.'],
            'answer': 'P(x̄ > 53) ≈ 0.0668.',
            'check': 'A single student spending more than 53 is quite likely, but a whole sample averaging 3 above the mean is unusual, which is exactly what the small standard error says.'},
        'mistakes': ['Using σ instead of σ/√n when the question is about a mean.', 'Claiming the CLT makes the individual data normal. It is the sample mean that becomes normal.', 'Applying the CLT to very small samples from a skewed population.', 'Thinking doubling n halves the standard error.'],
        'real_world': 'Quality-control charts plot the mean of small samples taken every hour. Because sample means are close to normal, limits at 3 standard errors flag a process that has drifted.',
        'exam_strategy': 'Write "by the Central Limit Theorem, since n = … is large" when you use normality for a mean of non-normal data. That sentence is often a mark on its own.',
        'recap': ['x̄ is unbiased for μ.', 'SE = σ/√n.', 'CLT: x̄ ≈ normal for large n.', 'Four times the sample size halves the SE.']},
    T3: {
        'overview': 'A confidence interval for a mean gives a range of plausible values for μ, with a stated confidence level. Use z when σ is known and the t distribution when σ is estimated by s.',
        'key_terms': ['Point estimate', 'Margin of error', 'Confidence level', 'Critical value', 't distribution', 'Degrees of freedom'],
        'explanation': [
            'The interval is x̄ ± (critical value) × (standard error). With σ known it is x̄ ± z* σ/√n, where z* = 1.96 for 95%. Higher confidence or smaller samples give wider intervals.',
            'In practice σ is usually unknown and we use s. Estimating σ adds uncertainty, so the critical value comes from the t distribution with n − 1 degrees of freedom. The t curve has heavier tails than the normal and approaches it as n grows: t* for 95% is 2.262 with 9 degrees of freedom, 2.064 with 24, and close to 1.96 for large samples.',
            'Interpretation matters. "We are 95% confident that μ lies between 68.1 and 75.9" means the method captures μ in 95% of samples. It does not mean there is a 95% probability that this particular fixed interval contains μ, and it says nothing about where 95% of individual values lie.'],
        'formulas_label': 'Formulas',
        'formulas': ['σ known: x̄ ± z* σ/√n', 'σ unknown: x̄ ± t*(n − 1) s/√n', 'z*: 1.645 (90%), 1.96 (95%), 2.576 (99%)', 'Sample size for margin E: n = (z*σ/E)²'],
        'steps': ['Find x̄, n and σ or s.', 'Choose z* (σ known) or t* with n − 1 degrees of freedom (σ unknown).', 'Compute the standard error and the margin of error.', 'Write the interval and interpret it in context.'],
        'worked_example': {
            'problem': 'A random sample of 16 students sleeps a mean of 20 hours per weekend with s = 4. Find a 95% confidence interval for the mean.',
            'steps': ['σ is unknown, so use t with 15 degrees of freedom: t* = 2.131.', 'SE = 4/√16 = 1.', 'Margin = 2.131 × 1 = 2.131, so the interval is 20 ± 2.131.'],
            'answer': '95% CI: (17.869, 22.131) hours.',
            'check': 'A z interval would give 20 ± 1.96, slightly narrower. The t interval is wider because s itself is uncertain.'},
        'mistakes': ['Using z* when σ is unknown and n is small.', 'Using n instead of n − 1 degrees of freedom.', 'Interpreting the interval as covering 95% of individual values.', 'Forgetting to divide by √n.'],
        'real_world': 'Drug trials report a confidence interval for the average drop in blood pressure. Doctors look at whether the whole interval represents a worthwhile effect, not just at the single best estimate.',
        'exam_strategy': 'State the critical value with its degrees of freedom ("t₁₅ = 2.131"), show the standard error, and finish with a sentence in context. Each step usually earns a mark.',
        'recap': ['Interval = estimate ± critical value × SE.', 'σ known: z; σ unknown: t with n − 1 df.', 'More confidence: wider interval.', 'Interpret the method, not one fixed interval.']},
    T4: {
        'overview': 'Surveys report percentages with a "margin of error". That margin comes from the confidence interval for a population proportion, and the same formula tells you how many people to survey.',
        'key_terms': ['Sample proportion', 'Standard error of p̂', 'Margin of error', 'Success–failure condition', 'Sample size calculation'],
        'explanation': [
            'If x of n sampled individuals have a characteristic, p̂ = x/n estimates the population proportion p. Its standard error is √(p̂(1 − p̂)/n), and the interval is p̂ ± z* √(p̂(1 − p̂)/n).',
            'The normal approximation needs enough successes and failures: n p̂ and n(1 − p̂) should both be at least about 10. The sample should also be random, and smaller than about 10% of the population.',
            'To plan a survey with margin of error E, solve n = (z*/E)² p(1 − p). If you have no estimate of p, use p = 0.5, which gives the largest (safest) n. Always round up. A ±3% margin at 95% confidence needs about 1068 people, which is why national polls often survey around 1000 to 1100.'],
        'formulas_label': 'Formulas',
        'formulas': ['p̂ = x/n', 'SE = √(p̂(1 − p̂)/n)', 'CI: p̂ ± z* √(p̂(1 − p̂)/n)', 'Sample size: n = (z*/E)² p(1 − p), rounded up', 'Check: np̂ ≥ 10 and n(1 − p̂) ≥ 10'],
        'steps': ['Compute p̂ = x/n.', 'Check the success–failure condition.', 'Compute the SE and the margin z* × SE.', 'Write p̂ ± margin and interpret it in context.'],
        'worked_example': {
            'problem': 'In a random sample of 400 students, 120 say they work part-time. Find a 95% confidence interval for the proportion of all students who work part-time.',
            'steps': ['p̂ = 120/400 = 0.30. Check: 120 ≥ 10 and 280 ≥ 10 ✓.', 'SE = √(0.3 × 0.7 / 400) = √0.000525 ≈ 0.0229.', 'Margin = 1.96 × 0.0229 ≈ 0.0449.'],
            'answer': '95% CI: 0.30 ± 0.045, about (0.255, 0.345), so between roughly 25.5% and 34.5%.',
            'check': 'The margin of about 4.5 percentage points is in line with ±1/√n = ±0.05, a quick rule of thumb for 95% intervals.'},
        'mistakes': ['Using p̂ = x rather than x/n.', 'Forgetting the square root in the SE.', 'Rounding a sample size down.', 'Saying the margin of error covers bias from a poor sample. It only covers random sampling variation.'],
        'real_world': 'Opinion polls quoting "±3 percentage points" are reporting this margin. When two parties are 2 points apart and the margin is 3, the poll cannot say who is ahead.',
        'exam_strategy': 'Show p̂, the condition check, the SE and the margin separately. Give the final interval both as decimals and in a sentence about the population.',
        'recap': ['p̂ = x/n; SE = √(p̂(1 − p̂)/n).', 'Need np̂ and n(1 − p̂) ≥ 10.', 'n = (z*/E)² p(1 − p); use 0.5 if unknown; round up.', 'The margin covers sampling error only.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'X ~ N(170, 8²). Find P(X < 180) to 4 d.p.', ['0.8944', '0.7887', '0.1056', '0.9332'], 0, 'z = 1.25 and Φ(1.25) = 0.8944.', ans=Phi(1.25), num=True),
    Q(T1, 'A score of 85 on a test with mean 70 and SD 10 has z =', ['1.5', '15', '0.15', '−1.5'], 0, '(85 − 70)/10 = 1.5.', ans=R(3, 2)),
    Q(T1, 'About what percentage of a normal distribution lies within 2 standard deviations of the mean?', ['95%', '68%', '99.7%', '50%'], 0, 'This is the middle part of the 68–95–99.7 rule.'),
    Q(T1, 'Z ~ N(0, 1). Find P(Z > 1.5) to 4 d.p.', ['0.0668', '0.9332', '0.1336', '0.4332'], 0, '1 − Φ(1.5) = 1 − 0.9332 = 0.0668.', ans=1 - Phi(1.5), num=True),
    Q(T1, 'X ~ N(170, 8²). Which height marks the tallest 10%, to 1 d.p.?', ['180.3', '178.0', '183.2', '172.6'], 0, 'z = 1.282, so 170 + 1.282 × 8 ≈ 180.3.', ans=R(round(10 * (170 + 8 * zq(0.9))), 10)),
    Q(T1, 'Exam marks are N(60, 12²). Find P(48 < X < 72) to 4 d.p.', ['0.6827', '0.9545', '0.8413', '0.3413'], 0, 'z = ±1, so Φ(1) − Φ(−1) ≈ 0.6827.', ans=Phi(1) - Phi(-1), num=True),
    # T2
    Q(T2, 'A population has σ = 12. What is the standard error of x̄ for n = 36?', ['2', '12', '0.33', '6'], 0, 'σ/√n = 12/6 = 2.', ans=2),
    Q(T2, 'μ = 50, σ = 12, n = 36. Find P(x̄ > 53) to 4 d.p.', ['0.0668', '0.4013', '0.9332', '0.1587'], 0, 'z = (53 − 50)/2 = 1.5, and 1 − Φ(1.5) = 0.0668.', ans=1 - Phi(1.5), num=True),
    Q(T2, 'The Central Limit Theorem says that for large n:', ['the sample mean is approximately normal', 'the population becomes normal', 'every sample is normal', 'the standard deviation equals the mean'], 0, 'It is the sampling distribution of x̄ that becomes approximately normal.'),
    Q(T2, 'By what factor must n increase to halve the standard error of x̄?', ['4', '2', '√2', '8'], 0, 'SE = σ/√n, so halving it needs √n to double, which means n × 4.', ans=4),
    Q(T2, 'p = 0.4 and n = 150. What is the standard error of p̂ to 3 d.p.?', ['0.040', '0.016', '0.024', '0.400'], 0, '√(0.4 × 0.6 / 150) = √0.0016 = 0.04.', ans=sp.sqrt(R(24, 100) / 150), num=True),
    Q(T2, 'The mean of the sampling distribution of x̄ equals:', ['μ', 'σ/√n', 'x̄ of the first sample', 'σ'], 0, 'x̄ is an unbiased estimator of μ.'),
    # T3
    Q(T3, 'x̄ = 72, σ = 10 and n = 25. What is the 95% confidence interval for μ?', ['(68.08, 75.92)', '(70.04, 73.96)', '(52.4, 91.6)', '(67.5, 76.5)'], 0, 'SE = 10/5 = 2; 72 ± 1.96 × 2 = 72 ± 3.92.'),
    Q(T3, 'What is the critical value t* for a 95% interval with n = 16?', ['2.131', '1.96', '2.120', '1.753'], 0, 'Degrees of freedom = 15, and t₁₅ for 95% (0.025 in each tail) is 2.131.', ans=tq(15, 0.975), num=True),
    Q(T3, 'x̄ = 20, s = 4 and n = 16. What is the margin of error for 95% confidence, to 3 d.p.?', ['2.131', '1.960', '8.524', '0.533'], 0, 'SE = 4/4 = 1, so the margin is 2.131 × 1.', ans=tq(15, 0.975), num=True),
    Q(T3, 'Which change makes a confidence interval narrower?', ['A larger sample size', 'A higher confidence level', 'A larger standard deviation', 'Using t instead of z'], 0, 'A larger n reduces σ/√n.'),
    Q(T3, 'Which is the correct interpretation of a 95% CI of (68.1, 75.9) for a mean?', ['We are 95% confident the population mean lies between 68.1 and 75.9', '95% of individuals score between 68.1 and 75.9', 'The sample mean is between 68.1 and 75.9 with probability 0.95', '95% of sample means lie in this interval'], 0, 'Confidence is about the population mean, through the long-run success rate of the method.'),
    Q(T3, 'How large a sample gives a 95% margin of error of 2 when σ = 10?', ['97', '96', '10', '49'], 0, 'n = (1.96 × 10 / 2)² = 96.04, rounded up to 97.', ans=ceil((1.96 * 10 / 2) ** 2)),
    # T4
    Q(T4, '120 of 400 sampled students work part-time. What is the 95% margin of error to 3 d.p.?', ['0.045', '0.023', '0.030', '0.090'], 0, 'SE = √(0.3 × 0.7/400) ≈ 0.0229, and 1.96 × 0.0229 ≈ 0.045.', ans=1.96 * pse, num=True),
    Q(T4, 'What sample size gives a 95% margin of error of 0.03 with p unknown?', ['1068', '1067', '33', '544'], 0, '(1.96/0.03)² × 0.25 = 1067.1, rounded up to 1068.', ans=ceil((1.96 / 0.03) ** 2 * 0.25)),
    Q(T4, 'Why use p = 0.5 when planning a survey with no prior estimate?', ['p(1 − p) is largest at 0.5, so n is safely large', 'Most proportions are 0.5', 'It makes the interval narrower', 'It removes bias'], 0, 'p(1 − p) peaks at 0.25 when p = 0.5, giving the largest required sample.'),
    Q(T4, 'In a sample of 50, 3 people said yes. Why is the normal interval for p questionable?', ['There are fewer than 10 successes', 'The sample is too large', 'p̂ is above 0.5', 'The SE is zero'], 0, 'n p̂ = 3 < 10, so the normal approximation is poor.'),
    Q(T4, 'A poll reports 52% ± 3%. Which conclusion is justified?', ['The true proportion is plausibly anywhere from 49% to 55%', 'A clear majority definitely supports the policy', 'Exactly 52% of the population agree', 'The poll is biased'], 0, 'The interval includes values below 50%, so a majority is not established.'),
    Q(T4, 'p̂ = 0.6 and n = 600. What is the standard error to 3 d.p.?', ['0.020', '0.040', '0.010', '0.001'], 0, '√(0.6 × 0.4 / 600) = √0.0004 = 0.02.', ans=sp.sqrt(R(24, 100) / 600), num=True),
]

FLASH = [
    ['z-score', 'z = (x − μ)/σ: standard deviations from the mean.'],
    ['68–95–99.7 rule', 'Share of a normal distribution within 1, 2 and 3 SDs of the mean.'],
    ['Standard error of x̄', 'σ/√n.'],
    ['Central Limit Theorem', 'For large n, x̄ is approximately normal whatever the population shape.'],
    ['Critical z values', '90%: 1.645; 95%: 1.96; 99%: 2.576.'],
    ['When to use t', 'σ unknown: use s and t with n − 1 degrees of freedom.'],
    ['CI for a proportion', 'p̂ ± z* √(p̂(1 − p̂)/n).'],
    ['Sample size for a proportion', 'n = (z*/E)² p(1 − p); use p = 0.5 if unknown, round up.'],
]
