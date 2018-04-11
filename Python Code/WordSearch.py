def WordSearch(board,word):
	r, c = len(board), len(board[0])

	def DFS(i,j, word):
		if len(word)==0:
			return True
		if i>=0 and j>=0 and i<r and j < c and board[i][j] == word[0]:
			tmp = board[i][j]
			board[i][j] = '#'
			res = DFS(i+1,j, word[1:]) or DFS(i-1,j, word[1:]) or DFS(i,j-1, word[1:]) or DFS(i,j+1, word[1:])
			board[i][j] = tmp
			return res
		else:
			return False
	
	for i in range(r):
		for j in range(c):
			if board[i][j] == word[0] and DFS(i,j, word):
				return True
	return False
			
	

a= [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print WordSearch(a,"ABCB")
print WordSearch(a,"ABCCED")
print WordSearch(a,"SEE")

