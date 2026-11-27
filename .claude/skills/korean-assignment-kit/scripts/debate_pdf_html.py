import re,sys,html,markdown
D=sys.argv[1]
MD=sys.argv[2] if len(sys.argv)>2 else 'final2.md'
FACTS=sys.argv[3] if len(sys.argv)>3 else 'brief.md'
md=open(D+'/'+MD,encoding='utf-8').read()
md='\n'.join(('참고: F3의 업무위탁 계약 해지 시점은 2021년 12월로 원문에서 확인했습니다(매일노동뉴스 2026.07.08.).' if l.startswith('참고(V 사실이지만 확인 필요)') else l) for l in md.split('\n'))
brief=open(D+'/'+FACTS,encoding='utf-8').read()
E=html.escape
def inline(t):
    t=E(t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    # F refs -> badges
    def badge(m):
        inner=m.group(1)
        inner=re.sub(r'·S',r'<i class="s">·S</i>',inner)
        return f'<span class="f">{inner}</span>'
    t=re.sub(r'\(((?:F\d+(?:·S)?(?:,\s*)?)+)\)',badge,t)
    return t
secs={}
for m in re.finditer(r'^## (\d)\. (.+?)\n(.*?)(?=^## |\Z)',md,flags=re.M|re.S):
    secs[int(m.group(1))]=(m.group(2),m.group(3).strip())
def paras(txt): return [p.strip() for p in re.split(r'\n\s*\n',txt) if p.strip()]
out=[]
# ---------- cover / cheat sheet ----------
import json,os
cv=json.load(open(D+'/cover.json',encoding='utf-8'))
li=lambda xs:''.join(f'<li>{inline(x)}</li>' for x in xs)
qs=lambda xs:''.join(f'<p>"{E(x.strip(chr(34)))}"</p>' for x in xs)
out.append(f'''<section class="cover"><div class="kicker">토론 준비 자료</div><h1>{E(cv.get("title","토론 자료"))}</h1>
<p class="motion">논제 · {E(cv["motion"])}</p>
<div class="core"><b>이 토론의 진짜 질문</b><br>{inline(cv["core"])}</div>
<div class="two"><div class="col pro"><h3>찬성 한눈에</h3><ol>{li(cv["pro"])}</ol><p class="mini">{inline(cv.get("pro_design",""))}</p></div>
<div class="col con"><h3>반대 한눈에</h3><ol>{li(cv["con"])}</ol><p class="mini">{inline(cv.get("con_alt",""))}</p></div></div>
<div class="two"><div class="col pro light"><h3>찬성의 결정타 질문</h3>{qs(cv["pro_q"])}</div>
<div class="col con light"><h3>반대의 결정타 질문</h3>{qs(cv["con_q"])}</div></div>
<div class="warn"><b>절대 하지 말 것</b> · {inline(cv["dont"])}</div>
<p class="legend"><span class="f">F7</span> = 출처 번호(맨 뒤 부록) &nbsp; <span class="f">F17<i class="s">·S</i></span> = 원문 미확인, 토론 전 확인 필요</p></section>''')
# ---------- section 1 ----------
t,b=secs[1]
h=markdown.markdown(re.sub(r'\n(\d\. |- )',r'\n\n\1',b),extensions=['sane_lists'])
h=re.sub(r'\(((?:F\d+(?:·S)?(?:,\s*)?)+)\)',lambda m:'<span class="f">'+m.group(1).replace('·S','<i class="s">·S</i>')+'</span>',h)
out.append(f'<section><h2><span class="no">1</span>{E(t)}</h2><div class="neutral">{h}</div></section>')
# ---------- 입론 ----------
for n,cls,label in [(2,'pro','찬성'),(3,'con','반대')]:
    t,b=secs[n]; ps=paras(b)
    body=''
    for p in ps:
        p2=inline(p)
        p2=re.sub(r'^(첫째|둘째|셋째|넷째),',r'<b class="ord">\1,</b>',p2)
        body+=f'<p>{p2}</p>'
    out.append(f'<section class="{cls}"><h2><span class="no">{n}</span>{E(t)}</h2><div class="speech {cls}"><div class="tag">{label} 입론 · 읽는 원고</div>{body}</div></section>')
# ---------- 반론 ----------
for n,cls in [(4,'pro'),(5,'con')]:
    t,b=secs[n]; cards=''
    for blk in re.split(r'\n(?=\*\*반론 \d)',b):
        mm=re.match(r'\*\*(반론 \d)\*\*\s*\n(.*)',blk,flags=re.S)
        if not mm: continue
        items=re.findall(r'^- (상대 주장|허점|재반박 근거):\s*(.*)$',mm.group(2),flags=re.M)
        d=dict(items)
        fall=re.match(r'\*\*(.+?)\*\*\s*(.*)',d['허점'])
        fname,frest=(fall.group(1),fall.group(2)) if fall else ('',d['허점'])
        cards+=f'''<div class="card {cls}"><div class="ct">{mm.group(1)} <span class="fall">{E(fname.rstrip('.'))}</span></div>
<div class="row"><div class="lab">상대 주장</div><div class="val">{inline(d["상대 주장"])}</div></div>
<div class="row"><div class="lab">허점</div><div class="val">{inline(frest)}</div></div>
<div class="row"><div class="lab">재반박</div><div class="val">{inline(d["재반박 근거"])}</div></div></div>'''
    out.append(f'<section><h2><span class="no {cls}">{n}</span>{E(t)}</h2>{cards}</section>')
# ---------- 교차조사 ----------
t,b=secs[6]; html6=''
for grp in re.split(r'\n(?=\*\*)',b):
    mm=re.match(r'\*\*(.+?)\*\*\s*\n(.*)',grp,flags=re.S)
    if not mm: continue
    cls='pro' if mm.group(1).startswith('찬성') else 'con'
    qs=re.findall(r'^\d\.\s*질문:\s*(.*?)\n\s*- (.+?) 답변 요령:\s*(.*?)$',mm.group(2),flags=re.M)
    rows=''.join(f'<tr><td class="qn">Q{i+1}</td><td><div class="q">{inline(q)}</div><div class="a"><b>{E(who)} 답:</b> {inline(a)}</div></td></tr>' for i,(q,who,a) in enumerate(qs))
    html6+=f'<h3 class="{cls}">{E(mm.group(1))}</h3><table class="qa {cls}">{rows}</table>'
out.append(f'<section><h2><span class="no">6</span>{E(t)}</h2>{html6}</section>')
# ---------- 약점 ----------
t,b=secs[7]; html7='<div class="two">'
for grp in re.split(r'\n(?=\*\*)',b):
    mm=re.match(r'\*\*(.+?)\*\*\s*\n(.*)',grp,flags=re.S)
    if not mm: continue
    cls='pro' if mm.group(1).startswith('찬성') else 'con'
    items=''
    for it in re.split(r'\n(?=\d\.\s)',mm.group(2).strip()):
        w=re.match(r'\d\.\s*약점:\s*(.*?)\n(.*)',it,flags=re.S)
        if not w: continue
        subs=re.findall(r'^\s*- (방어|주의):\s*(.*)$',w.group(2),flags=re.M)
        items+=f'<div class="weak"><div class="wl">약점</div><p>{inline(w.group(1))}</p>'+''.join(f'<div class="wl {"g" if k=="방어" else "o"}">{k}</div><p>{inline(v)}</p>' for k,v in subs)+'</div>'
    html7+=f'<div class="col {cls}"><h3>{E(mm.group(1))}</h3>{items}</div>'
html7+='</div>'
out.append(f'<section><h2><span class="no">7</span>{E(t)}</h2>{html7}</section>')
# ---------- 8, 9 tables ----------
for n in (8,9):
    t,b=secs[n]
    h=markdown.markdown(b,extensions=['tables'])
    h=re.sub(r'\(((?:F\d+(?:·S)?(?:,\s*)?)+)\)',lambda m:'<span class="f">'+m.group(1).replace('·S','<i class="s">·S</i>')+'</span>',h)
    h=h.replace('<table>','<table class="grid">')
    h=h.replace('<p><strong>찬성 측 허점</strong></p>','<h3 class="pro">찬성 측 허점</h3>').replace('<p><strong>반대 측 허점</strong></p>','<h3 class="con">반대 측 허점</h3>')
    out.append(f'<section><h2><span class="no">{n}</span>{E(t)}</h2>{h}</section>')
# ---------- appendix ----------
facts=brief[brief.index('## 사실 목록')+len('## 사실 목록'):] if '## 사실 목록' in brief else brief
fh=markdown.markdown(re.sub(r'\n(- )',r'\n\n\1',facts))
fh=re.sub(r'(F\d+) \((V|S)\)',lambda m:f'<b>{m.group(1)}</b> <span class="tier {m.group(2)}">{"원문 확인" if m.group(2)=="V" else "미확인"}</span>',fh)
out.append(f'<section class="appx"><h2><span class="no">부록</span>사실 목록</h2>{fh}<p class="mini">{inline(cv.get("appendix_note",""))}</p></section>')
CSS=open(D+'/style.css',encoding='utf-8') if os.path.exists(D+'/style.css') else open(os.path.join(os.path.dirname(__file__),'..','templates','debate_style.css'),encoding='utf-8').read()
open(D+'/'+MD.replace('.md','')+'_pretty.html','w',encoding='utf-8').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>토론 자료</title><style>{CSS}</style></head><body>{"".join(out)}</body></html>')
print('ok', len(out))
