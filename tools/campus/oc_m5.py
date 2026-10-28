"""Organic Chemistry, module 5: Spectroscopy, biomolecules and synthesis."""
from verify import Q
from oc_common import mass, r, nmr_mult
T1, T2, T3, T4 = ('Infrared spectroscopy and mass spectrometry', 'NMR spectroscopy', 'Amines, amino acids and proteins', 'Polymers and synthesis planning')
EX = {'C': 12.0, 'H': 1.007825, 'O': 15.994915, 'N': 14.003074}
exact = lambda d: sum(EX[k] * v for k, v in d.items())
assert r(exact({'C': 4, 'H': 8, 'O': 2}), 4) == 88.0524 and r(exact({'C': 5, 'H': 12, 'O': 1}), 4) == 88.0888
assert r(1e4 / 5.81, 0) == 1721 and r(75.78 / 24.22, 1) == 3.1 and 2.0 * 400 == 800
assert nmr_mult(2) == 3 and nmr_mult(3) == 4 and nmr_mult(0) == 1 and nmr_mult(6) == 7
assert r((2.34 + 9.60) / 2, 2) == 5.97 and r((2.34 + 9.69) / 2, 1) == 6.0 and 20 ** 3 == 8000 and 20 ** 2 == 400
assert r(mass('C2H5NO2') + mass('C3H7NO2') - mass('H2O'), 0) == 146
assert r(28000 / mass('C2H4'), -1) == 1000 and r(0.8 ** 3 * 100, 1) == 51.2 and r(0.9 ** 5 * 100, 0) == 59
assert r(mass('C4H8O2') / (mass('C2H4O2') + mass('C2H6O')) * 100, 0) == 83

MODULE = {
    'title': 'Spectroscopy, biomolecules and synthesis',
    'topics': [T1, T2, T3, T4],
    'overview': 'The final module shows how chemists identify unknown compounds with infrared, mass and NMR spectra, applies the course to nitrogen compounds and the amino acids and proteins of living things, and ends with polymers and the logic of planning multi-step syntheses.',
    'key_terms': ['Wavenumber', 'Absorption band', 'Molecular ion', 'Fragmentation', 'Isotope pattern', 'Chemical shift', 'Integration', 'Spin–spin splitting', 'n + 1 rule', 'Amine basicity', 'Zwitterion', 'Isoelectric point', 'Peptide bond', 'Addition and condensation polymers', 'Retrosynthesis'],
    'explanation': [
        'Infrared spectra reveal functional groups (a strong C=O band near 1700 cm⁻¹, a broad O–H band above 3200 cm⁻¹). Mass spectra give the molar mass from the molecular ion and clues from fragments and isotope patterns. ¹H NMR shows how many kinds of hydrogen there are, how many of each (integration) and how many neighbours each has (splitting).',
        'Amines are bases and nucleophiles because of the nitrogen lone pair. Amino acids carry both an amine and a carboxylic acid group, exist as zwitterions, and join by amide (peptide) bonds into proteins.',
        'Polymers form by addition (alkenes linking up) or condensation (monomers joining with loss of water). Synthesis planning works backwards from the target (retrosynthesis), choosing reactions from the whole course and keeping the number of steps small, because yields multiply.'],
    'quick_facts': [
        'IR: O–H 3200–3550 (broad), C=O 1680–1750, C≡N ≈ 2250 cm⁻¹.',
        'MS: Cl gives M : M+2 ≈ 3 : 1; Br ≈ 1 : 1.',
        'NMR: n neighbours → n + 1 peaks.',
        'pI = (pKa₁ + pKa₂)/2 for simple amino acids.',
        'Overall yield = product of step yields.'],
}

