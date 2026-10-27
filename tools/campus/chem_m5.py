"""General Chemistry, module 5: Thermodynamics, redox and an introduction to organic chemistry."""
from verify import Q
from chem_common import r
T1, T2, T3, T4 = ('Entropy and Gibbs free energy', 'Redox and oxidation numbers', 'Electrochemical cells', 'Introduction to organic chemistry')

dG = -92.2 - 298 * (-198.8 / 1000)
assert r(dG, 1) == -33.0 and r(92.2 / 0.1988, 0) == 464
ox = {'KMnO4': (+1) * -1 + 4 * 2, 'Cr2O7': (-2 + 7 * 2) / 2, 'H2SO4': 4 * 2 - 2 * 1}
assert ox == {'KMnO4': 7, 'Cr2O7': 6.0, 'H2SO4': 6}
E = 0.34 - (-0.76)
assert r(E, 2) == 1.10 and r(-2 * 96485 * E / 1000, 0) == -212
assert r(0.80 - 0.34, 2) == 0.46

MODULE = {
    'title': 'Thermodynamics, redox and organic chemistry',
    'topics': [T1, T2, T3, T4],
    'overview': 'Why do some reactions happen on their own while others need a push? This module answers with entropy and Gibbs free energy, then turns to redox reactions and the electrochemical cells that power batteries and corrode bridges, and ends with an introduction to organic chemistry, the chemistry of carbon compounds.',
    'key_terms': ['Entropy', 'Spontaneous', 'Gibbs free energy', 'Oxidation', 'Reduction', 'Oxidation number', 'Standard electrode potential', 'Galvanic cell', 'Functional group', 'Homologous series', 'Isomer'],
    'explanation': [
        'A spontaneous process happens without continuous outside help. Spontaneity depends on both enthalpy and entropy (a measure of how spread out energy and matter are), combined in the Gibbs free energy: ΔG = ΔH − TΔS. A negative ΔG means the reaction is thermodynamically favourable.',
        'Redox reactions transfer electrons: oxidation is loss of electrons and reduction is gain (OIL RIG). Oxidation numbers track electron transfer. In a galvanic cell, a spontaneous redox reaction is split into two half-cells so the electron flow can do useful work as an electric current.',
        'Organic chemistry studies carbon compounds, which form chains and rings with a huge variety of structures. Compounds are organised into homologous series with the same functional group, which decides their reactions.'],
    'quick_facts': [
        'ΔG = ΔH − TΔS; spontaneous if ΔG < 0.',
        'OIL RIG: Oxidation Is Loss, Reduction Is Gain (of electrons).',
        'E°cell = E°(cathode) − E°(anode); positive means spontaneous.',
        'ΔG° = −nFE°cell, F = 96 485 C/mol.',
        'Alkanes CₙH₂ₙ₊₂; alkenes CₙH₂ₙ contain C=C.'],
}

