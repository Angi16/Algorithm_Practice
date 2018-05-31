# An array and a number is given, we have to find the index of that element
# If that number does not exist we'll return -1
# We'll use Linear Search technique

def Lsearch(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:return i
	return -1

n,x=map(int,input().split()) # length of array and the number to be find
arr=list(map(int,input().split()))
z=Lsearch(arr,x)
print(z)