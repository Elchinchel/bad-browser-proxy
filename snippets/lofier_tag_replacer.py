import re
#args = [read("sites.json", {})["http://vk.com/dev/methods"]]
def rem_tag(re, tag, text):
 return re.sub(r"<{}[^>]*>".format(tag), "", text, flags=re.DOTALL)
def rem_pair(re, tag, text):
  regex = r'(<{tag}[^>]*>.*?)+(</{tag}[^>]*>)'
  for open, close in re.findall(regex.format(tag=tag), text, flags=re.DOTALL):
    text = text.replace(open+close, "")
  return text
r = rem_tag(re, "link", args[0])
r = rem_tag(re, "meta", r)
r = rem_pair(re, "script", r)
r = rem_tag(re, "script", r)
r = rem_pair(re, "style", r)
r = rem_tag(re, "style", r)