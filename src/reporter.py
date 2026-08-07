REPORT_RULES = {
    "length": {
        "positive": True,
        "weakness": "Password is too short.",
        "suggestion": "Use at least 8 characters.",
    },

    "uppercase": {
        "positive": True,
        "weakness": "Password does not contain an uppercase letter.",
        "suggestion": "Add at least one uppercase letter.",
    },

    "lowercase": {
        "positive": True,
        "weakness": "Password does not contain a lowercase letter.",
        "suggestion": "Add at least one lowercase letter.",
    },

    "digits": {
        "positive": True,
        "weakness": "Password does not contain a digit.",
        "suggestion": "Add at least one digit.",
    },

    "special": {
        "positive": True,
        "weakness": "Password does not contain a special character.",
        "suggestion": "Add at least one special character.",
    },

    "common_password": {
        "positive": False,
        "weakness": "Password is a commonly used password.",
        "suggestion": "Choose a unique password that is not commonly used.",
    },

    "weak_patterns": {
        "positive": False,
        "weakness": "Password contains predictable patterns.",
        "suggestion": "Avoid sequences, repeated characters, and common keyboard patterns.",
    },
}

def generate_report(score: int, strength: str, analysis: dict[str, bool]) -> dict[str, object]:
    """
    Generate a password security report based on the analysis results.
    """

    detected_weaknesses = []
    suggestions = []

    for rule, config in REPORT_RULES.items():
        if config["positive"] != analysis[rule]:
            detected_weaknesses.append(config["weakness"])
            suggestions.append(config["suggestion"])

    return {
        "score": score,
        "strength": strength,
        "weaknesses": detected_weaknesses,
        "suggestions": suggestions,
    }