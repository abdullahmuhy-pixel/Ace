"""Principles of Macroeconomics, module 4: Fiscal policy and public debt."""
from verify import Q, sp
T1, T2, T3, T4 = ('The government budget', 'Fiscal policy and its multipliers', 'Automatic stabilisers and crowding out', 'Public debt and its sustainability')
R = sp.Rational
mpc = R(8, 10)
assert 350 - 300 == 50 and 50 - 20 == 30 and R(600, 1500) * 100 == 40
assert -mpc / (1 - mpc) == -4 and -(-4) * 10 == 40 and 1 / (1 - mpc) * 10 + (-mpc / (1 - mpc)) * 10 == 10
assert (R(5, 100) - R(3, 100)) * 60 == R(12, 10)

MODULE = {
    'title': 'Fiscal policy and public debt',
    'topics': [T1, T2, T3, T4],
    'overview': 'Fiscal policy is the government\'s use of spending and taxes to influence the economy. This module explains the budget, how changes in spending and taxes affect output through multipliers, the built-in stabilisers that soften recessions, the risk that government borrowing crowds out private investment, and when public debt becomes a problem.',
    'key_terms': ['Budget deficit', 'Budget surplus', 'Primary balance', 'Expansionary fiscal policy', 'Tax multiplier', 'Balanced-budget multiplier', 'Automatic stabilisers', 'Crowding out', 'Debt-to-GDP ratio'],
    'explanation': [
        'The budget balance is tax revenue minus government spending. A deficit must be financed by borrowing, which adds to public debt. The size of debt is judged relative to GDP, because a larger economy can carry more debt.',
        'Higher government spending or lower taxes shift AD right (expansionary policy); the reverse is contractionary. Spending changes have a larger multiplier than tax changes, because part of a tax cut is saved rather than spent.',
        'Some fiscal effects happen automatically: in a recession tax revenue falls and benefit payments rise, cushioning demand. Deliberate policy is slowed by decision and implementation lags, and heavy borrowing can raise interest rates and crowd out private investment. Whether debt is sustainable depends on the interest rate, growth and the primary balance.'],
    'quick_facts': [
        'Deficit = spending − revenue; primary balance excludes interest payments.',
        'Spending multiplier = 1/(1 − MPC); tax multiplier = −MPC/(1 − MPC).',
        'Balanced-budget multiplier = 1 (simple model).',
        'Automatic stabilisers: taxes and transfers that move with the cycle.',
        'Debt ratio rises if r > g unless there is a primary surplus.'],
}

