def DistinctIslands2(grid):
	islands = set()
	r, c = len(grid), len(grid[0])
	directions = [(0,1),(0,-1),(1,0),(-1,0)]

	def DFS(grid,i,j,res):
		if 0<=i<r and 0<=j<c and grid[i][j]==1:
			grid[i][j] =0
			res.append((i,j))
			for d in directions:
				DFS(grid,i+d[0],j+d[1],res)
			return True
		return False

	def normalize(islands):
		shapes = [[] for _ in xrange(8)]
		for x,y in islands:
			rotations_reflections = [ [x,y], [x,-y], [-x,y], [-x,-y], [y,x], [y,-x], [-y,x], [-y,-x]]

			for i in xrange(len(rotations_reflections)):
				shapes[i].append(rotations_reflections[i])

		for shape in shapes:
			shape.sort()   # Time O(nlogn) ...where n is size of islands, that would be max r*c
			origin = list(shape[0])
			for p in shape:
				p[0] -= origin[0]
				p[1] -= origin[1]
			return min(shapes)

	for i in range(r):
		for j in range(c):
			isl
			if DFS(grid,i,j,[]):
				islands.add(str(normalize()))
	print len(islands)

DistinctIslands2([
	[1,1,0,0],
	[1,1,0,0],
	[0,0,1,1],
	[0,0,1,1]])

DistinctIslands2([
	[1,1,1,0,0],
	[1,0,0,0,1],
	[0,1,0,0,1],
	[0,1,1,1,0]])