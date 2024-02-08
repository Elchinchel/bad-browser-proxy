lines = []
i = 0
while True:
  line = request.form.get(f"line{i}", None)
  if line is None:
    break
  if line != '.':

    lines.append(line.replace("&lt;", "<").replace("&amp;", "&"))
  i += 1

write_snippet(request.form.get("name"), "\n".join(lines))
r = redirect("/snippet_edit?"+urlencode({"name": request.form.get("name")}))