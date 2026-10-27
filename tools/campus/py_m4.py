"""Programming with Python, module 4: Files, objects and testing."""
import os
import tempfile
from verify import Q
from py_common import check as c
T1, T2, T3, T4 = ('Reading and writing files', 'Classes and objects', 'Inheritance and polymorphism', 'Testing and debugging')

tmp = os.path.join(tempfile.mkdtemp(), 'notes.txt').replace('\\', '/')
A = [
    c(f'with open("{tmp}", "w") as f:\n    f.write("a\\nb\\nc\\n")\nwith open("{tmp}") as f:\n    print(len(f.readlines()))', '3'),
    c(f'with open("{tmp}", "a") as f:\n    f.write("d\\n")\nwith open("{tmp}") as f:\n    print(f.read().split())', "['a', 'b', 'c', 'd']"),
    c(f'with open("{tmp}") as f:\n    for line in f:\n        print(line.strip(), end="")', 'abcd'),
    c('class Account:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n    def deposit(self, amt):\n        self.balance += amt\na = Account("Ada")\na.deposit(50)\nprint(a.balance)', '50'),
    c('class Dog:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return self.name + " says woof"\nprint(Dog("Rex").speak())', 'Rex says woof'),
    c('class P:\n    def __init__(self, x):\n        self.x = x\na = P(1)\nb = P(1)\nprint(a == b, a.x == b.x)', 'False True'),
    c('class Animal:\n    def speak(self):\n        return "..."\nclass Cat(Animal):\n    def speak(self):\n        return "meow"\nclass Fish(Animal):\n    pass\nprint(Cat().speak(), Fish().speak())', 'meow ...'),
    c('class A:\n    def hi(self):\n        return "A"\nclass B(A):\n    def hi(self):\n        return "B+" + super().hi()\nprint(B().hi())', 'B+A'),
    c('class Shape:\n    def area(self):\n        return 0\nclass Sq(Shape):\n    def __init__(self, s):\n        self.s = s\n    def area(self):\n        return self.s ** 2\nprint(sum(s.area() for s in [Sq(2), Sq(3), Shape()]))', '13'),
    c('print(isinstance(True, int))', 'True'),
    c('def add(a, b):\n    return a + b\nassert add(2, 3) == 5\nprint("ok")', 'ok'),
    c('def avg(a):\n    return sum(a) / len(a)\ntry:\n    avg([])\nexcept ZeroDivisionError:\n    print("empty list")', 'empty list'),
]

MODULE = {
    'title': 'Files, objects and testing',
    'topics': [T1, T2, T3, T4],
    'overview': 'Useful programs keep data after they stop running, model real things clearly, and can be trusted to work. This module covers reading and writing files, object-oriented programming with classes, inheritance, and the testing and debugging habits that professional programmers rely on.',
    'key_terms': ['File mode', 'with statement', 'Class', 'Object', 'Attribute', 'Method', 'self', '__init__', 'Inheritance', 'Polymorphism', 'Unit test', 'assert', 'Debugging'],
    'explanation': [
        'Files let a program store data permanently. Open a file with a mode ("r" read, "w" write, "a" append), preferably inside a with statement, which closes it automatically even if an error occurs.',
        'A class is a blueprint that bundles data (attributes) with behaviour (methods). Each object created from the class has its own attributes. Inheritance lets a new class reuse and extend an existing one, and polymorphism lets different classes respond to the same method call in their own way.',
        'Testing checks that code does what it should, using assert statements or a testing framework such as unittest or pytest. Debugging finds and fixes the cause of wrong behaviour, using error messages, print statements and debuggers to narrow it down.'],
    'quick_facts': [
        'with open(name, "r") as f: closes the file automatically.',
        '"w" overwrites; "a" appends.',
        '__init__ sets up a new object; self refers to the object itself.',
        'class Child(Parent): inherits methods; super() calls the parent version.',
        'assert condition fails loudly if the condition is false.'],
}

