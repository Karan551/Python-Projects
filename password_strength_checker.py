import re


def get_password_strength(password):
    strong = 0
    if len(password) >= 8:
        strong += 1
    if re.search(r"[a-z]", password):
        strong += 1
    if re.search(r"[A-Z]", password):
        strong += 1
    if re.search(r"[0-9]", password):
        strong += 1
    if re.search(r"[@#$%^&*!+=]", password):
        strong += 1

    return strong


def main():
    user_password = input("Enter a password: ")
    strength = get_password_strength(user_password)

    if strength == 5:
        print("Password Strength : Very strong.")
    elif strength == 4:
        print("Password Strength :  Strong.")
    elif strength == 3:
        print("Password Strength :  Medium.")
    elif strength == 2:
        print("Password Strength : Weak.")
    else:
        print("Password Strength : Very weak.")


if __name__ == "__main__":
    main()
