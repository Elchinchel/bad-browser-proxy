name = request.args.get("name")
snippet = read_snippet(name)
i = 0
body = f'<form action="snippet_save" method="post"><input hidden name="name" value="{name}">'
if snippet == '':
  snippet =  '\n'
for line in snippet.splitlines():
  body += f'''<textarea name="line{i}">{line.replace('&','&amp;').replace("<","&lt;")}</textarea>
<br>'''
  i += 1
code_query = urlencode({"code": f"r=su('{name}')\n", "back": f'/snippet_edit?{urlencode({"name": name})}'})
r = body + ('<input type="submit" value="save"> <a href="/snippets">snips</a>' +
f' <a href="/run?{code_query}">run</a></form>')