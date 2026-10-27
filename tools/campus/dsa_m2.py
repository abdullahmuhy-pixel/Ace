"""Data Structures and Algorithms, module 2: Linear data structures and hashing."""
from verify import Q, sp
from py_common import check
T1, T2, T3, T4 = ('Arrays and dynamic arrays', 'Linked lists', 'Stacks and queues', 'Hash tables')
check('a=[10,20,30,40]\na.insert(0,5)\nprint(a[2])', 20)
check('a=[3,1,4,1,5]\na.pop(1)\nprint(a)', '[3, 4, 1, 5]')
check('''class N:
    def __init__(s,v,n=None): s.v=v; s.n=n
h=None
for v in [1,2,3]: h=N(v,h)
out=[]
while h: out.append(h.v); h=h.n
print(out)''', '[3, 2, 1]')
check('s=[]\nfor x in [1,2,3]: s.append(x)\nprint(s.pop(), s.pop())', '3 2')
check('from collections import deque\nq=deque()\nfor x in [1,2,3]: q.append(x)\nprint(q.popleft())', 1)
check('''def post(e):
    s=[]
    for t in e.split():
        if t in '+-*': b=s.pop(); a=s.pop(); s.append(a+b if t=='+' else a-b if t=='-' else a*b)
        else: s.append(int(t))
    return s[0]
print(post('2 3 4 * +'), post('5 1 2 + 4 * + 3 -'))''', '14 14')
check('''def ok(x):
    s=[]; p={')':'(',']':'['}
    for c in x:
        if c in '([': s.append(c)
        elif c in ')]':
            if not s or s.pop()!=p[c]: return False
    return not s
print(ok('([()])'), ok('([)]'))''', 'True False')
check('''T=[None]*7
for k in [10,17,24]:
    i=k%7
    while T[i] is not None: i=(i+1)%7
    T[i]=k
print(T.index(10),T.index(17),T.index(24))''', '3 4 5')
assert 50 % 7 == 1 and 75 / 100 == 0.75

MODULE = {
    'title': 'Linear data structures and hashing',
    'topics': [T1, T2, T3, T4],
    'overview': 'Choosing the right container is half of writing fast code. This module compares arrays and linked lists, introduces stacks and queues with their classic uses, and explains hash tables, the structure behind dictionaries and sets with average O(1) lookup.',
    'key_terms': ['Array', 'Dynamic array', 'Random access', 'Linked list', 'Node', 'Pointer', 'Stack (LIFO)', 'Queue (FIFO)', 'Deque', 'Hash function', 'Collision', 'Chaining', 'Open addressing', 'Load factor'],
    'explanation': [
        'Arrays store items in consecutive memory, so a[i] takes O(1) time, but inserting or deleting in the middle shifts elements, O(n). Linked lists store items in nodes joined by pointers: inserting at a known position is O(1), but reaching the kth item takes O(k).',
        'Stacks (last in, first out) and queues (first in, first out) restrict access to make certain algorithms simple: stacks for undo, recursion and bracket matching; queues for scheduling and breadth-first search.',
        'Hash tables map keys to array positions with a hash function. With a good hash function and a moderate load factor, insertion, deletion and lookup take O(1) time on average, which is why Python dictionaries and sets are so fast.'],
    'quick_facts': [
        'Array: access O(1), insert/delete in middle O(n).',
        'Linked list: insert at head O(1), access kth O(k).',
        'Stack: push/pop at the top, LIFO. Queue: enqueue at back, dequeue at front, FIFO.',
        'Hash table: O(1) average lookup, O(n) worst case.',
        'Load factor α = n/m; resize when it gets large (e.g. above 0.75).'],
}

