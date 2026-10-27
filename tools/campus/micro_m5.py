"""Principles of Microeconomics, module 5: Factor markets and market failure."""
from verify import Q, sp
T1, T2, T3, T4 = ('Labour markets and wages', 'Externalities', 'Public goods and common resources', 'Asymmetric information')
R = sp.Rational
Qv = sp.Symbol('Q')
Qs_ = sp.solve(sp.Eq(50 - Qv / 2, 16 + Qv / 2), Qv)[0]
assert Qs_ == 34 and 50 - Qs_ / 2 == 33 and sp.solve(sp.Eq(50 - Qv / 2, 10 + Qv / 2), Qv)[0] == 40 and R(1, 2) * 6 * (40 - 34) == 18
assert 15 * 4 == 60

MODULE = {
    'title': 'Factor markets and market failure',
    'topics': [T1, T2, T3, T4],
    'overview': 'Markets for labour and other inputs decide how income is shared. Markets can also fail: when costs or benefits spill onto others, when goods cannot be charged for, or when one side knows more than the other, the market outcome is not efficient. This module explains each failure and the policy tools used to fix it.',
    'key_terms': ['Marginal revenue product', 'Derived demand', 'Externality', 'Pigouvian tax', 'Public good', 'Free rider', 'Tragedy of the commons', 'Adverse selection', 'Moral hazard'],
    'explanation': [
        'The demand for labour is derived from the demand for the goods it produces. A firm hires workers up to the point where the extra revenue a worker brings in (the marginal revenue product) equals the wage.',
        'A market fails when it leaves out costs or benefits. Externalities fall on third parties; public goods cannot exclude non-payers; common resources get overused; and hidden information lets one side take advantage of the other.',
        'Policy tools target each failure: taxes and subsidies that price externalities, regulation and tradable permits, government provision of public goods, property rights or quotas for common resources, and disclosure rules, warranties and insurance design for information problems. Governments can also fail, so each intervention needs its own cost-benefit test.'],
    'quick_facts': [
        'MRP = MP × P (in competitive product markets); hire until MRP = wage.',
        'Negative externality: MSC > MPC ⇒ overproduction.',
        'Pigouvian tax = marginal external cost at the optimum.',
        'Public goods are non-rival and non-excludable.',
        'Adverse selection: before the deal; moral hazard: after it.'],
}

