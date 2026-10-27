"""Discrete Mathematics and Logic, module 5: Graphs and trees."""
import heapq
import math
from verify import Q, n, sp
T1, T2, T3, T4 = ('Graph basics', 'Euler and Hamilton paths', 'Trees', 'Graph algorithms and colouring')
E = {('A', 'B'): 4, ('A', 'C'): 2, ('C', 'B'): 1, ('B', 'D'): 5, ('C', 'D'): 8, ('C', 'E'): 10, ('D', 'E'): 2}
G = {}
for (u, v), w in E.items(): G.setdefault(u, []).append((v, w)); G.setdefault(v, []).append((u, w))
dist = {'A': 0}; pq = [(0, 'A')]
while pq:
    du, u = heapq.heappop(pq)
    for v, w in G[u]:
        if du + w < dist.get(v, 1e9): dist[v] = du + w; heapq.heappush(pq, (dist[v], v))
assert dist == {'A': 0, 'B': 3, 'C': 2, 'D': 8, 'E': 10}
par = {v: v for v in G}
def root(a):
    while par[a] != a: a = par[a]
    return a
mst = 0
for (u, v), w in sorted(E.items(), key=lambda z: z[1]):
    if root(u) != root(v): par[root(u)] = root(v); mst += w
assert mst == 10
assert sum([3, 3, 2, 2, 2]) // 2 == 6 and 5 * 4 // 2 == 10 and 3 * 3 == 9 and math.factorial(4) // 2 == 12
assert 4 ** (4 - 2) == 16 and 2 ** (3 + 1) - 1 == 15 and 2 * 5 + 1 == 11 and 8 - 12 + 6 == 2

MODULE = {
    'title': 'Graphs and trees',
    'topics': [T1, T2, T3, T4],
    'overview': 'Graphs model networks of every kind: roads, social networks, the internet and dependencies in software. This module covers the language of graphs, Euler and Hamilton routes, trees, and the classic algorithms for shortest paths, spanning trees and colouring.',
    'key_terms': ['Graph', 'Vertex', 'Edge', 'Degree', 'Handshake lemma', 'Complete graph', 'Bipartite graph', 'Path', 'Cycle', 'Connected', 'Euler circuit', 'Hamilton cycle', 'Tree', 'Spanning tree', 'Dijkstra\'s algorithm', 'Minimum spanning tree', 'Chromatic number', 'Planar graph'],
    'explanation': [
        'A graph is a set of vertices joined by edges. The degree of a vertex is the number of edges touching it, and the sum of all degrees is twice the number of edges (the handshake lemma). Special graphs include complete graphs Kₙ, cycles and bipartite graphs.',
        'An Euler circuit uses every edge exactly once, and exists exactly when the graph is connected and every degree is even; a Hamilton cycle visits every vertex exactly once, and no simple test is known. Trees are connected graphs with no cycles; they always have n − 1 edges.',
        'Algorithms answer practical questions: breadth-first and depth-first search explore graphs, Dijkstra\'s algorithm finds shortest paths, Kruskal\'s and Prim\'s algorithms find cheapest connecting networks, and colouring assigns resources without conflicts.'],
    'quick_facts': [
        'Σ deg(v) = 2|E|, so the number of odd-degree vertices is even.',
        'Kₙ has n(n − 1)/2 edges.',
        'Euler circuit ⇔ connected and all degrees even; Euler path ⇔ exactly 0 or 2 odd vertices.',
        'A tree with n vertices has n − 1 edges.',
        'Planar connected graphs: V − E + F = 2.'],
}

