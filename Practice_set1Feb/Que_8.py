# Program to Subtract a List from Another List
num_List_1=[10,20,30,40,50]
num_List_2=[5,5,5,5,5]

res=[]
for i in range(len(num_List_1)):
    sub=num_List_1[i] - num_List_2[i]
    res.append(sub)
print(res)