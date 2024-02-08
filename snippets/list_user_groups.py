token = request.cookies["token"]
user_id = request.args["id"]
body = ""
for group in su("vk_api", token, "groups.get", {"user_id": user_id, "extended": 1})[0]["items"]:
  body += f'''<a href="/show_group?{urlencode({"id": group["id"]})}">
{group["name"]}</a><br>'''
r = f'<html><head><title>Группы</title></head><body>{body}</body></html>'