def allowOneDuplicate(nums):
	if len(nums)<2: return nums
	i, curr, prev = 2, nums[1], nums[0]

	while i < len(nums):
		if nums[i] == prev:
			nums.pop(i)
		else:
			prev =curr
			curr = nums[i]
			i += 1
	return nums

def anotherMethod(nums):   #No clue whats happenening
	i = 0
	print nums
	for n in nums:
		print nums[:i+1]
		if i < 2 or n > nums[i-2]:
			nums[i] = n
			i += 1
	return nums

print allowOneDuplicate([1,1,1,1,1,1,2,3,3,3,4,5,6,6,8])
print anotherMethod([1,1,1,1,1,1,2,3,3,3,4,5,6,6,8])
