from collections import defaultdict
def longestConsecutive(nums):
	d ={}
	maxLen = 0
	for n in nums:
		if d.has_key(n):
			continue
		start = end = n
		if d.has_key(n+1):
			end = d[n+1][1]
		if d.has_key(n-1):
			start = d[n-1][0]
		d[start] = d[end] = d[n] = (start,end)
		maxLen = max(end-start+1,maxLen)
	return maxLen

print longestConsecutive([100,4,200,1,3,2,101,105,103,102,104])