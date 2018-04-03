def substringsSizeK(s,k):
	res = []
	for i in range(len(s)-k+1):
		if s[i:i+k] not in res:
			res.append(s[i:i+k])
	res.sort()
	return res
	
print substringsSizeK("caaab",2)
