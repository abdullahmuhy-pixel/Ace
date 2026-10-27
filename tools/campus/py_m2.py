"""Programming with Python, module 2: Data structures."""
from verify import Q
from py_common import check as c
T1, T2, T3, T4 = ('Lists', 'Tuples and dictionaries', 'Sets', 'Comprehensions and nested data')

A = [
    c('a = [3, 1, 4]\na.append(1)\nprint(a)', '[3, 1, 4, 1]'), c('a = [3, 1, 4, 1]\nprint(len(a), a[2])', '4 4'),
    c('a = [5, 2, 9]\na.sort()\nprint(a)', '[2, 5, 9]'), c('a = [10, 20, 30, 40]\nprint(a[1:3])', '[20, 30]'),
    c('a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)', '[1, 2, 3, 4]'), c('a = [4, 8, 15]\nprint(sum(a), max(a))', '27 15'),
    c('a = [1, 2, 3]\na.insert(0, 9)\nprint(a)', '[9, 1, 2, 3]'), c('a = [1, 2, 3]\nprint(a.pop(), a)', '3 [1, 2]'),
    c('d = {"Ada": 85, "Kofi": 72}\nprint(d["Kofi"])', '72'), c('d = {"a": 1}\nd["b"] = 2\nprint(len(d))', '2'),
    c('d = {"a": 1}\nprint(d.get("z", 0))', '0'), c('t = (2, 4, 6)\nprint(t[1])', '4'),
    c('d = {"x": 1, "y": 2}\nprint(list(d.keys()))', "['x', 'y']"), c('x, y = (3, 7)\nprint(y)', '7'),
    c('s = {1, 2, 2, 3}\nprint(len(s))', '3'), c('a = {1, 2, 3}\nb = {2, 3, 4}\nprint(sorted(a & b))', '[2, 3]'),
    c('a = {1, 2, 3}\nb = {2, 3, 4}\nprint(sorted(a | b))', '[1, 2, 3, 4]'), c('a = {1, 2, 3}\nb = {2, 3, 4}\nprint(sorted(a - b))', '[1]'),
    c('print(3 in {1, 2, 3})', 'True'), c('print(len(set("banana")))', '3'),
    c('print([x * x for x in range(4)])', '[0, 1, 4, 9]'), c('print([x for x in range(10) if x % 3 == 0])', '[0, 3, 6, 9]'),
    c('m = [[1, 2], [3, 4]]\nprint(m[1][0])', '3'), c('print({w: len(w) for w in ["hi", "sun"]})', "{'hi': 2, 'sun': 3}"),
    c('m = [[1, 2], [3, 4]]\nprint(sum(sum(r) for r in m))', '10'), c('names = ["Ada", "Bo"]\nprint([n.upper() for n in names])', "['ADA', 'BO']"),
]

MODULE = {
    'title': 'Data structures',
    'topics': [T1, T2, T3, T4],
    'overview': 'Real programs work with collections of data: lists of marks, records of students, sets of unique tags. Python\'s built-in data structures (lists, tuples, dictionaries and sets) cover most needs, and comprehensions let you build new collections in one clear line.',
    'key_terms': ['List', 'Mutable', 'Index', 'Method', 'Tuple', 'Immutable', 'Dictionary', 'Key', 'Set', 'Comprehension'],
    'explanation': [
        'A list is an ordered, changeable (mutable) sequence: you can add, remove and sort items. A tuple is like a list but cannot be changed (immutable), which makes it useful for fixed records such as coordinates.',
        'A dictionary maps keys to values, like a phone book: look up a value by its key instead of by position. A set stores unique items with no order and supports fast membership tests and set operations such as union and intersection.',
        'Choosing the right structure makes code simpler and faster. Use a list for an ordered collection, a dictionary for lookups by name or ID, a set for uniqueness and membership, and a tuple for small fixed groups. Comprehensions build lists, sets and dictionaries from other collections concisely.'],
    'quick_facts': [
        'Lists are mutable and ordered: a.append(x), a.sort(), a[i].',
        'Assigning b = a makes b refer to the same list, not a copy.',
        'Dictionary lookup: d[key]; safe lookup: d.get(key, default).',
        'Sets remove duplicates: | union, & intersection, - difference.',
        '[expr for x in seq if cond] builds a list.'],
}

