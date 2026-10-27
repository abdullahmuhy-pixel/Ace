"""Data Structures and Algorithms, module 4: Searching and sorting."""
import math
from verify import Q, sp
from py_common import check
T1, T2, T3, T4 = ('Binary search', 'Simple sorts', 'Merge sort and quicksort', 'Lower bounds and linear-time sorting')
BS = '''def bs(a,x):
    lo,hi,c=0,len(a)-1,0
    while lo<=hi:
        m=(lo+hi)//2; c+=1
        if a[m]==x: return m,c
        if a[m]<x: lo=m+1
        else: hi=m-1
    return -1,c
a=[2,5,8,12,16,23,38,56,72,91]
'''
check(BS + 'print(bs(a,23))', '(5, 3)')
check(BS + 'print(bs(a,91))', '(9, 4)')
check(BS + 'print(bs(a,7))', '(-1, 3)')
check('''a=[5,2,4,6,1,3]
for i in range(1,3):
    k=a[i]; j=i-1
    while j>=0 and a[j]>k: a[j+1]=a[j]; j-=1
    a[j+1]=k
print(a)''', '[2, 4, 5, 6, 1, 3]')
check('a=[5,1,4,2,8]\nfor j in range(4):\n    if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]\nprint(a)', '[1, 4, 2, 5, 8]')
check('a=[64,25,12,22,11]\nm=min(range(5),key=lambda x:a[x])\na[0],a[m]=a[m],a[0]\nprint(a)', '[11, 25, 12, 22, 64]')
check('''def merge(x,y):
    i=j=0; o=[]
    while i<len(x) and j<len(y):
        if x[i]<=y[j]: o.append(x[i]); i+=1
        else: o.append(y[j]); j+=1
    return o+x[i:]+y[j:]
print(merge([1,4,7],[2,3,9]))''', '[1, 2, 3, 4, 7, 9]')
check('''a=[3,8,2,5,1,4,7,6]; p=a[-1]; i=0
for j in range(len(a)-1):
    if a[j]<=p: a[i],a[j]=a[j],a[i]; i+=1
a[i],a[-1]=a[-1],a[i]
print(a, i)''', '[3, 2, 5, 1, 4, 6, 7, 8] 5')
check('''a=[4,2,2,8,3,3,1]; k=max(a)+1; c=[0]*k
for x in a: c[x]+=1
print([v for v in range(k) for _ in range(c[v])])''', '[1, 2, 2, 3, 3, 4, 8]')
assert math.floor(math.log2(10)) + 1 == 4 and math.floor(math.log2(1024)) + 1 == 11 and math.ceil(math.log2(math.factorial(10))) == 22

MODULE = {
    'title': 'Searching and sorting',
    'topics': [T1, T2, T3, T4],
    'overview': 'Searching and sorting are the most common algorithmic tasks and the classic way to learn algorithm design. This module covers binary search, the simple quadratic sorts, the divide-and-conquer sorts merge sort and quicksort, and the limits on how fast comparison sorting can be.',
    'key_terms': ['Linear search', 'Binary search', 'Insertion sort', 'Selection sort', 'Bubble sort', 'Stable sort', 'In-place', 'Merge sort', 'Merge', 'Quicksort', 'Pivot', 'Partition', 'Comparison lower bound', 'Counting sort', 'Radix sort'],
    'explanation': [
        'Binary search halves a sorted range at each step, so it needs at most ⌊log₂ n⌋ + 1 comparisons: 4 for 10 items, 11 for 1024. It only works on sorted data.',
        'Insertion, selection and bubble sort are simple O(n²) algorithms; insertion sort is fast on nearly sorted data. Merge sort and quicksort use divide and conquer to reach O(n log n): merge sort always, quicksort on average, with an O(n²) worst case if pivots are chosen badly.',
        'No comparison-based sort can beat Ω(n log n) in the worst case, because it must distinguish n! orderings. Sorts that do not compare, like counting sort and radix sort, can run in linear time when keys are small integers.'],
    'quick_facts': [
        'Binary search: O(log n), needs sorted input.',
        'Insertion, selection, bubble: O(n²); insertion O(n) on sorted input.',
        'Merge sort: O(n log n) always, O(n) extra space, stable.',
        'Quicksort: O(n log n) average, O(n²) worst, in place.',
        'Comparison sorting needs at least log₂(n!) ≈ n log₂ n comparisons.'],
}

