token = request.cookies["token"]
gid = request.args["id"]
group, _ = su("vk_api", token, "groups.getById", {"group_ids": gid, "fields": "photo_100"})
group = group[0]
r = f'''<head><title>{group["name"]}</title></head><body>
<img src="/get_image?{urlencode({"url": group["photo_100"]})}"><br>
{group["name"]}<br>
<a href="/join_group?id={gid}">Подписаться</a>
</body>'''