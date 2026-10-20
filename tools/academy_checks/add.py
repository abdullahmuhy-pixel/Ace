#!/usr/bin/env python3
"""Run every executable quick check, then place the checks into the course sources.
usage: python3 tools/academy_checks/add.py [--dry]
Exits 1 if any check's real output differs from its marked answer, or a lesson is missing."""
import json, os, sqlite3, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
SRC = os.path.join(HERE, '..', '..', 'courses', 'src')
from coding import CHECKS

SEED = """
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price INTEGER, stock INTEGER);
INSERT INTO products VALUES (1,'Exercise book','School',350,120),(2,'Pen','School',100,300),(3,'Rice 1kg','Food',1500,40),
 (4,'Phone credit','Services',500,999),(5,'Beans 1kg','Food',1200,25),(6,'Calculator','School',4500,8);
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, city TEXT);
INSERT INTO customers VALUES (1,'Ama','Accra'),(2,'Chidi','Lagos'),(3,'Wanjiru','Nairobi'),(4,'Mwila','Lusaka'),(5,'Fatmata','Freetown');
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, qty INTEGER);
INSERT INTO orders VALUES (1,1,1,4),(2,2,3,2),(3,1,2,10),(4,3,6,1),(5,2,1,3),(6,4,4,2);
"""


def run(lang, code):
    if lang == 'python':
        with tempfile.TemporaryDirectory() as d:
            return subprocess.run([sys.executable, '-I', '-c', code], capture_output=True, text=True, cwd=d, timeout=20).stdout.strip()
    if lang == 'js':
        return subprocess.run(['node', '-e', code], capture_output=True, text=True, timeout=20).stdout.strip()
    if lang == 'sql':
        db = sqlite3.connect(':memory:'); db.executescript(SEED)
        stmts = [s for s in code.split(';') if s.strip()]
        for s in stmts[:-1]: db.execute(s)
        rows = db.execute(stmts[-1]).fetchall()
        return ', '.join(str(r[0]) for r in rows)
    raise ValueError(lang)


bad = []
for slug, lessons in CHECKS.items():
    for lid, cks in lessons.items():
        for ck in cks:
            if '_run' in ck:
                got = run(*ck['_run'])
                if got != ck['o'][ck['a']]: bad.append(f'{slug}/{lid}: "{ck["q"][:40]}" ran to {got!r}, marked {ck["o"][ck["a"]]!r}')
                elif any(o == got for i, o in enumerate(ck['o']) if i != ck['a']): bad.append(f'{slug}/{lid}: two options equal the output')
n = sum(len(c) for l in CHECKS.values() for c in l.values())
ran = sum('_run' in c for l in CHECKS.values() for cs in l.values() for c in cs)
if bad:
    for b in bad: print('PROBLEM', b)
    sys.exit(1)
print(f'{ran} of {n} checks executed and match their marked answer')
if '--dry' in sys.argv: sys.exit(0)

for slug, lessons in CHECKS.items():
    p = os.path.join(SRC, slug + '.json'); c = json.load(open(p, encoding='utf-8'))
    ids = {l['id'] for l in c['lessons']}
    if set(lessons) != ids: print('PROBLEM', slug, 'lessons differ:', ids ^ set(lessons)); sys.exit(1)
    for l in c['lessons']:
        body = [b for b in l['body'] if 'check' not in b]
        c1, c2 = [{k: v for k, v in ck.items() if k != '_run'} for ck in lessons[l['id']]]
        end = len(body) - 1 if 'tip' in body[-1] else len(body)
        body.insert(end, {'check': c2})
        hs = [i for i, b in enumerate(body) if 'h' in b]
        body.insert(hs[-1] if hs else max(1, end // 2), {'check': c1})
        l['body'] = body
    open(p, 'w', encoding='utf-8').write(json.dumps(c, ensure_ascii=False, indent=1))
    print('updated', slug)
