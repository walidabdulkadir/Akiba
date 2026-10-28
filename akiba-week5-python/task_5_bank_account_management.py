class BankAccount:
    def __init__(self, owner, balance):
        self.owner, self.balance = owner, balance
        
    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance =  new_balance
        return self.balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
          new_withdraw = self.balance - amount
          self.balance = new_withdraw 
          return self.balance
          
    def display_balance(self):
        
        print(f"""
              Account Owner: {self.owner}
              Current Balance: {self.balance} Birr
              """)
        
    
Customer1 = BankAccount("Walid" , 10000)
Customer2 = BankAccount("Ahmed" , 5000)

Customer1.deposit(5000)
Customer1.withdraw(2000)
Customer1.display_balance()

Customer2.deposit(5000)
Customer2.withdraw(200000)
Customer2.display_balance()