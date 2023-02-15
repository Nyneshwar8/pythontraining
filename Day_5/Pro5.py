
Name=["Alfaiz","Shubhangi","Gayatri","Akshay","Madhuri"]
res=map(lambda s:s[0]=="A",Name)
print(list(res))


Animal=["Cat","Dog","Horse","owl","Ship"]
res=map(lambda a:a[1]=="o" , Animal)
print(tuple(res))



Post=["CEO","Vice President","Manager","Staff","Senior devloper"]
res=filter(lambda A:A[2]=="n",Post)
print(list(res))

from functools import reduce
list=[2,3,4,5,6,7,5]
a=(reduce(lambda x,y:x*y,list))
print(a)