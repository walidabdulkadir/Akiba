import random
count = 1

secret = random.randint(1, 3)
while count <= 5:
    guess = int(input("Enter a number from 1-10 : "))
    if secret == guess:
        print("Congratulations!")
        print(f""" 
              You guessed the number
              in {count} attempts.
              
              """)
        
        break
    else:
       print(f"""
             Wrong guess! 
             Attempt {count} of 5.
             
            """)
       count += 1
       continue
else:
    print("Game Over!!!")