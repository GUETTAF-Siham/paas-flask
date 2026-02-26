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

    # Si JSON (Postman)
    if request.is_json:
        data = request.get_json()
        return jsonify({"received": data}), 200

    # Si formulaire HTML (navigateur)
    elif request.form:
        data = {
            "nom": request.form.get("nom"),
            "classe": request.form.get("classe")
        }
        return jsonify({"received": data}), 200

    else:
        return jsonify({"error": "Aucune donnée reçue"}), 400

@app.route('/form')
def form():
    return '''
    <h2>Envoyer des données</h2>
    <form action="/api/postdata" method="post">
        <input type="text" name="nom" placeholder="Nom"><br><br>
        <input type="text" name="classe" placeholder="Classe"><br><br>
        <button type="submit">Envoyer</button>
    </form>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
