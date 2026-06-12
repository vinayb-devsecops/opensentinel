import json

with open("reports/cve_report.json", "r") as f:
    data = json.load(f)

print("OpenSentinel Dashboard")
print("======================")
print(f"Total CVEs: {len(data)}")

for cve in data[:5]:
    print(f"- {cve['cve_id']}")
