"""Programming with Python, module 5: Algorithms and working with data."""
import math
from verify import Q
from py_common import check as c, out
T1, T2, T3, T4 = ('Searching algorithms', 'Sorting algorithms', 'Algorithm efficiency and Big O', 'Processing data with Python')

BS = '''def bsearch(a, t):
    lo, hi, steps = 0, len(a) - 1, 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if a[mid] == t:
            return mid, steps
        if a[mid] < t:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, steps
'''
A = [
    c(BS + 'print(bsearch([3, 8, 12, 19, 25, 31, 40], 25))', '(4, 3)'),
    c(BS + 'print(bsearch([3, 8, 12, 19, 25, 31, 40], 5)[0])', '-1'),
    c(BS + 'print(max(bsearch(list(range(1024)), t)[1] for t in range(1024)))', '11'),
    c('def lin(a, t):\n    for i, x in enumerate(a):\n        if x == t:\n            return i\n    return -1\nprint(lin([7, 3, 9, 3], 3))', '1'),
    c('a = [5, 1, 4, 2]\nfor i in range(len(a) - 1):\n    if a[i] > a[i + 1]:\n        a[i], a[i + 1] = a[i + 1], a[i]\nprint(a)', '[1, 4, 2, 5]'),
    c('a = [29, 10, 14, 37, 13]\nm = a.index(min(a))\na[0], a[m] = a[m], a[0]\nprint(a)', '[10, 29, 14, 37, 13]'),
    c('def merge(x, y):\n    r = []\n    i = j = 0\n    while i < len(x) and j < len(y):\n        if x[i] <= y[j]:\n            r.append(x[i]); i += 1\n        else:\n            r.append(y[j]); j += 1\n    return r + x[i:] + y[j:]\nprint(merge([1, 4, 9], [2, 3, 10]))', '[1, 2, 3, 4, 9, 10]'),
    c('people = [("Ada", 31), ("Bo", 25), ("Chi", 28)]\nprint([p[0] for p in sorted(people, key=lambda p: p[1])])', "['Bo', 'Chi', 'Ada']"),
    c('import csv, io\ndata = "name,mark\\nAda,72\\nBo,58\\nChi,90\\n"\nrows = list(csv.DictReader(io.StringIO(data)))\nprint(sum(int(r["mark"]) for r in rows) / len(rows))', '73.33333333333333'),
    c('sales = [("north", 120), ("south", 80), ("north", 60)]\nt = {}\nfor region, amt in sales:\n    t[region] = t.get(region, 0) + amt\nprint(t)', "{'north': 180, 'south': 80}"),
    c('marks = [72, 58, 90, 45]\nprint(len([m for m in marks if m >= 50]))', '3'),
    c('from collections import Counter\nprint(Counter("mississippi").most_common(1))', "[('i', 4)]"),
]
assert math.floor(math.log2(1024)) + 1 == 11 and math.ceil(math.log2(1000001)) == 20

MODULE = {
    'title': 'Algorithms and working with data',
    'topics': [T1, T2, T3, T4],
    'overview': 'An algorithm is a precise, step-by-step method for solving a problem. This module studies the classic searching and sorting algorithms, measures how their running time grows with the size of the input using Big O notation, and applies these ideas to real data processing in Python.',
    'key_terms': ['Algorithm', 'Linear search', 'Binary search', 'Bubble sort', 'Selection sort', 'Merge sort', 'Big O', 'Time complexity', 'CSV', 'Aggregation'],
    'explanation': [
        'The same problem can be solved by algorithms that differ hugely in speed. Linear search checks every item; binary search halves a sorted list each step. Simple sorts such as bubble and selection sort compare neighbouring or minimum items; merge sort divides the list and merges sorted halves.',
        'Big O notation describes how the number of steps grows as the input size n grows, ignoring constant factors. O(log n) grows very slowly, O(n) in proportion to the input, O(n log n) a little faster, and O(n²) quickly becomes impractical for large inputs.',
        'In practice, Python\'s built-in sorted() and dictionary lookups are highly optimised, and much real programming is processing data: reading files, filtering, grouping and summarising. Knowing the underlying algorithms helps you choose sensible approaches and spot slow code.'],
    'quick_facts': [
        'Linear search: O(n); works on unsorted data.',
        'Binary search: O(log n); needs sorted data.',
        'Bubble, selection, insertion sort: O(n²).',
        'Merge sort: O(n log n); Python\'s sorted() is O(n log n).',
        'Dictionary lookup is O(1) on average.'],
}

