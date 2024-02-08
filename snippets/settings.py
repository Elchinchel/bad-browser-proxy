rev_msg = su("get_storage", "rev_msg_order", "off")
su("sleep", 0.5)
show_date = (su("get_storage", "show_msg_date") == "on")
r = f'''<head><title>Настрой_о4ка</title></head><body>
<a href="/vk_list_conversations">К списку диалогов</a><br>
<form action="/settings_set" method="post">
<input type="checkbox" {"checked" if rev_msg == "on" else ""} name="rev_msg_order"> 
Поле ввода сверху диалога<br>
<input type="checkbox" name="show_msg_date" {"checked" if show_date else ""}>
Показывать время отправки сообщений<br>
<input type="number">
<input type="submit" value="Сохранить">
</form></body>'''