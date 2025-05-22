import re
import tkinter as tk
from tkinter import messagebox

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

def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    result = check_password_strength(password)
    result_label.config(text=f"Password Strength: {result}")

# Set up the window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x150")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*")  # Hide password characters
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=on_check)
check_button.pack(pady=5)

result_label = tk.Label(root, text="Password Strength: ")
result_label.pack(pady=5)

# Run the app
root.mainloop()
