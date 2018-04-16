class UndirectedGraphNode:
	def __init__(x):
		label = x
		neighbors = []

def CloneGraph(node):

	if not node:
		return 

	cloneNode = UndirectedGraphNode(node.label)
	d = {node: cloneNode}

	stack = [node]

	while stack: 
		node = stack.pop()
		for neighbor in node.neighbors:
			if neighbor not in d:
				neighborClone = UndirectedGraphNode(neighbor.label)
				d[neighbor] = neighborClone
				d[node].neighbors.append(neighborClone)
				stack.append(neighbor)
			else: 
				d[neighbor].neighbors.append(d[neighbor])
	return cloneNode

def CloneGraphBFS(node):
	if not node: return 
	
	nodeCopy = UndirectedGraphNode(node.label)
	d = {node: nodeCopy}

	queue = [node]
	while queue:
		node = queue.pop(0)
		for neighbor in node.neighbors:
			if neighbor not in d:
				neighborCopy = UndirectedGraphNode(neighbor.label)
				d[neighbor] = neighborCopy
				d[node].neighbors.append(neighborCopy)
				queue.append(neighbor)
			else:
				d[neighbor].neighbors.append(d[neighbor])
	return nodeCopy