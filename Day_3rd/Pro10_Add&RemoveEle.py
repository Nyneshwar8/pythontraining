
list=[1,2,3,4,5,6,7,8,9]

#Add single element at a time.
res=list.append(10)
print(list)

#Add multiple element at a time.
res=list.extend((10,20,30,50,60,))
print(list)

#Remove single element at a time.
res=list.remove(1)
print(list)

#remove multiple element at a time.
del list[0:7]
print(list)