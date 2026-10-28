"""Introduction to Data Analysis, module 1: Data and descriptive statistics."""
import statistics as st
import numpy as np
from verify import Q
T1, T2, T3, T4 = ('Data, variables and tidy datasets', 'Measures of centre and spread', 'Distributions, z-scores and outliers', 'Choosing the right chart')
r = lambda v, d: round(v + 0.0, d)
D = [22, 25, 25, 28, 30, 31, 33, 35, 38, 63]  # delivery times in minutes, 10 orders
q1, q3 = st.median(D[:5]), st.median(D[5:])
assert st.mean(D) == 33 and st.median(D) == 30.5 and st.mode(D) == 25 and r(st.stdev(D), 1) == 11.6 and max(D) - min(D) == 41
assert (q1, q3, q3 - q1) == (25, 35, 10) and (q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)) == (10, 50)
assert list(np.percentile(D, [25, 75])) == [25.75, 34.5]  # numpy's default (linear) method differs from the halves method
E = D[:-1]
assert r(st.mean(E), 2) == 29.67 and st.median(E) == 30 and r(st.stdev(E), 1) == 5.2
assert r((63 - 33) / st.stdev(D), 2) == 2.58 and (78 - 65) / 8 == 1.625 and (50 - 65) / 8 == -1.875
assert (3 * 70 + 2 * 80 + 1 * 50) / 6 == 70
rows, cols = 1200, 8; assert rows * cols == 9600

MODULE = {
    'title': 'Data and descriptive statistics',
    'topics': [T1, T2, T3, T4],
    'overview': 'Data analysis turns raw records into answers. This module starts with what data is and how to arrange it tidily, then summarises a variable with measures of centre and spread, describes the shape of distributions and spots outliers, and ends with how to choose a chart that tells the truth.',
    'key_terms': ['Observation', 'Variable', 'Categorical', 'Numerical', 'Tidy data', 'Mean', 'Median', 'Mode', 'Standard deviation', 'Interquartile range', 'Skewness', 'z-score', 'Outlier', 'Histogram', 'Box plot'],
    'explanation': [
        'A dataset is a table of observations (rows) and variables (columns). Variables are categorical (nominal or ordinal) or numerical (discrete or continuous), and the type decides which summaries and charts make sense. Tidy data has one observation per row, one variable per column and one value per cell.',
        'The centre of a numerical variable is summarised by the mean or median, and its spread by the standard deviation or interquartile range. The mean and standard deviation are pulled by extreme values; the median and IQR are resistant, so they suit skewed data such as incomes or delivery times.',
        'z-scores measure how many standard deviations a value is from the mean, and the 1.5 × IQR rule flags outliers. Good charts match the question: bar charts compare categories, histograms and box plots show distributions, line charts show change over time and scatter plots show relationships.'],
    'quick_facts': [
        'Tidy: one row per observation, one column per variable.',
        'Mean = Σx/n; median = middle value when sorted.',
        'Sample SD uses n − 1; IQR = Q3 − Q1.',
        'z = (x − mean)/SD.',
        'Outlier rule: below Q1 − 1.5 IQR or above Q3 + 1.5 IQR.'],
}

