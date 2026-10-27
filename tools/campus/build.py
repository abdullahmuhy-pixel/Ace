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

# Courses on the plan, shown as "coming soon" in the catalogue. Nothing is shown as live until it is written and checked.
CATALOGUE = [
    {'name': 'Calculus I', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng', 'comp', 'biz', 'health']},
    {'name': 'Linear Algebra', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng', 'comp']},
    {'name': 'Probability and Statistics', 'track': 'First-year core', 'status': 'live', 'faculties': ['sci', 'eng', 'comp', 'biz', 'health', 'soc']},
    {'name': 'Programming with Python', 'track': 'First-year core', 'status': 'soon', 'faculties': ['comp', 'eng', 'sci', 'biz']},
    {'name': 'Principles of Microeconomics', 'track': 'First-year core', 'status': 'live', 'faculties': ['biz', 'soc']},
    {'name': 'Principles of Macroeconomics', 'track': 'First-year core', 'status': 'soon', 'faculties': ['biz', 'soc']},
    {'name': 'Financial Accounting I', 'track': 'First-year core', 'status': 'soon', 'faculties': ['biz']},
    {'name': 'General Chemistry', 'track': 'First-year core', 'status': 'soon', 'faculties': ['sci', 'eng', 'health']},
    {'name': 'Physics I: Mechanics', 'track': 'First-year core', 'status': 'soon', 'faculties': ['sci', 'eng']},
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
    'exams': {'First-year core': {'body': 'Ace Campus', 'subjects': {'Calculus I': CALC1, 'Linear Algebra': LA, 'Probability and Statistics': STAT, 'Calculus II': CALC2, 'Principles of Microeconomics': MICRO}}},
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
<h2>Principles of Microeconomics ({nq5} questions)</h2><ul>{rows(MICRO)}</ul></div>
<script type="application/json" id="syllabus-data">{js}</script>
</body>
</html>
'''
open(OUT, 'w', encoding='utf-8').write(page)
for nm, C, n in (('Calculus I', CALC1, nq), ('Linear Algebra', LA, nq2), ('Probability and Statistics', STAT, nq3), ('Calculus II', CALC2, nq4), ('Principles of Microeconomics', MICRO, nq5)):
    print(f'{nm}: {sum(len(m["topics"]) for m in C["modules"])} topics, {n} questions, {len(C["flashcards"])} flashcards')
print('wrote', os.path.relpath(OUT))
