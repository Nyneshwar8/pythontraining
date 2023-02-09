
list = [75, 15, 25, 57, 45]
M = 3
N = 5
# print the list
print("List is: ", list)
print("Numbers divisible by {0} and {1}".format(M, N))
for num in list:
  if (num%M==0 and num%N==0):
   print(num)