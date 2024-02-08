import requests
from io import BytesIO
from flask import send_file
from PIL import Image
#url = "https://vk.com/sticker/1-54013-64"
url = request.args["url"]
file = BytesIO()
file_ = BytesIO()
resp = requests.get(url)
file.write(resp.content)
file.seek(0)
ctype = resp.headers["Content-Type"].split("/")[1]
image = Image.open(file)
if ctype != "jpeg":
  bg = Image.new("RGB", image.size, (255, 255, 255))
  if len(image.split()) < 3:
    bg.paste(image)
  else:
    bg.paste(image, mask=image.split()[3])
  bg.save(file_, format="JPEG", quality=50)
else:
  image = image.save(file_, format="JPEG", quality=50)
file_.seek(0)
r = send_file(file_, as_attachment=True,
attachment_filename="image.jpeg", mimetype="image/jpeg")