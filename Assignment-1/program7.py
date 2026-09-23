# Number Analyzer using Functions


# Count number of digits
def count_digits(number):
    count = 0

    if number == 0:
        return 1

    while number > 0:
        number = number // 10
        count += 1

    return count


# Find sum of digits
def sum_of_digits(number):
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total


# Find product of digits
def product_of_digits(number):
    product = 1

    if number == 0:
        return 0

    while number > 0:
        digit = number % 10
        product *= digit
        number = number // 10

    return product


# Reverse the number
def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return reverse


# Check Even / Odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Check Prime
def check_prime(number):
    if number < 2:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False

    return True


# Check Palindrome
def check_palindrome(number):

    reverse = reverse_number(number)

    if number == reverse:
        return True
    else:
        return False


# Check Armstrong
def check_armstrong(number):

    digits = count_digits(number)
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    return total == number




number = int(input("Enter a number: "))

print(" Number Analysis ")

print("Number           :", number)
print("Number of digits :", count_digits(number))
print("Sum of digits    :", sum_of_digits(number))
print("Product of digits:", product_of_digits(number))
print("Reverse          :", reverse_number(number))
print("Even/Odd         :", check_even_odd(number))

if check_prime(number):
    print(f"{number} isPrime")
else:
    print(f"{number} is Not Prime")

if check_palindrome(number):
    print(f"{number} is Palindrome")
else:
    print(f"{number} is not Palindrome")

if check_armstrong(number):
   print (f"{number} is Armstrong")
else:
    print(f"{number} is not Armstrong")