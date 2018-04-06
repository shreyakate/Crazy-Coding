from collections import defaultdict
class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))

	def DFS(self,root):						#Overall O(V+E)
			stack = []
			visited = [False]*(len(self.graph))
			stack.append(root)
			visited[root] = True
			while stack:             #O(V)
				s = stack.pop()
				print s,
				for i in self.graph[s]:		#O(E)
					if visited[i[0]] == False:
						stack.append(i[0])
						visited[i[0]]=True

g = Graph()
g.addEdge(0, 1,1)
g.addEdge(0, 2,1)
g.addEdge(1, 3,1)
g.addEdge(1, 4,1)
g.addEdge(2, 4,1)
g.addEdge(3, 5,1)
g.addEdge(3, 4,1)
g.addEdge(4, 5,1)
g.addEdge(4, 2,1)
g.addEdge(4, 3,1)
g.addEdge(4, 1,1)
g.addEdge(5, 4,1)
g.addEdge(5, 3,1)
g.DFS(0)