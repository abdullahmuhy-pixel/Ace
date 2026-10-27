"""Cell Biology, module 3: Membranes, transport and signalling."""
from verify import Q
T1, T2, T3, T4 = ('Membrane structure', 'Diffusion and osmosis', 'Active transport and bulk transport', 'Cell signalling')
assert round((2.3 - 2.0) / 2.0 * 100, 6) == 15 and round((1.6 - 2.0) / 2.0 * 100, 6) == -20
assert -400 > -700
assert -300 + 200 == -100
assert 3 * 2 == 6

MODULE = {
    'title': 'Membranes, transport and signalling',
    'topics': [T1, T2, T3, T4],
    'overview': 'Every cell is wrapped in a membrane that controls what enters and leaves and how the cell receives messages. This module covers the fluid mosaic model, passive transport by diffusion and osmosis, active and bulk transport, and how signals cross the membrane to change what a cell does.',
    'key_terms': ['Fluid mosaic model', 'Phospholipid bilayer', 'Channel protein', 'Carrier protein', 'Diffusion', 'Facilitated diffusion', 'Osmosis', 'Water potential', 'Active transport', 'Endocytosis', 'Exocytosis', 'Receptor', 'Second messenger'],
    'explanation': [
        'Membranes are a phospholipid bilayer with proteins floating in it, the fluid mosaic model. Small non-polar molecules cross directly; ions and polar molecules need protein channels or carriers.',
        'Passive transport moves substances down their concentration gradient without ATP: simple diffusion, facilitated diffusion and osmosis (water moving from higher to lower water potential). Active transport uses ATP to pump substances against their gradient, and bulk transport moves large amounts in vesicles.',
        'Signalling molecules such as hormones bind receptors. Non-polar signals like steroids cross the membrane; polar ones bind surface receptors that trigger a cascade inside the cell, often amplifying the signal through second messengers.'],
    'quick_facts': [
        'Passive: no ATP, down the gradient. Active: ATP, against the gradient.',
        'Osmosis: water moves from higher (less negative) to lower (more negative) water potential.',
        'Pure water has Ψ = 0; solutions are negative.',
        'Na⁺/K⁺ pump: 3 Na⁺ out, 2 K⁺ in per ATP.',
        'Steroid hormones: receptors inside the cell; peptide hormones: surface receptors.'],
}

