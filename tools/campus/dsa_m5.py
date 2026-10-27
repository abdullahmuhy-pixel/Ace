"""Data Structures and Algorithms, module 5: Graph algorithms and algorithm design."""
from verify import Q, sp
from py_common import check
T1, T2, T3, T4 = ('Graph traversal: BFS and DFS', 'Shortest paths and minimum spanning trees', 'Greedy algorithms', 'Dynamic programming')
GR = "G={'A':['B','C'],'B':['D'],'C':['D','E'],'D':['F'],'E':['F'],'F':[]}\n"
check(GR + '''from collections import deque
q=deque(['A']); seen={'A'}; o=[]; d={'A':0}
while q:
    u=q.popleft(); o.append(u)
    for v in G[u]:
        if v not in seen: seen.add(v); d[v]=d[u]+1; q.append(v)
print(''.join(o), d['F'])''', 'ABCDEF 3')
check(GR + '''o=[]
def dfs(u):
    o.append(u)
    for v in G[u]:
        if v not in o: dfs(v)
dfs('A')
print(''.join(o))''', 'ABDFCE')
check('''import heapq
E={('A','B'):4,('A','C'):2,('C','B'):1,('B','D'):5,('C','D'):8,('C','E'):10,('D','E'):2}
G={}
for (u,v),w in E.items(): G.setdefault(u,[]).append((v,w)); G.setdefault(v,[]).append((u,w))
seen={'A'}; h=[(w,v) for v,w in G['A']]; heapq.heapify(h); tot=0
while h:
    w,v=heapq.heappop(h)
    if v in seen: continue
    seen.add(v); tot+=w
    for x,wx in G[v]:
        if x not in seen: heapq.heappush(h,(wx,x))
print(tot)''', 10)
check('''E=[('S','A',4),('S','B',5),('A','C',-3),('B','C',2),('C','T',1)]
d={'S':0,'A':9e9,'B':9e9,'C':9e9,'T':9e9}
for _ in range(4):
    for u,v,w in E:
        if d[u]+w<d[v]: d[v]=d[u]+w
print(d['C'], d['T'])''', '1 2')
check('''acts=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
end=-1; c=0
for s,f in sorted(acts,key=lambda a:a[1]):
    if s>=end: c+=1; end=f
print(c)''', 4)
check('''def greedy(n,coins):
    c=0
    for x in sorted(coins,reverse=True):
        c+=n//x; n%=x
    return c
best=[0]+[99]*6
for i in range(1,7):
    best[i]=min(best[i-x]+1 for x in (1,3,4) if x<=i)
print(greedy(6,[1,3,4]), best[6])''', '3 2')
check('''from functools import lru_cache
@lru_cache(None)
def f(n): return n if n<2 else f(n-1)+f(n-2)
print(f(30))''', 832040)
check('''items=[(1,1),(3,4),(4,5),(5,7)]; W=5
dp=[0]*(W+1)
for w,v in items:
    for c in range(W,w-1,-1): dp[c]=max(dp[c],dp[c-w]+v)
print(dp[W])''', 7)
check('''a,b='ABCBDAB','BDCABA'
L=[[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        L[i+1][j+1]=L[i][j]+1 if a[i]==b[j] else max(L[i][j+1],L[i+1][j])
print(L[-1][-1])''', 4)
check('''a,b='kitten','sitting'
D=[[i+j if i*j==0 else 0 for j in range(len(b)+1)] for i in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        D[i][j]=min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+(a[i-1]!=b[j-1]))
print(D[-1][-1])''', 3)
check('w=[1,1]\nfor i in range(2,6): w.append(w[-1]+w[-2])\nprint(w[5])', 8)

