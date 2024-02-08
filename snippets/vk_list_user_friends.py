token = request.cookies["token"]
user_id = request.args["id"]
body = ""
for friend in su("vk_api", token, "friends.get", {"user_id": user_id, "fields": "first_name,last_name"})[0]["items"]:
  body += f'''<a href="/vk_show_user?{urlencode({"id": friend["id"]})}"
>{friend["first_name"]} {friend["last_name"]}</a><br>'''
r = f'<html><head><title>Друзья</title></head><body>{body}</body></html>'