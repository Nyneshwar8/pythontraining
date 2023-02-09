# This is My first Class Program.
#
# class FirstPro:
#     a = 10
#     b=200
#     c=a*b
# objectCreation=FirstPro()
#
# print(objectCreation.a,objectCreation.b,objectCreation.c)



class Car:

    def __init__(self, Name , test):
        self.Name = Name
        self.test = test

    def __repr__(self):
        return repr("Car Name is "+self.Name+"Top Speed"+str(self.test))

Audi = Car ("Audi", 125)

print(Audi)
repr(Audi)


# Second Program

# class Demo_pro:
#     a=10
#     def sumValue(self):
#         print(self.a)
#         self.c=self.a*self.a
#         print(self.c)
#
# object=Demo_pro()
# object.sumValue()



# 3rd Program

class TCS:
    def __init__(self):
        print("welcome to .....")

object=TCS()





