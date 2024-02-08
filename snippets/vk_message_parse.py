time = lambda: round(__import__("time").time())
msg = args[0]
extended = args[1]
escape = args[2] if len(args) > 2 else True
text = msg["text"]
att_types = {
  "photo": "Фотография", "video": "Видеозапись", "gift": "Подарок",
"audio_message": "Голосовое сообщение", "doc": "Документ"
}
def parse_atts(loc, msg):
  text = ""
  atts = msg["attachments"]
  for a in atts:
    type = a["type"]
    att = a[type]
    if type == "sticker":
      text += f'<<img src="/get_image?{urlencode({"url": att["images_with_background"][0]["url"]})}">>'
    elif type == "graffiti":
      text += f'<<a href="/get_image?{urlencode({"url": att["url"]})}">>[Граффити]<</a>>'
    elif type == "photo":
      text += f'''<<a href="/get_image?{urlencode({"url": att["sizes"][-1]["url"]})}">>
<<img src="/get_image?{urlencode({"url": att["sizes"][0]["url"]})}">><</a>>'''
    elif type == "audio":
      name = f'{att["artist"]} - {att["title"]}'
      link = f'/get_voice?{urlencode({"url": att["url"], "name": name})}'
      text += f'[<<a href="{link}">>{name}<</a>> ({att["duration"]}c.)]'
    elif type == "wall":
      link = f'''/show_wall?{urlencode({"post": f'{att["from_id"]}_{att["id"]}'})}'''
      text += f'[<<a href="{link}">>запись со стены<</a>>]'
    elif type == "audio_message":
      link = f'''/get_voice?{urlencode({"url": att["link_mp3"], "name": f'{att["owner_id"]}_{loc["time"]()}'})}'''
      text += f'[<<a href="{link}">>гс<</a>> ({att["duration"]} сек.)]\n'
    else:
      text += f"[{loc['att_types'].get(type, type)}]"
  return text
def fwd_render(loc, msg):
  text = msg["text"]
  for fwd in msg.get("fwd_messages", []):
    text += "\n[Пересыл]\n" + loc["parse_atts"](loc, fwd) + loc["fwd_render"](loc, fwd)
  return text
if extended:
  if "fwd_messages" in msg:
    text = fwd_render(locals(), msg)
  if "reply_message" in msg:
    msg["reply_message"]["text"] = su("text_trim", msg["reply_message"]["text"], 50)
    text += "\n[Ответ]\n" + su("vk_message_parse", msg["reply_message"], 1, 0)
  if msg["attachments"]:
    text += f'\n{parse_atts(locals(), msg)}'
else:
  if not msg["text"]:
    att = msg["attachments"]
    if att:
      text = att_types.get(att[0]["type"], att[0]["type"])
  else:
    if len(text) > 50:
      text = su("text_trim", text, 50)
  if "reply_message" in msg:
    text = "[Ответ] " + text
  elif msg["fwd_messages"]:
    text = "[Пересыл] " + text
#text = str(msg)
if escape:
  r = su("format_mentions", text, True)
  r = r.replace("<", "&lt;").replace(">", "&gt;").replace("]", "&#093;").replace("\n", "<br>")
  r = r.replace("&lt;"*2, "<").replace("&gt;"*2, ">")
else:
  r = text