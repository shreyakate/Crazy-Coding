def firstMissingPositive(nums):
	# x = nums[0]
	# y = 1
	# for i in range(1,len(nums)):
	# 	if nums[i] <=0: 
	# 		continue
	# 	x ^= nums[i]
	# 	y ^= i

	# print 0 | (1<<12)
	# print x, y , x^y

	expectedNum = 1
	missingNum = expectedNum

	while missingNum == expectedNum:
		for n in nums:
			print n , missingNum, expectedNum
			if n <= 0: continue
			if n != expectedNum: continue
			expectedNum += 1
		if missingNum == expectedNum: break

		missingNum = expectedNum
	return missingNum

# print firstMissingPositive([1,2,0])
print firstMissingPositive([3,4,-1,1])
# print firstMissingPositive([7,8,9,11,12])