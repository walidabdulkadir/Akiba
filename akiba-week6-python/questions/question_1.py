class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")
        
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am a student in the {self.department} department.")
      
  
student1 = Student("Alice", "S001", "Computer Science")
student2 = Student("Bob", "S002", "Mathematics")

student1.introduce()
student1.display_info()

student2.introduce()
student2.display_info()