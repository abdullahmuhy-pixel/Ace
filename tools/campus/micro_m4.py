"""Principles of Microeconomics, module 4: Market structures."""
from verify import Q, sp
T1, T2, T3, T4 = ('Perfect competition', 'Monopoly', 'Monopolistic competition', 'Oligopoly and game theory')
R = sp.Rational
q = sp.Symbol('q', positive=True)
TC = 100 + 10 * q + q ** 2
q40 = sp.solve(sp.Eq(40, sp.diff(TC, q)), q)[0]
assert q40 == 15 and 40 * 15 - TC.subs(q, 15) == 125
assert sp.solve(sp.Eq(30, sp.diff(TC, q)), q)[0] == 10 and 30 * 10 - TC.subs(q, 10) == 0
Qm = sp.solve(sp.Eq(sp.diff((100 - 2 * q) * q, q), 20), q)[0]
Pm = 100 - 2 * Qm
assert sp.diff((100 - 2 * q) * q, q) == 100 - 4 * q
assert (Qm, Pm, (Pm - 20) * Qm) == (20, 60, 800) and R(1, 2) * (60 - 20) * (40 - 20) == 400

MODULE = {
    'title': 'Market structures',
    'topics': [T1, T2, T3, T4],
    'overview': 'How a firm sets price and output depends on how much competition it faces. This module runs from perfect competition (many small price-takers) through monopolistic competition and oligopoly to monopoly (one seller), and compares the outcomes for prices, profits and efficiency.',
    'key_terms': ['Price taker', 'Marginal revenue', 'Profit maximisation', 'Shutdown point', 'Barriers to entry', 'Market power', 'Product differentiation', 'Oligopoly', 'Nash equilibrium', 'Prisoners\' dilemma'],
    'explanation': [
        'Every profit-maximising firm produces where marginal revenue equals marginal cost (MR = MC). What differs between structures is the shape of demand facing the firm, and so the relationship between price and MR.',
        'A perfectly competitive firm is a price taker: P = MR, so it produces where P = MC, and in the long run entry and exit drive profit to zero. A monopolist faces the whole downward-sloping market demand, so MR < P, and it restricts output to keep the price above MC.',
        'Between these extremes, monopolistic competition has many firms selling differentiated products, and oligopoly has a few interdependent firms whose best choices depend on what rivals do. Game theory is the tool for analysing that interdependence.'],
    'quick_facts': [
        'Profit maximum: MR = MC.',
        'Perfect competition: P = MR = MC; long-run P = minimum ATC.',
        'Shut down in the short run if P < minimum AVC.',
        'Monopoly: MR < P; for linear demand P = a − bQ, MR = a − 2bQ.',
        'Nash equilibrium: no player gains by changing strategy alone.'],
}

