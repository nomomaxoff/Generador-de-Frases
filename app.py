from flask import Flask, jsonify, render_template
import requests
import random

app = Flask(__name__)

API_KEY = "9CBtnQEJiPw4XjWC9H3dXuIEXbTvrxwJeLeStmxI"

@app.route("/") #Define root como endpoint. 
def home():
    return render_template("index.html")

@app.route("/frase-aleatoria")
def get_quote():
    url = "https://api.api-ninjas.com/v2/quotes?categories=success,wisdom&limit=10"
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # lista de frases
        selected = random.choice(data)  # frase aleatoria
        return jsonify({
            "frase": selected["quote"],
            "autor": selected["author"]
        })
    else:
        return jsonify({
            "frase": "Error al obtener la frase",
            "autor": ""
        }), 500

if __name__ == "__main__":
    app.run(debug=True)