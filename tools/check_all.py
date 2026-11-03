#!/usr/bin/env python3
"""Validates every syllabus file. Exit code 1 if anything is wrong, so CI blocks a bad edit.
usage: python3 tools/check_all.py [folder-with-*-syllabus.html]   (default: app/)"""
import json, sys, glob, os, re
folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'app')
problems = []; totals = {'files': 0, 'questions': 0, 'topics': 0}
NOTE_KEYS = ['overview', 'key_terms', 'explanation', 'formulas_label', 'formulas', 'steps', 'worked_example', 'mistakes', 'real_world', 'exam_strategy', 'recap']
for path in sorted(glob.glob(os.path.join(folder, '*-syllabus.html'))):
    name = os.path.basename(path); h = open(path, encoding='utf-8').read()
    try:
        a = h.index('>', h.index('id="syllabus-data"')) + 1; b = h.index('</script>', a); D = json.loads(h[a:b])
    except Exception as e:
        problems.append(f'{name}: cannot read syllabus-data ({e})'); continue
    totals['files'] += 1
    for k in ('country', 'currency', 'exams'):
        if k not in D: problems.append(f'{name}: missing "{k}"')
    for ek, ex in D.get('exams', {}).items():
        for sk, s in ex.get('subjects', {}).items():
            where = f'{name} / {ek} / {sk}'
            if s.get('same_as'):
                if s['same_as'] not in D['exams'] or sk not in D['exams'][s['same_as']]['subjects']: problems.append(f'{where}: same_as target missing')
                continue
            mods = s.get('modules')
            if not mods: problems.append(f'{where}: no modules'); continue
            notes = s.get('topic_notes', {})
            for m in mods:
                for t in m.get('topics', []):
                    totals['topics'] += 1
                    n = notes.get(t)
                    qn = [q for q in m.get('questions', []) if q.get('topic') == t]
                    if not n: problems.append(f'{where}: topic "{t}" has no notes')
                    else:
                        for k in NOTE_KEYS:
                            if not n.get(k): problems.append(f'{where}: "{t}" notes missing {k}')
                    if len(qn) < 5: problems.append(f'{where}: topic "{t}" has only {len(qn)} questions')
                for q in m.get('questions', []):
                    totals['questions'] += 1
                    if q.get('topic') not in m.get('topics', []): problems.append(f'{where}: question topic "{q.get("topic")}" is not in module "{m["title"]}"')
                    if q.get('type') == 'mcq':
                        o = q.get('o', [])
                        if len(o) != 4: problems.append(f'{where}: "{q["q"][:50]}" has {len(o)} options')
                        elif len({x.strip().lower() for x in o}) != 4: problems.append(f'{where}: duplicate options in "{q["q"][:50]}"')
                        if not isinstance(q.get('a'), int) or not 0 <= q.get('a', -1) < len(o): problems.append(f'{where}: bad answer index in "{q["q"][:50]}"')
                        if not q.get('e'): problems.append(f'{where}: no explanation for "{q["q"][:50]}"')
                        # a template slip shows up as an option that is literally "undefined"/"NaN", or an unfilled {{...}}; the word "undefined" in maths prose is fine
                        if not re.search(r'Java|int\[|undefined|cot|sec|\b5\.0 / 0|Animal', q['q']) and any(re.fullmatch(r'\s*(undefined|NaN)\s*', str(x)) for x in o) or not re.search(r'Java|int\[|Animal|pd\.|pandas', q['q']) and any(re.search(r'\bNaN\b|\{\{(?!CUR)|\$\{', str(x)) for x in [q['q'], *o, q.get('e', '')]): problems.append(f'{where}: placeholder text in "{q["q"][:50]}"')
            mk = s.get('mock_exam') or {}
            if not mk.get('questions') or not mk.get('minutes'): problems.append(f'{where}: mock_exam incomplete')
print(f"checked {totals['files']} files, {totals['topics']} topics, {totals['questions']} questions")
for p in problems[:80]: print('PROBLEM', p)
if len(problems) > 80: print(f'... and {len(problems) - 80} more')
sys.exit(1 if problems else 0)
