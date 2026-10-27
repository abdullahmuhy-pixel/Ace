"""Probability and Statistics, module 3: Random variables and distributions."""
from math import comb, exp, factorial
from verify import Q, sp
T1, T2, T3, T4 = ('Discrete random variables: expectation and variance', 'The binomial distribution', 'The Poisson distribution', 'Continuous random variables')
R = sp.Rational
xs, ps = [0, 1, 2, 3], [R(1, 10), R(3, 10), R(4, 10), R(2, 10)]
EX = sum(x * p for x, p in zip(xs, ps)); EX2 = sum(x * x * p for x, p in zip(xs, ps))
assert EX == R(17, 10) and EX2 == R(37, 10) and EX2 - EX ** 2 == R(81, 100)
b3 = comb(10, 3) * 0.3 ** 3 * 0.7 ** 7
assert round(b3, 4) == 0.2668
p2 = exp(-4) * 4 ** 2 / factorial(2)
assert round(p2, 4) == 0.1465 and round(exp(-1), 3) == 0.368

MODULE = {
    'title': 'Random variables and distributions',
    'topics': [T1, T2, T3, T4],
    'overview': 'A random variable attaches a number to each outcome of an experiment. This module covers how to describe one with a probability distribution, its mean (expected value) and variance, and the standard models you will meet again and again: binomial, Poisson, uniform and exponential.',
    'key_terms': ['Random variable', 'Probability distribution', 'Expected value', 'Variance', 'Binomial', 'Poisson', 'Probability density function', 'Cumulative distribution function'],
    'explanation': [
        'A discrete random variable takes separate values (counts), and its distribution lists each value with its probability. A continuous random variable takes any value in an interval (times, weights), and its distribution is a density curve where areas give probabilities.',
        'The expected value E(X) is the long-run average of X over many repetitions, and the variance measures spread around it. Linear changes behave simply: E(aX + b) = aE(X) + b and Var(aX + b) = a²Var(X).',
        'Recognising the model saves work. A fixed number of independent yes/no trials with the same probability is binomial. Counts of rare events in a fixed interval of time or space are Poisson. Waiting times between such events are exponential.'],
    'quick_facts': [
        'E(X) = Σx P(X = x); Var(X) = E(X²) − [E(X)]².',
        'Binomial: mean np, variance np(1 − p).',
        'Poisson: mean = variance = λ.',
        'Continuous: P(X = a) = 0; probabilities are areas.',
        'Uniform on [a, b]: mean (a + b)/2, variance (b − a)²/12.'],
}

