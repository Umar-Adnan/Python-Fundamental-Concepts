roll_numbers = [101,105,101,108,105,110]
roll_numbers_unique = set(roll_numbers)
print("Unique roll numbers are:", roll_numbers_unique) # Output: Unique roll numbers are: {101, 105, 108, 110}


Employees = [
    (101, "Alice", 50000),
    (102, "Bob", 60000),
    (103, "Charlie", 70000)
]
e_id = int(input("Enter employee ID to search: "))
for emp in Employees:
    if emp[0] == e_id:
        print(f"Employee found: ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")
        break
else:
    print("Employee not found.")