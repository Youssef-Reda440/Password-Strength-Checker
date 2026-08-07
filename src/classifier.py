STRENGTH_CATEGORIES = (
    ("Very Weak", 0, 30),
    ("Weak", 30, 50),
    ("Medium", 50, 70),
    ("Strong", 70, 90),
    ("Very Strong", 90, 101),
)

def classify_strength(score: int) -> str:
    """
    Classify the password based on its score.
    """

    for category, minimum, maximum in STRENGTH_CATEGORIES:
        if minimum <= score < maximum:
            return category

    raise ValueError("Invalid password score.")