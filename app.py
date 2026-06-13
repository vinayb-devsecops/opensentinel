from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "opensentinel-dev-key"

DB_FILE = "database/opensentinel.db"

def load_cves():

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT *
        FROM cves
        ORDER BY cve_id
    """).fetchall()

    conn.close()

    return [dict(row) for row in rows]



@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        if (
            request.form.get("username") == "admin"
            and
            request.form.get("password") == "opensentinel"
        ):
            session["user"] = "admin"
            return redirect("/")

    return render_template("login.html")

@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

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



@app.route("/cve/<cve_id>")
def cve_detail(cve_id):

    for cve in load_cves():
        if cve["cve_id"] == cve_id:
            return render_template(
                "cve_detail.html",
                cve=cve
            )

    return {"error": "Not Found"}, 404



from flask import send_file

@app.route("/download/csv")
def download_csv():
    return send_file(
        "exports/cve_export.csv",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)

from charts.stats import get_summary

@app.route("/api/analytics")
def api_analytics():
    return get_summary()
