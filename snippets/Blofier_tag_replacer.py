html = 'abc<script>def<h5>foo</h5>'
def gen(text, prev_gen=None):
 for c in text:
  yield c
 if prev_gen is not None:
  for c in prev_gen:
   yield c
text = gen(html)
payload = ''
try:
 while True:
  c = text.__next__()
  if c != '<':
   payload += c
   continue
  tag_name=tag_atts=tag_body=next_tag_name=''
  try:
   while True:
    c = text.__next__()
    if c in {'\n','\r',' ','>'} or len(tag_name) > 10:
     if tag_name not in {'script','style'}:

      payload += '<' + tag_name + c
      break
     text = gen(c, text)
     while True:
      c = text.__next__()
      if c != '>':
       tag_atts += c
       if len(tag_atts) > 2000:
        raise StopIteration
       continue
      try:
       while True:
        c = text.__next__()
        if c != '<':
         tag_body += c
         if len(tag_body) > 100000:
          raise StopIteration

         continue
        c = text.__next__()
        new_tag = ''
        close = True if c == '/' else False
        while True:
         c = text.__next__()
         if c not in {'\n', '\r', ' ', '>'}:
          if len(new_tag) > 10:
           tag_body += '<'+('/' if close else '')+new_tag
           break
          if new_tag == tag_name:
           if not close:
            tag_body += '<' + ('/' if close else '') + new_tag
            raise KeyError
           for _ in range(100):
            c = text.__next__()
            if c == '>':
             raise IndexError
            new_tag += c
           tag_body += '<' + ('/' if close else '') + new_tag
          raise StopIteration
         new_tag += c
      except StopIteration:
       text = gen(tag_body, text)
    tag_name += c
  except StopIteration:
   text = gen('<'+tag_name+tag_atts, text)
except StopIteration:
 r = payload.replace('<', '&lt;')