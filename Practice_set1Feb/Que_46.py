# Python program to multiply all numbers of a list
import math

# Getting list from user
myList = []
length = int(input("Enter number of elements: "))
for i in range(0, length):
    value = int(input())
    myList.append(value)

# multiplying all numbers of a list
productVal = math.prod(myList)

# Printing values
print("List : ", myList)
print("Product of all values= ", productVal)