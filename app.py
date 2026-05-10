from flask import Flask, request, jsonify
import os

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return "Flask API is running on Replit"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": users})

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "added", "users": users})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)