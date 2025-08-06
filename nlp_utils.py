# nlp_utils.py
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_faq():
    """Charge le fichier JSON et retourne la liste des questions-réponses"""
    with open("faq.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["faq"]  # <--- Important : accéder à la clé "faq"


def find_best_answer(user_question, faq_data, threshold=0.3):
    """Renvoie la meilleure réponse trouvée via similarité cosinus"""
    questions = [item["question"] for item in faq_data]
    answers = [item["answer"] for item in faq_data]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions + [user_question])
    
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    best_match_idx = cosine_similarities.argmax()
    best_score = cosine_similarities[best_match_idx]

    if best_score < threshold:
        return "Je ne suis pas sûr de comprendre ta question. Peux-tu la reformuler ?"

    return answers[best_match_idx]
