def BestFit(input, procSize):
	alloc = [-1]*(len(procSize))

	for i in range(len(procSize)):
		diff = 3456789
		for j in range(len(input)):
			if input[j]> procSize[i] and (input[j]-procSize[i])< diff:
				alloc[i] = j
				diff = input[j]-procSize[i]

		if alloc[i]>-1:
			input[alloc[i]] = 0
	for i in range(len(alloc)):
		if alloc[i] == -1 :
			print str(i+1) + "\t" + str(procSize[i]) + "\t Not Allocated"
		else:
			print str(i+1) + "\t" + str(procSize[i]) + "\t" + str(alloc[i]+1)

BestFit([100,500,200,300,600],[212,417,100,426])
