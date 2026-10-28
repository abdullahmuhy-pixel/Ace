"""Organic Chemistry, module 4: Aromatic and carbonyl chemistry."""
import math
from verify import Q
from oc_common import mass, r
T1, T2, T3, T4 = ('Benzene and aromaticity', 'Electrophilic aromatic substitution', 'Aldehydes and ketones', 'Carboxylic acids and their derivatives')
huckel = lambda pi: pi % 4 == 2
assert huckel(6) and huckel(10) and huckel(2) and not huckel(4) and not huckel(8)
assert 3 * -120 - (-208) == -152
n_bz = 7.8 / mass('C6H6')
assert r(n_bz, 4) == 0.0999 and r(n_bz * mass('C6H5NO2'), 1) == 12.3 and r(9.8 / (n_bz * mass('C6H5NO2')) * 100, 0) == 80
assert r(mass('C4H10O'), 2) == 74.12 and r(mass('C4H8O2'), 2) == 88.10 and r(2 / 3 * mass('C4H8O2'), 1) == 58.7
x1 = 2 / 3; assert r(x1 ** 2 / (1 - x1) ** 2, 6) == 4
x3 = (16 - math.sqrt(256 - 144)) / 6; assert r(x3 ** 2 / ((1 - x3) * (3 - x3)), 6) == 4 and r(x3 * 100, 0) == 90

MODULE = {
    'title': 'Aromatic and carbonyl chemistry',
    'topics': [T1, T2, T3, T4],
    'overview': 'Two families dominate real-world organic chemistry: aromatic compounds built on benzene rings, and carbonyl compounds containing C=O. This module explains why benzene is unusually stable, how it substitutes rather than adds, how aldehydes and ketones undergo nucleophilic addition, and how carboxylic acids and their derivatives interconvert by nucleophilic acyl substitution.',
    'key_terms': ['Aromaticity', 'Hückel\'s rule', 'Delocalisation energy', 'Electrophilic aromatic substitution', 'Arenium ion', 'Directing group', 'Friedel–Crafts', 'Carbonyl group', 'Nucleophilic addition', 'Grignard reagent', 'Imine', 'Acyl chloride', 'Ester', 'Amide', 'Nucleophilic acyl substitution'],
    'explanation': [
        'Benzene is a flat ring of six sp² carbons whose six π electrons are delocalised all the way round. Cyclic, planar, conjugated rings with 4n + 2 π electrons (Hückel\'s rule) are aromatic and especially stable; benzene is about 152 kJ/mol more stable than three isolated C=C bonds would predict.',
        'Because addition would destroy that stability, benzene reacts with strong electrophiles by substitution: nitration, halogenation, sulfonation and Friedel–Crafts alkylation and acylation. Existing substituents control both rate and position: electron donors activate and direct ortho/para; electron-withdrawing groups deactivate and direct meta.',
        'The C=O bond is polar, with δ+ carbon. Aldehydes and ketones add nucleophiles (hydride, Grignard reagents, cyanide, amines). Carboxylic acid derivatives, which have a leaving group on the carbonyl carbon, instead undergo addition followed by elimination: acyl chlorides react fastest, then anhydrides, esters and amides.'],
    'quick_facts': [
        'Aromatic: cyclic, planar, conjugated, 4n + 2 π electrons.',
        'EAS: electrophile attacks, arenium ion, H⁺ lost.',
        'o/p directors: –OH, –NH₂, –CH₃, halogens; meta: –NO₂, –CHO, –COOH, –CN.',
        'Grignard + HCHO → 1°, + RCHO → 2°, + ketone → 3° alcohol.',
        'Reactivity: acyl chloride > anhydride > ester > amide.'],
}

