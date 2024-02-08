token = ""
data = {} if len(args) < 2 else args[1]
#r = su("vk_api", token, args[0], data)
from flask import make_response
r = make_response("ok")
r =