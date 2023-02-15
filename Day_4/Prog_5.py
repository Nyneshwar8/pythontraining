# from functools import reduce
#
# def add(x, y):
#     return x + y
#
# list = [2, 4, 7, 3]
# print(reduce(add, list))


from functools import reduce

list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))


from functools import reduce
list=[6,6,1,9,9,9]
print(reduce(lambda a,b:a+b,list,10))
# print(list)