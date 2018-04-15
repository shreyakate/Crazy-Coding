def NextElement2(nums):
	if not nums: return []
	stack,res = [], [-1] *len(nums)
	for i in range(len(nums))*2:
		while stack and  nums[stack[-1]] < nums[i]:
			res[stack.pop()] = nums[i]
		stack.append(i)
	return res

print NextElement2([1,2,1])