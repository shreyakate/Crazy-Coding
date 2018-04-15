def decodeWays(s):
	if not s or len(s) == 0:
		return 0

	n = len(s)
	dp = [0 for _ in range(n+1)]
	dp[0] = 1
	dp[1] = 1 if s[0] != '0' else 0
	for i in range(2,n+1):
		prev, last = int(s[i-1]), int(s[i-2:i])
		print prev , last
		if prev >=1 and prev <=9:
			dp[i] += dp[i-1]
		if last >= 10 and last <=26:
			dp[i] += dp[i-2]
	return dp[n]

print decodeWays("123")