NOTES = {
    T1: {
        'overview': 'Aromatic rings have delocalised π electrons that give extra stability and distinctive reactivity.',
        'key_terms': ['Kekulé structure', 'Delocalised π system', 'Resonance energy', 'Hückel\'s rule', 'Antiaromatic', 'Heterocycle', 'Pyridine', 'Pyrrole'],
        'explanation': [
            'All six C–C bonds in benzene are the same length (140 pm, between a single at 154 pm and a double at 134 pm), because the π electrons are shared over the whole ring rather than fixed in three double bonds. Kekulé structures are two resonance contributors to one real structure.',
            'Hydrogenating cyclohexene releases about 120 kJ/mol. Three isolated C=C would release 360 kJ/mol, but benzene releases only about 208 kJ/mol: it is about 152 kJ/mol more stable, its delocalisation (resonance) energy.',
            'Hückel\'s rule: a cyclic, planar, fully conjugated ring with 4n + 2 π electrons (2, 6, 10 …) is aromatic. Benzene (6) and naphthalene (10) qualify; cyclobutadiene (4) is antiaromatic and unstable. Heterocycles count lone pairs that are part of the π system: pyrrole\'s N lone pair makes 6; in pyridine the N lone pair lies in the ring plane and is not counted. The cyclopentadienyl anion, with 6 π electrons, is aromatic.'],
        'formulas_label': 'Rules',
        'formulas': ['Aromatic: 4n + 2 π electrons (n = 0, 1, 2 …)', 'Antiaromatic: 4n π electrons, planar and conjugated', 'Resonance energy ≈ 3 × 120 − 208 ≈ 152 kJ/mol'],
        'steps': ['Check the ring is cyclic and planar.', 'Check every ring atom has a p orbital (conjugated).', 'Count π electrons, including relevant lone pairs and charges.', 'Apply 4n + 2.'],
        'worked_example': {
            'problem': 'Is the cyclopentadienyl anion, C₅H₅⁻, aromatic?',
            'steps': ['Planar five-membered ring; the anionic carbon is sp² with its lone pair in a p orbital, so the ring is fully conjugated.', 'π electrons: two C=C (4) + the lone pair (2) = 6.', '6 = 4(1) + 2.'],
            'answer': 'Yes, it is aromatic (6 π electrons).',
            'check': 'This explains why cyclopentadiene (pKa about 16) is unusually acidic for a hydrocarbon ✓.'},
        'mistakes': ['Counting every lone pair (only those in the π system count).', 'Forgetting the planarity requirement.', 'Treating Kekulé structures as two different molecules.', 'Saying any ring with alternating double bonds is aromatic.'],
        'real_world': 'DNA bases (adenine, guanine, cytosine, thymine) are aromatic heterocycles; their flat rings stack inside the double helix.',
        'exam_strategy': 'Write the π electron count next to each ring; Hückel questions are then quick.',
        'recap': ['Delocalised π.', 'Equal bonds.', '152 kJ/mol stabilisation.', '4n + 2 rule.']},
    T2: {
        'overview': 'Benzene keeps its aromatic ring by substituting rather than adding. Substituents already on the ring control where and how fast new groups go.',
        'key_terms': ['Electrophile', 'Arenium (σ) complex', 'Nitration', 'Halogenation', 'Sulfonation', 'Friedel–Crafts alkylation', 'Friedel–Crafts acylation', 'Activating group', 'Deactivating group', 'Ortho/para and meta directors'],
        'explanation': [
            'Mechanism: a strong electrophile (E⁺) accepts π electrons, giving a resonance-stabilised arenium ion; loss of H⁺ restores the aromatic ring. Nitration uses HNO₃ and H₂SO₄ to make NO₂⁺; bromination needs Br₂ with FeBr₃; Friedel–Crafts acylation uses RCOCl with AlCl₃ and avoids the rearrangements and over-alkylation of Friedel–Crafts alkylation.',
            'Donor groups (–OH, –OCH₃, –NH₂, –CH₃) activate the ring and direct ortho/para, because they stabilise the positive charge when E⁺ adds at those positions. Withdrawing groups (–NO₂, –CN, –CHO, –COOH) deactivate the ring and direct meta. Halogens are the exception: they deactivate but direct ortho/para.',
            'Yields: nitrating 7.8 g of benzene (0.0999 mol) can give at most 12.3 g of nitrobenzene (123.11 g/mol); obtaining 9.8 g is about an 80% yield. A disubstituted benzene has three positional isomers: ortho (1,2), meta (1,3) and para (1,4).'],
        'formulas_label': 'Reagents',
        'formulas': ['Nitration: HNO₃/H₂SO₄ → NO₂⁺', 'Bromination: Br₂/FeBr₃', 'Acylation: RCOCl/AlCl₃', 'Sulfonation: SO₃/H₂SO₄'],
        'steps': ['Identify the electrophile and how it is generated.', 'Classify the existing substituent (activating/deactivating, o/p or m).', 'Predict the position.', 'For syntheses, order the steps so each group directs the next correctly.'],
        'worked_example': {
            'problem': 'Plan a synthesis of m-bromonitrobenzene from benzene.',
            'steps': ['Both groups must end up meta to each other.', '–NO₂ is a meta director; Br is ortho/para.', 'So nitrate first (HNO₃/H₂SO₄), then brominate (Br₂/FeBr₃).'],
            'answer': 'Nitration, then bromination.',
            'check': 'Brominating first would give mainly o- and p-bromonitrobenzene ✓.'},
        'mistakes': ['Drawing addition products for benzene.', 'Forgetting the Lewis acid catalyst.', 'Calling halogens meta directors.', 'Doing Friedel–Crafts on strongly deactivated rings (it fails).'],
        'real_world': 'Paracetamol and many dyes are made by sequences of aromatic substitutions on simple benzene derivatives.',
        'exam_strategy': 'In synthesis questions, decide the order of steps from the directing effects before writing any reagents.',
        'recap': ['Substitution keeps aromaticity.', 'Generate a strong E⁺.', 'Donors o/p, acceptors meta.', 'Order matters.']},
    T3: {
        'overview': 'Aldehydes and ketones react by nucleophilic addition to the electrophilic carbonyl carbon.',
        'key_terms': ['Carbonyl group', 'Nucleophilic addition', 'Hydride reduction', 'Grignard reagent', 'Cyanohydrin', 'Imine', 'Hemiacetal and acetal', 'Tollens\' test', '2,4-DNP test'],
        'explanation': [
            'The C=O carbon is δ+ and trigonal planar, so nucleophiles attack from either face. Aldehydes are more reactive than ketones because they have less steric hindrance and only one electron-donating alkyl group.',
            'NaBH₄ or LiAlH₄ reduce aldehydes to primary and ketones to secondary alcohols. Grignard reagents (RMgBr) add carbon: methanal gives primary alcohols, other aldehydes secondary, ketones tertiary. CH₃MgBr with propanone, then acid work-up, gives 2-methylpropan-2-ol (C₄H₁₀O, 74.12 g/mol). HCN adds to give cyanohydrins (a new stereocentre, formed as a racemate); primary amines give imines (C=N).',
            'Tests: 2,4-dinitrophenylhydrazine gives an orange precipitate with any aldehyde or ketone; Tollens\' reagent gives a silver mirror (and Fehling\'s a red precipitate) only with aldehydes, which are easily oxidised.'],
        'formulas_label': 'Rules',
        'formulas': ['NaBH₄: aldehyde → 1° alcohol; ketone → 2°', 'RMgBr + HCHO → 1°; + RCHO → 2°; + R₂CO → 3°', 'R₂C=O + R′NH₂ → R₂C=NR′ + H₂O', 'Tollens: aldehydes only'],
        'steps': ['Identify the nucleophile.', 'Draw attack at the carbonyl carbon, forming an alkoxide.', 'Protonate in the work-up.', 'Check the class of alcohol or other product.'],
        'worked_example': {
            'problem': 'Which carbonyl compound and Grignard reagent make butan-2-ol?',
            'steps': ['Butan-2-ol, CH₃CH(OH)CH₂CH₃, is a secondary alcohol, so start from an aldehyde.', 'Split one C–C bond to the carbinol carbon: ethanal + CH₃CH₂MgBr, or propanal + CH₃MgBr.', 'Add acid work-up after the Grignard step.'],
            'answer': 'Ethanal with ethylmagnesium bromide (or propanal with methylmagnesium bromide), then H₃O⁺.',
            'check': '2 + 2 = 4 carbons ✓; aldehyde + Grignard gives a 2° alcohol ✓.'},
        'mistakes': ['Using Grignard reagents in water or alcohol (they are destroyed).', 'Expecting ketones to give a positive Tollens\' test.', 'Forgetting the acid work-up.', 'Mixing up which carbonyl gives which class of alcohol.'],
        'real_world': 'Methanal (formaldehyde) solution preserves biological specimens by forming cross-links with proteins.',
        'exam_strategy': 'For Grignard synthesis questions, work backwards from the alcohol carbon and cut one bond to it.',
        'recap': ['δ+ carbonyl carbon.', 'Hydride and Grignard additions.', 'Imines and cyanohydrins.', 'Tollens for aldehydes.']},
    T4: {
        'overview': 'Carboxylic acids and their derivatives interconvert by nucleophilic acyl substitution. Their relative reactivity decides which conversions are easy.',
        'key_terms': ['Carboxylic acid', 'Acyl chloride', 'Acid anhydride', 'Ester', 'Amide', 'Nucleophilic acyl substitution', 'Tetrahedral intermediate', 'Fischer esterification', 'Saponification'],
        'explanation': [
            'Mechanism: the nucleophile adds to C=O, forming a tetrahedral intermediate, which collapses and expels the leaving group. The better the leaving group, the more reactive the derivative: acyl chloride (Cl⁻) > anhydride > ester > amide. Reactive derivatives can be turned into less reactive ones directly, not the reverse.',
            'Fischer esterification (acid + alcohol, H₂SO₄ catalyst) is an equilibrium with K ≈ 4 for ethanoic acid and ethanol. Starting with 1 mol of each, x²/(1 − x)² = 4 gives x = 2/3 mol of ester (about 58.7 g of ethyl ethanoate, 88.10 g/mol). Using 3 mol of ethanol pushes the yield to about 0.90 mol (Le Chatelier).',
            'Esters are hydrolysed by acid (reversible) or by base (saponification, irreversible because the carboxylate is formed): this is how soap is made from fats. Amides are very stable, which is why proteins, held together by amide (peptide) bonds, last.'],
        'formulas_label': 'Rules',
        'formulas': ['Reactivity: RCOCl > (RCO)₂O > RCOOR′ > RCONH₂', 'RCOOH + R′OH ⇌ RCOOR′ + H₂O, K ≈ 4', 'RCOOR′ + OH⁻ → RCOO⁻ + R′OH', 'RCOCl + NH₃ → RCONH₂ + HCl'],
        'steps': ['Identify the derivative and nucleophile.', 'Check the conversion goes downhill in reactivity.', 'Draw addition, then elimination.', 'Use equilibrium expressions for yields where relevant.'],
        'worked_example': {
            'problem': '1.0 mol ethanoic acid and 3.0 mol ethanol reach equilibrium (K = 4). How much ester forms?',
            'steps': ['x²/[(1 − x)(3 − x)] = 4.', 'x² = 4(3 − 4x + x²), so 3x² − 16x + 12 = 0.', 'x = (16 − √112)/6 ≈ 0.90 mol (the other root exceeds 1).'],
            'answer': 'About 0.90 mol of ethyl ethanoate.',
            'check': 'More than the 0.67 mol obtained with equal amounts, as Le Chatelier predicts ✓.'},
        'mistakes': ['Treating esterification as complete.', 'Converting amides to acyl chlorides directly (uphill).', 'Forgetting saponification gives the salt, not the acid.', 'Choosing the root of the quadratic larger than 1 mol.'],
        'real_world': 'Aspirin is made by esterifying salicylic acid with ethanoic anhydride, a classic acyl substitution.',
        'exam_strategy': 'Memorise the reactivity ladder; most "can this conversion happen?" questions are answered by it.',
        'recap': ['Addition then elimination.', 'Reactivity ladder.', 'Esterification equilibrium.', 'Saponification irreversible.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Hückel\'s rule says aromatic rings have how many π electrons?', ['4n + 2', '4n', '2n', 'n + 2'], 0, '2, 6, 10 …'),
    Q(T1, 'Cyclobutadiene, with 4 π electrons, is:', ['antiaromatic', 'aromatic', 'non-planar and aromatic', 'more stable than benzene'], 0, '4n.'),
    Q(T1, 'From hydrogenation data (cyclohexene −120, benzene −208 kJ/mol), benzene\'s resonance energy is about:', ['152 kJ/mol', '88 kJ/mol', '208 kJ/mol', '360 kJ/mol'], 0, '360 − 208.'),
    Q(T1, 'The C–C bonds in benzene are:', ['all equal, between single and double', 'alternately single and double', 'all double', 'all single'], 0, '140 pm.'),
    Q(T1, 'How many π electrons does naphthalene have?', ['10', '8', '12', '6'], 0, 'n = 2.', ans=10, num=True),
    Q(T1, 'Pyrrole is aromatic because:', ['the N lone pair joins the π system, making 6', 'it has 4 π electrons', 'it is not planar', 'N has no lone pair'], 0, '4 + 2.'),
    # T2
    Q(T2, 'The electrophile in nitration is:', ['NO₂⁺', 'NO₃⁻', 'HNO₃', 'NO'], 0, 'From HNO₃/H₂SO₄.'),
    Q(T2, 'Benzene reacts with bromine only when a catalyst such as FeBr₃ is present because:', ['a stronger electrophile is needed', 'bromine is a nucleophile', 'benzene adds Br₂ easily', 'FeBr₃ is a reducing agent'], 0, 'Aromatic stability.'),
    Q(T2, 'The –NO₂ group on benzene is:', ['deactivating and meta-directing', 'activating and ortho/para-directing', 'deactivating and ortho/para-directing', 'activating and meta-directing'], 0, 'Electron-withdrawing.'),
    Q(T2, 'To make m-bromonitrobenzene from benzene you should:', ['nitrate first, then brominate', 'brominate first, then nitrate', 'do both at once', 'use Friedel–Crafts alkylation'], 0, 'NO₂ directs meta.'),
    Q(T2, '7.8 g benzene gives 9.8 g nitrobenzene. The yield is about:', ['80%', '126%', '64%', '98%'], 0, '9.8/12.3.'),
    Q(T2, 'How many positional isomers does a disubstituted benzene with two identical groups have?', ['3', '2', '4', '6'], 0, 'ortho, meta, para.', ans=3, num=True),
    # T3
    Q(T3, 'Propanone + CH₃MgBr, then acid, gives:', ['2-methylpropan-2-ol', 'butan-2-ol', 'propan-2-ol', 'butanal'], 0, 'Ketone → 3° alcohol.'),
    Q(T3, 'NaBH₄ reduces butanal to:', ['butan-1-ol', 'butan-2-ol', 'butanoic acid', 'butane'], 0, 'Aldehyde → 1°.'),
    Q(T3, 'A silver mirror with Tollens\' reagent shows:', ['an aldehyde', 'a ketone', 'an alcohol', 'an ester'], 0, 'Aldehydes oxidise.'),
    Q(T3, 'An orange precipitate with 2,4-DNP indicates:', ['an aldehyde or ketone', 'an alcohol only', 'an alkene', 'an amine'], 0, 'Carbonyl test.'),
    Q(T3, 'Butan-2-ol can be made from ethanal and:', ['ethylmagnesium bromide', 'methylmagnesium bromide', 'propylmagnesium bromide', 'NaBH₄ only'], 0, '2 + 2 carbons.'),
    Q(T3, 'Aldehydes are more reactive to nucleophiles than ketones because they are:', ['less hindered and less electron-rich at C', 'more hindered', 'aromatic', 'ionic'], 0, 'One alkyl group.'),
    # T4
    Q(T4, 'The most reactive carboxylic acid derivative is:', ['an acyl chloride', 'an ester', 'an amide', 'an anhydride'], 0, 'Cl⁻ leaves best.'),
    Q(T4, '1 mol ethanoic acid + 1 mol ethanol (K = 4) gives at equilibrium about:', ['0.67 mol ester', '0.50 mol ester', '1.0 mol ester', '0.80 mol ester'], 0, 'x/(1 − x) = 2.'),
    Q(T4, 'With 3 mol ethanol instead, the ester formed is about:', ['0.90 mol', '0.67 mol', '1.0 mol', '0.75 mol'], 0, 'Le Chatelier.'),
    Q(T4, 'Saponification of an ester with NaOH gives:', ['a carboxylate salt and an alcohol', 'a carboxylic acid and water', 'an acyl chloride', 'an amide'], 0, 'Irreversible.'),
    Q(T4, '2/3 mol of ethyl ethanoate (88.10 g/mol) has a mass of about:', ['58.7 g', '88.1 g', '29.4 g', '132 g'], 0, '0.667 × 88.10.'),
    Q(T4, 'Proteins are stable because their peptide links are:', ['amides, the least reactive derivatives', 'esters', 'acyl chlorides', 'anhydrides'], 0, 'Poor leaving group.'),
]

FLASH = [
    ['Aromaticity', 'Cyclic, planar, conjugated, 4n + 2 π electrons.'],
    ['Benzene resonance energy', 'About 152 kJ/mol.'],
    ['EAS mechanism', 'E⁺ adds → arenium ion → loses H⁺.'],
    ['Directing groups', 'Donors and halogens o/p; –NO₂, –CHO, –COOH, –CN meta.'],
    ['Grignard additions', 'HCHO → 1°, RCHO → 2°, ketone → 3° alcohol.'],
    ['Carbonyl tests', '2,4-DNP: any C=O; Tollens: aldehydes only.'],
    ['Acyl derivative reactivity', 'Acyl chloride > anhydride > ester > amide.'],
    ['Fischer esterification', 'Acid + alcohol ⇌ ester + water, K ≈ 4.'],
]
