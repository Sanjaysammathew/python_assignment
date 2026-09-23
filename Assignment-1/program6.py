# Login System

# Store correct username and password
correct_username = "admin"
correct_password = "1234"

# Allow maximum 3 attempts
for attempt in range(3):

    # Get username and password from user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check whether both credentials are correct
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break

    else:
        # Calculate remaining attempts
        remaining_attempts = 2 - attempt

        if remaining_attempts > 0:
            print("Invalid username or password.")
            print(f"Remaining attempts: {remaining_attempts}")

        else:
            print("Invalid username or password.")
            print("Account locked.")