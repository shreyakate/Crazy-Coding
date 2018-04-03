def StringOcuurencs(s,t):
	i, ls, lt= 0, len(s),len(t)
	count = 0
	while i<ls-lt+1:
		if s[i:i+lt] == t:
			i += lt
			count += 1
		i += 1
	return count

print StringOcuurencs('Helhelloloworldhelloeuydghello', 'hello')
