# A Dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are mutable, meaning they can be changed after creation.
# They are defined using curly braces {}.

# Example of a dictionary
student_marks = { "Ali": 95, "Ahmed": 98, "Ayesha": 96 }

# Accessing values using keys
print("Ali's marks are : ", student_marks["Ali"]) # Output: 95

# Adding a new key-value pair
student_marks["Fatima"] = 92
print(student_marks) # Output: {'Ali': 95, 'Ahmed': 98, 'Ayesha': 96, 'Fatima': 92}

# Updating an existing key-value pair
student_marks["Ahmed"] = 99
print(student_marks) # Output: {'Ali': 95, 'Ahmed': 99, 'Ayesha': 96, 'Fatima': 92}

# Removing a key-value pair
del student_marks["Fatima"]
print(student_marks) # Output: {'Ali': 95, 'Ahmed': 99, 'Ayesha': 96}



Tests = {
    "Ali" : [11,55,99,66,35],
    "Umar" : [22,44,88,77,33],
    "Nomi" : [33,66,99,55,22],
}

for i in Tests:
    print(f"{i}'s scores are: {Tests[i]}")