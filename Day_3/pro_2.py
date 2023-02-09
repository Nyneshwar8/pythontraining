# List using Lambda fun.
myset={3,2,1,4}
makelist=lambda i:list(i)
mylist=makelist(myset)
print(mylist)

myset=list(map (lambda i:i,myset))
print(myset)

myset=[i for i in range(8)if i%2!=0]
print(myset)

# Nested Condition
myset=[i for i in range(8) if i%2==0 if i%3==0]
print(myset)

list=["even" if i%2==0 else "odd" for i in range(8)]
print(list)