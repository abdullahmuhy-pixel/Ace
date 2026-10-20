#!/usr/bin/env python3
"""Build the Ace Education website as real, crawlable pages.

  python3 build.py                      (SITE_URL defaults to the GitHub Pages address)
  SITE_URL=https://aceeducation.app/ python3 build.py      (once you own a domain)

Output in dist/ (flat, upload every file to the repo root, no folders):
  index.html, exam-prep-<country>.html x13, features.html, ... , site.css, site.js,
  sitemap.xml, robots.txt, llms.txt, llms-full.txt, og-image.png, 404.html
Every page already contains its full text (so Google, Bing and AI crawlers that do not run JavaScript can read it);
site.js then takes over in the browser for fast navigation.
"""
import json, os, re, sys, threading, http.server, functools, datetime, shutil
import data
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
SITE_URL = os.environ.get('SITE_URL', 'https://abdullahmuhy-pixel.github.io/Ace/')
if not SITE_URL.endswith('/'): SITE_URL += '/'
GSC = os.environ.get('GOOGLE_VERIFY', '')      # Google Search Console "HTML tag" content value
BING = os.environ.get('BING_VERIFY', '')       # Bing Webmaster "msvalidate.01" content value
TODAY = datetime.date.today().isoformat()
OUT = 'dist'; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)

D = data.build()
J = json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
css = open('style.css', encoding='utf-8').read(); meta = open('meta.js', encoding='utf-8').read(); app = open('app.js', encoding='utf-8').read()
fonts = open('_fonts.txt', encoding='utf-8').read().strip()
open(f'{OUT}/site.css', 'w', encoding='utf-8').write(css)
open(f'{OUT}/site.js', 'w', encoding='utf-8').write(f'const SITE_URL={json.dumps(SITE_URL)};\nconst SITE_DATA={J};\n{meta}\n{app}\n')
render_shell = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><link rel="stylesheet" href="site.css"></head><body><div id="root"></div><script src="site.js"></script></body></html>'
open(f'{OUT}/_render.html', 'w', encoding='utf-8').write(render_shell)

# ---------- render every route in a real browser ----------
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=OUT))
threading.Thread(target=srv.serve_forever, daemon=True).start()
PORT = srv.server_address[1]

pages = []     # (filename, route, meta, html)
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1200, 'height': 900})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(f'http://127.0.0.1:{PORT}/_render.html?route='); pg.wait_for_selector('#root header')
    info = pg.evaluate("""() => ({ccs: CCS, slug: SLUG, pages: PAGES, guides: GUIDES.map(g => g[0]), faq: FAQ, CM: CM,
        T: T, tot: TOT, ex: Object.fromEntries(CCS.map(cc => [cc, D[cc].ex.map(e => ({k: e.k, b: e.b, subs: e.s.map(s => s.n)}))]))})""")
    routes = [('index', '')] + [(f'exam-prep-{info["slug"][cc]}', f'exam-prep-{info["slug"][cc]}') for cc in info['ccs']] \
        + [(x, x) for x in info['pages']] + [(f'guide-{g}', f'guide-{g}') for g in info['guides']]
    for fname, route in routes:
        pg.goto(f'http://127.0.0.1:{PORT}/_render.html?route={route}'); pg.wait_for_selector('#root main')
        html = pg.inner_html('#root')
        m = pg.evaluate("() => routeMeta(S.page, S.arg)")
        pages.append((fname, route, m, html))
    # social card
    pg2 = br.new_page(viewport={'width': 1200, 'height': 630})
    pg2.set_content(f"""<body style="margin:0;width:1200px;height:630px;background:#0A6B47;color:#fff;font-family:Segoe UI,Arial,sans-serif;display:flex;flex-direction:column;justify-content:center;padding:0 90px;box-sizing:border-box">
      <div style="display:flex;align-items:center;gap:18px;font-size:44px;font-weight:800"><span style="width:46px;height:46px;border-radius:50%;background:#fff;display:inline-block;position:relative"><span style="position:absolute;inset:13px;border-radius:50%;background:#F3C623"></span></span>Ace Education</div>
      <div style="font-size:74px;font-weight:800;line-height:1.05;margin-top:34px;max-width:980px">Exam prep for the exam you will sit.</div>
      <div style="font-size:32px;margin-top:30px;opacity:.92;max-width:1000px">{info['tot']['exams']} exams · {len(info['ccs'])} countries · {info['tot']['q']:,} practice questions · WASSCE, NECO, JAMB, KCSE, GCSE, A-Level, NSC and more</div></body>""")
    pg2.screenshot(path=f'{OUT}/og-image.png'); br.close()
