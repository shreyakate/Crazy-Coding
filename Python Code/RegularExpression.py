def RegularExpression(s, p):
	m = len(s)
	n = len(p)

	dp = [[False] * (m+1) for _ in range(n+1)]
	dp[0][0] = True

	for i  in xrange(1,n+1):
		x = p[i-1]
		if x == '*' and i > 1:
			dp[i][0] = dp[i-2][0]

		for j in xrange(1, m+1):
			if x == '*':
				dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and p[i-2] == s[j-1]) or (dp[i][j-1] and p[i-2]=='.')
			elif x == '.' or x == s[j-1]:
				dp[i][j] = dp[i-1][j-1]

	return dp[-1][-1]


print RegularExpression("aab","c*a*b")