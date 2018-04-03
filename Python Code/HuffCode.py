import heapq
class HuffmanNode:
	freq = 0
	ch = left = right = None
	def __init__(self,left,ch,freq,right):
		self.left = left
		self.ch = ch
		self.freq = freq
		self.right = right

def HuffmanCoding(chars,freq):
	heap = []
	for i in range(len(chars)):
		x = HuffmanNode(None,chars[i],freq[i],None)
		heapq.heappush(heap,(x.freq,x))

	root = None
	while len(heap)>1:
		afreq,a = heapq.heappop(heap)
		bfreq,b = heapq.heappop(heap)
		print a.ch, afreq, b.ch, bfreq
		root = HuffmanNode(a,'-',afreq + bfreq, b)
		heapq.heappush(heap,(root.freq,root)) 
	printHuffman(root,"")

def printHuffman(root, s):
	if root.left is None and root.right is None and root.ch:
		print root.ch + " : " + s
		return
	printHuffman(root.left, s+'0')
	printHuffman(root.right, s+'1')

HuffmanCoding(['a','b','c','d','e','f'],[5,9,12,13,16,45])






		

