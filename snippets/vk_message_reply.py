token = request.cookies["token"]
peer_id = request.args["peer_id"]
reply_to = request.args["reply_to"]
msg = su("vk_api", token, "messages.getById", {"message_ids": reply_to})[0]["items"][0]
reply_to = urlencode({"reply_to": reply_to})
r = f'''<html><head><title>Ответ на сообщение</title></head>
<body>
<div>{su("vk_message_parse", msg, True)}</div>
<form action="/vk_send_message?{
urlencode({"peer_id": peer_id, "params": reply_to})}" method="post">
{''.join([('<textarea name="text%d"></textarea>' % i) for i in range(5)])}
<input type="submit" value="Ответить">
</form></body></html>'''