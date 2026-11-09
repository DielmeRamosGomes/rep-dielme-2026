# pip install flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "mensagem": "Olá! Minha aplicação Python está rodando no Docker! 🐍🐳",
        "status": "sucesso"
    })

if __name__ == '__main__':
    # host='0.0.0.0' é fundamental para aceitar conexões vindas de fora do container
    app.run(host='0.0.0.0', port=5000)