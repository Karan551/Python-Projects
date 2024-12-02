import random
import textwrap

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emoji_dct = {ROCK: "🪨", PAPER: "📰", SCISSORS: "✂"}
result_status = {"user": 0, "computer": 0, "draw": 0}
all_choices = tuple(emoji_dct.keys())


def get_user_choice():
    while True:
        user_choice = input("Rock , Paper or Scissor? (r/p/s): ").lower()

        if user_choice in all_choices:
            return user_choice
        else:
            print("Invalid choice")


def display_choices(user_choice, computer_choice):
    print(f"You choose {emoji_dct[user_choice]}")
    print(f"Computer choose {emoji_dct[computer_choice]}")


def display_result():
    print("*" * 50)
    long_text = f"You won {result_status["user"]} times And Computer won {result_status["computer"]} times\
                          And Draw game {result_status["draw"]} times."

    print(textwrap.fill(long_text, width=50))
    print("Thanks for playing.")


def determine_winner(user_choice, computer_choice, total_round):
    if (
            user_choice == ROCK and computer_choice == SCISSORS or
            user_choice == SCISSORS and computer_choice == PAPER or
            user_choice == PAPER and computer_choice == ROCK
    ):
        print("You won!")
        result_status["user"] += 1
    elif user_choice == computer_choice:
        print("Tie Game!")
        result_status["draw"] += 1
    else:
        print("Computer won!")
        result_status["computer"] += 1
    if total_round != 3:
        print(f"{3 - total_round} attempts left.")


def play_game():
    total_round = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(all_choices)

        display_choices(user_choice, computer_choice)

        total_round += 1

        determine_winner(user_choice, computer_choice, total_round)

        if total_round == 3:
            print("Game over!")
            display_result()
            quit()

        should_continue = input("Do you want to play again (y/n) ? ").lower()
        if should_continue == "y":
            continue
        elif should_continue == "n":
            display_result()
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    play_game()
