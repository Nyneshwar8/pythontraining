# FUNCTIONAL PROGRAMMING

# def starts_with_A(s):
#     return s[0] == "A"
#
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filter_object = filter(starts_with_A, fruit)
#
# print(list(filter_object))


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))

cars =["Verna","Harrior","Safari","Thar","Loggy"]

obj=map(lambda a:a[1]=='a',cars)
print(list(obj))

