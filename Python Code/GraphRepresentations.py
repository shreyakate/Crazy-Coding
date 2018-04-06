class Node:
	def __init__(self,data, weight):
		self.data = data
		self.weight = weight
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self,data,weight):
		node = Node(data,weight)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = self.tail.next
		self.tail.next = None

	def printList(self):
		curr = self.head
		while curr:
			print (curr.data,curr.weight),
			curr = curr.next

class Graph:
	def __init__(self,vertices):
		self.vertices = vertices
		self.graph = [[ 0 for _ in range(vertices)] for _ in range(vertices)]
		self.adjList = [None for _ in range(vertices)]

	def addEdge(self,u,v,w):
		if 0<=u<len(self.graph) and 0<=v<len(self.graph):
			self.graph[u][v] = w
		if self.adjList[u] == None: 
			self.adjList[u] = LinkedList()
			self.adjList[u].addNode(v,w)
		else:
			self.adjList[u].addNode(v,w)

	def printGraph(self):
		for i in range(len(self.graph)):
			for j in range(len(self.graph)):
				print self.graph[i][j],
			print ''

		for i in range(len(self.adjList)):
			if self.adjList[i]:
				print "Vertex" + str(i),
				print self.adjList[i].printList()
			else:
				print "Vertex" + str(i) + " " +str(None)

				

g = Graph(5)
g.addEdge(0, 1,1);
g.addEdge(0, 4,1);
g.addEdge(1, 2,1);
g.addEdge(1, 4,1);
g.addEdge(2, 3,1);
g.addEdge(3, 4,1);

g.printGraph()