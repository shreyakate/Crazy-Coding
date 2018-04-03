def getMaxOccurringChar(str):
	count = [0] * 256
	max = -1
	c =''
	for ch in str:
		count[ord(ch)] += 1
	for i in str:
		if max < count[ord(i)]:
			max = count[ord(i)]
			c = i
	return c

print getMaxOccurringChar("3w4edr5ftygbhjenriou8y7t6wf5dq4sezxadfcsghxbhyude8")