url = args[0]
full = args[1]
page = int(args[2])
sites = read("sites.json", {})
if url in sites:
  r = sites[url]
else:
  r = su("http_get", url)
  r = su("lofier_tag_replacer", r)
  r = su("lofier_link_modifier", r, url)
  sites[url] = r
  write("sites.json", sites)
if not full:
  import re
  body = re.findall(r'<body>(.*)</body>', r, flags=re.DOTALL)
  r = body[0] if body else r
  pages = su("lofier_paginator", r)
  r = pages[page] #.replace("<","&lt;")
  if not '<title>' in r:
    r = f'<title>Page {page+1}</title>' + r
  r += "<br>"
  for i in range(len(pages)):    r += f'<a href="/lofier_get?{urlencode({"url": url, "page": i})}">{(i+1) if i != page else "^"}</a>'
  r += f'<a href="/lofier_get?{urlencode({"url": url, "full": 1})}">full</a>'