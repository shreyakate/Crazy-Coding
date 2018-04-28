def findDisappearedNumbers(nums):
	res= []
	setter = [1 for _ in range(len(nums))]
	for n in nums:
		setter[n-1] = 0

	for i in range(len(setter)):
		if setter[i] ==1:
			res.append(i+1)
	return res



print findDisappearedNumbers([4,3,2,7,2,3,8,1])

