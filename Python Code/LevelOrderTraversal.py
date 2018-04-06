class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


def levelOrderTraversal(root):
	queue =[]
	queue.append(root)
	while queue:
		node = queue.pop(0)
		if node:
			print node.data, 
			queue.append(node.left)
			queue.append(node.right)

def height(root):
	if root is None:
		return 0
	return max(height(root.left),height(root.right)) +1

def printlevelOrder(root):
	h = height(root)
	for i in range(1,h+1):
		printGivenLevel(root,i)

def printGivenLevel(root, level):
	if root is None:
		return
	if level == 1:
		print root.data,
	elif level >1:
		printGivenLevel(root.left, level-1)
		printGivenLevel(root.right, level-1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

levelOrderTraversal(root)
print ''
printlevelOrder(root)