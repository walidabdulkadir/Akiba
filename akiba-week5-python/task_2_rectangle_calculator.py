class Rectangle:
    def __init__(self, length, width ):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    

r1 = Rectangle(10, 20)
r2 = Rectangle(15, 25)

print(r1)
print("Area =" ,r1.area())
print("Perimeter =" ,r1.perimeter())

print(r2)
print("Area =" ,r2.area())
print("Perimeter =" ,r2.perimeter())