import sys
def Sum3Closest(nums,k):
	diff = sys.maxint
	nums.sort()
	i=0
	res =[]
	while i<len(nums)-2:
		start = i+1
		end = len(nums)-1
		while start<end:
			a = nums[i] + nums[start] + nums[end]
			if abs(k-a)<diff:
				diff = abs(k-a)
				res = [nums[i],nums[start], nums[end]]
				if diff == 0:
					return res
			start += 1
			end -= 1
		i +=1
	return res

print Sum3Closest([-1, 2, 1, -4],1)

