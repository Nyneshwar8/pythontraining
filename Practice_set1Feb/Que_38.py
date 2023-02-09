# Extract Even and odd number from a given list in Python
list=[25,33,78,95,64,37,19,46,82]

even=[]
odd=[]
for i in list:
 if i%2==0:
    print('{} is an even number.',i)
 else:
    print('{} is an odd number.',i)
