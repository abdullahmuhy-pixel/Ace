"""Cell Biology, module 2: Cell structure."""
from verify import Q
T1, T2, T3, T4 = ('Cell theory and microscopy', 'Prokaryotic and eukaryotic cells', 'Organelles and the endomembrane system', 'The cytoskeleton, cell walls and junctions')
assert 40 * 1000 / 20 == 2000 and 2 * 5000 / 1000 == 10
assert 6 * 1 ** 2 / 1 ** 3 == 6 and 6 * 3 ** 2 / 3 ** 3 == 2
assert 15 * 1000 / 3000 == 5
assert 6 * 2 ** 2 / 2 ** 3 == 3

MODULE = {
    'title': 'Cell structure',
    'topics': [T1, T2, T3, T4],
    'overview': 'The cell is the basic unit of life. This module covers how we see cells (microscopy and magnification), the difference between prokaryotic and eukaryotic cells, the organelles that divide work inside a eukaryotic cell, and the structures that give cells shape and connect them.',
    'key_terms': ['Cell theory', 'Magnification', 'Resolution', 'Prokaryote', 'Eukaryote', 'Nucleus', 'Ribosome', 'Endoplasmic reticulum', 'Golgi apparatus', 'Mitochondrion', 'Chloroplast', 'Lysosome', 'Cytoskeleton', 'Cell junction'],
    'explanation': [
        'Cell theory states that all living things are made of cells, the cell is the basic unit of life, and all cells come from pre-existing cells. Light microscopes reveal cells and large organelles; electron microscopes, with far better resolution, reveal fine internal structure.',
        'Prokaryotes (bacteria and archaea) are small and lack a nucleus and membrane-bound organelles. Eukaryotes (animals, plants, fungi and protists) are larger and divide their work among membrane-bound organelles, a design that allows specialised compartments.',
        'Proteins for export are made on the rough endoplasmic reticulum, modified in the Golgi apparatus and released by vesicles. Mitochondria and chloroplasts transfer energy. The cytoskeleton shapes the cell and moves things within it, while cell walls and junctions hold tissues together.'],
    'quick_facts': [
        'Magnification = image size ÷ actual size.',
        '1 mm = 1000 µm; 1 µm = 1000 nm.',
        'Prokaryotes: no nucleus, 70S ribosomes, circular DNA.',
        'Eukaryotes: nucleus, membrane-bound organelles, 80S ribosomes.',
        'Secretory pathway: rough ER → Golgi → vesicle → membrane.'],
}

