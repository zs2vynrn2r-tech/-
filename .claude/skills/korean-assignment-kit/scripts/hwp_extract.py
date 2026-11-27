import json,sys
from hwpx import HwpxDocument
HP='{http://www.hancom.co.kr/hwpml/2011/paragraph}'
d=HwpxDocument.open(sys.argv[1])
def walk(P):
    segs=[]; link=None
    for run in P.findall(HP+'run'):
        for ch in run:
            if ch.tag==HP+'t':
                if ch.text: segs.append(['t',ch.text,link])
                for sub in ch:
                    if sub.tag==HP+'lineBreak': segs.append(['br',None,None])
                    if sub.tail: segs.append(['t',sub.tail,link])
            elif ch.tag==HP+'ctrl':
                for c in ch:
                    if c.tag==HP+'fieldBegin' and c.get('type')=='HYPERLINK': link=c.get('name')
                    elif c.tag==HP+'fieldEnd': link=None
                    elif c.tag==HP+'footNote':
                        segs.append(['fn',[s for fp in c.findall('.//'+HP+'p') for s in walk(fp)],None])
    return segs
ps=list(d.paragraphs); st=[i for i,p in enumerate(ps) if p.text.startswith('계약서상')][0]
rows=[[c.text.strip() for c in r.cells] for r in d.tables[0].rows]
conds=[ps[i].text.replace('','❍') for i in range(st) if '' in ps[i].text]
json.dump({'table':rows,'conds':conds,'paras':[walk(p.element) for p in ps[st:]]},open(sys.argv[2],'w'),ensure_ascii=False)
