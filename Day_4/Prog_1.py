# set1,set2,set3={1,2,3},{4,5,6},{7,8,9}
# a=set1.union(set2,set3)
# print(a)
#
# set1,set2,set3={1,2,3,3},{4,5,6,3},{7,8,9,3}
# a=set1.intersection(set2,set3)
# print(a)
#
# set1,set2={11,18,3,3},{4,5,6,3,18}
# a=set1.difference(set2)
# print(a)
#
#
# a =(lambda x, y: x + y)(2,3)
# print(a)


set1,set2={6,6,9},{4,8,6}
s=set1.union(set2)
print(s)

s=set1.intersection(set2)
print(s)

s=set1.difference(set1)
print(s)