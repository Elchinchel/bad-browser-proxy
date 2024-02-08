token = request.cookies.get("token")
if token:
  convs, _ = su("vk_api", token, "messages.getConversations")
else:
  convs = {}
peers = su("vk_get_info", token, {c["conversation"]["peer"]["id"] for c in convs.get("items", [])})
body = '<a href="/settings">Настройки</a><br><br>'
for item in convs.get("items", []):
  conv = item["conversation"]
  peer = conv["peer"]
  type = peer["type"]
  if type == "chat":
    sets = conv["chat_settings"]
    img = sets.get("photo", {}).get("photo_50")
    name = sets["title"]
  else:
    img = peers[peer["id"]]["photo"]
    name = peers[peer["id"]]["name"]
  msg = item["last_message"]
  text = su("vk_message_parse", msg, False)
  unread = conv.get("unread_count")
  if unread is not None:
    link = f'/vk_show_conversation?{urlencode({"peer_id": peer["id"], "offset": int(unread/40)*40})}'
    read = f'<a href="/mark_as_read?peer_id={peer["id"]}">^</a>'
    text = f'<i>{text}</i> (<a href="{link}">{unread}</a>) {read}'
  if conv["out_read"] != item["last_message"]["id"]:
    text = "¤ " + text
  body += f'''
<div>
<img src="/get_image?{urlencode({"url": img})}" height="25">
<a href="/vk_show_conversation?{urlencode({"peer_id": peer["id"]})}
">{name}</a>
{text}
</div>
  '''
unread = convs.get("unread_count", 0)
if token:
  r = '<html><head><title>Диалоги (%d)</title></head><body>%s</body></html>' % (unread, body)
else:
  r = su("vk_auth")