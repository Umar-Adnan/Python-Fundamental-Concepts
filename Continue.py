# This is a simple Python program that demonstrates the use of the 'continue' statement in a loop.
# The program iterates through the numbers 0 to 6, but skips the number 3
# and continues with the next iteration.
for i in range(0,7):
    if i == 3:
        continue
    print(i)

# This program demonstrates the use of the 'continue' statement in a while loop.
i = 0
while i < 7:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1