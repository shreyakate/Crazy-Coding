def Sum2(arr,k):
	arr.sort()
	l, r = 0, len(arr)-1
	res =[]
	while l<r:
		if arr[l] + arr[r] == k:
			res.append([arr[l], arr[r]])
			l += 1
			r -= 1
		elif arr[l] + arr[r] <k:
			l += 1
		else:
			r-= 1
	print res
Sum2([1,3,-3,7,-8,2,16,34,-81,80,80,-81,80],-1)
