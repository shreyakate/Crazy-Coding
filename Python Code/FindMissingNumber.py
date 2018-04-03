def findPivot(arr,l,h):
	if l == h : return l
	if l<h:
		mid = l + (h-l)/2
		if arr[mid]<arr[mid-1]:
			return mid
		elif arr[mid]<=arr[h]:
			return findPivot(arr,l,mid-1)
		else:
			return findPivot(arr,mid+1,h)
	else:
		return -1

def BinarySearch(arr,n,l,h):
	if l<=h:
		mid = l + (h-l)//2
		if arr[mid]==n:
			return mid
		elif arr[mid]> n:
			return BinarySearch(arr,n,l,mid-1)
		else:
			return BinarySearch(arr,n,mid+1,h)
	else:
		return -1

def searchSortedRotated(arr,n):
	x = findPivot(arr,0,len(arr)-1)
	if arr[x]==n: return x
	elif arr[x]<n<=arr[len(arr)-1]:
		return BinarySearch(arr,n,x+1,len(arr)-1)
	else:
		return BinarySearch(arr,n,0,x-1)

print searchSortedRotated([5, 6, 7, 8, 9, 10,1,2,3,4],4)
print searchSortedRotated([1,2,3,4,5,6,7,8,9],4)
print searchSortedRotated([1,2,3,5,6,7,8,9],4)
print searchSortedRotated([5, 6, 7, 8, 9, 10,1,2,3,4],5)




