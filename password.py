import string

def check_password(password):
    """
    Validates a password based on:
    - Minimum length of 8
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one special character
    Returns True if valid, otherwise raises ValueError.
    """

    if not isinstance(password, str):
        raise ValueError("Password must be a string.")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not any(c.islower() for c in password):
        raise ValueError("Password must contain at least one lowercase letter.")

    special_chars = string.punctuation
    if not any(c in special_chars for c in password):
        raise ValueError("Password must contain at least one special character.")

    return True