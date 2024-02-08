su("vk_api", request.cookies["token"], "groups.join", {"group_id": request.args["id"]})
r = redirect(f'/show_group?id={request.args["id"]}')