NOTES = {
    T1: {
        'overview': 'A discrete probability distribution lists every value a random variable can take and its probability. From it you can find the expected value (the long-run mean) and the variance.',
        'key_terms': ['Random variable', 'Probability mass function', 'Expected value', 'Variance', 'Linear transformation'],
        'explanation': [
            'A valid distribution has every probability between 0 and 1 and the probabilities add to 1. That fact is often used to find a missing probability, for example a constant k in a table.',
            'The expected value E(X) = Σx P(X = x) weights each value by how likely it is. It need not be a possible value: the expected number of heads in 3 tosses is 1.5. Think of it as the average you would see over a very long run.',
            'The variance is Var(X) = E[(X − μ)²], and it is easiest to compute as E(X²) − [E(X)]², where E(X²) = Σx² P(X = x). For a linear change Y = aX + b, E(Y) = aE(X) + b and Var(Y) = a²Var(X). Adding a constant shifts the distribution but does not change its spread.'],
        'formulas_label': 'Formulas',
        'formulas': ['ΣP(X = x) = 1', 'E(X) = Σx P(X = x)', 'Var(X) = E(X²) − [E(X)]²', 'E(aX + b) = aE(X) + b', 'Var(aX + b) = a²Var(X)'],
        'steps': ['Check the probabilities add to 1 (find any unknown).', 'Multiply each value by its probability and add to get E(X).', 'Multiply each x² by its probability and add to get E(X²).', 'Var(X) = E(X²) − [E(X)]²; take the square root for the SD.'],
        'worked_example': {
            'problem': 'X takes values 0, 1, 2, 3 with probabilities 0.1, 0.3, 0.4, 0.2. Find E(X) and Var(X).',
            'steps': ['E(X) = 0(0.1) + 1(0.3) + 2(0.4) + 3(0.2) = 0 + 0.3 + 0.8 + 0.6 = 1.7.', 'E(X²) = 0(0.1) + 1(0.3) + 4(0.4) + 9(0.2) = 0.3 + 1.6 + 1.8 = 3.7.', 'Var(X) = 3.7 − 1.7² = 3.7 − 2.89 = 0.81.'],
            'answer': 'E(X) = 1.7, Var(X) = 0.81 and SD = 0.9.',
            'check': 'The probabilities add to 1 ✓ and the mean 1.7 lies between the most likely values 1 and 2.'},
        'mistakes': ['Computing [E(X)]² and calling it E(X²).', 'Forgetting to square a in Var(aX + b).', 'Thinking adding a constant changes the variance.', 'Not checking that the probabilities add to 1.'],
        'real_world': 'Insurers price policies by expected value. If a policy pays 100 000 with probability 0.002, the expected payout is 200, and the premium is set above that to cover costs and risk.',
        'exam_strategy': 'Lay the work out as a table with columns x, P(X = x), xP and x²P, then add down. It is fast, easy to check, and earns method marks.',
        'recap': ['Probabilities add to 1.', 'E(X) = Σx P(x).', 'Var = E(X²) − [E(X)]².', 'Var(aX + b) = a²Var(X).']},
    T2: {
        'overview': 'The binomial distribution counts the number of successes in a fixed number of independent trials, each with the same probability of success. It models pass/fail, yes/no and defective/not-defective counts.',
        'key_terms': ['Bernoulli trial', 'Binomial distribution', 'n', 'p', 'Cumulative probability'],
        'explanation': [
            'X ~ B(n, p) needs four conditions: a fixed number of trials n, two outcomes per trial, independent trials, and a constant success probability p. Drawing without replacement from a small group breaks independence, so it is not binomial.',
            'P(X = k) = nCk p^k (1 − p)^(n − k). The term nCk counts the arrangements of k successes among n trials, and the powers give the probability of any one arrangement.',
            'The mean is np and the variance is np(1 − p). For "at most" and "at least" questions use cumulative probabilities from tables or a calculator, and remember that P(X ≥ k) = 1 − P(X ≤ k − 1).'],
        'formulas_label': 'Formulas',
        'formulas': ['P(X = k) = nCk p^k (1 − p)^(n − k)', 'E(X) = np', 'Var(X) = np(1 − p)', 'P(X ≥ k) = 1 − P(X ≤ k − 1)'],
        'steps': ['Check the four binomial conditions.', 'Identify n, p and the values of k needed.', 'Apply the formula, or a cumulative table for ranges.', 'Use the complement for "at least" questions.'],
        'worked_example': {
            'problem': '30% of a city\'s students use a particular app. In a random sample of 10 students, find P(exactly 3 use it) and the expected number who use it.',
            'steps': ['X ~ B(10, 0.3).', 'P(X = 3) = 10C3 × 0.3³ × 0.7⁷ = 120 × 0.027 × 0.0823543 ≈ 0.2668.', 'E(X) = np = 10 × 0.3 = 3.'],
            'answer': 'P(X = 3) ≈ 0.2668 and E(X) = 3.',
            'check': 'The most likely value of a binomial is near its mean, and 3 is the mean here, so a fairly large probability makes sense.'},
        'mistakes': ['Forgetting the nCk factor.', 'Using binomial when trials are not independent (small population without replacement).', 'Treating "at least 3" as P(X ≤ 3) or 1 − P(X ≤ 3).', 'Swapping p and 1 − p.'],
        'real_world': 'Airlines overbook because the number of passengers who show up is roughly binomial. If each of 200 ticket holders shows up with probability 0.95, they can calculate how likely it is that more than 190 arrive.',
        'exam_strategy': 'State "X ~ B(n, p)" with the values filled in before calculating. Examiners award a mark for naming the distribution and its parameters.',
        'recap': ['Fixed n, two outcomes, independent, constant p.', 'P(X = k) = nCk p^k (1 − p)^(n − k).', 'Mean np, variance np(1 − p).', 'At least k: 1 − P(X ≤ k − 1).']},
    T3: {
        'overview': 'The Poisson distribution models the number of times a rare event happens in a fixed interval of time, area or volume: calls per hour, typing errors per page, accidents per month.',
        'key_terms': ['Poisson distribution', 'Rate λ', 'Interval', 'Rare events', 'Poisson approximation'],
        'explanation': [
            'X ~ Po(λ) when events occur singly, independently and at a constant average rate λ per interval. P(X = k) = e^(−λ) λ^k / k! for k = 0, 1, 2, …, with no upper limit.',
            'The mean and the variance are both λ. If a sample of counts has a variance close to its mean, a Poisson model is plausible; a variance much larger than the mean suggests events are clustered.',
            'The rate scales with the interval: 4 calls per hour means λ = 2 for half an hour and λ = 8 for two hours. A binomial with large n and small p is approximately Poisson with λ = np.'],
        'formulas_label': 'Formulas',
        'formulas': ['P(X = k) = e^(−λ) λ^k / k!', 'E(X) = Var(X) = λ', 'Rate scales with the interval length', 'B(n, p) ≈ Po(np) for large n, small p'],
        'steps': ['Check the events are random, independent and at a constant rate.', 'Scale λ to the interval in the question.', 'Apply the formula, or cumulative tables for ranges.', 'Use 1 − P(X = 0) for "at least one".'],
        'worked_example': {
            'problem': 'A help desk receives on average 4 calls per hour. Find the probability of exactly 2 calls in an hour, and of at least one call in 15 minutes.',
            'steps': ['X ~ Po(4): P(X = 2) = e^(−4) × 4² / 2! = 8e^(−4) ≈ 0.1465.', 'For 15 minutes, λ = 4 × 0.25 = 1.', 'P(at least 1) = 1 − e^(−1) ≈ 1 − 0.368 = 0.632.'],
            'answer': 'P(2 calls in an hour) ≈ 0.1465; P(at least 1 call in 15 minutes) ≈ 0.632.',
            'check': 'With an average of only 1 call per 15 minutes, it is reasonable that about a third of quarter-hours have no calls.'},
        'mistakes': ['Not rescaling λ to the interval asked about.', 'Using Poisson when there is a fixed maximum number of trials and p is not small.', 'Forgetting e^(−λ) in the formula.', 'Calculating 1 − P(X = 1) for "at least one".'],
        'real_world': 'Hospitals use Poisson models for emergency arrivals per hour to decide how many staff to roster, so that queues are short at the busiest times without paying for idle staff.',
        'exam_strategy': 'Write "X ~ Po(λ)" with the rescaled λ for the interval. Then check that your answer is sensible against the mean.',
        'recap': ['Counts of rare events in an interval.', 'P(X = k) = e^(−λ)λ^k / k!.', 'Mean = variance = λ.', 'Rescale λ to the interval.']},
    T4: {
        'overview': 'A continuous random variable can take any value in an interval. Its probabilities are areas under a probability density function (pdf), and the cumulative distribution function (cdf) accumulates that area.',
        'key_terms': ['Probability density function', 'Cumulative distribution function', 'Uniform distribution', 'Exponential distribution', 'Area under the curve'],
        'explanation': [
            'A pdf f(x) is never negative and has total area 1. P(a < X < b) is the area under f between a and b, which is ∫ f(x) dx from a to b. Any single value has probability 0, so < and ≤ give the same answer for continuous variables.',
            'The cdf is F(x) = P(X ≤ x), so P(a < X ≤ b) = F(b) − F(a). The mean is E(X) = ∫ x f(x) dx, and the median m solves F(m) = 0.5.',
            'Two standard models: the uniform distribution on [a, b] has constant density 1/(b − a), mean (a + b)/2 and variance (b − a)²/12. The exponential distribution with rate λ models waiting times between Poisson events, with P(X > t) = e^(−λt) and mean 1/λ.'],
        'formulas_label': 'Formulas',
        'formulas': ['∫ f(x) dx over all x = 1', 'P(a < X < b) = ∫ₐᵇ f(x) dx = F(b) − F(a)', 'E(X) = ∫ x f(x) dx', 'Uniform[a, b]: f = 1/(b − a), mean (a + b)/2', 'Exponential: P(X > t) = e^(−λt), mean 1/λ'],
        'steps': ['Check (or use) total area = 1.', 'For a probability, integrate f between the limits (or use areas of shapes).', 'For the mean, integrate x f(x).', 'For a median, solve F(m) = 0.5.'],
        'worked_example': {
            'problem': 'X has pdf f(x) = 2x for 0 ≤ x ≤ 1 and 0 otherwise. Find P(X < 0.5) and E(X).',
            'steps': ['Total area: ∫₀¹ 2x dx = [x²]₀¹ = 1 ✓.', 'P(X < 0.5) = ∫₀^0.5 2x dx = 0.5² = 0.25.', 'E(X) = ∫₀¹ x × 2x dx = [2x³/3]₀¹ = 2/3.'],
            'answer': 'P(X < 0.5) = 0.25 and E(X) = 2/3.',
            'check': 'The density rises towards 1, so most of the area is on the right: a mean above 0.5 and only a quarter of the area below 0.5 both make sense.'},
        'mistakes': ['Treating f(x) as a probability. It is a density and can be bigger than 1.', 'Thinking P(X = a) is f(a).', 'Forgetting to check that the total area is 1 when finding a constant k.', 'Using the uniform variance (b − a)/12 without squaring.'],
        'real_world': 'Reliability engineers model the time until a component fails with continuous distributions such as the exponential, and use them to set warranty periods and maintenance schedules.',
        'exam_strategy': 'Sketch the pdf first. Many probabilities are areas of rectangles or triangles and need no integration at all.',
        'recap': ['Probabilities are areas under f(x).', 'P(X = a) = 0.', 'E(X) = ∫ x f(x) dx.', 'Uniform: (a + b)/2 and (b − a)²/12; exponential: e^(−λt).']},
}

