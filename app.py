from flask import Flask, render_template
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
    return render_template("index.html", cves=cves)

@app.route("/api/cves")
def api_cves():
    return load_cves()

if __name__ == "__main__":
    app.run(debug=True)
