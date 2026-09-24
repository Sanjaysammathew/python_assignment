# Product Management System

# Demonstrates:
# Functions
# Type Hints
# Positional-only Arguments
# Keyword-only Arguments
# *args
# **kwargs
# any()
# all()
# zip()
# enumerate()
# Inner Function
# Multiple Return Values
# Recursion
# match-case
# Menu Driven Program


# Product Data

products = [
    {"id": 1, "name": "Laptop", "price": 55000, "stock": 5},
    {"id": 2, "name": "Mouse", "price": 800, "stock": 15},
    {"id": 3, "name": "Keyboard", "price": 1500, "stock": 10},
    {"id": 4, "name": "Monitor", "price": 12000, "stock": 6},
    {"id": 5, "name": "Headphones", "price": 2500, "stock": 12},
    {"id": 6, "name": "Webcam", "price": 3500, "stock": 8},
    {"id": 7, "name": "Speaker", "price": 4000, "stock": 7},
    {"id": 8, "name": "Printer", "price": 9000, "stock": 4},
    {"id": 9, "name": "USB Drive", "price": 700, "stock": 20},
    {"id": 10, "name": "Tablet", "price": 25000, "stock": 5}
]


# Display Products
# enumerate()

def display_products(products: list[dict]) -> None:

    print("\nPRODUCT LIST")

    for number, product in enumerate(products, start=1):
        print(
            f"{number}. "
            f"ID: {product['id']} | "
            f"{product['name']} | "
            f"₹{product['price']} | "
            f"Stock: {product['stock']}"
        )


# Find Product
# Positional-only argument

def find_product(
    products: list[dict],
    product_id: int,
    /
) -> dict | None:

    for product in products:

        if product["id"] == product_id:
            return product

    return None


# Add Product
# Keyword-only arguments

def add_product(
    products: list[dict],
    *,
    name: str,
    price: float,
    stock: int
) -> None:

    new_id = len(products) + 1

    product = {
        "id": new_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(product)

    print("Product added successfully!")


# Validate Product
# any() and all()

def validate_product(
    name: str,
    price: float,
    stock: int
) -> bool:

    values = [name, price, stock]

    # any() checks if at least one value is None

    if any(value is None for value in values):
        return False

    # all() checks if all conditions are True

    return all([
        name.strip() != "",
        price > 0,
        stock >= 0
    ])


# Update Product
# **kwargs

def update_product(
    product: dict,
    **kwargs: object
) -> None:

    for key, value in kwargs.items():

        if key in product:
            product[key] = value

    print("Product updated successfully!")


# Show Selected Products
# *args

def show_products(*products: dict) -> None:

    print("\nSELECTED PRODUCTS")

    for product in products:

        print(
            f"{product['name']} - "
            f"₹{product['price']} - "
            f"Stock: {product['stock']}"
        )


# Compare Product Names and Prices
# zip()

def compare_products(products: list[dict]) -> None:

    names = [product["name"] for product in products]
    prices = [product["price"] for product in products]

    print("\nPRODUCT PRICES")

    for name, price in zip(names, prices):
        print(f"{name}: ₹{price}")


# Calculate Product Value
# Multiple Return Values

def calculate_product_value(
    price: float,
    stock: int
) -> tuple[float, float]:

    total = price * stock
    tax = total * 0.18

    return total, tax


# Inner Function

def product_summary(product: dict) -> None:

    def format_price(price: float) -> str:
        return f"₹{price:,.2f}"

    print("\nPRODUCT SUMMARY")

    print(f"Name  : {product['name']}")
    print(f"Price : {format_price(product['price'])}")
    print(f"Stock : {product['stock']}")


# Recursion

def calculate_total_stock(
    products: list[dict],
    index: int = 0
) -> int:

    # Base condition

    if index == len(products):
        return 0

    # Recursive call

    return (
        products[index]["stock"]
        + calculate_total_stock(products, index + 1)
    )


# Display Menu
# enumerate()

def display_menu() -> None:

    menu = [
        "Display Products",
        "Add Product",
        "Update Product",
        "Product Summary",
        "Compare Products",
        "Calculate Total Stock",
        "Exit"
    ]

    print("\nPRODUCT MANAGEMENT")

    for number, item in enumerate(menu, start=1):
        print(f"{number}. {item}")


# Main Program

def main() -> None:

    while True:

        display_menu()

        choice = int(input("\nEnter your choice: "))

        match choice:

            # Display products

            case 1:
                display_products(products)


            # Add product

            case 2:

                name = input("Enter product name: ")
                price = float(input("Enter price: "))
                stock = int(input("Enter stock: "))

                if validate_product(name, price, stock):

                    add_product(
                        products,
                        name=name,
                        price=price,
                        stock=stock
                    )

                else:
                    print("Invalid product details.")


            # Update product

            case 3:

                product_id = int(
                    input("Enter product ID: ")
                )

                product = find_product(
                    products,
                    product_id
                )

                if product:

                    price = float(
                        input("Enter new price: ")
                    )

                    stock = int(
                        input("Enter new stock: ")
                    )

                    update_product(
                        product,
                        price=price,
                        stock=stock
                    )

                else:
                    print("Product not found.")


            # Product summary

            case 4:

                product_id = int(
                    input("Enter product ID: ")
                )

                product = find_product(
                    products,
                    product_id
                )

                if product:

                    product_summary(product)

                    total, tax = calculate_product_value(
                        product["price"],
                        product["stock"]
                    )

                    print(f"Total Value: ₹{total:,.2f}")
                    print(f"Tax: ₹{tax:,.2f}")

                else:
                    print("Product not found.")


            # zip() and *args

            case 5:

                compare_products(products)

                # if len(products) >= 2:

                #     show_products(
                #         products[0],
                #         products[1]
                #     )


            # Recursion

            case 6:

                total_stock = calculate_total_stock(products)

                print(f"\nTotal Stock: {total_stock}")


            # Exit

            case 7:

                print("\nThank you for using Product Management System!")

                break


            # Invalid choice

            case _:

                print("Invalid choice. Please select 1-7.")


# Start Program

main()