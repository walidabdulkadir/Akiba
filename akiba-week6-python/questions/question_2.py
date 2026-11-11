class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            
        else:
            self.__balance += amount
            print(f"{amount} Birr deposited successfully")
            
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
            
        elif amount < 0:
            print("Invalid withdraw amount")
            
        else:
            self.__balance -= amount
            print(f"{amount} Birr withdrawn successfully")
            
    def get_balance(self):
        print(f"Current balance: {self.__balance} Birr")

account = BankAccount("Walid" , 1000)

account.deposit(200)
account.withdraw(100)
account.get_balance()