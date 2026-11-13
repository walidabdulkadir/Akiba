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