bookmarks = read("bookmarks.json", {})
body = ""
for name, url in bookmarks.items():
  body += f'<a href="/bookmark_delete?{urlencode({"name": name})}">X</a> <a href="{url}">{name}</a><br>'
r = '<html><head><title>Bookmarks</title></head><body>%s<form action="/bookmark_add" method="post"><input name="name"><input name="url" value="http://"><input type="submit" value="add bookmark"></form></body></html>' % body