import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Route GET simple
@app.route('/')
def home():
    return "Hello World from Render Etudiant!"

# Route GET JSON
@app.route('/api/data')
def data():
    return jsonify({"message": "Exemple de JSON via un PaaS"})

# 🔵 TP3 : Route POST
@app.route('/api/postdata', methods=['POST'])
def post_data():
    # Vérifie que le client envoie bien du JSON
    if not request.is_json:
        return jsonify({"error": "Le contenu doit être au format JSON"}), 400

    data = request.get_json()

    # Vérifie que des données existent
    if not data:
        return jsonify({"error": "Aucune donnée JSON reçue"}), 400

    # Réponse correcte
    return jsonify({"received": data}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
