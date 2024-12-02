import os
from work_file import read_data_to_file, write_data_to_file, delete_data_to_file
from pathlib import Path

# TODO: write a data into a file.

FILE = "./my_files/task.txt"


# def write_data_to_file(data):
#     with open("./my_files/task.txt", "a+") as f:
#         f.write(data)


# def read_data_to_file():
#     with open("./my_files/task.txt", "r+") as f:
#         return f.readlines()


def display_menu():
    long_text = """Todo List Menu:
    1. View Tasks 
    2. Add a Task
    3. Remove a Task
    4. View Complete Task
    5. Exit
    """
    print(long_text)


def get_choice():
    choices = ("1", "2", "3", "4", "5")
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice not in choices:
            print("Please enter a valid choice.")
            continue
        return user_choice


def display_tasks(lst, label="add"):
    if lst:
        if label != "add":
            print("Completed Task is:")

        for task in lst:
            print(f" {task}", end="")
        print()
    else:
        print(f"Please {label} at least one task to show.")


def add_task(lst, task):
    lst.append(task)
    return


def remove_task(lst: list, completed_task_lst):
    display_tasks(lst)
    while True:
        try:
            task_index = int(input("Which task you want to remove: "))
            if 0 < task_index <= len(lst):
                completed_task = lst.pop(task_index - 1)
                delete_data_to_file(FILE, task_index)
                completed_task_lst.append(completed_task)
                return
            else:
                print("Please enter a valid task number.")
                continue
        except ValueError:
            raise ValueError


def main():
    lst = []
    completed_task_lst = []
    # load initial stage of file
    task = read_data_to_file(FILE)
    count = len(task)
    while True:
        display_menu()
        user_choice = get_choice()

        if user_choice == "1":
            # display_tasks(lst)
            task = read_data_to_file(FILE)
            display_tasks(task)

        elif user_choice == "2":
            task = input("Enter a new Task: ").title().strip()
            count += 1

            task = f"{count}. " + task + "\n"

            write_data_to_file(FILE, task)

        elif user_choice == "3":
            # TODO fix this code
            prev_data = read_data_to_file(FILE)

            remove_task(prev_data, completed_task_lst)


        elif user_choice == "4":
            display_tasks(completed_task_lst, label="Complete")

        elif user_choice == "5":
            print("Thanks.\n")
            quit()
        else:
            print("Invalid choice.")
            continue


if __name__ == "__main__":
    main()
    pass
