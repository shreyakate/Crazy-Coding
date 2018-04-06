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

	def AllTopoSortUtil(self,result,visited):
		flag = False
		for i in range(self.vert):
			if self.links[i]==0 and not visited[i]:
				for j in self.graph[i]:
					self.links[j] -= 1

				result.append(i)
				# print result, self.links
				visited[i] = True
				self.AllTopoSortUtil(result,visited)
				print i
				visited[i] = False
				result.pop()
				for j in self.graph[i]:
					self.links[j] += 1
				
				flag = True

		if not flag:
			print result

	def AllTopoSort(self):
		result =[]
		visited = [False] * self.vert
		print self.links
		self.AllTopoSortUtil(result,visited)
		

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.AllTopoSort()