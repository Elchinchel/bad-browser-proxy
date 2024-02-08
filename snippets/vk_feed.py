token = request.cookies["token"]

news, _ = su("vk_api", token, "newsfeed.get", {})
text = ""
for el in news["items"]:
  if el["type"] in {"friend"}:
    continue
  text += str(el)
r = str(news)