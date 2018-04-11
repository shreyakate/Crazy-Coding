def MultiplyStrings(num1,num2):
	n1, n2= len(num1), len(num2)
	n3 = n1+n2
	l1 = [int(ch) for ch in reversed(num1)]
	l2 = [int(ch) for ch in reversed(num2)]
	l3 = [0] * n3

	for i in range(n1):
		for j in range(n2):
			l3[i+j] += l1[i] * l2[j]

	for i in range(n3-1):
		l3[i+1] += l3[i]/10
		l3[i] = l3[i]%10

	return ''.join([str(i) for i in reversed(l3)]).strip('0')



print MultiplyStrings("123","456")
