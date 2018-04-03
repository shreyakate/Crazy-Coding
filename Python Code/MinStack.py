import sys
class MinStack:
	def __init__(self):
		self.stack = []
		self.mins = sys.maxint

	def push(self,data):
		if data <= self.mins:
			self.stack.append(self.mins)
			self.mins = data
		self.stack.append(data)

	def peek(self):
		if len(self.stack)>=1 :
			return self.stack[-1]
		return -1

	def pop(self):
		if len(self.stack)<1: 
			return -1
		x = self.stack.pop()
		if x == self.mins:
			self.mins = self.stack.pop()
		return x

	def getMin(self):
		return self.mins

stack = MinStack()
stack.push(-2)
stack.push(0)
print stack.getMin()
stack.push(-3)
print stack.getMin()
print stack.pop()
print stack.peek()
print stack.getMin()