if errs: print('JS errors:', errs[:3]); sys.exit(1)
os.remove(f'{OUT}/_render.html')

# ---------- write pages ----------
esc = lambda s: str(s).replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')
slug = info['slug']; CM = info['CM']
def hreflangs():
    out = [f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}">']
    for cc in info['ccs']:
        out.append(f'<link rel="alternate" hreflang="{"es-ES" if cc == "ES" else "en-" + cc}" href="{SITE_URL}exam-prep-{slug[cc]}">')
    return '\n'.join(out)
REDIRECT = '<script>try{if(!location.hash&&!location.search&&Object.keys(localStorage).some(function(k){return /^sb-.*-auth-token$/.test(k)}))location.replace("app/")}catch(e){}</script>'
def page_html(fname, route, m, body, noindex=False):
    url = SITE_URL + m['path']
    lang = m.get('lang', 'en').split('-')[0]
    ld = json.dumps({'@context': 'https://schema.org', '@graph': [x for x in m['ld'] if x]}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    alt = hreflangs() if (route.startswith('exam-prep-') or route == '') else ''
    ver = (f'<meta name="google-site-verification" content="{GSC}">' if GSC else '') + (f'<meta name="msvalidate.01" content="{BING}">' if BING else '')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(m['title'])}</title>
