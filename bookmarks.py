from main import app, su, read, write, request, redirect
from urllib.parse import urlencode


@app.route("/bookmarks")
def bookmark_list():
  return su("bookmark_list")


@app.route("/bookmark_delete")
def bookmark_delete():
  return su("bookmark_delete")


@app.route("/bookmark_add", methods=["POST"])
def bookmark_add():
  return su("bookmark_add")
