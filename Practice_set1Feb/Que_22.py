# Program to remove duplicate elements from the list.
num=[11,22,33,44,55,22,33,44]
s=[22,33,44]

res=[i for i in num if i in s]
print(res)