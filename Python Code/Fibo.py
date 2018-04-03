def RecFibo(n):
	if n < 1 : return
	if n == 1: return 1
	if n == 2: return 1

	return RecFibo(n-1) + RecFibo(n-2)\

def IterFibo(n):
	if n < 1 : return
	if n == 1: return 1
	if n == 2: return 1
	else:
		a = b = 1
		for i in range(n-2):
			c = a + b
			a = b
			b = c
		return c

def printFibo(n):
	for i in range(n+1):

		print i ,RecFibo(i), IterFibo(i)


printFibo(6)