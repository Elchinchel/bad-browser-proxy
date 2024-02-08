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
r = parse_atts(locals(), {"attachments": args[0]})