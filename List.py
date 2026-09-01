marks = [95, 68.2, 58.99, "A"]

print(marks[0]) #prints first element of the list
print(marks[-1]) #prints last element of the list

print(marks[3]) #prints fourth element of the list

#slicing the list
print(marks[0:2]) #prints first two elements of the list
print(marks[1:3]) #prints second and third elements of the list

#all three combinations of slicing the list
print(marks[1:]) #prints all elements from second to last
print(marks[:3]) #prints first three elements of the list
print(marks[:]) #prints all elements of the list

#Loop on list
for i in marks:
    print(i) #prints all elements of the list one by one

#List methods
marks.append(100) #adds 100 to the end of the list
print(marks)

marks.insert(1, 98) #adds 98 at index 1
print(marks)

print(70 in marks) #checks if 70 is present in the list or not

print(len(marks)) #prints the length of the list
marks.clear() #removes all elements from the list
print(marks) #prints empty list
print(len(marks)) #prints the length of the list
print(marks.count(95)) #counts the number of times 95 is present in the list
print(marks.index(68.2)) #prints the index of 68.2 in the list
print(marks.pop()) #removes and returns the last element of the list
print(marks) #prints the list after removing the last element