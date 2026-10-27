#!/usr/bin/env python3
"""Build app/campus-syllabus.html, the Ace Campus course file, from the course sources in tools/campus.
Every maths answer is checked with SymPy before anything is written. Exit code 1 on any problem.
usage: PYTHONPATH=/path/to/sympy:/path/to/mpmath python3 tools/campus/build.py"""
import json, os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import verify
import calc1_m1, calc1_m2, calc1_m3, calc1_m4, calc1_m5
import la_m1, la_m2, la_m3, la_m4, la_m5
import stat_m1, stat_m2, stat_m3, stat_m4, stat_m5
import calc2_m1, calc2_m2, calc2_m3, calc2_m4, calc2_m5
import micro_m1, micro_m2, micro_m3, micro_m4, micro_m5
import macro_m1, macro_m2, macro_m3, macro_m4, macro_m5
import acc_m1, acc_m2, acc_m3, acc_m4, acc_m5
import py_m1, py_m2, py_m3, py_m4, py_m5
import chem_m1, chem_m2, chem_m3, chem_m4, chem_m5
import phys_m1, phys_m2, phys_m3, phys_m4, phys_m5

OUT = os.path.join(HERE, '..', '..', 'app', 'campus-syllabus.html')
problems = []


def course(name, mods, info):
    modules, notes, flash, qs_all = [], {}, [], []
    for m in mods:
        probs = verify.check_questions(m.QUESTIONS, f'{name} / {m.MODULE["title"]}'); problems.extend(probs)
        mod = dict(m.MODULE); mod['explanation'] = '\n\n'.join(mod['explanation']) if isinstance(mod['explanation'], list) else mod['explanation']; mod['questions'] = [verify.strip(q) for q in m.QUESTIONS]
        for t in mod['topics']:
            n = sum(1 for q in m.QUESTIONS if q['topic'] == t)
            if n < 6: problems.append(f'{name}: "{t}" has only {n} questions')
            if t not in m.NOTES: problems.append(f'{name}: "{t}" has no notes')
        for q in m.QUESTIONS:
            if q['topic'] not in mod['topics']: problems.append(f'{name}: question topic {q["topic"]!r} not in module')
            if len(set(o.strip().lower() for o in q['o'])) != 4: problems.append(f'{name}: options in "{q["q"][:50]}"')
        modules.append(mod); notes.update(m.NOTES); flash += m.FLASH; qs_all += m.QUESTIONS
    out = dict(info); out.update({'modules': modules, 'topic_notes': notes, 'flashcards': flash,
                                  'mock_exam': {'questions': 30, 'minutes': 60, 'source': 'Built from this course\'s question bank, in the style of a first-year final.'}})
    return out, len(qs_all)


CALC1, nq = course('Calculus I', [calc1_m1, calc1_m2, calc1_m3, calc1_m4, calc1_m5], {
    'source': 'Written by Ace for first-year university Calculus I. Matches the common core of courses such as MTH 101/102 (Nigeria), MATH 111 (Ghana), MAT1500 (South Africa), MA1001/MATH1001 (UK and Ireland) and Calculus I in North America.',
    'paper_info': 'First-year core • usually 3 to 4 credits • limits, derivatives, applications and integrals',
    'faculties': ['sci', 'eng', 'comp', 'biz', 'health'],
})

LA, nq2 = course('Linear Algebra', [la_m1, la_m2, la_m3, la_m4, la_m5], {
    'source': 'Written by Ace for first-year university Linear Algebra. Matches the common core of courses such as MTH 104/MAT 121 (Nigeria), MATH 122 (Ghana), MAM1000 linear algebra half (South Africa), MATH1002/MA1002 (UK and Ireland) and Linear Algebra in North America.',
    'paper_info': 'First-year core • usually 3 to 4 credits • systems, matrices, determinants, vector spaces and eigenvalues',
    'faculties': ['sci', 'eng', 'comp'],
})

