import random
import re

FILE = "./my_files/words.txt"


def read_words():
    """
    This function is used to read words from a file.
    :return: list
    :rtype: list
    """
    try:
        with open(FILE, "r+") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print("File doesn't exists.")
        return []


def display_word(secret_word: str, guessed_letters: list):
    """
    This function is used to display words and guessed letters that is entered by an user.

    :param secret_word:str

    :param guessed_letters:list

    :return:None
    :rtype:
    """

    word_to_display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += "-"

    print(word_to_display)


def get_guess(guessed_letters):
    """
    This function will take input from user and return that input.

    :param guessed_letters: list
    :type guessed_letters: list
    :return:string
    :rtype:str

    """
    while True:
        user_guess = input("Enter a letter: ").lower()
        if len(user_guess) != 1:
            print("Enter only one letter.")
        elif not re.search(r"[a-z]", user_guess):
            print("Enter only letters from a to z.")
        elif user_guess in guessed_letters:
            print("You already guess this letter.")
        else:
            return user_guess


def is_word_guessed(secret_word: str, guessed_letters: list):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def main():
    words = read_words()
    if not words:
        print("No words loaded!")
        return

    secret_word = random.choice(words)
    attempts = 6
    guessed_letters = []

    while attempts > 0:

        display_word(secret_word, guessed_letters)

        guess = get_guess(guessed_letters)

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good Guess.")

            if is_word_guessed(secret_word, guessed_letters):
                print("Congratulations! You guessed the word.")
                break
        else:
            print("Wrong guess.")
            attempts -= 1

    if attempts == 0:
        print(f"Game over! The Secret word is {secret_word}")
        return


if __name__ == "__main__":
    main()
