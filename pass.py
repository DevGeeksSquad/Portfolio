# This script generates a random password of a specified length,
# ensuring it contains at least one lowercase letter,
# one uppercase letter, one digit, and one special character.
# The user can specify the length of the password or exit the program.

import random
import string

# Different character sets for password generation
letters_lower = string.ascii_lowercase  # Lowercase letters (a-z)
letters_upper = string.ascii_uppercase  # Uppercase letters (A-Z)
digits = string.digits  # Digits (0-9)
special_chars = string.punctuation  # Special characters (!@#$%^&*...)

def generate_password(length=12):
    # Ensure the password length is at least 1
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Make sure the password contains at least one of each character type
    password = [
        random.choice(letters_lower),  # Add a lowercase letter
        random.choice(letters_upper),  # Add an uppercase letter
        random.choice(digits),  # Add a digit
        random.choice(special_chars),  # Add a special character
    ]

    # Fill the rest of the password with random characters from all character sets
    all_characters = letters_lower + letters_upper + digits + special_chars
    password += random.choices(all_characters, k=length-4)  # Subtracting 4 because we already added 4 characters

    # Shuffle the password to make sure the characters are randomly arranged
    random.shuffle(password)
    return ''.join(password)  # Convert the list to a string and return the password

while True:
    print("Enter the length of the password (or 'exit' to quit):")
    user_input = input()  # Get user input for password length
    if user_input.lower() == 'exit':  # Allow user to exit the loop
        break
    try:
        length = int(user_input)  # Convert user input to integer
        if length < 1:  # Check if the length is a positive integer
            print("Please enter a positive integer.")
            continue
        password = generate_password(length)  # Generate password with the given length
        print(f"Generated password: {password}")  # Display the generated password
    except ValueError:
        print("Invalid input. Please enter a positive integer.")  # Handle invalid input

