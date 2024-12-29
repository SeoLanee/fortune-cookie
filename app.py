from flask import Flask, Response, jsonify
from flask_cors import CORS
from fortune import generate

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return Response(status=200)

@app.route("/fortune", methods=["POST"])
def fortune_generator():
    phrase = generate()
    return jsonify(
        fortune=phrase
    )

if __name__ == "__main__":
    app.run()
