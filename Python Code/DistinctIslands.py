def DistinctIslands(grid):
	islands = []
	r, c = len(grid), len(grid[0])

	def DFS(grid,i,j,topx,topy,res):
		if 0<=i<r and 0<=j<c and grid[i][j]==1:
			grid[i][j] =0
			res.append((i-topx,j-topy))
			DFS(grid,i-1,j,topx,topy,res)
			DFS(grid,i+1,j,topx,topy,res)
			DFS(grid,i,j-1,topx,topy,res)
			DFS(grid,i,j+1,topx,topy,res)
			return res
		return 
	for i in range(r):
		for j in range(c):
			if grid[i][j]==1:
				x = DFS(grid,i,j,i,j,[])
				if x:
					islands.append(tuple(x))
	print len(set(islands))
DistinctIslands(
	[
	[1,1,0,0],
	[1,1,0,0],
	[0,0,1,1],
	[0,0,1,1]])
DistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]])

DistinctIslands(
[[1, 1, 1, 1], 
 [1, 0, 1, 0], 
 [0, 0, 0, 0],
 [0, 1, 1, 1], 
 [1, 1, 0, 1]])