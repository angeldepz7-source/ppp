from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HEADERS = {"Authorization": "Bearer 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"}

@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.json
    mensaje = data["mensaje"]

    response = requests.post(API_URL, headers=HEADERS, json={
        "inputs": mensaje
    })

    resultado = response.json()

    try:
        respuesta = resultado[0]["generated_text"]
    except:
        respuesta = "Error al responder"

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run()