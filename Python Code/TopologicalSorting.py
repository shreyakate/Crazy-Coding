from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def topoSortUtil(self,u,visited,stack):
		visited[u] = True

		for i in self.graph[u]:
			if visited[i] == False:
				self.topoSortUtil(i,visited,stack)

		stack.insert(0,u)

	def topologicalSort(self):
		stack = []
		visited = [False]*self.vertices

		for i in range(self.vertices):
			if visited[i] == False:
				self.topoSortUtil(i,visited,stack)

		print stack

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()