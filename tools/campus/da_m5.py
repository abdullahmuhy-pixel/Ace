"""Introduction to Data Analysis, module 5: Experiments, time series, SQL and communication."""
import math
import sqlite3
from scipy import stats
from verify import Q
T1, T2, T3, T4 = ('A/B tests and experiments', 'Time series: trend, seasonality and growth', 'SQL for analysts', 'Communicating results ethically and reproducibly')
r = lambda v, d: round(v + 0.0, d)
p1, p2, pp = 200 / 4000, 260 / 4000, 460 / 8000
se = math.sqrt(pp * (1 - pp) * (2 / 4000)); z = (p2 - p1) / se
assert (p1, p2, pp) == (0.05, 0.065, 0.0575) and r(se, 5) == 0.00521 and r(z, 2) == 2.88 and r(2 * (1 - stats.norm.cdf(z)), 3) == 0.004 and r((p2 - p1) / p1, 2) == 0.3
se2 = math.sqrt(p1 * (1 - p1) / 4000 + p2 * (1 - p2) / 4000)
assert (r((p2 - p1 - 1.96 * se2) * 100, 1), r((p2 - p1 + 1.96 * se2) * 100, 1)) == (0.5, 2.5)
M = [100, 104, 98, 110, 115, 120]
assert sum(M[-3:]) / 3 == 115 and r((M[-1] / M[-2] - 1) * 100, 1) == 4.3 and r(((146.41 / 100) ** 0.25 - 1) * 100, 6) == 10 and r((120 / 100 - 1) * 100, 6) == 20
db = sqlite3.connect(':memory:'); db.execute('create table sales(city text, amount int)')
db.executemany('insert into sales values(?, ?)', [('Lagos', 120), ('Accra', 80), ('Nairobi', 95), ('Lagos', 150), ('Accra', 60)])
q = lambda s: db.execute(s).fetchall()
assert q('SELECT city, SUM(amount) FROM sales GROUP BY city ORDER BY 2 DESC LIMIT 1') == [('Lagos', 270)]
assert q('SELECT COUNT(*) FROM sales WHERE amount > 90') == [(3,)] and q('SELECT AVG(amount) FROM sales') == [(101.0,)]
assert q('SELECT COUNT(*) FROM (SELECT city FROM sales GROUP BY city HAVING SUM(amount) > 100)') == [(2,)]
assert q('SELECT city, COUNT(*) FROM sales GROUP BY city ORDER BY city') == [('Accra', 2), ('Lagos', 2), ('Nairobi', 1)]

MODULE = {
    'title': 'Experiments, time series, SQL and communication',
    'topics': [T1, T2, T3, T4],
    'overview': 'The last module brings the analyst\'s toolkit together: running A/B tests that can show cause and effect, analysing data that change over time, querying databases with SQL, and communicating results clearly, honestly and reproducibly while respecting people\'s privacy.',
    'key_terms': ['Randomisation', 'Control group', 'A/B test', 'Conversion rate', 'Lift', 'Time series', 'Trend', 'Seasonality', 'Moving average', 'Growth rate', 'CAGR', 'SQL', 'GROUP BY', 'JOIN', 'Reproducibility'],
    'explanation': [
        'Randomised experiments are the cleanest way to establish cause. In an A/B test, users are randomly shown version A or B, and the difference in outcomes is tested for significance and reported with a confidence interval.',
        'Time series need special care: values depend on what came before, and patterns combine trend, seasonality and noise. Moving averages smooth noise, and growth rates (month on month, year on year, compound annual) summarise change.',
        'Most organisational data live in databases queried with SQL: SELECT, WHERE, GROUP BY, HAVING, ORDER BY and JOIN cover most needs. Finally, results matter only if people understand and trust them: lead with the answer, show uncertainty, keep analyses reproducible and handle personal data lawfully (POPIA in South Africa, the NDPA in Nigeria, the Data Protection Act in Kenya, GDPR in Europe).'],
    'quick_facts': [
        'Randomisation balances confounders between groups.',
        'Two-proportion z = (p₂ − p₁)/√(p(1 − p)(1/n₁ + 1/n₂)).',
        'Moving average smooths noise; YoY growth removes seasonality.',
        'CAGR = (end/start)^(1/years) − 1.',
        'SQL order: SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT.'],
}

