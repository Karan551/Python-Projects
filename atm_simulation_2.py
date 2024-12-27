class ATM:
    def __init__(self):
        self.balance = 0

    def deposit(self, money):
        if money <= 0:
            raise ValueError("Please enter a value greater than zero.")
        self.balance += money

    def withdrawal(self, money):
        if self.balance <= money:
            raise ValueError("Insufficient Balance.")
        if self.balance == 0:
            raise ValueError("Please deposit a money.")
        self.balance -= money

    def check_balance(self):
        return self.balance


class ATMController:
    def __init__(self):
        self.atm = ATM()

    @staticmethod
    def display_menu():
        long_text = """Welcome To The ATM:
            1. Check Balance
            2. Deposit
            3. Withdraw
            4. Exit
        """
        print(long_text)

    def get_amount(self, label):
        amount = int(input(f"Enter amount that you want to {label}: "))
        if amount <= 0:
            raise ValueError("Please enter a valid amount.")

        if label == "deposit":
            self.atm.balance += amount
            print(f"Successfully {amount} amount deposited into your account.")

        elif label == "withdraw":
            if amount > self.atm.balance:
                print("Insufficient Balance.")
            else:
                self.atm.balance -= amount
                print(f"Successfully {amount} amount {label} from your account.")

    def run(self):
        while True:
            self.display_menu()

            user_input = input("Enter Your Choice: ")
            if user_input == "1":
                balance = self.atm.check_balance()
                print(f"Your current balance is: {balance}")

            elif user_input == "2":
                self.get_amount("deposit")

            elif user_input == "3":
                self.get_amount("withdraw")
            elif user_input == "4":
                print("Thanks for using this ATM.")
                quit()
            else:
                print("Please enter a valid choice.")


def main():
    atm = ATMController()
    atm.run()


if __name__ == "__main__":
    main()
