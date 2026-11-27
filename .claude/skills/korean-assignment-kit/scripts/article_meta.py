import sys,re,html
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8',errors='replace').read()
    def m(p):
        r=re.search(p,s,re.I|re.S); return html.unescape(r.group(1)).strip() if r else '-'
    title=m(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)')
    date=m(r'(?:article:published_time|datePublished)["\']?\s*(?:content=|:)\s*["\']([^"\']+)')
    author=m(r'<meta[^>]+(?:name|property)=["\'](?:author|dable:author|article:author)["\'][^>]+content=["\']([^"\']+)')
    if author=='-': author=m(r'"author"\s*:\s*\{[^}]*"name"\s*:\s*"([^"]+)')
    if author=='-': author=m(r'"author"\s*:\s*\[\s*\{[^}]*"name"\s*:\s*"([^"]+)')
    print(f.split('/')[-1],'|',title,'|',date,'|',author)
