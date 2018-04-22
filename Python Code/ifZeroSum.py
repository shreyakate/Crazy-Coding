def ifZeroSum(arr):
	d ={}
	s = 0
	d[arr[0]] = 0
	for i in range(1,len(arr)):
		for k in d.keys():
			s = k+ arr[i]
			if s == 0:
				return True
			else:
				d[s] = 0
				d[s-arr[i]] =0
	return False

print ifZeroSum([-3,4,-2,5])	 

