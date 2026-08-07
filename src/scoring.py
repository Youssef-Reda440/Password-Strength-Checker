RULES = {
    "length"         : {"score": 20, "positive": True},
    "uppercase"      : {"score": 10, "positive": True},
    "lowercase"      : {"score": 10, "positive": True},
    "digits"         : {"score": 10, "positive": True},
    "special"        : {"score": 15, "positive": True},
    "common_password": {"score": 20, "positive": False},
    "weak_patterns"  : {"score": 15, "positive": False},
}

def calculate_score(analysis: dict) -> int:
    score = 0
    for rule, config in RULES.items():
        if config["positive"] == analysis[rule]:
            score += config["score"]

    return score