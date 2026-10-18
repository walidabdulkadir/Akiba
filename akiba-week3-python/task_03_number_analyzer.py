number = 123

def prime_checker(number):
    if number < 2:
        return "Not prime"
    
    is_prime = True 
    
    for divisor in range(2,number):
        if number % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        return "prime"
    else:
        return "Not prime"

def get_divisors(number):
    
    if number <= 0:
        return "invalid input"
    
    divisors = []
    for divisor in range(1, number+1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors

def sum_of_digits(number):
    digit_sum = 0
    
    for digit in str(number):
        digit_int = int(digit)
        digit_sum += digit_int
    return digit_sum
        
def reverse_number(number):
    word = str(number)
    reverse_num = word[::-1]
    return reverse_num

def analyze_number(number):
    prime_check = prime_checker(number)
    divisors = get_divisors(number)
    digits_sum = sum_of_digits(number)
    reverse = reverse_number(number)
    
    print(f"""
        
    =============="Analyze Number ==============
    Number: {number}
    Prime Checker: {prime_check} 
    All positive divisors : {divisors}
    Sum of digits : {digits_sum}
    Reverse of a number : {reverse}
    """)
    
analyze_number(number)