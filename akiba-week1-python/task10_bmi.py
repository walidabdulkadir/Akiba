name = input("Enter your name : ")
weight = float(input("Enter your Weight in kilograms : "))
height = float(input("Enter your Height in meters : "))

bmi = weight / (height ** 2)

print(f"""
================================
          BMI REPORT
================================

Name: {name}
Weight: {weight} kg
Height: {height} m

BMI: {bmi}
================================

      
      """)