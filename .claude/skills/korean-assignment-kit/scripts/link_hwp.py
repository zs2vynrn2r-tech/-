import re,sys,copy,inspect
from hwpx import HwpxDocument
src,out_hwp,out_hwpx=sys.argv[1:4]
d=HwpxDocument.open(src)
HP='{http://www.hancom.co.kr/hwpml/2011/paragraph}'
URL=re.compile(r'https?://\S+?(?=\s\(검색일|\s*$)')
link_style={}
def style_for(cp):
    if cp not in link_style:
        link_style[cp]=d.styles.ensure_run(underline=True,color='#0000FF',base_char_pr_id_ref=cp)
    return link_style[cp]
def linkify(para, adder):
    P=para.element
    ts=[t for t in P.iter(HP+'t') if t.text and 'http' in t.text]
    if not ts: return 0
    assert len(ts)==1
    t=ts[0]; m=URL.search(t.text); url=m.group(0)
    run=t.getparent(); assert run.tag==HP+'run'
    assert run is [r for r in P if r.tag==HP+'run'][-1] and t is list(run)[-1], 'url not at end'
    before,after=t.text[:m.start()],t.text[m.end():]
    t.text=before
    cp=run.get('charPrIDRef')
    n_before=len([r for r in P if r.tag==HP+'run'])
    adder(url,url,para)
    runs=[r for r in P if r.tag==HP+'run']
    new=runs[n_before:]
    for r in new:
        if r.find(HP+'t') is not None: r.set('charPrIDRef',style_for(cp))
        else: r.set('charPrIDRef',cp)
    if after:
        nr=copy.deepcopy(run)
        for ch in list(nr): nr.remove(ch)
        tt=copy.deepcopy(t); tt.text=after; nr.append(tt); P.append(nr)
    return 1
cnt=0
fns=d.notes.footnotes() if callable(d.notes.footnotes) else d.notes.footnotes
for n in fns:
    for p in n.paragraphs:
        cnt+=linkify(p, lambda u,txt,p,n=n: n.add_hyperlink(u,txt,paragraph=p) if 'paragraph' in inspect.signature(n.add_hyperlink).parameters else n.add_hyperlink(u,txt))
for p in d.paragraphs:
    if 'http' in p.text: cnt+=linkify(p, lambda u,txt,p: d.refs.add_hyperlink(u,txt,paragraph=p))
print('links',cnt)
d.save(out_hwpx); d.save(out_hwp)
