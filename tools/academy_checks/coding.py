"""Quick checks for the Ace Academy "Start coding" path.
Two per lesson. The first goes before the lesson's last heading, the second before the closing tip (or at the end).
Any check with run= is executed by tools/academy_checks/add.py, and its output must equal the marked option exactly.
run: 'python' | 'js' | 'sql' (SQLite, loaded with the course's products / customers / orders tables).
runcode: code to execute instead of the code shown (used when the shown code raises on purpose)."""


def C(q, o, a, e, code=None, run=None, runcode=None):
    d = {'q': q, 'o': o, 'a': a, 'e': e}
    if code: d['code'] = code
    if run: d['_run'] = (run, runcode or code)
    return d


CHECKS = {
    'intro-python': {
        'first-program': [
            C('What does this print?', ['1400', '354', 'price * quantity'], 0, 'Python multiplies the values stored in the two variables: 350 × 4 = 1400.',
              'price = 350\nquantity = 4\nprint(price * quantity)', 'python'),
            C('What does this print?', ["<class 'float'>", "<class 'int'>", "<class 'str'>"], 0, 'A number with a decimal point is a float. Whole numbers are int and text is str.',
              'print(type(12.5))', 'python'),
        ],
        'input-and-f-strings': [
            C('input() always gives you text. What does this print?', ['45', '9', 'a + b'], 0, 'Both values are strings, so + joins them. Convert with int() first to add them as numbers.',
              'a = "4"\nb = "5"\nprint(a + b)', 'python'),
            C('What does this print?', ['19.99', '19.98', '19.989'], 0, ':.2f rounds to 2 decimal places, so 19.989 becomes 19.99.',
              'price = 19.989\nprint(f"{price:.2f}")', 'python'),
        ],
        'numbers-and-decisions': [
            C('What does this print?', ['3 2', '3.4 2', '2 3'], 0, '// gives the whole-number part of the division (3) and % gives the remainder (2), because 5 × 3 + 2 = 17.',
              'print(17 // 5, 17 % 5)', 'python'),
            C('What does this print?', ['C', 'B', 'F', 'Nothing'], 0, '55 fails the first two tests, passes score >= 50, so the C branch runs and the rest are skipped.',
              'score = 55\nif score >= 70:\n    print("A")\nelif score >= 60:\n    print("B")\nelif score >= 50:\n    print("C")\nelse:\n    print("F")', 'python'),
        ],
        'loops': [
            C('What does this print?', ['[1, 4, 7]', '[1, 4, 7, 10]', '[3, 6, 9]'], 0, 'range starts at 1, steps by 3 and stops before 10, so 10 is not included.',
              'print(list(range(1, 10, 3)))', 'python'),
            C('What does this print?', ['32', '16', '20'], 0, 'n doubles 1 → 2 → 4 → 8 → 16 → 32. At 32 the condition n < 20 is false, so the loop stops and prints 32.',
              'n = 1\nwhile n < 20:\n    n = n * 2\nprint(n)', 'python'),
        ],
        'lists-and-functions': [
            C('What does this print?', ['4 60', '3 85', '4 72'], 0, 'append adds 60 to the end, so there are 4 items and index -1 is the last one, 60.',
              'scores = [72, 58, 85]\nscores.append(60)\nprint(len(scores), scores[-1])', 'python'),
            C('What does this print?', ['4.5', '4', '5'], 0, 'The function returns 9 / 2. In Python 3, / always gives a float, so the result is 4.5.',
              'def half(x):\n    return x / 2\n\nprint(half(9))', 'python'),
        ],
        'errors-and-project': [
            C('Running this line stops the program. Which error does the last line of the traceback name?', ['TypeError', 'SyntaxError', 'NameError'], 0, 'You cannot join text and a number with +. Use str(5) or an f-string. The kind of error is on the last line of the traceback.',
              'print("Total: " + 5)', 'python', 'try:\n    print("Total: " + 5)\nexcept Exception as e:\n    print(type(e).__name__)'),
            C('Where should you start reading a traceback?', ['At the bottom: the last line names the error', 'At the top: the first line is the error', 'Anywhere: every line says the same thing'], 0, 'Read from the bottom. The last line says what went wrong, and the line above shows where in your code.'),
        ],
    },
    'python-next-steps': {
        'dicts-tuples-sets': [
            C('What does this print?', ['0', 'None', 'KeyError'], 0, 'get returns the default you give it (0) when the key is missing, instead of crashing like prices["yam"] would.',
              'prices = {"rice": 1200, "beans": 900}\nprint(prices.get("yam", 0))', 'python'),
            C('What does this print?', ['3', '4', '2'], 0, 'A set keeps only unique items, so the repeated "a" is stored once: a, b and c.',
              'print(len({"a", "b", "a", "c"}))', 'python'),
        ],
        'strings-fstrings': [
            C('What does this print?', ['7285', '157', '72 85'], 0, 'split gives strings, so + joins "72" and "85". Use int() on each part to add them as numbers.',
              'parts = "Ama,72,85".split(",")\nprint(parts[1] + parts[2])', 'python'),
            C('What does this print?', ['86%', '85.6%', '0.86'], 0, ':.0% multiplies by 100, rounds to 0 decimal places and adds a % sign.',
              'print(f"{0.856:.0%}")', 'python'),
        ],
        'files-csv': [
            C('You want to add a new line to the end of notes.txt without losing what is already there. Which mode do you open it in?', ['"a" (append)', '"w" (write)', '"r" (read)'], 0, '"w" empties the file first, and "r" only reads. "a" adds to the end.'),
            C('csv.DictReader reads a row where the score column holds 72. What is row["score"]?', ['The text "72" (a string)', 'The number 72 (an int)', 'The number 72.0 (a float)'], 0, 'CSV files store text, so every value arrives as a string. Convert with int(row["score"]) before doing maths.',
              None, 'python', 'import csv, io\nrow = next(csv.DictReader(io.StringIO("name,score\\nAma,72\\n")))\nprint(\'The text "72" (a string)\' if isinstance(row["score"], str) else "number")'),
        ],
        'errors-try-except': [
            C('What does this print?', ['bad', 'ok', 'bad and then ok'], 0, 'int("12a") raises ValueError, so the except block runs. The else block only runs when no error happened.',
              'try:\n    n = int("12a")\nexcept ValueError:\n    print("bad")\nelse:\n    print("ok")', 'python'),
            C('Opening a file that does not exist for reading raises which error?', ['FileNotFoundError', 'ValueError', 'KeyError'], 0, 'Catch FileNotFoundError to start fresh when there is no saved data yet.',
              'open("missing.txt")', 'python', 'try:\n    open("/nonexistent-ace/missing.txt")\nexcept Exception as e:\n    print(type(e).__name__)'),
        ],
        'comprehensions': [
            C('What does this print?', ['[72, 91]', '[45, 38]', '[True, False]'], 0, 'The if at the end keeps only the marks that are 50 or more.',
              'print([m for m in [45, 72, 38, 91] if m >= 50])', 'python'),
            C('What does this print?', ["{'Ama': 3, 'Kofi': 4}", "['Ama', 'Kofi']", '{3, 4}'], 0, 'A dictionary comprehension builds key: value pairs, here each name and its length.',
              'print({n: len(n) for n in ["Ama", "Kofi"]})', 'python'),
        ],
        'modules': [
            C('What does this print?', ['5.0', '5', '3'], 0, 'Sorted, the list is 1, 3, 7, 9. With an even count the median is the mean of the middle two: (3 + 7) / 2 = 5.0.',
              'import statistics\nprint(statistics.median([7, 1, 9, 3]))', 'python'),
            C('What does this print?', ['17', '18', '-17'], 0, 'Subtracting two dates gives a timedelta; .days is the number of days between them.',
              'from datetime import date\nprint((date(2026, 12, 18) - date(2026, 12, 1)).days)', 'python'),
        ],
        'project-gradebook': [
            C('Why does the grade book save scores to a CSV file?', ['So the scores are still there the next time the program runs', 'Because Python cannot keep numbers in a dictionary', 'To make the program run faster'], 0, 'Variables vanish when a program ends. A file keeps the data between runs.'),
            C('What does this print?', ['82.7', '82.6', '248'], 0, 'The sum is 248 and there are 3 students. 248 / 3 = 82.67, which rounds to 82.7.',
              'scores = {"Ama": 72, "Kofi": 85, "Zainab": 91}\nprint(round(sum(scores.values()) / len(scores), 1))', 'python'),
        ],
    },
    'html-css-basics': {
        'page-structure': [
            C('Which element goes inside <head> and sets the text on the browser tab rather than on the page?', ['<title>', '<h1>', '<p>'], 0, 'The head holds information about the page. <title> names the tab; <h1> and <p> are visible content in the body.'),
            C('How many <h1> headings should a normal page have?', ['One, for the main heading', 'One for every paragraph', 'As many as possible, for bigger text'], 0, 'Headings describe the outline of the page. Use one <h1>, then <h2> and <h3> for sections. Use CSS, not headings, to change size.'),
        ],
        'text-links-images-lists': [
            C('What is missing from this image?', ['An alt attribute describing the picture', 'An href attribute', 'A closing </img> tag'], 0, 'alt text is read aloud by screen readers and shown if the image fails to load. img has no closing tag, and href belongs on links.',
              '<img src="map.png">'),
            C('Which element makes a numbered list?', ['<ol>', '<ul>', '<li>'], 0, '<ol> is an ordered (numbered) list and <ul> uses bullets. Each item inside either one is an <li>.'),
        ],
        'semantic-html': [
            C('Which element should hold the main menu of links across the site?', ['<nav>', '<footer>', '<aside>'], 0, '<nav> marks the main navigation, so screen readers and search engines can find it.'),
            C('What is the main benefit of semantic elements like <header>, <main> and <article>?', ['They tell browsers, screen readers and search engines what each part of the page is', 'They make the page load colourful styles automatically', 'They are required, or the page will not display'], 0, 'A <div> would look the same, but semantic elements carry meaning that assistive technology and search engines use.'),
        ],
        'css-selectors': [
            C('Which elements does this rule style?', ['Every element with class="price"', 'The one element with id="price"', 'Every <price> tag'], 0, 'A dot selects by class. A # selects by id, and a plain name selects by tag.',
              '.price { color: green; }'),
            C('Both rules target the same paragraphs. What colour is the text?', ['Red', 'Blue', 'A mix of red and blue'], 0, 'When two rules are equally specific, the one that comes later wins. That is the cascade.',
              'p { color: blue; }\np { color: red; }'),
        ],
        'colours-fonts-box-model': [
            C('What colour is #FF0000?', ['Red', 'Green', 'Blue'], 0, 'Hex colours go red, green, blue. FF is the maximum, so this is full red with no green or blue.'),
            C('Without box-sizing: border-box, how wide is the visible box?', ['224px', '200px', '212px'], 0, 'By default width is only the content: 200 + 10 + 10 padding + 2 + 2 border = 224px. With border-box it would be exactly 200px.',
              '.card {\n  width: 200px;\n  padding: 10px;\n  border: 2px solid black;\n}'),
        ],
        'responsive-flexbox': [
            C('What does flex-wrap: wrap do in a flex container?', ['Lets items move onto a new line when they do not fit', 'Wraps each item in a border', 'Stops items from ever moving'], 0, 'Without wrap, flex items squeeze onto one line. With wrap, they flow onto the next line on narrow screens.'),
            C('When do the rules inside this media query apply?', ['When the screen is 600px wide or narrower', 'When the screen is wider than 600px', 'Only when the page is printed'], 0, 'max-width: 600px means "up to 600px", so these rules are for phones and other narrow screens.',
              '@media (max-width: 600px) {\n  .menu { display: none; }\n}'),
        ],
    },
    'javascript-basics': {
        'variables-and-types': [
            C('What happens when this runs?', ['An error, because a const cannot be given a new value', 'rate becomes 0.7', 'rate quietly stays 0.5'], 0, 'const is for values that never change, and reassigning it throws a TypeError. Use let for values that change.',
              'const rate = 0.5;\nrate = 0.7;', 'js', 'const rate = 0.5;\ntry { rate = 0.7; console.log("rate becomes 0.7"); } catch (e) { console.log(e.name === "TypeError" ? "An error, because a const cannot be given a new value" : e.name); }'),
            C('What does this print?', ['string', 'number', 'object'], 0, 'The quotes make "350" text. Without quotes, typeof 350 would be number.',
              'console.log(typeof "350");', 'js'),
        ],
        'operators-and-templates': [
            C('What does this print?', ['53', '8', 'NaN'], 0, 'When one side of + is a string, JavaScript joins instead of adding. "5" - 3 would give 2, because - only works on numbers.',
              'console.log("5" + 3);', 'js'),
            C('What does this print?', ['3 pens cost 150', '${n} pens cost ${n * 50}', '3 pens cost n * 50'], 0, 'Inside backticks, ${…} is replaced by the value of the expression.',
              'const n = 3;\nconsole.log(`${n} pens cost ${n * 50}`);', 'js'),
        ],
        'conditions': [
            C('What does this print?', ['false', 'true', 'undefined'], 0, '=== checks the value and the type. 0 is a number and "0" is a string, so they are not strictly equal.',
              'console.log(0 === "0");', 'js'),
            C('What does this print?', ['no', 'yes', '""'], 0, 'An empty string is falsy, so the condition counts as false and the value after : is used.',
              'const credit = "";\nconsole.log(credit ? "yes" : "no");', 'js'),
        ],
        'loops': [
            C('What does this print?', ['12', '20', '6'], 0, 'i takes the values 2, 4 and 6, and 2 + 4 + 6 = 12.',
              'let s = 0;\nfor (let i = 2; i <= 6; i += 2) {\n  s += i;\n}\nconsole.log(s);', 'js'),
            C('What does this print?', ['1 2 4 5', '1 2 3 4 5', '1 2'], 0, 'continue skips 3 (a multiple of 3), and break stops the loop once i reaches 6.',
              'const out = [];\nfor (let i = 1; i <= 10; i++) {\n  if (i % 3 === 0) continue;\n  if (i > 5) break;\n  out.push(i);\n}\nconsole.log(out.join(" "));', 'js'),
        ],
        'arrays-objects': [
            C('What does this print?', ['72,90', '45,38', '72,90,45,38'], 0, 'filter keeps only the items for which the test is true.',
              'console.log([45, 72, 38, 90].filter(m => m >= 50).join(","));', 'js'),
            C('What does this print?', ['75', '705', 'undefined'], 0, 'Dots reach into nested objects: s.marks.maths is the number 70, and 70 + 5 = 75.',
              'const s = { name: "Kofi", marks: { maths: 70 } };\nconsole.log(s.marks.maths + 5);', 'js'),
        ],
        'functions-and-project': [
            C('What does this print?', ['undefined', '8', '4'], 0, 'The function works out x * 2 but never returns it. A function with no return gives undefined.',
              'function f(x) {\n  x * 2;\n}\nconsole.log(f(4));', 'js'),
            C('What does this print?', ['21', '73', 'n * 3'], 0, 'An arrow function with no braces returns the expression after =>, so triple(7) is 21.',
              'const triple = n => n * 3;\nconsole.log(triple(7));', 'js'),
        ],
    },
    'git-github-basics': {
        'what-is-version-control': [
            C('What is the difference between Git and GitHub?', ['Git is the tool that tracks changes; GitHub is a website that hosts Git repositories', 'They are two names for the same program', 'GitHub tracks changes; Git is only for sharing'], 0, 'Git runs on your computer and works without the internet. GitHub stores repositories online so people can share and collaborate.'),
            C('What is a commit?', ['A saved snapshot of the project with a message saying what changed', 'A copy of the project on another computer', 'A file that lists people working on the project'], 0, 'Each commit is a point in history you can look back at or return to.'),
        ],
        'github-in-the-browser': [
            C('You edited README.md on github.com. What saves the change into the project\'s history?', ['Committing the change with a short message', 'Closing the browser tab', 'Downloading the file'], 0, 'Nothing is recorded until you commit. The message explains what you changed and why.'),
            C('Where on GitHub do you see who changed a file and when?', ['In its history: the list of commits', 'In the repository description', 'In your account settings'], 0, 'Every commit appears in the history with its author, date and message.'),
        ],
        'first-local-repo': [
            C('What does this command do?', ['Moves the current version of notes.txt into the staging area, ready for the next commit', 'Creates a commit straight away', 'Uploads notes.txt to GitHub'], 0, 'git add stages changes. git commit then records everything that is staged.',
              'git add notes.txt'),
            C('What does git log --oneline show?', ['One line per commit: a short id and its message', 'Every line of every file', 'The files that are not yet staged'], 0, 'It is a compact view of the history. git status shows what is staged or changed.'),
        ],
        'branches-and-merging': [
            C('What does this command do?', ['Creates a branch called add-quiz and switches to it', 'Deletes the branch add-quiz', 'Merges add-quiz into main'], 0, '-c means create. Without it, git switch moves to a branch that already exists.',
              'git switch -c add-quiz'),
            C('When does a merge conflict happen?', ['When both branches changed the same lines of the same file', 'Every time you merge', 'When a branch has more than one commit'], 0, 'Git cannot guess which version to keep, so it marks the lines and asks you to choose.'),
        ],
        'pull-requests': [
            C('What is a pull request?', ['A request to merge the changes on one branch into another, with space for review and discussion', 'A way to download a repository', 'A message asking the owner for access'], 0, 'Teams review the changes in the pull request before merging them into main.'),
            C('You want to contribute to a project you cannot push to. What do you do?', ['Fork it, make the change in your copy, then open a pull request', 'Email the owner your whole project', 'Push to their main branch anyway'], 0, 'A fork is your own copy on GitHub. The pull request asks the owners to bring in your change.'),
        ],
        'remotes-readme': [
            C('What does this command do?', ['Brings new commits from GitHub into your local branch', 'Sends your commits to GitHub', 'Deletes your local changes'], 0, 'pull downloads and merges. push is the one that sends your commits up.',
              'git pull'),
            C('Which belongs in a good README?', ['What the project does and how to install or run it', 'Your passwords, so others can log in', 'Every line of the code, copied in'], 0, 'A README is the front page of a repository. Never put secrets in it.'),
        ],
    },
    'sql-basics': {
        'tables-and-select': [
            C('What does this query return from the products table?', ['The name and stock columns for all 6 rows', 'Only the first row', 'Every column, sorted by stock'], 0, 'SELECT picks columns. Without WHERE or LIMIT you get every row.',
              'SELECT name, stock FROM products;'),
            C('Which products column should be stored as TEXT?', ['name', 'price', 'stock'], 0, 'Names are words. Prices and stock counts are numbers, so you can do maths with them.'),
        ],
        'filter-sort': [
            C('Which products does this return?', ['Rice 1kg, Beans 1kg', 'Rice 1kg only', 'Exercise book, Pen'], 0, 'BETWEEN includes both ends: Rice costs 1500 and Beans 1200.',
              "SELECT name FROM products\nWHERE price BETWEEN 1000 AND 1500;", 'sql'),
            C('What does this return?', ['Pen', 'Calculator', 'Exercise book'], 0, 'ORDER BY price sorts from cheapest up, and LIMIT 1 keeps just the first row: Pen at 100.',
              'SELECT name FROM products\nORDER BY price\nLIMIT 1;', 'sql'),
        ],
        'aggregates-group-by': [
            C('What does this return?', ['65', '2', '2700'], 0, 'Only the Food rows count: Rice has 40 in stock and Beans 25.',
              "SELECT SUM(stock) FROM products\nWHERE category = 'Food';", 'sql'),
            C('Which categories does this return?', ['Food, School', 'School', 'Food, School, Services'], 0, 'HAVING filters the groups after counting. Services has only 1 product, so it is dropped.',
              'SELECT category FROM products\nGROUP BY category\nHAVING COUNT(*) >= 2\nORDER BY category;', 'sql'),
        ],
        'joins': [
            C('Who placed order 4?', ['Wanjiru', 'Mwila', 'Ama'], 0, 'Order 4 has customer_id 3, and the join matches it to customer 3, Wanjiru in Nairobi.',
              'SELECT c.name\nFROM orders o\nJOIN customers c ON c.id = o.customer_id\nWHERE o.id = 4;', 'sql'),
            C('How many rows does this return?', ['7', '6', '5'], 0, 'The 6 orders give 6 rows, and LEFT JOIN keeps Fatmata with no orders as one more row.',
              'SELECT COUNT(*)\nFROM customers c\nLEFT JOIN orders o ON o.customer_id = c.id;', 'sql'),
        ],
        'changing-data': [
            C('Exercise book (id 1) starts with 120 in stock. What does the SELECT return?', ['100', '120', '20'], 0, 'UPDATE changes the stored value in place: 120 − 20 = 100.',
              'UPDATE products SET stock = stock - 20 WHERE id = 1;\nSELECT stock FROM products WHERE id = 1;', 'sql'),
            C('Someone forgot the WHERE. How many products now cost 0?', ['6', '1', '0'], 0, 'Without WHERE, UPDATE changes every row in the table. Always run a SELECT with the same WHERE first.',
              'UPDATE products SET price = 0;\nSELECT COUNT(*) FROM products WHERE price = 0;', 'sql'),
        ],
        'designing-tables': [
            C('What does PRIMARY KEY do for the id column?', ['Makes it a unique identifier for each row', 'Makes it the first column shown', 'Encrypts the value'], 0, 'No two rows can share a primary key, so other tables can point to a row by its id.'),
            C('What does NOT NULL on the name column mean?', ['Every row must have a name', 'The name cannot be the word "null"', 'Names must be unique'], 0, 'NOT NULL refuses rows with a missing value. UNIQUE is the rule that stops duplicates.'),
        ],
    },
}
