def MoveZeros(nums):
	i, l = 0,0
	while i<len(nums):
		if nums[i] != 0:
			nums[l] = nums[i]
			l += 1
		i += 1
	while l<len(nums):
		nums[l] = 0
		l += 1
	print nums

MoveZeros([0, 1, 0, 3, 12])

MoveZeros([0, 0, 0, 0, 0])

MoveZeros([0, 0, 0, 3, 12])