def IslandPerimeter(grid):
	r = len(grid)
	c = len(grid[0])
	perimeter = 0
	for i in range(r):
		for j in range(c):
			if grid[i][j] == 1: 
				perimeter += 4
				if i != 0 and grid[i-1][j]==1: perimeter -=1 
				if i != r-1 and grid[i+1][j]==1: perimeter -=1
				if j != 0 and grid[i][j-1]==1: perimeter -=1
				if j != c-1 and grid[i][j+1]==1: perimeter -=1
	return perimeter

print IslandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])

# Another solution

# r= len(grid)
# c= len(grid[0])
# count=0
# for i in range(0,r):
#     for j in range(0,c):
#         if(grid[i][j]==1):
#             count += 4
#             if(grid[i-1][j]==1 and i!=0):
#                 count -= 1
#             if(i!=r-1):
#                 if(grid[i+1][j]==1):
#                     count -= 1
#             if(j!=c-1):
#                 if(grid[i][j+1]==1):
#                     count -= 1
#             if(grid[i][j-1]==1 and j!=0):
#                 count -= 1
# return count