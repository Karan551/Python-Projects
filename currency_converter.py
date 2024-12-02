
currencies = ("USD", "EUR", "CAD", "INR")


def get_amount():
    while True:
        try:
            user_amount = float(input("Enter the amount that you want to convert: "))
            if user_amount <= 0:
                raise ValueError
            return user_amount
        except ValueError:
            print("Invalid input.")


def get_currency(label):
    while True:
        currency = input(f"{label} (USD/EUR/CAD/INR): ").upper()
        if currency not in currencies:
            print("Invalid currency.")
        else:
            return currency


def convert_amount(amount, source_currency, target_currency):
    exchange_rates = {
        "USD": {"EUR": 0.95, "CAD": 1.40, "INR": 84.49},
        "EUR": {"USD": 1.06, "CAD": 1.48, "INR": 89.34},
        "CAD": {"USD": 0.72, "EUR": 0.68, "INR": 60.39},
        "INR": {"USD": 0.012, "EUR": 0.011, "CAD": 0.017}
    }

    if source_currency == target_currency:
        return amount

    # return round(amount * exchange_rates[source_currency][target_currency], 4)

    converted_amount = amount * exchange_rates[source_currency][target_currency]
    return "{:.2f}".format(converted_amount)


def main():
    amount = get_amount()
    source_currency = get_currency("Source Currency")
    target_currency = get_currency("Target Currency")
    converted_amount = convert_amount(amount, source_currency, target_currency)
    print(f"So {amount} {source_currency} is = {converted_amount} {target_currency}.")


if __name__ == "__main__":
    main()
