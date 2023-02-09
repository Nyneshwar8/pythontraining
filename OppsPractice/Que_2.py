# # arithmatic functions

class math:
    a=12
    b=3
    c = a + b
    d = a * b
    e = a - b
    f = a / b
    g =a // b
arith=math()
print(arith.c,arith.d,arith.e,arith.f,arith.g)



list=[11,18,9,12,23,4,17]
list1=[]
for index in range(len(list)):
  value=list[index]
  if value > 15:
     list1.append(value)
list[index]=15
print("modify",list ,"list1",list1)





