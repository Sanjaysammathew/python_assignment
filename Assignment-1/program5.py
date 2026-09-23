# 5. Shopping Cart Calculator
# Given multiple product prices:
# Enter number of products: 5
# Accept the prices using a loop.
# Calculate:
# •	Subtotal
# •	Discount
# •	Tax
# •	Final amount
# Apply different discounts based on the subtotal.


# Shopping Cart Calculator

# Get number of products
number_of_products = int(input("Enter number of products: "))

# Empty list to store product prices
prices = []

# Accept prices using a loop
for i in range(number_of_products):
    price = float(input(f"Enter price of product {i + 1}: "))
    prices.append(price)

# Calculate subtotal
subtotal = sum(prices)

# Apply discount based on subtotal
if subtotal < 1000:
    discount_rate = 0

elif subtotal < 5000:
    discount_rate = 0.10

elif subtotal < 10000:
    discount_rate = 0.20

else:
    discount_rate = 0.30

# Calculate discount
discount = subtotal * discount_rate

# Calculate amount after discount
amount_after_discount = subtotal - discount

# Calculate tax
tax = amount_after_discount * 0.05

# Calculate final amount
final_amount = amount_after_discount + tax

# Display bill
print("\n Shopping Bill ")
print(f"Subtotal       : ₹{subtotal:.2f}")
print(f"Discount       : ₹{discount:.2f}")
print(f"Tax            : ₹{tax:.2f}")
print(f"Final Amount   : ₹{final_amount:.2f}")
