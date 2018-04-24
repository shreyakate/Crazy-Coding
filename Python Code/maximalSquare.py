def maximalSquare(matrix):
	r, c = len(matrix), len(matrix[0])
	dp = [[0 if matrix[i][j] == 0 else 1 for j in range(c)] for i in range(r)]
	side = -100
	for i in range(1,r):
		for j in range(1,c):
			if matrix[i][j]==1:
					dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
					side = max(dp[i][j],side)
			else:
				dp[i][j] = 0
	
	return side*side


def maxSquare(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] and i and j:
				matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1

	side = max([max(i) for i in matrix])
	return side * side

matrix = [[1,0,1,0,0],
[1,0,1,1,1],
[1,1,1,1,1],
[1,0,0,1,0]]

matrix1 = [[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1]]

print maximalSquare(matrix1)
print maxSquare(matrix)