NOTES = {
    T1: {
        'overview': 'Searching finds whether an item is in a collection and where. Linear search works on any list; binary search is much faster but needs the list to be sorted.',
        'key_terms': ['Linear search', 'Binary search', 'Sorted data', 'Midpoint', 'Comparison', 'Worst case'],
        'explanation': [
            'Linear search checks items one by one from the start until it finds the target or reaches the end. In the worst case (target last or missing) it makes n comparisons.',
            'Binary search works on sorted data. Compare the target with the middle item: if equal, stop; if the target is larger, search the right half; otherwise the left half. Each step halves the remaining range, so a list of 1024 items needs at most 11 comparisons, and a million items about 20.',
            'Binary search is only correct if the data are sorted, and sorting first costs time. For a single search of unsorted data, linear search can be the better choice; for many searches, sort once (or use a set or dictionary) and then search quickly.'],
        'formulas_label': 'Key facts',
        'formulas': ['Linear search: up to n comparisons', 'Binary search: about log₂ n comparisons', 'mid = (lo + hi) // 2', '1024 items → at most 11 binary-search steps'],
        'steps': ['Check whether the data are sorted.', 'Choose linear or binary search.', 'For binary search, track lo, hi and mid.', 'Stop when found or when lo > hi.'],
        'worked_example': {
            'problem': 'Binary search for 25 in [3, 8, 12, 19, 25, 31, 40], using mid = (lo + hi) // 2.',
            'steps': ['lo = 0, hi = 6: mid = 3 and a[3] = 19 < 25, so lo = 4.', 'lo = 4, hi = 6: mid = 5 and a[5] = 31 > 25, so hi = 4.', 'lo = 4, hi = 4: mid = 4 and a[4] = 25: found.'],
            'answer': 'Found at index 4 after 3 comparisons.',
            'check': 'Linear search would need 5 comparisons to reach index 4; running the course\'s bsearch code returns (4, 3) ✓.'},
        'mistakes': ['Running binary search on unsorted data.', 'Off-by-one errors in updating lo and hi (use mid + 1 and mid − 1).', 'Forgetting the case where the item is not present.', 'Thinking binary search is always better, even for one search on unsorted data.'],
        'real_world': 'Looking up a word in a printed dictionary is binary search: you open near the middle and discard half the book each time.',
        'exam_strategy': 'Trace binary search in a table with columns lo, hi, mid and a[mid]. Use the exact midpoint rule in the question.',
        'recap': ['Linear: any data, O(n).', 'Binary: sorted data, O(log n).', 'Halve the range each step.', 'Handle "not found".']},
    T2: {
        'overview': 'Sorting puts items in order. Simple algorithms are easy to understand but slow on large data; divide-and-conquer algorithms such as merge sort are much faster.',
        'key_terms': ['Bubble sort', 'Selection sort', 'Insertion sort', 'Merge sort', 'Pass', 'Swap', 'Stable sort', 'key function'],
        'explanation': [
            'Bubble sort compares neighbouring pairs and swaps them if they are out of order; after each pass the largest remaining item has "bubbled" to the end. Selection sort finds the smallest item and swaps it into the next position. Insertion sort builds a sorted part one item at a time, like sorting playing cards in your hand.',
            'These simple sorts take O(n²) comparisons in the worst case. Merge sort splits the list in half, sorts each half recursively and merges the two sorted halves in a single pass, giving O(n log n) time.',
            'In real Python code you use sorted(data) or data.sort(), which use an efficient, stable algorithm (Timsort). The key parameter sorts by any property: sorted(people, key=lambda p: p[1]) sorts records by their second field.'],
        'formulas_label': 'Key facts',
        'formulas': ['Bubble / selection / insertion: O(n²)', 'Merge sort: O(n log n)', 'sorted(data, key=..., reverse=True)', 'Stable: equal items keep their original order'],
        'steps': ['Identify the algorithm.', 'Trace one pass carefully, noting swaps.', 'Repeat until the list is sorted.', 'In practice, use sorted() with a key.'],
        'worked_example': {
            'problem': 'Show the first pass of bubble sort on [5, 1, 4, 2].',
            'steps': ['Compare 5 and 1: swap → [1, 5, 4, 2].', 'Compare 5 and 4: swap → [1, 4, 5, 2].', 'Compare 5 and 2: swap → [1, 4, 2, 5].'],
            'answer': 'After the first pass the list is [1, 4, 2, 5], with the largest value in place.',
            'check': 'Running one pass of the course code gives [1, 4, 2, 5] ✓.'},
        'mistakes': ['Confusing selection sort with bubble sort.', 'Forgetting that merge needs both halves already sorted.', 'Using sort() and expecting it to return the list (it returns None).', 'Sorting numbers stored as strings ("10" comes before "9").'],
        'real_world': 'Online shops sort millions of products by price or rating instantly; they rely on O(n log n) sorting and on indexes, not on simple quadratic sorts.',
        'exam_strategy': 'Show the list after every pass or merge step. Trace questions award marks for intermediate states, not just the final sorted list.',
        'recap': ['Bubble: swap neighbours.', 'Selection: pick the minimum.', 'Merge: split, sort, merge.', 'Use sorted() with key in practice.']},
    T3: {
        'overview': 'Big O notation describes how an algorithm\'s running time (or memory use) grows as the input gets larger. It lets you compare algorithms independently of the computer.',
        'key_terms': ['Time complexity', 'Big O', 'Constant time', 'Logarithmic', 'Linear', 'Quadratic', 'Worst case', 'Space complexity'],
        'explanation': [
            'Count the basic operations as a function of n and keep only the fastest-growing term, ignoring constants. A loop over n items is O(n); two nested loops over n items are O(n²); halving the problem each step is O(log n); a dictionary lookup is O(1) on average.',
            'Growth rates matter at scale. For n = 1 000 000, an O(log n) search takes about 20 steps, O(n) about a million, and O(n²) about a trillion, which is far too slow. Doubling n doubles O(n) work but quadruples O(n²) work.',
            'Big O usually describes the worst case. Space complexity measures extra memory. Choosing the right data structure is often the biggest improvement: checking membership in a list is O(n), but in a set it is O(1) on average.'],
        'formulas_label': 'Common orders',
        'formulas': ['O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)', 'One loop over n: O(n)', 'Nested loops over n: O(n²)', 'Halving each step: O(log n)'],
        'steps': ['Identify the input size n.', 'Count how many times the main operation runs.', 'Keep the dominant term and drop constants.', 'Compare with alternatives.'],
        'worked_example': {
            'problem': 'A program checks whether any two numbers in a list of n numbers are equal by comparing every pair. What is its complexity, and how could it be improved?',
            'steps': ['Comparing every pair uses nested loops: about n²/2 comparisons, which is O(n²).', 'Alternative: add each number to a set and check membership before adding.', 'Each set operation is O(1) on average, so the total is O(n).'],
            'answer': 'O(n²) for the pairwise method; O(n) with a set.',
            'check': 'For n = 100 000 that is about 5 billion comparisons versus about 100 000 set operations.'},
        'mistakes': ['Keeping constants and lower terms (writing O(2n + 5) instead of O(n)).', 'Thinking O(n log n) is slower than O(n²).', 'Ignoring the hidden cost of operations such as x in list (which is O(n)).', 'Confusing time complexity with actual seconds.'],
        'real_world': 'A search engine that answers in milliseconds relies on O(log n) and O(1) index lookups; the same task with O(n) scanning of the web would be impossible.',
        'exam_strategy': 'Justify a Big O answer by pointing to the loop structure ("the outer loop runs n times and the inner loop n times, so O(n²)").',
        'recap': ['Big O = growth rate.', 'Drop constants and small terms.', 'log n ≪ n ≪ n log n ≪ n².', 'Data structures change complexity.']},
    T4: {
        'overview': 'Much everyday programming is data processing: reading records from files, cleaning them, filtering, grouping and summarising. Python\'s built-in tools make this short and clear.',
        'key_terms': ['CSV', 'DictReader', 'Filtering', 'Grouping', 'Aggregation', 'Counter', 'Data cleaning', 'pandas'],
        'explanation': [
            'csv.DictReader turns each row of a CSV file into a dictionary keyed by the column names, so code can say row["mark"] instead of row[1]. Values arrive as strings and must be converted with int() or float().',
            'Common steps are filtering (a list comprehension with a condition), grouping and totalling (a dictionary with get() to accumulate values per key), counting (collections.Counter) and sorting (sorted with a key). Together these answer questions such as "total sales per region" or "most common reason for a complaint".',
            'Real data are messy: missing values, extra spaces, inconsistent capitals and wrong types. Clean as you read (strip(), lower(), checks for empty fields). For large datasets, the pandas library provides fast tables (DataFrames) with grouping and summarising built in.'],
        'formulas_label': 'Patterns',
        'formulas': ['rows = list(csv.DictReader(f))', '[r for r in rows if condition]', 'totals[k] = totals.get(k, 0) + v', 'Counter(items).most_common(n)', 'sorted(rows, key=lambda r: r["mark"])'],
        'steps': ['Read the data into a list of records.', 'Clean and convert each field.', 'Filter the records you need.', 'Group, count or total.', 'Sort and present the result.'],
        'worked_example': {
            'problem': 'Sales records are ("north", 120), ("south", 80), ("north", 60). Find the total per region.',
            'steps': ['Start with totals = {}.', 'For each record: totals[region] = totals.get(region, 0) + amount.', 'north: 120 + 60 = 180; south: 80.'],
            'answer': 'totals is {"north": 180, "south": 80}.',
            'check': 'The grand total 260 equals the sum of all records ✓.'},
        'mistakes': ['Forgetting that CSV values are strings.', 'Not handling blank or malformed rows.', 'Overwriting totals instead of adding to them.', 'Treating "North" and "north" as different groups.'],
        'real_world': 'NGOs and businesses analyse survey and sales data exactly this way, often starting with a few lines of Python before moving to pandas or a dashboard.',
        'exam_strategy': 'Write the processing as clear steps (read, clean, filter, group, report) with a short comment for each; it shows structured thinking even if a detail is wrong.',
        'recap': ['DictReader for named columns.', 'Convert strings to numbers.', 'Group with a dictionary; count with Counter.', 'Clean messy data.']},
}
QUESTIONS = [
    # T1
    Q(T1, 'Binary search requires the data to be:', ['sorted', 'unique', 'numbers only', 'short'], 0, 'It discards half the range based on order.'),
    Q(T1, 'At most how many comparisons does binary search need for 1024 sorted items?', ['11', '10', '512', '1024'], 0, 'floor(log₂ 1024) + 1 = 11.', ans=11),
    Q(T1, 'Linear search for 3 in [7, 3, 9, 3] returns the index:', ['1', '3', '0', '2'], 0, 'It stops at the first match.'),
    Q(T1, 'Binary search for 5 in [3, 8, 12, 19, 25, 31, 40] returns:', ['−1 (not found)', '0', '1', '5'], 0, '5 is not in the list.'),
    Q(T1, 'About how many steps does binary search take for a million sorted items?', ['20', '1000', '500000', '1000000'], 0, 'log₂ 1 000 000 ≈ 20.', ans=20),
    Q(T1, 'For a single search of unsorted data, the better choice is usually:', ['linear search', 'binary search', 'sorting twice', 'merge sort'], 0, 'Sorting first would cost more than one linear scan.'),
    # T2
    Q(T2, 'After one pass of bubble sort on [5, 1, 4, 2], the list is:', ['[1, 4, 2, 5]', '[1, 2, 4, 5]', '[1, 5, 4, 2]', '[5, 4, 2, 1]'], 0, 'Neighbours are swapped as the 5 bubbles to the end.'),
    Q(T2, 'After the first step of selection sort on [29, 10, 14, 37, 13], the list is:', ['[10, 29, 14, 37, 13]', '[10, 13, 14, 29, 37]', '[29, 10, 14, 13, 37]', '[13, 10, 14, 37, 29]'], 0, 'The minimum, 10, is swapped into position 0.'),
    Q(T2, 'Merging the sorted lists [1, 4, 9] and [2, 3, 10] gives:', ['[1, 2, 3, 4, 9, 10]', '[1, 4, 9, 2, 3, 10]', '[1, 2, 4, 3, 9, 10]', '[10, 9, 4, 3, 2, 1]'], 0, 'Take the smaller front item each time.'),
    Q(T2, 'The worst-case time of bubble sort is:', ['O(n²)', 'O(n log n)', 'O(n)', 'O(log n)'], 0, 'Up to n passes of up to n comparisons.'),
    Q(T2, 'Sorting [("Ada", 31), ("Bo", 25), ("Chi", 28)] by age gives names in the order:', ['Bo, Chi, Ada', 'Ada, Bo, Chi', 'Ada, Chi, Bo', 'Chi, Bo, Ada'], 0, '25, 28, 31.'),
    Q(T2, 'What does a.sort() return?', ['None', 'the sorted list', 'the original list', 'True'], 0, 'It sorts in place; use sorted(a) to get a new list.'),
    # T3
    Q(T3, 'Two nested loops each running n times have complexity:', ['O(n²)', 'O(2n)', 'O(n)', 'O(log n)'], 0, 'n × n operations.'),
    Q(T3, 'Which grows slowest as n increases?', ['O(log n)', 'O(n)', 'O(n log n)', 'O(n²)'], 0, 'Logarithmic growth is very slow.'),
    Q(T3, 'O(3n + 7) simplifies to:', ['O(n)', 'O(3n)', 'O(n + 7)', 'O(1)'], 0, 'Drop constants and lower terms.'),
    Q(T3, 'Doubling the input size of an O(n²) algorithm multiplies the work by about:', ['4', '2', '8', '1'], 0, '(2n)² = 4n².', ans=4),
    Q(T3, 'Checking x in a Python list of n items is:', ['O(n)', 'O(1)', 'O(log n)', 'O(n²)'], 0, 'It may scan every item; a set makes it O(1) on average.'),
    Q(T3, 'Merge sort runs in:', ['O(n log n)', 'O(n²)', 'O(n)', 'O(log n)'], 0, 'log n levels of splitting, n work per level.'),
    # T4
    Q(T4, 'Marks 72, 58 and 90 read with csv.DictReader. Their average is about:', ['73.3', '72', '58', '220'], 0, '220 ÷ 3 ≈ 73.33.'),
    Q(T4, 'Totalling ("north", 120), ("south", 80), ("north", 60) by region gives north =', ['180', '120', '260', '60'], 0, '120 + 60.', ans=180),
    Q(T4, 'How many of the marks [72, 58, 90, 45] are 50 or more?', ['3', '2', '4', '1'], 0, '72, 58 and 90.', ans=3),
    Q(T4, 'Counter("mississippi").most_common(1) gives:', ['[("i", 4)]', '[("s", 4)]', '[("m", 1)]', '[("p", 2)]'], 0, 'i and s both appear 4 times; i is counted first in order of first appearance.'),
    Q(T4, 'Values read by csv.DictReader are:', ['strings', 'integers', 'floats', 'already the right type'], 0, 'Convert them before doing arithmetic.'),
    Q(T4, 'Which library is widely used for large tabular datasets in Python?', ['pandas', 'random', 'math', 'turtle'], 0, 'Its DataFrame supports fast grouping and summaries.'),
]

FLASH = [
    ['Linear search', 'Checks each item in turn; O(n); any data.'],
    ['Binary search', 'Halves a sorted range each step; O(log n).'],
    ['Bubble sort', 'Swap neighbours; largest bubbles to the end; O(n²).'],
    ['Merge sort', 'Split, sort halves, merge; O(n log n).'],
    ['Big O', 'Growth rate of work with input size; drop constants.'],
    ['Common orders', 'O(1) < O(log n) < O(n) < O(n log n) < O(n²).'],
    ['Group and total', 'totals[k] = totals.get(k, 0) + v.'],
    ['csv.DictReader', 'Rows as dictionaries; values are strings.'],
]
