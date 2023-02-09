
list1 = [10, 20, 30, 40, 50]
list2 = [2, 3, 4, 5, 6]

sub = []
for i in range(len(list1)):
    item = list1[i] - list2[i]
    sub.append(item)

print(sub)


x=[10,20,30,40,50]
y=[5,4,6,7,8]

sub=[]
for i in range(len(x)):
    res=x[i]-y[i]
    sub.append(res)
print(sub)


a=[100,200,300,400,500]
b=[50,150,250,350,450]

sub=[]
for i in range(len(a)):
    res=a[i]-b[i]
    sub.append(res)
print(sub)

year=int(input("Write a year here:-"))
if year%4==0:
    print("This is leap year")
else:
    print("This is not a leap year")