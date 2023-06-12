import random
import string
import msvcrt


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    # Prompt the user for the desired password length
    length = int(input("Enter the desired character length for your password: "))

    # Prompt for options
    # use_uppercase = input("Upper Case: YES / NO? ").lower() == 'y'
    use_uppercase = True
    # use_lowercase = input("Lower Case: YES / NO? ").lower() == 'y'
    use_lowercase = True
    # use_numbers = input("Numbers: YES / NO? ").lower() == 'y'
    use_numbers = True
    # use_special_chars = input("Special Characters: YES / NO? ").lower() == 'y'
    use_special_chars = True

    while True:
        # Generates the password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
        print("\nGenerated Password:\n" + password)

        print("\nPress Enter to regenerate password or Esc to exit.")

        key = ord(msvcrt.getch())
        if key == 13:  # Enter key
            continue
        elif key == 27:  # Esc key
            break


main()
