class SubsetProblem:
	res =[]
	def subsets(self,nums):
		self.res =[]
		self.subs([],nums)
		return self.res

	def subs(self,curr,nums):
		if curr not in self.res:
			self.res.append(curr)
		if nums:
			self.subs(curr+[nums[0]],nums[1:])
			self.subs(curr,nums[1:])
		else: 
			return

	def backtracking(self,nums):
		def backtrack(curr,start,end):
			ans.append(curr[:])
			for i in range(start, end):
				if i > start and nums[i] == nums[i-1]:
					continue 
				curr.append(nums[i])
				backtrack(curr,i+1,end)
				curr.pop()
		ans =[]
		nums.sort()
		backtrack([],0,len(nums))
		return ans


s = SubsetProblem()
print s.subsets([1,2,3])
print s.backtracking([1,2,3])
print s.subsets([1,2,2])
print s.backtracking([1,2,2])

