def maxSubArray(nums):
	if not nums: return -2147483648
	maxSum, tmpSum, neg, maxNeg = 0,0, 0,-2147483648

	for i in range(1,len(nums)):
		nums[i] = max(nums[i-1]+nums[i], nums[i])
	print nums
	return max(nums)

	for n in nums:
		if n < 0:
			neg += 1
			maxNeg == max(n,maxNeg)
		if n + tmpSum < 0:
			tmpSum = 0
			continue
		tmpSum += n
		maxSum = max(maxSum, tmpSum)

	if neg == len(nums):
		return maxNeg
	return maxSum

print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