QUESTIONS = [
    # T1
    Q(T1, 'X takes values 0, 1, 2, 3 with probabilities 0.1, 0.3, 0.4, 0.2. Find E(X).', ['1.7', '1.5', '2', '0.85'], 0, '0 + 0.3 + 0.8 + 0.6 = 1.7.', ans=EX),
    Q(T1, 'For the same X, Var(X) is:', ['0.81', '3.7', '0.9', '2.89'], 0, 'E(X²) = 3.7, so Var = 3.7 − 1.7² = 0.81.', ans=EX2 - EX ** 2),
    Q(T1, 'P(X = 1) = 0.2, P(X = 2) = k and P(X = 3) = 0.5, with no other values. What is k?', ['0.3', '0.5', '0.7', '0.2'], 0, 'The probabilities add to 1: 0.2 + k + 0.5 = 1, so k = 0.3.', ans=R(3, 10)),
    Q(T1, 'E(X) = 4 and Var(X) = 9. Find Var(2X + 5).', ['36', '18', '23', '41'], 0, 'Var(aX + b) = a²Var(X) = 4 × 9 = 36. The +5 has no effect.', ans=4 * 9),
    Q(T1, 'E(X) = 4. Find E(3X − 2).', ['10', '12', '14', '4'], 0, '3 × 4 − 2 = 10.', ans=3 * 4 - 2),
    Q(T1, 'A game pays 10 with probability 0.2 and 0 otherwise. It costs 3 to play. What is the expected profit per game?', ['−1', '2', '−3', '1'], 0, 'Expected payout 10 × 0.2 = 2, minus the cost of 3, gives −1.', ans=-1),
    # T2
    Q(T2, 'X ~ B(10, 0.3). Find P(X = 3) to 4 d.p.', ['0.2668', '0.0270', '0.3000', '0.6496'], 0, '10C3 × 0.3³ × 0.7⁷ ≈ 0.2668.', ans=b3, num=True),
    Q(T2, 'X ~ B(20, 0.25). What is E(X)?', ['5', '15', '3.75', '0.25'], 0, 'np = 20 × 0.25 = 5.', ans=5),
    Q(T2, 'X ~ B(20, 0.25). What is Var(X)?', ['3.75', '5', '1.94', '15'], 0, 'np(1 − p) = 20 × 0.25 × 0.75 = 3.75.', ans=R(375, 100)),
    Q(T2, 'A fair coin is tossed 4 times. What is P(exactly 2 heads)?', ['3/8', '1/2', '1/4', '1/16'], 0, '4C2 × 0.5⁴ = 6/16 = 3/8.', ans=R(comb(4, 2), 16)),
    Q(T2, 'Which situation is NOT binomial?', ['Drawing 3 cards from a deck without replacement and counting hearts', 'Counting heads in 10 coin tosses', 'Counting defective items among 50 from a large production run', 'Counting correct guesses on 20 four-option questions'], 0, 'Without replacement from 52 cards, the probability changes from draw to draw, so the trials are not independent.'),
    Q(T2, 'X ~ B(5, 0.2). Find P(X ≥ 1) to 4 d.p.', ['0.6723', '0.3277', '0.4096', '0.2000'], 0, '1 − P(X = 0) = 1 − 0.8⁵ = 1 − 0.32768 = 0.67232.', ans=1 - 0.8 ** 5, num=True),
    # T3
    Q(T3, 'X ~ Po(4). Find P(X = 2) to 4 d.p.', ['0.1465', '0.0733', '0.2381', '0.0183'], 0, 'e^(−4) × 16 / 2 = 8e^(−4) ≈ 0.1465.', ans=p2, num=True),
    Q(T3, 'X ~ Po(3). What is Var(X)?', ['3', '9', '√3', '1/3'], 0, 'For a Poisson distribution the variance equals the mean λ.', ans=3),
    Q(T3, 'Calls arrive at 6 per hour. What is λ for a 20-minute period?', ['2', '6', '3', '18'], 0, '20 minutes is a third of an hour: 6 × 1/3 = 2.', ans=2),
    Q(T3, 'X ~ Po(1). Find P(X ≥ 1) to 3 d.p.', ['0.632', '0.368', '0.264', '1.000'], 0, '1 − e^(−1) ≈ 1 − 0.368 = 0.632.', ans=1 - exp(-1), num=True),
    Q(T3, 'Which is best modelled by a Poisson distribution?', ['Typing errors per page of a long report', 'Heights of students', 'Number of heads in 10 tosses', 'Time taken to run 100 m'], 0, 'Errors are rare, independent events counted in a fixed interval (a page).'),
    Q(T3, 'A binomial with n = 500 and p = 0.004 is approximately Poisson with λ =', ['2', '0.004', '500', '125'], 0, 'λ = np = 500 × 0.004 = 2.', ans=2),
    # T4
    Q(T4, 'X has pdf f(x) = 2x on [0, 1]. Find P(X < 0.5).', ['0.25', '0.5', '0.75', '1'], 0, '∫₀^0.5 2x dx = 0.5² = 0.25.', ans=sp.integrate(2 * sp.Symbol('x'), (sp.Symbol('x'), 0, R(1, 2)))),
    Q(T4, 'X has pdf f(x) = 2x on [0, 1]. Find E(X).', ['2/3', '1/2', '1/3', '1'], 0, '∫₀¹ 2x² dx = 2/3.', ans=sp.integrate(2 * sp.Symbol('x') ** 2, (sp.Symbol('x'), 0, 1))),
    Q(T4, 'X is uniform on [2, 10]. Find P(3 < X < 7).', ['0.5', '0.4', '0.625', '0.3'], 0, 'The density is 1/8, so the probability is 4 × 1/8 = 0.5.', ans=R(4, 8)),
    Q(T4, 'X is uniform on [2, 10]. Find Var(X), to 3 d.p.', ['5.333', '0.667', '6.000', '2.309'], 0, '(b − a)²/12 = 64/12 ≈ 5.333.', ans=R(64, 12), num=True),
    Q(T4, 'f(x) = kx² on [0, 3] is a pdf. What is k?', ['1/9', '1/3', '9', '1/27'], 0, '∫₀³ kx² dx = 9k = 1, so k = 1/9.', ans=R(1, 9)),
    Q(T4, 'Waiting time X is exponential with rate λ = 0.5 per minute. Find P(X > 2) to 3 d.p.', ['0.368', '0.632', '0.500', '0.135'], 0, 'P(X > t) = e^(−λt) = e^(−1) ≈ 0.368.', ans=exp(-1), num=True),
]

FLASH = [
    ['Expected value', 'E(X) = Σx P(X = x): the long-run average.'],
    ['Variance shortcut', 'Var(X) = E(X²) − [E(X)]².'],
    ['Var(aX + b)', 'a²Var(X); the constant b has no effect.'],
    ['Binomial conditions', 'Fixed n, two outcomes, independent trials, constant p.'],
    ['Binomial mean and variance', 'np and np(1 − p).'],
    ['Poisson', 'P(X = k) = e^(−λ)λ^k / k!; mean = variance = λ.'],
    ['Continuous probability', 'Area under the pdf; P(X = a) = 0.'],
    ['Uniform on [a, b]', 'Mean (a + b)/2, variance (b − a)²/12.'],
]
