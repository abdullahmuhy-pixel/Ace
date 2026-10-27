"""Cell Biology, module 1: The molecules of life."""
from verify import Q
T1, T2, T3, T4 = ('Water, pH and the chemistry of life', 'Carbohydrates and lipids', 'Proteins', 'Nucleic acids')
assert 10 ** (5 - 3) == 100
assert 100 - 2 * 30 == 40 and 40 / 2 == 20
assert 100 - 1 == 99 and 3 == 3
assert 4 ** 3 == 64

MODULE = {
    'title': 'The molecules of life',
    'topics': [T1, T2, T3, T4],
    'overview': 'All cells are built from the same small set of molecules. This module covers water and pH, then the four classes of biological macromolecules: carbohydrates, lipids, proteins and nucleic acids, focusing on how their structure explains their function.',
    'key_terms': ['Hydrogen bond', 'pH', 'Buffer', 'Monomer', 'Polymer', 'Condensation reaction', 'Hydrolysis', 'Monosaccharide', 'Triglyceride', 'Phospholipid', 'Amino acid', 'Peptide bond', 'Nucleotide'],
    'explanation': [
        'Living things are mostly water, and water\'s polarity and hydrogen bonding give it the properties life depends on: a solvent for ions and polar molecules, a high specific heat capacity and cohesion. pH measures hydrogen ion concentration, and buffers keep it steady inside cells.',
        'Most large biological molecules are polymers built from monomers by condensation reactions (releasing water) and broken down by hydrolysis (using water). Sugars build polysaccharides; amino acids build proteins; nucleotides build DNA and RNA. Lipids are not true polymers but are assembled the same way.',
        'Structure decides function everywhere in biology: the branching of glycogen allows rapid release of glucose, the amphipathic shape of phospholipids forms membranes, the folded shape of an enzyme forms its active site, and the base pairing of DNA allows it to be copied.'],
    'quick_facts': [
        'Condensation joins monomers and releases water; hydrolysis splits them using water.',
        'pH = −log[H⁺]; one pH unit is a tenfold change.',
        'Carbohydrates: (CH₂O)ₙ; glucose is C₆H₁₂O₆.',
        'Proteins: 20 amino acids joined by peptide bonds.',
        'DNA: A pairs with T, G with C; RNA uses U instead of T.'],
}

