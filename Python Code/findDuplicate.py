def findDuplicate(nums):
	# for n in nums:
	# 	temp = abs(n)
	# 	if nums[temp-1] <0:
	# 		return temp
	# 	nums[temp-1] *= -1

        # the same with linked list cycle
	slow, fast = nums[0], nums[nums[0]]
	while slow != fast:
		slow, fast = nums[slow], nums[nums[fast]]
	fast = 0
	while slow != fast:
		slow, fast = nums[slow], nums[fast]
	return slow
        

print findDuplicate([1,3,1,6,5,2])
print findDuplicate([1,3,3,6,5,2])	
print findDuplicate([1,3,6,6,5,2])		


