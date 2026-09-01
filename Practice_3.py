# Simple Calculator Program
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /, %, **): ") 
if operation == '+':
    result = n1 + n2
    print("The result of addition is:", result)
elif operation == '-':
    result = n1 - n2
    print("The result of subtraction is:", result)
elif operation == '*':
    result = n1 * n2
    print("The result of multiplication is:", result)
elif operation == '/':
    if n2 != 0: # Check for division by zero before performing division
        result = n1 / n2
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == '%':
    if n2 != 0: # Check for division by zero before performing modulus operation
        result = n1 % n2
        print("The result of modulus is:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == '**':
    result = n1 ** n2
    print("The result of exponentiation is:", result)
else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /, %, **).")

print("Thank you for using the calculator!")