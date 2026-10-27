"""Programming with Python, module 3: Functions, modules and errors."""
from verify import Q
from py_common import check as c
T1, T2, T3, T4 = ('Defining and calling functions', 'Scope, default arguments and recursion', 'Modules and the standard library', 'Errors and exceptions')

A = [
    c('def area(w, h):\n    return w * h\nprint(area(3, 4))', '12'), c('def f(x):\n    x = x + 1\nprint(f(2))', 'None'),
    c('def stats(a):\n    return min(a), max(a)\nlo, hi = stats([4, 9, 1])\nprint(lo, hi)', '1 9'),
    c('def greet(name="friend"):\n    return "Hi " + name\nprint(greet())', 'Hi friend'), c('def power(b, e=2):\n    return b ** e\nprint(power(3), power(2, 5))', '9 32'),
    c('x = 10\ndef f():\n    x = 5\n    return x\nf()\nprint(x)', '10'),
    c('def fact(n):\n    return 1 if n <= 1 else n * fact(n - 1)\nprint(fact(5))', '120'),
    c('def fib(n):\n    return n if n < 2 else fib(n - 1) + fib(n - 2)\nprint(fib(7))', '13'),
    c('import math\nprint(math.sqrt(16))', '4.0'), c('import math\nprint(math.floor(3.7), math.ceil(3.2))', '3 4'),
    c('from statistics import mean\nprint(mean([2, 4, 9]))', '5'), c('import random\nrandom.seed(1)\nx = random.randint(1, 6)\nprint(1 <= x <= 6)', 'True'),
    c('try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print("cannot divide")', 'cannot divide'),
    c('try:\n    n = int("abc")\nexcept ValueError:\n    n = 0\nprint(n)', '0'),
    c('d = {}\ntry:\n    d["x"]\nexcept KeyError:\n    print("missing")\nfinally:\n    print("done")', 'missing\ndone'),
    c('try:\n    x = [1, 2][5]\nexcept IndexError:\n    print("bad index")', 'bad index'),
    c('def check_age(a):\n    if a < 0:\n        raise ValueError("negative")\n    return a\ntry:\n    check_age(-1)\nexcept ValueError as e:\n    print(e)', 'negative'),
]

MODULE = {
    'title': 'Functions, modules and errors',
    'topics': [T1, T2, T3, T4],
    'overview': 'As programs grow, they must be organised. Functions package reusable steps under a name, modules group related functions and give access to Python\'s large standard library, and exception handling keeps programs running sensibly when something goes wrong.',
    'key_terms': ['Function', 'Parameter', 'Argument', 'Return value', 'Scope', 'Default argument', 'Recursion', 'Module', 'import', 'Exception', 'try/except'],
    'explanation': [
        'A function is defined once with def and called many times. Parameters receive the values passed in (arguments), and return sends a result back. Good functions do one job, have clear names and avoid surprising side effects.',
        'Variables created inside a function are local: they exist only during that call and do not affect variables with the same name outside. Recursion, a function calling itself, solves problems that break into smaller copies of themselves, but always needs a base case that stops it.',
        'Modules such as math, random, statistics, datetime and csv provide tested tools you can import instead of writing them yourself. Exceptions such as ValueError and ZeroDivisionError signal problems at run time; try/except lets a program handle them instead of crashing.'],
    'quick_facts': [
        'def name(params): ... return value.',
        'A function without return gives None.',
        'Local variables do not change globals of the same name.',
        'Recursion needs a base case.',
        'try: ... except SomeError: ... finally: ... (finally always runs).'],
}

