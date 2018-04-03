
def ActivitySelection(start,finish):
	if len(start) !=len(finish): 
		return []

	times_list = [[start[i],finish[i]] for i in range(len(start))]   	# t: n 	    s: n
	sorted_list = sorted(times_list ,key =lambda x: x[1]) 				# t: nlogn  s: n
	
	res = [sorted_list[0]]												# t: 1 		s: n

	for i in range(1,len(sorted_list)):
		if res[-1][1] <= sorted_list[i][0]:
			res.append(sorted_list[i])
	return res

print ActivitySelection([1,0,3,5,8,5],[2,6,4,7,9,9])
print ActivitySelection([10,12,20],[20,25,30])
print ActivitySelection([5,1,3,0,5,8],[9,2,4,6,7,9])
print ActivitySelection([1],[2])

