age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
    print("You cannot vote.")
    print("You cannot apply for a driver's license.")
    print("You can work part-time.")
else:
    print("You are an adult.")
    print("You are eligible to vote.")
    print("You can also apply for a driver's license.")
    print("You can work full-time.")

print("Thank you for providing your age.")