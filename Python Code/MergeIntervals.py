def MergeIntervals(intervals):
	if not intervals: return []
	if len(intervals) == 1: return intervals


	start = sorted([x[0] for x in intervals])
	end = sorted([x[1] for x in intervals])
	i, j, tmp, rooms = 0,0,0,0
	while i<len(start):
		if end[j]<=start[i]:
			tmp -= 1
			j += 1
		else:
			tmp += 1
			i += 1
		rooms = max(rooms,tmp)

	return rooms

print MergeIntervals([[1,3],[2,6],[8,10],[15,18]])
print MergeIntervals( [[1,4],[4,5]])
print MergeIntervals([[0, 30],[5, 10],[15, 20]])
print MergeIntervals([[0, 10],[10, 20],[25, 30]])
