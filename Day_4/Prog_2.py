# FUNCTIONAL PROGRAMING

# def starts_with_A(s):
#     return s[0] == "A"
#
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(starts_with_A, fruit)
#
# print(list(map_object))


# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(lambda s: s[0] == "A", fruit)
#
# print(list(map_object))


# animal=["Cat","Dog","Horse","Panther","Tiger"]
# anim=map(lambda ani:ani[1]=="o",animal)
# print(list(anim))


# def check(s):
#     return s[0] =="A"
# names=["Alfaiz","Akshay","Shubhz","Gau","Guaru","Nyno"]
# obj=map(check,names)
# print(tuple(obj))
#
# print(list(obj))

names=["Alfaiz","Akshay","Shubhz","Gau","Gauru","Nyno"]
names=map(lambda frnd:frnd[2]=="u",names)
print(list(names))