NOTES = {
    T1: {
        'overview': 'A/B tests let organisations measure the effect of a change by random assignment.',
        'key_terms': ['Randomisation', 'Control and treatment', 'Primary metric', 'Conversion rate', 'Absolute and relative lift', 'Two-proportion z-test', 'Peeking', 'Sample ratio mismatch'],
        'explanation': [
            'Randomly assigning users to A (control) or B (treatment) makes the groups alike on average in everything except the change, so a difference in outcomes can be attributed to the change. Choose one primary metric and the sample size before starting.',
            'Example: A converts 200 of 4000 users (5.0%); B converts 260 of 4000 (6.5%). Absolute lift = 1.5 percentage points; relative lift = 30%. Pooled p = 460/8000 = 0.0575, SE ≈ 0.00521, z ≈ 2.88, two-sided p ≈ 0.004: strong evidence B converts better. A 95% CI for the difference is about 0.5 to 2.5 percentage points.',
            'Common traps: checking results daily and stopping when p < 0.05 ("peeking") inflates false positives; testing many metrics and reporting only the significant one; unequal group sizes that signal a broken assignment (sample ratio mismatch); and novelty effects that fade after launch.'],
        'formulas_label': 'Formulas',
        'formulas': ['Conversion = conversions/users', 'Relative lift = (p_B − p_A)/p_A', 'z = (p_B − p_A)/√(p(1 − p)(1/n_A + 1/n_B)), p pooled', 'CI: (p_B − p_A) ± 1.96√(p_A(1 − p_A)/n_A + p_B(1 − p_B)/n_B)'],
        'steps': ['Define the metric and sample size in advance.', 'Randomise and check group sizes.', 'Compute rates, lift, z and p.', 'Report the effect with a confidence interval and decide.'],
        'worked_example': {
            'problem': 'A: 200/4000 conversions; B: 260/4000. Is B better at α = 0.05?',
            'steps': ['p_A = 0.050, p_B = 0.065; pooled p = 0.0575.', 'SE = √(0.0575 × 0.9425 × 2/4000) ≈ 0.00521; z = 0.015/0.00521 ≈ 2.88.', 'Two-sided p ≈ 0.004 < 0.05.'],
            'answer': 'Yes: B\'s conversion is higher by about 1.5 points (95% CI roughly 0.5 to 2.5 points), a 30% relative lift.',
            'check': 'The CI excludes 0, agreeing with the test ✓.'},
        'mistakes': ['Stopping the test as soon as p dips below 0.05.', 'Confusing absolute and relative lift.', 'Assigning users by choice instead of at random.', 'Testing many metrics without adjustment.'],
        'real_world': 'Online retailers and mobile-money apps run hundreds of A/B tests a year on prices, layouts and messages.',
        'exam_strategy': 'Report both absolute and relative lift; examiners often ask which is which.',
        'recap': ['Randomise.', 'One primary metric.', 'Lift and z-test.', 'No peeking.']},
    T2: {
        'overview': 'Time series are observations in time order. Their structure (trend, seasonality, noise) shapes how they should be analysed.',
        'key_terms': ['Time series', 'Trend', 'Seasonality', 'Noise', 'Moving average', 'Month-on-month growth', 'Year-on-year growth', 'CAGR', 'Autocorrelation', 'Forecast'],
        'explanation': [
            'Monthly sales of 100, 104, 98, 110, 115, 120 (R thousand) rise overall (trend) with a dip in month 3 (noise or a seasonal effect). A 3-month moving average smooths the noise: the latest is (110 + 115 + 120)/3 = 115.',
            'Growth rates: month on month, 120/115 − 1 ≈ 4.3%. Year on year compares the same month a year earlier and removes seasonality: if the same month last year was 100, growth is 20%. Compound annual growth rate: from 100 to 146.41 over 4 years, CAGR = (146.41/100)^(1/4) − 1 = 10% per year.',
            'Consecutive values are correlated (autocorrelation), so ordinary tests that assume independence can mislead. Simple forecasts (last value, seasonal naive, moving average) are useful baselines that more complex models must beat. Always plot the series first, and adjust money values for inflation when comparing over many years.'],
        'formulas_label': 'Formulas',
        'formulas': ['k-period moving average = mean of last k values', 'Growth = new/old − 1', 'CAGR = (end/start)^(1/n) − 1', 'YoY compares the same period a year apart'],
        'steps': ['Plot the series.', 'Identify trend and seasonality.', 'Smooth with moving averages if needed.', 'Summarise with appropriate growth rates.'],
        'worked_example': {
            'problem': 'Revenue grew from R100 million to R146.41 million in 4 years. Find the CAGR.',
            'steps': ['Ratio = 146.41/100 = 1.4641.', 'Fourth root: 1.4641^(1/4) = 1.10.', 'CAGR = 1.10 − 1 = 0.10.'],
            'answer': '10% per year.',
            'check': '100 × 1.1⁴ = 146.41 ✓.'},
        'mistakes': ['Comparing December with November for a seasonal business.', 'Averaging annual growth rates instead of using CAGR.', 'Ignoring inflation over long periods.', 'Treating time-ordered data as independent.'],
        'real_world': 'Retailers in South Africa compare December with the previous December because festive-season sales dwarf other months.',
        'exam_strategy': 'State which growth measure you are using and why (MoM for recent change, YoY for seasonal data, CAGR for multi-year).',
        'recap': ['Trend + season + noise.', 'Moving averages.', 'MoM, YoY, CAGR.', 'Baseline forecasts.']},
    T3: {
        'overview': 'SQL is the language for getting data out of relational databases. A handful of clauses answers most business questions.',
        'key_terms': ['Table', 'Row', 'Column', 'SELECT', 'WHERE', 'GROUP BY', 'Aggregate function', 'HAVING', 'ORDER BY', 'LIMIT', 'JOIN', 'NULL'],
        'explanation': [
            'A table sales(city, amount) holds the five rows Lagos 120, Accra 80, Nairobi 95, Lagos 150, Accra 60. SELECT COUNT(*) FROM sales WHERE amount > 90 returns 3; SELECT AVG(amount) FROM sales returns 101.0.',
            'GROUP BY summarises by category: SELECT city, SUM(amount) FROM sales GROUP BY city ORDER BY 2 DESC LIMIT 1 returns Lagos, 270. WHERE filters rows before grouping; HAVING filters groups after: SELECT city FROM sales GROUP BY city HAVING SUM(amount) > 100 returns 2 cities (Accra 140, Lagos 270).',
            'JOIN combines tables on a key: SELECT o.id, c.name FROM orders o JOIN customers c ON o.cust_id = c.id is an inner join; LEFT JOIN keeps all orders. NULL means unknown: use IS NULL, not = NULL, and remember that COUNT(column) skips NULLs while COUNT(*) does not.'],
        'formulas_label': 'Syntax',
        'formulas': ['SELECT cols FROM table WHERE condition', 'GROUP BY col with SUM, AVG, COUNT, MIN, MAX', 'HAVING aggregate condition', 'ORDER BY col DESC LIMIT n', 'a JOIN b ON a.key = b.key'],
        'steps': ['Identify the tables and keys.', 'Filter rows with WHERE.', 'Group and aggregate; filter groups with HAVING.', 'Sort and limit the output.'],
        'worked_example': {
            'problem': 'Write a query for the city with the highest total sales, and give its result.',
            'steps': ['Group by city and sum amount.', 'Sort by the total descending.', 'Keep the first row.'],
            'answer': 'SELECT city, SUM(amount) FROM sales GROUP BY city ORDER BY 2 DESC LIMIT 1 → Lagos, 270.',
            'check': 'Running it in SQLite returns (Lagos, 270) ✓.'},
        'mistakes': ['Using WHERE with an aggregate (needs HAVING).', 'Selecting columns that are neither grouped nor aggregated.', 'Writing = NULL instead of IS NULL.', 'Forgetting join conditions and getting every combination of rows.'],
        'real_world': 'Almost every company\'s sales, customer and stock data sit in SQL databases; analysts query them daily.',
        'exam_strategy': 'Write clauses in the fixed order SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT.',
        'recap': ['SELECT and WHERE.', 'GROUP BY with aggregates.', 'HAVING filters groups.', 'JOINs on keys.']},
    T4: {
        'overview': 'Analysis is only useful if it is understood, trusted and done responsibly.',
        'key_terms': ['Executive summary', 'Uncertainty', 'Reproducibility', 'Version control', 'Data protection law', 'Personal information', 'Anonymisation', 'Pseudonymisation', 'Informed consent', 'Algorithmic bias'],
        'explanation': [
            'Lead with the answer: "Variant B lifts conversion by 1.5 points (95% CI 0.5 to 2.5); we recommend launching it." Then give the evidence, the method and the caveats. Show uncertainty (intervals, ranges) rather than false precision, and choose charts that make the key comparison obvious.',
            'Reproducibility means someone else can rerun your work and get the same result: keep raw data unchanged, script every cleaning step (in Python, R or SQL rather than by hand), record software versions and use version control such as Git.',
            'Personal data must be handled lawfully: South Africa\'s POPIA, Nigeria\'s Data Protection Act 2023, Kenya\'s Data Protection Act 2019 and the EU\'s GDPR require a lawful purpose, minimal collection, security and respect for people\'s rights. Remove or mask identifiers, beware that combinations of age, location and gender can re-identify people, and check models for unfair effects on groups.'],
        'formulas_label': 'Checklist',
        'formulas': ['Answer first, then evidence', 'Report uncertainty', 'Scripted, versioned analysis', 'Lawful, minimal, secure use of personal data'],
        'steps': ['Write the one-sentence finding.', 'Support it with one or two clear charts and intervals.', 'State limitations and assumptions.', 'Check reproducibility and privacy before sharing.'],
        'worked_example': {
            'problem': 'Rewrite "Our analysis of 8000 users using a two-proportion z-test produced z = 2.88" for a manager.',
            'steps': ['Lead with the decision-relevant finding.', 'Give the size of the effect and its uncertainty in plain units.', 'Put the method in a short note.'],
            'answer': '"The new checkout page increased conversion from 5.0% to 6.5% (likely between 0.5 and 2.5 points). We recommend launching it. (A/B test, 8000 users, p ≈ 0.004.)"',
            'check': 'A manager can act on the first sentence alone ✓.'},
        'mistakes': ['Burying the conclusion under methods.', 'Reporting point estimates without uncertainty.', 'Editing raw data by hand.', 'Sharing datasets containing identifiable personal information.'],
        'real_world': 'Regulators in South Africa, Nigeria and Kenya have fined organisations for mishandling personal data, so analysts must build privacy into their work.',
        'exam_strategy': 'For communication questions, write the summary sentence first and keep technical terms in brackets.',
        'recap': ['Answer first.', 'Show uncertainty.', 'Reproducible scripts.', 'Protect personal data.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The main reason to randomise users in an A/B test is to:', ['balance confounders so differences can be attributed to the change', 'increase the sample size', 'make results significant', 'save time'], 0, 'Fair comparison.'),
    Q(T1, 'A converts 200/4000 users and B 260/4000. The absolute lift is:', ['1.5 percentage points', '30%', '60 users', '6.5%'], 0, '6.5 − 5.0.'),
    Q(T1, 'The relative lift is:', ['30%', '1.5%', '13%', '65%'], 0, '0.015/0.05.'),
    Q(T1, 'The two-proportion z statistic is about:', ['2.88', '1.5', '0.3', '5.75'], 0, '0.015/0.00521.', ans=2.88, num=True),
    Q(T1, 'Checking results every day and stopping once p < 0.05:', ['inflates the false-positive rate', 'is best practice', 'reduces bias', 'has no effect'], 0, 'Peeking.'),
    Q(T1, 'A 95% CI for the difference of 0.5 to 2.5 points means:', ['B is plausibly better by between 0.5 and 2.5 points', 'B is worse', 'the test failed', 'there is no difference'], 0, 'Excludes zero.'),
    # T2
    Q(T2, 'Sales 110, 115, 120 for the last three months give a 3-month moving average of:', ['115', '120', '110', '345'], 0, 'Mean.', ans=115, num=True),
    Q(T2, 'Growth from 115 to 120 month on month is about:', ['4.3%', '5%', '4.2%', '0.43%'], 0, '120/115 − 1.'),
    Q(T2, 'Revenue grows from 100 to 146.41 over 4 years. The CAGR is:', ['10%', '11.6%', '46.4%', '9.2%'], 0, '1.4641^(1/4) − 1.'),
    Q(T2, 'For a strongly seasonal business, the fairest growth comparison is usually:', ['year on year', 'month on month', 'day on day', 'none'], 0, 'Same season.'),
    Q(T2, 'A regular pattern that repeats every year is called:', ['seasonality', 'trend', 'noise', 'autocorrelation'], 0, 'Calendar cycle.'),
    Q(T2, 'Consecutive values in a time series being related is called:', ['autocorrelation', 'multicollinearity', 'independence', 'stratification'], 0, 'Breaks independence.'),
    # T3
    Q(T3, 'SELECT COUNT(*) FROM sales WHERE amount > 90 returns (amounts 120, 80, 95, 150, 60):', ['3', '2', '5', '1'], 0, '120, 95, 150.', ans=3, num=True),
    Q(T3, 'SELECT AVG(amount) FROM sales returns:', ['101.0', '95.0', '505', '5'], 0, '505/5.'),
    Q(T3, 'The city with the highest total (GROUP BY city ORDER BY SUM DESC LIMIT 1) is:', ['Lagos, 270', 'Accra, 140', 'Nairobi, 95', 'Lagos, 150'], 0, '120 + 150.'),
    Q(T3, 'To keep only cities whose total exceeds 100, use:', ['HAVING SUM(amount) > 100', 'WHERE SUM(amount) > 100', 'ORDER BY 100', 'LIMIT 100'], 0, 'Filter groups.'),
    Q(T3, 'How many cities have total sales above 100?', ['2', '3', '1', '0'], 0, 'Accra 140, Lagos 270.', ans=2, num=True),
    Q(T3, 'To find rows where email is missing, write:', ['WHERE email IS NULL', 'WHERE email = NULL', 'WHERE email = ""', 'WHERE NULL'], 0, 'NULL needs IS.'),
    # T4
    Q(T4, 'A report for managers should start with:', ['the main finding and recommendation', 'the full method', 'raw data tables', 'the code'], 0, 'Answer first.'),
    Q(T4, 'Reproducible analysis means:', ['others can rerun the scripted steps and get the same results', 'results are always significant', 'data are edited by hand', 'only one person can run it'], 0, 'Scripts and versions.'),
    Q(T4, 'South Africa\'s main data-protection law is:', ['POPIA', 'GDPR', 'HIPAA', 'NDPA'], 0, 'Protection of Personal Information Act.'),
    Q(T4, 'Removing names but keeping exact age, village and gender may still allow:', ['re-identification of individuals', 'perfect anonymity', 'better accuracy only', 'nothing'], 0, 'Combinations identify.'),
    Q(T4, 'Showing a result as "6.5% (likely 5.9% to 7.1%)" rather than "6.5132%":', ['communicates uncertainty honestly', 'hides the result', 'is less accurate', 'breaks reproducibility'], 0, 'Avoid false precision.'),
    Q(T4, 'Keeping raw data unchanged and scripting all cleaning helps:', ['reproducibility and error-checking', 'make files smaller', 'increase p-values', 'avoid charts'], 0, 'Audit trail.'),
]

FLASH = [
    ['A/B test', 'Random assignment to control and treatment; compare one primary metric.'],
    ['Absolute vs relative lift', 'p_B − p_A vs (p_B − p_A)/p_A.'],
    ['Peeking', 'Stopping early when p < 0.05 inflates false positives.'],
    ['Moving average', 'Mean of the last k values; smooths noise.'],
    ['CAGR', '(end/start)^(1/years) − 1.'],
    ['SQL clause order', 'SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT.'],
    ['WHERE vs HAVING', 'WHERE filters rows; HAVING filters groups.'],
    ['Responsible analysis', 'Answer first, show uncertainty, reproducible, lawful use of personal data.'],
]
