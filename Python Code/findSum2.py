def  findSum2(arr, x):
	arr.sort()
	l = 0
	r = len(arr)-1
	while l<r:
		if arr[l]+arr[r]== x:
			return [l,r]
		elif arr[l]+arr[r]>x:
			r -=1
		else: 
			l += 1
	return []

print findSum2([1,4,45,6,10,-8],16)

