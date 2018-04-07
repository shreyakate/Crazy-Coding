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

	def detectCycle(self,root):
		visited = [False]*(len(self.vertices))
		stack = []
		stack.append(root)
		while stack:
			node = stack.pop()
			if visited[node] == True:
				return True
			visited[node] = True
			for i in self.graph[node]:
				stack.append(i)
		return False

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print g.detectCycle(0)