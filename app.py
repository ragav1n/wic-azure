from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

jokes = [
    {"setup": "Why don’t scientists trust atoms?", "punchline": "Because they make up everything!"},
    {"setup": "Why did the math book look sad?", "punchline": "Because it had too many problems."},
    {"setup": "Why can’t your nose be 12 inches long?", "punchline": "Because then it would be a foot!"},
    {"setup": "Why was the computer cold?", "punchline": "Because it left its Windows open."},
    {"setup": "Why did the scarecrow win an award?", "punchline": "Because he was outstanding in his field!"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/joke")
def get_joke():
    joke = random.choice(jokes)
    return jsonify(joke)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

