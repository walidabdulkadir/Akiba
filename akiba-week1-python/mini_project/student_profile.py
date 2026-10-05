full_name = input("Enter your name : ")
age = int(input("Enter your age : "))
student_id = input("Enter id : ")
city = input("Enter city : ")
university = input("Enter university : ")
department = input("Enter department : ")
email = input("Enter Email : ")
phone_number = int(input("Enter phone number : "))
fav_programming_language = input("Enter Favorite programming language : ")
goal = input("Enter your goal : ")

print(f"""
================================================
              AKIBA STUDENT PROFILE
================================================

Name:                 {full_name}
Student ID:           {student_id}
Age:                  {age}
City:                 {city}
University:           {university}
Department:           {department}
Email:                {email.lower()}
Phone:                {phone_number}
Favorite Language:    {fav_programming_language}

Programming Goal:
{goal}

================================================

      """)