"""Principles of Macroeconomics, module 2: Aggregate demand and aggregate supply."""
from verify import Q, sp
T1, T2, T3, T4 = ('Consumption, saving and the multiplier', 'Aggregate demand', 'Aggregate supply', 'Macroeconomic equilibrium and shocks')
R = sp.Rational
Y = sp.Symbol('Y')
Ye = sp.solve(sp.Eq(Y, 50 + R(8, 10) * Y + 100), Y)[0]
assert Ye == 750 and 1 / (1 - R(8, 10)) == 5 and 5 * 20 == 100
assert 1 / (R(1, 10) + R(2, 10) + R(2, 10)) == 2 and 1 / (1 - R(3, 4)) == 4

MODULE = {
    'title': 'Aggregate demand and aggregate supply',
    'topics': [T1, T2, T3, T4],
    'overview': 'The AD–AS model is the macroeconomic version of demand and supply. It explains why output and the price level rise and fall together in booms and recessions, and why some shocks (such as an oil price spike) bring both inflation and falling output. The multiplier shows why changes in spending have a bigger effect on GDP than the initial change.',
    'key_terms': ['Marginal propensity to consume', 'Multiplier', 'Aggregate demand', 'Aggregate supply', 'Short-run aggregate supply', 'Long-run aggregate supply', 'Output gap', 'Stagflation'],
    'explanation': [
        'Household spending depends mainly on income. Out of each extra unit of income, a fraction (the marginal propensity to consume, MPC) is spent and the rest saved. Spending by one person is income for another, so an initial injection of spending is multiplied as it passes round the economy.',
        'Aggregate demand (AD) is total planned spending, C + I + G + (X − M), at each price level. Short-run aggregate supply (SRAS) slopes upward because some costs, especially wages, are slow to adjust. Long-run aggregate supply (LRAS) is vertical at the economy\'s potential output, set by its resources and technology.',
        'Shifts in AD move output and prices in the same direction (demand shocks). Shifts in SRAS move them in opposite directions (supply shocks). The gap between actual and potential output tells policymakers whether the economy is overheating or has spare capacity.'],
    'quick_facts': [
        'MPC + MPS = 1.',
        'Simple multiplier = 1/(1 − MPC) = 1/MPS.',
        'With taxes and imports: multiplier = 1/(MPS + MPT + MPM).',
        'AD = C + I + G + (X − M).',
        'LRAS is vertical at potential output.'],
}

