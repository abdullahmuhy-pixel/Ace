"""General Chemistry, module 4: Rates, equilibrium, acids and bases."""
import math
from verify import Q
from chem_common import r, pH
T1, T2, T3, T4 = ('Reaction rates and rate laws', 'Chemical equilibrium and Kc', 'Le Chatelier\'s principle', 'Acids, bases and pH')

assert r(0.693 / 0.0231, 1) == 30.0 and 2 ** 2 * 3 == 12
Kc = 0.70 ** 2 / (0.10 * 0.10)
assert r(Kc, 0) == 49
h = math.sqrt(1.8e-5 * 0.10)
assert r(h, 5) == 0.00134 and r(pH(h), 2) == 2.87 and r(pH(1e-3), 1) == 3.0 and r(14 - pH(1e-2), 1) == 12.0 and r(pH(2.5e-4), 2) == 3.60
assert r(10 ** -4.5, 7) == 0.0000316

MODULE = {
    'title': 'Rates, equilibrium, acids and bases',
    'topics': [T1, T2, T3, T4],
    'overview': 'Knowing that a reaction releases energy does not tell you how fast it goes or how far. This module covers reaction rates and rate laws, chemical equilibrium and its constant, how equilibria respond to change, and the chemistry of acids and bases, including pH.',
    'key_terms': ['Rate of reaction', 'Rate constant', 'Order of reaction', 'Activation energy', 'Catalyst', 'Dynamic equilibrium', 'Equilibrium constant', 'Le Chatelier\'s principle', 'Brønsted–Lowry acid', 'pH', 'Ka'],
    'explanation': [
        'Reactions happen when particles collide with enough energy (the activation energy) and the right orientation. Rate increases with concentration, temperature, surface area and catalysts. A rate law such as rate = k[A]ᵐ[B]ⁿ is found from experiments, not from the balanced equation.',
        'Many reactions are reversible and reach dynamic equilibrium, where the forward and reverse rates are equal and concentrations stay constant. The equilibrium constant K expresses the position of equilibrium; it changes only with temperature. Le Chatelier\'s principle predicts how an equilibrium shifts when conditions change.',
        'Acids donate protons (H⁺) and bases accept them. pH = −log₁₀[H⁺] measures acidity on a logarithmic scale. Strong acids ionise completely; weak acids only partly, which is described by the acid dissociation constant Ka.'],
    'quick_facts': [
        'Rate = k[A]ᵐ[B]ⁿ; orders come from experiment.',
        'First-order half-life t½ = 0.693/k.',
        'For aA + bB ⇌ cC + dD: Kc = [C]ᶜ[D]ᵈ / ([A]ᵃ[B]ᵇ).',
        'Catalysts speed up both directions; they do not change K.',
        'pH = −log[H⁺]; pH + pOH = 14 at 25 °C.'],
}

