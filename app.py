from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open("cbc_content.json", "r") as file:
    cbc_content = json.load(file)

@app.route("/")
def home():
    return "AI Tutor Backend Running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    subject = data.get("subject")
    grade = data.get("grade")
    topic = data.get("topic")
    try:
        lessons = cbc_content[subject][grade][topic]
        return jsonify({"status": "success", "lessons": lessons})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)