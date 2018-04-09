def permuteUnique(nums):
	def backtrack(curr,size):
		if len(curr) == size:
			ans.append(curr[:])
		else:
			for i in range(size):
				print i,curr, visited
				if visited[i] or (i>0 and nums[i-1] == nums[i] and not visited[i-1]):
					continue
				visited[i] = True
				curr.append(nums[i])
				backtrack(curr,size)
				curr.pop()
				visited[i] = False

	ans =[]
	visited = [False] * len(nums)
	nums.sort()
	backtrack([],len(nums))
	return ans

print permuteUnique([1,1,2])

