"""Data Structures and Algorithms, module 3: Trees and heaps."""
from verify import Q, sp
from py_common import check
T1, T2, T3, T4 = ('Binary trees and traversals', 'Binary search trees', 'Balanced trees (AVL)', 'Heaps and priority queues')
BST = '''class N:
    def __init__(s,v): s.v=v; s.l=None; s.r=None
def ins(t,v):
    if t is None: return N(v)
    if v<t.v: t.l=ins(t.l,v)
    else: t.r=ins(t.r,v)
    return t
t=None
for v in [50,30,70,20,40,60,80]: t=ins(t,v)
def ino(t): return ino(t.l)+[t.v]+ino(t.r) if t else []
def pre(t): return [t.v]+pre(t.l)+pre(t.r) if t else []
def post(t): return post(t.l)+post(t.r)+[t.v] if t else []
def h(t): return -1 if t is None else 1+max(h(t.l),h(t.r))
from collections import deque
def lvl(t):
    q=deque([t]); o=[]
    while q:
        x=q.popleft(); o.append(x.v)
        for c in (x.l,x.r):
            if c: q.append(c)
    return o
'''
check(BST + 'print(ino(t))', '[20, 30, 40, 50, 60, 70, 80]')
check(BST + 'print(pre(t))', '[50, 30, 20, 40, 70, 60, 80]')
check(BST + 'print(post(t))', '[20, 40, 30, 60, 80, 70, 50]')
check(BST + 'print(lvl(t))', '[50, 30, 70, 20, 40, 60, 80]')
check(BST + 'print(h(t))', 2)
check(BST + 'u=None\nfor v in [1,2,3,4,5]: u=ins(u,v)\nprint(h(u))', 4)
check('import heapq\nh=[1,3,5,7,9,8]\nheapq.heappush(h,2)\nprint(h)', '[1, 3, 2, 7, 9, 8, 5]')
check('import heapq\nh=[]\nfor x in [5,3,8,1]: heapq.heappush(h,x)\nprint([heapq.heappop(h) for _ in range(4)])', '[1, 3, 5, 8]')
check('import heapq\nh=[1,3,5,7,9,8]\nprint(heapq.heappop(h), h)', '1 [3, 7, 5, 8, 9]')
assert 2 ** (3 + 1) - 1 == 15 and (5 - 1) // 2 == 2 and 2 * 2 + 1 == 5

MODULE = {
    'title': 'Trees and heaps',
    'topics': [T1, T2, T3, T4],
    'overview': 'Trees organise data hierarchically and make searching fast. This module covers binary trees and their traversals, binary search trees, self-balancing AVL trees that guarantee O(log n) operations, and heaps, which power priority queues and heapsort.',
    'key_terms': ['Binary tree', 'Root', 'Leaf', 'Height', 'Inorder', 'Preorder', 'Postorder', 'Level order', 'Binary search tree', 'Successor', 'AVL tree', 'Balance factor', 'Rotation', 'Heap', 'Heap property', 'Priority queue', 'Heapify'],
    'explanation': [
        'A binary tree node has at most two children. Traversals visit every node in a fixed order: inorder (left, node, right), preorder (node, left, right), postorder (left, right, node) and level order (by depth, using a queue).',
        'A binary search tree keeps smaller keys to the left and larger keys to the right, so search, insert and delete follow one path from the root: O(h) for height h. Balanced trees keep h = O(log n); without balancing, inserting sorted data creates a chain with h = n − 1.',
        'A heap is a complete binary tree stored in an array, where each parent is no larger (min-heap) than its children. The minimum is always at the root, and insert and remove-min take O(log n), which makes heaps ideal priority queues.'],
    'quick_facts': [
        'Inorder traversal of a BST gives the keys in sorted order.',
        'BST operations cost O(h); h = O(log n) if balanced, up to n − 1 if not.',
        'AVL: |balance factor| ≤ 1 at every node, restored by rotations.',
        'Heap array: children of i at 2i + 1 and 2i + 2, parent at (i − 1)//2.',
        'Heap insert/extract: O(log n); build-heap: O(n); heapsort: O(n log n).'],
}

