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

def TwoSum(arr,k):
	d ={}
	res =[]
	for i in range(len(arr)):
		m = k - arr[i]
		if m in d:
			res.append([m,arr[i]])
		else:
			d[arr[i]] = m
	return res


Sum2([1,3,-3,7,-8,2,16,34,-81,80,80,-81,80],-1)
print TwoSum([1,3,-3,7,-8,2,16,34,-81,80,80,-81,80],-1)
