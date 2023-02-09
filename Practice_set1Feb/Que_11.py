# Python program to print list elements in different ways.
a = [1, 2, 3, 4, 5,9]
print(*a)

print(*a, sep=", ")

print(*a, sep="\n")

a=[2*i for i in range(1,8)]

print(*a)