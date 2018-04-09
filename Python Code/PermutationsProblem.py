class PermutationsProblem:
	res = []
	def permuations(self,nums):
		self.res = []
		self.genPerms(nums,0)
		return self.res

	def genPerms(self,nums,start):
		if start >= len(nums):
			self.res.append(nums[:])

		for i in range(start, len(nums)):
			nums[start], nums[i] = nums[i],nums[start]
			self.genPerms(nums,start+1)
			nums[start], nums[i] = nums[i],nums[start]

	def backtracking(self,nums):
		def backtrack(start,end):
			if start == end:
				ans.append(nums[:])
			for i in range(start,end):
				nums[start], nums[i] = nums[i],nums[start]
				backtrack(start+1,end)
				nums[start], nums[i] = nums[i],nums[start]
		
		ans =[]
		backtrack(0,len(nums))
		return ans


p = PermutationsProblem()
print p.permuations([1,2,3])
print p.backtracking([1,2,3])



