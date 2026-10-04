name = input("Enter your name : ")
salary = int(input("Enter your salary : "))
transport = int(input("Enter your Transport allowance : "))
food = int(input("Enter your food alowance : "))

groos_salary = salary + transport + food

print(f"""
      ========================================
                EMPLOYEE PAYSLIP
      ========================================

              Employee: {name}

       Basic Salary:          {salary} ETB
       Transport Allowance:    {transport} ETB
       Food Allowance:         {food} ETB
      ----------------------------------------
       Gross Salary:          {groos_salary} ETB
      ========================================
 
      """)