class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def firstDifferentNode(tree1,tree2):
	if tree1 is None and tree2 is None:
		return None
	elif tree1 is None and tree2 is not None:
		return tree2.data
	elif tree2 is None and tree1 is not None:
		return tree1.data
	elif tree1 and tree2:
		if tree1.data != tree2.data:
			return tree1.data
		return firstDifferentNode(tree1.left,tree2.left) or  firstDifferentNode(tree1.right, tree2.right)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.right = Node(4)
root1.right.left = Node(5)
root1.right.right = Node(6)
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(5)
root2.left.right = Node(4)
root2.right.left = Node(5)
root2.right.right = Node(7)

print firstDifferentNode(root1,root2)


