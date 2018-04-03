from collections import defaultdict
class Graph():
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.V = vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def isCyclic(self):
		visited = [False] * self.V
		stack = [False] * self.V
		for node in range(self.V):
			if visited[node] == False:
				if self.isCyclicUtil(node, visited,stack) == True:
					return True
		return False

	def isCyclicUtil(self,node,visited,stack):
		visited[node] = True
		stack[node] = True
		for neighbour in self.graph[node]:
			if visited[neighbour] == False:
				if self.isCyclicUtil(neighbour,visited, stack) == True:
					return True
			elif stack[neighbour] == True:
				return True
		stack[node] = False
		return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
	print "Graph has a Cycle"
else:
	print "No Cycle detected"


