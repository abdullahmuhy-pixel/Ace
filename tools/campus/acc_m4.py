"""Financial Accounting I, module 4: Interpreting financial statements (ratio analysis)."""
from verify import Q, sp
T1, T2, T3, T4 = ('Profitability ratios', 'Liquidity ratios', 'Efficiency (working capital) ratios', 'Gearing and investor ratios')
R = sp.Rational
# figures from module 3: revenue 195 000, GP 80 000, NP 26 600, equity 74 000, loan 10 000, CA 71 000, inventory 25 000, CL 19 000, receivables 36 100, payables 15 000, purchases 120 000, COGS 115 000
gm, nm, roce = R(80000, 195000) * 100, R(26600, 195000) * 100, R(26600, 84000) * 100
cur, quick = R(71000, 19000), R(71000 - 25000, 19000)
inv_d, rec_d, pay_d = R(25000, 115000) * 365, R(36100, 195000) * 365, R(15000, 120000) * 365
gear = R(10000, 84000) * 100
assert [round(float(v), 1) for v in (gm, nm, roce, cur, quick, inv_d, rec_d, pay_d, gear)] == [41.0, 13.6, 31.7, 3.7, 2.4, 79.3, 67.6, 45.6, 11.9]
assert R(1000000, 2000000) == R(1, 2) and R(6, 1) / R(1, 2) == 12 and R(1, 2) / R(1, 5) == R(5, 2) and R(50000, 5000) == 10
ccc = inv_d + rec_d - pay_d
assert round(float(ccc)) == 101

MODULE = {
    'title': 'Interpreting financial statements',
    'topics': [T1, T2, T3, T4],
    'overview': 'Numbers in financial statements mean little on their own. Ratios turn them into comparable measures of profitability, liquidity, efficiency and financial risk, so users can compare a business with its past and with competitors. This module uses the statements from module 3 throughout.',
    'key_terms': ['Gross profit margin', 'Net profit margin', 'ROCE', 'Current ratio', 'Quick ratio', 'Inventory days', 'Receivable days', 'Payable days', 'Gearing', 'Earnings per share'],
    'explanation': [
        'A ratio is only useful in context. Compare it with the same business in earlier years, with competitors, or with an industry average, and always explain what might cause a change.',
        'Profitability ratios show how well sales and capital turn into profit. Liquidity ratios show whether the business can pay its short-term debts. Efficiency ratios show how quickly inventory sells and cash is collected and paid. Gearing shows how much the business relies on borrowing.',
        'Ratios have limits: they use historical figures, different accounting policies can distort comparisons, year-end figures may not be typical, and they show symptoms rather than causes. Good analysis combines several ratios with information about the business.'],
    'quick_facts': [
        'Gross margin = gross profit ÷ revenue × 100.',
        'ROCE = operating profit ÷ capital employed × 100.',
        'Current ratio = CA ÷ CL; quick ratio = (CA − inventory) ÷ CL.',
        'Receivable days = receivables ÷ credit sales × 365.',
        'Gearing = non-current debt ÷ (equity + non-current debt) × 100.'],
}

