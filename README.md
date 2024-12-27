# 🚀 Exciting Python Projects I've Developed! 🚀

Over the last few months, I’ve been working on some interesting Python projects that span a variety of applications—from
simple games to useful utilities. These projects have helped me solidify my understanding of programming, especially the
power of **Object-Oriented Programming (OOP)**. Take a look at the list below! 👇

---

## 1. **To-Do List App** 📝

A simple, command-line to-do list to help manage tasks efficiently. Features include adding, editing, and deleting
tasks.

---

## 2. **Work Guessing Game** 🎮

A fun and interactive game where you guess randomly generated workplace-related words!

---

## 3. **Rock Paper Scissors Game** ✋✌️✊

A classic game where you can play against the computer. A great introduction to game development in Python.

---

## 4. **Text Editor with Python** 🖋️

A basic text editor built using Python’s GUI libraries. Easy to use for quick text editing!

---

## 5. **Quiz Game** 📚

A multiple-choice quiz game that tracks your score and challenges your knowledge.

---

## 6. **QR Code Generator** 📲

Generate QR codes for URLs or text using Python. Simple and fun way to create scannable codes.

---

## 7. **Pig Dice Game** 🎲

A dice game where you accumulate points without going bust. Fun, strategic, and interactive!

---

## 8. **Dice Roll Simulator** 🎲

Customizable dice roll simulator to generate random dice rolls with a specified number of dice and sides.

---

## 9. **Simple Currency Converter** 💱

A quick and easy way to convert currency values using real-time exchange rates (via APIs).

---

## 10. **ATM Simulation (OOP)** 🏦

An ATM simulation system built using OOP principles. It includes features like checking balance, depositing, and
withdrawing funds.

---

## 11. **Cow and Bulls Game** 🐄🐂

A word-guessing game where you try to guess a 4-letter word based on "cows" and "bulls" feedback.

---

## 12. **Password Generator** 🔐

A password generator that creates random, strong passwords based on specified criteria.

---

## 13. **Password Strength Checker** 🛡️

A tool to check the strength of your password based on complexity, length, and patterns.

---

### Why These Projects Matter:

These projects reflect my journey in **learning Python** and applying concepts like **OOP** and **algorithms** to
real-world scenarios. Each one taught me something new, and I’m excited to continue building more sophisticated
applications.

---

### Let's Connect!

If you'd like to collaborate, or just want to share feedback on my projects, feel free to reach out! I'm always open to
learning and improving.



---

### Tech Stack

- **Programming Language:** Python
- **Libraries/Tools:**
    - `random` (for games and simulations)
    - `string` (for password generation)
    - `requests` (for API calls in currency conversion)

---

### Example of Code Snippet:

```python
# Password Generator Function

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

```