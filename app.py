from flask import Flask
from models.db import init_db
from routes.users import users_bp

app = Flask(__name__)

init_db()

app.register_blueprint(users_bp)

@app.route("/")
def home():
    return "Backend API running"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)