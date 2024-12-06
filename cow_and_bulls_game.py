import random

# HERE we can get some information about this project.
"""
Project Description :   
bulls -> It means right digit right spot.
cows  -> It means right digit but wrong spot.
"""

level_dct = {
    "E": {"level": "easy", "secret_length": 4, "attempts": 4},
    "M": {"level": "medium", "secret_length": 6, "attempts": 3},
    "H": {"level": "hard", "secret_length": 8, "attempts": 2},
}


def generate_secret(secret_length: int):
    digit_lst = list(range(10))
    random.shuffle(digit_lst)
    unique_digits = "".join([str(i) for i in digit_lst[:secret_length]])
    return unique_digits


def cow_and_bull(secret: str, guess: str, secret_length: int):
    bulls = sum([1 for i in range(secret_length) if guess[i] == secret[i]])
    cows = sum([1 for i in range(secret_length) if guess[i] in secret]) - bulls

    return cows, bulls


def main():
    # generate a secret number.
    while True:
        select_level = input("Please select difficulty levels(E/M/H): ").upper()
        print(f"You have selected {level_dct[select_level]["level"]} level.")
        print(f"And You have {level_dct[select_level]["attempts"]} attempts to guess.")

        if select_level not in level_dct:
            print("Please enter a valid level name.")
            continue

        secret_length = level_dct[select_level]["secret_length"]
        user_attempts = level_dct[select_level]["attempts"]

        while user_attempts > 0:
            computer_secret = generate_secret(secret_length)

            print(f"I have generated {secret_length}-digit number with unique digits. Please Try to guess it.")

            user_guess = input("Enter Your guess: ")

            if len(user_guess) == secret_length and user_guess.isdigit() and len(set(user_guess)) == secret_length:
                cows, bulls = cow_and_bull(computer_secret, user_guess, secret_length)

                print(f"{cows} cows and {bulls} bulls.")

                if bulls == secret_length:
                    print("Congratulations You guess exact number.")
                    quit()

            else:
                print(f"Please enter a {secret_length}-digit unique number.")

            # decrease user attempts
            user_attempts -= 1
        else:
            print("Thanks for Playing!")
            quit()


if __name__ == "__main__":
    main()

