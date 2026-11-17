# part A
class Dog:
    def sound(self):
        return "Woof!"
    
class Cat:
    def sound(self):
        return "Meow!"

class Cow:
    def sound(self):
        return "Moo!"
    
Dog1 = Dog()
Cat1 = Cat() 
Cow1 = Cow()   

print(Dog1.sound())    
print(Cat1.sound())
print(Cow1.sound())

# Part B
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self): pass

class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def calculate_area(self): return self.l * self.w

class Circle(Shape):
    def __init__(self, r): self.r = r
    def calculate_area(self): return math.pi * self.r**2

rect, circle = Rectangle(5, 10), Circle(7)
print(f"Rectangle Area: {rect.calculate_area()}")
print(f"Circle Area: {circle.calculate_area():.2f}")