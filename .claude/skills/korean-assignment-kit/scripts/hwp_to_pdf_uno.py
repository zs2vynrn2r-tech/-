import json,sys,time,uno
from com.sun.star.beans import PropertyValue
from com.sun.star.text.ControlCharacter import PARAGRAPH_BREAK, LINE_BREAK
data=json.load(open(sys.argv[1])); out=sys.argv[2]
ctx=uno.getComponentContext()
res=ctx.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',ctx)
for _ in range(60):
    try: c=res.resolve('uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext'); break
    except Exception: time.sleep(1)
desk=c.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',c)
def P(n,v): p=PropertyValue(); p.Name=n; p.Value=v; return p
doc=desk.loadComponentFromURL('private:factory/swriter','_blank',0,(P('Hidden',True),))
FONT='NanumMyeongjo'
ps=doc.StyleFamilies.getByName('PageStyles').getByName('Standard')
ps.Width,ps.Height=21000,29700
ps.LeftMargin=ps.RightMargin=2500; ps.TopMargin=ps.BottomMargin=1500
std=doc.StyleFamilies.getByName('ParagraphStyles').getByName('Standard')
for k,v in [('CharFontName',FONT),('CharFontNameAsian',FONT),('CharHeight',13),('CharHeightAsian',13)]: std.setPropertyValue(k,v)
ls=uno.createUnoStruct('com.sun.star.style.LineSpacing'); ls.Mode=0; ls.Height=160
std.ParaLineSpacing=ls
fs=doc.StyleFamilies.getByName('ParagraphStyles').getByName('Footnote')
for k,v in [('CharFontName',FONT),('CharFontNameAsian',FONT),('CharHeight',9),('CharHeightAsian',9)]: fs.setPropertyValue(k,v)
ls2=uno.createUnoStruct('com.sun.star.style.LineSpacing'); ls2.Mode=0; ls2.Height=120; fs.ParaLineSpacing=ls2
text=doc.Text; cur=text.createTextCursor()
from com.sun.star.style.ParagraphAdjust import LEFT,CENTER,BLOCK
def para(adjust=BLOCK,size=13,bold=False,indent=0):
    cur.ParaAdjust=adjust; cur.CharHeight=size; cur.CharHeightAsian=size
    cur.CharWeight=150 if bold else 100; cur.CharWeightAsian=150 if bold else 100
    cur.ParaFirstLineIndent=indent
    cur.HyperLinkURL=''; cur.CharColor=0x000000; cur.CharUnderline=0
def put(t,url=None,target=None):
    tx=target or text; c=cur if target is None else target
    start=c.getEnd()
    tx.insertString(c,t,False)
    if url:
        r=tx.createTextCursorByRange(start); r.goRight(len(t),True)
        r.HyperLinkURL=url; r.HyperLinkTarget='_blank'
        r.CharColor=0x0000FF; r.CharUnderline=1
    if target is None:
        cur.HyperLinkURL=''; cur.HyperLinkTarget=''; cur.CharColor=0x000000; cur.CharUnderline=0
def brk(): text.insertControlCharacter(cur,PARAGRAPH_BREAK,False)
# header
para(LEFT,11,True); put('[붙임3]'); brk()
para(CENTER,20,True); put('2026학년도 2학기 글쓰기 튜터링 실시 자료'); brk()
para(LEFT,13)
tb=doc.createInstance('com.sun.star.text.TextTable'); tb.initialize(2,4)
text.insertTextContent(cur,tb,False)
seps=tb.TableColumnSeparators; tot=45067; acc=0; w=[8904,15607,6831,13725]
for i in range(3): acc+=w[i]; seps[i].Position=int(acc/tot*10000)
tb.TableColumnSeparators=seps
tr=data['table']
cells={'A1':tr[0][0],'B1':tr[0][1],'A2':tr[1][0],'B2':tr[1][1],'C2':tr[1][2],'D2':tr[1][3]}
tc=tb.createCursorByCellName('B1'); tc.goRight(2,True); tc.mergeRange()
for k,v in cells.items():
    cell=tb.getCellByName(k); cell.setString(v)
    cc=cell.createTextCursor(); cc.gotoEnd(True); cc.CharHeight=12; cc.CharHeightAsian=12; cc.ParaAdjust=CENTER
    if k in('A1','A2','C2'): cell.BackColor=0xE7E6E6; cc.CharWeight=150; cc.CharWeightAsian=150
para(LEFT,13)
for cnd in data['conds']: put(cnd); brk()
brk()
import re
def is_head(t):
    return bool(re.match(r'^(I|II|III)\. |^\d\. |^참고문헌$|^법령·판례$|^신문 기사$',t))
first=True; in_refs=False
for segs in data['paras']:
    plain=''.join(s[1] for s in segs if s[0]=='t').strip()
    if first: para(CENTER,15,True); first=False
    elif is_head(plain):
        para(LEFT,13,True)
        if plain.endswith('참고문헌'): in_refs=True
    elif in_refs and plain.startswith(('근로기준법.','산업안전보건법.','대법원','서울고등법원','스페인','Directive','Uber','경향신문,','곽용희','나주예','어고은','이동희','이지민','임온유')): para(LEFT,13,False)
    else: para(BLOCK,13,False,460)
    for kind,val,url in segs:
        if kind=='t': put(val,url)
        elif kind=='br': text.insertControlCharacter(cur,LINE_BREAK,False)
        elif kind=='fn':
            fn=doc.createInstance('com.sun.star.text.Footnote')
            text.insertTextContent(cur,fn,False)
            fc=fn.Text.createTextCursor(); fc.gotoEnd(False)
            for k2,v2,u2 in val:
                if k2=='t':
                    st=fc.getEnd(); fn.Text.insertString(fc,v2,False)
                    if u2:
                        r=fn.Text.createTextCursorByRange(st); r.goRight(len(v2),True)
                        r.HyperLinkURL=u2; r.HyperLinkTarget='_blank'; r.CharColor=0x0000FF; r.CharUnderline=1
                        fc.HyperLinkURL=''; fc.CharColor=0x000000; fc.CharUnderline=0
    brk()
doc.storeToURL(uno.systemPathToFileUrl(out),(P('FilterName','writer_pdf_Export'),))
doc.storeToURL(uno.systemPathToFileUrl(out[:-4]+'.odt'),())
doc.close(True)
print('ok')
