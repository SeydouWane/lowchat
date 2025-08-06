from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from nlp_utils import load_faq, find_best_answer

app = Flask(__name__, template_folder="templates")
CORS(app)  # Autorise les requêtes frontend (HTML local)

# Charger la base FAQ au démarrage
faq_data = load_faq()

# Route GET pour servir l'interface du chatbot
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")  # Ton fichier index.html doit être dans le dossier "templates/"

# Route POST pour interagir avec le bot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Merci de formuler une question."})

    response = find_best_answer(user_message, faq_data)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