NOTES = {
    T1: {
        'overview': 'Binary search finds an item in a sorted array by repeatedly halving the search range.',
        'key_terms': ['Sorted array', 'Middle index', 'Search range', 'Iteration count', 'Off-by-one errors'],
        'explanation': [
            'Keep lo and hi; check the middle m = (lo + hi)//2. If a[m] is the target, stop; if it is smaller, search the right half (lo = m + 1); otherwise the left half (hi = m − 1). Stop when lo > hi (not found).',
            'In [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], searching for 23: lo = 0, hi = 9 gives m = 4 (16 < 23, so lo = 5); then m = 7 (56 > 23, so hi = 6); then m = 5, where 23 is found after 3 comparisons.',
            'The worst case for n items is ⌊log₂ n⌋ + 1 comparisons. Searching 91 in the 10-item list takes 4; searching for 7 (absent) takes 3 before the range empties. For 1024 items, at most 11.'],
        'formulas_label': 'Facts',
        'formulas': ['m = (lo + hi)//2', 'Worst case: ⌊log₂ n⌋ + 1 comparisons', 'Requires sorted data', 'O(log n) time, O(1) space (iterative)'],
        'steps': ['Set lo = 0, hi = n − 1.', 'Compare with a[m].', 'Discard the half that cannot contain the target.', 'Stop when found or lo > hi.'],
        'worked_example': {
            'problem': 'Trace binary search for 91 in [2, 5, 8, 12, 16, 23, 38, 56, 72, 91].',
            'steps': ['lo = 0, hi = 9: m = 4 (16 < 91), lo = 5.', 'm = 7 (56 < 91), lo = 8; m = 8 (72 < 91), lo = 9.', 'm = 9: found 91 at index 9 after 4 comparisons.'],
            'answer': 'Index 9, after 4 comparisons.',
            'check': '⌊log₂ 10⌋ + 1 = 4, the worst case ✓.'},
        'mistakes': ['Using binary search on unsorted data.', 'Infinite loops from lo = m instead of m + 1.', 'Using < instead of ≤ in the loop condition.', 'Overflow in (lo + hi) in fixed-width languages (use lo + (hi − lo)//2).'],
        'real_world': 'Git\'s "bisect" command uses binary search over commits to find which change introduced a bug.',
        'exam_strategy': 'Trace with a table of lo, hi, m and a[m]; most questions ask for the sequence of middle elements.',
        'recap': ['Sorted input only.', 'Halve each step.', 'log₂ n comparisons.', 'Careful with bounds.']},
    T2: {
        'overview': 'The simple sorts are easy to code and analyse, and insertion sort is genuinely useful for small or nearly sorted inputs.',
        'key_terms': ['Insertion sort', 'Selection sort', 'Bubble sort', 'Pass', 'Swap', 'Stable', 'In-place', 'Adaptive'],
        'explanation': [
            'Insertion sort grows a sorted prefix, inserting each new item into place. On [5, 2, 4, 6, 1, 3], after inserting the 2nd and 3rd items the array is [2, 4, 5, 6, 1, 3]. It is O(n²) in general but O(n) on already sorted input, and stable.',
            'Bubble sort swaps adjacent out-of-order pairs; each pass moves the largest remaining item to the end. One pass on [5, 1, 4, 2, 8] gives [1, 4, 2, 5, 8]. Selection sort repeatedly swaps the minimum of the unsorted part into place: one step on [64, 25, 12, 22, 11] gives [11, 25, 12, 22, 64]. Selection sort is not stable.',
            'All three are in place (O(1) extra space) and O(n²) in the worst case, so they are only practical for small arrays. Real libraries switch to insertion sort for tiny subarrays inside faster algorithms.'],
        'formulas_label': 'Comparison',
        'formulas': ['Insertion: O(n²) worst, O(n) best, stable', 'Selection: O(n²) always, not stable, few swaps', 'Bubble: O(n²) worst, O(n) best with early exit, stable', 'All in place'],
        'steps': ['Write the array after each pass.', 'Track the sorted part.', 'Count comparisons and swaps if asked.', 'Check stability with equal keys.'],
        'worked_example': {
            'problem': 'Show [5, 2, 4, 6, 1, 3] after the first two insertion-sort steps.',
            'steps': ['Insert 2: [2, 5, 4, 6, 1, 3].', 'Insert 4 between 2 and 5: [2, 4, 5, 6, 1, 3].', 'The first three items are now sorted.'],
            'answer': '[2, 4, 5, 6, 1, 3].',
            'check': 'Running the insertion-sort loop twice prints this array ✓.'},
        'mistakes': ['Confusing insertion and selection sort.', 'Claiming selection sort is stable.', 'Forgetting bubble sort can stop early when no swaps occur.', 'Thinking O(n²) sorts are fine for large data.'],
        'real_world': 'Card players sort a hand with insertion sort: each new card is slotted into place among those already held.',
        'exam_strategy': 'Questions usually ask for the array after a given number of passes; write every pass on its own line.',
        'recap': ['Insertion: grow sorted prefix.', 'Selection: pick the minimum.', 'Bubble: swap neighbours.', 'All O(n²).']},
    T3: {
        'overview': 'Divide-and-conquer sorting reaches O(n log n): merge sort splits evenly and merges, quicksort partitions around a pivot.',
        'key_terms': ['Divide and conquer', 'Merge', 'Merge sort', 'Partition', 'Pivot', 'Lomuto partition', 'Quicksort', 'Randomised pivot'],
        'explanation': [
            'Merge sort splits the array in half, sorts each half recursively and merges them. Merging [1, 4, 7] and [2, 3, 9] repeatedly takes the smaller front item: [1, 2, 3, 4, 7, 9]. T(n) = 2T(n/2) + n gives O(n log n) in every case; it needs O(n) extra space and is stable.',
            'Quicksort picks a pivot, partitions so smaller items go left and larger right, then sorts each side. Lomuto partition on [3, 8, 2, 5, 1, 4, 7, 6] with pivot 6 gives [3, 2, 5, 1, 4, 6, 7, 8] with the pivot at index 5.',
            'With good pivots quicksort is O(n log n) and very fast in practice, in place. With bad pivots (for example always the last element of already sorted data) it degrades to O(n²); random or median-of-three pivots make this extremely unlikely.'],
        'formulas_label': 'Comparison',
        'formulas': ['Merge sort: O(n log n) all cases, O(n) space, stable', 'Quicksort: O(n log n) average, O(n²) worst, in place, not stable', 'Merge of sizes p and q: at most p + q − 1 comparisons', 'Partition: O(n)'],
        'steps': ['Split (merge sort) or partition (quicksort).', 'Recurse on the parts.', 'Merge (merge sort only).', 'Analyse with T(n) = 2T(n/2) + n.'],
        'worked_example': {
            'problem': 'Partition [3, 8, 2, 5, 1, 4, 7, 6] using the last element as pivot (Lomuto).',
            'steps': ['Pivot 6; scan left to right, moving items ≤ 6 to the front: 3, 2, 5, 1, 4.', 'Then place the pivot after them.', 'Result: [3, 2, 5, 1, 4, 6, 7, 8], pivot at index 5.'],
            'answer': '[3, 2, 5, 1, 4, 6, 7, 8].',
            'check': 'Everything left of 6 is smaller and everything right is larger ✓.'},
        'mistakes': ['Saying quicksort is always O(n log n).', 'Forgetting merge sort needs extra memory.', 'Losing elements when merging (forgetting leftovers).', 'Choosing the first element as pivot on sorted data.'],
        'real_world': 'Python\'s built-in sort (Timsort) combines merge sort with insertion sort; C\'s qsort and many libraries use quicksort variants.',
        'exam_strategy': 'For merge sort, draw the recursion tree of splits and merges; for quicksort, write the array after each partition.',
        'recap': ['Merge sort: split and merge.', 'Quicksort: partition around a pivot.', 'n log n average.', 'Quicksort worst case n².']},
    T4: {
        'overview': 'Comparison sorts cannot beat n log n, but sorts that use key values directly can be linear.',
        'key_terms': ['Decision tree', 'Comparison lower bound', 'Counting sort', 'Radix sort', 'Bucket sort', 'Stability'],
        'explanation': [
            'A comparison sort can be drawn as a decision tree whose leaves are the n! possible orderings. A binary tree with n! leaves has height at least log₂(n!) ≈ n log₂ n, so any comparison sort needs Ω(n log n) comparisons in the worst case. For 10 items, at least ⌈log₂ 10!⌉ = 22 comparisons.',
            'Counting sort counts how often each key from 0 to k − 1 appears, then writes them out: [4, 2, 2, 8, 3, 3, 1] becomes [1, 2, 2, 3, 3, 4, 8]. It runs in O(n + k), excellent when k is small.',
            'Radix sort sorts by one digit at a time (least significant first) using a stable sort such as counting sort: O(d(n + k)) for d digits. It sorts fixed-length keys like IDs or postal codes in linear time.'],
        'formulas_label': 'Facts',
        'formulas': ['Comparison sorts: Ω(n log n)', 'log₂(n!) ≈ n log₂ n − 1.44n', 'Counting sort: O(n + k)', 'Radix sort: O(d(n + k)), needs a stable inner sort'],
        'steps': ['Decide whether keys are small integers.', 'If yes, consider counting or radix sort.', 'Otherwise use an O(n log n) comparison sort.', 'Check whether stability is needed.'],
        'worked_example': {
            'problem': 'What is the minimum worst-case number of comparisons needed to sort 10 items by comparisons?',
            'steps': ['There are 10! = 3 628 800 orderings.', 'log₂(3 628 800) ≈ 21.8.', 'So at least 22 comparisons.'],
            'answer': '22.',
            'check': 'Merge sort uses at most about 25 comparisons for 10 items, close to this bound ✓.'},
        'mistakes': ['Thinking counting sort works for any data.', 'Using an unstable inner sort in radix sort.', 'Ignoring k in counting sort\'s cost.', 'Believing a comparison sort can be O(n) in the worst case.'],
        'real_world': 'Census and banking systems sort millions of records by fixed-length numeric keys with radix sort.',
        'exam_strategy': 'If asked whether a sort can beat n log n, say "not by comparisons; yes with counting or radix sort for small integer keys".',
        'recap': ['Decision-tree bound.', 'Counting sort.', 'Radix sort.', 'Stability matters.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Binary search requires the data to be:', ['sorted', 'unsorted', 'in a linked list', 'unique'], 0, 'Halving relies on order.'),
    Q(T1, 'Searching 23 in [2, 5, 8, 12, 16, 23, 38, 56, 72, 91] finds it at index:', ['5', '6', '4', '23'], 0, 'Zero-based.', ans=5),
    Q(T1, 'Binary search on 10 sorted items needs at most how many comparisons?', ['4', '10', '5', '3'], 0, '⌊log₂ 10⌋ + 1.', ans=4),
    Q(T1, 'Binary search on 1024 sorted items needs at most how many comparisons?', ['11', '10', '1024', '512'], 0, '⌊log₂ 1024⌋ + 1.', ans=11),
    Q(T1, 'The time complexity of binary search is:', ['O(log n)', 'O(n)', 'O(1)', 'O(n log n)'], 0, 'Halving.'),
    Q(T1, 'If a[m] < target, the next search range is:', ['lo = m + 1 to hi', 'lo to m − 1', 'lo to m', 'm to hi'], 0, 'Discard the left half.'),
    # T2
    Q(T2, '[5, 2, 4, 6, 1, 3] after the first two insertion-sort steps is:', ['[2, 4, 5, 6, 1, 3]', '[2, 5, 4, 6, 1, 3]', '[1, 2, 4, 6, 5, 3]', '[2, 4, 5, 1, 3, 6]'], 0, 'Insert 2, then 4.'),
    Q(T2, 'One bubble-sort pass on [5, 1, 4, 2, 8] gives:', ['[1, 4, 2, 5, 8]', '[1, 2, 4, 5, 8]', '[1, 5, 4, 2, 8]', '[5, 1, 4, 2, 8]'], 0, 'Adjacent swaps.'),
    Q(T2, 'One selection-sort step on [64, 25, 12, 22, 11] gives:', ['[11, 25, 12, 22, 64]', '[25, 64, 12, 22, 11]', '[11, 12, 22, 25, 64]', '[12, 25, 64, 22, 11]'], 0, 'Swap the minimum to the front.'),
    Q(T2, 'Insertion sort on already sorted data runs in:', ['O(n)', 'O(n²)', 'O(n log n)', 'O(log n)'], 0, 'One comparison per item.'),
    Q(T2, 'Which simple sort is not stable?', ['Selection sort', 'Insertion sort', 'Bubble sort', 'Merge sort'], 0, 'Long-distance swaps.'),
    Q(T2, 'The worst-case time of insertion, selection and bubble sort is:', ['O(n²)', 'O(n log n)', 'O(n)', 'O(2ⁿ)'], 0, 'Quadratic.'),
    # T3
    Q(T3, 'Merging [1, 4, 7] and [2, 3, 9] gives:', ['[1, 2, 3, 4, 7, 9]', '[1, 4, 7, 2, 3, 9]', '[1, 2, 4, 3, 7, 9]', '[2, 3, 9, 1, 4, 7]'], 0, 'Take the smaller front item.'),
    Q(T3, 'Merge sort runs in:', ['O(n log n) in all cases', 'O(n²) worst case', 'O(n) best case', 'O(log n)'], 0, 'Even splits always.'),
    Q(T3, 'Lomuto partition of [3, 8, 2, 5, 1, 4, 7, 6] with pivot 6 places the pivot at index:', ['5', '7', '0', '6'], 0, 'Five items ≤ 6 come first.', ans=5),
    Q(T3, 'Quicksort\'s worst case is:', ['O(n²)', 'O(n log n)', 'O(n)', 'O(log n)'], 0, 'Bad pivots.'),
    Q(T3, 'Quicksort\'s worst case happens with last-element pivots on:', ['already sorted data', 'random data', 'data with all distinct keys', 'small arrays only'], 0, 'Unbalanced partitions.'),
    Q(T3, 'Compared with quicksort, merge sort:', ['needs O(n) extra space', 'is in place', 'is never O(n log n)', 'is unstable'], 0, 'Merging needs a buffer.'),
    # T4
    Q(T4, 'Any comparison sort needs, in the worst case, at least:', ['Ω(n log n) comparisons', 'Ω(n) comparisons', 'Ω(n²) comparisons', 'Ω(log n) comparisons'], 0, 'Decision-tree bound.'),
    Q(T4, 'The minimum worst-case comparisons to sort 10 items is:', ['22', '10', '45', '100'], 0, '⌈log₂ 10!⌉.', ans=22),
    Q(T4, 'Counting sort on n keys in the range 0 to k − 1 runs in:', ['O(n + k)', 'O(n log n)', 'O(nk)', 'O(k log n)'], 0, 'Count then output.'),
    Q(T4, 'Counting sort of [4, 2, 2, 8, 3, 3, 1] outputs:', ['[1, 2, 2, 3, 3, 4, 8]', '[8, 4, 3, 3, 2, 2, 1]', '[1, 2, 3, 4, 8]', '[4, 2, 2, 8, 3, 3, 1]'], 0, 'Keeps duplicates.'),
    Q(T4, 'Radix sort needs its per-digit sort to be:', ['stable', 'in place', 'recursive', 'comparison-based'], 0, 'Preserves earlier digit order.'),
    Q(T4, 'Radix sort on n keys with d digits in base k runs in:', ['O(d(n + k))', 'O(n log n)', 'O(n²)', 'O(dk)'], 0, 'd counting-sort passes.'),
]

FLASH = [
    ['Binary search', 'Halve a sorted range each step: O(log n).'],
    ['Insertion sort', 'Insert each item into a sorted prefix; O(n²), O(n) if sorted.'],
    ['Stable sort', 'Equal keys keep their original order.'],
    ['Merge sort', 'Split, sort halves, merge: O(n log n) always, O(n) space.'],
    ['Quicksort', 'Partition around a pivot: O(n log n) average, O(n²) worst.'],
    ['Comparison lower bound', 'Ω(n log n), from log₂(n!).'],
    ['Counting sort', 'O(n + k) for integer keys below k.'],
    ['Radix sort', 'Digit by digit with a stable sort: O(d(n + k)).'],
]