NOTES = {
    T1: {
        'overview': 'In perfect competition, many firms sell an identical product and none can affect the market price. Each firm takes the price as given and chooses output where price equals marginal cost.',
        'key_terms': ['Price taker', 'Homogeneous product', 'Free entry and exit', 'P = MC', 'Normal profit', 'Shutdown point', 'Break-even point'],
        'explanation': [
            'The assumptions are many buyers and sellers, identical products, perfect information, and free entry and exit. Each firm faces a horizontal demand curve at the market price, so selling one more unit adds exactly P to revenue: MR = P.',
            'The firm maximises profit where P = MC. Profit per unit is P − ATC. In the short run it keeps producing even at a loss as long as P covers AVC, because the fixed costs must be paid anyway. Below minimum AVC it shuts down. The firm\'s supply curve is its MC curve above minimum AVC.',
            'In the long run, profits attract new firms, raising market supply and lowering the price; losses cause exit. This continues until P = minimum ATC and firms earn normal profit (zero economic profit). The outcome is both allocatively efficient (P = MC) and productively efficient (lowest ATC).'],
        'formulas_label': 'Rules',
        'formulas': ['MR = P', 'Profit maximum: P = MC', 'Profit = (P − ATC) × Q', 'Shut down if P < min AVC', 'Long run: P = min ATC, zero economic profit'],
        'steps': ['Set P = MC and solve for Q.', 'Compute TR = P × Q and TC at that Q.', 'Profit = TR − TC.', 'Check P against minimum AVC for shutdown.', 'Predict entry or exit in the long run.'],
        'worked_example': {
            'problem': 'A competitive firm has TC = 100 + 10Q + Q² (MC = 10 + 2Q). The market price is 40. Find its output and profit, and say what happens in the long run.',
            'steps': ['P = MC: 40 = 10 + 2Q, so Q = 15.', 'TR = 40 × 15 = 600 and TC = 100 + 150 + 225 = 475.', 'Profit = 600 − 475 = 125 > 0.'],
            'answer': 'Q = 15 and profit = 125. Profits attract entry, so the price falls towards minimum ATC = 30, where profit is zero.',
            'check': 'At P = 30, P = MC gives Q = 10 and TR = TC = 300, so profit is exactly zero ✓.'},
        'mistakes': ['Setting P = ATC instead of P = MC to choose output.', 'Shutting down whenever there is a loss (only if P < AVC).', 'Thinking competitive firms earn zero accounting profit (zero economic profit still covers the opportunity cost).', 'Drawing a downward-sloping demand curve for the individual firm.'],
        'real_world': 'Markets for farm produce such as maize or tomatoes are close to perfect competition: each farmer is too small to influence the price and must accept what the market pays.',
        'exam_strategy': 'Draw the firm and the market side by side, with the price set in the market and carried across to the firm as a horizontal line. That pairing is what examiners look for.',
        'recap': ['Price taker: MR = P.', 'Produce where P = MC.', 'Short run: stay open if P ≥ AVC.', 'Long run: P = min ATC, zero economic profit.']},
    T2: {
        'overview': 'A monopoly is the only seller of a good with no close substitutes, protected by barriers to entry. It chooses output where MR = MC and charges the highest price buyers will pay for that quantity.',
        'key_terms': ['Monopoly', 'Barriers to entry', 'Marginal revenue', 'Market power', 'Deadweight loss', 'Natural monopoly', 'Price discrimination'],
        'explanation': [
            'Barriers to entry keep rivals out: legal ones (patents, licences), control of a key resource, economies of scale so large that one firm can supply the whole market most cheaply (natural monopoly), and network effects.',
            'Because the monopolist faces the downward-sloping market demand, it must cut the price on all units to sell one more, so MR < P. For linear demand P = a − bQ, MR = a − 2bQ. It produces where MR = MC, then reads the price off the demand curve.',
            'Compared with a competitive market with the same costs, a monopoly produces less and charges more. Its profit can persist in the long run because entry is blocked, and the lost trades create a deadweight loss. Governments respond with competition law, regulation of prices (common for natural monopolies such as water and electricity grids), or public ownership.'],
        'formulas_label': 'Formulas',
        'formulas': ['Demand P = a − bQ ⇒ MR = a − 2bQ', 'Profit maximum: MR = MC', 'Price from the demand curve at that Q', 'Profit = (P − ATC) × Q', 'DWL = ½ × (Pm − MC) × (Qc − Qm) for constant MC'],
        'steps': ['Write MR from the demand curve.', 'Set MR = MC and solve for Q.', 'Substitute Q into demand to get P.', 'Compute profit.', 'Compare with the competitive outcome P = MC.'],
        'worked_example': {
            'problem': 'A monopolist faces P = 100 − 2Q with constant MC = 20 and no fixed costs. Find its output, price, profit and the deadweight loss.',
            'steps': ['MR = 100 − 4Q. Set MR = MC: 100 − 4Q = 20, so Q = 20 and P = 100 − 40 = 60.', 'Profit = (60 − 20) × 20 = 800.', 'Competitive outcome: P = MC = 20 gives Q = 40. DWL = ½ × (60 − 20) × (40 − 20) = 400.'],
            'answer': 'Q = 20, P = 60, profit 800, deadweight loss 400.',
            'check': 'The monopoly sells half the competitive quantity at a price three times the marginal cost, so a large DWL is expected.'},
        'mistakes': ['Setting P = MC for a monopolist.', 'Reading the price off the MR curve instead of the demand curve.', 'Writing MR with the same slope as demand.', 'Assuming monopolies always make profits (they can make losses if demand is weak).'],
        'real_world': 'Pharmaceutical patents give temporary monopolies, which is why new medicines are expensive until the patent expires and generic versions enter at much lower prices.',
        'exam_strategy': 'On the diagram, show MR below demand with twice the slope, mark Q where MR = MC, go up to demand for P, and shade the profit rectangle and the DWL triangle.',
        'recap': ['Barriers to entry protect the monopoly.', 'MR < P; MR = MC sets Q.', 'Price comes from the demand curve.', 'Less output, higher price, DWL.']},
    T3: {
        'overview': 'Monopolistic competition has many firms selling similar but differentiated products, such as restaurants or clothing brands. Each has a little market power, but free entry removes long-run profit.',
        'key_terms': ['Product differentiation', 'Brand', 'Advertising', 'Excess capacity', 'Free entry', 'Non-price competition'],
        'explanation': [
            'Because each firm\'s product is slightly different, it faces a downward-sloping demand curve and sets output where MR = MC, like a small monopoly. Firms compete through product quality, location, branding and advertising as well as price.',
            'In the short run a firm can make profits. These attract new firms with similar products, which take customers and shift each firm\'s demand curve left until it just touches the ATC curve. In the long run P = ATC and economic profit is zero.',
            'The long-run outcome is not fully efficient: price is above MC, and output is below the level that minimises ATC (excess capacity). The benefit is variety: consumers value having many different products to choose from.'],
        'formulas_label': 'Rules',
        'formulas': ['Short run: MR = MC, P > MC', 'Long run: P = ATC (zero economic profit)', 'Long run: P > MC and output below minimum ATC (excess capacity)', 'Free entry and exit'],
        'steps': ['Identify differentiated products and free entry.', 'Short run: MR = MC, profit possible.', 'Entry shifts each firm\'s demand left.', 'Long run: demand tangent to ATC, zero profit.'],
        'worked_example': {
            'problem': 'A new coffee shop in a busy street earns large profits. Predict what happens over the next few years.',
            'steps': ['Profits attract new coffee shops (free entry).', 'Customers spread across more shops, so each shop\'s demand falls and becomes more elastic.', 'Entry continues until profits are normal.'],
            'answer': 'Each shop ends up earning only normal profit, with prices above marginal cost and some unused capacity (empty tables at quiet times).',
            'check': 'This matches the long-run tangency P = ATC, with P > MC.'},
        'mistakes': ['Confusing monopolistic competition with monopoly (here entry is free).', 'Saying long-run profit is positive.', 'Forgetting excess capacity.', 'Ignoring non-price competition.'],
        'real_world': 'Hair salons, bakeries and clothing brands are classic cases: many sellers, each with loyal customers, but anyone can open a rival shop.',
        'exam_strategy': 'Draw the long-run diagram with demand just touching ATC at the profit-maximising output, to the left of the minimum of ATC. Label the excess capacity.',
        'recap': ['Many firms, differentiated products.', 'Short-run profit; long-run zero profit.', 'P > MC; excess capacity.', 'Benefit: variety.']},
    T4: {
        'overview': 'In an oligopoly a few large firms dominate, and each firm\'s best decision depends on what its rivals do. Game theory studies these strategic decisions.',
        'key_terms': ['Oligopoly', 'Interdependence', 'Collusion', 'Cartel', 'Game theory', 'Dominant strategy', 'Nash equilibrium', 'Prisoners\' dilemma'],
        'explanation': [
            'Oligopolies arise where barriers to entry let only a few firms operate, as in mobile networks, airlines and cement. Firms are interdependent: a price cut by one affects the others\' sales, so each must predict its rivals\' reactions.',
            'A game has players, strategies and payoffs. A dominant strategy is best whatever the other player does. A Nash equilibrium is a pair of strategies where neither player can gain by changing on their own.',
            'The prisoners\' dilemma explains why collusion is unstable. Two firms jointly earn most by both charging high prices, but each gains by secretly undercutting the other, so both end up charging low prices. Cartels (formal collusion) are illegal in most countries, and repeated interaction, trust and punishment strategies can sometimes sustain cooperation anyway.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Dominant strategy: best response to every rival strategy', 'Nash equilibrium: no profitable one-sided change', 'Prisoners\' dilemma: individual incentives lead to a worse joint outcome', 'Collusion raises joint profit but is unstable and usually illegal'],
        'steps': ['Write the payoff matrix.', 'For each rival strategy, find each player\'s best response.', 'Look for dominant strategies.', 'Identify the Nash equilibrium.', 'Compare it with the jointly best outcome.'],
        'worked_example': {
            'problem': 'Two airlines choose a High or Low fare. Profits (A, B): both High (50, 50); A High, B Low (10, 70); A Low, B High (70, 10); both Low (30, 30). Find the Nash equilibrium.',
            'steps': ['If B is High, A earns 70 from Low and 50 from High: choose Low.', 'If B is Low, A earns 30 from Low and 10 from High: choose Low. So Low is dominant for A.', 'By symmetry, Low is dominant for B too.'],
            'answer': 'The Nash equilibrium is (Low, Low) with profits (30, 30), although (High, High) would give both 50.',
            'check': 'This is a prisoners\' dilemma: each firm\'s self-interest leaves both worse off.'},
        'mistakes': ['Confusing the Nash equilibrium with the best joint outcome.', 'Reading the wrong payoff in each cell (the first number usually belongs to the row player).', 'Assuming every game has a dominant strategy.', 'Thinking collusion is stable without enforcement.'],
        'real_world': 'Competition authorities regularly fine cartels, in industries from cement to banking, that were caught fixing prices; their leniency programmes exploit the prisoners\' dilemma by rewarding the first member to confess.',
        'exam_strategy': 'Underline each player\'s best response in the payoff matrix. The cell where both are underlined is the Nash equilibrium, and the working is easy for the marker to follow.',
        'recap': ['Few interdependent firms.', 'Dominant strategy and Nash equilibrium.', 'Prisoners\' dilemma explains unstable collusion.', 'Cartels are usually illegal.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A perfectly competitive firm has MC = 10 + 2Q and the price is 40. Its profit-maximising output is:', ['15', '20', '10', '25'], 0, 'P = MC: 40 = 10 + 2Q.', ans=q40),
    Q(T1, 'With TC = 100 + 10Q + Q², price 40 and output 15, profit is:', ['125', '600', '475', '0'], 0, 'TR 600 − TC 475 = 125.', ans=125),
    Q(T1, 'For a perfectly competitive firm, marginal revenue equals:', ['the price', 'zero', 'average cost', 'twice the price'], 0, 'Each extra unit sells at the market price.'),
    Q(T1, 'In the short run a competitive firm should shut down if:', ['P < minimum AVC', 'P < minimum ATC', 'it makes any loss', 'MC is rising'], 0, 'If it cannot cover variable costs, producing adds to its losses.'),
    Q(T1, 'In long-run competitive equilibrium:', ['P = minimum ATC and economic profit is zero', 'firms earn large profits', 'P > MC', 'there are barriers to entry'], 0, 'Entry and exit remove profits and losses.'),
    Q(T1, 'With TC = 100 + 10Q + Q², the long-run competitive price is:', ['30', '40', '10', '20'], 0, 'Minimum ATC is 30, at Q = 10.', ans=30),
    # T2
    Q(T2, 'Demand is P = 100 − 2Q. Marginal revenue is:', ['100 − 4Q', '100 − 2Q', '100 − Q', '50 − Q'], 0, 'TR = 100Q − 2Q², so MR = 100 − 4Q.'),
    Q(T2, 'With P = 100 − 2Q and MC = 20, the monopoly output is:', ['20', '40', '30', '10'], 0, '100 − 4Q = 20.', ans=Qm),
    Q(T2, 'In that market, the monopoly price is:', ['60', '20', '80', '40'], 0, 'P = 100 − 2(20) = 60.', ans=Pm),
    Q(T2, 'In that market, the deadweight loss of monopoly is:', ['400', '800', '200', '1600'], 0, '½ × (60 − 20) × (40 − 20).', ans=400),
    Q(T2, 'Which is a barrier to entry?', ['A patent', 'Many small competitors', 'Identical products', 'Perfect information'], 0, 'A patent legally blocks rivals from making the product.'),
    Q(T2, 'A natural monopoly arises when:', ['economies of scale let one firm supply the market most cheaply', 'the government owns the firm', 'demand is very elastic', 'there are many substitutes'], 0, 'For example water pipes or power grids.'),
    # T3
    Q(T3, 'Monopolistic competition is characterised by:', ['many firms with differentiated products and free entry', 'one firm and high barriers', 'a few interdependent firms', 'identical products and price takers'], 0, 'Think restaurants or clothing brands.'),
    Q(T3, 'In the long run, a firm in monopolistic competition earns:', ['zero economic profit', 'large profits', 'losses', 'monopoly profits'], 0, 'Entry continues until demand is tangent to ATC.'),
    Q(T3, 'Excess capacity in monopolistic competition means:', ['output is below the level that minimises ATC', 'firms produce too much', 'firms run at full capacity', 'prices equal marginal cost'], 0, 'The tangency point is on the falling part of ATC.'),
    Q(T3, 'Which is non-price competition?', ['Advertising and branding', 'Cutting prices', 'Selling at marginal cost', 'Fixing prices with rivals'], 0, 'Firms try to make their product seem different and better.'),
    Q(T3, 'In long-run monopolistic competition, price compared with marginal cost is:', ['higher', 'equal', 'lower', 'zero'], 0, 'Each firm still faces a downward-sloping demand curve.'),
    Q(T3, 'A key benefit of monopolistic competition for consumers is:', ['product variety', 'the lowest possible prices', 'no advertising', 'identical products'], 0, 'The cost of slightly higher prices buys more choice.'),
    # T4
    Q(T4, 'Payoffs (A, B): HH (50, 50), HL (10, 70), LH (70, 10), LL (30, 30). The Nash equilibrium is:', ['Low, Low', 'High, High', 'High, Low', 'Low, High'], 0, 'Low is a dominant strategy for both firms.'),
    Q(T4, 'In that game, A\'s dominant strategy is:', ['Low', 'High', 'none', 'to copy B'], 0, 'Low beats High whatever B chooses (70 > 50, 30 > 10).'),
    Q(T4, 'A Nash equilibrium is a situation where:', ['no player can gain by changing strategy alone', 'joint profit is maximised', 'every player gets the same payoff', 'one firm leaves the market'], 0, 'Each strategy is a best response to the others.'),
    Q(T4, 'Why is collusion in a cartel often unstable?', ['Each member gains by secretly cheating', 'Cartels always lower prices', 'Members have identical costs', 'Demand is perfectly elastic'], 0, 'It is a prisoners\' dilemma.'),
    Q(T4, 'An oligopoly is a market with:', ['a few large interdependent firms', 'one firm', 'many small firms', 'no barriers to entry'], 0, 'Each firm must consider rivals\' reactions.'),
    Q(T4, 'In the airline game, joint profit is highest at:', ['High, High', 'Low, Low', 'High, Low', 'Low, High'], 0, '50 + 50 = 100 is the largest total.'),
]

FLASH = [
    ['Profit maximisation', 'Produce where MR = MC.'],
    ['Price taker', 'Perfectly competitive firm: MR = P.'],
    ['Shutdown rule', 'Short run: shut down if P < minimum AVC.'],
    ['Long-run perfect competition', 'P = minimum ATC; zero economic profit.'],
    ['Monopoly MR', 'For P = a − bQ, MR = a − 2bQ.'],
    ['Natural monopoly', 'Economies of scale let one firm supply the market most cheaply.'],
    ['Monopolistic competition (long run)', 'Zero profit, P > MC, excess capacity.'],
    ['Nash equilibrium', 'No player gains by changing strategy alone.'],
]
