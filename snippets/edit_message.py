token = request.cookies["token"]
msg_id = request.args["id"]
q = request.args
query = urlencode({"peer_id": q["peer_id"]})
if request.method == "GET":
  msg = su("vk_api", token, "messages.getById", {"message_ids": msg_id})[0]["items"][0]
  r = f'''<head><title>Редактирование сообщения</title></head><body>
<form action="/edit_message?{query}&id={msg_id}" method="post">'''
  chunks = [""]
  for c in msg["text"]:
    if len(chunks[-1]) > 60:
      chunks.append("")
    chunks[-1] += c
  for i, chunk in enumerate(chunks):
    r += f'<textarea name="text{i}">{chunk}</textarea><br>'
  r += f'<input type="submit" value="Сохранить"></form>'
else:
  text = ""
  for i in range(50):
    t = request.form.get(f"text{i}")
    if t is None:
      break
    text += t
  _, err = su("vk_api", token, "messages.edit", {"message_id": msg_id, "message": text, "peer_id": q["peer_id"]})
  r = redirect(f"/vk_show_conversation?{query}") if err is None else str(err)