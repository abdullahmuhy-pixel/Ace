#!/usr/bin/env python3
"""Validate app/universities/<CC>.json. Exits 1 on problems. Run: python3 tools/check_unis.py [folder]"""
import json, glob, os, re, sys
folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'app', 'universities')
CC = {'NG','GH','SL','GM','KE','ZM','GB','CA','ES','IE','ZA','UG','TZ','LR','MT','ZW','BW','FR'}
problems = []; n = 0; nu = 0; nc = 0
url = lambda s: isinstance(s, str) and re.fullmatch(r'https://[a-z0-9.-]+\.[a-z]{2,}(/\S*)?', s) is not None
for p in sorted(glob.glob(os.path.join(folder, '??.json'))):
    cc = os.path.basename(p)[:2]; n += 1
    def bad(m): problems.append(f'{cc}: {m}')
    try: d = json.load(open(p, encoding='utf-8'))
    except Exception as e: bad(f'invalid JSON: {e}'); continue
    if cc not in CC or d.get('country') != cc: bad('country must equal the file name and be one of the 10 codes')
    if not re.fullmatch(r'20\d\d-\d\d-\d\d', str(d.get('updated', ''))): bad('updated must be YYYY-MM-DD')
    ao = d.get('admissions_overview') or {}
    if not ao.get('summary') or not url(ao.get('official_url')): bad('admissions_overview needs summary and an official https url')
    us = d.get('universities') or []
    if not (3 <= len(us) <= 12): bad(f'{len(us)} universities (want 3-12)')
    ids = set()
    for u in us:
        i = u.get('id', '?'); nu += 1
        if not re.fullmatch(r'[a-z0-9-]{2,30}', i) or i in ids: bad(f'{i}: bad or duplicate id')
        ids.add(i)
        for k in ('name', 'short', 'type', 'city'):
            if not u.get(k): bad(f'{i}: missing {k}')
        if u.get('type') not in ('public', 'private', 'other'): bad(f'{i}: type must be public, private or other')
        if not url(u.get('url')): bad(f'{i}: url must be an https link')
        if u.get('admissions_url') and not url(u['admissions_url']): bad(f'{i}: admissions_url must be https')
        if not re.fullmatch(r'20\d\d-\d\d-\d\d', str(u.get('verified_on', ''))): bad(f'{i}: verified_on YYYY-MM-DD (date you checked the official site)')
        fs = u.get('faculties') or []
        if len(fs) < 2: bad(f'{i}: at least 2 faculties/schools')
        for f in fs:
            if not f.get('name') or len(f.get('courses') or []) < 2: bad(f'{i}: faculty {f.get("name")} needs 2+ courses')
            for c in f.get('courses') or []:
                nc += 1
                if not c.get('name'): bad(f'{i}: course without name')
                if 'years' in c and not (isinstance(c['years'], int) and 1 <= c['years'] <= 8): bad(f'{i}: {c.get("name")} years 1-8')
                if re.search(r'cut-?off|aggregate|points? of|\bfee', json.dumps(c).lower()) : bad(f'{i}: {c.get("name")} mentions cut-offs or fees; leave those out (they change every year)')
print(f'checked {n} files, {nu} universities, {nc} courses')
if problems: print('\n'.join(problems)); sys.exit(1)