NOTES = {
    T1: {
        'overview': 'Whether a reaction can happen on its own depends on enthalpy and entropy together. Gibbs free energy combines them into one test.',
        'key_terms': ['Entropy S', 'Second law of thermodynamics', 'Spontaneous process', 'Gibbs free energy G', 'ΔG = ΔH − TΔS', 'Feasibility temperature'],
        'explanation': [
            'Entropy measures the dispersal of energy and matter. It increases from solid to liquid to gas, when more gas molecules are produced, when substances dissolve, and as temperature rises. The second law says the total entropy of the universe increases in any spontaneous process.',
            'ΔG = ΔH − TΔS (with T in kelvin and ΔS converted to kJ when ΔH is in kJ). A reaction is spontaneous when ΔG < 0. Exothermic reactions with increasing entropy are always spontaneous; endothermic reactions with decreasing entropy never are; the other two cases depend on temperature.',
            'For ammonia synthesis, ΔH = −92.2 kJ and ΔS = −198.8 J/K. At 298 K, ΔG = −92.2 − 298(−0.1988) = −33.0 kJ: favourable. Above T = ΔH/ΔS ≈ 464 K, ΔG becomes positive. Note that a negative ΔG says nothing about speed: diamond turning into graphite is favourable but immeasurably slow.'],
        'formulas_label': 'Formulas',
        'formulas': ['ΔG = ΔH − TΔS', 'Spontaneous if ΔG < 0', 'Feasibility switch at T = ΔH/ΔS', 'Convert ΔS from J/K to kJ/K'],
        'steps': ['Note the signs of ΔH and ΔS.', 'Convert ΔS to kJ/K.', 'Substitute T in kelvin.', 'Decide spontaneity from the sign of ΔG.', 'Find the switch temperature if asked.'],
        'worked_example': {
            'problem': 'For N₂ + 3H₂ → 2NH₃, ΔH = −92.2 kJ and ΔS = −198.8 J/K. Is it spontaneous at 298 K? Above what temperature does it stop being spontaneous?',
            'steps': ['ΔG = −92.2 − 298 × (−0.1988) = −92.2 + 59.2 = −33.0 kJ.', 'ΔG < 0, so it is spontaneous at 298 K.', 'ΔG = 0 when T = 92.2 / 0.1988 ≈ 464 K.'],
            'answer': 'Spontaneous at 298 K (ΔG ≈ −33.0 kJ); not spontaneous above about 464 K.',
            'check': 'With negative ΔH and negative ΔS, low temperatures favour the reaction ✓.'},
        'mistakes': ['Forgetting to convert ΔS from J to kJ.', 'Using °C instead of K.', 'Thinking a spontaneous reaction must be fast.', 'Thinking all exothermic reactions are spontaneous at all temperatures.'],
        'real_world': 'Ice melts on its own above 0 °C even though melting is endothermic, because the entropy gain (TΔS) outweighs ΔH at those temperatures.',
        'exam_strategy': 'Show the unit conversion of ΔS explicitly. It is the single most common error in Gibbs energy questions.',
        'recap': ['Entropy: dispersal of energy and matter.', 'ΔG = ΔH − TΔS.', 'ΔG < 0: spontaneous.', 'Spontaneous ≠ fast.']},
    T2: {
        'overview': 'Redox reactions involve the transfer of electrons. Oxidation numbers make it easy to see which species is oxidised and which is reduced.',
        'key_terms': ['Oxidation', 'Reduction', 'Oxidising agent', 'Reducing agent', 'Oxidation number', 'Half-equation', 'Disproportionation'],
        'explanation': [
            'Oxidation is loss of electrons (or increase in oxidation number); reduction is gain of electrons (decrease in oxidation number). OIL RIG helps remember it. The oxidising agent is the species that is reduced; the reducing agent is oxidised.',
            'Oxidation number rules: elements are 0; monatomic ions equal their charge; oxygen is usually −2 (−1 in peroxides); hydrogen is usually +1 (−1 in metal hydrides); the numbers in a neutral compound add to 0, and in an ion to its charge. In KMnO₄, Mn is +7; in Cr₂O₇²⁻, Cr is +6; in H₂SO₄, S is +6.',
            'Redox equations can be built from half-equations: balance the atoms, balance oxygen with H₂O and hydrogen with H⁺ (in acid), then balance charge with electrons, and combine so electrons cancel. For example, Zn → Zn²⁺ + 2e⁻ and Cu²⁺ + 2e⁻ → Cu combine to Zn + Cu²⁺ → Zn²⁺ + Cu.'],
        'formulas_label': 'Rules',
        'formulas': ['Oxidation: loss of e⁻, oxidation number ↑', 'Reduction: gain of e⁻, oxidation number ↓', 'O usually −2; H usually +1; elements 0', 'Sum of oxidation numbers = overall charge'],
        'steps': ['Assign oxidation numbers to every atom.', 'Find which increase (oxidised) and decrease (reduced).', 'Name the oxidising and reducing agents.', 'Write and combine half-equations.'],
        'worked_example': {
            'problem': 'Find the oxidation number of Mn in KMnO₄.',
            'steps': ['K is +1 and each O is −2, so oxygen totals −8.', 'The compound is neutral: +1 + Mn + (−8) = 0.', 'Mn = +7.'],
            'answer': 'Mn is +7.',
            'check': 'Permanganate is a strong oxidising agent precisely because Mn is in such a high oxidation state ✓.'},
        'mistakes': ['Confusing the oxidising agent with the substance oxidised.', 'Forgetting that an ion\'s oxidation numbers add to its charge.', 'Unbalanced charge in half-equations.', 'Treating oxidation number as a real charge in covalent compounds.'],
        'real_world': 'Rusting is the oxidation of iron by oxygen; galvanising coats iron with zinc, which is oxidised first and so protects the iron underneath.',
        'exam_strategy': 'Write oxidation numbers above each element in the equation. Changes are then easy to see and to explain.',
        'recap': ['OIL RIG.', 'Oxidation number rules.', 'Oxidising agent is reduced.', 'Balance half-equations by atoms, then charge.']},
    T3: {
        'overview': 'An electrochemical (galvanic) cell turns a spontaneous redox reaction into electrical energy. Standard electrode potentials predict the cell voltage and which way electrons flow.',
        'key_terms': ['Galvanic cell', 'Anode', 'Cathode', 'Salt bridge', 'Standard electrode potential E°', 'Cell potential', 'Electrolysis'],
        'explanation': [
            'Each half-cell has a standard electrode potential E° measured against the standard hydrogen electrode (0 V). The more positive E°, the stronger the tendency to be reduced. In a cell, the half-cell with the more positive E° is the cathode (reduction) and the other is the anode (oxidation).',
            'E°cell = E°(cathode) − E°(anode). For a zinc–copper (Daniell) cell, E°(Cu²⁺/Cu) = +0.34 V and E°(Zn²⁺/Zn) = −0.76 V, so E°cell = 0.34 − (−0.76) = 1.10 V. Electrons flow through the wire from zinc to copper; the salt bridge lets ions move to keep the solutions neutral.',
            'A positive E°cell means the reaction is spontaneous, linked to free energy by ΔG° = −nFE°cell (F = 96 485 C/mol). For the Daniell cell, n = 2 and ΔG° ≈ −212 kJ. Electrolysis is the reverse: an external voltage drives a non-spontaneous reaction, used to extract aluminium and to electroplate metals.'],
        'formulas_label': 'Formulas',
        'formulas': ['E°cell = E°cathode − E°anode', 'Anode: oxidation; cathode: reduction', 'ΔG° = −nFE°cell', 'F = 96 485 C/mol'],
        'steps': ['Look up the two standard potentials.', 'The more positive one is the cathode.', 'E°cell = cathode − anode.', 'Write the overall equation and electron flow direction.', 'Find ΔG° if asked.'],
        'worked_example': {
            'problem': 'For a cell with Zn²⁺/Zn (−0.76 V) and Cu²⁺/Cu (+0.34 V), find E°cell and ΔG°.',
            'steps': ['Copper has the more positive E°, so it is the cathode; zinc is the anode.', 'E°cell = 0.34 − (−0.76) = 1.10 V.', 'ΔG° = −2 × 96 485 × 1.10 J ≈ −212 kJ.'],
            'answer': 'E°cell = 1.10 V; ΔG° ≈ −212 kJ: spontaneous.',
            'check': 'Zinc metal really does push copper out of copper sulfate solution, as this predicts ✓.'},
        'mistakes': ['Adding potentials instead of subtracting.', 'Reversing the sign of E° when it is already used in the subtraction formula.', 'Mixing up anode and cathode.', 'Multiplying E° by stoichiometric coefficients.'],
        'real_world': 'Lithium-ion batteries in phones and the zinc–carbon cells in torches are galvanic cells; recharging a battery is electrolysis.',
        'exam_strategy': 'Label anode, cathode, electron flow and salt bridge on a diagram. Diagram labels are a reliable source of marks.',
        'recap': ['More positive E°: cathode.', 'E°cell = cathode − anode.', 'Positive E°cell: spontaneous.', 'ΔG° = −nFE°.']},
    T4: {
        'overview': 'Organic chemistry is the chemistry of carbon compounds. Carbon\'s four bonds and ability to form chains and rings create millions of compounds, organised into families with the same functional group.',
        'key_terms': ['Hydrocarbon', 'Alkane', 'Alkene', 'Functional group', 'Homologous series', 'IUPAC naming', 'Structural isomer', 'Addition reaction'],
        'explanation': [
            'Alkanes (CₙH₂ₙ₊₂) such as methane, ethane and propane have only single bonds and are fairly unreactive apart from burning. Alkenes (CₙH₂ₙ), such as ethene, contain a C=C double bond and undergo addition reactions; they decolourise bromine water, a simple test for unsaturation.',
            'Functional groups decide reactions: alcohols (–OH, e.g. ethanol), carboxylic acids (–COOH, e.g. ethanoic acid), esters (–COO–), amines (–NH₂) and halogenoalkanes (–Cl, –Br). A homologous series has the same functional group and differs by CH₂ each step, with gradually changing physical properties.',
            'IUPAC names show chain length (meth-, eth-, prop-, but-, pent- for 1 to 5 carbons) and functional group (-ane, -ene, -ol, -oic acid). Structural isomers have the same molecular formula but different structures: C₄H₁₀ has two (butane and 2-methylpropane).'],
        'formulas_label': 'Key facts',
        'formulas': ['Alkanes CₙH₂ₙ₊₂; alkenes CₙH₂ₙ', 'Prefixes: meth 1, eth 2, prop 3, but 4, pent 5', 'Suffixes: -ane, -ene, -ol, -oic acid', 'Bromine water: orange → colourless with alkenes'],
        'steps': ['Find the longest carbon chain.', 'Identify the functional group.', 'Number the chain to give the group the lowest number.', 'Combine prefix, position and suffix.'],
        'worked_example': {
            'problem': 'Name CH₃CH₂CH₂OH and give the molecular formula of the alkane with 5 carbons.',
            'steps': ['The chain has 3 carbons (prop-) and an –OH group on carbon 1.', 'Name: propan-1-ol.', 'Alkane with n = 5: CₙH₂ₙ₊₂ gives C₅H₁₂ (pentane).'],
            'answer': 'Propan-1-ol; pentane is C₅H₁₂.',
            'check': 'C₅H₁₂ fits CₙH₂ₙ₊₂ with n = 5 ✓.'},
        'mistakes': ['Counting a branch as part of the longest chain.', 'Forgetting the position number of the functional group.', 'Writing alkenes as CₙH₂ₙ₊₂.', 'Thinking isomers have different molecular formulas.'],
        'real_world': 'Plastics such as polythene are made by joining thousands of ethene molecules (addition polymerisation); medicines, fuels, dyes and fibres are all organic compounds.',
        'exam_strategy': 'Draw the structure before naming or after naming to check. Branching and numbering mistakes show up immediately in a drawing.',
        'recap': ['Alkanes single bonds; alkenes C=C.', 'Functional groups decide reactions.', 'IUPAC: chain + position + group.', 'Isomers: same formula, different structure.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'ΔH = −92.2 kJ, ΔS = −198.8 J/K, T = 298 K. ΔG, to 1 d.p., is:', ['−33.0 kJ', '−151.4 kJ', '+33.0 kJ', '59.2 kJ'], 0, '−92.2 − 298(−0.1988).'),
    Q(T1, 'Above what temperature does that reaction stop being spontaneous (nearest K)?', ['464 K', '298 K', '273 K', '1000 K'], 0, 'T = 92.2/0.1988.', ans=464),
    Q(T1, 'A reaction is always spontaneous if:', ['ΔH < 0 and ΔS > 0', 'ΔH > 0 and ΔS < 0', 'ΔH > 0 and ΔS > 0', 'ΔH < 0 and ΔS < 0'], 0, 'Then ΔG is negative at every temperature.'),
    Q(T1, 'Which change increases entropy?', ['A solid dissolving in water', 'A gas condensing', 'Water freezing', 'Gas molecules combining into fewer molecules'], 0, 'Particles become more dispersed.'),
    Q(T1, 'A negative ΔG tells us a reaction is:', ['thermodynamically favourable but not necessarily fast', 'always fast', 'endothermic', 'at equilibrium'], 0, 'Rate is a kinetic question.'),
    Q(T1, 'In ΔG = ΔH − TΔS, T must be in:', ['kelvin', 'degrees Celsius', 'any unit', 'joules'], 0, 'Absolute temperature.'),
    # T2
    Q(T2, 'The oxidation number of Mn in KMnO₄ is:', ['+7', '+2', '+4', '−1'], 0, '+1 + Mn − 8 = 0.', ans=7),
    Q(T2, 'The oxidation number of Cr in Cr₂O₇²⁻ is:', ['+6', '+7', '+3', '+12'], 0, '2Cr − 14 = −2.', ans=6),
    Q(T2, 'The oxidation number of S in H₂SO₄ is:', ['+6', '+4', '−2', '+2'], 0, '2 + S − 8 = 0.', ans=6),
    Q(T2, 'In Zn + Cu²⁺ → Zn²⁺ + Cu, zinc is:', ['oxidised (the reducing agent)', 'reduced', 'the oxidising agent', 'unchanged'], 0, 'Zn loses 2 electrons.'),
    Q(T2, 'Reduction is:', ['gain of electrons', 'loss of electrons', 'gain of oxygen', 'loss of hydrogen ions'], 0, 'RIG.'),
    Q(T2, 'The oxidising agent in a reaction is the species that is:', ['reduced', 'oxidised', 'unchanged', 'a catalyst'], 0, 'It takes electrons from the other species.'),
    # T3
    Q(T3, 'E°(Cu²⁺/Cu) = +0.34 V and E°(Zn²⁺/Zn) = −0.76 V. E°cell is:', ['1.10 V', '0.42 V', '−1.10 V', '0.26 V'], 0, '0.34 − (−0.76).'),
    Q(T3, 'In that cell, the anode is:', ['zinc', 'copper', 'the salt bridge', 'the wire'], 0, 'Oxidation happens at the more negative electrode.'),
    Q(T3, 'For that cell (n = 2), ΔG° is about:', ['−212 kJ', '+212 kJ', '−106 kJ', '−1.10 kJ'], 0, '−2 × 96 485 × 1.10 J.', ans=-212),
    Q(T3, 'E°(Ag⁺/Ag) = +0.80 V and E°(Cu²⁺/Cu) = +0.34 V. E°cell is:', ['0.46 V', '1.14 V', '−0.46 V', '0.80 V'], 0, '0.80 − 0.34.'),
    Q(T3, 'The salt bridge in a galvanic cell:', ['allows ions to flow to keep the solutions neutral', 'carries electrons', 'stores energy', 'is the cathode'], 0, 'Electrons travel through the external wire.'),
    Q(T3, 'Electrolysis uses electrical energy to:', ['drive a non-spontaneous reaction', 'produce electricity', 'stop corrosion only', 'measure pH'], 0, 'It is the reverse of a galvanic cell.'),
    # T4
    Q(T4, 'The molecular formula of pentane is:', ['C₅H₁₂', 'C₅H₁₀', 'C₅H₈', 'C₄H₁₀'], 0, 'CₙH₂ₙ₊₂ with n = 5.'),
    Q(T4, 'Bromine water turns from orange to colourless with:', ['alkenes', 'alkanes', 'carboxylic acids', 'water'], 0, 'Addition across the C=C double bond.'),
    Q(T4, 'CH₃CH₂CH₂OH is named:', ['propan-1-ol', 'propanoic acid', 'propane', 'ethanol'], 0, '3 carbons, –OH on carbon 1.'),
    Q(T4, 'How many structural isomers does C₄H₁₀ have?', ['2', '1', '3', '4'], 0, 'Butane and 2-methylpropane.', ans=2),
    Q(T4, 'The functional group of a carboxylic acid is:', ['–COOH', '–OH', '–NH₂', 'C=C'], 0, 'For example ethanoic acid, CH₃COOH.'),
    Q(T4, 'Members of a homologous series differ by:', ['CH₂', 'CH₃', 'H₂', 'C₂H₄'], 0, 'Each member adds one CH₂ unit.'),
]

FLASH = [
    ['Gibbs free energy', 'ΔG = ΔH − TΔS; spontaneous if ΔG < 0.'],
    ['Entropy', 'Dispersal of energy and matter; rises solid → liquid → gas.'],
    ['OIL RIG', 'Oxidation Is Loss, Reduction Is Gain of electrons.'],
    ['Oxidation number rules', 'Elements 0; O usually −2; H usually +1; sum = charge.'],
    ['Cell potential', 'E°cell = E°cathode − E°anode.'],
    ['ΔG and E°', 'ΔG° = −nFE°cell.'],
    ['Alkanes and alkenes', 'CₙH₂ₙ₊₂ single bonds; CₙH₂ₙ with C=C.'],
    ['Structural isomers', 'Same molecular formula, different structures.'],
]
