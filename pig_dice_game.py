# -------------------------pig_dice_game--------------------------
from random import randint

# Brief intro for this project :
"""
1. Two players play in this game.
2. Allow players to set a custom target score before starting this game.
3. Each player will roll a die. The player who rolls a 1 lose all points.
4. The player requires player to decide to roll again or not.
5. The player who scores 100 points or target points first wins the game.
6. If the player rolls two 6s consecutively, the player's score is reset to 0.
"""


def roll_die():
    return randint(1, 6)


def player_turn(user_name: str):
    score = 0
    prev_roll = 0
    print(f"{user_name.title()}'s turn :-")

    while True:
        result = roll_die()

        if result == 6 and prev_roll == 6:
            print("You rolled two 6s consecutively! Your score is reset to 0.")
            return 0

        # update prev_roll
        prev_roll = result

        print(f"You roll a : {result}")

        if result == 1:
            return 0

        # increment user's score
        score += result

        user_choice = input("Roll again? (y/n): ").lower()

        if user_choice == 'n':
            return score


def get_max_index(lst: list):
    max_value = max(lst)
    return lst.index(max_value)


def get_user_choice(label: str):
    try:
        user_choice = int(input("Enter target score: "))
        if user_choice <= 0 or user_choice == 1:
            print(f"please enter a valid {label} greater than 1.")
            quit()
    except Exception as e:
        print(f"Please enter a valid {label}. ::", type(e).__name__)
        quit()

    return user_choice


def main():
    # get target score
    target_score = get_user_choice(label="target score")

    user_score_lst = [0, 0]
    current_player = 0

    while True:

        print(f"-----Player {current_player + 1}'s turn -----")
        user = input("Enter Your name: ")
        turn_score = player_turn(user)
        user_score_lst[current_player] += turn_score

        print(f"You scored {turn_score} points this turn.")
        for index, score in enumerate(user_score_lst):
            print(f"Player {index + 1}'s score: {score}")

        if user_score_lst[current_player] >= target_score:
            position = get_max_index(user_score_lst) + 1
            print(f"Player {position}. Congrats you won this game.")
            quit()

        current_player = 1 if current_player == 0 else 0


if __name__ == "__main__":
    main()
    pass
