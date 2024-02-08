import json
def read(filename):
  with open("/home/chat/JSON/"+filename, "r") as file:
    return json.loads(file.read())
def load_ref(reference, read):
  filename, path = reference.split("#")
  data = read(filename)
  for key in path.split("/")[1:]:
    data = data[key]
  return data
schema = read("methods.json")
body = ""
group = request.args.get("group")
method = request.args.get("method")
if not (method or group):
  groups = set()
  for method in schema["methods"]:
    groups.add(method["name"].split(".")[0])
  groups = list(groups)
  groups.sort()
  for group in groups:
    body += f'<a href="/vk_api_methods?{urlencode({"group": group})}">{group}</a><br>'
elif group:
  for method in schema["methods"]:
    name = method["name"]
    if name.split(".")[0] == group:
      desc = method.get("description", "")
      body += f'''<div><a href="/vk_api_methods?{urlencode({"method": name})}">{name}</a><br>
{desc}</div><br>'''
else:
  for method_ in schema["methods"]:
    if method_["name"] == method:
      method = method_
  name = method["name"]
  resp = {}
  for k, v in method["responses"].items():
    resp.update({k: load_ref(v["$ref"], read)})
  body = f'''<b>{name}</b><br><i>{method.get("description", "no desc")}</i><br>&gt;params:
{"<br>".join([
f'<br><i>{p["name"]}</i>: {p["type"]}<br>{p.get("description", "")}' for p in method.get("parameters", [])
])}&gt;responses:<br>{"<br>".join([f"<i>{k}</i>:<br>{v}" for k, v in resp.items()])}'''
r = '<html><head><title>VK API methods</title></head><body>%s</body></html>' % body