from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():

    try:
        with open("reports/cve_report.json","r") as f:
            cves = json.load(f)
    except:
        cves = []

    return render_template("index.html", cves=cves)

if __name__ == "__main__":
    app.run(debug=True)
