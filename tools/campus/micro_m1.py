"""Principles of Microeconomics, module 1: Scarcity, demand and supply."""
from verify import Q, sp
T1, T2, T3, T4 = ('Scarcity, opportunity cost and the PPF', 'Demand', 'Supply', 'Market equilibrium and change')
P = sp.Symbol('P')
eq = sp.solve(sp.Eq(100 - 2 * P, 2 * P - 20), P)[0]
assert eq == 30 and 100 - 2 * eq == 40
eq2 = sp.solve(sp.Eq(120 - 2 * P, 2 * P - 20), P)[0]
assert eq2 == 35 and 120 - 2 * eq2 == 50
assert sp.solve(sp.Eq(60 - 3 * P, 2 * P - 10), P)[0] == 14

MODULE = {
    'title': 'Scarcity, demand and supply',
    'topics': [T1, T2, T3, T4],
    'overview': 'Economics studies how people, firms and governments choose when resources are scarce. This module builds the most-used model in the subject: demand and supply meeting in a market to set a price and a quantity, and how that outcome changes when conditions change.',
    'key_terms': ['Scarcity', 'Opportunity cost', 'Production possibility frontier', 'Demand', 'Supply', 'Equilibrium', 'Shortage', 'Surplus', 'Ceteris paribus'],
    'explanation': [
        'Because wants are unlimited and resources are limited, every choice has an opportunity cost: the value of the next best alternative given up. The production possibility frontier (PPF) shows this trade-off for a whole economy.',
        'The law of demand says that, other things equal (ceteris paribus), a higher price means a lower quantity demanded. The law of supply says a higher price means a higher quantity supplied. A change in the good\'s own price moves along a curve; a change in anything else shifts the whole curve.',
        'The market settles where quantity demanded equals quantity supplied. At any other price there is a shortage or a surplus that pushes the price back towards equilibrium. Most exam questions come down to three steps: which curve shifts, in which direction, and what happens to price and quantity.'],
    'quick_facts': [
        'Opportunity cost = the next best alternative forgone.',
        'Points inside the PPF are inefficient; points outside are unattainable.',
        'Own-price change: movement along the curve. Other factors: shift of the curve.',
        'Equilibrium: Qd = Qs.',
        'Demand up: P and Q rise. Supply up: P falls, Q rises.'],
}

