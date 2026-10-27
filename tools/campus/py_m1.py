"""Programming with Python, module 1: Python basics."""
from verify import Q
from py_common import check
T1, T2, T3, T4 = ('Variables, types and expressions', 'Input, output and strings', 'Making decisions with if', 'Repeating with loops')

c = check
A = [
    c('print(7 // 2)', '3'), c('print(7 % 2)', '1'), c('print(7 / 2)', '3.5'), c('print(2 ** 3)', '8'),
    c('print(type(3.0).__name__)', 'float'), c('print(int("12") + 3)', '15'), c('print(3 + 4 * 2)', '11'),
    c('name = "Ada"\nprint("Hi " + name)', 'Hi Ada'), c('print(len("Nairobi"))', '7'), c('s = "python"\nprint(s[0], s[-1])', 'p n'),
    c('s = "python"\nprint(s[1:4])', 'yth'), c('print("ab" * 3)', 'ababab'), c('x = 3.14159\nprint(f"{x:.2f}")', '3.14'),
    c('print("Lagos".upper())', 'LAGOS'),
    c('m = 65\nif m >= 70:\n    print("A")\nelif m >= 50:\n    print("C")\nelse:\n    print("F")', 'C'),
    c('x = 5\nprint(x > 3 and x < 10)', 'True'), c('print(not (4 == 4))', 'False'), c('n = 7\nprint("even" if n % 2 == 0 else "odd")', 'odd'),
    c('t = 0\nfor i in range(1, 5):\n    t += i\nprint(t)', '10'), c('print(list(range(2, 10, 3)))', '[2, 5, 8]'),
    c('n = 1\nwhile n < 20:\n    n *= 2\nprint(n)', '32'),
    c('for i in range(5):\n    if i == 3:\n        break\nprint(i)', '3'),
    c('c = 0\nfor ch in "banana":\n    if ch == "a":\n        c += 1\nprint(c)', '3'),
    c('total = 0\nfor i in range(10):\n    if i % 2:\n        continue\n    total += i\nprint(total)', '20'),
]

MODULE = {
    'title': 'Python basics',
    'topics': [T1, T2, T3, T4],
    'overview': 'Python is one of the most widely used programming languages in science, data, web development and automation, and it is the usual first language in university computing courses. This module covers the building blocks every program uses: values and variables, input and output, decisions and loops.',
    'key_terms': ['Variable', 'Data type', 'Expression', 'String', 'f-string', 'Condition', 'Boolean', 'for loop', 'while loop', 'range'],
    'explanation': [
        'A program is a sequence of instructions. Python runs them top to bottom, storing values in variables. Each value has a type, such as int (whole numbers), float (decimals), str (text) and bool (True or False), and the type decides which operations make sense.',
        'Programs talk to users through input() and print(). input() always returns a string, so numbers must be converted with int() or float(). Strings can be joined, repeated, sliced and formatted, and f-strings are the clearest way to mix text and values.',
        'Control flow lets a program choose and repeat. if, elif and else choose between paths using Boolean conditions. for loops repeat over a sequence such as range(); while loops repeat while a condition stays true. Indentation (four spaces) shows which lines belong to each block, and it is part of Python\'s syntax.'],
    'quick_facts': [
        '/ always gives a float; // is floor division; % is the remainder; ** is a power.',
        'input() returns a string: convert with int() or float().',
        'Indexing starts at 0; s[-1] is the last character; s[a:b] stops before b.',
        'range(a, b, step) stops before b.',
        'break leaves a loop; continue skips to the next iteration.'],
}

