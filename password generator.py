import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validate_input(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a valid number.")

def main():
    try:
        length = validate_input("Enter the length of the password: ")
        use_letters = input("Include letters? (yes/no): ").lower().startswith('y')
        use_numbers = input("Include numbers? (yes/no): ").lower().startswith('y')
        use_symbols = input("Include symbols? (yes/no): ").lower().startswith('y')
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Error: Length must be an integer.")

if __name__ == "__main__":
    main()


