# chat.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_utils import load_faq, find_best_answer

app = Flask(__name__)
CORS(app)  # Autorise les requêtes frontend (HTML local)

# Charger la base FAQ au lancement
faq_data = load_faq()

@app.route('/')
def index():
    return "API de Chatbot FORCE-N en cours d'exécution."

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
