from collections import defaultdict
class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))


	def BFSUtil(self,u,visited):
		visited[u] = True
		print u,

		if self.graph[u]: 
			for i in self.graph[u]:
				if visited[i[0]] == False:
					self.BFSUtil(i[0],visited)

	def BFS(self):						#Overall O(V+E)
			visited = [False]*(len(self.graph)+1)
			for u, v in self.graph.items():
				if visited[u] == False:
					self.BFSUtil(u,visited)
g = Graph()
g.addEdge(0, 1,1)
g.addEdge(0, 2,1)
g.addEdge(1, 2,1)
g.addEdge(2, 0,1)
g.addEdge(2, 3,1)
g.addEdge(3, 3,1)
g.addEdge(4, 5,1)      #disconnected graph
g.addEdge(4, 6,1)	   #disconnected graph
g.addEdge(5, 6,1)      #disconnected graph
g.BFS()