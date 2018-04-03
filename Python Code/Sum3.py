def Sum3(arr,target):

	arr.sort()
	i = 0
	res =[]
	while i <len(arr)-2:
		k = target - arr[i]
		l ,r = i+1, len(arr)-1
		while l<r:
			if arr[l] + arr[r] == k:
				res.append([arr[i],arr[l], arr[r]])
				l += 1
				r -= 1
			elif arr[l] + arr[r] <k:
				l += 1
			else:
				r-= 1
		i += 1
	print res

Sum3([1,3,-3,7,-8,0,2,16,34,-81,80],-4)