NOTES = {
    T1: {
        'overview': 'A list holds an ordered collection of items that can be changed. Lists are the most-used data structure in Python.',
        'key_terms': ['List', 'Index', 'Slice', 'append', 'insert', 'pop', 'sort', 'Aliasing'],
        'explanation': [
            'Create a list with square brackets: marks = [72, 85, 60]. Access items by index from 0 (marks[0] is 72) and use slices such as marks[1:3]. len(), sum(), min() and max() work on lists of numbers.',
            'Lists are mutable. append(x) adds to the end, insert(i, x) adds at a position, pop() removes and returns the last item (or pop(i) for a position), remove(x) deletes the first matching value and sort() sorts in place. sorted(a) returns a new sorted list without changing a.',
            'Assigning b = a does not copy the list: both names refer to the same object, so changing b changes a. This is called aliasing. Use b = a.copy() or b = a[:] for a separate copy.'],
        'formulas_label': 'List methods',
        'formulas': ['a.append(x), a.insert(i, x)', 'a.pop(), a.remove(x)', 'a.sort() (in place) vs sorted(a) (new list)', 'b = a.copy() for an independent copy'],
        'steps': ['Create the list.', 'Access or slice by index.', 'Change it with methods.', 'Copy explicitly if you need the original unchanged.'],
        'worked_example': {
            'problem': 'a = [1, 2, 3]; b = a; b.append(4). What is a now, and how would you avoid this?',
            'steps': ['b = a makes b another name for the same list.', 'b.append(4) changes that single list.', 'So a also shows the change.'],
            'answer': 'a is [1, 2, 3, 4]. Use b = a.copy() to get an independent list.',
            'check': 'Running the code confirms a prints [1, 2, 3, 4].'},
        'mistakes': ['Expecting b = a to copy the list.', 'Writing a = a.sort(), which sets a to None.', 'Indexing past the end (IndexError).', 'Modifying a list while looping over it.'],
        'real_world': 'A class register or a shopping basket in an app is naturally a list: ordered, and items are added and removed.',
        'exam_strategy': 'When a question mixes assignment and methods, draw boxes for objects and arrows for names. Aliasing questions become easy to trace.',
        'recap': ['Ordered and mutable.', 'Index from 0; slices stop before the end.', 'sort() vs sorted().', 'b = a is not a copy.']},
    T2: {
        'overview': 'Tuples are fixed, ordered groups of values. Dictionaries store key–value pairs for fast lookup by key.',
        'key_terms': ['Tuple', 'Immutable', 'Unpacking', 'Dictionary', 'Key', 'Value', 'get()', 'items()'],
        'explanation': [
            'A tuple is written with brackets: point = (3, 7). It cannot be changed after creation, which protects data that should stay fixed. Tuples support unpacking: x, y = point sets x to 3 and y to 7. Functions often return several values as a tuple.',
            'A dictionary maps unique keys to values: scores = {"Ada": 85, "Kofi": 72}. scores["Kofi"] gives 72. Assigning to a new key adds it; assigning to an existing key replaces the value. Looking up a missing key with [] raises a KeyError, so d.get(key, default) is safer.',
            'Loop over a dictionary with for k, v in d.items(). keys() and values() give the keys and values. Since Python 3.7, dictionaries keep insertion order. Keys must be immutable (strings, numbers, tuples), but values can be anything, including lists and other dictionaries.'],
        'formulas_label': 'Syntax',
        'formulas': ['t = (a, b, c); x, y = (3, 7)', 'd = {key: value}', 'd[key], d[key] = value, d.get(key, default)', 'for k, v in d.items():'],
        'steps': ['Use a tuple for fixed groups and returning several values.', 'Use a dictionary when you look things up by a key.', 'Use get() when a key may be missing.', 'Loop with items() to get keys and values together.'],
        'worked_example': {
            'problem': 'Count how many times each word appears in the list ["a", "b", "a", "c", "a"].',
            'steps': ['counts = {}', 'for w in words: counts[w] = counts.get(w, 0) + 1', 'This adds 1 to the existing count or starts from 0.'],
            'answer': 'counts is {"a": 3, "b": 1, "c": 1}.',
            'check': 'The counts add up to 5, the number of words ✓.'},
        'mistakes': ['Trying to change a tuple item.', 'Using d[key] for a key that may not exist.', 'Using a list as a dictionary key.', 'Expecting keys to be looked up by position.'],
        'real_world': 'Dictionaries are how programs store records such as {"name": ..., "age": ...}, and they map directly onto JSON, the format most web APIs use.',
        'exam_strategy': 'When asked to choose a structure, justify it: "a dictionary, because we need to look up each student\'s mark by name quickly".',
        'recap': ['Tuples are immutable; unpack them.', 'Dictionaries map keys to values.', 'get() avoids KeyError.', 'items() for looping.']},
    T3: {
        'overview': 'A set is an unordered collection of unique items. Sets remove duplicates and make membership tests and set operations simple and fast.',
        'key_terms': ['Set', 'Unique', 'Membership', 'Union', 'Intersection', 'Difference', 'Hashing'],
        'explanation': [
            'Create a set with braces, s = {1, 2, 3}, or from a sequence with set(...). Duplicates are dropped automatically, so set("banana") is {"b", "a", "n"}, with 3 items. An empty set is set(), because {} creates an empty dictionary.',
            'Sets support the operations from mathematics: a | b (union, items in either), a & b (intersection, items in both), a - b (difference, items in a but not b). x in s is very fast, even for large sets, because sets use hashing.',
            'Sets have no order and no indexing; use sorted(s) to get an ordered list. Like dictionary keys, set items must be immutable.'],
        'formulas_label': 'Operations',
        'formulas': ['a | b union', 'a & b intersection', 'a - b difference', 'x in s membership', 'set() is the empty set; {} is an empty dict'],
        'steps': ['Convert the data to a set to remove duplicates.', 'Use set operations to compare groups.', 'Use in for fast membership tests.', 'Sort if you need an ordered result.'],
        'worked_example': {
            'problem': 'Students in Maths: {"Ada", "Bo", "Chi"}; in Physics: {"Bo", "Chi", "Dan"}. Who takes both? Who takes Maths only?',
            'steps': ['Both: maths & physics = {"Bo", "Chi"}.', 'Maths only: maths - physics = {"Ada"}.', 'Either: maths | physics has 4 students.'],
            'answer': 'Both: Bo and Chi; Maths only: Ada.',
            'check': '|M ∪ P| = |M| + |P| − |M ∩ P| = 3 + 3 − 2 = 4 ✓.'},
        'mistakes': ['Using {} to create an empty set.', 'Trying to index a set.', 'Expecting a set to keep the original order.', 'Putting lists inside a set.'],
        'real_world': 'Spam filters and social networks use sets to check instantly whether an address is on a block list or whether two users share friends.',
        'exam_strategy': 'Draw a quick Venn diagram for set-operation questions; it makes |, & and - easy to read off.',
        'recap': ['Unique, unordered items.', 'Union, intersection, difference.', 'Fast membership with in.', 'set() for an empty set.']},
    T4: {
        'overview': 'Comprehensions build new lists, sets or dictionaries from existing data in one readable line. Nested lists represent tables and grids.',
        'key_terms': ['List comprehension', 'Filter', 'Dictionary comprehension', 'Nested list', 'Row and column', 'Generator expression'],
        'explanation': [
            'A list comprehension [expr for x in seq] applies an expression to each item. Adding a condition filters: [x for x in range(10) if x % 3 == 0] gives [0, 3, 6, 9]. It replaces a for loop that appends to a list.',
            'The same idea builds dictionaries and sets: {w: len(w) for w in words} maps each word to its length. A generator expression such as sum(x * x for x in data) computes values one at a time without building a list.',
            'A nested list stores a table: m = [[1, 2], [3, 4]]. m[1][0] is row 1, column 0, which is 3. Loop over rows with for row in m and over values with an inner loop. Comprehensions are great when short; if one becomes hard to read, use an ordinary loop.'],
        'formulas_label': 'Syntax',
        'formulas': ['[expr for x in seq]', '[expr for x in seq if condition]', '{k: v for x in seq}', 'm[row][col] for nested lists', 'sum(expr for x in seq)'],
        'steps': ['Write the loop you would use.', 'Move the expression to the front.', 'Add the condition at the end.', 'Check readability.'],
        'worked_example': {
            'problem': 'Given names = ["Ada", "Bo"], build a list of the names in capitals, and a dictionary of name lengths.',
            'steps': ['[n.upper() for n in names] gives ["ADA", "BO"].', '{n: len(n) for n in names} gives {"Ada": 3, "Bo": 2}.', 'Each replaces a three-line loop.'],
            'answer': '["ADA", "BO"] and {"Ada": 3, "Bo": 2}.',
            'check': 'Running both lines in Python gives exactly these results.'},
        'mistakes': ['Putting the condition before for.', 'Confusing m[0][1] (row 0, column 1) with m[1][0].', 'Writing very long comprehensions that hide the logic.', 'Creating a grid with [[0] * 3] * 3, which repeats the same inner list.'],
        'real_world': 'Data scientists use comprehensions constantly to clean data, for example removing empty entries from survey responses or converting every price to a float.',
        'exam_strategy': 'If asked to rewrite a loop as a comprehension (or the reverse), show both versions; they are a common short question.',
        'recap': ['[expr for x in seq if cond].', 'Dictionary and set comprehensions.', 'm[row][col].', 'Keep comprehensions readable.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'a = [3, 1, 4]; a.append(1). What is a?', ['[3, 1, 4, 1]', '[1, 3, 1, 4]', '[3, 1, 4]', '[1, 1, 3, 4]'], 0, 'append adds to the end.'),
    Q(T1, 'a = [5, 2, 9]; a.sort(). What is a?', ['[2, 5, 9]', '[9, 5, 2]', '[5, 2, 9]', 'None'], 0, 'sort() sorts in place, ascending.'),
    Q(T1, 'a = [10, 20, 30, 40]. What is a[1:3]?', ['[20, 30]', '[10, 20, 30]', '[20, 30, 40]', '[10, 20]'], 0, 'Indices 1 and 2.'),
    Q(T1, 'a = [1, 2, 3]; b = a; b.append(4). What is a?', ['[1, 2, 3, 4]', '[1, 2, 3]', '[4, 1, 2, 3]', 'An error'], 0, 'a and b name the same list.'),
    Q(T1, 'a = [4, 8, 15]. What do sum(a) and max(a) give?', ['27 and 15', '27 and 4', '15 and 27', '3 and 15'], 0, '4 + 8 + 15 = 27.'),
    Q(T1, 'a = [1, 2, 3]. What does a.pop() return?', ['3', '1', '[1, 2]', 'None'], 0, 'pop() removes and returns the last item.'),
    # T2
    Q(T2, 'd = {"Ada": 85, "Kofi": 72}. What is d["Kofi"]?', ['72', '85', '"Kofi"', 'An error'], 0, 'Look up by key.'),
    Q(T2, 'd = {"a": 1}. What is d.get("z", 0)?', ['0', 'None', 'An error', '1'], 0, 'get() returns the default for a missing key.'),
    Q(T2, 't = (2, 4, 6). What is t[1]?', ['4', '2', '6', 'An error'], 0, 'Index from 0.'),
    Q(T2, 'x, y = (3, 7). What is y?', ['7', '3', '(3, 7)', 'An error'], 0, 'Tuple unpacking.'),
    Q(T2, 'What happens with t = (1, 2); t[0] = 5?', ['A TypeError: tuples cannot be changed', 't becomes (5, 2)', 't becomes (1, 5)', 'Nothing'], 0, 'Tuples are immutable.'),
    Q(T2, 'Which cannot be a dictionary key?', ['A list', 'A string', 'An integer', 'A tuple of numbers'], 0, 'Keys must be immutable.'),
    # T3
    Q(T3, 'What is len({1, 2, 2, 3})?', ['3', '4', '2', '1'], 0, 'Duplicates are removed.'),
    Q(T3, 'a = {1, 2, 3}, b = {2, 3, 4}. What is sorted(a & b)?', ['[2, 3]', '[1, 2, 3, 4]', '[1]', '[4]'], 0, 'Intersection: in both.'),
    Q(T3, 'a = {1, 2, 3}, b = {2, 3, 4}. What is sorted(a | b)?', ['[1, 2, 3, 4]', '[2, 3]', '[1, 4]', '[1]'], 0, 'Union: in either.'),
    Q(T3, 'a = {1, 2, 3}, b = {2, 3, 4}. What is sorted(a - b)?', ['[1]', '[4]', '[2, 3]', '[1, 4]'], 0, 'Difference: in a, not in b.'),
    Q(T3, 'What is len(set("banana"))?', ['3', '6', '2', '1'], 0, 'Unique letters b, a, n.'),
    Q(T3, 'How do you create an empty set?', ['set()', '{}', '[]', 'set[]'], 0, '{} creates an empty dictionary.'),
    # T4
    Q(T4, 'What is [x * x for x in range(4)]?', ['[0, 1, 4, 9]', '[1, 4, 9, 16]', '[0, 1, 2, 3]', '[0, 2, 4, 6]'], 0, 'Squares of 0 to 3.'),
    Q(T4, 'What is [x for x in range(10) if x % 3 == 0]?', ['[0, 3, 6, 9]', '[3, 6, 9]', '[0, 3, 6]', '[1, 4, 7]'], 0, 'Multiples of 3 from 0 to 9.'),
    Q(T4, 'm = [[1, 2], [3, 4]]. What is m[1][0]?', ['3', '2', '1', '4'], 0, 'Row 1, column 0.'),
    Q(T4, 'm = [[1, 2], [3, 4]]. What is sum(sum(r) for r in m)?', ['10', '3', '7', '[3, 7]'], 0, '3 + 7.'),
    Q(T4, 'What is {w: len(w) for w in ["hi", "sun"]}?', ['{"hi": 2, "sun": 3}', '{2: "hi", 3: "sun"}', '["hi", "sun"]', '{5}'], 0, 'Each word maps to its length.'),
    Q(T4, 'Which is a correct list comprehension?', ['[n for n in nums if n > 0]', '[if n > 0 for n in nums]', '[for n in nums: n]', '[n if n > 0 in nums]'], 0, 'Expression, then for, then if.'),
]

FLASH = [
    ['List', 'Ordered, mutable: append, insert, pop, sort.'],
    ['Aliasing', 'b = a makes both names refer to the same list; use a.copy().'],
    ['sort() vs sorted()', 'sort() changes the list; sorted() returns a new one.'],
    ['Tuple', 'Ordered and immutable; supports unpacking.'],
    ['Dictionary', 'Key → value; d.get(key, default) avoids KeyError.'],
    ['Set', 'Unique, unordered; |, &, - operations; fast membership.'],
    ['List comprehension', '[expr for x in seq if condition].'],
    ['Nested list access', 'm[row][col].'],
]
