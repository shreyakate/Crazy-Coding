def powerOf10(n):
	num= str(n)
	zero = num.count('0')
	one = num.count('1')
	other = len(num)-zero -one
	if other==0 and one == 1 and  zero%2 ==0 :
		return True
	return False

print powerOf10(10000)
