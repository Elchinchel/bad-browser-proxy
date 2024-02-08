from datetime import datetime as dt
offset = int(request.args.get("offset", 0))
peer_id = int(request.args["peer_id"])
token = request.cookies["token"]
query = urlencode({"peer_id": peer_id})
reverse = (su("get_storage", "rev_msg_order") == "on")
su("sleep", 0.5)
show_date = (su("get_storage", "show_msg_date") == "on")
messages_ = su("vk_api", token,  "messages.getHistory",
{"peer_id": peer_id, "offset": offset, "count": 40, "extended": 1})[0]
messages = messages_["items"]
conv = messages_["conversations"][0]
if int(peer_id) > 2e9:
  conv_name = conv["chat_settings"]["title"]
else:
  conv_name = su("vk_get_info", token, [peer_id])[peer_id]["name"]
if not reverse:
  messages = messages[::-1]
peers = su("vk_get_info", token, {m["from_id"] for m in messages})
if offset:
  offset = f'''<a href="/vk_show_conversation?{query+f"&offset={offset-40}"}">-</a>
<i> Сдвиг - {offset} </i>
<a href="/vk_show_conversation?{query+f"&offset={offset+40}"}">+</a>'''
else:
  offset = f'<a href="/vk_show_conversation?{query+f"&offset={offset+40}"}">~листануть смс~</a>'
body = f'''<a href="/vk_list_conversations?{urlencode({"token": token})}">Назад</a> <a
href="/vk_show_conversation?{query}"
>Обновить</a><br>{offset}<br>'''
msgs_html = ""
for msg in messages:
  if msg["peer_id"] > 2e9:
    name = peers[msg["from_id"]]["name"]
  else:
    name = "Я" if msg["out"] else peers[msg["from_id"]]["name"].split()[0]
  msgs_html += f'''<div>
{"¤ " if (msg["id"] > conv["in_read"] or conv["out_read"] < msg["id"]) else ""}
{dt.fromtimestamp(msg["date"]+(3600*3)).strftime("%H:%M ") if show_date else ""}
<a href="{peers[msg["from_id"]]["link"]}">{name}</a>: 
{su("vk_message_parse", msg, True)}
 <a href="/vk_message_reply?{query}&reply_to={msg["id"]}">R</a>
{f' <a href="/edit_message?{query}&id={msg["id"]}">E</a>' if msg["out"] else ""}
</div>'''
input = f'''<form
action="/vk_send_message?{query}"
method="post">
<textarea name="text"></textarea>
<input type="submit" name="send" value="Отправить">
</form>'''
if reverse:
  body += input + msgs_html
else:
  body += msgs_html + input
r = f'<html><head><title>{conv_name}</title></head><body>{body}</body></html>'