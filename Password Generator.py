import random
import string


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
    # print(str(use_uppercase))

    # use_lowercase = input("Lower Case: YES / NO? ").lower() == 'y'
    use_lowercase = True
    # print(str(use_lowercase))

    # use_numbers = input("Numbers: YES / NO? ").lower() == 'y'
    use_numbers = True
    # print(str(use_numbers))

    # use_special_chars = input("Special Characters: YES / NO? ").lower() == 'y'
    use_special_chars = True
    # print(str(use_special_chars))

    # Generates the password
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    print("\nGenerated Password:\n" + password)

    password = input("\nPress Enter to exit ")
    while password != "":
        if password != "":
            print("You didn't press Enter. ")

        password = input("\nPress Enter to exit ")


main()
