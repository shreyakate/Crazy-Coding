from collections import defaultdict
def BestAverage(grades):
	d = defaultdict(list)
	bestAvg = 0
	person = ''
	for i in grades:
		d[i[0]].append(i[1])
		if sum(d[i[0]])/len(d[i[0]]) > bestAvg:
			bestAvg = sum(d[i[0]])/len(d[i[0]])
			person = i[0]
	print person + " " + str(bestAvg)

BestAverage([["Alice", 85],["Bob",95],["Alice",100],["Chandler",92],["Alice",100],["Alice",100]])