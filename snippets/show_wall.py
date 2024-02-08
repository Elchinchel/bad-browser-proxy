post = request.args["post"]
token = request.cookies["token"]
resp, _ = su("vk_api", token, "wall.getById", {"posts": post, "extended": 1})
post = resp["items"][0]
r = f'''<head><title>Wall post</title></head><body>
{su("escape", post.get("text"))}
{su("escape", su("att_parse", post.get("attachments", [])))}
</body>'''