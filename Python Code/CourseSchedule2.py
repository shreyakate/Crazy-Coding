from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.vertices = []

	def addEdge(self,u,v):
		if u not in self.vertices:
			self.vertices.append(u)
		if v not in self.vertices:
			self.vertices.append(v)

		self.graph[u].append(v)

	def detectCycleUtil(self,v,visited,recStack):
		visited[v] = True
		recStack[v] = True

		for neighbour in self.graph[v]:
			if visited[neighbour] == False:
				if self.detectCycleUtil(neighbour,visited,recStack) == True:
					return True
			elif recStack[neighbour] == True:
				return True

			recStack[v] = False
			return False

	def detectCycle(self):
		visited = [False]*(len(self.vertices))
		recStack = [False]*(len(self.vertices))
		for node in range(len(self.vertices)):
			if visited[node] == False:
				if self.detectCycleUtil(node,visited,recStack) == True:
					return True
		return False

	def topoSortUtil(self,u,visited,stack):
		visited[u] = True

		for i in self.graph[u]:
			if visited[i] == False:
				self.topoSortUtil(i,visited,stack)

		stack.insert(0,u)

	def topologicalSort(self):
		stack = []
		visited = [False]*(len(self.vertices))

		for i in self.vertices:
			if visited[i] == False:
				self.topoSortUtil(i,visited,stack)

		print stack


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(3, 4)
# g.addEdge(4,2)
if  g.detectCycle() : print []
else:
	g.topologicalSort()