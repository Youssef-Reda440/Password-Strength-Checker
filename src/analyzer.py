from pathlib import Path
import string

WEAK_PATTERNS = (
    # Numeric sequences
    "123",
    "1234",
    "12345",
    "123456",
    "1234567",
    "12345678",
    "0123",
    "9876",
    "987654",

    # Repeated numbers
    "0000",
    "1111",
    "2222",
    "3333",
    "4444",
    "5555",
    "6666",
    "7777",
    "8888",
    "9999",

    # Alphabet sequences
    "abc",
    "abcd",
    "abc123",
    "abcdef",

    # Keyboard patterns
    "qwerty",
    "qwertyui",
    "asdf",
    "asdfgh",
    "zxcv",
    "zxcvb",

    # Common words
    "password",
    "admin",
    "administrator",
    "welcome",
    "login",
    "guest",
    "root",
    "user",
    "default",
    "test",
    "demo",

    # Popular passwords
    "letmein",
    "iloveyou",
    "monkey",
    "dragon",
    "football",
    "baseball",
    "master",
    "shadow",
    "superman",
    "pokemon",

    # Repeated characters
    "aaaa",
    "bbbb",
    "cccc",
    "xxxx",
    "zzzz",

    # Simple patterns
    "pass",
    "admin123",
)

COMMON_PASSWORDS_PATH = (
    Path(__file__).resolve().parent.parent
    / "resources"
    / "10k-common-passwords.txt"
)

MIN_PASSWORD_LENGTH = 8       

def analyze_password(password: str) -> dict:
    analysis = {
        "length": _check_length(password),
        "uppercase": _check_uppercase(password),
        "lowercase": _check_lowercase(password),
        "digits": _check_digits(password),
        "special": _check_special_characters(password),
        "common_password": _check_common_password(password),
        "weak_patterns": _check_weak_patterns(password),
    }

    return analysis

def _check_length(password: str) -> bool:
    """
    Check whether the password meets the minimum length requirement.
    """

    return len(password) >= MIN_PASSWORD_LENGTH

def _check_uppercase(password: str) -> bool:
    """
    Check whether the password contains at least one uppercase letter.
    """

    return any(char.isupper() for char in password)

def _check_lowercase(password: str) -> bool:
    """
    Check whether the password contains at least one lowercase letter.
    """
    
    return any(char.islower() for char in password)

def _check_digits(password: str) -> bool:
    """
    Check whether the password contains at least one digit.
    """
    
    return any(char.isdigit() for char in password)

def _check_special_characters(password: str) -> bool:
    """
    Check whether the password contains at least one special character.
    """

    return any(char in string.punctuation for char in password)

def _check_weak_patterns(password: str) -> bool:
    """
    Check whether the password contains any common weak pattern.
    """

    password = password.lower()
    return any(pattern in password for pattern in WEAK_PATTERNS)

def _check_common_password(password: str) -> bool:
    """
    Check whether the password is a common password.
    """

    return password.lower() in COMMON_PASSWORDS

def _load_common_passwords() -> set[str]:
    """
    Load common passwords from the resource file.
    """

    with COMMON_PASSWORDS_PATH.open("r", encoding="utf-8") as file:
        return {
            line.strip().lower()
            for line in file
            if line.strip()
        }

COMMON_PASSWORDS = _load_common_passwords()