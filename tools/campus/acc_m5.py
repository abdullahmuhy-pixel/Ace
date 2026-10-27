"""Financial Accounting I, module 5: Control accounts, errors, partnerships and companies."""
from verify import Q, sp
T1, T2, T3, T4 = ('Control accounts', 'Correcting errors and the suspense account', 'Partnership accounts', 'Limited company accounts')
R = sp.Rational
rc = 12000 + 80000 - 70000 - 1000 - 2000 - 500
assert rc == 18500
pc = 9000 + 50000 - 45000 - 800 - 1200
assert pc == 12000
resid = 90000 - 10000 - R(5, 100) * 60000 - R(5, 100) * 40000
a_share, b_share = resid * R(3, 5), resid * R(2, 5)
assert (resid, a_share, b_share, 10000 + 3000 + a_share, 2000 + b_share) == (75000, 45000, 30000, 58000, 32000)
tax = 200000 * R(25, 100)
assert (tax, 200000 - tax, 200000 + 150000 - 100000) == (50000, 150000, 250000)
assert 1000000 * R(1, 2) == 500000 and 1000000 * R(1, 10) == 100000

MODULE = {
    'title': 'Control accounts, errors, partnerships and companies',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module completes the first-year course. Control accounts check the accuracy of large ledgers, journal entries correct errors found after the trial balance, and the final two topics adapt everything you have learned to partnerships and limited companies, the forms most real businesses take.',
    'key_terms': ['Receivables control account', 'Payables control account', 'Contra entry', 'Suspense account', 'Journal correction', 'Appropriation account', 'Current account (partnership)', 'Share capital', 'Share premium', 'Retained earnings'],
    'explanation': [
        'Businesses with many customers and suppliers keep individual accounts in subsidiary ledgers and a summary control account in the general ledger. The control account balance should equal the total of the individual accounts, which helps find errors and deters fraud.',
        'Errors found after preparing the trial balance are corrected with journal entries. Errors that made the trial balance disagree are corrected through the suspense account until it is cleared. Each correction may also change the profit figure.',
        'Partnerships share profits according to their agreement, using an appropriation account for salaries, interest on capital and the profit-sharing ratio. Limited companies separate the owners (shareholders) from the business; their equity is made up of share capital, share premium and retained earnings, and they pay tax and dividends.'],
    'quick_facts': [
        'Receivables control: opening + credit sales − receipts − discounts − returns − write-offs = closing.',
        'Correct errors with a journal: debit what should be higher, credit what should be lower.',
        'Partnership: residual profit = profit − salaries − interest on capital, shared in the agreed ratio.',
        'Share premium = (issue price − nominal value) × shares issued.',
        'Retained earnings = opening + profit after tax − dividends.'],
}

