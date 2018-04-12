class Solution(object):
    res = []
    def genSets(self,curr,nums):
        if curr not in self.res:
            self.res.append(curr) 
        if nums:
            self.genSets(curr,nums[1:])
            self.genSets(curr+[nums[0]],nums[1:]) 
        else:
            return
        
    def subsets(self, nums):
        self.res =[]
        nums.sort()
        self.genSets([],nums)
        return self.res

s = Solution()
print s.subsets([4,4,4,1,4])

def subsetters2(nums):
    def backtrack(start,end,curr):
        ans.append(curr[:])
        for i in range(start,end):
            if i>start and nums[i-1] ==nums[i]:
                continue
            curr.append(nums[i])
            backtrack(i+1,end,curr)
            curr.pop()
    
    ans =[]
    nums.sort()
    backtrack(0,len(nums),[])
    return ans

print subsetters2([1,2,2])