NOTES = {
    T1: {
        'overview': 'Variables store values so a program can use and change them. Every value has a type, and operators combine values into expressions.',
        'key_terms': ['Variable', 'Assignment', 'int', 'float', 'str', 'bool', 'Operator precedence', 'Type conversion'],
        'explanation': [
            'Assignment uses =: price = 250 stores 250 in the variable price. Names should describe their contents (total_marks, not t), may contain letters, digits and underscores, and cannot start with a digit. Python is case-sensitive, so Total and total are different variables.',
            'Arithmetic operators are +, -, *, / (true division, always a float), // (floor division), % (remainder) and ** (power). Python follows the usual precedence: ** first, then *, /, //, %, then + and -. Use brackets when in doubt: 3 + 4 * 2 is 11, but (3 + 4) * 2 is 14.',
            'type() shows a value\'s type. Converting between types uses int(), float() and str(). int("12") + 3 is 15, but "12" + 3 is an error, because Python does not silently mix text and numbers.'],
        'formulas_label': 'Operators',
        'formulas': ['7 / 2 → 3.5   7 // 2 → 3   7 % 2 → 1   2 ** 3 → 8', 'Precedence: ** then * / // % then + -', 'int("12") → 12, str(5) → "5", float("2.5") → 2.5', 'x += 1 means x = x + 1'],
        'steps': ['Choose a clear variable name.', 'Assign a value of the right type.', 'Build the expression, adding brackets for clarity.', 'Convert types where needed.', 'Print the result to check it.'],
        'worked_example': {
            'problem': 'A student has 135 minutes of video lectures. Write expressions for the number of whole hours and the minutes left over.',
            'steps': ['hours = 135 // 60 gives 2.', 'minutes = 135 % 60 gives 15.', 'print(hours, "h", minutes, "min") shows 2 h 15 min.'],
            'answer': 'hours = 135 // 60 → 2 and minutes = 135 % 60 → 15.',
            'check': '2 × 60 + 15 = 135 ✓.'},
        'mistakes': ['Using = (assignment) where == (comparison) is meant.', 'Expecting 7 / 2 to give 3.', 'Adding a string and a number.', 'Starting a variable name with a digit or using spaces.'],
        'real_world': 'Mobile-money apps use // and % to split amounts into notes and coins, and to work out fees on banded transaction amounts.',
        'exam_strategy': 'When asked what an expression evaluates to, work through the precedence step by step and write the type of the result (int or float) as well as the value.',
        'recap': ['Variables store values; = assigns.', 'int, float, str, bool.', '/ vs // vs %.', 'Convert types explicitly.']},
    T2: {
        'overview': 'Programs read input from the user and display results. Because input always arrives as text, strings and conversions are central to almost every program.',
        'key_terms': ['print()', 'input()', 'String', 'Index', 'Slice', 'Concatenation', 'f-string', 'Method'],
        'explanation': [
            'print() displays values separated by spaces. input("prompt") shows a prompt and returns what the user types as a string. To read a number: age = int(input("Age: ")).',
            'A string is a sequence of characters, indexed from 0. s[0] is the first character and s[-1] the last. Slices s[a:b] take characters from index a up to but not including b. len(s) gives the length. + joins strings and * repeats them.',
            'String methods return new strings: upper(), lower(), strip() removes surrounding spaces, replace(), split() breaks text into a list. f-strings insert values neatly: f"Total: {total:.2f}" shows the total with two decimal places.'],
        'formulas_label': 'String tools',
        'formulas': ['s[0], s[-1], s[a:b], len(s)', '"ab" + "cd" → "abcd"; "ab" * 3 → "ababab"', 's.upper(), s.lower(), s.strip(), s.split()', 'f"{x:.2f}" formats to 2 decimal places'],
        'steps': ['Read input with input().', 'Convert to a number if needed.', 'Process the value.', 'Format the output with an f-string.'],
        'worked_example': {
            'problem': 'Write a program that asks for a price and a quantity, then prints the total with two decimal places.',
            'steps': ['price = float(input("Price: "))', 'qty = int(input("Quantity: "))', 'print(f"Total: {price * qty:.2f}")'],
            'answer': 'For price 12.5 and quantity 3 it prints Total: 37.50.',
            'check': 'Without float() and int(), price * qty would fail, because both inputs are strings.'},
        'mistakes': ['Forgetting that input() returns a string.', 'Thinking s[1:4] includes index 4.', 'Expecting a method like upper() to change the original string (strings are immutable).', 'Mixing quotes incorrectly inside strings.'],
        'real_world': 'Registration systems clean user input with strip() and lower() so that " Ada@Mail.com " and "ada@mail.com" are recognised as the same email address.',
        'exam_strategy': 'For slicing questions, write the indices above the characters before reading off the answer. It prevents off-by-one errors.',
        'recap': ['input() gives a string.', 'Index from 0; slices stop before the end.', 'Methods return new strings.', 'f-strings for formatting.']},
    T3: {
        'overview': 'if statements let a program choose what to do based on conditions. Conditions are Boolean expressions that are either True or False.',
        'key_terms': ['Boolean', 'Comparison operator', 'if', 'elif', 'else', 'and', 'or', 'not', 'Nested condition'],
        'explanation': [
            'Comparisons (==, !=, <, <=, >, >=) produce True or False. Combine them with and (both true), or (at least one true) and not (reverses a value). Python also allows chained comparisons such as 0 <= mark <= 100.',
            'An if statement runs its block only when the condition is true. elif adds further conditions, checked in order, and else catches everything left. Only the first matching branch runs, so order matters: check the strictest condition first.',
            'A conditional expression gives a value in one line: label = "even" if n % 2 == 0 else "odd". Keep conditions readable; deeply nested ifs are often clearer as elif chains.'],
        'formulas_label': 'Syntax',
        'formulas': ['if condition:   (indented block)', 'elif other_condition:', 'else:', 'a if condition else b', 'and, or, not; ==, !=, <, <=, >, >='],
        'steps': ['List the cases the program must handle.', 'Order them from most to least specific.', 'Write if / elif / else with correct indentation.', 'Test each branch with sample values, including boundaries.'],
        'worked_example': {
            'problem': 'Write code that prints a grade: A for marks of 70 or more, C for 50 to 69, and F below 50. What does it print for 65?',
            'steps': ['if m >= 70: print("A")', 'elif m >= 50: print("C")', 'else: print("F")'],
            'answer': 'For m = 65 it prints C.',
            'check': 'Test the boundaries too: 70 → A, 50 → C, 49 → F.'},
        'mistakes': ['Using = instead of == in a condition.', 'Putting a broad condition first so later branches never run.', 'Forgetting the colon or the indentation.', 'Writing x == 1 or 2 instead of x == 1 or x == 2.'],
        'real_world': 'Loan apps use chains of conditions to decide whether to approve an application, for example checking income, existing debt and repayment history in order.',
        'exam_strategy': 'Trace the code with the given value line by line, noting which condition is true first. Write down the branch taken before giving the output.',
        'recap': ['Comparisons give True or False.', 'and, or, not combine conditions.', 'First true branch wins.', 'Test boundary values.']},
    T4: {
        'overview': 'Loops repeat code. for loops go through a sequence a known number of times; while loops repeat until a condition becomes false.',
        'key_terms': ['for loop', 'range()', 'while loop', 'Accumulator', 'Counter', 'break', 'continue', 'Infinite loop'],
        'explanation': [
            'for i in range(5) runs with i = 0, 1, 2, 3, 4. range(a, b) starts at a and stops before b; range(a, b, step) uses a step. A for loop can also go through the characters of a string or the items of a list.',
            'A common pattern is the accumulator: start total = 0, then add to it inside the loop. A counter adds 1 each time a condition is met. Summing 1 to 4 with a loop gives 10.',
            'A while loop repeats while its condition is true, so something inside must eventually make it false, or the loop runs forever. break exits a loop immediately; continue skips the rest of the current iteration and moves to the next.'],
        'formulas_label': 'Syntax',
        'formulas': ['for i in range(start, stop, step):', 'for item in sequence:', 'while condition:', 'total += value  (accumulator)', 'break exits; continue skips'],
        'steps': ['Decide: known number of repeats (for) or until a condition (while)?', 'Initialise any accumulator or counter before the loop.', 'Update inside the loop.', 'Make sure a while loop can end.', 'Trace a few iterations to check.'],
        'worked_example': {
            'problem': 'What does this print? n = 1, then while n < 20: n *= 2, then print(n).',
            'steps': ['n goes 1 → 2 → 4 → 8 → 16.', '16 < 20, so the loop runs again: n = 32.', '32 < 20 is false, so the loop stops.'],
            'answer': 'It prints 32.',
            'check': 'The loop checks the condition before each pass, so it can overshoot 20.'},
        'mistakes': ['Off-by-one errors with range (range(1, 5) stops at 4).', 'Forgetting to update the variable in a while loop.', 'Resetting the accumulator inside the loop.', 'Confusing break with continue.'],
        'real_world': 'A loop that reads every row of a sales file and adds up the totals is one of the most common programs in business data work.',
        'exam_strategy': 'Use a trace table with one row per iteration and a column for each variable. It is the most reliable way to answer "what is printed?" questions.',
        'recap': ['for: known repeats; while: until a condition.', 'range stops before the end.', 'Accumulators start before the loop.', 'break vs continue.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'What does print(7 // 2) display?', ['3', '3.5', '4', '1'], 0, '// is floor division.'),
    Q(T1, 'What does print(7 % 2) display?', ['1', '3', '3.5', '0'], 0, '% gives the remainder.'),
    Q(T1, 'What does print(3 + 4 * 2) display?', ['11', '14', '24', '10'], 0, 'Multiplication comes before addition.'),
    Q(T1, 'What is the type of 3.0?', ['float', 'int', 'str', 'bool'], 0, 'It has a decimal point.'),
    Q(T1, 'What does print(int("12") + 3) display?', ['15', '123', 'An error', '12 3'], 0, 'int("12") converts the text to 12.'),
    Q(T1, 'Which is a valid variable name?', ['total_marks', '2nd_score', 'total marks', 'class'], 0, 'Names cannot start with a digit, contain spaces, or be keywords such as class.'),
    # T2
    Q(T2, 'What does print(len("Nairobi")) display?', ['7', '6', '8', 'Nairobi'], 0, 'Seven characters.'),
    Q(T2, 's = "python". What is s[1:4]?', ['yth', 'pyt', 'ytho', 'tho'], 0, 'Indices 1, 2 and 3.'),
    Q(T2, 's = "python". What is s[-1]?', ['n', 'p', 'o', 'An error'], 0, 'Negative indices count from the end.'),
    Q(T2, 'What does print("ab" * 3) display?', ['ababab', 'ab3', 'An error', 'aaabbb'], 0, '* repeats a string.'),
    Q(T2, 'x = 3.14159. What does print(f"{x:.2f}") display?', ['3.14', '3.1', '3.14159', '3.142'], 0, '.2f rounds to two decimal places.'),
    Q(T2, 'age = input("Age: ") and the user types 20. What is the type of age?', ['str', 'int', 'float', 'bool'], 0, 'input() always returns a string.'),
    # T3
    Q(T3, 'm = 65. With if m >= 70 → "A", elif m >= 50 → "C", else "F", what is printed?', ['C', 'A', 'F', 'Nothing'], 0, 'The first true condition is m >= 50.'),
    Q(T3, 'x = 5. What is x > 3 and x < 10?', ['True', 'False', '5', 'An error'], 0, 'Both comparisons are true.'),
    Q(T3, 'What is not (4 == 4)?', ['False', 'True', '4', 'None'], 0, '4 == 4 is True, and not reverses it.'),
    Q(T3, 'n = 7. What is "even" if n % 2 == 0 else "odd"?', ['odd', 'even', '1', 'True'], 0, '7 % 2 is 1, so the condition is false.'),
    Q(T3, 'Which correctly tests whether x is 1 or 2?', ['x == 1 or x == 2', 'x == 1 or 2', 'x = 1 or x = 2', 'x == (1 or 2)'], 0, 'Each side of or must be a full comparison.'),
    Q(T3, 'In an if / elif / else chain, how many branches run?', ['At most one', 'All that are true', 'Exactly two', 'All of them'], 0, 'The first true branch runs and the rest are skipped.'),
    # T4
    Q(T4, 'What does t = 0; for i in range(1, 5): t += i; print(t) display?', ['10', '15', '4', '6'], 0, '1 + 2 + 3 + 4.'),
    Q(T4, 'What is list(range(2, 10, 3))?', ['[2, 5, 8]', '[2, 5, 8, 11]', '[3, 6, 9]', '[2, 3, 4]'], 0, 'Start 2, step 3, stop before 10.'),
    Q(T4, 'n = 1; while n < 20: n *= 2. What is n after the loop?', ['32', '16', '20', '64'], 0, '1, 2, 4, 8, 16, 32.'),
    Q(T4, 'How many times does "a" appear when counting letters of "banana" in a loop?', ['3', '2', '6', '1'], 0, 'b-a-n-a-n-a.'),
    Q(T4, 'Summing i over range(10) but skipping odd i with continue gives:', ['20', '25', '45', '10'], 0, '0 + 2 + 4 + 6 + 8.'),
    Q(T4, 'Which loop runs forever?', ['n = 5; while n > 0: print(n)', 'for i in range(5): print(i)', 'n = 5; while n > 0: n -= 1', 'for c in "abc": print(c)'], 0, 'n is never changed, so the condition stays true.'),
]

FLASH = [
    ['/ vs // vs %', '7 / 2 = 3.5, 7 // 2 = 3, 7 % 2 = 1.'],
    ['input()', 'Always returns a string; convert with int() or float().'],
    ['String slice s[a:b]', 'From index a up to but not including b.'],
    ['f-string format', 'f"{x:.2f}" shows x to 2 decimal places.'],
    ['elif chain', 'Only the first true branch runs.'],
    ['range(a, b, step)', 'Starts at a, steps by step, stops before b.'],
    ['Accumulator pattern', 'Set total = 0 before the loop; add inside it.'],
    ['break vs continue', 'break exits the loop; continue skips to the next iteration.'],
]
