# 3. ATM Transaction Simulator
# Create an ATM program that allows the user to:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Change PIN
# 5. Exit
# Requirements:
# •	Maximum 3 PIN attempts.
# •	Withdrawal cannot exceed balance.
# •	Deposit must be positive.
# •	Use match-case.
# •	Use a loop to keep the ATM running.
# •	Use break for Exit.


Initial_balance = 1000

pin = 1234

maximum_count = 3


# PIN verification
for i in range(maximum_count):

    user_pin = int(input("Enter a pin: "))

    if pin == user_pin:
        print("Verified Successfully")
        break

    else:
        print("Invalid Pin")

else:
    print("You have exceeded the maximum PIN attempts.")
    print("Your account is blocked.")
    exit()


# ATM Menu
while True:

    print("\nATM MENU")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change Pin")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        # Check Balance
        case 1:
            print(f"The Balance: {Initial_balance}")


        # Deposit
        case 2:

            amount = int(input("Enter amount: "))

            if amount > 0:
                Initial_balance += amount

                print(f"The Deposited Amount: {amount}")
                print(f"The Balance: {Initial_balance}")

            else:
                print("Invalid Amount")


        # Withdraw
        case 3:

            amount = int(input("Enter amount: "))

            if amount <= 0:
                print("Invalid Amount")

            elif amount > Initial_balance:
                print("Insufficient Balance")

            else:
                Initial_balance -= amount

                print(f"The Withdraw Amount: {amount}")
                print(f"The Balance: {Initial_balance}")


        # Change PIN
        case 4:

            old_pin = int(input("Enter old pin: "))

            if old_pin == pin:

                new_pin = int(input("Enter new pin: "))

                # Update the actual PIN
                pin = new_pin

                print("Pin changed Successfully")

            else:
                print("Invalid Pin")


        # Exit
        case 5:

            print("Thank you for using ATM")
            break


        # Invalid choice
        case _:

            print("Invalid choice. Please select 1-5.")