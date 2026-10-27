"""Financial Accounting I, module 2: Period-end adjustments."""
from verify import Q, sp
T1, T2, T3, T4 = ('Accruals and prepayments', 'Depreciation of non-current assets', 'Inventory valuation', 'Irrecoverable debts and allowances')
R = sp.Rational
assert 13000 - 1000 == 12000 and 46000 + 4000 == 50000
sl = (50000 - 5000) / 5
assert sl == 9000 and 50000 - 2 * sl == 32000
rb1 = 50000 * R(2, 10); rb2 = (50000 - rb1) * R(2, 10)
assert (rb1, rb2, 50000 - rb1 - rb2) == (10000, 8000, 32000)
assert 30000 - (50000 - 18000) == -2000
fifo_cogs = 100 * 10 + 50 * 12; avg = R(100 * 10 + 100 * 12, 200)
assert (fifo_cogs, 50 * 12, avg, 150 * avg, 50 * avg) == (1600, 600, 11, 1650, 550)
allow = (40000 - 2000) * R(5, 100)
assert allow == 1900 and allow - 1500 == 400 and 2000 + 400 == 2400

MODULE = {
    'title': 'Period-end adjustments',
    'topics': [T1, T2, T3, T4],
    'overview': 'A trial balance shows cash and recorded transactions, but profit must reflect what was really earned and used in the period. This module covers the adjustments made at the end of each period: accruals and prepayments, depreciation of long-lived assets, valuing closing inventory, and allowing for customers who will not pay.',
    'key_terms': ['Accrued expense', 'Prepayment', 'Accrued income', 'Depreciation', 'Carrying amount', 'Residual value', 'FIFO', 'Weighted average cost', 'Net realisable value', 'Allowance for receivables'],
    'explanation': [
        'Every adjustment applies the accruals concept: expenses and income are matched to the period they belong to. Each adjustment changes both the income statement (profit) and the statement of financial position (an asset or a liability).',
        'Depreciation spreads the cost of a non-current asset over its useful life. Inventory at the year end is valued at the lower of cost and net realisable value, and the cost formula chosen (FIFO or weighted average) affects both closing inventory and cost of sales.',
        'Customers who will clearly never pay are written off as irrecoverable debts, and an allowance is made for those who may not pay. Prudence applies: assets should not be overstated.'],
    'quick_facts': [
        'Expense = paid + closing accrual − opening accrual − closing prepayment + opening prepayment.',
        'Straight line: (cost − residual) ÷ useful life.',
        'Reducing balance: rate × carrying amount.',
        'Inventory: lower of cost and net realisable value.',
        'Allowance change, not the whole allowance, goes to the income statement each year.'],
}