NOTES = {
    T1: {
        'overview': 'Wages are set in labour markets. Firms demand labour because workers produce goods that can be sold; workers supply labour by trading off income against leisure.',
        'key_terms': ['Derived demand', 'Marginal product of labour', 'Marginal revenue product', 'Labour supply', 'Wage differentials', 'Monopsony', 'Trade union'],
        'explanation': [
            'A worker\'s value to a competitive firm is the marginal revenue product MRP = MP × P: the extra output times the price it sells for. The firm hires until MRP equals the wage, so the MRP curve is the firm\'s demand curve for labour. It slopes down because of diminishing marginal returns.',
            'Labour demand shifts with the price of the product, with productivity (better machines or skills raise MP) and with the prices of other inputs. Labour supply depends on the wage, population, skills and training required, and how pleasant the job is.',
            'Wages differ because of skills and education (human capital), compensating differentials for dangerous or unpleasant work, discrimination, and market power. A monopsony (a single dominant employer) pays less and hires fewer workers than a competitive market; trade unions can push wages up but may reduce employment.'],
        'formulas_label': 'Formulas',
        'formulas': ['MP = ΔQ / ΔL', 'MRP = MP × P (competitive product market)', 'Hire while MRP ≥ wage', 'Labour demand curve = MRP curve'],
        'steps': ['Find the marginal product of each extra worker.', 'Multiply by the product price to get MRP.', 'Compare MRP with the wage.', 'Hire up to the last worker whose MRP is at least the wage.'],
        'worked_example': {
            'problem': 'A bakery sells bread at 4 per loaf. The 3rd worker adds 15 loaves a day and the 4th adds 10. The daily wage is 50. How many workers should it hire?',
            'steps': ['MRP of the 3rd worker = 15 × 4 = 60, which is above the wage of 50.', 'MRP of the 4th worker = 10 × 4 = 40, which is below 50.', 'Hire the 3rd but not the 4th.'],
            'answer': 'Hire 3 workers.',
            'check': 'If the wage fell to 40, the 4th worker would just be worth hiring, showing that labour demand slopes down.'},
        'mistakes': ['Comparing MP (in units) directly with the wage (in money).', 'Using total product instead of marginal product.', 'Thinking labour demand is independent of product demand.', 'Assuming every wage gap is caused by discrimination.'],
        'real_world': 'Software engineers earn high wages because their marginal revenue product is high: their work is sold to millions of users at almost no extra cost.',
        'exam_strategy': 'Show the MRP calculation for each worker in a small table. Comparing each MRP with the wage makes the hiring decision obvious and earns the method marks.',
        'recap': ['Labour demand is derived demand.', 'MRP = MP × P.', 'Hire until MRP = wage.', 'Wage gaps: skills, conditions, discrimination, market power.']},
    T2: {
        'overview': 'An externality is a cost or benefit that falls on people outside a transaction. Because the market ignores it, too much is produced when there are external costs and too little when there are external benefits.',
        'key_terms': ['Externality', 'Marginal private cost', 'Marginal social cost', 'Marginal external cost', 'Pigouvian tax', 'Coase theorem', 'Tradable permits'],
        'explanation': [
            'With a negative externality such as pollution, marginal social cost (MSC) = marginal private cost (MPC) + marginal external cost. The market produces where demand meets MPC, which is more than the efficient amount where demand meets MSC. The extra units cost society more than they are worth, creating a deadweight loss.',
            'With a positive externality such as vaccination or education, marginal social benefit exceeds private benefit, so the market produces too little. A subsidy equal to the external benefit can correct it.',
            'Policy options: a Pigouvian tax equal to the external cost makes producers face the full cost; regulation sets limits; tradable permits cap total pollution and let firms trade the right to pollute, so cuts happen where they are cheapest. The Coase theorem says that with clear property rights and low bargaining costs, the affected parties can negotiate the efficient outcome themselves.'],
        'formulas_label': 'Formulas',
        'formulas': ['MSC = MPC + MEC', 'MSB = MPB + MEB', 'Efficient output: MSB = MSC', 'Pigouvian tax = MEC at the efficient output', 'DWL ≈ ½ × MEC × (Q_market − Q_optimal)'],
        'steps': ['Identify whether the externality is a cost or a benefit.', 'Add the external amount to the private curve.', 'Find the market output and the social optimum.', 'Compare and compute the deadweight loss.', 'Choose a corrective tax, subsidy or regulation.'],
        'worked_example': {
            'problem': 'Demand is P = 50 − Q/2 and marginal private cost is MPC = 10 + Q/2. Each unit causes 6 of pollution damage. Find the market output, the efficient output and the deadweight loss.',
            'steps': ['Market: 50 − Q/2 = 10 + Q/2 gives Q = 40.', 'MSC = 16 + Q/2. Efficient: 50 − Q/2 = 16 + Q/2 gives Q = 34 and P = 33.', 'DWL = ½ × 6 × (40 − 34) = 18.'],
            'answer': 'The market produces 40 instead of 34; the deadweight loss is 18. A tax of 6 per unit would correct it.',
            'check': 'With a tax of 6 the firm\'s cost curve becomes MSC, so it chooses Q = 34 itself ✓.'},
        'mistakes': ['Putting the external cost on the demand side.', 'Thinking the efficient amount of pollution is zero.', 'Mixing up positive and negative externalities.', 'Using the market price instead of the external cost as the tax.'],
        'real_world': 'Carbon taxes and emissions trading schemes put a price on greenhouse gases so that firms take the climate damage into account when deciding how much to produce and which technology to use.',
        'exam_strategy': 'Draw MPC and MSC as separate supply-side curves, mark Q_market and Q_optimal, and shade the DWL triangle between them. Then name a policy and its drawback.',
        'recap': ['MSC = MPC + MEC.', 'Negative externality: too much; positive: too little.', 'Tax or subsidy equal to the external effect.', 'Permits, regulation and Coase bargaining are alternatives.']},
    T3: {
        'overview': 'Some goods cannot easily be sold in markets. Public goods are under-provided because people can use them without paying, and common resources are over-used because nobody owns them.',
        'key_terms': ['Rival', 'Excludable', 'Public good', 'Free rider', 'Common resource', 'Tragedy of the commons', 'Club good'],
        'explanation': [
            'Goods are classified by two properties. Rival: one person\'s use reduces what is left for others. Excludable: non-payers can be prevented from using it. Private goods (food) are both; public goods (street lighting, national defence) are neither; common resources (fish in the sea) are rival but not excludable; club goods (streaming services) are excludable but not rival.',
            'For public goods, everyone hopes others will pay: the free-rider problem. Private firms cannot charge enough, so the good is under-provided or not provided at all. Governments usually provide such goods and fund them through taxes.',
            'For common resources, each user ignores the cost of their use to others, so the resource is over-used and can collapse: the tragedy of the commons. Solutions include quotas, licences, property rights and community management rules.'],
        'formulas_label': 'Classification',
        'formulas': ['Private: rival and excludable', 'Public: non-rival and non-excludable', 'Common resource: rival, non-excludable', 'Club good: non-rival (up to a point), excludable'],
        'steps': ['Ask: does one person\'s use reduce what is available to others?', 'Ask: can non-payers be excluded?', 'Classify the good.', 'Identify the problem (free riding or overuse) and a fix.'],
        'worked_example': {
            'problem': 'Classify a public fishing lake and explain the likely problem.',
            'steps': ['Rival: each fish caught is not available to anyone else.', 'Non-excludable: anyone can fish without paying.', 'So it is a common resource.'],
            'answer': 'It will tend to be overfished (tragedy of the commons); fishing licences or catch limits can protect it.',
            'check': 'If entry were controlled with paid permits, it would become excludable, closer to a club good.'},
        'mistakes': ['Calling any government-provided good a public good (schools and hospitals are rival and excludable).', 'Confusing non-rival with non-excludable.', 'Forgetting that congestion can make "public" roads rival.', 'Missing the free-rider explanation.'],
        'real_world': 'Many ocean fisheries collapsed in the twentieth century from overfishing; catch quotas and protected areas have helped some stocks recover.',
        'exam_strategy': 'Classify with both properties explicitly ("non-rival because…, non-excludable because…") before naming the problem. One property alone rarely earns full marks.',
        'recap': ['Rival? Excludable?', 'Public goods: free riding, under-provision.', 'Common resources: overuse.', 'Fixes: government provision, quotas, property rights.']},
    T4: {
        'overview': 'When one side of a deal knows more than the other, markets can break down or behave badly. The two classic problems are adverse selection and moral hazard.',
        'key_terms': ['Asymmetric information', 'Adverse selection', 'Moral hazard', 'Signalling', 'Screening', 'Principal–agent problem'],
        'explanation': [
            'Adverse selection happens before a deal, because of hidden characteristics. In the used-car "market for lemons", buyers cannot tell good cars from bad, so they offer an average price. Owners of good cars then withdraw, the average quality falls, and the market can unravel. In insurance, the people most likely to claim are the most eager to buy.',
            'Moral hazard happens after a deal, because of hidden actions. Once insured, people may take less care; a manager paid a fixed salary may not work in the owner\'s interest (the principal–agent problem).',
            'Markets respond with signalling (warranties, educational qualifications, brand reputation), screening (medical checks, credit scores, deductibles), and incentive design (excess payments, performance pay). Governments add disclosure laws, compulsory insurance and regulation.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Adverse selection: hidden characteristics, before the deal', 'Moral hazard: hidden actions, after the deal', 'Signalling: the informed side reveals quality', 'Screening: the uninformed side tests for quality'],
        'steps': ['Identify who knows more.', 'Ask whether the problem arises before the deal (selection) or after it (behaviour).', 'Explain the inefficiency.', 'Suggest a signalling, screening or incentive solution.'],
        'worked_example': {
            'problem': 'A health insurer charges everyone the same premium. Explain the problem and suggest a solution.',
            'steps': ['People know their own health better than the insurer (asymmetric information).', 'At an average premium, healthy people find insurance poor value and drop out, while less healthy people stay: adverse selection.', 'Premiums must then rise, driving out more healthy people.'],
            'answer': 'Adverse selection can make the pool ever riskier. Screening (health checks), group or compulsory insurance can keep the pool balanced.',
            'check': 'If insured people then took fewer health precautions, that would be moral hazard, a separate problem after the contract.'},
        'mistakes': ['Mixing up adverse selection and moral hazard.', 'Saying the problem is simply "lack of information" without saying who lacks it.', 'Suggesting a solution that does not address the hidden information.', 'Forgetting that signals must be costly to be believable.'],
        'real_world': 'Car insurers offer lower premiums to drivers who install a tracking device, which reduces both adverse selection (careful drivers reveal themselves) and moral hazard (drivers know they are monitored).',
        'exam_strategy': 'Use the timing test in your answer ("this arises before the contract, so it is adverse selection"). It shows the examiner you understand the difference.',
        'recap': ['Asymmetric information: one side knows more.', 'Adverse selection: before; moral hazard: after.', 'Signalling and screening.', 'Incentives and regulation as fixes.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A worker adds 15 units of output, each selling for 4. Her marginal revenue product is:', ['60', '19', '15', '4'], 0, 'MRP = MP × P = 15 × 4.', ans=60),
    Q(T1, 'A competitive firm hires workers until:', ['MRP equals the wage', 'MP equals the wage', 'total product is maximised', 'average product is maximised'], 0, 'Beyond that point an extra worker costs more than she brings in.'),
    Q(T1, 'Labour demand is called derived demand because:', ['it depends on the demand for the goods workers produce', 'it is set by the government', 'workers demand jobs', 'it never changes'], 0, 'Firms want labour only for what it produces.'),
    Q(T1, 'The MRP of the 4th worker is 40 and the wage is 50. The firm should:', ['not hire the 4th worker', 'hire the 4th worker', 'hire more than 4 workers', 'raise the wage'], 0, 'She would bring in less than she costs.'),
    Q(T1, 'Higher pay for dangerous jobs is an example of:', ['a compensating differential', 'discrimination', 'monopsony', 'derived demand'], 0, 'Wages compensate for unpleasant or risky conditions.'),
    Q(T1, 'A rise in the price of the product a firm sells will:', ['shift its labour demand to the right', 'shift its labour demand to the left', 'not affect labour demand', 'reduce marginal product'], 0, 'MRP = MP × P rises.'),
    # T2
    Q(T2, 'With a negative production externality, the free market produces:', ['more than the efficient output', 'less than the efficient output', 'exactly the efficient output', 'nothing'], 0, 'Producers ignore the external cost.'),
    Q(T2, 'Demand P = 50 − Q/2, MPC = 10 + Q/2 and external cost 6 per unit. The efficient output is:', ['34', '40', '30', '36'], 0, '50 − Q/2 = 16 + Q/2.', ans=Qs_),
    Q(T2, 'In that market, the deadweight loss of the free market is:', ['18', '36', '6', '12'], 0, '½ × 6 × (40 − 34).', ans=18),
    Q(T2, 'The correcting (Pigouvian) tax in that market is:', ['6 per unit', '33 per unit', '16 per unit', '40 per unit'], 0, 'Set the tax equal to the marginal external cost.'),
    Q(T2, 'Vaccination is an example of:', ['a positive externality', 'a negative externality', 'a public good', 'moral hazard'], 0, 'Others benefit because the disease spreads less.'),
    Q(T2, 'The Coase theorem says efficient outcomes can be reached by bargaining if:', ['property rights are clear and bargaining costs are low', 'the government sets prices', 'there are many affected parties', 'information is hidden'], 0, 'Clear rights let the parties negotiate.'),
    # T3
    Q(T3, 'A public good is:', ['non-rival and non-excludable', 'rival and excludable', 'rival and non-excludable', 'provided only by firms'], 0, 'For example street lighting.'),
    Q(T3, 'Fish in the open sea are:', ['a common resource', 'a public good', 'a club good', 'a private good'], 0, 'Rival but not excludable.'),
    Q(T3, 'The free-rider problem means that public goods are:', ['under-provided by markets', 'over-provided by markets', 'always free', 'excludable'], 0, 'People can benefit without paying, so firms cannot cover their costs.'),
    Q(T3, 'A streaming subscription service is best described as:', ['a club good', 'a public good', 'a common resource', 'a merit good'], 0, 'Excludable (you must pay) but non-rival (one person watching does not stop another).'),
    Q(T3, 'The tragedy of the commons refers to:', ['overuse of a shared resource', 'under-provision of a public good', 'monopoly pricing', 'hidden information'], 0, 'Each user ignores the cost imposed on others.'),
    Q(T3, 'Which is NOT a public good, although governments often provide it?', ['Secondary schooling', 'National defence', 'A lighthouse', 'Flood defences'], 0, 'School places are rival and excludable.'),
    # T4
    Q(T4, 'Drivers take less care once fully insured. This is:', ['moral hazard', 'adverse selection', 'a public good', 'signalling'], 0, 'A hidden action after the contract.'),
    Q(T4, 'In the used-car "market for lemons", good cars leave the market because of:', ['adverse selection', 'moral hazard', 'externalities', 'economies of scale'], 0, 'Buyers cannot judge quality, so they pay only an average price.'),
    Q(T4, 'A seller offering a 3-year warranty on a used car is:', ['signalling quality', 'screening buyers', 'creating moral hazard', 'free riding'], 0, 'Only sellers of good cars can afford to offer it.'),
    Q(T4, 'An insurer requiring a medical examination is:', ['screening', 'signalling', 'moral hazard', 'collusion'], 0, 'The uninformed side tests for hidden characteristics.'),
    Q(T4, 'The principal–agent problem arises when:', ['an agent\'s actions are hidden from the person they work for', 'two firms collude', 'a good is non-excludable', 'demand is elastic'], 0, 'For example managers working for shareholders.'),
    Q(T4, 'Adverse selection differs from moral hazard because it:', ['arises from hidden characteristics before the deal', 'arises from hidden actions after the deal', 'only occurs in labour markets', 'is the same thing'], 0, 'Timing is the key difference.'),
]

FLASH = [
    ['MRP', 'MP × P; a competitive firm hires until MRP = wage.'],
    ['Derived demand', 'Demand for an input that comes from demand for the output.'],
    ['Marginal social cost', 'MSC = MPC + marginal external cost.'],
    ['Pigouvian tax', 'A tax equal to the marginal external cost.'],
    ['Public good', 'Non-rival and non-excludable; free-rider problem.'],
    ['Tragedy of the commons', 'Overuse of a rival, non-excludable resource.'],
    ['Adverse selection', 'Hidden characteristics before a deal.'],
    ['Moral hazard', 'Hidden actions after a deal.'],
]
