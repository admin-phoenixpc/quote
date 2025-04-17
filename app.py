from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__, template_folder="templates")
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

        def extract_build(prefix):
            return {
                "CPU": form.get(f"{prefix}_cpu"),
                "GPU": form.get(f"{prefix}_gpu"),
                "RAM": form.get(f"{prefix}_ram"),
                "SSD": form.get(f"{prefix}_ssd"),
                "Cooler": form.get(f"{prefix}_cooler"),
                "PSU": form.get(f"{prefix}_psu"),
                "Case": form.get(f"{prefix}_case"),
                "Note": form.get(f"{prefix}_note"),
                "TotalPrice": sum(int(form.get(f"{prefix}_{part}_price", 0)) for part in ["cpu", "gpu", "ram", "ssd", "cooler", "psu", "case"]),
                "TotalWatt": sum(int(form.get(f"{prefix}_{part}_watt", 0)) for part in ["cpu", "gpu", "ram", "ssd", "cooler"])
            }

        builds[budget] = {
            "Intel": extract_build("intel"),
            "AMD": extract_build("amd")
        }

        save_data(builds)
        return jsonify({"status": "saved"})

    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True)