STAT, nq3 = course('Probability and Statistics', [stat_m1, stat_m2, stat_m3, stat_m4, stat_m5], {
    'source': 'Written by Ace for first-year university Probability and Statistics. Matches the common core of courses such as STA 111/112 (Nigeria), STAT 111 (Ghana), STA1000 (South Africa), MA1003/STAT1001 (UK and Ireland) and Introductory Statistics in North America. Every numerical answer was checked in code.',
    'paper_info': 'First-year core • usually 3 to 4 credits • data, probability, distributions, inference and regression',
    'faculties': ['sci', 'eng', 'comp', 'biz', 'health', 'soc'],
})

CALC2, nq4 = course('Calculus II', [calc2_m1, calc2_m2, calc2_m3, calc2_m4, calc2_m5], {
    'source': 'Written by Ace for university Calculus II. Matches the common core of courses such as MTH 201/MAT 201 (Nigeria), MATH 223 (Ghana), MAM1000 second semester (South Africa), MA1002/MATH1002 (UK and Ireland) and Calculus II in North America. Every answer was checked with SymPy.',
    'paper_info': 'First or second year • usually 3 to 4 credits • integration techniques, applications, series, differential equations, parametric and polar curves',
    'faculties': ['sci', 'eng', 'comp'],
})

MICRO, nq5 = course('Principles of Microeconomics', [micro_m1, micro_m2, micro_m3, micro_m4, micro_m5], {
    'source': 'Written by Ace for first-year university Principles of Microeconomics. Matches the common core of courses such as ECO 101 (Nigeria), ECON 101 (Ghana), ECO1010 (South Africa), EC1001/Principles of Economics (UK and Ireland) and Microeconomics 101 in North America. Every numerical answer was checked in code.',
    'paper_info': 'First-year core • usually 3 credits • demand and supply, elasticity, costs, market structures and market failure',
    'faculties': ['biz', 'soc'],
})

MACRO, nq6 = course('Principles of Macroeconomics', [macro_m1, macro_m2, macro_m3, macro_m4, macro_m5], {
    'source': 'Written by Ace for first-year university Principles of Macroeconomics. Matches the common core of courses such as ECO 102 (Nigeria), ECON 102 (Ghana), ECO1020 (South Africa), EC1002/Principles of Economics (UK and Ireland) and Macroeconomics 101 in North America. Every numerical answer was checked in code.',
    'paper_info': 'First-year core • usually 3 credits • GDP, inflation, unemployment, AD–AS, money, fiscal policy, growth and the open economy',
    'faculties': ['biz', 'soc'],
})

ACC, nq7 = course('Financial Accounting I', [acc_m1, acc_m2, acc_m3, acc_m4, acc_m5], {
    'source': 'Written by Ace for first-year university Financial Accounting. Matches the common core of courses such as ACC 101/102 (Nigeria), ACCT 101 (Ghana), ACC1011 (South Africa), AC1001/Financial Accounting (UK and Ireland) and Financial Accounting I in North America, following IFRS terminology. Every figure was checked in code.',
    'paper_info': 'First-year core • usually 3 credits • double entry, adjustments, financial statements, ratios, partnerships and companies',
    'faculties': ['biz'],
})

PY, nq8 = course('Programming with Python', [py_m1, py_m2, py_m3, py_m4, py_m5], {
    'source': 'Written by Ace for first-year university Introduction to Programming in Python. Matches the common core of courses such as CSC 101/102 and CPE 101 (Nigeria), DCIT 101 (Ghana), CSC1015F (South Africa), CS1 programming modules (UK and Ireland) and CS1 in North America. Every "what does this print?" answer was checked by running the code.',
    'paper_info': 'First-year core • usually 3 to 4 credits • Python basics, data structures, functions, files, objects, algorithms and data processing',
    'faculties': ['comp', 'eng', 'sci', 'biz'],
})