NOTES = {
    T1: {
        'overview': 'Before analysing anything, know what each row represents and what type each variable is.',
        'key_terms': ['Observation (case)', 'Variable', 'Nominal', 'Ordinal', 'Discrete', 'Continuous', 'Tidy data', 'Primary and secondary data', 'Metadata'],
        'explanation': [
            'Each row of a dataset is one observation (a customer, an order, a day) and each column is a variable measured on it. A table of 1200 orders with 8 variables holds 9600 values. Knowing the unit of observation prevents mistakes such as averaging totals that were already averages.',
            'Categorical variables put observations into groups: nominal ones have no order (province, payment method), ordinal ones do (satisfaction from "poor" to "excellent"). Numerical variables are counts (discrete: items in a basket) or measurements (continuous: delivery time). Postal codes and phone numbers look numerical but are categorical: averaging them is meaningless.',
            'Tidy data (one row per observation, one column per variable, one value per cell) is what most analysis tools expect. A spreadsheet with months spread across columns ("Jan", "Feb", …) is "wide"; reshaping it to columns month and sales makes it tidy. Metadata, such as a data dictionary, records units, codes and how the data were collected.'],
        'formulas_label': 'Checklist',
        'formulas': ['What is one row?', 'What type is each column?', 'What are the units and codes?', 'Is the table tidy?'],
        'steps': ['State the unit of observation.', 'Classify each variable.', 'Check units and missing-value codes.', 'Reshape to tidy form if needed.'],
        'worked_example': {
            'problem': 'A survey file has columns: respondent ID, province, age, satisfaction (1 = very poor … 5 = very good) and monthly spend (R). Classify each variable.',
            'steps': ['Respondent ID: an identifier (categorical, not for arithmetic).', 'Province: nominal; age and monthly spend: numerical (continuous in principle).', 'Satisfaction: ordinal, even though it is coded as numbers.'],
            'answer': 'ID and province categorical (nominal); satisfaction ordinal; age and spend numerical.',
            'check': 'Averaging IDs would be meaningless, confirming they are not numerical data ✓.'},
        'mistakes': ['Treating numeric codes as quantities.', 'Mixing units (rand and thousands of rand) in one column.', 'Storing two variables in one column ("Male_25").', 'Not knowing what one row represents.'],
        'real_world': 'Statistics South Africa publishes data dictionaries with every release so analysts know exactly what each column means.',
        'exam_strategy': 'When asked which summary or chart to use, first classify the variable; the answer follows from its type.',
        'recap': ['Rows are observations.', 'Categorical vs numerical.', 'Codes are not numbers.', 'Tidy data.']},
    T2: {
        'overview': 'Two numbers summarise most variables: a measure of centre and a measure of spread.',
        'key_terms': ['Mean', 'Median', 'Mode', 'Weighted mean', 'Range', 'Variance', 'Standard deviation', 'Quartiles', 'Interquartile range', 'Resistant statistic'],
        'explanation': [
            'Delivery times for 10 orders (minutes): 22, 25, 25, 28, 30, 31, 33, 35, 38, 63. Mean = 330/10 = 33; median = average of the 5th and 6th values = (30 + 31)/2 = 30.5; mode = 25. The single late delivery (63) drags the mean above the median.',
            'Spread: range = 63 − 22 = 41. The sample standard deviation, s = √(Σ(x − x̄)²/(n − 1)), is about 11.6 minutes. Quartiles by the halves method: Q1 = median of the lower five = 25, Q3 = median of the upper five = 35, so IQR = 10. Software may use other quartile methods (numpy\'s default gives 25.75 and 34.5), so always say which you used.',
            'Removing the 63 changes the mean to 29.67 and the SD to 5.2, but the median only to 30. That is what "resistant" means. A weighted mean accounts for importance: marks of 70 (weight 3), 80 (weight 2) and 50 (weight 1) average (210 + 160 + 50)/6 = 70.'],
        'formulas_label': 'Formulas',
        'formulas': ['x̄ = Σx/n', 's = √(Σ(x − x̄)²/(n − 1))', 'IQR = Q3 − Q1', 'Weighted mean = Σwx/Σw'],
        'steps': ['Sort the data.', 'Find the mean and median.', 'Find the SD and quartiles.', 'Report centre and spread together, matched (mean with SD, median with IQR).'],
        'worked_example': {
            'problem': 'Find the median and IQR of the delivery times 22, 25, 25, 28, 30, 31, 33, 35, 38, 63.',
            'steps': ['n = 10, so the median is the mean of the 5th and 6th values: (30 + 31)/2 = 30.5.', 'Lower half 22, 25, 25, 28, 30: Q1 = 25. Upper half 31, 33, 35, 38, 63: Q3 = 35.', 'IQR = 35 − 25 = 10.'],
            'answer': 'Median 30.5 minutes, IQR 10 minutes.',
            'check': 'Half the deliveries took between 25 and 35 minutes ✓.'},
        'mistakes': ['Forgetting to sort before finding the median.', 'Using n instead of n − 1 for a sample SD.', 'Reporting the mean for strongly skewed data without comment.', 'Not stating the quartile method.'],
        'real_world': 'House prices are reported as medians because a few mansions would inflate the mean.',
        'exam_strategy': 'Pair your statistics: mean with SD for symmetric data, median with IQR for skewed data or data with outliers.',
        'recap': ['Mean, median, mode.', 'SD uses n − 1.', 'IQR from quartiles.', 'Medians resist outliers.']},
    T3: {
        'overview': 'The shape of a distribution matters as much as its centre and spread. z-scores and outlier rules put individual values in context.',
        'key_terms': ['Distribution', 'Symmetric', 'Right (positive) skew', 'Left skew', 'Bimodal', 'z-score', 'Empirical rule', 'Outlier', 'Fence'],
        'explanation': [
            'A distribution is symmetric, right-skewed (a long tail of large values, mean > median) or left-skewed (mean < median); it may be bimodal, often a sign of two groups mixed together. The delivery times are right-skewed: mean 33 > median 30.5.',
            'A z-score, z = (x − mean)/SD, says how unusual a value is. In a test with mean 65 and SD 8, a mark of 78 has z = 1.625 and 50 has z = −1.875. For roughly bell-shaped data, about 68%, 95% and 99.7% of values lie within 1, 2 and 3 SDs of the mean (the empirical rule).',
            'The 1.5 × IQR rule: fences are Q1 − 1.5 IQR and Q3 + 1.5 IQR. For the deliveries, 25 − 15 = 10 and 35 + 15 = 50, so 63 is an outlier (its z-score is about 2.58). Outliers should be investigated, not deleted automatically: a 63-minute delivery may be a real problem worth fixing.'],
        'formulas_label': 'Formulas',
        'formulas': ['z = (x − x̄)/s', 'Empirical rule: 68–95–99.7', 'Lower fence = Q1 − 1.5 IQR', 'Upper fence = Q3 + 1.5 IQR'],
        'steps': ['Plot the data (histogram or box plot).', 'Describe shape, centre and spread.', 'Compute fences or z-scores.', 'Investigate any outliers before deciding what to do.'],
        'worked_example': {
            'problem': 'Is the 63-minute delivery an outlier by the 1.5 × IQR rule (Q1 = 25, Q3 = 35)?',
            'steps': ['IQR = 10; 1.5 × IQR = 15.', 'Upper fence = 35 + 15 = 50.', '63 > 50.'],
            'answer': 'Yes, it is an outlier.',
            'check': 'Its z-score, (63 − 33)/11.6 ≈ 2.58, also marks it as unusual ✓.'},
        'mistakes': ['Deleting outliers without checking them.', 'Applying the empirical rule to strongly skewed data.', 'Confusing right skew with "most values are on the right".', 'Computing z-scores with the wrong SD.'],
        'real_world': 'Banks flag card transactions with extreme z-scores relative to a customer\'s usual spending as possible fraud.',
        'exam_strategy': 'Describe distributions with four words: shape, centre, spread, unusual values.',
        'recap': ['Skew moves the mean.', 'z-scores standardise.', '68–95–99.7.', 'Fences flag outliers.']},
    T4: {
        'overview': 'A chart should answer a question at a glance. The right chart depends on the variable types and the comparison you want to show.',
        'key_terms': ['Bar chart', 'Histogram', 'Box plot', 'Line chart', 'Scatter plot', 'Stacked bar', 'Axis baseline', 'Data-ink', 'Misleading chart'],
        'explanation': [
            'One categorical variable: a bar chart of counts or percentages (better than a pie chart for comparing sizes). One numerical variable: a histogram (shape) or box plot (median, quartiles and outliers). Change over time: a line chart. Two numerical variables: a scatter plot. Comparing a numerical variable across groups: side-by-side box plots.',
            'Honest charts start bar axes at zero, label axes with units, use consistent scales across panels and avoid 3D effects that distort size. Truncating a bar axis can make a 2% difference look like a doubling.',
            'Design for the reader: order bars by size unless the categories have a natural order, use colour to highlight what matters rather than decorate, and give the chart a title that states the finding ("Late deliveries cluster on Fridays") rather than just the topic.'],
        'formulas_label': 'Chart chooser',
        'formulas': ['Categorical → bar chart', 'Numerical distribution → histogram or box plot', 'Over time → line chart', 'Two numerical → scatter plot', 'Numerical by group → box plots'],
        'steps': ['Write the question the chart answers.', 'Identify the variable types.', 'Pick the chart type.', 'Check axes, labels, scale and title.'],
        'worked_example': {
            'problem': 'Which chart shows how delivery time depends on distance travelled for 500 orders?',
            'steps': ['Both delivery time and distance are numerical.', 'The question is about a relationship between two numerical variables.', 'Use a scatter plot with distance on the x-axis (explanatory) and time on the y-axis (response).'],
            'answer': 'A scatter plot.',
            'check': 'A bar chart would need categories, which we do not have ✓.'},
        'mistakes': ['Using a pie chart with many slices.', 'Starting a bar axis above zero.', 'Using a line chart for unordered categories.', 'Leaving out units.'],
        'real_world': 'News graphics teams follow strict chart rules because a misleading axis can change how readers vote or invest.',
        'exam_strategy': 'Justify a chart choice in one sentence naming the variable types and the question.',
        'recap': ['Match chart to variable types.', 'Bars start at zero.', 'Label everything.', 'Title states the finding.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'In a tidy dataset, each row is:', ['one observation', 'one variable', 'one summary statistic', 'one chart'], 0, 'Columns are variables.'),
    Q(T1, 'Customer satisfaction rated 1 to 5 is:', ['ordinal', 'continuous', 'nominal', 'discrete numerical with meaningful averages always'], 0, 'Ordered categories.'),
    Q(T1, 'Postal codes are best treated as:', ['categorical', 'continuous', 'ratio data', 'discrete counts'], 0, 'Labels, not quantities.'),
    Q(T1, 'A table of 1200 orders with 8 variables contains how many values?', ['9600', '1208', '150', '960'], 0, '1200 × 8.', ans=9600, num=True),
    Q(T1, 'A spreadsheet with one column per month of sales is:', ['wide, not tidy', 'tidy', 'long', 'normalised'], 0, 'Month is a variable.'),
    Q(T1, 'The number of items in a basket is:', ['discrete numerical', 'continuous numerical', 'nominal', 'ordinal'], 0, 'Counts.'),
    # T2
    Q(T2, 'The mean of 22, 25, 25, 28, 30, 31, 33, 35, 38, 63 is:', ['33', '30.5', '25', '41'], 0, '330/10.', ans=33, num=True),
    Q(T2, 'The median of that data is:', ['30.5', '30', '31', '33'], 0, '(30 + 31)/2.', ans=30.5, num=True),
    Q(T2, 'Using the halves method, its IQR is:', ['10', '41', '11.6', '13'], 0, '35 − 25.', ans=10, num=True),
    Q(T2, 'Its sample standard deviation is about:', ['11.6', '11.0', '5.2', '10'], 0, 'Using n − 1.', ans=11.6, num=True),
    Q(T2, 'Removing the value 63 changes the median from 30.5 to:', ['30', '29.67', '28', '31'], 0, 'Median is resistant.', ans=30, num=True),
    Q(T2, 'Marks of 70 (weight 3), 80 (weight 2) and 50 (weight 1) have a weighted mean of:', ['70', '66.7', '75', '65'], 0, '420/6.', ans=70, num=True),
    # T3
    Q(T3, 'A distribution with mean 33 and median 30.5 is probably:', ['right-skewed', 'left-skewed', 'perfectly symmetric', 'uniform'], 0, 'Mean pulled up.'),
    Q(T3, 'Test mean 65, SD 8. A mark of 78 has z-score:', ['1.625', '13', '0.62', '−1.625'], 0, '13/8.', ans=1.625, num=True),
    Q(T3, 'A mark of 50 on that test has z-score:', ['−1.875', '1.875', '−15', '−0.53'], 0, '−15/8.', ans=-1.875, num=True),
    Q(T3, 'With Q1 = 25 and Q3 = 35, the upper outlier fence is:', ['50', '45', '40', '52.5'], 0, '35 + 15.', ans=50, num=True),
    Q(T3, 'For bell-shaped data, about what percentage lies within 2 SDs of the mean?', ['95%', '68%', '99.7%', '50%'], 0, 'Empirical rule.'),
    Q(T3, 'When you find an outlier, you should first:', ['investigate why it occurred', 'delete it', 'replace it with the mean', 'double it'], 0, 'It may be real.'),
    # T4
    Q(T4, 'To compare the number of orders by payment method, use a:', ['bar chart', 'scatter plot', 'line chart', 'histogram'], 0, 'One categorical variable.'),
    Q(T4, 'To show the shape of a numerical variable, use a:', ['histogram', 'pie chart', 'line chart', 'stacked bar'], 0, 'Distribution.'),
    Q(T4, 'To show monthly sales over two years, use a:', ['line chart', 'pie chart', 'box plot', 'bar of categories sorted by size'], 0, 'Time order.'),
    Q(T4, 'To show the relationship between distance and delivery time, use a:', ['scatter plot', 'bar chart', 'pie chart', 'histogram'], 0, 'Two numerical variables.'),
    Q(T4, 'A bar chart whose y-axis starts at 95 instead of 0:', ['can exaggerate small differences', 'is always more accurate', 'is required by convention', 'hides outliers'], 0, 'Truncated axis.'),
    Q(T4, 'The best chart title:', ['states the finding', 'is a single word', 'repeats the axis labels', 'is left out'], 0, 'Tell the reader what to see.'),
]

FLASH = [
    ['Tidy data', 'One row per observation, one column per variable, one value per cell.'],
    ['Variable types', 'Categorical (nominal, ordinal) or numerical (discrete, continuous).'],
    ['Mean vs median', 'Mean is pulled by outliers; median is resistant.'],
    ['Sample SD', 's = √(Σ(x − x̄)²/(n − 1)).'],
    ['IQR', 'Q3 − Q1; spread of the middle half.'],
    ['z-score', 'z = (x − mean)/SD.'],
    ['Outlier fences', 'Q1 − 1.5 IQR and Q3 + 1.5 IQR.'],
    ['Chart chooser', 'Bar: categories; histogram/box: distribution; line: time; scatter: relationship.'],
]
