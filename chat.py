from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from nlp_utils import load_faq, find_best_answer

app = Flask(__name__, template_folder="templates")
CORS(app) 

faq_data = load_faq()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")  

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
