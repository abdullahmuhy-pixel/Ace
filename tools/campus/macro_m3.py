"""Principles of Macroeconomics, module 3: Money, banking and monetary policy."""
from verify import Q, sp
T1, T2, T3, T4 = ('Money and its functions', 'Banks and money creation', 'Central banks and monetary policy', 'The quantity theory of money and inflation')
R = sp.Rational
assert 1 / R(1, 10) == 10 and 1000 * 10 == 10000 and 1000 * R(9, 10) == 900 and 1 / R(2, 10) == 5
assert R(200 * 5, 500) == 2 and 8 + 0 - 3 == 5

MODULE = {
    'title': 'Money, banking and monetary policy',
    'topics': [T1, T2, T3, T4],
    'overview': 'Money makes trade possible, banks create most of it, and central banks try to manage it to keep inflation low and stable. This module explains what money is, how commercial banks expand the money supply through lending, how central banks set interest rates, and the long-run link between money growth and inflation.',
    'key_terms': ['Medium of exchange', 'Store of value', 'Unit of account', 'Fractional reserve banking', 'Money multiplier', 'Central bank', 'Policy rate', 'Open market operations', 'Quantity theory of money'],
    'explanation': [
        'Money is anything widely accepted in payment. It solves the "double coincidence of wants" problem of barter. Today most money is not notes and coins but bank deposits, including mobile-money balances.',
        'Banks keep only a fraction of deposits as reserves and lend the rest. Each loan is spent and redeposited somewhere, allowing further lending, so the banking system as a whole creates money. The central bank influences this process through interest rates, reserve requirements and buying or selling assets.',
        'In the short run, monetary policy changes spending and output by changing interest rates. In the long run, output is set by real resources, so faster money growth mainly produces higher inflation. That is why most central banks now aim at an inflation target.'],
    'quick_facts': [
        'Functions of money: medium of exchange, unit of account, store of value, standard of deferred payment.',
        'Simple money multiplier = 1 ÷ reserve ratio.',
        'Lower policy rate ⇒ more borrowing and spending (expansionary).',
        'Open market purchases add reserves; sales remove them.',
        'MV = PY; in growth rates, %ΔM + %ΔV ≈ %ΔP + %ΔY.'],
}

