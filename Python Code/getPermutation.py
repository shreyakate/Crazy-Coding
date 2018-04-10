# def getPermutation(n,k):

# 	# nums = ''.join([''+str(i) for i in range(1,n+1)])
# 	nums = [i for i in range(1,n+1)]
# 	def backtrack(start,end,count):
# 		if start == end:
# 			ans.append(nums[:])
			
# 		else:
# 			for i in range(start,end):
# 				nums[start],nums[i]=nums[i],nums[start]
# 				backtrack(start+1,end,count)
# 				nums[start],nums[i]=nums[i],nums[start]

# 	ans = []
# 	backtrack(0,len(nums),1)
# 	return ''.join(str(i) for i in ans[k-1])

def getPermutation( n, k):       #executes very fast!!!
        nums = [str(i) for i in range(1, n+1)]
        fact = [1] * n
        for i in range(1,n):
            fact[i] = i*fact[i-1]
        k -= 1
        ans = []
        for i in range(n, 0, -1):
            id = k / fact[i-1]
            k %= fact[i-1]
            ans.append(nums[id])
            nums.pop(id)
            print i, id, k, nums, fact[i-1], ans
        return ''.join(ans)

print getPermutation(9,40001)