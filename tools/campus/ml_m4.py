"""Machine Learning Foundations, module 4: Unsupervised learning."""
import numpy as np
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage
from verify import Q
T1, T2, T3, T4 = ('k-means clustering', 'Hierarchical clustering and distance', 'Principal component analysis', 'Evaluating clusters and finding anomalies')
r = lambda v, d: round(float(v), d)
X = np.array([1, 2, 3, 10, 11, 12.])[:, None]
c = np.array([1., 2.]); lab = np.argmin(abs(X - c), axis=1); c1 = np.array([X[lab == k].mean() for k in range(2)])
assert lab.tolist() == [0, 1, 1, 1, 1, 1] and c1.tolist() == [1, 7.6]
km = KMeans(2, init=np.array([[1.], [2.]]), n_init=1).fit(X)
assert sorted(km.cluster_centers_.ravel().tolist()) == [2, 11] and km.inertia_ == 4
L = linkage(np.array([0, 1, 5, 6, 20.])[:, None], 'single'); assert L[:, 2].tolist() == [1, 1, 4, 14]
Lc = linkage(np.array([0, 1, 5, 6, 20.])[:, None], 'complete'); assert Lc[2, 2] == 6
ev = np.linalg.eigvalsh(np.array([[3, 1], [1, 3.]])); assert ev.tolist() == [2, 4] and r(4 / 6, 3) == 0.667
assert (5 + 3) / (5 + 3 + 1.5 + 0.5) == 0.8 and 5 / 10 == 0.5 and (8 - 2) / 8 == 0.75 and (3 - 6) / 6 == -0.5
assert 100 * 3 == 300

MODULE = {
    'title': 'Unsupervised learning',
    'topics': [T1, T2, T3, T4],
    'overview': 'Unsupervised learning finds structure in data without labels. This module covers k-means and hierarchical clustering for grouping similar observations, principal component analysis for compressing many features into a few, and ways to judge clusters and detect unusual observations.',
    'key_terms': ['Clustering', 'Centroid', 'k-means', 'Within-cluster sum of squares', 'Elbow method', 'Hierarchical clustering', 'Linkage', 'Dendrogram', 'Dimensionality reduction', 'Principal component', 'Explained variance', 'Silhouette score', 'Anomaly', 'Outlier score', 'Curse of dimensionality'],
    'explanation': [
        'Clustering groups observations so that members of a group are similar. k-means alternates between assigning points to the nearest centroid and moving each centroid to the mean of its points; hierarchical clustering repeatedly merges the closest groups and records the merges in a dendrogram.',
        'Principal component analysis finds new axes (principal components) along which the data vary most. Keeping the first few components compresses the data, removes noise and makes visualisation possible, at the cost of some interpretability.',
        'Without labels, quality is judged by internal measures such as the within-cluster sum of squares and the silhouette score, by stability, and above all by whether the groups are useful. Anomaly detection flags observations that fit no normal pattern, such as fraudulent transactions or faulty sensors.'],
    'quick_facts': [
        'k-means: assign to nearest centroid, update centroids, repeat.',
        'Inertia (WCSS) always falls as k grows; use the elbow or silhouette.',
        'Single linkage: closest pair; complete linkage: farthest pair.',
        'PCA: components are eigenvectors of the covariance matrix; variance = eigenvalue.',
        'Silhouette s = (b − a)/max(a, b), from −1 to 1.'],
}

