from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify(status="UP")

@app.route("/api/message")
def message():
    return jsonify(message="Hello from Backend via RKE2")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
