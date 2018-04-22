def CourseSchedule(numCourses, prerequisites):
	graph = [ [] for _ in xrange(numCourses)]
	visit = [ 0 for _ in xrange(numCourses)]

	for x,y in prerequisites:
		graph[x].append(y)

	def DFS(v):
		if visit[v] == -1: return False
		if visit[v] == 1: return True
		visit[v] = -1

		for u in graph[v]:
			if not DFS(u):
				return False
		visit[v] = 1
		return True

	for i in xrange(numCourses):
		if not DFS(i):
			return False
	return True

print CourseSchedule(5,[[1,0],[3,1],[3,2],[4,3],[0,2],[2,4]])


