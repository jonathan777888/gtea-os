from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Bienvenue dans GTEA OS",
        "status": "running"
    })


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "Le champ 'text' est obligatoire."
        }), 400

    text = data["text"]

    # Version MVP simple, sans IA pour l’instant
    summary = text[:300] + "..." if len(text) > 300 else text

    key_points = [
        "Comprendre le contenu du document",
        "Identifier les notions importantes",
        "Préparer une révision structurée"
    ]

    revision_questions = [
        "Quel est le sujet principal du document ?",
        "Quelles sont les notions les plus importantes ?",
        "Quels mots-clés faut-il retenir ?",
        "Quels exemples sont donnés ?",
        "Quelles informations pourraient être demandées en devoir ?",
        "Comment résumer ce document en quelques phrases ?",
        "Quelles parties sont difficiles à comprendre ?",
        "Quelles actions faut-il faire après lecture ?",
        "Comment expliquer ce contenu à quelqu’un d’autre ?",
        "Quelles questions poser au formateur ?"
    ]

    return jsonify({
        "summary": summary,
        "key_points": key_points,
        "revision_questions": revision_questions
    })


if __name__ == "__main__":
    app.run(debug=True)
