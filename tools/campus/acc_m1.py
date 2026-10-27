"""Financial Accounting I, module 1: The accounting framework."""
from verify import Q, sp
T1, T2, T3, T4 = ('The accounting equation', 'Double-entry bookkeeping', 'The trial balance', 'Accounting concepts and principles')
# accounting equation example: owner invests 50 000 cash, borrows 20 000, buys equipment 30 000 cash, buys inventory 10 000 on credit
cash = 50000 + 20000 - 30000
assets = cash + 30000 + 10000
liab = 20000 + 10000
assert (cash, assets, liab, assets - liab) == (40000, 80000, 30000, 50000)
assert 120000 - 45000 == 75000 and 60000 + 25000 == 85000
tb_dr = 15000 + 40000 + 8000 + 22000 + 5000
tb_cr = 50000 + 30000 + 10000
assert tb_dr == tb_cr == 90000

MODULE = {
    'title': 'The accounting framework',
    'topics': [T1, T2, T3, T4],
    'overview': 'Accounting records, summarises and reports a business\'s financial activity so that owners, lenders, managers and tax authorities can make decisions. This module builds the foundation: the accounting equation, double-entry bookkeeping, the trial balance and the concepts that guide every judgement an accountant makes.',
    'key_terms': ['Asset', 'Liability', 'Equity', 'Accounting equation', 'Debit', 'Credit', 'Ledger', 'Trial balance', 'Accruals concept', 'Going concern'],
    'explanation': [
        'Everything a business owns (assets) is financed either by what it owes to others (liabilities) or by the owners (equity). So Assets = Liabilities + Equity always holds. Every transaction changes at least two items in a way that keeps the equation in balance.',
        'Double-entry bookkeeping records each transaction twice: as a debit in one account and a credit in another, for equal amounts. Debits increase assets and expenses; credits increase liabilities, equity and income. Listing all account balances in a trial balance checks that total debits equal total credits.',
        'Accounting concepts such as accruals (record income and expenses when earned or incurred, not when cash moves), going concern, consistency, prudence and materiality guide how transactions are measured. They are set out in frameworks such as IFRS, which most of our countries use.'],
    'quick_facts': [
        'Assets = Liabilities + Equity.',
        'Equity = capital + profit − drawings.',
        'DEAD CLIC: Debits increase Expenses, Assets, Drawings; Credits increase Liabilities, Income, Capital.',
        'A trial balance checks arithmetic, not every error.',
        'Accruals: match income and expenses to the period, not to cash.'],
}

