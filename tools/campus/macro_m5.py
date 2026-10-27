"""Principles of Macroeconomics, module 5: Growth and the open economy."""
from verify import Q, sp
T1, T2, T3, T4 = ('Long-run economic growth', 'International trade and protection', 'Exchange rates', 'The balance of payments')
R = sp.Rational
assert (100 - 2 * 10, max(0, 2 * 10 - 20)) == (80, 0) and (100 - 2 * 12, 2 * 12 - 20) == (76, 4) and 2 * (76 - 4) == 144
assert 20 * 1500 == 30000 and 20 * 1600 == 32000 and R(3000, 5) == 600
assert 500 - 600 - 30 + 80 == -50 and R(70, 7) == 10

MODULE = {
    'title': 'Growth and the open economy',
    'topics': [T1, T2, T3, T4],
    'overview': 'In the long run, living standards depend on productivity growth. Most economies are also open: they trade goods, services and capital with the rest of the world. This module covers what drives long-run growth, why countries trade and why they sometimes restrict trade, how exchange rates are set and what they do, and how a country\'s transactions with the world are recorded.',
    'key_terms': ['Productivity', 'Physical capital', 'Human capital', 'Technology', 'Institutions', 'Tariff', 'Quota', 'Exchange rate', 'Depreciation', 'Purchasing power parity', 'Current account', 'Financial account'],
    'explanation': [
        'Output per person rises when each worker can produce more. That depends on physical capital (machines and infrastructure), human capital (skills and health), technology, and institutions such as property rights and the rule of law. Because growth compounds, small differences in growth rates create huge differences in income over a generation.',
        'Countries gain from trade by specialising according to comparative advantage. Tariffs and quotas protect domestic producers but raise prices for consumers and create deadweight losses, although governments sometimes use them to shelter new industries or for strategic reasons.',
        'An exchange rate is the price of one currency in terms of another. Its movements change the price of exports and imports, and therefore trade flows, inflation and the cost of foreign debt. The balance of payments records every transaction with the rest of the world; a current-account deficit must be matched by a financial-account inflow.'],
    'quick_facts': [
        'Growth sources: capital, labour, human capital, technology, institutions.',
        'Rule of 70: doubling time ≈ 70 ÷ growth rate.',
        'A tariff raises domestic prices, cuts imports and creates deadweight losses.',
        'Depreciation makes exports cheaper abroad and imports dearer at home.',
        'Current account + capital account + financial account ≈ 0.'],
}

