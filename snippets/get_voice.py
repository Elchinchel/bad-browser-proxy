import requests
from io import BytesIO
from flask import send_file
name = request.args["name"]
url = request.args["url"]
file = BytesIO()
resp = requests.get(url)
file.write(resp.content)
file.seek(0)
ctype = resp.headers["Content-Type"] #.split("/")[1]
r = send_file(file, as_attachment=True,
attachment_filename=f"{name}.mp3", mimetype=ctype)