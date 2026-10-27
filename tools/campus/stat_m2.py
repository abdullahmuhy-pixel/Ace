"""Probability and Statistics, module 2: Probability."""
from math import comb, perm, factorial
from fractions import Fraction as F
from verify import Q, sp
T1, T2, T3, T4 = ('Sample spaces and the rules of probability', 'Conditional probability and independence', "Bayes' theorem", 'Counting: permutations and combinations')
R = sp.Rational

# checked numbers
bayes = F(1, 100) * F(95, 100) / (F(1, 100) * F(95, 100) + F(99, 100) * F(5, 100))
assert round(float(bayes), 3) == 0.161 and F(1, 100) * F(95, 100) + F(99, 100) * F(5, 100) == F(59, 1000)
assert comb(10, 3) == 120 and perm(10, 3) == 720 and F(comb(5, 2) * comb(4, 1), comb(9, 3)) == F(40, 84)
assert F(3, 10) + F(4, 10) - F(1, 10) == F(6, 10)

MODULE = {
    'title': 'Probability',
    'topics': [T1, T2, T3, T4],
    'overview': 'Probability is the language for uncertainty and the foundation of everything that follows in statistics. This module builds the basic rules, conditional probability and independence, Bayes\' theorem for reversing a conditional, and the counting methods that make probabilities computable.',
    'key_terms': ['Sample space', 'Event', 'Complement', 'Mutually exclusive', 'Independent', 'Conditional probability', 'Bayes\' theorem', 'Permutation', 'Combination'],
    'explanation': [
        'A probability is a number from 0 to 1 attached to an event. With equally likely outcomes it is a count: favourable outcomes divided by total outcomes. The addition rule handles "or", the multiplication rule handles "and", and the complement rule turns "at least one" into "1 minus none".',
        'Conditional probability P(A | B) restricts attention to the cases where B happened. Events are independent when knowing one tells you nothing about the other. Bayes\' theorem reverses a conditional, turning P(positive test | disease) into the question patients actually care about, P(disease | positive test).',
        'Counting rules (the multiplication principle, permutations and combinations) let you find the number of equally likely outcomes without listing them all. The key question is always whether order matters.'],
    'quick_facts': [
        'P(A′) = 1 − P(A).',
        'P(A ∪ B) = P(A) + P(B) − P(A ∩ B).',
        'Independent: P(A ∩ B) = P(A)P(B).',
        'P(A | B) = P(A ∩ B) / P(B).',
        'nCr = n! / (r!(n − r)!); nPr = n! / (n − r)!.'],
}

