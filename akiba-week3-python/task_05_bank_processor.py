balance = 1000
transaction_history = []


def deposit_money(amount):
    current_balance = balance
    
    if amount <= 0:
        return "Invalid Input"
    else:
        current_balance += amount
    
    record_transaction("deposit", amount, current_balance)
    print(f"Successfully deposited {amount} ETB")   
    
def withdraw_money(amount):
    current_balance = balance
    
    if amount <= 0:
       print("Invalid Input")   
       return
   
    
    
    elif amount > current_balance:
        return "Insufficient balance"
    else:
        current_balance -= amount
        
    record_transaction("withdrawal", amount, current_balance)
    print(f"Successfully withdrew {amount} ETB")

def check_balance():
    print(f"Current balance: {balance} ETB")

def record_transaction(transaction_type, amount, current_balance):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": current_balance
    }
    transaction_history.append(transaction)

def transaction_summary():
    total_deposited = 0
    total_withdrawn = 0
    
    for transaction in transaction_history:
        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        else:
            total_withdrawn += transaction["amount"]
            
    print("\n--- Transaction Summary ---")
    print(f"Total deposited: {total_deposited} ETB")
    print(f"Total withdrawn: {total_withdrawn} ETB")
    print(f"Final balance: {balance} ETB")
    print("\n--- Transaction History ---")
    
    for transaction in transaction_history:
        print(transaction)



while True:
    print("\n--- Banking System ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit_money(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw_money(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        transaction_summary()

    elif choice == "5":
        print("Thank you for using Akiba banking system!")
        break

    else:
        print("Invalid option. Please choose between 1 and 5.")