NOTES = {
    T1: {
        'overview': 'The consumption function links household spending to income. Because spending becomes someone else\'s income, a change in spending has a multiplied effect on total output.',
        'key_terms': ['Consumption function', 'Autonomous consumption', 'MPC', 'MPS', 'Injections', 'Leakages', 'Multiplier'],
        'explanation': [
            'A simple consumption function is C = a + bY, where a is autonomous consumption (spending even at zero income, financed by savings or borrowing) and b is the MPC. Saving is the rest of income: MPS = 1 − MPC.',
            'In a simple economy with investment I, equilibrium output solves Y = C + I. With C = 50 + 0.8Y and I = 100: Y = 150 + 0.8Y, so 0.2Y = 150 and Y = 750.',
            'If investment rises by 20, the first round adds 20 to incomes; households spend 0.8 × 20 = 16, which adds another 16, then 12.8, and so on. The total is 20 × 1/(1 − 0.8) = 100. In a real economy taxes and imports are also leakages, so the multiplier is 1/(MPS + MPT + MPM), which is much smaller.'],
        'formulas_label': 'Formulas',
        'formulas': ['C = a + bY, with b = MPC', 'MPC + MPS = 1', 'Equilibrium: Y = C + I (+ G + X − M)', 'Simple multiplier k = 1/(1 − MPC)', 'Open economy: k = 1/(MPS + MPT + MPM)', 'ΔY = k × ΔInjection'],
        'steps': ['Write total spending as a function of Y.', 'Set Y equal to total spending and solve.', 'Compute the multiplier from the leakages.', 'Multiply the change in injections by k.'],
        'worked_example': {
            'problem': 'C = 50 + 0.8Y and I = 100. Find equilibrium output, then the effect of investment rising by 20.',
            'steps': ['Y = 50 + 0.8Y + 100, so 0.2Y = 150 and Y = 750.', 'Multiplier k = 1/(1 − 0.8) = 5.', 'ΔY = 5 × 20 = 100, so the new output is 850.'],
            'answer': 'Y = 750, rising to 850 after the extra investment.',
            'check': 'Solving directly with I = 120: 0.2Y = 170 gives Y = 850 ✓.'},
        'mistakes': ['Using 1/MPC instead of 1/(1 − MPC).', 'Forgetting taxes and imports as leakages in a real economy.', 'Thinking the multiplier works instantly.', 'Confusing a movement along the consumption function with a shift in it.'],
        'real_world': 'Governments use multiplier estimates to judge stimulus packages. Because much spending in small open economies leaks into imports, their multipliers are usually well below those of large economies.',
        'exam_strategy': 'Show the multiplier formula with the numbers substituted, then the multiplied change. If you use the open-economy version, list each leakage separately.',
        'recap': ['MPC + MPS = 1.', 'Equilibrium: Y = planned spending.', 'k = 1/(1 − MPC) in the simple model.', 'More leakages, smaller multiplier.']},
    T2: {
        'overview': 'Aggregate demand is total planned spending on domestic output at each price level. It slopes downward and shifts when any component of spending changes for reasons other than the price level.',
        'key_terms': ['Aggregate demand', 'Wealth effect', 'Interest-rate effect', 'Exchange-rate effect', 'Shift of AD', 'Fiscal and monetary policy'],
        'explanation': [
            'AD slopes down for three reasons. A lower price level raises the real value of wealth (wealth effect), lowers interest rates and so encourages borrowing (interest-rate effect), and makes domestic goods cheaper relative to foreign ones (exchange-rate effect on net exports).',
            'AD shifts right when any part of C + I + G + (X − M) rises at every price level: higher consumer confidence, lower income taxes, lower interest rates, more business optimism, higher government spending, a weaker currency or faster growth abroad.',
            'Fiscal policy (government spending and taxes) and monetary policy (interest rates and the money supply) both work mainly by shifting AD. The size of the shift in output depends on the multiplier.'],
        'formulas_label': 'Key ideas',
        'formulas': ['AD = C + I + G + (X − M)', 'Price level ↓ ⇒ quantity of real output demanded ↑ (movement along AD)', 'AD shifts with changes in C, I, G, X or M', 'ΔY ≈ multiplier × initial change in spending'],
        'steps': ['Identify which component of spending changes.', 'Decide whether AD shifts right or left.', 'Remember the multiplier enlarges the shift.', 'Check that a price-level change is a movement, not a shift.'],
        'worked_example': {
            'problem': 'A major trading partner enters recession, and at the same time the domestic currency depreciates. What happens to AD?',
            'steps': ['The partner\'s recession reduces demand for our exports: AD shifts left.', 'Depreciation makes our exports cheaper and imports dearer: net exports rise, AD shifts right.', 'The two effects work in opposite directions.'],
            'answer': 'The net effect on AD is ambiguous; it depends on which effect is larger.',
            'check': 'Both effects work through net exports (X − M), so the answer hinges on how much export volumes change.'},
        'mistakes': ['Shifting AD when only the price level changed.', 'Mixing AD with the demand curve for one good.', 'Forgetting that higher interest rates reduce C and I.', 'Thinking a stronger currency raises net exports.'],
        'real_world': 'During the COVID-19 lockdowns consumption and investment collapsed together, a large leftward shift of AD that governments countered with record spending and interest-rate cuts.',
        'exam_strategy': 'Name the AD component that changes and the mechanism ("lower interest rates reduce the cost of borrowing, so investment rises, shifting AD right"). The chain of reasoning is what earns the marks.',
        'recap': ['AD = C + I + G + (X − M).', 'Downward slope: wealth, interest-rate, exchange-rate effects.', 'Shifts come from changes in spending components.', 'Policy works mainly through AD.']},
    T3: {
        'overview': 'Aggregate supply shows the total output firms produce at each price level. In the short run it slopes upward; in the long run it is vertical at potential output.',
        'key_terms': ['Short-run aggregate supply', 'Long-run aggregate supply', 'Potential output', 'Sticky wages', 'Supply shock', 'Productive capacity'],
        'explanation': [
            'In the short run, many costs (especially wages set by contracts) are fixed. A higher price level then raises firms\' profits per unit, so they produce more: SRAS slopes upward.',
            'In the long run wages and other costs adjust to the price level, so output returns to potential output, the level the economy can sustain with full employment of its resources. LRAS is therefore vertical at potential output and does not depend on the price level.',
            'SRAS shifts left with higher costs (oil, wages, taxes on production) and right with lower costs or productivity gains. LRAS shifts right with more or better resources: a larger labour force, more capital, better education and new technology. Supply-side policies aim to shift LRAS right.'],
        'formulas_label': 'Key ideas',
        'formulas': ['SRAS slopes up (sticky costs)', 'LRAS vertical at potential output', 'SRAS shifts with production costs', 'LRAS shifts with resources, technology and productivity'],
        'steps': ['Decide whether the change affects costs (SRAS) or capacity (LRAS), or both.', 'Shift the right curve in the right direction.', 'Find the new equilibrium.', 'Describe the effect on output and the price level.'],
        'worked_example': {
            'problem': 'A government invests heavily in education and broadband internet. Show the long-run effect.',
            'steps': ['Better skills and infrastructure raise the economy\'s productive capacity.', 'LRAS shifts right (and SRAS with it as costs per unit fall).', 'Potential output rises.'],
            'answer': 'Higher potential output and, other things equal, downward pressure on the price level.',
            'check': 'This is long-run growth, distinct from a short-run demand boom, which would raise prices without raising capacity.'},
        'mistakes': ['Drawing LRAS sloping upward.', 'Shifting SRAS because the price level changed.', 'Treating a rise in demand as a rise in potential output.', 'Forgetting that a single cost shock can shift SRAS without moving LRAS.'],
        'real_world': 'Investments in electricity supply raise potential output in many African economies, because unreliable power is one of the biggest constraints on how much firms can produce.',
        'exam_strategy': 'Say clearly whether you are discussing the short run or the long run. The same event can raise output in the short run but leave it unchanged in the long run.',
        'recap': ['SRAS slopes up because costs are sticky.', 'LRAS is vertical at potential output.', 'Costs shift SRAS; capacity shifts LRAS.', 'Supply-side policy targets LRAS.']},
    T4: {
        'overview': 'The economy settles where AD meets SRAS. Comparing that point with potential output shows whether there is a recessionary or inflationary gap, and how the economy adjusts after a shock.',
        'key_terms': ['Macroeconomic equilibrium', 'Recessionary gap', 'Inflationary gap', 'Demand shock', 'Supply shock', 'Stagflation', 'Self-correction'],
        'explanation': [
            'Short-run equilibrium is where AD crosses SRAS. If this output is below potential, there is a recessionary (negative output) gap with high unemployment; if above, an inflationary (positive) gap with rising prices and labour shortages.',
            'A demand shock moves output and prices in the same direction: a fall in AD lowers both. A supply shock moves them in opposite directions: an oil price spike shifts SRAS left, raising prices while lowering output. This combination is called stagflation and is hard for policymakers, because fighting inflation deepens the recession.',
            'Without policy, the economy tends to self-correct as wages adjust: in a recessionary gap falling wage pressure eventually shifts SRAS right. This can be slow and painful, which is the case for using fiscal and monetary policy to shift AD back towards potential output.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Short-run equilibrium: AD = SRAS', 'Recessionary gap: Y < Y potential', 'Inflationary gap: Y > Y potential', 'Demand shock: P and Y move together', 'Supply shock: P and Y move in opposite directions'],
        'steps': ['Identify the shock and which curve shifts.', 'Find the new short-run equilibrium.', 'Compare with potential output.', 'Describe the self-correction or the policy response.'],
        'worked_example': {
            'problem': 'Starting at potential output, world oil prices double. Describe the short-run effects and the policy dilemma.',
            'steps': ['Higher energy costs shift SRAS left.', 'The price level rises and real output falls below potential: stagflation.', 'Stimulating AD would close the output gap but add to inflation; tightening would curb inflation but deepen the recession.'],
            'answer': 'Higher inflation and lower output at the same time, with no policy that fixes both quickly.',
            'check': 'Output and prices moved in opposite directions, the signature of a supply shock ✓.'},
        'mistakes': ['Calling any recession a supply shock.', 'Forgetting that a recessionary gap means unemployment above the natural rate.', 'Assuming self-correction is fast.', 'Shifting LRAS for a temporary cost shock.'],
        'real_world': 'The oil crises of the 1970s caused stagflation across many economies, and the 2022 energy price surge after the invasion of Ukraine produced a milder version.',
        'exam_strategy': 'Draw LRAS as well as AD and SRAS on every equilibrium diagram, so the gap between actual and potential output is visible.',
        'recap': ['Equilibrium where AD meets SRAS.', 'Recessionary vs inflationary gap.', 'Demand shocks: P and Y together; supply shocks: opposite.', 'Stagflation is the policy dilemma.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'MPC = 0.8. The simple multiplier is:', ['5', '1.25', '0.2', '8'], 0, '1/(1 − 0.8) = 5.', ans=5),
    Q(T1, 'C = 50 + 0.8Y and I = 100. Equilibrium output is:', ['750', '150', '600', '1000'], 0, '0.2Y = 150.', ans=Ye),
    Q(T1, 'With a multiplier of 5, investment rising by 20 raises output by:', ['100', '20', '25', '4'], 0, '5 × 20.', ans=100),
    Q(T1, 'If MPC = 0.75, the MPS is:', ['0.25', '0.75', '1.33', '4'], 0, 'MPC + MPS = 1.', ans=R(1, 4)),
    Q(T1, 'MPS = 0.1, MPT = 0.2 and MPM = 0.2. The open-economy multiplier is:', ['2', '10', '5', '0.5'], 0, '1/(0.1 + 0.2 + 0.2) = 2.', ans=2),
    Q(T1, 'Which is a leakage from the circular flow?', ['Imports', 'Government spending', 'Exports', 'Investment'], 0, 'Spending on imports leaves the domestic economy.'),
    # T2
    Q(T2, 'A fall in the price level, other things equal, causes:', ['a movement down along AD', 'AD to shift right', 'AD to shift left', 'LRAS to shift'], 0, 'The quantity of real output demanded rises along the curve.'),
    Q(T2, 'Which shifts AD to the right?', ['A cut in income tax', 'A rise in interest rates', 'A stronger domestic currency', 'A fall in consumer confidence'], 0, 'Higher disposable income raises consumption.'),
    Q(T2, 'A rise in interest rates tends to:', ['reduce consumption and investment', 'raise investment', 'raise exports', 'shift LRAS right'], 0, 'Borrowing becomes more expensive.'),
    Q(T2, 'A depreciation of the domestic currency tends to:', ['raise net exports and shift AD right', 'lower exports', 'shift AD left', 'have no effect on AD'], 0, 'Exports become cheaper abroad and imports dearer.'),
    Q(T2, 'Government spending rises by 10 with a multiplier of 4. AD shifts right by about:', ['40', '10', '14', '2.5'], 0, '4 × 10.', ans=40),
    Q(T2, 'The AD curve slopes down partly because a lower price level:', ['raises the real value of wealth', 'raises interest rates', 'makes exports dearer', 'reduces real money balances'], 0, 'The wealth (real balance) effect.'),
    # T3
    Q(T3, 'In the long run, aggregate supply is:', ['vertical at potential output', 'horizontal', 'upward sloping', 'downward sloping'], 0, 'Long-run output depends on resources and technology, not on prices.'),
    Q(T3, 'SRAS slopes upward mainly because:', ['some costs, such as wages, are slow to adjust', 'consumers are richer', 'interest rates fall', 'imports rise'], 0, 'Sticky costs make higher prices more profitable in the short run.'),
    Q(T3, 'A rise in world oil prices shifts:', ['SRAS to the left', 'SRAS to the right', 'AD to the right', 'LRAS to the right'], 0, 'Production costs rise.'),
    Q(T3, 'Which shifts LRAS to the right?', ['Improved education and skills', 'Lower interest rates', 'Higher government transfers', 'A rise in the price level'], 0, 'It raises productive capacity.'),
    Q(T3, 'Supply-side policies aim to:', ['increase potential output', 'raise aggregate demand only', 'raise the price level', 'reduce exports'], 0, 'They shift LRAS right.'),
    Q(T3, 'Potential output is the level of output:', ['sustainable with full employment of resources', 'at which inflation is zero', 'at the peak of a boom', 'set by the government'], 0, 'The economy\'s long-run capacity.'),
    # T4
    Q(T4, 'An oil price shock that raises prices and lowers output is called:', ['stagflation', 'deflation', 'a demand-pull boom', 'a liquidity trap'], 0, 'Stagnation plus inflation.'),
    Q(T4, 'A fall in AD in the short run causes:', ['lower output and a lower price level', 'higher output and higher prices', 'lower output and higher prices', 'no change in output'], 0, 'Demand shocks move P and Y together.'),
    Q(T4, 'Output is below potential. The economy has:', ['a recessionary gap', 'an inflationary gap', 'stagflation', 'full employment'], 0, 'Unemployment is above its natural rate.'),
    Q(T4, 'A supply shock differs from a demand shock because:', ['prices and output move in opposite directions', 'prices and output move together', 'only prices change', 'only output changes'], 0, 'SRAS shifts along a downward-sloping AD curve.'),
    Q(T4, 'Without policy, a recessionary gap tends to close as:', ['wages and costs fall, shifting SRAS right', 'AD shifts further left', 'LRAS shifts left', 'prices rise'], 0, 'Self-correction works through the labour market, often slowly.'),
    Q(T4, 'An inflationary gap is best closed by:', ['reducing AD', 'raising AD', 'shifting LRAS left', 'cutting interest rates'], 0, 'Output is above potential, so demand should be cooled.'),
]

FLASH = [
    ['MPC + MPS', '= 1.'],
    ['Simple multiplier', '1/(1 − MPC) = 1/MPS.'],
    ['Open-economy multiplier', '1/(MPS + MPT + MPM).'],
    ['Aggregate demand', 'C + I + G + (X − M) at each price level.'],
    ['SRAS slope', 'Upward, because wages and costs are sticky.'],
    ['LRAS', 'Vertical at potential output.'],
    ['Stagflation', 'Rising prices with falling output, usually from a supply shock.'],
    ['Recessionary gap', 'Output below potential; unemployment above the natural rate.'],
]
