def classify(cvss_score):

    if cvss_score >= 9.0:
        return "Critical"

    if cvss_score >= 7.0:
        return "High"

    if cvss_score >= 4.0:
        return "Medium"

    return "Low"


print(classify(9.8))
print(classify(7.5))
print(classify(5.0))
print(classify(2.0))
