"""Financial Accounting I, module 3: Financial statements and the bank."""
from verify import Q, sp
T1, T2, T3, T4 = ('The income statement', 'The statement of financial position', 'The statement of cash flows', 'Bank reconciliation')
net_sales = 200000 - 5000
cogs = 20000 + 120000 - 25000
gp = net_sales - cogs
exp = 30000 + 12000 + 9000 + 2400
np_ = gp - exp
assert (net_sales, cogs, gp, exp, np_) == (195000, 115000, 80000, 53400, 26600)
nca = 50000 - 18000
ca = 25000 + 36100 + 1000 + 8900
cl, ncl = 15000 + 4000, 10000
eq = nca + ca - cl - ncl
assert (nca, ca, nca + ca, cl, eq) == (32000, 71000, 103000, 19000, 74000) and 60000 + np_ - 12600 == eq
cfo = 26600 + 9000 - 5000 - 4000 + 3000
assert cfo == 29600
assert 4500 - 50 + 250 == 4700 == 5200 + 900 - 1400

MODULE = {
    'title': 'Financial statements and the bank',
    'topics': [T1, T2, T3, T4],
    'overview': 'The financial statements are the end product of the accounting process. This module shows how to prepare and read the income statement (performance), the statement of financial position (position), and the statement of cash flows (liquidity), and how to reconcile the business\'s cash records with the bank statement.',
    'key_terms': ['Revenue', 'Cost of sales', 'Gross profit', 'Net profit', 'Statement of financial position', 'Working capital', 'Operating activities', 'Investing activities', 'Financing activities', 'Bank reconciliation'],
    'explanation': [
        'The income statement covers a period and shows revenue less expenses, first gross profit (sales minus cost of sales) and then net profit after operating expenses. The statement of financial position is a snapshot at the period end showing assets, liabilities and equity.',
        'Profit is not the same as cash. The statement of cash flows explains the change in cash, split into operating, investing and financing activities, and shows whether the business generates enough cash from its trading.',
        'A bank reconciliation explains differences between the cash book and the bank statement, for example cheques not yet presented or bank charges not yet recorded. It catches errors and fraud and confirms the true cash balance.'],
    'quick_facts': [
        'Gross profit = revenue − cost of sales.',
        'Net profit = gross profit + other income − expenses.',
        'Net assets = total assets − total liabilities = equity.',
        'Indirect method: profit + depreciation ± working-capital changes = operating cash flow.',
        'Update the cash book for items the bank knows about; adjust the bank balance for timing items.'],
}

