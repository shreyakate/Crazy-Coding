def medianSortedArrays(arr1, arr2):
	a = len(arr1)
	if a == 2:
		return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2
	if a%2 ==0 :
		m1 = (arr1[a/2]+arr1[a/2 - 1])/2
		m2 = (arr2[a/2]+arr2[a/2 - 1])/2
	else:
		m1 = arr1[a/2]
		m2 = arr2[a/2]
	if m1 == m2 :
		return m1
	elif m1 > m2:
		return medianSortedArrays(arr1[:a/2+1], arr2[a/2:])
	else:
		return medianSortedArrays(arr1[a/2:], arr2[:a/2+1])

def MedianArray(A):
	n = len(A)
	if n%2 == 1 : return A[n/2]
	else: return (A[n/2] + A[n/2-1])/2
		
def findMedianInSortMerge(A, B):
	m1 = MedianArray(A)
	m2 = MedianArray(B)
	n = len(A)
	if n==2:
		return (max(A[0],B[0])+min(A[1],B[1]))/2
	if m1 == m2: return m1
	elif m1 > m2:
		return findMedianInSortMerge(A[:n/2+1],B[n/2:])
	else: 
		return findMedianInSortMerge(A[n/2:],B[:n/2+1])
		
print findMedianInSortMerge([1,12,15,26,38], [2,13,17,30,45])
print findMedianInSortMerge([1, 2, 3, 6], [4, 6, 8, 10])

print medianSortedArrays([1,12,15,26,38], [2,13,17,30,45])
print medianSortedArrays([1, 2, 3, 6], [4, 6, 8, 10])
