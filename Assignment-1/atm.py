# ATM Transaction Simulator

balance = 1000
pin = 1234
maximum_attempts = 3


# PIN Verification
def verify_pin(pin: int) -> bool:
    for _ in range(maximum_attempts):
        user_pin = int(input("Enter PIN: "))

        if user_pin == pin:
            print("PIN verified successfully!")
            return True

        print("Invalid PIN")

    return False


# Check Balance
def check_balance(balance: int) -> None:
    print(f"Current Balance: ₹{balance}")


# Deposit
def deposit(balance: int) -> int:
    amount = int(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        print(f"Deposited: ₹{amount}")
    else:
        print("Invalid amount")

    return balance


# Withdraw
def withdraw(balance: int) -> int:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print(f"Withdrawn: ₹{amount}")

    return balance


# Change PIN
def change_pin(pin: int) -> int:
    old_pin = int(input("Enter old PIN: "))

    if old_pin == pin:
        pin = int(input("Enter new PIN: "))
        print("PIN changed successfully!")
    else:
        print("Invalid PIN")

    return pin


# ATM Menu
def atm(balance: int, pin: int) -> None:

    while True:

        print("\nATM MENU")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                check_balance(balance)

            case 2:
                balance = deposit(balance)

            case 3:
                balance = withdraw(balance)

            case 4:
                pin = change_pin(pin)

            case 5:
                print("Thank you for using the ATM!")
                break

            case _:
                print("Invalid choice. Please select 1-5.")


# Main Program
if verify_pin(pin):
    atm(balance, pin)
else:
    print("You have exceeded the maximum PIN attempts.")
    print("Your account is blocked.")