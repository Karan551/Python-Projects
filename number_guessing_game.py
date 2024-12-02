from random import randrange


def guess_number():
    count = 0
    max_attempt = 5
    while True:
        try:

            start_number = int(input("Enter a starting number range where you want to start guess:: "))
            stop_number = int(input("Enter a ending number range where you want to guess:: "))

            if start_number > stop_number:
                start_number, stop_number = stop_number, start_number

            user_input = int(input(f"Guess the number (between {start_number} and {stop_number}):: "))
            random_number = randrange(start_number, stop_number)
            count += 1
            if max_attempt == count:
                print("Game Over!")
                print(f"And the correct number is :: {random_number}")
                quit()
            if user_input > random_number:
                print("Too high Try again!")
                print(f"You have remain {5 - count} attempts.")
            elif user_input < random_number:
                print("Too Low Try again!")
                print(f"You have remain {5 - count} attempts.")
            else:
                print(f"Congratulations You guessed the number {count} attempts.")
                quit()

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    guess_number()
