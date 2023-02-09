
# Container Type

list=[10,50,30,450,57,16,0]
list1=[10,45,25,250,25,10,1]
list2=[]
print(list)

min_number=min(list)
print(min_number)

max_number=max(list)
print(max_number)

sum_number=sum(list)
print(sum_number)

print(len(list))

sorted_list=sorted(list)
print(sorted_list)

all_list=all(list)
print(all_list)

any_list=any(list)
print(any_list)

in_method=5 in list
print(in_method)

list.reverse()
print(list)


for ele1,ele2 in zip(list ,list1):
 i=ele1-ele2
 list2.append(i)
print(list2)


# tuple

tup=(10,20,30,40,50,60,40)
