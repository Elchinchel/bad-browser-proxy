r = args[0].replace("<", "&lt;").replace(">", "&gt;").replace("]", "&#093;").replace("\n", "<br>")
r = r.replace("&lt;"*2, "<").replace("&gt;"*2, ">")