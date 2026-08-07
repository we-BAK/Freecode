import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special symbol (!@#$...).")

    return score, feedback


print("=== 🔐 Password Strength Checker ===")
user_password = input("Enter a password to test: ")

score, tips = check_password_strength(user_password)

if score == 5:
    print("🟢 Strength: STRONG! Great password.")
elif score >= 3:
    print("🟡 Strength: MEDIUM. Could be better.")
else:
    print("🔴 Strength: WEAK. Needs improvement.")

if tips:
    print("\nSuggestions to improve:")
    for tip in tips:
        print(f" - {tip}")