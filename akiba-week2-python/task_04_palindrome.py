word = input("Enter a word : ")
word = word.lower()
reversed_word = word[::-1]

if word == reversed_word:
    print("Palindrome")
else:
    print("Not palindrome")