NOTES = {
    T1: {
        'overview': 'Files store data between runs of a program. Python reads and writes text files with open(), usually inside a with statement.',
        'key_terms': ['open()', 'Mode', 'read()', 'readlines()', 'write()', 'with statement', 'Path', 'CSV'],
        'explanation': [
            'open(name, "r") opens a file for reading; "w" creates or overwrites it; "a" adds to the end. Writing a file in "w" mode erases what was there, so use "a" to keep existing data.',
            'f.read() returns the whole file as one string, f.readlines() returns a list of lines, and for line in f reads one line at a time, which is best for large files. Each line includes its newline character, so use line.strip() to remove it.',
            'The with statement closes the file automatically at the end of the block, even if an error occurs. For tables of data, the csv module reads each row as a list (or a dictionary with csv.DictReader), handling commas inside quotes correctly.'],
        'formulas_label': 'Syntax',
        'formulas': ['with open("data.txt") as f: text = f.read()', 'with open("out.txt", "w") as f: f.write("line\\n")', 'for line in f: line.strip()', 'import csv; csv.reader(f)'],
        'steps': ['Choose the right mode.', 'Open the file in a with block.', 'Read or write the data.', 'Strip newlines and convert types when reading.', 'Handle FileNotFoundError if the file may be missing.'],
        'worked_example': {
            'problem': 'A file marks.txt holds one mark per line. Write code to print the average mark.',
            'steps': ['with open("marks.txt") as f:', '    marks = [int(line) for line in f if line.strip()]', 'print(sum(marks) / len(marks))'],
            'answer': 'The code reads each non-empty line, converts it to an int and prints the average.',
            'check': 'If the file holds 60, 70 and 80 on three lines, it prints 70.0.'},
        'mistakes': ['Using "w" when you meant to add to a file.', 'Forgetting to close a file (use with).', 'Forgetting that lines read from a file are strings with "\\n" at the end.', 'Assuming the file exists without handling FileNotFoundError.'],
        'real_world': 'School results systems export marks to CSV files that can be opened in a spreadsheet; Python scripts read them to produce reports automatically.',
        'exam_strategy': 'State the mode you choose and why ("a, so existing records are kept"). Mode errors are a favourite exam trap.',
        'recap': ['Modes r, w, a.', 'with closes files automatically.', 'Strip and convert lines.', 'csv for tables.']},
    T2: {
        'overview': 'Object-oriented programming models things as objects that combine data and behaviour. A class defines the structure; each object is an instance with its own data.',
        'key_terms': ['Class', 'Object (instance)', 'Attribute', 'Method', '__init__', 'self', 'Encapsulation'],
        'explanation': [
            'class Account: defines a new type. The special method __init__(self, owner, balance=0) runs when an object is created and sets its attributes: self.owner = owner. self is the object the method is working on.',
            'Methods are functions defined inside the class. a = Account("Ada") creates an object; a.deposit(50) calls a method that changes a.balance. Each object has its own attributes, so two accounts do not share balances.',
            'Encapsulation means keeping an object\'s data behind its methods, so rules (such as "no withdrawal larger than the balance") are enforced in one place. Two different objects with the same attribute values are still separate objects: a == b is False unless the class defines equality.'],
        'formulas_label': 'Syntax',
        'formulas': ['class Name:', '    def __init__(self, a):', '        self.a = a', '    def method(self):', 'obj = Name(value); obj.method()'],
        'steps': ['Identify the thing to model and its data.', 'Write __init__ to set the attributes.', 'Add methods for the behaviour.', 'Create objects and call methods.', 'Keep rules inside the methods.'],
        'worked_example': {
            'problem': 'Create an Account class with deposit and withdraw methods, where withdraw refuses to go below zero.',
            'steps': ['__init__ sets self.owner and self.balance = 0.', 'deposit(amt) adds amt to self.balance.', 'withdraw(amt) checks amt <= self.balance before subtracting, otherwise raises ValueError.'],
            'answer': 'a = Account("Ada"); a.deposit(50) gives a.balance of 50; a.withdraw(80) raises ValueError.',
            'check': 'The rule lives in one method, so every part of the program that withdraws money obeys it.'},
        'mistakes': ['Forgetting self as the first parameter of a method.', 'Writing balance instead of self.balance inside a method.', 'Calling Account.deposit(50) without an object.', 'Thinking two objects with the same data are the same object.'],
        'real_world': 'Banking, school-management and e-commerce systems model customers, students and orders as objects with their own data and rules.',
        'exam_strategy': 'When tracing object code, keep a small table of each object\'s attributes and update it after every method call.',
        'recap': ['Class = blueprint; object = instance.', '__init__ sets attributes.', 'self is the current object.', 'Encapsulate the rules.']},
    T3: {
        'overview': 'Inheritance lets a new class build on an existing one. Polymorphism lets different classes provide their own versions of the same method, so code can treat them uniformly.',
        'key_terms': ['Inheritance', 'Parent (base) class', 'Child (subclass)', 'Method overriding', 'super()', 'Polymorphism', 'isinstance()'],
        'explanation': [
            'class Cat(Animal): creates a subclass that inherits all of Animal\'s methods. It can add new methods or override existing ones by defining a method with the same name. A subclass that overrides nothing (such as class Fish(Animal): pass) simply uses the parent\'s methods.',
            'super() calls the parent class\'s version of a method, which lets the child extend rather than replace the behaviour. It is often used in __init__ so the parent can set up its attributes.',
            'Polymorphism: if Shape, Square and Circle all have an area() method, a loop can call s.area() on a mixed list without checking the type. isinstance(obj, Class) tests whether an object belongs to a class or any subclass of it (even True is an instance of int, because bool inherits from int).'],
        'formulas_label': 'Syntax',
        'formulas': ['class Child(Parent):', 'def method(self): (override)', 'super().method()', 'isinstance(obj, Class)'],
        'steps': ['Put shared behaviour in the parent.', 'Create subclasses for specialised types.', 'Override methods that behave differently.', 'Use super() to extend the parent\'s method.', 'Call methods polymorphically.'],
        'worked_example': {
            'problem': 'Shape has area() returning 0; Sq(s) overrides area() to return s ** 2. What is sum(x.area() for x in [Sq(2), Sq(3), Shape()])?',
            'steps': ['Sq(2).area() = 4.', 'Sq(3).area() = 9.', 'Shape().area() = 0.'],
            'answer': '4 + 9 + 0 = 13.',
            'check': 'Running the code prints 13; each object used its own version of area().'},
        'mistakes': ['Copying code into subclasses instead of inheriting it.', 'Overriding __init__ and forgetting to call super().__init__().', 'Using inheritance for unrelated things ("is-a" should be true).', 'Checking types with if-chains instead of using polymorphism.'],
        'real_world': 'Payment systems define a general Payment class with subclasses for card, bank transfer and mobile money; checkout code calls pay() without needing to know which kind it is.',
        'exam_strategy': 'For "what is printed" questions, find which class each object belongs to and look for the method in that class first, then in its parent.',
        'recap': ['Subclass inherits from parent.', 'Override to change behaviour.', 'super() reuses the parent version.', 'Polymorphism: same call, different behaviour.']},
    T4: {
        'overview': 'Testing shows that code works for chosen cases; debugging finds out why it does not. Both are core professional skills, not optional extras.',
        'key_terms': ['Unit test', 'Test case', 'Edge case', 'assert', 'unittest / pytest', 'Traceback', 'Logic error', 'Debugger', 'Breakpoint'],
        'explanation': [
            'A unit test checks one function with known inputs and expected outputs: assert add(2, 3) == 5. Good tests include normal cases, boundary cases (0, empty lists, the largest value) and invalid inputs. Frameworks such as unittest and pytest run many tests automatically.',
            'Errors come in three kinds: syntax errors (Python cannot read the code), run-time errors (exceptions such as ZeroDivisionError) and logic errors (the code runs but gives the wrong answer). Logic errors are the hardest, because nothing crashes.',
            'To debug, read the traceback from the bottom (the error type and line), reproduce the problem with a small input, and inspect values with print statements or a debugger\'s breakpoints. Change one thing at a time, and add a test for the bug so it cannot quietly return.'],
        'formulas_label': 'Tools',
        'formulas': ['assert condition, "message"', 'Test normal, boundary and invalid inputs', 'Read the traceback from the bottom up', 'Reproduce → isolate → fix → add a test'],
        'steps': ['Write the expected result before running the code.', 'Test normal, boundary and invalid cases.', 'When a test fails, reproduce it with the smallest input.', 'Inspect values to find where they go wrong.', 'Fix, rerun all tests, and keep the new test.'],
        'worked_example': {
            'problem': 'def avg(a): return sum(a) / len(a). Which test case reveals a problem, and how would you fix it?',
            'steps': ['avg([2, 4]) correctly returns 3.0.', 'avg([]) raises ZeroDivisionError, because len([]) is 0.', 'Decide the rule: for example, raise ValueError("empty list") or return 0, and test it.'],
            'answer': 'The empty list is the edge case that breaks the function; handle it explicitly.',
            'check': 'After the fix, both the normal and the edge-case tests pass.'},
        'mistakes': ['Only testing the "happy path".', 'Changing many things at once while debugging.', 'Ignoring the traceback\'s last line.', 'Deleting a failing test instead of fixing the code.'],
        'real_world': 'Software companies run thousands of automated tests on every change before it reaches users; a missed edge case can mean outages or wrong bank balances.',
        'exam_strategy': 'When asked to design tests, give a table with input, expected output and the reason for each case (normal, boundary, invalid).',
        'recap': ['Test normal, boundary and invalid inputs.', 'Syntax, run-time and logic errors.', 'Read tracebacks from the bottom.', 'Reproduce, isolate, fix, test.']},
}

