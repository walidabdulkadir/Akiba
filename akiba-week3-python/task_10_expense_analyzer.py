expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]


def add_expense(description, category, amount):
    if not description.strip() or not category.strip() or amount <= 0:
        return "Invalid expense."

    expenses.append({
        "description": description,
        "category": category,
        "amount": amount
    })

    return "Expense added successfully."


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def spending_by_category():
    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += expense["amount"]

    return categories


def largest_expense():
    if not expenses:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def expenses_above(threshold=200):
    for expense in expenses:
        if expense["amount"] > threshold:
            print(expense["description"], "-", expense["amount"])


def spending_report():
    total = total_expenses()
    categories = spending_by_category()

    print("\n--- EXPENSE REPORT ---")
    print("Total spending:", total)

    print("\nSpending by category:")

    for category, amount in categories.items():
        percentage = (amount / total) * 100
        print(f"{category}: {amount} ({percentage:.2f}%)")

    largest = largest_expense()

    if largest:
        print("\nLargest expense:", largest["description"], "-", largest["amount"])

    highest_category = max(categories, key=categories.get) if categories else None

    if highest_category:
        print("Highest spending category:", highest_category)
        print("Category total:", categories[highest_category])


print(add_expense("Coffee", "Food", 80))

print("\nExpenses above 200:")
expenses_above(200)

spending_report()