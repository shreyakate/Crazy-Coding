def WordBreak(s,dict):
	if not s: return True

	dp = [False]*(len(s)+1)
	dp[0] = True
	for i in range(len(s)):
		for j in range(i,len(s)):
			if dp[i]  and s[i:j+1] in dict:
				dp[j+1] = True

	print dp
	return dp[-1]
print WordBreak("leetcode",["leet","code"])
print WordBreak("geeksforgeeks",["Geeks","for"])
print WordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])


