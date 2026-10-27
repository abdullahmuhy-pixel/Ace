"""Cell Biology, module 5: The cell cycle and gene expression."""
from verify import Q
T1, T2, T3, T4 = ('The cell cycle and mitosis', 'Meiosis and genetic variation', 'DNA replication', 'Gene expression: transcription and translation')
assert 30 / 200 == 0.15 and round(0.10 * 24, 6) == 2.4 and round(0.15 * 20, 6) == 3
assert 2 ** 3 == 8 and round(2 ** 23 / 1e6, 1) == 8.4
assert 4 ** 3 == 64 and 64 - 3 == 61 and 300 * 3 == 900 and 300 * 3 + 3 == 903
comp = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
assert ''.join(comp[b] for b in 'TACGGA') == 'AUGCCU'
assert ''.join(comp[b] for b in 'TACAAACCG') == 'AUGUUUGGC'

MODULE = {
    'title': 'The cell cycle and gene expression',
    'topics': [T1, T2, T3, T4],
    'overview': 'Cells copy themselves and use their DNA to build proteins. This module covers the cell cycle and mitosis, meiosis and the variation it produces, how DNA is replicated accurately, and how genes are transcribed and translated into proteins.',
    'key_terms': ['Cell cycle', 'Interphase', 'Mitosis', 'Cytokinesis', 'Meiosis', 'Haploid', 'Diploid', 'Crossing over', 'Semi-conservative replication', 'DNA polymerase', 'Transcription', 'Translation', 'Codon', 'Mutation'],
    'explanation': [
        'Most of a cell\'s life is spent in interphase, growing and copying its DNA. Mitosis then separates the copies so that two genetically identical diploid cells form, for growth, repair and asexual reproduction.',
        'Meiosis makes haploid gametes with half the chromosome number, and crossing over and independent assortment make every gamete genetically different. DNA replication is semi-conservative: each new molecule keeps one old strand.',
        'Gene expression has two stages: transcription copies a gene into messenger RNA in the nucleus, and translation on ribosomes reads the mRNA three bases (one codon) at a time to join amino acids into a polypeptide. Mutations change the DNA sequence and may change the protein.'],
    'quick_facts': [
        'Cell cycle: G1 → S (DNA copied) → G2 → mitosis → cytokinesis.',
        'Mitosis: 2 identical diploid cells. Meiosis: 4 different haploid cells.',
        'Mitotic index = cells in mitosis ÷ total cells.',
        'DNA replication is semi-conservative; DNA polymerase adds nucleotides 5′ → 3′.',
        '64 codons: 61 code for amino acids, 3 are stop codons; AUG is the start codon.'],
}