NOTES = {
    T1: {
        'overview': 'The income statement measures performance over a period: revenue earned less the expenses incurred to earn it.',
        'key_terms': ['Revenue', 'Sales returns', 'Cost of sales', 'Gross profit', 'Operating expenses', 'Net profit', 'Other income'],
        'explanation': [
            'Start with net revenue: sales less sales returns. Cost of sales = opening inventory + purchases (less purchase returns, plus carriage inwards) − closing inventory. Gross profit is net revenue minus cost of sales, the profit from buying and selling before overheads.',
            'Then deduct operating expenses (wages, rent, utilities, depreciation, irrecoverable debts, carriage outwards) and add other income (rent received, discounts received, interest) to reach net profit for the year.',
            'All adjustments from module 2 flow into this statement: accruals and prepayments change expenses, depreciation is an expense, closing inventory reduces cost of sales, and changes in the allowance for receivables are expenses or income.'],
        'formulas_label': 'Layout',
        'formulas': ['Net revenue = sales − sales returns', 'Cost of sales = opening inventory + net purchases + carriage inwards − closing inventory', 'Gross profit = net revenue − cost of sales', 'Net profit = gross profit + other income − expenses'],
        'steps': ['Compute net revenue.', 'Compute cost of sales.', 'Find gross profit.', 'List and total expenses (after adjustments).', 'Find net profit.'],
        'worked_example': {
            'problem': 'Sales 200 000, sales returns 5 000, opening inventory 20 000, purchases 120 000, closing inventory 25 000. Expenses: wages 30 000, rent 12 000, depreciation 9 000, irrecoverable debts 2 400. Find gross and net profit.',
            'steps': ['Net revenue = 200 000 − 5 000 = 195 000.', 'Cost of sales = 20 000 + 120 000 − 25 000 = 115 000, so gross profit = 80 000.', 'Expenses = 30 000 + 12 000 + 9 000 + 2 400 = 53 400, so net profit = 26 600.'],
            'answer': 'Gross profit 80 000; net profit 26 600.',
            'check': 'Gross margin = 80 000/195 000 ≈ 41%, net margin ≈ 13.6%: plausible for a small retailer.'},
        'mistakes': ['Putting carriage outwards in cost of sales (it is an expense).', 'Adding closing inventory instead of deducting it.', 'Including drawings as an expense.', 'Including the cost of a new asset as an expense.'],
        'real_world': 'Listed companies publish income statements every half-year; analysts focus on gross margin to judge pricing power and on net margin to judge cost control.',
        'exam_strategy': 'Use the standard vertical layout with clear subtotals for net revenue, cost of sales, gross profit and expenses. Layout and labels are marked.',
        'recap': ['Net revenue − cost of sales = gross profit.', 'Gross profit − expenses + other income = net profit.', 'Adjustments flow in.', 'No drawings or capital items.']},
    T2: {
        'overview': 'The statement of financial position (balance sheet) shows what the business owns and owes at a point in time. It is the accounting equation in detail.',
        'key_terms': ['Non-current assets', 'Current assets', 'Current liabilities', 'Non-current liabilities', 'Working capital', 'Equity', 'Net assets'],
        'explanation': [
            'Non-current assets (property, equipment, vehicles) are shown at cost less accumulated depreciation. Current assets are listed in order of liquidity: inventory, receivables (net of the allowance), prepayments and cash.',
            'Current liabilities are due within a year: payables, accruals and overdrafts. Non-current liabilities include long-term loans. Net current assets (working capital) = current assets − current liabilities.',
            'Equity for a sole trader = opening capital + capital introduced + net profit − drawings. The statement balances when total assets − total liabilities (net assets) equals equity.'],
        'formulas_label': 'Layout',
        'formulas': ['Non-current assets at carrying amount', 'Working capital = current assets − current liabilities', 'Net assets = total assets − total liabilities', 'Equity = capital + profit − drawings = net assets'],
        'steps': ['List non-current assets at carrying amount.', 'List and total current assets.', 'List current and non-current liabilities.', 'Compute net assets.', 'Prepare the equity section and check it agrees.'],
        'worked_example': {
            'problem': 'Equipment cost 50 000, accumulated depreciation 18 000; inventory 25 000, net receivables 36 100, prepayment 1 000, cash 8 900; payables 15 000, accruals 4 000; bank loan (5 years) 10 000. Opening capital 60 000, profit 26 600, drawings 12 600. Prepare the key totals.',
            'steps': ['Non-current assets 32 000; current assets 71 000; total assets 103 000.', 'Current liabilities 19 000; non-current liabilities 10 000; net assets = 103 000 − 29 000 = 74 000.', 'Equity = 60 000 + 26 600 − 12 600 = 74 000.'],
            'answer': 'Net assets 74 000 = equity 74 000; working capital 71 000 − 19 000 = 52 000.',
            'check': 'The two totals agree, so the statement balances ✓.'},
        'mistakes': ['Showing receivables gross instead of net of the allowance.', 'Putting a long-term loan in current liabilities.', 'Adding drawings to equity.', 'Showing non-current assets at cost without depreciation.'],
        'real_world': 'Suppliers check a customer\'s working capital before granting credit; a business with more current liabilities than current assets may struggle to pay on time.',
        'exam_strategy': 'Always show the equity reconciliation (capital + profit − drawings). If the statement does not balance, the difference often points straight to the error.',
        'recap': ['Assets: non-current then current.', 'Liabilities: current then non-current.', 'Working capital = CA − CL.', 'Net assets = equity.']},
    T3: {
        'overview': 'The statement of cash flows explains how cash changed during the period, split into operating, investing and financing activities. It shows whether profits are turning into cash.',
        'key_terms': ['Operating activities', 'Investing activities', 'Financing activities', 'Indirect method', 'Working capital changes', 'Non-cash items'],
        'explanation': [
            'Operating cash flow (indirect method) starts with profit and adds back non-cash expenses such as depreciation. Then it adjusts for working capital: an increase in inventory or receivables uses cash (subtract), and an increase in payables saves cash (add).',
            'Investing activities cover buying and selling non-current assets and investments. Financing activities cover new capital or loans, loan repayments, drawings and dividends.',
            'The three sections add up to the change in cash between the two statements of financial position. A profitable business can still run out of cash if its inventory and receivables grow faster than its payables, which is why lenders watch this statement closely.'],
        'formulas_label': 'Indirect method',
        'formulas': ['Operating cash flow = profit + depreciation − increase in inventory − increase in receivables + increase in payables', 'Investing: − purchase of assets + proceeds from sales', 'Financing: + new capital and loans − repayments − drawings/dividends', 'Net change in cash = operating + investing + financing'],
        'steps': ['Start with profit.', 'Add back depreciation and other non-cash items.', 'Adjust for changes in inventory, receivables and payables.', 'Add investing and financing flows.', 'Check against the change in cash.'],
        'worked_example': {
            'problem': 'Profit 26 600, depreciation 9 000. During the year inventory rose by 5 000, receivables rose by 4 000 and payables rose by 3 000. Find the cash flow from operating activities.',
            'steps': ['Start: 26 600 + 9 000 = 35 600.', 'Increases in inventory and receivables use cash: 35 600 − 5 000 − 4 000 = 26 600.', 'The increase in payables saves cash: 26 600 + 3 000 = 29 600.'],
            'answer': 'Operating cash flow = 29 600.',
            'check': 'Operating cash exceeds profit here mainly because depreciation is added back, a non-cash expense.'},
        'mistakes': ['Subtracting depreciation instead of adding it back.', 'Getting the signs of working-capital changes the wrong way round.', 'Putting the purchase of equipment in operating activities.', 'Treating drawings or dividends as operating flows.'],
        'real_world': 'Many fast-growing businesses fail despite showing profits because their cash is tied up in inventory and unpaid customer invoices; the cash flow statement exposes this early.',
        'exam_strategy': 'Write each adjustment with a sign and a short label ("increase in receivables (4 000)"). Brackets for outflows are the convention examiners expect.',
        'recap': ['Operating, investing, financing.', 'Add back depreciation.', 'More inventory or receivables: less cash; more payables: more cash.', 'Profit ≠ cash.']},
    T4: {
        'overview': 'A bank reconciliation explains why the balance in the business\'s cash book differs from the bank statement, and finds the correct cash figure.',
        'key_terms': ['Cash book', 'Bank statement', 'Unpresented cheques', 'Outstanding lodgements', 'Bank charges', 'Direct credits', 'Dishonoured cheque'],
        'explanation': [
            'Some differences are items the bank knows about but the business has not recorded yet: bank charges, interest, direct debits, credit transfers from customers and dishonoured cheques. These are entered in the cash book first, giving an updated cash book balance.',
            'Other differences are timing items the business has recorded but the bank has not processed yet: unpresented cheques (paid out by the business but not yet cleared) and outstanding lodgements (deposits not yet credited by the bank).',
            'Reconciliation: adjusted bank balance = bank statement balance + outstanding lodgements − unpresented cheques. This should equal the updated cash book balance. Regular reconciliation detects errors and fraud quickly.'],
        'formulas_label': 'Formulas',
        'formulas': ['Updated cash book = cash book − charges and direct debits + credit transfers and interest received', 'Adjusted bank = bank statement + outstanding lodgements − unpresented cheques', 'Updated cash book = adjusted bank balance'],
        'steps': ['Compare the cash book and bank statement item by item.', 'Update the cash book for items only the bank has recorded.', 'Adjust the bank balance for timing items.', 'Check the two figures agree.'],
        'worked_example': {
            'problem': 'The cash book shows 4 500; the bank statement shows 5 200. Bank charges of 50 and a customer\'s credit transfer of 250 are not in the cash book. Cheques of 1 400 are unpresented and a deposit of 900 is not yet credited. Reconcile.',
            'steps': ['Updated cash book: 4 500 − 50 + 250 = 4 700.', 'Adjusted bank balance: 5 200 + 900 − 1 400 = 4 700.', 'The two agree.'],
            'answer': 'The correct cash balance is 4 700.',
            'check': 'Every difference was explained by either a missing cash-book entry or a timing difference ✓.'},
        'mistakes': ['Adjusting the bank balance for bank charges (they go in the cash book).', 'Adding unpresented cheques to the bank balance.', 'Forgetting dishonoured cheques reduce the cash book.', 'Mixing up which side each item belongs to.'],
        'real_world': 'Monthly bank reconciliations are a standard internal control; many cases of staff fraud are discovered when reconciliations are finally done after being skipped for months.',
        'exam_strategy': 'Present two separate parts: the updated cash book, then the bank reconciliation statement ending in the same figure. Equal final figures are your proof.',
        'recap': ['Bank-only items: update the cash book.', 'Timing items: adjust the bank balance.', 'Both must agree.', 'Reconcile regularly.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Opening inventory 20 000, purchases 120 000, closing inventory 25 000. Cost of sales is:', ['115000', '125000', '165000', '95000'], 0, '20 000 + 120 000 − 25 000.', ans=cogs),
    Q(T1, 'Net revenue 195 000 and cost of sales 115 000. Gross profit is:', ['80000', '310000', '115000', '195000'], 0, '195 000 − 115 000.', ans=gp),
    Q(T1, 'Gross profit 80 000 and expenses 53 400. Net profit is:', ['26600', '133400', '53400', '80000'], 0, '80 000 − 53 400.', ans=np_),
    Q(T1, 'Carriage outwards is shown as:', ['an expense after gross profit', 'part of cost of sales', 'a current asset', 'a deduction from sales'], 0, 'It is a selling cost.'),
    Q(T1, 'Which does NOT appear in the income statement?', ['Drawings', 'Depreciation', 'Rent', 'Discount received'], 0, 'Drawings reduce equity directly.'),
    Q(T1, 'Sales 200 000 and sales returns 5 000. Net revenue is:', ['195000', '205000', '200000', '5000'], 0, '200 000 − 5 000.', ans=net_sales),
    # T2
    Q(T2, 'Equipment cost 50 000, accumulated depreciation 18 000. It is shown at:', ['32000', '50000', '68000', '18000'], 0, 'Carrying amount.', ans=nca),
    Q(T2, 'Current assets 71 000 and current liabilities 19 000. Working capital is:', ['52000', '90000', '71000', '19000'], 0, '71 000 − 19 000.', ans=52000),
    Q(T2, 'Opening capital 60 000, profit 26 600, drawings 12 600. Closing capital is:', ['74000', '99200', '46000', '86600'], 0, '60 000 + 26 600 − 12 600.', ans=74000),
    Q(T2, 'A bank overdraft is classified as:', ['a current liability', 'a current asset', 'a non-current liability', 'equity'], 0, 'It is repayable on demand.'),
    Q(T2, 'Total assets 103 000 and total liabilities 29 000. Net assets are:', ['74000', '132000', '103000', '29000'], 0, '103 000 − 29 000.', ans=74000),
    Q(T2, 'Receivables are shown in the statement of financial position:', ['net of the allowance for receivables', 'including the allowance', 'at their sales value plus interest', 'as a liability'], 0, 'Prudence: only the amount expected to be collected.'),
    # T3
    Q(T3, 'Profit 26 600, depreciation 9 000, inventory up 5 000, receivables up 4 000, payables up 3 000. Operating cash flow is:', ['29600', '23600', '38600', '35600'], 0, '26 600 + 9 000 − 5 000 − 4 000 + 3 000.', ans=cfo),
    Q(T3, 'In the indirect method, depreciation is:', ['added back to profit', 'subtracted from profit', 'shown under financing', 'ignored'], 0, 'It is a non-cash expense.'),
    Q(T3, 'An increase in trade receivables:', ['reduces operating cash flow', 'increases operating cash flow', 'has no effect on cash', 'is a financing flow'], 0, 'Sales have been made but cash not yet collected.'),
    Q(T3, 'Buying a new delivery van is an:', ['investing outflow', 'operating outflow', 'financing outflow', 'operating inflow'], 0, 'It is a purchase of a non-current asset.'),
    Q(T3, 'Taking out a new bank loan is a:', ['financing inflow', 'investing inflow', 'operating inflow', 'financing outflow'], 0, 'It is a source of finance.'),
    Q(T3, 'A business can be profitable but short of cash because:', ['cash is tied up in inventory and receivables', 'depreciation uses cash', 'profit always equals cash', 'drawings are expenses'], 0, 'Working capital absorbs cash.'),
    # T4
    Q(T4, 'Cash book 4 500, bank charges 50 unrecorded, credit transfer 250 unrecorded. The updated cash book balance is:', ['4700', '4800', '4300', '4500'], 0, '4 500 − 50 + 250.', ans=4700),
    Q(T4, 'Bank statement 5 200, outstanding lodgement 900, unpresented cheques 1 400. Adjusted bank balance is:', ['4700', '7500', '5700', '3900'], 0, '5 200 + 900 − 1 400.', ans=4700),
    Q(T4, 'Unpresented cheques are:', ['deducted from the bank statement balance', 'added to the bank statement balance', 'deducted from the cash book', 'added to the cash book'], 0, 'The bank has not yet paid them out.'),
    Q(T4, 'Bank charges not yet recorded by the business should be:', ['deducted in the cash book', 'added to the bank balance', 'ignored', 'added in the cash book'], 0, 'The business must record them.'),
    Q(T4, 'A customer\'s cheque is returned unpaid (dishonoured). The business should:', ['reduce the cash book and reinstate the receivable', 'increase the cash book', 'adjust the bank statement', 'record it as a sale'], 0, 'The money was never actually received.'),
    Q(T4, 'The main purpose of a bank reconciliation is to:', ['confirm the correct cash balance and detect errors', 'calculate profit', 'record depreciation', 'value inventory'], 0, 'It is a key internal control.'),
]

FLASH = [
    ['Cost of sales', 'Opening inventory + purchases − closing inventory.'],
    ['Gross profit', 'Net revenue − cost of sales.'],
    ['Working capital', 'Current assets − current liabilities.'],
    ['Closing capital', 'Opening capital + profit − drawings.'],
    ['Indirect operating cash flow', 'Profit + depreciation ± working-capital changes.'],
    ['Investing vs financing', 'Assets bought/sold vs capital, loans and drawings.'],
    ['Unpresented cheques', 'Deduct from the bank statement balance.'],
    ['Bank charges', 'Record in the cash book (deduct).'],
]
