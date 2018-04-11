def removeDuplicates(nums):
	i=1
	curr = nums[0]
	while i<len(nums):
		if nums[i] == curr:
			nums.pop(i)
			# curr = nums[i-1]
		else:
			curr = nums[i]
			i+=1
	return nums
print removeDuplicates([1,1,1,1,1,1,2,3,3,3,4,5,6,6,8])

