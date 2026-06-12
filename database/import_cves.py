import json
import sqlite3

DB_FILE = "database/opensentinel.db"

conn = sqlite3.connect(DB_FILE)

with open("reports/cve_report.json", "r") as f:
    cves = json.load(f)

for cve in cves:

    conn.execute("""
        INSERT OR REPLACE INTO cves
        (
            cve_id,
            source,
            published,
            status,
            cvss_score
        )
        VALUES (?, ?, ?, ?, ?)
    """,
    (
        cve.get("cve_id"),
        cve.get("source"),
        cve.get("published"),
        cve.get("status"),
        cve.get("cvss_score")
    ))

conn.commit()
conn.close()

print(f"Imported {len(cves)} CVEs")
