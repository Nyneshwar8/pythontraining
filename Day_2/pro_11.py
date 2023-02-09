# # function call with list
#
a=[0,6,9,24,11,5,10,66,99]
#
# print(max(a))
#
# print(min(a))
#
# print(len(a))
#
# print(sum(a))
#
# print(sorted(a))
#
# a.append(7)
# print(a)
#
# a.insert(3,108)
# print(a)
#
# a.clear()
# print(a)
#
# a.remove(99)
# print(a)
#
# a.pop(6)
# print(a)
#
# a=[1,2,3,4,5,3,8,5,58,5]
#
# print(a.index(5))
# print(a.count(5))
#
# a.sort()
# print(a)
#
a.reverse()
print(a)
#
# # convert data type into list
# a="shubhangi"
# print(list(a))

a=[0,1,1,1]
print(any(a))
print(all(a))

# tab=[3*i for i in range(1,11)]
# print(tab)
# table=[3*i for i in range(1,11) if i%3==0]
# print(table)
# for i in [12,42,2,56,23,45]:
#     if i%2==0:
#       print(f"{i} composite\n")