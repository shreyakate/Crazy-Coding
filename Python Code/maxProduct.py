def maxProduct(nums):
	n = len(nums)
	max_end = min_end = max_so_far = nums[0]
	for m in nums[1:]:
		max_end, min_end=max(m, m*max_end, m*min_end), min(m, m*max_end, m*min_end)
		max_so_far=max(max_so_far, max_end)
		
	return max_so_far

print maxProduct([2,3,-2,4])
print maxProduct([-2,0,-1])
print maxProduct([2,3,10,17,-5,-19,-1,-2,4])
print maxProduct([1, -2, -3, 0, 7, -8, -2])

