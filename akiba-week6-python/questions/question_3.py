class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary} Birr")


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    # Method overriding
    def display_info(self):
        print("Manager Information:")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary} Birr")
        print(f"Department: {self.department}")


class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    # Method overriding
    def display_info(self):
        print("Developer Information:")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary} Birr")
        print(f"Programming Language: {self.programming_language}")



manager = Manager("Walid", 25000, "IT")
developer = Developer("Ahmed", 20000, "Python")

manager.display_info()
print("--------------------")
developer.display_info()