CHEM, nq9 = course('General Chemistry', [chem_m1, chem_m2, chem_m3, chem_m4, chem_m5], {
    'source': 'Written by Ace for first-year university General Chemistry. Matches the common core of courses such as CHM 101/102 (Nigeria), CHEM 111 (Ghana), CEM1000 (South Africa), CH1001/General Chemistry (UK and Ireland) and General Chemistry I in North America. Every numerical answer was checked in code using standard atomic weights.',
    'paper_info': 'First-year core • usually 3 to 4 credits • atoms and moles, bonding, gases, thermochemistry, equilibrium, acids, redox and organic basics',
    'faculties': ['sci', 'eng', 'health'],
})

PHYS, nq10 = course('Physics I: Mechanics', [phys_m1, phys_m2, phys_m3, phys_m4, phys_m5], {
    'source': 'Written by Ace for first-year university Physics I (Mechanics). Matches the common core of courses such as PHY 101 (Nigeria), PHY 101/111 (Ghana and Kenya), PHY1004/PHY1012 (South Africa), first-year mechanics in the UK and Ireland, and calculus- or algebra-based Physics I in North America. Uses g = 9.8 m/s²; every numerical answer was checked in code.',
    'paper_info': 'First-year core • usually 3 to 4 credits • kinematics, Newton\'s laws, energy, momentum, rotation, gravitation and oscillations',
    'faculties': ['sci', 'eng'],
})

