def atoi(s):
	i , num = 0, 0
	sign = 1
	#while there is white space..ignore it
	while i<len(s) and s[i]==' ': i += 1
	#ignore the '+' sign in front of the number
	if s[i] == '+':  i += 1
	#mark teh '-ve' sign fo rreturn the results later accordingly
	if s[i] == '-':  
		sign = -1
		i += 1
	# ignore all the preceding 0's
	if s[i]== '0':
		while i<len(s) and s[i] =='0': i += 1
	if '1' <= s[i]<= '9':
		while i<len(s) and '0' <= s[i]<= '9': 
			num = num * 10 + ord(s[i]) - ord('0')
			i += 1

	return num * sign


print atoi("     -0000015374")