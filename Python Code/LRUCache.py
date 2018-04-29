from collections import OrderedDict
class LRUCache:

	def __init__(self,capacity):
		self.capacity = capacity 
		self.cache = OrderedDict()
		self.size = 0

	def get(self, key):
		if self.cache.has_key(key):
			value = self.cache[key]
			# print self.cache , key,
			del self.cache[key]
			self.size -= 1
			# print self.cache
			self.put(key,value)
			return value
		else:
			return -1

	def put(self, key, value):
		if self.cache.has_key(key):
			del self.cache[key] 
			self.cache[key] = value
			self.size -= 1
            
		elif self.size == self.capacity:
			keyur = self.cache.keys()[0]
			del self.cache[keyur]
			self.size -= 1
            
		self.size += 1
		self.cache[key] = value


cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
cache.put(1, 1)
cache.put(2, 2)
print cache.get(1)       # returns 1
cache.put(3, 3)    #evicts key 2
print cache.get(2)      # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print cache.get(1)       # returns -1 (not found)
print cache.get(3)       #// returns 3
print cache.get(4)       #// returns 4



