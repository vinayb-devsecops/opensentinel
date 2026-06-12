import json
import requests

URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=10"

response = requests.get(URL, timeout=30)

if response.status_code != 200:
    print(f"Failed: {response.status_code}")
    exit(1)

data = response.json()

summary = []

for item in data["vulnerabilities"]:
    cve = item["cve"]

    summary.append({
        "cve_id": cve["id"],
        "source": cve["sourceIdentifier"],
        "published": cve["published"]
    })

with open("reports/cve_report.json", "w") as f:
    json.dump(summary, f, indent=2)

print(f"Generated report with {len(summary)} CVEs")
