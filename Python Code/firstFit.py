def firstFit(input, procSize):
	i = j = 0
	while i <len(procSize):
		j = 0
		alloc = False
		while j <len(input):
			if procSize[i]<=input[j]:
				print str(i+1) + "\t" + str(procSize[i]) + "\t" + str(j+1) 
				alloc = True
				input[j] -= procSize[i]
				#input.pop(j)       # I though we cannot re-use the input mem block 
				break
			j += 1

		if not alloc :
			print str(i+1) + "\t" + str(procSize[i]) + "\t Not Allocated"
		i += 1

firstFit([100,500,200,300,600],[212,200,290,426])