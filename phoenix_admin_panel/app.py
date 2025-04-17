from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__, template_folder=".")

DATA_FILE = "builds.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/builds", methods=["GET", "POST"])
def handle_builds():
    if request.method == "POST":
        form = request.json
        budget = str(form.get("budget"))
        builds = load_data()
        builds[budget] = {"Intel": {}, "AMD": {}}  # Simplified for brevity
        save_data(builds)
        return jsonify({"status": "saved"})

    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True)
