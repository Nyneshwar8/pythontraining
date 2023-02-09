list=[45,23,69,14,25,32]

list1=[12,36,45,96,78,55]

list.reverse()
print(list)

print(len(list))

print(min(list))

print(max(list))

print(sum(list))

print(enumerate)

emp=[]
for ele1,ele2 in zip(list ,list1):
 i=ele1-ele2
 emp.append(i)
print(emp)

print(all(list))
print(any(list))

