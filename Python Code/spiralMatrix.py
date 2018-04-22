def spiralMatrix(matrix):
	mini, minj, maxi, maxj = 0, 0 , len(matrix)-1, len(matrix[0])-1
	i, j = mini, minj
	res= []
	while mini <=i <= maxi:
		while j <= maxj and mini <=i <= maxi:
			print  i,j
			res.append(matrix[i][j])
			j += 1
		j -= 1
		mini += 1
		i += 1
		while i<= maxi and minj <= j <= maxj:
			print i,j
			res.append(matrix[i][j])
			i += 1
		i -=1 
		maxj -= 1
		j -= 1
		while j>=minj and mini <=i <= maxi:
			print i,j
			res.append(matrix[i][j])
			j -= 1
		j += 1
		maxi -= 1
		i -= 1
		while i>= mini and minj <= j <= maxj:
			print  i,j
			res.append(matrix[i][j])
			i -= 1
		i += 1
		minj +=1 
		j += 1
	return res


matrix = [ [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]

matrix1 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

matrix2 = [ [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [10,11,12],
 [13,14,15]]
print spiralMatrix(matrix) == [1,2,3,6,9,8,7,4,5]
# print spiralMatrix(matrix1) == [1,2,3,4,8,12,11,10,9,5,6,7]
# print spiralMatrix(matrix2) == [1,2,3,6,9,12,15,14,13,10,7,4,5,8,11]
# 0,0
# 0,1
# 0,2
# 0,3

# 1,3
# 2,3

# 2,2
# 2,1
# 2,0

# 1,0
# 1,1
# 1,2
# 1,1 