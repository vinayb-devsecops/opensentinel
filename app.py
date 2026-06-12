from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_cves():
    try:
        with open("reports/cve_report.json", "r") as f:
            return json.load(f)
    except:
        return []

@app.route("/")
def home():

    cves = load_cves()

    search = request.args.get("search", "")

    if search:
        cves = [
            cve for cve in cves
            if search.lower() in cve.get("cve_id", "").lower()
        ]

    stats = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    return render_template(
        "index.html",
        cves=cves,
        stats=stats,
        search=search
    )

@app.route("/api/cves")
def api_cves():
    return load_cves()

if __name__ == "__main__":
    app.run(debug=True)
