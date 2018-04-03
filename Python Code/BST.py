class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def insert(self,root,node):
		if root is None:
			root = node
		elif root.data < node.data:
			if root.right is None:
				root.right = node
			else:
				self.insert(root.right,node)
		else:
			if root.left is None:
				root.left = node
			else:
				self.insert(root.left,node)

	def contains(self,root,data):
		if  root is None or root.data == data:
			return root.data if root else None
		elif root.data<data:
			return self.contains(root.right,data)
		else:
			return self.contains(root.left,data)

	def inOrder(self,root):
		if not root:
			return 
		self.inOrder(root.left)
		print root.data
		self.inOrder(root.right)

r = Node(50)
b = BST()
b.insert(r,Node(30))
b.insert(r,Node(20))
b.insert(r,Node(40))
b.insert(r,Node(70))
b.insert(r,Node(60))
b.insert(r,Node(80))
print b.contains(r,60)
print b.contains(r,90)
b.inOrder(r)