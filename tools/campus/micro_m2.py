"""Principles of Microeconomics, module 2: Elasticity and government intervention."""
from verify import Q, sp
T1, T2, T3, T4 = ('Price elasticity of demand', 'Income, cross-price and supply elasticity', 'Price ceilings and price floors', 'Taxes, subsidies and their incidence')
R = sp.Rational
P = sp.Symbol('P')
ped = (R(80 - 100, 90)) / (R(12 - 10, 11))
assert ped == R(-11, 9) and round(float(ped), 2) == -1.22
Pt = sp.solve(sp.Eq(100 - 2 * P, 2 * (P - 4) - 20), P)[0]
Qt = 100 - 2 * Pt
assert (Pt, Qt, Pt - 4, 4 * Qt) == (32, 36, 28, 144) and R(1, 2) * 4 * (40 - Qt) == 8
assert (100 - 2 * 25, 2 * 25 - 20) == (50, 30) and (100 - 2 * 35, 2 * 35 - 20) == (30, 50)

MODULE = {
    'title': 'Elasticity and government intervention',
    'topics': [T1, T2, T3, T4],
    'overview': 'Knowing that demand slopes down is not enough: firms and governments need to know by how much quantity responds. Elasticity measures that responsiveness, and it decides what happens to revenue when prices change and who really pays a tax. This module also covers price controls and taxes, the most common ways governments change market outcomes.',
    'key_terms': ['Price elasticity of demand', 'Elastic', 'Inelastic', 'Total revenue', 'Income elasticity', 'Cross-price elasticity', 'Price ceiling', 'Price floor', 'Tax incidence', 'Deadweight loss'],
    'explanation': [
        'An elasticity is a ratio of percentage changes, so it has no units and can compare goods with very different prices. Demand is elastic if |PED| > 1 (quantity responds more than proportionally) and inelastic if |PED| < 1.',
        'Elasticity explains revenue. When demand is inelastic, raising the price raises total revenue; when it is elastic, raising the price lowers it. That is why firms selling necessities can raise prices more easily than firms with many competitors.',
        'Price ceilings set below equilibrium create shortages, and price floors set above equilibrium create surpluses. A tax raises the price buyers pay and lowers the price sellers keep, and the side with the less elastic curve bears more of the burden. Each of these interventions shrinks the quantity traded and creates a deadweight loss.'],
    'quick_facts': [
        'PED = %ΔQd ÷ %ΔP; elastic if |PED| > 1.',
        'Inelastic demand: price up ⇒ revenue up.',
        'YED > 0 normal, < 0 inferior, > 1 luxury.',
        'XED > 0 substitutes, < 0 complements.',
        'The less elastic side bears more of a tax.'],
}

