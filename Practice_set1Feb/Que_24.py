
# list = [10, 15, 20, 25, 30]
#
# m = 3
# n = 5
# print("Numbers divisible by {0} and {1}".format (m, n))
# for num in list:
# 	if( num%m==0 and num%n==0 ) :
# 		print(num)

#------slicing in python-----
# list=[1,2,3,4,5]
# # print(list[1:4])
# print((slice(100)))
#
# s="helloworld"
# print(s[slice(1,6)])

# def hello():
#     print('hello')

# def hello():
#         """
#         this function is says hello
#         """
# print(hello.__doc__)

# a=int(input('no1:-'))
# b=int(input('no2:-'))
# def add(a,b):
#     pass
#     print(a+b)
#
# add(a,b)
# -----Lambda--------
# lam=(lambda a,b:a**(b+2))(3,4)
# print(lam)

#------recursion------
# def facto(num):
#     if num==1:
#         return 1
#     return num*facto(num-1)
# print(facto(5))
#  # 5*4*3*2*1=120  facto count like this
#
# def add(a,b):
#     return a*b
# print(add(3,3))
#
# def func(a,b,c):
#     return a/b+c
# print(func(3,2,1))
#
# def add(a,b):
#   return a+b
# print(add(*range(5,7)))
#
# def add(a=2,*args):
#
#   for i in args:a+=1
#
#   return a
#
#   print(add(2,3,4))

# lam=(lambda no1,no2:(no1+no2))(8,9)
# print(lam)

# class panda :
#     def __init__(self,studentName,RollNo,MobNo):
#          self.studentName=studentName
#
#          self.RollNo = RollNo
#
#          self.MobNo = MobNo
#
#     def __repr__(self):
#          return repr("studentName is "+self.studentName + "RollNo " + str(self.RollNo) + "MobNo " +str(self.MobNo))
#
# name=panda("shubhz",12,9022884536)
#
# print(name)
# repr(name)




class Human:
    def __init__(self,StudentName,RollNo):
        self.StudenName=StudentName
        self.RollNo=RollNo

    def __repr__(self):
        return repr(self.StudenName+str(self.RollNo))

obj=Human("Shubhanmgi",69)
print(obj)
















