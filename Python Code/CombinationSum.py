class CombinationSum:
	res =[]

	def CombSum(self, nums, target):
		self.res =[]
		self.calSum(nums,[],target)
		return self.res

	def calSum(self, nums, curr, target):
		if target < 0: return 
		if target == 0: 
			self.res.append(curr)
			return 
		if nums:
			self.calSum(nums,curr+[nums[0]], target - nums[0])
			self.calSum(nums[1:],curr, target)

	def backtracking(self, candidates, target):
		def backtrack(tmp,start, end, target):
			print tmp,start, end, target,
			if target ==0:
				ans.append(tmp[:])
			elif target>0:
				for i in range(start,end):
					print i, tmp
					tmp.append(candidates[i])
					backtrack(tmp,i,end,target - candidates[i])
					tmp.pop()
		ans =[]
		candidates.sort(reverse = True)
		backtrack([],0,len(candidates),target)
		return ans

cmb = CombinationSum()

#print cmb.CombSum([2,3,6,7],7)
print cmb.backtracking([2,3,6,7],7)
