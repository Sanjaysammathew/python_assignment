# Menu-Based Number Analyzer


# Even / Odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Prime
def check_prime(number):
    if number < 2:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False

    return True


# Reverse
def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return reverse


# Palindrome
def check_palindrome(number):
    if number == reverse_number(number):
        return True
    else:
        return False


# Sum of digits
def sum_of_digits(number):
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total


# Armstrong
def check_armstrong(number):

    # Count digits
    temp = number
    digits = 0

    if number == 0:
        digits = 1
    else:
        while temp > 0:
            digits += 1
            temp = temp // 10

    # Calculate Armstrong sum
    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    if total == number:
        return True
    else:
        return False




number = int(input("Enter a number: "))

while True:

    print("\n NUMBER ANALYZER ")
    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Check Palindrome")
    print("4. Check Armstrong")
    print("5. Reverse Number")
    print("6. Sum of Digits")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("Result:", check_even_odd(number))

        case 2:
            if check_prime(number):
                print("Result: Prime")
            else:
                print("Result: Not Prime")

        case 3:
            if check_palindrome(number):
                print("Result: Palindrome")
            else:
                print("Result: Not Palindrome")

        case 4:
            if check_armstrong(number):
                print("Result: Armstrong")
            else:
                print("Result: Not Armstrong")

        case 5:
            print("Reverse:", reverse_number(number))

        case 6:
            print("Sum of digits:", sum_of_digits(number))

        case 7:
            print("Exiting...")
            break

        case _:
            print("Invalid choice. Please enter 1-7.")