NOTES = {
    T1: {
        'overview': 'Water is the medium of life. Its unusual properties come from polarity and hydrogen bonding. pH and buffers control the chemical environment inside cells.',
        'key_terms': ['Polar molecule', 'Hydrogen bond', 'Cohesion', 'Specific heat capacity', 'Solvent', 'pH', 'Buffer', 'Hydrophilic', 'Hydrophobic'],
        'explanation': [
            'In a water molecule, oxygen pulls shared electrons more strongly than hydrogen, making oxygen slightly negative and the hydrogens slightly positive. Neighbouring molecules attract through hydrogen bonds. These weak bonds, constantly breaking and reforming, explain cohesion (water moving up xylem), surface tension and water\'s high specific heat capacity, which keeps body and ocean temperatures stable.',
            'Water dissolves ions and polar molecules (hydrophilic substances) because its partial charges surround them. Non-polar substances such as oils are hydrophobic: they cluster together in water, a fact that drives membrane formation and protein folding.',
            'pH = −log[H⁺]. Each unit is a tenfold change, so pH 3 has 100 times more H⁺ than pH 5. Human blood is kept near pH 7.4 by buffers such as the carbonic acid–hydrogencarbonate system, which take up or release H⁺ to resist changes in pH.'],
        'formulas_label': 'Key ideas',
        'formulas': ['pH = −log₁₀[H⁺]', 'Difference of n pH units = 10ⁿ-fold change in [H⁺]', 'Blood pH ≈ 7.35 to 7.45', 'Buffer: weak acid + its conjugate base'],
        'steps': ['Identify the property asked about.', 'Link it to polarity or hydrogen bonding.', 'Give the biological consequence.', 'For pH, convert the difference to a power of ten.'],
        'worked_example': {
            'problem': 'Stomach fluid has pH 2 and the small intestine pH 8 (approximately). How many times more concentrated is H⁺ in the stomach?',
            'steps': ['Difference = 8 − 2 = 6 pH units.', 'Each unit is a factor of 10.', 'Ratio = 10⁶ = 1 000 000.'],
            'answer': 'About a million times more concentrated.',
            'check': 'Lower pH means more H⁺, so the stomach should have the higher concentration ✓.'},
        'mistakes': ['Thinking a pH change of 2 means twice the acidity.', 'Confusing hydrogen bonds (between molecules) with covalent bonds (within a molecule).', 'Saying oil does not mix with water because it is "heavier".', 'Forgetting that higher pH means fewer H⁺ ions.'],
        'real_world': 'Sweating cools you because breaking the hydrogen bonds to evaporate water takes a lot of energy from your skin.',
        'exam_strategy': 'For any "property of water" question, use the chain: polarity → hydrogen bonds → property → why it matters to living things.',
        'recap': ['Water is polar.', 'Hydrogen bonds explain cohesion and heat capacity.', 'pH is logarithmic.', 'Buffers resist pH change.']},
    T2: {
        'overview': 'Carbohydrates are the main energy source and structural material in many organisms. Lipids store energy and form membranes.',
        'key_terms': ['Monosaccharide', 'Disaccharide', 'Polysaccharide', 'Glycosidic bond', 'Starch', 'Glycogen', 'Cellulose', 'Triglyceride', 'Ester bond', 'Phospholipid', 'Saturated', 'Unsaturated', 'Steroid'],
        'explanation': [
            'Monosaccharides such as glucose (C₆H₁₂O₆), fructose and galactose are the building blocks. Two join by a condensation reaction to form a disaccharide (glucose + glucose → maltose + water; glucose + fructose → sucrose) linked by a glycosidic bond. Polysaccharides are long chains: starch (plants) and glycogen (animals, highly branched) store energy; cellulose (β-glucose, straight chains linked by hydrogen bonds into microfibrils) gives plant cell walls strength.',
            'A triglyceride is one glycerol joined to three fatty acids by ester bonds, releasing three water molecules. Saturated fatty acids have no C=C double bonds and pack tightly (solid fats); unsaturated ones have kinks from C=C bonds (liquid oils). Lipids store about twice as much energy per gram as carbohydrates.',
            'A phospholipid replaces one fatty acid with a phosphate group, giving a hydrophilic head and two hydrophobic tails. In water they form a bilayer, the basis of every cell membrane. Steroids such as cholesterol have four fused rings; cholesterol regulates membrane fluidity and is the starting point for hormones like testosterone and oestrogen.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Glucose: C₆H₁₂O₆', 'Monosaccharide + monosaccharide → disaccharide + H₂O', 'Glycerol + 3 fatty acids → triglyceride + 3 H₂O', 'Phospholipid: hydrophilic head, two hydrophobic tails'],
        'steps': ['Identify the monomers.', 'Name the bond formed (glycosidic or ester).', 'Count the water molecules released.', 'Link the structure to the function.'],
        'worked_example': {
            'problem': 'Explain why glycogen is a good energy store in animal cells.',
            'steps': ['It is a polymer of glucose, so it is compact and insoluble: it does not affect the cell\'s water potential.', 'It is highly branched, giving many ends where enzymes can remove glucose quickly.', 'Hydrolysis releases glucose for respiration when needed.'],
            'answer': 'Compact, insoluble and highly branched for rapid release of glucose.',
            'check': 'Each feature is linked to a function, which is what the mark scheme rewards ✓.'},
        'mistakes': ['Calling lipids polymers.', 'Confusing starch (plants) and glycogen (animals).', 'Forgetting water is released in condensation.', 'Saying unsaturated fats have more hydrogen.'],
        'real_world': 'Humans cannot digest cellulose because we lack the enzyme cellulase; cows rely on microbes in their stomachs to do it for them.',
        'exam_strategy': 'Structure-function questions want pairs: "branched, so…", "insoluble, so…". Write each feature with its consequence.',
        'recap': ['Glycosidic bonds join sugars.', 'Starch, glycogen store; cellulose supports.', 'Triglyceride = glycerol + 3 fatty acids.', 'Phospholipids form bilayers.']},
    T3: {
        'overview': 'Proteins do most of the work in cells: enzymes, transporters, receptors, antibodies and structural fibres. Their function depends on their folded three-dimensional shape.',
        'key_terms': ['Amino acid', 'R group', 'Peptide bond', 'Polypeptide', 'Primary structure', 'Secondary structure', 'Tertiary structure', 'Quaternary structure', 'Denaturation'],
        'explanation': [
            'Each amino acid has an amino group, a carboxyl group, a hydrogen and a variable R group; there are 20 common amino acids. Condensation joins them with peptide bonds, so a chain of 100 amino acids contains 99 peptide bonds.',
            'The primary structure is the sequence of amino acids. Hydrogen bonds between backbone groups give secondary structures (α-helix and β-pleated sheet). The tertiary structure is the overall 3D fold, held by interactions between R groups: hydrogen bonds, ionic bonds, disulfide bridges and hydrophobic interactions. Proteins with more than one polypeptide, like haemoglobin (four chains), have quaternary structure.',
            'High temperature or extreme pH break the weaker bonds holding the shape, so the protein denatures and loses its function, although the peptide bonds remain. A single amino acid change can matter: in sickle-cell disease, one substitution in haemoglobin changes how the molecules stack.'],
        'formulas_label': 'Key ideas',
        'formulas': ['n amino acids → n − 1 peptide bonds and n − 1 water molecules', 'Levels: primary → secondary → tertiary → quaternary', 'Denaturation breaks H, ionic and disulfide bonds, not peptide bonds'],
        'steps': ['Identify the level of structure.', 'Name the bonds involved at that level.', 'Explain how shape gives function.', 'Predict the effect of heat or pH.'],
        'worked_example': {
            'problem': 'A polypeptide contains 150 amino acids. How many peptide bonds does it have, and how many water molecules were released in making it?',
            'steps': ['Each bond joins two neighbouring amino acids.', 'A chain of n units has n − 1 links.', '150 − 1 = 149 peptide bonds, and 149 water molecules released.'],
            'answer': '149 peptide bonds and 149 water molecules.',
            'check': 'A chain of 2 amino acids (a dipeptide) has 1 bond, which fits the n − 1 rule ✓.'},
        'mistakes': ['Saying denaturation breaks peptide bonds.', 'Confusing secondary (backbone H bonds) with tertiary (R-group bonds).', 'Thinking all proteins have quaternary structure.', 'Saying a denatured enzyme is "killed".'],
        'real_world': 'Cooking an egg denatures its albumin protein, turning it from clear to white; the change cannot be reversed by cooling.',
        'exam_strategy': 'Name specific bonds for each level of structure; vague answers like "bonds break" rarely score.',
        'recap': ['20 amino acids, R groups differ.', 'Peptide bonds by condensation.', 'Four levels of structure.', 'Shape decides function.']},
    T4: {
        'overview': 'DNA stores genetic information and RNA helps express it. Both are polymers of nucleotides.',
        'key_terms': ['Nucleotide', 'Deoxyribose', 'Ribose', 'Phosphodiester bond', 'Base pairing', 'Double helix', 'Antiparallel', 'Purine', 'Pyrimidine', 'ATP'],
        'explanation': [
            'A nucleotide has a pentose sugar, a phosphate group and a nitrogenous base. DNA uses deoxyribose and the bases adenine (A), thymine (T), guanine (G) and cytosine (C). RNA uses ribose and uracil (U) instead of thymine. Nucleotides join by phosphodiester bonds into a sugar–phosphate backbone.',
            'DNA is a double helix of two antiparallel strands held together by hydrogen bonds between complementary bases: A with T (two hydrogen bonds) and G with C (three). So in any DNA molecule %A = %T and %G = %C (Chargaff\'s rule). If 30% of the bases are adenine, 30% are thymine and the remaining 40% splits into 20% guanine and 20% cytosine.',
            'RNA is usually single-stranded and comes in several types: messenger RNA carries the code, transfer RNA brings amino acids, and ribosomal RNA forms ribosomes. ATP (adenosine triphosphate) is a modified nucleotide that acts as the cell\'s energy currency.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Nucleotide = sugar + phosphate + base', 'A = T and G = C (Chargaff)', 'A–T: 2 hydrogen bonds; G–C: 3', 'DNA: deoxyribose, T; RNA: ribose, U'],
        'steps': ['Use complementary pairing.', 'Apply %A = %T, %G = %C.', 'Share the remainder equally between the other pair.', 'Compare DNA and RNA features.'],
        'worked_example': {
            'problem': 'A DNA sample has 30% adenine. Find the percentages of thymine, guanine and cytosine.',
            'steps': ['A pairs with T, so T = 30%.', 'A + T = 60%, leaving 40% for G + C.', 'G = C = 20%.'],
            'answer': 'T 30%, G 20%, C 20%.',
            'check': '30 + 30 + 20 + 20 = 100% ✓.'},
        'mistakes': ['Pairing A with G.', 'Saying RNA contains thymine.', 'Forgetting the strands are antiparallel.', 'Applying Chargaff\'s rule to single-stranded RNA.'],
        'real_world': 'DNA fingerprinting compares repeated sequences in DNA; it is used in paternity tests and to identify suspects or victims.',
        'exam_strategy': 'Make a table comparing DNA and RNA (sugar, bases, strands, location, function); comparison questions are common.',
        'recap': ['Nucleotides: sugar, phosphate, base.', 'A–T, G–C.', 'Double helix, antiparallel.', 'RNA: ribose, uracil, single strand.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Water molecules are attracted to each other mainly by:', ['hydrogen bonds', 'covalent bonds', 'ionic bonds', 'peptide bonds'], 0, 'Between δ+ hydrogen and δ− oxygen.'),
    Q(T1, 'A solution at pH 3 has how many times more H⁺ than one at pH 5?', ['100', '2', '10', '1000'], 0, '10² = 100.', ans=100),
    Q(T1, 'Water\'s high specific heat capacity means it:', ['resists changes in temperature', 'boils easily', 'freezes quickly', 'is a poor solvent'], 0, 'Many hydrogen bonds must be broken to warm it.'),
    Q(T1, 'A buffer:', ['resists changes in pH', 'makes a solution neutral', 'always lowers pH', 'is a strong acid'], 0, 'It takes up or releases H⁺.'),
    Q(T1, 'Substances that dissolve easily in water are described as:', ['hydrophilic', 'hydrophobic', 'non-polar', 'saturated'], 0, '"Water-loving".'),
    Q(T1, 'The normal pH of human blood is about:', ['7.4', '2.0', '5.5', '9.0'], 0, 'Slightly alkaline, kept by buffers.'),
    # T2
    Q(T2, 'Two glucose molecules join to form maltose. The bond and by-product are:', ['a glycosidic bond and water', 'a peptide bond and water', 'an ester bond and CO₂', 'a glycosidic bond and oxygen'], 0, 'Condensation reaction.'),
    Q(T2, 'The main storage polysaccharide in animals is:', ['glycogen', 'starch', 'cellulose', 'sucrose'], 0, 'Highly branched glucose polymer.'),
    Q(T2, 'Forming one triglyceride releases how many water molecules?', ['3', '1', '2', '4'], 0, 'One ester bond per fatty acid.', ans=3),
    Q(T2, 'Unsaturated fatty acids:', ['contain at least one C=C double bond', 'contain no double bonds', 'are always solid at room temperature', 'contain phosphate'], 0, 'Double bonds create kinks.'),
    Q(T2, 'Phospholipids form bilayers because they have:', ['a hydrophilic head and hydrophobic tails', 'only hydrophobic parts', 'only hydrophilic parts', 'peptide bonds'], 0, 'Amphipathic molecules.'),
    Q(T2, 'Cellulose is strong because:', ['straight β-glucose chains are hydrogen-bonded into microfibrils', 'it is highly branched', 'it contains peptide bonds', 'it is made of fructose'], 0, 'Parallel chains bond together.'),
    # T3
    Q(T3, 'A polypeptide of 100 amino acids contains how many peptide bonds?', ['99', '100', '101', '50'], 0, 'n − 1.', ans=99),
    Q(T3, 'The primary structure of a protein is:', ['its sequence of amino acids', 'its α-helices', 'its 3D fold', 'its number of chains'], 0, 'The order of amino acids.'),
    Q(T3, 'Secondary structure is held mainly by:', ['hydrogen bonds between backbone groups', 'disulfide bridges', 'peptide bonds', 'ionic bonds between R groups'], 0, 'α-helix and β-sheet.'),
    Q(T3, 'Which bond is NOT broken when a protein denatures?', ['Peptide bond', 'Hydrogen bond', 'Ionic bond', 'Disulfide bridge'], 0, 'The primary structure survives.'),
    Q(T3, 'Haemoglobin has quaternary structure because it:', ['has more than one polypeptide chain', 'contains an α-helix', 'has a sequence of amino acids', 'is an enzyme'], 0, 'Four chains.'),
    Q(T3, 'Amino acids differ from one another in their:', ['R groups', 'amino groups', 'carboxyl groups', 'peptide bonds'], 0, 'The variable side chain.'),
    # T4
    Q(T4, 'A DNA sample is 30% adenine. The percentage of guanine is:', ['20%', '30%', '40%', '70%'], 0, '(100 − 60)/2.', ans=20),
    Q(T4, 'Which base is found in RNA but not DNA?', ['Uracil', 'Thymine', 'Adenine', 'Guanine'], 0, 'U replaces T.'),
    Q(T4, 'The two strands of DNA are held together by:', ['hydrogen bonds between bases', 'phosphodiester bonds', 'peptide bonds', 'glycosidic bonds'], 0, 'Complementary base pairing.'),
    Q(T4, 'A nucleotide consists of:', ['a pentose sugar, a phosphate and a base', 'an amino acid and a sugar', 'glycerol and fatty acids', 'a base and an amino group'], 0, 'Three parts.'),
    Q(T4, 'G–C pairs are joined by how many hydrogen bonds?', ['3', '2', '1', '4'], 0, 'A–T has 2.', ans=3),
    Q(T4, 'The sugar in RNA is:', ['ribose', 'deoxyribose', 'glucose', 'fructose'], 0, 'DNA uses deoxyribose.'),
]

FLASH = [
    ['Hydrogen bond', 'Weak attraction between δ+ H and δ− O or N; gives water its properties.'],
    ['pH', '−log[H⁺]; one unit = tenfold change.'],
    ['Condensation', 'Joins monomers, releasing water.'],
    ['Hydrolysis', 'Splits polymers using water.'],
    ['Triglyceride', 'Glycerol + 3 fatty acids, joined by ester bonds.'],
    ['Peptide bond', 'Links amino acids in a polypeptide.'],
    ['Denaturation', 'Loss of 3D shape (and function) when weak bonds break.'],
    ['Chargaff\'s rule', 'In DNA, %A = %T and %G = %C.'],
]
