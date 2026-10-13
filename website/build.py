import json,data,os
os.makedirs('dist',exist_ok=True)
D=data.build()
J=json.dumps(D,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
css=open('style.css').read();meta=open('meta.js').read();app=open('app.js').read()
fonts='<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">'
title='<title>Ace Education</title>'
frag=f'{title}\n{fonts}\n<style>\n{css}</style>\n<div id="root"></div>\n<script>const SITE_DATA={J};</script>\n<script>\n{meta}\n</script>\n<script>\n{app}\n</script>\n'
open('dist/index.html','w',encoding='utf-8').write(frag)
full='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="description" content="Exam preparation for secondary schools in 13 countries: notes, quizzes, flashcards and mock exams for WASSCE, NECO, UTME, KCSE, GCSE, A-Level, OSSD, EBAU and more.">\n'+frag.replace('<div id="root">','</head>\n<body>\n<div id="root">',1).replace('<title>Ace Education</title>\n','<title>Ace Education</title>\n',1)+'</body>\n</html>\n'
# standalone needs head to include fonts/style: restructure
full=('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="description" content="Exam preparation for secondary schools in 13 countries: notes, quizzes, flashcards and mock exams for WASSCE, NECO, UTME, KCSE, GCSE, A-Level, OSSD, EBAU and more.">\n'
 f'{title}\n{fonts}\n<style>\n{css}</style>\n</head>\n<body>\n<div id="root"></div>\n<script>const SITE_DATA={J};</script>\n<script>\n{meta}\n</script>\n<script>\n{app}\n</script>\n</body>\n</html>\n')
open('dist/standalone.html','w',encoding='utf-8').write(full)
print(len(frag),len(full))
