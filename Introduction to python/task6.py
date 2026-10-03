name = input("Enter your name : ")
salary = int(input("Enter your salary : "))
trans = int(input("Enter your Transport allowance : "))
food = int(input("Enter your food alowance : "))

groos_salary = salary + trans + food

print(f"""
      ========================================
                EMPLOYEE PAYSLIP
      ========================================

              Employee: {name}

       Basic Salary:          {salary} ETB
       Transport Allowance:    {trans} ETB
       Food Allowance:         {food} ETB
      ----------------------------------------
       Gross Salary:          {groos_salary} ETB
      ========================================
 
      """)