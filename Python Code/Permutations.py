def Permutations(nums):
	perms =[[]]
	for n in nums:
		newPerm =[]
		for perm in perms:
			for i in xrange(len(perm)+1):
				newPerm.append(perm[:i] + [n] + perm[i:])
		perms = newPerm
	return perms

print Permutations([1,2,3])


