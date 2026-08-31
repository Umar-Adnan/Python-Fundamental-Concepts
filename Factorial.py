num=int(input("Enter a number to calculate its factorial: "))
factorial = 1
if num==0:
    print("The factorial of 0 is ", factorial)
elif num<0:
    print("Factorial is not defined for negative numbers.")

else:
    for i in range (1,num+1):
        factorial *= i
    print("The factorial of",num,"is: ",factorial)