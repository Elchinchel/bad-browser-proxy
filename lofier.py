from main import app, request, su


@app.route("/lofier")
def lofier_index():
  return su("lofier_index")


@app.route("/lofier_get")
def lofier_get():
  a = request.args
  return su("lofier_filth_maker", a.get("url"), a.get("full", 0), a.get("page", 0))
