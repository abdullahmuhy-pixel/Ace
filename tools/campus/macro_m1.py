"""Principles of Macroeconomics, module 1: Measuring the economy."""
from verify import Q, sp
T1, T2, T3, T4 = ('GDP and how it is measured', 'Real GDP and economic growth', 'Inflation and price indices', 'Unemployment')
R = sp.Rational
assert 600 + 150 + 200 + (100 - 120) == 930
assert R(1100 * 100, 110) == 1000 and R(1050 - 1000, 1000) * 100 == 5
assert R(216 - 200, 200) * 100 == 8 and R(100, 1000) * 100 == 10 and round(1000 / 1500 * 100, 1) == 66.7
assert R(70, 2) == 35

MODULE = {
    'title': 'Measuring the economy',
    'topics': [T1, T2, T3, T4],
    'overview': 'Macroeconomics looks at the economy as a whole. Before explaining booms, recessions and inflation, we need to measure them. This module covers the three headline statistics every government publishes: GDP (output), inflation (prices) and unemployment (jobs), and what each one does and does not tell us.',
    'key_terms': ['Gross domestic product', 'Expenditure approach', 'Nominal GDP', 'Real GDP', 'GDP deflator', 'Consumer price index', 'Inflation', 'Unemployment rate', 'Labour force'],
    'explanation': [
        'GDP is the market value of all final goods and services produced within a country in a period. It can be measured by adding spending, incomes or value added, and all three should give the same answer, because every amount spent is someone\'s income.',
        'Nominal GDP uses current prices, so it rises with inflation even if output does not. Real GDP uses constant prices and measures actual output. Economic growth is the percentage change in real GDP.',
        'Inflation is the rate at which the general price level rises, usually measured with a consumer price index. Unemployment counts people without work who are actively looking for it. Each statistic has known weaknesses, which matter when governments use them to set policy.'],
    'quick_facts': [
        'GDP = C + I + G + (X − M).',
        'Real GDP = nominal GDP ÷ deflator × 100.',
        'Inflation = (new index − old index) ÷ old index × 100%.',
        'Unemployment rate = unemployed ÷ labour force × 100%.',
        'Rule of 70: doubling time ≈ 70 ÷ growth rate (%).'],
}

