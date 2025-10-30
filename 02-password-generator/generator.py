"""
Password Generator
Generates secure random passwords based on user preferences.
Uses for loops to build passwords and validate criteria.
"""
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    password = []
    
    if use_upper:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        password.append(random.choice(string.digits))
    if use_symbols:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))
    
    # Fill remaining length
    for _ in range(length - len(password)):
        password.append(random.choice(characters))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

def get_yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'")

def main():
    print("🔐 Password Generator\n")
    
    while True:
        # Get password length
        while True:
            try:
                length = int(input("Password length (8-128): "))
                if 8 <= length <= 128:
                    break
                print("Length must be between 8 and 128")
            except ValueError:
                print("Please enter a valid number")
        
        # Get character preferences
        use_upper = get_yes_no("Include uppercase letters? (y/n): ")
        use_lower = get_yes_no("Include lowercase letters? (y/n): ")
        use_digits = get_yes_no("Include digits? (y/n): ")
        use_symbols = get_yes_no("Include symbols? (y/n): ")
        
        if not any([use_upper, use_lower, use_digits, use_symbols]):
            print("❌ You must select at least one character type!\n")
            continue
        
        # Generate multiple passwords
        print("\n✨ Generated Passwords:")
        for i in range(5):
            pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            print(f"{i+1}. {pwd}")
        
        if not get_yes_no("\nGenerate more passwords? (y/n): "):
            break
    
    print("\nThanks for using Password Generator! 👋")

if __name__ == "__main__":
    main()