NOTES = {
    T1: {
        'overview': 'Graphs are made of vertices and edges. A few counting facts describe them.',
        'key_terms': ['Vertex', 'Edge', 'Simple graph', 'Degree', 'Handshake lemma', 'Complete graph Kₙ', 'Bipartite graph', 'Adjacency matrix', 'Connected'],
        'explanation': [
            'Each edge adds 1 to the degree of each of its two ends, so Σ deg(v) = 2|E|. A graph with degrees 3, 3, 2, 2, 2 has 12/2 = 6 edges. It follows that every graph has an even number of odd-degree vertices: no graph can have degrees 3, 2, 2.',
            'The complete graph Kₙ joins every pair of n vertices: n(n − 1)/2 edges, so K₅ has 10. A bipartite graph splits the vertices into two groups with edges only between the groups; K₃,₃ has 3 × 3 = 9 edges.',
            'Graphs are stored as adjacency matrices (an n × n table of 0s and 1s, symmetric for undirected graphs) or adjacency lists (good for sparse graphs). A graph is connected if every pair of vertices is joined by a path.'],
        'formulas_label': 'Formulas',
        'formulas': ['Σ deg(v) = 2|E|', '|E(Kₙ)| = n(n − 1)/2', '|E(Kₘ,ₙ)| = mn', 'Number of odd-degree vertices is even'],
        'steps': ['List the vertices and their degrees.', 'Use the handshake lemma to count edges.', 'Check the parity of odd degrees.', 'Choose a representation (matrix or list).'],
        'worked_example': {
            'problem': 'Can a graph have 5 vertices with degrees 3, 3, 3, 2, 2?',
            'steps': ['Sum of degrees = 13.', 'The sum must equal 2|E|, which is even.', '13 is odd, so no such graph exists.'],
            'answer': 'No.',
            'check': 'Equivalently, it would have three odd-degree vertices, an odd number, which is impossible ✓.'},
        'mistakes': ['Forgetting to halve the degree sum.', 'Counting a loop as degree 1.', 'Assuming every graph is connected.', 'Confusing Kₙ with a cycle Cₙ.'],
        'real_world': 'Social networks are graphs: people are vertices, friendships are edges, and the degree is your number of friends.',
        'exam_strategy': 'For "does such a graph exist?" questions, check the degree sum parity first.',
        'recap': ['Vertices and edges.', 'Handshake lemma.', 'Kₙ edges.', 'Bipartite graphs.']},
    T2: {
        'overview': 'Euler routes use every edge once; Hamilton routes visit every vertex once. One has a simple test, the other is famously hard.',
        'key_terms': ['Walk', 'Path', 'Circuit', 'Euler path', 'Euler circuit', 'Hamilton path', 'Hamilton cycle', 'Königsberg bridges'],
        'explanation': [
            'Euler\'s theorem: a connected graph has an Euler circuit if and only if every vertex has even degree, and an Euler path (not a circuit) if and only if exactly two vertices have odd degree; the path must start and end at those two. The Königsberg bridges graph has four odd vertices, so no walk crosses every bridge exactly once.',
            'A Hamilton cycle visits every vertex exactly once and returns. Every complete graph Kₙ (n ≥ 3) has one, and K₅ has (5 − 1)!/2 = 12 distinct Hamilton cycles. Deciding whether a general graph has a Hamilton cycle is NP-complete: no fast algorithm is known.',
            'The travelling salesperson problem asks for the cheapest Hamilton cycle in a weighted complete graph, a hard problem solved approximately in logistics.'],
        'formulas_label': 'Key results',
        'formulas': ['Euler circuit ⇔ connected, all degrees even', 'Euler path ⇔ connected, exactly 2 odd vertices', 'Hamilton cycles in Kₙ: (n − 1)!/2', 'Hamilton cycle existence: NP-complete'],
        'steps': ['Check that the graph is connected.', 'Count odd-degree vertices.', 'Apply Euler\'s theorem.', 'For Hamilton questions, try to construct a cycle or find an obstacle.'],
        'worked_example': {
            'problem': 'The Königsberg graph has four land masses with degrees 5, 3, 3, 3. Is there a walk crossing every bridge exactly once?',
            'steps': ['All four degrees are odd.', 'An Euler path needs exactly 0 or 2 odd vertices.', 'With 4, neither a circuit nor a path exists.'],
            'answer': 'No.',
            'check': 'This was Euler\'s 1736 argument, the start of graph theory ✓.'},
        'mistakes': ['Confusing Euler (edges) with Hamilton (vertices).', 'Forgetting the connectedness condition.', 'Thinking a Hamilton cycle must use every edge.', 'Assuming Hamilton problems have an easy test.'],
        'real_world': 'Street-sweeping and snow-plough routes are Euler problems; delivery routes visiting each customer once are Hamilton problems.',
        'exam_strategy': 'For Euler questions, write the degree of every vertex next to it on the diagram; the answer follows immediately.',
        'recap': ['Euler: edges once.', 'Even degrees ⇒ circuit.', 'Hamilton: vertices once.', 'Hamilton is hard.']},
    T3: {
        'overview': 'Trees are connected graphs without cycles. They organise file systems, family trees, decision processes and data structures.',
        'key_terms': ['Tree', 'Leaf', 'Root', 'Rooted tree', 'Binary tree', 'Full binary tree', 'Height', 'Spanning tree', 'Cayley\'s formula'],
        'explanation': [
            'A tree with n vertices has exactly n − 1 edges (a tree with 10 vertices has 9 edges). Adding any edge creates exactly one cycle; removing any edge disconnects it. Every tree with at least 2 vertices has at least 2 leaves.',
            'In a rooted binary tree each node has at most two children. A binary tree of height h has at most 2ʰ⁺¹ − 1 nodes (15 for h = 3). A full binary tree (every internal node has exactly two children) with i internal nodes has 2i + 1 nodes and i + 1 leaves.',
            'A spanning tree of a connected graph uses all its vertices and some of its edges with no cycles. Cayley\'s formula says there are nⁿ⁻² labelled trees on n vertices: 4² = 16 for n = 4.'],
        'formulas_label': 'Formulas',
        'formulas': ['Tree: |E| = |V| − 1', 'Binary tree of height h: at most 2ʰ⁺¹ − 1 nodes', 'Full binary tree: 2i + 1 nodes, i + 1 leaves', 'Labelled trees on n vertices: nⁿ⁻²'],
        'steps': ['Check connected and acyclic.', 'Count with |E| = |V| − 1.', 'For rooted trees, identify root, internal nodes and leaves.', 'Apply binary tree bounds.'],
        'worked_example': {
            'problem': 'A full binary tree has 5 internal nodes. How many nodes and leaves does it have?',
            'steps': ['Each internal node has 2 children: 10 child slots.', 'Every node except the root is a child: nodes = 10 + 1 = 11.', 'Leaves = 11 − 5 = 6 = i + 1.'],
            'answer': '11 nodes, 6 leaves.',
            'check': 'Edges = 10 = 11 − 1, as for any tree ✓.'},
        'mistakes': ['Forgetting the root when counting nodes.', 'Thinking a tree can have a cycle.', 'Mixing up height and number of levels.', 'Using nⁿ for labelled trees.'],
        'real_world': 'Computer file systems are rooted trees: folders are internal nodes and files are leaves.',
        'exam_strategy': 'Use |E| = |V| − 1 as a quick check in any tree problem.',
        'recap': ['Connected, no cycles.', 'n − 1 edges.', 'Binary tree bounds.', 'Spanning trees.']},
    T4: {
        'overview': 'Graph algorithms find shortest routes, cheapest networks and conflict-free schedules.',
        'key_terms': ['Breadth-first search', 'Depth-first search', 'Weighted graph', 'Dijkstra\'s algorithm', 'Minimum spanning tree', 'Kruskal\'s algorithm', 'Prim\'s algorithm', 'Graph colouring', 'Chromatic number', 'Planar graph', 'Euler\'s formula'],
        'explanation': [
            'Dijkstra\'s algorithm finds shortest paths from a source in a graph with non-negative weights by repeatedly fixing the closest unvisited vertex. In the graph A–B 4, A–C 2, C–B 1, B–D 5, C–D 8, C–E 10, D–E 2, the shortest distances from A are B 3 (via C), D 8 and E 10 (A–C–B–D–E).',
            'A minimum spanning tree connects all vertices as cheaply as possible. Kruskal\'s algorithm adds edges from cheapest to dearest, skipping any that would form a cycle: in the same graph it picks C–B 1, A–C 2, D–E 2, skips A–B 4, then takes B–D 5, total 10.',
            'Colouring assigns colours so adjacent vertices differ; the minimum is the chromatic number. Kₙ needs n colours, bipartite graphs 2, odd cycles 3. For connected planar graphs, Euler\'s formula V − E + F = 2 holds: a cube has 8 − 12 + 6 = 2.'],
        'formulas_label': 'Key facts',
        'formulas': ['Dijkstra: non-negative weights, fix the nearest vertex each step', 'Kruskal: cheapest edge that does not form a cycle', 'χ(Kₙ) = n; χ(bipartite) = 2; χ(odd cycle) = 3', 'Planar: V − E + F = 2'],
        'steps': ['For shortest paths, keep a table of tentative distances.', 'For an MST, sort edges by weight and add without cycles.', 'For colouring, colour greedily and check lower bounds (cliques).', 'For planar graphs, check Euler\'s formula.'],
        'worked_example': {
            'problem': 'Find the minimum spanning tree weight for the graph above using Kruskal\'s algorithm.',
            'steps': ['Sorted: C–B 1, A–C 2, D–E 2, A–B 4, B–D 5, C–D 8, C–E 10.', 'Take C–B, A–C, D–E; skip A–B (cycle A–B–C); take B–D.', 'Four edges for five vertices: total 1 + 2 + 2 + 5 = 10.'],
            'answer': '10.',
            'check': 'A spanning tree on 5 vertices needs 4 edges ✓.'},
        'mistakes': ['Using Dijkstra with negative weights.', 'Adding an edge that forms a cycle in Kruskal\'s algorithm.', 'Stopping Dijkstra before all distances are fixed.', 'Assuming planar graphs can need 5 colours (4 always suffice).'],
        'real_world': 'Maps apps use variants of Dijkstra\'s algorithm for directions; exam timetabling is graph colouring (clashing exams are adjacent).',
        'exam_strategy': 'Show the full Dijkstra table or the Kruskal edge list in order; method marks depend on it.',
        'recap': ['Dijkstra for shortest paths.', 'Kruskal for MSTs.', 'Chromatic numbers.', 'V − E + F = 2.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'A graph has degrees 3, 3, 2, 2, 2. How many edges does it have?', ['6', '12', '5', '10'], 0, 'Half the degree sum.', ans=6),
    Q(T1, 'How many edges does K₅ have?', ['10', '20', '5', '25'], 0, '5 × 4/2.', ans=10),
    Q(T1, 'How many edges does K₃,₃ have?', ['9', '6', '15', '3'], 0, '3 × 3.', ans=9),
    Q(T1, 'Which degree sequence is impossible for a graph?', ['3, 3, 3, 2, 2', '3, 3, 2, 2, 2', '2, 2, 2, 2', '1, 1'], 0, 'Degree sum 13 is odd.'),
    Q(T1, 'The adjacency matrix of an undirected graph is always:', ['symmetric', 'diagonal', 'invertible', 'all ones'], 0, 'u–v and v–u.'),
    Q(T1, 'Kₙ has how many edges?', ['n(n − 1)/2', 'n²', 'n − 1', '2n'], 0, 'Every pair once.', ans=n * (n - 1) / 2),
    # T2
    Q(T2, 'A connected graph has an Euler circuit exactly when:', ['every vertex has even degree', 'every vertex has odd degree', 'it is complete', 'it has a Hamilton cycle'], 0, 'Euler\'s theorem.'),
    Q(T2, 'A connected graph with exactly two odd-degree vertices has:', ['an Euler path but no Euler circuit', 'an Euler circuit', 'no Euler path', 'a Hamilton cycle'], 0, 'Start and end at the odd vertices.'),
    Q(T2, 'The Königsberg bridges problem has no solution because the graph has:', ['four odd-degree vertices', 'no odd-degree vertices', 'too many vertices', 'no cycles'], 0, '5, 3, 3, 3.'),
    Q(T2, 'A Hamilton cycle visits:', ['every vertex exactly once', 'every edge exactly once', 'every vertex at least twice', 'only odd vertices'], 0, 'Definition.'),
    Q(T2, 'How many distinct Hamilton cycles does K₅ have?', ['12', '24', '120', '60'], 0, '(5 − 1)!/2.', ans=12),
    Q(T2, 'Deciding whether a general graph has a Hamilton cycle is:', ['NP-complete', 'solved by checking degrees', 'always possible', 'linear time'], 0, 'No fast algorithm known.'),
    # T3
    Q(T3, 'A tree with 10 vertices has how many edges?', ['9', '10', '11', '45'], 0, 'n − 1.', ans=9),
    Q(T3, 'A binary tree of height 3 has at most how many nodes?', ['15', '8', '7', '16'], 0, '2⁴ − 1.', ans=15),
    Q(T3, 'A full binary tree with 5 internal nodes has how many nodes?', ['11', '10', '6', '15'], 0, '2i + 1.', ans=11),
    Q(T3, 'How many labelled trees are there on 4 vertices?', ['16', '4', '24', '64'], 0, 'Cayley: 4².', ans=16),
    Q(T3, 'Adding one edge to a tree creates:', ['exactly one cycle', 'two components', 'no cycle', 'many cycles'], 0, 'Trees are maximally acyclic.'),
    Q(T3, 'A spanning tree of a connected graph:', ['includes every vertex and has no cycles', 'includes every edge', 'has a cycle through every vertex', 'is unique'], 0, 'Definition.'),
    # T4
    Q(T4, 'In the example graph, the shortest distance from A to B is:', ['3', '4', '2', '5'], 0, 'A–C–B = 2 + 1.', ans=3),
    Q(T4, 'In the example graph, the shortest distance from A to E is:', ['10', '12', '9', '14'], 0, 'A–C–B–D–E.', ans=10),
    Q(T4, 'The minimum spanning tree of the example graph has total weight:', ['10', '12', '13', '9'], 0, '1 + 2 + 2 + 5.', ans=10),
    Q(T4, 'Dijkstra\'s algorithm requires edge weights that are:', ['non-negative', 'integers', 'distinct', 'less than 10'], 0, 'Negative weights break it.'),
    Q(T4, 'The chromatic number of the cycle C₅ is:', ['3', '2', '5', '4'], 0, 'Odd cycle.', ans=3),
    Q(T4, 'A connected planar graph with 8 vertices and 12 edges has how many faces?', ['6', '4', '20', '2'], 0, 'V − E + F = 2.', ans=6),
]

FLASH = [
    ['Handshake lemma', 'Sum of degrees = 2 × number of edges.'],
    ['Complete graph Kₙ', 'Every pair joined: n(n − 1)/2 edges.'],
    ['Euler circuit', 'Uses every edge once; exists iff connected and all degrees even.'],
    ['Hamilton cycle', 'Visits every vertex once; no simple test (NP-complete).'],
    ['Tree', 'Connected, no cycles, n − 1 edges.'],
    ['Dijkstra\'s algorithm', 'Shortest paths with non-negative weights.'],
    ['Kruskal\'s algorithm', 'Add cheapest edges that do not form a cycle.'],
    ['Euler\'s formula', 'Planar connected: V − E + F = 2.'],
]
