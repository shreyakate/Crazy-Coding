class HuffmanNode:
	freq = 0
	ch = left = right = None
	def __init__(self,left,ch,freq,right):
		self.left = left
		self.ch = ch
		self.freq = freq
		self.right = right

def HuffmanSorted(chars, freq):
	q1 = q2 =[]
	# for i in range(len(chars)):
	# 	q1.append((chars[i],freq[i]))
	q1 = [HuffmanNode(None,chars[i],freq[i],None) for i in range(len(chars))]
	root = None
	last = False
	while q1 or q2:
		if q1 and q2:
			if q1[0].freq<q2[0].freq:
				a = q1.pop(0)
				b = q2.pop(0)
			else:
				a = q2.pop(0)
				b = q1.pop(0)
		elif q1:
			a = q1.pop(0)
			b = q1.pop(0)
		elif q2:
			a = q2.pop(0)
			if q2:
				b = q2.pop(0)
			else: 
				last = True
		print a.ch, a.freq, b.ch, b.freq
		root = HuffmanNode(a,'-',a.freq+b.freq,b)
		if not last:
			q2.append(root)
	printHuffman(root,'')

def printHuffman(root, s):
	if root.left is None and root.right is None and root.ch:
		print root.ch + " : " + s
		return
	printHuffman(root.left, s+'0')
	printHuffman(root.right, s+'1')
HuffmanSorted(['a','b','c','d','e','f'],[5,9,12,13,16,45])