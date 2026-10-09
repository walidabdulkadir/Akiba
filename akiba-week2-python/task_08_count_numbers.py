num = int(input("Enter a positive number: "))

count = 1
even_count = 0
odd_count = 0
total = 0

if num <= 0:
    print("Please, Enter a positive number")
else:
    while count <= num:
    # Check whether count is even or odd
        if count % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        total += count
        count += 1
    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)
    print("Sum:", total)