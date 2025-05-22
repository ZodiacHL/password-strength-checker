import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]
    score = errors.count(False)

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength

# --- Run it interactively ---
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"Your password is: {result}")
