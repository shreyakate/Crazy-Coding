def getMaxOccurringChar(str):
	count = [0] * 256
	max = -1
	c =''
	for ch in str:
		count[ord(ch)] += 1
		if count[ord(ch)] > max:
			max = count[ord(ch)]
			c = ch
	return c

print getMaxOccurringChar("3w4edrasdfghjklsdfghjsdfghjksdfghj5ftygbhjenriou8y7t6wf5dq4sezxadfcsghxbhyude8")