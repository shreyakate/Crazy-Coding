class CombinationSum2:
	res =[]
	def comnbsum2(self,nums, target):
		self.res =[]
		nums.sort()
		self.calSum(nums,[],target)
		return self.res

	def calSum(self, nums, curr,target):
		if target < 0:
			return
		if target == 0 and curr not in self.res:
			self.res.append(curr)
			return
		if nums:
			self.calSum(nums[1:],curr+[nums[0]], target - nums[0])
			self.calSum(nums[1:],curr, target)

	def backtracking(self,candidates,target):
		def backtrack(tmp,start,end,target):
			if target ==0:
				ans.append(tmp[:])
			elif target >0:
				for i in range(start,end):
					if i > start and candidates[i] == candidates[i-1]:
						continue
					tmp.append(candidates[i])
					backtrack(tmp,i+1,end,target-candidates[i])
					tmp.pop()

		ans =[]
		candidates.sort()
		backtrack([],0,len(candidates),target)
		return ans

cmb = CombinationSum2()
print cmb.comnbsum2([10, 1, 2, 7, 6, 1, 5],8)
print cmb.backtracking([10, 1, 2, 7, 6, 1, 5],8)


