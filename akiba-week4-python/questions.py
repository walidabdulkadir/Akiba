# Question 1

# 1, a, Mutable is an object that can be changed after it is created. Example: lists, dictionaries, and sets.
#    b, Immutable is an object that cannot be changed after it is created. Example: strings, tuples, and integers.

# 2,
#modifying a list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  

#modifying a string
word = "hello"
word = "H" + word[1:]
print(word)  # Hello

# Question 2

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b) 
print(a is c) 
print(a == c) 

# 1, output of the code is: True, False, True

# 2, "is" checks whether the two references point to the same object.
#    "==" checks whether the values of the two objects are equal.

# 3, b/c and b point to the same object in memory, while c is a different object with the same value.

# Question 3

numbers = [1, 2, 3]
values = numbers

values.append(4)

print(numbers)
print(values)

# # 1, Predict the output.
[1, 2, 3, 4]
[1, 2, 3, 4]

# 2, Both variables refer to the same list in memory.

# 3,
numbers = [1, 2, 3]
values = numbers.copy()

values.append(4)

print(numbers)  # [1, 2, 3]
print(values)   # [1, 2, 3, 4]

# Question 4

scores = [50, 60, 70]
def update_list(items):
    items.append(100)

update_list(scores)

print(scores)

# 1,
[50, 60, 70, 100]

# 2, The function receives a reference to the original list. Since lists are mutable, 
#    items.append(100) modifies the same list that scores refers to.

# 3, 
scores = [50, 60, 70]
def update_list(items):
    new_list = items.copy()
    new_list.append(100)
    print(new_list)

update_list(scores)
print(scores)


# Question 5

# 1, Python manages objects in memory automatically through memory 
#    allocation, reference counting, and garbage collection.

#    Garbage collection: identifying and reclaiming unreachable
#    objects that reference each other in a cycle.

# 2,
num = [1,2,3,4]
new_num = num
num.append(5)

del num
print(new_num)
 
# 3, del num deletes the variable name num, but it does not
#    directly destroy the list object.

# 4, yes, if there is no another reference that referee to the list

# 5, it becomes eligible for memory reclamation, 
#    and no longer can be displayed