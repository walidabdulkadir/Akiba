# num1, num2, num3 = map(int, input("Enter three numbers : ").split())
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the Third number : "))

if num1 == num2 and num2 == num3:
    print("All numbers are equal. ")
elif num1 == num2 or num2 == num3 or num3 == num1:
    print("Two numbers are Equal")
elif num1 > num2 and num2 > num3:
    print(f"{num1} is the greater number")
elif num1 < num2 and num2 > num3:
    print(f"{num2} is the greater")
elif num1 < num3 and num3 > num2:
    print(f"{num3} is the greater")
