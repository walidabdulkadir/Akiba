numbers = []
count = 1
total = 0
even_count = 0
odd_count = 0


while count <= 10:
    num = int(input(f"Enter number {count}: "))
    numbers.append(num)
    count += 1

largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    
    total += number
    
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
    
    if number > largest:
        largest = number
        
    if number < smallest:
        smallest = number
        
average = total / len(numbers)        
            
   
print(f"""
===================================
    NUMBER ANALYZER
===================================
  Total           : {total}
  Average         : {average}
  Even Count      : {even_count}
  Odd Count       : {odd_count}
  Largest Number  : {largest}
  Smallest Number : {smallest}
===================================
      """)  
