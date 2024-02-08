import re
text = args[0]
double = args[1] if len(args) > 1 else False
for type, id, name in re.findall(r"\[(id|club)(\d+)\|(.+?)\]", text):
  link = f'<a href="/{"vk_show_user" if type == "id" else "show_group" }?id={id}">{name}</a>'
  if double:
    link = link.replace("<", "<<").replace(">", ">>")
  text = text.replace(f'[{type}{id}|{name}]', link, 1)
r = text