peer_id = request.args["peer_id"]
su("vk_api", request.cookies["token"], "messages.markAsRead", {
"peer_id": peer_id, "mark_conversation_as_read": 1})
r = redirect("/vk_list_conversations")