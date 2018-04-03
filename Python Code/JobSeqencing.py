def JobSeqencing(job):
	sorted_job = sorted(job, key=lambda x: x[2], reverse= True)
	print sorted_job
	timer = 1
	slot = [None]*(len(sorted_job)-1)
	for i in range(len(sorted_job)):					# O(n)
		if slot[sorted_job[i][1]-1] is not None:
			j = sorted_job[i][1]-1
			while j>=0:    										# O(n^2)    
				if slot[j] is None: 
					slot[j] = sorted_job[i][0]
					break
				j -= 1
		else:
			slot[sorted_job[i][1]-1] = sorted_job[i][0]
	return filter(lambda v: v is not None, slot)				# O(n)

print JobSeqencing([['a',2,100],['b',1,19],['c',2,27],['d',1,25],['e',3,15]])

#JobSeqencing([['a',4,20],['b',1,10],['c',1,40],['d',1,30]])


