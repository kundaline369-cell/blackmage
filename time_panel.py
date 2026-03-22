from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<h2>Painel BlackMage</h2>

<form method="post">
<button name="acao" value="teste">Testar</button>
</form>

<pre>{{resposta}}</pre>
"""

@app.route("/", methods=["GET","POST"])
def index():
    resposta = ""
    if request.method == "POST":
        resposta = "funcionando"

    return render_template_string(HTML, resposta=resposta)

app.run(host="0.0.0.0", port=8080)