NOTES = {
    T1: {
        'overview': 'The sample space lists every possible outcome of an experiment, and events are sets of outcomes. Three rules (complement, addition and multiplication for independent events) solve most basic probability questions.',
        'key_terms': ['Experiment', 'Sample space', 'Event', 'Complement', 'Union', 'Intersection', 'Mutually exclusive'],
        'explanation': [
            'Every probability lies between 0 (impossible) and 1 (certain), and the probabilities of all outcomes in the sample space add to 1. If all outcomes are equally likely, P(A) = number of outcomes in A ÷ number of outcomes in the sample space.',
            'The complement A′ is "A does not happen", so P(A′) = 1 − P(A). This is the fastest route to "at least one" questions: P(at least one six in 4 rolls) = 1 − P(no sixes) = 1 − (5/6)⁴.',
            'For "A or B" use the addition rule P(A ∪ B) = P(A) + P(B) − P(A ∩ B). The subtraction stops outcomes in both events being counted twice. If A and B are mutually exclusive (they cannot happen together), P(A ∩ B) = 0 and the rule simplifies to P(A) + P(B). A Venn diagram or a two-way table makes these questions visual.'],
        'formulas_label': 'Rules',
        'formulas': ['0 ≤ P(A) ≤ 1, and P(S) = 1', 'P(A′) = 1 − P(A)', 'P(A ∪ B) = P(A) + P(B) − P(A ∩ B)', 'Mutually exclusive: P(A ∩ B) = 0'],
        'steps': ['Define the experiment and list or describe the sample space.', 'Write each event in words and in symbols.', 'Decide whether you need "or" (addition), "and" (multiplication) or "not" (complement).', 'Check whether events overlap before adding.', 'Check the answer lies between 0 and 1.'],
        'worked_example': {
            'problem': 'In a class, 30% of students study economics, 40% study statistics and 10% study both. What is the probability that a random student studies economics or statistics?',
            'steps': ['P(E) = 0.3, P(S) = 0.4 and P(E ∩ S) = 0.1.', 'The events overlap, so use the full addition rule.', 'P(E ∪ S) = 0.3 + 0.4 − 0.1 = 0.6.'],
            'answer': 'P(economics or statistics) = 0.6.',
            'check': 'The probability of neither is 1 − 0.6 = 0.4, which matches a Venn diagram with 0.2 E only, 0.1 both, 0.3 S only and 0.4 outside.'},
        'mistakes': ['Adding probabilities of events that overlap without subtracting P(A ∩ B).', 'Confusing mutually exclusive with independent.', 'Getting a probability above 1 and not noticing.', 'Listing outcomes that are not equally likely and then counting them as if they were.'],
        'real_world': 'Insurers combine probabilities in exactly this way: the chance that a policy pays out for fire or flood is the sum of the two chances minus the chance of both in the same year.',
        'exam_strategy': 'Draw a Venn diagram or two-way table for any "or", "and" or "neither" question. Fill the overlap first, then the "only" regions, then the outside.',
        'recap': ['P(A′) = 1 − P(A).', 'Or: add, then subtract the overlap.', 'Mutually exclusive: no overlap.', '"At least one" = 1 − "none".']},
    T2: {
        'overview': 'Conditional probability measures how likely A is once we know B has happened. Independence is the special case where that knowledge changes nothing.',
        'key_terms': ['Conditional probability', 'Independent events', 'Multiplication rule', 'Two-way table', 'Tree diagram'],
        'explanation': [
            'P(A | B), read "A given B", is P(A ∩ B) / P(B). Knowing B happened shrinks the sample space to B, and we ask what fraction of B is also in A. In a two-way table this means reading across only the row or column for B.',
            'Rearranging gives the general multiplication rule P(A ∩ B) = P(B) × P(A | B). Tree diagrams apply it branch by branch: multiply along a path and add across the paths that lead to the event you want. Drawing without replacement changes the probabilities on later branches.',
            'A and B are independent if P(A | B) = P(A), or equivalently P(A ∩ B) = P(A)P(B). Independence is a property you check with numbers, not something you assume because events "feel unrelated". Mutually exclusive events with positive probabilities are never independent: if one happens, the other cannot.'],
        'formulas_label': 'Formulas',
        'formulas': ['P(A | B) = P(A ∩ B) / P(B)', 'P(A ∩ B) = P(B) P(A | B)', 'Independent ⇔ P(A ∩ B) = P(A) P(B)', 'Tree: multiply along branches, add between paths'],
        'steps': ['Identify the given event (after the bar).', 'Restrict to the cases where the given event happened.', 'Use the formula or read the table.', 'To test independence, compare P(A ∩ B) with P(A)P(B).'],
        'worked_example': {
            'problem': 'A bag holds 5 red and 3 blue counters. Two are drawn without replacement. Find P(both red).',
            'steps': ['P(first red) = 5/8.', 'Given the first was red, 4 red remain out of 7, so P(second red | first red) = 4/7.', 'Multiply: 5/8 × 4/7 = 20/56 = 5/14.'],
            'answer': 'P(both red) = 5/14 ≈ 0.357.',
            'check': 'Counting gives the same answer: C(5,2) / C(8,2) = 10/28 = 5/14.'},
        'mistakes': ['Mixing up P(A | B) and P(B | A).', 'Forgetting that probabilities change after drawing without replacement.', 'Assuming events are independent without checking.', 'Thinking mutually exclusive events are independent.'],
        'real_world': 'Insurers set car premiums using conditional probabilities: P(claim | driver aged under 25) is higher than P(claim) for all drivers, so younger drivers pay more.',
        'exam_strategy': 'Underline the word "given" or the phrase "if it is known that". Whatever follows is the condition, and it goes in the denominator.',
        'recap': ['P(A | B) = P(A ∩ B) / P(B).', 'Without replacement changes later branches.', 'Independence: P(A ∩ B) = P(A)P(B).', 'Exclusive is not the same as independent.']},
    T3: {
        'overview': 'Bayes\' theorem turns a conditional around. It answers questions like "given a positive test, how likely is the disease?" from information about how the test behaves, and it often gives surprising answers when the condition is rare.',
        'key_terms': ['Prior probability', 'Posterior probability', 'Likelihood', 'Law of total probability', 'False positive', 'Sensitivity', 'Specificity'],
        'explanation': [
            'The law of total probability finds P(B) by splitting into cases: P(B) = P(B | A)P(A) + P(B | A′)P(A′). Bayes\' theorem then gives P(A | B) = P(B | A)P(A) / P(B). The prior P(A) is what we believed before the evidence, and the posterior P(A | B) is what we believe after it.',
            'Medical tests are the classic case. Sensitivity is P(positive | disease) and specificity is P(negative | no disease). When a disease is rare, most positive results can come from the large healthy group, even with a good test. This is called the base-rate effect.',
            'A frequency table makes Bayes intuitive. Imagine 10 000 people and fill in how many are in each case. The posterior is then just the count of people with the disease who tested positive, divided by everyone who tested positive.'],
        'formulas_label': 'Formulas',
        'formulas': ['P(B) = P(B | A)P(A) + P(B | A′)P(A′)', 'P(A | B) = P(B | A)P(A) / P(B)', 'Sensitivity = P(+ | disease)', 'Specificity = P(− | no disease)'],
        'steps': ['Write the prior P(A) and P(A′).', 'Write P(B | A) and P(B | A′).', 'Find P(B) by the law of total probability.', 'Divide the "A and B" path by P(B).', 'Interpret the answer in context.'],
        'worked_example': {
            'problem': 'A disease affects 1% of people. A test is positive for 95% of people with the disease and for 5% of people without it. If a person tests positive, what is the probability they have the disease?',
            'steps': ['P(D) = 0.01, P(D′) = 0.99, P(+ | D) = 0.95 and P(+ | D′) = 0.05.', 'P(+) = 0.95 × 0.01 + 0.05 × 0.99 = 0.0095 + 0.0495 = 0.059.', 'P(D | +) = 0.0095 / 0.059 ≈ 0.161.'],
            'answer': 'About 16%: most positive results come from healthy people.',
            'check': 'With 10 000 people, 100 have the disease and 95 of them test positive, while 495 of the 9 900 healthy people also test positive. 95 / 590 ≈ 0.161 ✓.'},
        'mistakes': ['Answering with P(+ | D) = 0.95 instead of P(D | +).', 'Forgetting the false positives when finding P(+).', 'Ignoring the prior (the base rate).', 'Using percentages and decimals together without converting.'],
        'real_world': 'This is why screening programmes follow a positive result with a second, more specific test. It is also how spam filters work: they update the probability that an email is spam as each suspicious word appears.',
        'exam_strategy': 'Draw a tree with the condition (disease or not) on the first branches and the test result on the second. Bayes is then one path divided by the sum of two paths.',
        'recap': ['Total probability: add over the cases.', 'Bayes: P(A | B) = P(B | A)P(A) / P(B).', 'Rare conditions mean many false positives.', 'A frequency table of 10 000 people makes it concrete.']},
    T4: {
        'overview': 'Many probabilities are counts of equally likely outcomes. The multiplication principle, permutations and combinations count those outcomes quickly. The deciding question is whether order matters.',
        'key_terms': ['Multiplication principle', 'Factorial', 'Permutation', 'Combination', 'With replacement', 'Without replacement'],
        'explanation': [
            'The multiplication principle: if one choice has m options and a second has n, there are m × n ways to make both. A 4-digit PIN with digits 0 to 9 has 10⁴ = 10 000 possibilities, because each digit can repeat.',
            'A permutation is an ordered arrangement. The number of ways to arrange r items chosen from n distinct items is nPr = n! / (n − r)!. Choosing a chair, a secretary and a treasurer from 10 people gives 10 × 9 × 8 = 720 ways, because the roles are different.',
            'A combination is a selection where order does not matter: nCr = n! / (r!(n − r)!). Choosing a committee of 3 from 10 gives 120 ways, which is 720 ÷ 3!, because each committee was counted 3! times as a permutation. Probabilities follow by dividing favourable selections by total selections.'],
        'formulas_label': 'Formulas',
        'formulas': ['n! = n × (n − 1) × … × 1, and 0! = 1', 'nPr = n! / (n − r)!', 'nCr = n! / (r!(n − r)!)', 'Arrangements of n items with repeats: n! / (n₁! n₂! …)'],
        'steps': ['Decide whether order matters.', 'Decide whether repetition is allowed.', 'Use a power, nPr or nCr accordingly.', 'For probability, divide favourable counts by total counts.'],
        'worked_example': {
            'problem': 'A committee of 3 is chosen at random from 5 women and 4 men. What is the probability it has exactly 2 women?',
            'steps': ['Total committees: 9C3 = 84.', 'Favourable: choose 2 of 5 women and 1 of 4 men, so 5C2 × 4C1 = 10 × 4 = 40.', 'Probability = 40 / 84 = 10/21.'],
            'answer': 'P(exactly 2 women) = 10/21 ≈ 0.476.',
            'check': 'Other cases: 3 women 10, 1 woman 5C1 × 4C2 = 30, no women 4. 10 + 40 + 30 + 4 = 84 ✓.'},
        'mistakes': ['Using permutations when order does not matter.', 'Forgetting that 0! = 1.', 'Multiplying when the cases should be added ("2 women or 3 women").', 'Using 10⁴ when repetition is not allowed (it should be 10P4).'],
        'real_world': 'Lottery odds come from combinations. Choosing 6 numbers from 49 gives 49C6 = 13 983 816 possible tickets, which is why the jackpot is so unlikely.',
        'exam_strategy': 'Write "order matters?" and "repetition?" in the margin and answer both before choosing a formula. That one habit prevents most counting errors.',
        'recap': ['Multiply the options for successive choices.', 'Order matters: nPr.', 'Order does not matter: nCr.', 'Probability = favourable ÷ total.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A fair die is rolled. What is P(a number greater than 4)?', ['1/3', '1/2', '2/3', '1/6'], 0, 'Outcomes 5 and 6 give 2 of 6 = 1/3.', ans=R(2, 6)),
    Q(T1, 'P(A) = 0.3, P(B) = 0.5 and P(A ∩ B) = 0.1. What is P(A ∪ B)?', ['0.7', '0.8', '0.15', '0.9'], 0, '0.3 + 0.5 − 0.1 = 0.7.', ans=R(7, 10)),
    Q(T1, 'If P(rain) = 0.35, what is P(no rain)?', ['0.65', '0.35', '0.7', '0'], 0, 'Complement: 1 − 0.35 = 0.65.', ans=R(65, 100)),
    Q(T1, 'A fair coin is tossed 3 times. What is P(at least one head)?', ['7/8', '1/8', '1/2', '3/8'], 0, '1 − P(no heads) = 1 − (1/2)³ = 7/8.', ans=1 - R(1, 8)),
    Q(T1, 'Events A and B are mutually exclusive with P(A) = 0.2 and P(B) = 0.45. What is P(A or B)?', ['0.65', '0.09', '0.55', '0.25'], 0, 'No overlap, so add: 0.2 + 0.45 = 0.65.', ans=R(65, 100)),
    Q(T1, 'Which value cannot be a probability?', ['1.2', '0', '1', '0.999'], 0, 'Probabilities lie between 0 and 1 inclusive.'),
    # T2
    Q(T2, 'P(A ∩ B) = 0.12 and P(B) = 0.4. Find P(A | B).', ['0.3', '0.048', '0.52', '0.12'], 0, '0.12 / 0.4 = 0.3.', ans=R(12, 40)),
    Q(T2, 'Two cards are drawn without replacement from a standard 52-card deck. What is P(both aces)?', ['1/221', '1/169', '4/52', '1/13'], 0, '4/52 × 3/51 = 12/2652 = 1/221.', ans=R(4, 52) * R(3, 51)),
    Q(T2, 'P(A) = 0.5, P(B) = 0.4 and P(A ∩ B) = 0.2. Are A and B independent?', ['Yes, because P(A)P(B) = 0.2', 'No, because they overlap', 'No, because P(A ∪ B) = 0.7', 'Yes, because P(A) > P(B)'], 0, 'P(A)P(B) = 0.5 × 0.4 = 0.2 = P(A ∩ B).'),
    Q(T2, 'Of 200 students, 80 drive to campus and 30 of those drivers live off campus. What is P(lives off campus | drives)?', ['0.375', '0.15', '0.4', '0.3'], 0, 'Restrict to the 80 drivers: 30/80 = 0.375.', ans=R(30, 80)),
    Q(T2, 'A and B are independent with P(A) = 0.6 and P(B) = 0.3. What is P(A ∩ B)?', ['0.18', '0.9', '0.5', '0.3'], 0, 'Independent: multiply, 0.6 × 0.3 = 0.18.', ans=R(18, 100)),
    Q(T2, 'A bag has 5 red and 3 blue counters. Two are drawn without replacement. What is P(one of each colour)?', ['15/28', '15/56', '30/64', '1/2'], 0, 'Red then blue 5/8 × 3/7 = 15/56, blue then red 3/8 × 5/7 = 15/56, total 30/56 = 15/28.', ans=2 * R(5, 8) * R(3, 7)),
    # T3
    Q(T3, 'A disease has prevalence 1%. A test has sensitivity 95% and a false positive rate of 5%. What is P(disease | positive), to 3 d.p.?', ['0.161', '0.950', '0.010', '0.059'], 0, '0.0095 / (0.0095 + 0.0495) ≈ 0.161.', ans=sp.Rational(bayes.numerator, bayes.denominator), num=True),
    Q(T3, 'In the same test, what is P(positive) overall?', ['0.059', '0.0095', '0.05', '0.95'], 0, '0.95 × 0.01 + 0.05 × 0.99 = 0.059.', ans=R(59, 1000)),
    Q(T3, 'Machine A makes 60% of a factory\'s parts with 2% faulty; machine B makes 40% with 5% faulty. What is P(faulty)?', ['0.032', '0.035', '0.07', '0.02'], 0, '0.6 × 0.02 + 0.4 × 0.05 = 0.012 + 0.020 = 0.032.', ans=R(6, 10) * R(2, 100) + R(4, 10) * R(5, 100)),
    Q(T3, 'Using the machine data, a part is faulty. What is P(it came from machine B)?', ['0.625', '0.4', '0.05', '0.375'], 0, '0.020 / 0.032 = 0.625.', ans=(R(4, 10) * R(5, 100)) / (R(6, 10) * R(2, 100) + R(4, 10) * R(5, 100))),
    Q(T3, 'In Bayes\' theorem, P(A) before the evidence is called the:', ['prior', 'posterior', 'likelihood', 'complement'], 0, 'The prior is updated by the evidence to give the posterior P(A | B).'),
    Q(T3, 'Specificity of a test is:', ['P(negative | no disease)', 'P(positive | disease)', 'P(disease | positive)', 'P(no disease | negative)'], 0, 'Specificity measures how well the test clears healthy people.'),
    # T4
    Q(T4, 'In how many ways can a chair, a secretary and a treasurer be chosen from 10 people?', ['720', '120', '30', '1000'], 0, 'Order matters (different roles): 10P3 = 10 × 9 × 8 = 720.', ans=perm(10, 3)),
    Q(T4, 'How many committees of 3 can be chosen from 10 people?', ['120', '720', '30', '1000'], 0, '10C3 = 720 / 3! = 120.', ans=comb(10, 3)),
    Q(T4, 'How many 4-digit PINs are possible if digits can repeat?', ['10000', '5040', '9999', '40'], 0, '10 choices for each of 4 digits: 10⁴ = 10000.', ans=10 ** 4),
    Q(T4, 'How many distinct arrangements are there of the letters of LEVEL?', ['30', '120', '60', '20'], 0, '5! / (2! × 2!) = 120 / 4 = 30 (two Ls and two Es).', ans=factorial(5) // (factorial(2) * factorial(2))),
    Q(T4, 'A committee of 3 is chosen from 5 women and 4 men. What is P(exactly 2 women)?', ['10/21', '5/14', '40/729', '2/3'], 0, '5C2 × 4C1 / 9C3 = 40 / 84 = 10/21.', ans=R(comb(5, 2) * comb(4, 1), comb(9, 3))),
    Q(T4, 'What is 0!?', ['1', '0', 'Undefined', 'Infinity'], 0, 'By definition 0! = 1, which makes nCn = 1 work.'),
]

FLASH = [
    ['Addition rule', 'P(A ∪ B) = P(A) + P(B) − P(A ∩ B).'],
    ['Complement rule', 'P(A′) = 1 − P(A); "at least one" = 1 − "none".'],
    ['Conditional probability', 'P(A | B) = P(A ∩ B) / P(B).'],
    ['Independent events', 'P(A ∩ B) = P(A)P(B), so P(A | B) = P(A).'],
    ['Bayes\' theorem', 'P(A | B) = P(B | A)P(A) / P(B).'],
    ['Base-rate effect', 'When a condition is rare, most positive tests can be false positives.'],
    ['Permutation', 'Order matters: nPr = n! / (n − r)!.'],
    ['Combination', 'Order does not matter: nCr = n! / (r!(n − r)!).'],
]
