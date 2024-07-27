import re

def check_password(password):
    if len(password) < 8:
        return "Password too short"
    if not re.search(r"[A-Z]", password):
        return "Must contain an uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Must contain a lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Must contain a digit"
    if not re.search(r"[!@#$%^&*(),.?:{}|<>]", password):
        return "Must contain a special character"
    return "Password is strong"

password = input("Enter your password: ")
print(check_password(password))
