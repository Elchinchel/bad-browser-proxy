bookmarks = read("bookmarks.json", {})
name = request.form["name"]
bookmarks[name] = bookmarks.get(name, "") + request.form["url"]
write("bookmarks.json", bookmarks)
r = redirect("/bookmarks")