number = int(input("Enter a number : "))

digits_sum = 0

while number > 0:
    digit = number % 10
    digits_sum += digit
    number = number // 10
print(f"The sum all digits are : {digits_sum}")