def get_recommendation(score):

    if score >= 80:
        return "🟢 Strong Match"

    elif score >= 60:
        return "🟡 Moderate Match"

    else:
        return "🔴 Not Recommended"


def hiring_probability(score):

    if score >= 80:
        return 90

    elif score >= 60:
        return 75

    elif score >= 40:
        return 50

    else:
        return 20