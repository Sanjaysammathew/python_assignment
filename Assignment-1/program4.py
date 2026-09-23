# 4. Electricity Bill Generator
# Input:
# Customer Name
# Units Consumed
# Calculate the bill using slabs.
# Also display:
# Customer Name
# Units Consumed
# Energy Charge
# Tax
# Total Bill
# Handle invalid/negative units.

# | Units consumed |        Rate |
# | -------------- | ----------: |
# | 0–100          | ₹2 per unit |
# | 101–200        | ₹3 per unit |
# | 201–300        | ₹5 per unit |
# | Above 300      | ₹7 per unit |


customer_name = input("Enter a customer name: ")
unit = int(input("Enter units consumed: "))

# Check whether units are valid
if unit < 0:
    print("Please enter a valid unit")

else:
    # Calculate energy charge based on slabs
    if unit <= 100:
        energy_charge = unit * 2

    elif unit <= 200:
        energy_charge = (100 * 2) + ((unit - 100) * 3)

    elif unit <= 300:
        energy_charge = (100 * 2) + (100 * 3) + ((unit - 200) * 5)

    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + ((unit - 300) * 7)

    # Tax = 5% of energy charge
    tax = energy_charge * 0.05

    # Calculate total bill
    total_bill = energy_charge + tax

    # Display bill
    print(f"Customer Name  : {customer_name}")
    print(f"Units Consumed : {unit}")
    print(f"Energy Charge  : ₹{energy_charge:.2f}")
    print(f"Tax            : ₹{tax:.2f}")
    print(f"Total Bill     : ₹{total_bill:.2f}")