NOTES = {
    T1: {
        'overview': 'Scarcity forces choices, and every choice has an opportunity cost. The production possibility frontier is a simple diagram of what an economy can produce with its resources and technology.',
        'key_terms': ['Scarcity', 'Opportunity cost', 'Production possibility frontier', 'Efficiency', 'Economic growth', 'Comparative advantage'],
        'explanation': [
            'Opportunity cost is measured in what you give up, not in money alone. The cost of a year at university includes the earnings you could have made in that year, not just the fees.',
            'A PPF shows the maximum combinations of two goods an economy can produce. Points on the frontier are efficient, points inside waste resources (for example through unemployment), and points outside cannot be reached yet. The frontier is usually bowed outwards because resources are not equally good at producing both goods, so opportunity cost rises as you specialise more.',
            'The frontier shifts outwards with economic growth: more resources, better technology or more skilled workers. Trade is based on comparative advantage: a country should specialise in the good it produces at the lower opportunity cost, even if another country is better at producing both.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Opportunity cost of X = units of Y given up ÷ units of X gained', 'On the PPF: efficient; inside: inefficient; outside: unattainable', 'Comparative advantage: lower opportunity cost', 'Growth: the PPF shifts outward'],
        'steps': ['Identify the choice and the next best alternative.', 'Measure what is given up per unit gained.', 'On a PPF, read the slope between two points.', 'Compare opportunity costs to find comparative advantage.'],
        'worked_example': {
            'problem': 'In one day Ama can make 20 shirts or 10 bags; Kofi can make 12 shirts or 4 bags. Who has the comparative advantage in bags?',
            'steps': ['Ama: 1 bag costs 20/10 = 2 shirts.', 'Kofi: 1 bag costs 12/4 = 3 shirts.', 'Ama gives up fewer shirts for each bag.'],
            'answer': 'Ama has the comparative advantage in bags; Kofi in shirts (1 shirt costs him 1/3 bag, Ama 1/2 bag).',
            'check': 'Ama is better at both (absolute advantage), yet trade still pays because the opportunity costs differ.'},
        'mistakes': ['Measuring opportunity cost only in money.', 'Confusing absolute and comparative advantage.', 'Saying a point inside the PPF is unattainable (it is attainable but wasteful).', 'Forgetting that opportunity cost rises along a bowed-out PPF.'],
        'real_world': 'Governments face a PPF too: money spent on roads cannot also be spent on hospitals. Budget debates are arguments about where on the frontier the country should be.',
        'exam_strategy': 'When asked for opportunity cost, give it per unit and in terms of the other good ("1 bag costs 2 shirts"). Vague answers such as "she loses shirts" rarely score.',
        'recap': ['Every choice has an opportunity cost.', 'PPF: on, inside, outside.', 'Bowed out: rising opportunity cost.', 'Specialise by comparative advantage.']},
    T2: {
        'overview': 'Demand is the quantity buyers are willing and able to buy at each price. It slopes downwards, and it shifts when anything other than the good\'s own price changes.',
        'key_terms': ['Demand schedule', 'Law of demand', 'Normal good', 'Inferior good', 'Substitute', 'Complement', 'Change in quantity demanded'],
        'explanation': [
            'The demand curve slopes down because of the substitution effect (the good becomes relatively dearer, so buyers switch) and the income effect (a higher price reduces what your income can buy). A price change causes a movement along the curve, called a change in quantity demanded.',
            'The curve shifts when other things change: income (demand for normal goods rises with income, for inferior goods it falls), prices of related goods (a substitute getting dearer raises demand; a complement getting dearer lowers it), tastes, expectations of future prices, and the number of buyers.',
            'A linear demand curve such as Qd = 100 − 2P can be read both ways: at P = 30, Qd = 40, and the price at which demand falls to zero is 50. Market demand is the horizontal sum of every buyer\'s demand.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Law of demand: P ↑ ⇒ Qd ↓', 'Shift factors: income, related prices, tastes, expectations, number of buyers', 'Substitutes: P of one ↑ ⇒ demand for the other ↑', 'Complements: P of one ↑ ⇒ demand for the other ↓'],
        'steps': ['Ask: did the good\'s own price change? Then move along the curve.', 'Otherwise identify the shift factor.', 'Decide the direction of the shift.', 'Draw the new curve and read the effect.'],
        'worked_example': {
            'problem': 'The price of petrol rises sharply. What happens to the demand for cars and for bus tickets?',
            'steps': ['Petrol and cars are complements: dearer petrol makes driving more expensive.', 'Demand for cars shifts left.', 'Buses are a substitute for driving, so demand for bus tickets shifts right.'],
            'answer': 'Demand for cars falls (shifts left); demand for bus travel rises (shifts right).',
            'check': 'Neither good\'s own price changed, so both effects are shifts, not movements along the curves.'},
        'mistakes': ['Saying "demand falls" when the good\'s own price rises (quantity demanded falls).', 'Mixing up substitutes and complements.', 'Assuming all goods are normal goods.', 'Shifting the curve the wrong way (left is a decrease).'],
        'real_world': 'When mobile data became cheap, demand for SMS messages (a substitute) collapsed, while demand for smartphones (a complement) soared.',
        'exam_strategy': 'Use the precise phrases "change in demand" (shift) and "change in quantity demanded" (movement). Examiners mark the distinction.',
        'recap': ['Demand slopes down.', 'Own price: movement; other factors: shift.', 'Normal vs inferior goods.', 'Substitutes and complements.']},
    T3: {
        'overview': 'Supply is the quantity sellers are willing and able to sell at each price. It usually slopes upwards, and it shifts when production conditions change.',
        'key_terms': ['Supply schedule', 'Law of supply', 'Input prices', 'Technology', 'Change in quantity supplied', 'Shift in supply'],
        'explanation': [
            'Higher prices make production more profitable and cover the rising extra cost of producing more, so quantity supplied rises with price. A change in the good\'s own price moves along the supply curve.',
            'Supply shifts with input prices (dearer inputs shift supply left), technology (better technology shifts it right), the number of sellers, expectations, taxes and subsidies on producers, and natural events such as weather for farm goods.',
            'A linear supply curve such as Qs = 2P − 20 means nothing is supplied below a price of 10, and each 1 rise in price adds 2 units. Market supply is the horizontal sum of every firm\'s supply.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Law of supply: P ↑ ⇒ Qs ↑', 'Shift factors: input prices, technology, number of sellers, expectations, taxes and subsidies, weather', 'Leftward shift = decrease in supply', 'Rightward shift = increase in supply'],
        'steps': ['Did the good\'s own price change? Move along.', 'Otherwise identify the cost or capacity factor.', 'Dearer or harder production shifts supply left; cheaper or easier shifts it right.', 'Draw and read the new equilibrium.'],
        'worked_example': {
            'problem': 'A drought cuts the cocoa harvest. What happens to the supply of chocolate?',
            'steps': ['Cocoa is an input to chocolate.', 'Less cocoa raises its price, increasing chocolate producers\' costs.', 'Supply of chocolate shifts left.'],
            'answer': 'The supply of chocolate decreases (shifts left).',
            'check': 'The price of chocolate did not cause the change, so this is a shift, not a movement.'},
        'mistakes': ['Saying "supply rises" when the price rises (it is quantity supplied).', 'Shifting supply up and calling it an increase (up and left is a decrease).', 'Forgetting that a subsidy to producers shifts supply right.', 'Confusing a demand factor (income) with a supply factor.'],
        'real_world': 'Cheaper solar panels, thanks to better technology and mass production, have shifted the supply of solar electricity far to the right, cutting its price by around 90% in a decade.',
        'exam_strategy': 'Name the shift factor explicitly ("an increase in input costs shifts supply to the left"). The cause is worth as much as the direction.',
        'recap': ['Supply slopes up.', 'Costs and technology shift supply.', 'Left = decrease, right = increase.', 'Own price: movement along.']},
    T4: {
        'overview': 'Equilibrium is where demand and supply meet. When a curve shifts, the market moves to a new equilibrium, and the direction of the price and quantity changes can be predicted.',
        'key_terms': ['Equilibrium price', 'Equilibrium quantity', 'Shortage', 'Surplus', 'Comparative statics', 'Simultaneous shifts'],
        'explanation': [
            'Set Qd = Qs and solve for P, then substitute to find Q. With Qd = 100 − 2P and Qs = 2P − 20, 100 − 2P = 2P − 20 gives P = 30 and Q = 40. Above 30 there is a surplus that pushes the price down; below 30 a shortage pushes it up.',
            'Four basic cases: demand up raises P and Q; demand down lowers both; supply up lowers P and raises Q; supply down raises P and lowers Q.',
            'When both curves shift at once, one of P or Q is certain and the other is ambiguous, because it depends on which shift is bigger. For example, if demand and supply both rise, Q definitely rises but P could go either way.'],
        'formulas_label': 'Rules',
        'formulas': ['Equilibrium: Qd = Qs', 'Excess demand (shortage) when P < P*', 'Excess supply (surplus) when P > P*', 'D↑: P↑ Q↑; D↓: P↓ Q↓; S↑: P↓ Q↑; S↓: P↑ Q↓'],
        'steps': ['Write Qd = Qs and solve for P.', 'Substitute to find Q.', 'For a change, decide which curve shifts and which way.', 'Read the new P and Q; flag ambiguity for double shifts.'],
        'worked_example': {
            'problem': 'Qd = 100 − 2P and Qs = 2P − 20. Find the equilibrium. Then incomes rise and demand becomes Qd = 120 − 2P. Find the new equilibrium.',
            'steps': ['100 − 2P = 2P − 20 gives 4P = 120, so P = 30 and Q = 40.', 'New: 120 − 2P = 2P − 20 gives 4P = 140, so P = 35.', 'Q = 120 − 70 = 50.'],
            'answer': 'Equilibrium moves from P = 30, Q = 40 to P = 35, Q = 50.',
            'check': 'Demand rose, and both P and Q rose, matching the basic rule.'},
        'mistakes': ['Shifting both curves when only one factor changed.', 'Mislabelling a shortage as a surplus.', 'Claiming a definite price change when both curves shift.', 'Algebra slips when solving Qd = Qs.'],
        'real_world': 'When a new phone launches, demand surges and stocks run out. The shortage shows the launch price is below the market-clearing price, which is why resale prices online jump in the first weeks.',
        'exam_strategy': 'Draw a fully labelled diagram (axes P and Q, both curves, old and new equilibria, arrows for the shift). In essay questions, the diagram often carries a third of the marks.',
        'recap': ['Solve Qd = Qs.', 'Shortage below, surplus above equilibrium.', 'Know the four basic shifts.', 'Double shifts: one effect is ambiguous.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'The opportunity cost of an activity is:', ['the value of the next best alternative given up', 'its money price', 'the total cost of all alternatives', 'the time it takes'], 0, 'It is what you give up by choosing it.'),
    Q(T1, 'A point inside a PPF represents:', ['inefficient use of resources', 'an unattainable output', 'efficient production', 'economic growth'], 0, 'More of one good could be produced without giving up any of the other.'),
    Q(T1, 'Ama can make 20 shirts or 10 bags a day. Her opportunity cost of one bag is:', ['2 shirts', '1/2 shirt', '10 shirts', '20 shirts'], 0, '20 shirts ÷ 10 bags = 2 shirts per bag.'),
    Q(T1, 'Kofi can make 12 shirts or 4 bags a day. His opportunity cost of one shirt is:', ['1/3 bag', '3 bags', '4 bags', '1/4 bag'], 0, '4 bags ÷ 12 shirts = 1/3 bag per shirt.'),
    Q(T1, 'An outward shift of a country\'s PPF is caused by:', ['better technology', 'higher unemployment', 'a move along the frontier', 'a fall in demand'], 0, 'More productive capacity means more of both goods can be made.'),
    Q(T1, 'A PPF is bowed outwards because:', ['resources are not equally suited to producing both goods', 'resources are unlimited', 'prices are rising', 'demand is falling'], 0, 'Moving resources that suit one good less well raises the opportunity cost.'),
    # T2
    Q(T2, 'A fall in the price of a good leads to:', ['an increase in quantity demanded', 'an increase in demand', 'a decrease in supply', 'a shift of the demand curve right'], 0, 'An own-price change is a movement along the demand curve.'),
    Q(T2, 'Incomes rise and demand for bus travel falls. Bus travel is:', ['an inferior good', 'a normal good', 'a complement to income', 'a luxury good'], 0, 'Demand for inferior goods falls as income rises.'),
    Q(T2, 'Tea and coffee are substitutes. If coffee gets dearer, demand for tea:', ['increases', 'decreases', 'stays the same', 'becomes zero'], 0, 'Buyers switch to the substitute.'),
    Q(T2, 'Qd = 100 − 2P. What is the quantity demanded at P = 30?', ['40', '70', '60', '30'], 0, '100 − 60 = 40.', ans=100 - 2 * 30),
    Q(T2, 'Qd = 100 − 2P. At what price does quantity demanded fall to zero?', ['50', '100', '25', '200'], 0, '100 − 2P = 0 gives P = 50.', ans=50),
    Q(T2, 'Printers and ink cartridges are complements. A fall in printer prices will:', ['increase demand for cartridges', 'decrease demand for cartridges', 'decrease the supply of cartridges', 'have no effect on cartridges'], 0, 'More printers sold means more cartridges needed.'),
    # T3
    Q(T3, 'Which shifts the supply of bread to the right?', ['A fall in the price of flour', 'A rise in the price of bread', 'A rise in incomes', 'A tax on bakers'], 0, 'Cheaper inputs lower costs, so more is supplied at every price.'),
    Q(T3, 'A rise in the price of a good leads to:', ['an increase in quantity supplied', 'an increase in supply', 'a shift of supply to the right', 'a decrease in demand'], 0, 'An own-price change is a movement along the supply curve.'),
    Q(T3, 'Qs = 2P − 20. What is the quantity supplied at P = 30?', ['40', '20', '60', '10'], 0, '2(30) − 20 = 40.', ans=2 * 30 - 20),
    Q(T3, 'Qs = 2P − 20. Below what price is nothing supplied?', ['10', '20', '0', '40'], 0, '2P − 20 = 0 gives P = 10.', ans=10),
    Q(T3, 'A government subsidy paid to producers of a good will:', ['shift supply to the right', 'shift supply to the left', 'shift demand to the right', 'have no effect'], 0, 'A subsidy lowers producers\' effective costs.'),
    Q(T3, 'A new law requires costly safety equipment in every factory. Supply:', ['shifts left', 'shifts right', 'does not change', 'becomes perfectly elastic'], 0, 'Higher costs reduce the quantity firms will sell at each price.'),
    # T4
    Q(T4, 'Qd = 100 − 2P and Qs = 2P − 20. What is the equilibrium price?', ['30', '40', '20', '50'], 0, '100 − 2P = 2P − 20 gives P = 30.', ans=eq),
    Q(T4, 'In the same market, what is the equilibrium quantity?', ['40', '30', '60', '50'], 0, 'Q = 100 − 2(30) = 40.', ans=40),
    Q(T4, 'Qd = 60 − 3P and Qs = 2P − 10. What is the equilibrium price?', ['14', '10', '12', '18'], 0, '60 − 3P = 2P − 10 gives 5P = 70.', ans=14),
    Q(T4, 'If the price is below equilibrium, there is:', ['a shortage, and the price tends to rise', 'a surplus, and the price tends to fall', 'equilibrium', 'a shortage, and the price tends to fall'], 0, 'Qd > Qs below equilibrium.'),
    Q(T4, 'Supply of a good decreases. The equilibrium price and quantity:', ['rise and fall respectively', 'both rise', 'both fall', 'fall and rise respectively'], 0, 'A leftward supply shift raises P and lowers Q.'),
    Q(T4, 'Demand and supply both increase. Which is certain?', ['Quantity rises', 'Price rises', 'Price falls', 'Both rise'], 0, 'Both shifts raise Q; their effects on P work in opposite directions.'),
]

FLASH = [
    ['Opportunity cost', 'The value of the next best alternative given up.'],
    ['Comparative advantage', 'Producing a good at a lower opportunity cost than others.'],
    ['Change in quantity demanded', 'Movement along the demand curve, caused by the good\'s own price.'],
    ['Inferior good', 'Demand falls when income rises.'],
    ['Complements', 'Goods used together; a price rise in one reduces demand for the other.'],
    ['Supply shift factors', 'Input prices, technology, number of sellers, expectations, taxes and subsidies.'],
    ['Equilibrium', 'Where Qd = Qs.'],
    ['Double shift rule', 'When both curves shift, either P or Q is ambiguous.'],
]
