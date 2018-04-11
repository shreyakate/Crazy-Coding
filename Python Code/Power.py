def Power(x,n):
	if not n :
		return 1
	if n < 0:
		return 1/Power(x,-n)
	if n%2 :
		return x * Power(x, n-1)
	return Power(x*x,n/2)
print Power(2.10000, 3)
print Power(34.00515,-3)

def PowerIter(x,n):
	res = 1.0
	if not n : return res
	count = abs(n)
	if n<0:
		x = 1/x
		n = -n

	while count-1:
		if n%2:
			res *= x
			n -= 1
		else:
			res *= x*x
			n /= 2
		count -=1
	return res

print PowerIter(2.10000, 3)
print PowerIter(34.00515,-3)