NOTES = {
    T1: {
        'overview': 'Long-run economic growth is a sustained rise in real GDP per person. It comes from increases in productivity, which depend on capital, skills, technology and good institutions.',
        'key_terms': ['Labour productivity', 'Physical capital', 'Human capital', 'Technological progress', 'Diminishing returns to capital', 'Catch-up growth', 'Institutions'],
        'explanation': [
            'Output per worker depends on how much capital each worker has, how skilled and healthy they are, and the technology they use. Investment in machines raises output, but with diminishing returns: each extra machine adds less. Sustained growth therefore needs continuing technological progress.',
            'Poorer countries can grow faster by adopting existing technology and building capital where it is scarce (catch-up or convergence). This explains the rapid growth of East Asian economies, but catch-up is not automatic.',
            'Institutions matter: secure property rights, enforceable contracts, low corruption, macroeconomic stability and good public services encourage saving, investment and innovation. Growth also has costs, such as pollution and inequality, so economists increasingly focus on inclusive and sustainable growth.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Living standards ≈ real GDP per person', 'Productivity = output ÷ hours worked', 'Doubling time ≈ 70 ÷ growth rate (%)', 'Diminishing returns to capital ⇒ technology is needed for sustained growth'],
        'steps': ['Identify the source of growth (capital, labour, skills, technology, institutions).', 'Explain the mechanism for productivity.', 'Consider diminishing returns.', 'Evaluate costs and sustainability.'],
        'worked_example': {
            'problem': 'Country A grows at 7% a year and country B at 2%. How long does each take to double real GDP per person?',
            'steps': ['Rule of 70: A doubles in 70/7 = 10 years.', 'B doubles in 70/2 = 35 years.', 'In 35 years A doubles about 3.5 times, roughly an 11-fold increase.'],
            'answer': 'A doubles in about 10 years, B in about 35.',
            'check': '1.07³⁵ ≈ 10.7, consistent with "about 11 times" ✓.'},
        'mistakes': ['Equating growth in total GDP with growth in living standards (population matters).', 'Ignoring diminishing returns to capital.', 'Treating growth as automatic for poor countries.', 'Forgetting institutions as a cause of growth.'],
        'real_world': 'South Korea and Ghana had similar income per person in the early 1960s; decades of high investment, education and export-led industrialisation made South Korea many times richer today.',
        'exam_strategy': 'Link each growth factor to productivity explicitly ("better education raises human capital, so each worker produces more"). Lists of factors without mechanisms score poorly.',
        'recap': ['Growth = rising real GDP per person.', 'Capital, skills, technology, institutions.', 'Diminishing returns to capital.', 'Compound growth makes big differences.']},
    T2: {
        'overview': 'International trade lets countries specialise in what they do relatively best. Trade barriers such as tariffs protect some domestic producers but usually make the country as a whole worse off.',
        'key_terms': ['Comparative advantage', 'Gains from trade', 'Tariff', 'Quota', 'Protectionism', 'Infant industry', 'Dumping', 'Terms of trade'],
        'explanation': [
            'If countries specialise according to comparative advantage and trade, total output rises and both can consume beyond their own production possibilities. Trade also brings competition, economies of scale and access to new technology. The gains are not shared equally: workers in import-competing industries can lose.',
            'A tariff is a tax on imports. It raises the domestic price, which increases domestic production, reduces consumption and cuts imports. The government collects revenue, domestic producers gain, consumers lose more than both gains combined, and the difference is deadweight loss. A quota limits the quantity of imports directly.',
            'Arguments for protection include protecting infant industries until they are competitive, national security, responding to dumping (selling below cost), and protecting jobs in the short run. Costs include higher prices, retaliation by other countries and inefficient firms that never become competitive.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Domestic price with tariff = world price + tariff', 'Imports = Qd − Qs at the domestic price', 'Tariff revenue = tariff × imports', 'Consumer loss > producer gain + tariff revenue (deadweight loss)'],
        'steps': ['Find Qd and Qs at the world price; imports are the gap.', 'Add the tariff to the price.', 'Recompute Qd, Qs and imports.', 'Compute revenue and identify gains, losses and deadweight loss.'],
        'worked_example': {
            'problem': 'Domestic demand is Qd = 100 − 2P and supply is Qs = 2P − 20. The world price is 10. A tariff of 2 is imposed. Find imports before and after, and the tariff revenue.',
            'steps': ['At P = 10: Qd = 80, Qs = 0, so imports = 80.', 'With the tariff, P = 12: Qd = 76, Qs = 4, so imports = 72.', 'Revenue = 2 × 72 = 144.'],
            'answer': 'Imports fall from 80 to 72; tariff revenue is 144; domestic production rises from 0 to 4.',
            'check': 'Consumers now buy 4 fewer units and pay 2 more on each of the 76 they buy, a loss larger than the revenue plus the producers\' gain.'},
        'mistakes': ['Thinking a tariff is paid by foreign exporters (domestic buyers pay most of it).', 'Forgetting that domestic production rises under a tariff.', 'Computing revenue with the old import quantity.', 'Treating comparative and absolute advantage as the same.'],
        'real_world': 'The African Continental Free Trade Area aims to remove most tariffs between African countries, to expand regional trade, which is currently a small share of the continent\'s total trade.',
        'exam_strategy': 'On a tariff diagram, label world price, world price + tariff, the four quantities, the revenue rectangle and the two deadweight-loss triangles. Then evaluate with one argument for and one against.',
        'recap': ['Trade by comparative advantage raises total output.', 'Tariff: higher price, fewer imports, revenue, DWL.', 'Some gain, consumers lose more.', 'Infant industry and security arguments.']},
    T3: {
        'overview': 'An exchange rate is the price of one currency in another. It is set by demand and supply in currency markets (or fixed by the government), and its movements change the prices of exports and imports.',
        'key_terms': ['Exchange rate', 'Appreciation', 'Depreciation', 'Floating rate', 'Fixed rate', 'Devaluation', 'Purchasing power parity', 'Real exchange rate'],
        'explanation': [
            'Demand for a currency comes from foreigners buying the country\'s exports and assets; supply comes from residents buying imports and foreign assets. Higher interest rates, strong export prices and investor confidence tend to raise demand and cause appreciation; high inflation and political risk tend to cause depreciation.',
            'A depreciation makes exports cheaper for foreigners and imports more expensive at home. It tends to raise net exports (after a delay) but also raises inflation through import prices and increases the local cost of foreign-currency debt. An appreciation does the reverse.',
            'Under a fixed regime the central bank buys or sells its currency to hold the rate, which requires foreign reserves. Purchasing power parity (PPP) says that in the long run exchange rates should move so that the same basket costs the same everywhere; the Big Mac index is a light-hearted test.'],
        'formulas_label': 'Formulas',
        'formulas': ['Local price of an import = foreign price × exchange rate (local per foreign)', 'Depreciation: more local currency per unit of foreign currency', 'PPP rate = local price ÷ foreign price of the same basket', 'Real exchange rate adjusts the nominal rate for relative prices'],
        'steps': ['Write the rate as local currency per unit of foreign currency.', 'Convert prices by multiplying or dividing.', 'Decide whether the currency appreciated or depreciated.', 'Trace the effects on trade, inflation and debt.'],
        'worked_example': {
            'problem': 'A product costs $20. The exchange rate moves from 1500 to 1600 naira per dollar. What happens to its naira price, and what does this mean for the naira?',
            'steps': ['Before: 20 × 1500 = 30 000 naira.', 'After: 20 × 1600 = 32 000 naira.', 'More naira are needed per dollar, so the naira has depreciated.'],
            'answer': 'The import price rises from 30 000 to 32 000 naira; the naira has depreciated.',
            'check': 'Nigerian exports priced in naira become cheaper for dollar buyers, which is the other side of the same change.'},
        'mistakes': ['Mixing up the quote direction (local per foreign vs foreign per local).', 'Saying a depreciation makes exports dearer.', 'Ignoring the effect of depreciation on inflation and foreign debt.', 'Expecting PPP to hold in the short run.'],
        'real_world': 'Several African currencies depreciated sharply in 2023 and 2024, raising the local price of imported fuel and food and adding to inflation, while making exports more competitive.',
        'exam_strategy': 'State the quote convention at the start of your answer ("naira per dollar"), because "the rate rose" means opposite things under the two conventions.',
        'recap': ['Exchange rate = price of a currency.', 'Depreciation: exports cheaper, imports dearer.', 'Also raises inflation and foreign-debt costs.', 'PPP is a long-run guide.']},
    T4: {
        'overview': 'The balance of payments records all transactions between a country and the rest of the world. The current account covers trade and income; the financial account covers investment and borrowing.',
        'key_terms': ['Balance of payments', 'Current account', 'Trade balance', 'Primary income', 'Secondary income (transfers)', 'Financial account', 'Remittances', 'Foreign direct investment'],
        'explanation': [
            'The current account adds the balance on goods and services (exports minus imports), primary income (wages, interest and profits flowing in and out) and secondary income (transfers such as remittances and aid). Remittances from people working abroad are a major inflow for many developing countries.',
            'The financial account records purchases and sales of assets: foreign direct investment (building factories, buying firms), portfolio investment (shares and bonds) and loans, as well as changes in the central bank\'s reserves. A current-account deficit must be financed by a net financial inflow, so the accounts balance overall (apart from errors).',
            'A current-account deficit is not automatically bad: a country borrowing to invest in productive capacity can repay later from higher output. It becomes a concern when it finances consumption, is very large, or relies on short-term flows that can reverse suddenly.'],
        'formulas_label': 'Formulas',
        'formulas': ['Current account = trade balance + primary income + secondary income', 'Trade balance = exports − imports', 'Current account + capital account + financial account ≈ 0', 'CA deficit ⇒ net financial inflow'],
        'steps': ['Sort each item into the right account.', 'Add up the current account components.', 'Find the financing in the financial account.', 'Judge sustainability: what is the deficit financing?'],
        'worked_example': {
            'problem': 'Exports are 500, imports 600, net primary income −30 and net transfers (mostly remittances) +80. Find the current-account balance.',
            'steps': ['Trade balance = 500 − 600 = −100.', 'Add primary income: −100 − 30 = −130.', 'Add transfers: −130 + 80 = −50.'],
            'answer': 'A current-account deficit of 50, which must be matched by net financial inflows of about 50.',
            'check': 'Remittances of 80 cut the deficit a lot, showing why they matter so much for many economies.'},
        'mistakes': ['Putting foreign direct investment in the current account.', 'Forgetting income and transfers and using the trade balance alone.', 'Assuming every deficit is harmful.', 'Mixing up primary and secondary income.'],
        'real_world': 'Remittances to Nigeria, Ghana, Kenya and other countries amount to billions of dollars a year, often larger than foreign direct investment, supporting household spending and the current account.',
        'exam_strategy': 'Lay out the current account as a short table with each component and its sign. Then comment on what the deficit or surplus finances.',
        'recap': ['CA = trade + income + transfers.', 'Financial account: investment and borrowing.', 'A CA deficit needs a financial inflow.', 'Judge deficits by what they finance.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'At 7% annual growth, real GDP per person doubles in about:', ['10 years', '7 years', '14 years', '70 years'], 0, '70 ÷ 7 = 10.', ans=10),
    Q(T1, 'Sustained long-run growth in output per worker mainly requires:', ['technological progress', 'more money printing', 'higher tariffs', 'lower savings'], 0, 'Capital alone faces diminishing returns.'),
    Q(T1, 'Better education and health raise growth by increasing:', ['human capital', 'the money supply', 'the exchange rate', 'import tariffs'], 0, 'Skilled, healthy workers are more productive.'),
    Q(T1, 'Catch-up (convergence) growth means poorer countries can grow faster by:', ['adopting existing technology and building scarce capital', 'reducing trade', 'raising inflation', 'cutting education'], 0, 'Returns to capital are higher where it is scarce.'),
    Q(T1, 'Which institution most supports investment and growth?', ['Secure property rights', 'High inflation', 'Frequent policy reversals', 'Corruption'], 0, 'People invest when they expect to keep the returns.'),
    Q(T1, 'Diminishing returns to capital means that:', ['each extra machine adds less output', 'output falls as capital rises', 'capital never matters', 'labour productivity falls'], 0, 'Output still rises, but by smaller amounts.'),
    # T2
    Q(T2, 'Qd = 100 − 2P, Qs = 2P − 20 and the world price is 10. Imports are:', ['80', '60', '100', '0'], 0, 'Qd = 80 and Qs = 0.', ans=80),
    Q(T2, 'A tariff of 2 raises the price to 12. Imports become:', ['72', '76', '80', '4'], 0, 'Qd = 76 and Qs = 4.', ans=72),
    Q(T2, 'The tariff revenue is:', ['144', '160', '152', '8'], 0, '2 × 72.', ans=144),
    Q(T2, 'Who usually bears most of the cost of a tariff?', ['Domestic consumers', 'Foreign governments', 'The domestic government', 'Nobody'], 0, 'They pay higher prices.'),
    Q(T2, 'The infant-industry argument for protection says:', ['new industries need temporary protection until they are competitive', 'old industries deserve permanent subsidies', 'trade always harms growth', 'tariffs lower prices'], 0, 'Protection should be temporary.'),
    Q(T2, 'Selling exports abroad below their cost of production is called:', ['dumping', 'a quota', 'a subsidy', 'devaluation'], 0, 'Countries often respond with anti-dumping duties.'),
    # T3
    Q(T3, 'A $20 good, at 1500 naira per dollar, costs:', ['30000 naira', '1520 naira', '75 naira', '3000 naira'], 0, '20 × 1500 = 30 000.'),
    Q(T3, 'The rate moves from 1500 to 1600 naira per dollar. The naira has:', ['depreciated', 'appreciated', 'not changed', 'been revalued'], 0, 'More naira are needed for each dollar.'),
    Q(T3, 'A depreciation of a country\'s currency tends to:', ['make its exports cheaper abroad', 'make its imports cheaper', 'lower inflation', 'reduce foreign-debt costs'], 0, 'Foreign buyers need less of their own currency.'),
    Q(T3, 'A burger costs 3000 naira in Lagos and $5 in New York. The implied PPP rate is:', ['600 naira per dollar', '15000 naira per dollar', '0.0017 naira per dollar', '3005 naira per dollar'], 0, '3000 ÷ 5 = 600.'),
    Q(T3, 'Higher domestic interest rates tend to make the currency:', ['appreciate', 'depreciate', 'unchanged', 'fixed'], 0, 'Foreign investors buy the currency to earn the higher return.'),
    Q(T3, 'To keep a fixed exchange rate, a central bank needs:', ['enough foreign currency reserves', 'a budget surplus', 'zero inflation', 'no imports'], 0, 'It buys or sells its currency at the fixed rate.'),
    # T4
    Q(T4, 'Exports 500, imports 600, net primary income −30 and transfers +80. The current account is:', ['−50', '−100', '−130', '50'], 0, '−100 − 30 + 80.', ans=-50),
    Q(T4, 'Remittances from citizens working abroad are recorded as:', ['secondary income in the current account', 'foreign direct investment', 'exports of goods', 'primary income'], 0, 'They are transfers, with nothing given in return.'),
    Q(T4, 'A foreign firm building a factory in Ghana is recorded in:', ['the financial account', 'the current account', 'secondary income', 'the trade balance'], 0, 'It is foreign direct investment.'),
    Q(T4, 'A current-account deficit must be matched by:', ['a net financial-account inflow', 'a trade surplus', 'higher taxes', 'lower interest rates'], 0, 'The balance of payments sums to zero overall.'),
    Q(T4, 'Interest paid on foreign debt is recorded as:', ['a primary income outflow', 'an import of goods', 'a transfer inflow', 'a financial inflow'], 0, 'Interest and profits are primary income.'),
    Q(T4, 'A current-account deficit is least worrying when it finances:', ['productive investment', 'consumer imports', 'short-term speculation', 'government wages'], 0, 'Investment raises future capacity to repay.'),
]

FLASH = [
    ['Sources of growth', 'Physical capital, human capital, technology, institutions.'],
    ['Diminishing returns to capital', 'Each extra unit of capital adds less output.'],
    ['Tariff effects', 'Higher domestic price, more domestic output, fewer imports, revenue, deadweight loss.'],
    ['Depreciation', 'Exports cheaper abroad, imports dearer at home, higher inflation risk.'],
    ['Purchasing power parity', 'Long-run exchange rate equalises the price of the same basket.'],
    ['Current account', 'Trade balance + primary income + secondary income.'],
    ['Financial account', 'FDI, portfolio investment, loans and reserve changes.'],
    ['BoP identity', 'A current-account deficit is financed by a net financial inflow.'],
]
