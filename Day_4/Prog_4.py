#-------Add two numbers using String Formating.

num1=10
num2=20
sum=num1+num2

print("sum Of {0} and {1} is {2}".format(num1,num2,sum))


#-------Factorial number using function.

def facto(n):
    return 1 if (n==1 or n==0) else n * facto(n-1)

print("Factorial of ","is",facto(6))


#-------Print Max Number using Function.
def max(a,b):
    if a>=b:
        return a
    else:
        return b
a=99
b=6

print(max(a,b))