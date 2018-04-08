from collections import deque
class Stream:
	def __init__(self,size):
		self.size = size
		self.sum = 0
		self.queue = deque([])

def MovingAverage(dataStream,size):
	s = Stream(size)
	for val in dataStream:
		if len(s.queue) == s.size:
			s.sum -= s.queue.popleft()
		s.sum += val
		s.queue.append(val)
		print 1.0 * s.sum/ len(s.queue)

MovingAverage([1,4,8,2,4,1,2,4,6,8],5)

