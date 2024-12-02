import random
from termcolor import cprint
import json

QUESTION = "question"
OPTIONS = "options"
ANSWER = "answer"


def ask_subject():
    subjects_dct = {
        "gk": "GK",
        "sci": "SCIENCE",
        "hist": "HISTORY",
        "geo": "GEOGRAPHY"
    }

    user_choice = input("Choose your subject ? (gk/sci/hist/geo): ").lower()
    if user_choice not in subjects_dct:
        return False
    return subjects_dct[user_choice].lower()


def get_questions():
    return [
        {
            QUESTION: "What is the capital of France ?",
            OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            ANSWER: "C"
        },
        {
            QUESTION: "Which planet is known as the red planet?",
            OPTIONS: ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            ANSWER: "B"
        },
        {
            QUESTION: "What is the capital of India ?",
            OPTIONS: ["A. Delhi", "B. Paris", "C. Kanpur", "D. Rome"],
            ANSWER: "A"
        },
        {
            QUESTION: "What is the largest ocean on Earth ?",
            OPTIONS: ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
            ANSWER: "D"
        },
    ]


def load_questions(subject):
    with open("sample_questions.json") as f:
        response = json.load(f)
        return response[subject]


def ask_question(question_number, question_dct):
    print(f"Question {question_number}: {question_dct[QUESTION]} ")

    for option in question_dct[OPTIONS]:
        print(option)

    user_answer = input("Enter Your answer:").upper().strip()
    return user_answer


def check_answer(question_dct, user_answer):
    return question_dct[ANSWER] == user_answer


def quiz():
    user_subject = ask_subject()

    if user_subject:
        score = 0

        sample_questions = load_questions(user_subject)
        random.shuffle(sample_questions)
        total_marks = len(sample_questions)

        for key, value in enumerate(sample_questions, 1):
            user_answer = ask_question(key, value)

            if check_answer(value, user_answer):
                cprint("Correct!", "green")
                score += 1
            else:
                cprint(f"Wrong answer And Correct Answer is {value[ANSWER]}", "red")
                # score -= 1

            print()

        print(f"Your Final score is: {score}/{total_marks}")

    else:
        print("Invalid Choice")


def main():
    quiz()


# sample_question
if __name__ == "__main__":
    main()

