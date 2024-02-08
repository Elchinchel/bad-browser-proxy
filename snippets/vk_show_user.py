token = request.cookies["token"]
user_id = request.args["id"] 
user = su("vk_api", token, "users.get", {"user_ids": user_id, "fields": "photo_100"})[0][0]
name = f'{user["first_name"]} {user["last_name"]}'
r = f'''<html><head><title>{name}</title></head><body>
<img src="/get_image?{urlencode({"url": user["photo_100"]})}">
<a href="/vk_show_conversation?{urlencode({ "peer_id": user["id"], "conv_name": name})}"
>Открыть диалог</a>
<br><a href="/vk_list_user_friends?{urlencode({"id": user_id})}">Друзья</a><br>
<a href="/list_user_groups?id={user_id}">Группы<a>
</body></html>'''