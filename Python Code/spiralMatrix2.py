def spiralMatrix2(n):
	res = [[0 for _ in range(n)] for _ in range(n)]
	i, mini, maxi = 0,0, n-1
	j, minj, maxj = 0,0, n-1
	num = 1
	while mini <=i <= maxi:
		while j <= maxj and mini <=i <= maxi:
			res[i][j] = num
			num += 1
			j += 1
		j -= 1
		mini += 1
		i += 1
		while i<= maxi and minj <= j <= maxj:
			res[i][j] = num
			num += 1
			i += 1
		i -=1 
		maxj -= 1
		j -= 1
		while j>=minj and mini <=i <= maxi:
			res[i][j] = num
			num += 1
			j -= 1
		j += 1
		maxi -= 1
		i -= 1
		while i>= mini and minj <= j <= maxj:
			res[i][j] = num
			num += 1
			i -= 1
		i += 1
		minj +=1 
		j += 1
	return res

print spiralMatrix2(4)
# 0 0
# 0 1
# 0 2
# 1 2
# 2 2
# 2 1
# 2 0
# 1 0
# 1 1