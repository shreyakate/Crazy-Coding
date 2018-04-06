from collections import defaultdict
class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))

	def BFS(self,root):						#Overall O(V+E)
			queue = []
			visited = [False]*(len(self.graph))
			queue.append(root)
			visited[root] = True
			while queue:                    #O(V)
				s = queue.pop(0)
				print s,
				for i in self.graph[s]:		#O(E)
					if visited[i[0]] == False:
						queue.append(i[0])
						visited[i[0]]=True

g = Graph()
g.addEdge(0, 1,1)
g.addEdge(0, 2,1)
g.addEdge(1, 2,1)
g.addEdge(2, 0,1)
g.addEdge(2, 3,1)
g.addEdge(3, 3,1)
g.addEdge(5,6,1)      #disconnected graph
g.addEdge(5,7,1)
g.addEdge(7,6,1)
g.BFS(2)