NOTES = {
    T1: {
        'overview': 'IR spectroscopy identifies functional groups from bond vibrations; mass spectrometry measures molar mass and fragment masses.',
        'key_terms': ['Wavenumber', 'Fingerprint region', 'Stretching vibration', 'Molecular ion (M⁺)', 'Base peak', 'Fragment ion', 'M+2 peak', 'High-resolution mass'],
        'explanation': [
            'IR bands are quoted as wavenumbers, 1/λ in cm⁻¹: a band at λ = 5.81 μm is at 10⁴/5.81 ≈ 1721 cm⁻¹, typical of a C=O stretch. Key bands: O–H in alcohols 3200–3550 (broad, from hydrogen bonding), O–H in acids 2500–3300 (very broad), N–H 3300–3500, C–H 2850–3100, C≡N about 2250, C=O 1680–1750, C=C 1620–1680. Below 1500 cm⁻¹ is the fingerprint region, unique to each compound.',
            'In a mass spectrometer, molecules lose an electron to form M⁺; the peak with the highest m/z (apart from isotope peaks) gives the molar mass. Fragments reveal structure: a peak at m/z 43 often means CH₃CO⁺, and loss of 15 means loss of CH₃.',
            'Isotopes: chlorine (³⁵Cl : ³⁷Cl ≈ 75.8 : 24.2) gives M and M+2 peaks in about a 3 : 1 ratio; bromine gives about 1 : 1. High-resolution MS separates formulas with the same nominal mass: C₄H₈O₂ is 88.0524, C₅H₁₂O is 88.0888.'],
        'formulas_label': 'Data',
        'formulas': ['Wavenumber = 1/λ (cm⁻¹)', 'C=O 1680–1750 cm⁻¹; O–H 3200–3550 cm⁻¹', 'M⁺ gives molar mass', 'Cl: M : M+2 ≈ 3 : 1; Br ≈ 1 : 1'],
        'steps': ['Look for the C=O and O–H regions first.', 'Find M⁺ in the mass spectrum.', 'Check for M+2 patterns.', 'Match fragments to likely groups.'],
        'worked_example': {
            'problem': 'An unknown has M⁺ at m/z 88 (high resolution 88.0524), a strong IR band at 1740 cm⁻¹ and no band above 3100 cm⁻¹. What kind of compound is it?',
            'steps': ['88.0524 matches C₄H₈O₂ rather than C₅H₁₂O (88.0888).', '1740 cm⁻¹ shows C=O; no O–H band rules out an acid or alcohol.', 'C₄H₈O₂ with C=O and no O–H fits an ester.'],
            'answer': 'An ester of formula C₄H₈O₂, such as ethyl ethanoate or methyl propanoate.',
            'check': 'NMR (next topic) would decide between the esters ✓.'},
        'mistakes': ['Reading the base peak as the molecular ion.', 'Forgetting that acids show both broad O–H and C=O.', 'Over-interpreting the fingerprint region.', 'Ignoring M+2 peaks for halogens.'],
        'real_world': 'Drug-testing laboratories and airport security use mass spectrometry to identify tiny amounts of substances.',
        'exam_strategy': 'Start with three questions: is there C=O? is there O–H or N–H? what is M⁺?',
        'recap': ['Wavenumbers.', 'C=O and O–H bands.', 'M⁺ = molar mass.', 'Isotope patterns.']},
    T2: {
        'overview': 'Proton NMR is the most powerful tool for working out structures: it shows hydrogen environments, how many hydrogens each has and how they are connected.',
        'key_terms': ['Chemical environment', 'Chemical shift δ (ppm)', 'TMS reference', 'Shielding', 'Integration', 'Spin–spin coupling', 'n + 1 rule', 'Coupling constant J', '¹³C NMR'],
        'explanation': [
            'Chemical shift δ = (frequency difference/spectrometer frequency) × 10⁶ ppm: on a 400 MHz instrument, a signal 800 Hz from TMS is at δ 2.0. Electronegative atoms deshield nearby protons: alkyl C–H 0.9–1.5, H–C–C=O about 2.0–2.5, H–C–O 3.3–4.3, aromatic 6.5–8, aldehyde 9–10, carboxylic acid 10–12.',
            'Integration gives the relative number of H in each environment. Splitting follows the n + 1 rule: protons with n equivalent neighbours on adjacent carbons appear as n + 1 peaks. In ethanol, CH₃ (2 neighbours) is a triplet, CH₂ (3 neighbours) a quartet and OH usually a singlet.',
            'Ethyl ethanoate, CH₃COOCH₂CH₃, shows three signals in a 3 : 2 : 3 ratio: a singlet near δ 2.0 (CH₃CO), a quartet near δ 4.1 (OCH₂) and a triplet near δ 1.2 (CH₃). ¹³C NMR counts carbon environments: propan-2-ol 2, butanone 4, benzene 1, methylbenzene 5.'],
        'formulas_label': 'Rules',
        'formulas': ['δ = Δν (Hz)/ν₀ (MHz) in ppm', 'n neighbours → n + 1 peaks', 'Integration ∝ number of H', 'Equivalent H do not split each other'],
        'steps': ['Count signals (environments).', 'Use integration for H counts.', 'Use splitting for neighbours.', 'Use δ values to place groups next to O, C=O or rings.'],
        'worked_example': {
            'problem': 'C₄H₈O₂ (an ester) shows: δ 1.2 (3H, triplet), δ 2.0 (3H, singlet), δ 4.1 (2H, quartet). Identify it.',
            'steps': ['Triplet (3H) and quartet (2H) together make an ethyl group, CH₃CH₂–.', 'The CH₂ at δ 4.1 is attached to O; the singlet CH₃ at δ 2.0 is next to C=O.', 'So CH₃–CO–O–CH₂CH₃.'],
            'answer': 'Ethyl ethanoate.',
            'check': 'Methyl propanoate would put a 3H singlet near δ 3.7 (OCH₃) and the CH₂ quartet near δ 2.3 ✓.'},
        'mistakes': ['Counting the proton itself in n.', 'Splitting by protons on the same carbon (equivalent).', 'Reading integration as absolute numbers rather than ratios.', 'Forgetting OH and NH often appear as singlets.'],
        'real_world': 'MRI scanners in hospitals are NMR machines tuned to the hydrogen nuclei in water and fat in the body.',
        'exam_strategy': 'Make a table with columns δ, integration, splitting and inference for each signal before proposing a structure.',
        'recap': ['Environments.', 'Integration.', 'n + 1 splitting.', 'Shifts locate groups.']},
    T3: {
        'overview': 'Nitrogen compounds and amino acids connect organic chemistry to biology.',
        'key_terms': ['Primary, secondary, tertiary amine', 'Basicity', 'pKaH', 'Aniline', 'Amino acid', 'Zwitterion', 'Isoelectric point', 'Peptide bond', 'Primary structure'],
        'explanation': [
            'Amines are bases: their lone pair accepts H⁺. Basicity is measured by the pKa of the conjugate acid (pKaH): methylamine about 10.6 is more basic than ammonia (9.2) because the alkyl group pushes electrons onto N; aniline (4.6) is far weaker because its lone pair is delocalised into the ring. Amines are also good nucleophiles, reacting with haloalkanes and acyl chlorides.',
            'Amino acids, H₂N–CHR–COOH, exist mainly as zwitterions (H₃N⁺–CHR–COO⁻) in solution. The isoelectric point, where the net charge is zero, is the average of the two pKa values for those without ionisable side chains: glycine (2.34, 9.60) has pI ≈ 5.97 and alanine (2.34, 9.69) about 6.0. All the common amino acids except glycine are chiral, and nature uses the L forms.',
            'Two amino acids join by a peptide (amide) bond with loss of water: glycylalanine has M = 75.07 + 89.10 − 18.02 ≈ 146 g/mol. Sequence matters: with 20 amino acids there are 20³ = 8000 possible tripeptides.'],
        'formulas_label': 'Formulas',
        'formulas': ['Stronger base ↔ higher pKaH', 'pI = (pKa₁ + pKa₂)/2', 'Peptide of n residues: M = ΣM(amino acids) − (n − 1) × 18.02', 'Number of sequences = 20ⁿ'],
        'steps': ['Locate the nitrogen lone pair.', 'Ask if it is delocalised (less basic) or pushed by alkyl groups (more basic).', 'For amino acids, find pKa values and the pI.', 'For peptides, subtract water for each bond.'],
        'worked_example': {
            'problem': 'Find the isoelectric point of glycine (pKa₁ = 2.34, pKa₂ = 9.60) and its charge at pH 2.',
            'steps': ['pI = (2.34 + 9.60)/2 = 5.97.', 'At pH 2, below pKa₁, the carboxyl group is mostly protonated.', 'The amine is protonated too, so the net charge is positive.'],
            'answer': 'pI ≈ 5.97; at pH 2 glycine is mostly the cation (+1).',
            'check': 'Below the pI amino acids are positive and move to the cathode in electrophoresis ✓.'},
        'mistakes': ['Thinking aniline is a stronger base than alkylamines.', 'Drawing amino acids as neutral molecules in water.', 'Forgetting to subtract water when forming peptides.', 'Calling glycine chiral.'],
        'real_world': 'Gel electrophoresis separates proteins and DNA fragments by their charge at a chosen pH, used in forensic and medical testing.',
        'exam_strategy': 'For basicity ranking, ask where the lone pair is and whether anything pulls it away.',
        'recap': ['Lone pair basicity.', 'Zwitterions.', 'pI average.', 'Peptide bonds lose water.']},
    T4: {
        'overview': 'Polymers are giant molecules made of repeating units; synthesis planning combines the reactions of the course to build target molecules efficiently.',
        'key_terms': ['Monomer', 'Repeat unit', 'Addition polymer', 'Condensation polymer', 'Nylon', 'Polyester', 'Degree of polymerisation', 'Retrosynthesis', 'Overall yield', 'Atom economy'],
        'explanation': [
            'Addition polymers form from alkenes: ethene → polyethene, chloroethene → PVC, propene → polypropene; nothing is lost, so the repeat unit has the monomer\'s formula. A polyethene chain of molar mass 28 000 g/mol contains about 28 000/28.05 ≈ 1000 monomer units.',
            'Condensation polymers form when two functional groups join and lose a small molecule (usually water): diacids plus diamines give polyamides such as nylon-6,6; diacids plus diols give polyesters such as PET. Their ester and amide links can be hydrolysed, which makes some of them easier to recycle or biodegrade.',
            'Retrosynthesis works backwards, disconnecting bonds the course has taught you to make. Short routes matter because yields multiply: three steps at 80% give 0.8³ = 51.2% overall; five steps at 90% give about 59%. Atom economy measures waste: making ethyl ethanoate from ethanoic acid and ethanol has an atom economy of 88.10/(60.05 + 46.07) ≈ 83%.'],
        'formulas_label': 'Formulas',
        'formulas': ['Degree of polymerisation = M(polymer)/M(repeat unit)', 'Overall yield = y₁ × y₂ × …', 'Atom economy = M(desired product)/ΣM(reactants) × 100%'],
        'steps': ['Identify the target\'s functional groups.', 'Disconnect a bond you know how to form.', 'Repeat until you reach simple starting materials.', 'Check the forward route, yields and atom economy.'],
        'worked_example': {
            'problem': 'A three-step synthesis has yields of 80% at each step. Starting from 1.00 mol, how much product forms?',
            'steps': ['Overall yield = 0.80 × 0.80 × 0.80.', '= 0.512.', 'Product = 0.512 mol.'],
            'answer': '0.512 mol (51.2% overall).',
            'check': 'Each step loses material, so the overall yield is below every single-step yield ✓.'},
        'mistakes': ['Drawing addition polymers with the double bond kept.', 'Forgetting the water lost in condensation polymers.', 'Adding yields instead of multiplying.', 'Confusing atom economy with percentage yield.'],
        'real_world': 'PET bottles are polyesters; chemical recycling breaks their ester links back into monomers.',
        'exam_strategy': 'In synthesis questions, write the reagents and conditions above each arrow; examiners award marks for both.',
        'recap': ['Addition vs condensation.', 'Repeat units.', 'Retrosynthesis.', 'Yields multiply.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A strong IR band at 1720 cm⁻¹ indicates:', ['a C=O group', 'an O–H group', 'a C≡N group', 'an aromatic ring only'], 0, 'Carbonyl stretch.'),
    Q(T1, 'A band at λ = 5.81 μm has a wavenumber of about:', ['1721 cm⁻¹', '581 cm⁻¹', '5810 cm⁻¹', '172 cm⁻¹'], 0, '10⁴/5.81.'),
    Q(T1, 'A broad band from 2500 to 3300 cm⁻¹ plus a C=O band suggests:', ['a carboxylic acid', 'a ketone', 'an ether', 'an alkane'], 0, 'Acid O–H.'),
    Q(T1, 'A compound with one Cl atom shows M and M+2 peaks in the ratio about:', ['3 : 1', '1 : 1', '1 : 3', '9 : 1'], 0, '75.8 : 24.2.'),
    Q(T1, 'High-resolution MS gives M⁺ = 88.0524. The formula is:', ['C₄H₈O₂', 'C₅H₁₂O', 'C₄H₁₂N₂', 'C₆H₁₆'], 0, 'C₅H₁₂O = 88.0888.'),
    Q(T1, 'The molecular ion peak gives:', ['the molar mass', 'the number of carbons only', 'the functional groups', 'the boiling point'], 0, 'M⁺.'),
    # T2
    Q(T2, 'On a 400 MHz spectrometer a signal 800 Hz from TMS has δ:', ['2.0 ppm', '0.5 ppm', '8.0 ppm', '320 ppm'], 0, '800/400.'),
    Q(T2, 'Protons with 3 equivalent neighbours appear as a:', ['quartet', 'triplet', 'doublet', 'singlet'], 0, 'n + 1 = 4.'),
    Q(T2, 'The CH₃ group in ethanol appears as a:', ['triplet', 'quartet', 'singlet', 'doublet'], 0, 'Next to CH₂.'),
    Q(T2, 'Ethyl ethanoate has how many ¹H NMR signals?', ['3', '2', '4', '8'], 0, 'CH₃CO, OCH₂, CH₃.', ans=3, num=True),
    Q(T2, 'How many ¹³C environments does methylbenzene (toluene) have?', ['5', '7', '4', '6'], 0, 'CH₃, ipso, ortho, meta, para.', ans=5, num=True),
    Q(T2, 'A signal at δ 9.7 suggests:', ['an aldehyde H', 'an alkyl CH₃', 'an alcohol OH next to CH₂', 'an alkene H'], 0, 'Aldehydes 9–10.'),
    # T3
    Q(T3, 'Which is the strongest base?', ['methylamine', 'ammonia', 'aniline', 'ethanamide'], 0, 'Alkyl donation.'),
    Q(T3, 'Aniline is a weak base because:', ['its lone pair is delocalised into the ring', 'it has no lone pair', 'it is ionic', 'nitrogen is not electronegative'], 0, 'Resonance.'),
    Q(T3, 'The isoelectric point of glycine (pKa 2.34 and 9.60) is about:', ['5.97', '7.00', '11.94', '3.63'], 0, 'Average.', ans=5.97, num=True),
    Q(T3, 'The molar mass of the dipeptide glycylalanine is about:', ['146 g/mol', '164 g/mol', '128 g/mol', '182 g/mol'], 0, '75.07 + 89.10 − 18.02.'),
    Q(T3, 'How many different tripeptides can be made from the 20 common amino acids?', ['8000', '60', '1140', '400'], 0, '20³.', ans=8000, num=True),
    Q(T3, 'In water at its isoelectric point an amino acid exists mainly as:', ['a zwitterion', 'a neutral molecule with no charges', 'a cation', 'an anion'], 0, 'H₃N⁺ and COO⁻.'),
    # T4
    Q(T4, 'PVC is made by addition polymerisation of:', ['chloroethene', 'ethene', 'propene', 'ethanol'], 0, 'Vinyl chloride.'),
    Q(T4, 'Nylon-6,6 is formed from a diacid and a diamine by:', ['condensation polymerisation', 'addition polymerisation', 'radical substitution', 'hydrogenation'], 0, 'Loses water.'),
    Q(T4, 'A polyethene chain of 28 000 g/mol contains about how many monomer units?', ['1000', '100', '28 000', '10 000'], 0, '28 000/28.05.'),
    Q(T4, 'Three steps at 80% yield each give an overall yield of:', ['51.2%', '80%', '240%', '64%'], 0, '0.8³.'),
    Q(T4, 'The atom economy of making ethyl ethanoate from ethanoic acid and ethanol is about:', ['83%', '100%', '67%', '50%'], 0, '88.10/106.12.'),
    Q(T4, 'Retrosynthesis means:', ['working backwards from the target to simple starting materials', 'repeating a synthesis', 'running a reaction in reverse in the flask', 'recycling polymers'], 0, 'Disconnections.'),
]

FLASH = [
    ['Key IR bands', 'O–H 3200–3550 broad; C=O 1680–1750; C≡N ≈ 2250 cm⁻¹.'],
    ['Mass spectrum', 'M⁺ gives molar mass; Cl 3 : 1 and Br 1 : 1 M+2 patterns.'],
    ['Chemical shift', 'δ = Δν/ν₀ × 10⁶ ppm; electronegative neighbours raise δ.'],
    ['n + 1 rule', 'n equivalent neighbours → n + 1 peaks.'],
    ['Amine basicity', 'Alkylamines > ammonia > aniline.'],
    ['Isoelectric point', 'pI = (pKa₁ + pKa₂)/2; zero net charge.'],
    ['Polymer types', 'Addition from alkenes; condensation loses water (nylon, polyester).'],
    ['Overall yield', 'Multiply step yields; keep routes short.'],
]