NOTES = {
    T1: {
        'overview': 'The accounting equation, Assets = Liabilities + Equity, is the backbone of all accounting. Every transaction changes it, but it always balances.',
        'key_terms': ['Asset', 'Liability', 'Equity (capital)', 'Drawings', 'Current and non-current', 'Dual aspect'],
        'explanation': [
            'An asset is a resource controlled by the business that will bring future economic benefit (cash, inventory, equipment, amounts owed by customers). A liability is an obligation to pay out resources (bank loans, amounts owed to suppliers). Equity is the owners\' claim: the assets left after all liabilities are paid.',
            'Each transaction has a dual aspect. Buying equipment for cash swaps one asset for another; buying inventory on credit increases an asset and a liability; the owner investing cash increases an asset and equity. The equation stays balanced after every transaction.',
            'Equity grows with profits and new capital and falls with losses and drawings (cash or goods the owner takes out for personal use). Assets and liabilities are classified as current (expected to turn into cash or be paid within a year) or non-current.'],
        'formulas_label': 'Formulas',
        'formulas': ['Assets = Liabilities + Equity', 'Equity = Assets − Liabilities', 'Closing equity = opening equity + capital introduced + profit − drawings', 'Profit = increase in net assets − capital introduced + drawings'],
        'steps': ['List the items each transaction affects.', 'Decide whether each item increases or decreases.', 'Check the equation still balances.', 'Total assets, liabilities and equity at the end.'],
        'worked_example': {
            'problem': 'Thandi starts a business with 50 000 of her own cash, borrows 20 000 from a bank, buys equipment for 30 000 cash and buys inventory for 10 000 on credit. Show the accounting equation.',
            'steps': ['Cash = 50 000 + 20 000 − 30 000 = 40 000. Assets = cash 40 000 + equipment 30 000 + inventory 10 000 = 80 000.', 'Liabilities = bank loan 20 000 + payable to supplier 10 000 = 30 000.', 'Equity = capital 50 000.'],
            'answer': 'Assets 80 000 = Liabilities 30 000 + Equity 50 000.',
            'check': 'Each transaction kept the equation balanced, so the totals agree ✓.'},
        'mistakes': ['Recording only one side of a transaction.', 'Treating drawings as a business expense.', 'Counting an owner\'s personal assets as business assets (the business entity concept).', 'Classifying a loan repayable in five years as a current liability.'],
        'real_world': 'Banks ask small businesses for a statement of financial position before lending, because the accounting equation shows how much of the business is already financed by debt.',
        'exam_strategy': 'Lay out transactions in a table with columns for each asset, liability and equity item. A row-by-row table makes the dual aspect visible and earns method marks.',
        'recap': ['A = L + E always.', 'Every transaction has two effects.', 'Equity rises with profit and capital, falls with drawings.', 'Classify current vs non-current.']},
    T2: {
        'overview': 'Double-entry bookkeeping records each transaction as an equal debit and credit in two accounts. It keeps the accounting equation in balance and creates a complete record in the ledger.',
        'key_terms': ['Ledger', 'T-account', 'Debit', 'Credit', 'Journal', 'Balance carried down', 'Credit sale', 'Receivables', 'Payables'],
        'explanation': [
            'Each account is drawn as a T: debits on the left, credits on the right. Debits increase assets, expenses and drawings; credits increase liabilities, income and capital. The memory aid DEAD CLIC (Debit: Expenses, Assets, Drawings; Credit: Liabilities, Income, Capital) helps.',
            'Examples: a cash sale debits Cash and credits Sales; buying inventory on credit debits Purchases (or Inventory) and credits Payables; paying rent debits Rent expense and credits Cash; a customer paying what they owe debits Cash and credits Receivables.',
            'At the end of a period each account is balanced: add both sides, and the difference is the balance carried down to the next period. Transactions are often first entered in a journal (book of prime entry) with a short narration before being posted to the ledger.'],
        'formulas_label': 'Rules',
        'formulas': ['Debit (left): increase in assets, expenses, drawings', 'Credit (right): increase in liabilities, income, capital', 'Every entry: total debits = total credits', 'Balance c/d = larger side total − smaller side total'],
        'steps': ['Identify the two accounts affected.', 'Decide which increases and which decreases.', 'Apply DEAD CLIC to choose debit and credit.', 'Post to both T-accounts.', 'Balance the accounts at period end.'],
        'worked_example': {
            'problem': 'Record these transactions: (1) sold goods for 5000 cash; (2) bought goods for 3000 on credit from Ade Ltd; (3) paid rent of 1200 in cash.',
            'steps': ['(1) Dr Cash 5000, Cr Sales 5000.', '(2) Dr Purchases 3000, Cr Payables (Ade Ltd) 3000.', '(3) Dr Rent expense 1200, Cr Cash 1200.'],
            'answer': 'Each transaction has an equal debit and credit; the Cash account now has a debit balance of 3800.',
            'check': 'Total debits 9200 = total credits 9200 ✓.'},
        'mistakes': ['Reversing debit and credit for income (sales are credits).', 'Debiting the supplier\'s account when buying on credit (it should be credited).', 'Recording a cash payment as a debit to Cash.', 'Forgetting to post the second side.'],
        'real_world': 'Accounting software still uses double entry underneath: every invoice or payment you enter automatically creates a matching debit and credit.',
        'exam_strategy': 'Write the journal entry (Dr …, Cr …, amount, narration) before posting to T-accounts. Examiners can then credit your reasoning even if the posting slips.',
        'recap': ['Every transaction: equal debit and credit.', 'DEAD CLIC.', 'Balance accounts at period end.', 'Journal first, then ledger.']},
    T3: {
        'overview': 'A trial balance lists every ledger balance in debit and credit columns. If double entry has been done correctly, the two totals agree, but some errors still pass unnoticed.',
        'key_terms': ['Trial balance', 'Debit balance', 'Credit balance', 'Error of omission', 'Error of commission', 'Error of principle', 'Compensating error', 'Suspense account'],
        'explanation': [
            'Assets, expenses and drawings normally have debit balances; liabilities, capital and income have credit balances. Listing them all gives two totals that should be equal. If they are not, an arithmetic or posting error has occurred, and a temporary suspense account holds the difference until it is found.',
            'Some errors do not affect the totals: omission (a transaction not recorded at all), commission (right type of account, wrong one, such as the wrong customer), principle (wrong type of account, such as capital spending recorded as an expense), original entry (wrong amount on both sides), complete reversal (debit and credit swapped) and compensating errors that cancel out.',
            'So a balanced trial balance shows only that debits equal credits. It is the starting point for preparing the financial statements, after adjustments for items such as depreciation and accruals.'],
        'formulas_label': 'Rules',
        'formulas': ['Debit side: assets, expenses, drawings', 'Credit side: liabilities, capital, income', 'Total debits = total credits', 'Difference ⇒ suspense account until corrected'],
        'steps': ['List each ledger balance.', 'Place it in the debit or credit column.', 'Add both columns.', 'Investigate any difference.'],
        'worked_example': {
            'problem': 'Prepare a trial balance from: cash 15 000, equipment 40 000, rent expense 8 000, purchases 22 000, drawings 5 000, capital 50 000, sales 30 000, bank loan 10 000.',
            'steps': ['Debits: cash 15 000 + equipment 40 000 + rent 8 000 + purchases 22 000 + drawings 5 000 = 90 000.', 'Credits: capital 50 000 + sales 30 000 + loan 10 000 = 90 000.', 'The totals agree.'],
            'answer': 'Trial balance totals: debit 90 000, credit 90 000.',
            'check': 'Agreement shows correct double entry arithmetic, but errors such as omission could still exist.'},
        'mistakes': ['Putting drawings on the credit side.', 'Listing sales as a debit.', 'Thinking a balanced trial balance proves the books are correct.', 'Leaving a suspense account in the final statements.'],
        'real_world': 'Auditors look beyond the trial balance because the most serious errors and frauds, such as fictitious sales recorded on both sides, keep the trial balance in balance.',
        'exam_strategy': 'Name the type of error precisely and say whether it affects the trial balance. Questions on errors often give one mark for the name and one for the effect.',
        'recap': ['Debit and credit balances.', 'Totals should agree.', 'Six errors that do not show.', 'Suspense account for differences.']},
    T4: {
        'overview': 'Accounting concepts and principles make financial statements reliable and comparable. They guide decisions such as when to recognise income, how to value assets and how much detail to report.',
        'key_terms': ['Business entity', 'Going concern', 'Accruals (matching)', 'Consistency', 'Prudence', 'Materiality', 'Historical cost', 'IFRS'],
        'explanation': [
            'The business entity concept treats the business as separate from its owner. Going concern assumes the business will continue in the foreseeable future, so assets are valued at cost less depreciation rather than at forced-sale prices.',
            'The accruals (matching) concept records income when earned and expenses when incurred, regardless of when cash moves, and matches expenses to the income they help generate. Consistency means using the same methods from year to year so results can be compared.',
            'Prudence means not overstating assets or income, for example by providing for doubtful debts. Materiality means items too small to affect decisions need not be treated in full detail (a cheap stapler can be expensed rather than depreciated). These concepts underpin International Financial Reporting Standards (IFRS) and national standards based on them.'],
        'formulas_label': 'Concepts',
        'formulas': ['Business entity: business ≠ owner', 'Going concern: business continues', 'Accruals: income earned, expenses incurred', 'Consistency, prudence, materiality'],
        'steps': ['Identify the accounting decision.', 'Find the concept that applies.', 'Apply it to the numbers.', 'Explain how it makes the statements more useful.'],
        'worked_example': {
            'problem': 'A business pays its December electricity bill of 2 000 in January. In which year is the expense recorded, and why?',
            'steps': ['The electricity was used in December, in the year being reported.', 'The accruals concept records expenses when incurred.', 'So the expense belongs to this year, with an accrued liability of 2 000 at the year end.'],
            'answer': 'Record 2 000 of electricity expense this year and an accrual (liability) of 2 000.',
            'check': 'If it were recorded next year, this year\'s profit would be overstated by 2 000, breaking the matching principle.'},
        'mistakes': ['Recording expenses only when cash is paid.', 'Mixing the owner\'s personal spending into the business accounts.', 'Changing depreciation methods every year without reason.', 'Applying prudence so heavily that profits are deliberately understated.'],
        'real_world': 'When a company is in serious financial difficulty, auditors may add a "going concern" warning to its accounts, signalling that asset values could fall sharply if it closes.',
        'exam_strategy': 'Name the concept and apply it to the scenario in one or two sentences. A correct definition without application usually gets only half the marks.',
        'recap': ['Entity and going concern.', 'Accruals/matching.', 'Consistency and prudence.', 'Materiality.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Assets are 80 000 and liabilities are 30 000. Equity is:', ['50000', '110000', '30000', '80000'], 0, 'Equity = assets − liabilities.', ans=50000),
    Q(T1, 'Buying equipment for cash:', ['increases one asset and decreases another', 'increases assets and liabilities', 'decreases equity', 'increases liabilities'], 0, 'Equipment up, cash down; totals unchanged.'),
    Q(T1, 'Buying inventory on credit:', ['increases assets and liabilities', 'increases assets and equity', 'decreases cash', 'decreases liabilities'], 0, 'Inventory up, payables up.'),
    Q(T1, 'Opening equity 60 000, profit 25 000, drawings 10 000, no new capital. Closing equity is:', ['75000', '85000', '95000', '45000'], 0, '60 000 + 25 000 − 10 000.', ans=75000),
    Q(T1, 'Drawings are:', ['amounts the owner takes out for personal use', 'a business expense', 'a liability', 'income'], 0, 'They reduce equity, not profit.'),
    Q(T1, 'A bank loan repayable in five years is a:', ['non-current liability', 'current liability', 'current asset', 'part of equity'], 0, 'It is not due within a year.'),
    # T2
    Q(T2, 'A cash sale of 5000 is recorded as:', ['Dr Cash, Cr Sales', 'Dr Sales, Cr Cash', 'Dr Cash, Cr Capital', 'Dr Receivables, Cr Sales'], 0, 'Cash (asset) rises; sales (income) rises.'),
    Q(T2, 'Buying goods on credit from a supplier is recorded as:', ['Dr Purchases, Cr Payables', 'Dr Payables, Cr Purchases', 'Dr Purchases, Cr Cash', 'Dr Cash, Cr Payables'], 0, 'Purchases (expense) up, payables (liability) up.'),
    Q(T2, 'Paying rent in cash is recorded as:', ['Dr Rent expense, Cr Cash', 'Dr Cash, Cr Rent expense', 'Dr Rent expense, Cr Capital', 'Dr Capital, Cr Cash'], 0, 'Expense up, asset down.'),
    Q(T2, 'A customer pays an amount owed. The entry is:', ['Dr Cash, Cr Receivables', 'Dr Receivables, Cr Cash', 'Dr Cash, Cr Sales', 'Dr Sales, Cr Receivables'], 0, 'Cash up, receivables down.'),
    Q(T2, 'In DEAD CLIC, credits increase:', ['liabilities, income and capital', 'expenses, assets and drawings', 'only cash', 'only assets'], 0, 'Debits increase the other three.'),
    Q(T2, 'Cash receipts total 9000 and payments total 5200. The Cash account balance is:', ['3800 debit', '3800 credit', '14200 debit', '5200 credit'], 0, 'Receipts exceed payments, so a debit balance of 3800.'),
    # T3
    Q(T3, 'Which normally has a credit balance?', ['Sales', 'Purchases', 'Drawings', 'Equipment'], 0, 'Income accounts have credit balances.'),
    Q(T3, 'Debits: cash 15 000, equipment 40 000, rent 8 000, purchases 22 000, drawings 5 000. Total debits are:', ['90000', '85000', '70000', '95000'], 0, '15 + 40 + 8 + 22 + 5 thousand.', ans=tb_dr),
    Q(T3, 'A purchase of a delivery van is debited to Vehicle repairs. This is an error of:', ['principle', 'commission', 'omission', 'original entry'], 0, 'A capital item was recorded as an expense: the wrong type of account.'),
    Q(T3, 'A sale to J. Banda is posted to J. Bandele\'s account. This is an error of:', ['commission', 'principle', 'omission', 'reversal'], 0, 'Right type of account, wrong individual account.'),
    Q(T3, 'Which error makes the trial balance totals disagree?', ['Posting only the debit side of an entry', 'Omitting a transaction entirely', 'An error of principle', 'A complete reversal of entries'], 0, 'One-sided postings break the equality of debits and credits.'),
    Q(T3, 'A suspense account is used to:', ['hold a trial balance difference until the errors are found', 'record cash sales', 'store drawings', 'record depreciation'], 0, 'It is temporary.'),
    # T4
    Q(T4, 'December electricity paid in January is recorded in December because of the:', ['accruals concept', 'going concern concept', 'entity concept', 'materiality concept'], 0, 'Expenses are recorded when incurred.'),
    Q(T4, 'The owner\'s private car repairs should not be in the business accounts because of the:', ['business entity concept', 'prudence concept', 'consistency concept', 'going concern concept'], 0, 'The business is separate from its owner.'),
    Q(T4, 'Valuing assets at cost less depreciation rather than forced-sale value relies on the:', ['going concern concept', 'materiality concept', 'entity concept', 'realisation concept'], 0, 'The business is assumed to continue.'),
    Q(T4, 'Expensing a cheap calculator instead of depreciating it applies the:', ['materiality concept', 'consistency concept', 'going concern concept', 'entity concept'], 0, 'The amount is too small to affect decisions.'),
    Q(T4, 'Using the same depreciation method every year applies the:', ['consistency concept', 'prudence concept', 'accruals concept', 'entity concept'], 0, 'It makes results comparable over time.'),
    Q(T4, 'Making an allowance for customers who may not pay applies the:', ['prudence concept', 'going concern concept', 'materiality concept', 'consistency concept'], 0, 'Assets and income should not be overstated.'),
]

FLASH = [
    ['Accounting equation', 'Assets = Liabilities + Equity.'],
    ['Equity movement', 'Closing = opening + capital introduced + profit − drawings.'],
    ['DEAD CLIC', 'Debit: Expenses, Assets, Drawings. Credit: Liabilities, Income, Capital.'],
    ['Trial balance', 'List of ledger balances; total debits = total credits.'],
    ['Error of principle', 'Correct amount in the wrong type of account (e.g. capital item as an expense).'],
    ['Error of commission', 'Correct type of account but the wrong individual account.'],
    ['Accruals concept', 'Record income when earned and expenses when incurred.'],
    ['Prudence', 'Do not overstate assets or income.'],
]
