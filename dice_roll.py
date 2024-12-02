from random import randint


def dice_roll():
    count = 0
    while True:
        user_input = input("Roll the dice? (y/n): ").lower()
        if user_input == "n":
            if not count:
                print("See You Next time.")
                quit()

            if count:
                print(f"You have rolled dice {count} times.")
            elif count == 1:
                print(f"You have rolled dice {count} time.")
            print("Thanks For Playing!")
            quit()
        elif user_input == "y":
            user_result = []
            user_choice = int(input("How many dice you want to roll:: "))
            count += 1
            for i in range(user_choice):
                dice_1 = randint(1, 6)
                user_result.append(dice_1)

            if user_result:
                print(tuple(user_result))
        else:
            print("Invalid input!")


if __name__ == "__main__":
    dice_roll()
