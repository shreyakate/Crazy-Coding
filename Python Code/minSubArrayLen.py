import sys
def minSubArrayLen(s, nums):
	start = end = total = 0 
	minLen = sys.maxint

	while end<len(nums):
		if total<s: 
			total += nums[end]
			end += 1
		while total>=s:
			if (end - start<minLen):
				minLen = end -start
			total -= nums[start]
			start += 1
	
	return minLen

print minSubArrayLen(7,[2,3,1,2,4,3])