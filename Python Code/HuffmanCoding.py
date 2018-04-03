import heapq
class HuffmanNode:
	freq = 0
	ch = left = right = None
	def __init__(self,left,ch,freq,right):
		self.left = left
		self.ch = ch
		self.freq = freq
		self.right = right
class Heap(object):
    def __init__(self):
        self._heap = []

    def push(self, freq, node):
        # assert freq >= 0
        heapq.heappush(self._heap, (freq, node))

    def pop(self):
        freq,node = heapq.heappop(self._heap) 
        return (freq,node)

    def __len__(self):
        return len(self._heap)

def HuffmanCoding(chars,freq):
	heap = Heap()
	for i in range(len(chars)):
		x = HuffmanNode(None,chars[i],freq[i],None)
		heap.push(x.freq,x)

	root = None
	while len(heap)>1:
		afreq,a = heap.pop()
		bfreq,b = heap.pop()
		print a.ch, afreq, b.ch, bfreq
		root = HuffmanNode(a,'-',afreq + bfreq,b)
		heap.push(root.freq,root) 
	printHuffman(root,"")

def printHuffman(root, s):
	if root.left is None and root.right is None and root.ch:
		print root.ch + " : " + s
		return
	printHuffman(root.left, s+'0')
	printHuffman(root.right, s+'1')

HuffmanCoding(['a','b','c','d','e','f'],[5,9,12,13,16,45])






		

