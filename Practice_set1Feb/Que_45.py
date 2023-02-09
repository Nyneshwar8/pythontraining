# Python program to remove empty list from a list of lists

list=[4,5,[],8,[],96,[],[],2]
while [] in list:
  list.remove([])

print(list)
