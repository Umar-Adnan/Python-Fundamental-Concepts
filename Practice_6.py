#Question 1
def check_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_or_odd(10))  # Output: Even
print(check_even_or_odd(7))   # Output: Odd

#Question 2
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

str = input("Enter a string: ")
print("Number of vowels:", count_vowels(str))


#Question 3
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if check_prime(num):
    print(num, " is a prime number.")
else:
    print(num, " is not a prime number.")


#Question 4
def avg_of_list(list):
    if len(list) == 0:
        return 0
    return sum(list) / len(list)

numbers = [1, 2, 3, 4, 5]
print("Average:", avg_of_list(numbers))
