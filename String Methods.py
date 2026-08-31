# String Methods in Python
name = " M  Umar  Adnan "
print(name.upper())  # Converts the string to uppercase
print(name.lower())  # Converts the string to lowercase
print(name.find("Adnan"))  # Finds the index of the substring "Adnan"
print(name.replace("Adnan", "Ahmed"))  # Replaces the substring "Adnan" with "Ahmed"
print(name)
print("nan" in name)  # Checks if the substring "nan" is present in the string
print(name.split())  # Splits the string into a list of words
print(name.strip())  # Removes any leading and trailing whitespace
print(name.lstrip())  # Removes leading whitespace
print(name.rstrip())  # Removes trailing whitespace
print(name.startswith("M"))  # Checks if the string starts with "M"
print(name.endswith("n"))  # Checks if the string ends with "n"
print(name.count("a"))  # Counts the occurrences of the substring "a"
print(name.isalpha())  # Checks if all characters in the string are alphabetic