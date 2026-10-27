"""Principles of Microeconomics, module 3: Consumers, producers and costs."""
from verify import Q, sp
T1, T2, T3, T4 = ('Consumer and producer surplus', 'Utility and consumer choice', 'Production and short-run costs', 'Long-run costs and economies of scale')
R = sp.Rational
q = sp.Symbol('q', positive=True)
TC = 100 + 10 * q + q ** 2
MC, ATC = sp.diff(TC, q), TC / q
qmin = sp.solve(sp.diff(ATC, q), q)[0]
assert qmin == 10 and ATC.subs(q, 10) == 30 and MC.subs(q, 10) == 30 and TC.subs(q, 10) == 300 and (TC - 100).subs(q, 10) / 10 == 20
assert R(1, 2) * 40 * (50 - 30) == 400 and R(1, 2) * 40 * (30 - 10) == 400
Ls, Qs = [0, 1, 2, 3, 4], [0, 10, 25, 35, 40]
MP = [Qs[i + 1] - Qs[i] for i in range(4)]
assert MP == [10, 15, 10, 5]

MODULE = {
    'title': 'Consumers, producers and costs',
    'topics': [T1, T2, T3, T4],
    'overview': 'Behind every demand curve are consumers choosing how to spend a budget, and behind every supply curve are firms facing costs. This module measures the gains from trade with consumer and producer surplus, explains consumer choice with marginal utility, and builds the cost curves that every later model of firms uses.',
    'key_terms': ['Consumer surplus', 'Producer surplus', 'Marginal utility', 'Diminishing marginal utility', 'Marginal product', 'Fixed cost', 'Variable cost', 'Marginal cost', 'Average total cost', 'Economies of scale'],
    'explanation': [
        'Consumer surplus is the gap between what buyers would be willing to pay and what they actually pay; producer surplus is the gap between the price sellers receive and their minimum acceptable price. Their sum, total surplus, is largest at the competitive equilibrium.',
        'Consumers get less extra satisfaction from each additional unit (diminishing marginal utility). They do best when the last unit of money spent on each good gives the same extra utility. That rule explains why demand curves slope down.',
        'In the short run at least one input (such as the factory) is fixed, so adding workers eventually brings diminishing marginal returns and rising marginal cost. In the long run every input can change, and average cost depends on economies or diseconomies of scale.'],
    'quick_facts': [
        'CS = area under demand above price; PS = area above supply below price.',
        'Optimal choice: MUx/Px = MUy/Py.',
        'TC = FC + VC; ATC = TC/Q; MC = ΔTC/ΔQ.',
        'MC cuts ATC and AVC at their minimum points.',
        'Economies of scale: long-run average cost falls as output rises.'],
}

