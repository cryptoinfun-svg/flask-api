from flask import Blueprint, request, jsonify
import sqlite3
from config import DATABASE

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["GET"])
def get_users():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute("SELECT id, name, age FROM users")
    rows = cur.fetchall()

    conn.close()

    return jsonify([
        {"id": r[0], "name": r[1], "age": r[2]}
        for r in rows
    ])