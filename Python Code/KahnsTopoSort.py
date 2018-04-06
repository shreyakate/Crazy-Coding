from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.vertices = []
		self.links =[0] * vertices
		self.vert = vertices

	def addEdge(self,u,v):
		if u not in self.vertices:
			self.vertices.append(u)
		if v not in self.vertices:
			self.vertices.append(v)

		self.graph[u].append(v)
		self.links[v] += 1

	def kahnTopoSort(self):
		queue =[]
		visited = 0
		for i in range(len(self.links)):
			if self.links[i]==0:
				queue.append(i)

		while queue:
			u = queue.pop(0)
			print  u,
			visited += 1
			for i in self.graph[u]:
				self.links[i] -= 1
				if self.links[i] == 0:
					queue.append(i)

		if visited == self.vert:
			print True
		else:
			print False

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.kahnTopoSort()