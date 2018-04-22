from collections import deque
class DataStream:
	def __init__(self,size):
		self.size = size
		self.stream = deque([])
		self.sum = 0

def MovingAvg(dataStream,size):
	s = DataStream(size)

	for data in dataStream:
		if len(s.stream) == size:
			s.sum -= s.stream.popleft()
			s.stream.append(data)
			s.sum += data
		else:
			s.stream.append(data)
			s.sum += data
		print s.sum*1.0/len(s.stream),

MovingAvg([1,4,8,2,4,1,2,4,6,8],5)
print " next"
MovingAvg([1,10,3,5,7,6],3)