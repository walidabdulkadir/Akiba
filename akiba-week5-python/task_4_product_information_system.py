class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        total = self.price * self.quantity
        return total
        
    def __str__(self):
        return f"""Product:{self.name}
                   Price: {self.price}, 
                   Quantity: {self.quantity}, 
                   Total Value: {self.total_value()}
    """
        

p1 = Product("Phone", 15000, 4)
p2 = Product("Headphone", 5000, 3)
p3 = Product("Laptop", 60000, 2)

print(p1)
print(p2)
print(p3)