QUESTIONS = [
    # T1
    Q(T1, 'Which mode adds text to the end of an existing file?', ['"a"', '"w"', '"r"', '"x"'], 0, '"w" would overwrite the file.'),
    Q(T1, 'A file holds three lines a, b, c. What is len(f.readlines())?', ['3', '1', '6', '0'], 0, 'One list item per line.'),
    Q(T1, 'Why use with open(...) as f?', ['The file is closed automatically', 'It reads faster', 'It creates a backup', 'It is required to write'], 0, 'Even if an error occurs.'),
    Q(T1, 'Each line read from a text file usually ends with:', ['a newline character', 'a comma', 'a space', 'nothing'], 0, 'Use strip() to remove it.'),
    Q(T1, 'Opening a missing file in "r" mode raises:', ['FileNotFoundError', 'ValueError', 'KeyError', 'TypeError'], 0, 'The file does not exist.'),
    Q(T1, 'Which module reads comma-separated data correctly, including quoted commas?', ['csv', 'math', 'random', 'os'], 0, 'csv handles quoting rules.'),
    # T2
    Q(T2, 'What does __init__ do?', ['Sets up a new object\'s attributes', 'Deletes an object', 'Prints an object', 'Imports a class'], 0, 'It runs when the object is created.'),
    Q(T2, 'Inside a method, self refers to:', ['the object the method was called on', 'the class name', 'the parent class', 'the module'], 0, 'It gives access to the object\'s attributes.'),
    Q(T2, 'a = Account("Ada"); a.deposit(50), with balance starting at 0. What is a.balance?', ['50', '0', '100', 'None'], 0, 'deposit adds to the balance.'),
    Q(T2, 'Dog("Rex").speak() returns self.name + " says woof". What is returned?', ['Rex says woof', 'woof', 'Dog says woof', 'Rex'], 0, 'name is "Rex".'),
    Q(T2, 'a = P(1) and b = P(1) for a simple class P. What is a == b?', ['False', 'True', '1', 'An error'], 0, 'They are different objects unless equality is defined.'),
    Q(T2, 'Encapsulation means:', ['keeping data and the rules that change it together in a class', 'hiding all code', 'using many global variables', 'copying classes'], 0, 'Rules live in the methods.'),
    # T3
    Q(T3, 'Cat overrides speak() to return "meow"; Fish(Animal) defines nothing. What do Cat().speak() and Fish().speak() return if Animal.speak returns "..."?', ['"meow" and "..."', '"meow" and "meow"', '"..." and "..."', 'An error'], 0, 'Fish inherits Animal\'s method.'),
    Q(T3, 'B.hi returns "B+" + super().hi(), and A.hi returns "A". What does B().hi() return?', ['B+A', 'A', 'B', 'A+B'], 0, 'super() calls the parent\'s method.'),
    Q(T3, 'Areas of Sq(2), Sq(3) and Shape() (area 0) add up to:', ['13', '5', '25', '9'], 0, '4 + 9 + 0.'),
    Q(T3, 'What is isinstance(True, int)?', ['True', 'False', 'An error', 'None'], 0, 'bool is a subclass of int.'),
    Q(T3, 'Defining a method in a subclass with the same name as in the parent is called:', ['overriding', 'overloading', 'importing', 'encapsulating'], 0, 'The subclass version is used.'),
    Q(T3, 'Polymorphism lets a program:', ['call the same method on different types of objects', 'run two programs at once', 'avoid classes', 'store many files'], 0, 'Each class responds in its own way.'),
    # T4
    Q(T4, 'assert add(2, 3) == 5 with a correct add function:', ['does nothing and the program continues', 'prints 5', 'raises an error', 'returns True'], 0, 'assert only complains when the condition is false.'),
    Q(T4, 'avg(a) returns sum(a) / len(a). Which input causes an error?', ['[]', '[0]', '[2, 4]', '[-1, 1]'], 0, 'Division by len([]) = 0.'),
    Q(T4, 'Code runs without crashing but gives the wrong answer. This is a:', ['logic error', 'syntax error', 'run-time error', 'compile error'], 0, 'Nothing tells you it is wrong except the result.'),
    Q(T4, 'When reading a traceback, the most useful line is usually:', ['the last line, with the error type and message', 'the first line', 'any import line', 'the line numbers only'], 0, 'Then work up to find where your code called it.'),
    Q(T4, 'Testing with an empty list or zero is testing:', ['an edge (boundary) case', 'the happy path', 'performance', 'style'], 0, 'Edge cases find many bugs.'),
    Q(T4, 'After fixing a bug, good practice is to:', ['add a test that would have caught it', 'delete all tests', 'stop testing', 'rewrite the program'], 0, 'This stops the bug returning.'),
]

FLASH = [
    ['File modes', '"r" read, "w" write (overwrite), "a" append.'],
    ['with open(...)', 'Closes the file automatically.'],
    ['__init__', 'Runs when an object is created; sets attributes.'],
    ['self', 'The object a method is acting on.'],
    ['Inheritance', 'class Child(Parent): reuses and extends Parent.'],
    ['super()', 'Calls the parent class\'s version of a method.'],
    ['Three kinds of error', 'Syntax, run-time (exceptions), logic.'],
    ['Good tests', 'Normal, boundary (edge) and invalid inputs.'],
]
