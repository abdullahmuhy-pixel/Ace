"""Probability and Statistics, module 1: Describing data."""
import statistics as st
from verify import Q, sp
T1, T2, T3, T4 = ('Types of data and sampling', 'Measures of centre', 'Measures of spread', 'Shape, box plots and outliers')

# numbers used in the notes, checked here
WE2 = [12, 15, 15, 18, 20, 22]
assert st.mean(WE2) == 17 and st.median(WE2) == 16.5 and st.mode(WE2) == 15
WE3 = [2, 4, 4, 4, 5, 5, 7, 9]
assert st.mean(WE3) == 5 and st.pvariance(WE3) == 4 and st.pstdev(WE3) == 2
assert abs(st.variance(WE3) - 32 / 7) < 1e-12 and round(st.stdev(WE3), 3) == 2.138
WE4 = [3, 5, 7, 8, 9, 11, 13, 15, 40]
q1, q3 = st.median(WE4[:4]), st.median(WE4[5:])
assert (st.median(WE4), q1, q3) == (9, 6, 14) and q1 - 1.5 * (q3 - q1) == -6 and q3 + 1.5 * (q3 - q1) == 26

MODULE = {
    'title': 'Describing data',
    'topics': [T1, T2, T3, T4],
    'overview': 'Statistics starts by describing what you have before drawing conclusions from it. This module covers what kind of data you are holding, how it was collected, and the handful of numbers and pictures that summarise it: the centre, the spread, the shape and any unusual values.',
    'key_terms': ['Population', 'Sample', 'Categorical', 'Numerical', 'Mean', 'Median', 'Standard deviation', 'Interquartile range', 'Skew', 'Outlier'],
    'explanation': [
        'Every statistical question starts with two checks. What type is each variable (a category or a number)? And how were the data collected? A biased sample cannot be rescued by clever calculations later, so the sampling method matters as much as the arithmetic.',
        'A distribution is summarised by its centre (mean or median), its spread (standard deviation or interquartile range) and its shape (symmetric or skewed, one peak or several). The right summary depends on the shape: for skewed data and data with outliers, the median and IQR describe a typical value better than the mean and standard deviation.',
        'Always draw a picture before calculating. A histogram or box plot shows skew, gaps and outliers in seconds, and tells you which numbers are worth reporting.'],
    'quick_facts': [
        'Sample statistics estimate population parameters: x̄ estimates μ, s estimates σ.',
        'The median resists outliers; the mean does not.',
        'Sample variance divides by n − 1, population variance by N.',
        'IQR = Q3 − Q1 covers the middle 50% of the data.',
        'Outlier rule: below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR.'],
}

