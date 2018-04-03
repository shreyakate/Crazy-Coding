class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None 

def EqualBinaryTree(tree1,tree2):
	if tree1 is None and tree2 is None : 
		return True
	if tree1 and tree2:
		return ((tree1.data == tree2.data) 
			     and EqualBinaryTree(tree1.left,tree2.left) 
			     and EqualBinaryTree(tree1.right,tree2.right))
	else:
		return False

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.right = Node(4)
root1.right.left = Node(5)
root1.right.right = Node(6)
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.right = Node(4)
root2.right.left = Node(5)
root2.right.right = Node(7)
print EqualBinaryTree(root1,root2)