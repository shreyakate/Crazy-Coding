def canAttendMeetings(intervals):
	if not intervals: return True
	if len(intervals) == 1: return True

	sorted_intervals = sorted(intervals, key = lambda x: x[0])
	end = sorted_intervals[0][1]   #end time for the 1st interval
	for i in range(1,len(sorted_intervals)):
		if end > sorted_intervals[i][0]:
			return False
		end = sorted_intervals[i][1]
	return True



print canAttendMeetings([[0, 30],[5, 10],[15, 20]])