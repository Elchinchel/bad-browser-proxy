tokens = {
"логин":  "вставь сюда токен от странички вк"
}
from flask import make_response
r = make_response(redirect("/vk_list_conversations"))
#raise Exception(request.form)
r.set_cookie("token", tokens.get(request.form["login"].lower(), ""))