# Python 3 code to find sum
# of elements in given array

def _sum(arr):
	sum = 0
	for i in arr:
		sum = sum + i
	return(sum)
arr = []
arr = [12, 3, 4, 15]
n = len(arr)
ans = _sum(arr)
print('Sum of the array is ', ans)
