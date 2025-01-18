# TODO Advance functionality about to complete
# HERE basic functionality completed.


def display_menu():
    while True:
        print("1. Logged in")
        print("2. Log out")
        choice_list = ("1", "2")

        user_input = input("Enter Your choice: ")

        if user_input in choice_list:
            return user_input
        else:
            print("Invalid Input.")


class ATM:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        self.logged_in = False
        self.user_pin = None

    # get user choice
    user_choice = display_menu()

    if user_choice == "1":
        def get_pin(self):
            user_pin = input("Enter your pin to logged in: ")
            self.user_pin = user_pin

            if self.check_pin(user_pin):
                print("Logged in successfully.")
                self.__login(user_pin)
    elif user_choice == "2":
        user_pin = input("Enter your pin to logged out: ")

        if self.check_pin(user_pin):
            print("Logged in successfully.")
            self.__logout(user_pin)

    def __login(self, entered_pin):
        """To Log in a user."""
        if self.pin == entered_pin:
            self.logged_in = True

    def __logout(self):
        """To Log out a user."""
        self.logged_in = False

    def set_pin(self, new_pin):
        self.pin = new_pin

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        if self.logged_in:
            return self.balance
        else:
            print("Please Login first to see your balance")
            self.get_pin()

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive or greater than zero.")

        if self.logged_in:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive or greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient Balance.")
        if self.logged_in:
            self.balance -= amount
        else:
            print("Please login first.")


class ATMController:
    def __init__(self, pin):
        self.pin = pin
        self.atm = ATM(pin)

    @staticmethod
    def display_menu():
        long_text = """\nWelcome To The ATM:
        1. Check Balance
        2. Deposit
        3. Withdraw
        4. Exit
        """
        print(long_text)

    def check_balance(self):
        current_balance = self.atm.check_balance()
        print("Your current balance is:", current_balance)

    @staticmethod
    def get_amount(prompt):
        try:
            rupees = int(input(prompt))
            return rupees
        except Exception as e:
            print("error:", e)

    def run(self):
        while True:
            self.display_menu()

            user_choice = input("Please choose an option: ")
            if user_choice == "1":
                self.check_balance()

            elif user_choice == "2":
                try:
                    amount = self.get_amount("Enter the amount that you want to deposit: ")
                    self.atm.deposit(amount)

                    print(f"Successfully {amount} amount deposited into your account.")

                except ValueError as error:
                    print("Error in amount deposit:", error)

            elif user_choice == "3":
                try:
                    amount = self.get_amount("Enter the amount that you want to withdraw: ")
                    self.atm.withdraw(amount)
                    print(f"{amount} Amount successfully withdraw from your account.")

                except ValueError as e:
                    print("Error in amount withdrew.", e)

            elif user_choice == "4":
                print("Thanks for using this ATM.")
                quit()
            else:
                print("Invalid option")


def main():
    user_pin = input("Enter your pin: ")
    my_atm = ATMController(user_pin)
    my_atm.run()


if __name__ == "__main__":
    main()
