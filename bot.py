from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Blackmage Bot Online"

@app.route('/responder', methods=['POST'])
def responder():
    msg = request.json.get("msg")

    if "preço" in msg.lower():
        return {"resposta": "leituras a partir de 10 reais"}
    
    if "tarot" in msg.lower():
        return {"resposta": "faço leitura completa com resposta rápida"}
    
    return {"resposta": "me chama no privado que te explico melhor"}

app.run(host='0.0.0.0', port=5000)
