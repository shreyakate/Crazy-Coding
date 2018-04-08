def IsolatedIslands(grid):
	count = 0
	r, c = len(grid), len(grid[0])
	def VisitIsland(grid,i,j):
		if grid[i][j] ==1:
			grid[i][j] =0
			VisitIsland(grid, (i+1)%r, j%c)
			VisitIsland(grid, (i-1)%r, j%c)
			VisitIsland(grid, i%r, (j+1)%c)
			VisitIsland(grid, i%r, (j-1)%c)
			return
		return

	for i in range(r):
		for j in range(c):
			if grid[i][j]==1:
				VisitIsland(grid,i,j)
				count += 1
	return count

print IsolatedIslands([
	[0,0,1,1],
	[0,0,0,0],
	[0,0,1,1],
	[0,0,1,1]])

print IsolatedIslands([
	[1,1,1,1,0],
	[1,1,0,1,0],
	[1,1,0,0,0],
	[0,0,0,0,0]])

print IsolatedIslands([
	[1,1,0,0,0],
	[1,1,0,0,0],
	[0,0,1,0,0],
	[0,0,0,1,1]])

print IsolatedIslands([[1,0,1,1,0,1,1]])