MODULE = {
    'title': 'Graph algorithms and algorithm design',
    'topics': [T1, T2, T3, T4],
    'overview': 'This module applies data structures to graphs and introduces two of the most important design techniques. It covers breadth-first and depth-first search, shortest paths and minimum spanning trees, greedy algorithms and when they work, and dynamic programming for problems with overlapping subproblems.',
    'key_terms': ['Adjacency list', 'Breadth-first search', 'Depth-first search', 'Visited set', 'Dijkstra\'s algorithm', 'Bellman–Ford', 'Prim\'s algorithm', 'Kruskal\'s algorithm', 'Greedy choice', 'Activity selection', 'Dynamic programming', 'Memoisation', 'Tabulation', 'Optimal substructure', 'Knapsack', 'Longest common subsequence', 'Edit distance'],
    'explanation': [
        'Graphs are usually stored as adjacency lists. Breadth-first search explores level by level with a queue and finds shortest paths in unweighted graphs; depth-first search goes as deep as possible with recursion or a stack and underlies cycle detection and topological sorting. Both run in O(V + E).',
        'For weighted graphs, Dijkstra\'s algorithm (with a heap, O((V + E) log V)) finds shortest paths when weights are non-negative; Bellman–Ford handles negative weights in O(VE). Prim\'s and Kruskal\'s algorithms find minimum spanning trees.',
        'Greedy algorithms make the locally best choice and never reconsider; they are fast but only correct for problems with the right structure. Dynamic programming solves overlapping subproblems once and stores the answers, turning exponential recursions into polynomial algorithms.'],
    'quick_facts': [
        'BFS (queue) and DFS (stack/recursion): O(V + E).',
        'BFS gives shortest paths in unweighted graphs.',
        'Dijkstra: non-negative weights; Bellman–Ford: negative weights allowed.',
        'Greedy works for activity selection, not for coin change with arbitrary coins.',
        'DP = recursion + storing results (memoisation or tables).'],
}

