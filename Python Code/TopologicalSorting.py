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

	def topoSortUtil(self,u,visited,stack):
		visited[ord(u)-ord('A')] = True

		for i in self.graph[u]:
			if visited[ord(i)-ord('A')] == False:
				self.topoSortUtil(i,visited,stack)

		stack.insert(0,u)

	def topologicalSort(self):
		stack = []
		visited = [False]*(len(self.vertices))

		for i in self.vertices:
			if visited[ord(i)-ord('A')] == False:
				self.topoSortUtil(i,visited,stack)

		print stack

# g = Graph()
# g.addEdge(5, 2)
# g.addEdge(5, 0)
# g.addEdge(4, 0)
# g.addEdge(4, 1)
# g.addEdge(2, 3)
# g.addEdge(3, 1)
# g.topologicalSort()

g1 = Graph()
g1.addEdge('A','B')
g1.addEdge('A','F')
g1.addEdge('G','A')
g1.addEdge('G','B')
g1.addEdge('B','H')
g1.addEdge('G','C')
g1.addEdge('I','C')
g1.addEdge('D','H')
g1.addEdge('D','C')
g1.addEdge('D','I')
g1.addEdge('D','E')
g1.addEdge('E','I')
g1.addEdge('J','E')
g1.topologicalSort()