NOTES = {
    T1: {
        'overview': 'Chemical kinetics studies how fast reactions go and why. Collision theory explains the factors that change rates, and rate laws describe them quantitatively.',
        'key_terms': ['Rate', 'Collision theory', 'Activation energy', 'Catalyst', 'Rate law', 'Order', 'Rate constant k', 'Half-life'],
        'explanation': [
            'Particles must collide with at least the activation energy Ea and the right orientation. Raising concentration or pressure increases collision frequency; raising temperature increases both frequency and, more importantly, the fraction of collisions with enough energy; a larger surface area exposes more particles; a catalyst provides a route with lower Ea.',
            'The rate law rate = k[A]ᵐ[B]ⁿ must be determined experimentally. If doubling [A] doubles the rate, the reaction is first order in A; if it quadruples the rate, second order; if the rate does not change, zero order. The overall order is m + n.',
            'For a first-order reaction the half-life t½ = 0.693/k is constant, independent of concentration. Radioactive decay and many drug-elimination processes are first order.'],
        'formulas_label': 'Formulas',
        'formulas': ['rate = k[A]ᵐ[B]ⁿ', 'Overall order = m + n', 'First order: t½ = ln 2 / k ≈ 0.693/k', 'Doubling [A]: rate × 2ᵐ'],
        'steps': ['Compare experiments where only one concentration changes.', 'Find the factor change in rate.', 'Deduce the order (factor = (concentration factor)^order).', 'Write the rate law and find k.'],
        'worked_example': {
            'problem': 'rate = k[A]²[B]. What happens to the rate if [A] is doubled and [B] is tripled?',
            'steps': ['Doubling [A] multiplies the rate by 2² = 4.', 'Tripling [B] multiplies it by 3¹ = 3.', 'Total factor = 4 × 3 = 12.'],
            'answer': 'The rate increases 12-fold.',
            'check': 'The overall order is 3, and the factors multiply because the rate law is a product ✓.'},
        'mistakes': ['Taking orders from the balanced-equation coefficients.', 'Thinking a catalyst is used up.', 'Saying temperature only increases collision frequency (the energy effect matters more).', 'Using t½ = 0.693/k for reactions that are not first order.'],
        'real_world': 'Refrigeration slows the reactions that spoil food, and catalytic converters in cars speed up reactions that turn toxic exhaust gases into less harmful ones.',
        'exam_strategy': 'When deducing orders, show the pair of experiments you compare and the factor change in both concentration and rate.',
        'recap': ['Collision theory: energy and orientation.', 'Rate laws come from experiment.', 'Doubling and factor rules.', 'First-order half-life is constant.']},
    T2: {
        'overview': 'In a reversible reaction at equilibrium, forward and reverse reactions continue at equal rates. The equilibrium constant describes where the equilibrium lies.',
        'key_terms': ['Reversible reaction', 'Dynamic equilibrium', 'Equilibrium constant Kc', 'Reaction quotient Q', 'Position of equilibrium', 'Homogeneous'],
        'explanation': [
            'At dynamic equilibrium, concentrations are constant (not necessarily equal) because the forward and reverse rates are equal. It is reached in a closed system from either direction.',
            'For aA + bB ⇌ cC + dD, Kc = [C]ᶜ[D]ᵈ / ([A]ᵃ[B]ᵇ), using equilibrium concentrations. Pure solids and liquids are left out. A large K (much greater than 1) means products dominate; a small K means reactants dominate.',
            'The reaction quotient Q has the same form but uses current concentrations. If Q < K the reaction moves forward; if Q > K it moves backward; if Q = K it is at equilibrium. K depends only on temperature.'],
        'formulas_label': 'Formulas',
        'formulas': ['Kc = [C]ᶜ[D]ᵈ / ([A]ᵃ[B]ᵇ)', 'Q < K: forward; Q > K: reverse; Q = K: at equilibrium', 'Leave out pure solids and liquids', 'K changes only with temperature'],
        'steps': ['Write the Kc expression from the balanced equation.', 'Substitute equilibrium concentrations.', 'Calculate K (or Q).', 'Interpret its size or compare Q with K.'],
        'worked_example': {
            'problem': 'For H₂ + I₂ ⇌ 2HI at equilibrium, [H₂] = 0.10, [I₂] = 0.10 and [HI] = 0.70 mol/L. Find Kc.',
            'steps': ['Kc = [HI]² / ([H₂][I₂]).', 'Kc = 0.70² / (0.10 × 0.10) = 0.49 / 0.010.', 'Kc = 49.'],
            'answer': 'Kc = 49: the products are favoured.',
            'check': 'There is much more HI than H₂ or I₂, consistent with K > 1 ✓.'},
        'mistakes': ['Forgetting to raise concentrations to their coefficients.', 'Putting reactants on top.', 'Including solids or pure liquids.', 'Thinking equilibrium means equal concentrations.'],
        'real_world': 'The oxygen carried by haemoglobin depends on an equilibrium: high oxygen pressure in the lungs drives binding, low pressure in tissues drives release.',
        'exam_strategy': 'Write the Kc expression before substituting numbers; examiners often give a mark for the expression alone.',
        'recap': ['Dynamic: equal rates, constant concentrations.', 'Kc from the balanced equation.', 'Q vs K predicts the direction.', 'K depends only on T.']},
    T3: {
        'overview': 'Le Chatelier\'s principle: if a system at equilibrium is disturbed, it shifts to oppose the change. It predicts the effects of concentration, pressure and temperature.',
        'key_terms': ['Le Chatelier\'s principle', 'Concentration change', 'Pressure change', 'Temperature change', 'Catalyst', 'Haber process'],
        'explanation': [
            'Adding a reactant shifts the equilibrium to the right to use it up; removing a product also shifts it right. Increasing pressure (by compressing) shifts it towards the side with fewer gas moles.',
            'Temperature is different: it changes K itself. Raising the temperature favours the endothermic direction. For an exothermic forward reaction, heating shifts the equilibrium left and lowers K.',
            'Catalysts speed up the forward and reverse reactions equally, so equilibrium is reached faster but its position and K are unchanged. Industry balances yield against rate: the Haber process (N₂ + 3H₂ ⇌ 2NH₃, exothermic) uses high pressure and an iron catalyst at a compromise temperature of about 400–450 °C.'],
        'formulas_label': 'Effects',
        'formulas': ['Add reactant / remove product: shift right', 'Higher pressure: towards fewer gas moles', 'Higher temperature: towards the endothermic side (K changes)', 'Catalyst: faster to equilibrium; position unchanged'],
        'steps': ['Identify the change.', 'Decide which shift opposes it.', 'For temperature, check whether the forward reaction is exo- or endothermic.', 'State the effect on yield and on K.'],
        'worked_example': {
            'problem': 'N₂ + 3H₂ ⇌ 2NH₃, ΔH = −92 kJ/mol. Predict the effect on the yield of ammonia of (a) higher pressure and (b) higher temperature.',
            'steps': ['(a) Left side has 4 gas moles, right side 2: higher pressure shifts right, increasing the yield.', '(b) The forward reaction is exothermic, so heating favours the reverse reaction.', 'Yield decreases and K becomes smaller at the higher temperature.'],
            'answer': 'Higher pressure increases the yield; higher temperature decreases it (but speeds up the reaction).',
            'check': 'This is why the Haber process uses a compromise temperature with a catalyst.'},
        'mistakes': ['Saying a catalyst increases the yield.', 'Saying a pressure change alters K.', 'Ignoring whether the reaction is exothermic when temperature changes.', 'Counting solids in the gas-mole comparison.'],
        'real_world': 'Ammonia from the Haber process makes the fertilisers that feed roughly half the world\'s population; its conditions are a textbook Le Chatelier compromise.',
        'exam_strategy': 'Always state the direction of shift, the reason in terms of opposing the change, and the effect on yield. Three short statements earn the full marks.',
        'recap': ['The system opposes the change.', 'Pressure: towards fewer gas moles.', 'Temperature changes K.', 'Catalysts do not shift equilibrium.']},
    T4: {
        'overview': 'Acids donate protons and bases accept them. pH measures how acidic a solution is, and Ka describes how strongly a weak acid ionises.',
        'key_terms': ['Brønsted–Lowry acid', 'Base', 'Conjugate pair', 'Strong acid', 'Weak acid', 'pH', 'Kw', 'Ka', 'Neutralisation'],
        'explanation': [
            'In the Brønsted–Lowry definition, an acid is a proton (H⁺) donor and a base a proton acceptor. When an acid gives up a proton it becomes its conjugate base: HCl/Cl⁻ and NH₄⁺/NH₃ are conjugate pairs.',
            'pH = −log₁₀[H⁺]. Each pH unit is a tenfold change in [H⁺]. Water ionises slightly: Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴ at 25 °C, so pH + pOH = 14 and neutral water has pH 7. 0.0010 mol/L HCl (a strong acid) has pH 3; 0.010 mol/L NaOH has pOH 2 and pH 12.',
            'Weak acids such as ethanoic acid ionise only partly: Ka = [H⁺][A⁻]/[HA]. For a weak acid of concentration c, [H⁺] ≈ √(Ka × c). With Ka = 1.8 × 10⁻⁵ and c = 0.10 mol/L, [H⁺] ≈ 1.34 × 10⁻³ and pH ≈ 2.87, much higher than a strong acid of the same concentration (pH 1).'],
        'formulas_label': 'Formulas',
        'formulas': ['pH = −log[H⁺]; [H⁺] = 10⁻ᵖᴴ', 'Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴ (25 °C)', 'pH + pOH = 14', 'Weak acid: [H⁺] ≈ √(Ka × c)', 'Strong acid: [H⁺] = acid concentration (monoprotic)'],
        'steps': ['Decide whether the acid or base is strong or weak.', 'Find [H⁺] (or [OH⁻]).', 'Take −log to get pH (or pOH, then 14 − pOH).', 'Check the answer is sensible (acid < 7, base > 7).'],
        'worked_example': {
            'problem': 'Find the pH of 0.10 mol/L ethanoic acid (Ka = 1.8 × 10⁻⁵).',
            'steps': ['[H⁺] ≈ √(1.8 × 10⁻⁵ × 0.10) = √(1.8 × 10⁻⁶).', '[H⁺] ≈ 1.34 × 10⁻³ mol/L.', 'pH = −log(1.34 × 10⁻³) ≈ 2.87.'],
            'answer': 'pH ≈ 2.87.',
            'check': 'Only about 1.3% of the acid has ionised, which is why the pH is well above 1 ✓.'},
        'mistakes': ['Treating a weak acid as fully ionised.', 'Forgetting the minus sign in pH = −log[H⁺].', 'Thinking pH 4 is twice as acidic as pH 5 (it is ten times).', 'Using pH + pOH = 14 at temperatures other than 25 °C without comment.'],
        'real_world': 'Farmers test soil pH because crops absorb nutrients best in a narrow pH range; lime (a base) is added to acidic soils, which are common in parts of tropical Africa.',
        'exam_strategy': 'Give pH values to two decimal places and show [H⁺] on the line before. For weak acids, state the approximation you used.',
        'recap': ['Acids donate H⁺; bases accept H⁺.', 'pH = −log[H⁺]; logarithmic scale.', 'Kw = 10⁻¹⁴; pH + pOH = 14.', 'Weak acids: [H⁺] ≈ √(Ka·c).']},
}

