# Python Program to Print Numbers in a Range Without using Loops

def looping(upper):
    if(upper>0):
        looping(upper-1)
        print(upper)
upper=int(input("Enter upper limit: "))
looping(upper)