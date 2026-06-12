import requests

URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=5"

response = requests.get(URL, timeout=30)

if response.status_code != 200:
    print(f"Failed: {response.status_code}")
    exit(1)

data = response.json()

print(f"Total CVEs Returned: {len(data['vulnerabilities'])}")

for cve in data["vulnerabilities"]:
    print(cve["cve"]["id"])
