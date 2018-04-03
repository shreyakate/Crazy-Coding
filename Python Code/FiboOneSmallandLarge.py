def FiboOneSmallandLarge(n):
	a = b =1 
	x = a+b
	while x < n:
		x = a + b 
		a = b
		b = x 
	return [a,b]

print FiboOneSmallandLarge(42)