NOTES = {
    T1: {
        'overview': 'Consumer surplus and producer surplus measure the gains that buyers and sellers get from trading in a market. They are the basic tools for judging whether an outcome is efficient.',
        'key_terms': ['Willingness to pay', 'Consumer surplus', 'Producer surplus', 'Total surplus', 'Efficiency', 'Deadweight loss'],
        'explanation': [
            'Each point on the demand curve shows the most some buyer would pay for that unit. If the market price is lower, the buyer gains the difference. Adding over all units gives consumer surplus: the area below the demand curve and above the price.',
            'Each point on the supply curve shows the lowest price at which some seller would supply that unit (its marginal cost). Producer surplus is the area above the supply curve and below the price.',
            'At the competitive equilibrium total surplus is as large as possible: every unit that is worth more to a buyer than it costs to produce gets traded. Taxes, price controls and monopoly reduce the quantity traded and cause a deadweight loss, a loss of surplus that nobody gains.'],
        'formulas_label': 'Formulas (linear curves)',
        'formulas': ['CS = ½ × Q* × (demand intercept − P*)', 'PS = ½ × Q* × (P* − supply intercept)', 'Total surplus = CS + PS', 'DWL = surplus lost on units no longer traded'],
        'steps': ['Find the equilibrium P* and Q*.', 'Find where demand and supply meet the price axis.', 'Compute the two triangles.', 'For an intervention, recompute and find the lost area.'],
        'worked_example': {
            'problem': 'Qd = 100 − 2P and Qs = 2P − 20, with equilibrium P = 30 and Q = 40. Find CS and PS.',
            'steps': ['Demand meets the price axis at P = 50; supply at P = 10.', 'CS = ½ × 40 × (50 − 30) = 400.', 'PS = ½ × 40 × (30 − 10) = 400.'],
            'answer': 'CS = 400, PS = 400, and total surplus = 800.',
            'check': 'After the tax of 4 in the previous module, total surplus plus tax revenue was 800 − 8, the 8 being the deadweight loss ✓.'},
        'mistakes': ['Using the quantity intercept instead of the price intercept.', 'Forgetting the ½ for a triangle.', 'Thinking a transfer (such as tax revenue) is a deadweight loss.', 'Placing CS above the price but below supply.'],
        'real_world': 'Ride-sharing apps that adjust prices in real time try to capture more consumer surplus, charging more when willingness to pay is high, such as late at night in the rain.',
        'exam_strategy': 'Shade CS and PS in different styles on a labelled diagram and write the triangle formula with numbers. The area method earns marks even if the arithmetic slips.',
        'recap': ['CS: under demand, above price.', 'PS: above supply, below price.', 'Competitive equilibrium maximises total surplus.', 'DWL is surplus nobody receives.']},
    T2: {
        'overview': 'Utility is the satisfaction a consumer gets from goods. Because extra units add less and less satisfaction, a consumer with a limited budget does best by equalising the satisfaction per unit of money across goods.',
        'key_terms': ['Utility', 'Total utility', 'Marginal utility', 'Diminishing marginal utility', 'Budget constraint', 'Equi-marginal principle'],
        'explanation': [
            'Marginal utility (MU) is the extra utility from one more unit. It typically falls as you consume more: the first slice of pizza is worth more to you than the fifth. This is the law of diminishing marginal utility.',
            'With a budget, the consumer should buy the good that gives the most extra utility per unit of money, MU/P. Spending is optimal when MUx/Px = MUy/Py: shifting money from one good to the other could not raise total utility.',
            'If the price of X falls, MUx/Px rises, so the consumer buys more X until the ratios are equal again. That is the law of demand, derived from the behaviour of individual consumers. The budget line itself shows every affordable combination: Px·x + Py·y = income.'],
        'formulas_label': 'Formulas',
        'formulas': ['MU = ΔTU / ΔQ', 'Optimum: MUx/Px = MUy/Py', 'Budget line: Px·x + Py·y = M', 'Slope of the budget line = −Px/Py'],
        'steps': ['Compute MU/P for each good.', 'Buy more of the good with the higher MU/P.', 'Continue until the ratios are equal or the budget is used up.', 'Check the budget constraint.'],
        'worked_example': {
            'problem': 'Px = 2 and Py = 4. At the current choice, MUx = 10 and MUy = 24. Should the consumer change anything?',
            'steps': ['MUx/Px = 10/2 = 5 utils per unit of money.', 'MUy/Py = 24/4 = 6 utils per unit of money.', 'Y gives more satisfaction per unit of money.'],
            'answer': 'Spend a little less on X and more on Y until the two ratios are equal.',
            'check': 'As more Y is bought, MUy falls and MUx rises, so the ratios move towards each other ✓.'},
        'mistakes': ['Comparing MUx with MUy without dividing by price.', 'Confusing total utility with marginal utility.', 'Thinking diminishing MU means total utility falls.', 'Ignoring the budget constraint.'],
        'real_world': 'All-you-can-eat buffets are profitable because diminishing marginal utility sets in fast: after a few plates, the next one is worth little to the customer.',
        'exam_strategy': 'Show the two ratios as numbers with units ("5 utils per unit of money") and say which way spending should move. A bare "buy more Y" scores less.',
        'recap': ['MU falls as consumption rises.', 'Compare MU/P, not MU alone.', 'Optimum: MUx/Px = MUy/Py.', 'This explains why demand slopes down.']},
    T3: {
        'overview': 'In the short run a firm has some fixed inputs. Adding variable inputs such as labour eventually gives diminishing marginal returns, which shapes the firm\'s cost curves.',
        'key_terms': ['Short run', 'Total product', 'Marginal product', 'Diminishing marginal returns', 'Fixed cost', 'Variable cost', 'Average total cost', 'Marginal cost'],
        'explanation': [
            'Marginal product (MP) is the extra output from one more worker. At first MP may rise as workers specialise, but with a fixed factory each extra worker eventually adds less: this is the law of diminishing marginal returns.',
            'Total cost TC = fixed cost (FC, paid even at zero output) + variable cost (VC). Averages divide by output: AFC = FC/Q falls continuously, AVC = VC/Q, and ATC = TC/Q. Marginal cost MC = ΔTC/ΔQ is the cost of one more unit.',
            'Because of diminishing returns, MC eventually rises. When MC is below ATC it pulls the average down; when it is above, it pulls the average up. So MC cuts AVC and ATC at their lowest points. For TC = 100 + 10Q + Q², MC = 10 + 2Q and ATC is lowest at Q = 10, where ATC = MC = 30.'],
        'formulas_label': 'Formulas',
        'formulas': ['MP = ΔQ / ΔL', 'TC = FC + VC', 'AFC = FC/Q, AVC = VC/Q, ATC = TC/Q', 'MC = ΔTC/ΔQ (or d(TC)/dQ)', 'MC = ATC at minimum ATC'],
        'steps': ['Separate fixed from variable costs.', 'Compute the averages by dividing by Q.', 'Compute MC from changes in TC.', 'Locate minimum ATC where MC = ATC.'],
        'worked_example': {
            'problem': 'A firm has TC = 100 + 10Q + Q². Find FC, and ATC, AVC and MC at Q = 10.',
            'steps': ['FC = 100 (the part that does not depend on Q).', 'At Q = 10: TC = 100 + 100 + 100 = 300, so ATC = 30 and AVC = 200/10 = 20.', 'MC = 10 + 2Q = 30.'],
            'answer': 'FC = 100; at Q = 10, ATC = 30, AVC = 20 and MC = 30.',
            'check': 'MC = ATC at Q = 10, so this is the minimum of ATC ✓ (ATC is about 30.11 at Q = 9 and 30.09 at Q = 11, both above 30).'},
        'mistakes': ['Counting fixed cost in marginal cost (it never changes MC).', 'Thinking diminishing returns means output falls.', 'Drawing MC cutting ATC away from its minimum.', 'Confusing AFC with FC.'],
        'real_world': 'A small restaurant with a fixed kitchen can add cooks up to a point; after that, extra cooks get in each other\'s way and output per extra cook falls, a direct example of diminishing returns.',
        'exam_strategy': 'Draw MC through the bottom of both the AVC and ATC curves. Examiners check this crossing point on every cost diagram.',
        'recap': ['Short run: some inputs are fixed.', 'Diminishing marginal returns raise MC.', 'TC = FC + VC; averages divide by Q.', 'MC cuts ATC and AVC at their minimums.']},
    T4: {
        'overview': 'In the long run every input can change. Long-run average cost shows how cost per unit depends on the scale of the firm, through economies and diseconomies of scale.',
        'key_terms': ['Long run', 'Long-run average cost (LRAC)', 'Economies of scale', 'Diseconomies of scale', 'Minimum efficient scale', 'Returns to scale'],
        'explanation': [
            'Economies of scale make LRAC fall as output grows: specialisation of labour, bulk buying of inputs, cheaper finance for large firms, and spreading large fixed costs (research, equipment) over more units.',
            'Diseconomies of scale make LRAC rise at very large sizes, mostly because of management problems: communication becomes slower, coordination harder and workers less motivated.',
            'The minimum efficient scale (MES) is the smallest output at which LRAC reaches its lowest level. If MES is large relative to the market, only a few firms can survive (as in car making or aircraft); if it is small, many firms compete (as in hairdressing).'],
        'formulas_label': 'Key ideas',
        'formulas': ['Economies of scale: LRAC falls as Q rises', 'Diseconomies of scale: LRAC rises as Q rises', 'Constant returns: LRAC flat', 'MES: lowest output at minimum LRAC'],
        'steps': ['Decide whether all inputs can change (long run).', 'Identify the source of falling or rising average cost.', 'Locate the minimum efficient scale.', 'Relate MES to market size to predict market structure.'],
        'worked_example': {
            'problem': 'Doubling a firm\'s inputs raises output from 1000 to 2400 units, while total cost doubles from 50 000 to 100 000. What is happening to average cost?',
            'steps': ['Average cost before: 50 000 / 1000 = 50 per unit.', 'After: 100 000 / 2400 ≈ 41.7 per unit.', 'Output more than doubled when inputs doubled.'],
            'answer': 'Average cost falls from 50 to about 41.7: the firm enjoys economies of scale (increasing returns to scale).',
            'check': 'If output had exactly doubled, average cost would have stayed at 50 (constant returns).'},
        'mistakes': ['Confusing diminishing returns (short run, one fixed input) with diseconomies of scale (long run).', 'Thinking bigger is always cheaper.', 'Mixing up internal economies (inside the firm) with external economies (the whole industry).', 'Forgetting that MES depends on technology, not just on demand.'],
        'real_world': 'Online platforms have huge economies of scale: once the software is built, serving one more user costs almost nothing, which is one reason why a few large tech firms dominate.',
        'exam_strategy': 'Give a named source of economies of scale with a real example (bulk buying, technical, financial, managerial). Lists without explanation earn few marks.',
        'recap': ['Long run: all inputs variable.', 'Economies of scale lower LRAC.', 'Diseconomies raise LRAC at large sizes.', 'MES shapes market structure.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Qd = 100 − 2P and Qs = 2P − 20, with P* = 30 and Q* = 40. Consumer surplus is:', ['400', '800', '200', '600'], 0, '½ × 40 × (50 − 30) = 400.', ans=400),
    Q(T1, 'In the same market, producer surplus is:', ['400', '800', '200', '300'], 0, '½ × 40 × (30 − 10) = 400.', ans=400),
    Q(T1, 'Consumer surplus is the area:', ['below demand and above the price', 'above supply and below the price', 'below supply and above the price', 'under the whole demand curve'], 0, 'It is willingness to pay minus the price actually paid.'),
    Q(T1, 'A buyer would pay up to 80 for a ticket that costs 50. Her consumer surplus on it is:', ['30', '80', '50', '130'], 0, '80 − 50 = 30.', ans=30),
    Q(T1, 'Total surplus is maximised:', ['at the competitive equilibrium', 'when price is highest', 'when quantity is largest possible', 'when there is a tax'], 0, 'Every unit worth more than its cost is traded, and no others.'),
    Q(T1, 'A deadweight loss is:', ['surplus lost that nobody gains', 'tax revenue', 'a transfer from buyers to sellers', 'the cost of production'], 0, 'It is the loss of mutually beneficial trades that no longer happen.'),
    # T2
    Q(T2, 'Px = 2, Py = 4, MUx = 10 and MUy = 24. The consumer should:', ['buy more Y and less X', 'buy more X and less Y', 'not change', 'stop buying Y'], 0, 'MUy/Py = 6 > MUx/Px = 5.'),
    Q(T2, 'Diminishing marginal utility means:', ['each extra unit adds less satisfaction', 'total utility falls', 'the price falls', 'utility becomes negative immediately'], 0, 'Total utility still rises, just by smaller amounts.'),
    Q(T2, 'The consumer optimum condition is:', ['MUx/Px = MUy/Py', 'MUx = MUy', 'Px = Py', 'TUx = TUy'], 0, 'Equal extra satisfaction per unit of money spent.'),
    Q(T2, 'Total utility from 1, 2 and 3 cups of tea is 10, 18 and 24. The marginal utility of the 3rd cup is:', ['6', '24', '8', '18'], 0, '24 − 18 = 6.', ans=24 - 18),
    Q(T2, 'Income is 100, Px = 5 and Py = 10. The most X the consumer can buy is:', ['20', '10', '15', '50'], 0, '100 / 5 = 20 when nothing is spent on Y.', ans=20),
    Q(T2, 'If Px falls, MUx/Px rises, so the consumer buys more X. This explains:', ['the downward slope of demand', 'the upward slope of supply', 'diminishing returns', 'economies of scale'], 0, 'Lower price leads to a higher quantity demanded.'),
    # T3
    Q(T3, 'Output with 0 to 4 workers is 0, 10, 25, 35, 40. The marginal product of the 3rd worker is:', ['10', '35', '15', '5'], 0, '35 − 25 = 10.', ans=MP[2]),
    Q(T3, 'In that data, diminishing marginal returns begin with the:', ['3rd worker', '2nd worker', '1st worker', '4th worker'], 0, 'MP rises from 10 to 15, then falls to 10 for the 3rd worker.'),
    Q(T3, 'TC = 100 + 10Q + Q². Fixed cost is:', ['100', '110', '10', '0'], 0, 'The part of cost that does not depend on Q.', ans=100),
    Q(T3, 'TC = 100 + 10Q + Q². At Q = 10, ATC is:', ['30', '20', '300', '10'], 0, 'TC = 300, and 300/10 = 30.', ans=ATC.subs(q, 10)),
    Q(T3, 'TC = 100 + 10Q + Q². At what output is ATC lowest?', ['10', '5', '20', '100'], 0, 'MC = 10 + 2Q equals ATC = 100/Q + 10 + Q when Q² = 100.', ans=qmin),
    Q(T3, 'Marginal cost cuts average total cost:', ['at the minimum of ATC', 'at the maximum of ATC', 'where ATC is rising fastest', 'never'], 0, 'Below the average, MC pulls it down; above, it pulls it up.'),
    # T4
    Q(T4, 'Economies of scale mean that as a firm grows:', ['long-run average cost falls', 'marginal product falls', 'fixed costs disappear', 'prices must rise'], 0, 'Cost per unit falls with scale.'),
    Q(T4, 'Which is a source of diseconomies of scale?', ['Coordination and communication problems', 'Bulk buying of inputs', 'Specialisation of workers', 'Cheaper borrowing'], 0, 'Large organisations become harder to manage.'),
    Q(T4, 'Doubling inputs raises output from 1000 to 2400 and cost from 50 000 to 100 000. Average cost falls to about:', ['41.7', '50', '25', '83.3'], 0, '100 000 / 2400 ≈ 41.7.'),
    Q(T4, 'Diminishing marginal returns differ from diseconomies of scale because:', ['they occur in the short run with a fixed input', 'they occur only in the long run', 'they mean output falls', 'they are the same thing'], 0, 'Diseconomies of scale apply when all inputs can change.'),
    Q(T4, 'If the minimum efficient scale is large relative to market demand, the market tends to have:', ['few firms', 'many small firms', 'no firms', 'perfect competition'], 0, 'Only a few firms can produce at the low-cost scale.'),
    Q(T4, 'Constant returns to scale mean that doubling all inputs:', ['exactly doubles output', 'more than doubles output', 'less than doubles output', 'leaves output unchanged'], 0, 'Long-run average cost stays flat.'),
]

FLASH = [
    ['Consumer surplus', 'Area below demand and above the price.'],
    ['Producer surplus', 'Area above supply and below the price.'],
    ['Diminishing marginal utility', 'Each extra unit adds less satisfaction.'],
    ['Consumer optimum', 'MUx/Px = MUy/Py.'],
    ['Diminishing marginal returns', 'With a fixed input, extra workers eventually add less output.'],
    ['Cost identities', 'TC = FC + VC; ATC = TC/Q; MC = ΔTC/ΔQ.'],
    ['MC and ATC', 'MC cuts ATC at its minimum.'],
    ['Economies of scale', 'Long-run average cost falls as output rises.'],
]
