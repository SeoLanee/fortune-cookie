from flask import Flask, Response, jsonify
from fortune import generate
app = Flask(__name__)

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
