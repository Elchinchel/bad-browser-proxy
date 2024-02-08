r = ""
for c in args[0]:
  if len(r) > args[1]:
    if c in {" ", "\n"}:
      r += "..."
      break
  r += c