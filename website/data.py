import json,re
import os
W=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','app')+os.sep
FILES={'NG':'nigeria','GH':'ghana','SL':'sierra-leone','GM':'gambia','KE':'kenya','ZM':'zambia','GB':'uk','CA':'canada','ES':'spain','IE':'ireland','ZA':'south-africa','UG':'uganda','TZ':'tanzania','LR':'liberia','MT':'malta','ZW':'zimbabwe','BW':'botswana','FR':'france'}
def load(cc):
    h=open(W+FILES[cc]+'-syllabus.html',encoding='utf-8').read()
    a=h.index('>',h.index('id="syllabus-data"'))+1;b=h.index('</script>',a)
    return json.loads(h[a:b])
def build():
    out={}
    for cc in FILES:
        d=load(cc);cur=d.get('currency','');sub=lambda s:s.replace('{{CUR}}',cur) if isinstance(s,str) else s
        ex_out=[]
        for ek,e in d['exams'].items():
            subs=[]
            for sk,s in e['subjects'].items():
                src=s
                if 'modules' not in s and s.get('same_as'): src=d['exams'][s['same_as']]['subjects'][sk]
                mods=src.get('modules',[]);tn=src.get('topic_notes',{})
                mods_o=[];mcq=0;notes=0
                for m in mods:
                    qs=list(m.get('questions',[]))
                    cnt={}
                    for q in qs: cnt[q['topic']]=cnt.get(q['topic'],0)+1
                    mcq+=len(qs)
                    tps=[[t,cnt.get(t,0),1 if t in tn else 0] for t in m.get('topics',[])]
                    notes+=sum(x[2] for x in tps)
                    mods_o.append([m['title'],tps])
                mk=src.get('mock_exam') or {}
                subs.append({'n':sk,'p':src.get('paper_info',''),'m':mods_o,'q':mcq,'nt':notes,'t':sum(len(x[1]) for x in mods_o),'fc':len(src.get('flashcards',[])),'mk':[mk.get('questions',0),mk.get('minutes',0)],'sa':bool(s.get('same_as') and 'modules' not in s)})
            ex_out.append({'k':ek,'b':e.get('body',''),'s':subs})
        # sample question + worked example
        sample=None
        e0=next(iter(d['exams'].values()));
        pref=[k for k in e0['subjects'] if re.search('Math|Matem',k)] or list(e0['subjects'])
        s0=e0['subjects'][pref[0]]
        mods=s0.get('modules',[])
        for m in mods[1:]+mods[:1]:
            qs=[q for q in m.get('questions',[]) if q['type']=='mcq']
            if len(qs)>=3:
                q=qs[2];sample={'s':pref[0],'ex':next(iter(d['exams'])),'t':q['topic'],'q':sub(q['q']),'o':[sub(x) for x in q['o']],'a':q['a'],'e':sub(q['e'])};break
        we=None
        tn=s0.get('topic_notes',{})
        for t,n in tn.items():
            w=n.get('worked_example')
            if w and len(w.get('steps',[]))>=2 and len(w['problem'])<160:
                we={'t':t,'p':sub(w['problem']),'s':[sub(x) for x in w['steps']],'a':sub(w['answer']),'c':sub(w.get('check',''))}
                if cc!='ES' or True: break
        qt=qr=nt=nr=0
        for e in d['exams'].values():
            for s_ in e['subjects'].values():
                if 'modules' not in s_: continue
                for m in s_['modules']:
                    for q in m.get('questions',[]): qt+=1;qr+=1 if q.get('reviewed') else 0
                for n in s_.get('topic_notes',{}).values(): nt+=1;nr+=1 if n.get('reviewed') else 0
        out[cc]={'cur':cur,'ex':ex_out,'sample':sample,'we':we,'st':[qt,qr,nt,nr]}
    return out
if __name__=='__main__':
    D=build();j=json.dumps(D,ensure_ascii=False,separators=(',',':'));print(len(j))
    tot=0
    for cc,v in D.items():
        q=sum(s['q'] for e in v['ex'] for s in e['s']);print(cc,[ (e['k'],len(e['s']),sum(s['q'] for s in e['s']),sum(s['t'] for s in e['s']),sum(s['nt'] for s in e['s'])) for e in v['ex']],bool(v['sample']),bool(v['we']));tot+=q
    print(tot)
