from collections import defaultdict
def TrieNode:
	def __init__(self):
		self.children = defaultdict(TrieNode)
		self.isEnd = False


def Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self,word):
		curr = self.root
		for ch in word:
			curr = curr.child[ch]
		curr.isEnd = True

	def search(self,word):
		curr = self.root
		for ch in word:
			curr = curr.child.get(ch)
			if not curr:
				return False
		return curr.isEnd 

	def startsWith(self,prefix):
		curr = self.root
		for ch in prefix:
			curr = curr.child.get(ch)
			if not curr:
				return False
		return True

	
