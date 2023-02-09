# print list after removing ODD numbers.
list = [11,12,22,78,31,33, 44, 55]

print (list)

for i in list:
 if(i % 2 != 0):
  list.remove(i)

print("After removing EVEN No:-", list)