NOTES = {
    T1: {
        'overview': 'Binary trees are visited systematically by traversals, each useful for different tasks.',
        'key_terms': ['Root', 'Parent', 'Child', 'Leaf', 'Depth', 'Height', 'Inorder', 'Preorder', 'Postorder', 'Level order'],
        'explanation': [
            'Height is the number of edges on the longest root-to-leaf path. A binary tree of height h has at most 2ʰ⁺¹ − 1 nodes. The tree built from 50, 30, 70, 20, 40, 60, 80 is perfectly balanced with height 2.',
            'Traversals of that tree: inorder 20, 30, 40, 50, 60, 70, 80 (sorted, because it is a BST); preorder 50, 30, 20, 40, 70, 60, 80 (useful to copy a tree); postorder 20, 40, 30, 60, 80, 70, 50 (useful to delete a tree or evaluate expression trees); level order 50, 30, 70, 20, 40, 60, 80.',
            'Recursive traversals are short: inorder(t) = inorder(t.left) + [t.value] + inorder(t.right). Level order needs a queue: dequeue a node, record it, enqueue its children.'],
        'formulas_label': 'Traversal orders',
        'formulas': ['Inorder: left, node, right', 'Preorder: node, left, right', 'Postorder: left, right, node', 'Level order: by depth with a queue', 'Max nodes at height h: 2ʰ⁺¹ − 1'],
        'steps': ['Draw the tree.', 'Apply the traversal rule recursively.', 'Write nodes as you "visit" them.', 'Check the count matches the number of nodes.'],
        'worked_example': {
            'problem': 'Give the postorder traversal of the BST built from 50, 30, 70, 20, 40, 60, 80.',
            'steps': ['Left subtree (30 with 20, 40): 20, 40, 30.', 'Right subtree (70 with 60, 80): 60, 80, 70.', 'Then the root: 20, 40, 30, 60, 80, 70, 50.'],
            'answer': '20, 40, 30, 60, 80, 70, 50.',
            'check': 'The root is last in postorder, as expected ✓.'},
        'mistakes': ['Mixing up preorder and postorder.', 'Using a stack for level order (gives DFS).', 'Counting height in nodes instead of edges.', 'Forgetting empty subtrees.'],
        'real_world': 'Compilers store code as expression trees; evaluating them uses a postorder traversal.',
        'exam_strategy': 'Mark each node with a small number in visiting order on your diagram; it prevents skipped nodes.',
        'recap': ['Four traversals.', 'Inorder of BST is sorted.', 'Level order uses a queue.', 'Height in edges.']},
    T2: {
        'overview': 'Binary search trees keep data ordered so search, insertion and deletion follow a single path.',
        'key_terms': ['BST property', 'Search path', 'Insertion', 'Deletion', 'Inorder successor', 'Degenerate tree'],
        'explanation': [
            'Every key in the left subtree is smaller than the node, every key in the right subtree is larger. To find 60 in the example tree: 50 → go right to 70 → go left to 60: three comparisons.',
            'Deletion has three cases: a leaf is simply removed; a node with one child is replaced by that child; a node with two children is replaced by its inorder successor (the smallest key in its right subtree). Deleting 50 from the example replaces it with 60.',
            'All operations cost O(h). Inserting keys in sorted order (1, 2, 3, 4, 5) builds a chain of height 4, where searching is O(n). This is why balanced trees exist.'],
        'formulas_label': 'Costs',
        'formulas': ['Search, insert, delete: O(h)', 'Balanced: h = O(log n)', 'Degenerate (sorted inserts): h = n − 1', 'Two-child delete: use inorder successor'],
        'steps': ['Compare with the current node.', 'Go left if smaller, right if larger.', 'Insert where you fall off the tree.', 'For deletion, identify which of the three cases applies.'],
        'worked_example': {
            'problem': 'Delete 50 (the root) from the BST built from 50, 30, 70, 20, 40, 60, 80.',
            'steps': ['50 has two children.', 'Its inorder successor is the smallest key in the right subtree: 60.', 'Replace 50 by 60 and remove 60 from its old place (a leaf).'],
            'answer': 'The new root is 60; the tree stays a valid BST.',
            'check': 'Inorder traversal gives 20, 30, 40, 60, 70, 80, still sorted ✓.'},
        'mistakes': ['Replacing a two-child node with an arbitrary child.', 'Forgetting duplicates need a consistent rule.', 'Claiming BST search is always O(log n).', 'Breaking the BST property after deletion.'],
        'real_world': 'Ordered maps in C++ (std::map) and Java (TreeMap) are balanced binary search trees.',
        'exam_strategy': 'After any insertion or deletion, write the inorder traversal to check the BST property still holds.',
        'recap': ['Left smaller, right larger.', 'O(h) operations.', 'Three deletion cases.', 'Sorted inserts degenerate.']},
    T3: {
        'overview': 'AVL trees rebalance themselves after every change so the height stays O(log n).',
        'key_terms': ['Balance factor', 'AVL property', 'Left rotation', 'Right rotation', 'Double rotation', 'LL, RR, LR, RL cases'],
        'explanation': [
            'The balance factor of a node is height(left) − height(right). In an AVL tree every node has balance factor −1, 0 or 1. This guarantees h ≤ about 1.44 log₂ n, so all operations are O(log n).',
            'After an insertion, walk back up and fix the first unbalanced node with rotations. Inserting 10, 20, 30 makes 10 right-heavy (the RR case); a single left rotation at 10 makes 20 the root with children 10 and 30.',
            'The four cases: LL (single right rotation), RR (single left rotation), LR (left rotation on the child, then right rotation), RL (right rotation on the child, then left rotation). Red-black trees are another common balanced tree with looser balance but fewer rotations.'],
        'formulas_label': 'Rules',
        'formulas': ['Balance factor = h(left) − h(right)', 'AVL: balance factor ∈ {−1, 0, 1}', 'Height O(log n) ⇒ all operations O(log n)', 'LL: right rotate; RR: left rotate; LR, RL: double rotation'],
        'steps': ['Insert as in a normal BST.', 'Update heights on the way back up.', 'Find the first node with |balance| = 2.', 'Identify the case and rotate.'],
        'worked_example': {
            'problem': 'Insert 10, 20, 30 into an empty AVL tree.',
            'steps': ['After 10, 20: 10 has balance −1 (fine).', 'After 30: 10 has balance −2, right child 20 is right-heavy: RR case.', 'Left rotation at 10: root 20, left 10, right 30.'],
            'answer': 'A balanced tree with root 20.',
            'check': 'All balance factors are now 0 ✓.'},
        'mistakes': ['Using a single rotation for LR or RL cases.', 'Computing balance factors from depths instead of heights.', 'Forgetting to update heights after rotating.', 'Rebalancing the wrong node.'],
        'real_world': 'Databases and file systems use balanced trees (often B-trees, which generalise these ideas to many children per node) to keep lookups fast on disk.',
        'exam_strategy': 'Write the balance factor next to every node after each insertion; the unbalanced node and the case are then obvious.',
        'recap': ['Balance factor in {−1, 0, 1}.', 'Rotations fix imbalance.', 'Four cases.', 'O(log n) guaranteed.']},
    T4: {
        'overview': 'Heaps keep the smallest (or largest) item instantly available, which is exactly what a priority queue needs.',
        'key_terms': ['Complete binary tree', 'Min-heap', 'Max-heap', 'Sift up', 'Sift down', 'Build-heap', 'Priority queue', 'Heapsort'],
        'explanation': [
            'A heap is stored in an array: the children of index i are at 2i + 1 and 2i + 2, and the parent of i is at (i − 1)//2. In a min-heap every parent is ≤ its children, so the minimum is at index 0. [1, 3, 5, 7, 9, 8] is a valid min-heap.',
            'Insert: append, then sift up while smaller than the parent. Inserting 2 into [1, 3, 5, 7, 9, 8] puts it at index 6, swaps with its parent 5 (index 2) and stops below 1: [1, 3, 2, 7, 9, 8, 5]. Extract-min: take the root, move the last element to the root, sift down: popping from [1, 3, 5, 7, 9, 8] returns 1 and leaves [3, 7, 5, 8, 9].',
            'Both operations are O(log n). Building a heap from n items bottom-up is O(n). Heapsort builds a heap and extracts repeatedly: O(n log n) in place. Python\'s heapq is a min-heap: pushing 5, 3, 8, 1 and popping gives 1, 3, 5, 8.'],
        'formulas_label': 'Formulas',
        'formulas': ['children(i) = 2i + 1, 2i + 2', 'parent(i) = (i − 1)//2', 'insert, extract-min: O(log n)', 'build-heap: O(n); heapsort: O(n log n)'],
        'steps': ['Locate the new or moved element.', 'Compare with parent (sift up) or children (sift down).', 'Swap until the heap property holds.', 'Write the array after each step.'],
        'worked_example': {
            'problem': 'Insert 2 into the min-heap [1, 3, 5, 7, 9, 8].',
            'steps': ['Append at index 6: parent index (6 − 1)//2 = 2, value 5.', '2 < 5: swap; now at index 2, parent index 0 value 1.', '2 > 1: stop. Result [1, 3, 2, 7, 9, 8, 5].'],
            'answer': '[1, 3, 2, 7, 9, 8, 5].',
            'check': 'Python\'s heapq.heappush gives the same array ✓.'},
        'mistakes': ['Thinking a heap is fully sorted.', 'Using 2i and 2i + 1 with 0-based indices.', 'Sifting in the wrong direction.', 'Claiming build-heap is O(n log n) (it is O(n)).'],
        'real_world': 'Operating systems schedule processes with priority queues, and Dijkstra\'s shortest-path algorithm uses a heap to pick the nearest vertex.',
        'exam_strategy': 'Draw both the tree and the array; checking parent-child pairs is easier on the tree.',
        'recap': ['Array-based tree.', 'Min at the root.', 'Sift up and down.', 'O(log n) operations.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Inorder traversal of the BST built from 50, 30, 70, 20, 40, 60, 80 gives:', ['20, 30, 40, 50, 60, 70, 80', '50, 30, 20, 40, 70, 60, 80', '20, 40, 30, 60, 80, 70, 50', '50, 30, 70, 20, 40, 60, 80'], 0, 'Sorted order.'),
    Q(T1, 'Its preorder traversal is:', ['50, 30, 20, 40, 70, 60, 80', '20, 30, 40, 50, 60, 70, 80', '20, 40, 30, 60, 80, 70, 50', '50, 70, 80, 60, 30, 40, 20'], 0, 'Node, left, right.'),
    Q(T1, 'Its postorder traversal is:', ['20, 40, 30, 60, 80, 70, 50', '50, 30, 20, 40, 70, 60, 80', '20, 30, 40, 50, 60, 70, 80', '80, 70, 60, 50, 40, 30, 20'], 0, 'Left, right, node.'),
    Q(T1, 'Its height (in edges) is:', ['2', '3', '7', '1'], 0, 'Perfectly balanced, 3 levels.', ans=2),
    Q(T1, 'A binary tree of height 3 has at most how many nodes?', ['15', '8', '7', '16'], 0, '2⁴ − 1.', ans=15),
    Q(T1, 'Level-order traversal uses a:', ['queue', 'stack', 'heap', 'hash table'], 0, 'Breadth first.'),
    # T2
    Q(T2, 'Searching for 60 in the example BST visits:', ['50, 70, 60', '50, 30, 60', '50, 60', '20, 30, 40, 50, 60'], 0, 'Right then left.'),
    Q(T2, 'Inserting 1, 2, 3, 4, 5 in order into an empty BST gives height:', ['4', '2', '3', '5'], 0, 'A chain.', ans=4),
    Q(T2, 'Deleting a BST node with two children replaces it with its:', ['inorder successor', 'left child', 'parent', 'deepest leaf'], 0, 'Smallest in the right subtree.'),
    Q(T2, 'Deleting 50 from the example BST makes the new root:', ['60', '40', '70', '30'], 0, 'Inorder successor.', ans=60),
    Q(T2, 'Search in a BST of height h costs:', ['O(h)', 'O(1)', 'O(n²)', 'O(2ʰ)'], 0, 'One path.'),
    Q(T2, 'In the worst case, an unbalanced BST with n nodes has search cost:', ['O(n)', 'O(log n)', 'O(1)', 'O(n log n)'], 0, 'Degenerate chain.'),
    # T3
    Q(T3, 'In an AVL tree every balance factor is:', ['−1, 0 or 1', 'exactly 0', 'between −2 and 2', 'positive'], 0, 'AVL property.'),
    Q(T3, 'Inserting 10, 20, 30 into an empty AVL tree gives root:', ['20', '10', '30', 'none'], 0, 'Left rotation.', ans=20),
    Q(T3, 'The RR case is fixed by a:', ['single left rotation', 'single right rotation', 'double rotation', 'deletion'], 0, 'Right-right heavy.'),
    Q(T3, 'The LR case needs:', ['a left rotation on the child, then a right rotation', 'one right rotation', 'one left rotation', 'no rotation'], 0, 'Double rotation.'),
    Q(T3, 'Operations on an AVL tree with n keys cost:', ['O(log n)', 'O(n)', 'O(1)', 'O(n log n)'], 0, 'Height is O(log n).'),
    Q(T3, 'The balance factor of a node is:', ['height(left) − height(right)', 'number of children', 'depth − height', 'size(left) − size(right) of the whole tree'], 0, 'Definition.'),
    # T4
    Q(T4, 'In a 0-indexed heap array, the children of index 2 are at:', ['5 and 6', '4 and 5', '3 and 4', '2 and 3'], 0, '2i + 1, 2i + 2.'),
    Q(T4, 'The parent of index 5 is at index:', ['2', '3', '1', '4'], 0, '(5 − 1)//2.', ans=2),
    Q(T4, 'Inserting 2 into the min-heap [1, 3, 5, 7, 9, 8] gives:', ['[1, 3, 2, 7, 9, 8, 5]', '[1, 2, 3, 7, 9, 8, 5]', '[1, 3, 5, 7, 9, 8, 2]', '[2, 1, 3, 7, 9, 8, 5]'], 0, 'Sift up past 5.'),
    Q(T4, 'Pushing 5, 3, 8, 1 into a min-heap and popping everything gives:', ['1, 3, 5, 8', '5, 3, 8, 1', '8, 5, 3, 1', '1, 5, 3, 8'], 0, 'Sorted order.'),
    Q(T4, 'Building a heap from n items bottom-up takes:', ['O(n)', 'O(n log n)', 'O(log n)', 'O(n²)'], 0, 'Most nodes are near the bottom.'),
    Q(T4, 'Heapsort runs in:', ['O(n log n)', 'O(n²)', 'O(n)', 'O(log n)'], 0, 'n extractions of O(log n).'),
]

FLASH = [
    ['Inorder traversal', 'Left, node, right; sorted order for a BST.'],
    ['Preorder / postorder', 'Node first / node last.'],
    ['BST property', 'Left subtree smaller, right subtree larger.'],
    ['Inorder successor', 'Smallest key in the right subtree; replaces a deleted two-child node.'],
    ['AVL tree', 'Balance factors in {−1, 0, 1}; rotations keep height O(log n).'],
    ['Heap array indices', 'Children 2i + 1, 2i + 2; parent (i − 1)//2.'],
    ['Min-heap', 'Every parent ≤ its children; minimum at the root.'],
    ['Priority queue', 'Insert and extract-min in O(log n) with a heap.'],
]