NOTES = {
    T1: {
        'overview': 'A control account summarises all entries made in a subsidiary ledger. Its balance should agree with the total of the individual customer or supplier accounts.',
        'key_terms': ['Sales ledger', 'Purchases ledger', 'Receivables control', 'Payables control', 'Contra (set-off)', 'Discounts allowed', 'Discounts received'],
        'explanation': [
            'The receivables (sales ledger) control account is debited with opening receivables and credit sales, and credited with cash received, discounts allowed, sales returns, irrecoverable debts written off and contra entries. The closing balance is the total owed by customers.',
            'The payables (purchases ledger) control account is credited with opening payables and credit purchases, and debited with payments, discounts received, purchase returns and contras. Its balance is the total owed to suppliers.',
            'A contra entry sets off an amount when a business both sells to and buys from the same firm. If the control account and the list of individual balances disagree, errors are traced and corrected in whichever record is wrong. Control accounts also separate duties: different staff keep the individual ledgers and the control accounts, which helps prevent fraud.'],
        'formulas_label': 'Formulas',
        'formulas': ['Receivables: opening + credit sales − cash − discounts allowed − returns in − irrecoverable debts − contras = closing', 'Payables: opening + credit purchases − payments − discounts received − returns out − contras = closing', 'Cash sales do not enter the receivables control account'],
        'steps': ['Identify credit transactions only.', 'Put increases on the normal-balance side.', 'Put decreases on the opposite side.', 'Balance the account and compare with the ledger list.'],
        'worked_example': {
            'problem': 'Receivables at the start were 12 000. Credit sales 80 000, cash received from customers 70 000, discounts allowed 1 000, sales returns 2 000, irrecoverable debt written off 500. Find the closing balance.',
            'steps': ['Debits: 12 000 + 80 000 = 92 000.', 'Credits: 70 000 + 1 000 + 2 000 + 500 = 73 500.', 'Closing balance = 92 000 − 73 500 = 18 500 debit.'],
            'answer': 'Receivables at the end are 18 500.',
            'check': 'If the list of customer balances totals, say, 18 200, there is an error of 300 to trace.'},
        'mistakes': ['Including cash sales.', 'Putting discounts received in the receivables control account.', 'Recording a contra on the wrong side.', 'Treating the allowance for receivables as a control account entry.'],
        'real_world': 'Accounting software keeps control accounts automatically, but finance teams still reconcile them to the customer list each month to catch posting errors and unauthorised entries.',
        'exam_strategy': 'Draw the control account as a T-account with each item labelled. Before balancing, check every item is a credit transaction.',
        'recap': ['Summary of a subsidiary ledger.', 'Credit transactions only.', 'Should equal the list of balances.', 'Helps detect errors and fraud.']},
    T2: {
        'overview': 'Errors found after the trial balance are corrected with journal entries. If an error caused the trial balance to disagree, the correction also clears the suspense account.',
        'key_terms': ['Journal entry', 'Suspense account', 'Error correction', 'Effect on profit', 'Single-sided error', 'Transposition'],
        'explanation': [
            'To correct an error, compare what was done with what should have been done, and write the journal entry that moves from one to the other. Debit the account that is too low (for an asset or expense) and credit the one that is too high, with a short narration.',
            'If only one side of an entry was posted, or the two sides were different amounts, the trial balance did not agree and the difference went to suspense. The correcting entry includes the suspense account, and once all such errors are fixed the suspense balance is zero.',
            'Many corrections change profit. Increasing an expense or reducing income lowers profit; reducing an expense or increasing income raises it. Corrections between asset and liability accounts change the statement of financial position only.'],
        'formulas_label': 'Method',
        'formulas': ['Correction = what should have been − what was done', 'Single-sided errors involve the suspense account', 'Expense ↑ or income ↓ ⇒ profit ↓', 'Suspense balance after all corrections = 0'],
        'steps': ['Write down the entry that was made.', 'Write down the correct entry.', 'Journal the difference.', 'Note any suspense entry.', 'State the effect on profit.'],
        'worked_example': {
            'problem': 'A rent payment of 450 was credited to Cash but not debited to Rent. Correct the error and state the effect on profit.',
            'steps': ['Only the credit was posted, so the trial balance debit side was 450 short; suspense was debited with 450.', 'Correction: Dr Rent 450, Cr Suspense 450.', 'Rent expense rises by 450.'],
            'answer': 'Journal: Dr Rent expense 450, Cr Suspense 450. Profit falls by 450.',
            'check': 'The suspense account now has 450 debit and 450 credit, so it is cleared ✓.'},
        'mistakes': ['Reversing the correcting entry (debiting suspense when it should be credited).', 'Forgetting to state the effect on profit.', 'Using suspense for errors that did not affect the trial balance.', 'Correcting the wrong account.'],
        'real_world': 'Auditors review year-end journals closely, because unusual manual corrections are a common way to hide errors or manipulate profit.',
        'exam_strategy': 'For each error, give the journal (Dr, Cr, amount, narration) and a separate line for the effect on profit. Questions often ask for a corrected profit figure at the end.',
        'recap': ['Journal the difference.', 'Single-sided errors go through suspense.', 'State the profit effect.', 'Suspense must clear to zero.']},
    T3: {
        'overview': 'A partnership is a business owned by two or more people. Its accounts are like a sole trader\'s, except that profit must be shared according to the partnership agreement.',
        'key_terms': ['Partnership agreement', 'Appropriation account', 'Partner salary', 'Interest on capital', 'Interest on drawings', 'Profit-sharing ratio', 'Capital account', 'Current account'],
        'explanation': [
            'The partnership agreement sets out how profit is shared. Common terms are salaries for partners who work in the business, interest on the capital each partner has invested, interest charged on drawings, and a ratio for sharing whatever is left.',
            'The appropriation account starts with net profit, adds interest on drawings, deducts salaries and interest on capital, and shares the residual profit in the agreed ratio. Partner salaries are not expenses of the business; they are part of the profit share.',
            'Each partner usually has a fixed capital account (long-term investment) and a current account, which is credited with salary, interest and profit share and debited with drawings and interest on drawings. Without an agreement, many legal systems default to equal profit sharing and no salaries or interest.'],
        'formulas_label': 'Formulas',
        'formulas': ['Residual = net profit + interest on drawings − salaries − interest on capital', 'Each share = residual × partner\'s ratio', 'Partner total = salary + interest on capital + share of residual − interest on drawings', 'Current account closing = opening + total share − drawings'],
        'steps': ['Start with net profit.', 'Deduct salaries and interest on capital; add interest on drawings.', 'Share the residual in the agreed ratio.', 'Post each partner\'s total to their current account.'],
        'worked_example': {
            'problem': 'A and B share profits 3 : 2. Net profit is 90 000. A gets a salary of 10 000. Interest on capital is 5%: A\'s capital is 60 000 and B\'s is 40 000. Share the profit.',
            'steps': ['Interest on capital: A 3 000, B 2 000.', 'Residual = 90 000 − 10 000 − 3 000 − 2 000 = 75 000.', 'Shared 3 : 2: A 45 000, B 30 000.'],
            'answer': 'A receives 10 000 + 3 000 + 45 000 = 58 000; B receives 2 000 + 30 000 = 32 000.',
            'check': '58 000 + 32 000 = 90 000, the whole profit ✓.'},
        'mistakes': ['Treating partner salaries as business expenses.', 'Sharing the profit before deducting salaries and interest.', 'Using the capital ratio instead of the agreed profit-sharing ratio.', 'Posting drawings to the capital account when current accounts are kept.'],
        'real_world': 'Law and accounting firms are often partnerships; the profit-sharing formula is one of the most negotiated parts of the partnership agreement.',
        'exam_strategy': 'Lay out the appropriation account in a vertical format and finish with a check that the shares add up to the net profit.',
        'recap': ['Agreement sets the terms.', 'Salaries and interest first, then the ratio.', 'Salaries are not expenses.', 'Current accounts track each partner.']},
    T4: {
        'overview': 'A limited company is a separate legal entity owned by shareholders, who are liable only up to the amount they invested. Its financial statements show tax, dividends and a different equity section.',
        'key_terms': ['Limited liability', 'Ordinary shares', 'Nominal value', 'Share premium', 'Retained earnings', 'Dividends', 'Income tax expense', 'Statement of changes in equity'],
        'explanation': [
            'Shareholders own the company but are not personally liable for its debts beyond their investment (limited liability). Directors run the company and must publish financial statements, which are often audited.',
            'Equity consists of share capital (nominal value of shares issued), share premium (the amount received above nominal value) and reserves, mainly retained earnings. Retained earnings = opening balance + profit after tax − dividends.',
            'The company pays income tax on its profit, shown as an expense in the income statement. Dividends are distributions to shareholders, not expenses; they reduce retained earnings and appear in the statement of changes in equity. Directors\' salaries, by contrast, are expenses because directors are employees.'],
        'formulas_label': 'Formulas',
        'formulas': ['Share premium = (issue price − nominal value) × number of shares', 'Profit after tax = profit before tax − tax', 'Retained earnings = opening + profit after tax − dividends', 'Dividends = dividend per share × number of shares'],
        'steps': ['Compute tax and profit after tax.', 'Compute dividends.', 'Update retained earnings.', 'Record any share issue in share capital and share premium.'],
        'worked_example': {
            'problem': 'A company has profit before tax of 200 000 and pays tax at 25%. Retained earnings at the start were 200 000. It pays a dividend of 0.10 per share on 1 000 000 shares. Find the closing retained earnings.',
            'steps': ['Tax = 25% × 200 000 = 50 000, so profit after tax = 150 000.', 'Dividends = 0.10 × 1 000 000 = 100 000.', 'Retained earnings = 200 000 + 150 000 − 100 000 = 250 000.'],
            'answer': 'Closing retained earnings are 250 000.',
            'check': 'Dividends reduce equity directly; they do not appear as an expense in the income statement ✓.'},
        'mistakes': ['Recording dividends as an expense.', 'Putting the whole issue price into share capital.', 'Treating directors\' pay as drawings.', 'Forgetting income tax.'],
        'real_world': 'When a company lists on a stock exchange, it issues new shares above their nominal value; the excess raised is recorded as share premium.',
        'exam_strategy': 'Prepare a short statement of changes in equity with columns for share capital, share premium and retained earnings. It keeps every movement in the right column.',
        'recap': ['Limited liability.', 'Equity: capital, premium, retained earnings.', 'Tax is an expense; dividends are not.', 'Retained = opening + PAT − dividends.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Opening receivables 12 000, credit sales 80 000, receipts 70 000, discounts allowed 1 000, returns 2 000, write-off 500. Closing receivables are:', ['18500', '19500', '22000', '17500'], 0, '92 000 − 73 500.', ans=rc),
    Q(T1, 'Opening payables 9 000, credit purchases 50 000, payments 45 000, discounts received 800, returns out 1 200. Closing payables are:', ['12000', '14000', '11200', '13200'], 0, '59 000 − 47 000.', ans=pc),
    Q(T1, 'Which item does NOT appear in the receivables control account?', ['Cash sales', 'Discounts allowed', 'Credit sales', 'Irrecoverable debts written off'], 0, 'Only credit transactions are recorded.'),
    Q(T1, 'A contra entry is used when:', ['a business both sells to and buys from the same firm', 'a debt is written off', 'cash is banked', 'a customer pays early'], 0, 'The two balances are set off against each other.'),
    Q(T1, 'Discounts received appear in the:', ['payables control account', 'receivables control account', 'sales account', 'bank reconciliation'], 0, 'They reduce what is owed to suppliers.'),
    Q(T1, 'A key benefit of control accounts is that they:', ['help detect errors and deter fraud', 'calculate depreciation', 'replace the trial balance', 'value inventory'], 0, 'They provide an independent check on the subsidiary ledger.'),
    # T2
    Q(T2, 'Rent of 450 was credited to Cash but not debited to Rent. The correcting entry is:', ['Dr Rent 450, Cr Suspense 450', 'Dr Suspense 450, Cr Rent 450', 'Dr Cash 450, Cr Rent 450', 'Dr Rent 450, Cr Cash 450'], 0, 'Post the missing debit and clear suspense.'),
    Q(T2, 'Correcting that error changes profit by:', ['−450', '450', '0', '−900'], 0, 'Rent expense rises.', ans=-450),
    Q(T2, 'Sales of 1 000 were credited to Rent received in error. Correcting it changes profit by:', ['0', '1000', '−1000', '2000'], 0, 'Both are income; total income is unchanged.', ans=0),
    Q(T2, 'Equipment of 5 000 was debited to Repairs. The correction:', ['increases profit by 5000', 'decreases profit by 5000', 'does not change profit', 'clears the suspense account'], 0, 'An expense of 5 000 is removed (before considering depreciation).'),
    Q(T2, 'Which error is corrected through the suspense account?', ['A payment posted only to the Cash account', 'An error of principle', 'A complete reversal', 'An omitted transaction'], 0, 'Only errors that unbalanced the trial balance involve suspense.'),
    Q(T2, 'After all errors are corrected, the suspense account balance should be:', ['zero', 'equal to profit', 'equal to the cash balance', 'a debit'], 0, 'It is only a temporary holding account.'),
    # T3
    Q(T3, 'Profit 90 000; A\'s salary 10 000; interest on capital 3 000 (A) and 2 000 (B). The residual profit is:', ['75000', '80000', '85000', '90000'], 0, '90 000 − 10 000 − 3 000 − 2 000.', ans=resid),
    Q(T3, 'Residual 75 000 shared 3 : 2. A\'s share is:', ['45000', '30000', '37500', '25000'], 0, '75 000 × 3/5.', ans=a_share),
    Q(T3, 'A\'s total profit (salary 10 000 + interest 3 000 + share 45 000) is:', ['58000', '55000', '48000', '45000'], 0, 'Add all three.', ans=58000),
    Q(T3, 'A partner\'s salary is treated as:', ['an appropriation of profit', 'a business expense', 'a liability', 'drawings'], 0, 'It is part of how profit is shared.'),
    Q(T3, 'Interest charged on a partner\'s drawings:', ['is added back to the profit to be shared', 'reduces the business\'s expenses', 'is paid to the bank', 'increases the partner\'s share'], 0, 'It is charged to the partner and shared out.'),
    Q(T3, 'A partner\'s current account is credited with:', ['salary, interest on capital and profit share', 'drawings', 'interest on drawings', 'losses'], 0, 'Drawings and interest on drawings are debits.'),
    # T4
    Q(T4, 'Profit before tax 200 000 and tax at 25%. Profit after tax is:', ['150000', '50000', '175000', '200000'], 0, '200 000 − 50 000.', ans=150000),
    Q(T4, 'Opening retained earnings 200 000, profit after tax 150 000, dividends 100 000. Closing retained earnings are:', ['250000', '450000', '350000', '150000'], 0, '200 000 + 150 000 − 100 000.', ans=250000),
    Q(T4, '1 000 000 shares of nominal value 1 are issued at 1.50. The share premium is:', ['500000', '1500000', '1000000', '50000'], 0, '0.50 × 1 000 000.', ans=500000),
    Q(T4, 'Dividends paid to shareholders are:', ['a reduction in retained earnings, not an expense', 'an operating expense', 'a liability forever', 'part of cost of sales'], 0, 'They are distributions of profit.'),
    Q(T4, 'Limited liability means shareholders:', ['can lose only what they invested', 'are personally liable for all debts', 'cannot receive dividends', 'run the company'], 0, 'The company is a separate legal person.'),
    Q(T4, 'A dividend of 0.10 per share on 1 000 000 shares totals:', ['100000', '10000', '1000000', '0.10'], 0, '0.10 × 1 000 000.', ans=100000),
]

FLASH = [
    ['Receivables control account', 'Opening + credit sales − receipts − discounts − returns − write-offs.'],
    ['Contra entry', 'Set-off between a customer and supplier who are the same firm.'],
    ['Suspense account', 'Temporary account for trial balance differences; must clear to zero.'],
    ['Error correction', 'Journal the difference between what was done and what should have been.'],
    ['Partnership appropriation', 'Profit − salaries − interest on capital + interest on drawings, then share the residual.'],
    ['Partner salary', 'An appropriation of profit, not an expense.'],
    ['Share premium', '(Issue price − nominal value) × shares issued.'],
    ['Retained earnings', 'Opening + profit after tax − dividends.'],
]
