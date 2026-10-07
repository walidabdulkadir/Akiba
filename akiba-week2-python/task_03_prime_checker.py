number = int(input("Enter a number : "))

if number < 2:
    print("Not prime")
else:
    is_prime = True
    
    for divisor in range(2,number):
        if number % divisor == 0:
            is_prime = False
            break
        
    if is_prime:
        print("prime")
    else:
        print("Not prime")