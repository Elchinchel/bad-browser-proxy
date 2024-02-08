last_messages = read("vk_last_messages", [])
text = request.form.get("text", "")
for i in range(5):
  t = request.form.get(f"text{i}")
  if t is None:
    break
  text += t
params = request.args.get("params", {})
err = None
if params:
  from urllib.parse import parse_qs
  params = {k: v[0] for k, v in parse_qs(params).items()}
if text not in last_messages and text != "":
  _, err = su("vk_api", request.cookies["token"],  "messages.send", dict({
"peer_id": request.args["peer_id"],
"message": text,
"random_id": 0
}, **params))
  last_messages = last_messages[:5]
  last_messages.append(text)
  write("vk_last_messages", last_messages)
if not err:
  r = redirect(
'/vk_show_conversation?'+
urlencode({"peer_id": request.args["peer_id"]}))
else:
  r = str(err)