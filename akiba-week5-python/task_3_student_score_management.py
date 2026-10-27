class Student:
    school_name = "Akiba Academy"
    
    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department
    
    def display(self):
        print(f"""
              School: {self.school_name}
              Name: {self.name}
              Score: {self.score}
              Department: {self.department}
              """)
        
s1 = Student("Walid", "90", "CS")
s2 = Student("Ahmed", "80", "IT")
s3 = Student("Oumer", "95", "IS")

# Original display
s1.display()
s2.display()
s3.display()

s1.score = "60"

# updated
s1.display()
s2.display()
s3.display()