NOTES = {
    T1: {
        'overview': 'The government budget compares spending with revenue. Deficits are financed by borrowing, which accumulates as public debt.',
        'key_terms': ['Revenue', 'Expenditure', 'Budget deficit', 'Budget surplus', 'Primary balance', 'Public debt', 'Direct and indirect taxes'],
        'explanation': [
            'Revenue comes mainly from taxes: direct taxes on income and profits, and indirect taxes on spending such as VAT and excise duties. Many resource-rich countries also rely on oil or mining royalties. Spending covers public services (health, education, security), investment in infrastructure, transfers such as pensions, and interest on debt.',
            'Deficit = spending − revenue. The primary balance excludes interest payments, showing whether current policy (as opposed to past borrowing) is adding to the debt. A government with a primary surplus can still run an overall deficit if interest costs are high.',
            'Debt is the stock of all past borrowing; the deficit is the flow added each year. The deficit and debt are usually expressed as a percentage of GDP. Taxes are described as progressive (richer people pay a larger share of income), proportional or regressive.'],
        'formulas_label': 'Formulas',
        'formulas': ['Budget balance = revenue − spending', 'Primary balance = revenue − (spending − interest)', 'Debt this year = debt last year + deficit', 'Debt ratio = debt ÷ GDP × 100%'],
        'steps': ['Add up revenue and spending.', 'Compute the overall balance.', 'Remove interest for the primary balance.', 'Express figures as a share of GDP.'],
        'worked_example': {
            'problem': 'A government collects 300 in revenue and spends 350, including 20 of interest on its debt. Find the overall and primary balances.',
            'steps': ['Overall balance = 300 − 350 = −50 (a deficit of 50).', 'Non-interest spending = 350 − 20 = 330.', 'Primary balance = 300 − 330 = −30 (a primary deficit of 30).'],
            'answer': 'Overall deficit 50; primary deficit 30.',
            'check': 'The difference between the two is exactly the interest bill of 20 ✓.'},
        'mistakes': ['Confusing the deficit (a flow) with the debt (a stock).', 'Treating a falling deficit as a falling debt.', 'Forgetting interest when computing the overall balance.', 'Mixing up progressive and regressive taxes.'],
        'real_world': 'Many oil-exporting countries see their deficits swing sharply with world oil prices, because royalties are a large share of revenue.',
        'exam_strategy': 'Always say whether a figure is a flow (deficit) or a stock (debt), and express it as a share of GDP when comparing countries or years.',
        'recap': ['Deficit = spending − revenue.', 'Primary balance excludes interest.', 'Debt accumulates deficits.', 'Compare as % of GDP.']},
    T2: {
        'overview': 'Fiscal policy shifts aggregate demand. Because of the multiplier, changes in spending and taxes have larger effects on GDP than the initial amounts, but spending and tax changes are not equally powerful.',
        'key_terms': ['Expansionary policy', 'Contractionary policy', 'Spending multiplier', 'Tax multiplier', 'Balanced-budget multiplier', 'Discretionary policy'],
        'explanation': [
            'An increase in government purchases G adds directly to spending, and the multiplier 1/(1 − MPC) magnifies it. With MPC = 0.8, an extra 10 of spending raises GDP by 50 in the simple model.',
            'A tax cut first raises disposable income; households spend only the MPC fraction of it. So the tax multiplier is −MPC/(1 − MPC): with MPC = 0.8 it is −4, and a tax cut of 10 raises GDP by 40, less than the same amount of spending.',
            'If spending and taxes both rise by 10, GDP rises by 50 − 40 = 10: the balanced-budget multiplier is 1. Real-world multipliers are smaller because of imports, taxes that rise with income, and crowding out, and they are larger in deep recessions when interest rates are low and resources idle.'],
        'formulas_label': 'Formulas',
        'formulas': ['Spending multiplier = 1/(1 − MPC)', 'Tax multiplier = −MPC/(1 − MPC)', 'Balanced-budget multiplier = 1', 'ΔY = multiplier × change in G or T'],
        'steps': ['Decide whether the policy changes G or T.', 'Choose the matching multiplier.', 'Multiply by the change, with the right sign.', 'Combine effects for mixed policies.'],
        'worked_example': {
            'problem': 'MPC = 0.8. Compare the effect on GDP of (a) a 10 increase in government spending and (b) a 10 tax cut. What if spending and taxes both rise by 10?',
            'steps': ['(a) Spending multiplier = 5, so ΔY = 50.', '(b) Tax multiplier = −0.8/0.2 = −4, so a tax cut of 10 gives ΔY = +40.', 'Both up by 10: 50 − 40 = 10.'],
            'answer': 'Spending raises GDP by 50, the tax cut by 40, and the balanced rise by 10.',
            'check': 'The tax cut is weaker because 20% of the extra disposable income is saved in the first round.'},
        'mistakes': ['Using the spending multiplier for a tax change.', 'Forgetting the minus sign of the tax multiplier.', 'Thinking a balanced-budget increase has no effect.', 'Ignoring leakages and crowding out in real economies.'],
        'real_world': 'Infrastructure spending is popular in recessions because it adds directly to demand and also raises future productive capacity, though projects can take years to start.',
        'exam_strategy': 'Present the two multipliers side by side when comparing spending and tax policies, and comment on real-world factors that shrink them.',
        'recap': ['Spending multiplier 1/(1 − MPC).', 'Tax multiplier −MPC/(1 − MPC).', 'Balanced-budget multiplier 1.', 'Real multipliers are smaller.']},
    T3: {
        'overview': 'Automatic stabilisers soften the business cycle without any new decisions. Discretionary fiscal policy is more powerful but slower, and heavy borrowing can crowd out private spending.',
        'key_terms': ['Automatic stabilisers', 'Progressive tax', 'Unemployment benefits', 'Time lags', 'Crowding out', 'Cyclical vs structural deficit'],
        'explanation': [
            'In a recession, income tax revenue falls automatically (especially with progressive taxes) and spending on benefits rises. This supports disposable income and spending. In a boom the reverse happens. These automatic stabilisers reduce the size of the multiplier and the swings in GDP.',
            'Discretionary policy (deliberate changes to spending or tax rates) faces lags: recognising the problem, passing the budget, and spending the money. By the time a stimulus arrives, the economy may already be recovering.',
            'Crowding out: when the government borrows more, it competes with private borrowers for funds, which can raise interest rates and reduce private investment. Crowding out is strong when the economy is near full employment and weak in a deep recession. Economists also separate the cyclical deficit (caused by the cycle) from the structural deficit (which would remain at full employment).'],
        'formulas_label': 'Key ideas',
        'formulas': ['Recession: taxes ↓ and transfers ↑ automatically', 'Actual deficit = cyclical + structural', 'Crowding out: G ↑ ⇒ interest rates ↑ ⇒ I ↓', 'Lags: recognition, decision, implementation'],
        'steps': ['Identify whether the change is automatic or discretionary.', 'Consider timing and lags.', 'Assess crowding out given the state of the economy.', 'Separate cyclical from structural deficits.'],
        'worked_example': {
            'problem': 'During a recession the deficit rises from 2% to 6% of GDP although no tax rates or programmes changed. Explain.',
            'steps': ['Falling incomes and profits reduce tax revenue automatically.', 'Rising unemployment increases spending on benefits.', 'Both widen the deficit without any new decisions.'],
            'answer': 'Automatic stabilisers caused the rise; most of the increase is a cyclical deficit that should shrink when the economy recovers.',
            'check': 'If the deficit stayed high after full recovery, that remaining part would be structural.'},
        'mistakes': ['Treating every deficit increase as reckless policy.', 'Assuming crowding out is always complete.', 'Forgetting the lags in discretionary policy.', 'Confusing cyclical and structural deficits.'],
        'real_world': 'Countries with large welfare systems saw their deficits widen automatically in the 2009 recession, which helped stop household spending from collapsing.',
        'exam_strategy': 'In evaluation, mention when crowding out is likely to be weak (spare capacity, low interest rates) and when it is likely to be strong (near full employment).',
        'recap': ['Stabilisers work automatically.', 'Discretionary policy has lags.', 'Crowding out depends on spare capacity.', 'Cyclical vs structural deficit.']},
    T4: {
        'overview': 'Public debt is the total owed by the government. Whether it is sustainable depends on the debt ratio, the interest rate on the debt, the growth rate of the economy and the primary balance.',
        'key_terms': ['Debt-to-GDP ratio', 'Interest rate–growth differential', 'Primary surplus', 'Sustainability', 'Default', 'External debt'],
        'explanation': [
            'The debt ratio changes each year approximately by (r − g) × d − primary surplus, where r is the interest rate on debt, g the growth rate of nominal GDP and d the current debt ratio. If r > g, the ratio grows unless the government runs a primary surplus.',
            'With d = 60%, r = 5% and g = 3%, the ratio rises by about (0.05 − 0.03) × 60 = 1.2 percentage points a year with a balanced primary budget. A primary surplus of 1.2% of GDP is needed just to keep the ratio stable.',
            'Debt becomes dangerous when investors doubt it will be repaid: interest rates jump, making the problem worse, and a default or bailout can follow. Debt in foreign currency is especially risky, because a depreciation raises its local-currency value. Borrowing for productive investment that raises future growth is easier to sustain than borrowing for current spending.'],
        'formulas_label': 'Formulas',
        'formulas': ['Δd ≈ (r − g) × d − primary surplus (all as % of GDP)', 'Stable debt needs primary surplus ≈ (r − g) × d', 'Debt ratio = debt ÷ GDP', 'Foreign-currency debt rises with depreciation'],
        'steps': ['Find d, r and g.', 'Compute (r − g) × d.', 'Subtract the primary surplus.', 'Judge whether the ratio rises or falls.'],
        'worked_example': {
            'problem': 'A country\'s debt is 60% of GDP, the interest rate on debt is 5% and nominal GDP grows 3%. What primary balance keeps the debt ratio stable?',
            'steps': ['(r − g) × d = (5% − 3%) × 60 = 1.2 percentage points.', 'With a balanced primary budget, the ratio would rise by 1.2 points a year.', 'To stop it rising, a primary surplus of 1.2% of GDP is needed.'],
            'answer': 'A primary surplus of about 1.2% of GDP.',
            'check': 'If growth rose to 5% (r = g), a balanced primary budget would be enough to keep the ratio stable.'},
        'mistakes': ['Judging debt by its size alone rather than as a share of GDP.', 'Forgetting that growth reduces the debt ratio.', 'Ignoring the currency in which debt is owed.', 'Assuming all public debt is bad.'],
        'real_world': 'Several African countries faced debt distress after 2020 as global interest rates rose and their currencies weakened, increasing the cost of dollar-denominated debt; some restructured their debts with creditors.',
        'exam_strategy': 'Use the debt-dynamics formula with numbers, then evaluate: is the borrowing for investment, what currency is it in, and is growth likely to exceed interest rates?',
        'recap': ['Δd ≈ (r − g)d − primary surplus.', 'r > g pushes the ratio up.', 'Foreign-currency debt is riskier.', 'Investment borrowing is easier to sustain.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Revenue 300 and spending 350. The budget balance is:', ['−50', '50', '650', '−350'], 0, '300 − 350 = −50, a deficit.', ans=-50),
    Q(T1, 'Of the 350 spent, 20 is interest. The primary balance is:', ['−30', '−50', '−70', '30'], 0, '300 − 330 = −30.', ans=-30),
    Q(T1, 'Debt 600 and GDP 1500. The debt-to-GDP ratio is:', ['40%', '60%', '25%', '250%'], 0, '600/1500 = 0.4.', ans=40),
    Q(T1, 'The deficit differs from the debt because the deficit is:', ['a yearly flow, the debt is the accumulated stock', 'always larger', 'owed to foreigners', 'measured in real terms'], 0, 'Deficits add to the debt each year.'),
    Q(T1, 'A tax where richer people pay a larger share of income is:', ['progressive', 'regressive', 'proportional', 'indirect'], 0, 'The average tax rate rises with income.'),
    Q(T1, 'VAT is an example of:', ['an indirect tax', 'a direct tax', 'a transfer payment', 'a subsidy'], 0, 'It is a tax on spending.'),
    # T2
    Q(T2, 'MPC = 0.8. The tax multiplier is:', ['−4', '−5', '4', '−0.8'], 0, '−0.8/(1 − 0.8) = −4.', ans=-4),
    Q(T2, 'MPC = 0.8. A tax cut of 10 raises GDP by:', ['40', '50', '10', '8'], 0, '−4 × (−10) = 40.', ans=40),
    Q(T2, 'MPC = 0.8. Government spending rises by 10. GDP rises by:', ['50', '40', '10', '8'], 0, 'Multiplier 5 × 10.', ans=50),
    Q(T2, 'Spending and taxes both rise by 10 (MPC = 0.8). GDP rises by:', ['10', '0', '50', '90'], 0, '50 − 40 = 10; the balanced-budget multiplier is 1.', ans=10),
    Q(T2, 'A tax cut has a smaller effect than an equal rise in spending because:', ['part of the tax cut is saved', 'taxes are never cut', 'spending is always wasted', 'the MPC is zero'], 0, 'Only the MPC fraction of the extra income is spent in the first round.'),
    Q(T2, 'Which is expansionary fiscal policy?', ['Cutting income tax rates', 'Raising interest rates', 'Selling government bonds', 'Raising VAT'], 0, 'Higher disposable income raises consumption.'),
    # T3
    Q(T3, 'Which is an automatic stabiliser?', ['Unemployment benefits', 'A new road programme', 'A one-off tax rebate', 'An interest-rate cut'], 0, 'Spending on benefits rises automatically when unemployment rises.'),
    Q(T3, 'In a recession, with no change in policy, the budget deficit usually:', ['widens', 'narrows', 'stays the same', 'turns into a surplus'], 0, 'Tax revenue falls and benefit spending rises.'),
    Q(T3, 'Crowding out occurs when government borrowing:', ['raises interest rates and reduces private investment', 'raises private investment', 'lowers interest rates', 'reduces imports'], 0, 'The government competes for loanable funds.'),
    Q(T3, 'Crowding out is likely to be weakest when:', ['the economy is in a deep recession with low interest rates', 'the economy is at full employment', 'interest rates are rising fast', 'investment demand is strong'], 0, 'With idle resources and low rates, extra borrowing pushes rates up little.'),
    Q(T3, 'The structural deficit is the deficit that:', ['would remain with the economy at full employment', 'is caused by the business cycle', 'is always zero', 'includes only interest payments'], 0, 'It does not disappear when the economy recovers.'),
    Q(T3, 'A key weakness of discretionary fiscal policy is:', ['time lags in decision and implementation', 'it has no effect on AD', 'it is controlled by the central bank', 'it always causes deflation'], 0, 'Help may arrive after the recession ends.'),
    # T4
    Q(T4, 'Debt 60% of GDP, r = 5%, g = 3%. With a balanced primary budget, the debt ratio rises by about:', ['1.2 points a year', '2 points a year', '3 points a year', '0.6 points a year'], 0, '(0.05 − 0.03) × 60 = 1.2.'),
    Q(T4, 'In that case, the primary surplus needed to keep the debt ratio stable is about:', ['1.2% of GDP', '2% of GDP', '5% of GDP', '0%'], 0, 'It must offset (r − g) × d = 1.2.'),
    Q(T4, 'If nominal GDP growth exceeds the interest rate on debt (g > r), a balanced primary budget makes the debt ratio:', ['fall', 'rise', 'stay constant', 'double'], 0, '(r − g) × d is negative.'),
    Q(T4, 'Why is foreign-currency debt riskier?', ['A depreciation raises its value in local currency', 'It has no interest', 'It cannot be repaid', 'It is always short-term'], 0, 'The local cost of repayment rises when the currency falls.'),
    Q(T4, 'Borrowing is easier to sustain when it finances:', ['productive investment that raises future growth', 'current consumption only', 'interest payments', 'tax cuts for imports'], 0, 'Higher growth reduces the future debt ratio.'),
    Q(T4, 'Investors losing confidence in a government\'s debt typically causes:', ['higher interest rates on new borrowing', 'lower interest rates', 'automatic debt cancellation', 'a budget surplus'], 0, 'This can make the debt problem worse.'),
]

FLASH = [
    ['Budget deficit', 'Government spending minus revenue (a flow).'],
    ['Primary balance', 'Revenue minus non-interest spending.'],
    ['Tax multiplier', '−MPC/(1 − MPC).'],
    ['Balanced-budget multiplier', '1 in the simple model.'],
    ['Automatic stabilisers', 'Taxes and transfers that move with the cycle without new decisions.'],
    ['Crowding out', 'Government borrowing raises interest rates and reduces private investment.'],
    ['Debt dynamics', 'Δd ≈ (r − g)d − primary surplus.'],
    ['Structural deficit', 'The deficit that would remain at full employment.'],
]