QUESTIONS = [
    # T1
    Q(T1, 'rate = k[A]²[B]. If [A] doubles and [B] triples, the rate increases by a factor of:', ['12', '6', '5', '18'], 0, '2² × 3.', ans=12),
    Q(T1, 'Doubling [A] doubles the rate. The reaction is ___ order in A.', ['first', 'zero', 'second', 'third'], 0, '2¹ = 2.'),
    Q(T1, 'A first-order reaction has k = 0.0231 s⁻¹. Its half-life, to 1 d.p., is:', ['30.0 s', '0.0231 s', '43.3 s', '15.0 s'], 0, '0.693 ÷ 0.0231.'),
    Q(T1, 'A catalyst increases the rate by:', ['providing a route with lower activation energy', 'increasing the temperature', 'being used up', 'raising the activation energy'], 0, 'More collisions have enough energy.'),
    Q(T1, 'Raising the temperature speeds up reactions mainly because:', ['more collisions have energy above Ea', 'particles get bigger', 'Ea falls', 'the equilibrium shifts'], 0, 'The energy distribution shifts.'),
    Q(T1, 'The order of a reaction with respect to a reactant is found:', ['from experiments', 'from the balanced equation', 'from the molar mass', 'from ΔH'], 0, 'Coefficients do not give orders in general.'),
    # T2
    Q(T2, 'H₂ + I₂ ⇌ 2HI with [H₂] = [I₂] = 0.10 and [HI] = 0.70 mol/L. Kc is:', ['49', '7', '0.020', '70'], 0, '0.70²/(0.10 × 0.10).', ans=49),
    Q(T2, 'At dynamic equilibrium:', ['forward and reverse rates are equal', 'reactions have stopped', 'concentrations of reactants and products are equal', 'K = 1'], 0, 'Concentrations are constant, not necessarily equal.'),
    Q(T2, 'A very large K means at equilibrium:', ['products are favoured', 'reactants are favoured', 'the reaction is fast', 'nothing happens'], 0, 'The numerator dominates.'),
    Q(T2, 'If Q < K, the reaction will:', ['proceed forward', 'proceed in reverse', 'stay as it is', 'stop'], 0, 'More products are needed to reach K.'),
    Q(T2, 'For CaCO₃(s) ⇌ CaO(s) + CO₂(g), Kc equals:', ['[CO₂]', '[CaO][CO₂]/[CaCO₃]', '[CaCO₃]/[CaO]', '1'], 0, 'Pure solids are left out.'),
    Q(T2, 'The value of K changes only when:', ['the temperature changes', 'a catalyst is added', 'the pressure changes', 'a reactant is added'], 0, 'K is temperature-dependent.'),
    # T3
    Q(T3, 'For N₂ + 3H₂ ⇌ 2NH₃, increasing pressure:', ['shifts equilibrium right', 'shifts it left', 'has no effect', 'changes K'], 0, '4 gas moles become 2.'),
    Q(T3, 'For an exothermic forward reaction, raising the temperature:', ['shifts equilibrium left and lowers K', 'shifts it right', 'increases K', 'has no effect'], 0, 'Heat favours the endothermic reverse reaction.'),
    Q(T3, 'Adding a catalyst to a system at equilibrium:', ['does not change the position of equilibrium', 'increases the yield', 'shifts it left', 'increases K'], 0, 'It speeds both directions equally.'),
    Q(T3, 'Removing a product from an equilibrium mixture:', ['shifts equilibrium right', 'shifts it left', 'changes K', 'stops the reaction'], 0, 'The system replaces the product.'),
    Q(T3, 'For H₂ + I₂ ⇌ 2HI (all gases), increasing pressure:', ['has no effect on position', 'shifts it right', 'shifts it left', 'doubles K'], 0, 'Both sides have 2 gas moles.'),
    Q(T3, 'The Haber process uses about 450 °C rather than a low temperature because:', ['the rate would be too slow at low temperature', 'yield is higher when hot', 'K increases with temperature', 'iron melts at low temperature'], 0, 'It is a compromise between yield and rate.'),
    # T4
    Q(T4, 'The pH of 0.0010 mol/L HCl is:', ['3', '0.001', '11', '−3'], 0, '−log(1.0 × 10⁻³).', ans=3),
    Q(T4, 'The pH of 0.010 mol/L NaOH at 25 °C is:', ['12', '2', '10', '14'], 0, 'pOH = 2, so pH = 14 − 2.', ans=12),
    Q(T4, 'The pH of 0.10 mol/L ethanoic acid (Ka = 1.8 × 10⁻⁵), to 2 d.p., is:', ['2.87', '1.00', '4.74', '5.74'], 0, '[H⁺] ≈ √(1.8 × 10⁻⁶) = 1.34 × 10⁻³.', ans=r(pH(h), 2)),
    Q(T4, 'The conjugate base of NH₄⁺ is:', ['NH₃', 'NH₂⁻', 'OH⁻', 'H⁺'], 0, 'NH₄⁺ loses a proton.'),
    Q(T4, 'Compared with pH 5, a solution of pH 3 has [H⁺]:', ['100 times higher', '2 times higher', '100 times lower', 'the same'], 0, 'Each unit is a factor of 10.'),
    Q(T4, '[H⁺] = 2.5 × 10⁻⁴ mol/L. The pH, to 2 d.p., is:', ['3.60', '4.00', '2.50', '3.40'], 0, '−log(2.5 × 10⁻⁴).', ans=r(pH(2.5e-4), 2)),
]

FLASH = [
    ['Rate law', 'rate = k[A]ᵐ[B]ⁿ; orders found by experiment.'],
    ['First-order half-life', 't½ = 0.693/k, independent of concentration.'],
    ['Catalyst', 'Lowers activation energy; not used up; does not change K.'],
    ['Kc expression', '[products]^coefficients ÷ [reactants]^coefficients.'],
    ['Q vs K', 'Q < K forward; Q > K reverse.'],
    ['Le Chatelier', 'Equilibrium shifts to oppose a change.'],
    ['pH', 'pH = −log[H⁺]; pH + pOH = 14 at 25 °C.'],
    ['Weak acid pH', '[H⁺] ≈ √(Ka × c).'],
]
