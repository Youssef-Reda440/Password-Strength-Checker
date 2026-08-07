MAX_PASSWORD_LENGTH = 128

def get_password() -> str:
    """
    Prompt the user until a valid password is entered.
    """

    while True:
        password = input("Enter your password: ")
        is_valid, error = _validate_input(password)
        if is_valid:
            return password
        
        print(f"[!] {error}\n")
        
def _validate_input(password: str) -> tuple[bool, str | None]:
    """
    Validate the user's password.
    Args:
        password: The password entered by the user.
    Returns:
        A tuple containing:
            - True and None if the password is valid.
            - False and an error message otherwise.
    """

    if not password:
        return False, "Password cannot be empty."
    
    if password.isspace():
        return False, "Password cannot contain only whitespace."

    if len(password) > MAX_PASSWORD_LENGTH:
        return False, f"Password cannot exceed {MAX_PASSWORD_LENGTH} characters."
     
    return True, None