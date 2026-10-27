class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

student1 = Student("Walid", "20", "CS")
student2 = Student("Ahmed", "22", "IT")
student3 = Student("Oumer", "24", "IS")

student1.display_info()
student2.display_info()
student3.display_info()