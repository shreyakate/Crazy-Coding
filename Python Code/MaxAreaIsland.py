def MaxAreaIsland(grid):
	def Area(grid, i,j):
		if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1:
			grid[i][j] = 0
			return 1 + Area(grid,i-1,j) + Area(grid,i+1,j) + Area(grid,i,j-1) + Area(grid,i,j+1)
		return 0

	area = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			area = max(area, Area(grid,i,j))
	return area


print MaxAreaIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]])

print MaxAreaIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])


