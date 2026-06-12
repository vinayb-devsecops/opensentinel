def classify(cvss_score):

    if cvss_score >= 9.0:
        return "Critical"

    if cvss_score >= 7.0:
        return "High"

    if cvss_score >= 4.0:
        return "Medium"

    return "Low"


def severity_counts(scores):

    result = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for score in scores:
        result[classify(score)] += 1

    return result


print(severity_counts([9.8, 9.1, 8.0, 7.5, 5.2, 3.1]))
