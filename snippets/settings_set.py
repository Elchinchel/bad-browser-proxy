sets_names = ["show_msg_date",
"rev_msg_order",
"mark_as_read"]
for name in sets_names:
  su("set_storage", name, request.form.get(name, "off"))
  su("sleep", 0.5)
r = redirect("/vk_list_conversations")