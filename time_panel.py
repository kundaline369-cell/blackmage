from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

HTML = """
<h2>Painel BlackMage</h2>

<form method="post">
<button name="acao" value="status">Status</button>
<button name="acao" value="scan">Scan</button>
<button name="acao" value="ping">Ping</button>
</form>

<pre>{{resposta}}</pre>
"""

# ------------------------
# ROTA WEB
# ------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""

    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "status":
            resposta = "Sistema online"
        elif acao == "scan":
            resposta = "Scan executado"
        elif acao == "ping":
            resposta = "pong"

    return render_template_string(HTML, resposta=resposta)

# ------------------------
# API REAL
# ------------------------

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "status": "online",
        "sistema": "BlackMage"
    })

@app.route("/api/connect", methods=["GET"])
def connect():
    return jsonify({
        "msg": "conectado ao núcleo BlackMage"
    })

@app.route("/api/command", methods=["POST"])
def command():
    data = request.json
    cmd = data.get("cmd")

    if cmd == "scan":
        return jsonify({"resultado": "scan completo"})
    elif cmd == "ping":
        return jsonify({"resultado": "pong"})
    elif cmd == "status":
        return jsonify({"resultado": "ativo"})
    else:
        return jsonify({"erro": "comando inválido"})

# ------------------------
# START
# ------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
