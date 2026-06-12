import requests

URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=5"

response = requests.get(URL, timeout=30)

if response.status_code == 200:
    print("Connected to NVD API")
else:
    print(f"Failed: {response.status_code}")
