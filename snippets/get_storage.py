value, err = su("vk_api", request.cookies["token"], "storage.get", {"key": args[0]})
if len(args) == 2:
  if value is None:
    value = args[1]
elif value is None:
  value = err
r = value