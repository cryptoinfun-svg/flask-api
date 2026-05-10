from flask import Flask, request
import os

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return """
    <h2>Name & Age App</h2>

    <form action="/add" method="post">
        Name: <input name="name"><br><br>
        Age: <input name="age"><br><br>
        <button type="submit">Submit</button>
    </form>

    <hr>

    <h3>Users</h3>
    <ul>
        """ + "".join([f"<li>{u['name']} - {u['age']}</li>" for u in users]) + """
    </ul>
    """

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]

    users.append({"name": name, "age": age})

    return home()

@app.route("/users")
def api():
    return {"users": users}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)