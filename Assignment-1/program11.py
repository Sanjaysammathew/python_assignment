# Mini Banking Application

# List to store all accounts
accounts = []


# 1. Create Account
def create_account():

    account_number = input("Enter Account Number: ")

    # Check whether account already exists
    for account in accounts:
        if account["account_number"] == account_number:
            print("Account already exists.")
            return

    name = input("Enter Account Holder Name: ")

    # Initial balance
    balance = 0

    account = {
        "account_number": account_number,
        "name": name,
        "balance": balance,
        "transactions": []
    }

    accounts.append(account)

    print("Account created successfully!")


# Find account
def find_account(account_number):

    for account in accounts:
        if account["account_number"] == account_number:
            return account

    return None


# 2. Deposit
def deposit():

    account_number = input("Enter Account Number: ")

    account = find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    amount = float(input("Enter deposit amount: "))

    # Validation
    if amount <= 0:
        print("Deposit amount must be greater than 0.")
        return

    account["balance"] += amount

    # Add transaction
    account["transactions"].append(
        f"Deposited ₹{amount:.2f}"
    )

    print("Deposit successful!")
    print("Current Balance: ₹", account["balance"])


# 3. Withdraw
def withdraw():

    account_number = input("Enter Account Number: ")

    account = find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    amount = float(input("Enter withdrawal amount: "))

    # Validation
    if amount <= 0:
        print("Withdrawal amount must be greater than 0.")
        return

    # Check sufficient balance
    if amount > account["balance"]:
        print("Insufficient balance.")
        return

    account["balance"] -= amount

    # Add transaction
    account["transactions"].append(
        f"Withdrawn ₹{amount:.2f}"
    )

    print("Withdrawal successful!")
    print("Current Balance: ₹", account["balance"])


# 4. Check Balance
def check_balance():

    account_number = input("Enter Account Number: ")

    account = find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    print("\n Account Details ")
    print("Account Number:", account["account_number"])
    print("Name:", account["name"])
    print("Balance: ₹", account["balance"])


# 5. Transaction History
def transaction_history():

    account_number = input("Enter Account Number: ")

    account = find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    print("\n Transaction History ")

    if len(account["transactions"]) == 0:
        print("No transactions found.")

    else:
        for transaction in account["transactions"]:
            print(transaction)




while True:

    print("\n MINI BANKING APPLICATION")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            create_account()

        case 2:
            deposit()

        case 3:
            withdraw()

        case 4:
            check_balance()

        case 5:
            transaction_history()

        case 6:
            print("Thank you for using the banking application.")
            break

        case _:
            print("Invalid choice. Please enter 1-6.")