NOTES = {
    T1: {
        'overview': 'Money is any asset that is generally accepted in exchange for goods and services. It is defined by what it does, not by what it is made of.',
        'key_terms': ['Barter', 'Double coincidence of wants', 'Medium of exchange', 'Unit of account', 'Store of value', 'Fiat money', 'Liquidity'],
        'explanation': [
            'Under barter, trade needs a double coincidence of wants: you must find someone who has what you want and wants what you have. Money removes this problem, which lowers the cost of trading and allows specialisation.',
            'Money has four functions: a medium of exchange (used to pay), a unit of account (prices are quoted in it), a store of value (holds purchasing power over time), and a standard of deferred payment (debts are written in it). High inflation damages the store-of-value and unit-of-account functions first.',
            'Modern money is fiat money: it has value because the government declares it legal tender and people trust it, not because it is backed by gold. Measures of the money supply include narrow money (notes, coins and instant-access deposits) and broad money (which adds savings deposits). Liquidity is how quickly an asset can be turned into spending without loss.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Four functions: exchange, account, store, deferred payment', 'Fiat money: value from trust and legal tender', 'Narrow money ⊂ broad money', 'Liquidity: ease of conversion to spending'],
        'steps': ['Identify which function is in question.', 'Explain the problem money solves.', 'Assess how well an asset performs each function.', 'Classify it as money or near-money by liquidity.'],
        'worked_example': {
            'problem': 'Does a mobile-money balance (such as M-Pesa) count as money?',
            'steps': ['Medium of exchange: widely accepted for payments in shops and between people ✓.', 'Unit of account: balances are in the national currency ✓.', 'Store of value: holds its value as well as cash, apart from inflation ✓.'],
            'answer': 'Yes. It performs the functions of money and is a form of deposit money.',
            'check': 'Central banks in Kenya and elsewhere include mobile-money balances in their analysis of the money supply, for exactly this reason.'},
        'mistakes': ['Defining money by its physical form.', 'Thinking credit cards are money (they are a way of borrowing; the money is the later bank payment).', 'Confusing store of value with medium of exchange.', 'Thinking fiat money is worthless because it is not backed by gold.'],
        'real_world': 'In very high inflation, such as Zimbabwe in 2008, the local currency stopped working as a store of value and unit of account, and people switched to US dollars and South African rand.',
        'exam_strategy': 'When asked to evaluate whether something is money, test it against each function in turn. A structured answer earns more than a single yes or no.',
        'recap': ['Money solves the double coincidence of wants.', 'Four functions.', 'Fiat money relies on trust.', 'Most money is bank deposits.']},
    T2: {
        'overview': 'Commercial banks keep a fraction of deposits as reserves and lend the rest. As loans are spent and redeposited, the banking system creates new money.',
        'key_terms': ['Reserves', 'Reserve ratio', 'Fractional reserve banking', 'Money multiplier', 'Bank run', 'Deposit insurance'],
        'explanation': [
            'A bank\'s balance sheet has assets (reserves, loans, securities) and liabilities (deposits). If the reserve ratio is 10%, a new deposit of 1000 allows the bank to keep 100 and lend 900.',
            'The 900 is spent and ends up as a deposit in another bank, which keeps 90 and lends 810, and so on. The total deposits created are 1000 × 1/0.1 = 10 000. The simple money multiplier is 1 ÷ reserve ratio.',
            'In practice the multiplier is smaller, because people hold some cash and banks keep extra reserves; and modern central banks control interest rates rather than reserves directly. Because banks lend most deposits, they would fail if everyone withdrew at once (a bank run), so countries use deposit insurance, capital requirements and the central bank as lender of last resort.'],
        'formulas_label': 'Formulas',
        'formulas': ['Required reserves = reserve ratio × deposits', 'Excess reserves can be lent', 'Simple money multiplier = 1 ÷ reserve ratio', 'Maximum new deposits = initial deposit × multiplier'],
        'steps': ['Find the reserve ratio.', 'Compute the multiplier 1/rr.', 'Multiply by the initial deposit for the total.', 'Subtract the initial deposit for newly created money.'],
        'worked_example': {
            'problem': 'The reserve ratio is 10%. A customer deposits 1000 in cash. What is the maximum increase in total deposits in the banking system?',
            'steps': ['The first bank keeps 100 and lends 900.', 'Multiplier = 1/0.1 = 10.', 'Maximum total deposits = 1000 × 10 = 10 000.'],
            'answer': 'Up to 10 000 in total deposits, of which 9000 is newly created.',
            'check': 'The rounds 1000 + 900 + 810 + … form a geometric series with sum 1000/(1 − 0.9) = 10 000 ✓.'},
        'mistakes': ['Using the reserve ratio itself as the multiplier.', 'Forgetting that cash holdings reduce the multiplier.', 'Counting the original cash deposit as newly created money.', 'Thinking banks lend out depositors\' cash only, rather than creating deposits.'],
        'real_world': 'Bank failures, such as several in the 2008 financial crisis and smaller regional failures since, show why deposit insurance and strong capital rules matter for confidence.',
        'exam_strategy': 'If the question asks for the "maximum" change, use the simple multiplier and say it is a maximum because leakages (cash holdings, excess reserves) make the real effect smaller.',
        'recap': ['Banks keep a fraction as reserves.', 'Multiplier = 1/reserve ratio.', 'Real multipliers are smaller.', 'Deposit insurance prevents bank runs.']},
    T3: {
        'overview': 'The central bank manages a country\'s money and banking system. Its main tool is the policy interest rate, which it sets to keep inflation close to its target while supporting output and jobs.',
        'key_terms': ['Central bank', 'Policy rate', 'Open market operations', 'Reserve requirement', 'Inflation targeting', 'Transmission mechanism', 'Quantitative easing'],
        'explanation': [
            'Central banks (such as the Central Bank of Nigeria, the South African Reserve Bank or the European Central Bank) issue currency, supervise banks, act as lender of last resort and run monetary policy. Many have an explicit inflation target, often around 2% to 6%.',
            'The main tool is the policy rate, the rate at which the central bank lends to commercial banks. Open market operations (buying or selling government bonds) and reserve requirements help keep market rates close to it. In crises central banks may also buy large amounts of assets (quantitative easing).',
            'The transmission mechanism: a cut in the policy rate lowers loan and mortgage rates, raises asset prices and often weakens the currency. Consumption, investment and net exports rise, shifting AD right. The effects take about one to two years to fully work through, so policy must look ahead.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Expansionary: lower rates, buy bonds, lower reserve ratio', 'Contractionary: higher rates, sell bonds, higher reserve ratio', 'Rate cut ⇒ C, I, X − M rise ⇒ AD shifts right', 'Policy works with long and variable lags'],
        'steps': ['Diagnose: is inflation above or below target? Is there an output gap?', 'Choose expansionary or contractionary policy.', 'Trace the effect through the transmission mechanism.', 'Note the time lags and side effects.'],
        'worked_example': {
            'problem': 'Inflation is 9% against a target of 3% to 6%, and the economy is close to full capacity. What should the central bank do, and how does it work?',
            'steps': ['Inflation is above target, so policy should be tightened.', 'Raise the policy rate (and sell bonds to drain reserves).', 'Higher borrowing costs reduce consumption and investment, and a stronger currency reduces net exports.'],
            'answer': 'Raise interest rates. AD shifts left, easing pressure on prices over the following year or two.',
            'check': 'The cost is slower growth and possibly higher unemployment in the short run, which the bank must weigh.'},
        'mistakes': ['Saying the central bank lowers rates to fight inflation.', 'Confusing monetary policy (central bank) with fiscal policy (government).', 'Forgetting the time lags.', 'Thinking open market purchases reduce the money supply.'],
        'real_world': 'Between 2022 and 2023 central banks around the world raised interest rates rapidly to bring down the surge in inflation that followed the pandemic and the energy price shock.',
        'exam_strategy': 'Write out the transmission chain step by step (rate → borrowing → spending → AD → prices). Each link is usually credited.',
        'recap': ['Policy rate is the main tool.', 'Open market operations and reserves support it.', 'Rate cut: expansionary; rate rise: contractionary.', 'Effects take time.']},
    T4: {
        'overview': 'The quantity theory of money links the money supply to the price level. In the long run, persistent inflation is mainly caused by money growing faster than real output.',
        'key_terms': ['Equation of exchange', 'Velocity of money', 'Quantity theory', 'Money neutrality', 'Hyperinflation', 'Fisher effect'],
        'explanation': [
            'The equation of exchange MV = PY says that money times the number of times it is spent (velocity V) equals nominal GDP (price level P times real output Y). It is true by definition; it becomes a theory when we add assumptions.',
            'The quantity theory assumes V is fairly stable and Y is set by real resources in the long run. Then increases in M mainly raise P. In growth rates: %ΔM + %ΔV ≈ %ΔP + %ΔY. If money grows 8% a year, velocity is stable and real output grows 3%, inflation is about 5%.',
            'Money is neutral in the long run: it affects prices, not real output. Governments that finance large deficits by printing money cause very high inflation (hyperinflation), as in Germany in 1923 or Zimbabwe in 2008. The Fisher effect says higher expected inflation raises nominal interest rates one for one.'],
        'formulas_label': 'Formulas',
        'formulas': ['MV = PY', 'P = MV ÷ Y', '%ΔM + %ΔV ≈ %ΔP + %ΔY', 'Fisher: nominal rate ≈ real rate + expected inflation'],
        'steps': ['Write MV = PY with the known values.', 'Solve for the unknown.', 'For growth rates, use the growth-rate form.', 'Interpret: is money growth outpacing real output?'],
        'worked_example': {
            'problem': 'Money grows 8% a year, velocity is constant and real GDP grows 3% a year. Estimate inflation. Then find P if M = 200, V = 5 and Y = 500.',
            'steps': ['%ΔP ≈ %ΔM + %ΔV − %ΔY = 8 + 0 − 3 = 5%.', 'For the level: P = MV/Y = 200 × 5 / 500.', 'P = 2.'],
            'answer': 'Inflation about 5% a year; price level P = 2.',
            'check': 'Nominal GDP = MV = 1000 = PY = 2 × 500 ✓.'},
        'mistakes': ['Treating MV = PY as always predicting inflation, even when velocity changes.', 'Adding instead of subtracting real growth.', 'Thinking printing money makes a country richer in the long run.', 'Confusing velocity with the money multiplier.'],
        'real_world': 'In 2020 money supplies grew fast in many countries without immediate inflation because velocity fell during lockdowns; inflation came later as spending recovered.',
        'exam_strategy': 'State the assumptions (stable V, Y at potential) when you use the quantity theory to predict inflation; evaluation marks come from questioning them.',
        'recap': ['MV = PY.', 'Stable V and Y: more M means higher P.', 'Growth form: %ΔP ≈ %ΔM + %ΔV − %ΔY.', 'Money is neutral in the long run.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Prices quoted in naira or cedis show money acting as a:', ['unit of account', 'store of value', 'medium of exchange', 'standard of deferred payment'], 0, 'It is the common measure of value.'),
    Q(T1, 'Money solves the barter problem known as:', ['the double coincidence of wants', 'diminishing returns', 'the free-rider problem', 'adverse selection'], 0, 'Barter needs both traders to want what the other has.'),
    Q(T1, 'Fiat money has value because:', ['people trust it and the government declares it legal tender', 'it is backed by gold', 'it is made of valuable metal', 'banks guarantee it'], 0, 'Its value rests on acceptance and trust.'),
    Q(T1, 'High inflation damages money\'s function as a:', ['store of value', 'medium of exchange only', 'physical object', 'barter good'], 0, 'Money loses purchasing power quickly.'),
    Q(T1, 'Which is the most liquid asset?', ['Cash', 'A house', 'A 10-year bond', 'A factory'], 0, 'Cash can be spent immediately without loss.'),
    Q(T1, 'A credit card is best described as:', ['a way of borrowing, not money itself', 'narrow money', 'broad money', 'fiat money'], 0, 'The money changes hands later, when the card bill is paid.'),
    # T2
    Q(T2, 'The reserve ratio is 10%. The simple money multiplier is:', ['10', '0.1', '9', '100'], 0, '1/0.1.', ans=10),
    Q(T2, 'With a 10% reserve ratio, a 1000 deposit can raise total deposits by up to:', ['10000', '1000', '9000', '1100'], 0, '1000 × 10.', ans=10000),
    Q(T2, 'With a 10% reserve ratio, the first bank can lend out of a 1000 deposit:', ['900', '100', '1000', '9000'], 0, 'It keeps 10% (100) as reserves.', ans=900),
    Q(T2, 'The reserve ratio is 20%. The simple money multiplier is:', ['5', '20', '0.2', '4'], 0, '1/0.2.', ans=5),
    Q(T2, 'The actual money multiplier is smaller than 1/reserve ratio because:', ['people hold some cash and banks keep extra reserves', 'banks lend all deposits', 'interest rates are zero', 'the central bank prints money'], 0, 'These are leakages from the deposit-creation process.'),
    Q(T2, 'Deposit insurance is designed to prevent:', ['bank runs', 'inflation', 'unemployment', 'trade deficits'], 0, 'Depositors know their money is safe, so they do not rush to withdraw.'),
    # T3
    Q(T3, 'To reduce inflation, a central bank would normally:', ['raise the policy interest rate', 'lower the policy interest rate', 'buy government bonds', 'cut taxes'], 0, 'Higher rates reduce borrowing and spending.'),
    Q(T3, 'Open market purchases of government bonds by the central bank:', ['add reserves and lower interest rates', 'remove reserves', 'raise interest rates', 'raise the reserve ratio'], 0, 'The bank pays for the bonds with new reserves.'),
    Q(T3, 'Which is monetary policy?', ['Changing the policy interest rate', 'Raising income tax', 'Building new roads', 'Cutting import tariffs'], 0, 'Monetary policy is run by the central bank.'),
    Q(T3, 'A cut in interest rates usually causes the domestic currency to:', ['depreciate', 'appreciate', 'stay fixed', 'disappear'], 0, 'Lower returns make the currency less attractive to foreign investors.'),
    Q(T3, 'Why must monetary policy be forward-looking?', ['Its effects take one to two years to work through', 'It works instantly', 'Inflation never changes', 'Governments decide it'], 0, 'Long and variable lags.'),
    Q(T3, 'Quantitative easing means the central bank:', ['buys large amounts of assets to lower long-term rates', 'raises taxes', 'sells all its bonds', 'fixes the exchange rate'], 0, 'Used when short-term rates are already near zero.'),
    # T4
    Q(T4, 'M = 200, V = 5 and Y = 500. The price level P is:', ['2', '0.5', '2000', '5'], 0, 'P = MV/Y = 1000/500.', ans=2),
    Q(T4, 'Money grows 8%, velocity is constant and real output grows 3%. Inflation is about:', ['5%', '11%', '8%', '3%'], 0, '8 + 0 − 3.', ans=5),
    Q(T4, 'In the equation MV = PY, V stands for:', ['the velocity of money', 'value added', 'volume of trade', 'variance of prices'], 0, 'How many times each unit of money is spent per period.'),
    Q(T4, 'Money neutrality means that in the long run money affects:', ['prices but not real output', 'real output but not prices', 'neither', 'only interest rates'], 0, 'Real output depends on real resources.'),
    Q(T4, 'Hyperinflation is usually caused by:', ['governments printing money to finance large deficits', 'too little money', 'high productivity growth', 'falling oil prices'], 0, 'Money grows far faster than output.'),
    Q(T4, 'Expected inflation rises by 3 points with an unchanged real rate. By the Fisher effect, nominal interest rates:', ['rise by about 3 points', 'fall by 3 points', 'stay the same', 'double'], 0, 'Nominal ≈ real + expected inflation.'),
]

FLASH = [
    ['Functions of money', 'Medium of exchange, unit of account, store of value, standard of deferred payment.'],
    ['Fiat money', 'Valuable because of trust and legal tender, not backing.'],
    ['Money multiplier', '1 ÷ reserve ratio (a maximum).'],
    ['Policy rate', 'Interest rate set by the central bank; its main tool.'],
    ['Open market purchase', 'Central bank buys bonds: more reserves, lower rates.'],
    ['Transmission mechanism', 'Rate → borrowing → spending → AD → prices.'],
    ['Equation of exchange', 'MV = PY.'],
    ['Quantity theory (growth form)', '%ΔP ≈ %ΔM + %ΔV − %ΔY.'],
]