NOTES = {
    T1: {
        'overview': 'The fluid mosaic model describes membranes as a flexible bilayer of phospholipids with a mosaic of proteins, cholesterol and carbohydrates.',
        'key_terms': ['Phospholipid bilayer', 'Integral protein', 'Peripheral protein', 'Channel protein', 'Carrier protein', 'Cholesterol', 'Glycoprotein', 'Glycolipid', 'Selectively permeable'],
        'explanation': [
            'Phospholipids arrange with hydrophilic heads facing the watery inside and outside of the cell and hydrophobic tails inside. The layer is fluid: molecules move sideways. Its hydrophobic core blocks ions and most polar molecules, making the membrane selectively permeable.',
            'Proteins form the mosaic. Integral proteins span the bilayer and include channels (pores for specific ions) and carriers (which change shape to move molecules). Peripheral proteins sit on the surface, often as enzymes or anchors to the cytoskeleton. Glycoproteins and glycolipids carry carbohydrate chains on the outer surface, acting as receptors and recognition markers, such as the ABO blood group antigens.',
            'Cholesterol sits between phospholipids in animal membranes and buffers fluidity: it stops the membrane becoming too fluid when warm and too rigid when cold. Unsaturated fatty acid tails, with their kinks, also increase fluidity. High temperatures and organic solvents disrupt membranes and make them leaky.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Bilayer: heads out, tails in', 'Channel: pore; carrier: changes shape', 'Glycoproteins: recognition and receptors', 'Cholesterol: regulates fluidity'],
        'steps': ['Name the component.', 'State where it sits in the membrane.', 'Give its function.', 'Explain the effect of temperature if asked.'],
        'worked_example': {
            'problem': 'Beetroot pieces were placed in water at different temperatures. Above about 50 °C, the water turned red much faster. Explain.',
            'steps': ['The red pigment is held inside the vacuole by membranes.', 'High temperature increases phospholipid movement and denatures membrane proteins, making gaps.', 'The membranes become more permeable, so pigment leaks out.'],
            'answer': 'Heat disrupts the bilayer and denatures membrane proteins, so the membranes leak pigment.',
            'check': 'The sudden rise near 50 °C matches the temperature at which many proteins denature ✓.'},
        'mistakes': ['Drawing tails facing the water.', 'Saying the membrane is rigid.', 'Saying cholesterol is found in all membranes (it is mainly in animal cells).', 'Confusing channel and carrier proteins.'],
        'real_world': 'Cystic fibrosis is caused by a faulty chloride channel protein (CFTR), which leads to thick, sticky mucus in the lungs.',
        'exam_strategy': 'Draw and label a short section of membrane even when not asked; it makes your explanation clearer and often earns marks.',
        'recap': ['Phospholipid bilayer.', 'Proteins: channels, carriers, receptors.', 'Cholesterol buffers fluidity.', 'Selectively permeable.']},
    T2: {
        'overview': 'Diffusion and osmosis move substances passively, down a gradient, using only the kinetic energy of molecules.',
        'key_terms': ['Concentration gradient', 'Simple diffusion', 'Facilitated diffusion', 'Fick\'s law', 'Osmosis', 'Water potential (Ψ)', 'Isotonic', 'Hypotonic', 'Hypertonic', 'Turgid', 'Plasmolysis'],
        'explanation': [
            'Simple diffusion is the net movement of particles from high to low concentration; oxygen and carbon dioxide cross membranes this way. Facilitated diffusion uses channel or carrier proteins for polar molecules and ions such as glucose and Na⁺. Fick\'s law: rate ∝ surface area × concentration difference ÷ thickness of the barrier, which is why lungs have a huge, thin surface.',
            'Osmosis is the net movement of water across a partially permeable membrane from higher to lower water potential (Ψ). Pure water has Ψ = 0 kPa; adding solutes makes it negative. If a cell has Ψ = −700 kPa and the solution around it is −400 kPa, water enters the cell.',
            'Animal cells in a hypotonic solution swell and may burst (lysis); in a hypertonic solution they shrink. Plant cells gain water until the wall pushes back (turgid) and lose water until the membrane pulls away from the wall (plasmolysis). In a classic experiment, potato pieces that change from 2.0 g to 2.3 g gained 15% of their mass, so the solution had a higher water potential than the potato.'],
        'formulas_label': 'Formulas',
        'formulas': ['Rate of diffusion ∝ (surface area × concentration difference) ÷ thickness', 'Ψ = Ψs + Ψp', 'Pure water: Ψ = 0; solutions: Ψ < 0', '% change in mass = (final − initial)/initial × 100'],
        'steps': ['Find the water potential on each side.', 'Water moves towards the more negative Ψ.', 'Predict the effect on the cell.', 'For experiments, use % change in mass.'],
        'worked_example': {
            'problem': 'Potato cylinders of 2.0 g were placed in sucrose solutions. In 0.1 mol/L they became 2.3 g; in 0.8 mol/L they became 1.6 g. Calculate each % change and explain.',
            'steps': ['0.1 mol/L: (2.3 − 2.0)/2.0 × 100 = +15%. Water entered by osmosis, so the solution had a higher Ψ than the cells.', '0.8 mol/L: (1.6 − 2.0)/2.0 × 100 = −20%. Water left, so the solution had a lower Ψ.', 'The concentration with 0% change (isotonic) lies between them; plotting a graph finds it.'],
            'answer': '+15% and −20%.',
            'check': 'Mass gain in the dilute solution and loss in the concentrated one match expectations ✓.'},
        'mistakes': ['Saying water moves from low to high water potential.', 'Describing osmosis as movement of solute.', 'Forgetting that a more negative Ψ means less free water.', 'Using absolute mass changes when pieces start at different masses.'],
        'real_world': 'Hospital drips use saline isotonic with blood (0.9% NaCl); pure water injected into veins would make red blood cells swell and burst.',
        'exam_strategy': 'Always use the phrase "from a higher water potential to a lower water potential across a partially permeable membrane" in osmosis answers.',
        'recap': ['Diffusion: down the gradient.', 'Facilitated: through proteins, still passive.', 'Osmosis: water, high to low Ψ.', 'Use % change in mass.']},
    T3: {
        'overview': 'Active transport uses ATP to move substances against their concentration gradient. Bulk transport moves large particles or volumes in vesicles.',
        'key_terms': ['Active transport', 'Carrier protein (pump)', 'ATP', 'Sodium–potassium pump', 'Co-transport', 'Endocytosis', 'Phagocytosis', 'Pinocytosis', 'Exocytosis'],
        'explanation': [
            'Active transport moves molecules or ions from low to high concentration using carrier proteins (pumps) and energy from ATP hydrolysis. Root hair cells take up mineral ions from dilute soil this way; cells that do a lot of active transport contain many mitochondria. Inhibitors of respiration, such as cyanide, stop active transport.',
            'The sodium–potassium pump moves 3 Na⁺ out and 2 K⁺ in for each ATP used, keeping the inside of the cell negative and setting up gradients that nerve cells use for impulses. Co-transport uses one gradient to drive another: in the gut, Na⁺ flowing back into cells carries glucose with it against its own gradient.',
            'Bulk transport uses vesicles. In endocytosis the membrane folds in to engulf material: phagocytosis takes in solids (white blood cells engulfing bacteria) and pinocytosis takes in fluid. In exocytosis vesicles fuse with the membrane to release contents, such as hormones or neurotransmitters. Both need ATP.'],
        'formulas_label': 'Comparison',
        'formulas': ['Diffusion: down gradient, no ATP, no protein', 'Facilitated diffusion: down gradient, no ATP, protein', 'Active transport: against gradient, ATP, carrier protein', 'Na⁺/K⁺ pump: 3 Na⁺ out, 2 K⁺ in per ATP'],
        'steps': ['Check the direction relative to the gradient.', 'Check whether ATP is needed.', 'Check whether a protein is involved.', 'Name the process.'],
        'worked_example': {
            'problem': 'Root cells take up nitrate even when its concentration in the root is higher than in the soil. When the roots are treated with a respiratory poison, uptake stops. Explain.',
            'steps': ['Uptake against a concentration gradient must be active transport.', 'Active transport needs ATP from respiration.', 'The poison stops respiration, so no ATP is made and the pumps stop.'],
            'answer': 'Nitrate is taken up by active transport, which depends on ATP from respiration.',
            'check': 'If it were diffusion, the poison would have no effect ✓.'},
        'mistakes': ['Saying active transport moves substances "along" the gradient.', 'Calling facilitated diffusion active because it uses proteins.', 'Getting the Na⁺/K⁺ pump numbers backwards.', 'Forgetting bulk transport uses ATP.'],
        'real_world': 'The drug digoxin, used for heart failure, partly blocks the Na⁺/K⁺ pump in heart cells, increasing the force of contraction.',
        'exam_strategy': 'Look for clues: "against a gradient" or "affected by respiratory inhibitors" both point to active transport.',
        'recap': ['Active: ATP, against the gradient.', 'Na⁺/K⁺ pump: 3 out, 2 in.', 'Co-transport uses one gradient for another.', 'Endo- and exocytosis use vesicles.']},
    T4: {
        'overview': 'Cells communicate with chemical signals. A signal binds a receptor, the message is relayed and amplified inside the cell, and the cell responds.',
        'key_terms': ['Ligand', 'Receptor', 'Signal transduction', 'G-protein-coupled receptor', 'Second messenger', 'cAMP', 'Kinase', 'Amplification', 'Intracellular receptor'],
        'explanation': [
            'Cell signalling has three stages: reception (a ligand binds a specific receptor), transduction (the message is relayed through a chain of molecules) and response (the cell changes, for example by activating an enzyme or switching on a gene). The receptor\'s shape is complementary to its ligand, so only cells with the right receptor respond.',
            'Polar signals such as adrenaline and insulin cannot cross the membrane and bind surface receptors. Many act through G-protein-coupled receptors: adrenaline binding activates a G protein, which activates adenylyl cyclase to make cyclic AMP (cAMP), the second messenger. cAMP activates protein kinases, which phosphorylate other proteins in a cascade.',
            'Each step activates many molecules at the next step, so one hormone molecule can trigger the breakdown of millions of glycogen units: amplification. Non-polar signals such as steroid hormones (oestrogen, testosterone) cross the membrane and bind intracellular receptors, which then act directly on genes.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Reception → transduction → response', 'Polar ligand → surface receptor → second messenger', 'Steroid → intracellular receptor → gene expression', 'Cascades amplify the signal'],
        'steps': ['Decide if the signal is polar or non-polar.', 'Locate the receptor.', 'Trace the relay steps.', 'State the response.'],
        'worked_example': {
            'problem': 'Explain how a small amount of adrenaline can quickly raise blood glucose.',
            'steps': ['Adrenaline binds a G-protein-coupled receptor on liver cells.', 'The G protein activates adenylyl cyclase, which makes many cAMP molecules.', 'cAMP activates a kinase cascade; each enzyme activates many others, so huge numbers of glycogen phosphorylase molecules break down glycogen to glucose.'],
            'answer': 'Through a second-messenger cascade that amplifies the signal at each step.',
            'check': 'The answer covers reception, transduction and response ✓.'},
        'mistakes': ['Saying adrenaline enters the cell.', 'Thinking the hormone itself breaks down glycogen.', 'Confusing first and second messengers.', 'Saying all receptors are on the surface.'],
        'real_world': 'Cholera toxin locks a G protein in its "on" state; cAMP stays high in gut cells, which pump out chloride and water, causing severe diarrhoea.',
        'exam_strategy': 'Use the three words reception, transduction and response as the skeleton of any signalling answer.',
        'recap': ['Ligand binds a specific receptor.', 'Second messengers relay the message.', 'Cascades amplify.', 'Steroids act inside the cell.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'In the bilayer, the phospholipid tails face:', ['each other, inside the membrane', 'the watery cytoplasm', 'the outside of the cell', 'the cell wall'], 0, 'Hydrophobic tails avoid water.'),
    Q(T1, 'The role of cholesterol in animal membranes is to:', ['regulate membrane fluidity', 'pump ions', 'store energy', 'act as a receptor for hormones'], 0, 'Buffers fluidity.'),
    Q(T1, 'Glycoproteins on the membrane surface often act as:', ['receptors and recognition markers', 'energy stores', 'pumps for Na⁺', 'cell wall components'], 0, 'For example blood group antigens.'),
    Q(T1, 'Ions cannot easily cross the bilayer because:', ['its core is hydrophobic', 'they are too large', 'the membrane has pores everywhere', 'they are non-polar'], 0, 'Charged particles are repelled.'),
    Q(T1, 'A carrier protein differs from a channel protein in that it:', ['changes shape to move molecules across', 'forms a permanently open pore', 'is not specific', 'is found only in plants'], 0, 'Carriers bind and flip.'),
    Q(T1, 'Above about 50 °C, membranes become leaky mainly because:', ['membrane proteins denature and the bilayer is disrupted', 'cholesterol is made', 'phospholipids turn into proteins', 'osmosis stops'], 0, 'Beetroot experiment.'),
    # T2
    Q(T2, 'A cell has Ψ = −700 kPa and is placed in a solution of Ψ = −400 kPa. Water moves:', ['into the cell', 'out of the cell', 'neither way', 'only through the cell wall'], 0, 'From higher (less negative) to lower Ψ.'),
    Q(T2, 'The water potential of pure water is:', ['0 kPa', '−100 kPa', '100 kPa', '−1000 kPa'], 0, 'Solutions are negative.'),
    Q(T2, 'A 2.0 g potato piece becomes 2.3 g. The percentage change in mass is:', ['+15%', '+30%', '+0.3%', '−15%'], 0, '0.3/2.0 × 100.', ans=15),
    Q(T2, 'Facilitated diffusion:', ['uses channel or carrier proteins but no ATP', 'uses ATP', 'moves substances against the gradient', 'needs vesicles'], 0, 'Passive.'),
    Q(T2, 'Doubling the thickness of an exchange surface (other things equal) makes the rate of diffusion:', ['halve', 'double', 'stay the same', 'quadruple'], 0, 'Fick\'s law.'),
    Q(T2, 'Red blood cells placed in pure water:', ['swell and may burst', 'shrink', 'become plasmolysed', 'stay the same'], 0, 'Hypotonic surroundings.'),
    # T3
    Q(T3, 'Active transport moves substances:', ['against their concentration gradient using ATP', 'down their gradient without ATP', 'only through the bilayer', 'only in vesicles'], 0, 'Definition.'),
    Q(T3, 'For each ATP, the Na⁺/K⁺ pump moves:', ['3 Na⁺ out and 2 K⁺ in', '2 Na⁺ out and 3 K⁺ in', '3 Na⁺ in and 2 K⁺ out', '1 Na⁺ out and 1 K⁺ in'], 0, 'Keeps the inside negative.'),
    Q(T3, 'A respiratory poison stops ion uptake by roots. This shows uptake is by:', ['active transport', 'simple diffusion', 'osmosis', 'facilitated diffusion'], 0, 'It needs ATP.'),
    Q(T3, 'A white blood cell engulfing a bacterium is an example of:', ['phagocytosis', 'pinocytosis', 'exocytosis', 'osmosis'], 0, '"Cell eating".'),
    Q(T3, 'Glucose absorption in the gut using the Na⁺ gradient is called:', ['co-transport', 'osmosis', 'exocytosis', 'simple diffusion'], 0, 'Na⁺ and glucose move together.'),
    Q(T3, 'Release of a hormone in vesicles that fuse with the membrane is:', ['exocytosis', 'endocytosis', 'phagocytosis', 'facilitated diffusion'], 0, 'Vesicle fuses outward.'),
    # T4
    Q(T4, 'The three stages of cell signalling are:', ['reception, transduction, response', 'diffusion, osmosis, transport', 'transcription, translation, folding', 'binding, digestion, release'], 0, 'Standard model.'),
    Q(T4, 'Adrenaline acts through a surface receptor because it:', ['is polar and cannot cross the bilayer', 'is a steroid', 'is too small', 'is an enzyme'], 0, 'Polar ligands stay outside.'),
    Q(T4, 'A common second messenger is:', ['cyclic AMP', 'adrenaline', 'glucose', 'cholesterol'], 0, 'Made by adenylyl cyclase.'),
    Q(T4, 'Steroid hormones bind receptors:', ['inside the cell', 'only on the cell surface', 'in the cell wall', 'on ribosomes'], 0, 'They cross the membrane.'),
    Q(T4, 'Signal amplification means:', ['each step activates many molecules at the next step', 'the hormone is copied', 'the receptor grows larger', 'the cell divides'], 0, 'Cascades multiply the effect.'),
    Q(T4, 'Only certain cells respond to a hormone because:', ['only they have the specific receptor', 'the hormone only travels to them', 'other cells destroy it', 'they are larger'], 0, 'Complementary shapes.'),
]

FLASH = [
    ['Fluid mosaic model', 'Phospholipid bilayer with proteins floating in it.'],
    ['Cholesterol', 'Regulates fluidity of animal membranes.'],
    ['Facilitated diffusion', 'Passive movement through channel or carrier proteins.'],
    ['Osmosis', 'Water from higher to lower water potential across a partially permeable membrane.'],
    ['Water potential', 'Ψ; pure water 0 kPa, solutions negative.'],
    ['Active transport', 'Carrier proteins use ATP to move substances against a gradient.'],
    ['Endocytosis', 'Membrane folds in to take material into vesicles.'],
    ['Second messenger', 'Molecule such as cAMP that relays a signal inside the cell.'],
]