<meta name="description" content="{esc(m['description'])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{'noindex' if noindex else 'index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'}">
{alt}
<meta property="og:site_name" content="Ace Education">
<meta property="og:type" content="{m['type']}">
<meta property="og:title" content="{esc(m['title'])}">
<meta property="og:description" content="{esc(m['description'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(m['title'])}">
<meta name="twitter:description" content="{esc(m['description'])}">
<meta name="twitter:image" content="{SITE_URL}og-image.png">
<meta name="theme-color" content="#0A6B47">
<link rel="icon" href="app/icon.svg" type="image/svg+xml">
{ver}
{fonts}
<link rel="stylesheet" href="site.css">
<script type="application/ld+json">{ld}</script>
{REDIRECT if route == '' else ''}
</head>
<body>
<div id="root">{body}</div>
<noscript><p style="padding:1rem">Ace Education works best with JavaScript on. The text on this page is still readable, and the student app is at <a href="app/">app/</a>.</p></noscript>
<script src="site.js" defer></script>
</body>
</html>
'''
for fname, route, m, body in pages:
    open(f'{OUT}/{fname}.html', 'w', encoding='utf-8').write(page_html(fname, route, m, body))
# 404
fm = {'title': 'Page not found | Ace Education', 'description': 'This page does not exist.', 'path': '404', 'type': 'website', 'ld': []}
open(f'{OUT}/404.html', 'w', encoding='utf-8').write(page_html('404', '404', fm, f'<main class="wrap" style="padding:4rem 0;text-align:center"><h1>That page is not here.</h1><p><a href="./">Go to the Ace Education home page</a> or <a href="countries">pick your country</a>.</p></main>', noindex=True))

# ---------- sitemap, robots, llms ----------
prio = lambda r: '1.0' if r == '' else '0.9' if r.startswith('exam-prep-') else '0.7' if r in ('features', 'countries', 'syllabus', 'schools', 'guides') else '0.5'
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for fname, route, m, _ in pages:
    sm.append(f'<url><loc>{SITE_URL}{m["path"]}</loc><lastmod>{TODAY}</lastmod><changefreq>{"weekly" if route in ("", "countries") else "monthly"}</changefreq><priority>{prio(route)}</priority></url>')
sm.append('</urlset>')
open(f'{OUT}/sitemap.xml', 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
bots = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'anthropic-ai', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot-Extended', 'Bingbot', 'Googlebot', 'DuckDuckBot', 'CCBot', 'Amazonbot', 'Meta-ExternalAgent']
robots = 'User-agent: *\nAllow: /\n\n' + '\n'.join(f'User-agent: {b}\nAllow: /\n' for b in bots) + f'\nSitemap: {SITE_URL}sitemap.xml\n'
open(f'{OUT}/robots.txt', 'w').write(robots)

CMs = CM; T = info['T']
lines = ['# Ace Education', '',
 f'> Ace Education is an exam prep and study app for secondary school and university students in {len(info["ccs"])} countries: ' + ', '.join(CMs[cc]['name'] for cc in info['ccs']) + f'. It offers topic notes, quizzes, a question bank, flashcards, timed mock exams, a weak-topic radar and an AI study buddy for {info["tot"]["exams"]} exams, written for each country\'s own exam body, subjects, currency and examples. Students can sign up free; schools and tutoring centres can ask for a plan.', '',
 '## Key pages', f'- [Home]({SITE_URL}): what Ace Education is and who it is for',
 f'- [Countries and exams]({SITE_URL}countries): every country, exam, grading scale and question count',
 f'- [Features]({SITE_URL}features): everything in the student app', f'- [Syllabus explorer]({SITE_URL}syllabus): browse every subject, module and topic',
 f'- [For schools]({SITE_URL}schools): class, teacher and admin tools', f'- [Study guides]({SITE_URL}guides): revision, mock exams and wellbeing',
 f'- [Student app]({SITE_URL}app/): the study app itself', '', '## Exam prep by country']
for cc in info['ccs']:
    ex = info['ex'][cc]
    lines.append(f'- [{CMs[cc]["name"]}: {", ".join(e["k"] for e in ex)}]({SITE_URL}exam-prep-{slug[cc]}): {T[cc]["subs"]} subjects, {T[cc]["q"]:,} practice questions')
lines += ['', '## Guides'] + [f'- [{g}]({SITE_URL}guide-{g})' for g in info['guides']]
open(f'{OUT}/llms.txt', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
full = ['# Ace Education: full reference', '', f'Exam prep and study app. {len(info["ccs"])} countries, {info["tot"]["exams"]} exams, {info["tot"]["q"]:,} practice questions, {info["tot"]["t"]:,} topic notes. Site: {SITE_URL}', '']
for cc in info['ccs']:
    c = CMs[cc]; t = T[cc]
    full += [f'## {c["name"]}', f'URL: {SITE_URL}exam-prep-{slug[cc]}', f'Exams: {c["sys"]}', f'Grading: {c["scale"]}', f'Levels: {c["levels"]}', f'Totals: {t["subs"]} subjects, {t["t"]:,} topics, {t["q"]:,} questions.']
    for e in info['ex'][cc]:
        full.append(f'- {e["k"]} ({e["b"]}): ' + ', '.join(e['subs']))
    full.append('')
full += ['## FAQ'] + [f'**{q}** {a}' for q, a in info['faq']]
open(f'{OUT}/llms-full.txt', 'w', encoding='utf-8').write('\n'.join(full) + '\n')

print('built', len(pages) + 1, 'pages;', sorted(os.listdir(OUT))[:6], '...', sum(os.path.getsize(f'{OUT}/{f}') for f in os.listdir(OUT)) // 1024, 'KB')
