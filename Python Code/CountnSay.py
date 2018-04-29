def CountnSay(n):
	s = '1'
	for i in range(n-1):
		j = 1
		count = 1
		tmp = ''
		while j <len(s):
			if s[j-1] == s[j]:
				count += 1
				j += 1
				continue
			tmp += str(count)+s[j-1]
			count = 1
			j += 1
		tmp += str(count) + s[j-1]
		s = tmp
	return s

print CountnSay(34)

			