NOTES = {
    T1: {
        'overview': 'Data are values recorded about individuals (people, firms, plots of land). Before analysing them, you need to know what type each variable is and whether the individuals you have represent the group you care about.',
        'key_terms': ['Population', 'Sample', 'Parameter', 'Statistic', 'Categorical variable', 'Numerical variable', 'Simple random sample', 'Bias'],
        'explanation': [
            'The population is the whole group you want to learn about; the sample is the part you actually measure. A number that describes a population is a parameter (μ, σ, p) and the matching number from a sample is a statistic (x̄, s, p̂). Statistics vary from sample to sample; parameters are fixed but usually unknown.',
            'Categorical variables put individuals into groups (faculty, blood type, yes or no). Ordinal variables are categorical with a natural order (grade A to F, satisfaction 1 to 5). Numerical variables are counts or measurements: discrete if they come from counting (number of siblings) and continuous if they are measured (height, time).',
            'In a simple random sample every group of n individuals has the same chance of being chosen. Stratified sampling takes a random sample within each group (for example each faculty), and cluster sampling picks whole groups at random. Convenience samples and voluntary responses (only people who choose to reply) are usually biased: they systematically over- or under-represent part of the population.'],
        'formulas_label': 'Definitions',
        'formulas': ['Parameter (population): μ, σ, p', 'Statistic (sample): x̄, s, p̂', 'Discrete: counted; continuous: measured', 'Bias: a systematic error in one direction'],
        'steps': ['Name the population and the sample.', 'Classify each variable: categorical (nominal or ordinal) or numerical (discrete or continuous).', 'Identify the sampling method.', 'Ask who could be missing or over-represented, and in which direction that pushes the result.'],
        'worked_example': {
            'problem': 'A lecturer asks the 40 students who attend a Friday 8 a.m. lecture how many hours they study per week, and uses the average for all 300 students on the course. Identify the population, sample, variable type and the main problem.',
            'steps': ['Population: all 300 students on the course. Sample: the 40 who attend the Friday 8 a.m. lecture.', 'Variable: hours of study per week, a numerical (continuous) variable.', 'The sample is a convenience sample: students who come to an early Friday lecture are likely to be more committed than average.'],
            'answer': 'The estimate is probably biased upwards, because the most engaged students are over-represented.',
            'check': 'A simple random sample of 40 names from the full class list would remove this bias.'},
        'mistakes': ['Treating a large sample as automatically unbiased. A large biased sample is just precisely wrong.', 'Calling a numerical code (such as a student number) a numerical variable.', 'Confusing a statistic (from the sample) with a parameter (of the population).', 'Calling a stratified sample a cluster sample, or the reverse.'],
        'real_world': 'Election polls fail when their samples miss groups who vote differently, for example people without internet access in an online poll. Good pollsters stratify by region, age and sex so each group is represented in the right proportion.',
        'exam_strategy': 'When asked to criticise a study, name the specific group that is over- or under-represented and say which way that moves the result. "The sample is biased" alone rarely earns the mark.',
        'recap': ['Population vs sample; parameter vs statistic.', 'Categorical (nominal, ordinal) vs numerical (discrete, continuous).', 'Random sampling avoids bias; size does not.', 'Say who is missing and in which direction it pushes the result.']},
    T2: {
        'overview': 'A measure of centre gives one typical value for a set of data. The mean, median and mode answer slightly different questions, and choosing the right one depends on the shape of the data.',
        'key_terms': ['Mean', 'Median', 'Mode', 'Weighted mean', 'Resistant measure', 'Grouped data'],
        'explanation': [
            'The mean is the balance point of the data: add the values and divide by how many there are. It uses every value, which makes it efficient but sensitive to outliers. One very large salary can pull the mean income far above what most people earn.',
            'The median is the middle value once the data are in order. With n values it is the value in position (n + 1)/2, and when n is even it is the average of the two middle values. Because it depends only on order, the median is resistant to outliers. The mode is the most frequent value and is the only measure that works for categorical data.',
            'For a frequency table, multiply each value (or class midpoint, for grouped data) by its frequency, add, and divide by the total frequency. A weighted mean works the same way, with weights such as credit units instead of frequencies.'],
        'formulas_label': 'Formulas',
        'formulas': ['x̄ = Σx / n', 'Grouped or frequency data: x̄ = Σfx / Σf', 'Median position: (n + 1)/2 in ordered data', 'Weighted mean = Σwx / Σw'],
        'steps': ['Put the data in order.', 'Mean: add the values and divide by n.', 'Median: find position (n + 1)/2; average the two middle values if n is even.', 'Mode: the most frequent value.', 'Compare mean and median to judge skew.'],
        'worked_example': {
            'problem': 'Six test marks are 12, 15, 15, 18, 20 and 22. Find the mean, median and mode.',
            'steps': ['Sum = 12 + 15 + 15 + 18 + 20 + 22 = 102, so the mean = 102 / 6 = 17.', 'n = 6 is even, so the median is the average of the 3rd and 4th values: (15 + 18)/2 = 16.5.', '15 appears twice, more than any other value, so the mode is 15.'],
            'answer': 'Mean 17, median 16.5, mode 15.',
            'check': 'The mean (17) sits just above the median (16.5), consistent with the slightly longer upper tail (20, 22).'},
        'mistakes': ['Finding the median without first ordering the data.', 'Using position n/2 instead of (n + 1)/2.', 'Using class boundaries instead of midpoints for grouped data.', 'Reporting the mean for strongly skewed data such as incomes or house prices.'],
        'real_world': 'Governments report median household income rather than mean income, because a few very high earners lift the mean well above what a typical household receives.',
        'exam_strategy': 'If a question asks which average to use, link your choice to the data: "the median, because the data are right-skewed by one large value". The reason carries the mark.',
        'recap': ['Mean = Σx / n; uses every value.', 'Median = middle of ordered data; resistant.', 'Mode = most frequent; works for categories.', 'Skewed data or outliers: prefer the median.']},
    T3: {
        'overview': 'Two data sets can share a mean yet look completely different. Measures of spread (range, variance, standard deviation and interquartile range) describe how far values typically sit from the centre.',
        'key_terms': ['Range', 'Deviation', 'Variance', 'Standard deviation', 'Sample vs population', 'Coefficient of variation'],
        'explanation': [
            'The range (largest minus smallest) is quick but depends on just two values, so a single outlier can double it. The interquartile range (next topic) ignores the extremes and measures the spread of the middle half.',
            'The standard deviation measures a typical distance from the mean. Find each deviation x − x̄, square it so negatives do not cancel, average the squares (this is the variance) and take the square root to return to the original units. For a sample we divide by n − 1 instead of n. This makes s² an unbiased estimate of σ², because deviations measured from x̄ are slightly smaller on average than deviations from the true mean μ.',
            'The coefficient of variation CV = s / x̄ × 100% compares spread between data in different units or with very different means. A spread of 5 kg means a lot for newborns and very little for adult cattle.'],
        'formulas_label': 'Formulas',
        'formulas': ['Range = max − min', 'Population variance: σ² = Σ(x − μ)² / N', 'Sample variance: s² = Σ(x − x̄)² / (n − 1)', 'Shortcut: Σ(x − x̄)² = Σx² − (Σx)²/n', 'CV = s / x̄ × 100%'],
        'steps': ['Find the mean.', 'Subtract the mean from each value and square the result.', 'Add the squares.', 'Divide by n − 1 for a sample (or N for a whole population).', 'Take the square root for the standard deviation.'],
        'worked_example': {
            'problem': 'For the data 2, 4, 4, 4, 5, 5, 7, 9, find the population standard deviation and the sample standard deviation.',
            'steps': ['Mean = 40 / 8 = 5.', 'Squared deviations: 9, 1, 1, 1, 0, 0, 4, 16, which add to 32.', 'Population variance = 32 / 8 = 4, so σ = 2.', 'Sample variance = 32 / 7 ≈ 4.571, so s ≈ 2.138.'],
            'answer': 'σ = 2 and s ≈ 2.138.',
            'check': 'The sample value is slightly larger because it divides by 7 instead of 8.'},
        'mistakes': ['Forgetting to square the deviations, so they add to zero.', 'Dividing by n when the question is about a sample.', 'Forgetting the square root and reporting the variance as the standard deviation.', 'Misusing the calculator: σn and sn−1 are different keys.'],
        'real_world': 'Factories track the standard deviation of a product\'s weight or size. Two machines with the same average output are not equally good if one has twice the spread and produces more rejects.',
        'exam_strategy': 'Write the formula you are using and state whether it is the sample or population version. If you use the calculator\'s statistics mode, still show the mean and Σ(x − x̄)² so method marks are available.',
        'recap': ['Range is quick but sensitive to outliers.', 'Variance = average squared deviation.', 'Sample: divide by n − 1.', 'SD is in the original units; CV compares relative spread.']},
    T4: {
        'overview': 'The shape of a distribution and its unusual values change which summaries are honest. Box plots built from the five-number summary show centre, spread, skew and outliers in one picture.',
        'key_terms': ['Quartiles', 'Five-number summary', 'Interquartile range', 'Box plot', 'Right skew', 'Left skew', 'Outlier'],
        'explanation': [
            'The quartiles split ordered data into four equal parts. In this course we use the common textbook method: Q2 is the median, Q1 is the median of the lower half and Q3 the median of the upper half, leaving the overall median out of both halves when n is odd. Software and some lecturers use slightly different rules, so small differences are normal.',
            'The five-number summary is minimum, Q1, median, Q3 and maximum. A box plot draws a box from Q1 to Q3 with a line at the median and whiskers to the most extreme values that are not outliers. A value is flagged as an outlier if it lies more than 1.5 × IQR below Q1 or above Q3.',
            'In right-skewed data the long tail is on the high side and the mean is pulled above the median (incomes, waiting times). In left-skewed data the tail is on the low side and the mean falls below the median (marks on an easy test). In symmetric data the mean and median are close.'],
        'formulas_label': 'Formulas',
        'formulas': ['IQR = Q3 − Q1', 'Lower fence = Q1 − 1.5 × IQR', 'Upper fence = Q3 + 1.5 × IQR', 'Right skew: mean > median; left skew: mean < median'],
        'steps': ['Order the data and find the median.', 'Find Q1 and Q3 as the medians of the lower and upper halves.', 'Compute IQR = Q3 − Q1 and the two fences.', 'Flag values outside the fences as outliers.', 'Draw the box plot and describe its shape.'],
        'worked_example': {
            'problem': 'Check the data 3, 5, 7, 8, 9, 11, 13, 15, 40 for outliers.',
            'steps': ['n = 9, so the median is the 5th value, 9.', 'Lower half 3, 5, 7, 8 gives Q1 = 6; upper half 11, 13, 15, 40 gives Q3 = 14.', 'IQR = 14 − 6 = 8, and 1.5 × 8 = 12.', 'Fences: 6 − 12 = −6 and 14 + 12 = 26.'],
            'answer': '40 is above the upper fence of 26, so it is an outlier. No value is below −6.',
            'check': 'Without 40 the largest value is 15, well inside the fences, so 40 is the only outlier.'},
        'mistakes': ['Using the range instead of the IQR in the outlier rule.', 'Drawing the whisker all the way to an outlier instead of to the last non-outlier.', 'Reading "skewed right" as "most values are on the right". The tail is on the right; most values are on the left.', 'Deleting an outlier without investigating it. It may be a data error, or the most important observation.'],
        'real_world': 'Banks flag card transactions that are far outside a customer\'s usual spending pattern. The idea is the same as the outlier rule: define what is normal for that customer, then investigate what falls well outside it.',
        'exam_strategy': 'When comparing two box plots, comment on centre (medians), spread (IQRs), shape and outliers, and always use the context, for example "Group B\'s median waiting time is 4 minutes longer".',
        'recap': ['Five-number summary: min, Q1, median, Q3, max.', 'IQR = Q3 − Q1.', 'Outliers: beyond 1.5 × IQR from the box.', 'Tail direction names the skew; the mean follows the tail.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A researcher measures the blood pressure of 150 patients at one clinic to learn about all adults in a city. The 150 patients are the:', ['sample', 'population', 'parameter', 'statistic'], 0, 'The sample is the part of the population actually measured.'),
    Q(T1, 'Which is a parameter?', ['The mean height of all students at a university', 'The mean height of 50 students chosen at random', 'The proportion of a sample who own a laptop', 'A sample standard deviation'], 0, 'A parameter describes the whole population; the others come from samples.'),
    Q(T1, 'Number of children in a household is a:', ['discrete numerical variable', 'continuous numerical variable', 'nominal categorical variable', 'ordinal categorical variable'], 0, 'It is a count, so it is discrete.'),
    Q(T1, 'Customer satisfaction rated "poor, fair, good, excellent" is:', ['ordinal categorical', 'nominal categorical', 'discrete numerical', 'continuous numerical'], 0, 'The categories have a natural order but are not measurements.'),
    Q(T1, 'A university randomly samples 20 students from each of its 8 faculties. This is:', ['stratified sampling', 'cluster sampling', 'convenience sampling', 'systematic sampling'], 0, 'A random sample is taken within every group (stratum).'),
    Q(T1, 'An online newspaper asks readers to vote on a new tax. The main problem is:', ['voluntary response bias', 'the sample is too large', 'the variable is numerical', 'there is no population'], 0, 'People who choose to respond often hold stronger views than the population as a whole.'),
    # T2
    Q(T2, 'Find the mean of 4, 7, 7, 9 and 13.', ['8', '7', '9', '40'], 0, '(4 + 7 + 7 + 9 + 13) / 5 = 40 / 5 = 8.', ans=st.mean([4, 7, 7, 9, 13])),
    Q(T2, 'Find the median of 3, 9, 1, 7, 5, 11.', ['6', '5', '7', '9'], 0, 'Ordered: 1, 3, 5, 7, 9, 11. The middle two are 5 and 7, so the median is 6.', ans=st.median([3, 9, 1, 7, 5, 11])),
    Q(T2, 'A student scores 70 in a 3-credit course and 50 in a 1-credit course. What is the credit-weighted mean?', ['65', '60', '62.5', '55'], 0, '(70 × 3 + 50 × 1) / 4 = 260 / 4 = 65.', ans=sp.Rational(70 * 3 + 50 * 1, 4)),
    Q(T2, 'Values 1, 2, 3, 4 have frequencies 2, 5, 2, 1. What is the mean?', ['2.2', '2.5', '2', '2.4'], 0, 'Σfx = 2 + 10 + 6 + 4 = 22 and Σf = 10, so 22 / 10 = 2.2.', ans=sp.Rational(1 * 2 + 2 * 5 + 3 * 2 + 4 * 1, 10)),
    Q(T2, 'The salaries in a small firm are strongly right-skewed. Which average best represents a typical salary?', ['The median', 'The mean', 'The range', 'The maximum'], 0, 'The median is not pulled up by the few very high salaries.'),
    Q(T2, 'Five numbers have mean 10. Four of them are 8, 9, 11 and 12. What is the fifth?', ['10', '8', '12', '50'], 0, 'The total must be 5 × 10 = 50, and 8 + 9 + 11 + 12 = 40, so the fifth is 10.', ans=50 - 40),
    # T3
    Q(T3, 'What is the population variance of 2, 4, 4, 4, 5, 5, 7, 9?', ['4', '2', '32', '4.571'], 0, 'The squared deviations from the mean 5 add to 32, and 32 / 8 = 4.', ans=st.pvariance(WE3)),
    Q(T3, 'Find the sample standard deviation of 1, 3, 5 (to 3 d.p.).', ['2.000', '1.633', '4.000', '2.449'], 0, 'Mean 3; squared deviations 4, 0, 4 add to 8; s² = 8 / 2 = 4, so s = 2.', ans=st.stdev([1, 3, 5]), num=True),
    Q(T3, 'Why does the sample variance divide by n − 1?', ['To make s² an unbiased estimate of σ²', 'Because one value is always an outlier', 'To make the answer smaller', 'Because the mean is always zero'], 0, 'Deviations from x̄ are on average a little smaller than deviations from μ, and dividing by n − 1 corrects for this.'),
    Q(T3, 'Data A: 10, 10, 10. Data B: 0, 10, 20. Which statement is true?', ['Same mean, B has the larger standard deviation', 'Same standard deviation, different means', 'A has the larger standard deviation', 'Both have standard deviation 0'], 0, 'Both means are 10. A has no spread at all, while B\'s values sit 10 from the mean.'),
    Q(T3, 'A data set has mean 50 and standard deviation 5. What is the coefficient of variation?', ['10%', '5%', '250%', '0.1%'], 0, 'CV = 5 / 50 × 100% = 10%.'),
    Q(T3, 'For n = 5 values, Σx = 20 and Σx² = 100. What is the sample variance?', ['5', '4', '20', '25'], 0, 'Σ(x − x̄)² = Σx² − (Σx)²/n = 100 − 400/5 = 20, and s² = 20 / 4 = 5.', ans=sp.Rational(100 - sp.Rational(400, 5), 4)),
    # T4
    Q(T4, 'Using the median-of-halves method, what is Q1 of 3, 5, 7, 8, 9, 11, 13, 15, 40?', ['6', '5', '7', '8'], 0, 'The lower half is 3, 5, 7, 8, whose median is (5 + 7)/2 = 6.', ans=q1),
    Q(T4, 'Q1 = 20 and Q3 = 30. What is the upper fence for outliers?', ['45', '40', '35', '60'], 0, 'IQR = 10, so the upper fence is 30 + 1.5 × 10 = 45.', ans=30 + sp.Rational(3, 2) * 10),
    Q(T4, 'In a right-skewed distribution, usually:', ['mean > median', 'mean < median', 'mean = median', 'there is no median'], 0, 'The long upper tail pulls the mean above the median.'),
    Q(T4, 'The middle 50% of a data set lies between:', ['Q1 and Q3', 'the minimum and the median', 'the mean ± 1 standard deviation', 'Q2 and Q3'], 0, 'That is the box of a box plot, whose length is the IQR.'),
    Q(T4, 'Q1 = 12 and Q3 = 18. Which value is an outlier?', ['28', '25', '20', '5'], 0, 'IQR = 6, so the fences are 12 − 9 = 3 and 18 + 9 = 27. Only 28 lies outside.'),
    Q(T4, 'Marks on a very easy test bunch near 100 with a few low scores. The distribution is:', ['left-skewed', 'right-skewed', 'symmetric', 'uniform'], 0, 'The tail stretches towards the low values on the left.'),
]

FLASH = [
    ['Parameter vs statistic', 'Parameter describes the population (μ, σ, p); a statistic describes a sample (x̄, s, p̂).'],
    ['Stratified sample', 'A random sample taken within each group (stratum).'],
    ['Median', 'Middle of the ordered data, position (n + 1)/2; resistant to outliers.'],
    ['Sample variance', 's² = Σ(x − x̄)² / (n − 1).'],
    ['Standard deviation', 'Square root of the variance; a typical distance from the mean.'],
    ['IQR', 'Q3 − Q1, the spread of the middle 50%.'],
    ['Outlier rule', 'Below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR.'],
    ['Right skew', 'Long tail to the right; mean usually above the median.'],
]
