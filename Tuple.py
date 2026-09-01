#Tuple is a collection of ordered and immutable elements.
#Tuples are similar to lists, but they cannot be changed after creation.
#They are defined using parentheses ().

#All other operations are same as list except for the methods like append, insert, pop, clear etc.
#which are not available in tuple
marks = (95,98,97,65,98,12,45,78,89,90,100,99,88,76,85,92,91,87,84,82)

#We can make tuples without parentheses, but it is recommended to use them for clarity.
students = "Ali", "Ahmed", "Ayesha", "Fatima"
print(students, type(students)) #prints the entire tuple and it's type
print(students[0]) #prints first element of the tuple
print(students[-1]) #prints last element of the tuple



print(type(marks)) #prints the type of the tuple
print(len(marks))
print(max(marks))
print(min(marks))

for i in marks:
    print(i)

