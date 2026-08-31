p1= float(input("Enter the first number: "))
p2= float(input("Enter the second number: "))
p3= float(input("Enter the third number: "))

total = p1 + p2 + p3

average = total / 3.0
print("The total of the three numbers is:", total)
print("The average of the three numbers is:", average)

name = input("Enter your name: ")
print(name.startswith("S") or name.startswith("s"))  # Checks if the name starts with "S" or "s"
