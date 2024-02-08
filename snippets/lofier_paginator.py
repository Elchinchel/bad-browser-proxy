pages = [""]
tag = False
for char in args[0]:
  pages[-1] += char
  if char == '<':
    tag = True
  elif char == '>':
    tag = False
  if len(pages[-1]) > 8192 and not tag:
    pages.append("")
r = pages