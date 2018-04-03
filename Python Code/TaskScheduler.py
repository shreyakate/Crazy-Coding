import heapq

import collections 

def fastestTaskSequence(tasks, n):
	frequencies = dict()
	a = []
	for ch in tasks:
		if ch in frequencies:
			frequencies[ch] += 1
		else:
			frequencies[ch] = 1
	for key, val in frequencies.iteritems():
		heapq.heappush(a, [-val, key])
	result = ''
	while len(a):
		temp = []
		for i in range(n+1):
			if len(a):
				task = heapq.heappop(a)
				result += task[1]
				temp.append(task)
			else:
				break
		itemPushed = len(temp)
		while len(temp):
			task = temp.pop()
			task[0] -= 1
			if task[0] > 0:
				heapq.heappop(a, task)
		if len(a):
			result += '_' * (n+1-itemPushed)
	return result

print fastestTaskSequence('AAABBB', 2)