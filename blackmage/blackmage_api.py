from flask import Flask, request, jsonify, render_template_string
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENAI_API_KEY")

HTML = """
<h1 style="color:red;">🩸 BlackMage Web</h1>
<input id="prompt" placeholder="Digite...">
<button onclick="send()">Enviar</button>
<pre id="res"></pre>

<script>
async function send(){
 let p = document.getElementById("prompt").value;
 let r = await fetch("/query", {
   method:"POST",
   headers:{"Content-Type":"application/json"},
   body: JSON.stringify({prompt:p})
 });
 let d = await r.json();
 document.getElementById("res").innerText = d.resposta;
}
</script>
"""

@app.route("/")
def home():
    return HTML

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    prompt = data.get("prompt","")

    try:
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model":"gpt-4o-mini",
                "messages":[
                    {"role":"system","content":"Você é o BlackMage, direto e estratégico"},
                    {"role":"user","content":prompt}
                ]
            }
        )

        resposta = r.json()["choices"][0]["message"]["content"]

    except Exception as e:
        resposta = f"Erro IA: {e}"

    return jsonify({"resposta":resposta})

app.run(host="0.0.0.0", port=8000)
