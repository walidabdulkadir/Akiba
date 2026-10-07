check_number = int(input("Enter a number: "))

if check_number == 0:
    print("the number is zero")
    
elif check_number > 0:
    if check_number % 2 == 0:
        print("the number is positive and even")
    else: 
        print("the number is positive and odd")
        
else:
    if check_number % 2 == 0:
        print("the number is negative and even")
    else:
        print("the number is negative and odd")