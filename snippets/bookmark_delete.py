bookmarks = read("bookmarks.json", {})
del bookmarks[request.args.get("name")]
write("bookmarks.json", bookmarks)
r = redirect("/bookmarks")