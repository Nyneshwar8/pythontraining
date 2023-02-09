# Program to find the differences of two lists.
num=[45,23,89,97,69,12]

num1=[12,97,23,22,33]

res=[i for i in num if i not in num1]
print(res)
