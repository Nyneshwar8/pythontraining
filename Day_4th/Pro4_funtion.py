# def hello():
#     print("hello")
#
def hello():
    """
    This function says hello
    """

    print(hello.__doc__)
hello()


def sum(num1,num2):
    print(f"{num1}+{num2}={num1+num2}")
sum(4.2,2)


def add_compair(num1,num2):
    if num1>num2:return num1+num2
    print("What about me")
print(add_compair(6,3))


def fun():
    print(7)
del fun
fun()


lis=(lambda a,b:a**(b+2))(3,4)
print(lis)



def fecto(num):
    if num==1:
        return 1
    return num*fecto(num-1)
print(fecto(10))


def fun(a,b,c):
    y=a/b+c
    print(y)

    return y
fun(2,3,4)

def fun(a,b,c):
    return a/b+c
fun(2,3,4)
print(fun)


def greeting(name='user'):
    print(f"hello,{name}")
greeting("Alfaiz")


def sum(a=3,b=5):
    print(a+b)
print(sum(4,b=5))


# This function we are write multiple elements and how to call function how to add it
def shopping(*item,list=[]):
    list.append(item)
    return list
print(shopping("Pizza","burger","cheez","coke"))


def shop(*args):
    for i in args:
        print(i)
shop(*[1,2,3,4,5,6,7,8,9,0 ,])