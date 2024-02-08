token = args[0]
peers = args[1]
known_peers = {int(k): v for k, v in read("peers.json", {}).items()}
users = []
groups = []
for peer in peers:
  if peer not in known_peers:
    if peer > 0:
      users.append(str(peer))
    else:
      groups.append(str(abs(peer)))
if users:
  users, _ = su("vk_api", token, "users.get", {"user_ids": ",".join(users), "fields": "photo_50"})
  for user in users:
    known_peers.update({user["id"]: {
"name": user["first_name"]+" "+user["last_name"],
"link": "/vk_show_user?id=%d" % (user["id"],),
"photo": user["photo_50"]
    }})
if groups:
  groups, _ = su("vk_api", token, "groups.getById", {"group_ids": ",".join(groups), "fields": "photo_50"})
  for group in groups:
    known_peers.update({0-group["id"]: {
"name": group["name"],
"link": "/show_group?id=%d" % (group["id"]),
"photo": group["photo_50"]
}})
if users or groups:
  write("peers.json", known_peers)
r = {}
for peer in peers:
  if peer < 2e9:
    r.update({peer: known_peers[peer]})