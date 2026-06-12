import json
import csv

with open("reports/cve_report.json", "r") as f:
    data = json.load(f)

with open("exports/cve_export.csv", "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "cve_id",
        "source",
        "published",
        "status"
    ])

    for cve in data:

        writer.writerow([
            cve.get("cve_id"),
            cve.get("source"),
            cve.get("published"),
            cve.get("status")
        ])

print("CSV export completed")
