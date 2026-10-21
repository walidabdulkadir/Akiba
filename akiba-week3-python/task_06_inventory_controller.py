products = [
    {"name": "Notebook", "price": 10.0, "quantity": 1},
    {"name": "Pen", "price": 2.0, "quantity": 3}
]


def search_product(name):
    for product in products:
        if product["name"].lower() == name.lower():
            return product
    return None


def add_product(name, price, quantity):
    if not name.strip():
        return "Name cannot be empty."
    if price < 0 or quantity < 0:
        return "Price and quantity cannot be negative."
    if search_product(name):
        return "Product already exists."

    products.append({"name": name, "price": price, "quantity": quantity})
    return "Product added successfully."


def update_price(name, price):
    product = search_product(name)
    if product and price >= 0:
        product["price"] = price
        return "Price updated."
    return "Product not found or invalid price."


def increase_stock(name, quantity):
    product = search_product(name)
    if product and quantity > 0:
        product["quantity"] += quantity
        return "Stock increased."
    return "Product not found or invalid quantity."


def sell_product(name, quantity):
    product = search_product(name)
    if product and quantity > 0:
        if quantity <= product["quantity"]:
            product["quantity"] -= quantity
            return "Sale successful."
        return "Insufficient stock."
    return "Product not found or invalid quantity."


def total_inventory_value():
    total = 0
    for product in products:
        total += product["price"] * product["quantity"]
    return total


def low_stock_report(threshold=5):
    for product in products:
        if product["quantity"] < threshold:
            print(product["name"], "-", product["quantity"], "left")


while True:
    print("\n1. Add Product")
    print("2. Search Product")
    print("3. Update Price")
    print("4. Increase Stock")
    print("5. Sell Product")
    print("6. Total Inventory Value")
    print("7. Low Stock Report")
    print("8. Display Inventory")
    print("9. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        print(add_product(name, price, quantity))

    elif choice == "2":
        product = search_product(input("Name: "))
        print(product if product else "Product not found.")

    elif choice == "3":
        name = input("Name: ")
        price = float(input("New price: "))
        print(update_price(name, price))

    elif choice == "4":
        name = input("Name: ")
        quantity = int(input("Quantity to add: "))
        print(increase_stock(name, quantity))

    elif choice == "5":
        name = input("Name: ")
        quantity = int(input("Quantity to sell: "))
        print(sell_product(name, quantity))

    elif choice == "6":
        print("Inventory value:", total_inventory_value())

    elif choice == "7":
        threshold = int(input("Low-stock threshold (default 5): ") or 5)
        if threshold >= 0:
            low_stock_report(threshold)
        else:
            print("Threshold cannot be negative.")

    elif choice == "8":
        for product in products:
            print(product)

    elif choice == "9":
        break

    else:
        print("Invalid choice.")