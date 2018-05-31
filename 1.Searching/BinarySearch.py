# An array and a number is given, we have to find the index of that element
# If that number does not exist we'll return -1
# We'll use Binary Search technique


def BinarySearch (arr, l, r, x):
	if r >= l:
		mid = l + (r - l)//2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return BinarySearch(arr, l, mid-1, x)
		else:
			return BinarySearch(arr, mid+1, r, x)
	else:
		return -1
	
n,x=map(int,input().split())
arr=list(map(int,input().split()))
z=BinarySearch(arr,0,len(arr)-1,x)
if z != -1:
	print(z)