def route_snippet(app, snippet):
  exec('@app.route("/%(name)s")\ndef %(name)s():\n  return su("%(name)s")' % {"name": snippet})
route_snippet(app, "vk_show_conversation")
@app.route("/vk_send_message", methods=["POST"])
def vk_send_message():
  return su("vk_send_message")
@app.route("/edit_message", methods=["GET", "POST"])
def edit_message():
  return su("edit_message")
@app.route("/vk_auth_set", methods=["POST"])
def settoken():
  return su("vk_auth_set")
@app.route("/settings_set", methods=["POST"])
def settings_set():
  return su("settings_set")
route_snippet(app, "vk_list_conversations")
route_snippet(app, "get_image")
route_snippet(app, "vk_api_methods")
route_snippet(app, "vk_message_reply")
route_snippet(app, "vk_show_user")
route_snippet(app, "vk_list_user_friends")
route_snippet(app, "get_voice")
route_snippet(app, "vk_feed")
route_snippet(app, "show_group")
route_snippet(app, "join_group")
route_snippet(app, "mark_as_read")
route_snippet(app, "list_user_groups")
route_snippet(app, "show_wall")
route_snippet(app, "settings")