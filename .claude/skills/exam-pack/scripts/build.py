#!/usr/bin/env python3
"""Render guide.json / mock.json into print HTML matching the sample styles."""
import json, re, sys, html

GREEN = "#1d6b4e"

BASE_CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; background:#fff; color:#151515;
  font-family: 'Noto Sans CJK KR','Noto Sans KR',sans-serif; font-size: 9.6pt; line-height:1.62;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width:210mm; height:297mm; position:relative; padding:20mm 18mm 22mm 18mm; overflow:hidden; page-break-after: always; }
.foot { position:absolute; left:18mm; right:18mm; bottom:11mm; display:flex; justify-content:space-between;
  font-size:8pt; color:#9a9a9a; }
.foot .r { color:#555; }
.g { color: GREEN; }
b, strong { font-weight:700; }
.cover .kicker { font-size:9pt; color:#666; margin-top:62mm; }
.cover h1 { font-size:34pt; line-height:1.15; margin:3mm 0 0; font-weight:900; letter-spacing:-0.5pt; }
.cover h1 .t2 { display:block; color:GREEN; font-weight:400; }
.cover .term { font-size:9pt; color:#555; margin-top:7mm; }
.cover .info { position:absolute; left:18mm; right:18mm; bottom:34mm; }
.cover .info div { display:flex; font-size:9pt; margin:3.2mm 0; }
.cover .info span:first-child { width:22mm; color:GREEN; font-weight:700; }
"""

GUIDE_CSS = """
.toc h2 { font-size:17pt; font-weight:400; margin:0 0 10mm; }
.toc .u { display:flex; margin-bottom:7mm; }
.toc .u .n { width:16mm; font-size:24pt; color:GREEN; font-weight:300; line-height:1; }
.toc .u h3 { margin:0 0 2mm; font-size:11pt; }
.toc .u .s { font-size:8.6pt; margin:1mm 0; }
.toc .u .s span { display:inline-block; width:12mm; color:GREEN; font-weight:700; }
.unit .lab { font-size:8.5pt; color:#666; margin-top:28mm; }
.unit .big { font-size:72pt; color:GREEN; font-weight:300; line-height:1; margin:4mm 0 6mm; }
.unit h2 { font-size:20pt; margin:0; }
.unit .pg { font-size:8.5pt; color:#666; margin:2mm 0 12mm; }
.unit table { width:100%; border-collapse:collapse; }
.unit td { border-top:1px solid #ccc; padding:4mm 0; vertical-align:top; font-size:8.8pt; }
.unit tr:last-child td { border-bottom:1px solid #ccc; }
.unit td.id { width:14mm; color:GREEN; font-weight:700; }
.unit td.t { width:52mm; font-weight:700; }
.unit .cnt { font-size:8.3pt; color:#555; margin-top:4mm; }
.sec h2 { font-size:15pt; margin:0 0 4mm; padding-bottom:3mm; border-bottom:1.2px solid #222; }
.sec h2 .id { color:GREEN; font-weight:300; margin-right:3mm; }
.cap { font-size:7.8pt; color:#777; margin:5mm 0 2mm; }
.frame div, .list div { display:flex; }
.frame div { margin:2.2mm 0; }
.frame .k { width:24mm; flex:none; color:GREEN; font-weight:700; }
.list { border-left:0; }
.list div { margin:0; }
.list .k { width:22mm; flex:none; color:GREEN; font-weight:700; padding:2.2mm 0; font-size:8.8pt; }
.list .k.hand { color:#b3471d; }
.list .v { flex:1; border-left:1px solid #ccc; padding:2.2mm 0 2.2mm 5mm; }
.list .v.hand { background:#fbf4ec; }
table.q { width:100%; border-collapse:collapse; margin-bottom:2mm; }
table.q th { background:#f1f1f1; font-weight:400; font-size:8pt; color:#444; text-align:left; padding:2.2mm 2mm; border-top:1.2px solid #222; }
table.q td { border-bottom:1px solid #ddd; padding:2.4mm 2mm; vertical-align:top; font-size:9pt; }
table.q td.no { width:10mm; font-weight:700; }
table.q td.d { width:13mm; white-space:nowrap; }
table.q td.L { width:20mm; color:GREEN; text-align:center; font-size:8.3pt; }
table.q td.ans { width:26mm; }
table.q td.ox { width:14mm; text-align:center; color:#555; letter-spacing:2mm; }
table.q th.c { text-align:center; }
.dot { display:inline-block; width:2.1mm; height:2.1mm; border-radius:50%; background:#d4d4d4; margin-right:0.6mm; }
.dot.on { background:GREEN; }
.case { margin:3mm 0 7mm; break-inside:avoid; }
.case .h { font-weight:700; margin-bottom:1.5mm; }
.case .h .L { color:GREEN; font-weight:400; font-size:8.3pt; margin-left:2mm; }
.case .opt { margin:1mm 0 0 4mm; }
.case .blank { height:16mm; }
table.a { width:100%; border-collapse:collapse; }
table.a th { background:#f1f1f1; font-weight:400; font-size:8pt; color:#444; text-align:left; padding:2.2mm 2mm; border-top:1.2px solid #222; }
table.a td { border-bottom:1px solid #ddd; padding:2.4mm 2mm; vertical-align:top; font-size:8.8pt; }
table.a td.no { width:10mm; font-weight:700; }
table.a td.an { width:30mm; font-weight:700; }
table.a td.L { width:18mm; color:GREEN; text-align:center; font-size:8.2pt; }
h3.ans { font-size:15pt; margin:0 0 2mm; }
figure.dg { margin:3mm 0 1mm; padding:3mm; background:#fff; border:1px solid #e3e3e3; border-radius:2mm; break-inside:avoid; }
figure.dg figcaption { font-size:8pt; color:#555; margin-top:1.5mm; }
.case .box { border:1px solid #ccc; border-radius:1.5mm; padding:2mm 3mm; margin:1.5mm 0; background:#fafafa; }
"""

MOCK_CSS = """
.mh { font-size:17pt; font-weight:700; padding-bottom:4mm; border-bottom:1.2px solid #222; margin-bottom:7mm; }
.mh .id { color:GREEN; font-weight:300; font-size:20pt; margin-right:3mm; }
.qq { margin-bottom:8mm; break-inside:avoid; }
.qq .n { font-weight:700; font-size:11pt; }
.qq .u { color:GREEN; font-size:7.5pt; margin-left:2mm; }
.qq .st { font-family:'Noto Serif CJK KR',serif; margin:2.5mm 0 1.5mm; font-size:9.6pt; }
.qq .ox { color:#555; margin-left:5mm; letter-spacing:5mm; font-size:9pt; }
.qq .opt { margin:1.2mm 0 0 4mm; font-size:9.2pt; }
table.a { width:100%; border-collapse:collapse; }
table.a th { background:#f1f1f1; font-weight:400; font-size:8pt; color:#444; text-align:left; padding:2.4mm 2mm; border-top:1.2px solid #222; }
table.a td { border-bottom:1px solid #ddd; padding:3mm 2mm; vertical-align:middle; font-family:'Noto Serif CJK KR',serif; font-size:9pt; }
table.a td.no { width:12mm; font-weight:700; font-family:'Noto Sans CJK KR'; }
table.a td.an { width:12mm; color:GREEN; font-weight:700; text-align:center; font-family:'Noto Sans CJK KR'; }
table.a td.u { width:16mm; color:GREEN; font-size:8pt; text-align:center; font-family:'Noto Sans CJK KR'; }
h3.ans { font-size:17pt; margin:0 0 2mm; }
.qq .box { border:1px solid #bbb; border-radius:1.5mm; padding:2.5mm 3.5mm; margin:1.5mm 0 2mm; font-family:'Noto Serif CJK KR',serif; font-size:9.2pt; }
.sub { font-size:8pt; color:#777; margin-bottom:7mm; }
"""

def md(s):
    s = html.escape(str(s))
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s.replace("\n", "<br>")

TONES = {  # fill, stroke, text
    "main": ("#e6f1ec", GREEN, "#123d2d"),
    "accent": ("#fbefe6", "#b3471d", "#6b2a10"),
    "muted": ("#f3f3f3", "#9a9a9a", "#333"),
    "plain": ("#ffffff", "#333333", "#151515"),
}

def _clip(n, tx, ty):
    """point on border of node n toward (tx,ty)"""
    cx, cy = n["x"] + n["w"] / 2, n["y"] + n["h"] / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (n["w"] / 2) / abs(dx) if dx else 1e9
    sy = (n["h"] / 2) / abs(dy) if dy else 1e9
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s

def _wrap(text, maxch):
    out, cur = [], ""
    for ch in str(text):
        if ch == "\n":
            out.append(cur); cur = ""; continue
        cur += ch
        if len(cur) >= maxch and ch == " ":
            out.append(cur.strip()); cur = ""
        elif len(cur) >= maxch + 4:
            out.append(cur); cur = ""
    if cur.strip():
        out.append(cur.strip())
    return out

def diagram(d):
    """Render diagram DSL to inline SVG figure."""
    if d.get("svg"):
        svg = d["svg"]
    else:
        W, H = d.get("w", 640), d.get("h", 240)
        nodes = {n["id"]: n for n in d.get("nodes", [])}
        p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(d.get("caption",""))}" style="width:100%;max-width:{W*0.265:.0f}mm;height:auto;font-family:Noto Sans CJK KR,sans-serif">']
        p.append(f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#333"/></marker>'
                 f'<marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{GREEN}"/></marker>'
                 f'<marker id="aha" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#b3471d"/></marker></defs>')
        for gp in d.get("groups", []):
            p.append(f'<rect x="{gp["x"]}" y="{gp["y"]}" width="{gp["w"]}" height="{gp["h"]}" rx="8" fill="{gp.get("fill","none")}" stroke="#9a9a9a" stroke-dasharray="5 4"/>')
            p.append(f'<text x="{gp["x"]+8}" y="{gp["y"]+15}" font-size="11" fill="#666">{html.escape(gp.get("label",""))}</text>')
        for e in d.get("edges", []):
            a, b = nodes[e["from"]], nodes[e["to"]]
            ax, ay = a["x"] + a["w"] / 2, a["y"] + a["h"] / 2
            bx, by = b["x"] + b["w"] / 2, b["y"] + b["h"] / 2
            off = e.get("offset", 0)
            if off:
                import math
                L = math.hypot(bx - ax, by - ay) or 1
                nx, ny = -(by - ay) / L * off, (bx - ax) / L * off
                ax, ay, bx, by = ax + nx, ay + ny, bx + nx, by + ny
            x1, y1 = _clip(a, bx, by) if not off else _clip({**a, "x": a["x"] + (ax - a["x"] - a["w"]/2), "y": a["y"] + (ay - a["y"] - a["h"]/2)}, bx, by)
            x2, y2 = _clip(b, ax, ay) if not off else _clip({**b, "x": b["x"] + (bx - b["x"] - b["w"]/2), "y": b["y"] + (by - b["y"] - b["h"]/2)}, ax, ay)
            tone = e.get("tone", "plain")
            col = {"main": GREEN, "accent": "#b3471d"}.get(tone, "#333")
            mk = {"main": "ahg", "accent": "aha"}.get(tone, "ah")
            dash = ' stroke-dasharray="5 4"' if e.get("style") == "dashed" else ""
            dr = e.get("dir", "->")
            ms = f' marker-end="url(#{mk})"' if dr in ("->", "<->") else ""
            ms += f' marker-start="url(#{mk})"' if dr == "<->" else ""
            cross = e.get("cross")
            p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="1.6"{dash}{ms}/>')
            mx, my = (x1 + x2) / 2 + e.get("lx", 0), (y1 + y2) / 2 + e.get("ly", -6)
            if cross:
                p.append(f'<text x="{x1+(x2-x1)*0.7:.1f}" y="{y1+(y2-y1)*0.7+5:.1f}" font-size="16" font-weight="700" text-anchor="middle" fill="#b3471d" stroke="#fff" stroke-width="3" paint-order="stroke">✕</text>')
            if e.get("label"):
                for k, ln in enumerate(str(e["label"]).split("\n")):
                    p.append(f'<text x="{mx:.1f}" y="{my + k*13:.1f}" font-size="11" text-anchor="middle" fill="{col}" stroke="#fff" stroke-width="3" paint-order="stroke">{html.escape(ln)}</text>')
        for n in d.get("nodes", []):
            f, s, t = TONES.get(n.get("tone", "plain"), TONES["plain"])
            rx = 18 if n.get("shape") == "pill" else 6
            p.append(f'<rect x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" rx="{rx}" fill="{f}" stroke="{s}" stroke-width="1.3"/>')
            lines = [(ln, 12.5, "700") for ln in str(n.get("label", "")).split("\n")]
            if n.get("sub"):
                lines += [(ln, 10.5, "400") for ln in str(n["sub"]).split("\n")]
            total = sum(sz * 1.3 for _, sz, _ in lines)
            y = n["y"] + n["h"] / 2 - total / 2 + lines[0][1]
            for ln, sz, wt in lines:
                p.append(f'<text x="{n["x"]+n["w"]/2}" y="{y:.1f}" font-size="{sz}" font-weight="{wt}" text-anchor="middle" fill="{t}">{html.escape(ln)}</text>')
                y += sz * 1.3
        for nt in d.get("notes", []):
            col = {"main": GREEN, "accent": "#b3471d"}.get(nt.get("tone"), "#555")
            for k, ln in enumerate(str(nt["text"]).split("\n")):
                p.append(f'<text x="{nt["x"]}" y="{nt["y"] + k*14}" font-size="{nt.get("size",11)}" text-anchor="{nt.get("anchor","start")}" fill="{col}" font-weight="{nt.get("weight",400)}">{html.escape(ln)}</text>')
        p.append("</svg>")
        svg = "".join(p)
    cap = f'<figcaption>{md(d.get("caption",""))}</figcaption>' if d.get("caption") else ""
    return f'<figure class="dg">{svg}{cap}</figure>'

def dots(n):
    n = int(n or 1)
    return "".join(f'<span class="dot{" on" if i < n else ""}"></span>' for i in range(3))

def cover(meta):
    info = "".join(f"<div><span>{md(k)}</span><span>{md(v)}</span></div>" for k, v in meta["info"])
    return f'''<section class="page cover" style="border-top:2.2mm solid {GREEN}">
<div class="kicker">{md(meta["kicker"])}</div>
<h1>{md(meta["subject"])}<span class="t2">{md(meta["title2"])}</span></h1>
<div class="term">{md(meta["term"])}</div>
<div class="info">{info}</div></section>'''

# ---------------- flow pagination (client side) -----------------
# We emit a long stream of blocks per "chapter"; JS packs them into A4 pages.
PAGINATE_JS = r"""
function paginate(){
  const src = document.getElementById('stream');
  const out = document.getElementById('out');
  const blocks = Array.from(src.children);
  let page=null, body=null, footR='';
  const MAXH = 297*3.7795 - (20+24)*3.7795;
  function newPage(){
    page=document.createElement('section'); page.className='page';
    body=document.createElement('div'); page.appendChild(body);
    const f=document.createElement('div'); f.className='foot'; f.innerHTML='<span class="l"></span><span class="r">'+footR+'</span>';
    page.appendChild(f); out.appendChild(page);
  }
  for(const b of blocks){
    if(b.dataset.fixed){ const fr=b.dataset.foot||''; footR=fr; out.appendChild(b); page=null; continue; }
    if(b.dataset.foot!==undefined) footR=b.dataset.foot;
    if(b.dataset.newpage==='1' || !page){ newPage(); }
    body.appendChild(b);
    if(body.scrollHeight>MAXH){
      // try splitting tables row-wise
      if(b.tagName==='TABLE' && b.tBodies[0] && b.tBodies[0].rows.length>1){
        body.removeChild(b);
        const head=b.tHead?b.tHead.outerHTML:'';
        let cur=b.cloneNode(false); cur.innerHTML=head+'<tbody></tbody>';
        body.appendChild(cur);
        const rows=Array.from(b.tBodies[0].rows);
        for(const r of rows){
          cur.tBodies[0].appendChild(r);
          if(body.scrollHeight>MAXH){
            cur.tBodies[0].removeChild(r);
            if(cur.tBodies[0].rows.length===0){ body.removeChild(cur);}
            // carry preceding caption if it is alone at page end
            newPage(); cur=b.cloneNode(false); cur.innerHTML=head+'<tbody></tbody>'; body.appendChild(cur);
            cur.tBodies[0].appendChild(r);
          }
        }
      } else if(b.classList.contains('list') && b.children.length>1){
        body.removeChild(b);
        let cur=b.cloneNode(false); body.appendChild(cur);
        for(const r of Array.from(b.children)){
          cur.appendChild(r);
          if(body.scrollHeight>MAXH){ cur.removeChild(r); newPage(); cur=b.cloneNode(false); body.appendChild(cur); cur.appendChild(r);}
        }
      } else {
        body.removeChild(b);
        // move orphan caption along
        const prev=body.lastElementChild;
        let carry=null;
        if(prev && prev.classList.contains('cap')){ carry=prev; body.removeChild(prev);}
        newPage(); if(carry) body.appendChild(carry); body.appendChild(b);
      }
    }
    // avoid caption orphan at bottom: handled when next block overflows
  }
  // page numbers
  const pages=out.querySelectorAll('.page');
  pages.forEach((p,i)=>{ let f=p.querySelector('.foot'); if(!f){f=document.createElement('div');f.className='foot';f.innerHTML='<span class="l"></span><span class="r"></span>';p.appendChild(f);} f.querySelector('.l').textContent=(i+1); });
  src.remove();
  document.body.dataset.done='1';
}
"""

def wrap(title, css, stream):
    css = css.replace("GREEN", GREEN)
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>{css}</style></head><body><div id="out"></div><div id="stream" style="width:174mm">{stream}</div>
<script>{PAGINATE_JS}
document.fonts.ready.then(paginate);</script></body></html>'''

# ---------------- guide -----------------
def build_guide(d):
    m = d["meta"]
    S = []
    S.append(f'<div data-fixed="1">{cover(m)}</div>')
    # TOC
    toc = '<div class="toc" data-newpage="1" data-foot=""><h2>Contents</h2>'
    for u in d["units"]:
        toc += f'<div class="u"><div class="n">{md(u["no"])}</div><div><h3>{md(u["title"])}</h3>'
        for s in u["sections"]:
            toc += f'<div class="s"><span>{md(s["id"])}</span>{md(s["title"])}</div>'
        toc += '</div></div>'
    toc += '</div>'
    S.append(toc)
    for u in d["units"]:
        foot = f'{u["no"]}단원 · {u["title"]}'
        rows = "".join(f'<tr><td class="id">{md(s["id"])}</td><td class="t">{md(s["title"])}</td><td>{md(s.get("keywords",""))}</td></tr>' for s in u["sections"])
        nt = sum(len(s.get("terms", [])) for s in u["sections"])
        no = sum(len(s.get("ox", [])) for s in u["sections"])
        nc = sum(len(s.get("cases", [])) for s in u["sections"])
        S.append(f'<div class="unit" data-newpage="1" data-foot="{html.escape(foot)}"><div class="lab">Unit</div><div class="big">{md(u["no"])}</div><h2>{md(u["title"])}</h2><div class="pg">{md(u.get("pages",""))}</div><table>{rows}</table><div class="cnt">용어 {nt} · OX {no} · 사례 {nc} · 모두 {nt+no+nc}문제</div></div>')
        for s in u["sections"]:
            S.append(f'<div class="sec" data-newpage="1"><h2><span class="id">{md(s["id"])}</span>{md(s["title"])}</h2></div>')
            S.append('<div class="cap">Frame · 왜 필요한가</div>')
            S.append('<div class="frame">' + "".join(f'<div><span class="k">{md(k)}</span><span>{md(v)}</span></div>' for k, v in s["frame"]) + '</div>')
            S.append('<div class="cap">List · 핵심 정리</div>')
            items = ""
            for it in s["list"]:
                hand = " hand" if it.get("tag") == "필기" else ""
                dg = diagram(it["diagram"]) if it.get("diagram") else ""
                items += f'<div><span class="k{hand}">{md(it["id"])} {md(it.get("tag",""))}</span><span class="v{hand}">{md(it["text"])}{dg}</span></div>'
            S.append(f'<div class="list">{items}</div>')
            n = 0
            ans = []
            if s.get("terms"):
                S.append('<div class="cap" data-newpage="1">Term Check · 설명에 맞는 용어 적기</div>')
                tr = ""
                for t in s["terms"]:
                    n += 1
                    tr += f'<tr><td class="no">{n:02d}</td><td class="d">{dots(t.get("diff"))}</td><td>{md(t["q"])}</td><td class="L">{md(t.get("L",""))}</td><td class="ans"></td></tr>'
                    ans.append((n, t["a"], t.get("why", ""), t.get("L", "")))
                S.append(f'<table class="q"><thead><tr><th>No.</th><th>난이도</th><th>설명</th><th class="c">L</th><th>용어</th></tr></thead><tbody>{tr}</tbody></table>')
            if s.get("ox"):
                S.append('<div class="cap">Problems · OX</div>')
                tr = ""
                for t in s["ox"]:
                    n += 1
                    tr += f'<tr><td class="no">{n:02d}</td><td class="d">{dots(t.get("diff"))}</td><td>{md(t["q"])}</td><td class="L">{md(t.get("L",""))}</td><td class="ox">OX</td></tr>'
                    ans.append((n, t["a"], t.get("why", ""), t.get("L", "")))
                S.append(f'<table class="q"><thead><tr><th>No.</th><th>난이도</th><th>문장</th><th class="c">L</th><th class="c">O / X</th></tr></thead><tbody>{tr}</tbody></table>')
            if s.get("cases"):
                S.append('<div class="cap">사례 · 객관식</div>')
                for t in s["cases"]:
                    n += 1
                    opts = "".join(f'<div class="opt">{md(o)}</div>' for o in t.get("options", []))
                    blank = "" if opts else '<div class="blank"></div>'
                    bx = f'<div class="box">{md(t["box"])}</div>' if t.get("box") else ""
                    S.append(f'<div class="case"><div class="h">{n:02d} {dots(t.get("diff"))}<span class="L">[{md(t.get("L",""))}]</span></div><div>{md(t["q"])}</div>{bx}{opts}{blank}</div>')
                    ans.append((n, t["a"], t.get("why", ""), t.get("L", "")))
            S.append(f'<div data-newpage="1"><h3 class="ans">정답 · 해설</h3><div class="cap">Block {md(s["id"])} · {md(s["title"])}</div></div>')
            tr = "".join(f'<tr><td class="no">{k:02d}</td><td class="an">{md(a)}</td><td>{md(w)}</td><td class="L">{md(L)}</td></tr>' for k, a, w, L in ans)
            S.append(f'<table class="a"><thead><tr><th>No.</th><th>답</th><th>왜</th><th>L</th></tr></thead><tbody>{tr}</tbody></table>')
    return wrap(f'{m["subject"]} {m["title2"]}', BASE_CSS + GUIDE_CSS, "\n".join(S))

# ---------------- mock -----------------
def build_mock(d):
    m = d["meta"]
    S = [f'<div data-fixed="1">{cover(m)}</div>']
    for ex in d["exams"]:
        eid = ex["id"]
        S.append(f'<div class="mh" data-newpage="1" data-foot="{eid} – 문제"><span class="id">{md(eid)}</span>{md(ex["title"])} · {len(ex["questions"])}문제</div>')
        for i, q in enumerate(ex["questions"], 1):
            if q["type"] == "ox":
                body = '<div class="ox">O X</div>'
            else:
                body = "".join(f'<div class="opt">{md(o)}</div>' for o in q["options"])
            bx = f'<div class="box">{md(q["box"])}</div>' if q.get("box") else ""
            S.append(f'<div class="qq"><span class="n">{i:02d}</span><span class="u">{md(q.get("unit",""))}</span><div class="st">{md(q["stem"])}</div>{bx}{body}</div>')
        S.append(f'<div data-newpage="1" data-foot="{eid} – 정답"><h3 class="ans">{md(ex["title"])} 정답 · 해설</h3><div class="sub">{md(eid)}</div></div>')
        tr = "".join(f'<tr><td class="no">{i:02d}</td><td class="an">{md(q["a"])}</td><td>{md(q["why"])}</td><td class="u">{md(q.get("unit",""))}</td></tr>' for i, q in enumerate(ex["questions"], 1))
        S.append(f'<table class="a"><thead><tr><th>No.</th><th>답</th><th>왜</th><th>단원</th></tr></thead><tbody>{tr}</tbody></table>')
    return wrap(f'{m["subject"]} {m["title2"]}', BASE_CSS + MOCK_CSS, "\n".join(S))

if __name__ == "__main__":
    kind, src, dst = sys.argv[1:4]
    d = json.load(open(src, encoding="utf-8"))
    out = build_guide(d) if kind == "guide" else build_mock(d)
    open(dst, "w", encoding="utf-8").write(out)
    print("wrote", dst)