NOTES = {
    T1: {
        'overview': 'The cell cycle is the sequence of growth, DNA copying and division. Mitosis divides the copied chromosomes equally so daughter cells are genetically identical.',
        'key_terms': ['Interphase', 'G1, S and G2', 'Chromatid', 'Centromere', 'Prophase', 'Metaphase', 'Anaphase', 'Telophase', 'Cytokinesis', 'Mitotic index', 'Checkpoint', 'Cancer'],
        'explanation': [
            'Interphase has three parts: G1 (growth and normal function), S (DNA replication, so each chromosome becomes two sister chromatids joined at a centromere and DNA content doubles) and G2 (more growth and checks). Checkpoints between stages stop the cycle if DNA is damaged.',
            'Mitosis: in prophase chromosomes condense and the spindle forms; in metaphase chromosomes line up at the equator; in anaphase sister chromatids are pulled to opposite poles; in telophase nuclear envelopes reform. Cytokinesis then divides the cytoplasm (a cleavage furrow in animals, a cell plate in plants). A human cell with 46 chromosomes produces two cells with 46.',
            'The mitotic index is the proportion of cells in mitosis: 30 of 200 cells gives 0.15. Because the proportion of cells in a stage reflects the time spent in it, a 20-hour cycle with an index of 0.15 spends about 3 hours in mitosis. Cancer is uncontrolled division, often after mutations in genes that control checkpoints.'],
        'formulas_label': 'Formulas',
        'formulas': ['Mitotic index = cells in mitosis ÷ total cells counted', 'Time in a stage ≈ (cells in stage ÷ total) × cycle length', 'Mitosis: 2n → 2 × 2n (identical)', 'S phase doubles DNA content'],
        'steps': ['Count cells in each stage.', 'Divide by the total.', 'Multiply by the cycle length for time.', 'Identify stages from chromosome positions.'],
        'worked_example': {
            'problem': 'In a root-tip squash, 30 of 200 cells are in mitosis. The cell cycle lasts 20 hours. Estimate the mitotic index and the time spent in mitosis.',
            'steps': ['Mitotic index = 30 ÷ 200 = 0.15.', 'Time in mitosis ≈ 0.15 × 20 h.', '= 3 hours.'],
            'answer': 'Index 0.15; about 3 hours in mitosis.',
            'check': 'Most cells (85%) are in interphase, consistent with interphase being the longest stage ✓.'},
        'mistakes': ['Calling interphase a "resting" stage.', 'Saying DNA is copied during mitosis.', 'Confusing chromatids and chromosomes.', 'Forgetting cytokinesis is separate from mitosis.'],
        'real_world': 'Many chemotherapy drugs target dividing cells, which is why hair follicles and the gut lining, which also divide quickly, are affected too.',
        'exam_strategy': 'Learn one clear identifying feature per stage (metaphase: lined up at the middle; anaphase: V-shapes moving apart).',
        'recap': ['G1, S, G2, then mitosis.', 'PMAT.', 'Identical diploid cells.', 'Mitotic index estimates time.']},
    T2: {
        'overview': 'Meiosis halves the chromosome number to make gametes and shuffles genetic material so offspring vary.',
        'key_terms': ['Diploid (2n)', 'Haploid (n)', 'Homologous chromosomes', 'Bivalent', 'Crossing over', 'Chiasma', 'Independent assortment', 'Random fertilisation', 'Non-disjunction'],
        'explanation': [
            'Meiosis has two divisions after one round of DNA replication. Meiosis I separates homologous chromosomes (one from each parent), halving the number; meiosis II separates sister chromatids, like mitosis. The result is four haploid cells: in humans, 23 chromosomes each from a 46-chromosome cell.',
            'Variation comes from three sources. Crossing over: in prophase I, homologous chromosomes pair and swap sections at chiasmata, creating new combinations of alleles. Independent assortment: in metaphase I, each pair lines up independently, so with n pairs there are 2ⁿ combinations (8 for n = 3; about 8.4 million for humans, with n = 23). Random fertilisation multiplies the variety further.',
            'Errors happen: if homologous chromosomes or chromatids fail to separate (non-disjunction), gametes get an extra or missing chromosome. Three copies of chromosome 21 cause Down syndrome.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Meiosis: 2n → 4 × n (all different)', 'Combinations by independent assortment = 2ⁿ', 'Meiosis I: homologues separate; meiosis II: chromatids separate', 'Fertilisation: n + n → 2n'],
        'steps': ['Identify whether homologues or chromatids are separating.', 'Track the chromosome number.', 'Name the source of variation.', 'Use 2ⁿ for combinations.'],
        'worked_example': {
            'problem': 'An organism has a diploid number of 6. How many genetically different gametes can independent assortment alone produce?',
            'steps': ['2n = 6, so n = 3 homologous pairs.', 'Each pair can line up two ways.', '2³ = 8 combinations.'],
            'answer': '8 different gametes (before crossing over).',
            'check': 'With crossing over, many more combinations are possible, so 8 is a minimum ✓.'},
        'mistakes': ['Saying meiosis produces two cells.', 'Using the diploid number in 2ⁿ.', 'Saying crossing over happens in meiosis II.', 'Confusing homologous chromosomes with sister chromatids.'],
        'real_world': 'Because of crossing over and independent assortment, brothers and sisters (other than identical twins) each inherit a different mix of their parents\' chromosomes, which is why siblings can look so different.',
        'exam_strategy': 'In "compare mitosis and meiosis" questions, cover number of divisions, number and ploidy of cells, genetic identity, and where each happens.',
        'recap': ['Two divisions, four haploid cells.', 'Crossing over in prophase I.', 'Independent assortment: 2ⁿ.', 'Non-disjunction causes aneuploidy.']},
    T3: {
        'overview': 'Before a cell divides, its DNA must be copied accurately. Replication is semi-conservative and is carried out by a team of enzymes.',
        'key_terms': ['Semi-conservative', 'Helicase', 'Replication fork', 'Primer', 'DNA polymerase', 'Leading strand', 'Lagging strand', 'Okazaki fragment', 'DNA ligase', 'Proofreading', 'Meselson–Stahl experiment'],
        'explanation': [
            'Helicase unwinds the double helix and breaks hydrogen bonds between bases, forming a replication fork. Each strand acts as a template. Free nucleotides pair with complementary bases, and DNA polymerase joins them into a new strand, always adding to the 3′ end, so new strands grow 5′ → 3′.',
            'Because the strands are antiparallel, one new strand (leading) is made continuously towards the fork, while the other (lagging) is made in short Okazaki fragments away from the fork. Primase lays down short RNA primers to start each piece, and DNA ligase joins the fragments. DNA polymerase proofreads, giving an error rate of about one in a billion bases.',
            'Meselson and Stahl grew bacteria in heavy nitrogen (¹⁵N), then moved them to light nitrogen (¹⁴N). After one generation all DNA was of intermediate density; after two, half was intermediate and half light. This fits semi-conservative replication: each new molecule keeps one original strand.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Semi-conservative: each daughter = 1 old + 1 new strand', 'DNA polymerase: 5′ → 3′ only', 'Leading strand continuous; lagging strand in Okazaki fragments', 'After g generations in ¹⁴N: 2 hybrid molecules, rest light'],
        'steps': ['Unwind (helicase).', 'Prime (primase).', 'Extend (DNA polymerase).', 'Join fragments (ligase).'],
        'worked_example': {
            'problem': 'In the Meselson–Stahl experiment, what proportion of DNA molecules is intermediate (¹⁵N/¹⁴N) after two generations in ¹⁴N?',
            'steps': ['Generation 1: every molecule has one heavy and one light strand (all hybrid).', 'Generation 2: each hybrid separates; the heavy strand pairs with a new light strand (hybrid) and the light strand with a new light strand (light).', 'So half are hybrid and half are light.'],
            'answer': '50% intermediate, 50% light.',
            'check': 'Conservative replication would give heavy and light bands, never a single intermediate band in generation 1 ✓.'},
        'mistakes': ['Saying DNA polymerase unwinds DNA.', 'Saying both strands are made continuously.', 'Writing that replication happens in mitosis.', 'Confusing ligase with polymerase.'],
        'real_world': 'The polymerase chain reaction (PCR), used in COVID-19 testing and forensics, copies DNA in a test tube using a heat-stable DNA polymerase.',
        'exam_strategy': 'Name each enzyme with its job; marks are usually given for "helicase breaks hydrogen bonds" and "DNA polymerase joins nucleotides".',
        'recap': ['Semi-conservative.', 'Helicase, primase, polymerase, ligase.', 'Leading and lagging strands.', 'Meselson–Stahl confirmed it.']},
    T4: {
        'overview': 'Genes are instructions for proteins. Transcription copies a gene into mRNA; translation reads the mRNA to build a polypeptide.',
        'key_terms': ['Gene', 'Template strand', 'RNA polymerase', 'mRNA', 'Splicing', 'Intron', 'Exon', 'Codon', 'Anticodon', 'tRNA', 'Ribosome', 'Genetic code', 'Mutation', 'Frameshift'],
        'explanation': [
            'Transcription happens in the nucleus. RNA polymerase unwinds a section of DNA and builds mRNA complementary to the template strand, with U in place of T. A template reading 3′-TACGGA-5′ gives mRNA 5′-AUGCCU-3′. In eukaryotes, introns are cut out and exons spliced together before the mRNA leaves the nucleus.',
            'Translation happens on ribosomes. Each codon (three bases) codes for one amino acid. With four bases, there are 4³ = 64 codons: 61 code for amino acids and 3 are stop codons; AUG is the start codon (methionine). tRNA molecules carry specific amino acids and have anticodons that pair with codons. The ribosome joins amino acids with peptide bonds until it reaches a stop codon. A 300-amino-acid protein needs 900 coding bases, plus a stop codon.',
            'The code is degenerate (several codons per amino acid) and universal (shared by almost all life). Mutations change the DNA sequence: a substitution may be silent, change one amino acid (as in sickle-cell anaemia) or create a stop codon; an insertion or deletion of one base causes a frameshift that changes every codon after it.'],
        'formulas_label': 'Key ideas',
        'formulas': ['DNA template → mRNA: A→U, T→A, G→C, C→G', 'Codons: 4³ = 64 (61 amino acids + 3 stop)', 'Amino acids × 3 = coding bases', 'Start codon AUG; stop codons UAA, UAG, UGA'],
        'steps': ['Write the mRNA complementary to the template.', 'Split it into codons from AUG.', 'Use the code to find amino acids.', 'Predict the effect of a mutation.'],
        'worked_example': {
            'problem': 'A DNA template strand reads 3′-TAC AAA CCG-5′. Give the mRNA and the amino acids (AUG = Met, UUU = Phe, GGC = Gly).',
            'steps': ['Complement each base: T→A, A→U, C→G, G→C.', 'mRNA: 5′-AUG UUU GGC-3′.', 'Codons read: Met – Phe – Gly.'],
            'answer': 'mRNA AUGUUUGGC; Met–Phe–Gly.',
            'check': 'The first codon is AUG, the start codon, as expected for the beginning of a gene ✓.'},
        'mistakes': ['Putting T in mRNA.', 'Reading the coding strand instead of the template.', 'Saying each base codes for one amino acid.', 'Thinking all mutations are harmful.'],
        'real_world': 'mRNA vaccines deliver an mRNA for a viral protein; the body\'s own ribosomes translate it, and the immune system learns to recognise the protein.',
        'exam_strategy': 'Line up DNA, mRNA, codons and amino acids in columns; it keeps base-pairing questions error-free.',
        'recap': ['Transcription: DNA → mRNA (nucleus).', 'Translation: mRNA → protein (ribosome).', '64 codons, AUG start.', 'Frameshifts change everything after.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'DNA is replicated during:', ['the S phase of interphase', 'prophase', 'anaphase', 'cytokinesis'], 0, 'S = synthesis.'),
    Q(T1, '30 of 200 cells are in mitosis. The mitotic index is:', ['0.15', '0.30', '6.67', '0.85'], 0, '30 ÷ 200.', ans=0.15, num=True),
    Q(T1, 'With a mitotic index of 0.15 and a 20-hour cycle, time in mitosis is about:', ['3 hours', '15 hours', '1.5 hours', '0.75 hours'], 0, '0.15 × 20.'),
    Q(T1, 'Sister chromatids separate during:', ['anaphase', 'metaphase', 'prophase', 'interphase'], 0, 'Pulled to opposite poles.'),
    Q(T1, 'Chromosomes line up at the equator during:', ['metaphase', 'anaphase', 'telophase', 'prophase'], 0, 'Middle stage.'),
    Q(T1, 'A human body cell with 46 chromosomes divides by mitosis. Each daughter cell has:', ['46 chromosomes', '23 chromosomes', '92 chromosomes', '44 chromosomes'], 0, 'Identical diploid cells.'),
    # T2
    Q(T2, 'Meiosis produces:', ['four genetically different haploid cells', 'two identical diploid cells', 'four identical diploid cells', 'two haploid cells'], 0, 'Gametes.'),
    Q(T2, 'An organism with 2n = 6 can make how many gamete types by independent assortment alone?', ['8', '6', '64', '3'], 0, '2³.', ans=8),
    Q(T2, 'Crossing over occurs during:', ['prophase I', 'prophase II', 'anaphase II', 'interphase'], 0, 'Homologues pair as bivalents.'),
    Q(T2, 'In meiosis I, the structures that separate are:', ['homologous chromosomes', 'sister chromatids', 'centrioles', 'nucleoli'], 0, 'Halves the number.'),
    Q(T2, 'Down syndrome usually results from:', ['non-disjunction of chromosome 21', 'crossing over', 'a frameshift mutation', 'independent assortment'], 0, 'Three copies of 21.'),
    Q(T2, 'Human gametes contain:', ['23 chromosomes', '46 chromosomes', '22 chromosomes', '92 chromosomes'], 0, 'Haploid.'),
    # T3
    Q(T3, 'DNA replication is described as semi-conservative because:', ['each new molecule has one original and one new strand', 'half the DNA is copied', 'only one strand is copied', 'the original molecule is kept intact'], 0, 'Meselson–Stahl.'),
    Q(T3, 'The enzyme that unwinds DNA and breaks hydrogen bonds is:', ['helicase', 'DNA polymerase', 'ligase', 'RNA polymerase'], 0, 'Forms the fork.'),
    Q(T3, 'DNA polymerase adds nucleotides only to the:', ['3′ end, so strands grow 5′ → 3′', '5′ end', 'middle of the strand', 'RNA primer\'s 5′ end'], 0, 'Directionality.'),
    Q(T3, 'Okazaki fragments are found on the:', ['lagging strand', 'leading strand', 'mRNA', 'tRNA'], 0, 'Made away from the fork.'),
    Q(T3, 'After two generations in ¹⁴N (Meselson–Stahl), the proportion of hybrid DNA is:', ['50%', '100%', '25%', '0%'], 0, 'Half hybrid, half light.', ans=50),
    Q(T3, 'Okazaki fragments are joined by:', ['DNA ligase', 'helicase', 'primase', 'RNA polymerase'], 0, 'Seals the backbone.'),
    # T4
    Q(T4, 'A DNA template strand reads TACGGA. The mRNA is:', ['AUGCCU', 'ATGCCT', 'TACGGA', 'UACGGA'], 0, 'Complementary, with U for T.'),
    Q(T4, 'How many different codons are there?', ['64', '20', '61', '4'], 0, '4³.', ans=64),
    Q(T4, 'A protein of 300 amino acids needs how many coding bases (excluding the stop codon)?', ['900', '300', '100', '903'], 0, '3 per amino acid.', ans=900),
    Q(T4, 'Transcription in eukaryotes takes place in the:', ['nucleus', 'ribosome', 'cytoplasm', 'Golgi apparatus'], 0, 'mRNA then leaves.'),
    Q(T4, 'The anticodon is found on:', ['tRNA', 'mRNA', 'DNA', 'the ribosome\'s large subunit only'], 0, 'Pairs with the codon.'),
    Q(T4, 'Deleting a single base from a gene usually causes:', ['a frameshift that changes all later codons', 'no change', 'one amino acid change only', 'a longer protein every time'], 0, 'Reading frame shifts.'),
]

FLASH = [
    ['Interphase', 'G1, S (DNA replication), G2: most of the cell cycle.'],
    ['Mitosis', 'Prophase, metaphase, anaphase, telophase; two identical diploid cells.'],
    ['Mitotic index', 'Cells in mitosis ÷ total cells.'],
    ['Meiosis', 'Two divisions; four different haploid cells.'],
    ['Independent assortment', '2ⁿ combinations of chromosomes in gametes.'],
    ['Semi-conservative replication', 'Each new DNA has one old and one new strand.'],
    ['Codon', 'Three mRNA bases coding for one amino acid; 64 in total.'],
    ['Frameshift', 'Insertion or deletion that shifts the reading frame.'],
]
