import string
import random


def main():
    password = ""
    all_chars = string.ascii_lowercase
    try:
        password_length = int(input("Enter password length: "))
        if password_length < 0:
            print("Please enter a positive number.")
            quit()

    except ValueError:
        raise ValueError

    if password_length < 4:
        print("Please generate a password at least 4 digits.")
        quit()

    include_upper_letter = input("Include uppercase letters? (y/n): ").lower() == "y"
    include_number = input("Include numbers? (y/n): ").lower() == "y"
    include_special_char = input("Include special characters? (y/n): ").lower() == "y"

    if include_upper_letter:
        all_chars += string.ascii_uppercase
    if include_number:
        all_chars += string.digits
    if include_special_char:
        all_chars += string.punctuation

    for _ in range(password_length):
        index = random.randrange(1, len(all_chars))
        password += all_chars[index]

    return password


if __name__ == "__main__":
    try:
        gen_password = main()
        print("And Generated password is::", gen_password)
    except Exception as e:
        print(e)
