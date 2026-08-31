# #Question 1 : Print all odd numbers from 1 to 20
for i in range(1,21):
    if i % 2 != 0:
        print(i)

# #Question 2 : Print the table of 57
for i in range(57, 570, 57):
    print(i)

# #Question 2(Another way) : Print the table of 57
for i in range(0, 11):
    print("57 x", i, "=", 57 * i)

# #Question 3 : Print all multiples of 3 from 1 to 50 but skip 15
for i in range(1,51):
    if i % 3 == 0:
        if i == 15:
            continue
        print(i)

#Question 4
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print(i)
        break