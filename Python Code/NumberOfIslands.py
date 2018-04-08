def NumberOfIslands(grid):
    if not grid: return 0
    r,c = len(grid), len(grid[0])
    count = 0
    
    def VisitIsland(grid,i,j):
        if 0<=i<r and 0<=j<c and grid[i][j]=='1':
            grid[i][j] ='0'
            VisitIsland(grid,(i+1),j)
            VisitIsland(grid,(i-1),j)
            VisitIsland(grid,i,(j+1))
            VisitIsland(grid,i,(j-1))
            return
        return
    
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='1':
                VisitIsland(grid,i,j)
                count += 1
    return count

print NumberOfIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print NumberOfIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print NumberOfIslands([])