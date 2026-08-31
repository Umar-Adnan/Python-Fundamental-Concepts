marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("You have received an A grade.")
elif marks >= 80 and marks < 90:
    print("You have received a B grade.")
elif marks >= 70 and marks < 80:
    print("You have received a C grade.")
elif marks >= 60 and marks < 70:
    print("You have received a D grade.")
elif marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
else:
    print("You have received an F grade.")
