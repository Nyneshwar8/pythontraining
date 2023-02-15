# Factorial number using function.

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1)
print("Factorial of ","is",factorial(3))
