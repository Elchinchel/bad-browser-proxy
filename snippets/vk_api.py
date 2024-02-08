# args: token, method[, params]
import json, requests
r = requests.post(
f'https://api.vk.com/method/{args[1]}?v=5.100&lang=ru&access_token={args[0]}',
data=args[2] if len(args) > 2 else {}).json()
r = (r.get("response"), r.get("error"))