NOTES = {
    T1: {
        'overview': 'Functions give a name to a block of code so it can be reused, tested and understood on its own.',
        'key_terms': ['def', 'Parameter', 'Argument', 'return', 'None', 'Docstring', 'Multiple return values'],
        'explanation': [
            'def area(w, h): return w * h defines a function with two parameters. Calling area(3, 4) passes the arguments 3 and 4 and gives back 12. A function stops as soon as it reaches return.',
            'If a function has no return statement, it returns None. A common bug is printing inside a function and forgetting to return the value, so the caller receives None. Functions can return several values as a tuple: return min(a), max(a).',
            'A docstring (a string on the first line of the function) explains what the function does. Breaking a program into small functions with clear inputs and outputs makes it easier to test and reuse.'],
        'formulas_label': 'Syntax',
        'formulas': ['def name(param1, param2):', '    """What it does."""', '    return result', 'value = name(arg1, arg2)', 'return a, b → a tuple'],
        'steps': ['Decide the inputs (parameters) and output (return value).', 'Write the def line and docstring.', 'Write the body and return the result.', 'Call it with test values and check the output.'],
        'worked_example': {
            'problem': 'Write a function that returns the average of a list of marks, and use it on [60, 75, 90].',
            'steps': ['def average(marks):', '    return sum(marks) / len(marks)', 'print(average([60, 75, 90]))'],
            'answer': 'It prints 75.0.',
            'check': '(60 + 75 + 90) ÷ 3 = 225 ÷ 3 = 75 ✓.'},
        'mistakes': ['Printing instead of returning a value.', 'Forgetting the brackets when calling: average instead of average(m).', 'Passing arguments in the wrong order.', 'Writing code after return and expecting it to run.'],
        'real_world': 'Payroll software has a function to calculate tax for one employee; calling it for every employee is far safer than repeating the calculation in many places.',
        'exam_strategy': 'When tracing a function call, write the parameter values next to the call, then follow the body. Note whether the function returns a value or None.',
        'recap': ['def, parameters, return.', 'No return means None.', 'Return several values as a tuple.', 'Small, single-purpose functions.']},
    T2: {
        'overview': 'Scope decides where a variable can be seen. Default arguments make parameters optional, and recursion lets a function call itself to solve smaller versions of a problem.',
        'key_terms': ['Local scope', 'Global scope', 'Default argument', 'Keyword argument', 'Recursion', 'Base case', 'Recursive case'],
        'explanation': [
            'Variables assigned inside a function are local. In x = 10; def f(): x = 5, the function\'s x is a separate local variable, so the global x is still 10 after calling f(). Pass values in as arguments and return results rather than relying on globals.',
            'Default arguments give parameters a value if none is passed: def power(b, e=2) makes power(3) return 9 and power(2, 5) return 32. Keyword arguments name the parameter at the call, power(b=2, e=5), which improves readability.',
            'A recursive function calls itself on a smaller input until it reaches a base case. Factorial: fact(n) = n × fact(n − 1), with fact(1) = 1, so fact(5) = 120. Without a base case, recursion never stops and Python raises a RecursionError. Some recursive solutions, such as naive Fibonacci, repeat work and are slow.'],
        'formulas_label': 'Patterns',
        'formulas': ['def f(a, b=default):', 'f(b=1, a=2)  (keyword arguments)', 'def fact(n): return 1 if n <= 1 else n * fact(n - 1)', 'Base case + recursive case'],
        'steps': ['Identify the base case.', 'Express the problem in terms of a smaller version.', 'Make sure every call moves towards the base case.', 'Trace a small example.'],
        'worked_example': {
            'problem': 'Trace fact(4) where fact(n) returns 1 if n <= 1 else n * fact(n - 1).',
            'steps': ['fact(4) = 4 × fact(3); fact(3) = 3 × fact(2); fact(2) = 2 × fact(1).', 'fact(1) = 1 is the base case.', 'Working back: 2 × 1 = 2, 3 × 2 = 6, 4 × 6 = 24.'],
            'answer': 'fact(4) = 24.',
            'check': '4! = 4 × 3 × 2 × 1 = 24 ✓.'},
        'mistakes': ['Expecting a function to change a global variable just by assigning to the same name.', 'Missing the base case.', 'A recursive call that does not get smaller.', 'Using a mutable default such as def f(a=[]), which is shared between calls.'],
        'real_world': 'Recursion is natural for tree-shaped data, such as folders inside folders on a computer or comments with replies to replies.',
        'exam_strategy': 'For recursion, write the chain of calls going down to the base case, then the values coming back up. Examiners often give marks for the trace itself.',
        'recap': ['Local variables stay inside the function.', 'Defaults make parameters optional.', 'Recursion: base case + smaller call.', 'Trace down, then back up.']},
    T3: {
        'overview': 'Modules let you organise your own code and reuse Python\'s standard library, a large collection of tested tools that come with every installation.',
        'key_terms': ['Module', 'import', 'from … import', 'Standard library', 'math', 'random', 'statistics', 'datetime', 'Package'],
        'explanation': [
            'import math gives access to math.sqrt, math.pi, math.floor and more. from statistics import mean imports a single name so you can call mean() directly. Any .py file you write can be imported as a module.',
            'Useful standard modules: math (mathematical functions), random (random numbers for simulations and games), statistics (mean, median, stdev), datetime (dates and times), csv (reading spreadsheet-style files) and os and pathlib (files and folders).',
            'Beyond the standard library, packages such as numpy, pandas and matplotlib are installed with pip and are the foundation of data science in Python. Reusing well-tested modules is faster and safer than writing everything yourself.'],
        'formulas_label': 'Syntax',
        'formulas': ['import math → math.sqrt(16) gives 4.0', 'from statistics import mean', 'import random; random.randint(1, 6)', 'math.floor(3.7) gives 3; math.ceil(3.2) gives 4'],
        'steps': ['Find a module that does what you need.', 'Import it (or the names you need).', 'Call its functions with the module prefix if needed.', 'Read the documentation for parameters and return types.'],
        'worked_example': {
            'problem': 'Simulate rolling a die 6 000 times and estimate the proportion of sixes.',
            'steps': ['import random', 'sixes = sum(1 for _ in range(6000) if random.randint(1, 6) == 6)', 'print(sixes / 6000)'],
            'answer': 'The result is close to 1/6 ≈ 0.167, varying slightly from run to run.',
            'check': 'random.seed(…) makes the run repeatable, which helps when testing.'},
        'mistakes': ['Calling sqrt(16) after import math without the math. prefix.', 'Naming your own file random.py, which hides the real module.', 'Expecting random results to be identical each run without a seed.', 'Forgetting that math.sqrt returns a float.'],
        'real_world': 'Banks and engineers run Monte Carlo simulations with the random module to estimate risk, by repeating a model thousands of times with random inputs.',
        'exam_strategy': 'When a question uses a module function, state what it returns, including the type (math.sqrt(16) returns the float 4.0).',
        'recap': ['import a module, then module.name.', 'from module import name.', 'Know math, random, statistics, datetime, csv.', 'Reuse tested code.']},
    T4: {
        'overview': 'Exceptions are errors that happen while a program runs, such as dividing by zero or converting "abc" to a number. Handling them keeps programs from crashing and lets them respond helpfully.',
        'key_terms': ['Syntax error', 'Exception', 'Traceback', 'try', 'except', 'else', 'finally', 'raise', 'ValueError', 'ZeroDivisionError'],
        'explanation': [
            'Syntax errors (such as a missing colon) stop the program before it runs. Exceptions happen during execution: ZeroDivisionError, ValueError (for example int("abc")), TypeError (adding a string to a number), KeyError (missing dictionary key) and IndexError (index out of range).',
            'Put risky code in a try block and handle specific errors in except blocks. else runs only if no exception occurred, and finally always runs, which is useful for closing files or connections. Catch specific exceptions rather than using a bare except, which can hide real bugs.',
            'Your own code can signal problems with raise ValueError("message"). Validating input and raising clear errors early makes bugs easier to find than letting bad data spread through a program.'],
        'formulas_label': 'Syntax',
        'formulas': ['try:', 'except ValueError:', 'except (KeyError, IndexError) as e:', 'else: (no exception)', 'finally: (always runs)', 'raise ValueError("message")'],
        'steps': ['Identify which lines can fail.', 'Wrap them in try.', 'Catch the specific exceptions and respond.', 'Use finally for clean-up.', 'Raise exceptions for invalid input in your own functions.'],
        'worked_example': {
            'problem': 'Write code that asks for a number and keeps asking until the user enters a valid integer.',
            'steps': ['while True:', '    try: n = int(input("Number: ")); break', '    except ValueError: print("Please enter a whole number.")'],
            'answer': 'The loop repeats on invalid input and stops once int() succeeds.',
            'check': 'Typing "abc" prints the message; typing "42" sets n to 42 and leaves the loop.'},
        'mistakes': ['Using a bare except that hides unrelated bugs.', 'Putting too much code in the try block.', 'Catching the wrong exception type.', 'Confusing syntax errors (cannot be caught at run time) with exceptions.'],
        'real_world': 'Payment apps catch network exceptions so that a dropped connection shows a "try again" message instead of crashing in the middle of a transaction.',
        'exam_strategy': 'Name the exact exception a line would raise and explain why. Questions often ask which except block runs for a given input.',
        'recap': ['Exceptions happen at run time.', 'try / except specific errors.', 'finally always runs.', 'raise errors for bad input.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'def area(w, h): return w * h. What is area(3, 4)?', ['12', '7', 'None', '34'], 0, '3 × 4.'),
    Q(T1, 'def f(x): x = x + 1 (no return). What does print(f(2)) display?', ['None', '3', '2', 'An error'], 0, 'A function without return gives None.'),
    Q(T1, 'def stats(a): return min(a), max(a). After lo, hi = stats([4, 9, 1]), what are lo and hi?', ['1 and 9', '4 and 9', '9 and 1', '1 and 4'], 0, 'The function returns a tuple.'),
    Q(T1, 'In def area(w, h), w and h are called:', ['parameters', 'arguments', 'return values', 'modules'], 0, 'Arguments are the values passed in a call.'),
    Q(T1, 'What happens to code written after a return statement in the same block?', ['It never runs', 'It runs first', 'It runs after the caller', 'It causes an error'], 0, 'return ends the function immediately.'),
    Q(T1, 'Which is the main reason to use functions?', ['To reuse and organise code', 'To make programs run slower', 'To avoid variables', 'To replace loops'], 0, 'Write once, call many times, test separately.'),
    # T2
    Q(T2, 'def greet(name="friend"): return "Hi " + name. What is greet()?', ['Hi friend', 'Hi', 'Hi name', 'An error'], 0, 'The default is used.'),
    Q(T2, 'def power(b, e=2): return b ** e. What are power(3) and power(2, 5)?', ['9 and 32', '6 and 10', '9 and 10', '8 and 32'], 0, '3² and 2⁵.'),
    Q(T2, 'x = 10; def f(): x = 5; return x. After calling f(), what is the global x?', ['10', '5', 'None', 'An error'], 0, 'The function\'s x is local.'),
    Q(T2, 'fact(n) returns 1 if n <= 1 else n * fact(n - 1). What is fact(5)?', ['120', '24', '15', '5'], 0, '5 × 4 × 3 × 2 × 1.'),
    Q(T2, 'fib(n) returns n if n < 2 else fib(n - 1) + fib(n - 2). What is fib(7)?', ['13', '8', '21', '7'], 0, '0, 1, 1, 2, 3, 5, 8, 13.'),
    Q(T2, 'A recursive function with no base case will:', ['raise a RecursionError', 'return None', 'run once', 'return 0'], 0, 'It keeps calling itself until Python stops it.'),
    # T3
    Q(T3, 'import math; print(math.sqrt(16)) displays:', ['4.0', '4', '16', '256'], 0, 'sqrt returns a float.'),
    Q(T3, 'What do math.floor(3.7) and math.ceil(3.2) give?', ['3 and 4', '4 and 3', '3 and 3', '4 and 4'], 0, 'floor rounds down, ceil rounds up.'),
    Q(T3, 'from statistics import mean; mean([2, 4, 9]) is:', ['5', '4', '15', '4.5'], 0, '15 ÷ 3.'),
    Q(T3, 'random.randint(1, 6) returns:', ['a whole number from 1 to 6 inclusive', 'a decimal between 1 and 6', 'a number from 1 to 5', 'always 1'], 0, 'Both ends are included.'),
    Q(T3, 'After import math, calling sqrt(9) on its own gives:', ['a NameError', '3.0', '3', '9'], 0, 'You must write math.sqrt, or import the name directly.'),
    Q(T3, 'Which module would you use to read a spreadsheet saved as comma-separated values?', ['csv', 'math', 'random', 'statistics'], 0, 'csv reads and writes comma-separated files.'),
    # T4
    Q(T4, 'What does try: print(10 / 0) except ZeroDivisionError: print("cannot divide") display?', ['cannot divide', 'inf', '0', 'An error message and a crash'], 0, 'The exception is caught.'),
    Q(T4, 'int("abc") raises:', ['ValueError', 'TypeError', 'KeyError', 'ZeroDivisionError'], 0, 'The text cannot be converted to an integer.'),
    Q(T4, '"5" + 3 raises:', ['TypeError', 'ValueError', 'IndexError', 'SyntaxError'], 0, 'A string and a number cannot be added.'),
    Q(T4, 'A finally block runs:', ['always, whether or not an exception occurred', 'only if an exception occurred', 'only if no exception occurred', 'never'], 0, 'Useful for clean-up.'),
    Q(T4, 'x = [1, 2][5] raises:', ['IndexError', 'KeyError', 'ValueError', 'TypeError'], 0, 'Index 5 does not exist.'),
    Q(T4, 'Why avoid a bare except: block?', ['It can hide unrelated bugs', 'It is slower', 'It is a syntax error', 'It always crashes'], 0, 'Catch the specific exceptions you expect.'),
]

FLASH = [
    ['Function without return', 'Returns None.'],
    ['Multiple return values', 'return a, b gives a tuple; unpack with x, y = f().'],
    ['Local scope', 'Assigning inside a function creates a local variable.'],
    ['Default argument', 'def f(a, b=2): b is optional.'],
    ['Recursion', 'Base case + a call on a smaller input.'],
    ['import vs from … import', 'import math → math.sqrt; from math import sqrt → sqrt.'],
    ['Common exceptions', 'ValueError, TypeError, KeyError, IndexError, ZeroDivisionError.'],
    ['finally', 'Always runs; used for clean-up.'],
]