NOTES = {
    T1: {
        'overview': 'Price elasticity of demand (PED) measures how strongly quantity demanded responds to a change in price. It decides whether a price rise raises or lowers total revenue.',
        'key_terms': ['PED', 'Elastic', 'Inelastic', 'Unit elastic', 'Midpoint method', 'Total revenue'],
        'explanation': [
            'PED = (% change in quantity demanded) ÷ (% change in price). It is negative because of the law of demand, so we usually compare its absolute value with 1. The midpoint (arc) method divides each change by the average of the old and new values, so the answer is the same whether the price rises or falls.',
            'Demand is more elastic when there are close substitutes, when the good is a large share of income, when it is a luxury rather than a necessity, when the market is narrowly defined (one brand rather than all food), and over a longer time period.',
            'Total revenue TR = P × Q. If |PED| > 1, a price cut raises revenue because quantity rises by a larger percentage. If |PED| < 1, a price rise raises revenue. At |PED| = 1, revenue is at its maximum.'],
        'formulas_label': 'Formulas',
        'formulas': ['PED = %ΔQd / %ΔP', 'Midpoint: %ΔQ = ΔQ / average Q, %ΔP = ΔP / average P', '|PED| > 1 elastic; < 1 inelastic; = 1 unit elastic', 'TR = P × Q'],
        'steps': ['Compute the percentage change in quantity.', 'Compute the percentage change in price.', 'Divide, keeping the sign.', 'Compare |PED| with 1.', 'Predict the effect on total revenue.'],
        'worked_example': {
            'problem': 'The price of a concert ticket rises from 10 to 12 and sales fall from 100 to 80. Find the PED by the midpoint method and the effect on revenue.',
            'steps': ['%ΔQ = −20 / 90 ≈ −22.2%.', '%ΔP = 2 / 11 ≈ 18.2%.', 'PED = −22.2 / 18.2 ≈ −1.22, so demand is elastic.', 'Revenue: 10 × 100 = 1000 before and 12 × 80 = 960 after.'],
            'answer': 'PED ≈ −1.22 (elastic), and revenue falls from 1000 to 960.',
            'check': 'Elastic demand means a price rise lowers revenue, which matches the numbers.'},
        'mistakes': ['Dividing %ΔP by %ΔQ.', 'Calling demand elastic when PED = −0.8 because the number is negative.', 'Confusing the slope of the demand curve with its elasticity (elasticity changes along a straight line).', 'Forgetting to use percentages.'],
        'real_world': 'Governments tax cigarettes, fuel and alcohol heavily partly because demand for them is inelastic: the tax raises a lot of revenue without cutting sales by much.',
        'exam_strategy': 'Always interpret the number: "PED = −0.4, so demand is price-inelastic: a 10% price rise reduces quantity demanded by only 4% and raises revenue."',
        'recap': ['PED = %ΔQd / %ΔP.', 'Elastic if |PED| > 1.', 'Substitutes and time make demand more elastic.', 'Inelastic: price up raises revenue.']},
    T2: {
        'overview': 'Other elasticities measure responses to income, to the prices of related goods, and of supply to price. Their signs classify goods and tell firms how markets will react.',
        'key_terms': ['Income elasticity (YED)', 'Cross-price elasticity (XED)', 'Price elasticity of supply (PES)', 'Luxury', 'Necessity', 'Substitute', 'Complement'],
        'explanation': [
            'YED = %ΔQd ÷ %Δincome. Normal goods have YED > 0: necessities between 0 and 1, luxuries above 1. Inferior goods have YED < 0. As economies grow, spending shifts towards high-YED goods such as travel and services.',
            'XED = %ΔQd of good A ÷ %ΔP of good B. A positive XED means substitutes (B dearer, demand for A rises); a negative XED means complements; close to zero means the goods are unrelated. Competition authorities use XED to decide which products are in the same market.',
            'PES = %ΔQs ÷ %ΔP. Supply is more elastic when firms have spare capacity, can store stock, can switch inputs easily, and over longer periods. In the very short run, supply of goods such as fresh fish or concert seats is almost perfectly inelastic.'],
        'formulas_label': 'Formulas',
        'formulas': ['YED = %ΔQd / %ΔIncome', 'XED = %ΔQd(A) / %ΔP(B)', 'PES = %ΔQs / %ΔP', 'YED > 1 luxury; 0–1 necessity; < 0 inferior', 'XED > 0 substitutes; < 0 complements'],
        'steps': ['Identify which elasticity the question needs.', 'Put the response on top and the cause underneath.', 'Compute and keep the sign.', 'Classify the good or the relationship.'],
        'worked_example': {
            'problem': 'When average income rises 10%, demand for restaurant meals rises 15% and demand for bread rises 2%. Classify both goods.',
            'steps': ['Restaurant meals: YED = 15 / 10 = 1.5.', 'Bread: YED = 2 / 10 = 0.2.', 'Both are positive, so both are normal goods.'],
            'answer': 'Restaurant meals are a luxury (YED > 1); bread is a necessity (0 < YED < 1).',
            'check': 'It is plausible that spending on eating out grows faster than income while spending on bread barely changes.'},
        'mistakes': ['Putting the cause on top.', 'Ignoring the sign of XED or YED, which carries the classification.', 'Confusing a necessity (YED between 0 and 1) with an inferior good (YED < 0).', 'Assuming supply is equally elastic in the short and long run.'],
        'real_world': 'Supermarkets stock more own-brand basics in recessions because those goods have low or negative income elasticity, while sales of luxuries fall fastest.',
        'exam_strategy': 'State the formula with the labels in words before substituting numbers, then classify with the sign and the size. The classification is often worth more than the calculation.',
        'recap': ['YED: normal, inferior, luxury.', 'XED: substitutes or complements.', 'PES rises with time and spare capacity.', 'The sign matters.']},
    T3: {
        'overview': 'Governments sometimes fix prices by law. A maximum price (ceiling) below equilibrium causes shortages; a minimum price (floor) above equilibrium causes surpluses.',
        'key_terms': ['Price ceiling', 'Price floor', 'Binding', 'Shortage', 'Surplus', 'Black market', 'Minimum wage'],
        'explanation': [
            'A price ceiling only has an effect (it is binding) if it is set below the equilibrium price. Then quantity demanded exceeds quantity supplied, and the gap is a shortage. Rationing happens by queues, waiting lists or favouritism, and illegal resale (black markets) often appears.',
            'A price floor is binding only if it is set above equilibrium. Quantity supplied then exceeds quantity demanded, creating a surplus. With agricultural price floors, governments often have to buy and store the surplus; with a minimum wage, the surplus of labour is unemployment.',
            'Both controls reduce the quantity actually traded to the smaller of Qd and Qs, creating a deadweight loss. They can still be chosen for fairness reasons, for example rent controls to protect tenants, but the side effects need to be weighed.'],
        'formulas_label': 'Rules',
        'formulas': ['Binding ceiling: P_max < P*', 'Shortage = Qd − Qs at the ceiling', 'Binding floor: P_min > P*', 'Surplus = Qs − Qd at the floor', 'Quantity traded = min(Qd, Qs)'],
        'steps': ['Find the market equilibrium.', 'Check whether the control is binding.', 'Compute Qd and Qs at the controlled price.', 'Find the shortage or surplus and the quantity traded.'],
        'worked_example': {
            'problem': 'Qd = 100 − 2P and Qs = 2P − 20 (equilibrium P = 30). A rent ceiling of 25 is imposed. Find the effect.',
            'steps': ['25 < 30, so the ceiling is binding.', 'Qd = 100 − 50 = 50 and Qs = 50 − 20 = 30.', 'Shortage = 50 − 30 = 20; only 30 units are rented.'],
            'answer': 'A shortage of 20 units, and the quantity traded falls from 40 to 30.',
            'check': 'A floor of 35 instead would give Qd = 30 and Qs = 50, a surplus of 20, mirroring the ceiling case.'},
        'mistakes': ['Saying a ceiling above equilibrium causes a shortage (it has no effect).', 'Confusing ceilings with floors.', 'Taking the quantity traded as Qd when Qs is smaller.', 'Ignoring black markets and non-price rationing.'],
        'real_world': 'Many cities with strict rent controls have long waiting lists for housing, while minimum prices for crops in some countries have led to large government-held stockpiles.',
        'exam_strategy': 'On the diagram, draw the control as a horizontal line, mark Qd and Qs where it crosses each curve, and bracket the shortage or surplus. A labelled gap is usually a mark on its own.',
        'recap': ['Ceiling below equilibrium: shortage.', 'Floor above equilibrium: surplus.', 'Non-binding controls do nothing.', 'Quantity traded falls; deadweight loss appears.']},
    T4: {
        'overview': 'A tax drives a wedge between the price buyers pay and the price sellers receive. Who really bears the tax (its incidence) depends on elasticities, not on who hands the money to the government.',
        'key_terms': ['Specific (per-unit) tax', 'Ad valorem tax', 'Tax incidence', 'Tax revenue', 'Deadweight loss', 'Subsidy'],
        'explanation': [
            'A per-unit tax t on sellers shifts the supply curve up by t. The new equilibrium has a higher price for buyers (Pb) and a lower price kept by sellers (Ps = Pb − t). Tax revenue is t × the new quantity.',
            'The burden falls more on whichever side is less elastic, because that side cannot easily escape by changing how much it buys or sells. If demand is perfectly inelastic, buyers pay the whole tax. The legal incidence (who pays the tax office) does not matter: a tax on buyers gives exactly the same outcome.',
            'The deadweight loss is the lost surplus on units that are no longer traded, roughly ½ × t × (fall in quantity). A subsidy works in reverse: it lowers the buyer price, raises the seller price, increases quantity and costs the government s × the new quantity.'],
        'formulas_label': 'Formulas',
        'formulas': ['Ps = Pb − t', 'Tax revenue = t × Q_after', 'Buyer burden = Pb − P*; seller burden = P* − Ps', 'DWL ≈ ½ × t × (Q* − Q_after)', 'Subsidy cost = s × Q_after'],
        'steps': ['Shift supply: replace P with P − t in the supply equation.', 'Solve for the new buyer price and quantity.', 'Find the seller price Ps = Pb − t.', 'Compute revenue, the burden shares and the DWL.'],
        'worked_example': {
            'problem': 'Qd = 100 − 2P and Qs = 2P − 20 (equilibrium P = 30, Q = 40). A tax of 4 per unit is placed on sellers. Find the new prices, the revenue and the deadweight loss.',
            'steps': ['New supply: Qs = 2(P − 4) − 20 = 2P − 28.', '100 − 2P = 2P − 28 gives P = 32 and Q = 36. Sellers keep 32 − 4 = 28.', 'Revenue = 4 × 36 = 144. DWL = ½ × 4 × (40 − 36) = 8.'],
            'answer': 'Buyers pay 32 (up 2), sellers keep 28 (down 2), revenue 144, deadweight loss 8.',
            'check': 'The curves have equal and opposite slopes, so the burden splits equally, 2 and 2 ✓.'},
        'mistakes': ['Assuming the side that legally pays the tax bears all of it.', 'Computing revenue with the old quantity.', 'Shifting supply down instead of up for a tax.', 'Forgetting the deadweight loss.'],
        'real_world': 'Because demand for fuel is inelastic in the short run, most of a fuel tax increase is passed on to motorists at the pump.',
        'exam_strategy': 'Mark Pb, Ps, the tax wedge, the revenue rectangle and the deadweight-loss triangle on one diagram. Then state who bears more and why, citing elasticity.',
        'recap': ['Tax wedge: Pb − Ps = t.', 'The less elastic side pays more.', 'Revenue = t × new Q.', 'DWL ≈ ½ × t × ΔQ.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Price rises from 10 to 12 and quantity falls from 100 to 80. What is the midpoint PED, to 2 d.p.?', ['−1.22', '−0.82', '−1.00', '−2.00'], 0, '(−20/90) ÷ (2/11) = −11/9 ≈ −1.22.', ans=ped, num=True),
    Q(T1, 'A 10% price rise reduces quantity demanded by 5%. Demand is:', ['inelastic', 'elastic', 'unit elastic', 'perfectly elastic'], 0, 'PED = −5/10 = −0.5, and |−0.5| < 1.'),
    Q(T1, 'Demand is price-inelastic. A price rise will:', ['increase total revenue', 'decrease total revenue', 'leave total revenue unchanged', 'make demand elastic'], 0, 'Quantity falls proportionally less than the price rises.'),
    Q(T1, 'Which good is likely to have the most elastic demand?', ['One brand of bottled water', 'Insulin', 'Salt', 'Electricity'], 0, 'Many close substitutes make demand very elastic.'),
    Q(T1, 'PED = −2. If price falls by 5%, quantity demanded:', ['rises by 10%', 'falls by 10%', 'rises by 2.5%', 'rises by 5%'], 0, '%ΔQ = PED × %ΔP = −2 × −5% = +10%.'),
    Q(T1, 'Along a straight-line demand curve, elasticity:', ['changes from point to point', 'is the same everywhere', 'equals the slope', 'is always 1'], 0, 'The slope is constant but the ratio P/Q changes.'),
    # T2
    Q(T2, 'Income rises 10% and demand for a good rises 15%. The good is:', ['a luxury', 'a necessity', 'inferior', 'a complement'], 0, 'YED = 15/10 = 1.5 > 1.'),
    Q(T2, 'YED = −0.4. The good is:', ['inferior', 'a luxury', 'a necessity', 'a substitute'], 0, 'Negative income elasticity means an inferior good.'),
    Q(T2, 'The price of good B rises 20% and demand for good A rises 10%. XED is:', ['0.5', '2', '−0.5', '−2'], 0, '10/20 = 0.5, so A and B are substitutes.', ans=R(1, 2)),
    Q(T2, 'A negative cross-price elasticity means the goods are:', ['complements', 'substitutes', 'unrelated', 'inferior'], 0, 'A price rise in one reduces demand for the other.'),
    Q(T2, 'Price rises 5% and quantity supplied rises 10%. PES is:', ['2', '0.5', '−2', '15'], 0, '10/5 = 2, so supply is elastic.', ans=2),
    Q(T2, 'Supply is usually more elastic:', ['in the long run than the short run', 'when there is no spare capacity', 'for perishable goods that cannot be stored', 'when inputs are hard to obtain'], 0, 'Over time firms can expand capacity and enter the market.'),
    # T3
    Q(T3, 'Qd = 100 − 2P, Qs = 2P − 20. A ceiling of 25 creates a shortage of:', ['20', '10', '30', '50'], 0, 'Qd = 50 and Qs = 30.', ans=50 - 30),
    Q(T3, 'In the same market, a floor of 35 creates a surplus of:', ['20', '10', '30', '50'], 0, 'Qd = 30 and Qs = 50.', ans=50 - 30),
    Q(T3, 'A price ceiling set above the equilibrium price:', ['has no effect', 'causes a shortage', 'causes a surplus', 'raises the price'], 0, 'It is not binding: the market price is already below it.'),
    Q(T3, 'With a binding price ceiling, the quantity actually traded equals:', ['quantity supplied at the ceiling', 'quantity demanded at the ceiling', 'the equilibrium quantity', 'zero'], 0, 'Sellers will only sell Qs, which is the smaller amount.'),
    Q(T3, 'A minimum wage set above the market wage tends to cause:', ['a surplus of labour (unemployment)', 'a shortage of labour', 'no change in employment', 'lower wages'], 0, 'A binding price floor in the labour market.'),
    Q(T3, 'Which is a common side effect of a binding price ceiling?', ['A black market', 'Unsold surplus stock', 'Higher legal prices', 'More firms entering'], 0, 'Buyers who cannot get the good may pay more illegally.'),
    # T4
    Q(T4, 'Qd = 100 − 2P, Qs = 2P − 20, and a tax of 4 per unit is placed on sellers. The new price buyers pay is:', ['32', '34', '30', '28'], 0, '100 − 2P = 2(P − 4) − 20 gives P = 32.', ans=Pt),
    Q(T4, 'In that case, the price sellers keep is:', ['28', '32', '30', '26'], 0, '32 − 4 = 28.', ans=Pt - 4),
    Q(T4, 'The tax revenue is:', ['144', '160', '128', '8'], 0, '4 × 36 = 144.', ans=4 * Qt),
    Q(T4, 'The deadweight loss of the tax is:', ['8', '16', '4', '144'], 0, '½ × 4 × (40 − 36) = 8.', ans=8),
    Q(T4, 'Demand is perfectly inelastic. A per-unit tax on sellers is borne:', ['entirely by buyers', 'entirely by sellers', 'equally', 'by the government'], 0, 'Buyers buy the same quantity whatever the price, so the whole tax passes to them.'),
    Q(T4, 'Placing the same per-unit tax on buyers instead of sellers would:', ['give the same prices and quantity', 'make buyers bear all of it', 'make sellers bear all of it', 'remove the deadweight loss'], 0, 'Incidence depends on elasticities, not on who legally pays.'),
]

FLASH = [
    ['PED', '%ΔQd ÷ %ΔP; elastic if |PED| > 1.'],
    ['Revenue rule', 'Inelastic demand: price up ⇒ revenue up. Elastic: price up ⇒ revenue down.'],
    ['YED classes', '> 1 luxury; 0 to 1 necessity; < 0 inferior.'],
    ['XED signs', '> 0 substitutes; < 0 complements.'],
    ['Binding price ceiling', 'Below equilibrium; causes a shortage.'],
    ['Binding price floor', 'Above equilibrium; causes a surplus.'],
    ['Tax incidence', 'The less elastic side bears more of the tax.'],
    ['Deadweight loss of a tax', '≈ ½ × t × fall in quantity.'],
]
