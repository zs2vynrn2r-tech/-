import json,sys
from hwpx import HwpxDocument
form,content,out=sys.argv[1:4]
c=json.load(open(content))
cells=[]
if isinstance(c,dict): cells=c.get('cells',[]); c=c['paras']
doc=HwpxDocument.open(form)
# header table
t=doc.tables[0] if doc.tables else None
for r_,c_,txt_ in cells: t.set_cell_text(r_,c_,txt_)
# page: 좌우 25mm, 상하 15mm, 머리말·꼬리말 15mm (1mm = 283.465 HWPUNIT)
mm=lambda v: round(v*283.465)
doc.page.set_margins(left=mm(25),right=mm(25),top=mm(15),bottom=mm(15),header=mm(15),footer=mm(15),section='all')
st=doc.styles
BODY_CHAR='20'; BODY_PARA='1'   # form's 13pt 휴먼명조 / justify 160%
bold13=st.ensure_run(bold=True,size=13,base_char_pr_id_ref=BODY_CHAR)
bold15=st.ensure_run(bold=True,size=15,base_char_pr_id_ref=BODY_CHAR)
center=st.ensure_paragraph_format(base_para_pr_id_ref=BODY_PARA,alignment='CENTER')
left=st.ensure_paragraph_format(base_para_pr_id_ref=BODY_PARA,alignment='LEFT')
indent=st.ensure_paragraph_format(base_para_pr_id_ref=BODY_PARA,margins={'intent':mm(13*0.3528)*1})  # first-line indent ≈ 1 char
in_refs=False
for p in c:
    s,txt=p['style'],p['text']
    if s=='HEADING_1':
        para=doc.add_paragraph(txt,para_pr_id_ref=center,char_pr_id_ref=bold15)
    elif s in('HEADING_2','HEADING_3') or txt in('법령·판례','신문 기사'):
        if txt=='참고문헌': in_refs=True
        para=doc.add_paragraph(txt,para_pr_id_ref=left,char_pr_id_ref=bold13)
    else:
        para=doc.add_paragraph(txt,para_pr_id_ref=(left if in_refs else indent),char_pr_id_ref=BODY_CHAR)
        for off,ft in sorted(p['fns'],key=lambda f:-f[0]):
            doc.notes.add_footnote(ft,paragraph=para,offset=off)
rep=doc.save(out)
print(rep.path, getattr(rep,'editor_open_safety',None))
