from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def detectCycleUndirectedUtil(self, v, visited,parent):
		visited[v] = True

		for i in self.graph[v]:
			if visited[i] == False:
				if(self.detectCycleUndirectedUtil(i,visited,v)):
					return True
			elif parent != i:
				return True

		return False
	def detectCycleUndirected(self):
		visited = [False] * self.vertices

		for  i in range(self.vertices):
			if visited[i] == False:
				if (self.detectCycleUndirectedUtil(i,visited,-1)):
					return True
		return False

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
if g.detectCycleUndirected():
    print "Graph contains cycle"
else :
    print "Graph does not contain cycle "
g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)
 
if g1.detectCycleUndirected():
    print "Graph contains cycle"
else :
    print "Graph does not contain cycle "