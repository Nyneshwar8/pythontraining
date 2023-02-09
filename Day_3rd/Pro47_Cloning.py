def fun(li1):
    li_copy = li1[:]
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = fun(li1)
print("Original List:", li1)
print("After Cloning:", li2)