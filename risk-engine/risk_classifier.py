def classify(cvss_score):

    if cvss_score >= 9.0:
        return "Critical"

    if cvss_score >= 7.0:
        return "High"

    if cvss_score >= 4.0:
        return "Medium"

    return "Low"


test_scores = [9.8, 8.1, 6.5, 3.2]

for score in test_scores:
    print(f"CVSS: {score} -> {classify(score)}")