NOTES = {
    T1: {
        'overview': 'Cell theory unites biology. Microscopes made it possible, and understanding magnification and resolution lets you measure what you see.',
        'key_terms': ['Cell theory', 'Magnification', 'Resolution', 'Light microscope', 'Transmission electron microscope', 'Scanning electron microscope', 'Micrometre', 'Surface area to volume ratio'],
        'explanation': [
            'Cell theory: all organisms are made of one or more cells; the cell is the smallest unit of life; cells arise only from existing cells by division. Viruses are not cells and are not usually considered alive on their own.',
            'Magnification = image size ÷ actual size; convert both to the same unit first. A cell 20 µm across that appears 40 mm (40 000 µm) wide in a photo is magnified 2000 times. Resolution is the ability to tell two close points apart: about 200 nm for a light microscope and about 0.2 nm or better for a transmission electron microscope. More magnification without more resolution only gives a bigger blur.',
            'Cells are small because of the surface area to volume ratio. A cube of side 1 µm has SA:V = 6:1; at side 3 µm it falls to 2:1. Larger cells have too little membrane to exchange materials fast enough for their volume, so cells divide or develop folds and microvilli.'],
        'formulas_label': 'Formulas',
        'formulas': ['Magnification = image size ÷ actual size', 'Actual size = image size ÷ magnification', '1 mm = 1000 µm, 1 µm = 1000 nm', 'Cube: SA:V = 6/side'],
        'steps': ['Convert all lengths to the same unit (usually µm).', 'Write the formula triangle.', 'Substitute and calculate.', 'Check the answer is a sensible size.'],
        'worked_example': {
            'problem': 'A mitochondrion is 2 µm long. In an electron micrograph it is magnified 5000 times. How long is the image, in mm?',
            'steps': ['Image size = actual size × magnification.', '2 µm × 5000 = 10 000 µm.', '10 000 µm ÷ 1000 = 10 mm.'],
            'answer': '10 mm.',
            'check': 'A 1 cm image on a page is a reasonable size for a micrograph ✓.'},
        'mistakes': ['Mixing mm and µm in the magnification formula.', 'Confusing magnification with resolution.', 'Thinking a light microscope can show ribosomes.', 'Inverting the formula.'],
        'real_world': 'Cryo-electron microscopy, which won the 2017 Nobel Prize in Chemistry, lets scientists see the shapes of individual proteins such as the SARS-CoV-2 spike.',
        'exam_strategy': 'Always show unit conversion as a separate line; it is where most marks are lost in magnification questions.',
        'recap': ['All life is cellular.', 'M = image ÷ actual.', 'Resolution limits detail.', 'Small cells have high SA:V.']},
    T2: {
        'overview': 'All cells share a membrane, cytoplasm, ribosomes and DNA, but prokaryotes and eukaryotes are organised very differently.',
        'key_terms': ['Prokaryote', 'Eukaryote', 'Nucleoid', 'Plasmid', 'Cell wall', 'Peptidoglycan', 'Flagellum', '70S and 80S ribosomes', 'Endosymbiotic theory'],
        'explanation': [
            'Prokaryotic cells (bacteria and archaea) are typically 1 to 5 µm long. Their DNA is a single circular chromosome in a region called the nucleoid, often with small extra rings called plasmids. They have 70S ribosomes, a cell wall (made of peptidoglycan in bacteria) and sometimes a capsule, pili and a flagellum.',
            'Eukaryotic cells are usually 10 to 100 µm. Their linear DNA is wrapped around histone proteins inside a nucleus, and they contain membrane-bound organelles and 80S ribosomes. Plant cells add a cellulose cell wall, chloroplasts and a large central vacuole; animal cells have centrioles and no cell wall; fungi have chitin walls.',
            'Endosymbiotic theory explains where mitochondria and chloroplasts came from: they were once free-living prokaryotes engulfed by a larger cell. Evidence: they have their own circular DNA, 70S ribosomes, double membranes, and divide by a process like binary fission.'],
        'formulas_label': 'Comparison',
        'formulas': ['Prokaryote: no nucleus, circular DNA, 70S ribosomes, 1–5 µm', 'Eukaryote: nucleus, linear DNA with histones, 80S ribosomes, 10–100 µm', 'Plant extras: cell wall, chloroplasts, large vacuole', 'Animal extras: centrioles, no wall'],
        'steps': ['Check for a nucleus.', 'Check for membrane-bound organelles.', 'Look at ribosome size and DNA form.', 'Use extra features (wall, chloroplasts) to place eukaryotes.'],
        'worked_example': {
            'problem': 'A cell has a cell wall, 70S ribosomes, circular DNA and no nucleus. Classify it and name one feature that rules out a plant cell.',
            'steps': ['No nucleus and 70S ribosomes: prokaryotic.', 'The cell wall alone does not decide (plants also have walls).', 'A plant cell would have a nucleus and 80S ribosomes.'],
            'answer': 'A prokaryote (for example a bacterium); the lack of a nucleus rules out a plant cell.',
            'check': 'Every listed feature matches the prokaryote column ✓.'},
        'mistakes': ['Saying prokaryotes have no DNA or no ribosomes.', 'Thinking only plant cells have walls.', 'Calling viruses prokaryotes.', 'Forgetting mitochondria have their own DNA.'],
        'real_world': 'Many antibiotics, such as streptomycin, target 70S ribosomes or peptidoglycan walls, so they harm bacteria without harming human cells.',
        'exam_strategy': 'In comparison questions, write matched pairs ("prokaryotes have 70S ribosomes, whereas eukaryotes have 80S").',
        'recap': ['Prokaryotes: no nucleus.', '70S vs 80S ribosomes.', 'Plants: wall, chloroplasts, vacuole.', 'Endosymbiosis explains mitochondria.']},
    T3: {
        'overview': 'Eukaryotic cells divide labour among organelles. The endomembrane system makes, packages and ships proteins and lipids.',
        'key_terms': ['Nucleus', 'Nucleolus', 'Rough ER', 'Smooth ER', 'Golgi apparatus', 'Vesicle', 'Lysosome', 'Mitochondrion', 'Chloroplast', 'Vacuole', 'Exocytosis'],
        'explanation': [
            'The nucleus holds the DNA, surrounded by a double nuclear envelope with pores that let mRNA out. The nucleolus makes ribosomal RNA. Ribosomes, free in the cytoplasm or on the rough endoplasmic reticulum (RER), make proteins.',
            'The secretory pathway: proteins made on the RER enter its channels, travel in vesicles to the Golgi apparatus, are modified (for example by adding carbohydrate) and sorted, then leave in vesicles that fuse with the membrane (exocytosis). The smooth ER makes lipids and steroids and detoxifies drugs, which is why liver cells have a lot of it. Lysosomes contain hydrolytic enzymes that digest worn-out organelles and engulfed material.',
            'Mitochondria carry out aerobic respiration; their folded inner membrane (cristae) gives a large area for ATP production, so active cells such as muscle and sperm have many. Chloroplasts carry out photosynthesis on stacks of thylakoid membranes (grana). Plant vacuoles store water and solutes and keep cells turgid.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Secretory pathway: RER → vesicle → Golgi → vesicle → exocytosis', 'Mitochondria: respiration (cristae)', 'Chloroplasts: photosynthesis (thylakoids)', 'Lysosomes: digestion (hydrolytic enzymes)'],
        'steps': ['Identify the organelle by structure.', 'State its function.', 'Link its features to the function.', 'For pathways, list organelles in order.'],
        'worked_example': {
            'problem': 'Trace the route of a digestive enzyme from where its gene is read to its release from a pancreatic cell.',
            'steps': ['The gene is transcribed into mRNA in the nucleus; mRNA leaves through a nuclear pore.', 'Ribosomes on the rough ER translate it; the protein enters the ER and is folded.', 'A vesicle carries it to the Golgi, where it is modified and packaged; a secretory vesicle fuses with the cell membrane and releases it by exocytosis.'],
            'answer': 'Nucleus → ribosome on RER → vesicle → Golgi → secretory vesicle → exocytosis.',
            'check': 'Pancreatic cells are packed with RER and Golgi, consistent with high protein secretion ✓.'},
        'mistakes': ['Saying the Golgi makes proteins.', 'Confusing the nucleolus with the nucleus.', 'Saying plant cells have no mitochondria.', 'Forgetting vesicles link the ER and Golgi.'],
        'real_world': 'Tay–Sachs disease is caused by a missing lysosomal enzyme; undigested lipids build up in nerve cells.',
        'exam_strategy': 'When asked "suggest why this cell has many X", link the organelle\'s function to the cell\'s job (sperm: many mitochondria for swimming).',
        'recap': ['Nucleus stores DNA.', 'RER → Golgi → exocytosis.', 'Mitochondria and chloroplasts transfer energy.', 'Lysosomes digest.']},
    T4: {
        'overview': 'The cytoskeleton gives cells shape and lets them move. Cell walls, the extracellular matrix and cell junctions hold cells together in tissues.',
        'key_terms': ['Cytoskeleton', 'Microfilament (actin)', 'Microtubule', 'Intermediate filament', 'Motor protein', 'Cilia and flagella', 'Extracellular matrix', 'Tight junction', 'Desmosome', 'Gap junction', 'Plasmodesmata'],
        'explanation': [
            'The cytoskeleton has three types of fibre. Microfilaments (actin, the thinnest) support the cell surface and drive muscle contraction and cell crawling. Microtubules (tubulin, hollow tubes, the widest) form tracks for vesicles, the spindle in cell division, and the core of cilia and flagella. Intermediate filaments (such as keratin) bear tension and anchor organelles.',
            'Motor proteins such as kinesin and dynein walk along microtubules, using ATP, to carry vesicles and organelles. Cilia and flagella have a "9 + 2" arrangement of microtubules; dynein makes them bend.',
            'Plant cells have a cellulose wall and connect through plasmodesmata, channels through the walls. Animal cells sit in an extracellular matrix of collagen and other proteins and join by junctions: tight junctions seal neighbouring cells (stopping leaks between gut cells), desmosomes rivet cells together (skin), and gap junctions let ions and small molecules pass directly between cells (heart muscle).'],
        'formulas_label': 'Key ideas',
        'formulas': ['Microfilaments: actin, ~7 nm, movement and shape', 'Microtubules: tubulin, ~25 nm, tracks, spindle, cilia', 'Intermediate filaments: ~10 nm, tension', 'Junctions: tight (seal), desmosome (anchor), gap (communicate)'],
        'steps': ['Identify the fibre or junction from its description.', 'State its function.', 'Give a tissue where it matters.', 'Link structure to function.'],
        'worked_example': {
            'problem': 'Heart muscle cells must contract in a coordinated wave. Which junction allows this, and why?',
            'steps': ['Coordination needs electrical signals to pass quickly from cell to cell.', 'Gap junctions are channels that let ions flow directly between cytoplasms.', 'So the electrical impulse spreads rapidly through the tissue.'],
            'answer': 'Gap junctions, because they let ions pass directly between neighbouring cells.',
            'check': 'Tight junctions seal and desmosomes anchor; neither lets ions through, so gap junctions are the only fit ✓.'},
        'mistakes': ['Confusing microtubules with microfilaments.', 'Thinking the cytoskeleton is fixed and rigid.', 'Mixing up tight junctions and gap junctions.', 'Saying animal cells have plasmodesmata.'],
        'real_world': 'The cancer drug paclitaxel (Taxol) stabilises microtubules so the spindle cannot work, stopping cancer cells from dividing.',
        'exam_strategy': 'Learn one example tissue for each junction; examiners often describe the tissue and ask which junction it uses.',
        'recap': ['Three cytoskeleton fibres.', 'Motor proteins walk on microtubules.', 'Cilia: 9 + 2.', 'Tight seal, desmosome anchors, gap connects.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A cell 20 µm wide appears 40 mm wide in a photograph. The magnification is:', ['×2000', '×2', '×200', '×20 000'], 0, '40 000 µm ÷ 20 µm.'),
    Q(T1, 'A 2 µm mitochondrion magnified ×5000 appears:', ['10 mm long', '1 mm long', '100 mm long', '0.4 mm long'], 0, '10 000 µm = 10 mm.'),
    Q(T1, 'Resolution is:', ['the ability to distinguish two close points as separate', 'how many times larger the image is', 'the brightness of the image', 'the size of the specimen'], 0, 'Definition.'),
    Q(T1, 'The surface area to volume ratio of a cube with sides of 3 µm is:', ['2:1', '6:1', '3:1', '1:2'], 0, '54 ÷ 27.'),
    Q(T1, 'Which structure can a light microscope NOT resolve?', ['Ribosomes', 'Nucleus', 'Cell wall', 'Chloroplast'], 0, 'About 25 nm, below 200 nm resolution.'),
    Q(T1, 'One statement of cell theory is that:', ['all cells come from pre-existing cells', 'all cells have a nucleus', 'all cells have a cell wall', 'viruses are the smallest cells'], 0, 'Cells arise by division.'),
    # T2
    Q(T2, 'Prokaryotic cells have:', ['70S ribosomes and circular DNA', 'a nucleus and 80S ribosomes', 'mitochondria', 'linear DNA wrapped on histones'], 0, 'No nucleus.'),
    Q(T2, 'Bacterial cell walls are made of:', ['peptidoglycan', 'cellulose', 'chitin', 'collagen'], 0, 'Murein.'),
    Q(T2, 'Which is found in plant cells but not animal cells?', ['Chloroplasts', 'Mitochondria', 'Ribosomes', 'Golgi apparatus'], 0, 'Plants photosynthesise.'),
    Q(T2, 'Evidence that mitochondria were once free-living bacteria:', ['they have their own circular DNA and 70S ribosomes', 'they make proteins for export', 'they are found in all cells', 'they have no membrane'], 0, 'Endosymbiotic theory.'),
    Q(T2, 'Small extra rings of DNA in bacteria are called:', ['plasmids', 'histones', 'nucleoli', 'centrioles'], 0, 'They often carry antibiotic resistance genes.'),
    Q(T2, 'Typical eukaryotic cells are about:', ['10 to 100 µm', '1 to 5 nm', '1 to 5 mm', '0.1 to 1 µm'], 0, 'Prokaryotes are 1 to 5 µm.'),
    # T3
    Q(T3, 'Proteins for secretion are made on:', ['ribosomes on the rough ER', 'the smooth ER', 'the Golgi apparatus', 'lysosomes'], 0, 'Then sent to the Golgi.'),
    Q(T3, 'The Golgi apparatus:', ['modifies, sorts and packages proteins', 'makes ATP', 'stores DNA', 'carries out photosynthesis'], 0, 'Then vesicles carry them away.'),
    Q(T3, 'Lysosomes contain:', ['hydrolytic enzymes', 'chlorophyll', 'DNA', 'ribosomes'], 0, 'For digestion.'),
    Q(T3, 'Liver cells, which detoxify drugs, have a lot of:', ['smooth ER', 'chloroplasts', 'cilia', 'cell wall'], 0, 'Detoxification and lipid synthesis.'),
    Q(T3, 'Cristae increase the surface area of:', ['the inner mitochondrial membrane', 'the nuclear envelope', 'the cell wall', 'the thylakoid'], 0, 'More area for ATP production.'),
    Q(T3, 'The nucleolus makes:', ['ribosomal RNA', 'ATP', 'lipids', 'lysosomes'], 0, 'rRNA for ribosomes.'),
    # T4
    Q(T4, 'The spindle in cell division is made of:', ['microtubules', 'microfilaments', 'intermediate filaments', 'collagen'], 0, 'Tubulin fibres.'),
    Q(T4, 'Muscle contraction relies on which cytoskeletal protein?', ['Actin', 'Tubulin', 'Keratin', 'Cellulose'], 0, 'Actin and myosin.'),
    Q(T4, 'Which junction lets ions pass directly between neighbouring animal cells?', ['Gap junction', 'Tight junction', 'Desmosome', 'Plasmodesma'], 0, 'Communication channels.'),
    Q(T4, 'Tight junctions:', ['seal neighbouring cells to stop leaks between them', 'let ions pass between cells', 'connect plant cells', 'move cilia'], 0, 'Gut lining.'),
    Q(T4, 'Plant cells communicate through:', ['plasmodesmata', 'gap junctions', 'desmosomes', 'microvilli'], 0, 'Channels through cell walls.'),
    Q(T4, 'Cilia and flagella in eukaryotes have microtubules in a:', ['9 + 2 arrangement', '3 + 3 arrangement', 'single tube', 'random mesh'], 0, 'Dynein bends them.'),
]

FLASH = [
    ['Magnification', 'Image size ÷ actual size (same units).'],
    ['Resolution', 'Ability to distinguish two close points; ~200 nm for light microscopes.'],
    ['Prokaryote', 'No nucleus; circular DNA; 70S ribosomes.'],
    ['Endosymbiotic theory', 'Mitochondria and chloroplasts descend from engulfed prokaryotes.'],
    ['Rough ER', 'Ribosome-studded; makes proteins for export.'],
    ['Golgi apparatus', 'Modifies, sorts and packages proteins into vesicles.'],
    ['Microtubules', 'Tubulin tubes: tracks, spindle, cilia.'],
    ['Gap junction', 'Channel joining the cytoplasm of neighbouring animal cells.'],
]