# Courses on the plan, shown as "coming soon" in the catalogue. Nothing is shown as live until it is written and checked.
CATALOGUE = [
    {'name': 'Calculus I', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng', 'comp', 'biz', 'health']},
    {'name': 'Linear Algebra', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng', 'comp']},
    {'name': 'Probability and Statistics', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng', 'comp', 'biz', 'health', 'soc']},
    {'name': 'Programming with Python', 'track': 'First-year core', 'status': 'live', 'faculties': ['comp', 'eng', 'sci', 'biz']},
    {'name': 'Principles of Microeconomics', 'track': 'First-year core', 'status': 'live', 'faculties': ['biz', 'soc']},
    {'name': 'Principles of Macroeconomics', 'track': 'First-year core', 'status': 'live', 'faculties': ['biz', 'soc']},
    {'name': 'Financial Accounting I', 'track': 'First-year core', 'status': 'live', 'faculties': ['biz']},
    {'name': 'General Chemistry', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng', 'health']},
    {'name': 'Physics I: Mechanics', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng']},
    {'name': 'Cell Biology', 'track': 'First-year core', 'status': 'soon', 'faculties': ['sci', 'health']},
    {'name': 'Academic Writing and Research Methods', 'track': 'First-year core', 'status': 'soon', 'faculties': ['sci', 'eng', 'comp', 'biz', 'health', 'soc', 'law', 'arts', 'edu']},
    {'name': 'Introduction to Psychology', 'track': 'First-year core', 'status': 'soon', 'faculties': ['soc', 'health', 'edu']},
    {'name': 'Calculus II', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng', 'comp']},
    {'name': 'Differential Equations', 'track': 'Second year', 'status': 'soon', 'faculties': ['sci', 'eng']},
    {'name': 'Data Structures and Algorithms', 'track': 'Second year', 'status': 'soon', 'faculties': ['comp', 'eng']},
    {'name': 'Discrete Mathematics and Logic', 'track': 'Second year', 'status': 'soon', 'faculties': ['comp', 'sci']},
    {'name': 'Organic Chemistry', 'track': 'Second year', 'status': 'soon', 'faculties': ['sci', 'health']},
    {'name': 'Electricity and Magnetism', 'track': 'Second year', 'status': 'soon', 'faculties': ['sci', 'eng']},
    {'name': 'Introduction to Data Analysis', 'track': 'Second year', 'status': 'soon', 'faculties': ['sci', 'comp', 'biz', 'soc', 'health']},
    {'name': 'Machine Learning Foundations', 'track': 'Second year', 'status': 'soon', 'faculties': ['comp', 'sci', 'eng']},
]

DATA = {
    'country': 'UN', 'currency': '$', 'schema_version': 3, 'portal': 'campus',
    'schema_note': 'Ace Campus university courses. Same shape as the school syllabus files: exams are tracks, subjects are courses. The app replaces the currency with the student\'s home currency. Built by tools/campus/build.py; edit the sources there, not this file.',
    'settings': {'quiz_questions': 5, 'mock_default': {'questions': 30, 'minutes': 60}},
    'faculties': {'sci': 'Science', 'eng': 'Engineering', 'comp': 'Computing', 'biz': 'Business and economics', 'health': 'Health and medicine', 'soc': 'Social sciences', 'law': 'Law', 'arts': 'Arts and humanities', 'edu': 'Education'},
    'catalogue': CATALOGUE,
    'exams': {'First-year core': {'body': 'Ace Campus', 'subjects': {'Calculus I': CALC1, 'Linear Algebra': LA, 'Probability and Statistics': STAT, 'Calculus II': CALC2, 'Principles of Microeconomics': MICRO, 'Principles of Macroeconomics': MACRO, 'Financial Accounting I': ACC, 'Programming with Python': PY, 'General Chemistry': CHEM, 'Physics I: Mechanics': PHYS}}},
}

if problems:
    for p in problems: print('PROBLEM', p)
    sys.exit(1)

js = json.dumps(DATA, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
live = [c for c in CATALOGUE if c['status'] == 'live']
rows = lambda C: ''.join(f'<li><b>{html.escape(m["title"])}</b>: {html.escape(", ".join(m["topics"]))}</li>' for m in C['modules'])
page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Ace Campus: course data</title>
<style>body{{margin:0;background:#F5F7F4;color:#14231C;font:14px/1.5 system-ui,sans-serif}}.w{{max-width:820px;margin:0 auto;padding:16px}}h1{{font-size:20px}}li{{margin:6px 0}}</style>
</head>
<body>
<div class="w"><h1>Ace Campus course data</h1>
<p>This file feeds the Ace Campus portal. {len(live)} courses live, {len(CATALOGUE) - len(live)} on the plan. Every numerical answer was checked in code (SymPy) when this file was built.</p>
<h2>Calculus I ({nq} questions)</h2><ul>{rows(CALC1)}</ul>
<h2>Linear Algebra ({nq2} questions)</h2><ul>{rows(LA)}</ul>
<h2>Probability and Statistics ({nq3} questions)</h2><ul>{rows(STAT)}</ul>
<h2>Calculus II ({nq4} questions)</h2><ul>{rows(CALC2)}</ul>
<h2>Principles of Microeconomics ({nq5} questions)</h2><ul>{rows(MICRO)}</ul>
<h2>Principles of Macroeconomics ({nq6} questions)</h2><ul>{rows(MACRO)}</ul>
<h2>Financial Accounting I ({nq7} questions)</h2><ul>{rows(ACC)}</ul>
<h2>Programming with Python ({nq8} questions)</h2><ul>{rows(PY)}</ul>
<h2>General Chemistry ({nq9} questions)</h2><ul>{rows(CHEM)}</ul>
<h2>Physics I: Mechanics ({nq10} questions)</h2><ul>{rows(PHYS)}</ul></div>
<script type="application/json" id="syllabus-data">{js}</script>
</body>
</html>
'''
open(OUT, 'w', encoding='utf-8').write(page)
for nm, C, n in (('Calculus I', CALC1, nq), ('Linear Algebra', LA, nq2), ('Probability and Statistics', STAT, nq3), ('Calculus II', CALC2, nq4), ('Principles of Microeconomics', MICRO, nq5), ('Principles of Macroeconomics', MACRO, nq6), ('Financial Accounting I', ACC, nq7), ('Programming with Python', PY, nq8), ('General Chemistry', CHEM, nq9), ('Physics I: Mechanics', PHYS, nq10)):
    print(f'{nm}: {sum(len(m["topics"]) for m in C["modules"])} topics, {n} questions, {len(C["flashcards"])} flashcards')
print('wrote', os.path.relpath(OUT))