NOTES = {
    T1: {
        'overview': 'Profitability ratios measure how much profit a business earns relative to its sales and to the capital invested in it.',
        'key_terms': ['Gross profit margin', 'Net profit margin', 'Return on capital employed', 'Capital employed', 'Mark-up'],
        'explanation': [
            'Gross profit margin = gross profit ÷ revenue × 100 shows how much of each sale is left after the cost of the goods. It changes with selling prices, purchase costs and the mix of products sold.',
            'Net profit margin = net profit ÷ revenue × 100 also reflects overheads such as wages and rent. A stable gross margin with a falling net margin points to rising expenses.',
            'Return on capital employed (ROCE) = operating profit ÷ capital employed × 100, where capital employed = equity + non-current liabilities. It measures how well all long-term funds are used and can be compared with the interest rate the business pays or could earn elsewhere.'],
        'formulas_label': 'Formulas',
        'formulas': ['Gross margin = GP ÷ revenue × 100', 'Net margin = NP ÷ revenue × 100', 'ROCE = operating profit ÷ (equity + non-current liabilities) × 100', 'Mark-up = GP ÷ cost of sales × 100'],
        'steps': ['Take the figures from the statements.', 'Apply the formula.', 'Compare with last year or competitors.', 'Suggest reasons for differences.'],
        'worked_example': {
            'problem': 'Revenue 195 000, gross profit 80 000, net profit 26 600, equity 74 000, long-term loan 10 000. Find the gross margin, net margin and ROCE (treat net profit as operating profit; interest is ignored for simplicity).',
            'steps': ['Gross margin = 80 000 ÷ 195 000 × 100 ≈ 41.0%.', 'Net margin = 26 600 ÷ 195 000 × 100 ≈ 13.6%.', 'ROCE = 26 600 ÷ (74 000 + 10 000) × 100 ≈ 31.7%.'],
            'answer': 'Gross margin 41.0%, net margin 13.6%, ROCE 31.7%.',
            'check': 'Net margin is below gross margin, as it must be, because overheads are deducted.'},
        'mistakes': ['Dividing by cost of sales for margin (that is mark-up).', 'Using total assets instead of capital employed for ROCE without saying so.', 'Calculating ratios without interpreting them.', 'Comparing ratios computed in different ways.'],
        'real_world': 'Supermarkets typically run net margins of only a few per cent but very high sales volumes, while software firms can have net margins above 25%; comparisons only make sense within an industry.',
        'exam_strategy': 'For each ratio give the formula, the figures, the result to one decimal place, and one sentence of interpretation. The interpretation is often worth as much as the calculation.',
        'recap': ['Gross vs net margin.', 'ROCE uses capital employed.', 'Margin ≠ mark-up.', 'Always interpret.']},
    T2: {
        'overview': 'Liquidity ratios measure whether a business has enough short-term assets to pay its short-term debts as they fall due.',
        'key_terms': ['Current ratio', 'Quick (acid-test) ratio', 'Liquidity', 'Working capital', 'Overtrading'],
        'explanation': [
            'Current ratio = current assets ÷ current liabilities. A ratio around 1.5 to 2 is often seen as comfortable, but the right level depends on the industry: supermarkets with fast-selling inventory and cash sales often operate below 1.',
            'Quick ratio = (current assets − inventory) ÷ current liabilities. It excludes inventory, which may take time to sell. A quick ratio well below 1 can mean the business depends on selling stock to pay its bills.',
            'Very high ratios are not always good: they may mean too much cash sitting idle or slow-moving inventory and uncollected receivables. Overtrading, growing faster than working capital allows, shows as falling liquidity even while sales rise.'],
        'formulas_label': 'Formulas',
        'formulas': ['Current ratio = CA ÷ CL', 'Quick ratio = (CA − inventory) ÷ CL', 'Working capital = CA − CL'],
        'steps': ['Find current assets, inventory and current liabilities.', 'Compute both ratios.', 'Compare with the industry and previous years.', 'Comment on whether the level is too low or too high.'],
        'worked_example': {
            'problem': 'Current assets 71 000 (including inventory 25 000) and current liabilities 19 000. Find the current and quick ratios.',
            'steps': ['Current ratio = 71 000 ÷ 19 000 ≈ 3.7 : 1.', 'Quick ratio = (71 000 − 25 000) ÷ 19 000 = 46 000 ÷ 19 000 ≈ 2.4 : 1.', 'Both are well above 1.'],
            'answer': 'Current ratio 3.7 : 1, quick ratio 2.4 : 1: strong liquidity, possibly too much tied up in receivables.',
            'check': 'Receivables (36 100) are the largest current asset, which links to the efficiency ratios in the next topic.'},
        'mistakes': ['Including inventory in the quick ratio.', 'Saying a higher current ratio is always better.', 'Expressing the ratio as a percentage instead of x : 1.', 'Ignoring the industry context.'],
        'real_world': 'Lenders often write minimum current ratios into loan agreements (covenants); breaching them can let the bank demand early repayment.',
        'exam_strategy': 'Write liquidity ratios as "x : 1" and interpret both directions: too low (risk of not paying) and too high (idle resources).',
        'recap': ['Current = CA ÷ CL.', 'Quick excludes inventory.', 'Context matters.', 'Too high can be inefficient.']},
    T3: {
        'overview': 'Efficiency ratios measure how fast working capital moves: how long inventory sits, how long customers take to pay, and how long the business takes to pay suppliers.',
        'key_terms': ['Inventory days', 'Inventory turnover', 'Receivable days', 'Payable days', 'Cash conversion cycle'],
        'explanation': [
            'Inventory days = inventory ÷ cost of sales × 365: how many days of sales the inventory represents. Lower usually means fresher stock and less cash tied up, but too low risks running out.',
            'Receivable days = trade receivables ÷ credit sales × 365: the average time customers take to pay. Compare with the credit terms offered (for example 30 days). Payable days = trade payables ÷ credit purchases × 365: how long the business takes to pay its suppliers.',
            'The cash conversion cycle = inventory days + receivable days − payable days: how long cash is tied up between paying for goods and collecting from customers. Shortening it frees cash without borrowing.'],
        'formulas_label': 'Formulas',
        'formulas': ['Inventory days = inventory ÷ cost of sales × 365', 'Receivable days = receivables ÷ credit sales × 365', 'Payable days = payables ÷ credit purchases × 365', 'Cash cycle = inventory days + receivable days − payable days'],
        'steps': ['Use year-end (or average) balances.', 'Divide by the matching flow (cost of sales, sales or purchases).', 'Multiply by 365.', 'Compare with credit terms and the industry.'],
        'worked_example': {
            'problem': 'Inventory 25 000, cost of sales 115 000, receivables 36 100, sales 195 000 (all on credit), payables 15 000, purchases 120 000. Find the three ratios and the cash cycle.',
            'steps': ['Inventory days = 25 000 ÷ 115 000 × 365 ≈ 79 days.', 'Receivable days = 36 100 ÷ 195 000 × 365 ≈ 68 days; payable days = 15 000 ÷ 120 000 × 365 ≈ 46 days.', 'Cash cycle ≈ 79 + 68 − 46 ≈ 101 days.'],
            'answer': 'About 79, 68 and 46 days, and a cash cycle of about 101 days.',
            'check': 'If customers were given 30-day terms, 68 days shows weak credit control: chasing debts would free a lot of cash.'},
        'mistakes': ['Dividing inventory by sales instead of cost of sales.', 'Using cash sales in receivable days.', 'Thinking longer payable days are always good (suppliers may refuse credit).', 'Forgetting to multiply by 365.'],
        'real_world': 'Large retailers often have negative cash cycles: they sell goods for cash before they have to pay suppliers, so suppliers effectively finance their growth.',
        'exam_strategy': 'Link efficiency ratios to liquidity in your interpretation: slow receivables explain high current ratios and low cash.',
        'recap': ['Inventory days: stock holding.', 'Receivable days vs credit terms.', 'Payable days: supplier credit.', 'Cash cycle = inv + rec − pay.']},
    T4: {
        'overview': 'Gearing measures how much a business is financed by debt, and investor ratios measure returns to shareholders.',
        'key_terms': ['Gearing', 'Interest cover', 'Earnings per share', 'Price/earnings ratio', 'Dividend cover', 'Financial risk'],
        'explanation': [
            'Gearing = non-current debt ÷ (equity + non-current debt) × 100. High gearing means large interest commitments; it magnifies returns to owners when profits are good but increases the risk of failure when they fall. Interest cover = operating profit ÷ interest shows how comfortably interest can be paid.',
            'For companies, earnings per share (EPS) = profit for ordinary shareholders ÷ number of ordinary shares. The price/earnings (P/E) ratio = share price ÷ EPS shows how much investors pay for each unit of earnings; a high P/E suggests high expected growth.',
            'Dividend cover = EPS ÷ dividend per share shows how many times the dividend could be paid from earnings; low cover means the dividend may be at risk. Investors combine these with profitability and liquidity ratios before buying shares.'],
        'formulas_label': 'Formulas',
        'formulas': ['Gearing = non-current debt ÷ (equity + non-current debt) × 100', 'Interest cover = operating profit ÷ interest', 'EPS = profit for ordinary shareholders ÷ number of shares', 'P/E = share price ÷ EPS', 'Dividend cover = EPS ÷ dividend per share'],
        'steps': ['Find debt, equity, profit, interest and share data.', 'Compute the ratios.', 'Judge the level of financial risk.', 'Interpret from an investor\'s point of view.'],
        'worked_example': {
            'problem': 'A company earns profit of 1 000 000 for ordinary shareholders on 2 000 000 shares. The share price is 6 and the dividend is 0.20 per share. Find EPS, P/E and dividend cover.',
            'steps': ['EPS = 1 000 000 ÷ 2 000 000 = 0.50.', 'P/E = 6 ÷ 0.50 = 12.', 'Dividend cover = 0.50 ÷ 0.20 = 2.5 times.'],
            'answer': 'EPS 0.50, P/E 12, dividend cover 2.5.',
            'check': 'A cover of 2.5 means the company pays out 40% of earnings and keeps 60% for reinvestment.'},
        'mistakes': ['Using total liabilities instead of non-current debt in gearing.', 'Inverting the P/E ratio.', 'Assuming high gearing is always bad.', 'Ignoring interest cover when judging debt.'],
        'real_world': 'Stock exchanges in Lagos, Johannesburg and Nairobi publish P/E ratios daily; investors compare them across similar companies to judge whether shares look cheap or expensive.',
        'exam_strategy': 'When discussing gearing, mention both sides: debt is often cheaper than equity and boosts returns, but it adds fixed interest costs and risk.',
        'recap': ['Gearing: reliance on debt.', 'Interest cover: safety of interest.', 'EPS, P/E, dividend cover for investors.', 'Debt magnifies gains and losses.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Gross profit 80 000 on revenue 195 000. Gross margin, to 1 d.p., is:', ['41.0%', '69.6%', '13.6%', '58.9%'], 0, '80 000 ÷ 195 000 × 100.'),
    Q(T1, 'Net profit 26 600 on revenue 195 000. Net margin, to 1 d.p., is:', ['13.6%', '33.3%', '41.0%', '26.6%'], 0, '26 600 ÷ 195 000 × 100.'),
    Q(T1, 'Net profit 26 600, equity 74 000 and loan 10 000. ROCE, to 1 d.p., is:', ['31.7%', '35.9%', '266.0%', '13.6%'], 0, '26 600 ÷ 84 000 × 100.'),
    Q(T1, 'Gross profit 80 000 and cost of sales 115 000. Mark-up, to 1 d.p., is:', ['69.6%', '41.0%', '143.8%', '30.4%'], 0, '80 000 ÷ 115 000 × 100.'),
    Q(T1, 'Gross margin stays at 41% but net margin falls from 16% to 12%. The most likely cause is:', ['higher operating expenses', 'lower selling prices', 'higher purchase costs', 'more sales returns'], 0, 'Those would change gross margin too.'),
    Q(T1, 'Capital employed for ROCE is usually:', ['equity + non-current liabilities', 'current assets − current liabilities', 'total assets + total liabilities', 'equity only'], 0, 'All long-term funds.'),
    # T2
    Q(T2, 'Current assets 71 000 and current liabilities 19 000. The current ratio is about:', ['3.7 : 1', '2.4 : 1', '0.27 : 1', '52 : 1'], 0, '71 000 ÷ 19 000.'),
    Q(T2, 'In the same business, inventory is 25 000. The quick ratio is about:', ['2.4 : 1', '3.7 : 1', '1.3 : 1', '0.4 : 1'], 0, '46 000 ÷ 19 000.'),
    Q(T2, 'The quick ratio excludes inventory because:', ['inventory may take time to turn into cash', 'inventory has no value', 'inventory is a liability', 'it is a non-current asset'], 0, 'It is the least liquid current asset.'),
    Q(T2, 'A very high current ratio may indicate:', ['idle cash or slow-moving inventory and receivables', 'imminent insolvency', 'high gearing', 'falling sales'], 0, 'Resources may be under-used.'),
    Q(T2, 'Current assets 30 000 and current liabilities 40 000. Working capital is:', ['−10000', '10000', '70000', '0.75'], 0, '30 000 − 40 000.', ans=-10000),
    Q(T2, 'Overtrading typically shows as:', ['rapidly rising sales with falling liquidity', 'falling sales and rising cash', 'low gearing', 'a high quick ratio'], 0, 'Growth outruns the working capital to support it.'),
    # T3
    Q(T3, 'Inventory 25 000 and cost of sales 115 000. Inventory days, to the nearest day, are:', ['79', '47', '68', '46'], 0, '25 000 ÷ 115 000 × 365 ≈ 79.3.', ans=round(float(inv_d))),
    Q(T3, 'Receivables 36 100 and credit sales 195 000. Receivable days, to the nearest day, are:', ['68', '79', '46', '30'], 0, '36 100 ÷ 195 000 × 365 ≈ 67.6.', ans=round(float(rec_d))),
    Q(T3, 'Payables 15 000 and credit purchases 120 000. Payable days, to the nearest day, are:', ['46', '68', '79', '125'], 0, '15 000 ÷ 120 000 × 365 ≈ 45.6.', ans=round(float(pay_d))),
    Q(T3, 'With inventory days 79, receivable days 68 and payable days 46, the cash cycle is about:', ['101 days', '193 days', '57 days', '147 days'], 0, '79 + 68 − 46.'),
    Q(T3, 'Customers are given 30 days\' credit but receivable days are 68. This suggests:', ['weak credit control', 'excellent credit control', 'high gearing', 'high inventory'], 0, 'Customers pay much later than agreed.'),
    Q(T3, 'Which change shortens the cash conversion cycle?', ['Collecting from customers faster', 'Holding more inventory', 'Paying suppliers sooner', 'Giving longer credit to customers'], 0, 'Fewer receivable days.'),
    # T4
    Q(T4, 'Loan 10 000 and equity 74 000. Gearing, to 1 d.p., is:', ['11.9%', '13.5%', '88.1%', '7.4%'], 0, '10 000 ÷ 84 000 × 100.'),
    Q(T4, 'Profit 1 000 000 and 2 000 000 shares. EPS is:', ['0.50', '2.00', '0.20', '1.00'], 0, '1 000 000 ÷ 2 000 000.', ans=R(1, 2)),
    Q(T4, 'Share price 6 and EPS 0.50. The P/E ratio is:', ['12', '3', '0.083', '6.5'], 0, '6 ÷ 0.50.', ans=12),
    Q(T4, 'EPS 0.50 and dividend 0.20 per share. Dividend cover is:', ['2.5', '0.4', '0.3', '10'], 0, '0.50 ÷ 0.20.', ans=R(5, 2)),
    Q(T4, 'Operating profit 50 000 and interest 5 000. Interest cover is:', ['10 times', '0.1 times', '45 times', '5 times'], 0, '50 000 ÷ 5 000.'),
    Q(T4, 'High gearing means:', ['returns to owners are magnified and financial risk is higher', 'the business has no debt', 'liquidity is always strong', 'profit margins are high'], 0, 'Fixed interest must be paid whatever profits are.'),
]

FLASH = [
    ['Gross margin', 'GP ÷ revenue × 100.'],
    ['ROCE', 'Operating profit ÷ (equity + non-current liabilities) × 100.'],
    ['Current ratio', 'Current assets ÷ current liabilities.'],
    ['Quick ratio', '(Current assets − inventory) ÷ current liabilities.'],
    ['Receivable days', 'Receivables ÷ credit sales × 365.'],
    ['Cash conversion cycle', 'Inventory days + receivable days − payable days.'],
    ['Gearing', 'Non-current debt ÷ (equity + non-current debt) × 100.'],
    ['P/E ratio', 'Share price ÷ EPS.'],
]