NOTES = {
    T1: {
        'overview': 'Arrays give instant access by index; their weakness is inserting and deleting in the middle.',
        'key_terms': ['Contiguous memory', 'Index', 'Random access', 'Shifting', 'Dynamic array', 'Capacity'],
        'explanation': [
            'Because elements sit next to each other, the address of a[i] is start + i × size, so access is O(1). Appending to the end of a dynamic array is O(1) amortised.',
            'Inserting at position 0 shifts every element one place right: O(n). After a = [10, 20, 30, 40] and a.insert(0, 5), a[2] is 20. Removing from the middle shifts the rest left: a = [3, 1, 4, 1, 5] after a.pop(1) becomes [3, 4, 1, 5].',
            'Arrays are cache-friendly (neighbouring items are loaded together), which often makes them faster in practice than linked structures even when the Big-O is the same.'],
        'formulas_label': 'Costs',
        'formulas': ['Access a[i]: O(1)', 'Append: O(1) amortised', 'Insert/delete at front or middle: O(n)', 'Search unsorted: O(n)'],
        'steps': ['Identify the operations your program needs most.', 'Use arrays for frequent indexed access.', 'Avoid repeated inserts at the front.', 'Consider a deque for both ends.'],
        'worked_example': {
            'problem': 'What does this print? a = [10, 20, 30, 40]; a.insert(0, 5); print(a[2])',
            'steps': ['After insert: [5, 10, 20, 30, 40].', 'Index 2 is the third element.', 'It is 20.'],
            'answer': '20.',
            'check': 'Running the code prints 20 ✓.'},
        'mistakes': ['Assuming insert at the front is O(1) for arrays.', 'Off-by-one index errors.', 'Using a list as a queue with pop(0), which is O(n).', 'Forgetting that indices shift after insert or delete.'],
        'real_world': 'Images are stored as arrays of pixels so any pixel can be read instantly by its row and column.',
        'exam_strategy': 'When asked for the cost of an operation, say what moves in memory; that justifies the Big-O.',
        'recap': ['O(1) access.', 'O(n) middle inserts.', 'Amortised O(1) append.', 'Cache-friendly.']},
    T2: {
        'overview': 'Linked lists trade fast access for cheap insertions and deletions at known positions.',
        'key_terms': ['Node', 'Next pointer', 'Head', 'Tail', 'Singly linked list', 'Doubly linked list', 'Traversal', 'Sentinel'],
        'explanation': [
            'Each node holds a value and a pointer to the next node; the list is reached from its head. Inserting at the head is O(1): make a new node point to the old head. Pushing 1, 2, 3 at the head gives the order 3, 2, 1.',
            'Finding the kth item means following k pointers: O(k), and searching is O(n). Deleting a node needs its predecessor in a singly linked list; a doubly linked list (with previous pointers too) deletes a given node in O(1).',
            'Linked lists are useful when items are inserted and removed constantly at known places, as in an LRU cache (combined with a hash table) or the free lists inside memory allocators.'],
        'formulas_label': 'Costs',
        'formulas': ['Insert at head: O(1)', 'Insert at tail with a tail pointer: O(1)', 'Access kth: O(k)', 'Delete given node: O(1) doubly, O(n) singly (to find predecessor)'],
        'steps': ['Draw boxes and arrows for the nodes.', 'Update pointers in the right order.', 'Handle the empty list and the head separately.', 'Trace with a small example.'],
        'worked_example': {
            'problem': 'Starting with an empty list, insert 1, then 2, then 3 at the head. What is the order when traversed?',
            'steps': ['After 1: [1].', 'After 2: 2 → 1.', 'After 3: 3 → 2 → 1.'],
            'answer': '3, 2, 1.',
            'check': 'Running the node code prints [3, 2, 1] ✓.'},
        'mistakes': ['Losing the rest of the list by updating pointers in the wrong order.', 'Forgetting the empty-list case.', 'Assuming O(1) indexing.', 'Not updating the tail pointer.'],
        'real_world': 'Music player playlists with "next" and "previous" are naturally doubly linked lists.',
        'exam_strategy': 'Always draw the before and after pointer diagrams; most marks are for correct pointer updates.',
        'recap': ['Nodes and pointers.', 'O(1) head insert.', 'O(k) access.', 'Doubly linked for O(1) delete.']},
    T3: {
        'overview': 'Stacks and queues restrict where items enter and leave, which makes them perfect for certain jobs.',
        'key_terms': ['Stack', 'Push', 'Pop', 'Peek', 'LIFO', 'Queue', 'Enqueue', 'Dequeue', 'FIFO', 'Deque', 'Postfix expression'],
        'explanation': [
            'A stack is last in, first out: after pushing 1, 2, 3, pop returns 3 then 2. Stacks check balanced brackets: push each opening bracket, and each closing one must match the top. "([()])" is balanced; "([)]" is not.',
            'Stacks evaluate postfix (reverse Polish) expressions: push numbers; on an operator, pop two and push the result. "2 3 4 * +" = 2 + 12 = 14, and "5 1 2 + 4 * + 3 −" = 14. The call stack of a running program is a stack of function frames.',
            'A queue is first in, first out: enqueue 1, 2, 3 and dequeue gives 1. Queues model waiting lines, printer jobs and breadth-first search. In Python use collections.deque for O(1) operations at both ends.'],
        'formulas_label': 'Operations (all O(1))',
        'formulas': ['Stack: push, pop, peek at the top', 'Queue: enqueue at back, dequeue at front', 'Deque: add/remove at both ends', 'Python: list as stack, deque as queue'],
        'steps': ['Decide whether order is LIFO or FIFO.', 'Trace the contents after each operation.', 'For postfix, pop the right operand first.', 'Check the structure is empty at the end where required.'],
        'worked_example': {
            'problem': 'Evaluate the postfix expression 5 1 2 + 4 * + 3 −.',
            'steps': ['Push 5, 1, 2; + gives 3: stack [5, 3].', 'Push 4; * gives 12: stack [5, 12]; + gives 17.', 'Push 3; − gives 17 − 3 = 14.'],
            'answer': '14.',
            'check': 'The stack-based evaluator in code prints 14 ✓.'},
        'mistakes': ['Popping operands in the wrong order for − and /.', 'Using list.pop(0) for a queue (O(n)).', 'Confusing LIFO and FIFO.', 'Not checking for an empty stack before popping.'],
        'real_world': 'The undo button in an editor is a stack of actions; a printer queue serves jobs in the order they were sent.',
        'exam_strategy': 'Write the stack contents after every token when evaluating expressions; it makes errors easy to spot and earns method marks.',
        'recap': ['Stack: LIFO.', 'Queue: FIFO.', 'Brackets and postfix.', 'Use deque for queues.']},
    T4: {
        'overview': 'Hash tables store key-value pairs for near-instant lookup by computing where each key should go.',
        'key_terms': ['Hash function', 'Bucket', 'Collision', 'Separate chaining', 'Open addressing', 'Linear probing', 'Load factor', 'Rehashing'],
        'explanation': [
            'A hash function maps a key to an index: with h(k) = k mod 7, key 50 goes to slot 1. Different keys can map to the same slot (a collision). Separate chaining keeps a small list in each slot; open addressing finds another empty slot.',
            'With linear probing in a table of size 7, inserting 10, 17 and 24 (all ≡ 3 mod 7) places them in slots 3, 4 and 5. Clustering like this slows probing, so good hash functions spread keys evenly.',
            'The load factor α = n/m (items over slots) controls performance: 75 items in 100 slots is α = 0.75. Lookups average O(1 + α), so tables resize (rehash into a bigger array) when α passes a threshold. In the worst case (all keys colliding) operations degrade to O(n).'],
        'formulas_label': 'Key facts',
        'formulas': ['Index = h(key) mod m', 'Load factor α = n/m', 'Average lookup O(1) for bounded α', 'Worst case O(n) when everything collides'],
        'steps': ['Compute the hash index.', 'Resolve collisions by chaining or probing.', 'Track the load factor.', 'Rehash into a larger table when needed.'],
        'worked_example': {
            'problem': 'Insert 10, 17, 24 into a table of size 7 with h(k) = k mod 7 and linear probing. Where does each go?',
            'steps': ['10 mod 7 = 3: slot 3.', '17 mod 7 = 3: taken, probe slot 4.', '24 mod 7 = 3: slots 3 and 4 taken, so slot 5.'],
            'answer': '10 → 3, 17 → 4, 24 → 5.',
            'check': 'Simulating the table in code gives slots 3, 4, 5 ✓.'},
        'mistakes': ['Forgetting to wrap around the end of the table when probing.', 'Thinking hash tables keep keys sorted.', 'Ignoring the worst case.', 'Using mutable objects as dictionary keys in Python.'],
        'real_world': 'Python dictionaries, database indexes and caches all rely on hashing for fast lookups.',
        'exam_strategy': 'Show the table after each insertion; examiners check the probe sequence step by step.',
        'recap': ['Hash to an index.', 'Collisions: chain or probe.', 'Watch the load factor.', 'O(1) average.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Accessing a[i] in an array takes:', ['O(1)', 'O(n)', 'O(log n)', 'O(i²)'], 0, 'Address arithmetic.'),
    Q(T1, 'Inserting at the front of an array of n items takes:', ['O(n)', 'O(1)', 'O(log n)', 'O(n²)'], 0, 'Every element shifts.'),
    Q(T1, 'a = [10, 20, 30, 40]; a.insert(0, 5); print(a[2]) prints:', ['20', '30', '10', '5'], 0, '[5, 10, 20, 30, 40].', ans=20),
    Q(T1, 'a = [3, 1, 4, 1, 5]; a.pop(1) leaves a as:', ['[3, 4, 1, 5]', '[3, 1, 4, 5]', '[1, 4, 1, 5]', '[3, 1, 4, 1]'], 0, 'Removes index 1.'),
    Q(T1, 'Appending to a Python list takes:', ['O(1) amortised', 'O(n) always', 'O(log n)', 'O(n²)'], 0, 'Dynamic array doubling.'),
    Q(T1, 'Using list.pop(0) as a queue operation costs:', ['O(n)', 'O(1)', 'O(log n)', 'O(n²)'], 0, 'Shifts all items.'),
    # T2
    Q(T2, 'Inserting at the head of a linked list takes:', ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'], 0, 'Change one pointer.'),
    Q(T2, 'Accessing the kth element of a linked list takes:', ['O(k)', 'O(1)', 'O(log k)', 'O(k²)'], 0, 'Follow k pointers.'),
    Q(T2, 'Inserting 1, 2, 3 at the head gives which traversal order?', ['3, 2, 1', '1, 2, 3', '2, 3, 1', '1, 3, 2'], 0, 'Newest first.'),
    Q(T2, 'Deleting a given node in O(1) needs a:', ['doubly linked list', 'singly linked list', 'array', 'stack'], 0, 'Needs the previous pointer.'),
    Q(T2, 'Compared with arrays, linked lists are better at:', ['inserting and deleting at known positions', 'random access', 'binary search', 'using less memory per item'], 0, 'Pointer updates only.'),
    Q(T2, 'Each node in a singly linked list stores:', ['a value and a next pointer', 'only a value', 'an index', 'two values'], 0, 'Definition.'),
    # T3
    Q(T3, 'Push 1, 2, 3 onto a stack, then pop twice. The values popped are:', ['3 then 2', '1 then 2', '3 then 1', '2 then 3'], 0, 'LIFO.'),
    Q(T3, 'Enqueue 1, 2, 3, then dequeue. The value removed is:', ['1', '3', '2', 'none'], 0, 'FIFO.', ans=1),
    Q(T3, 'The postfix expression 2 3 4 * + evaluates to:', ['14', '20', '24', '9'], 0, '2 + 3 × 4.', ans=14),
    Q(T3, 'Which bracket string is balanced?', ['([()])', '([)]', '(()', '])'], 0, 'Each closer matches the top.'),
    Q(T3, 'The postfix expression 5 1 2 + 4 * + 3 − evaluates to:', ['14', '18', '12', '20'], 0, '5 + 12 − 3.', ans=14),
    Q(T3, 'Breadth-first search uses a:', ['queue', 'stack', 'heap', 'hash table'], 0, 'FIFO order by distance.'),
    # T4
    Q(T4, 'With h(k) = k mod 7, key 50 maps to slot:', ['1', '7', '0', '3'], 0, '50 = 7 × 7 + 1.', ans=1),
    Q(T4, 'With linear probing in a size-7 table, inserting 10 then 17 puts 17 in slot:', ['4', '3', '0', '5'], 0, '17 mod 7 = 3, taken.', ans=4),
    Q(T4, '75 items in a hash table with 100 slots have load factor:', ['0.75', '1.33', '75', '0.25'], 0, 'n/m.', ans=0.75, num=True),
    Q(T4, 'Average-case lookup in a well-designed hash table is:', ['O(1)', 'O(log n)', 'O(n)', 'O(n log n)'], 0, 'Bounded load factor.'),
    Q(T4, 'Worst-case lookup in a hash table is:', ['O(n)', 'O(1)', 'O(log n)', 'O(n²)'], 0, 'All keys collide.'),
    Q(T4, 'Keeping a small list in each slot to handle collisions is called:', ['separate chaining', 'linear probing', 'rehashing', 'double hashing'], 0, 'Chains.'),
]

FLASH = [
    ['Array', 'Contiguous memory; O(1) access; O(n) middle insert.'],
    ['Linked list', 'Nodes with pointers; O(1) head insert; O(k) access.'],
    ['Stack', 'Last in, first out: push and pop at the top.'],
    ['Queue', 'First in, first out: enqueue at back, dequeue at front.'],
    ['Postfix evaluation', 'Push numbers; on an operator pop two, push the result.'],
    ['Hash function', 'Maps a key to a table index.'],
    ['Collision', 'Two keys hash to the same slot; resolved by chaining or probing.'],
    ['Load factor', 'α = items/slots; resize when it grows too large.'],
]
