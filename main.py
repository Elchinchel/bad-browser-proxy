import os, json, traceback
from flask import Flask, request, redirect
from urllib.parse import urlencode


path = os.path.dirname(__file__)
os.makedirs(os.path.join(path, 'snippets'), exist_ok=True)


class SnippetError(Exception):
    def __init__(self, name, traceback):
        self.name = name
        self.traceback = traceback


def read(filename, default):
    try:
        with open(os.path.join(path, filename), "r", encoding="utf-8") as file:
            return json.loads(file.read())
    except FileNotFoundError:
            return default


def write(filename, messages):
    with open(os.path.join(path, filename), "w", encoding="utf-8") as file:
        file.write(json.dumps(messages, ensure_ascii=False, indent=2))


def read_snippet(name):
    with open(os.path.join(path, 'snippets', name + '.py'), "r", encoding="utf-8") as file:
        return file.read()


def write_snippet(name, data):
    with open(os.path.join(path, 'snippets', name + '.py'), "w", encoding="utf-8") as file:
        file.write(data)


def wrap_body(body):
    return '<html><style>div {outline: 1px solid black}</style>'+body+'</body></html>'


def snippet_use(name, *args):
    data = {"args": args}
    try:
        exec(read_snippet(name), globals(), data)
        return data.get("r")
    except Exception:
        raise SnippetError(name, traceback.format_exc())


app = Flask(__name__)
su = snippet_use


@app.route("/")
def index():
    return "Hello from flask!"


@app.route("/run")
def exec_input():
    return '<form action="runner" method="POST"><input hidden name="back" value="'+request.args.get("back", "run")+'"><textarea name="code">'+request.args.get("code", "")+'</textarea><input type="submit" value="run"></form>'


@app.route("/runner", methods=["POST"])
def exec_run():
    data = {}
    exec(request.form.get("code"), globals(), data)
    r = str(data.get("r"))
    return '<a href="'+request.form['back']+'">back</a><br>result:<br>'+r


@app.route('/code')
def get_code():
    with open(__file__, 'r', encoding='utf-8') as r:
        return r.read().replace('    ', '&nbsp;&nbsp;&nbsp;&nbsp;').replace('<', '&lt;').replace('\n', '<br>')


@app.route("/snippets")
def snippet_list():
    snippets = os.listdir(os.path.join(path, 'snippets'))
    body = ""
    for name in snippets:
        name = name[:-3]
        body += f'<a href="snippet_edit?{urlencode({"name": name})}">{name}</a><br>'
    body += '<form action="snippet_create" method="post"><input name="name"><input type="submit" value="add snippet"></form>'
    return body


@app.route("/snippet_edit")
def snippet_show():
    return su("snippet_edit")


@app.route("/snippet_create", methods=["POST"])
def snippet_create():
    write_snippet(request.form.get("name"), '')
    return redirect("/snippets")


@app.route("/snippet_save", methods=["POST"])
def snippet_append():
    return su("snippet_save")


@app.errorhandler(Exception)
def errorhandler(e):
    return traceback.format_exc().replace("\n", "<br>")


@app.errorhandler(SnippetError)
def snippet_error(e):
    return f'snippet "{e.name}"<br>{e.traceback}'.replace("\n", "<br>")


# Попробовать загрузить сниппет с роутами.
# В случае неудачи -- не падать, потому что
# единственный интерфейс к изменению кода сайта -- сам сайт.
try:
    su("routes")
except Exception:
    pass
