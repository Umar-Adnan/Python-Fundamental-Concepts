#Changing the type of a variable is called type casting or type conversion.

print(1+2.4) # Type conversion(Done implicitly) from int to float
print(1+int(3.5)) # Type casting(Done explicitly) from float to int

age = input("Enter your age: ") # input() function always returns a string
age = int(age) # Type casting from string to int
print("Your age is: ", age)
print("Your age after 5 years will be: ", age + 5) # Type conversion from int to int
