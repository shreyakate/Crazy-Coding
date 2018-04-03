def uniqueSubStringK(s,k):
	res =[]
	for i in range(len(s)-k):
		if s[i:i+k] in s[:i] or s[i:i+k] in s[i+k:]:
			continue
		else:
			res.append(s[i:i+k])
	return res

print uniqueSubStringK("geeksforgeeks", 2)