NOTES = {
    T1: {
        'overview': 'Accruals and prepayments adjust expenses and income so that each period shows what it actually used or earned, not just what was paid or received in cash.',
        'key_terms': ['Accrued expense', 'Prepaid expense', 'Accrued income', 'Deferred income', 'Matching'],
        'explanation': [
            'An accrued expense is a cost incurred but not yet paid at the year end, such as wages owed for the last week. Add it to the expense and show it as a current liability.',
            'A prepayment is a cost paid in advance for a future period, such as rent paid for next year. Remove it from this year\'s expense and show it as a current asset.',
            'The same logic applies to income: income earned but not received (accrued income) is added and shown as an asset; income received in advance (deferred income) is removed and shown as a liability.'],
        'formulas_label': 'Formulas',
        'formulas': ['Expense = cash paid + closing accrual − closing prepayment', '(with opening balances: − opening accrual + opening prepayment)', 'Accrued expense: current liability', 'Prepayment: current asset'],
        'steps': ['Find the cash paid or received in the period.', 'Identify amounts owing or paid in advance at the year end.', 'Adjust to the amount for the period only.', 'Show the balance in the statement of financial position.'],
        'worked_example': {
            'problem': 'A business with a 31 December year end pays 13 000 rent during the year; the monthly rent is 1 000, and the payment includes January next year. It also paid wages of 46 000, with 4 000 still owing at year end. Find the expenses.',
            'steps': ['Rent: 13 000 paid, but 1 000 is for next year (a prepayment), so the expense is 12 000.', 'Wages: 46 000 paid plus 4 000 owing (an accrual), so the expense is 50 000.', 'Show a prepayment asset of 1 000 and an accrued liability of 4 000.'],
            'answer': 'Rent expense 12 000; wages expense 50 000.',
            'check': 'Rent of 1 000 × 12 months = 12 000 ✓.'},
        'mistakes': ['Adding a prepayment to the expense instead of deducting it.', 'Showing an accrual as an asset.', 'Ignoring opening accruals and prepayments from last year.', 'Confusing accrued income with deferred income.'],
        'real_world': 'Annual software subscriptions are paid up front but expensed month by month; the unexpired part sits on the statement of financial position as a prepayment.',
        'exam_strategy': 'Use a ledger account or a one-line calculation for each expense, and state both the income statement figure and the balance sheet item.',
        'recap': ['Accrual: owing, add to expense, liability.', 'Prepayment: paid ahead, deduct, asset.', 'Same idea for income.', 'Match to the period.']},
    T2: {
        'overview': 'Depreciation allocates the cost of a non-current asset, such as machinery or vehicles, over the years it is used. It is an expense even though no cash is paid.',
        'key_terms': ['Depreciation', 'Straight-line method', 'Reducing-balance method', 'Residual value', 'Useful life', 'Accumulated depreciation', 'Carrying amount', 'Disposal'],
        'explanation': [
            'Straight-line depreciation charges the same amount each year: (cost − residual value) ÷ useful life. A machine costing 50 000 with residual value 5 000 and a 5-year life is depreciated by 9 000 a year.',
            'Reducing-balance depreciation charges a fixed percentage of the carrying amount each year, giving larger charges early on. At 20%, the same machine is depreciated by 10 000 in year 1 and 8 000 in year 2. It suits assets that lose value quickly, such as vehicles.',
            'Accumulated depreciation is shown against the asset\'s cost; cost minus accumulated depreciation is the carrying amount. On disposal, compare the sale proceeds with the carrying amount: a higher price gives a profit, a lower price a loss on disposal.'],
        'formulas_label': 'Formulas',
        'formulas': ['Straight line = (cost − residual value) ÷ useful life', 'Reducing balance = rate × opening carrying amount', 'Carrying amount = cost − accumulated depreciation', 'Profit/loss on disposal = proceeds − carrying amount'],
        'steps': ['Choose the method stated.', 'Compute each year\'s charge.', 'Accumulate the depreciation.', 'Find the carrying amount, and the gain or loss on any disposal.'],
        'worked_example': {
            'problem': 'A machine costs 50 000 with a residual value of 5 000 and a 5-year life. Find the straight-line charge and the carrying amount after 2 years. It is then sold for 30 000 when accumulated depreciation is 18 000. Find the profit or loss.',
            'steps': ['Charge = (50 000 − 5 000) ÷ 5 = 9 000 a year.', 'After 2 years: 50 000 − 18 000 = 32 000.', 'Disposal: 30 000 − 32 000 = −2 000.'],
            'answer': 'Depreciation 9 000 a year; carrying amount 32 000; loss on disposal 2 000.',
            'check': 'Reducing balance at 20% happens to give the same carrying amount after 2 years: 50 000 − 10 000 − 8 000 = 32 000.'},
        'mistakes': ['Forgetting to subtract the residual value in straight line.', 'Applying the reducing-balance rate to cost every year.', 'Treating depreciation as a cash outflow.', 'Comparing proceeds with cost instead of carrying amount on disposal.'],
        'real_world': 'Delivery companies use reducing-balance depreciation for vans because their value drops sharply in the first years, which matches the charge to their real fall in value.',
        'exam_strategy': 'Lay out a small depreciation schedule (year, opening amount, charge, closing amount). It makes multi-year questions and disposals easy to follow.',
        'recap': ['Straight line: equal charges.', 'Reducing balance: % of carrying amount.', 'Carrying amount = cost − accumulated depreciation.', 'Disposal: proceeds vs carrying amount.']},
    T3: {
        'overview': 'Closing inventory must be valued to work out cost of sales and profit. The rules are the lower of cost and net realisable value, with cost found by FIFO or weighted average.',
        'key_terms': ['Cost of sales', 'Closing inventory', 'FIFO', 'Weighted average cost', 'Net realisable value', 'Periodic vs perpetual'],
        'explanation': [
            'Cost of sales = opening inventory + purchases − closing inventory. So the value placed on closing inventory directly affects profit: overstating it overstates profit.',
            'When prices change, the cost formula matters. FIFO (first in, first out) assumes the oldest goods are sold first, so closing inventory reflects the latest prices. Weighted average cost uses the average price of all units available. LIFO is not allowed under IFRS.',
            'Inventory is valued at the lower of cost and net realisable value (NRV), the expected selling price less costs to complete and sell. Damaged or obsolete goods may have an NRV below cost and must be written down. This applies prudence.'],
        'formulas_label': 'Formulas',
        'formulas': ['Cost of sales = opening inventory + purchases − closing inventory', 'FIFO: oldest costs go to cost of sales first', 'Weighted average = total cost ÷ total units', 'Value = lower of cost and NRV'],
        'steps': ['List purchases in date order with units and prices.', 'Allocate units sold by FIFO or the average cost.', 'Value the units left.', 'Compare with NRV and take the lower.'],
        'worked_example': {
            'problem': 'A shop buys 100 units at 10, then 100 at 12, and sells 150. Find cost of sales and closing inventory by FIFO and weighted average.',
            'steps': ['FIFO: cost of sales = 100 × 10 + 50 × 12 = 1600; closing = 50 × 12 = 600.', 'Average cost = (1000 + 1200) ÷ 200 = 11 per unit.', 'Weighted average: cost of sales = 150 × 11 = 1650; closing = 50 × 11 = 550.'],
            'answer': 'FIFO: cost of sales 1600, closing inventory 600. Weighted average: 1650 and 550.',
            'check': 'In both methods cost of sales + closing inventory = 2200, the total cost of goods bought ✓.'},
        'mistakes': ['Applying FIFO backwards (selling the newest first).', 'Forgetting to compare with net realisable value.', 'Using the selling price as the inventory value.', 'Treating closing inventory as an expense.'],
        'real_world': 'When fuel prices rise, FIFO shows higher profits for fuel retailers than the average-cost method, because cheaper older stock is charged to cost of sales first.',
        'exam_strategy': 'Show a units-and-cost table for each method. Check that cost of sales plus closing inventory equals total cost available; it catches most slips.',
        'recap': ['Closing inventory affects profit.', 'FIFO vs weighted average.', 'Lower of cost and NRV.', 'Cost of sales + closing inventory = cost available.']},
    T4: {
        'overview': 'Not every customer pays. Debts that will definitely not be collected are written off, and an allowance is made for those that might not be, so that receivables are not overstated.',
        'key_terms': ['Trade receivables', 'Irrecoverable (bad) debt', 'Allowance for receivables', 'Debt recovered', 'Net receivables'],
        'explanation': [
            'An irrecoverable debt (for example a customer who has gone bankrupt) is written off: debit Irrecoverable debts expense and credit Receivables. Profit falls and receivables fall.',
            'An allowance for receivables estimates the part of the remaining receivables that may not be collected, often as a percentage. Only the change in the allowance each year goes to the income statement: an increase is an expense, a decrease is income. The allowance is deducted from receivables in the statement of financial position.',
            'If a debt previously written off is later paid, it is recorded as a recovery (income). Allowances apply prudence and the accruals concept: the cost of credit sales that will not be collected is recognised in the same period as the sales.'],
        'formulas_label': 'Formulas',
        'formulas': ['Write-off: Dr Irrecoverable debts, Cr Receivables', 'Allowance = % × receivables after write-offs', 'Income statement charge = write-offs + increase in allowance', 'Net receivables = receivables − allowance'],
        'steps': ['Write off known bad debts first.', 'Compute the new allowance on the remaining receivables.', 'Find the change from last year\'s allowance.', 'Show the charge and the net receivables.'],
        'worked_example': {
            'problem': 'Receivables are 40 000 before adjustments. A 2 000 debt is irrecoverable. The allowance is to be 5% of the remaining receivables; last year it was 1 500. Find the total charge to the income statement and the net receivables.',
            'steps': ['Write off 2 000: receivables become 38 000.', 'New allowance = 5% × 38 000 = 1 900; increase = 1 900 − 1 500 = 400.', 'Total charge = 2 000 + 400 = 2 400.'],
            'answer': 'Charge 2 400; net receivables 38 000 − 1 900 = 36 100.',
            'check': 'Only the 400 increase goes to the income statement, not the whole 1 900 ✓.'},
        'mistakes': ['Calculating the allowance before writing off irrecoverable debts.', 'Charging the whole allowance every year instead of the change.', 'Adding the allowance to receivables.', 'Treating a decrease in the allowance as an expense.'],
        'real_world': 'Banks and mobile-lending apps set aside allowances for expected loan losses; changes in those allowances move their reported profits significantly in downturns.',
        'exam_strategy': 'Do the steps in order (write off, then allowance, then change) and label each line. Order errors are the most common source of lost marks here.',
        'recap': ['Write off definite bad debts.', 'Allowance on what remains.', 'Charge only the change in allowance.', 'Net receivables = receivables − allowance.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Rent paid 13 000 includes 1 000 for next year. The rent expense for this year is:', ['12000', '13000', '14000', '1000'], 0, 'Deduct the prepayment.', ans=12000),
    Q(T1, 'Wages paid 46 000 and 4 000 owing at year end. The wages expense is:', ['50000', '42000', '46000', '4000'], 0, 'Add the accrual.', ans=50000),
    Q(T1, 'An accrued expense appears in the statement of financial position as:', ['a current liability', 'a current asset', 'equity', 'a non-current asset'], 0, 'It is an amount owed.'),
    Q(T1, 'A prepayment appears as:', ['a current asset', 'a current liability', 'income', 'an expense'], 0, 'The business has paid for a future benefit.'),
    Q(T1, 'Commission earned this year but received next year is:', ['accrued income (an asset)', 'deferred income (a liability)', 'a prepayment', 'an expense'], 0, 'Income earned but not yet received.'),
    Q(T1, 'Insurance paid 9 000; opening prepayment 1 000; closing prepayment 2 000. The expense is:', ['8000', '9000', '10000', '12000'], 0, '9 000 + 1 000 − 2 000.', ans=8000),
    # T2
    Q(T2, 'Cost 50 000, residual value 5 000, life 5 years. Straight-line depreciation per year is:', ['9000', '10000', '11000', '45000'], 0, '(50 000 − 5 000) ÷ 5.', ans=9000),
    Q(T2, 'Cost 50 000 at 20% reducing balance. Year 2 depreciation is:', ['8000', '10000', '6400', '9000'], 0, 'Year 1: 10 000; year 2: 20% × 40 000.', ans=rb2),
    Q(T2, 'Carrying amount equals:', ['cost − accumulated depreciation', 'cost + depreciation', 'market value', 'sale proceeds'], 0, 'It is shown in the statement of financial position.'),
    Q(T2, 'Carrying amount 32 000, sold for 30 000. The result is:', ['a loss of 2000', 'a profit of 2000', 'a profit of 30000', 'no gain or loss'], 0, 'Proceeds below carrying amount.'),
    Q(T2, 'Reducing-balance depreciation gives:', ['higher charges in early years', 'equal charges every year', 'higher charges in later years', 'no charge'], 0, 'The rate applies to a shrinking carrying amount.'),
    Q(T2, 'Depreciation is best described as:', ['allocating an asset\'s cost over its useful life', 'saving cash to replace the asset', 'the fall in market value', 'a cash payment'], 0, 'It is a non-cash expense.'),
    # T3
    Q(T3, 'Buy 100 at 10, then 100 at 12; sell 150. FIFO cost of sales is:', ['1600', '1650', '1800', '1500'], 0, '100 × 10 + 50 × 12.', ans=fifo_cogs),
    Q(T3, 'In the same case, FIFO closing inventory is:', ['600', '550', '500', '1000'], 0, '50 × 12.', ans=600),
    Q(T3, 'In the same case, weighted average closing inventory is:', ['550', '600', '500', '1100'], 0, 'Average 11 × 50.', ans=550),
    Q(T3, 'Goods cost 600 but can only be sold for 520 after 20 of selling costs. They are valued at:', ['500', '600', '520', '620'], 0, 'NRV = 520 − 20 = 500 < cost.', ans=500),
    Q(T3, 'Opening inventory 5 000, purchases 30 000, closing inventory 8 000. Cost of sales is:', ['27000', '35000', '43000', '22000'], 0, '5 000 + 30 000 − 8 000.', ans=27000),
    Q(T3, 'Overstating closing inventory will:', ['overstate profit', 'understate profit', 'not affect profit', 'reduce assets'], 0, 'Cost of sales is understated.'),
    # T4
    Q(T4, 'Writing off an irrecoverable debt is recorded as:', ['Dr Irrecoverable debts, Cr Receivables', 'Dr Receivables, Cr Irrecoverable debts', 'Dr Cash, Cr Receivables', 'Dr Sales, Cr Receivables'], 0, 'An expense up, an asset down.'),
    Q(T4, 'Receivables 38 000 after write-offs; allowance 5%. The allowance is:', ['1900', '2000', '1500', '400'], 0, '5% × 38 000.', ans=allow),
    Q(T4, 'Last year\'s allowance was 1 500 and this year\'s is 1 900. The income statement charge for the allowance is:', ['400', '1900', '1500', '3400'], 0, 'Only the increase.', ans=400),
    Q(T4, 'Write-offs 2 000 and allowance increase 400. Total charge is:', ['2400', '2000', '1900', '3900'], 0, '2 000 + 400.', ans=2400),
    Q(T4, 'Net receivables shown are 38 000 less an allowance of 1 900:', ['36100', '38000', '39900', '1900'], 0, '38 000 − 1 900.', ans=36100),
    Q(T4, 'If the allowance falls from 2 000 to 1 600, the 400 difference is:', ['income in the income statement', 'an expense', 'a liability', 'ignored'], 0, 'A decrease in the allowance increases profit.'),
]

FLASH = [
    ['Accrued expense', 'Incurred but unpaid; add to expense; current liability.'],
    ['Prepayment', 'Paid in advance; deduct from expense; current asset.'],
    ['Straight-line depreciation', '(Cost − residual) ÷ useful life.'],
    ['Reducing balance', 'Rate × opening carrying amount.'],
    ['Disposal', 'Proceeds − carrying amount = profit or loss.'],
    ['Inventory rule', 'Lower of cost and net realisable value.'],
    ['FIFO', 'Oldest costs go to cost of sales first.'],
    ['Allowance for receivables', 'Only the change goes to the income statement.'],
]
