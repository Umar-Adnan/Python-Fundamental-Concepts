import random

num= int(input("Enter the number of attempts you want to guess the number: "))
secret_number = random.randint(1, 100) #Generates a random number between 1 and 100
for _ in range(num): #Here _ is used as a throwaway variable since we don't need to use the loop variable in this case.
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break
else:
    print("Sorry, you've used all your attempts. The number was:", secret_number)