NOTES = {
    T1: {
        'overview': 'k-means is the most widely used clustering algorithm: simple, fast and easy to explain.',
        'key_terms': ['Centroid', 'Assignment step', 'Update step', 'Convergence', 'Inertia (WCSS)', 'k-means++ initialisation', 'Elbow method'],
        'explanation': [
            'Algorithm: choose k starting centroids; assign each point to its nearest centroid; move each centroid to the mean of its assigned points; repeat until nothing changes. Each step lowers the within-cluster sum of squares (WCSS, or inertia).',
            'Example: points 1, 2, 3, 10, 11, 12 with k = 2 and starting centroids 1 and 2. Step 1: only 1 is nearer to 1; the rest go to 2, so the centroids move to 1 and 7.6. Step 2: 1, 2, 3 join the first cluster and 10, 11, 12 the second; centroids 2 and 11. Step 3: no change. WCSS = (1 + 0 + 1) + (1 + 0 + 1) = 4.',
            'k-means can converge to poor solutions from bad starts, so k-means++ initialisation and several restarts are used. Choosing k: WCSS always decreases as k grows, so look for an "elbow" where adding clusters stops helping much, or use silhouette scores. k-means assumes roughly round clusters of similar size and needs scaled features.'],
        'formulas_label': 'Formulas',
        'formulas': ['Assign: cluster(x) = argminₖ ||x − μₖ||', 'Update: μₖ = mean of points in cluster k', 'WCSS = Σₖ Σ_{x in k} ||x − μₖ||²'],
        'steps': ['Scale features.', 'Choose k and initial centroids.', 'Alternate assignment and update until stable.', 'Compare WCSS or silhouette across k values.'],
        'worked_example': {
            'problem': 'Run k-means (k = 2) on 1, 2, 3, 10, 11, 12 from centroids 1 and 2.',
            'steps': ['Assign: {1} and {2, 3, 10, 11, 12}; update: 1 and 7.6.', 'Assign: {1, 2, 3} and {10, 11, 12}; update: 2 and 11.', 'Assign again: no change, so stop.'],
            'answer': 'Clusters {1, 2, 3} and {10, 11, 12} with centroids 2 and 11; WCSS = 4.',
            'check': 'scikit-learn\'s KMeans from the same start gives centroids 2 and 11 and inertia 4 ✓.'},
        'mistakes': ['Not scaling features.', 'Choosing k by minimising WCSS (it always prefers more clusters).', 'Running k-means once from one random start.', 'Using k-means for long, curved or very unequal clusters.'],
        'real_world': 'Retailers cluster customers by spending patterns to design targeted promotions.',
        'exam_strategy': 'Show a small table of each iteration: assignments, then new centroids.',
        'recap': ['Assign and update.', 'WCSS falls.', 'Initialisation matters.', 'Choose k carefully.']},
    T2: {
        'overview': 'Hierarchical clustering builds a tree of nested clusters, so you can choose the number of clusters after seeing the structure.',
        'key_terms': ['Agglomerative clustering', 'Distance matrix', 'Single linkage', 'Complete linkage', 'Average linkage', 'Ward\'s method', 'Dendrogram', 'Cutting the tree'],
        'explanation': [
            'Agglomerative clustering starts with every point as its own cluster and repeatedly merges the two closest clusters. "Closest" depends on the linkage: single linkage uses the nearest pair of points, complete linkage the farthest pair, average linkage the mean distance, and Ward\'s method the merge that least increases within-cluster variance.',
            'Points 0, 1, 5, 6, 20: first {0, 1} and {5, 6} merge at distance 1. Under single linkage, those two clusters merge at distance 4 (from 1 to 5); under complete linkage at 6 (from 0 to 6). Finally 20 joins at 14 (single linkage, from 6 to 20).',
            'A dendrogram shows the merges and their heights; cutting it at a chosen height gives the clusters (cutting between 4 and 14 here gives {0, 1, 5, 6} and {20}). Single linkage can create long "chains"; complete and Ward give more compact clusters. Hierarchical methods need all pairwise distances, so they suit small and medium datasets.'],
        'formulas_label': 'Linkage rules',
        'formulas': ['Single: min distance between members', 'Complete: max distance between members', 'Average: mean pairwise distance', 'Ward: smallest increase in WCSS'],
        'steps': ['Compute pairwise distances (after scaling).', 'Merge the closest pair of clusters.', 'Update distances with the linkage rule.', 'Draw the dendrogram and cut it.'],
        'worked_example': {
            'problem': 'Cluster 0, 1, 5, 6, 20 with single linkage. At what heights do the merges happen?',
            'steps': ['Merge 0 and 1 (distance 1), and 5 and 6 (distance 1).', 'Merge {0, 1} with {5, 6}: closest pair 1 and 5, distance 4.', 'Merge with 20: closest pair 6 and 20, distance 14.'],
            'answer': 'Heights 1, 1, 4 and 14.',
            'check': 'SciPy\'s linkage function gives merge heights 1, 1, 4, 14 ✓.'},
        'mistakes': ['Forgetting to scale before computing distances.', 'Confusing single and complete linkage.', 'Reading the horizontal order of a dendrogram as meaningful.', 'Using hierarchical clustering on millions of points.'],
        'real_world': 'Biologists use hierarchical clustering to group genes with similar expression patterns and to draw family trees of species.',
        'exam_strategy': 'Keep an updated distance table after each merge; the next merge is its smallest entry.',
        'recap': ['Merge closest clusters.', 'Linkage choices.', 'Dendrogram.', 'Cut to choose clusters.']},
    T3: {
        'overview': 'Principal component analysis compresses many correlated features into a few uncorrelated components that keep most of the variation.',
        'key_terms': ['Dimensionality reduction', 'Covariance matrix', 'Eigenvector', 'Eigenvalue', 'Principal component', 'Explained variance ratio', 'Scree plot', 'Loadings'],
        'explanation': [
            'PCA centres (and usually standardises) the data, then finds the directions of greatest variance: the eigenvectors of the covariance matrix. Each eigenvalue is the variance along its component.',
            'For covariance matrix [[3, 1], [1, 3]] the eigenvalues are 4 and 2, with eigenvectors along (1, 1)/√2 and (1, −1)/√2. The first component explains 4/(4 + 2) ≈ 66.7% of the variance. With eigenvalues 5, 3, 1.5 and 0.5, the first two components explain (5 + 3)/10 = 80%.',
            'Keep enough components to explain most variance (a scree plot helps), or two or three for plotting. Components are combinations of original features, so they are harder to interpret; loadings show each feature\'s weight. PCA captures only linear structure, and features with large scales dominate unless standardised.'],
        'formulas_label': 'Formulas',
        'formulas': ['Components = eigenvectors of the covariance matrix', 'Variance along component = eigenvalue', 'Explained ratio = λᵢ/Σλ', 'Projection: z = Vᵀ(x − μ)'],
        'steps': ['Standardise the features.', 'Compute the covariance matrix.', 'Find eigenvalues and eigenvectors.', 'Keep the top components and project the data.'],
        'worked_example': {
            'problem': 'Eigenvalues of a covariance matrix are 5, 3, 1.5 and 0.5. How many components explain at least 80% of the variance?',
            'steps': ['Total variance = 10.', 'First component: 50%; first two: 80%.', 'Two components reach 80%.'],
            'answer': 'Two components.',
            'check': 'Three would explain 95%, so the gain from the third is 15 points ✓.'},
        'mistakes': ['Running PCA on unscaled features with different units.', 'Interpreting components as original features.', 'Fitting PCA on all data before a train–test split.', 'Assuming PCA finds clusters.'],
        'real_world': 'Face-recognition systems once used PCA "eigenfaces" to represent images with a few dozen numbers instead of thousands of pixels.',
        'exam_strategy': 'Explained variance questions only need the eigenvalues: divide each by their sum.',
        'recap': ['Directions of most variance.', 'Eigenvalues = variance.', 'Explained ratio.', 'Standardise first.']},
    T4: {
        'overview': 'Without labels, you need other ways to judge clusters, and to spot the unusual points that matter most.',
        'key_terms': ['Silhouette score', 'Cohesion', 'Separation', 'Cluster stability', 'Anomaly detection', 'Isolation forest', 'Distance-based outliers', 'Curse of dimensionality'],
        'explanation': [
            'The silhouette of a point compares a, its mean distance to its own cluster, with b, its mean distance to the nearest other cluster: s = (b − a)/max(a, b). With a = 2 and b = 8, s = 0.75 (well clustered); with a = 6 and b = 3, s = −0.5 (probably in the wrong cluster). Averaging over points helps choose k.',
            'Good clusters are also stable (similar when the data are resampled) and useful (they lead to different actions). A segmentation that marketing cannot act on is not a good segmentation, whatever its score.',
            'Anomaly detection flags rare, unusual observations: simple rules (z-score above 3), distance to the nearest neighbours, or isolation forests, which isolate anomalies in few random splits. In high dimensions distances become similar (the curse of dimensionality), so reduce dimensions or choose features carefully. Flagged anomalies should be reviewed by people; with 100 000 daily transactions, even a 0.3% flag rate means 300 cases to check.'],
        'formulas_label': 'Formulas',
        'formulas': ['Silhouette s = (b − a)/max(a, b)', 's near 1: well clustered; near 0: on a boundary; negative: misassigned', 'Simple anomaly rule: |z| > 3'],
        'steps': ['Compute internal scores (WCSS, silhouette) for several k.', 'Check stability on resamples.', 'Ask whether clusters are actionable.', 'For anomalies, score, rank and review the top cases.'],
        'worked_example': {
            'problem': 'A point has mean distance 2 to its own cluster and 8 to the nearest other cluster. Find its silhouette.',
            'steps': ['a = 2, b = 8.', 's = (8 − 2)/max(2, 8).', '= 6/8 = 0.75.'],
            'answer': '0.75: the point sits comfortably in its cluster.',
            'check': 'If a and b were equal, s would be 0, on the boundary ✓.'},
        'mistakes': ['Judging clusters only by a score.', 'Treating every anomaly as an error to delete.', 'Using raw distances in very high dimensions.', 'Forgetting the human review workload of anomaly flags.'],
        'real_world': 'Electricity utilities use anomaly detection on smart-meter data to spot faults and illegal connections.',
        'exam_strategy': 'For silhouette questions, identify a and b explicitly before substituting.',
        'recap': ['Silhouette.', 'Stability and usefulness.', 'Anomaly methods.', 'Curse of dimensionality.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'k-means alternates between:', ['assigning points to the nearest centroid and recomputing centroids', 'splitting and merging trees', 'gradient steps and pruning', 'labelling and testing'], 0, 'Two steps.'),
    Q(T1, 'Points 1, 2, 3, 10, 11, 12 with starting centroids 1 and 2: after the first update the centroids are:', ['1 and 7.6', '2 and 11', '1.5 and 9', '1 and 2'], 0, '{1} and the rest.'),
    Q(T1, 'The final centroids are:', ['2 and 11', '1 and 7.6', '3 and 10', '6.5 and 6.5'], 0, '{1, 2, 3}, {10, 11, 12}.'),
    Q(T1, 'The final within-cluster sum of squares is:', ['4', '2', '0', '8'], 0, '2 + 2.', ans=4, num=True),
    Q(T1, 'As k increases, WCSS:', ['never increases', 'always increases', 'stays constant', 'becomes negative'], 0, 'More centroids.'),
    Q(T1, 'k-means++ is used to:', ['choose better starting centroids', 'pick k automatically', 'label the data', 'reduce dimensions'], 0, 'Initialisation.'),
    # T2
    Q(T2, 'Single linkage measures the distance between clusters by:', ['the closest pair of points', 'the farthest pair', 'the centroids only', 'the number of points'], 0, 'Minimum.'),
    Q(T2, 'For points 0, 1, 5, 6, 20, single linkage merges {0, 1} and {5, 6} at distance:', ['4', '6', '5', '1'], 0, '1 to 5.', ans=4, num=True),
    Q(T2, 'Under complete linkage, the same merge happens at distance:', ['6', '4', '5', '14'], 0, '0 to 6.', ans=6, num=True),
    Q(T2, 'Point 20 joins (single linkage) at distance:', ['14', '19', '20', '15'], 0, '6 to 20.', ans=14, num=True),
    Q(T2, 'A dendrogram is:', ['a tree diagram of cluster merges', 'a scatter plot', 'an ROC curve', 'a confusion matrix'], 0, 'Merge heights.'),
    Q(T2, 'Cutting that dendrogram between heights 4 and 14 gives:', ['2 clusters', '5 clusters', '1 cluster', '3 clusters'], 0, '{0, 1, 5, 6} and {20}.'),
    # T3
    Q(T3, 'PCA components are the eigenvectors of the:', ['covariance matrix', 'confusion matrix', 'distance matrix', 'identity matrix'], 0, 'Directions of variance.'),
    Q(T3, 'Covariance matrix [[3, 1], [1, 3]] has eigenvalues:', ['4 and 2', '3 and 3', '3 and 1', '6 and 0'], 0, '3 ± 1.'),
    Q(T3, 'The first component then explains about:', ['66.7% of the variance', '50%', '75%', '100%'], 0, '4/6.'),
    Q(T3, 'Eigenvalues 5, 3, 1.5, 0.5: the first two components explain:', ['80%', '50%', '95%', '30%'], 0, '8/10.'),
    Q(T3, 'Before PCA, features in different units should be:', ['standardised', 'squared', 'one-hot encoded', 'left alone'], 0, 'Otherwise scale dominates.'),
    Q(T3, 'A drawback of PCA is that components:', ['are harder to interpret than original features', 'always lose all information', 'require labels', 'cannot be plotted'], 0, 'Mixtures of features.'),
    # T4
    Q(T4, 'With a = 2 and b = 8, the silhouette is:', ['0.75', '0.25', '4', '−0.75'], 0, '6/8.', ans=0.75, num=True),
    Q(T4, 'With a = 6 and b = 3, the silhouette is:', ['−0.5', '0.5', '0.33', '−2'], 0, '−3/6.', ans=-0.5, num=True),
    Q(T4, 'A negative silhouette suggests the point is:', ['probably in the wrong cluster', 'perfectly clustered', 'an exact centroid', 'missing'], 0, 'Closer to another cluster.'),
    Q(T4, 'A simple anomaly rule flags values with:', ['|z| > 3', '|z| < 1', 'z = 0', 'positive z only'], 0, 'Very unusual.'),
    Q(T4, 'Flagging 0.3% of 100 000 daily transactions means reviewing about:', ['300 cases', '30 cases', '3000 cases', '3 cases'], 0, '0.003 × 100 000.'),
    Q(T4, 'In very high dimensions, distances between points tend to:', ['become similar, weakening distance-based methods', 'become more varied', 'become zero', 'become negative'], 0, 'Curse of dimensionality.'),
]

FLASH = [
    ['k-means', 'Assign to nearest centroid, move centroids to means, repeat.'],
    ['Choosing k', 'Elbow in WCSS or highest silhouette; check usefulness.'],
    ['Single vs complete linkage', 'Closest pair vs farthest pair.'],
    ['Dendrogram', 'Tree of merges; cut it to get clusters.'],
    ['PCA', 'Eigenvectors of covariance; eigenvalues are variances.'],
    ['Explained variance ratio', 'λᵢ/Σλ.'],
    ['Silhouette', '(b − a)/max(a, b), from −1 to 1.'],
    ['Anomaly detection', 'Flag rare, unusual points for review (z-score, distances, isolation forest).'],
]