NOTES = {
    T1: {
        'overview': 'Gross domestic product (GDP) is the total value of final goods and services produced inside a country in a year. It is the most widely used measure of the size of an economy.',
        'key_terms': ['Final goods', 'Intermediate goods', 'Value added', 'Expenditure approach', 'Income approach', 'Circular flow', 'GDP per capita'],
        'explanation': [
            'Only final goods count. The flour a bakery buys is an intermediate good, already included in the price of the bread, so counting it too would double-count. Equivalently, GDP is the sum of the value added at each stage of production.',
            'The expenditure approach adds consumption (C), investment by firms in capital goods and housing (I), government spending on goods and services (G) and net exports (exports X minus imports M): GDP = C + I + G + (X − M). Transfer payments such as pensions are not in G, because nothing is produced in exchange.',
            'GDP leaves things out: unpaid work at home, the informal economy, pollution and leisure. GDP per capita (GDP ÷ population) is a better guide to living standards, but it hides inequality, so economists also use measures such as the Human Development Index.'],
        'formulas_label': 'Formulas',
        'formulas': ['GDP = C + I + G + (X − M)', 'GDP = sum of value added at each stage', 'GDP per capita = GDP ÷ population', 'GNI = GDP + net income from abroad'],
        'steps': ['Identify the final spending categories.', 'Exclude intermediate goods, transfers and second-hand sales.', 'Add C + I + G + (X − M).', 'Divide by population if a per-person figure is needed.'],
        'worked_example': {
            'problem': 'An economy has consumption 600, investment 150, government purchases 200, exports 100 and imports 120 (in billions). Find GDP.',
            'steps': ['Net exports = 100 − 120 = −20.', 'GDP = 600 + 150 + 200 − 20.', 'GDP = 930.'],
            'answer': 'GDP = 930 billion.',
            'check': 'Imports are subtracted because they are already counted inside C, I and G but were produced abroad.'},
        'mistakes': ['Counting intermediate goods (double counting).', 'Including transfer payments in G.', 'Adding imports instead of subtracting them.', 'Counting the sale of a second-hand car as new production.'],
        'real_world': 'Ghana and Nigeria both revised their GDP up sharply after "rebasing" (updating the base year and including newer industries such as telecoms and film), showing how much measurement choices matter.',
        'exam_strategy': 'When a question gives a list of items, mark each as "in" or "out" with a short reason (intermediate, transfer, second-hand). This earns marks even if one item is wrong.',
        'recap': ['Final goods only, or value added.', 'GDP = C + I + G + (X − M).', 'Transfers and second-hand sales are excluded.', 'GDP per capita for living standards, with caveats.']},
    T2: {
        'overview': 'Real GDP removes the effect of price changes, so it shows how much more the economy is actually producing. Its growth rate is the main measure of economic progress.',
        'key_terms': ['Nominal GDP', 'Real GDP', 'Base year', 'GDP deflator', 'Growth rate', 'Business cycle', 'Recession'],
        'explanation': [
            'Nominal GDP values output at current prices. Real GDP values it at base-year prices, so if output is unchanged but prices double, nominal GDP doubles while real GDP stays the same. The GDP deflator = nominal ÷ real × 100 is a broad price index.',
            'The growth rate is (this year\'s real GDP − last year\'s) ÷ last year\'s × 100%. Small differences compound: at 2% a year an economy doubles in about 35 years, at 7% in about 10 years (the rule of 70).',
            'Real GDP fluctuates around its long-run trend in the business cycle: expansion, peak, contraction and trough. A recession is commonly defined as two consecutive quarters of falling real GDP.'],
        'formulas_label': 'Formulas',
        'formulas': ['Real GDP = nominal GDP ÷ deflator × 100', 'Deflator = nominal ÷ real × 100', 'Growth = (Y₁ − Y₀)/Y₀ × 100%', 'Doubling time ≈ 70 ÷ growth rate'],
        'steps': ['Convert nominal figures to real using the deflator.', 'Compute the percentage change in real GDP.', 'Use per-capita figures to compare living standards.', 'Use the rule of 70 for doubling times.'],
        'worked_example': {
            'problem': 'Nominal GDP is 1100 and the GDP deflator is 110. Last year real GDP was 1000. Find this year\'s real GDP and the growth rate.',
            'steps': ['Real GDP = 1100 ÷ 110 × 100 = 1000.', 'Growth = (1000 − 1000)/1000 = 0%.', 'All of the rise in nominal GDP was due to prices.'],
            'answer': 'Real GDP is 1000, so real growth is 0%: the economy did not grow.',
            'check': 'A deflator of 110 means prices are 10% above the base year, matching nominal GDP 10% above real GDP ✓.'},
        'mistakes': ['Calling a rise in nominal GDP "growth".', 'Multiplying by the deflator instead of dividing.', 'Comparing countries\' total GDP instead of GDP per capita.', 'Adding growth rates over several years instead of compounding.'],
        'real_world': 'China\'s growth of around 10% a year for three decades doubled its economy roughly every 7 years, lifting hundreds of millions of people out of poverty.',
        'exam_strategy': 'State whether each figure is nominal or real before using it. Many questions are designed to catch students who compare a nominal number with a real one.',
        'recap': ['Real GDP removes price changes.', 'Deflator = nominal/real × 100.', 'Growth = % change in real GDP.', 'Rule of 70 for doubling time.']},
    T3: {
        'overview': 'Inflation is a sustained rise in the general price level. It is measured with price indices such as the consumer price index (CPI), and it changes the real value of money, wages and debts.',
        'key_terms': ['Inflation', 'Deflation', 'Consumer price index', 'Basket of goods', 'Real wage', 'Real interest rate', 'Demand-pull', 'Cost-push'],
        'explanation': [
            'The CPI tracks the cost of a fixed basket of goods a typical household buys, relative to a base year set at 100. The inflation rate is the percentage change in the index. If the basket costs 200 last year and 216 this year, inflation is 8%.',
            'Inflation reduces purchasing power. Real values adjust for it: the real wage is the nominal wage divided by the price level, and the real interest rate ≈ nominal rate − inflation. Unexpected inflation transfers wealth from lenders to borrowers and hurts people on fixed incomes.',
            'Causes include demand-pull (spending grows faster than the economy can produce) and cost-push (rising costs such as oil prices or wages). The CPI can overstate inflation because it is slow to reflect new products, quality improvements and households switching to cheaper goods.'],
        'formulas_label': 'Formulas',
        'formulas': ['CPI = cost of basket now ÷ cost in base year × 100', 'Inflation = (CPI₁ − CPI₀)/CPI₀ × 100%', 'Real wage = nominal wage ÷ price index × 100', 'Real interest rate ≈ nominal rate − inflation'],
        'steps': ['Find the basket cost in each year.', 'Convert to index numbers.', 'Compute the percentage change.', 'Adjust wages or interest rates to real terms.'],
        'worked_example': {
            'problem': 'A basket costs 200 last year and 216 this year. A saver earns 6% interest. Find the inflation rate and the real interest rate.',
            'steps': ['Inflation = (216 − 200)/200 × 100% = 8%.', 'Real interest ≈ 6% − 8% = −2%.', 'The saver\'s money buys less at the end of the year than at the start.'],
            'answer': 'Inflation is 8% and the real interest rate is about −2%.',
            'check': 'A negative real rate means saving loses purchasing power, which is why people move savings into assets when inflation is high.'},
        'mistakes': ['Taking the change in the index points (16) as the inflation rate without dividing.', 'Thinking a fall in inflation means prices are falling (that is deflation).', 'Subtracting the real rate from inflation the wrong way round.', 'Assuming a rise in one price is inflation.'],
        'real_world': 'In periods of very high inflation, such as Zimbabwe in 2008, prices changed so fast that money lost its function as a store of value and people switched to foreign currencies.',
        'exam_strategy': 'Distinguish clearly between "the price level" and "the inflation rate". A falling inflation rate still means prices are rising, just more slowly.',
        'recap': ['CPI tracks a fixed basket.', 'Inflation = % change in the CPI.', 'Real rate ≈ nominal − inflation.', 'Demand-pull vs cost-push.']},
    T4: {
        'overview': 'Unemployment counts people who want work and are actively looking but cannot find it. Its rate and its causes guide government policy on jobs.',
        'key_terms': ['Labour force', 'Unemployment rate', 'Participation rate', 'Frictional unemployment', 'Structural unemployment', 'Cyclical unemployment', 'Natural rate', 'Discouraged workers'],
        'explanation': [
            'The labour force is everyone employed plus everyone unemployed (without work, available and actively searching). The unemployment rate is unemployed ÷ labour force × 100%. The participation rate is the labour force as a share of the working-age population.',
            'Economists distinguish three types. Frictional unemployment is short spells between jobs while people search. Structural unemployment comes from a mismatch between workers\' skills or locations and the jobs available, for example when an industry declines. Cyclical unemployment rises in recessions when demand falls.',
            'The natural rate of unemployment is the frictional plus structural rate, the level when the economy is at full employment. The official rate understates hardship because discouraged workers who stop looking are not counted, and part-time workers who want full-time jobs (underemployment) count as employed.'],
        'formulas_label': 'Formulas',
        'formulas': ['Labour force = employed + unemployed', 'Unemployment rate = unemployed ÷ labour force × 100%', 'Participation rate = labour force ÷ working-age population × 100%', 'Natural rate = frictional + structural'],
        'steps': ['Find the labour force.', 'Compute the unemployment rate.', 'Classify the unemployment by its cause.', 'Match a policy to the cause.'],
        'worked_example': {
            'problem': 'A country has 1500 (thousand) people of working age; 900 are employed and 100 are unemployed. Find the unemployment and participation rates.',
            'steps': ['Labour force = 900 + 100 = 1000.', 'Unemployment rate = 100/1000 × 100% = 10%.', 'Participation rate = 1000/1500 × 100% ≈ 66.7%.'],
            'answer': 'Unemployment rate 10%; participation rate about 66.7%.',
            'check': 'The other 500 are outside the labour force (students, retirees, discouraged workers), so they appear in neither the numerator nor the labour force.'},
        'mistakes': ['Dividing by the whole population instead of the labour force.', 'Counting discouraged workers as unemployed.', 'Confusing structural with cyclical unemployment.', 'Thinking the natural rate is zero.'],
        'real_world': 'Many African economies have low measured unemployment but high underemployment and informal work, which is why youth employment programmes focus on skills and job quality, not only on headline unemployment.',
        'exam_strategy': 'Match the policy to the type: training and relocation help for structural unemployment, demand stimulus for cyclical, and job-matching services for frictional.',
        'recap': ['Rate = unemployed ÷ labour force.', 'Frictional, structural, cyclical.', 'Natural rate = frictional + structural.', 'Official figures miss discouraged workers and underemployment.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'C = 600, I = 150, G = 200, X = 100 and M = 120. GDP is:', ['930', '1170', '1050', '950'], 0, '600 + 150 + 200 + (100 − 120) = 930.', ans=930),
    Q(T1, 'Which is included in GDP?', ['A new house built this year', 'A state pension payment', 'Flour bought by a bakery', 'A used car sold this year'], 0, 'New housing is investment; the others are transfers, intermediate goods or second-hand sales.'),
    Q(T1, 'Imports are subtracted in the expenditure approach because:', ['they are counted in C, I and G but produced abroad', 'they reduce consumption', 'they are taxed', 'they are intermediate goods'], 0, 'Subtracting them leaves only domestic production.'),
    Q(T1, 'A farmer sells wheat to a miller for 100, the miller sells flour to a baker for 160, and the baker sells bread for 250. The contribution to GDP is:', ['250', '510', '160', '100'], 0, 'Only the final good counts: 250 (= value added 100 + 60 + 90).', ans=250),
    Q(T1, 'GDP per capita is:', ['GDP divided by population', 'GDP divided by the labour force', 'GDP minus taxes', 'GDP divided by prices'], 0, 'It measures output per person.'),
    Q(T1, 'Which is NOT counted in GDP?', ['Unpaid housework', 'Teachers\' salaries in state schools', 'Business spending on new machines', 'Exports of cocoa'], 0, 'Unpaid work has no market transaction.'),
    # T2
    Q(T2, 'Nominal GDP is 1100 and the deflator is 110. Real GDP is:', ['1000', '1210', '990', '1100'], 0, '1100 ÷ 110 × 100 = 1000.', ans=1000),
    Q(T2, 'Real GDP rises from 1000 to 1050. The growth rate is:', ['5%', '50%', '0.5%', '105%'], 0, '50/1000 × 100%.', ans=5),
    Q(T2, 'At 2% growth a year, real GDP doubles in about:', ['35 years', '20 years', '50 years', '70 years'], 0, 'Rule of 70: 70 ÷ 2 = 35.', ans=35),
    Q(T2, 'If prices double and output does not change, real GDP:', ['stays the same', 'doubles', 'halves', 'rises by 50%'], 0, 'Only nominal GDP doubles.'),
    Q(T2, 'A recession is commonly defined as:', ['two consecutive quarters of falling real GDP', 'any rise in unemployment', 'inflation above 10%', 'one month of lower output'], 0, 'This is the usual rule of thumb.'),
    Q(T2, 'Which is best for comparing living standards between countries?', ['Real GDP per capita', 'Nominal GDP', 'Total real GDP', 'Population'], 0, 'It adjusts for both prices and population size.'),
    # T3
    Q(T3, 'The CPI rises from 200 to 216. Inflation is:', ['8%', '16%', '216%', '1.08%'], 0, '16/200 × 100%.', ans=8),
    Q(T3, 'The nominal interest rate is 6% and inflation is 8%. The real interest rate is about:', ['−2%', '14%', '2%', '0.75%'], 0, '6% − 8%.', ans=-2),
    Q(T3, 'Inflation falls from 10% to 4%. Prices are:', ['still rising, but more slowly', 'falling', 'unchanged', 'rising faster'], 0, 'A lower positive inflation rate is not deflation.'),
    Q(T3, 'A sharp rise in oil prices causing general price rises is:', ['cost-push inflation', 'demand-pull inflation', 'deflation', 'structural unemployment'], 0, 'Higher production costs push prices up.'),
    Q(T3, 'Unexpected inflation tends to benefit:', ['borrowers with fixed-rate loans', 'lenders', 'people on fixed pensions', 'savers'], 0, 'They repay with money worth less than expected.'),
    Q(T3, 'A wage rises from 1000 to 1100 while the price index rises from 100 to 110. The real wage:', ['is unchanged', 'rises by 10%', 'falls by 10%', 'rises by 1%'], 0, '1100 ÷ 110 × 100 = 1000, the same as before.'),
    # T4
    Q(T4, '900 employed, 100 unemployed. The unemployment rate is:', ['10%', '11.1%', '9%', '100%'], 0, '100 ÷ 1000.', ans=10),
    Q(T4, 'Working-age population 1500, labour force 1000. The participation rate is about:', ['66.7%', '50%', '150%', '33.3%'], 0, '1000/1500 ≈ 0.667.'),
    Q(T4, 'A coal miner loses his job when mines close and lacks skills for the new tech jobs. This is:', ['structural unemployment', 'frictional unemployment', 'cyclical unemployment', 'seasonal unemployment'], 0, 'A mismatch between skills and available jobs.'),
    Q(T4, 'Unemployment that rises during a recession is:', ['cyclical', 'frictional', 'structural', 'natural'], 0, 'It follows the business cycle.'),
    Q(T4, 'A graduate spending two months searching for the right job is:', ['frictionally unemployed', 'structurally unemployed', 'cyclically unemployed', 'not in the labour force'], 0, 'Short-term search between jobs.'),
    Q(T4, 'Discouraged workers who stop looking for work are:', ['not counted as unemployed', 'counted as unemployed', 'counted as employed', 'counted twice'], 0, 'They leave the labour force, so the official rate understates hardship.'),
]

FLASH = [
    ['GDP (expenditure)', 'C + I + G + (X − M).'],
    ['Final vs intermediate goods', 'Only final goods count, to avoid double counting.'],
    ['Real GDP', 'Nominal GDP ÷ deflator × 100.'],
    ['Rule of 70', 'Doubling time ≈ 70 ÷ growth rate.'],
    ['Inflation rate', '(CPI₁ − CPI₀)/CPI₀ × 100%.'],
    ['Real interest rate', '≈ nominal rate − inflation.'],
    ['Unemployment rate', 'Unemployed ÷ labour force × 100%.'],
    ['Natural rate of unemployment', 'Frictional + structural.'],
]
