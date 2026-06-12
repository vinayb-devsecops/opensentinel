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

    for cve in cves:

        score = cve.get("cvss_score")

        if score is None:
            continue

        if score >= 9.0:
            stats["Critical"] += 1
        elif score >= 7.0:
            stats["High"] += 1
        elif score >= 4.0:
            stats["Medium"] += 1
        else:
            stats["Low"] += 1

    return render_template(
        "index.html",
        cves=cves,
        stats=stats,
        search=search
    )

@app.route("/api/cves")
def api_cves():
    return load_cves()

@app.route("/api/cves/<cve_id>")
def get_cve(cve_id):

    for cve in load_cves():
        if cve.get("cve_id") == cve_id:
            return cve

    return {"error": "CVE not found"}, 404

@app.route("/api/stats")
def api_stats():

    cves = load_cves()

    return {
        "total": len(cves)
    }

if __name__ == "__main__":
    app.run(debug=True)
