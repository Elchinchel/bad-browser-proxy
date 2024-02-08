from urllib.parse import urljoin
import re
r = args[0]
links = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', r, flags=re.DOTALL)
for link, name in links:
  if not link.startswith("http"):
    query = urlencode({"url": urljoin(args[1], link)})
  else:
    query = urlencode({"url": link})
  r = re.sub(rf'(<a.*?href="){re.escape(link)}(".*?>{re.escape(name)}</a>)',
  rf'\1{"/lofier_get?"+query}\2', r,
  count=1, flags=re.DOTALL)