NOTES = {
    T1: {
        'overview': 'BFS and DFS are the two basic ways to explore a graph; most graph algorithms are built on one of them.',
        'key_terms': ['Adjacency list', 'Adjacency matrix', 'Visited set', 'Queue', 'Stack', 'Recursion', 'BFS tree', 'Topological sort', 'Cycle detection'],
        'explanation': [
            'Adjacency lists use O(V + E) memory and are best for sparse graphs; adjacency matrices use O(V²) but answer "is there an edge u–v?" in O(1).',
            'In the directed graph A→B, A→C, B→D, C→D, C→E, D→F, E→F, BFS from A visits A, B, C, D, E, F (level by level), and F is 3 edges from A. DFS from A, taking neighbours in order, visits A, B, D, F, C, E.',
            'Both mark vertices as visited to avoid repeating work and run in O(V + E). DFS finishing times give a topological order of a directed acyclic graph, and a DFS that meets a vertex still on the recursion stack has found a cycle.'],
        'formulas_label': 'Facts',
        'formulas': ['BFS: queue, level order, shortest unweighted paths', 'DFS: stack or recursion, deep first', 'Both: O(V + E) with adjacency lists', 'Adjacency matrix: O(V²) space'],
        'steps': ['Choose BFS (distances) or DFS (structure).', 'Mark the start as visited.', 'Process neighbours in a fixed order.', 'Record the visiting order or distances.'],
        'worked_example': {
            'problem': 'Give the BFS order from A and the distance to F in the graph A→B, A→C, B→D, C→D, C→E, D→F, E→F.',
            'steps': ['Level 0: A. Level 1: B, C.', 'Level 2: D (from B), E (from C).', 'Level 3: F. Order A, B, C, D, E, F; distance to F = 3.'],
            'answer': 'A, B, C, D, E, F; distance 3.',
            'check': 'Running the BFS code prints ABCDEF 3 ✓.'},
        'mistakes': ['Forgetting to mark vertices as visited (infinite loops).', 'Using a stack for BFS.', 'Expecting BFS to give shortest weighted paths.', 'Marking visited too late in BFS (duplicates in the queue).'],
        'real_world': 'Web crawlers explore links with BFS; maze solvers and puzzle games often use DFS.',
        'exam_strategy': 'Write the queue (BFS) or stack (DFS) contents at each step; questions usually ask for the visiting order.',
        'recap': ['BFS: queue, levels.', 'DFS: deep first.', 'O(V + E).', 'Mark visited.']},
    T2: {
        'overview': 'Weighted graphs need dedicated algorithms for shortest paths and minimum spanning trees.',
        'key_terms': ['Relaxation', 'Dijkstra\'s algorithm', 'Bellman–Ford algorithm', 'Negative edge', 'Negative cycle', 'Prim\'s algorithm', 'Kruskal\'s algorithm', 'Union–find'],
        'explanation': [
            'Shortest-path algorithms repeatedly "relax" edges: if d[u] + w(u, v) < d[v], update d[v]. Dijkstra\'s algorithm always relaxes from the closest unfinished vertex, using a priority queue: O((V + E) log V). It fails with negative weights.',
            'Bellman–Ford relaxes every edge V − 1 times, O(VE), and works with negative weights. With edges S→A 4, S→B 5, A→C −3, B→C 2, C→T 1, it finds d(C) = 1 (via A) and d(T) = 2. A further improvement after V − 1 rounds reveals a negative cycle.',
            'Prim\'s algorithm grows a minimum spanning tree from a start vertex, always adding the cheapest edge leaving the tree (with a heap: O(E log V)). Kruskal\'s algorithm sorts all edges and adds them unless they create a cycle, using union–find. In the graph A–B 4, A–C 2, C–B 1, B–D 5, C–D 8, C–E 10, D–E 2 both give total weight 10.'],
        'formulas_label': 'Summary',
        'formulas': ['Relax: d[v] = min(d[v], d[u] + w)', 'Dijkstra: O((V + E) log V), weights ≥ 0', 'Bellman–Ford: O(VE), negative weights, detects negative cycles', 'Prim/Kruskal: O(E log V)'],
        'steps': ['Check whether any weights are negative.', 'Pick Dijkstra or Bellman–Ford.', 'Keep a distance table and update it as edges relax.', 'For MSTs, add cheapest safe edges.'],
        'worked_example': {
            'problem': 'With edges S→A 4, S→B 5, A→C −3, B→C 2, C→T 1, find the shortest distances to C and T from S.',
            'steps': ['Negative weight present: use Bellman–Ford.', 'd(A) = 4, d(B) = 5; C via A: 4 − 3 = 1 (better than 5 + 2 = 7).', 'd(T) = d(C) + 1 = 2.'],
            'answer': 'd(C) = 1, d(T) = 2.',
            'check': 'Running Bellman–Ford in code prints 1 2 ✓.'},
        'mistakes': ['Using Dijkstra with negative weights.', 'Running Bellman–Ford for too few rounds.', 'Adding cycle-forming edges in Kruskal.', 'Confusing shortest-path trees with minimum spanning trees.'],
        'real_world': 'Internet routing protocols use these algorithms: link-state routing (OSPF) runs Dijkstra, and distance-vector routing is based on Bellman–Ford.',
        'exam_strategy': 'Show a table of distances after each step or round; it is the standard way to earn method marks.',
        'recap': ['Relaxation.', 'Dijkstra (≥ 0).', 'Bellman–Ford (negatives).', 'Prim and Kruskal.']},
    T3: {
        'overview': 'Greedy algorithms build a solution step by step, always taking the choice that looks best now.',
        'key_terms': ['Greedy choice property', 'Optimal substructure', 'Activity selection', 'Interval scheduling', 'Coin change', 'Huffman coding', 'Counterexample'],
        'explanation': [
            'Activity selection: to fit the most non-overlapping activities in a room, repeatedly choose the one that finishes earliest. For the activities (1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16), this picks 4: (1, 4), (5, 7), (8, 11), (12, 16), which is optimal.',
            'Greedy fails when the problem lacks the right structure. Making 6 with coins {1, 3, 4}, greedy takes 4 + 1 + 1 (3 coins), but 3 + 3 uses only 2. With standard currency denominations greedy happens to work, but not in general.',
            'Proving a greedy algorithm correct usually uses an exchange argument: any optimal solution can be changed to include the greedy choice without getting worse. Huffman coding, Dijkstra, Prim and Kruskal are all greedy algorithms with such proofs.'],
        'formulas_label': 'Key ideas',
        'formulas': ['Greedy: best local choice, never undone', 'Needs the greedy-choice property + optimal substructure', 'Activity selection: earliest finish time', 'Disprove with a counterexample'],
        'steps': ['Define the greedy rule.', 'Sort by the rule if needed.', 'Take items that remain feasible.', 'Prove (exchange argument) or test against a counterexample.'],
        'worked_example': {
            'problem': 'Does greedy (largest coin first) give the fewest coins for 6 using coins {1, 3, 4}?',
            'steps': ['Greedy: 4, then 1, then 1: 3 coins.', 'Alternative: 3 + 3: 2 coins.', 'So greedy is not optimal here.'],
            'answer': 'No: greedy uses 3 coins, the optimum is 2.',
            'check': 'A dynamic-programming table in code gives 2 for the optimum ✓.'},
        'mistakes': ['Assuming greedy is always optimal.', 'Sorting by start time in activity selection.', 'Proving correctness with examples only.', 'Forgetting feasibility checks.'],
        'real_world': 'Huffman coding, a greedy algorithm, compresses files in formats like ZIP and JPEG.',
        'exam_strategy': 'When asked whether a greedy method works, look for a small counterexample first; if none exists, give an exchange argument.',
        'recap': ['Locally best choices.', 'Earliest finish wins.', 'Coin change counterexample.', 'Exchange arguments.']},
    T4: {
        'overview': 'Dynamic programming solves problems by combining answers to smaller overlapping subproblems, computing each one only once.',
        'key_terms': ['Overlapping subproblems', 'Optimal substructure', 'Memoisation (top-down)', 'Tabulation (bottom-up)', 'State', 'Recurrence', '0/1 knapsack', 'Longest common subsequence', 'Edit distance'],
        'explanation': [
            'Naive recursive Fibonacci recomputes the same values exponentially often; storing results (memoisation) computes F(30) = 832 040 in linear time. The number of ways to climb 5 stairs taking 1 or 2 steps at a time follows the same recurrence: 8.',
            '0/1 knapsack: dp[c] = best value with capacity c, updated for each item. With items (weight, value) (1, 1), (3, 4), (4, 5), (5, 7) and capacity 5, the best value is 7. Longest common subsequence of ABCBDAB and BDCABA has length 4; the edit distance from kitten to sitting is 3 (two substitutions and one insertion).',
            'Designing a DP: define the state (what a subproblem means), write the recurrence, choose the order to fill the table, and read off the answer. The cost is usually (number of states) × (work per state), for example O(nW) for knapsack and O(mn) for LCS.'],
        'formulas_label': 'Recurrences',
        'formulas': ['Fibonacci: F(n) = F(n − 1) + F(n − 2)', 'Knapsack: dp[c] = max(dp[c], dp[c − w] + v)', 'LCS: L[i][j] = L[i−1][j−1] + 1 if match, else max(L[i−1][j], L[i][j−1])', 'Edit distance: min(delete, insert, substitute)'],
        'steps': ['Define the state.', 'Write the recurrence and base cases.', 'Fill the table in dependency order.', 'Read off (and if needed reconstruct) the answer.'],
        'worked_example': {
            'problem': 'Items (weight, value): (1, 1), (3, 4), (4, 5), (5, 7). Capacity 5. Find the best total value.',
            'steps': ['Options within weight 5: {5} → 7; {1, 4} → 6; {1, 3} → 5.', 'The DP table over capacities 0–5 records the best for each capacity.', 'dp[5] = 7.'],
            'answer': '7 (take the item of weight 5).',
            'check': 'Running the knapsack DP prints 7 ✓.'},
        'mistakes': ['Iterating capacity upwards in 0/1 knapsack (reuses items).', 'Missing base cases.', 'Defining the state too vaguely.', 'Using DP when subproblems do not overlap (plain divide and conquer suffices).'],
        'real_world': 'Spell checkers use edit distance, DNA sequence alignment uses LCS-style DP, and "diff" tools compare files with it.',
        'exam_strategy': 'Draw the DP table and fill it explicitly; examiners give marks for correct cells even if the final answer slips.',
        'recap': ['Overlapping subproblems.', 'Memoise or tabulate.', 'State + recurrence.', 'Knapsack, LCS, edit distance.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'In the example graph, BFS from A visits vertices in the order:', ['A, B, C, D, E, F', 'A, B, D, F, C, E', 'A, C, E, F, B, D', 'F, D, E, B, C, A'], 0, 'Level by level.'),
    Q(T1, 'In the example graph, DFS from A (neighbours in order) visits:', ['A, B, D, F, C, E', 'A, B, C, D, E, F', 'A, C, D, E, F, B', 'A, B, D, C, E, F'], 0, 'Deep first.'),
    Q(T1, 'The BFS distance (number of edges) from A to F is:', ['3', '2', '4', '5'], 0, 'A → B → D → F.', ans=3),
    Q(T1, 'BFS and DFS with adjacency lists run in:', ['O(V + E)', 'O(V²)', 'O(E log V)', 'O(VE)'], 0, 'Each vertex and edge once.'),
    Q(T1, 'Shortest paths in an unweighted graph are found by:', ['BFS', 'DFS', 'Bellman–Ford only', 'Kruskal\'s algorithm'], 0, 'Level order = distance order.'),
    Q(T1, 'An adjacency matrix for V vertices uses memory:', ['O(V²)', 'O(V + E)', 'O(E)', 'O(V)'], 0, 'V × V table.'),
    # T2
    Q(T2, 'Dijkstra\'s algorithm may give wrong answers when:', ['some edge weights are negative', 'the graph is large', 'the graph is undirected', 'weights are integers'], 0, 'Greedy finalisation breaks.'),
    Q(T2, 'With S→A 4, S→B 5, A→C −3, B→C 2, C→T 1, the shortest distance to T is:', ['2', '6', '8', '1'], 0, 'S→A→C→T = 4 − 3 + 1.', ans=2),
    Q(T2, 'Bellman–Ford runs in:', ['O(VE)', 'O(V + E)', 'O(E log V)', 'O(V²)'], 0, 'V − 1 rounds over all edges.'),
    Q(T2, 'Prim\'s algorithm on the graph A–B 4, A–C 2, C–B 1, B–D 5, C–D 8, C–E 10, D–E 2 gives an MST of weight:', ['10', '12', '9', '13'], 0, 'Same as Kruskal.', ans=10),
    Q(T2, 'Kruskal\'s algorithm uses which structure to detect cycles efficiently?', ['union–find', 'a stack', 'a queue', 'a hash table only'], 0, 'Disjoint sets.'),
    Q(T2, 'The operation d[v] = min(d[v], d[u] + w(u, v)) is called:', ['relaxation', 'partition', 'rotation', 'hashing'], 0, 'Core of shortest paths.'),
    # T3
    Q(T3, 'For activity selection, the greedy rule that is optimal is:', ['earliest finish time first', 'earliest start time first', 'shortest activity first', 'longest activity first'], 0, 'Leaves the most room.'),
    Q(T3, 'The maximum number of compatible activities in the example list is:', ['4', '3', '5', '6'], 0, '(1,4), (5,7), (8,11), (12,16).', ans=4),
    Q(T3, 'Making 6 with coins {1, 3, 4}, greedy (largest first) uses how many coins?', ['3', '2', '6', '4'], 0, '4 + 1 + 1.', ans=3),
    Q(T3, 'The optimal number of coins for 6 with {1, 3, 4} is:', ['2', '3', '1', '6'], 0, '3 + 3.', ans=2),
    Q(T3, 'Greedy algorithms are correct when the problem has:', ['the greedy-choice property and optimal substructure', 'overlapping subproblems only', 'negative weights', 'no constraints'], 0, 'Both properties.'),
    Q(T3, 'Which of these is a greedy algorithm?', ['Huffman coding', 'Bellman–Ford', 'Edit distance', 'Merge sort'], 0, 'Merge cheapest pair each step.'),
    # T4
    Q(T4, 'F(30), computed with memoisation, is:', ['832040', '514229', '1346269', '317811'], 0, 'Computed in code.', ans=832040),
    Q(T4, 'The number of ways to climb 5 stairs taking 1 or 2 steps at a time is:', ['8', '5', '10', '13'], 0, 'Fibonacci-like.', ans=8),
    Q(T4, 'Items (1, 1), (3, 4), (4, 5), (5, 7) with capacity 5: the best value is:', ['7', '6', '9', '5'], 0, 'Take the weight-5 item.', ans=7),
    Q(T4, 'The LCS length of ABCBDAB and BDCABA is:', ['4', '3', '5', '6'], 0, 'For example BCBA.', ans=4),
    Q(T4, 'The edit distance from kitten to sitting is:', ['3', '2', '4', '7'], 0, 'k→s, e→i, insert g.', ans=3),
    Q(T4, 'Dynamic programming is useful when subproblems:', ['overlap', 'are all independent', 'cannot be stored', 'are random'], 0, 'Reuse stored results.'),
]

FLASH = [
    ['BFS', 'Queue-based, level by level; shortest unweighted paths; O(V + E).'],
    ['DFS', 'Stack or recursion, deep first; cycles and topological sort; O(V + E).'],
    ['Dijkstra', 'Shortest paths, non-negative weights, priority queue.'],
    ['Bellman–Ford', 'Handles negative weights; O(VE); detects negative cycles.'],
    ['Greedy algorithm', 'Locally best choice, never undone; needs proof.'],
    ['Activity selection', 'Pick the earliest-finishing compatible activity.'],
    ['Dynamic programming', 'Solve overlapping subproblems once; store results.'],
    ['0/1 knapsack', 'dp[c] = max(dp[c], dp[c − w] + v), capacity downwards.'],
]
