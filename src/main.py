from input_handler import get_password
from analyzer import analyze_password
from scoring import calculate_score
from classifier import classify_strength
from reporter import generate_report

def main():
    """
    Run the password strength checker application.
    """

    password = get_password()
    analysis = analyze_password(password)
    score    = calculate_score(analysis)
    strength = classify_strength(score)
    report   = generate_report(score, strength, analysis)

    display_report(report)

def display_report(report: dict):
    """
    Display the password security report in a readable format.
    """

    print(f"Score: {report['score']}/100") 
    print(f"Strength: {report['strength']}") 

    if report['weaknesses']:
        print("\nDetected Weaknesses:")
        for weakness in report['weaknesses']:
            print(f"- {weakness}")

        print("\nSuggestions:")
        for suggestion in report['suggestions']:
            print(f"- {suggestion}")
    else:
        print("\nExcellent! No weaknesses were detected.")
        print("\nNo security improvements are needed.")
        
if __name__ == "__main__":
    main()