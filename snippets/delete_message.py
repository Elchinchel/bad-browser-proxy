su()
q = request.args
r = redirect(f'/vk_show_conversation?{urlencode({"conv_name": q["conv_name"], "peer_id": "peer_id"})}')