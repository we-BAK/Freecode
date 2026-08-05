import random
import string

def generate_password(length=12):
    # Combine uppercase letters, lowercase letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password


user_length = int(input("Enter password length: "))
new_password = generate_password(user_length)

print(f"🔒 Your generated password: {new_password}")