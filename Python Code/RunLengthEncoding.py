def RunLengthEncoding(code):
	ch = code[0]
	count = 1
	i = 1
	res = ''
	while i <len(code):
		if ch == code[i]:
			count += 1
		else:
			res += ch + str(count)
			count = 1
			ch = code[i]
		i += 1
	
	res += ch + str(count) 
	return res

print RunLengthEncoding('aaabcc')

