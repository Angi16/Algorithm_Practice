
# An array and a number is given, we have to find the index of that element
# If that number does not exist we'll return -1
# We'll use Binary Search technique


def TernarySearch(arr,l,r,x):
	if(r>=l):
		mid1=l + (r - l)//3
		mid2=mid1 + (r-l)//3
		if (arr[mid1]==x):
			return mid1
		if (arr[mid2]==x):
			return mid2
		if (arr[mid1] >x ):
			return TernarySearch(arr, l, mid1-1,x)
		if(arr[mid2]< x):
			return TernarySearch(arr,mid2 + 1, x)
		return TernarySearch(arr,mid1+1,mid2-1,x)
	return(-1)

n,x=map(int,input().split()) # array length and number to be found
arr=list(map(int,input().split()))
z=TernarySearch(arr,0,len(arr)-1,x)
if z != -1:
	print(z)
		